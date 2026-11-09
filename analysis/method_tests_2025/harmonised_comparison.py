#!/usr/bin/env python3
"""The harmonised comparison of the methods (decision 35; Paper B, section 5): each method run on one set of inputs, its defining choices kept.
Usage (repository root): python3 -I analysis/method_tests_2025/harmonised_comparison.py
Reads: cross_method.csv and model_entry.csv (the readings as the authors would run them, and the model's entry), henry_godden_summary.csv, cassidy.csv,
second_build_values.csv, foran_poldy_balance.csv, half_index.csv, fbs_au_world_2021_23.csv, half_fbs_countries.csv, fao_qcl_countries.csv, half_qcl_world.csv,
fao_world_land_production.csv and the model's land layer (web/public/data/2025-fixed/regions.json, zone 1). Writes harmonised_comparison.csv only.

The boundary (decision 35). Equalised, where a method takes the input:
  data year       FAOSTAT 2021-23 (the model's 2025 data taken as the same vintage);
  land base       Australia's cropland and pasture as they are: FAOSTAT agricultural land 31.65 + 331.87 = 363.5 Mha, which equals the model's ABS holdings
                  (cropping 316,499 km2 and pasture 3,318,689 km2) to 0.01 Mha, so the two bases are one run. A method that counts production counts the production
                  of that land: no scale-up to a potential land area and no per-hectare rate applied to land that did not grow the crop;
  consumption     the FAO food balance 2021-23, per person as the food balance gives it (food supply in kcal and protein, food use in kg);
  population      27,608,200 (the model's). No harmonised capacity reading takes a head count as an input: each method's capacity is its output, and its per-person
                  basis is the food balance's own (FAO's head count for the same years), so population enters only the model's rows.
Kept: world-average productivity (Simpson, HALF), no diet balance (Henry and Godden), cropland only (Cassidy), the item-by-item reading (Foran and Poldy),
the weather record (Fearnside), the model's pairing of pasture and crops. No method is given the model's diet, yields or land classes.
The one sensitivity: the footprint methods with Australia's land expressed in world-average hectares, the local-productivity adjustment of Wackernagel and Rees
(1996, p. 78: a hectare twice as productive as the world average counts as two). Here a land type's world-average hectares are the hectares that would grow
Australia's 2021-23 output of it at the method's own world-average productivity.
The method scripts are not changed: simpson_food.py and half_index.py are run here in memory up to the line that writes their output, so their functions and
data are used as they stand and their csvs are not rewritten."""
import csv, collections, contextlib, io, json, math
D = 'analysis/method_tests_2025/'
def rows(path): return list(csv.reader(open(path)))
def dicts(path): return list(csv.DictReader(open(path)))
def run_upto(script, marker):
    """Run a method script in memory up to (not including) the line that writes its csv; return its namespace."""
    src = open(D + script).read()
    assert src.count(marker) == 1, (script, marker)
    ns = {'__name__': 'harmonised_' + script[:-3]}
    with contextlib.redirect_stdout(io.StringIO()): exec(compile(src[:src.index(marker)], D + script, 'exec'), ns)
    return ns
# ---------------------------------------------------------------- the readings as the authors would run them, and the model
CM = {r['method']: r for r in dicts(D + 'cross_method.csv')}
ME = {r['release']: r for r in dicts(D + 'model_entry.csv')}
M_FIX, M_IMP = float(ME['2025-fixed']['short term (million)']), float(ME['2025-improved']['short term (million)'])
POP_MODEL = float(next(r for r in dicts('results/2025-fixed.csv') if r['zone'] == '1' and r['preset'] == 'short')['population'])
# ---------------------------------------------------------------- the land base: FAOSTAT agricultural land against the model's ABS holdings
LU = collections.defaultdict(list)
for r in dicts(D + 'half_landuse.csv'):
    if r['Area'] == 'Australia' and r['Year'] in ('2021', '2022', '2023'): LU[r['Item']].append(float(r['Value']) / 1000)
fao_crop, fao_past = (sum(LU[k]) / len(LU[k]) for k in ('Cropland', 'Permanent meadows and pastures'))
z1 = json.load(open('web/public/data/2025-fixed/regions.json'))['regions']
z1 = z1['1'] if '1' in z1 else next(v for v in z1.values() if v.get('id') == 1)
abs_crop, abs_past = z1['land']['cropping'] / 1e4, z1['land']['pasture'] / 1e4             # km2 -> Mha
assert abs((fao_crop + fao_past) - (abs_crop + abs_past)) < 0.05, 'the two land bases differ; run both'
LAND = fao_crop + fao_past
# ---------------------------------------------------------------- the consumption basis: FAO food balance 2021-23, Australia, per person
FB = collections.defaultdict(dict)
for r in dicts(D + 'fbs_au_world_2021_23.csv'):
    try: FB[(r['Area'], r['Item'], r['Element'])][r['Year']] = float(r['Value'])
    except ValueError: pass
pop_fbs = sum(FB[('Australia', 'Population', 'Total Population - Both sexes')].values()) * 1000     # three years summed, persons
kcal_day = sum(FB[('Australia', 'Grand Total', 'Food supply (kcal)')].values()) * 1e6 / pop_fbs / 365  # FAO's per-day basis (365 days)
prot_day = sum(FB[('Australia', 'Grand Total', 'Protein supply quantity (t)')].values()) * 1e6 / pop_fbs / 365
out = [['method', 'reading', '(a) as the authors would run it (million)', '(b) harmonised (million)', '(c) input effect, b - a (million)', '(c) input effect, b over a',
        '(d) method effect, b - corrected 41.5 (million)', '(d) b over corrected', '(d) b - improved 53.6 (million)', '(d) b over improved',
        '(e) local-productivity adjustment, Wackernagel and Rees p. 78 (million)', 'inputs equalised', 'defining choices kept', 'note']]
def f(x, d=1): return '' if x is None else round(x, d) + 0.0                                  # + 0.0 turns -0.0 into 0.0
def row(method, reading, a, b, e=None, eq='', kept='', note='', c_blank=False):
    c = None if (a is None or b is None or c_blank) else b - a
    out.append([method, reading, f(a), f(b), f(c), f(b / a, 3) if c is not None else '', f(None if b is None else b - M_FIX), f(None if b is None else b / M_FIX, 2),
                f(None if b is None else b - M_IMP), f(None if b is None else b / M_IMP, 2), f(e), eq, kept, note])
# ---------------------------------------------------------------- Energy and protein balance (Gifford; Henry and Godden)
hg = rows(D + 'henry_godden_summary.csv')
E = float(next(r for r in hg if r and r[0] == 'TOTAL')[1]); P = float(next(r for r in hg if r and r[0] == 'TOTAL')[2])     # 1e15 J; 1e10 g
hg_e = E * 1e15 / (kcal_day * 365 * 4184) / 1e6                                             # people (million), energy
hg_p = P * 1e10 / (prot_day * 365) / 1e6                                                    # people (million), protein
NAME = 'Energy and protein balance (Gifford; Henry and Godden)'
EQ_HG = 'land base: production of the land as it is (no scale-up); consumption: food balance supply per person (%.0f kcal and %.1f g of protein a day) in place of the factors inferred from Gifford' % (kcal_day, prot_day)
KEPT_HG = 'each nutrient counted alone (no diet balance); exports counted as food; food products only'
for r in hg:
    if r and r[0].startswith(('production as it is', 'in-use land', "Henry and Godden's 1990-91")):
        lab = {'p': 'production as it is', 'i': "scaled to Nix's 70 Mha over 59.95 Mha in use", 'H': "scaled to Nix's 70 Mha over 45.7 Mha in use"}[r[0][0]]
        row(NAME, 'energy, ' + lab, float(r[3]), hg_e, eq=EQ_HG, kept=KEPT_HG)
        row(NAME, 'protein, ' + lab, float(r[4]), hg_p, eq=EQ_HG, kept=KEPT_HG)
# ---------------------------------------------------------------- Simpson (food-row footprint) and HALF: run their scripts in memory
S = run_upto('simpson_food.py', "csv.writer(open('analysis/method_tests_2025/simpson_food.csv'")
H = run_upto('half_index.py', "csv.writer(open('analysis/method_tests_2025/half_index.csv'")
Y21 = S['Y21']
QA = collections.defaultdict(dict)                                                          # Australia and world, QCL, 2021-23
for r in dicts(D + 'fao_qcl_countries.csv'):
    if r['Value'] != '': QA[(r['Area'], r['Item'], r['Element'])][r['Year']] = float(r['Value'])
def au(item, el='Production'): d = QA.get(('Australia', item, el), {}); v = [d[y] for y in Y21 if y in d]; return sum(v) / len(v) if v else 0.0
# build 1 (this folder's FAO build): already on the harmonised inputs (FAOSTAT 2021-23 world yields, food balance consumption, the 363.5 Mha)
sf = {r[1]: float(r[2]) for r in rows(D + 'simpson_food.csv')[1:] if r[0] == '2021-23'}
sf3 = {r[1]: float(r[2]) for r in rows(D + 'simpson_food.csv')[1:] if r[0] == '2021-23 build 3 (thesis rates)'}
crop1, past1 = S['summ']['2021-23'][0], S['summ']['2021-23'][1]
assert abs(sf['crop land total'] - crop1) < 6e-4 and abs(sf['pasture total'] - past1) < 6e-4
# local productivity, build 1: Australia's 2021-23 output in world-average hectares at the build's own world yields and pasture rule
yk = S['yield_kg_per_ha']
GROUPS = {'Cereals, primary': 'Cereals, primary', 'Roots and Tubers, Total': 'Roots and Tubers, Total', 'Pulses, Total': 'Pulses, Total', 'Vegetables Primary': 'Vegetables Primary',
          'Fruit Primary': 'Fruit Primary', 'Treenuts, Total': 'Treenuts, Total'}
eq_crop1 = (sum(au(a) / yk(w, Y21) for a, w in GROUPS.items()) + au('Raw cane or beet sugar (centrifugal only)') / S['sugar_yield'](Y21)
            + au('Oilcrops, Oil Equivalent') / S['oil_yield'](Y21)) * 1000 / 1e6                # t x 1000 / (kg/ha) = ha; -> Mha
_, _, hk = S['footprint'](S['C21'], Y21)                                                    # world pasture, ha per kg of ruminant protein (the build's protein rule)
RUMQ = {'Beef and Buffalo Meat, primary': 'Bovine Meat', 'Sheep and Goat Meat': 'Mutton & Goat Meat', 'Milk, Total': 'Milk - Excluding Butter'}
eq_past1 = sum(au(q) * S['prot'](fb) for q, fb in RUMQ.items()) * hk / 1e6                  # t x g/kg = kg protein; x ha/kg; -> Mha
NAME = 'Ecological footprint, food row (Simpson)'
EQ_S = 'none needed for builds 1 and 2: already on FAOSTAT 2021-23 world yields, food balance consumption and the 363.5 Mha'
KEPT_S = 'world-average productivity; consumption footprint (imports and exports drop out); the build\'s own pasture-sharing rule'
EQN1 = 'local productivity: Australia\'s 2021-23 output is %.1f Mha of world-average cropland (against %.2f Mha) and %.1f Mha of world-average pasture (against %.2f Mha)' % (eq_crop1, fao_crop, eq_past1, fao_past)
row(NAME, 'build 1, cropland-bound', sf['people the cropland supports at this footprint (million)'], fao_crop / crop1, e=eq_crop1 / crop1, eq=EQ_S, kept=KEPT_S, note=EQN1)
row(NAME, 'build 1, pasture', sf['people the pasture supports (million)'], fao_past / past1, e=eq_past1 / past1, eq=EQ_S, kept=KEPT_S, note=EQN1)
row(NAME, 'build 1, crop and pasture together', sf['people, crop plus pasture together (million)'], LAND / (crop1 + past1), e=(eq_crop1 + eq_past1) / (crop1 + past1), eq=EQ_S, kept=KEPT_S, note=EQN1)
# build 2 (V04): its 2021-23 footprint only; it cannot be re-run here
SB = {r['quantity']: float(r['value']) for r in dicts(D + 'second_build_values.csv') if r['method'] == 'simpson_food'}
sb = lambda start: next(v for k, v in SB.items() if k.startswith(start))
c2, p2 = sb('2021-23 crop land, second build'), sb('2021-23 pasture, second build')
row(NAME, 'build 2 (V04), cropland-bound', sb('people the cropland supports'), fao_crop / c2, eq=EQ_S, kept=KEPT_S, c_blank=True,
    note='independent build, figures from second_build_values.csv; not re-run, so no local-productivity reading; the filed %.0f against %.1f here is the rounding of the filed footprint (%.3f ha), not an input' % (sb('people the cropland supports'), fao_crop / c2, c2))
row(NAME, 'build 2 (V04), crop and pasture together', sb('people, crop plus pasture together'), LAND / (c2 + p2), eq=EQ_S, kept=KEPT_S, c_blank=True,
    note='not an input effect: the filed %.0f is the pasture-only reading (%.2f Mha over %.3f ha = %.1f); crop and pasture together on the same footprint (%.3f + %.3f ha) is %.1f'
         % (sb('people, crop plus pasture together'), fao_past, p2, fao_past / p2, c2, p2, LAND / (c2 + p2)))
# build 3 (thesis rates): the printed 1990 world yields replaced by FAOSTAT 2021-23 world yields of the same rows; the rates that are not dated FAO yields are kept
# (sheep-meat pasture rate 34 kg/ha from a stocking rate, the 6:1 feed ratio, food energies, the 13:1 cane ratio, garden charged at the vegetable yield)
THESIS_TO_FAO = {'16 wheat': 'Wheat', '17 rice': 'Rice', '19 barley': 'Barley', '20 corn': 'Maize (corn)', '21 rye': 'Rye', '22 oats': 'Oats', '23 millet + other cereals': 'Millet',
                 '24 sorghum': 'Sorghum', '15 cereals': 'Cereals, primary', '26 potatoes': 'Potatoes', '31 pulses 32-36,39 (?)': 'Pulses, Total', '67 sugar cane + sugar trade': 'Sugar cane',
                 '38 ground nuts': 'Groundnuts, excluding shelled', 'treenuts, total': 'Treenuts, Total', '49 vegetables and melons': 'Vegetables Primary', 'palm oil': None}
ty_1990 = S['ty']
def ty_2021(item):
    if item not in THESIS_TO_FAO: raise KeyError(item)
    w = THESIS_TO_FAO[item]
    return S['oil_yield'](Y21) if w is None else yk(w, Y21)                                # the thesis's oil placeholder (1,000 kg/ha) replaced by the world oil yield of build 1
S['ty'] = ty_2021
pl3, fe3, ga3, pa3 = S['build3'](S['C21'], S['G21'], {'38 ground nuts': S['fbs']('Groundnuts'), 'treenuts, total': S['fbs']('Treenuts')})
S['ty'] = ty_1990
cr3 = sum(pl3.values()) + fe3 + ga3
assert abs(pa3 - sf3['pasture total']) < 6e-4                                               # the pasture rate is not a dated yield, so pasture is unchanged
# local productivity, build 3: Australia's output at the same (2021-23) rows; red meat on pasture at the thesis's sheep-meat rate, as the build charges it
B3Q = {'Wheat': '16 wheat', 'Rice': '17 rice', 'Barley': '19 barley', 'Maize (corn)': '20 corn', 'Rye': '21 rye', 'Oats': '22 oats', 'Millet': '23 millet + other cereals', 'Sorghum': '24 sorghum',
       'Triticale': '15 cereals', 'Canary seed': '15 cereals', 'Potatoes': '26 potatoes', 'Pulses, Total': '31 pulses 32-36,39 (?)', 'Sugar cane': '67 sugar cane + sugar trade',
       'Groundnuts, excluding shelled': '38 ground nuts', 'Treenuts, Total': 'treenuts, total', 'Vegetables Primary': '49 vegetables and melons', 'Fruit Primary': '49 vegetables and melons'}
eq_crop3 = (sum(au(q) * 1000 / ty_2021(t) for q, t in B3Q.items()) + au('Oilcrops, Oil Equivalent') * 1000 / ty_2021('palm oil')) / 1e6
eq_past3 = (au('Beef and Buffalo Meat, primary') + au('Sheep and Goat Meat')) * 1000 / S['RATE']['sheep meat kg/ha/yr (p. 285)'] / 1e6
EQ_S3 = "data year: the thesis's printed 1990 world yields replaced by FAOSTAT 2021-23 world yields of the same rows (its oil placeholder by the world oil yield)"
KEPT_S3 = 'world-average productivity; the thesis rates that are not dated yields (sheep-meat pasture rate, feed ratio, food energies, cane ratio, garden at the vegetable yield)'
EQN3 = 'footprint on 2021-23 yields %.3f ha of crop (garden included) and %.3f of pasture a person; local productivity: Australia\'s output is %.1f Mha of cropland and %.1f Mha of pasture at these rates' % (cr3, pa3, eq_crop3, eq_past3)
row(NAME, 'build 3 (thesis rates), cropland-bound', sf3['people the cropland supports at this footprint (million)'], fao_crop / cr3, e=eq_crop3 / cr3, eq=EQ_S3, kept=KEPT_S3, note=EQN3)
row(NAME, 'build 3 (thesis rates), pasture', sf3['people the pasture supports (million)'], fao_past / pa3, e=eq_past3 / pa3, eq=EQ_S3, kept=KEPT_S3, note=EQN3)
row(NAME, 'build 3 (thesis rates), crop and pasture together', sf3['people, crop plus pasture together (million)'], LAND / (cr3 + pa3), e=(eq_crop3 + eq_past3) / (cr3 + pa3), eq=EQ_S3, kept=KEPT_S3, note=EQN3)
# ---------------------------------------------------------------- HALF
half_au = float(next(r for r in rows(D + 'half_index.csv') if r[0] == '2021-23' and r[1] == 'Australia')[2])          # ha a person, world-average production
w = H['world'](H['Y21'] if 'Y21' in H else ('2021', '2022', '2023'))
QW = H['Q']; yv = H['yv']; YR = ('2021', '2022', '2023')
eq_croph = 0.0
for item, names in H['AREA'].items():                                                      # world cropland (harvested x adjustment) per tonne produced, times Australia's tonnes
    a_w = sum(yv(QW.get((n, 'Area harvested'), {}), YR) for n in names) * w['adj'] * H['AREA_SHARE'].get(item, 1.0)
    p_w = sum(yv(QW.get((n, 'Production'), {}), YR) for n in names)
    p_a = sum(au(n) for n in names)
    if p_w > 0: eq_croph += a_w / p_w * p_a
FH = H['F']
rum_au = sum(yv(FH.get(('Australia', p, 'Production'), {}), YR) * H['FCR'][p] for p in H['RUM'])
eq_pasth = rum_au * w['pasture'] / w['rum_need']                                            # all world pasture to ruminants by feed need, the method's rule
eq_croph /= 1e6; eq_pasth /= 1e6
NAME = 'HALF index (Alexander)'
assert round(LAND / half_au) == float(CM[NAME]['low'])                                     # cross_method.csv holds the same reading rounded to a whole million
row(NAME, "agricultural land over the diet's land a person", LAND / half_au, LAND / half_au, e=(eq_croph + eq_pasth) / half_au,
    eq='none needed: already on FAOSTAT 2021-23, the food balance diet and the 363.5 Mha', kept='world-average production; ruminants take all pasture; land by use, mass and value',
    note='diet %.3f ha a person; local productivity: Australia\'s 2021-23 output is %.1f Mha of world-average cropland and %.1f Mha of world-average pasture' % (half_au, eq_croph, eq_pasth))
# ---------------------------------------------------------------- Cassidy
cas = {r[1]: r for r in rows(D + 'cassidy.csv') if r[0] == '2021-23'}['Australia']
c_ppl, c_mha = float(cas[10]), float(cas[2])
kc = kcal_day / 2700                                                                         # the paper's 2,700 kcal a day against the food balance supply
CB = {r['quantity']: float(r['value']) for r in dicts(D + 'second_build_values.csv') if r['method'] == 'cassidy'}
cb = lambda start: next(v for k, v in CB.items() if k.startswith(start))
c_ppl2 = cb('Australia 2021-23, people per ha delivered') * cb('Australia 2021-23, cropland')
NAME = 'People per hectare (Cassidy)'
EQ_C = 'consumption: food balance supply (%.0f kcal a day) in place of the paper\'s 2,700; land base: the delivered calories of the cropland as it is' % kcal_day
KEPT_C = 'cropland only (no grazing); calories delivered after feed and other uses; exports by importers\' use; the paper\'s feed-to-food efficiencies'
row(NAME, 'this build, delivered calories', c_ppl, c_ppl / kc, eq=EQ_C, kept=KEPT_C)
row(NAME, 'second build (V05), delivered calories', c_ppl2, c_ppl2 / kc, eq=EQ_C, kept=KEPT_C)
row(NAME, 'this build, rate scaled to all %.2f Mha of cropland' % fao_crop, float(CM[NAME]['high']), c_ppl / kc, eq=EQ_C, kept=KEPT_C,
    note='the %.0f applies the rate per harvested hectare of %.1f Mha to fallow and other-crop land; on the equalised land base the cropland delivers what it grows' % (float(CM[NAME]['high']), c_mha))
# ---------------------------------------------------------------- Foran and Poldy
fp = rows(D + 'foran_poldy_balance.csv')[1:]
def fpv(item_start, value_start):
    import re
    return float(re.findall(r'[\d.]+', next(r[1] for r in fp if r[0].startswith(item_start) and r[1].startswith(value_start)).rsplit(':', 1)[-1])[0])
NAME = 'Commodity balance (Foran and Poldy)'
EQ_F = 'consumption: food balance food use per person 2021-23 in place of their 2050 requirement per person; production FAOSTAT 2021-23 (as before)'
KEPT_F = 'item by item, the item that runs out first binds; domestic requirement only; their embodied feed grain per person kept for the grain-with-feed reading'
for lab, a_s, b_s in (('meat', 'meat', 'meat'), ('fish', 'fish', 'fish'), ('grain with embodied feed grain', 'grain with', 'grain with')):
    row(NAME, lab, fpv('capacity reading 2021-23, their', a_s), fpv('capacity reading 2021-23, actual', b_s), eq=EQ_F, kept=KEPT_F,
        note='whole millions as the balance script writes them' + ('; the food balance gives feed for all livestock, exports included, so their per-person feed grain stays' if lab.startswith('grain') else ''))
# ---------------------------------------------------------------- Fearnside: the model's own failure curve, so no equalised input can be given to it
fe = next(r for r in dicts(D + 'fearnside_failure_curve.csv') if r['release'] == '2025-fixed')
NAME = 'Failure probability (Fearnside)'
for lab, col in (('average year', 'capacity, average year'), ('1 in 10', 'at 1 in 10 (10%)'), ('1 in 100', 'at 1 in 100 (1%)')):
    row(NAME, lab, float(fe[col]), None, eq='cannot take an equalised input: the readings are the model\'s own runs with the weather allowance (corrected method, 2025 data)',
        kept='the weather record (150 years of wheat, oats and barley yields)', note='left blank, not forced')
# ---------------------------------------------------------------- the model
for rel, lab in (('2025-fixed', 'The model, thesis method corrected'), ('2025-improved', 'The model, improved')):
    v = float(ME[rel]['short term (million)'])
    row(lab, 'short term, average year', v, v, eq='the reference: population %.0f, 2025 data, ABS holdings %.1f Mha' % (POP_MODEL, abs_crop + abs_past),
        kept='its own diet, yields, land classes and pairing of pasture and crops')
# ---------------------------------------------------------------- how much of the gap to the model is inputs and how much method
# On a ratio scale each reading's gap to the corrected model, a over 41.5, is the input factor (a over b) times the method factor (b over 41.5), exactly.
# Per method: the mean absolute logarithm of each factor over its readings with both a and b; then the methods weighted equally.
by = collections.defaultdict(list)
for r in out[1:]:
    if r[4] != '' and not r[0].startswith('The model'): by[r[0]].append((math.log(r[2] / r[3]), math.log(r[3] / M_FIX)))
li = sum(sum(abs(x) for x, _ in v) / len(v) for v in by.values()) / len(by)
lm = sum(sum(abs(y) for _, y in v) / len(v) for v in by.values()) / len(by)
fac = [r[5] for r in out[1:] if r[5] != '' and not r[0].startswith('The model')]
out.append(['Summary (%d methods with a harmonised reading)' % len(by), 'the gap to the corrected model split into inputs and method', '', '', '', '', '', '', '', '', '',
            '', '', 'mean absolute log factor, methods weighted equally: inputs %.2f, method %.2f; inputs %.0f%% of the two together; input factors (b over a) %.2f to %.2f; per-person bases on the FAO head count, %.2f million (2021-23), against the model population of %.2f'
            % (li, lm, 100 * li / (li + lm), min(fac), max(fac), pop_fbs / 3e6, POP_MODEL / 1e6)])
csv.writer(open(D + 'harmonised_comparison.csv', 'w', newline='')).writerows(out)
for r in out: print(' | '.join(str(x) for x in r[:11]))
print('land base: FAOSTAT %.3f + %.3f = %.3f Mha; model ABS holdings %.3f + %.3f = %.3f Mha' % (fao_crop, fao_past, LAND, abs_crop, abs_past, abs_crop + abs_past))
print('food balance per person: %.0f kcal and %.1f g protein a day; FAO population %.3f million; model population %.4f million' % (kcal_day, prot_day, pop_fbs / 3e6, POP_MODEL / 1e6))
print('world-average hectares of Australian output: build 1 cropland %.1f, pasture %.1f; build 3 cropland %.1f, pasture %.1f; HALF cropland %.1f, pasture %.1f (Mha)'
      % (eq_crop1, eq_past1, eq_crop3, eq_past3, eq_croph, eq_pasth))
print('build 3 on 2021-23 yields: crop %.3f (garden included), pasture %.3f ha a person' % (cr3, pa3))
