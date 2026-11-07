#!/usr/bin/env python3
"""What moves the number (Paper B, section 6, figure 3): each design choice measured with the model on the same data (Australia, 2025, corrected method unless stated).
Usage (repository root): python3 -I analysis/method_tests_2025/design_choices.py   (reads analysis/comparators_2025/rerun.csv and diet_land.csv and energy_exports.csv, results/scale_curve.csv,
results/<release>.csv (2011-thesis among them, to check the ladder's first step), analysis/sensitivity_2025/monte_carlo_2025-fixed_all_summary.csv and published_values.csv (the ladder's two
published endpoints, 9.4 and 100); writes design_choices.csv and ladder.csv)"""
import csv, collections
def table(path): return list(csv.reader(open(path)))
R = collections.defaultdict(dict)                                                  # release -> variant -> setting -> capacity (million)
for row in table('analysis/comparators_2025/rerun.csv')[1:]:
    R[row[0]].setdefault(','.join(row[1:-2]).split(' (')[0], {})[row[-2]] = float(row[-1])
drought = R['2025-fixed']['R1 drought allowance']; waste = R['2025-fixed']['R3 no avoidable waste']; crop2 = R['2025-fixed']['R2 cropland doubled']
drought_i = R['2025-improved']['R1 drought allowance']; waste_i = R['2025-improved']['R3 no avoidable waste']
def res(rel, preset):
    r = next(r for r in csv.DictReader(open(f'results/{rel}.csv')) if r['zone'] == '1' and r['preset'] == preset); return float(r['capacity']) / 1e6
fixed_s, fixed_l, imp_s, imp_l = res('2025-fixed', 'short'), res('2025-fixed', 'long'), res('2025-improved', 'short'), res('2025-improved', 'long')
sc = [r for r in csv.DictReader(open('results/scale_curve.csv')) if r['release'] == '2025-fixed' and r['preset'] == 'short' and r['yield_basis'] == 'state']
share = {r['level']: float(r['share_of_national']) for r in sc}
diets = {r[0]: float(r[1]) for r in table('analysis/comparators_2025/diet_land.csv')[1:]}
EX_ALL = 'all foods (adds meat, dairy, oils, fruit, vegetables, cottonseed, other sweeteners, tree nuts, wine, offals, fish)'
ex = {(r[0], r[1]): r[5] for r in table('analysis/comparators_2025/energy_exports.csv')[1:]}
ex_bal, ex_trd, ex_mid = float(ex[(EX_ALL, 'FAO balance energy')]), float(ex[(EX_ALL, 'as-traded densities')]), float(ex[('all foods: midpoint of the span', 'midpoint')])
PUB = {(r['table'], r['row']): float(r['value']) for r in csv.DictReader(open('analysis/method_tests_2025/published_values.csv'))}
thesis_long, csiro_uq = PUB[('ladder', 'thesis long-term figure as built (2011 data error kept)')], PUB[('ladder', 'exports counted as a proportion (CSIRO and UQ 2025)')]
assert round(res('2011-thesis', 'long'), 1) == thesis_long, 'the published 9.4 no longer matches results/2011-thesis.csv'

mc = next(r for r in csv.DictReader(open('analysis/sensitivity_2025/monte_carlo_2025-fixed_all_summary.csv')) if r['zone'] == '1' and r['setting'] == 'short')
mcl = next(r for r in csv.DictReader(open('analysis/sensitivity_2025/monte_carlo_2025-fixed_all_summary.csv')) if r['zone'] == '1' and r['setting'] == 'long')
p5, p95 = float(mc['p5']) / 1e6, float(mc['p95']) / 1e6
dl = diets["Guideline diet, 15% meat and eggs"], diets["Guideline diet, 5% meat and eggs"]
rows = [['design choice', 'what is compared', 'capacity low (million)', 'capacity high (million)', 'high over low', 'method and release', 'source']]
def add(c, w, lo, hi, m, s): rows.append([c, w, round(lo, 1), round(hi, 1), round(hi / lo, 2), m, s])
add('Drought allowance', 'average year; worst year of 5, 10, 20, 50, 100', drought['100'], drought['1'], 'corrected', 'rerun.csv R1')
add('Avoidable waste', '12% (default) against none', drought['1'], waste['average year'], 'corrected', 'rerun.csv R3')
add('Avoidable waste', '12% against none', imp_s, waste_i['average year'], 'improved', 'rerun.csv R3')
add('Land available', 'cropland as it is against doubled out of non-agricultural land', drought['1'], crop2['average year'], 'corrected', 'rerun.csv R2')
add('Unit of self-sufficiency', 'nation; sum over states, NRM regions, SA4, SA3, SA2 (state yield basis)', share['SA2'] * fixed_s, fixed_s, 'corrected', 'scale_curve.csv: shares ' + ', '.join(f'{k} {v:.0%}' for k, v in share.items() if k in ('State', 'NRM region', 'SA4', 'SA3', 'SA2')))
add('Diet', 'guideline diets from 15% to 5% meat and eggs', dl[0], dl[1], 'improved', 'diet_land.csv')
add('Diet (optimised)', 'default diet against nutrition-optimised diet C (ten micronutrients)', diets["The model's default diet (12% meat and eggs, 57.8% red)"], diets['Optimised C: free choice'], 'improved', 'diet_land.csv')
add('Australian settings', 'thesis method corrected against improved', fixed_s, imp_s, 'short term', 'results/<release>.csv')
add('Time frame', 'long-term settings against short-term settings', fixed_l, fixed_s, 'corrected', 'results/2025-fixed.csv')
add('Exports counted', 'the model against the CSIRO and UQ proportional count (27 at home + 63 abroad)', fixed_s, csiro_uq, 'published count', 'published_values.csv (comparators_2025/README.md)')
add('Exports counted (energy)', "the model against exports alone as an energy count, all foods, at FAO's own food energy per kg", fixed_s, ex_bal, 'energy count', 'energy_exports.csv, FAO balance energy')
add('Exports counted (energy)', 'the model against exports alone as an energy count, all foods, at typed as-traded densities', fixed_s, ex_trd, 'energy count', 'energy_exports.csv, as-traded densities')
add('Uncertainty (Monte Carlo)', '5th to 95th percentile over 13 uncertain choices', p5, p95, 'corrected', 'monte_carlo_2025-fixed_all_summary.csv')
csv.writer(open('analysis/method_tests_2025/design_choices.csv', 'w', newline='')).writerows(rows)
drivers = sorted(((k.replace('influence_', ''), float(v)) for k, v in mc.items() if k.startswith('influence_')), key=lambda kv: -kv[1])[:3]
driversl = sorted(((k.replace('influence_', ''), float(v)) for k, v in mcl.items() if k.startswith('influence_')), key=lambda kv: -kv[1])[:3]
ladder = [['step', 'million people', 'definition'],
          ['thesis long-term figure as built (2011 data, error kept)', thesis_long, 'long-term settings'],
          ['long term, corrected (2025)', round(fixed_l, 1), 'low-meat, organic, no avoidable waste, 100-year allowance, 30% reserve'],
          ['worst of 100 years, short-term diet', round(drought['100'], 1), 'weather allowance only'],
          ['worst of 10 years (Jones: 30 to 35)', round(drought['10'], 1), 'weather allowance'],
          ['average year', round(fixed_s, 1), 'today\'s diet and settings'],
          ['average year, improved settings', round(imp_s, 1), 'Australian settings'],
          ['average year, no avoidable waste', round(waste['average year'], 1), 'no waste'],
          ['average year, improved, no avoidable waste', round(waste_i['average year'], 1), 'both'],
          ['exports counted as a proportion (CSIRO and UQ 2025)', csiro_uq, 'domestic plus exported share'],
          ['energy count of exports alone, all foods', ex_mid, 'calories of exports: midpoint of %.1f (FAO balance energy) and %.1f (as-traded densities)' % (ex_bal, ex_trd)]]
csv.writer(open('analysis/method_tests_2025/ladder.csv', 'w', newline='')).writerows(ladder)
for r in rows: print(r)
print(); [print(r) for r in ladder]
print('MC drivers short:', drivers, ' long:', driversl)
