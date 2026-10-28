#!/usr/bin/env python3
"""Food supply (kcal per person per day) of a country from the FAO food balance sheets, by FAO item, for the diet templates of SCOPE.md E16.
Usage: python3 -I analysis/diet_templates/fao_diet.py FBS_CSV "Papua New Guinea" OUT.csv      (FBS_CSV: FoodBalanceSheets_E_Oceania_NOFLAG.csv from https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_Oceania.zip; latest year in the file)
Writes the items with at least 10 kcal, the share of the grand total, and prints the groups that matter for a template."""
import csv, sys
src, country, out = sys.argv[1:4]
rows = [r for r in csv.DictReader(open(src, encoding='latin-1')) if r['Area'] == country and r['Element'].startswith('Food supply (kcal/capita/day)')]
year = [k for k in rows[0] if k.startswith('Y')][-1]; tot = next(float(r[year]) for r in rows if r['Item'] == 'Grand Total')
items = sorted(((r['Item'], float(r[year])) for r in rows if r[year] and float(r[year]) >= 10), key=lambda x: -x[1])
with open(out, 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['country', 'year', 'item', 'kcal_per_person_day', 'share_of_total'])
    for i, v in items: w.writerow([country, year[1:], i, round(v, 1), round(v / tot, 4)])
print(country, year[1:], 'grand total', tot, 'kcal;', len(items), 'items')
