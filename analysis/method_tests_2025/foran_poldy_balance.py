#!/usr/bin/env python3
"""Method test: the commodity balance (Foran and Poldy 2002, Future Dilemmas, CSIRO Resource Futures, chapter 2, Table 2.5) applied to Australia on current data.
Usage (repository root): python3 -I analysis/method_tests_2025/foran_poldy_balance.py   (reads fao_au_production_1997_2023.csv, fbs_au_world_2021_23.csv; writes foran_poldy_balance.csv)

Foran and Poldy ask a balance question, not a capacity question: in 2050, under three population paths and a diet that stays much as it is, does domestic production cover the human requirement for
grain, meat and fish? ('a positive food balance in all main food commodity items, apart from fish'.) Their numbers (report, Table 1.1 and Table 2.5, read from the full report in `Comparators/`):
  population 2050 (million): zero net immigration 20.6, 70,000 a year 25.1, 0.67% a year 32.5;
  requirement 2050 (Mt a year): grain 2.136, 2.713, 3.568; meat 2.278, 2.893, 3.804; fish 0.346, 0.439, 0.577; production 1997-98 (ABS): grain 31.578, meat 3.514, fish 0.223;
  grain embodied in meat (feed): a further 6.0, 7.6 and 10.0 Mt.
A capacity reading (as the register in analysis/comparators_2025 derived it): production over the requirement per person, commodity by commodity; the commodity that gives the smallest population binds."""
import csv, collections
POP = {'zero': 20.6, 'base': 25.1, 'high': 32.5}
REQ = {'grain': {'zero': 2.136, 'base': 2.713, 'high': 3.568}, 'meat': {'zero': 2.278, 'base': 2.893, 'high': 3.804}, 'fish': {'zero': 0.346, 'base': 0.439, 'high': 0.577}}
EMBODIED = {'zero': 6.0, 'base': 7.6, 'high': 10.0}
PROD9798 = {'grain': 31.578, 'meat': 3.514, 'fish': 0.223}
per_person = {c: {s: REQ[c][s] / POP[s] * 1000 for s in POP} for c in REQ}                # kg a person a year
emb_pp = {s: EMBODIED[s] / POP[s] * 1000 for s in POP}
Q = collections.defaultdict(dict)
for r in csv.DictReader(open('analysis/method_tests_2025/fao_au_production_1997_2023.csv')): Q[r['Item']][r['Year']] = float(r['Value']) / 1e6          # Mt
F = collections.defaultdict(dict)
for r in csv.DictReader(open('analysis/method_tests_2025/fbs_au_world_2021_23.csv')):
    if r['Area'] == 'Australia':
        try: F[(r['Item'], r['Element'])][r['Year']] = float(r['Value'])
        except ValueError: pass
mean = lambda d, ys: sum(d[y] for y in ys) / len(ys)
fao9798 = {'grain': mean(Q['Cereals, primary'], ('1997', '1998')), 'meat': mean(Q['Meat, Total'], ('1997', '1998'))}
Y3 = ('2021', '2022', '2023')
prod_now = {'grain': mean(Q['Cereals, primary'], Y3), 'meat': mean(Q['Meat, Total'], Y3), 'fish': mean(F[('Fish, Seafood', 'Production')], Y3) / 1000}
pop_now = mean(F[('Population', 'Total Population - Both sexes')], ('2021', '2022')) / 1000                         # million
food_now = {'grain': sum(mean(F[(i, 'Food')], Y3) for i in ['Wheat and products', 'Barley and products', 'Maize and products', 'Oats', 'Rice and products', 'Rye and products', 'Sorghum and products', 'Millet and products', 'Cereals, other'] if (i, 'Food') in F) / 1000 / pop_now * 1000,
            'meat': mean(F[('Meat', 'Food')], Y3) / 1000 / pop_now * 1000, 'fish': mean(F[('Fish, Seafood', 'Food')], Y3) / 1000 / pop_now * 1000}    # kg a person a year
out = [['item', 'value', 'note']]
for c in REQ:
    out.append([f'requirement per person, base case 2050 (kg)', f'{c}: {per_person[c]["base"]:.0f}', 'Foran and Poldy Table 2.5 over population'])
    out.append([f'actual food use per person 2021-23 (kg)', f'{c}: {food_now[c]:.0f}', 'FAO food balance (grain: cereals; fish includes imports)'])
out.append(['embodied feed grain per person, base case 2050 (kg)', f'{emb_pp["base"]:.0f}', 'Foran and Poldy: extra 7.6 Mt'])
out.append(['fidelity: FAO 1997-98 production against their ABS figures (Mt)', f'grain {fao9798["grain"]:.2f} against 31.58; meat {fao9798["meat"]:.2f} against 3.51', 'FAOSTAT crops and livestock'])
out.append(['fidelity: their balance, production over base-case requirement', ', '.join(f'{c} {PROD9798[c] / REQ[c]["base"]:.2f}' for c in REQ), 'above 1 is positive; their conclusion is positive except fish'])
out.append(['fidelity: capacity reading on 1997-98 production, base-case requirement per person (million)', ', '.join(f'{k} {v:.0f}' for k, v in {'meat': PROD9798['meat'] / per_person['meat']['base'] * 1000, 'grain direct': PROD9798['grain'] / per_person['grain']['base'] * 1000, 'grain with feed grain': PROD9798['grain'] / (per_person['grain']['base'] + emb_pp['base']) * 1000, 'fish': PROD9798['fish'] / per_person['fish']['base'] * 1000}.items()), 'the register derived 30 to 32 (meat) and 76 to 80 (grain with feed grain)'])
cap = {'meat': prod_now['meat'] / per_person['meat']['base'] * 1000, 'grain, direct': prod_now['grain'] / per_person['grain']['base'] * 1000,
       'grain with embodied feed grain': prod_now['grain'] / (per_person['grain']['base'] + emb_pp['base']) * 1000, 'fish': prod_now['fish'] / per_person['fish']['base'] * 1000}
capa = {'meat (actual food use per person)': prod_now['meat'] / food_now['meat'] * 1000, 'grain with feed grain (actual grain use per person plus their embodied grain)': prod_now['grain'] / (food_now['grain'] + emb_pp['base']) * 1000, 'fish (actual food use per person)': prod_now['fish'] / food_now['fish'] * 1000}
out.append(['production now, mean 2021-23 (Mt)', ', '.join(f'{k} {v:.2f}' for k, v in prod_now.items()), 'FAO QCL (cereals, meat); FBS (fish)'])
for k, v in cap.items(): out.append(['capacity reading 2021-23, their requirement per person (million)', f'{k}: {v:.0f}', ''])
for k, v in capa.items(): out.append(['capacity reading 2021-23, actual use per person (million)', f'{k}: {v:.0f}', ''])
csv.writer(open('analysis/method_tests_2025/foran_poldy_balance.csv', 'w', newline='')).writerows(out)
for r in out: print(r)
