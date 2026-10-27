#!/usr/bin/env python3
"""The regional yield matrix of the 2025 release: the 135 rows of the model's Yield sheet for the 60 zones of 2011, from the 2022-23 to 2024-25 ABS data.

Usage: python3 -I zone_yields.py          (run from the repository root; needs xlrd)
Writes data/2025/yield_matrix.csv (regionId, then one column per Yield sheet row, g/m2) and data/2025/yield_provenance.csv (how each cell was made).

Per row of the Yield sheet:
  reported crop   (12 field crops and avocados, bananas, macadamias have area and production at SA2)
                  SA2 area and tonnes go to the 2011 zones (zones_2011 shares: cropland share of the part of the SA2 in each zone); stage 1 (yields.crop_year, thesis
                  thresholds of 10 ha and 10 t, and a zone yield over three times or under a tenth of the national yield of that year removed: the ABS levy production is attributed to
                  where the levy is paid, which gives Queensland canola 8 t/ha in 2022-23 and some zones almost none; the tenth is the thesis's own lower limit for thin data) per year, stage 2 (three-year mean), stage 3 (fill of the pairs the author marked, national x the zone's major-crops factor;
                  divide by 1 + 0.55 x irrigation share; x100). Where the zone has no figure and the pair is not marked for filling but the 2011 model had a yield, that yield
                  moves by the crop's own national change since 2006-2010.
  other crops, derived rows    the 2011 yield of the zone times the factor of the crop's group (group_trend.py, SCOPE.md B10; data/abs-2022-25/group_trend.json)
  animal products, honey, wild fish, timber    carried from 2011 and marked so: the livestock inputs are a separate layer (SCOPE.md B12)
National and state zones take the ABS national and state figures (NSW with the ACT), as the 2011 model took the state tables.
"""
import collections, csv, json, os, statistics, sys
import xlrd
ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, 'pipeline', 'yields')); sys.path.insert(0, os.path.join(ROOT, 'pipeline', 'yields', 'recent'))
import yields
from average import five_year_average
from fill import model_yield

# environment overrides, used by analysis/sensitivity_2025 and analysis/reliability_2025: ZY_YEARS, ZY_CAP, ZY_FLOOR, ZY_FACTORS (json), ZY_OUT (output folder),
# ZY_SOURCE=2016-21 (the 2016-17 to 2020-21 cubes: national and state zones only, the ABS unreliable cells removed; the regional zones are left empty)
SOURCE = os.environ.get('ZY_SOURCE', '2022-25')
YEARS = tuple(os.environ.get('ZY_YEARS', '2022-23,2023-24,2024-25').split(','))
OUT = os.environ.get('ZY_OUT', 'data/2025'); os.makedirs(os.path.join(ROOT, OUT), exist_ok=True)
rd = lambda p: list(csv.DictReader(open(os.path.join(ROOT, p))))
M = {int(k): v for k, v in json.load(open(os.path.join(ROOT, 'pipeline/land/zone_to_nrm2011.json')))['zones'].items()}
ZONE_OF = {c: z for z, codes in M.items() for c in codes}
STATES = {2: [2, 9], 15: [3], 26: [4], 40: [5], 49: [6], 56: [7], 60: [8]}       # zone -> columns of the 2022-25 cubes (NSW with ACT)
crops = json.load(open(os.path.join(ROOT, 'pipeline/yields/abs_current/model_crops.json')))['crops']
groups = json.load(open(os.path.join(ROOT, 'pipeline/yields/recent/groups.json')))['groups']
trend = json.load(open(os.path.join(ROOT, 'data/abs-2022-25/group_trend.json')))['2025']
FACTOR = {g: v['factor'] for g, v in trend.items()}
FACTOR.update(json.loads(os.environ.get('ZY_FACTORS', '{}')))
DERIVED_GROUP = {'Berries': 'fruit', 'Melons': 'vegetables', 'Orange-mandarine': 'fruit', 'Other citrus': 'fruit', 'Stone fruit': 'fruit', 'Lettuce': 'vegetables', 'Buckwheat': 'field crops', 'Quinoa': 'field crops',
                 'Rye': 'field crops', 'Spelt': 'field crops', 'Fig': 'fruit', 'Passionfruit': 'fruit', 'Persimmon': 'fruit', 'Rhubarb': 'vegetables', 'Chestnut': 'nuts', 'Hazelnut': 'nuts', 'Linseed': 'field crops',
                 'Pine': 'nuts', 'Pistachio': 'nuts', 'Sesame seed': 'field crops', 'Broccoflower': 'vegetables', 'Chives': 'vegetables', 'Kale': 'vegetables', 'Alfalfa': 'field crops', 'Choko': 'vegetables',
                 'Cassava': 'vegetables', 'Coffee': 'fruit', 'Tea leaf': 'fruit'}
CARRIED = ('Sheep meat', 'Sheep wool', 'Dairy milk', 'Cattle meat', 'Chicken meat', 'Duck meat', 'Turkey meat', 'Chicken eggs', 'Pig meat', 'Fish', 'Seafood', 'Honey', 'milk (goat)', 'milk (sheep)', 'fish (wild caught)', 'timber')

# ---- the 2011 model's yields -------------------------------------------------------------------------------------------------------------------
wb = xlrd.open_workbook(os.path.join(ROOT, 'model/model.xls')); ws = wb.sheet_by_name('Yield')
yield_rows = [r for r in range(4, 139)]                                    # 1-based sheet rows 4..138, as build-data injects them
label = {r: str(ws.cell_value(r - 1, 0)) for r in yield_rows}
old = {r: [None] + [(ws.cell_value(r - 1, 6 + z) if isinstance(ws.cell_value(r - 1, 6 + z), float) and ws.cell_value(r - 1, 6 + z) > 0 else None) for z in range(1, 61)] for r in yield_rows}
irr = {int(r['regionId']): float(r['irrigation']) for r in rd('data/2011/default-inputs-short-term.csv')}
raw_old = lambda r, z: None if old[r][z] is None else old[r][z] / 100 * (1 + 0.55 * irr[z])          # t/ha before the zero-irrigation conversion

# ---- SA2 to zone allocation -----------------------------------------------------------------------------------------------------------------
classes = {int(r['Value']): r['TERTV8'].split(' ')[0].rstrip('.') for r in rd('data/sa2/clum_classes.csv')}
CROPLAND = ('3.3', '3.4', '3.5', '3.6', '4.3', '4.4', '4.5', '4.6')
under = lambda code, ps: any(code == p or code.startswith(p + '.') for p in ps)
piece = collections.defaultdict(lambda: collections.defaultdict(float))
for r in rd('data/nrm2011/land_use_by_sa2_nrm2011_piece.csv'):
    p = piece[(r['zone_name'], int(r['nrmr_code_2011']))]; k = float(r['km2']); p['total'] += k
    if under(classes[int(r['class_code'])], CROPLAND): p['cropland'] += k
share = collections.defaultdict(dict)                                       # sa2 -> zone -> share of its cropland (area where none)
parts = collections.defaultdict(dict)
for (s, n), p in piece.items():
    if n in ZONE_OF: parts[s][n] = p
for s, d in parts.items():
    key = 'cropland' if sum(p['cropland'] for p in d.values()) > 0 else 'total'; tot = sum(p[key] for p in d.values())
    for n, p in d.items(): share[s][ZONE_OF[n]] = share[s].get(ZONE_OF[n], 0) + p[key] / tot

regs = json.load(open(os.path.join(ROOT, 'data/abs-2022-25/regions.json')))['regions']
col_sa2 = {r['column']: r['code'] for r in regs if r['kind'] == 'sa2'}


BAD = set()
def zone_cube(year):
    global BAD
    folder = 'abs-2016-21' if SOURCE == '2016-21' else 'abs-2022-25'
    raw = json.load(open(os.path.join(ROOT, f'data/{folder}/cube_{year}.json')))
    cube, out = raw['rows'], {}
    if SOURCE == '2016-21': BAD = {(yields.norm(l), zone) for l, c in raw['unreliable'] for zone, cols in STATES.items() if c in cols}
    for lab, v in cube.items():
        z = [None] * 61
        for col, code in (col_sa2.items() if SOURCE != '2016-21' else ()):
            if v[col] is None or code not in share: continue
            for zone, sh in share[code].items(): z[zone] = (z[zone] or 0) + v[col] * sh
        z[1] = v[1]
        for zone, cols in STATES.items():
            xs = [v[c] for c in cols if v[c] is not None]; z[zone] = sum(xs) if xs else None
        out[yields.norm(lab)] = z
    return out


per_year = collections.defaultdict(list); capped = collections.Counter(); byyear = {}
CAP, FLOOR = float(os.environ.get('ZY_CAP', 3.0)), float(os.environ.get('ZY_FLOOR', 0.1))
for y in YEARS:
    zc = zone_cube(y)
    for i, c in enumerate(crops, start=1):
        if yields.norm(c + ' (t)') in zc and yields.norm(c + ' (ha)') in zc:
            v = yields.crop_year(zc, c, thresholds=True, deleted=BAD)
            for z in range(1, 61):                                          # a crop that returns less than its seed has no yield (Queensland oats: 0.2 t/ha less 0.0425 seed)
                if v[z] is not None and v[z] <= 0: v[z] = None; capped['(at or below zero after the seed deduction)'] += 1
            for z in range(2, 61):                                          # levy production is attributed to where the levy is paid: a zone yield over CAP times, or under FLOOR times, the national yield of the year is not a yield
                if v[z] is not None and v[1] and (v[z] > CAP * v[1] or v[z] < FLOOR * v[1]): v[z] = None; capped[c] += 1
            per_year[i].append(v); byyear.setdefault(c, {})[y] = v
json.dump({'note': 'Stage 1 yields (t/ha, before the zero-irrigation conversion) per crop, year and zone (index = zone id, 0 unused), after the plausibility rules; used by livestock_zone.py for the feed grain', 'yields': byyear}, open(os.path.join(ROOT, OUT, 'crop_yields_by_year.json'), 'w'))
avg = {i: five_year_average(v) for i, v in per_year.items()}
FILL = {(int(r) - 2, z) for r, zs in json.load(open(os.path.join(ROOT, 'pipeline/yields/archive_fill_mask.json')))['fillCells'].items() for z in zs}
from fill import MAJOR_ROWS
filled = model_yield({**{r: [None] * 61 for r in MAJOR_ROWS}, **avg}, irr, FILL)      # g/m2 with the fill of marked pairs (potatoes are not reported, so the major-crops factor has six crops)

# ---- the matrix --------------------------------------------------------------------------------------------------------------------------------
own_ratio = {}
for i in avg:
    n = avg[i][1]; o = raw_old(3 + i, 1)
    if n and o: own_ratio[i] = n / o
matrix = {z: {} for z in range(1, 61)}; prov = []; count = collections.Counter()
for r in yield_rows:
    i = r - 3; name = label[r].split(' (')[0].strip()                       # i: row of the averaged table (1 to 91 are the crops)
    for z in range(1, 61):
        o = old[r][z]
        if i in avg:                                                        # a crop with area and production in 2022-25
            if avg[i][z] is not None: v, how = filled[i][z], 'observed 2022-25'
            elif filled[i][z] is not None: v, how = filled[i][z], 'filled (marked pair)'
            elif o is not None and i in own_ratio: v, how = o * own_ratio[i], "2011 x the crop's own national change"
            else: v, how = None, 'none'
        elif 1 <= i <= 91:                                                  # a crop the ABS no longer reports
            g = groups[crops[i - 1]]; v, how = (None if o is None else o * FACTOR[g]), f'2011 x group factor ({g})'
        elif any(label[r].startswith(c) for c in CARRIED):
            v, how = o, 'carried from 2011'
        else:                                                               # derived and literature-based rows
            g = DERIVED_GROUP[name]; v, how = (None if o is None else o * FACTOR[g]), f'2011 x group factor ({g})'
        matrix[z][r] = 0 if v is None else v; count[how] += 1
        prov.append((z, r, label[r], how))
with open(os.path.join(ROOT, OUT, 'yield_matrix.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['regionId'] + yield_rows)
    for z in range(1, 61): w.writerow([z] + [round(matrix[z][r], 6) for r in yield_rows])
with open(os.path.join(ROOT, OUT, 'yield_provenance.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['regionId', 'sheetRow', 'label', 'how']); w.writerows(prov)
print('cells by how they were made:'); [print(f'  {v:6d}  {k}') for k, v in count.most_common()]
print(f'zone-years removed (over {CAP:g} or under {FLOOR:g} times the national yield of the year, or at or below zero after the seed deduction):', sum(capped.values()), dict(capped))
print('crops with their own 2022-25 data:', sorted(label[3 + i].split(' (')[0] for i in avg))
print('own national change (new/old):', {label[3 + i].split(' (')[0]: round(v, 2) for i, v in own_ratio.items()})
