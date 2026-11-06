#!/usr/bin/env python3
"""Method test: the failure-probability view of carrying capacity (Fearnside 1985, 1990) applied to Australia.
Usage (repository root): python3 -I analysis/method_tests_2025/fearnside_failure_curve.py   (reads analysis/comparators_2025/rerun.csv; writes fearnside_failure_curve.csv)

Fearnside defines capacity not as one number but as a relation between population density and the probability of failure: a settler fails in a year when consumption falls below a minimum standard;
the failure probability at each density comes from repeated simulations with variable yields; capacity is the density at which that probability reaches a maximum acceptable level the planner chooses.
His deterministic (average-year) runs show no failure over the same densities where stochastic runs fail often: variability is what the average hides.

Applied here with the model: the variable is the weather, as the model already holds it: the drought allowance ('resilience') scales the harvest to the worst year expected once in T years, from the 150-year record of
wheat, oats and barley yields (`analysis/resilience_2025/`), so capacity at return period T is the population the model feeds in a year of failure probability 1/T. The failure criterion is the model's own: the harvest
cannot supply the default diet (energy, protein and the rest of the diet sheet, nutritionally adequate by construction). One criterion; the allowance scales every yield by one factor taken from the wheat, oats and barley record: Fearnside also tests total protein, animal protein and cash, and runs full simulations.
The curve is read between the model's run points T = 1 (average year), 5, 10, 20, 50 and 100; the population is the release's (2011 zones 22.33 million; 2025 27.61 million)."""
import csv, math
R = {}
for row in list(csv.reader(open('analysis/comparators_2025/rerun.csv')))[1:]:        # the variant name holds a comma, so read the last two fields as setting and capacity
    rel, variant, setting, cap = row[0], ','.join(row[1:-2]), row[-2], row[-1]
    if variant.startswith('R1'): R.setdefault(rel, {})[int(setting)] = float(cap)
POP = {'2011-fixed': 22.326388, '2011-improved': 22.326388, '2011-corrected': 22.326388, '2025-fixed': 27.6082, '2025-improved': 27.6082, '2025-mirror': 27.6082}
def return_period(curve, n, how):
    """the T at which capacity falls to n (million): interpolation between run points, linear in T or in log T"""
    pts = sorted(curve.items())
    if n >= pts[0][1]: return 1.0                                       # fails in an average year
    if n < pts[-1][1]: return None                                       # beyond the 100-year point
    for (t0, c0), (t1, c1) in zip(pts, pts[1:]):
        if c0 >= n >= c1:
            f = (c0 - n) / (c0 - c1)
            return t0 + f * (t1 - t0) if how == 'linear' else math.exp(math.log(t0) + f * (math.log(t1) - math.log(t0)))
out = [['release', 'population (million)', 'capacity, average year', 'capacity at 1 in 5 (20%)', 'at 1 in 10 (10%)', 'at 1 in 20 (5%)', 'at 1 in 50 (2%)', 'at 1 in 100 (1%)',
        'failure return period at the population, years (linear in T to log T)', 'failure probability a year at the population, % (range)', 'capacity at 10% failure as share of average-year capacity']]
for rel in ('2011-fixed', '2025-fixed', '2011-improved', '2025-improved', '2025-mirror'):
    c = R[rel]; n = POP[rel]
    tl, tg = return_period(c, n, 'linear'), return_period(c, n, 'log')
    p = ('%.1f to %.1f' % (100 / tl, 100 / tg)) if tl and tg and tl > 1 else ('100 (fails in an average year)' if tl == 1 else '< 1')
    out.append([rel, n, c[1], c[5], c[10], c[20], c[50], c[100], ('%.0f to %.0f' % (tl, tg)) if tl and tl > 1 else '', p, round(c[10] / c[1], 2)])
csv.writer(open('analysis/method_tests_2025/fearnside_failure_curve.csv', 'w', newline='')).writerows(out)
for r in out: print(r)
