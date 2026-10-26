"""Parse the archived ABS NRM cubes (2006-07 to 2009-10) into area and production per region, crop and year."""
import re, glob, os, xlrd, collections

XLS = os.environ.get('ABS_XLS_DIR')
STATES = [('new south wales', 'NSW'), ('victoria', 'VIC'), ('queensland', 'QLD'), ('south australia', 'SA'),
          ('western australia', 'WA'), ('tasmania', 'TAS'), ('northern territory', 'NT'), ('australian capital', 'ACT')]
def norm(s):
    s = str(s).lower().replace('–', '-').replace('—', '-')
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()

# crop -> (regex for area label, regex for production label), all on lower-case labels
CROPS = {
    'Wheat':   (r'wheat for grain.*area \(ha\)', r'wheat for grain.*production \(t\)'),
    'Oats':    (r'oats for grain.*area \(ha\)', r'oats for grain.*production \(t\)'),
    'Barley':  (r'barley for grain.*area \(ha\)', r'barley for grain.*production \(t\)'),
    'Sorghum': (r'sorghum for grain.*area \(ha\)', r'sorghum for grain.*production \(t\)'),
    'Rice':    (r'rice for grain.*area \(ha\)', r'rice for grain.*production \(t\)'),
    'Canola':  (r'canola.*area \(ha\)', r'canola.*production \(t\)'),
    'Sugar cane': (r'sugar cane.*cut for crushing.*area \(ha\)', r'sugar cane.*cut for crushing.*production \(t\)'),
    'Maize':   (r'maize for grain.*area \(ha\)', r'maize for grain.*production \(t\)'),
    'Potatoes': (r'human consumption - potatoes - (processing and fresh market - total )?area \(ha\)$', r'human consumption - potatoes - (processing and fresh market - total )?production \(t\)$'),
}
EXCLUDE = re.compile(r'^\b$')   # nothing excluded: the label patterns are specific

def state_of_title(t):
    t = t.lower()
    for k, v in STATES:
        if k in t: return v
    return None

def parse_sheet(ws, est_offset):
    """Return {(region, label): value}; est_offset is the column offset of the estimate from the region-name column."""
    regions = [(c, str(ws.cell_value(4, c)).strip()) for c in range(1, ws.ncols) if str(ws.cell_value(4, c)).strip()]
    out = {}
    for r in range(6, ws.nrows):
        label = str(ws.cell_value(r, 0)).strip()
        if not label: continue
        for c, name in regions:
            v = ws.cell_value(r, c + est_offset)
            if isinstance(v, float): out[(name, label.lower())] = v
    return out

def collect():
    """data[year][(state, region_name)][crop] = [area, production]"""
    data = collections.defaultdict(lambda: collections.defaultdict(dict))
    files = {'2009-10': ['2009-10_NRM_all.xls'], '2008-09': ['2008-09_NRM_all.xls'], '2007-08': ['2007-08_NRM_all.xls'],
             '2006-07': [os.path.basename(p) for p in sorted(glob.glob(os.path.join(XLS, '2006-07_*.xls')))]}
    log = collections.Counter()
    for year, fns in files.items():
        for fn in fns:
            wb = xlrd.open_workbook(os.path.join(XLS, fn))
            for ws in wb.sheets():
                if ws.name == 'Contents': continue
                title = str(ws.cell_value(3, 0))
                st = state_of_title(title)
                off = 1 if year == '2006-07' else 0          # 2006-07 puts the business count first, estimate second
                if year == '2006-07':
                    st = {'NSW': 'NSW', 'VIC': 'VIC', 'QLD': 'QLD', 'SA': 'SA', 'WA': 'WA', 'TAS': 'TAS', 'NT_and_ACT': 'NT'}[fn.split('_', 1)[1].rsplit('.', 1)[0]] if fn.split('_', 1)[1].rsplit('.', 1)[0] in ('NSW','VIC','QLD','SA','WA','TAS','NT_and_ACT') else st
                if 'Australia' in title and year == '2008-09' and ws.name == 'Table_1': st = 'AUS'
                vals = parse_sheet(ws, off)
                for crop, (ra, rp) in CROPS.items():
                    ra_c, rp_c = re.compile(ra), re.compile(rp)
                    area_labels = sorted({l for (_, l) in vals if ra_c.search(l) and not EXCLUDE.search(l)}, key=len)
                    prod_labels = sorted({l for (_, l) in vals if rp_c.search(l) and not EXCLUDE.search(l)}, key=len)
                    if not area_labels or not prod_labels: continue
                    la, lp = area_labels[0], prod_labels[0]
                    for (name, l), v in vals.items():
                        if l != la: continue
                        pv = vals.get((name, lp))
                        if pv is None: continue
                        key = (st, name)
                        # NT and ACT share a sheet in some years: a region called ACT belongs to ACT
                        if re.fullmatch(r'act|australian capital territory', norm(name)): key = ('ACT', name)
                        data[year][key].setdefault(crop, [0.0, 0.0])
                        data[year][key][crop][0] += v; data[year][key][crop][1] += pv
                    log[(year, crop)] += 1
    return data, log

if __name__ == '__main__':
    data, log = collect()
    for y in sorted(data): print(y, 'regions', len(data[y]), 'sample', list(data[y].items())[:1])
    print({k: v for k, v in sorted(log.items())})
