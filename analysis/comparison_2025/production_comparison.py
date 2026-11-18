#!/usr/bin/env python3
"""The model's 2025 production inputs against FAOSTAT's, for the same items and years (brief B139, decision 145; R05b issue 6): the table behind the sentence "common land base and
food balance" in Paper B section 2, in place of putting the model on the FAOSTAT layer.
Usage (repository root):
  python3 -I analysis/comparison_2025/production_comparison.py                      writes production_comparison_2025.csv
  python3 -I analysis/comparison_2025/production_comparison.py --wrong-value-demo   plants one wrong value and shows the script's own check failing (nothing is written)
Reads (read only): data/abs-2016-21/cube_2020-21.json and data/abs-2022-25/cube_2022-23.json, cube_2023-24.json (the ABS crop production the model's crop yields are built from; the national
figure is column 1 of a cube, zone 1), data/2025/livestock_national_series.csv (wool, milk), pipeline/yields/archive_livestock_inputs.json (the 2010 national bases the 2025 milk and wool
inputs are scaled from), web/public/data/2025-fixed/regions.json (the land), and, for FAOSTAT, analysis/method_tests_2025/fao_qcl_countries.csv and fao_qcl_countries_2020.csv (Australia,
2020 and 2021-23) and half_landuse.csv (land).
YEAR RULE. FAOSTAT dates an Australian crop by the calendar year of harvest, ABS by the crop year to June. Winter field crops (wheat, oats, barley, canola, chickpeas, lentils) are harvested in the
calendar year the ABS crop year starts, so ABS 2022-23 is FAOSTAT 2022 (wheat: 41,199,485 t against 41,199 thousand tonnes); summer crops and horticulture (sorghum, maize, rice, sugar cane, fruit,
vegetables) are harvested or counted in the calendar year it ends, so ABS 2022-23 is FAOSTAT 2023 (sorghum: 2,326,266 t in both). The rule is agronomic and is typed before the comparison; the csv
shows it holds (the agreement is exact for the crops where the two series are the same series). ABS 2021-22 is not in the model's crop cubes and FAOSTAT 2024 is not in the files, so those years are not
compared. Milk and wool are flows over the financial year: they are set against FAOSTAT's calendar year the financial year starts and the one it ends, both shown, with no choice between them.
WHAT THE MODEL HOLDS AS A PRODUCTION INPUT, AND WHAT IT DOES NOT.
  crops   ABS area and production by region and crop (the cubes), national total here; the model turns these into yields.
  milk    each state's 2010 milk times the change in Dairy Australia's milk production of the state (pipeline/yields/recent/livestock_zone.py): national, the 2010 base 9,289,570 t times
          milk_Aust of the year over its 2009-10 value (data/2025/livestock_national_series.csv).
  wool    the ABS total wool of 2009-10 (352,737 t) times the change of the AWI committee's shorn greasy wool (343 Mkg in 2009-10).
  beef and sheep meat   ABS Livestock Products tonnes of meat produced in the year to June times a calibration to the thesis's 2010 figure (cattle 1.086, sheep and lamb 1.155). The ABS tables
          (xlsx) are not on disk, so the model's meat inputs for 2022-23 to 2024-25 cannot be recomputed here; the two figures the repository reports (cattle meat 2.10 Mt in 2020-21 and 3.00 Mt in
          2024-25, analysis/reliability_2025/README.md) are carried with that status, and the 2010 bases are compared with FAOSTAT's earliest year held (2011).
  poultry meat, pig meat, eggs   no production input: the model sets their yield from the mean grain and oilseed yield over a feed conversion ratio (pipeline/yields/livestock.py), so there is
          nothing to set against FAOSTAT; FAOSTAT's figures are listed for reference.
Land: cropland and pasture of the ABS holdings the model uses (2020-21) against FAOSTAT's land use (2021-23 mean).
Differences are (model input - FAOSTAT) / FAOSTAT."""
import csv, json, statistics, sys
D = 'analysis/method_tests_2025/'
DEMO = '--wrong-value-demo' in sys.argv
def dicts(p): return list(csv.DictReader(open(p, newline='')))
FAO = {}
for f in ('fao_qcl_countries.csv', 'fao_qcl_countries_2020.csv'):
    for x in dicts(D + f):
        if x['Area'] == 'Australia' and x['Value'] != '': FAO[(x['Item'], x['Element'], x['Year'])] = float(x['Value'])
CUBES = {'2020-21': json.load(open('data/abs-2016-21/cube_2020-21.json')), '2022-23': json.load(open('data/abs-2022-25/cube_2022-23.json')), '2023-24': json.load(open('data/abs-2022-25/cube_2023-24.json'))}
WINTER = {'Wheat', 'Oats', 'Barley', 'Canola', 'Chickpeas', 'Lentils'}                         # harvested in the calendar year the crop year starts; every other cube item in the year it ends
def fao_year(abs_name, fy): return fy[:4] if abs_name in WINTER else str(int(fy[:4]) + 1)
CROPS = {'Wheat': 'Wheat', 'Oats': 'Oats', 'Barley': 'Barley', 'Sorghum': 'Sorghum', 'Maize': 'Maize (corn)', 'Rice': 'Rice', 'Sugar cane': 'Sugar cane', 'Canola': 'Rape or colza seed',
         'Chickpeas': 'Chick peas, dry', 'Lentils': 'Lentils, dry', 'Potatoes': 'Potatoes', 'Tomatoes': 'Tomatoes', 'Onions': 'Onions and shallots, dry (excluding dehydrated)', 'Cabbages': 'Cabbages',
         'Pumpkins': 'Pumpkins, squash and gourds', 'Sweet corn': 'Green corn (maize)', 'Oranges': 'Oranges', 'Mandarins': 'Tangerines, mandarins, clementines', 'Apples': 'Apples', 'Pears': 'Pears',
         'Cherries': 'Cherries', 'Olives': 'Olives', 'Almonds': 'Almonds, in shell', 'Avocados': 'Avocados', 'Bananas': 'Bananas', 'Strawberries': 'Strawberries', 'Pineapples': 'Pineapples', 'Grape': 'Grapes'}
HEAD = ['section', 'item', 'year (ABS crop year or financial year / FAOSTAT year)', 'model input', 'FAOSTAT', 'unit', 'difference (model input - FAOSTAT)', 'difference, percent', 'basis of the model input', 'note']
ROWS = [HEAD]
def fx(x, d=2): return '' if x is None else round(x, d)
def add(sec, item, yr, m, f, unit, basis, note=''):
    ROWS.append([sec, item, yr, fx(m, 1) if m is not None else '', fx(f, 1) if f is not None else '', unit, fx(m - f, 1) if None not in (m, f) else '', fx(100 * (m / f - 1), 3) if None not in (m, f) and f else '', basis, note])
# ---------------------------------------------------------------- land
z1 = json.load(open('web/public/data/2025-fixed/regions.json'))['regions']['1']
LU = {}
for x in dicts(D + 'half_landuse.csv'):
    if x['Area'] == 'Australia' and x['Year'] in ('2021', '2022', '2023'): LU.setdefault(x['Item'], []).append(float(x['Value']) / 1000)
fc, fp = (sum(LU[k]) / 3 for k in ('Cropland', 'Permanent meadows and pastures'))
add('land', 'cropland', '2020-21 holdings / 2021-23 mean', z1['land']['cropping'] / 1e4, fc, 'Mha', 'ABS agricultural holdings, the model land layer (Settings, release 2025-fixed)', 'FAOSTAT land use, three-year mean')
add('land', 'pasture', '2020-21 holdings / 2021-23 mean', z1['land']['pasture'] / 1e4, fp, 'Mha', 'ABS agricultural holdings, the model land layer (Settings, release 2025-fixed)', 'FAOSTAT land use, three-year mean')
add('land', 'cropland and pasture together', '2020-21 holdings / 2021-23 mean', (z1['land']['cropping'] + z1['land']['pasture']) / 1e4, fc + fp, 'Mha', 'as above', 'the 0.01 Mha agreement of section S3')
# ---------------------------------------------------------------- crops
CROPDIFF = []
for fy, cube in CUBES.items():
    for abs_name, fao_name in CROPS.items():
        k = abs_name + ' (t)'
        if k not in cube['rows']: continue
        m = cube['rows'][k][1]; fyr = fao_year(abs_name, fy); f = FAO.get((fao_name, 'Production', fyr))
        if m is None or f is None: continue
        add('crops', abs_name, '%s / %s' % (fy, fyr), m, f, 't', 'ABS cube, national total (zone 1)', 'FAOSTAT item: ' + fao_name + ('' if abs_name in WINTER else '; harvested or counted in the calendar year the crop year ends'))
        CROPDIFF.append((abs_name, fy, m / f - 1, f))
FIELD = [x for x in CROPDIFF if x[0] in ('Wheat', 'Oats', 'Barley', 'Sorghum', 'Maize', 'Rice', 'Sugar cane', 'Canola', 'Chickpeas', 'Lentils')]
HORT = [x for x in CROPDIFF if x not in FIELD]
fa = [abs(x[2]) for x in FIELD]; ha_ = [abs(x[2]) for x in HORT]
ton20 = lambda keep: sum(CUBES['2020-21']['rows'][k + ' (t)'][1] for k in set(x[0] for x in CROPDIFF if x[1] == '2020-21' and keep(x[0])))
share_field = ton20(lambda n: n in set(x[0] for x in FIELD)) / ton20(lambda n: True)
ROWS.append(['crops, summary', 'field crops (wheat, oats, barley, sorghum, maize, rice, sugar cane, canola, chickpeas, lentils): %d comparisons' % len(FIELD), '', '', '', '', '', fx(100 * max(fa), 4),
             'largest absolute difference, percent; %d of %d comparisons within 0.001 percent' % (sum(1 for a in fa if a <= 1e-5), len(fa)),
             'FAOSTAT carries the ABS series for these crops (the same tonnes to the rounding of FAOSTAT\'s figures); they are %.0f%% of the tonnes of the compared crops in 2020-21' % (100 * share_field)])
ROWS.append(['crops, summary', 'fruit and vegetables of the cubes (%d comparisons of %d items, 2020-21 and 2022-23)' % (len(HORT), len(set(x[0] for x in HORT))), '', '', '', '', '', fx(100 * statistics.median(ha_), 1),
             'median absolute difference, percent; range %.1f to %.1f percent (absolute), largest %s' % (100 * min(ha_), 100 * max(ha_), max(HORT, key=lambda x: abs(x[2]))[0]),
             'FAOSTAT\'s fruit and vegetable series for Australia is not the ABS series (different source or definition, e.g. almonds in shell against kernel, not checked); they are %.0f%% of the tonnes of the compared crops in 2020-21' % (100 * (1 - share_field))])
# ---------------------------------------------------------------- milk and wool (model inputs rebuilt from the series and the 2010 bases)
SER = {x['series']: x for x in dicts('data/2025/livestock_national_series.csv')}
base = json.load(open('pipeline/yields/archive_livestock_inputs.json'))['years']['2010']
MILK0, WOOL0 = base['regions']['1']['milkTonnes'], base['national']['woolT']
for fy in ('2020-21', '2021-22', '2022-23', '2023-24'):
    m = MILK0 * float(SER['milk_Aust'][fy]) / float(SER['milk_Aust']['2009-10']); w_ = WOOL0 * float(SER['wool_shorn_greasy'][fy]) / float(SER['wool_shorn_greasy']['2009-10'])
    for fyr in (fy[:4], str(int(fy[:4]) + 1)):
        f = FAO.get(('Milk, Total', 'Production', fyr))
        if f is not None:
            add('milk', 'cow milk', '%s / %s' % (fy, fyr), m, f, 't', 'the 2010 national milk (%.0f t) times Dairy Australia milk_Aust of the year over 2009-10' % MILK0, 'FAOSTAT Milk, Total (raw milk of cattle); a financial-year flow against the calendar year the year %s' % ('starts' if fyr == fy[:4] else 'ends'))
        f = FAO.get(('Shorn wool, greasy, including fleece-washed shorn wool', 'Production', fyr))
        if f is not None:
            add('wool', 'shorn wool, greasy', '%s / %s' % (fy, fyr), w_, f, 't', 'the ABS total wool of 2009-10 (%.0f t) times the AWI shorn wool of the year over 2009-10' % WOOL0,
                'FAOSTAT shorn wool, greasy; the calendar year the year %s%s' % ('starts' if fyr == fy[:4] else 'ends', '; FAOSTAT 2022 and 2023 equal the AWI figures of 2022-23 and 2023-24 (328,000 and 318,000 t), so the whole difference there is the 2.84% base offset (ABS 2009-10 total over AWI 343 Mkg)' if fy in ('2022-23', '2023-24') and fyr == fy[:4] else ''))
# ---------------------------------------------------------------- meat: what can and cannot be set against FAOSTAT
add('beef (cattle meat)', 'archive base 2010 against FAOSTAT 2011', '2010 / 2011', base['national']['cattleMeatT'], FAO[('Beef and Buffalo Meat, primary', 'Production', '2011')], 't',
    'the archive\'s 2010 national cattle meat, to which the ABS tonnes are calibrated (x 1.086)', 'a one-year offset; FAOSTAT 2010 is not held; the calibration raises the ABS tonnes by 8.6% by construction')
add('sheep meat', 'archive base 2010 against FAOSTAT 2011 (sheep and goat meat)', '2010 / 2011', base['national']['sheepMeatT'], FAO[('Sheep and Goat Meat', 'Production', '2011')], 't',
    'the archive\'s 2010 national sheep meat, to which the ABS tonnes are calibrated (x 1.155)', 'a one-year offset; FAOSTAT includes goat meat (about 4% of sheep and goat meat in 2023: 38 of 885 kt in the held rows); the calibration raises the ABS tonnes by 15.5% by construction')
add('beef (cattle meat)', 'the repository\'s reported national figure, 2020-21, against FAOSTAT 2020', '2020-21 / 2020', 2.10e6, FAO[('Beef and Buffalo Meat, primary', 'Production', '2020')], 't',
    'REPORTED, not recomputed (analysis/reliability_2025/README.md: 2.10 million tonnes; the ABS xlsx are not on disk; whether this is before or after the 1.086 calibration is not stated there)', 'the 2024-25 figure (3.00 Mt) has no FAOSTAT year held')
for item, fao in (('poultry meat', 'Meat of chickens, fresh or chilled'), ('pig meat', 'Meat of pig with the bone, fresh or chilled'), ('eggs', 'Eggs Primary')):
    for y in ('2021', '2022', '2023'):
        add(item, 'no production input in the model', '- / %s' % y, None, FAO[(fao, 'Production', y)], 't', 'none: the yield is the mean grain and oilseed yield over a feed conversion ratio (pipeline/yields/livestock.py)', 'FAOSTAT shown for reference only')
# ---------------------------------------------------------------- the check: the national figure of the cube against FAOSTAT's for one headline crop, recomputed from the raw files
def check(claimed=None):
    m = CUBES['2022-23']['rows']['Wheat (t)'][1]; f = FAO[('Wheat', 'Production', '2022')]
    got = 100 * (m / f - 1); row = next(r for r in ROWS if r[0] == 'crops' and r[1] == 'Wheat' and r[2].startswith('2022-23'))
    want = float(row[7]) if claimed is None else claimed
    ok = abs(got - want) < 0.0006
    print('check: ABS wheat 2022-23 (%.0f t) against FAOSTAT 2022 (%.0f t), recomputed difference %.4f%%, csv/claimed %.4f%%: %s' % (m, f, got, want, 'PASS' if ok else 'MISMATCH'))
    return ok
if DEMO:
    print('EXAMPLE (deliberate wrong value): the wheat difference claimed as 2.5 percent instead of the computed value')
    ok = check(claimed=2.5); print('EXAMPLE wrong value check: %s' % ('PASS' if ok else 'FAIL (the planted value is rejected)')); sys.exit(0 if not ok else 1)
assert check()
csv.writer(open('analysis/comparison_2025/production_comparison_2025.csv', 'w', newline='')).writerows(ROWS)
for r in ROWS: print(' | '.join(str(x) for x in r[:8]))
