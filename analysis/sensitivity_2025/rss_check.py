#!/usr/bin/env python3
"""The quick range: does it match the Monte Carlo, and the likely range of every zone for the dashboard.
Usage: python3 analysis/sensitivity_2025/rss_check.py RELEASE [OAT_TAG [MC_TAG]]     (repository root)
  OAT_TAG  oat_RELEASE<OAT_TAG>.csv, the runs of `monte_carlo.mjs ... oat` (default ''; '_all' for the run with MC_ZONES=all MC_LONG=1)
  MC_TAG   monte_carlo_RELEASE<MC_TAG>_summary.csv, the Monte Carlo it is checked against (default = OAT_TAG); skipped if absent
Quick range: each uncertain choice is run over its range alone; the response is taken as piecewise linear between those runs; its mean and variance are taken under the choice's own distribution
(the one the Monte Carlo draws from); the effects of the choices are added (means) and combined in quadrature (variances); the 90% range is the mean plus and minus 1.645 standard deviations.
Writes quick_range_RELEASE<OAT_TAG>.csv (the comparison with the Monte Carlo) and, when results/RELEASE.csv exists, results/likely_range_RELEASE.csv: for every zone and preset the capacity,
its likely range at the release's defaults, and whether the population is robustly over capacity (above the whole range), robustly under (below it) or uncertain (inside it)."""
import csv, math, os, sys
REL = sys.argv[1]; OT = sys.argv[2] if len(sys.argv) > 2 else ''; MT = sys.argv[3] if len(sys.argv) > 3 else OT
oat = list(csv.DictReader(open(f'analysis/sensitivity_2025/oat_{REL}{OT}.csv'))); cols = [c for c in oat[0] if c not in ('input', 'value')]
base = {c: float(next(r for r in oat if r['input'] == 'base')[c]) for c in cols}
def tri_inv(u, a, c, b):
    f = (c - a) / (b - a); return a + math.sqrt(u * (b - a) * (c - a)) if u < f else b - math.sqrt((1 - u) * (b - a) * (b - c))
UNI = {'sf': (-1, 1), 'sh': (-1, 1), 'fuel': (2360, 2520), 'biofuel': (.0023, .005), 'timber': (.8, 1.0), 'orgfac': (.771, .845)}
TRI = {'meategg': (.115, .12, .13), 'redmeat': (.528, .578, .64), 'orgshare': (.02, .07, .12)}
DISCRETE = {'meat', 'restable'}                                  # equal chances over the runs
N = 4000
def pts_of(inp, col): return sorted((float(r['value']), float(r[col]) - base[col]) for r in oat if r['input'] == inp)
def effect_moments(inp, col):
    pts = pts_of(inp, col)
    if inp in DISCRETE:
        e = [f for _, f in pts]; m = sum(e) / len(e); return m, sum((x - m) ** 2 for x in e) / len(e)
    if inp in UNI: d = ('u',) + UNI[inp]
    elif inp in TRI: d = ('t',) + TRI[inp]
    else: d = ('t', pts[0][0], pts[1][0], pts[2][0])               # lfuel, lbench: triangular over the three runs (low, base, high)
    xs = [d[1] + ((i + .5) / N) * (d[2] - d[1]) if d[0] == 'u' else tri_inv((i + .5) / N, d[1], d[2], d[3]) for i in range(N)]
    def f(x):
        if x <= pts[0][0]: return pts[0][1]
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            if x <= x1: return y0 + (y1 - y0) * (x - x0) / (x1 - x0) if x1 > x0 else y0
        return pts[-1][1]
    ys = [f(x) for x in xs]; m = sum(ys) / N; return m, sum((y - m) ** 2 for y in ys) / N
inputs = sorted({r['input'] for r in oat if r['input'] != 'base'})
mcf = f'analysis/sensitivity_2025/monte_carlo_{REL}{MT}_summary.csv'
mc = {(r['zone'], r['setting']): r for r in csv.DictReader(open(mcf))} if os.path.exists(mcf) else {}
res = {}
if os.path.exists(f'results/{REL}.csv'):
    for r in csv.DictReader(open(f'results/{REL}.csv')): res[(r['zone'], r['preset'])] = r
out = [['zone', 'setting', 'base', 'quick_p5', 'quick_p95', 'mc_p5', 'mc_p50', 'mc_p95', 'quick_halfwidth', 'mc_halfwidth', 'halfwidth_ratio', 'top_driver']]
lik = [['release', 'zone', 'name', 'kind', 'preset', 'population', 'capacity', 'low', 'high', 'status', 'top_driver']]
ratios = []
print(f'{REL}{OT}: quick range' + (' against the Monte Carlo 90% range' if mc else ''))
for c in cols:
    z, k = c.split('_'); em = {i: effect_moments(i, c) for i in inputs}; mean = sum(m for m, _ in em.values()); sd = math.sqrt(sum(v for _, v in em.values()))
    top = max(inputs, key=lambda i: em[i][1]); lo, hi = base[c] + mean - 1.645 * sd, base[c] + mean + 1.645 * sd
    m = mc.get((z, k)); ratio = (hi - lo) / (float(m['p95']) - float(m['p5'])) if m else ''
    out.append([z, k, round(base[c]), round(lo), round(hi), m['p5'] if m else '', m['p50'] if m else '', m['p95'] if m else '', round((hi - lo) / 2), (float(m['p95']) - float(m['p5'])) / 2 if m else '', round(ratio, 3) if m else '', top])
    if m and base[c] > 3e5: ratios.append(ratio)
    r = res.get((z, k))
    if r:
        pop = float(r['population']); status = 'over' if pop > hi else 'under' if pop < lo else 'uncertain'
        lik.append([REL, z, r['name'], r['kind'], k, r['population'], r['capacity'], round(lo), round(hi), status, top])
    if z in ('1', '2', '26', '49') and m: print(f'  zone {z:>2} {k:5s} quick {lo/1e6:8.3f} to {hi/1e6:8.3f}   MC {float(m["p5"])/1e6:8.3f} to {float(m["p95"])/1e6:8.3f}   width ratio {ratio:.2f}   top: {top}')
if ratios: print(f'  width ratio over {len(ratios)} zone/settings with capacity over 300,000: min {min(ratios):.2f}, median {sorted(ratios)[len(ratios)//2]:.2f}, max {max(ratios):.2f}')
csv.writer(open(f'analysis/sensitivity_2025/quick_range_{REL}{OT}.csv', 'w', newline='')).writerows(out)
if len(lik) > 1 and OT:
    csv.writer(open(f'results/likely_range_{REL}.csv', 'w', newline='')).writerows(lik)
    cnt = {}
    for r in lik[1:]: cnt[(r[4], r[9])] = cnt.get((r[4], r[9]), 0) + 1
    print('  zone classes at the defaults:', dict(sorted(cnt.items())))
