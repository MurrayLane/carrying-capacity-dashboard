#!/usr/bin/env python3
"""Turn the downloaded ABS NRM cubes into cubes in the layout the yield pipeline reads (pipeline/yields/yields.py).

Usage: python3 -I build_cubes.py CUBE_DIR OUT_DIR      (CUBE_DIR from fetch_abs_current.py)

Writes OUT_DIR/regions.json and OUT_DIR/cube_<year>.json for 2016-17 to 2020-21. A cube is
  {"year", "rows": {"Wheat (ha)": [...], "Wheat (t)": [...], "Oranges trees (n)": [...]}, "unreliable": [["Wheat (ha)", col], ...]}
with one value per region (column 0 unused, as in the archive cubes; column 1 is Australia) and None where the ABS has no figure.
Units are the model's: hectares, tonnes. `unreliable` lists the cells the ABS marks as "too unreliable for general use" (relative standard
error above 50%, symbol **). The ABS gives no such flags for 2020-21, whose NRM figures are area-apportioned from SA2 with suppressed
cells set to zero; for that year a cell is listed when its area is under 10 ha or its tonnes are under 10 (the thesis's stated minimum).
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from abs_cube import read_cube
HERE = os.path.dirname(os.path.abspath(__file__))
YEARS = ('2016-17', '2017-18', '2018-19', '2019-20', '2020-21')
MIN_HA, MIN_T = 10.0, 10.0
cube_dir, out = sys.argv[1:3]; os.makedirs(out, exist_ok=True)
cmap = json.load(open(os.path.join(HERE, 'commodity_map.json')))['crops']
data = {y: read_cube(cube_dir, y) for y in YEARS}
codes0 = set(data[YEARS[0]][0])
assert all(set(data[y][0]) == codes0 for y in YEARS), 'the five years must share one set of regions'
ref = data['2020-21'][0]
region_codes = sorted(ref, key=lambda c: (c >= 100, c))                     # Australia, the states and territories, then the NRM regions
regions = [{'column': i + 1, 'code': c, 'label': ref[c]['label'], 'kind': 'nation' if c == 0 else 'state' if c < 100 else 'nrm'} for i, c in enumerate(region_codes)]
json.dump({'source': 'ABS Agricultural Commodities NRM tables, NRM regions (2016 edition)', 'regions': regions}, open(os.path.join(out, 'regions.json'), 'w'), indent=1)

def first(items, candidates):
    """The first candidate code the ABS published in this cube, with its factor."""
    for c in candidates:
        if c['code'] in items: return c
    return None

report = {}
for y in YEARS:
    cube, desc = data[y]; rows = {}; unreliable = []
    for crop in cmap:
        if crop['status'] == 'absent': continue
        name = crop['crop']
        for key, label, cands in (('area', f'{name} (ha)', crop['area']), ('trees', f'{name} trees (n)', crop['trees']), ('tonnes', f'{name} (t)', crop['tonnes'])):
            if not cands: continue
            avail = [c for c in cands if c['code'] in desc]
            if not avail: continue
            vals = [None] * (len(regions) + 1)
            for r in regions:
                items = cube[r['code']]['items']; c = first(items, avail)
                if c is None: continue
                est, flag, _ = items[c['code']]
                if est is None: continue
                vals[r['column']] = est * c['factor']
                if flag == '**': unreliable.append([label, r['column']])
            rows[label] = vals
    if y == '2020-21':
        # no reliability symbols exist for 2020-21, so the thesis's stated minimum (10 ha and 10 t, section 8.1 step 8) is applied to it instead
        for crop in cmap:
            n = crop['crop']; a, t = rows.get(f'{n} (ha)'), rows.get(f'{n} (t)'); tr = rows.get(f'{n} trees (n)')
            if not t or not (a or tr): continue
            for col in range(1, len(regions) + 1):
                small_area = a is not None and a[col] is not None and a[col] < MIN_HA
                if small_area or (t[col] is not None and t[col] < MIN_T):
                    for lab in (f'{n} (ha)', f'{n} trees (n)', f'{n} (t)'):
                        if lab in rows and [lab, col] not in unreliable: unreliable.append([lab, col])
    json.dump({'year': y, 'rows': rows, 'unreliable': unreliable}, open(os.path.join(out, f'cube_{y}.json'), 'w'))
    report[y] = len(rows)
print('rows per year', report)
