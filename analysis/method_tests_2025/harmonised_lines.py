#!/usr/bin/env python3
"""The harmonised comparison under both classifications of the productivity basis, and the cross-method table with local-productivity readings primary
(decisions 105 and 106; brief B113; Paper B, section 5).
Usage (repository root): python3 -I analysis/method_tests_2025/harmonised_lines.py
Reads: harmonised_comparison.csv, cross_method.csv and model_entry.csv (all as written by their own scripts; none is rewritten).
Writes: harmonised_comparison_lines.csv and cross_method_local.csv only.

Two classifications of the productivity basis (whether a hectare is counted at world-average or at Australia's own productivity):
  (a) part of the method (decision 35, as the paper stands): the harmonised reading is column (b) of harmonised_comparison.csv;
  (b) an input: every land-based method on Australia's own productivity. For the footprint (builds 1 and 3) and HALF the harmonised reading is column (e),
      the local-productivity adjustment (Wackernagel and Rees 1996, p. 78); the other methods already count Australia's own production or delivered
      calories, so their harmonised reading is column (b) on both lines. Footprint build 2 (V04) cannot be re-run, so it has no column (e) reading; it has
      no input-effect cell on line (a) either, so it is outside the paired set on both lines.
The paired set: every method reading with an as-run value (column a) and a harmonised value on the line, the model rows and Fearnside (blank) excluded;
five methods (energy and protein balance, footprint, HALF, people per hectare, commodity balance), weighted equally.

The input share (the share of the distance closed by harmonisation), for a method m with paired readings i = 1..n_m and a reference point R:
  distance as run       D_a(m, R) = (1/n_m) * sum_i | ln(a_i / R_a) |
  distance harmonised   D_h(m, R) = (1/n_m) * sum_i | ln(h_i / R_h) |
  share closed          S(m, R)   = (D_a - D_h) / D_a      (negative when harmonisation moves the method further away)
  all five methods      S(R)      = (sum_m D_a - sum_m D_h) / sum_m D_a     (methods weighted equally)
Three reference points R:
  the model             41.5 million, the corrected model's short-term figure (model_entry.csv, 2025-fixed); the same as run and harmonised;
  the median            the median of the five method centres, where a method's centre is the geometric mean of its paired readings; computed separately
                        as run (R_a, from the a_i) and harmonised (R_h, from the h_i), so the distance is to the centre of the methods at that stage;
  the geometric mean    the geometric mean of the five method centres, likewise computed as run and harmonised.
The model is not one of the five, so two of the three reference points are free of it.
Dispersion with no reference point, as run and harmonised: the standard deviation (population form, divisor n) of the natural logs, and the highest over
the lowest value, over (i) the five method centres and (ii) all paired readings; "share closed" for these is 1 - harmonised / as run on the log scale
(for the max-to-min ratio, 1 - ln(harmonised ratio) / ln(as-run ratio)).
For continuity with the paper's figure (B276) the script also writes the factor split it used: per reading, a / R = (a / h) * (h / R) exactly; per method the
mean absolute log of each factor; methods weighted equally; inputs over inputs plus method. With R = 41.5 on line (a) this must reproduce the 9.6% in the
summary row of harmonised_comparison.csv, and the script stops if it does not."""
import csv, math, statistics
D = 'analysis/method_tests_2025/'
def dicts(path): return list(csv.DictReader(open(path, newline='')))
HC = dicts(D + 'harmonised_comparison.csv')
K = list(HC[0].keys())
A, B, E = K[2], K[3], K[10]                                                                 # columns (a), (b), (e)
assert A.startswith('(a)') and B.startswith('(b)') and E.startswith('(e)'), K
ME = {r['release']: r for r in dicts(D + 'model_entry.csv')}
M_FIX, M_IMP = float(ME['2025-fixed']['short term (million)']), float(ME['2025-improved']['short term (million)'])
LOCAL = ('Ecological footprint, food row (Simpson)', 'HALF index (Alexander)')                # the methods that count world-average hectares
def num(s): return None if s == '' else float(s)
# ---------------------------------------------------------------- the paired readings on each line
LINES = {'(a) productivity basis part of the method (decision 35)': 'a', '(b) productivity basis an input (Australian productivity)': 'b'}
pairs = {}
for line, key in LINES.items():
    by = {}
    for r in HC:
        m = r['method']
        if m.startswith(('The model', 'Summary', 'Failure probability')): continue
        a = num(r[A])
        if m in LOCAL and key == 'b': h = num(r[E])                                          # on line (b) the footprint and HALF take column (e)
        else: h = num(r[B]) if r[K[4]] != '' else None                                       # line (a): readings with an input-effect cell (as the summary)
        if a is None or h is None: continue
        by.setdefault(m, []).append((r['reading'], a, h))
    pairs[line] = by
assert all(len(v) == 5 for v in pairs.values()), {k: list(v) for k, v in pairs.items()}
def gmean(xs): return math.exp(sum(math.log(x) for x in xs) / len(xs))
def sd(xs): return statistics.pstdev([math.log(x) for x in xs])
out = [['method', 'classification', 'reference', 'as_run', 'harmonised', 'share_closed', 'reference value as run (million)', 'reference value harmonised (million)',
        'readings', 'unit', 'note']]
def f(x, d=3): return '' if x is None else round(x, d) + 0.0
summary = {}
for line, by in pairs.items():
    cen_a = {m: gmean([a for _, a, _ in v]) for m, v in by.items()}
    cen_h = {m: gmean([h for _, _, h in v]) for m, v in by.items()}
    refs = {'the corrected model (41.5)': (M_FIX, M_FIX),
            'the median of the five method centres': (statistics.median(cen_a.values()), statistics.median(cen_h.values())),
            'the geometric mean of the five method centres': (gmean(cen_a.values()), gmean(cen_h.values()))}
    # the readings themselves, so every figure below can be checked by hand
    for m, v in by.items():
        for rd, a, h in v:
            out.append([m, line, 'reading: ' + rd, f(a, 1), f(h, 1), '', '', '', 1, 'million people',
                        'harmonised = column (e), local productivity' if (m in LOCAL and LINES[line] == 'b') else 'harmonised = column (b)'])
        out.append([m, line, 'method centre (geometric mean of its paired readings)', f(cen_a[m], 1), f(cen_h[m], 1), '', '', '', len(v), 'million people', ''])
    for ref, (ra, rh) in refs.items():
        Da = {m: sum(abs(math.log(a / ra)) for _, a, _ in v) / len(v) for m, v in by.items()}
        Dh = {m: sum(abs(math.log(h / rh)) for _, _, h in v) / len(v) for m, v in by.items()}
        for m in by:
            out.append([m, line, ref, f(Da[m]), f(Dh[m]), f((Da[m] - Dh[m]) / Da[m]), f(ra, 1), f(rh, 1), len(by[m]), 'mean absolute natural log distance', ''])
        tot = (sum(Da.values()) - sum(Dh.values())) / sum(Da.values())
        out.append(['All five methods, weighted equally', line, ref, f(sum(Da.values()) / 5), f(sum(Dh.values()) / 5), f(tot), f(ra, 1), f(rh, 1),
                    sum(len(v) for v in by.values()), 'mean absolute natural log distance', 'share closed = (sum of D as run - sum of D harmonised) / sum of D as run'])
        summary[(line, ref)] = (sum(Da.values()) / 5, sum(Dh.values()) / 5, tot)
        # the factor split the paper used (B276), on this line and reference: a/R_a = (a/h) * (h/R_a); input share = mean|ln(a/h)| / (that + mean|ln(h/R_a)|)
        li = sum(sum(abs(math.log(a / h)) for _, a, h in v) / len(v) for v in by.values()) / 5
        lm = sum(sum(abs(math.log(h / ra)) for _, _, h in v) / len(v) for v in by.values()) / 5
        out.append(['All five methods, weighted equally', line, ref + '; factor split as in the paper (B276)', f(li), f(lm), f(li / (li + lm)), f(ra, 1), f(ra, 1),
                    sum(len(v) for v in by.values()), 'as_run = mean absolute log input factor (a over h); harmonised = mean absolute log method factor (h over R); share_closed = input share',
                    'continuity only; not the input share defined above'])
        summary[(line, ref, 'factor')] = li / (li + lm)
    # dispersion with no reference point
    ra_all = [a for v in by.values() for _, a, _ in v]; rh_all = [h for v in by.values() for _, _, h in v]
    for lab, xa, xh in (('the five method centres', list(cen_a.values()), list(cen_h.values())), ('all paired readings', ra_all, rh_all)):
        s_a, s_h = sd(xa), sd(xh)
        q_a, q_h = max(xa) / min(xa), max(xh) / min(xh)
        out.append(['Dispersion (no reference point)', line, 'standard deviation of natural logs, ' + lab, f(s_a), f(s_h), f(1 - s_h / s_a), '', '', len(xa), 'log units',
                    'population form (divisor n); share closed = 1 - harmonised / as run'])
        out.append(['Dispersion (no reference point)', line, 'highest over lowest, ' + lab, f(q_a, 2), f(q_h, 2), f(1 - math.log(q_h) / math.log(q_a)), '', '', len(xa), 'ratio',
                    'as run %.1f to %.1f; harmonised %.1f to %.1f (million); share closed on the log scale' % (min(xa), max(xa), min(xh), max(xh))])
        summary[(line, 'sd', lab)] = (s_a, s_h); summary[(line, 'q', lab)] = (q_a, q_h, min(xa), max(xa), min(xh), max(xh))
# continuity check: line (a), reference 41.5, factor split = the paper's 9.6% (harmonised_comparison.csv summary row)
L_A, L_B = list(LINES)
legacy = next(r for r in HC if r['method'].startswith('Summary'))['note']
assert 'inputs %.0f%%' % (100 * summary[(L_A, 'the corrected model (41.5)', 'factor')]) in legacy, (summary[(L_A, 'the corrected model (41.5)', 'factor')], legacy)
csv.writer(open(D + 'harmonised_comparison_lines.csv', 'w', newline='')).writerows(out)
# ---------------------------------------------------------------- the cross-method table with the local-productivity readings primary
CM = dicts(D + 'cross_method.csv')
hc = lambda m, rd: next(r for r in HC if r['method'] == m and r['reading'] == rd)
FP = 'Ecological footprint, food row (Simpson)'; HA = 'HALF index (Alexander)'
fp_crop = [float(hc(FP, 'build %s, cropland-bound' % b)[E]) for b in ('1', '3 (thesis rates)')]
fp_both = [float(hc(FP, 'build %s, crop and pasture together' % b)[E]) for b in ('1', '3 (thesis rates)')]
fp_past = [float(hc(FP, 'build %s, pasture' % b)[E]) for b in ('1', '3 (thesis rates)')]
ha_loc = float(hc(HA, "agricultural land over the diet's land a person")[E])
# the secondary (world-average) footprint rows stand on the same 2021-23 world yields as the primary rows (V39, B123): column (b) of builds 1 and 3 (build 3's thesis 1990 yields
# replaced by FAOSTAT 2021-23); the cropland-bound and the crop-and-pasture rows, as the primary row, not pasture alone; build 2 cannot be re-run. The as-run 1990 reading (103.1 and 268.4) is the qualifier.
fp_w_crop = [float(hc(FP, 'build %s, cropland-bound' % b)[B]) for b in ('1', '3 (thesis rates)')]
fp_w_both = [float(hc(FP, 'build %s, crop and pasture together' % b)[B]) for b in ('1', '3 (thesis rates)')]
fp_1990 = [float(hc(FP, 'build 3 (thesis rates), %s' % k)[A]) for k in ('cropland-bound', 'crop and pasture together')]
cl = [['method', 'row', 'productivity basis', 'reading for Australia on current data (million people)', 'low', 'high', 'low over corrected model', 'high over corrected model',
       'low over improved model', 'high over improved model', 'source']]
def add(m, status, basis, reading, lo, hi, src):
    cl.append([m, status, basis, reading, lo, hi, round(lo / M_FIX, 2), round(hi / M_FIX, 2), round(lo / M_IMP, 2), round(hi / M_IMP, 2), src])
for r in CM:
    m, lo, hi = r['method'], float(r['low']), float(r['high'])
    if m == FP:
        add(m, 'primary', "Australia's own productivity (local-productivity adjustment, Wackernagel and Rees 1996 p. 78)",
            '%.1f to %.1f (cropland-bound %.1f to %.1f; crop and pasture together %.1f to %.1f; pasture alone %.1f to %.1f); builds 1 and 3 on 2021-23 world yields; build 2 cannot be re-run'
            % (min(fp_crop + fp_both), max(fp_crop + fp_both), min(fp_crop), max(fp_crop), min(fp_both), max(fp_both), min(fp_past), max(fp_past)),
            round(min(fp_crop + fp_both), 1), round(max(fp_crop + fp_both), 1), 'harmonised_comparison.csv column (e)')
        add(m + ', crop and pasture together', 'primary (sub-row)', "Australia's own productivity", '%.1f to %.1f (builds 1 and 3)' % (min(fp_both), max(fp_both)),
            round(min(fp_both), 1), round(max(fp_both), 1), 'harmonised_comparison.csv column (e)')
        add(m, 'secondary: world-average productivity (counterfactual)', "world-average hectares divided into Australia's physical hectares, on 2021-23 world yields",
            '%.1f to %.1f (cropland-bound %.1f to %.1f; crop and pasture together %.1f to %.1f; builds 1 and 3 on 2021-23 world yields; build 3 on the thesis\'s 1990 world yields reads %.1f and %.1f)'
            % (min(fp_w_crop + fp_w_both), max(fp_w_crop + fp_w_both), min(fp_w_crop), max(fp_w_crop), min(fp_w_both), max(fp_w_both), fp_1990[0], fp_1990[1]),
            round(min(fp_w_crop + fp_w_both), 1), round(max(fp_w_crop + fp_w_both), 1), 'harmonised_comparison.csv column (b)')
    elif m == HA:
        add(m, 'primary', "Australia's own productivity (local-productivity adjustment, Wackernagel and Rees 1996 p. 78)", '%.1f' % ha_loc, ha_loc, ha_loc, 'harmonised_comparison.csv column (e)')
        add(m, 'secondary: world-average productivity (counterfactual)', "world-average hectares divided into Australia's physical hectares", r['reading for Australia on current data (million people)'],
            lo, hi, 'cross_method.csv')
    elif m.startswith('Failure probability'):
        add(m, 'primary', "the model's own runs with the weather allowance (no world-average hectares)", r['reading for Australia on current data (million people)'], lo, hi, 'cross_method.csv')
    elif m.startswith('The model'):
        add(m, 'reference', "Australia's own land, yields and diet", r['reading for Australia on current data (million people)'], lo, hi, 'cross_method.csv (5th to 95th percentile)')
    else:
        add(m, 'primary', "Australia's own production (no world-average hectares)", r['reading for Australia on current data (million people)'], lo, hi, 'cross_method.csv')
AGG = ('Energy and protein balance (Gifford; Henry and Godden)', FP, HA, 'People per hectare (Cassidy)')
def grp(status_ok):
    sel = [r for r in cl[1:] if r[0] in AGG and status_ok(r[1])]
    return min(r[4] for r in sel), max(r[5] for r in sel)
g_loc = grp(lambda s: s == 'primary')
sel_w = [r for r in cl[1:] if r[0] in AGG and (r[1].startswith('secondary') or (r[1] == 'primary' and r[0] not in LOCAL))]
g_w = (min(r[4] for r in sel_w), max(r[5] for r in sel_w))
add('The aggregate methods (energy and protein balance, footprint, HALF, people per hectare)', 'summary: primary rows', 'footprint and HALF at Australian productivity',
    '%.1f to %.1f' % g_loc, g_loc[0], g_loc[1], 'rows above')
add('The aggregate methods (energy and protein balance, footprint, HALF, people per hectare)', 'summary: secondary (world-average footprint and HALF)', 'footprint and HALF at world-average productivity, footprint on 2021-23 world yields (103 at 1990 world yields)',
    '%.1f to %.1f' % g_w, g_w[0], g_w[1], 'rows above')
csv.writer(open(D + 'cross_method_local.csv', 'w', newline='')).writerows(cl)
# ---------------------------------------------------------------- print
for k, v in summary.items(): print(k, v)
print()
for r in cl: print(' | '.join(str(x) for x in r[:10]))
