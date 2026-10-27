#!/usr/bin/env python3
"""The animal-product rows of the 2025 yield matrix: the 2011 livestock method (livestock.py) on the 2010 class mix scaled to the herds and flocks of 2022-23 to 2024-25.

Usage: python3 -I livestock_zone.py ABS_DIR          (run from the repository root; ABS_DIR from analysis/recent_data/fetch_recent.py)
Reads   data/2025/yield_matrix.csv and crop_yields_by_year.json (zone_yields.py), the ABS herd and flock series (state totals, experimental, 2005 to 2025) and the ABS Livestock Products
        meat tables (7215009 to 7215012), the 2011 inputs (pipeline/yields/archive_livestock_inputs.json) and parameters.
Writes  data/2025/yield_matrix_livestock.csv (the matrix with the eleven animal-product rows replaced) and prints how the national figures compare with 2011.

Why this and not new class counts (SCOPE.md B12): no open source gives class counts below state level after 2020-21, and TableBuilder, ABARES and MLA hold nothing more.
  * class counts of each zone   the 2010 counts (the latest year of the archive, whose classes add up to the ABS flock and herd of that year) times the change of the state's total
                                 from 2009-10 to the year, for each of the five years 2020-21 to 2024-25 (the 2011 rows were a five-year mean), for sheep, dairy cattle and beef cattle separately (ABS Australian Agriculture: Livestock, experimental series). The mix inside each
                                 species is the 2010 mix; goats, deer, horses and the rest are the 2010 counts.
  * grazing land                the 2020-21 ABS grazing area of the zone (the land layer's pasture); hay area stays at its 2010 value; milk follows the dairy herd
  * national meat               ABS Livestock Products, tonnes of meat produced in the year to June (cattle and calves; sheep and lambs), five years, times the 2010 ratio of the archive's figure to the same ABS
                                 figure (cattle 1.086, sheep and lamb 1.155: the archive's source is not recorded and is higher in every year 2006 to 2010)
  * wool, feedlot grain         the 2010 figure times the national change in the flock or herd. These two are placeholders for a figure Murray can supply (ABARES or AWI wool production, ALFA
                                 feedlot survey); the ABS publishes neither
  * feed grain yields           the new crop yields of zone_yields.py for 2022-23 to 2024-25, their mean for the two earlier years (soybeans: the 2011 yield times the field-crop group factor)
Then livestock.livestock_year for each of the three years, the mean, the zero-irrigation conversion and g/m2, as for the 2011 rows.
"""
import csv, datetime, json, os, re, sys
import openpyxl
ROOT = os.getcwd(); ABS = sys.argv[1]
sys.path.insert(0, os.path.join(ROOT, 'pipeline', 'yields'))
from livestock import livestock_year, PRODUCTS
from average import five_year_average
# environment overrides, used by analysis/sensitivity_2025: LS_YEARS, LS_CAL=off (no calibration of the ABS meat tables), ZY_OUT (folder of zone_yields.py output, also written to)
YEARS = tuple(os.environ.get('LS_YEARS', '2020-21,2021-22,2022-23,2023-24,2024-25').split(',')); BASE = '2009-10'
OUT = os.environ.get('ZY_OUT', 'data/2025')          # five years, as the 2011 rows were; the crop yields only exist for the last three
rd = lambda p: list(csv.DictReader(open(os.path.join(ROOT, p))))
irr = {int(r['regionId']): float(r['irrigation']) for r in rd('data/2011/default-inputs-short-term.csv')}
pasture_km2 = {int(r['regionId']): float(r['pasture']) for r in rd('data/2025-land/default-inputs-short-term.csv')}
base = json.load(open(os.path.join(ROOT, 'pipeline/yields/archive_livestock_inputs.json')))['years']['2010']

# ---- zone to state --------------------------------------------------------------------------------------------------------------------------
STATE_ROW = {2: 1, 15: 2, 26: 3, 40: 4, 49: 5, 56: 6, 60: 7}                                                                                                   # state zone -> ABS state code
state_of = {}
for code, zs in {1: range(3, 15), 2: range(16, 26), 3: range(27, 40), 4: range(41, 49), 5: range(50, 56), 6: range(57, 60), 7: [60]}.items():
    for z in zs: state_of[z] = code
state_of.update(STATE_ROW)                                            # zone 1 (Australia) is handled by the national ratio

# ---- herd and flock series ------------------------------------------------------------------------------------------------------------------
def series(file, sheet, item_re):
    ws = openpyxl.load_workbook(os.path.join(ABS, file), read_only=True, data_only=True)[sheet]; rows = list(ws.iter_rows(values_only=True))
    cols = {}
    for c, h in enumerate(rows[3]):
        m = re.match(r'\s*(\d{4}-\d{2})', str(h))
        if m: cols[m.group(1)] = c
    out = {}
    for r in rows[4:]:
        if r[2] and re.search(item_re, str(r[2])): out[int(r[1])] = {y: r[c] for y, c in cols.items() if isinstance(r[c], (int, float))}
    return out
beef = series('AALDC_Cattle_herd_series_2005_to_2025.xlsx', 'Table 1', r'^Beef cattle')
dairy = series('AALDC_Cattle_herd_series_2005_to_2025.xlsx', 'Table 1', r'^Dairy cattle')
sheep = series('AALDC_Sheep_flock_series_2005_to_2025.xlsx', 'Table 1', r'^Sheep')
for name, s in (('sheep', sheep), ('beef', beef), ('dairy', dairy)):
    for y in YEARS + (BASE,): assert any(y in v for v in s.values()), f'{name}: no figures for {y}'
def ratio(s, state, year):
    """Change of the state's total since 2009-10 (1.0 where the state has no base figure, as for sheep in the Northern Territory)."""
    d = s.get(state, {}); b, n = d.get(BASE), d.get(year)
    return 1.0 if not b or n is None else n / b

# ---- national meat produced ---------------------------------------------------------------------------------------------------------------
def monthly(file):
    ws = openpyxl.load_workbook(os.path.join(ABS, file), read_only=True, data_only=True)['Data1']; out = {}
    for row in ws.iter_rows(min_row=11, values_only=True):
        if isinstance(row[0], datetime.datetime) and isinstance(row[1], (int, float)): out[row[0]] = row[1]
    return out
def fy(d, y): return sum(v for dt, v in d.items() if datetime.datetime(y - 1, 7, 1) <= dt <= datetime.datetime(y, 6, 30))
cattle_m = [monthly('7215009.xlsx'), monthly('7215010.xlsx')]; sheep_m = [monthly('7215011.xlsx'), monthly('7215012.xlsx')]
meat = lambda ds, y: sum(fy(d, y) for d in ds)
CAL_CATTLE = base['national']['cattleMeatT'] / meat(cattle_m, 2010); CAL_SHEEP = base['national']['sheepMeatT'] / meat(sheep_m, 2010)
if os.environ.get('LS_CAL') == 'off': CAL_CATTLE = CAL_SHEEP = 1.0

# ---- inputs per year ---------------------------------------------------------------------------------------------------------------------------
SHEEP = ('sheepLambs', 'sheepEwesToLamb', 'sheepEwesNotInLamb', 'sheepRams', 'sheepFeedlot'); DAIRY = ('dairyCows', 'dairyHeiferCalves', 'dairyHeifers1to2', 'dairyHeifersOver2', 'dairyBulls', 'milkTonnes')
BEEF = ('beefBulls', 'beefCows', 'beefCalves', 'beefBalance', 'cattleFeedlot')
raw_pasture_ha = {z: v * 100 for z, v in pasture_km2.items()}
def inputs_for(year):
    fyr = int('20' + year[-2:])
    regions = {}
    for z in range(1, 61):
        st = state_of.get(z); b = dict(base['regions'][str(z)])
        rs = ratio(sheep, 0 if z == 1 else st, year); rd_ = ratio(dairy, 0 if z == 1 else st, year); rb = ratio(beef, 0 if z == 1 else st, year)
        for ks, f in ((SHEEP, rs), (DAIRY, rd_), (BEEF, rb)):
            for k in ks:
                if b.get(k) is not None: b[k] *= f
        b['grazingHa'] = raw_pasture_ha[z]                           # hay area stays at 2010
        regions[str(z)] = b
    nat = dict(base['national']); rs0, rb0 = ratio(sheep, 0, year), ratio(beef, 0, year)
    nat.update(cattleMeatT=meat(cattle_m, fyr) * CAL_CATTLE, sheepMeatT=meat(sheep_m, fyr) * CAL_SHEEP, woolT=base['national']['woolT'] * rs0,
               sheepFeedlotGrainT=base['national']['sheepFeedlotGrainT'] * rs0, cattleFeedlotGrainT=base['national']['cattleFeedlotGrainT'] * rb0)
    return {'regions': regions, 'national': nat}

# ---- feed grain yields (t/ha, stage 1) -----------------------------------------------------------------------------------------------------
matrix = {int(r['regionId']): r for r in rd(OUT + '/yield_matrix.csv')}
byyear = json.load(open(os.path.join(ROOT, OUT, 'crop_yields_by_year.json')))['yields']
soy_row = '19'                                                         # sheet row of Soybeans (row 4 is wheat)
def feed(year):
    out = {}
    for c in ('Wheat', 'Oats', 'Barley', 'Sorghum', 'Maize', 'Canola'):
        have = byyear.get(c, {})
        if year in have: out[c] = have[year]
        else:                                                           # no crop figure for the year: the mean of the years there are
            out[c] = [None] + [(sum(v[z] for v in have.values() if v[z] is not None) / n if (n := sum(1 for v in have.values() if v[z] is not None)) else None) for z in range(1, 61)]
    out['Soybeans'] = [None] + [float(matrix[z][soy_row]) / 100 * (1 + 0.55 * irr[z]) if float(matrix[z][soy_row]) > 0 else None for z in range(1, 61)]
    return out

per_year = {p: [] for p in PRODUCTS}
for y in YEARS:
    res = livestock_year(inputs_for(y), feed(y))
    for p in PRODUCTS: per_year[p].append(res[p])
avg = {p: five_year_average(v) for p, v in per_year.items()}
ROW = {p: 95 + i for i, p in enumerate(PRODUCTS)}                     # Sheep meat is sheet row 95
new = {p: [None] + [None if avg[p][z] is None else avg[p][z] / (1 + 0.55 * irr[z]) * 100 for z in range(1, 61)] for p in PRODUCTS}

cols = [k for k in matrix[1] if k != 'regionId']
with open(os.path.join(ROOT, OUT, 'yield_matrix_livestock.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['regionId'] + cols)
    for z in range(1, 61):
        row = dict(matrix[z])
        for p in PRODUCTS:
            if p in ('Chicken meat', 'Duck meat', 'Turkey meat', 'Chicken eggs', 'Pig meat', 'Fish', 'Seafood', 'Sheep meat', 'Sheep wool', 'Dairy milk', 'Cattle meat'): row[str(ROW[p])] = round(new[p][z] or 0, 6)
        w.writerow([z] + [row[c] for c in cols])
print('calibration of the ABS meat tables to the archive in 2010: cattle %.3f, sheep and lamb %.3f' % (CAL_CATTLE, CAL_SHEEP))
print('national change in the herds and flocks since 2009-10:', {y: {'sheep': round(ratio(sheep, 0, y), 3), 'beef': round(ratio(beef, 0, y), 3), 'dairy': round(ratio(dairy, 0, y), 3)} for y in YEARS})
print('national meat produced (t, calibrated):', {y: (round(inputs_for(y)['national']['cattleMeatT']), round(inputs_for(y)['national']['sheepMeatT'])) for y in YEARS}, 'archive 2010:', (round(base['national']['cattleMeatT']), round(base['national']['sheepMeatT'])))
import xlrd
ws = xlrd.open_workbook(os.path.join(ROOT, 'model/model.xls')).sheet_by_name('Yield')
print(f'\n{"national yield, g/m2":24s}{"2011":>10s}{"2025":>10s}{"change":>9s}')
for p in PRODUCTS:
    o = ws.cell_value(ROW[p] - 1, 7); n = new[p][1]
    print(f'{p:24s}{o:10.1f}{(n or 0):10.1f}{((n or 0) / o - 1) * 100 if o else 0:8.0f}%')
