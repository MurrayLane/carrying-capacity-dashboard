#!/usr/bin/env python3
"""B132 check: recomputes analysis/paper_a/shocks_ranges_wide_zones.csv, shocks_ranges_wide_zones_own_table.csv and shocks_counts_wide_zones.csv independently of shocks_ranges.mjs and tipping_counts.py
(the widened draws of every zone times the factor read from analysis/resilience_2025/tables.csv, the 'data: ABS to 2024-25' rows for the release table and the 'loo reference' rows for the leave-one-out table;
percentiles by statistics.quantiles, method 'inclusive'), and checks the counts quoted in qa/reports/B132_regional_widened_draws.md.
Usage (repository root): python3 -I analysis/paper_a/check_shocks_ranges_wide_zones.py [RETURN_PERIOD COLUMN VALUE]
With the three optional arguments the quoted count is replaced by VALUE (COLUMN is over_at_central, over_at_p95_capacity, over_at_p5_capacity or inside_range; a wrong value given on purpose must fail). Exit status 1 on any failure."""
import csv, statistics, sys
STATE = lambda z: 'Australia' if z == 1 else 'New South Wales' if z < 15 else 'Victoria' if z < 26 else 'Queensland' if z < 40 else 'South Australia' if z < 49 else 'Western Australia' if z < 56 else 'Tasmania' if z < 60 else 'South Australia'   # the Northern Territory takes South Australia's row, as in the release
def table(method): return {r['location']: r for r in csv.DictReader(open('analysis/resilience_2025/tables.csv')) if r['method'] == method}
REL, LOO = table('data: ABS to 2024-25'), table('loo reference')
q = lambda v: statistics.quantiles(v, n=100, method='inclusive')
draws = list(csv.DictReader(open('analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide_all.csv')))
bad = 0; n = 0
for tag, f, own in (('wide', 'analysis/paper_a/shocks_ranges_wide_zones.csv', False), ('own', 'analysis/paper_a/shocks_ranges_wide_zones_own_table.csv', True)):
    rows = list(csv.DictReader(open(f)))
    if len(rows) != 180: bad += 1; print(f'{f}: {len(rows)} rows, not 180')
    for r in rows:
        z, T = int(r['zone']), int(r['return_period']); fr = float(REL[STATE(z)][str(T)]); fl = float(LOO[STATE(z)][str(T)]); P = int(r['population'])
        v = [float(x[f'{z}_short']) * (fl if own and x['restable'] == '1' else fr) for x in draws]; Q = q(v)
        for col, val in (('p5', Q[4]), ('p50', Q[49]), ('p95', Q[94])):
            n += 1
            if abs(round(val) - int(r[col])) > 1: bad += 1; print('MISMATCH', tag, z, T, col, r[col], round(val))
        n += 1; share = sum(1 for x in v if x < P) / len(v)
        if abs(share - float(r['share_draws_below_population'])) > 6e-5: bad += 1; print('MISMATCH share', tag, z, T, r['share_draws_below_population'], round(share, 4))
print(f'recomputed {n} percentiles and shares from the draws: {n - bad} agree (to one person; shares to 0.0001)')
# the counts, recomputed from the draws and the tables (not from the ranges file's percentiles)
cnt = {r['return_period']: r for r in csv.DictReader(open('analysis/paper_a/shocks_counts_wide_zones.csv'))}
pops = {int(r['zone']): int(r['population']) for r in csv.DictReader(open('analysis/paper_a/shocks_ranges_wide_zones.csv')) if r['return_period'] == '1'}
kind = {int(r['zone']): r['kind'] for r in csv.DictReader(open('analysis/paper_a/shocks_ranges_wide_zones.csv')) if r['return_period'] == '1'}
cen = {(int(r['zone']), r['return_period']): float(r['central']) for r in csv.DictReader(open('analysis/paper_a/shocks_ranges_wide_zones.csv'))}
REG = [z for z in pops if kind[z] == 'region' or z == 60]
calc = {}
for T in ('1', '10', '20'):
    vals = {z: [float(x[f'{z}_short']) * float(REL[STATE(z)][T]) for x in draws] for z in REG}
    Q = {z: q(vals[z]) for z in REG}
    per = [sum(1 for z in REG if vals[z][i] < pops[z]) for i in range(len(draws))]; Pq = q(per)
    calc[T] = {'regions': len(REG), 'over_at_central': sum(pops[z] > cen[(z, T)] for z in REG), 'over_at_p95_capacity': sum(pops[z] > Q[z][94] for z in REG), 'over_at_p5_capacity': sum(pops[z] > Q[z][4] for z in REG),
               'inside_range': sum(Q[z][4] <= pops[z] <= Q[z][94] for z in REG), 'draw_count_p5': round(Pq[4]), 'draw_count_p50': round(Pq[49]), 'draw_count_p95': round(Pq[94])}
    for col, val in calc[T].items():
        n += 1
        if int(cnt[T][col]) != val: bad += 1; print('MISMATCH count', T, col, cnt[T][col], val)
print('counts recomputed:', {T: {k: v for k, v in c.items() if k != 'regions'} for T, c in calc.items()}, '; regions', len(REG))
# the counts quoted in the report: (return period, column) -> value
QUOTED = {('10', 'over_at_central'): 21, ('10', 'over_at_p95_capacity'): 19, ('10', 'over_at_p5_capacity'): 26, ('10', 'inside_range'): 7,
          ('20', 'over_at_central'): 24, ('20', 'over_at_p95_capacity'): 22, ('20', 'over_at_p5_capacity'): 26, ('20', 'inside_range'): 4,
          ('1', 'over_at_central'): 16, ('1', 'over_at_p95_capacity'): 15, ('1', 'over_at_p5_capacity'): 23, ('1', 'inside_range'): 8}
if len(sys.argv) == 4: QUOTED[(sys.argv[1], sys.argv[2])] = int(sys.argv[3]); print(f'EXAMPLE: quoted value replaced by {sys.argv[3]}')
for (T, col), val in QUOTED.items():
    if calc[T][col] != val: bad += 1; print(f'FAIL quoted 1-in-{T} {col} = {val} but the draws give {calc[T][col]}')
    else: print(f'ok   quoted 1-in-{T} {col} = {val}')
sys.exit(1 if bad else 0)
