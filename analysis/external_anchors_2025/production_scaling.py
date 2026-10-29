#!/usr/bin/env python3
"""SCOPE.md E12, the external anchor: what could Australia's present production support if all of it stayed at home and people ate as they do now?
Usage: python3 -I analysis/external_anchors_2025/production_scaling.py FBS_CSV OUT.csv          (repository root; FBS_CSV as for consumption_2025/make_red_meat_mix.py)
For each food group of the FAO food balance sheet for Australia (mean 2021-23): production divided by the quantity eaten as food, times the population = the people the production would feed at today's consumption of that group.
This is a production check, not a land check: it ignores imports of the same food and the land the production uses. The binding groups (milk, fruit) are the ones a model of land must also be bound by."""
import csv, sys
src, out = sys.argv[1:3]
rows = [r for r in csv.DictReader(open(src, encoding='latin-1')) if r['Area'] == 'Australia']
Y = ('Y2021', 'Y2022', 'Y2023'); mean = lambda item, el: sum(float(next((r[y] for r in rows if r['Item'] == item and r['Element'] == el), 0) or 0) for y in Y) / 3
pop = mean('Grand Total', 'Total Population - Both sexes') if False else sum(float(next(r[y] for r in rows if r['Element'].startswith('Total Population'))) for y in Y) / 3 * 1000
GROUPS = [('Cereals', 'Cereals - Excluding Beer'), ('Beef and veal', 'Bovine Meat'), ('Mutton and goat', 'Mutton & Goat Meat'), ('Pork', 'Pigmeat'), ('Poultry', 'Poultry Meat'), ('Milk (excluding butter)', 'Milk - Excluding Butter'),
          ('Eggs', 'Eggs'), ('Fruit', 'Fruits - Excluding Wine'), ('Vegetables', 'Vegetables'), ('Starchy roots', 'Starchy Roots'), ('Pulses', 'Pulses'), ('Sugar (raw equivalent)', 'Sugar (Raw Equivalent)'), ('Vegetable oils', 'Vegetable Oils')]
res = [['group', 'production_kt', 'food_kt', 'exports_kt', 'imports_kt', 'production_over_food', 'people_fed_million_if_all_stayed']]
for name, item in GROUPS:
    p, f, e, i = (mean(item, el) for el in ('Production', 'Food', 'Export quantity', 'Import quantity'))
    res.append([name, round(p), round(f), round(e), round(i), round(p / f, 2) if f else '', round(p / f * pop / 1e6, 1) if f else ''])
csv.writer(open(out, 'w', newline='')).writerows(res)
print('population', round(pop / 1e6, 1), 'million'); [print(r) for r in res]
