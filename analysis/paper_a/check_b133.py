#!/usr/bin/env python3
"""B133: recomputes the figures of the paired draws, of 2011's bad years on the 2025 table and of the failure-probability range from their input files, and checks figures quoted from them.

Usage (repository root): python3 -I analysis/paper_a/check_b133.py [KEY=VALUE ...]
  With no arguments it checks every output file against its inputs and prints the figures.
  KEY is one of (VALUE in the unit shown):
    PRESET:BASIS:fall      share of draws with a fall, per cent, one decimal           PRESET is short or long; BASIS is all_draws, holdings_land_only or shared_choices_only
    PRESET:BASIS:unpaired  the unpaired share (2025 draws below the 2011 base value), per cent, one decimal
    PRESET:BASIS:p5, p50, p95   the paired difference, millions, two decimals
    fail:MODE:p5, p50, p95     the yearly failure probability, per cent, one decimal      MODE is linear or log-linear
    shock:BASIS:T:poc      national people over capacity (population over capacity), two decimals     BASIS is 2011_thesis_table, 2011_on_2025_table or 2025_2025_table; T is 1, 5, 10, 20, 50 or 100
    shock:BASIS:T:regions  regions over capacity (of 53)
Exit 1 on any mismatch."""
import csv, json, math, sys
sys.path.insert(0, 'analysis/paper_a')
from failure_probability_range import rp, pct, POP
def P(v, q):
    s = sorted(v); i = q * (len(s) - 1); lo = int(i); hi = min(lo + 1, len(s) - 1); return s[lo] + (s[hi] - s[lo]) * (i - lo)
bad, calc = [], {}
# 1. paired draws
W = {r['i']: r for r in csv.DictReader(open('analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv')) if r['block'] == 'A'}
D = list(csv.DictReader(open('analysis/sensitivity_2025/monte_carlo_draws_paired_2011-2025.csv')))
if len(D) != 2000: bad.append(f'paired draws file has {len(D)} rows, not 2000')
for r in D:
    w = W[r['draw']]
    for k in ('sf', 'sh', 'meat', 'meategg', 'redmeat', 'fuel', 'biofuel', 'timber', 'orgfac', 'orgshare', 'restable', 'lfuel', 'lbench', 'waste', 'lossaus', 'land', 'meatcal', 'energy', 'trendwin'):
        if r[k] != w[k]: bad.append(f"draw {r['draw']} {k}: {r[k]} against the widened draws {w[k]}")
    for k in ('short', 'long'):
        if int(r[f'cap2025_{k}']) != int(w[f'1_{k}']): bad.append(f"draw {r['draw']} cap2025_{k} differs from the widened draws")
        if int(r[f'cap2025_{k}']) - int(r[f'cap2011_{k}']) != int(r[f'diff_{k}']): bad.append(f"draw {r['draw']} diff_{k} is not 2025 minus 2011")
b11 = {'short': 33307814, 'long': 15350146}
for k in ('short', 'long'):
    BAS = {'all_draws': (D, 'cap2025_'), 'holdings_land_only': ([r for r in D if float(r['land']) == 0], 'cap2025_'), 'shared_choices_only': (D, 'cap2025_shared_only_')}
    for b, (S, col) in BAS.items():
        y11 = [int(r[f'cap2011_{k}']) for r in S]; y25 = [int(r[col + k]) for r in S]; df = [a - c for a, c in zip(y25, y11)]
        c = calc[f'{k}:{b}:'] = {'fall': 100 * sum(1 for x in df if x < 0) / len(df), 'unpaired': 100 * sum(1 for x in y25 if x < b11[k]) / len(y25), 'p5': P(df, .05) / 1e6, 'p50': P(df, .5) / 1e6, 'p95': P(df, .95) / 1e6, 'n': len(S)}
        for key, v in c.items(): calc[f'{k}:{b}:{key}'] = v
S_ = {(r['preset'], r['basis']): r for r in csv.DictReader(open('results/paired_change_2011-2025.csv'))}
for k in ('short', 'long'):
    for b in ('all_draws', 'holdings_land_only', 'shared_choices_only'):
        r, c = S_[(k, b)], calc[f'{k}:{b}:']
        for col, key in (('diff_p5', 'p5'), ('diff_p50', 'p50'), ('diff_p95', 'p95')):
            if abs(int(r[col]) - c[key] * 1e6) > 1: bad.append(f'results file {k} {b} {col}: {r[col]} against {c[key] * 1e6:.0f}')
        if abs(float(r['share_draws_with_a_fall']) * 100 - c['fall']) > 0.005: bad.append(f"results file {k} {b} share with a fall: {r['share_draws_with_a_fall']} against {c['fall'] / 100:.4f}")
        if int(r['n_draws']) != c['n']: bad.append(f'results file {k} {b} n_draws')
# 2. failure probability range (an independent read of the table: analysis/resilience_2025/tables.csv, the row 'data: ABS to 2024-25')
T = [r for r in csv.reader(open('analysis/resilience_2025/tables.csv')) if r[0] == 'Australia' and r[1] == 'data: ABS to 2024-25'][0]
mod = json.load(open('web/public/data/2025-fixed/model.json'))['sheets']['resilience']['cells']
for t in range(1, 151):
    if abs(float(T[1 + t]) - mod[f'2:{t + 1}']) > 1e-5: bad.append(f'table at {t} years: tables.csv {T[1 + t]} against the release {mod[f"2:{t + 1}"]}')
cap = [float(r['1_short']) for r in W.values()]
for mode in ('linear', 'log-linear'):
    pr = [1 / rp(POP / c, mode)[0] for c in cap]
    for q, n in ((.05, 'p5'), (.5, 'p50'), (.95, 'p95')): calc[f'fail:{mode}:{n}'] = 100 * P(pr, q)
F = {r['interpolation']: r for r in csv.DictReader(open('analysis/paper_a/failure_probability_range.csv'))}
for mode in ('linear', 'log-linear'):
    for n in ('p5', 'p50', 'p95'):
        if abs(float(F[mode][n]) * 100 - calc[f'fail:{mode}:{n}']) > 0.005: bad.append(f'failure file {mode} {n}: {F[mode][n]} against {calc[f"fail:{mode}:{n}"] / 100:.4f}')
# direct check of the linear rule with an independent interpolation on the anchors (10 and 20 years) for the base: 17.1 years
t0 = POP / 41503537; f10, f20 = float(T[11]), float(T[21])
if abs((10 + 10 * (f10 - t0) / (f10 - f20)) - 17.1) > 0.05: bad.append('the base return period is not 17.1 years')
# 3. 2011 on the 2025 table
Sh = list(csv.DictReader(open('analysis/paper_a/shocks_2011_on_2025_table.csv')))
fac = {int(t): float(T[1 + t]) for t in (1, 5, 10, 20, 50, 100)}
for r in Sh:
    if r['zone'] == '1' and r['basis'] in ('2011_on_2025_table', '2025_2025_table'):
        base = [x for x in Sh if x['zone'] == '1' and x['basis'] == r['basis'] and x['return_period'] == '1'][0]
        if abs(int(r['capacity']) / (int(base['capacity']) * fac[int(r['return_period'])]) - 1) > 3e-5: bad.append(f"{r['basis']} T {r['return_period']}: national capacity is not base times the table factor")
for b in ('2011_thesis_table', '2011_on_2025_table', '2025_2025_table'):
    for t in (1, 5, 10, 20, 50, 100):
        nat = [x for x in Sh if x['basis'] == b and x['zone'] == '1' and int(x['return_period']) == t][0]
        regs = [x for x in Sh if x['basis'] == b and x['kind'] in ('region',) or (x['basis'] == b and x['zone'] == '60')]
        regs = [x for x in regs if int(x['return_period']) == t]
        calc[f'shock:{b}:{t}:poc'] = int(nat['population']) / int(nat['capacity']); calc[f'shock:{b}:{t}:regions'] = sum(1 for x in regs if int(x['capacity']) < int(x['population']))
SM = {(r['basis'], r['return_period']): r for r in csv.DictReader(open('analysis/paper_a/shocks_2011_on_2025_table_summary.csv'))}
for (b, t), r in SM.items():
    if abs(float(r['people_over_capacity']) - calc[f'shock:{b}:{t}:poc']) > 0.0005 or int(r['regions_over_capacity_of_53']) != calc[f'shock:{b}:{t}:regions']: bad.append(f'summary file {b} {t} differs from the long file')
# quoted values
for a in sys.argv[1:]:
    key, val = a.split('=')
    if key.startswith('shock:'):
        c = calc[key]; want = f'{c:.2f}' if key.endswith('poc') else str(c)
    elif key.startswith('fail:'): want = f'{calc[key]:.1f}'
    else:
        c = calc[key]; want = f'{c:.1f}' if key.split(':')[-1] in ('fall', 'unpaired') else f'{c:.2f}'
    if want != val: bad.append(f'{key}: quoted {val}, the files give {want}')
if bad: print('\n'.join(bad)); sys.exit(1)
print('ok')
for k in ('short', 'long'):
    for b in ('all_draws', 'holdings_land_only', 'shared_choices_only'):
        c = calc[f'{k}:{b}:']; print(f"{k} {b}: n {c['n']}, fall {c['fall']:.1f}%, unpaired {c['unpaired']:.1f}%, difference p5 {c['p5']:.2f} p50 {c['p50']:.2f} p95 {c['p95']:.2f} million")
for m in ('linear', 'log-linear'): print(f"failure {m}: {calc[f'fail:{m}:p5']:.1f}% to {calc[f'fail:{m}:p95']:.1f}% (median {calc[f'fail:{m}:p50']:.1f}%)")
for b in ('2011_thesis_table', '2011_on_2025_table', '2025_2025_table'): print(b, ' '.join(f"T{t}: {calc[f'shock:{b}:{t}:poc']:.3f}/{calc[f'shock:{b}:{t}:regions']}" for t in (10, 20)))
