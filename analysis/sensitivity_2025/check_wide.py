#!/usr/bin/env python3
"""B115: recomputes the widened range from the draws and checks figures quoted from it (results/ranges_2025-fixed_wide.csv and the report).

Usage (repository root): python3 analysis/sensitivity_2025/check_wide.py [SETTING:STAT=VALUE ...]
  STAT is p5, p95, min or max (millions, one decimal) or r595 or rminmax (the ratios, two decimals). With no arguments it checks the ranges file against the draws.
Exit 1 on any mismatch.
"""
import csv, sys
def pct(v, q):
    s = sorted(v); i = q * (len(s) - 1); lo = int(i); hi = min(lo + 1, len(s) - 1); return s[lo] + (s[hi] - s[lo]) * (i - lo)
A = [r for r in csv.DictReader(open('analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv')) if r['block'] == 'A']
calc = {}
for k in ('short', 'long'):
    y = [float(r[f'1_{k}']) for r in A]
    calc[k] = {'p5': pct(y, .05), 'p95': pct(y, .95), 'min': min(y), 'max': max(y)}
    calc[k]['r595'] = calc[k]['p95'] / calc[k]['p5']; calc[k]['rminmax'] = calc[k]['max'] / calc[k]['min']
bad = []
for r in csv.DictReader(open('results/ranges_2025-fixed_wide.csv')):
    if r['variant'] != 'wide': continue
    c = calc[r['setting']]
    for stat, col in (('p5', 'p5'), ('p95', 'p95'), ('min', 'min'), ('max', 'max')):
        if round(c[stat]) != int(r[col]): bad.append(f"ranges file {r['setting']} {col}: {r[col]} against {round(c[stat])}")
for arg in sys.argv[1:]:
    key, val = arg.split('='); setting, stat = key.split(':'); c = calc[setting][stat]
    want = f'{c:.2f}' if stat.startswith('r') else f'{c / 1e6:.1f}'
    if want != val: bad.append(f'{key}: quoted {val}, the draws give {want}')
print('\n'.join(bad) if bad else f'ok: {len(A)} draws; ' + '; '.join(f"{k} {calc[k]['p5']/1e6:.1f} to {calc[k]['p95']/1e6:.1f} ({calc[k]['r595']:.2f}), min to max {calc[k]['min']/1e6:.1f} to {calc[k]['max']/1e6:.1f} ({calc[k]['rminmax']:.2f})" for k in calc))
sys.exit(1 if bad else 0)
