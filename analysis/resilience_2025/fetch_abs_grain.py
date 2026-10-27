#!/usr/bin/env python3
"""Wheat, oats and barley area and production for Australia and the states, from the ABS Agricultural Commodities (7121.0) archive cubes, to extend the thesis's 1861-2010 series.

Usage: python3 -I analysis/resilience_2025/fetch_abs_grain.py DIR YEAR [YEAR ...]       e.g. DIR 2010-11 2011-12 ... 2015-16   (run from the repository root)
Downloads the data cubes of each release into DIR (not committed), finds the one with the state sheets, and appends the rows to data/abs-history/grain_state.csv
(year, state, crop, area_ha, tonnes). The state rows are those whose region label is the state's own name (not an NRM region).
"""
import csv, os, re, subprocess, sys
import xlrd
ROOT = os.getcwd(); D = sys.argv[1]; YEARS = sys.argv[2:]; os.makedirs(D, exist_ok=True)
STATES = ['Australia', 'New South Wales', 'Victoria', 'Queensland', 'South Australia', 'Western Australia', 'Tasmania', 'Northern Territory']
CROPS = {'Wheat for grain': 'wheat', 'Oats for grain': 'oats', 'Barley for grain': 'barley'}
def get(u): return subprocess.run(['curl', '-s', '-m', '180', '-L', '-A', 'Mozilla/5.0', u], capture_output=True).stdout
out = os.path.join(ROOT, 'data/abs-history/grain_state.csv'); have = {}
if os.path.exists(out):
    for r in csv.DictReader(open(out)): have[(r['year'], r['state'], r['crop'])] = r
for y in YEARS:
    page = get(f'https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/7121.0{y}').decode('latin1')
    if 'openagent' not in page: page = get(f'https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/7121.0{y[:5]}20{y[5:]}').decode('latin1')      # the 2012-13 page is named 2012-2013
    found = False
    for href, name in re.findall(r'href="(/[^"]*openagent&([^&]*\.xls)&[^"]*)"', page, re.I):
        path = os.path.join(D, f'{y}_{name}')
        if not os.path.exists(path): open(path, 'wb').write(get('https://www.abs.gov.au' + href.replace(' ', '%20')))
        try: wb = xlrd.open_workbook(path)
        except Exception: continue
        rows = {}
        ABBR = {'Australia': 'Australia', 'NSW': 'New South Wales', 'Vic.': 'Victoria', 'Qld': 'Queensland', 'SA': 'South Australia', 'WA': 'Western Australia', 'Tas.': 'Tasmania', 'NT': 'Northern Territory'}
        for sh in wb.sheets():                                   # layout of 2010-11 to 2012-13: one sheet with the states as columns
            hdr = next((r for r in range(min(sh.nrows, 12)) if sh.ncols > 6 and str(sh.cell_value(r, 5)).strip() == 'Australia'), None)
            if hdr is None: continue
            cols = {c: ABBR[str(sh.cell_value(hdr, c)).strip()] for c in range(5, sh.ncols) if str(sh.cell_value(hdr, c)).strip() in ABBR}
            for r in range(hdr + 1, sh.nrows):
                row = sh.row_values(r)
                if str(row[3]).strip() in CROPS and re.match(r'(Area|Production)', str(row[4]).strip()):
                    for c, lab in cols.items():
                        if isinstance(row[c], float): rows.setdefault((lab, CROPS[str(row[3]).strip()]), {}).setdefault(str(row[4]).strip()[:4], row[c])
        for sh in wb.sheets():                                   # layout of 2011-12 and 2012-13: descriptions in column A, a (estimate, businesses) pair of columns per state
            hdr = next((r for r in range(min(sh.nrows, 12)) if sh.ncols > 6 and str(sh.cell_value(r, 3)).strip() == 'NSW'), None)
            if hdr is None: continue
            cols = {c: ('Australia' if str(sh.cell_value(hdr, c)).strip() == 'Total' else ABBR[str(sh.cell_value(hdr, c)).strip()]) for c in range(1, sh.ncols) if str(sh.cell_value(hdr, c)).strip() in ABBR or str(sh.cell_value(hdr, c)).strip() == 'Total'}
            for r in range(hdr + 1, sh.nrows):
                row = sh.row_values(r)
                m = re.match(r'Broadacre crops - (?:Cereal crops - )?(Wheat for grain|Oats for grain|Barley for grain) - (Area \(ha\)|Production \(t\))', str(row[0]))
                if m:
                    for c, lab in cols.items():
                        if isinstance(row[c], float): rows.setdefault((lab, CROPS[m.group(1)]), {}).setdefault(m.group(2)[:4], row[c])
        if 'NSW' not in wb.sheet_names() and not rows: continue
        for sh in wb.sheets():
            if sh.name == 'Contents': continue
            for r in range(sh.nrows):
                row = sh.row_values(r)
                if len(row) < 4: continue
                d, lab = str(row[2]), str(row[1]).strip()
                m = re.match(r'Broadacre crops - (?:Cereal crops - )?(Wheat for grain|Oats for grain|Barley for grain) - (Area \(ha\)|Production \(t\))', d)
                if m and lab in STATES: rows.setdefault((lab, CROPS[m.group(1)]), {}).setdefault(m.group(2)[:4], row[3])      # first occurrence: the state's own row, not an NRM region
        if rows:
            for (lab, crop), v in rows.items():
                if isinstance(v.get('Area'), float) and isinstance(v.get('Prod'), float): have[(y, lab, crop)] = {'year': y, 'state': lab, 'crop': crop, 'area_ha': v['Area'], 'tonnes': v['Prod']}
            found = True; print(y, 'from', name, len([k for k in have if k[0] == y]), 'rows'); break
    if not found: print(y, 'no state cube found')
with open(out, 'w', newline='') as f:
    w = csv.DictWriter(f, ['year', 'state', 'crop', 'area_ha', 'tonnes']); w.writeheader()
    for k in sorted(have): w.writerow(have[k])
