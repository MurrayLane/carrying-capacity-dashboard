#!/usr/bin/env python3
"""B133 (decision 135): the failure probability as a range across the widened draws.

Usage (repository root): python3 -I analysis/paper_a/failure_probability_range.py     (writes analysis/paper_a/failure_probability_range.csv)

For each of the 2,000 draws (block A of analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv, Australia, short term, 19 choices) the weather factor at which
capacity equals the 2025 population (27,608,200) is population over the draw's average-year capacity. Its return period is read off the drought factors of the release 2025-fixed
(the Australia row of the resilience sheet, the factor at 1 to 150 years; the draws are made at resilience 1, so every draw takes the release table, as in B112 and B123):
  linear      straight line in the return period between tabulated factors (the model's own rule and Paper A's: the base gives 17.1 years, 5.8% a year)
  log-linear  straight line in the logarithm of the return period between the table's anchors (1, 3, 5, 10, 20, 30, 50, 150 years; Paper B's reading: the base gives 16.4 years, 6.1% a year)
The yearly probability is the reciprocal of the return period. Two ends are outside the table: a draw whose capacity is below the population in an average year (factor needed above 1) is
set to a return period of 1 year (probability 1); a draw that needs a factor below the 150-year factor is set to 150 years (probability 1/150, an upper bound on the return period). Both counts are written.
The 5th, 50th and 95th percentiles use the rule of summarise_mc.py (straight line between order statistics)."""
import csv, json, math

POP = 27608200
anch = [1, 3, 5, 10, 20, 30, 50, 150]
tab = json.load(open('web/public/data/2025-fixed/model.json'))['sheets']['resilience']['cells']
f = {T: tab[f'2:{T + 1}'] for T in range(1, 151)}          # Australia row (resilience!B3 onward), factor at T years
assert all(f[T] >= f[T + 1] - 1e-12 for T in range(1, 150)), 'the table is not non-increasing'

def pct(v, q):
    s = sorted(v); i = q * (len(s) - 1); lo = int(i); hi = min(lo + 1, len(s) - 1); return s[lo] + (s[hi] - s[lo]) * (i - lo)

def rp(t, mode):
    """return period in years at which the factor equals t; (T, flag) with flag 'avg' (needs more than the average year), 'beyond' (past 150 years) or ''."""
    if t >= f[1]: return 1.0, 'avg'
    if t <= f[150]: return 150.0, 'beyond'
    if mode == 'linear':
        for T in range(1, 150):
            if f[T + 1] <= t < f[T] or (f[T] > t >= f[T + 1]): return T + (f[T] - t) / (f[T] - f[T + 1]), ''
    else:
        for a, b in zip(anch, anch[1:]):
            if f[b] <= t < f[a]: return math.exp(math.log(a) + (f[a] - t) / (f[a] - f[b]) * (math.log(b) - math.log(a))), ''
    raise SystemExit(f'no bracket for factor {t}')

if __name__ == '__main__':
    A = [r for r in csv.DictReader(open('analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv')) if r['block'] == 'A']
    cap = [float(r['1_short']) for r in A]
    base = 41503537                                         # 2025-fixed, Australia, short term, at its base settings (results/2025-fixed.csv)
    rows = [['draws', 'n_draws', 'table', 'interpolation', 'p5', 'p50', 'p95', 'return_period_years_at_p95_probability', 'return_period_years_median', 'return_period_years_at_p5_probability',
             'release_base_probability', 'release_base_return_period_years', 'draws_failing_in_an_average_year', 'draws_beyond_150_years']]
    for mode in ('linear', 'log-linear'):
        res = [rp(POP / c, mode) for c in cap]
        pr = [1 / T for T, _ in res]; T0, _ = rp(POP / base, mode)
        rows.append(['monte_carlo_draws_2025-fixed_wide.csv block A (19 choices, 2,000 draws; B115, decision 115)', len(cap), '2025-fixed resilience sheet, Australia row', mode,
                     f'{pct(pr, .05):.4f}', f'{pct(pr, .5):.4f}', f'{pct(pr, .95):.4f}', f'{1 / pct(pr, .95):.1f}', f'{1 / pct(pr, .5):.1f}', f'{1 / pct(pr, .05):.1f}',
                     f'{1 / T0:.4f}', f'{T0:.1f}', sum(1 for _, g in res if g == 'avg'), sum(1 for _, g in res if g == 'beyond')])
    csv.writer(open('analysis/paper_a/failure_probability_range.csv', 'w', newline='')).writerows(rows)
    for r in rows[1:]: print(r[3], 'p5', r[4], 'p50', r[5], 'p95', r[6], '| base', r[10], r[11], 'years | average-year failures', r[12], 'beyond 150', r[13])
