"""B114 (decision 107), step 2 of 2: the corrected 2025 model with the pairing of pasture-fed food with crops relaxed three ways.

Reads pairing_relaxed_inputs_<release>.csv and pairing_relaxed_meatscan_<release>.csv (written by pairing_relaxed_inputs.mjs from the
evaluator, unchanged) and writes pairing_relaxed.csv (variant; preset; capacity; change from base; which land binds; plus the
diet's energy and protein, the gap closed to the adjusted footprint and HALF readings, and how each figure was obtained).

How the model pairs the two kinds of land (Settings!C57:D62 of the workbook): cropland and pasture form one pool; the cropland a
person needs (crops, crop-fed meat, crop fibre, biofuel) must fit the existing cropland; cropland the crops do not need is handed to
pasture square metre for square metre, at pasture's own output; pasture can never grow crops. Capacity is the largest population
for which both hold. Every variant below keeps that frame and changes one thing:

  base  the model as it is (must reproduce the evaluator's capacity: the first check).
  1     pasture-fed meat and dairy may substitute into cropland at the crop-equivalent energy rate: the pasture-fed meat and dairy
        that the existing pasture cannot carry is replaced, kilojoule for kilojoule, by more of the diet's own cropland foods in
        their present proportions. Equivalently, one square metre of cropland not needed for crops stands in for k square metres
        of pasture, k being the food energy a square metre of cropland gives in the diet's cropland foods over the food energy a
        square metre of pasture gives in its pasture-fed meat and dairy. Energy is held; protein follows the swap and is reported.
        Variant 1p uses the plant foods alone as the replacement (a higher k).
  2     the diet's meat-and-egg share falls to what the existing pasture can carry while cropland feeds the rest: the model's own
        diet family (Settings!B10, 0.5% grid) through the evaluator, the population split between the two neighbouring diets of
        the family at which pasture stops binding, so that cropland and pasture are both full.
  3     a free allocation of land among food groups that maximises people with at least the diet's energy and protein: each food
        group's amount is free between 0 and 3 times its present amount (the guard of analysis/nutrition_lp_2025), land rules as
        the model's. 3u: the same with no upper limit (a bound, not a diet). Groups whose land is zero (recycled feed in the
        long term) stay at their present amount, as their supply is set by the waste recycled.

Readings compared (short term only; column (e) of Table 5 is an average-year reading on the present diet, so the long term has none):
the footprint at local productivity, build 1 64.8 and build 3 84.6 million (B270), and HALF at local productivity 76.0 million
(B272; other defensible readings 73.7 to 79.3). Gap closed = (variant - base) / (reading - base).

Run from the repository root:
  node analysis/pasture_2025/pairing_relaxed_inputs.mjs && python3 analysis/pasture_2025/pairing_relaxed.py
  python3 analysis/pasture_2025/pairing_relaxed.py --wrong-value-demo     shows the base check failing on a planted wrong value
"""
import csv
import os
import sys

import numpy as np
from scipy.optimize import linprog

HERE = os.path.dirname(os.path.abspath(__file__))
RELEASE = '2025-fixed'
READINGS = [('footprint build 1 (B270)', 64.8), ('HALF (B272)', 76.0), ('footprint build 3 (B270)', 84.6)]
CAP = 3.0
TOL = 1e-6


def read(name):
    with open(os.path.join(HERE, name), newline='') as f:
        return list(csv.DictReader(f))


def load(preset):
    rows = [r for r in read(f'pairing_relaxed_inputs_{RELEASE}.csv') if r['preset'] == preset]
    by = {r['item']: r for r in rows}
    num = lambda r, k: float(r[k])
    groups = [r for r in rows if not r['item'].startswith(('nonfood_', 'model_', 'land_', 'preset_'))]
    g = {
        'name': [r['item'] for r in groups],
        'c': np.array([num(r, 'cropland_m2_pp') for r in groups]),
        'p': np.array([num(r, 'pasture_m2_pp') for r in groups]),
        'e': np.array([num(r, 'energy_kj_pd') for r in groups]),
        'q': np.array([num(r, 'protein_g_pd') for r in groups]),
    }
    nf = [by[k] for k in ('nonfood_biofuel', 'nonfood_textiles', 'nonfood_timber_infrastructure')]
    g['c_nf'] = sum(num(r, 'cropland_m2_pp') for r in nf)
    g['p_nf'] = sum(num(r, 'pasture_m2_pp') for r in nf)
    g['o_nf'] = sum(num(r, 'other_m2_pp') for r in nf)
    land = by['land_km2']
    g['C'], g['P'], g['O'] = num(land, 'cropland_m2_pp'), num(land, 'pasture_m2_pp'), num(land, 'other_m2_pp')
    g['model_capacity'] = num(by['model_capacity'], 'cropland_m2_pp') / 1e6
    g['model_need'] = by['model_total_need']
    # The diet's energy and protein are the sums of the groups (the csv rounds to 10 figures; the sums agree with the evaluator's totals to 1e-4).
    g['E0'], g['Q0'] = float(g['e'].sum()), float(g['q'].sum())
    for tot, key in ((g['E0'], 'energy_kj_pd'), (g['Q0'], 'protein_g_pd')):
        assert abs(tot - num(by['model_total_need'], key)) <= 1e-4 * tot, key
    g['meategg'] = num(by['preset_meategg'], 'cropland_m2_pp')
    return g


def solve(g, lo, hi, k):
    """Largest population (million) with group amounts s (multiples of the present amounts) in [lo, hi].
    Variables x = (s_1..s_n, t), t = 1 / population in millions; minimise t. Land in km2, needs in m2 a person: need x million = km2.
      cropland:  sum s c + c_nf                         <= C t
      pool:      sum s p + p_nf + k (sum s c + c_nf)     <= P t + k C t     (idle cropland stands in for k m2 of pasture; k = 1 in the model)
      other:     o_nf                                    <= O t
      energy and protein at least the diet's."""
    n = len(g['c'])
    A, b = [], []
    A.append(list(g['c']) + [-g['C']]); b.append(-g['c_nf'])
    A.append(list(g['p'] + k * g['c']) + [-(g['P'] + k * g['C'])]); b.append(-(g['p_nf'] + k * g['c_nf']))
    A.append([0] * n + [-g['O']]); b.append(-g['o_nf'])
    A.append(list(-g['e']) + [0]); b.append(-g['E0'] * (1 - 1e-12))
    A.append(list(-g['q']) + [0]); b.append(-g['Q0'] * (1 - 1e-12))
    bounds = [(lo[i], hi[i]) for i in range(n)] + [(1e-9, None)]
    res = linprog([0] * n + [1], A_ub=A, b_ub=b, bounds=bounds, method='highs')
    if res.status != 0:
        raise RuntimeError(res.message)
    s, t = res.x[:n], res.x[n]
    return 1 / t, s, describe(g, s, 1 / t, k)


def describe(g, s, N, k):
    crop = (s @ g['c'] + g['c_nf']) * N             # km2 of cropland used for crops
    past = (s @ g['p'] + g['p_nf']) * N             # km2 of pasture use
    idle = g['C'] - crop
    pool_slack = g['P'] + k * idle - past           # pasture equivalent left over
    crop_full = idle <= TOL * g['C']
    past_full = pool_slack <= TOL * g['P']
    other_full = g['O'] - g['o_nf'] * N <= TOL * g['O']
    if other_full:
        bind = 'other land (timber and infrastructure)'
    elif crop_full and past_full:
        bind = 'cropland and pasture both full'
    elif crop_full:
        bind = 'cropland (pasture idle: %.0f km2)' % (pool_slack)
    elif k == 1:
        bind = 'pasture (with the %.0f km2 of cropland the crops leave idle ceded to it)' % idle
    else:
        bind = 'pasture (with the %.0f km2 of cropland the crops leave idle standing in for it at k = %.1f)' % (idle, k)
    return {'bind': bind, 'crop_km2': crop, 'past_km2': past, 'idle_crop_km2': idle,
            'energy': float(s @ g['e']), 'protein': float(s @ g['q'])}


def swap_diet(g, d, N, k, mask):
    """Variant 1 read as a diet: the share x of pasture-fed food energy grown instead as the cropland foods in mask."""
    pm = g['p'] > 0
    x = k * d['idle_crop_km2'] / (N * g['p'][pm].sum())          # pasture-equivalent km2 supplied by cropland over pasture-fed food need
    e_p, q_p = g['e'][pm].sum(), g['q'][pm].sum()
    q_per_kj = g['q'][mask].sum() / g['e'][mask].sum()
    d = dict(d)
    d['protein'] = g['Q0'] - x * q_p + x * e_p * q_per_kj
    d['energy'] = g['E0']
    d['bind'] = ('cropland and pasture both full: pasture carries %.0f%% of the pasture-fed meat and dairy, the other %.0f%% of its energy is '
                 'grown as cropland foods on the %.0f km2 of cropland the crops would leave idle' % (100 * (1 - x), 100 * x, d['idle_crop_km2']))
    return d, x


def crop_rate_k(g, plant_only):
    """Food energy per m2 of cropland in the diet's cropland foods over that of pasture in its pasture-fed meat and dairy
    (kJ a year per m2: kJ a day a person times 365.25 over m2 a person). Groups with no cropland (recycled feed) are left out."""
    animal = {'red_meat_crop_fed', 'white_meat_eggs'}
    cm = np.array([c > 0 and (not plant_only or nm not in animal) for nm, c in zip(g['name'], g['c'])])
    pm = g['p'] > 0
    crop_kj_m2 = 365.25 * g['e'][cm].sum() / g['c'][cm].sum()
    past_kj_m2 = 365.25 * g['e'][pm].sum() / g['p'][pm].sum()
    return crop_kj_m2 / past_kj_m2, crop_kj_m2, past_kj_m2, cm


def variant2(preset, g):
    scan = [r for r in read(f'pairing_relaxed_meatscan_{RELEASE}.csv') if r['preset'] == preset]
    scan.sort(key=lambda r: float(r['meategg']))
    # Highest meat share whose diet leaves pasture idle (cropland binds), and the next one up (pasture binds).
    i = max(j for j, r in enumerate(scan) if r['binding'] == 'cropland')
    lo_d, hi_d = scan[i], scan[i + 1]
    assert hi_d['binding'] == 'pasture'
    c = np.array([float(lo_d['cropland_m2_pp']), float(hi_d['cropland_m2_pp'])])
    p = np.array([float(lo_d['pasture_m2_pp']), float(hi_d['pasture_m2_pp'])])
    # People (million) on each of the two diets: both lands full.  c.n = C ; (c + p).n = C + P
    n = np.linalg.solve(np.array([c, c + p]), np.array([g['C'], g['C'] + g['P']]))
    assert (n > 0).all()
    N = n.sum()
    w = n / N
    mg = w @ [float(lo_d['meategg']), float(hi_d['meategg'])]
    en = w @ [float(lo_d['energy_kj_pd']), float(hi_d['energy_kj_pd'])]
    pr = w @ [float(lo_d['protein_g_pd']), float(hi_d['protein_g_pd'])]
    best = max(scan, key=lambda r: float(r['capacity']))
    note = ('model diet family through the evaluator: %.1f%% of people on the %.1f%% meat-and-egg diet (%.2f M alone, cropland binds) and %.1f%% on the %.1f%% diet (%.2f M alone, pasture binds); '
            'effective meat-and-egg share %.2f%% against %.1f%%. The best single diet of the family on the grid is %.1f%% at %.2f M (%s binds)'
            % (100 * w[0], 100 * float(lo_d['meategg']), float(lo_d['capacity']) / 1e6, 100 * w[1], 100 * float(hi_d['meategg']), float(hi_d['capacity']) / 1e6,
               100 * mg, 100 * g['meategg'], 100 * float(best['meategg']), float(best['capacity']) / 1e6, best['binding']))
    return N, {'bind': 'cropland and pasture both full', 'energy': en, 'protein': pr}, note, scan


def gap_text(N, base):
    parts = []
    for name, v in READINGS:
        share = (N - base) / (v - base)
        parts.append('%s %.1f: %s (%.0f%% of the gap)' % (name, v, 'closes' if N >= v else 'does not close', 100 * share))
    return '; '.join(parts)


def check_base(N, g, label='base'):
    """The closed form must give the evaluator's own capacity (and results/2025-fixed.csv), to 1e-6."""
    ref = g['model_capacity']
    with open(os.path.join(HERE, '..', '..', 'results', f'{RELEASE}.csv'), newline='') as f:
        res = [r for r in csv.DictReader(f) if r['zone'] == '1' and r['preset'] == g['preset']]
    pub = float(res[0]['capacity']) / 1e6
    ok = abs(N - ref) <= 1e-6 * ref and abs(N - pub) <= 1e-6 * pub
    print('%s check, %s: closed form %.6f M, evaluator %.6f M, results/%s.csv %.6f M: %s' % (label, g['preset'], N, ref, RELEASE, pub, 'PASS' if ok else 'FAIL'))
    return ok


def check_feasible(g, s, N, k, label):
    """Recompute every constraint from the solution, independently of the solver's own report."""
    crop = (s @ g['c'] + g['c_nf']) * N
    past = (s @ g['p'] + g['p_nf']) * N
    ok = crop <= g['C'] * (1 + 1e-7) and past <= g['P'] + k * (g['C'] - crop) + 1e-7 * g['P'] and \
        g['o_nf'] * N <= g['O'] * (1 + 1e-7) and s @ g['e'] >= g['E0'] * (1 - 1e-7) and s @ g['q'] >= g['Q0'] * (1 - 1e-7)
    if not ok:
        print('feasibility check FAILED for', label)
    return ok


def main():
    if '--wrong-value-demo' in sys.argv:
        g = load('short'); g['preset'] = 'short'
        print('EXAMPLE (deliberate wrong value): the base capacity given as 41.6 instead of the closed form')
        ok = check_base(41.6, g, label='EXAMPLE wrong value')
        sys.exit(0 if not ok else 1)
    out = [['release', 'variant', 'preset', 'capacity_million', 'change_from_base_million', 'change_from_base_pct', 'which_land_binds',
            'energy_kj_pd', 'protein_g_pd', 'gap_to_adjusted_footprint_and_half', 'how']]
    allok = True
    for preset in ('short', 'long'):
        g = load(preset); g['preset'] = preset
        n = len(g['c'])
        one = np.ones(n)
        N0, s0, d0 = solve(g, one, one, 1.0)
        allok &= check_base(N0, g)
        rows = [('base', N0, d0, 'the model as it is: closed form of Settings!C57:D62, equal to the evaluator')]
        for tag, plant in (('1', False), ('1p', True)):
            k, ckj, pkj, cm = crop_rate_k(g, plant)
            N, s, d = solve(g, one, one, k)
            allok &= check_feasible(g, s, N, k, tag)
            d, x = swap_diet(g, d, N, k, cm)
            rows.append((tag, N, d, 'pasture-fed meat and dairy replaced kJ for kJ by %s foods where pasture runs out: k = %.1f (%s foods %.0f kJ of food a year per m2 of cropland; pasture-fed meat and dairy %.2f kJ per m2 of pasture); same capacity as pooling the two lands at that rate'
                         % ('the diet\'s cropland plant' if plant else 'the diet\'s cropland', k, 'cropland plant' if plant else 'all cropland', ckj, pkj)))
        N2, d2, note2, _ = variant2(preset, g)
        rows.append(('2', N2, d2, note2))
        fixed = g['c'] + g['p'] == 0
        hi = np.where(fixed, 1.0, CAP); lo = np.where(fixed, 1.0, 0.0)
        for tag, h in (('3', hi), ('3u', np.where(fixed, 1.0, np.inf))):
            N, s, d = solve(g, lo, h, 1.0)
            allok &= check_feasible(g, s, N, 1.0, tag)
            mix = ', '.join('%s x%.2f' % (nm, v) for nm, v in zip(g['name'], s) if abs(v - 1) > 1e-6)
            rows.append((tag, N, d, 'linear program over food-group amounts, %s; energy and protein at least the diet\'s; groups changed: %s'
                         % ('each 0 to 3 times its present amount' if tag == '3' else 'no upper limit (a bound)', mix or 'none')))
        for tag, N, d, how in rows:
            gap = gap_text(N, N0) if preset == 'short' and tag != 'base' else ('' if tag == 'base' else 'no long-term reading in column (e)')
            out.append([RELEASE, tag, preset, '%.2f' % N, '%.2f' % (N - N0), '%.1f' % (100 * (N / N0 - 1)), d['bind'],
                        '%.0f' % d['energy'], '%.1f' % d['protein'], gap, how])
    with open(os.path.join(HERE, 'pairing_relaxed.csv'), 'w', newline='') as f:
        csv.writer(f, lineterminator='\n').writerows(out)
    for r in out:
        print(' | '.join(r[1:10]))
    if not allok:
        sys.exit('a check failed')


if __name__ == '__main__':
    main()
