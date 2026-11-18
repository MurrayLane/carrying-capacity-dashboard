#!/usr/bin/env python3
"""B134 (decision 141): the failure-probability view on the crop-only drought bound, beside the model's own rule.
Usage (repository root): python3 -I analysis/method_tests_2025/fearnside_failure_curve_crop_only.py     writes fearnside_failure_curve_crop_only.csv
        python3 -I analysis/method_tests_2025/fearnside_failure_curve_crop_only.py --wrong-value-demo     shows the check failing on a planted wrong value (writes nothing)

Reads analysis/resilience_2025/drought_bounds_paper_B.csv (capacity at 1 in 5, 10, 20, 50 and 100 with the drought factor on every yield, and on crops only; the 1 in 1 point is the mean year).
The interpolation is that of fearnside_failure_curve.py (linear in T, and linear in log T), copied here because that script writes its csv when imported; the original csv is kept unchanged.
First check: the both-applied curve, read at the 2025 population (27.6082 million), must give 5.8 to 6.1% a year, the figure fearnside_failure_curve.csv holds for 2025-fixed.
Reading the crop-only curve: its lowest point (1 in 100) is above the population, so the curve never falls to the population within the run points; the failure probability at the
population is then below 1 in 100 a year (below 1%), an upper bound set by the last run point; the curve is not extrapolated past 1 in 100."""
import csv, math, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
POP = 27.6082
DEMO = '--wrong-value-demo' in sys.argv

def return_period(curve, n, how):
    pts = sorted(curve.items())
    if n >= pts[0][1]: return 1.0
    if n < pts[-1][1]: return None
    for (t0, c0), (t1, c1) in zip(pts, pts[1:]):
        if c0 >= n >= c1:
            f = (c0 - n) / (c0 - c1)
            return t0 + f * (t1 - t0) if how == 'linear' else math.exp(math.log(t0) + f * (math.log(t1) - math.log(t0)))

def read_curves(rel):
    rows = [r for r in csv.DictReader(open(os.path.join(ROOT, 'analysis/resilience_2025/drought_bounds_paper_B.csv'))) if r['release'] == rel and r['preset'] == 'short']
    mean = float(rows[0]['mean_year_capacity']) / 1e6
    both, crop = {1: mean}, {1: mean}
    for r in rows:
        both[int(r['return_period'])] = float(r['both_applied']) / 1e6
        crop[int(r['return_period'])] = float(r['crop_only']) / 1e6
    return both, crop

def prob(curve, n):
    tl, tg = return_period(curve, n, 'linear'), return_period(curve, n, 'log')
    if tl is None: return None, None, 'below 1 (the curve stays above the population at 1 in 100)'
    if tl == 1.0: return 1.0, 1.0, '100 (fails in an average year)'
    return tl, tg, '%.1f to %.1f' % (100 / tl, 100 / tg)

out = [['release', 'population_million', 'drought_factor_on', 'capacity_mean_year', 'at_1_in_5', 'at_1_in_10', 'at_1_in_20', 'at_1_in_50', 'at_1_in_100',
        'failure_return_period_years_linear_to_log', 'failure_probability_pct_a_year_at_population', 'note']]
ok = True
for rel, note in (('2025-fixed', ''), ('2025-improved', 'approximate: the row-scaling rule differs from this release\'s own drought run by 0.1 to 0.4% at these points')):
    both, crop = read_curves(rel)
    for label, c in (('every yield (the model)', both), ('crops only (bound)', crop)):
        tl, tg, p = prob(c, POP)
        rp = '' if tl is None else ('%.0f to %.0f' % (tl, tg))
        out.append([rel, POP, label] + ['%.2f' % c[t] for t in (1, 5, 10, 20, 50, 100)] + [rp, p, note])
        if rel == '2025-fixed' and label.startswith('every'):
            shown = '6.5 to 6.9' if DEMO else p      # EXAMPLE wrong value in demo mode only
            ok = shown == '5.8 to 6.1'
            print('check, both-applied curve at the 2025 population: %s (fearnside_failure_curve.csv: 5.8 to 6.1): %s' % (shown, 'PASS' if ok else 'FAIL'))
for r in out: print(' | '.join(str(x) for x in r))
if DEMO:
    print('EXAMPLE (deliberate wrong value): the both-applied failure probability given as 6.5 to 6.9; nothing written'); sys.exit(0 if not ok else 1)
if not ok: sys.exit('check failed')
csv.writer(open(os.path.join(ROOT, 'analysis/method_tests_2025/fearnside_failure_curve_crop_only.csv'), 'w', newline=''), lineterminator='\n').writerows(out)
