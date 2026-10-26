"""Checks stage 1 (crops) against the archive: file 1 raw cubes -> file 5 sheets YYYY-adjt, rows 1 to 91 (the crops).
Usage: MODELS_DIR=/path/to/Models python3 -I verify_crops.py"""
import os, sys, re, collections, xlrd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json
from yields import read_cube, crop_year, norm
DEL = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'archive_deletions.json')))
D = os.path.join(os.environ['MODELS_DIR'], 'Yield data')
f1 = xlrd.open_workbook(os.path.join(D, '1 NRM-all 5 years - all t and ha.xls')); f5 = xlrd.open_workbook(os.path.join(D, '5 NRM-all 5 years - average.xls'))
tot = collections.Counter(); bad = collections.Counter()
for y in (2006, 2007, 2008, 2009, 2010):
    cube = read_cube(f1.sheet_by_name(str(y))); a = f5.sheet_by_name(f'{y}-adjt'); c = collections.Counter()
    for r in range(1, 92):
        base = re.sub(r'\s*\(t/ha\)\s*$', '', str(a.cell_value(r, 0))).strip()
        got = crop_year(cube, base, {(l, c) for l, c in DEL['unreliable'][str(y)]} | {(norm(b2 + sfx), c) for b2, c in DEL['later'][str(y)] for sfx in (' (ha)', ' trees (n)', ' (t)', ' lint (t)')})
        for col in range(1, 61):
            tg = a.cell_value(r, col); tg = tg if isinstance(tg, float) and tg != 0 else None
            g = got[col] if got else None
            if g is None and tg is None: k = 'both empty'
            elif g is not None and tg is not None and abs(g - tg) <= 1e-9 * max(1, abs(tg)): k = 'match'
            elif g is None: k = 'archive has value, rebuilt empty'
            elif tg is None: k = 'rebuilt has value, archive empty (deleted by a later rule)'
            else: k = 'values differ'
            c[k] += 1
            if k not in ('both empty', 'match'): bad[(k, base)] += 1
    print(y, dict(c)); tot += c
print('all', dict(tot))
for (k, b), n in sorted(bad.items(), key=lambda x: -x[1])[:14]: print('  ', n, k, '|', b)
