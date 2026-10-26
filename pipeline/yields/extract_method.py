"""Writes method.json: the constants of the yield method, taken from the original workbooks.

Usage: MODELS_DIR=/path/to/Models python3 -I extract_method.py
Sources (in Models/Yield data/): 2 NRM-all 5 years - adjustments.xls, sheet Summary (seed rates, area increases, trees per hectare).
Summary row i describes raw cube row i of the 2009 sheet of file 1, so each Summary label is tied to the cube's own label.
"""
import json, os, re, xlrd
D = os.path.join(os.environ['MODELS_DIR'], 'Yield data')
f1 = xlrd.open_workbook(os.path.join(D, '1 NRM-all 5 years - all t and ha.xls'))
f2 = xlrd.open_workbook(os.path.join(D, '2 NRM-all 5 years - adjustments.xls'))
raw = f1.sheet_by_name('2009'); sm = f2.sheet_by_name('Summary')
num = lambda v: v if isinstance(v, float) else None
adj = {}                       # cube label -> {seed, areaIncrease, treesPerHa}
for r in range(1, min(raw.nrows, sm.nrows)):
    lab = str(raw.cell_value(r, 0)).strip(); s, a, t = (num(sm.cell_value(r, c)) for c in (1, 2, 3))
    if s is None and a is None and t is None: continue
    if r >= 229: continue      # rows below the crops hold the mushroom hay area, handled below
    adj[lab] = {k: v for k, v in (('seed', s), ('areaIncrease', a), ('treesPerHa', t)) if v is not None}
method = {
  'source': 'Models/Yield data/2 NRM-all 5 years - adjustments.xls (Summary); thresholds and rules from thesis section 8.1, steps 8 to 13',
  'adjustments': adj,
  'minHa': 10, 'minTonnes': 10,
  'mushroomHayDivisor': 839.0,           # the adjustments file records 837.8136; the year sheets divide by 839.0
}
json.dump(method, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'method.json'), 'w'), indent=1)
print(len(adj), 'adjusted commodities')

# ---- the cells deleted from the raw cubes as unreliable (file 3, sheets YYYY-orig against YYYY-done) -----------------
f3 = xlrd.open_workbook(os.path.join(D, '3 NRM-all 5 years - delete non relev.xls'))
norm = lambda s: re.sub(r'[^a-z0-9]', '', str(s).lower())
deleted = {}
for y in (2006, 2007, 2008, 2009, 2010):
    o, d = f3.sheet_by_name(f'{y}-orig'), f3.sheet_by_name(f'{y}-done'); cells = []
    for r in range(1, min(o.nrows, d.nrows)):
        for c in range(1, 61):
            a, b = o.cell_value(r, c), d.cell_value(r, c)
            if isinstance(a, float) and a != 0 and not (isinstance(b, float) and b != 0): cells.append([norm(o.cell_value(r, 0)), c])
    deleted[str(y)] = cells
# ---- the later removals: cells the raw cubes and file 3 leave in, but the adjusted year sheets (file 5, YYYY-adjt) do not have ----
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yields import read_cube, crop_year
f5 = xlrd.open_workbook(os.path.join(D, '5 NRM-all 5 years - average.xls'))
bases = [re.sub(r'\s*\(t/ha\)\s*$', '', str(f5.sheet_by_name('2009-adjt').cell_value(r, 0))).strip() for r in range(1, 92)]
later = {}
for y in (2006, 2007, 2008, 2009, 2010):
    cube = read_cube(f1.sheet_by_name(str(y))); a5 = f5.sheet_by_name(f'{y}-adjt'); mask = {(l, c) for l, c in deleted[str(y)]}; cells = []
    for i, b in enumerate(bases):
        got = crop_year(cube, b, mask)
        for c in range(1, 61):
            v = a5.cell_value(i + 1, c)
            if got and got[c] is not None and not (isinstance(v, float) and v != 0): cells.append([b, c])
    later[str(y)] = cells
json.dump({'source': 'Two removal steps recorded as data. "unreliable": cells present in file 3 YYYY-orig and absent in YYYY-done (the ABS reliability step). '
           '"later": cells the rebuilt per-year yield has but the archive sheet YYYY-adjt (file 5) does not. The later step follows the diagnostic sheets in file 5 '
           '(one year only and far from the national value; two years only and under a tenth of it; Aver-val checks) but was applied with judgement, and no numeric rule reproduces it exactly.',
           'unreliable': deleted, 'later': later}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'archive_deletions.json'), 'w'))
print({y: (len(deleted[y]), len(later[y])) for y in deleted}, '(unreliable, later) deleted cells')

# ---- livestock inputs: the harmonised class counts and the numbers someone had to source, for each year (file 4, sheets YYYY-t-ha) ------
# File 4 puts the zones in columns C.. (C = Australia); zone id = column index - 1 (C is index 2). The rows are the same in every year's
# sheet. How the ABS item counts were turned into these classes differs by year (the ABS item definitions changed, and the workbook handles
# 2006 and 2007, 2008 and 2010, and 2009 differently in rows 104, 105, 110, 131, 132, 150 and 151), so the classes are taken as they stand in
# each sheet. The calculation from the classes onward (DSE, shares, hectares, yields) is identical in all five years.
f4 = xlrd.open_workbook(os.path.join(D, '4 NRM-all 5 years - t per ha.xls'))
ROWS = {  # file 4 row (1-based) -> input name
  94: 'grazingHa', 95: 'hayHa', 101: 'sheepLambs', 103: 'sheepEwesToLamb', 104: 'sheepEwesNotInLamb', 105: 'sheepRams', 110: 'sheepFeedlot',
  127: 'dairyCows', 128: 'dairyHeiferCalves', 129: 'dairyHeifers1to2', 130: 'dairyHeifersOver2', 132: 'dairyBulls', 142: 'milkTonnes',
  147: 'beefBulls', 148: 'beefCows', 149: 'beefCalves', 151: 'beefBalance', 156: 'cattleFeedlot',
  170: 'buffaloes', 171: 'deer', 172: 'goats', 173: 'horsesStud', 174: 'horsesOther', 175: 'otherLivestock'}
NATIONAL = {111: 'sheepFeedlotGrainT', 117: 'sheepMeatT', 123: 'woolT', 157: 'cattleFeedlotGrainT', 163: 'cattleMeatT'}
PARAM_ROWS = {106: 'dseLambs', 107: 'dseEwesToLamb', 108: 'dseEwesNotInLamb', 109: 'dseRams', 133: 'dseDairyCows', 134: 'dseDairyHeiferCalves', 135: 'dseDairyHeifers1to2',
  136: 'dseDairyHeifersOver2', 137: 'dseDairyBulls', 152: 'dseBeefBulls', 153: 'dseBeefCows', 154: 'dseBeefCalves', 155: 'dseBeefBalance', 177: 'dseBuffaloes', 178: 'dseDeer',
  179: 'dseGoats', 180: 'dseHorsesStud', 181: 'dseHorsesOther', 182: 'dseOtherLivestock', 184: 'fcrChickenMeat', 185: 'fcrDuckMeat', 186: 'fcrTurkeyMeat',
  187: 'fcrChickenEggs', 188: 'fcrPigMeat', 189: 'fcrFish', 192: 'fcrSeafood', 119: 'sheepFeedlotHaPerHead', 165: 'cattleFeedlotHaPerHead'}
EXTRA_C = {190: 'fishAreaYield', 193: 'seafoodAreaYield'}      # constants held in the Australia column
livestock = {}; params = {}
for y in (2006, 2007, 2008, 2009, 2010):
    sh = f4.sheet_by_name(f'{y}-t-ha'); cell = lambda r, c: sh.cell_value(r - 1, c) if r - 1 < sh.nrows and c < sh.ncols else None
    regions = {str(c - 1): {n: (cell(r, c) if isinstance(cell(r, c), float) else None) for r, n in ROWS.items()} for c in range(2, 62)}
    livestock[str(y)] = {'national': {n: cell(r, 2) for r, n in NATIONAL.items()}, 'regions': regions}
    params[str(y)] = {**{n: cell(r, 1) for r, n in PARAM_ROWS.items()}, **{n: cell(r, 2) for r, n in EXTRA_C.items()}}
json.dump({'source': 'Models/Yield data/4 NRM-all 5 years - t per ha.xls: the livestock block of each YYYY-t-ha sheet (class counts as they stand in the sheet). National constants are those of the Australia column.',
           'years': livestock}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'archive_livestock_inputs.json'), 'w'))
base = params['2009']
for y, got in params.items():
    for k, v in got.items():
        if abs(v - base[k]) > 1e-12: print('PARAMETER DIFFERS BY YEAR', y, k, v, base[k])
json.dump({'source': 'Models/Yield data/4 NRM-all 5 years - t per ha.xls, column B of the livestock block (grazing dry-sheep-equivalent factors, feed conversion ratios, feedlot land per head)', 'parameters': base},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'archive_livestock_parameters.json'), 'w'), indent=1)
print('livestock inputs for', list(livestock), '; parameters:', len(base))
