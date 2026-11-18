#!/usr/bin/env python3
"""B137 item 5: the national drought factor under variants of the record, with resilience.py's own functions (imported, not edited, nothing of its outputs rewritten).
Usage (repository root): python3 -I analysis/resilience_2025/resilience_variants.py HISTORIC_XLSX ABS_LIVESTOCK_DIR [ARCHIVE_XLS]
  HISTORIC_XLSX       'Historic Ag Commodities_1860 to 2022.xlsx' (as for resilience.py); the 2022-23 to 2024-25 cubes are read from data/abs-2022-25 by resilience.py
  ABS_LIVESTOCK_DIR   the folder holding 7215009.xlsx to 7215012.xlsx (ABS Livestock Products, monthly cattle and sheep meat, as read by pipeline/yields/recent/livestock_zone.py); used for the observed livestock-output ratio
  ARCHIVE_XLS         optional, default 'carrying-capacity-models/prelim models/resilience 150 years.xls' beside the repository (resilience.py needs it at import; it is not otherwise used)
Writes analysis/resilience_2025/drought_factor_variants.csv and analysis/resilience_2025/livestock_output_ratio.csv.
Variants (national, thesis reference and ranking as resilience.py): series = the unweighted mean of the wheat, oats and barley yields (the model's table) or the area-weighted yield (total tonnes over total hectares of the three grains);
start = the first season used (the whole record from 1861; 1950-51; 1970-71; 1990-91, 35 seasons). The reference window and the ranking are rebuilt from the first season used.
A factor at return period T is the ratio at rank round((n + 1) / T) of the n ratios. 'supported' says whether the record allows it: rank at least 3 for 1 in 10 and 1 in 20 (the 35-season record has rank 2 at 1 in 20);
1 in 100 is read, as in the model's table, from the 50 and 150 year anchors and is reported as supported only when n + 1 >= 150 (both anchors then have different ranks).
Capacity: short term, Australia, 2025-fixed (41.5 million in a mean year), with the factor on all output (the model's rule) and on crop output only (the bounds of drought_bounds.mjs), by drought_factor_variants_eval.mjs."""
import csv, importlib.util, os, statistics, subprocess, sys, tempfile, datetime
sys.dont_write_bytecode = True
HIST = sys.argv[1]; LIVE = sys.argv[2]
ARCH = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(os.getcwd()), 'carrying-capacity-models', 'prelim models', 'resilience 150 years.xls')
sys.argv = ['resilience.py', ARCH, HIST]
spec = importlib.util.spec_from_file_location('resilience', 'analysis/resilience_2025/resilience.py'); R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)

def historic_with_area():
    h = R.historic(); h.update(R.recent_cubes()); return h
H = historic_with_area()
years = sorted({y for (_, _, y) in H})
def series(weighted):
    out = {}
    for y in years:
        ys, ha, t = [], 0.0, 0.0; ok = True
        for crop in ('wheat', 'oats', 'barley'):
            d = H.get(('Australia', crop, y))
            if d and d.get('hectares', 0) > 0 and d.get('tonnes') is not None: ys.append(d['tonnes'] / d['hectares']); ha += d['hectares']; t += d['tonnes']
            else: ok = False
        if ok: out[y] = (t / ha) if weighted else statistics.mean(ys)          # all three grains needed, as in resilience.py
    return out
def factors(y):
    r = R.thesis_ratios(y); n = len(r); srt = sorted(r); res = {}
    for T in (10, 20):
        rank = max(1, min(n, round((n + 1) / T))); res[T] = (srt[rank - 1], rank, rank >= 3)
    a = R.anchors_rank(r); tab = R.interp(a); res[100] = (tab[99], f'interpolated, anchors at ranks {max(1, min(n, round((n + 1) / 50)))} and {max(1, min(n, round((n + 1) / 150)))}', n + 1 >= 150)
    return res, n
# check against the model's own table (data to 2024-25, Australia)
base_tab = {r['location']: r for r in csv.DictReader(open('analysis/resilience_2025/tables.csv')) if r['method'] == 'data: ABS to 2024-25'}['Australia']
ser_u = series(False); fu, nu = factors([ser_u[y] for y in sorted(ser_u)])
for T in (10, 20, 100):
    if abs(fu[T][0] - float(base_tab[str(T)])) > 1e-5: sys.exit(f'CHECK FAILED: full-record unweighted factor at {T} years {fu[T][0]:.6f} != tables.csv {base_tab[str(T)]}')
START = [(1861, 'whole record'), (1951, 'from 1950-51'), (1971, 'from 1970-71'), (1991, 'from 1990-91')]
rows, flist = [], []
for weighted in (False, True):
    s = series(weighted)
    for first, lab in START:
        ys = sorted(y for y in s if y >= first); f, n = factors([s[y] for y in ys])
        for T in (10, 20, 100):
            v, rk, sup = f[T]; rows.append(dict(series='area-weighted yield' if weighted else 'unweighted mean of grain yields (the model table)', start=lab, first_season=ys[0], last_season=ys[-1], seasons=n, return_period=T, factor=round(v, 4), rank_or_anchors=rk, supported='yes' if sup else 'no', _v=v))
mean_cap = None
with tempfile.TemporaryDirectory() as td:
    fi, fo = os.path.join(td, 'f.csv'), os.path.join(td, 'o.csv')
    csv.writer(open(fi, 'w', newline='')).writerows([['factor']] + [[r['_v']] for r in rows])
    p = subprocess.run(['node', 'analysis/resilience_2025/drought_factor_variants_eval.mjs', fi, fo], capture_output=True, text=True, check=True); print(p.stdout.strip())
    caps = list(csv.DictReader(open(fo)))
for r, c in zip(rows, caps):
    r['capacity_all_output'] = c['capacity_all_output']; r['capacity_crop_only'] = c['capacity_crop_only']
    r['capacity_all_output_million'] = f"{int(c['capacity_all_output']) / 1e6:.2f}"; r['capacity_crop_only_million'] = f"{int(c['capacity_crop_only']) / 1e6:.2f}"
cols = ['series', 'start', 'first_season', 'last_season', 'seasons', 'return_period', 'factor', 'rank_or_anchors', 'supported', 'capacity_all_output', 'capacity_all_output_million', 'capacity_crop_only', 'capacity_crop_only_million']
with open('analysis/resilience_2025/drought_factor_variants.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, cols, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
# observed livestock output: national red meat (cattle and calves plus sheep and lambs), tonnes in each year to June, 7215009 to 7215012 (livestock_zone.py's own reading), ratio to the reference of the same method
import openpyxl
def monthly(file):
    ws = openpyxl.load_workbook(os.path.join(LIVE, file), read_only=True, data_only=True)['Data1']; out = {}
    for row in ws.iter_rows(min_row=11, values_only=True):
        if isinstance(row[0], datetime.datetime) and isinstance(row[1], (int, float)): out[row[0]] = row[1]
    return out
ds = [monthly(f) for f in ('7215009.xlsx', '7215010.xlsx', '7215011.xlsx', '7215012.xlsx')]
def fy(d, y): return [v for dt, v in d.items() if datetime.datetime(y - 1, 7, 1) <= dt <= datetime.datetime(y, 6, 30)]
tot = {}
for y in range(1973, 2026):                                  # the tables are quarterly (September, December, March, June): four values make a complete year to June; 1973 to 2025 (the model's record ends in 2024-25)
    parts = [fy(d, y) for d in ds]
    if all(len(p) == 4 for p in parts): tot[y] = sum(sum(p) for p in parts)
w = csv.writer(open('analysis/resilience_2025/livestock_output_ratio.csv', 'w', newline='')); w.writerow(['record', 'year_to_june', 'red_meat_tonnes', 'ratio_to_reference', 'rank_from_worst_in_record'])
worst = {}
for rec, first in (('1973 to 2025 (all complete years)', 1973), ('2005 to 2025 (the 21 years of R05a)', 2005)):
    ys = sorted(y for y in tot if y >= first); ratios = R.thesis_ratios([tot[y] for y in ys]); order = sorted(range(len(ys)), key=lambda i: ratios[i])
    for i, y in enumerate(ys): w.writerow([rec, y, round(tot[y]), round(ratios[i], 4), order.index(i) + 1])
    worst[rec] = (len(ys), [(ys[i], round(ratios[i], 3)) for i in order[:4]])
    print('livestock output ratio', rec, len(ys), 'years; four worst', worst[rec][1])
if [y for y, _ in worst['2005 to 2025 (the 21 years of R05a)'][1][:2]] != [2022, 2021]: sys.exit('CHECK FAILED: the worst two years of 2005-2025 are not 2021-22 and 2020-21 (R05a)')
for r in rows:
    if r['return_period'] != 100 or r['supported'] == 'yes': print(r['series'][:12], r['start'], r['seasons'], r['return_period'], r['factor'], r['supported'], r['capacity_all_output_million'], r['capacity_crop_only_million'])
