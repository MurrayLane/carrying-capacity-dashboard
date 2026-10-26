#!/usr/bin/env python3
"""Static audit of the dashboard workbook and its default inputs.

Usage: python3 -I audit_workbook.py MODEL.xlsx WEBAPP_DIR      (needs openpyxl)

Reports: error cells, formulas that break their column's pattern, numbers typed into formulas, named ranges that
point nowhere, whether every food subtotal feeds exactly one category total, differences between the defaults
stored in the workbook and the CSV files the website served, and whether regional land and population add up to
their state and national rows.
"""
import collections, csv, re, sys
import openpyxl
from openpyxl.formula.translate import Translator
model, webapp = sys.argv[1:3]
wf, wv = openpyxl.load_workbook(model), openpyxl.load_workbook(model, data_only=True)

print("== 1. error values in stored results")
for ws in wv.worksheets:
    errs = [c.coordinate for r in ws.iter_rows() for c in r if isinstance(c.value, str) and c.value.startswith('#')]
    print(f"  {ws.title:11s} {len(errs)} error cells")

print("== 2. formulas that break their column's pattern")
for name in ('Base', 'Yield', 'Recycle', 'Diet'):
    cols = collections.defaultdict(list)
    for r in wf[name].iter_rows():
        for c in r:
            if isinstance(c.value, str) and c.value.startswith('=') and c.row >= 6:
                try: t = Translator(c.value, origin=c.coordinate).translate_formula("A100")
                except Exception: t = c.value
                cols[c.column_letter].append((c.coordinate, t))
    for col, items in cols.items():
        if len(items) < 20: continue
        cnt = collections.Counter(t for _, t in items); n = cnt.most_common(1)[0][1]
        odd = [a for a, t in items if cnt[t] <= 2 and n >= 0.5 * len(items)]
        if odd: print(f"  {name} column {col}: {len(items)} formulas, stray cells {odd[:6]} (subtotal rows in Base column Z are expected)")

print("== 3. numbers typed inside formulas (excluding 0, 1, 100%)")
cnt = collections.Counter()
for ws in wf.worksheets:
    for r in ws.iter_rows():
        for c in r:
            if isinstance(c.value, str) and c.value.startswith('='):
                f = re.sub(r'"[^"]*"', '', c.value); f = re.sub(r"\$?[A-Z]{1,3}\$?\d+", 'REF', f)
                for k in re.findall(r'(?<![\w.])(\d+\.?\d*%?)(?![\w(])', f):
                    if k not in ('0', '1', '100%', '1%', '2'): cnt[(ws.title, k)] += 1
print("  ", cnt.most_common(10))

print("== 4. named ranges pointing nowhere")
for n, v in wf.defined_names.items():
    if '#REF!' in (v.attr_text or ''): print("  ", n)

print("== 5. each food subtotal feeds exactly one category total")
st, b = wf['Settings'], wf['Base']
def rows_in(f):
    out = []
    for m in re.finditer(r'Base!AC(\d+)(?::(?:Base!)?AC(\d+))?|(?<![!\w])AC(\d+):AC(\d+)', f):
        a, bb, c, d = m.groups(); lo, hi = (int(a), int(bb or a)) if a else (int(c), int(d)); out += list(range(lo, hi + 1))
    return out
cover = collections.defaultdict(list)
for a in ['C33', 'C35', 'C36', 'C37', 'D37', 'D34', 'C38', 'C39', 'C40', 'C45', 'C46', 'C47', 'C48', 'D48', 'E49']:
    for r in rows_in(str(st[a].value)): cover[r].append(a)
sub = [r for r in range(6, 322) if isinstance(b.cell(r, 29).value, str) and b.cell(r, 29).value.startswith('=')]
print(f"  {len(sub)} subtotal rows; feeding no category: {[r for r in sub if r not in cover]}; counted twice: {[r for r, c in cover.items() if len(c) > 1]}")

print("== 6. workbook default blocks versus the CSV files the website served")
ws = wv['Settings']; keys = ['regionId','cropping','pasture','nonAg','infrastr1','nature1','resilience','food','meategg','redmeat','activity','recycling','losses','organic','irrigation','fuel','biofuel','fibre','fibreNat','fibreWool','timber','infrastr2','nature2','population']
for label, first, fn in (('short', 110, 'default-inputs-short-term.csv'), ('long', 138, 'default-inputs-long-term.csv')):
    blk = {int(ws.cell(first, c).value): [ws.cell(first + k, c).value for k in range(24)] for c in range(2, ws.max_column + 1)
           if isinstance(ws.cell(first, c).value, (int, float)) and ws.cell(first, c).value >= 1}
    rows = {int(r['regionId']): r for r in csv.DictReader(open(webapp + fn))}; diffs = collections.defaultdict(list)
    for rid, vals in blk.items():
        for k, v in zip(keys[1:], vals[1:]):
            try: a, bb = float(v), float(rows[rid][k])
            except Exception: continue
            if abs(a - bb) > max(1e-9, abs(bb) * 1e-6): diffs[k].append((rid, round(a, 4), bb))
    print(f"  {label}: " + ('identical' if not diffs else '; '.join(f"{k} differs in {len(v)} regions, e.g. {v[0]}" for k, v in diffs.items())))

print("== 7. do regional rows add up to their state and national rows (CSV)")
d = {int(r['regionId']): {k: (float(v) if k != 'regionName' else v) for k, v in r.items()} for r in csv.DictReader(open(webapp + 'default-inputs-short-term.csv'))}
groups = {1: [2, 15, 26, 40, 49, 56, 60], 2: range(3, 15), 15: range(16, 26), 26: range(27, 40), 40: range(41, 49), 49: range(50, 56), 56: range(57, 60)}
for p, ch in groups.items():
    print(f"  {d[p]['regionName'][:10]:11s}" + ' '.join(f"{k[:7]}={(sum(d[i][k] for i in ch) - d[p][k]) / d[p][k] * 100:+.1f}%" for k in ('cropping', 'pasture', 'nonAg', 'totalArea', 'population')))
