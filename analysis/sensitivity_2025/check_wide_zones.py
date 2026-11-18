#!/usr/bin/env python3
"""B132 check: the widened draws of every zone and their ranges file, independent of summarise_wide_zones.py (percentiles by statistics.quantiles, method 'inclusive', which is the same linear rule by another code path).

Usage (repository root): python3 -I analysis/sensitivity_2025/check_wide_zones.py [ZONE:PRESET:STAT=VALUE ...]
  STAT is p5, p50, p95, min or max (people, whole numbers). With no arguments it checks the files. Exit status 1 on any mismatch.
Checks: (1) 2,000 draws and 19 choice columns; every zone's short and long column present (60 zones, 120 columns);
(2) the choice columns equal those of block A of monte_carlo_draws_2025-fixed_wide.csv (to 5 decimals) and the Australian short and long columns equal its block A to the person (the zone 45 fix changes no national draw);
(3) the columns of Australia and the seven states equal those of monte_carlo_draws_2025-fixed_wide_states.csv to the person (the fix changes no state draw);
(4) every row of results/ranges_2025-fixed_wide_zones.csv recomputed from the draws (120 rows x 5 statistics) to one person; base equals results/ranges_2025-fixed.csv's base;
(5, 6) the land-source medians quoted in the README; the zone 45 columns against the release: nothing is compared there except that the draws exist and are not negative (Alinytjara Wilurara, zone 42, has capacity 0) (the raster land of zone 45 was rebuilt on the release land, X140)."""
import csv, statistics, sys
D = 'analysis/sensitivity_2025/'
draws = list(csv.DictReader(open(D + 'monte_carlo_draws_2025-fixed_wide_all.csv')))
A = [r for r in csv.DictReader(open(D + 'monte_carlo_draws_2025-fixed_wide.csv')) if r['block'] == 'A']
S = list(csv.DictReader(open(D + 'monte_carlo_draws_2025-fixed_wide_states.csv')))
bad = []
cols = list(draws[0]); choices = [c for c in cols if not c[0].isdigit()]; zonecols = [c for c in cols if c[0].isdigit()]
if len(draws) != 2000: bad.append(f'{len(draws)} draws, not 2000')
if len(choices) != 19: bad.append(f'{len(choices)} choice columns, not 19')
if len(zonecols) != 120: bad.append(f'{len(zonecols)} zone columns, not 120')
for c in choices:
    d = max(abs(float(a[c]) - float(b[c])) for a, b in zip(draws, A))
    if d > 1.5e-5: bad.append(f'choice {c}: differs from block A by {d}')
for c in ('1_short', '1_long'):
    d = max(abs(float(a[c]) - float(b[c])) for a, b in zip(draws, A))
    if d > 1: bad.append(f'{c}: differs from block A by {d} people')
    print(f'{c} against block A of the widened draws: maximum difference {d:g}')
st = [c for c in S[0] if c[0].isdigit()]
for c in st:
    d = max(abs(float(a[c]) - float(b[c])) for a, b in zip(draws, S))
    if d > 1: bad.append(f'{c}: differs from the state draws by {d} people')
print(f'{len(st)} state and national columns against monte_carlo_draws_2025-fixed_wide_states.csv: maximum difference', max(max(abs(float(a[c]) - float(b[c])) for a, b in zip(draws, S)) for c in st))
base = {(r['zone'], r['setting']): int(float(r['base'])) for r in csv.DictReader(open('results/ranges_2025-fixed.csv'))}
calc = {}
for c in zonecols:
    z, k = c.split('_'); y = [float(r[c]) for r in draws]
    q = statistics.quantiles(y, n=100, method='inclusive')
    calc[(z, k)] = {'p5': q[4], 'p50': q[49], 'p95': q[94], 'min': min(y), 'max': max(y)}
    if min(y) < 0: bad.append(f'{c}: a draw is negative')
n = 0
for r in csv.DictReader(open('results/ranges_2025-fixed_wide_zones.csv')):
    c = calc[(r['zone'], r['preset'])]; n += 1
    for stat in ('p5', 'p50', 'p95', 'min', 'max'):
        if abs(round(c[stat]) - int(r[stat])) > 1: bad.append(f"ranges file zone {r['zone']} {r['preset']} {stat}: {r[stat]} against {round(c[stat])}")
    if int(r['base']) != base[(r['zone'], r['preset'])]: bad.append(f"ranges file zone {r['zone']} {r['preset']} base {r['base']} against {base[(r['zone'], r['preset'])]}")
if n != 120: bad.append(f'{n} rows in the ranges file, not 120')
for arg in sys.argv[1:]:
    key, val = arg.split('='); z, k, stat = key.split(':'); got = round(calc[(z, k)][stat])
    if got != int(val): bad.append(f'{key}: quoted {val}, the draws give {got}')
# (6) the land-source medians quoted in the README (short term, 1,000 draws on each land source)
for z, name, lo, hi in (('32', 'Desert Channels', 82215, 2972), ('57', 'North Tasmania', 166406, 234040)):
    for land, want in ((0, lo), (1, hi)):
        m = statistics.median([float(r[f'{z}_short']) for r in draws if float(r['land']) == land])
        if abs(m - want) > 1: bad.append(f'{name} median on land source {land}: quoted {want}, the draws give {m:.0f}')
print('\n'.join(bad) if bad else f'ok: {len(draws)} draws, {len(choices)} choices, {len(zonecols)} zone columns; {n} rows x 5 statistics recomputed')
sys.exit(1 if bad else 0)
