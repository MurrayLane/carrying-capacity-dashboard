"""Checks stage 2 against the archive: the five YYYY-adjt sheets (file 5) -> sheet Aver-add rows 1 to 102.
Usage: MODELS_DIR=/path/to/Models python3 -I verify_average.py"""
import os, sys, collections, xlrd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from average import five_year_average
D = os.path.join(os.environ['MODELS_DIR'], 'Yield data'); f5 = xlrd.open_workbook(os.path.join(D, '5 NRM-all 5 years - average.xls'))
adjt = [f5.sheet_by_name(f'{y}-adjt') for y in (2006, 2007, 2008, 2009, 2010)]; add = f5.sheet_by_name('Aver-add')
c = collections.Counter(); bad = []
for r in range(1, 103):
    per = [[(s.cell_value(r, col) if isinstance(s.cell_value(r, col), float) else None) for col in range(0, 61)] for s in adjt]
    got = five_year_average(per)
    for col in range(1, 61):
        tg = add.cell_value(r, col); tg = tg if isinstance(tg, float) and tg != 0 else None; g = got[col]
        if g is None and tg is None: k = 'both empty'
        elif g is not None and tg is not None and abs(g - tg) <= 1e-9 * max(1, abs(tg)): k = 'match'
        else: k = 'differ'; bad.append((str(add.cell_value(r, 0)), col, g, tg))
        c[k] += 1
print(dict(c)); print(bad[:6])
