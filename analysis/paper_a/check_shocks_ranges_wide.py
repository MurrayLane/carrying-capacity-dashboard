#!/usr/bin/env python3
"""B123 check: recomputes analysis/paper_a/shocks_ranges_wide.csv and shocks_ranges_wide_own_table.csv independently of shocks_ranges.mjs (the widened draws times the factor read from
analysis/resilience_2025/tables.csv, the 'data: ABS to 2024-25' rows for the release table and the 'loo reference' rows for the leave-one-out table), checks that the national column of the
state draws equals block A of monte_carlo_draws_2025-fixed_wide.csv to the person, and checks the figures quoted in qa/reports/B123_shocks_on_widened_draws.md.
Usage (repository root): python3 -I analysis/paper_a/check_shocks_ranges_wide.py [FILE RETURN_PERIOD COLUMN VALUE]
With the four optional arguments the quoted value is replaced by VALUE (FILE is wide or own; a wrong value given on purpose must fail). Exit status 1 on any failure."""
import csv, sys
STATE = lambda z: 'Australia' if z == 1 else 'New South Wales' if z == 2 else 'Victoria' if z == 15 else 'Queensland' if z == 26 else 'South Australia' if z in (40, 60) else 'Western Australia' if z == 49 else 'Tasmania'
def table(method): return {r['location']: r for r in csv.DictReader(open('analysis/resilience_2025/tables.csv')) if r['method'] == method}
REL, LOO = table('data: ABS to 2024-25'), table('loo reference')
def pct(v, q):
    s = sorted(v); i = q * (len(s) - 1); lo = int(i); hi = min(lo + 1, len(s) - 1); return s[lo] + (s[hi] - s[lo]) * (i - lo)
draws = list(csv.DictReader(open('analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide_states.csv')))
bad = 0; n = 0
# (1) the national column of the state draws is block A of the published widened draws
blockA = [r for r in csv.DictReader(open('analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv')) if r['block'] == 'A']
diff = [i for i, (a, b) in enumerate(zip(draws, blockA)) if abs(float(a['1_short']) - float(b['1_short'])) > 1 or abs(float(a['1_long']) - float(b['1_long'])) > 1]
print(f'national column against block A of the widened draws: {len(draws)} against {len(blockA)} draws, {len(diff)} differ by more than one person')
bad += len(diff) + (len(draws) != len(blockA))
# (2) the two files
FILES = {}
for tag, f, own in (('wide', 'analysis/paper_a/shocks_ranges_wide.csv', False), ('own', 'analysis/paper_a/shocks_ranges_wide_own_table.csv', True)):
    rows = list(csv.DictReader(open(f))); FILES[tag] = rows
    for r in rows:
        z, T = int(r['zone']), int(r['return_period']); fr = float(REL[STATE(z)][str(T)]); fl = float(LOO[STATE(z)][str(T)]); P = int(r['population'])
        v = [float(x[f'{z}_short']) * (fl if own and x['restable'] == '1' else fr) for x in draws]
        for col, q in (('p5', .05), ('p50', .5), ('p95', .95)):
            n += 1
            if abs(round(pct(v, q)) - int(r[col])) > 1: bad += 1; print('MISMATCH', tag, z, T, col, r[col], round(pct(v, q)))
        n += 1; share = sum(1 for x in v if x < P) / len(v)
        if abs(share - float(r['share_draws_below_population'])) > 6e-5: bad += 1; print('MISMATCH share', tag, z, T, r['share_draws_below_population'], round(share, 4))
print(f'recomputed {n} percentiles and shares from the draws: {n - bad} agree (to one person; shares to 0.0001)')
# (3) the national figures quoted in qa/reports/B123_shocks_on_widened_draws.md: (file, return period, column) -> (value, decimals); capacities in millions, ratios and shares as printed there
nat = {(t, int(r['return_period'])): r for t in FILES for r in FILES[t] if r['zone'] == '1'}
QUOTED = {('wide', 10, 'p5'): (23.1, 1), ('wide', 10, 'p50'): (28.9, 1), ('wide', 10, 'p95'): (36.5, 1), ('wide', 10, 'central'): (30.8, 1),
          ('wide', 20, 'p5'): (19.7, 1), ('wide', 20, 'p50'): (24.7, 1), ('wide', 20, 'p95'): (31.2, 1), ('wide', 20, 'central'): (26.3, 1),
          ('wide', 1, 'p5'): (31.1, 1), ('wide', 1, 'p95'): (49.2, 1),
          ('wide', 10, 'population_over_capacity_at_p95'): (0.756, 3), ('wide', 10, 'population_over_capacity_at_p5'): (1.195, 3),
          ('wide', 20, 'population_over_capacity_at_p95'): (0.885, 3), ('wide', 20, 'population_over_capacity_at_p5'): (1.399, 3),
          ('wide', 10, 'capacity_over_population_p5'): (0.837, 3), ('wide', 10, 'capacity_over_population_p95'): (1.322, 3),
          ('wide', 20, 'capacity_over_population_p5'): (0.715, 3), ('wide', 20, 'capacity_over_population_p95'): (1.130, 3),
          ('wide', 1, 'share_draws_below_population'): (0.0045, 4), ('wide', 10, 'share_draws_below_population'): (0.3700, 4), ('wide', 20, 'share_draws_below_population'): (0.7765, 4),
          ('own', 10, 'p5'): (22.5, 1), ('own', 10, 'p95'): (35.9, 1), ('own', 20, 'p5'): (19.1, 1), ('own', 20, 'p95'): (30.5, 1),
          ('own', 10, 'share_draws_below_population'): (0.4200, 4), ('own', 20, 'share_draws_below_population'): (0.8230, 4)}
if len(sys.argv) == 5: QUOTED[(sys.argv[1], int(sys.argv[2]), sys.argv[3])] = (float(sys.argv[4]), QUOTED[(sys.argv[1], int(sys.argv[2]), sys.argv[3])][1]); print(f'EXAMPLE: quoted value replaced by {sys.argv[4]}')
for (t, T, col), (val, dec) in QUOTED.items():
    r = nat[(t, T)]; got = int(r[col]) / 1e6 if col in ('p5', 'p50', 'p95', 'central') else float(r[col])
    if abs(round(got, dec) - val) > 1e-9: bad += 1; print(f'FAIL quoted {t} 1-in-{T} {col} = {val} but the file gives {got:.4f}')
    else: print(f'ok   quoted {t} 1-in-{T} {col} = {val}')
# the sentence "27.6 million lies inside both ranges" (the national population inside p5 to p95 at 1 in 10 and 1 in 20, on the release table)
inside = all(nat[('wide', T)]['population_inside_p5_p95'] == 'yes' for T in (10, 20))
print('population inside both national ranges (release table):', inside); bad += 0 if inside else 1
sys.exit(1 if bad else 0)
