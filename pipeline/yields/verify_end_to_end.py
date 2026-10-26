"""Rebuilds the model's Yield sheet from the raw archive cubes and compares it with model/model.xls.
raw cubes (file 1) -> stage 1 (crops, livestock) -> stage 2 (five-year average) -> stage 3 (fill, irrigation conversion) -> g/m2.
Rows 103 to 133 (berries, melons, grouped citrus, literature estimates) are taken from the archive as recorded data.
Usage: MODELS_DIR=/path/to/Models python3 -I verify_end_to_end.py   (run from the repository root)"""
import os, sys, re, json, csv, collections, xlrd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yields import read_cube, crop_year, norm
from livestock import livestock_year, PRODUCTS
from average import five_year_average
from fill import model_yield
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
D = os.path.join(os.environ['MODELS_DIR'], 'Yield data')
f1 = xlrd.open_workbook(os.path.join(D, '1 NRM-all 5 years - all t and ha.xls')); f5 = xlrd.open_workbook(os.path.join(D, '5 NRM-all 5 years - average.xls'))
DEL = json.load(open(os.path.join(HERE, 'archive_deletions.json'))); LS = json.load(open(os.path.join(HERE, 'archive_livestock_inputs.json')))['years']
derived = json.load(open(os.path.join(HERE, 'archive_derived_yields.json')))['rows']
model = xlrd.open_workbook(os.path.join(REPO, 'model/model.xls')).sheet_by_name('Yield')
irr = {int(r['regionId']): float(r['irrigation']) for r in csv.DictReader(open(os.path.join(REPO, 'data/2011/default-inputs-short-term.csv')))}
adjt0 = f5.sheet_by_name('2009-adjt'); labels = {r: str(adjt0.cell_value(r, 0)) for r in range(1, 103)}
bases = {r: re.sub(r'\s*\(t/ha\)\s*$', '', labels[r]).strip() for r in range(1, 92)}
per_year = {r: [] for r in range(1, 103)}
for y in (2006, 2007, 2008, 2009, 2010):
    cube = read_cube(f1.sheet_by_name(str(y)))
    m_all = {(l, c) for l, c in DEL['unreliable'][str(y)]}
    m_later = m_all | {(norm(b + s), c) for b, c in DEL['later'][str(y)] for s in (' (ha)', ' trees (n)', ' (t)', ' lint (t)')}
    for r in range(1, 92): per_year[r].append(crop_year(cube, bases[r], m_later))
    feedcrops = {b: crop_year(cube, b, m_all) for b in ('Wheat', 'Oats', 'Barley', 'Sorghum', 'Maize', 'Canola', 'Soybeans')}
    ls = livestock_year(LS[str(y)], feedcrops)
    for i, p in enumerate(PRODUCTS): per_year[92 + i].append(ls[p])
avg = {r: five_year_average(per_year[r]) for r in per_year}
for r, vals in derived.items(): avg[int(r)] = [None] + vals
FILL = {(int(r) - 2, z) for r, zs in json.load(open(os.path.join(HERE, 'archive_fill_mask.json')))['fillCells'].items() for z in zs}   # sheet row 3 is Aver row 1
out = model_yield(avg, irr, FILL)
c = collections.Counter(); bad = collections.defaultdict(int)
for r, vals in out.items():
    for z in range(1, 61):
        mv = model.cell_value(r + 2, 6 + z); mv = mv if isinstance(mv, float) and mv != 0 else None; g = vals[z]
        if g is None and mv is None: k = 'both empty'
        elif g is not None and mv is not None and abs(g - mv) <= 1e-7 * max(1, abs(mv)): k = 'match'
        else: k = 'differ'; bad[str(model.cell_value(r + 2, 0)).split('(')[0].strip()] += 1
        c[k] += 1
print(dict(c)); print('cells that differ, by commodity:', sorted(bad.items(), key=lambda x: -x[1])[:12])
