#!/usr/bin/env python3
"""The proportional export count (CSIRO and UQ 2025: 27 million x 70/30, "around 100 million"; Bellotti 2017: 61 million) rebuilt from the food balance: production over domestic use,
times the population. This is the output behind "counting exports stretches the claims to 60 to 100 million".
Usage (repository root): python3 -I analysis/comparators_2025/proportional_count.py   (reads analysis/method_tests_2025/fbs_au_world_2021_23.csv and results/2025-fixed.csv; writes
analysis/comparators_2025/proportional_count.csv)
Recipe. Australia, FAO food balance, mean 2021-23, every leaf item (group rows left out, the duplicated group=item rows of eggs, milk and miscellaneous counted once). Domestic supply is
production + imports - exports - stock variation (this closes the balance: it equals the sum of food, feed, seed, losses, processing and other uses; wheat exactly). Each item is weighted by its
food energy per kg from FAOSTAT's own balance (Australia's food supply kcal over food quantity, the world's where Australia has no food use), or by mass. The ratio production / domestic use,
with feed counted as a domestic use and with it left out, times the population (FAO 2021-23 series, and the 2025 population of results/2025-fixed.csv), is the number of people the production
would supply in the proportions of domestic use. It is a proportion, not a capacity: no diet balance, no land, no weather."""
import csv, collections
SRC, OUT = 'analysis/method_tests_2025/fbs_au_world_2021_23.csv', 'analysis/comparators_2025/proportional_count.csv'
V = collections.defaultdict(dict)
for r in csv.DictReader(open(SRC)):
    try: V[(r['Area'], r['Item'], r['Element'])][r['Year']] = float(r['Value'])
    except ValueError: pass
def m(area, item, el):
    d = V.get((area, item, el), {}); return sum(d.values()) / len(d) if d else 0.0
GROUPS = {'Grand Total', 'Vegetal Products', 'Animal Products', 'Cereals - Excluding Beer', 'Starchy Roots', 'Sugar Crops', 'Sugar & Sweeteners', 'Pulses', 'Treenuts', 'Oilcrops', 'Vegetable Oils',
          'Vegetables', 'Fruits - Excluding Wine', 'Stimulants', 'Spices', 'Alcoholic Beverages', 'Meat', 'Offals', 'Animal fats', 'Fish, Seafood', 'Aquatic Products, Other', 'Population'}
ITEMS = sorted({i for (a, i, e) in V if a == 'Australia'} - GROUPS)
def kcal(item, order):
    for area in order:
        f, k = m(area, item, 'Food'), m(area, item, 'Food supply (kcal)')
        if f > 0 and k > 0: return k / f
    return 0.0                                                                              # no food energy anywhere (non-food alcohol): weight 0
def totals(weight):
    P = S = F = 0.0
    for i in ITEMS:
        w = weight(i)
        p = m('Australia', i, 'Production'); s = p + m('Australia', i, 'Import quantity') - m('Australia', i, 'Export quantity') - m('Australia', i, 'Stock Variation')
        P += p * w; S += s * w; F += m('Australia', i, 'Feed') * w
    return P, S, F
pop_fao = m('Australia', 'Population', 'Total Population - Both sexes') / 1000
pop_25 = next(float(r['population']) for r in csv.DictReader(open('results/2025-fixed.csv')) if r['zone'] == '1' and r['preset'] == 'short') / 1e6
BASES = [('energy, FAO kcal per kg (Australia first)', lambda i: kcal(i, ('Australia', 'World'))), ('energy, FAO kcal per kg (world first)', lambda i: kcal(i, ('World', 'Australia'))), ('mass', lambda i: 1.0)]
res = [['weighting', 'domestic use', 'production over domestic use', 'population (million)', 'population basis', 'people supplied in the proportions of domestic use (million)']]
for name, w in BASES:
    P, S, F = totals(w)
    for use, d in (('with feed', S), ('without feed', S - F)):
        for pop, pb in ((pop_fao, 'FAO series 2021-23'), (pop_25, '2025 (results/2025-fixed.csv)')):
            res.append([name, use, round(P / d, 3), round(pop, 2), pb, round(P / d * pop, 1)])
en = [r for r in res[1:] if r[0].startswith('energy')]
for use in ('with feed', 'without feed'):
    v = [r[5] for r in en if r[1] == use]; res.append(['energy, both FAO bases', use, '', '', 'both', f'{min(v)} to {max(v)}'])
csv.writer(open(OUT, 'w', newline='')).writerows(res); [print(r) for r in res]
