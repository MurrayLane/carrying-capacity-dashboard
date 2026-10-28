#!/usr/bin/env python3
"""Summarises monte_carlo_draws.csv: ranges for Australia and the states, and which choice drives the spread.

Usage: python3 analysis/sensitivity_2025/summarise_mc.py [DRAWS.csv TAG [RESULTS.csv]]   (from the repository root; RESULTS.csv is a results/<release>.csv whose capacities are the base column, for draws made on another release; writes monte_carlo<TAG>_summary.csv and monte_carlo<TAG>.md; the long-window run is DRAWS monte_carlo_draws_longwindow.csv, TAG _longwindow)
Ranges: the 5th, 25th, 50th, 75th and 95th percentiles of the draws.
Influence: the share of the variance of the output explained by one input alone (first-order index), estimated from the mean of the output in 20 equal-count
bins of that input (3 groups for the meat window). The expected noise of the binning, (bins - 1) / (N - 1) for each input, is taken off. The shares of the inputs add to about 100% when the choices act separately; the rest is interaction.
"""
import csv, statistics, sys
DRAWS = sys.argv[1] if len(sys.argv) > 1 else 'analysis/sensitivity_2025/monte_carlo_draws.csv'; TAG = sys.argv[2] if len(sys.argv) > 2 else ''; BASE_CSV = sys.argv[3] if len(sys.argv) > 3 else None
rows = [{k: float(v) for k, v in r.items()} for r in csv.DictReader(open(DRAWS))]
N = len(rows)
INPUTS = ['sf', 'sh', 'meat', 'meategg', 'redmeat', 'fuel', 'biofuel', 'timber', 'orgfac', 'orgshare']
NAME = {'sf': 'field-crop group factor (±14%)', 'sh': 'vegetable, fruit and nut factors (±20%)', 'meat': 'window of herd and meat data', 'meategg': 'meat and egg share of the diet',
        'redmeat': 'red meat share of the diet', 'fuel': 'liquid fuel per person', 'biofuel': 'biofuel share', 'timber': 'timber per person', 'orgfac': 'default organic yield factor',
        'orgshare': 'organic share of land (default and baseline)'}
ZONE = {1: 'Australia', 2: 'NSW and ACT', 15: 'Victoria', 26: 'Queensland', 40: 'South Australia', 49: 'Western Australia', 56: 'Tasmania', 60: 'Northern Territory'}
def pct(v, q):
    s = sorted(v); i = q * (len(s) - 1); lo = int(i); hi = min(lo + 1, len(s) - 1); return s[lo] + (s[hi] - s[lo]) * (i - lo)
def first_order(x, y):
    var = statistics.pvariance(y)
    if var == 0: return 0.0
    if len(set(x)) <= 3: groups = [[i for i in range(len(y)) if x[i] == v] for v in sorted(set(x))]
    else:
        order = sorted(range(len(y)), key=lambda i: x[i]); groups = [order[g * len(y) // 20:(g + 1) * len(y) // 20] for g in range(20)]
    m = statistics.mean(y); raw = sum(len(g) * (statistics.mean(y[i] for i in g) - m) ** 2 for g in groups if g) / (len(y) * var)
    return max(0.0, raw - (len(groups) - 1) / (len(y) - 1))           # binning adds (groups - 1) / (N - 1) of noise to every input; take it off
out = [['zone', 'setting', 'p5', 'p25', 'p50', 'p75', 'p95', 'base'] + ['influence_' + k for k in INPUTS]]
base = {}
if BASE_CSV:
    for r in csv.DictReader(open(BASE_CSV)): base[(int(r['zone']), r['preset'])] = float(r['capacity'])
else:
    for r in csv.DictReader(open('analysis/sensitivity_2025/results.csv')):
        if r['id'] == 'base': base[(int(r['zone']), r['preset'])] = float(r['capacity'])
for z in ZONE:
    for k in ('short', 'long'):
        y = [r[f'{z}_{k}'] for r in rows]
        out.append([z, k] + [round(pct(y, q)) for q in (.05, .25, .5, .75, .95)] + [round(base[(z, k)])] + [round(first_order([r[i] for r in rows], y), 3) for i in INPUTS])
with open(f'analysis/sensitivity_2025/monte_carlo{TAG}_summary.csv', 'w', newline='') as f: csv.writer(f).writerows(out)
S = {(r[0], r[1]): r for r in out[1:]}
def m(v): return f'{v / 1e6:.1f}'
md = [f'{N} random draws (Latin hypercube) of the ten uncertain choices. Capacity in millions of people; the 90% range is the 5th to the 95th percentile of the draws.', '',
      '| Zone | Short term: median | 90% range | base | Long term: median | 90% range | base |', '|---|---|---|---|---|---|---|']
for z, n in ZONE.items():
    s, l = S[(z, 'short')], S[(z, 'long')]
    f = (lambda v: m(v)) if z == 1 else (lambda v: f'{v / 1e6:.2f}')
    md.append(f'| {n} | {f(s[4])} | {f(s[2])} to {f(s[6])} | {f(s[7])} | {f(l[4])} | {f(l[2])} to {f(l[6])} | {f(l[7])} |')
md += ['', 'Share of the variance of Australia\'s capacity explained by each choice alone:', '', '| Choice | Short term | Long term |', '|---|---|---|']
inf = lambda k, key: S[(1, k)][8 + INPUTS.index(key)]
for key in sorted(INPUTS, key=lambda i: -max(inf('short', i), inf('long', i))):
    md.append(f'| {NAME[key]} | {inf("short", key) * 100:.0f}% | {inf("long", key) * 100:.0f}% |')
tot = lambda k: sum(inf(k, i) for i in INPUTS)
md += ['', f'The ten choices alone explain {tot("short") * 100:.0f}% of the short-term and {tot("long") * 100:.0f}% of the long-term variance; the rest is interaction.']
open(f'analysis/sensitivity_2025/monte_carlo{TAG}.md', 'w').write('\n'.join(md) + '\n'); print('\n'.join(md))
