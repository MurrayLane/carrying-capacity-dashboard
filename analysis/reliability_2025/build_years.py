#!/usr/bin/env python3
"""E10: the 2025 result year by year. Builds a yield matrix for each ABS crop year there is data for (2016-17 to 2020-21, 2022-23 to 2024-25) with that year's crops AND that year's herds and meat.

Usage: python3 -I analysis/reliability_2025/build_years.py WORK_DIR ABS_DIR          (from the repository root; ABS_DIR as for livestock_zone.py)
Writes WORK_DIR/<year>/yield_matrix_livestock.csv and WORK_DIR/years.json, which analysis/sensitivity_2025/evaluate.mjs reads.

For each year, as the 2025 matrix is made but with that year alone:
  crops          zone_yields.py with ZY_YEARS=<year>; for 2016-17 to 2020-21 from the 2016-21 cubes (ZY_SOURCE=2016-21: national and state zones only, which is all that is evaluated)
  group trend    the factors of the crops the ABS no longer reports, from THAT year's national yields of the reported crops (group_trend.factors, as for a window); 2022-23 onward carry the
                 2016-21 window factor for a group with fewer than three reported crops, as the window rule does
  animals        livestock_zone.py with LS_YEARS=<year> (herds and meat of that year; feed grain from that year's crop yields)
Land, population, diet and the other defaults are those of release 2025-organic.
"""
import json, os, subprocess, sys
import xlrd
ROOT = os.getcwd(); WORK, ABS = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]); PY = [sys.executable, '-I']
sys.path.insert(0, os.path.join(ROOT, 'pipeline', 'yields', 'recent'))
from group_trend import factors
YEARS_A = ['2016-17', '2017-18', '2018-19', '2019-20', '2020-21']; YEARS_B = ['2022-23', '2023-24', '2024-25']
crops = json.load(open(os.path.join(ROOT, 'pipeline/yields/abs_current/model_crops.json')))['crops']
groups = json.load(open(os.path.join(ROOT, 'pipeline/yields/recent/groups.json')))['groups']
trend = json.load(open(os.path.join(ROOT, 'data/abs-2022-25/group_trend.json')))
ws = xlrd.open_workbook(os.path.join(ROOT, 'model/model.xls')).sheet_by_name('Yield')
import csv
irr1 = {int(r['regionId']): float(r['irrigation']) for r in csv.DictReader(open(os.path.join(ROOT, 'data/2011/default-inputs-short-term.csv')))}[1]
old = {}
for i, c in enumerate(crops):
    v = ws.cell_value(3 + i, 7)
    if isinstance(v, float) and v > 0: old[c] = v / 100 * (1 + 0.55 * irr1)
def run(script, env, *args): subprocess.run(PY + [os.path.join(ROOT, 'pipeline/yields/recent', script), *args], env={**os.environ, **env}, check=True, stdout=subprocess.DEVNULL, cwd=ROOT)
spec = []; table = []
for y in YEARS_A + YEARS_B:
    d = os.path.join(WORK, y); os.makedirs(d, exist_ok=True); src = '2016-21' if y in YEARS_A else '2022-25'
    env = {'ZY_YEARS': y, 'ZY_SOURCE': src, 'ZY_OUT': d}
    run('zone_yields.py', env)                                                                    # first pass: this year's national yields
    nat = json.load(open(os.path.join(d, 'crop_yields_by_year.json')))['yields']
    ratios = {c: nat[c][y][1] / old[c] for c in crops if c in nat and y in nat[c] and nat[c][y][1] and c in old}
    earlier = None if y in YEARS_A else {g: v['factor'] for g, v in trend['2021'].items()}
    f = {g: v['factor'] for g, v in factors(ratios, groups, earlier).items()}
    run('zone_yields.py', {**env, 'ZY_FACTORS': json.dumps(f)})
    run('livestock_zone.py', {'LS_YEARS': y, 'ZY_OUT': d}, ABS)
    spec.append({'id': 'year_' + y, 'group': 'year', 'label': f'crops, herds and meat of {y} only', 'matrix': os.path.join(d, 'yield_matrix_livestock.csv')})
    table.append([y, src, {g: round(v, 3) for g, v in f.items()}, len(ratios)])
    print(y, src, 'reported crops', len(ratios), {g: round(v, 3) for g, v in f.items()})
json.dump(spec, open(os.path.join(WORK, 'years.json'), 'w'), indent=1)
json.dump({'note': 'group-trend factors used for each single year', 'years': table}, open(os.path.join(WORK, 'year_factors.json'), 'w'), indent=1)
