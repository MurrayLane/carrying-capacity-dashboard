#!/usr/bin/env python3
"""B123: every cell that differs between the old outputs and their -3 counterparts (the frozen 2011-fixed-3 and 2011-improved-3 releases).
Usage (repository root): python3 -I analysis/paper_a/diff_minus3.py        writes analysis/paper_a/minus3_cell_differences.csv and prints the count by file and column.
Pairs: long_term_levers, long_term_regions, method_effects_by_region, method_effects_summary, method_status (each with -3 beside it). Rows are matched by position (the -3 files
have the same rows in the same order; the script stops if the row counts differ); a column of the -3 file with no counterpart in the old file is listed once per row as 'new column'.
Deterministic."""
import csv, collections
PAIRS = ['long_term_levers', 'long_term_regions', 'method_effects_by_region', 'method_effects_summary', 'method_status']
KEY = {'long_term_levers': (1, 2, 3), 'long_term_regions': (1, 2), 'method_effects_by_region': (0, 1, 2, 3), 'method_effects_summary': (0, 1, 2), 'method_status': (0, 1)}
out = [['file', 'row', 'row key', 'column', 'old', 'new']]
for f in PAIRS:
    o = list(csv.reader(open(f'analysis/paper_a/{f}.csv', newline=''))); n = list(csv.reader(open(f'analysis/paper_a/{f}-3.csv', newline='')))
    if len(o) != len(n): raise SystemExit(f'{f}: {len(o)} rows against {len(n)}')
    for i, (a, b) in enumerate(zip(o, n)):
        if i == 0:
            for j in range(len(a), len(b)): out.append([f, 'header', '', 'column added', '', b[j]])
            continue
        key = ' | '.join(a[k] for k in KEY[f])
        for j, y in enumerate(b):
            if j >= len(a): out.append([f, i + 1, key, o[0][0:0] or n[0][j], '(no old column)', y])
            elif a[j] != y: out.append([f, i + 1, key, o[0][j], a[j], y])
csv.writer(open('analysis/paper_a/minus3_cell_differences.csv', 'w', newline='')).writerows(out)
c = collections.Counter((r[0], r[3]) for r in out[1:])
for k, v in sorted(c.items()): print(f'{k[0]:28s} {k[1][:70]:70s} {v}')
print(len(out) - 1, 'differing cells')
