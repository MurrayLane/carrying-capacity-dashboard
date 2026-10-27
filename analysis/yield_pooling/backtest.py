#!/usr/bin/env python3
"""E9 back-test: does pooling a thin region's yield toward its state beat the plain mean of the region's own years?

Usage: python3 -I analysis/yield_pooling/backtest.py          (from the repository root; writes analysis/yield_pooling/backtest.csv)

Data: the five ABS crop years 2016-17 to 2020-21 for the 55 NRM regions (data/abs-2016-21; the 2011 zones are built from NRM regions, so these are the same kind of unit), stage 1 of the
yield method (yields.crop_year, 10 ha and 10 t minimum, the ABS unreliable cells removed, seed deducted) and the plausibility rules of zone_yields.py (a regional yield over 3 or under 0.1 times
the national yield of the year is removed).
Test: hold out one year; estimate each region's relative yield for that year from the other years; compare with what the region actually yielded.
  relative yield  rho = region yield / national yield of the same year (this takes the weather of the year out; both estimators estimate the same thing)
  current         mean of the region's rho in the other years (the plain mean the 2025 matrix uses, expressed as a ratio)
  pooled          weight w on that mean and 1 - w on the prior: the mean of log rho of the other regions of the same state (the national figure, 1, if fewer than two other regions have the crop).
                  w = n a / (n a + k), n the number of other years the region has, a its mean reported area (ha); k = 0 is the current estimator.
Error: |log(estimate / actual)|, so a 2-fold miss either way scores 0.69. Reported unweighted (every region-crop-year the same: the thin regions count) and weighted by the actual area
(what the capacity calculation feels). k is chosen on the held-out years 2016-17 to 2018-19 and judged on 2019-20 and 2020-21, which played no part in the choice.
"""
import csv, json, math, os, sys, statistics
ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, 'pipeline', 'yields'))
import yields
YEARS = ('2016-17', '2017-18', '2018-19', '2019-20', '2020-21')
regs = json.load(open(os.path.join(ROOT, 'data/abs-2016-21/regions.json')))['regions']
NRM = [(r['column'], r['code'] // 100) for r in regs if r['kind'] == 'nrm']                  # (column, state)
crops = json.load(open(os.path.join(ROOT, 'pipeline/yields/abs_current/model_crops.json')))['crops']
CAP, FLOOR = 3.0, 0.1

def load(year):
    d = json.load(open(os.path.join(ROOT, f'data/abs-2016-21/cube_{year}.json')))
    cube = {yields.norm(l): v for l, v in d['rows'].items()}; bad = {(yields.norm(l), c) for l, c in d['unreliable']}
    return cube, bad
data = {}                                                          # crop -> year -> {col: (yield, area_ha)}
for y in YEARS:
    cube, bad = load(y)
    for c in crops:
        v = yields.crop_year(cube, c, deleted=bad, thresholds=True)
        if v is None: continue
        area = cube.get(yields.norm(c + ' (ha)')) or cube.get(yields.norm(c + ' trees (n)'))
        nat = v[1]
        if not nat or nat <= 0: continue
        for col, _ in NRM:
            if v[col] is None or v[col] <= 0 or v[col] > CAP * nat or v[col] < FLOOR * nat: continue
            data.setdefault(c, {}).setdefault(y, {})[col] = (v[col] / nat, (area[col] if area and area[col] else 0.0))
state_of = dict(NRM)

def estimate(c, col, others, k):
    """Estimated log rho of region `col` for crop c from the years `others`."""
    obs = [(data[c][s][col]) for s in others if col in data[c].get(s, {})]
    if not obs: return None
    own = statistics.mean(math.log(r) for r, _ in obs); a = statistics.mean(x for _, x in obs); n = len(obs)
    peers = []
    for col2, st in NRM:
        if col2 == col or st != state_of[col]: continue
        o2 = [math.log(data[c][s][col2][0]) for s in others if col2 in data[c].get(s, {})]
        if o2: peers.append(statistics.mean(o2))
    prior = statistics.mean(peers) if len(peers) >= 2 else 0.0
    w = 1.0 if k == 0 else n * a / (n * a + k)
    return w * own + (1 - w) * prior

def score(held, k):
    errs, wts = [], []
    for c in data:
        for t in held:
            for col, (rho, area) in data[c].get(t, {}).items():
                est = estimate(c, col, [s for s in YEARS if s != t], k)
                if est is None: continue
                errs.append(abs(est - math.log(rho))); wts.append(area)
    sw = sum(wts)
    return len(errs), statistics.mean(errs), statistics.median(errs), (sum(e * w for e, w in zip(errs, wts)) / sw if sw else float('nan')), sum(e > math.log(2) for e in errs) / len(errs)

KS = [0, 10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000]
train, test = YEARS[:3], YEARS[3:]
rows = [['k_ha_years', 'set', 'n', 'mean_abs_log_error', 'median_abs_log_error', 'area_weighted_mean_abs_log_error', 'share_over_2fold']]
print(f'{"k":>8s} | train: n  mean  median  weighted  >2x   | test: n  mean  median  weighted  >2x')
for k in KS:
    a, b = score(train, k), score(test, k)
    rows += [[k, 'train'] + [round(x, 4) if isinstance(x, float) else x for x in a], [k, 'test'] + [round(x, 4) if isinstance(x, float) else x for x in b]]
    print(f'{k:8d} | {a[0]:6d} {a[1]:.3f} {a[2]:.3f} {a[3]:.3f} {a[4]:.3f} | {b[0]:6d} {b[1]:.3f} {b[2]:.3f} {b[3]:.3f} {b[4]:.3f}')
best = min(KS, key=lambda k: score(train, k)[1])
print('k chosen on the training years (lowest mean error):', best)
with open(os.path.join(ROOT, 'analysis/yield_pooling/backtest.csv'), 'w', newline='') as f: csv.writer(f).writerows(rows)

# ---- how much does a longer window help? plain mean of m of the other years, every combination of years --------------------------------------------------------------------
import itertools
print('\nplain mean (k = 0) of m other years: mean and median absolute log error, all combinations')
longer = [['m_years_used', 'n', 'mean_abs_log_error', 'median_abs_log_error', 'area_weighted_mean_abs_log_error']]
for m in (1, 2, 3, 4):
    errs, wts = [], []
    for c in data:
        for t in YEARS:
            for col, (rho, area) in data[c].get(t, {}).items():
                for sub in itertools.combinations([s for s in YEARS if s != t], m):
                    est = estimate(c, col, sub, 0)
                    if est is None: continue
                    errs.append(abs(est - math.log(rho))); wts.append(area)
    row = [m, len(errs), round(statistics.mean(errs), 4), round(statistics.median(errs), 4), round(sum(e * w for e, w in zip(errs, wts)) / sum(wts), 4)]
    longer.append(row); print(f'm = {m}: n {row[1]:6d}  mean {row[2]:.3f}  median {row[3]:.3f}  weighted {row[4]:.3f}')
with open(os.path.join(ROOT, 'analysis/yield_pooling/backtest_window.csv'), 'w', newline='') as f: csv.writer(f).writerows(longer)
