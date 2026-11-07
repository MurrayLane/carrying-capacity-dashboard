#!/usr/bin/env python3
"""Builds the MC_WIN_DIR folder of the long-window Monte Carlo on the current base (defect X069): each window = base matrix + (window - base window),
the window and the base window both from one rebuild_off.py run (LS_SERIES=off), so the difference between the placeholder and the series construction
(rows 96 to 98: sheep wool, dairy milk, cattle meat; the X054 offset) cancels. Also writes base_window (equal to the base matrix), which the check in monte_carlo.mjs requires,
and check_meat_3y and check_meat_early (the same method on the short windows, to compare with a direct build).
Inputs: OFF_DIR from rebuild_off.py (needs the ABS files of analysis/recent_data/fetch_recent.py), data/2025/yield_matrix_livestock.csv.
Why not a direct build: data/2025/livestock_national_series.csv has no wool, cattle-on-feed or state milk figures for 2005-06 to 2019-20, so livestock_zone.py with the series
  cannot make the full-cycle windows. With this method rows 95 and 99 to 103 equal a direct build; in rows 96 to 98 the change between windows follows the flock and herds, not the series
  (on the two short windows: within 1.6% of a direct build for wool and cattle meat, 6.5% for milk).
Usage (repository root): python3 -I analysis/sensitivity_2025/make_win.py OFF_DIR WIN_DIR      then MC_WIN_DIR=WIN_DIR node analysis/sensitivity_2025/monte_carlo.mjs WORK_DIR OUT.csv 2000"""
import csv, os, sys
OFF, OUT = sys.argv[1:3]
def rd(p): rows = list(csv.reader(open(p))); return rows[0], {r[0]: r for r in rows[1:]}
head, base = rd('data/2025/yield_matrix_livestock.csv'); _, boff = rd(f'{OFF}/base_off/yield_matrix_livestock.csv')
def write(vid, m):
    os.makedirs(f'{OUT}/{vid}', exist_ok=True)
    with open(f'{OUT}/{vid}/yield_matrix_livestock.csv', 'w', newline='') as f: w = csv.writer(f); w.writerow(head); [w.writerow(m[z]) for z in base]
write('base_window', base)
for vid in ('meat_8y', 'meat_10y', 'meat_15y', 'meat_20y', 'meat_3y', 'meat_early'):
    _, win = rd(f'{OFF}/{vid}/yield_matrix_livestock.csv'); m = {}
    for z, row in base.items():
        m[z] = [row[0]] + [b if w == o else repr(round(float(b) + float(w) - float(o), 6)) for b, w, o in zip(row[1:], win[z][1:], boff[z][1:])]
    write('check_' + vid if vid in ('meat_3y', 'meat_early') else vid, m)
print('wrote', OUT)
