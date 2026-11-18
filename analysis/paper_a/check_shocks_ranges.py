#!/usr/bin/env python3
"""B112 check: recomputes analysis/paper_a/shocks_ranges.csv independently of shocks_ranges.mjs (the draws times the factor read from tables.csv, the
'data: ABS to 2024-25' rows, which equal the release's resilience sheet) and checks the national figures quoted in qa/reports/B112_shock_ranges.md.
Usage (repository root): python3 -I analysis/paper_a/check_shocks_ranges.py [DRAWS_ID RETURN_PERIOD COLUMN VALUE]
With the four optional arguments the quoted value is replaced by VALUE (a wrong value given on purpose must fail). Exit status 1 on any failure."""
import csv, sys
STATE = lambda z: 'Australia' if z == 1 else 'New South Wales' if z < 15 else 'Victoria' if z < 26 else 'Queensland' if z < 40 else 'South Australia' if z < 49 else 'Western Australia' if z < 56 else 'Tasmania' if z < 60 else 'South Australia'
TAB = {r['location']: r for r in csv.DictReader(open('analysis/resilience_2025/tables.csv')) if r['method'] == 'data: ABS to 2024-25'}
def pct(v, q):
    s = sorted(v); i = q * (len(s) - 1); lo = int(i); hi = min(lo + 1, len(s) - 1); return s[lo] + (s[hi] - s[lo]) * (i - lo)
rows = list(csv.DictReader(open('analysis/paper_a/shocks_ranges.csv'))); bad = 0; n = 0
draws = {}
for d in sorted({r['draws'] for r in rows}):
    draws[d] = list(csv.DictReader(open(f'analysis/sensitivity_2025/monte_carlo_draws_{d}.csv')))
for r in rows:
    z, T = int(r['zone']), int(r['return_period']); f = float(TAB[STATE(z)][str(T)])
    v = [float(x[f'{z}_short']) * f for x in draws[r['draws']]]
    for col, q in (('p5', .05), ('p50', .5), ('p95', .95)):
        n += 1
        if abs(round(pct(v, q)) - int(r[col])) > 1: bad += 1; print('MISMATCH', r['draws'], z, T, col, r[col], round(pct(v, q)))
print(f'recomputed {n} percentiles from the draws: {n - bad} agree to one person')
# the national figures quoted in the report, in millions to one decimal (ratios to two decimals)
QUOTED = {('2025-fixed_all', 10, 'p5'): 27.0, ('2025-fixed_all', 10, 'p95'): 34.0, ('2025-fixed_all', 20, 'p5'): 23.0, ('2025-fixed_all', 20, 'p95'): 29.0,
          ('2025-fixed_all', 10, 'central'): 30.8, ('2025-fixed_all', 20, 'central'): 26.3,
          ('2025-fixed_herdcycle_all', 1, 'p5'): 39.4, ('2025-fixed_herdcycle_all', 1, 'p95'): 43.8, ('2025-fixed_herdcycle_all', 10, 'p5'): 29.2,
          ('2025-fixed_herdcycle_all', 10, 'p95'): 32.5, ('2025-fixed_herdcycle_all', 20, 'p5'): 25.0, ('2025-fixed_herdcycle_all', 20, 'p95'): 27.8,
          ('2025-fixed_herdcycle5_all', 10, 'p5'): 29.2, ('2025-fixed_herdcycle5_all', 10, 'p95'): 32.5, ('2025-fixed_herdcycle5_all', 20, 'p5'): 25.0, ('2025-fixed_herdcycle5_all', 20, 'p95'): 27.8}
if len(sys.argv) == 5: QUOTED[(sys.argv[1], int(sys.argv[2]), sys.argv[3])] = float(sys.argv[4]); print(f'EXAMPLE: quoted value replaced by {sys.argv[4]}')
nat = {(r['draws'], int(r['return_period'])): r for r in rows if r['zone'] == '1'}
for (d, T, col), val in QUOTED.items():
    got = int(nat[(d, T)][col]) / 1e6
    if abs(round(got, 1) - val) > 1e-9: bad += 1; print(f'FAIL quoted {d} 1-in-{T} {col} = {val} but the file gives {got:.3f} million')
    else: print(f'ok   quoted {d} 1-in-{T} {col} = {val}')
sys.exit(1 if bad else 0)
