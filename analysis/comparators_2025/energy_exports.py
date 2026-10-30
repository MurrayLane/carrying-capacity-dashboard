#!/usr/bin/env python3
"""Export-inclusive 'people fed' counts (Bellotti 2017: exports feed 36.6 million; CSIRO and UQ 2025: about 100 million in all, 27 million Australians) reproduced as an energy balance, to show how much the count
depends on what is counted. Usage: python3 -I analysis/comparators_2025/energy_exports.py FBS_CSV OUT.csv          (repository root)
Exports of each commodity (FAO food balance sheet for Australia, mean 2021-23, thousand tonnes) times a food energy density (kcal/kg, standard values, stated below) over 2,100 kcal a person a day (about the
Australian average requirement of 8,800 kJ). Nothing is netted for imports and nothing for the feed or fuel use of the commodity abroad: that is the point of the exercise."""
import csv, sys
src, out = sys.argv[1:3]
rows = [r for r in csv.DictReader(open(src, encoding='latin-1')) if r['Area'] == 'Australia']
Y = ('Y2021', 'Y2022', 'Y2023'); ex = lambda item: sum(float(next((r[y] for r in rows if r['Item'] == item and r['Element'] == 'Export quantity'), 0) or 0) for y in Y) / 3
pr = lambda item: sum(float(next((r[y] for r in rows if r['Item'] == item and r['Element'] == 'Production'), 0) or 0) for y in Y) / 3
# kcal per kg of the commodity as exported (standard food composition values, rounded)
D = {'Wheat and products': 3400, 'Rice and products': 3600, 'Barley and products': 3300, 'Maize and products': 3600, 'Oats': 3800, 'Sorghum and products': 3400, 'Cereals, other': 3400,
     'Sugar (Raw Equivalent)': 3900, 'Rape and Mustardseed': 4900, 'Pulses': 3400, 'Bovine Meat': 2500, 'Mutton & Goat Meat': 2500, 'Pigmeat': 3000, 'Poultry Meat': 2000, 'Milk - Excluding Butter': 650,
     'Vegetable Oils': 8800, 'Fruits - Excluding Wine': 500, 'Vegetables': 250, 'Animal fats': 8000}
REQ = 2100 * 365.25
def people(items): return sum(ex(i) * 1e6 * D[i] for i in items) / REQ / 1e6       # thousand tonnes -> kg -> kcal -> people (million)
sets = [('wheat and rice only', ['Wheat and products', 'Rice and products']),
        ('all cereals (adds barley, sorghum, maize, oats)', ['Wheat and products', 'Rice and products', 'Barley and products', 'Maize and products', 'Oats', 'Sorghum and products', 'Cereals, other']),
        ('cereals, sugar, canola seed, pulses', ['Wheat and products', 'Rice and products', 'Barley and products', 'Maize and products', 'Oats', 'Sorghum and products', 'Cereals, other', 'Sugar (Raw Equivalent)', 'Rape and Mustardseed', 'Pulses']),
        ('all of the above plus meat, dairy, oils, fruit, vegetables', list(D))]
res = [['what is counted', 'people fed by exports, million (2,100 kcal a day)']] + [[n, round(people(i), 1)] for n, i in sets]
res += [['domestic population, FAO series 2021-23, million', 26.2], ['Bellotti 2017 (reported): exports feed', 36.6], ['CSIRO and UQ 2025 (reported): in all 100, of whom Australians 27, so abroad', 73]]
csv.writer(open(out, 'w', newline='')).writerows(res); [print(r) for r in res]
print('exports as a share of production, wheat and products:', round(ex('Wheat and products') / pr('Wheat and products'), 2), ' all cereals:', round(ex('Cereals - Excluding Beer') / pr('Cereals - Excluding Beer'), 2))
