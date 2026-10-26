#!/usr/bin/env python3
"""Checks the commodity mapping.
1. Against yields the ABS publishes itself (t/ha items such as WHEAT_YIELD_F, 2016-17 to 2019-20): area and tonnes from the cube must give the same yield.
2. Against the 2005-10 national yields (archive, Aver-add): the five-year national yield of each mapped crop now, as a ratio of then.
Usage: CUBE_DIR=/path/to/cubes MODELS_DIR=/path/to/Models python3 -I verify_mapping.py      (CUBE_DIR from fetch_abs_current.py)"""
import json, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
from abs_cube import read_cube
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
YEARS = ('2016-17', '2017-18', '2018-19', '2019-20', '2020-21')
cubes = {y: json.load(open(os.path.join(REPO, 'data/abs-2016-21', f'cube_{y}.json'))) for y in YEARS}
regions = json.load(open(os.path.join(REPO, 'data/abs-2016-21/regions.json')))['regions']
col = {r['code']: r['column'] for r in regions}
ABS_YIELD = {'Wheat': 'WHEAT_YIELD_F', 'Oats': 'OATS_YIELD_F', 'Barley': 'BARLEY_YIELD_F', 'Sorghum': 'SORGHUM_YIELD_F', 'Maize': 'MAIZE_YIELD_F', 'Rice': 'RICE_YIELD_F',
             'Canola': 'CANOLA_YIELD_F', 'Triticale': 'TRITICALE_YIELD_F', 'Sugar cane': 'SUGARCUTCRUSHING_YIELD_F', 'Bananas': 'BANANAS_YIELD_F', 'Pineapples': 'PINEAPPLES_YIELD_F', 'Grape': 'GRAPESTOTAL_YIELD_F'}
raw = {y: read_cube(os.environ['CUBE_DIR'], y) for y in YEARS}
print('1. cube yield (tonnes / area) against the ABS published yield (t/ha)')
tot = collections.Counter(); worst = []
for crop, code in ABS_YIELD.items():
    n = ok = 0
    for y in YEARS:
        rows = cubes[y]['rows']; a, t = rows.get(f'{crop} (ha)'), rows.get(f'{crop} (t)')
        if not a or not t: continue
        for r in regions:
            ab = raw[y][0][r['code']]['items'].get(code)
            if not ab or ab[0] in (None, 0) or not a[r['column']] or not t[r['column']]: continue
            n += 1; mine = t[r['column']] / a[r['column']]; rel = abs(mine / ab[0] - 1)
            ok += rel < 0.01
            if rel >= 0.01: worst.append((rel, crop, y, r['label'], round(mine, 3), ab[0]))
    tot['compared'] += n; tot['within 1%'] += ok; print(f'   {crop:12s} {ok:4d} of {n:4d} within 1%')
print('   all', dict(tot)); print('   largest differences:', sorted(worst, reverse=True)[:5])

print('\n2. national five-year yield now against 2005-10 (model crops with data in both)')
import xlrd
old = xlrd.open_workbook(os.path.join(os.environ['MODELS_DIR'], 'Yield data', '5 NRM-all 5 years - average.xls')).sheet_by_name('Aver-add')
oldy = {str(old.cell_value(r, 0)).replace(' (t/ha)', '').strip(): old.cell_value(r, 1) for r in range(1, 92) if isinstance(old.cell_value(r, 1), float)}
cm = json.load(open(os.path.join(HERE, 'commodity_map.json')))['crops']
rows_out = []
for c in cm:
    if c['status'] == 'absent': continue
    ys = []
    for y in YEARS:
        rows = cubes[y]['rows']; t = rows.get(f"{c['crop']} (t)"); a = rows.get(f"{c['crop']} (ha)") or rows.get(f"{c['crop']} trees (n)")
        if t and a and t[1] and a[1]: ys.append(t[1] / a[1] * (1 if f"{c['crop']} (ha)" in rows else 1))
    if ys and c['crop'] in oldy and c['trees'] == []: rows_out.append((c['crop'], len(ys), sum(ys) / len(ys), oldy[c['crop']]))
print('   crop           years  now t/ha  2005-10  ratio')
for n, k, now, then in rows_out: print(f'   {n:14s} {k:3d} {now:9.2f} {then:8.2f} {now / then:6.2f}' + ('   <-- check' if not 0.6 <= now / then <= 1.6 else ''))
