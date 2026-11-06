#!/usr/bin/env python3
"""Method test: the food row of the ecological footprint (Simpson, Petroeschevsky and Lowe 2000, after Wackernagel et al. 1993) applied to Australia on current data.
Usage (repository root): python3 -I analysis/method_tests_2025/simpson_food.py   (reads fao_world_land_production.csv and fbs_au_world_2021_23.csv; writes simpson_food.csv)

The recipe, as the paper describes it: per-person consumption of each food, times the land a tonne of that food needs at WORLD-AVERAGE productivity, summed to crop land and pasture
(imports and exports drop out: it is a consumption count). Simpson's energy land (fossil energy for the food system, 0.43 ha a person) and garden (0.03) and forest (0.08, packaging)
are not rebuilt here: this is the land part of the food row, crop plus pasture (Simpson: crop 0.407 + pasture 1.758 = 2.165 ha a person, 1991-92).
Footprint to capacity: Australia's own cropland and pasture divided by the land a person needs (land type by land type, and in total).
Consumption: 1991-92 from ABS 4306.0 Table 1 (apparent per-capita consumption); 2021-23 from the FAO food balance sheet (food use over population).
World productivity: FAOSTAT yields and areas (same years as the consumption). Pasture is shared among ruminant products (beef, sheep and goat meat, milk) by edible protein
(FAO world protein per kg of each). Pigmeat, poultry and eggs need feed crops: feed conversion ratios of Alexander et al. 2016 Table 1 (kg dry feed per kg edible weight) over a cereal
at 88% dry matter and the world cereal yield. Every number not read from the data is listed in ASSUMPTIONS and in the README."""
import csv, collections
W = collections.defaultdict(dict)
for r in csv.DictReader(open('analysis/method_tests_2025/fao_world_land_production.csv')):
    try: W[(r['Area'], r['Item'], r['Element'])][r['Year']] = float(r['Value'])
    except ValueError: pass
F = collections.defaultdict(dict)
for r in csv.DictReader(open('analysis/method_tests_2025/fbs_au_world_2021_23.csv')):
    try: F[(r['Area'], r['Item'], r['Element'])][r['Year']] = float(r['Value'])
    except ValueError: pass
def mean(d, years): v = [d[y] for y in years if y in d]; return sum(v) / len(v)
Y91, Y21 = ('1990', '1991', '1992'), ('2021', '2022', '2023')
def q(item, el, yrs, area='World'): return mean(W[(area, item, el)], yrs)
def yield_kg_per_ha(item, yrs): return q(item, 'Production', yrs) * 1000 / q(item, 'Area harvested', yrs)
OILCROPS = ['Soya beans', 'Rape or colza seed', 'Sunflower seed', 'Groundnuts, excluding shelled', 'Oil palm fruit', 'Olives', 'Coconuts, in shell', 'Sesame seed', 'Safflower seed', 'Linseed']
def oil_yield(yrs): return q('Oilcrops, Oil Equivalent', 'Production', yrs) * 1000 / sum(q(i, 'Area harvested', yrs) for i in OILCROPS)
def sugar_yield(yrs): return q('Raw cane or beet sugar (centrifugal only)', 'Production', yrs) * 1000 / q('Sugar Crops Primary', 'Area harvested', yrs)
def prot(item): return mean(F[('World', item, 'Protein supply quantity (t)')], Y21) / mean(F[('World', item, 'Food')], Y21)   # g protein per kg food
ASSUMPTIONS = {'milk solids to whole milk (share of solids)': 0.125, 'cereal dry matter': 0.88, 'FCR poultry': 3.3, 'FCR pork': 6.4, 'FCR eggs': 2.3, '1991-92 eggs kg a person (ABS 1978-79, later years not collected)': 12.4}
FCR = {'poultry': 3.3, 'pork': 6.4, 'eggs': 2.3}
def footprint(c, yrs):
    """c: kg a person a year of beef, sheep, pig, poultry, eggs, milk (whole-milk equivalent), cereals, potatoes, veg, fruit, sugar, oil, nuts, pulses"""
    yc = yield_kg_per_ha('Cereals, primary', yrs)
    crop = {'cereals': c['cereals'] / yield_kg_per_ha('Cereals, primary', yrs), 'roots': c['potatoes'] / yield_kg_per_ha('Roots and Tubers, Total', yrs),
            'pulses': c['pulses'] / yield_kg_per_ha('Pulses, Total', yrs), 'vegetables': c['veg'] / yield_kg_per_ha('Vegetables Primary', yrs),
            'fruit': c['fruit'] / yield_kg_per_ha('Fruit Primary', yrs), 'sugar': c['sugar'] / sugar_yield(yrs), 'oil': c['oil'] / oil_yield(yrs),
            'nuts': c['nuts'] / yield_kg_per_ha('Treenuts, Total', yrs)}
    for k, fcr in FCR.items(): crop['feed for ' + k] = c[k] * fcr / ASSUMPTIONS['cereal dry matter'] / yc
    rum = {'beef': ('Beef and Buffalo Meat, primary', prot('Bovine Meat')), 'sheep': ('Sheep and Goat Meat', prot('Mutton & Goat Meat')), 'milk': ('Milk, Total', prot('Milk - Excluding Butter'))}
    pasture_ha = mean(W[('World', 'Permanent meadows and pastures', 'Area')], yrs) * 1000      # 1000 ha -> ha
    protein_total = sum(q(it, 'Production', yrs) * 1000 * p / 1000 for it, p in rum.values())   # kg protein (t x 1000 kg x g/kg / 1000)
    ha_per_kg_protein = pasture_ha / protein_total
    past = {k: c[k] * p / 1000 * ha_per_kg_protein for k, (it, p) in rum.items()}
    return crop, past, ha_per_kg_protein
# consumption, kg a person a year
C91 = {'beef': 37.4, 'sheep': 13.4 + 7.6, 'pork': 19.3, 'poultry': 25.9, 'eggs': 12.4, 'milk': 23.3 / ASSUMPTIONS['milk solids to whole milk (share of solids)'],
       'cereals': 89.2, 'potatoes': 66.6, 'veg': 153.2 - 66.6, 'fruit': 120.1, 'sugar': 45.6, 'oil': 19.6 - 2.6, 'nuts': 2.2 + 4.3, 'pulses': 0.0}
pop = mean(F[('Australia', 'Population', 'Total Population - Both sexes')], Y21)          # thousand
def fbs(item):                                                                                # kg a person a year; an item with no food use is 0
    d = F.get(('Australia', item, 'Food'), {}); return (sum(d.values()) / len(d) / pop * 1000) if d else 0.0
GR = ['Wheat and products', 'Barley and products', 'Maize and products', 'Oats', 'Rice and products', 'Rye and products', 'Sorghum and products', 'Millet and products', 'Cereals, other']
C21 = {'beef': fbs('Bovine Meat'), 'sheep': fbs('Mutton & Goat Meat'), 'pork': fbs('Pigmeat'), 'poultry': fbs('Poultry Meat'), 'eggs': fbs('Eggs'), 'milk': fbs('Milk - Excluding Butter'),
       'cereals': sum(fbs(i) for i in GR), 'potatoes': fbs('Potatoes and products'), 'veg': fbs('Vegetables'), 'fruit': fbs('Fruits - Excluding Wine'), 'sugar': fbs('Sugar (Raw Equivalent)'),
       'oil': fbs('Vegetable Oils'), 'nuts': fbs('Treenuts') + fbs('Groundnuts'), 'pulses': fbs('Pulses')}
AUS = {'1991': {'crop': mean(W[('Australia', 'Cropland', 'Area')], ['1991']) / 1000, 'pasture': mean(W[('Australia', 'Permanent meadows and pastures', 'Area')], ['1991']) / 1000},
       '2021': {'crop': mean(W[('Australia', 'Cropland', 'Area')], Y21) / 1000, 'pasture': mean(W[('Australia', 'Permanent meadows and pastures', 'Area')], Y21) / 1000}}   # million ha
out = [['period', 'item', 'ha a person']]
summ = {}
for lab, C, yrs, au in (('1991-92', C91, Y91, AUS['1991']), ('2021-23', C21, Y21, AUS['2021'])):
    crop, past, hk = footprint(C, yrs)
    cr, pa = sum(crop.values()), sum(past.values())
    for k, v in crop.items(): out.append([lab, 'crop: ' + k, round(v, 4)])
    for k, v in past.items(): out.append([lab, 'pasture: ' + k, round(v, 4)])
    out += [[lab, 'crop land total', round(cr, 3)], [lab, 'pasture total', round(pa, 3)], [lab, 'crop plus pasture', round(cr + pa, 3)], [lab, 'world pasture ha per kg ruminant protein', round(hk, 4)]]
    out += [[lab, 'Australia cropland, Mha', round(au['crop'], 2)], [lab, 'Australia pasture, Mha', round(au['pasture'], 2)],
            [lab, 'people the cropland supports at this footprint (million)', round(au['crop'] / cr, 1)], [lab, 'people the pasture supports (million)', round(au['pasture'] / pa, 1)],
            [lab, 'people, crop plus pasture together (million)', round((au['crop'] + au['pasture']) / (cr + pa), 1)]]
    summ[lab] = (cr, pa, au)
csv.writer(open('analysis/method_tests_2025/simpson_food.csv', 'w', newline='')).writerows(out)
print('consumption 1991-92:', {k: round(v, 1) for k, v in C91.items()}); print('consumption 2021-23:', {k: round(v, 1) for k, v in C21.items()})
for r in out: print(r)
print("Simpson 1991-92: crop 0.407, pasture 1.758, crop+pasture 2.165 (food row), garden 0.032, energy 0.430, forest 0.084, total 2.711")
