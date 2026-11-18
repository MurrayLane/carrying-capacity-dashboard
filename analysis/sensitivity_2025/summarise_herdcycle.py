#!/usr/bin/env python3
"""B112: summarises a set of all-zones Monte Carlo draws into a ranges file in the format of results/ranges_<release>.csv, and writes the Australia table as Markdown.

Usage (repository root): python3 -I analysis/sensitivity_2025/summarise_herdcycle.py DRAWS.csv BASE_RESULTS.csv OUT_RANGES.csv OUT.md
  for example  analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_herdcycle_all.csv results/2025-fixed.csv results/ranges_2025-fixed_herdcycle.csv
               analysis/sensitivity_2025/monte_carlo_2025-fixed_herdcycle_all.md
Same rules as summarise_mc.py (percentiles by straight-line interpolation; first-order variance share from the mean of the output in groups of an input, less the
expected binning noise (groups - 1) / (N - 1)), with one change: an input with five or fewer distinct values (the meat window: three windows in the published run,
four or five in the herd-cycle runs) is grouped by its values, where summarise_mc.py does so only up to three values and would otherwise cut it into 20 bins.
With three meat windows this gives the published file exactly (checked in B112 on monte_carlo_draws_2025-fixed_all.csv against results/ranges_2025-fixed.csv).
It refuses to overwrite an existing output file."""
import csv, os, statistics, sys
DRAWS, BASE_CSV, OUT, MD = sys.argv[1:5]
for f in (OUT, MD):
    if os.path.exists(f): sys.exit(f'{f} exists; this script never overwrites an output (remove it yourself if you mean to regenerate it)')
rows = [{k: float(v) for k, v in r.items()} for r in csv.DictReader(open(DRAWS))]
N = len(rows); INPUTS = [c for c in rows[0] if not c[0].isdigit()]
NAME = {'sf': 'field-crop group factor (±14%)', 'sh': 'vegetable, fruit and nut factors (±20%)', 'meat': 'window of herd and meat data', 'meategg': 'meat and egg share of the diet',
        'redmeat': 'red meat share of the diet', 'fuel': 'liquid fuel per person', 'biofuel': 'biofuel share', 'timber': 'timber per person', 'orgfac': 'default organic yield factor',
        'orgshare': 'organic share of land (default and baseline)', 'restable': 'resilience table (all years or leave-one-out)', 'lfuel': 'long-term liquid fuel (156 to 253 L)', 'lbench': 'long-term feeding benchmark (30% to 52.5% of each stage)'}
def pct(v, q):
    s = sorted(v); i = q * (len(s) - 1); lo = int(i); hi = min(lo + 1, len(s) - 1); return s[lo] + (s[hi] - s[lo]) * (i - lo)
def first_order(x, y):
    var = statistics.pvariance(y)
    if var == 0: return 0.0
    if len(set(x)) <= 5: groups = [[i for i in range(len(y)) if x[i] == v] for v in sorted(set(x))]
    else:
        order = sorted(range(len(y)), key=lambda i: x[i]); groups = [order[g * len(y) // 20:(g + 1) * len(y) // 20] for g in range(20)]
    m = statistics.mean(y); raw = sum(len(g) * (statistics.mean(y[i] for i in g) - m) ** 2 for g in groups if g) / (len(y) * var)
    return max(0.0, raw - (len(groups) - 1) / (len(y) - 1))
base = {(int(r['zone']), r['preset']): float(r['capacity']) for r in csv.DictReader(open(BASE_CSV))}
out = [['zone', 'setting', 'p5', 'p25', 'p50', 'p75', 'p95', 'base'] + ['influence_' + k for k in INPUTS]]
for z in sorted({int(c.split('_')[0]) for c in rows[0] if c[0].isdigit()}):
    for k in ('short', 'long'):
        y = [r[f'{z}_{k}'] for r in rows]
        out.append([z, k] + [round(pct(y, q)) for q in (.05, .25, .5, .75, .95)] + [round(base[(z, k)])] + [round(first_order([r[i] for r in rows], y), 3) for i in INPUTS])
with open(OUT, 'w', newline='') as f: csv.writer(f).writerows(out)
S = {(r[0], r[1]): r for r in out[1:]}; a = lambda v: f'{v / 1e6:.1f}'
md = [f'{N} random draws (Latin hypercube) of the {len(INPUTS)} uncertain choices (`{DRAWS}`). Capacity in millions of people; the 90% range is the 5th to the 95th percentile of the draws.', '',
      '| Zone | Short term: median | 90% range | base | Long term: median | 90% range | base |', '|---|---|---|---|---|---|---|']
s, l = S[(1, 'short')], S[(1, 'long')]
md.append(f'| Australia | {a(s[4])} | {a(s[2])} to {a(s[6])} | {a(s[7])} | {a(l[4])} | {a(l[2])} to {a(l[6])} | {a(l[7])} |')
md += ['', "Share of the variance of Australia's capacity explained by each choice alone:", '', '| Choice | Short term | Long term |', '|---|---|---|']
inf = lambda k, key: S[(1, k)][8 + INPUTS.index(key)]
for key in sorted(INPUTS, key=lambda i: -max(inf('short', i), inf('long', i))): md.append(f'| {NAME[key]} | {inf("short", key) * 100:.0f}% | {inf("long", key) * 100:.0f}% |')
tot = lambda k: sum(inf(k, i) for i in INPUTS)
md += ['', f'The {len(INPUTS)} choices alone explain {tot("short") * 100:.0f}% of the short-term and {tot("long") * 100:.0f}% of the long-term variance; the rest is interaction.']
open(MD, 'w').write('\n'.join(md) + '\n'); print('\n'.join(md))
