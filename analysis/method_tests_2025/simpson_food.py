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
at 88% dry matter and the world cereal yield. Every number not read from the data is listed in ASSUMPTIONS and in the README.

Three builds of the 1991-92 food row are written to simpson_food.csv. Build 1 is this script's FAO build above (periods "1991-92" and "2021-23"). Build 2 is the independent
rebuild of V04, copied from second_build_values.csv (period "1991-92 build 2 (V04)"). Build 3, "thesis rates" (decision 32), charges the same ABS 1991-92 consumption at the rates
Wackernagel's 1994 UBC thesis prints, read from wackernagel_1994_food_factors.csv (periods "1991-92 build 3 (thesis rates)" and "2021-23 build 3 (thesis rates)"), and the wool and
plant-crop tests of brief B47 are written under period "1991-92 tests (thesis rates)". Published sources only; the authors were not consulted."""
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

# --- Build 2: the V04 independent rebuild, as filed in second_build_values.csv (1991-92 components; 2021-23 land and capacity)
SBV = [r for r in csv.DictReader(open('analysis/method_tests_2025/second_build_values.csv')) if r['method'] == 'simpson_food']
def sbv(start): return next(float(r['value']) for r in SBV if r['quantity'].startswith(start))
b2 = {'plant': sbv('crop land for plant foods, second build, 1991-92'), 'feed': sbv('crop land for animal products (feed), second build, 1991-92'), 'pasture': sbv('pasture (beef, sheep, milk), second build, 1991-92')}
P2 = '1991-92 build 2 (V04)'
out += [[P2, 'crop: plant foods', b2['plant']], [P2, 'crop: feed for animal products', b2['feed']], [P2, 'crop land total', round(b2['plant'] + b2['feed'], 3)],
        [P2, 'pasture total', b2['pasture']], [P2, 'crop plus pasture', round(b2['plant'] + b2['feed'] + b2['pasture'], 3)]]
# --- Build 3, "thesis rates": Wackernagel 1994 (UBC PhD thesis) rates, as transcribed in wackernagel_1994_food_factors.csv (thesis page in each row's source column)
TH = list(csv.DictReader(open('analysis/method_tests_2025/wackernagel_1994_food_factors.csv')))
def th(table, item, land_type=None):
    hit = [r for r in TH if r['table'] == table and r['item'] == item and (land_type is None or r['land_type'] == land_type)]
    assert len(hit) == 1, (table, item, len(hit)); return float(hit[0]['value'].replace(',', '').split()[0])
def ty(item): return th('Table A2.2', item, 'crop (world yield basis)')                       # FAO 1990 world yield, kg/ha (thesis pp. 295 to 296)
E41 = 'Appendix 2.1 e41 clothing {wool}'
RATE = {'sheep meat kg/ha/yr (p. 285)': th(E41, 'sheep meat production per hectare'), 'wool gross kg/ha/yr (p. 285)': th(E41, 'wool production per hectare'),
        'wool net kg/ha/yr (p. 285)': th(E41, 'net wool production'), 'share of sheep pasture to meat, % (p. 285)': th(E41, 'share of sheep pasture for meat'),
        'cattle pasture ha yr per kg of all meat (p. 284)': th('Appendix 2.1 e12 animal products', '3rd calculation, pasture per kg meat'),
        'feed cropland ha yr per kg of all meat (p. 284)': th('Appendix 2.1 e12 animal products', '3rd calculation, crop per kg meat'),
        'cereal food energy kJ/kg (p. 281)': th('Appendix 2.1 d12 animal products', 'nutritional energy of cereal or flour'),
        'meat food energy MJ/t (p. 297)': th('Table A2.3 data analysis', 'nutritional energy in meat'), 'egg food energy MJ/t (p. 297)': th('Table A2.3 data analysis', 'nutritional energy in eggs'),
        'cane per kg sugar, LDC average (p. 295)': th('Table A2.2 note', 'sugar cane'), 'beet per kg sugar (p. 295)': th('Table A2.2 note', 'sugar beets')}
# typed from the thesis text where the csv holds the figure only inside a note: the feed ratio for pork, poultry and eggs (p. 281: "for pork, turkey, chicken and eggs it is 6")
TH_TYPED = {'feed energy per unit product energy, pork, poultry and eggs (thesis p. 281)': 6}
# ABS 4306.0 1991-92 Table 3 detail behind C91 (kg a person): grain products by kind, nuts by kind, red meat by kind; population, technical note 2 (year ended 30 June)
ABS3 = {'flour': 71.7, 'oatmeal and rolled oats': 1.5, 'other breakfast foods (from grain)': 10.4, 'table rice': 5.6, 'peanuts (in shell)': 2.2, 'tree nuts (in shell)': 4.3,
        'beef and veal': 37.4, 'lamb': 13.4, 'mutton': 7.6}
POP = {'1990-91': 17176910, '1991-92': 17390836}
def build3(c, grain, nuts):
    """c as for footprint(); grain: kg by thesis yield row; nuts: kg by thesis yield row. Returns plant crop, feed crop, garden, pasture (ha a person)."""
    plant = {'cereals: ' + k: v / ty(k) for k, v in grain.items()}
    plant['potatoes'] = c['potatoes'] / ty('26 potatoes')
    plant['pulses'] = c['pulses'] / ty('31 pulses 32-36,39 (?)')
    plant['sugar (as cane, 13:1)'] = c['sugar'] * RATE['cane per kg sugar, LDC average (p. 295)'] / ty('67 sugar cane + sugar trade')
    plant['oil (placeholder yield 1000 kg/ha, flagged)'] = c['oil'] / ty('palm oil')
    for k, v in nuts.items(): plant['nuts: ' + k] = v / ty(k)
    fr = TH_TYPED['feed energy per unit product energy, pork, poultry and eggs (thesis p. 281)']
    feed_kg = fr * ((c['pork'] + c['poultry']) * RATE['meat food energy MJ/t (p. 297)'] + c['eggs'] * RATE['egg food energy MJ/t (p. 297)']) / RATE['cereal food energy kJ/kg (p. 281)']
    feed = feed_kg / ty('15 cereals')
    garden = (c['veg'] + c['fruit']) / ty('49 vegetables and melons')                        # thesis c11 (p. 279): fruit and vegetables as garden at 15 t/ha
    pasture = (c['beef'] + c['sheep']) / RATE['sheep meat kg/ha/yr (p. 285)']                 # all red meat at the sheep-meat rate; no dairy on pasture
    return plant, feed, garden, pasture
G91 = {'16 wheat': ABS3['flour'], '22 oats': ABS3['oatmeal and rolled oats'], '15 cereals': ABS3['other breakfast foods (from grain)'], '17 rice': ABS3['table rice']}
N91 = {'38 ground nuts': ABS3['peanuts (in shell)'], 'treenuts, total': ABS3['tree nuts (in shell)']}
C91b = dict(C91, beef=ABS3['beef and veal'], sheep=ABS3['lamb'] + ABS3['mutton'])
P3, P3z, PT = '1991-92 build 3 (thesis rates)', '2021-23 build 3 (thesis rates)', '1991-92 tests (thesis rates)'
pl3, fe3, ga3, pa3 = build3(C91b, G91, N91)
pl3t = sum(pl3.values())
A24 = {k: next(float(r['value'].replace(',', '')) for r in TH if r['table'] == 'Table A2.4' and r['item'] == k and r['unit'] == 'kJ/kg') for k in ('meat', 'poultry', 'eggs')}
fr4 = TH_TYPED['feed energy per unit product energy, pork, poultry and eggs (thesis p. 281)'] * (C91b['pork'] * A24['meat'] + C91b['poultry'] * A24['poultry'] + C91b['eggs'] * A24['eggs']) / RATE['cereal food energy kJ/kg (p. 281)'] / ty('15 cereals')
for k, v in pl3.items(): out.append([P3, 'crop: ' + k, round(v, 4)])
out += [[P3, 'crop: plant foods', round(pl3t, 4)], [P3, 'crop: feed for pork, poultry and eggs (6:1 by food energy)', round(fe3, 4)], [P3, 'crop land total', round(pl3t + fe3, 3)],
        [P3, 'garden: fruit and vegetables at 15 t/ha', round(ga3, 4)], [P3, 'pasture total', round(pa3, 3)], [P3, 'crop plus pasture', round(pl3t + fe3 + pa3, 3)],
        [P3, 'crop: feed for pork, poultry and eggs at Table A2.4 food energies (meat 11,000, poultry 8,000, eggs 6,000 kJ/kg), for comparison', round(fr4, 4)],
        [P3, 'pasture at the cattle rate (0.00322 ha yr per kg of all meat), for comparison', round((C91b['beef'] + C91b['sheep']) * RATE['cattle pasture ha yr per kg of all meat (p. 284)'], 3)]]
# 2021-23 on the same thesis rates, held at their printed 1990 values; FBS cereals by grain where the thesis prints a yield, otherwise the cereals average
GY = {'Wheat and products': '16 wheat', 'Barley and products': '19 barley', 'Maize and products': '20 corn', 'Oats': '22 oats', 'Rice and products': '17 rice', 'Rye and products': '21 rye',
      'Sorghum and products': '24 sorghum', 'Millet and products': '23 millet + other cereals', 'Cereals, other': '15 cereals'}
G21 = collections.defaultdict(float)
for i, k in GY.items(): G21[k] += fbs(i)
pl3z, fe3z, ga3z, pa3z = build3(C21, G21, {'38 ground nuts': fbs('Groundnuts'), 'treenuts, total': fbs('Treenuts')})
cr3z = sum(pl3z.values()) + fe3z + ga3z                                                       # garden counted on Australia's cropland for the capacity reading
au = AUS['2021']
out += [[P3z, 'crop: plant foods', round(sum(pl3z.values()), 4)], [P3z, 'crop: feed for pork, poultry and eggs (6:1 by food energy)', round(fe3z, 4)],
        [P3z, 'garden: fruit and vegetables at 15 t/ha', round(ga3z, 4)], [P3z, 'crop land total, garden included', round(cr3z, 3)], [P3z, 'pasture total', round(pa3z, 3)],
        [P3z, 'crop plus pasture', round(cr3z + pa3z, 3)],
        [P3z, 'people the cropland supports at this footprint (million)', round(au['crop'] / cr3z, 1)], [P3z, 'people the pasture supports (million)', round(au['pasture'] / pa3z, 1)],
        [P3z, 'people, crop plus pasture together (million)', round((au['crop'] + au['pasture']) / (cr3z + pa3z), 1)]]
# --- Tests (brief B47). Simpson's published cells, from published_values.csv where held there; the wool cell (Table 1, row 42) typed from the paper
PUBV = {r['row']: float(r['value']) for r in csv.DictReader(open('analysis/method_tests_2025/published_values.csv')) if r['table'] == 'simpson_fidelity'}
S_WOOL = 0.854                                                                                # Simpson 2000 Table 1, row 42 clothing, pasture
S_PLANT = PUBV['Crop land for plant foods']
# wool: what 0.854 ha requires
out += [[PT, 'wool: clean wool a person that 0.854 ha requires at 14.2 kg/ha net (kg)', round(S_WOOL * RATE['wool net kg/ha/yr (p. 285)'], 2)],
        [PT, 'wool: clean wool a person that 0.854 ha requires at 10.5 kg/ha gross (kg)', round(S_WOOL * RATE['wool gross kg/ha/yr (p. 285)'], 2)],
        [PT, "wool: the thesis's own consumption rule (world 0.373 kg a person x OECD factor 5 = 1.8 kg) at 14.2 kg/ha (ha)", round(th(E41, 'Canadian wool consumption assumed') / RATE['wool net kg/ha/yr (p. 285)'], 3)]]
# reading A, a per-person share of national production: ABS 7503.0 1990-91 total wool gross value ($4,180.9m, Table 22) over the average unit gross value ($3.93 a kg, Table 26)
WOOL_GV, WOOL_UV = 4180.9e6, 3.93
greasy_kt = WOOL_GV / WOOL_UV / 1e6
scoured = next(float(r['value'].replace(',', '')) for r in TH if r['table'] == 'Table A2.3' and r['item'] == '104 wool, scoured' and r['note'] == 'world production')
greasy_w90 = q('Shorn wool, greasy, including fleece-washed shorn wool', 'Production', ('1990',))
clean_ratio = scoured / greasy_w90                                                             # thesis world scoured wool (1989) over FAO world greasy wool (1990, nearest year on hand)
clean_pp = greasy_kt * 1e6 * clean_ratio / POP['1990-91']
out += [[PT, 'wool: Australian production 1990-91, greasy (kt; ABS 7503.0 gross value over unit value)', round(greasy_kt, 1)],
        [PT, 'wool: clean-to-greasy ratio (thesis world scoured 1989 over FAO world greasy 1990)', round(clean_ratio, 3)],
        [PT, 'wool: Australian production a person 1990-91, clean (kg)', round(clean_pp, 1)],
        [PT, 'wool: pasture for a per-person share of national production at 14.2 kg/ha net (ha)', round(clean_pp / RATE['wool net kg/ha/yr (p. 285)'], 3)],
        [PT, 'wool: pasture for a per-person share of national production at 10.5 kg/ha gross (ha)', round(clean_pp / RATE['wool gross kg/ha/yr (p. 285)'], 3)],
        [PT, 'wool: share of national production that 0.854 ha is at 14.2 kg/ha net (%)', round(S_WOOL * RATE['wool net kg/ha/yr (p. 285)'] / clean_pp * 100, 1)],
        [PT, 'wool: share of national production that 0.854 ha is at 10.5 kg/ha gross (%)', round(S_WOOL * RATE['wool gross kg/ha/yr (p. 285)'] / clean_pp * 100, 1)]]
# plant crop: three readings, one at a time
noncereal = pl3t - sum(v for k, v in pl3.items() if k.startswith('cereals: '))
need_grain = (S_PLANT - noncereal) * ty('15 cereals')
g21_all = sum(sum(F.get(('Australia', i, el), {}).values()) / 3 / pop * 1000 for i in GY for el in ('Food', 'Feed', 'Seed', 'Processing', 'Losses', 'Other uses (non-food)'))
g21_nofeed = sum(sum(F.get(('Australia', i, el), {}).values()) / 3 / pop * 1000 for i in GY for el in ('Food', 'Seed', 'Processing', 'Losses', 'Other uses (non-food)'))
X = {(r['table'], r['item']): float(r['value'].replace(',', '')) for r in TH if r['table'] == 'Table A2.2 cross-checking' and r['unit'] in ('ha', 'ha/capita')}
w_ratio = 1475426000 / X[('Table A2.2 cross-checking', 'world total crop area (added up)')]          # thesis p. 296: added-up world crop area "rather than 1,475,426,000 (FAOb 1990:tb1)"
c_ratio = 45980000 / X[('Table A2.2 cross-checking', 'sum of crop area in Canada')]               # thesis p. 296: Canadian crop area "rather than 45,980,000 arable and permanent crop land"
CAN = {k: next(float(r['value']) for r in TH if r['table'] == 'Table A2.4' and r['item'] == k and r['unit'] == 'kg/yr') for k in ('cereals', 'sugar', 'pulses', 'nuts', 'oils and fats', 'potatoes')}
can_kg, aus_kg = sum(CAN.values()), C91['cereals'] + C91['sugar'] + C91['pulses'] + C91['nuts'] + C91['oil'] + C91['potatoes']
d11 = X[('Table A2.2 cross-checking', 'd11 vegetarian products')]
out += [[PT, 'plant crop: build 3 on food use (ha)', round(pl3t, 3)],
        [PT, 'plant crop: grain a person that 0.312 needs at the cereals yield, other items fixed (kg)', round(need_grain)],
        [PT, 'plant crop (a1): grain at FAO 2021-23 Australian domestic use, all uses including feed and seed, as a proxy (kg a person)', round(g21_all)],
        [PT, 'plant crop (a1): with that grain at the cereals yield (ha)', round(noncereal + g21_all / ty('15 cereals'), 3)],
        [PT, 'plant crop (a2): grain at FAO 2021-23 Australian domestic use less feed, as a proxy (kg a person)', round(g21_nofeed)],
        [PT, 'plant crop (a2): with that grain at the cereals yield (ha)', round(noncereal + g21_nofeed / ty('15 cereals'), 3)],
        [PT, 'plant crop (b1): world total crop land over added-up harvested area (thesis p. 296)', round(w_ratio, 3)],
        [PT, 'plant crop (b1): build 3 food use times that ratio (ha)', round(pl3t * w_ratio, 3)],
        [PT, 'plant crop (b2): Canadian arable and permanent crop land over added-up crop area (thesis p. 296)', round(c_ratio, 3)],
        [PT, 'plant crop (b2): build 3 food use times that ratio (ha)', round(pl3t * c_ratio, 3)],
        [PT, 'plant crop (b3): build 3 food use plus garden, times the Canadian ratio (ha)', round((pl3t + ga3) * c_ratio, 3)],
        [PT, 'plant crop (c): Canadian d11 crop, 0.183 ha (thesis p. 296)', d11],
        [PT, 'plant crop (c): Canadian crop-food kg a person, Table A2.4 (cereals, sugar, pulses, nuts, oils, potatoes)', can_kg],
        [PT, 'plant crop (c): Australian crop-food kg a person, ABS 1991-92, same items', round(aus_kg, 1)],
        [PT, 'plant crop (c): Canadian 0.183 scaled by consumption (ha)', round(d11 * aus_kg / can_kg, 3)],
        [PT, 'plant crop (c): Canadian 0.183 scaled by cereals alone (ha)', round(d11 * C91['cereals'] / CAN['cereals'], 3)]]
csv.writer(open('analysis/method_tests_2025/simpson_food.csv', 'w', newline='')).writerows(out)
print('consumption 1991-92:', {k: round(v, 1) for k, v in C91.items()}); print('consumption 2021-23:', {k: round(v, 1) for k, v in C21.items()})
for r in out: print(r)
print("Simpson 1991-92: crop 0.407, pasture 1.758, crop+pasture 2.165 (food row), garden 0.032, energy 0.430, forest 0.084, total 2.711")
