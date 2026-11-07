#!/usr/bin/env python3
"""Export-inclusive 'people fed' counts (Bellotti 2017: exports feed 36.6 million; CSIRO and UQ 2025: about 100 million in all, 27 million Australians) reproduced as an energy count, to show how much the count
depends on what is counted and on the energy given to a kilogram of each export.
Usage (repository root): python3 -I analysis/comparators_2025/energy_exports.py [FBS_CSV] [OUT.csv]
  defaults: analysis/method_tests_2025/fbs_au_world_2021_23.csv (the repository's long-format FAOSTAT food balance extract, made by extract_fbs.py) and analysis/comparators_2025/energy_exports.csv.
Exports of each commodity (FAO food balance sheet for Australia, mean 2021-23, thousand tonnes) times a food energy per kg, over 2,100 kcal a person a day (about the Australian average requirement of
8,800 kJ). Nothing is netted for imports and nothing for the feed or fuel use of the commodity abroad: that is the point of the exercise. Two readings, both written:
  FAO balance energy   FAOSTAT's own food energy per kg (food supply kcal over food quantity) for Australia; the world's where Australia has no food use of the item; a typed value only where
                       neither gives one. The basis of every item is written to the output.
  as-traded densities  typed energy densities of the commodity as traded (standard food composition values, rounded, listed in TYPED below); FAO balance energy for an item with no typed value,
                       marked. This is the reading behind the single 258.1 figure (on the list of 19 items without the six added).
The span between the two readings is the answer: the count rests on the density table as much as on the tonnages."""
import csv, sys, collections
src = sys.argv[1] if len(sys.argv) > 1 else 'analysis/method_tests_2025/fbs_au_world_2021_23.csv'
out = sys.argv[2] if len(sys.argv) > 2 else 'analysis/comparators_2025/energy_exports.csv'
V = collections.defaultdict(dict)                       # (area, item, element) -> year -> value; duplicate group=item rows (Eggs, Milk) collapse to one
for r in csv.DictReader(open(src, encoding='utf-8')):
    try: V[(r['Area'], r['Item'], r['Element'])][r['Year']] = float(r['Value'])
    except ValueError: pass
def m(area, item, el):
    d = V.get((area, item, el), {}); return sum(d.values()) / len(d) if d else 0.0
ex = lambda item: m('Australia', item, 'Export quantity')                                  # thousand tonnes
pr = lambda item: m('Australia', item, 'Production')
# kcal per kg of the commodity as exported (standard food composition values, rounded): the table of the 258.1 figure, unchanged
TYPED = {'Wheat and products': 3400, 'Rice and products': 3600, 'Barley and products': 3300, 'Maize and products': 3600, 'Oats': 3800, 'Sorghum and products': 3400, 'Cereals, other': 3400,
         'Sugar (Raw Equivalent)': 3900, 'Rape and Mustardseed': 4900, 'Pulses': 3400, 'Bovine Meat': 2500, 'Mutton & Goat Meat': 2500, 'Pigmeat': 3000, 'Poultry Meat': 2000, 'Milk - Excluding Butter': 650,
         'Vegetable Oils': 8800, 'Fruits - Excluding Wine': 500, 'Vegetables': 250, 'Animal fats': 8000}
# exported food items that table left out (checker V16): no typed density, so FAO balance energy in both readings
ADDED = ['Cottonseed', 'Sweeteners, Other', 'Treenuts', 'Wine', 'Offals', 'Fish, Seafood']
REQ = 2100 * 365.25
def fao(item, order=('Australia', 'World')):
    for area in order:
        f, k = m(area, item, 'Food'), m(area, item, 'Food supply (kcal)')                  # 1000 t and million kcal: k / f is kcal per kg
        if f > 0 and k > 0: return k / f, f'FAO balance energy, {area}'
    if item in TYPED: return TYPED[item], 'typed (FAO gives none)'
    raise SystemExit(f'no energy for {item}')
def dens(item, reading):
    if reading == 'FAO balance energy': return fao(item)
    if item in TYPED: return TYPED[item], 'typed, as traded'
    k, b = fao(item); return k, b + ' (no typed value)'
def ppl(item, reading): return ex(item) * 1e6 * dens(item, reading)[0] / REQ / 1e6         # thousand tonnes -> kg -> kcal -> people (million)
CEREALS = ['Wheat and products', 'Rice and products', 'Barley and products', 'Maize and products', 'Oats', 'Sorghum and products', 'Cereals, other']
MORE = ['Sugar (Raw Equivalent)', 'Rape and Mustardseed', 'Pulses']
ALL = list(TYPED) + ADDED
sets = [('wheat and rice only', ['Wheat and products', 'Rice and products']),
        ('all cereals (adds barley, sorghum, maize, oats)', CEREALS),
        ('cereals, sugar, canola seed, pulses', CEREALS + MORE),
        ('all foods (adds meat, dairy, oils, fruit, vegetables, cottonseed, other sweeteners, tree nuts, wine, offals, fish)', ALL)]
READ = ('FAO balance energy', 'as-traded densities')
H = ['what is counted', 'reading', 'exports (thousand tonnes, mean 2021-23)', 'kcal per kg', 'basis of the kcal per kg', 'people fed by exports, million (2,100 kcal a day)']
res = [H]
for n, items in sets:
    for rd in READ: res.append([n, rd, '', '', '', round(sum(ppl(i, rd) for i in items), 1)])
lo, hi = (round(sum(ppl(i, rd) for i in ALL), 1) for rd in READ)
res.append(['all foods: span of the two readings', 'span', '', '', '', f'{lo} to {hi}'])
res.append(['all foods: midpoint of the span', 'midpoint', '', '', '', round((lo + hi) / 2, 1)])
res.append(['the list of 19 items without the six added, for the record (the single 258.1 figure)', 'as-traded densities', '', '', '', round(sum(ppl(i, READ[1]) for i in TYPED), 1)])
res.append(['all foods, FAO balance energy with the world\'s kcal per kg first, for the record', 'FAO balance energy, world first', '', '', '',
            round(sum(ex(i) * 1e6 * fao(i, ('World', 'Australia'))[0] for i in ALL) / REQ / 1e6, 1)])
for i in ALL:
    for rd in READ:
        k, b = dens(i, rd); res.append(['item: ' + i, rd, round(ex(i), 1), round(k), b, round(ppl(i, rd), 2)])
res += [['domestic population, FAO series 2021-23, million', 'FAO series', '', '', '', round(m('Australia', 'Population', 'Total Population - Both sexes') / 1000, 1)],
        ['Bellotti 2017 (reported): exports feed', 'reported', '', '', '', 36.6],
        ['CSIRO and UQ 2025 (reported): 63 abroad as the report states (100 in all less 27 at home would be 73)', 'reported', '', '', '', 63]]
csv.writer(open(out, 'w', newline='')).writerows(res); [print(r) for r in res if not r[0].startswith('item: ')]
left = sorted(((ex(i), i) for (a, i, e) in V if a == 'Australia' and e == 'Export quantity' and i not in ALL), reverse=True)[:12]
print('largest exported FBS rows not in the list (thousand tonnes; group rows included, so some are already counted through their parts):', [(i, round(x)) for x, i in left])
print('exports as a share of production, wheat and products:', round(ex('Wheat and products') / pr('Wheat and products'), 2), ' all cereals:', round(ex('Cereals - Excluding Beer') / pr('Cereals - Excluding Beer'), 2))
