#!/usr/bin/env python3
"""Robustness of the shares closed by harmonisation (brief B135; decision 142; Paper B, section 5.11 and Table 6).
Usage (repository root): python3 -I analysis/method_tests_2025/harmonised_robustness.py
Reads harmonised_comparison.csv, model_entry.csv (as written by their own scripts) and, to check the paper's figures, harmonised_comparison_lines.csv.
Writes harmonised_robustness.csv only. It does not touch harmonised_lines.py or any other output.
The paired set, the two lines, the distance, the share closed and the dispersion measures are those of harmonised_lines.py (see its docstring); this script
rebuilds them (same rules) and repeats them under variants. It stops if the base case does not give the paper's 4.1% and 38.5% and the 31.8% / 28.4% narrowing
printed in harmonised_comparison_lines.csv.
Variants: the reference (31.1, 41.5, 49.2, 53.6; the median and the geometric mean of the method centres, formed as run and harmonised); each method left out in
turn; the fish reading dropped; the pasture-alone readings of the footprint dropped; a method's centre as the median of its readings in place of the geometric mean;
the energy balance alone and with the footprint; the land scale-up readings classed as method (the scaled energy readings are kept at their as-run value on
harmonising; also the scaled people-per-hectare reading, as a second variant)."""
import csv, math, statistics
D = 'analysis/method_tests_2025/'
def dicts(p): return list(csv.DictReader(open(p, newline='')))
HC = dicts(D + 'harmonised_comparison.csv'); K = list(HC[0].keys()); A, B, E = K[2], K[3], K[10]
M_FIX = float([r for r in dicts(D + 'model_entry.csv') if r['release'] == '2025-fixed'][0]['short term (million)'])
LOCAL = ('Ecological footprint, food row (Simpson)', 'HALF index (Alexander)')
EN, FPm, HA, PH, CB = ('Energy and protein balance (Gifford; Henry and Godden)', 'Ecological footprint, food row (Simpson)', 'HALF index (Alexander)',
                       'People per hectare (Cassidy)', 'Commodity balance (Foran and Poldy)')
def num(s): return None if s == '' else float(s)
LINES = {'a': 'a', 'b': 'b'}
def base_pairs(key):
    by = {}
    for r in HC:
        m = r['method']
        if m.startswith(('The model', 'Summary', 'Failure probability')): continue
        a = num(r[A])
        h = num(r[E]) if (m in LOCAL and key == 'b') else (num(r[B]) if r[K[4]] != '' else None)
        if a is None or h is None: continue
        by.setdefault(m, []).append((r['reading'], a, h))
    return by
def gm(xs): return math.exp(sum(math.log(x) for x in xs) / len(xs))
def med(xs): return statistics.median(xs)
def sdl(xs): return statistics.pstdev([math.log(x) for x in xs])
def measure(by, ref, centre='gm'):
    """ref: a number, 'median' or 'gmean' (of the method centres). Returns dict of the measures for this set of paired readings."""
    cf = gm if centre == 'gm' else med
    ca = {m: cf([a for _, a, _ in v]) for m, v in by.items()}; ch = {m: cf([h for _, _, h in v]) for m, v in by.items()}
    if isinstance(ref, float): ra = rh = ref
    elif ref == 'median': ra, rh = med(list(ca.values())), med(list(ch.values()))
    else: ra, rh = gm(list(ca.values())), gm(list(ch.values()))
    Da = sum(sum(abs(math.log(a / ra)) for _, a, _ in v) / len(v) for v in by.values())
    Dh = sum(sum(abs(math.log(h / rh)) for _, _, h in v) / len(v) for v in by.values())
    xa, xh = list(ca.values()), list(ch.values())
    ra_all = [a for v in by.values() for _, a, _ in v]; rh_all = [h for v in by.values() for _, _, h in v]
    out = dict(share=(Da - Dh) / Da if Da else float('nan'), n=len(by), nread=len(ra_all))
    if len(xa) > 1:
        out.update(sd_a=sdl(xa), sd_h=sdl(xh), qa=max(xa) / min(xa), qh=max(xh) / min(xh))
    out.update(rsd_a=sdl(ra_all), rsd_h=sdl(rh_all), rqa=max(ra_all) / min(ra_all), rqh=max(rh_all) / min(rh_all))
    return out
def drop_methods(by, keep): return {m: v for m, v in by.items() if m in keep}
def drop_readings(by, pred): return {m: [x for x in v if not pred(m, x[0])] for m, v in by.items()}
def scale_as_method(by, pat_methods):
    out = {}
    for m, v in by.items():
        out[m] = [(rd, a, a if (m in pat_methods and 'scale' in rd) else h) for rd, a, h in v]
    return out
ALL = (EN, FPm, HA, PH, CB)
VARIANTS = []   # (name, transform of by, centre)
VARIANTS.append(('base (all 19 readings, geometric-mean centres)', lambda b: b, 'gm'))
short = {EN: 'energy and protein balance', FPm: 'footprint', HA: 'HALF', PH: 'people per hectare', CB: 'commodity balance'}
for m in ALL: VARIANTS.append(('%s left out' % short[m], (lambda mm: lambda b: drop_methods(b, [x for x in ALL if x != mm]))(m), 'gm'))
VARIANTS.append(('fish reading dropped', lambda b: drop_readings(b, lambda m, rd: m == CB and rd == 'fish'), 'gm'))
VARIANTS.append(('pasture-alone footprint readings dropped', lambda b: drop_readings(b, lambda m, rd: m == FPm and rd.endswith('pasture')), 'gm'))
VARIANTS.append(('method centre = median of its readings', lambda b: b, 'med'))
VARIANTS.append(('energy and protein balance alone', lambda b: drop_methods(b, [EN]), 'gm'))
VARIANTS.append(('energy and protein balance with footprint', lambda b: drop_methods(b, [EN, FPm]), 'gm'))
VARIANTS.append(('footprint and HALF left out', lambda b: drop_methods(b, [EN, PH, CB]), 'gm'))
VARIANTS.append(('land scale-up of the energy balance classed as method', lambda b: scale_as_method(b, [EN]), 'gm'))
VARIANTS.append(('land scale-up readings of the energy balance dropped', lambda b: drop_readings(b, lambda m, rd: m == EN and 'scale' in rd), 'gm'))
VARIANTS.append(('land scale-up of energy balance and people per hectare classed as method', lambda b: scale_as_method(b, [EN, PH]), 'gm'))
REFS = [('41.5', 41.5), ('31.1', 31.1), ('49.2', 49.2), ('53.6', 53.6), ('median of method centres', 'median'), ('geometric mean of method centres', 'gmean')]
def r(x, d=3): return '' if x is None else round(x, d) + 0.0
rows = [['variant', 'line', 'reference', 'share closed', 'SD of log method centres before', 'SD of log method centres after', 'narrowing of SD of centres',
         'max to min centre before', 'max to min centre after', 'SD of log readings before', 'SD of log readings after', 'narrowing of SD of readings',
         'max to min reading before', 'max to min reading after', 'methods', 'readings']]
R = {}
for vname, tf, cen in VARIANTS:
    for line in LINES:
        by = tf(base_pairs(line))
        for rn, rv in REFS:
            if vname.startswith('method centre =') is False and cen == 'med': continue
            if vname.endswith('alone') and isinstance(rv, str): continue          # one method: a centre reference is its own centre, no distance to measure
            ms = measure(by, float(rv) if isinstance(rv, float) else rv, cen)
            R[(vname, line, rn)] = ms
            sda, sdh = ms.get('sd_a'), ms.get('sd_h')
            rows.append([vname, line, rn, r(ms['share']), r(sda), r(sdh), r(1 - sdh / sda) if sda else '', r(ms.get('qa'), 2), r(ms.get('qh'), 2),
                         r(ms['rsd_a']), r(ms['rsd_h']), r(1 - ms['rsd_h'] / ms['rsd_a']), r(ms['rqa'], 2), r(ms['rqh'], 2), ms['n'], ms['nread']])
# ------------------------------------------------ checks against the paper's figures (stop if they fail)
base = lambda line, ref: R[('base (all 19 readings, geometric-mean centres)', line, ref)]
assert round(base('a', '41.5')['share'], 3) == 0.041 and round(base('b', '41.5')['share'], 3) == 0.385, (base('a', '41.5')['share'], base('b', '41.5')['share'])
assert round(1 - base('b', '41.5')['sd_h'] / base('b', '41.5')['sd_a'], 3) == 0.318
assert (round(base('b', '41.5')['sd_a'], 2), round(base('b', '41.5')['sd_h'], 2)) == (0.65, 0.44)       # "narrows by about a third": 0.65 to 0.44
assert (round(base('a', '41.5')['sd_a'], 2), round(base('a', '41.5')['sd_h'], 2)) == (0.65, 0.70)
assert (round(base('b', '41.5')['qa'], 1), round(base('b', '41.5')['qh'], 1)) == (6.2, 3.7)
# and against the existing csv written by harmonised_lines.py
L = dicts(D + 'harmonised_comparison_lines.csv')
for line, tag in (('a', '(a)'), ('b', '(b)')):
    for ref, lab in (('41.5', 'the corrected model (41.5)'), ('median of method centres', 'the median of the five method centres'),
                     ('geometric mean of method centres', 'the geometric mean of the five method centres')):
        old = [x for x in L if x['method'].startswith('All five methods') and x['classification'].startswith(tag) and x['reference'] == lab][0]
        assert abs(float(old['share_closed']) - round(base(line, ref)['share'], 3)) < 1e-9, (line, ref)
# ------------------------------------------------ the footprint's own accounting (decision 142): own-productivity reading = FAO population x land-weighted output / consumption
SF = {x['item']: float(x['ha a person']) for x in dicts(D + 'simpson_food.csv') if x['period'] == '2021-23'}
FPR = {x['reading']: x for x in HC if x['method'] == FPm}
POP = 26.20                                                                                   # FAO head count, 2021-23 mean (million); README, Bases section
acc = [['build', 'land type', 'footprint a person (world-average ha)', 'consumption (Mha, world-average)', 'own-productivity reading (million people)', 'output (Mha, world-average) = reading x footprint',
        'output over consumption', 'times corrected model (41.5)', 'times improved model (53.6)']]
def line_(build, lt, fpp, reading):
    cons = fpp * POP; outp = reading * fpp
    acc.append([build, lt, r(fpp), r(cons, 2), reading, r(outp, 2), r(outp / cons, 2), r(reading / M_FIX, 2), r(reading / 53.6, 2)])
b1 = {'cropland-bound': SF['crop land total'], 'pasture': SF['pasture total']}
for lt, rd in (('cropland-bound', 'build 1, cropland-bound'), ('pasture', 'build 1, pasture'), ('crop and pasture together', 'build 1, crop and pasture together')):
    fpp = b1['cropland-bound'] + b1['pasture'] if lt.startswith('crop and') else b1[lt]
    line_('build 1', lt, fpp, float(FPR[rd][K[10]]))
acc_pool = acc[-1]; acc_c, acc_p = acc[1], acc[2]
# pooled = consumption-weighted mean of the two ratios (this is the algebra; it must hold to rounding)
w = (acc_c[3] * acc_c[6] + acc_p[3] * acc_p[6]) / (acc_c[3] + acc_p[3])
assert abs(w - acc_pool[6]) < 0.02, (w, acc_pool[6])
assert abs(acc_pool[4] / POP - acc_pool[6]) < 0.006
# the binding land type: the lower of the cropland-bound and pasture readings in a build (B270)
bind = {'build 1': min(float(FPR['build 1, cropland-bound'][K[10]]), float(FPR['build 1, pasture'][K[10]])),
        'build 3': min(float(FPR['build 3 (thesis rates), cropland-bound'][K[10]]), float(FPR['build 3 (thesis rates), pasture'][K[10]]))}
assert (round(bind['build 1'], 1), round(bind['build 3'], 1)) == (53.9, 77.9), bind
for b, lt in (('build 3 (thesis rates)', 'cropland-bound'), ('build 3 (thesis rates)', 'pasture'), ('build 3 (thesis rates)', 'crop and pasture together')):
    rd = '%s, %s' % (b, lt); rv = float(FPR[rd][K[10]])
    fpp = {'cropland-bound': 0.307, 'pasture': 1.047, 'crop and pasture together': 1.354}[lt]    # README, Build 3 on 2021-23 consumption (garden on cropland)
    line_('build 3', lt, fpp, rv)
acc.append(['binding land type (lower of cropland-bound and pasture)', 'build 1 and build 3', '', '', '%.1f to %.1f' % (bind['build 1'], bind['build 3']), '', '',
            '%.2f to %.2f' % (bind['build 1'] / M_FIX, bind['build 3'] / M_FIX), '%.2f to %.2f' % (bind['build 1'] / 53.6, bind['build 3'] / 53.6)])
csv.writer(open(D + 'harmonised_robustness_footprint.csv', 'w', newline='')).writerows(acc)
for x in acc: print(x)
csv.writer(open(D + 'harmonised_robustness.csv', 'w', newline='')).writerows(rows)
# ------------------------------------------------ summaries printed (and used in the README)
CORE = [v[0] for v in VARIANTS if v[0] not in ('energy and protein balance alone', 'energy and protein balance with footprint', 'footprint and HALF left out')]
print('Core set (references, each method out, fish, pasture-alone, median centres, land scale-up): %d variants' % len(CORE))
def rng(line, refs, names=None):
    xs = [(v['share'], k) for k, v in R.items() if k[1] == line and k[2] in refs and (names is None or k[0] in names)]
    lo, hi = min(xs), max(xs); return lo, hi
for line in 'ab':
    print('line', line)
    for rn, _ in REFS:
        lo, hi = rng(line, [rn]); print('  ref %-34s range %6.1f%% (%s) to %6.1f%% (%s)' % (rn, 100 * lo[0], lo[1][0], 100 * hi[0], hi[1][0]))
    for lab, refs in (('to the model (4 references)', ['41.5', '31.1', '49.2', '53.6']), ('to the model, 41.5 only', ['41.5']), ('to the median', ['median of method centres']), ('to the geometric mean', ['geometric mean of method centres'])):
        lo, hi = rng(line, refs, CORE); print('  core set, %s: %.1f%% (%s) to %.1f%% (%s)' % (lab, 100 * lo[0], lo[1][0], 100 * hi[0], hi[1][0]))
        lo, hi = rng(line, refs); print('  all variants, %s: %.1f%% to %.1f%%' % (lab, 100 * lo[0], 100 * hi[0]))
for line in 'ab':
    xs = [(1 - v['sd_h'] / v['sd_a'], k) for k, v in R.items() if k[1] == line and k[2] == '41.5' and 'sd_a' in v and v['n'] >= 3]
    print('  narrowing of SD of centres line', line, ['%s: %.1f%%' % (k[0], 100 * x) for x, k in sorted(xs)])
for k, v in R.items():
    if k[2] == '41.5': print(k[0], k[1], round(100 * v['share'], 1), ('%.1f%%' % (100 * (1 - v['sd_h'] / v['sd_a']))) if 'sd_a' in v else '')
