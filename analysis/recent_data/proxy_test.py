#!/usr/bin/env python3
"""How well would a group trend predict the yield of a crop the ABS no longer reports?

Usage: python3 -I proxy_test.py        (run from the repository root)

For each crop the ABS still reports, the national yield of 2016-17 to 2020-21 (the pipeline's stage 1, five-year mean) is divided by the model's
2006-2010 national yield (model/model.xls, Yield!H). The ratio is how much that crop's yield moved. For each group the script then predicts every
crop's ratio from the median of the others (leave one out) and compares the error with the error of keeping the old yield (a ratio of 1).
Groups are by method: vegetables (area scaled up), tree crops (trees per hectare), nuts, and field crops plus the remaining horticulture.
"""
import json, math, os, statistics as st, sys
import xlrd
ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, 'pipeline', 'yields'))
import yields
CC = os.path.join(ROOT, 'pipeline', 'yields', 'abs_current')
crops = json.load(open(os.path.join(CC, 'model_crops.json')))['crops']
cmap = {c['crop']: c for c in json.load(open(os.path.join(CC, 'commodity_map.json')))['crops']}
ws = xlrd.open_workbook(os.path.join(ROOT, 'model', 'model.xls')).sheet_by_name('Yield')
YEARS = ('2016-17', '2017-18', '2018-19', '2019-20', '2020-21')
cubes = {y: json.load(open(os.path.join(ROOT, 'data', 'abs-2016-21', f'cube_{y}.json')))['rows'] for y in YEARS}
NUTS = {'Almonds', 'Macadamias', 'Pecans', 'Walnuts', 'Cashews'}
res = {}
for i, name in enumerate(crops):
    old = ws.cell_value(3 + i, 7)
    if cmap[name]['status'] == 'absent' or not isinstance(old, float) or old <= 0: continue
    ys = []
    for y in YEARS:
        out = yields.crop_year({yields.norm(k): v for k, v in cubes[y].items()}, name)
        if out and out[1]: ys.append(out[1])
    if len(ys) < 3: continue
    new = sum(ys) / len(ys) * 100                                   # t/ha to g/m2
    veg = yields.ADJ.get(yields.norm(name + ' (ha)'), {}).get('areaIncrease') is not None
    tree = yields.ADJ.get(yields.norm(name + ' trees (n)'), {}).get('treesPerHa')
    res[name] = ('vegetables' if veg else 'nuts' if name in NUTS else 'tree fruit' if tree else 'field crops and other horticulture', new, old, new / old)
pct = lambda e: f'{100 * (math.exp(e) - 1):.0f}%'
for g in ('field crops and other horticulture', 'vegetables', 'tree fruit', 'nuts'):
    rows = [(n, v) for n, v in res.items() if v[0] == g]
    print(f'\n## {g}: {len(rows)} crops, median new/old {st.median(v[3] for _, v in rows):.2f}')
    for n, v in rows: print(f'  {n:34s} old {v[2]:8.1f}  new {v[1]:8.1f}  ratio {v[3]:5.2f}')
    if len(rows) >= 4:
        loo = sorted(abs(math.log(st.median(w[3] for m, w in rows if m != n) / v[3])) for n, v in rows)
        keep = sorted(abs(math.log(v[3])) for _, v in rows)
        print(f'  group-median proxy: median error {pct(st.median(loo))}, 80th percentile {pct(loo[int(.8 * len(loo))])}')
        print(f'  keep old yield:     median error {pct(st.median(keep))}, 80th percentile {pct(keep[int(.8 * len(keep))])}')
