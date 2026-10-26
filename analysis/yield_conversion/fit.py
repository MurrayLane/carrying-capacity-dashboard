import json, random, statistics, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(os.path.join(HERE, 'pairs.json')))
SEED = {'Wheat': .067, 'Oats': .043, 'Barley': .045, 'Sorghum': .007, 'Maize': .022, 'Rice': .148, 'Canola': .003, 'Potatoes': 3.0, 'Sugar cane': 0.0}
def ols(x, y):
    n = len(x); mx, my = sum(x) / n, sum(y) / n; sxx = sum((a - mx) ** 2 for a in x)
    if sxx == 0: return None
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sxx; return k, my - k * mx
def cluster_boot(pairs, B=4000, seed=7):
    """pairs: list of (region, s, d). Resample regions with replacement."""
    by = collections.defaultdict(list)
    for rid, s, d in pairs: by[rid].append((s, d))
    regs = list(by); random.seed(seed); ks = []; ints = []
    for _ in range(B):
        samp = [p for rid in (random.choice(regs) for _ in regs) for p in by[rid]]
        r = ols([a for a, _ in samp], [b for _, b in samp])
        if r: ks.append(r[0]); ints.append(r[1])
    ks.sort(); ints.sort(); q = lambda v, p: v[int(p * len(v))]
    return q(ks, .025), q(ks, .5), q(ks, .975), q(ints, .025), q(ints, .975), sum(k <= 0 for k in ks) / len(ks)
good = [r for r in rows if r['n'] == 4 and r['spread'] < 0.6 and r['F'] > 0 and r['raw'] > 0]
print('low-noise subset: %d pairs from %d regions; crops %s' % (len(good), len({r['rid'] for r in good}), dict(collections.Counter(r['crop'] for r in good))))
variants = {'H1  (raw - seed)/F - 1   [seed deducted in t/ha]': lambda r: (r['raw'] - SEED[r['crop']] * 100) / r['F'] - 1,
            'H3  raw/F - 1            [no seed deduction]':    lambda r: r['raw'] / r['F'] - 1}
for name, f in variants.items():
    pr = [(r['rid'], r['s'], f(r)) for r in good]; pr = [p for p in pr if -0.5 < p[2] < 1]
    k, a0 = ols([p[1] for p in pr], [p[2] for p in pr]); lo, med, hi, ilo, ihi, p0 = cluster_boot(pr)
    print(f'{name}\n    k = {k:.2f}  95% interval {lo:.2f} to {hi:.2f}  P(k<=0)={p0:.3f}   intercept {a0:+.3f}  95% interval {ilo:+.3f} to {ihi:+.3f}')
# same on all pairs for comparison
pr = [(r['rid'], r['s'], (r['raw'] - SEED[r['crop']] * 100) / r['F'] - 1) for r in rows if r['F'] > 0 and r['raw'] > 0]; pr = [p for p in pr if -0.5 < p[2] < 1]
lo, med, hi, ilo, ihi, p0 = cluster_boot(pr); print(f'H1 on all {len(pr)} pairs: k interval {lo:.2f} to {hi:.2f}, median {med:.2f}, P(k<=0) {p0:.3f}')
# write the evidence table
import csv
with open(os.path.join(HERE, 'pairs.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['crop', 'region_id', 'state', 'years_available', 'abs_raw_avg_g_m2', 'yearly_spread', 'workbook_F_g_m2', 'irrigation_share', 'seed_t_ha', 'D_H1'])
    for r in rows: w.writerow([r['crop'], r['rid'], r['state'], r['n'], round(r['raw'], 2), round(r['spread'], 3), round(r['F'], 2), r['s'], SEED[r['crop']], round((r['raw'] - SEED[r['crop']] * 100) / r['F'] - 1, 4)])
print('wrote pairs.csv with', len(rows), 'rows')
