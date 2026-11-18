#!/usr/bin/env python3
"""B110: what moves between the -2 and the -3 releases and the Paper A outputs built on them, and the checks of brief B110 step 4.
Usage (repository root, after web/scripts/make-results.mjs 2011-fixed-3 2011-improved-3 and the -3 runs of analysis/paper_a): python3 -I analysis/population_2011/compare_2_and_3.py
Writes analysis/population_2011/changes_2_to_3.csv (one row per zone, preset and release pair whose population, capacity or status differs) and prints the
national counts and the checks. Exits non-zero if a check fails. Deterministic."""
import csv, collections, sys
rd = lambda p: list(csv.DictReader(open(p)))
L = lambda f: {(r['zone'], r['preset']): r for r in rd(f)}
STATES = {'2': range(3, 15), '15': range(16, 26), '26': range(27, 40), '40': range(41, 49), '49': range(50, 56), '56': range(57, 60)}
REGIONS = [str(z) for c in STATES.values() for z in c] + ['60']
fails = []
def check(ok, what):
    print(('pass  ' if ok else 'FAIL  ') + what)
    if not ok: fails.append(what)

# 1. results: population, capacity, status by zone
out = [['pair', 'zone', 'name', 'kind', 'preset', 'population -2', 'population -3', 'capacity -2', 'capacity -3', 'over -2', 'over -3']]
for t in ('fixed', 'improved'):
    a, b = L(f'results/2011-{t}-2.csv'), L(f'results/2011-{t}-3.csv')
    for k in sorted(a, key=lambda k: (int(k[0]), k[1])):
        x, y = a[k], b[k]
        if (x['population'], x['capacity'], x['over_capacity']) != (y['population'], y['capacity'], y['over_capacity']):
            out.append([f'2011-{t}-2 to 2011-{t}-3', k[0], x['name'], x['kind'], k[1], x['population'], y['population'], x['capacity'], y['capacity'], x['over_capacity'], y['over_capacity']])
    for p in ('short', 'long'):
        n2 = sum(int(a[(z, p)]['over_capacity']) for z in REGIONS); n3 = sum(int(b[(z, p)]['over_capacity']) for z in REGIONS)
        ch = [f"{a[(z, p)]['name']} {'over to under' if int(a[(z, p)]['over_capacity']) else 'under to over'}" for z in REGIONS if a[(z, p)]['over_capacity'] != b[(z, p)]['over_capacity']]
        print(f'2011-{t}: regions over capacity, {p}: -2 {n2}, -3 {n3}; status changes: {ch or "none"}')
    st = [(z, p) for z in ['1'] + list(STATES) + ['60'] for p in ('short', 'long') if a[(z, p)]['over_capacity'] != b[(z, p)]['over_capacity']]
    print(f'2011-{t}: national and state status changes: {st or "none"}')
csv.writer(open('analysis/population_2011/changes_2_to_3.csv', 'w', newline='')).writerows(out)

# 2. the checks of step 4
f2, f3, i2, i3 = (L(f'results/{r}.csv') for r in ('2011-fixed-2', '2011-fixed-3', '2011-improved-2', '2011-improved-3'))
check(all(f2[k]['capacity'] == f3[k]['capacity'] for k in f2), '2011-fixed-3 capacities equal 2011-fixed-2 in every zone and both presets (120 cells)')
moved = [(k, int(i2[k]['capacity']), int(i3[k]['capacity'])) for k in i2 if i2[k]['capacity'] != i3[k]['capacity']]
mx = max(moved, key=lambda m: abs(m[2] - m[1]) / m[1]) if moved else None
print(f'note  2011-improved-3 capacities differ from 2011-improved-2 in {len(moved)} of 120 cells (infrastructure land enters capacity through reserve-pro-rata); largest relative move {mx}')
for nm, R in (('2011-fixed-3', f3), ('2011-improved-3', i3)):
    for p in ('short', 'long'):
        check(all(int(R[(s, p)]['population']) == sum(int(R[(str(z), p)]['population']) for z in c) for s, c in STATES.items()), f'{nm} {p}: every state population equals the sum of its regions')
        check(int(R[('1', p)]['population']) == 22326388, f'{nm} {p}: the national population stays 22,326,388')
    tot = sum(int(R[(z, 'short')]['population']) for z in REGIONS)
    check(tot == 22336514, f'{nm}: the 52 NRM regions plus the Northern Territory sum to 22,336,514 (got {tot:,})')
abs_ = {r['zone']: int(r['abs_erp_2011_sa2_route']) for r in rd('analysis/population_2011/zone_population_2011_comparison.csv')}
check(all(int(f3[(z, p)]['population']) == abs_[z] for z in REGIONS for p in ('short', 'long')), '2011-fixed-3: every region carries the ABS figure of zone_population_2011_comparison.csv')

# 3. Paper A outputs, -2 against -3
def flips(f):
    r = rd(f); return {t: {x['name']: (x['flip'], x['clean and robust']) for x in r if x['term'] == t and x['flip']} for t in ('short', 'long')}, {t: sum(int(x['over 2011']) for x in r if x['term'] == t) for t in ('short', 'long')}
(F2, O2), (F3, O3) = flips('analysis/paper_a/regional_flips.csv'), flips('analysis/paper_a/regional_flips-3.csv')
for t in ('short', 'long'):
    print(f'flips {t}: over 2011 {O2[t]} to {O3[t]}; flips {len(F2[t])} to {len(F3[t])}; clean {sum(v[1] == "yes" for v in F2[t].values())} to {sum(v[1] == "yes" for v in F3[t].values())}; '
          f'gone {sorted(set(F2[t]) - set(F3[t])) or "none"}; new {sorted(set(F3[t]) - set(F2[t])) or "none"}; clean list -3 {sorted(k for k, v in F3[t].items() if v[1] == "yes")}')
r2 = {(r['release'][:10], r['return period (years)']): r for r in rd('analysis/paper_a/shocks_summary.csv')}
r3 = {(r['release'][:10], r['return period (years)']): r for r in rd('analysis/paper_a/shocks_summary-3.csv')}
for k in r2:
    d = [(c, r2[k][c], r3[k][c]) for c in r2[k] if c != 'release' and r2[k][c] != r3[k][c]]
    if d: print('shocks summary', k, d)
def tip(f, rel):
    G = collections.defaultdict(dict)
    for r in rd(f):
        if r['release'] == rel and r['kind'] != 'nation': G[r['name'].strip('"')][int(r['return_period'])] = float(r['capacity']) / float(r['population'])
    return {T: sorted(n for n, v in G.items() if v[1] >= 1 and v[T] < 1) for T in (10, 20)}
for rel2, rel3 in (('2011-fixed-2', '2011-fixed-3'), ('2025-fixed', '2025-fixed')):
    a, b = tip('analysis/paper_a/shocks_by_region.csv', rel2), tip('analysis/paper_a/shocks_by_region-3.csv', rel3)
    for T in (10, 20): print(f'tip at 1 in {T}, {rel2} -> {rel3}: {len(a[T])} {a[T]} -> {len(b[T])} {b[T]}')
s2, s3 = rd('analysis/paper_a/shocks_by_region.csv'), rd('analysis/paper_a/shocks_by_region-3.csv')
check(all(x['capacity'] == y['capacity'] for x, y in zip(s2, s3)) and len(s2) == len(s3), 'shocks_by_region-3 capacities equal shocks_by_region (-2) in all 648 rows')
check(all(x == y for x, y in zip(s2, s3) if x['release'] == '2025-fixed'), 'shocks_by_region-3 2025 rows identical to -2')
print('checks failed:', len(fails)); sys.exit(1 if fails else 0)
