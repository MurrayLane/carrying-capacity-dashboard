"""Checks livestock yields against the archive: file 4 inputs -> file 5 sheets YYYY-adjt, rows 'Sheep meat' to 'Seafood total'.
Usage: MODELS_DIR=/path/to/Models python3 -I verify_livestock.py"""
import os, sys, json, re, collections, xlrd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yields import read_cube, crop_year, norm
from livestock import livestock_year, PRODUCTS
HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(os.environ['MODELS_DIR'], 'Yield data')
f1 = xlrd.open_workbook(os.path.join(D, '1 NRM-all 5 years - all t and ha.xls')); f5 = xlrd.open_workbook(os.path.join(D, '5 NRM-all 5 years - average.xls'))
DEL = json.load(open(os.path.join(HERE, 'archive_deletions.json'))); LS = json.load(open(os.path.join(HERE, 'archive_livestock_inputs.json')))['years']
tot = collections.Counter(); worst = []
for y in (2006, 2007, 2008, 2009, 2010):
    cube = read_cube(f1.sheet_by_name(str(y))); a = f5.sheet_by_name(f'{y}-adjt')
    mask = {(l, c) for l, c in DEL['unreliable'][str(y)]} | {(norm(b + sfx), c) for b, c in DEL['later'][str(y)] for sfx in (' (ha)', ' trees (n)', ' (t)', ' lint (t)')}
    # the workbook computes feed and feedlot grain yields from the crop rows before the later removals
    mask0 = {(l, c) for l, c in DEL['unreliable'][str(y)]}
    crops = {b: crop_year(cube, b, mask0) for b in ('Wheat', 'Oats', 'Barley', 'Sorghum', 'Maize', 'Canola', 'Soybeans')}
    got = livestock_year(LS[str(y)], crops); rowof = {str(a.cell_value(r, 0)).replace(' (t/ha)', '').strip(): r for r in range(1, a.nrows)}
    c = collections.Counter()
    for p in PRODUCTS:
        r = rowof[p]
        for z in range(1, 61):
            tg = a.cell_value(r, z); tg = tg if isinstance(tg, float) else None; g = got[p][z]
            if (g in (None, 0.0)) and (tg in (None, 0.0)): k = 'both empty or zero'
            elif g is not None and tg is not None and abs(g - tg) <= 1e-9 * max(1, abs(tg)): k = 'match'
            else: k = 'differ'; worst.append((y, p, z, g, tg))
            c[k] += 1; c[p + ':' + k] += 1
    print(y, {k: v for k, v in c.items() if ':' not in k}); tot += c
print('all', {k: v for k, v in tot.items() if ':' not in k})
bad = collections.Counter((p) for y, p, z, g, tg in worst); print('differences by product:', dict(bad)); print(worst[:6])
