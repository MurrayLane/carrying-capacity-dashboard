#!/usr/bin/env python3
"""B115 (decision 108): the widened Monte Carlo on the corrected 2025 release, national: ranges and first-order and total-order indices.

Usage (from the repository root):
  MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 MC_ZONES=national node analysis/sensitivity_2025/monte_carlo.mjs WORK_DIR PART_k.csv sobol 2000 k 4     (k = 0 to 3; WORK_DIR as for monte_carlo.mjs)
  python3 analysis/sensitivity_2025/sobol_wide.py PART_0.csv PART_1.csv PART_2.csv PART_3.csv
Writes
  analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv   every run of the design (block A, B or AB_<choice>; i; the 19 choices; Australia short and long), sorted by i
  results/ranges_2025-fixed_wide.csv                               5th to 95th percentiles, min, max and the two ratios from block A (2,000 Latin hypercube draws of 19 choices),
                                                                   with the same figures for the existing 13-choice draws (monte_carlo_draws_2025-fixed_all.csv, 1,000 draws) beside them
  analysis/sensitivity_2025/sobol_2025-fixed.csv                   first-order and total-order indices of each choice, with bootstrap intervals
  analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md          the same as tables
Estimators (Saltelli et al. 2010, Computer Physics Communications 181: 259-270; Jansen 1999): with A and B two independent Latin hypercubes of N rows and AB_j the matrix A
with column j taken from B, V the variance of f over A and B together,
  first order  S_j  = mean( (f(B) - m) (f(AB_j) - f(A)) ) / V      (m the mean of f over A and B: the same in expectation as Saltelli's form with f(B) uncentred,
                                                                    and far less noisy when the output sits far from zero, as a capacity in people does)
  total order  ST_j = mean( (f(A) - f(AB_j))^2 ) / (2 V)
Intervals: 2.5th and 97.5th percentiles of 1,000 bootstrap resamples of the N draw indices (seed 20261118). The binned first-order estimate of summarise_mc.py
(20 equal-count bins, 3 or fewer values grouped, binning noise taken off) is given from block A as a check.
Deterministic: the design comes from monte_carlo.mjs's fixed seed and the bootstrap from a fixed seed.
"""
import csv, statistics, sys
import numpy as np
ROOT_MC = 'analysis/sensitivity_2025/'
parts = sys.argv[1:]
rows = [r for p in parts for r in csv.DictReader(open(p))]
NAMES = [c for c in rows[0] if c not in ('block', 'i') and not c[0].isdigit()]
OUTS = [c for c in rows[0] if c[0].isdigit()]
rows.sort(key=lambda r: (int(r['i']), ['A', 'B'].index(r['block']) if r['block'] in ('A', 'B') else 2 + NAMES.index(r['block'][3:])))
N = max(int(r['i']) for r in rows) + 1
assert len(rows) == N * (len(NAMES) + 2), f'{len(rows)} runs, expected {N * (len(NAMES) + 2)}'
assert all(r['i'] == str(k // (len(NAMES) + 2)) for k, r in enumerate(rows)), 'a run is missing or repeated'
with open(ROOT_MC + 'monte_carlo_draws_2025-fixed_wide.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

INFO = {   # choice: (description, distribution, source of the range)
 'sf': ('field-crop group factor', 'uniform, 14% below to 14% above the factor', 'the measured error of the group-trend rule (sensitivity README)'),
 'sh': ('vegetable, fruit and nut factors', 'uniform, 20% below to 20% above', 'the measured error of the group-trend rule (20 to 22%)'),
 'meat': ('window of herd and meat data', 'one of 2020-21 to 2024-25 (base), 2020-21 to 2022-23, 2022-23 to 2024-25, equal chances', 'author judgement (equal chances)'),
 'meategg': ('meat and egg share of the diet', 'triangular 0.115, 0.12, 0.13', 'FAO food balance proxy and the 2011 value; low end author judgement'),
 'redmeat': ('red meat share of the diet', 'triangular 0.528, 0.578, 0.64', 'FAO food balance proxy and the 2011 value; low end author judgement'),
 'fuel': ('liquid fuel per person', 'uniform 2,360 to 2,520 L', 'proxy and 2011 value (Australian Petroleum Statistics)'),
 'biofuel': ('biofuel share', 'uniform 0.23% to 0.5%', 'proxy and 2011 value'),
 'timber': ('timber per person', 'uniform 0.8 to 1.0 m3', 'proxy and 2011 value (FAO forestry)'),
 'orgfac': ('default organic yield factor', 'uniform 0.771 to 0.845', 'Ponisio et al. 2015'),
 'orgshare': ('organic share of land (default and baseline)', 'triangular 0.02, 0.07, 0.12', '2011 value, proxy, Australian Organic Market Report 2026'),
 'restable': ('resilience table (all years or leave-one-out)', 'one of the two, equal chances', 'author judgement (equal chances)'),
 'lfuel': ('long-term liquid fuel', 'triangular 156, 210, 253 L', 'light vehicles electrified, the re-derivation, the thesis'),
 'lbench': ('long-term feeding benchmark', 'triangular 0.30 to 0.525', 'South Korea and Japan; no effect in this release'),
 'waste': ('avoidable waste, short term', 'uniform 12% to 14%', 'analysis/waste_2025/README.md: FIAL 2021 baseline (312 kg a person, 58% at retail and consumer stages, 70% edible) over the FAO supply'),
 'lossaus': ('retail and consumer loss factors, US to Australian', 'uniform weight 0 to 1 between the thesis factors and methods/loss-factors-australia', 'Buzby 2010 and Muth 2011 (US); FIAL 2021 Table 5 and the Burnside bin audit 2022 (Australia)'),
 'land': ('source of cropping and pasture areas', 'ABS holdings or ABARES land-use raster, equal chances', 'the two sources (sensitivity README); equal chances author judgement'),
 'meatcal': ('calibration of the ABS meat tables', 'uniform 0 to 1 between the ABS tables as published and the archive 2010 level (cattle x1.086, sheep x1.155)', 'ABS Livestock Products 7215.0 and the thesis archive (archive above ABS in every year 2006 to 2010)'),
 'energy': ('energy requirement per person, short term', 'uniform food amount 1.000 to 1.286 (PAL 1.4 to 1.8)', 'NHMRC Nutrient Reference Values, dietary energy, Tables 3 and 4 (sedentary to moderate activity)'),
 'trendwin': ('window of the field-crop group trend', 'uniform between the 2022-25 factor (1.356) and the 2016-21 factor (1.289)', 'data/abs-2022-25/group_trend.json (SCOPE.md B10 rule on two windows)'),
}
def pct(v, q):
    s = sorted(v); i = q * (len(s) - 1); lo = int(i); hi = min(lo + 1, len(s) - 1); return s[lo] + (s[hi] - s[lo]) * (i - lo)
def first_order_binned(x, y):     # as summarise_mc.py
    var = statistics.pvariance(y)
    if var == 0: return 0.0
    if len(set(x)) <= 3: groups = [[i for i in range(len(y)) if x[i] == v] for v in sorted(set(x))]
    else:
        order = sorted(range(len(y)), key=lambda i: x[i]); groups = [order[g * len(y) // 20:(g + 1) * len(y) // 20] for g in range(20)]
    m = statistics.mean(y); raw = sum(len(g) * (statistics.mean(y[i] for i in g) - m) ** 2 for g in groups if g) / (len(y) * var)
    return max(0.0, raw - (len(groups) - 1) / (len(y) - 1))
base = {}
for r in csv.DictReader(open('results/2025-fixed.csv')):
    if r['zone'] == '1': base[r['preset']] = float(r['capacity'])
blk = lambda b: [r for r in rows if r['block'] == b]
A, B = blk('A'), blk('B')
old = list(csv.DictReader(open(ROOT_MC + 'monte_carlo_draws_2025-fixed_all.csv')))
rng_rows = [['variant', 'choices', 'draws', 'zone', 'setting', 'p5', 'p25', 'p50', 'p75', 'p95', 'min', 'max', 'base', 'ratio_p95_p5', 'ratio_max_min'] + ['influence_' + k for k in NAMES]]
for k in ('short', 'long'):
    for variant, draws, nch in (('wide', A, len(NAMES)), ('existing', old, 13)):
        y = [float(r[f'1_{k}']) for r in draws]
        q = [pct(y, p) for p in (.05, .25, .5, .75, .95)]
        inf = [round(first_order_binned([float(r[n]) for r in draws], y), 3) if n in draws[0] else '' for n in NAMES]
        rng_rows.append([variant, nch, len(draws), 1, k] + [round(v) for v in q] + [round(min(y)), round(max(y)), round(base[k]), round(q[4] / q[0], 3), round(max(y) / min(y), 3)] + inf)
with open('results/ranges_2025-fixed_wide.csv', 'w', newline='') as f: csv.writer(f).writerows(rng_rows)

rng = np.random.default_rng(20261118); BOOT = 1000
idx = rng.integers(0, N, size=(BOOT, N))
sob = [['setting', 'choice', 'description', 'distribution', 'source_of_range', 'first_order', 'first_order_ci_low', 'first_order_ci_high', 'total_order', 'total_order_ci_low', 'total_order_ci_high', 'first_order_binned']]
S = {}
for k in ('short', 'long'):
    fA = np.array([float(r[f'1_{k}']) for r in A]); fB = np.array([float(r[f'1_{k}']) for r in B])
    V = np.var(np.concatenate([fA, fB])); Vb = np.var(np.concatenate([fA[idx], fB[idx]], axis=1), axis=1)
    for n in NAMES:
        fAB = np.array([float(r[f'1_{k}']) for r in blk('AB_' + n)])
        f0 = np.mean(np.concatenate([fA, fB])); f0b = np.mean(np.concatenate([fA[idx], fB[idx]], axis=1), axis=1)[:, None]
        s1 = np.mean((fB - f0) * (fAB - fA)) / V; st = np.mean((fA - fAB) ** 2) / (2 * V)
        s1b = np.mean((fB[idx] - f0b) * (fAB[idx] - fA[idx]), axis=1) / Vb; stb = np.mean((fA[idx] - fAB[idx]) ** 2, axis=1) / (2 * Vb)
        binned = first_order_binned([float(r[n]) for r in A], list(fA))
        S[(k, n)] = (s1, st)
        sob.append([k, n, *INFO[n]] + [round(float(v), 4) for v in (s1, np.percentile(s1b, 2.5), np.percentile(s1b, 97.5), st, np.percentile(stb, 2.5), np.percentile(stb, 97.5))] + [round(binned, 4)])
with open(ROOT_MC + 'sobol_2025-fixed.csv', 'w', newline='') as f: csv.writer(f).writerows(sob)

R = {(r[0], r[4]): r for r in rng_rows[1:]}
m = lambda v: f'{v / 1e6:.1f}'
md = [f'# The widened Monte Carlo, corrected 2025 release, Australia (B115, decision 108)', '',
      f'{N} Latin hypercube draws of {len(NAMES)} choices (block A of the design), and {N * (len(NAMES) + 2):,} runs in all for the indices. Millions of people.', '',
      '| | Short term | Long term |', '|---|---|---|']
for v, lab in (('existing', 'Existing 13 choices, 1,000 draws'), ('wide', f'Widened, {len(NAMES)} choices, {N:,} draws')):
    s, l = R[(v, 'short')], R[(v, 'long')]
    md.append(f'| {lab}: 5th to 95th percentile | {m(s[5])} to {m(s[9])} (ratio {s[13]:.2f}) | {m(l[5])} to {m(l[9])} (ratio {l[13]:.2f}) |')
    md.append(f'| {lab}: min to max | {m(s[10])} to {m(s[11])} (ratio {s[14]:.2f}) | {m(l[10])} to {m(l[11])} (ratio {l[14]:.2f}) |')
    md.append(f'| {lab}: median | {m(s[7])} | {m(l[7])} |')
md += [f'| Base (the release) | {m(base["short"])} | {m(base["long"])} |', '', 'Share of the variance (first order: the choice alone; total order: the choice with all its interactions); 95% bootstrap interval in brackets.', '',
       '| Choice | Short: first order | Short: total order | Long: first order | Long: total order |', '|---|---|---|---|---|']
SB = {(r[0], r[1]): r for r in sob[1:]}
for n in sorted(NAMES, key=lambda n: -max(S[('short', n)][1], S[('long', n)][1])):
    c = lambda k, j: f'{100 * SB[(k, n)][j]:.1f}% ({100 * SB[(k, n)][j + 1]:.1f} to {100 * SB[(k, n)][j + 2]:.1f})'
    md.append(f'| {INFO[n][0]} | {c("short", 5)} | {c("short", 8)} | {c("long", 5)} | {c("long", 8)} |')
for k in ('short', 'long'):
    md.append('')
    md.append(f'{k.capitalize()} term: the first-order indices add to {100 * sum(S[(k, n)][0] for n in NAMES):.0f}% and the total-order indices to {100 * sum(S[(k, n)][1] for n in NAMES):.0f}%.')
open(ROOT_MC + 'monte_carlo_2025-fixed_wide.md', 'w').write('\n'.join(md) + '\n'); print('\n'.join(md))
