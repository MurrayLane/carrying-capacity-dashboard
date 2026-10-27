#!/usr/bin/env python3
"""The resilience (climate variability) table of the model: the thesis method reproduced from the archive, then run on data to 2024-25 and with a fitted tail.

Usage: python3 -I analysis/resilience_2025/resilience.py ARCHIVE_XLS HISTORIC_XLSX          (run from the repository root)
  ARCHIVE_XLS    'prelim models/resilience 150 years.xls' of the models archive (the thesis workings)
  HISTORIC_XLSX  'Historic Ag Commodities_1860 to 2022.xlsx', ABS Agricultural Commodities 2021-22 (successor of ABS 7124.0)
Writes analysis/resilience_2025/tables.csv (location, method, years 1 to 150), anchors.csv and replication.txt.

The thesis method (thesis chapter 8, Figure 34; the archive workbook), as reproduced here:
  series      for each location and year, the unweighted mean of the yields (t/ha) of wheat, oats and barley (a crop with no area counts as a yield of 0)
  reference   the mean of the 10 observations from 5 before to 4 after the year (observations, not calendar years: the early years are 1861, 1866, 1871, then annual), the window held at
              the first or last 10 observations at the ends
  ratio       yield / reference
  return      the n ratios ranked from worst; rank k is the event of return period (n + 1) / k years
  anchors     for the return period T in 1, 3, 5, 10, 20, 30, 50, 150: the ratio at rank round((n + 1) / T) (1 for T = 1); every other year of the table is read by straight-line interpolation
              between anchors (the 100-year value is the midpoint of the 50- and 150-year anchors)
Alternatives (SCOPE.md E14), each a change from the thesis method alone:
  'data'   the thesis method on the ABS series to 2021-22 and the ABS 2022-23 to 2024-25 cubes
  'loo'    reference = mean of the 20 other observations nearest in time (10 either side, the year itself left out), which a very bad year cannot pull down
  'gpd'    like 'loo', with the lower tail beyond the 20th percentile fitted by a generalised Pareto distribution instead of read from ranks; bootstrap interval from 500 resamples of years
"""
import csv, json, math, os, random, statistics, sys
import openpyxl, xlrd
ROOT = os.getcwd(); ARCH, HIST = sys.argv[1], sys.argv[2]
LOC = ['Australia', 'New South Wales', 'Victoria', 'Queensland', 'South Australia', 'Western Australia', 'Tasmania']
ANCH = [1, 3, 5, 10, 20, 30, 50, 150]

# ---- data --------------------------------------------------------------------------------------------------------------------------------------------------
def archive_series():
    s = xlrd.open_workbook(ARCH).sheet_by_name('commodities'); yrs = [int(v) for v in s.row_values(2)[1:] if v != '']; n = len(yrs)
    return yrs, {loc: s.row_values(3 + 3 * i)[1:1 + n] for i, loc in enumerate(LOC)}, {loc: s.row_values(5 + 3 * i)[1:1 + n] for i, loc in enumerate(LOC)}
def historic():
    wb = openpyxl.load_workbook(HIST, read_only=True, data_only=True); out = {}
    for tab, crop in (('Table 4', 'wheat'), ('Table 3', 'oats'), ('Table 1', 'barley')):
        rows = list(wb[tab].iter_rows(values_only=True)); years = [int(v) for v in rows[4][2:] if v not in (None, '')]; reg = None
        for r in rows[5:]:
            if r[0] not in (None, ''): reg = str(r[0]).strip()
            if reg and r[1] in ('hectares', 'tonnes'):
                for y, v in zip(years, r[2:2 + len(years)]):
                    if isinstance(v, (int, float)): out.setdefault((reg, crop, y), {})[r[1]] = float(v)
    return out
def recent_cubes():
    """2022-23 to 2024-25 (year labels 2023 to 2025): state columns of the ABS cubes (NSW with the ACT)."""
    cols = {'Australia': [1], 'New South Wales': [2, 9], 'Victoria': [3], 'Queensland': [4], 'South Australia': [5], 'Western Australia': [6], 'Tasmania': [7]}; out = {}
    for y, lab in ((2023, '2022-23'), (2024, '2023-24'), (2025, '2024-25')):
        rows = json.load(open(os.path.join(ROOT, f'data/abs-2022-25/cube_{lab}.json')))['rows']
        for loc, cs in cols.items():
            for crop, name in (('wheat', 'Wheat'), ('oats', 'Oats'), ('barley', 'Barley')):
                ha, t = rows.get(f'{name} (ha)'), rows.get(f'{name} (t)')
                if ha and t: out[(loc, crop, y)] = {'hectares': sum(ha[c] or 0 for c in cs), 'tonnes': sum(t[c] or 0 for c in cs)}
    return out
def series_from_abs(extra=True, zero_for_missing=False):
    """Mean yield of the three grains per location and year. The ABS series (to 2022) and the recent cubes; NSW is NSW with the ACT in the cubes and NSW alone in the historic series (the ACT grows almost no grain)."""
    h = historic()
    if extra: h.update(recent_cubes())
    years = sorted({y for (_, _, y) in h}); res = {}
    for loc in LOC:
        res[loc] = {}
        for y in years:
            ys = []
            for crop in ('wheat', 'oats', 'barley'):
                d = h.get((loc, crop, y))
                if d and d.get('hectares', 0) > 0 and d.get('tonnes') is not None: ys.append(d['tonnes'] / d['hectares'])
                elif zero_for_missing: ys.append(0.0)
            if len(ys) == (3 if zero_for_missing else 3): res[loc][y] = statistics.mean(ys)           # all three grains needed, as in the thesis (which counted an unplanted grain as 0)
    return res

# ---- method ------------------------------------------------------------------------------------------------------------------------------------------------
def thesis_ratios(y):
    n = len(y); ref = [statistics.mean(y[max(0, min(n - 10, i - 5)):max(0, min(n - 10, i - 5)) + 10]) for i in range(n)]
    return [a / b for a, b in zip(y, ref)]
def loo_ratios(y):
    """Reference from the 20 other observations nearest in time (10 either side where there are that many)."""
    n = len(y); out = []
    for i in range(n):
        lo, hi = max(0, min(n - 21, i - 10)), None
        w = [y[j] for j in range(lo, lo + 21) if j != i] if n > 21 else [v for j, v in enumerate(y) if j != i]
        out.append(y[i] / statistics.mean(w))
    return out
def anchors_rank(r):
    n = len(r); srt = sorted(r); a = {1: 1.0}
    for T in ANCH[1:]: a[T] = srt[max(1, min(n, round((n + 1) / T))) - 1]
    return a
def interp(a):
    pts = [(T, a[T]) for T in ANCH]; out = []
    for t in range(1, 151):
        for (t0, v0), (t1, v1) in zip(pts, pts[1:]):
            if t0 <= t <= t1: out.append(v0 + (v1 - v0) * (t - t0) / (t1 - t0)); break
    return out
def gpd_fit(exc):
    """Generalised Pareto (shape xi, scale sigma) by probability-weighted moments, for exceedances over the threshold."""
    n = len(exc); x = sorted(exc); b0 = statistics.mean(x); b1 = sum(((n - 1 - i) / (n - 1)) * x[i] for i in range(n)) / n          # alpha0 and alpha1 = E[X (1 - F)]
    xi = 2 - b0 / (b0 - 2 * b1); sigma = 2 * b0 * b1 / (b0 - 2 * b1)
    return max(-0.5, min(0.5, xi)), sigma
def anchors_gpd(r, q=0.2):
    n = len(r); srt = sorted(r); k = max(10, int(q * n)); thr = srt[k]                 # the k worst ratios lie below the threshold
    exc = [thr - v for v in srt[:k]]; xi, sigma = gpd_fit(exc); a = {1: 1.0}
    for T in ANCH[1:]:
        p = 1 / T                                                                       # probability of a year this bad
        if p >= k / n: a[T] = srt[max(1, min(n, round((n + 1) / T))) - 1]; continue
        z = (p / (k / n)) ** (-xi) if xi else None
        d = (sigma / xi) * ((p / (k / n)) ** (-xi) - 1) if xi else -sigma * math.log(p / (k / n))
        a[T] = max(0.02, thr - d)                                                         # shortfall below the threshold at probability p
    return a

if __name__ == '__main__':
    ayrs, ay, aratio = archive_series(); table = {}; rows = []
    log = []
    # 1. replication of the thesis table
    xl = xlrd.open_workbook(ARCH).sheet_by_name('years'); thesis = {str(xl.cell_value(r, 0)).strip(): [xl.cell_value(r, c) for c in range(1, 9)] for r in range(2, 9)}
    mx = 0.0
    for loc in LOC:
        r = thesis_ratios(ay[loc]); a = anchors_rank(r); mine = [a[T] for T in (150, 50, 30, 20, 10, 5, 3)] + [1.0]
        d = max(abs(m - t) for m, t in zip(mine, thesis[loc])); mx = max(mx, d); log.append(f'replication {loc}: largest difference from the thesis table {d:.2e}')
        table[(loc, 'thesis (archive data)')] = interp(a)
    log.append(f'ratios of the archive workbook reproduced: {max(abs(x - y) for x, y in zip(thesis_ratios(ay["Australia"]), aratio["Australia"])):.1e}')
    # 2. the same method on the ABS series (to 2021-22), then with the three recent years
    for label, extra in (('data: ABS to 2021-22', False), ('data: ABS to 2024-25', True)):
        s = series_from_abs(extra)
        for loc in LOC:
            yrs = sorted(s[loc]); y = [s[loc][t] for t in yrs]; table[(loc, label)] = interp(anchors_rank(thesis_ratios(y)))
            if extra and loc == 'Australia': log.append(f'ABS series 1861-2025: {len(y)} observations, Australia mean yield {statistics.mean(y):.2f} t/ha')
    # 3. improvements, on the series to 2024-25
    s = series_from_abs(True); boot = {}
    random.seed(20261027)
    for loc in LOC:
        yrs = sorted(s[loc]); y = [s[loc][t] for t in yrs]; r = loo_ratios(y)
        table[(loc, 'loo reference')] = interp(anchors_rank(r)); table[(loc, 'loo reference and fitted tail')] = interp(anchors_gpd(r))
        reps = []
        for _ in range(500):
            idx = sorted(random.randrange(len(r)) for _ in r); rr = [r[i] for i in idx]; reps.append(interp(anchors_gpd(rr)))
        for T in (10, 20, 50, 100, 150):
            vals = sorted(rep[T - 1] for rep in reps); boot[(loc, T)] = (vals[int(0.05 * 499)], vals[int(0.95 * 499)])
    # 4. storage: a population holding a stock of s years of grain is bound by the worst run of s+1 consecutive years, not by the single worst year
    stor = [['location', 'run_of_years', 'factor_at_20_years', 'factor_at_50_years', 'factor_at_100_years']]
    for loc in LOC:
        yrs = sorted(s[loc]); y = [s[loc][t] for t in yrs]; r = loo_ratios(y)
        for dlen in (1, 2, 3, 5):
            runs = [statistics.mean(r[i:i + dlen]) for i in range(len(r) - dlen + 1) if yrs[i + dlen - 1] - yrs[i] == dlen - 1]       # consecutive years only
            tab = interp(anchors_rank(runs)); stor.append([loc, dlen, round(tab[19], 4), round(tab[49], 4), round(tab[99], 4)])
    with open(os.path.join(ROOT, 'analysis/resilience_2025/storage.csv'), 'w', newline='') as f: csv.writer(f).writerows(stor)
    print('\nfactor at 100 years for the worst run of d consecutive years (loo reference), Australia:', {r[1]: r[4] for r in stor if r[0] == 'Australia'})
    with open(os.path.join(ROOT, 'analysis/resilience_2025/tables.csv'), 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['location', 'method'] + list(range(1, 151)))
        for (loc, m), v in table.items(): w.writerow([loc, m] + [round(x, 6) for x in v])
    with open(os.path.join(ROOT, 'analysis/resilience_2025/bootstrap.csv'), 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['location', 'years', 'p5', 'p95'])
        for (loc, T), (lo, hi) in boot.items(): w.writerow([loc, T, round(lo, 4), round(hi, 4)])
    open(os.path.join(ROOT, 'analysis/resilience_2025/replication.txt'), 'w').write('\n'.join(log) + '\n'); print('\n'.join(log))
    show = [1, 5, 10, 20, 50, 100, 150]
    print(f'\n{"Australia":38s}' + ''.join(f'{T:>7d}' for T in show))
    for (loc, m), v in table.items():
        if loc == 'Australia': print(f'{m:38s}' + ''.join(f'{v[T - 1]:7.3f}' for T in show))
    print('bootstrap 5-95% for the fitted tail, Australia:', {T: tuple(round(x, 3) for x in boot[("Australia", T)]) for T in (10, 50, 100, 150)})
