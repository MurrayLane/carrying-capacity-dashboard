#!/usr/bin/env python3
"""B137 item 2: the production-to-consumption balance of pasture-fed food against the model's short-term capacity over population, 2025 and 2011.
Usage (repository root): python3 -I analysis/paper_a/meat_balance_identity.py [FAO_DIR]      (default /tmp/claude-0/fao, which holds the extracted FAOSTAT bulk files kept by hash in qa/fao_bulk_hashes.csv)
Reads  FAO_DIR/q/Production_Crops_Livestock_E_All_Data_(Normalized).csv and FAO_DIR/x/FoodBalanceSheets_E_All_Data_(Normalized).csv (sha256 of both checked against qa/fao_bulk_hashes.csv; no network)
       results/2025-fixed.csv, results/2011-fixed-3.csv
Writes analysis/paper_a/meat_balance_identity.csv
Windows: 2021-23 for 2025 (as analysis/method_tests_2025/foran_poldy_balance.py) and 2010-12 for 2011 (the new food balance series starts in 2010; 2011 is the middle year).
Identity: if all the production of a food stayed at home and people ate as they do now, the people it would feed = production / (food eaten per person) = ratio x FAO population.
Rows: meat total on FAOSTAT production (QCL; reproduces R04b's 4.66 Mt, 2.96 Mt, 1.57), meat total on food-balance production, red meat (beef, mutton and goat), and milk excluding butter. Only the first row is the identity of the brief; the others show which food binds.
Checks (stop on failure): the 2021-23 meat row reproduces 4.66 Mt, 2.96 Mt and a ratio of 1.57 (R04b); the model column equals capacity over population in results/*.csv."""
import csv, hashlib, os, statistics, sys
FAO = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/fao'
Q = f'{FAO}/q/Production_Crops_Livestock_E_All_Data_(Normalized).csv'; X = f'{FAO}/x/FoodBalanceSheets_E_All_Data_(Normalized).csv'
hashes = {r['file']: r['sha256_csv'] for r in csv.DictReader(open('qa/fao_bulk_hashes.csv'))}
for f, k in ((Q, 'Production_Crops_Livestock_E_All_Data_(Normalized).zip'), (X, 'FoodBalanceSheets_E_All_Data_(Normalized).zip')):
    h = hashlib.sha256(); fh = open(f, 'rb')
    for b in iter(lambda: fh.read(1 << 24), b''): h.update(b)
    if h.hexdigest() != hashes[k]: sys.exit(f'CHECK FAILED: sha256 of {f} does not match qa/fao_bulk_hashes.csv')
YEARS = {'2025': ('2021', '2022', '2023'), '2011': ('2010', '2011', '2012')}
allyears = {y for ys in YEARS.values() for y in ys}
qcl, fbs = {}, {}
for r in csv.DictReader(open(Q, encoding='utf-8-sig')):
    if r['Area'] == 'Australia' and r['Item'] == 'Meat, Total' and r['Element'] == 'Production' and r['Year'] in allyears: qcl[r['Year']] = float(r['Value']) / 1e6          # Mt
for r in csv.DictReader(open(X, encoding='utf-8-sig')):
    if r['Area'] == 'Australia' and r['Year'] in allyears and r['Item'] in ('Meat', 'Bovine Meat', 'Mutton & Goat Meat', 'Milk - Excluding Butter', 'Population') and r['Element'] in ('Production', 'Food', 'Total Population - Both sexes'):
        fbs[(r['Item'], r['Element'], r['Year'])] = float(r['Value'])                                                                                                          # 1000 t; population 1000
mean = lambda f, ys: statistics.mean(f(y) for y in ys)
res = {rel: {(r['zone'], r['preset']): r for r in csv.DictReader(open(f'results/{rel}.csv'))} for rel in ('2025-fixed', '2011-fixed-3')}
MODEL = {'2025': '2025-fixed', '2011': '2011-fixed-3'}
CAUSE = {'2025': 'probable causes, not split: the model adds 12% waste to the diet and feeds milk and wool from the same land, which lowers it below the ratio, while the meat total includes grain-fed pork and poultry that cropland, not pasture, limits',
         '2011': 'the two agree within 2%; the probable causes are those of 2025 and are not split'}
out = [['window', 'model_year', 'item', 'production_Mt', 'consumption_Mt', 'ratio_production_over_consumption', 'fao_population_million', 'people_fed_if_all_stayed_home_million', 'model_release', 'model_population_million', 'model_short_capacity_million', 'model_capacity_over_population', 'ratio_minus_model', 'gap_and_cause']]
rows = {}
for my, ys in YEARS.items():
    pop = mean(lambda y: fbs[('Population', 'Total Population - Both sexes', y)], ys) / 1000
    mr = res[MODEL[my]][('1', 'short')]; cap = int(mr['capacity']) / 1e6; mp = int(mr['population']) / 1e6; mratio = float(mr['capacity_per_person'])
    assert abs(cap / mp - mratio) < 5e-4
    items = [('meat total, FAOSTAT production (QCL) over food-balance food', mean(lambda y: qcl[y], ys), mean(lambda y: fbs[('Meat', 'Food', y)], ys) / 1000),
             ('meat total, food-balance production over food', mean(lambda y: fbs[('Meat', 'Production', y)], ys) / 1000, mean(lambda y: fbs[('Meat', 'Food', y)], ys) / 1000),
             ('red meat (beef and veal, mutton and goat), production over food', mean(lambda y: fbs[('Bovine Meat', 'Production', y)] + fbs[('Mutton & Goat Meat', 'Production', y)], ys) / 1000, mean(lambda y: fbs[('Bovine Meat', 'Food', y)] + fbs[('Mutton & Goat Meat', 'Food', y)], ys) / 1000),
             ('milk excluding butter, production over food', mean(lambda y: fbs[('Milk - Excluding Butter', 'Production', y)], ys) / 1000, mean(lambda y: fbs[('Milk - Excluding Butter', 'Food', y)], ys) / 1000)]
    for k, (name, p, c) in enumerate(items):
        ratio = p / c; rows[(my, k)] = (p, c, ratio)
        tail = (CAUSE[my] if k < 2 else 'red meat is produced at about 2.5 to 3 times what is eaten, so it does not bind alone' if k == 2
                else 'milk is the nearest single food in 2025 and well above the model in 2010-12; the model binds on all pasture-fed food together')
        gap = f'{ratio - mratio:+.2f} ({100 * (ratio / mratio - 1):+.1f}%): ' + tail
        out.append([f'{ys[0]}-{ys[-1][-2:]}', my, name, f'{p:.3f}', f'{c:.3f}', f'{ratio:.3f}', f'{pop:.3f}', f'{ratio * pop:.2f}', MODEL[my], f'{mp:.3f}', f'{cap:.3f}', f'{mratio:.4f}', f'{ratio - mratio:+.3f}', gap])
p, c, ratio = rows[('2025', 0)]
if not (round(p, 2) == 4.66 and round(c, 2) == 2.96 and round(ratio, 2) == 1.57): sys.exit(f'CHECK FAILED: 2021-23 meat row {p:.3f} {c:.3f} {ratio:.3f} does not reproduce R04b (4.66, 2.96, 1.57)')
csv.writer(open('analysis/paper_a/meat_balance_identity.csv', 'w', newline='')).writerows(out)
for r in out: print(r[:13])
print('checks passed')
