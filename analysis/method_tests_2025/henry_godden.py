#!/usr/bin/env python3
"""Method test: energy and protein balance (Gifford et al. 1975; Henry and Godden 1995) applied to Australia on current data.
Usage (repository root): python3 -I analysis/method_tests_2025/henry_godden.py   (reads fbs_au_world_2021_23.csv, writes henry_godden_items.csv and henry_godden_summary.csv)

The recipe is Henry and Godden's (1995, read from the scanned paper, Tables 2 to 5):
  1. food energy and protein of domestic production, food products only, no wool or cotton fibre, imports ignored, exports counted as food;
  2. scale up by (potential intensive land / intensive land in use);
  3. divide by the consumption factors they inferred from Gifford et al. (people per unit of energy and of protein).
Their published check: 404 x 10^15 J and 306 x 10^10 g (1990-91), x 70/45.7, x 0.1760 and 0.2041 give 109 and 96 million.

Data: FAOSTAT food balance sheets, mean of 2021-2023 (the latest years), the leaf items below. Energy and protein per tonne are FAO's own world averages
(world food supply in kcal and tonnes of protein over world food use, same years), so no composition value is typed here. Edible output of an item is
production less feed, seed, non-food use, losses and processing (processing is removed where the processed product is counted separately: oil from oilseeds, sugar from cane,
wine from grapes, milk products), floored at zero. Exports are NOT removed (Henry and Godden count domestic consumption plus exports); imports are not added."""
import csv, collections
rows = list(csv.DictReader(open('analysis/method_tests_2025/fbs_au_world_2021_23.csv')))
V = collections.defaultdict(dict)
for r in rows:
    try: V[(r['Area'], r['Item'], r['Element'])][r['Year']] = float(r['Value'])
    except ValueError: pass
def m(area, item, el):
    d = V.get((area, item, el), {}); return sum(d.values()) / len(d) if d else 0.0
CEREAL = ['Wheat and products','Barley and products','Maize and products','Oats','Rice and products','Rye and products','Sorghum and products','Millet and products','Cereals, other']
# (item, group, subtract processing?)
ITEMS = [(i,'cereals',True) for i in CEREAL] + [
 ('Starchy Roots','roots',False),
 ('Sugar (Raw Equivalent)','sugar',False), ('Honey','sugar',False),
 ('Beans','pulses',False), ('Peas','pulses',False), ('Pulses, Other and products','pulses',False),
 ('Treenuts','nuts',False), ('Groundnuts','nuts',True),
 ('Rape and Mustardseed','oilseeds',True), ('Soyabeans','oilseeds',True), ('Sunflower seed','oilseeds',True), ('Cottonseed','oilseeds',True), ('Oilcrops, Other','oilseeds',True),
 ('Vegetable Oils','oil',False),
 ('Vegetables','vegetables',False), ('Fruits - Excluding Wine','fruit',True),
 ('Bovine Meat','meat',False), ('Mutton & Goat Meat','meat',False), ('Pigmeat','meat',False), ('Poultry Meat','meat',False), ('Meat, Other','meat',False), ('Offals','meat',False),
 ('Eggs','eggs',False), ('Milk - Excluding Butter','dairy',False), ('Fish, Seafood','fish',False)]
def edible(item, proc, area='Australia'):
    p = m(area, item, 'Production')
    sub = m(area, item, 'Feed') + m(area, item, 'Seed') + m(area, item, 'Other uses (non-food)') + m(area, item, 'Losses') + (m(area, item, 'Processing') if proc else 0)
    return max(0.0, p - sub)                      # 1000 t
def density(item):                                  # world: kcal per kg, protein g per kg (food use as the base)
    f = m('World', item, 'Food')
    if f <= 0: return None, None
    return m('World', item, 'Food supply (kcal)') / f, m('World', item, 'Protein supply quantity (t)') / f
out = [['item','group','production_kt','edible_output_kt','kcal_per_kg_world','protein_g_per_kg_world','energy_PJ','protein_1e10_g','note']]
tot = collections.defaultdict(lambda: [0.0, 0.0])
for item, grp, proc in ITEMS:
    e = edible(item, proc); k, pg = density(item); note = ''
    if k is None: note = 'no world food use: excluded'; k = pg = 0.0
    en = e * 1e6 * k * 4184 / 1e15                  # kt -> kg -> kcal -> J -> PJ x 1
    pr = e * 1e6 * pg / 1e10                        # kg x g/kg = g, in 1e10 g
    out.append([item, grp, round(m('Australia', item, 'Production')), round(e), round(k), round(pg, 1), round(en, 1), round(pr, 1), note])
    tot[grp][0] += en; tot[grp][1] += pr
E = sum(v[0] for v in tot.values()); P = sum(v[1] for v in tot.values())
csv.writer(open('analysis/method_tests_2025/henry_godden_items.csv', 'w', newline='')).writerows(out)
# consumption factors inferred by Henry and Godden from Gifford et al. (people, millions, per 1e15 J and per 1e10 g)
FE, FP = 0.1760, 0.2041
NIX = 70.0
popn = m('Australia', 'Population', 'Total Population - Both sexes') / 1000
# fidelity check of the recipe on their own totals
chk = [['check', 'energy', 'protein'], ['Henry and Godden 1990-91 totals (404e15 J, 306e10 g) x 70/45.7 x factors, million', round(404 * NIX / 45.7 * FE, 1), round(306 * NIX / 45.7 * FP, 1)], ['published Table 5', 109, 96]]
res = [['scenario', 'intensive land in use assumed (Mha)', 'scale-up', 'energy: people (million)', 'protein: people (million)']]
res.append(['production as it is (no scale-up)', '', 1.0, round(E * FE, 1), round(P * FP, 1)])
LAND = [('in-use land: 1990-91 sown pasture (28.3, unchanged) + 2025 cropping (31.65, model land layer)', 28.3 + 31.65),
        ("Henry and Godden's 1990-91 in-use land (45.7) left unchanged", 45.7)]
for label, L in LAND:
    res.append([label, L, round(NIX / L, 3), round(E * NIX / L * FE, 1), round(P * NIX / L * FP, 1)])
# the consumption factor: 0.1760 people per 1e15 J is 5.68 GJ a person a year, 15.6 MJ a day; compare a plain requirement of 8.8 MJ a day (2,100 kcal)
req = 8.8e6 * 365.25
res.append(['same production, plain requirement of 8.8 MJ a person a day instead of the inferred 15.6 (no scale-up)', '', 1.0, round(E * 1e15 / req / 1e6, 1), ''])
res.append(['implied energy per person in the inferred factor, MJ a day', '', '', round(1e15 / (FE * 1e6) / 365.25 / 1e6, 1), ''])
tab = [['group', 'energy_PJ', 'protein_1e10_g']] + [[g, round(v[0], 1), round(v[1], 1)] for g, v in sorted(tot.items(), key=lambda kv: -kv[1][0])] + [['TOTAL', round(E, 1), round(P, 1)]]
w = csv.writer(open('analysis/method_tests_2025/henry_godden_summary.csv', 'w', newline=''))
for blk in (chk, [[]], tab, [[]], res): w.writerows(blk)
for blk in (chk, tab, res): [print(r) for r in blk]; print()
print('population (FBS mean 2021-23, million):', round(popn, 2))
