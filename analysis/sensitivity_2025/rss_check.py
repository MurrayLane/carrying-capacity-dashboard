#!/usr/bin/env python3
"""Does a quick range from 28 runs match the 1,000-draw Monte Carlo?   Usage: python3 analysis/sensitivity_2025/rss_check.py RELEASE   (repository root; needs oat_RELEASE.csv from `monte_carlo.mjs ... oat` and the Monte Carlo summary)
Quick range: each uncertain choice is run over its range alone (oat_RELEASE.csv); the response is taken as piecewise linear between those runs; its mean and variance are taken under the choice's own distribution (the one the Monte Carlo draws from);
the effects of the ten choices are added (means) and combined in quadrature (variances), and the 90% range is the mean plus and minus 1.645 standard deviations.
Writes quick_range_RELEASE.csv with the quick range, the Monte Carlo percentiles and the difference."""
import csv, math, sys
REL = sys.argv[1]
oat = list(csv.DictReader(open(f'analysis/sensitivity_2025/oat_{REL}.csv'))); cols = [c for c in oat[0] if c not in ('input', 'value')]
base = {c: float(next(r for r in oat if r['input'] == 'base')[c]) for c in cols}
def tri_inv(u, a, c, b):
    f = (c - a) / (b - a); return a + math.sqrt(u * (b - a) * (c - a)) if u < f else b - math.sqrt((1 - u) * (b - a) * (b - c))
DIST = {'sf': ('u', -1, 1), 'sh': ('u', -1, 1), 'meategg': ('t', .115, .12, .13), 'redmeat': ('t', .528, .578, .64), 'fuel': ('u', 2360, 2520), 'biofuel': ('u', .0023, .005),
        'timber': ('u', .8, 1.0), 'orgfac': ('u', .771, .845), 'orgshare': ('t', .02, .07, .12)}
N = 4000
def effect_moments(inp, col):
    pts = sorted((float(r['value']), float(r[col]) - base[col]) for r in oat if r['input'] == inp)
    if inp == 'meat':                                            # discrete, equal chances
        e = [f for _, f in pts]; m = sum(e) / len(e); return m, sum((x - m) ** 2 for x in e) / len(e)
    if inp in ('sf', 'sh'):                                      # the draw is |s| times the run at +1 or -1 depending on the sign: piecewise linear through 0 at the base
        pts = sorted(pts)
    d = DIST[inp]; xs = []
    for i in range(N):
        u = (i + .5) / N; xs.append(d[1] + u * (d[2] - d[1]) if d[0] == 'u' else tri_inv(u, d[1], d[2], d[3]))
    def f(x):
        if x <= pts[0][0]: return pts[0][1]
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            if x <= x1: return y0 + (y1 - y0) * (x - x0) / (x1 - x0) if x1 > x0 else y0
        return pts[-1][1]
    ys = [f(x) for x in xs]; m = sum(ys) / N; return m, sum((y - m) ** 2 for y in ys) / N
mc = {(r['zone'], r['setting']): r for r in csv.DictReader(open(f'analysis/sensitivity_2025/monte_carlo_{REL}_summary.csv'))}
inputs = sorted({r['input'] for r in oat if r['input'] != 'base'})
out = [['zone', 'setting', 'base', 'quick_p5', 'quick_p95', 'mc_p5', 'mc_p50', 'mc_p95', 'quick_halfwidth', 'mc_halfwidth', 'halfwidth_ratio', 'top_driver']]
print(f'{REL}: quick range against Monte Carlo 90% range (millions; zone 1 = Australia)')
for c in cols:
    z, k = c.split('_'); mean = sum(effect_moments(i, c)[0] for i in inputs); var = sum(effect_moments(i, c)[1] for i in inputs); sd = math.sqrt(var)
    top = max(inputs, key=lambda i: effect_moments(i, c)[1]); lo, hi = base[c] + mean - 1.645 * sd, base[c] + mean + 1.645 * sd; m = mc[(z, k)]
    out.append([z, k, round(base[c]), round(lo), round(hi), m['p5'], m['p50'], m['p95'], round((hi - lo) / 2), (float(m['p95']) - float(m['p5'])) / 2, round((hi - lo) / (float(m['p95']) - float(m['p5'])), 3), top])
    if z in ('1', '2', '26', '49', '60'): print(f'  zone {z:>2} {k:5s} quick {lo/1e6:8.3f} to {hi/1e6:8.3f}   MC {float(m["p5"])/1e6:8.3f} to {float(m["p95"])/1e6:8.3f}   width ratio {(hi-lo)/(float(m["p95"])-float(m["p5"])):.2f}   top: {top}')
csv.writer(open(f'analysis/sensitivity_2025/quick_range_{REL}.csv', 'w', newline='')).writerows(out)
