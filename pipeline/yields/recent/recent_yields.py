#!/usr/bin/env python3
"""National and state yields of the two data windows against the model's 2006-2010 yields, and the group-trend factors.

Usage: python3 -I recent_yields.py          (run from the repository root; needs data/abs-2016-21 and data/abs-2022-25)

Stage 1 and 2 of the pipeline (yields.crop_year, the five-year mean) on the national and state columns of
  2021   data/abs-2016-21   five years, NRM tables, trees converted to hectares as in the thesis
  2025   data/abs-2022-25   three years, Data API, area in hectares
The model's seven zones with states (NSW and ACT together, as the thesis has them) are compared with the Yield sheet of model/model.xls after undoing its
zero-irrigation conversion (the default irrigation setting of each zone, data/2011). Writes data/abs-2022-25/national_state_yields.csv and
data/abs-2022-25/group_trend.json.
"""
import csv, json, os, statistics, sys
import xlrd
ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, 'pipeline', 'yields')); sys.path.insert(0, os.path.join(ROOT, 'pipeline', 'yields', 'recent'))
import yields
from average import five_year_average
from group_trend import factors, GROUPS

ZONES = {'Australia': (1, [1]), 'NSW and ACT': (2, [2, 9]), 'Victoria': (15, [3]), 'Queensland': (26, [4]), 'South Australia': (40, [5]), 'Western Australia': (49, [6]), 'Tasmania': (56, [7]), 'Northern Territory': (60, [8])}
WINDOWS = {'2021': ('data/abs-2016-21', ('2016-17', '2017-18', '2018-19', '2019-20', '2020-21')), '2025': ('data/abs-2022-25', ('2022-23', '2023-24', '2024-25'))}
crops = json.load(open(os.path.join(ROOT, 'pipeline/yields/abs_current/model_crops.json')))['crops']
groups = json.load(open(os.path.join(ROOT, 'pipeline/yields/recent/groups.json')))['groups']
ws = xlrd.open_workbook(os.path.join(ROOT, 'model/model.xls')).sheet_by_name('Yield')
irr = {int(r['regionId']): float(r['irrigation']) for r in csv.DictReader(open(os.path.join(ROOT, 'data/2011/default-inputs-short-term.csv')))}


def zone_cube(rows, unreliable):
    """Collapse the cube's columns to the eight zones: sums of area and tonnes, NSW with ACT."""
    out = {}; zone_cols = [cols for _, cols in ZONES.values()]
    for label, vals in rows.items():
        v = [None]
        for cols in zone_cols:
            xs = [vals[c] for c in cols if vals[c] is not None]
            v.append(sum(xs) if xs else None)
        out[yields.norm(label)] = v
    bad = {(yields.norm(l), i + 1) for i, cols in enumerate(zone_cols) for l, c in unreliable if c in cols}
    return out, bad


def window_yields(folder, years):
    per_year = {}
    for y in years:
        cube = json.load(open(os.path.join(ROOT, folder, f'cube_{y}.json')))
        zc, bad = zone_cube(cube['rows'], cube['unreliable'])
        for name in crops:
            out = yields.crop_year(zc, name, deleted=bad)
            if out is not None: per_year.setdefault(name, []).append(out)
    return {n: five_year_average(v) for n, v in per_year.items()}


new = {k: window_yields(*v) for k, v in WINDOWS.items()}
old = {}
for i, name in enumerate(crops):
    row = {}
    for j, (zone, (zid, _)) in enumerate(ZONES.items(), start=1):
        v = ws.cell_value(3 + i, 7 + zid - 1)
        row[j] = v / 100 * (1 + 0.55 * irr[zid]) if isinstance(v, float) and v > 0 else None        # t/ha, before the zero-irrigation conversion
    old[name] = row

rows = []
for name in crops:
    for j, zone in enumerate(ZONES, start=1):
        o, a, b = old[name].get(j), (new['2021'].get(name) or [None] * 9)[j], (new['2025'].get(name) or [None] * 9)[j]
        if o is None and a is None and b is None: continue
        rows.append([name, groups[name], zone, o, a, b])
with open(os.path.join(ROOT, 'data/abs-2022-25/national_state_yields.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['crop', 'group', 'zone', 'model_2006_10_t_ha', 'window_2016_21_t_ha', 'window_2022_25_t_ha'])
    for r in rows: w.writerow([r[0], r[1], r[2]] + [None if x is None else round(x, 4) for x in r[3:]])


def national_ratios(win):
    return {n: new[win][n][1] / old[n][1] for n in crops if n in new[win] and new[win][n][1] and old[n].get(1)}


r21, r25 = national_ratios('2021'), national_ratios('2025')
f21 = factors(r21, groups); f25 = factors(r25, groups, earlier={g: v['factor'] for g, v in f21.items()})
json.dump({'rule': 'SCOPE.md B10: median over the reported crops of a group of (national yield in the window / national yield 2006-2010); carried forward where the window reports none',
           '2021': f21, '2025': f25, 'ratios_2021': r21, 'ratios_2025': r25}, open(os.path.join(ROOT, 'data/abs-2022-25/group_trend.json'), 'w'), indent=1)

print('National yield, t/ha (model 2006-10 before the zero-irrigation conversion | 2016-21 | 2022-25)')
for n in crops:
    if n in r25 or (n in r21 and groups[n] == 'field crops'):
        fmt = lambda win: (lambda v: f'{v[1]:8.3f}' if v and v[1] else '       -')(new[win].get(n))
        print(f'  {n:14s} {old[n][1]:8.3f} | {fmt("2021")} | {fmt("2025")}')
for win, f in (('2016-21', f21), ('2022-25', f25)):
    print(f'\nGroup factors {win}')
    for g in GROUPS: print(f'  {g:12s} {f[g]["factor"]:.3f}  from {f[g]["crops"]} crops' + ('  (carried forward)' if f[g]['carried'] else ''))
