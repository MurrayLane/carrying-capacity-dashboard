#!/usr/bin/env python3
"""A third harmonisation line for Paper B (brief B139, decision 144; R05b issue 6): line (c) = line (b) plus one per-person requirement and one waste treatment,
the same for every method and for the model.
Usage (repository root):
  python3 -I analysis/method_tests_2025/harmonised_line_c.py                      writes harmonised_line_c.csv, harmonised_line_c_robustness.csv and harmonised_line_c_model_runs.csv
  python3 -I analysis/method_tests_2025/harmonised_line_c.py --wrong-value-demo   plants one wrong value and shows the script's own check failing (nothing is written)
Needs node (the evaluator is run, unchanged, by b139_model_runs.mjs for the model's side of the supply variants).
Reads (read only): harmonised_comparison.csv, harmonised_comparison_lines.csv (to prove that line (b) is rebuilt exactly), intake_variant.csv (the model-loss-factor share of the
food balance's energy), model_entry.csv, fbs_au_world_2021_23.csv, fao_au_production_1997_2023.csv, ladder.csv.

EXPECTED DIRECTION (written here as the brief asks, with the computation after it): WIDER. Every method divides by the FAO food supply (3,525 kcal, 14.8 MJ a person a day, waste inside it); the model
runs on 8.0 MJ eaten, waste charged separately. Putting the methods on the model's requirement raises every method reading by the same factor (about 1.5), and every reading but
the fish reading is above the model, so the distance to the model grows and the share closed falls (possibly below zero). Putting the model on the supply
requirement instead lowers the model by the same factor and widens the gap the same way. A fall in the share closed is the expected result, not an error.

The two requirements and the two waste treatments (four cells, c1 to c4):
  The model needs eaten energy E_m = 8.0 MJ a day (nutrition README, bases.csv) and charges waste on its own retail and consumer loss factors, whose energy-weighted eaten share of
  the food balance is s_e (intake_variant.csv, "intake share, model loss factors", energy row: 0.8202). The methods' per-person need is the FAO supply S = 3,525 kcal (14.75 MJ),
  which holds the waste.
  c1  requirement 8.0 MJ eaten, waste charged separately on the model's loss factors, for everyone. The methods' need becomes E_m / s_e, so every method reading is multiplied by
      M1 = S s_e / E_m (the diet of every method is the food balance's mix scaled to the new energy, so the item shares cancel and the factor is one number). The model is unchanged (41.5).
  c2  requirement the FAO supply (3,525 kcal, waste inside), for everyone. The methods are unchanged (line (b)). The model's food amount (Settings!B9) is raised to M1 so that its
      own supply-level need, E_m f / s_e, equals S; its waste stays charged on its own factors (the supply holds it). The model reading is the evaluator's, not 41.5 / M1.
  c3  requirement 8.0 MJ eaten, no avoidable waste charged to anyone. The methods' need becomes E_m, so every reading is multiplied by M0 = S / E_m. The model is the evaluator's run
      with avoidable waste 0 (55.3).
  c4  requirement the FAO supply, no avoidable waste charged to anyone. Methods unchanged; the model's food amount is M0 with avoidable waste 0.
Commodity balance, grain with embodied feed grain: only the direct grain falls with the requirement; their embodied feed grain (7.6 Mt over 25.1 million, 303 kg a person) is kept, as
in the intake variant (B116), so that reading is multiplied by (u + e) / (u / M + e) with u the direct grain use a person (kg).
Dispersion measures are unchanged by a uniform factor; the grain reading and the fish reading are the only readings that move relative to the others.
Distances, shares closed and dispersion are those of harmonised_lines.py (docstring there): D = mean absolute natural log distance, share closed = (D as run - D harmonised) / D as run,
methods weighted equally; references the model, the median and the geometric mean of the five method centres (as run and harmonised); the as-run reference for the model is 41.5.
"""
import collections, csv, json, math, statistics, subprocess, sys
D = 'analysis/method_tests_2025/'
DEMO = '--wrong-value-demo' in sys.argv
def dicts(p): return list(csv.DictReader(open(p, newline='')))
def rows(p): return list(csv.reader(open(p, newline='')))
def num(s): return None if s == '' else float(s)
HC = dicts(D + 'harmonised_comparison.csv'); K = list(HC[0].keys()); A, B, E = K[2], K[3], K[10]
ME = {r['release']: r for r in dicts(D + 'model_entry.csv')}
M_FIX = float(ME['2025-fixed']['short term (million)'])
LAD = {r['step']: float(r['million people']) for r in dicts(D + 'ladder.csv')}
M_FIX_NW = LAD['average year, no avoidable waste']
LOCAL = ('Ecological footprint, food row (Simpson)', 'HALF index (Alexander)')
EN, FPm, HA, PH, CB = ('Energy and protein balance (Gifford; Henry and Godden)', 'Ecological footprint, food row (Simpson)', 'HALF index (Alexander)',
                       'People per hectare (Cassidy)', 'Commodity balance (Foran and Poldy)')
GRAIN = 'grain with embodied feed grain'
# ---------------------------------------------------------------- the paired readings of line (b), rebuilt as harmonised_lines.py builds them
def paired(key):
    by = collections.OrderedDict()
    for r in HC:
        m = r['method']
        if m.startswith(('The model', 'Summary', 'Failure probability')): continue
        a = num(r[A])
        h = num(r[E]) if (m in LOCAL and key == 'b') else (num(r[B]) if r[K[4]] != '' else None)
        if a is None or h is None: continue
        by.setdefault(m, []).append((r['reading'], a, h))
    return by
PB = paired('b')
assert len(PB) == 5 and sum(len(v) for v in PB.values()) == 19
# ---------------------------------------------------------------- the bases (all read from the records, none typed)
FB = collections.defaultdict(dict)
for r in dicts(D + 'fbs_au_world_2021_23.csv'):
    try: FB[(r['Area'], r['Item'], r['Element'])][r['Year']] = float(r['Value'])
    except ValueError: pass
YR = ('2021', '2022', '2023')
def fbs(item, el): return sum(FB[('Australia', item, el)].get(y, 0.0) for y in YR)
pop_fbs = fbs('Population', 'Total Population - Both sexes') * 1000
KCAL = fbs('Grand Total', 'Food supply (kcal)') * 1e6 / pop_fbs / 365                    # kcal a person a day, the FAO supply (3,525)
S_MJ = KCAL * 4.184 / 1000
IV = {(r['method'], r['reading']): r for r in dicts(D + 'intake_variant.csv')}
S_E = float(IV[(EN, 'energy, production as it is')]['intake share, model loss factors'])      # energy-weighted eaten share of the food balance on the model's loss factors
E_M = 8.0                                                                                    # the model's requirement, MJ a day as eaten (records: nutrition README, bases.csv)
E_M_EVAL = 7375.853418013801 / 1000                                                          # the diet the evaluator's land is computed from (B114: 7,376 kJ a day); not 8.0: noted in the README
M1, M0 = S_MJ * S_E / E_M, S_MJ / E_M
M1x, M0x = S_MJ * S_E / E_M_EVAL, S_MJ / E_M_EVAL                                         # the same factors with the evaluator's 7.376 MJ in place of 8.0 (sensitivity)
# grain with embodied feed grain: direct grain use a person (kg) and their embodied feed grain, as the intake variant (bases_fidelity.py)
fp_pop = sum(FB[('Australia', 'Population', 'Total Population - Both sexes')][y] for y in YR) / 3 / 1000
GR = ['Wheat and products', 'Barley and products', 'Maize and products', 'Oats', 'Rice and products', 'Rye and products', 'Sorghum and products', 'Millet and products', 'Cereals, other']
U_GRAIN = sum(fbs(i, 'Food') for i in GR) / 3 / fp_pop                                      # 1000 t / million = kg a person
EMB = 7.6 / 25.1 * 1000
prod_grain = sum(float(r['Value']) for r in dicts(D + 'fao_au_production_1997_2023.csv') if r['Item'] == 'Cereals, primary' and r['Year'] in YR) / 3 / 1e6   # Mt
assert abs(prod_grain * 1000 / (U_GRAIN + EMB) - float(IV[(CB, GRAIN)]['supply basis (harmonised, million)'])) < 0.06, 'grain reading no longer reproduces the intake variant'
def grain_factor(M): return (U_GRAIN + EMB) / (U_GRAIN / M + EMB)
# ---------------------------------------------------------------- the model's side: the evaluator, unchanged
def model_runs(pairs_):
    out = subprocess.run(['node', D + 'b139_model_runs.mjs', 'cap'] + ['%.10f:%s' % p for p in pairs_], capture_output=True, text=True, check=True).stdout
    return {(round(r['food'], 8), r['losses']): r['capacity'] / 1e6 for r in json.loads(out)}
req = [(1.0, 0.12), (1.0, 0.0), (M1, 0.12), (M0, 0.0), (M1x, 0.12), (M0x, 0.0)]
MR = model_runs(req)
cap = lambda f, l: MR[(round(f, 8), l)]
assert round(cap(1.0, 0.12), 1) == M_FIX and round(cap(1.0, 0.0), 1) == M_FIX_NW, (cap(1.0, 0.12), cap(1.0, 0.0))     # the evaluator reproduces 41.5 and 55.3
R1 = lambda x: round(x, 1)                                                                   # model references to one decimal, as model_entry.csv holds 41.5
VARIANTS = collections.OrderedDict([
    ('(b) line (b) as it stands (the base the third line adds to)',
     dict(key='b', mult=1.0, grain=1.0, model=M_FIX, label='b', note='line (b): productivity an input; supply requirement and waste unequalised')),
    ("(c1) line (c): requirement 8.0 MJ as eaten, waste on the model's own loss factors, for methods and model; the model unchanged",
     dict(key='c1', mult=M1, grain=grain_factor(M1), model=R1(cap(1.0, 0.12)), label='c1',
          note='every method reading x %.4f (= %.0f kcal x %.4f eaten share / 8.0 MJ); grain with embodied feed grain x %.4f; model 41.5 as run' % (M1, KCAL, S_E, grain_factor(M1)))),
    ('(c2) line (c): requirement the FAO supply (3,525 kcal, waste inside it), for methods and model; the methods unchanged',
     dict(key='c2', mult=1.0, grain=1.0, model=R1(cap(M1, 0.12)), label='c2',
          note="the model's food amount raised to %.4f so its supply-level need is the FAO supply; model reading %.2f from the evaluator (the closed form 41.5 / %.4f gives %.2f)" % (M1, cap(M1, 0.12), M1, M_FIX / M1))),
    ('(c3) line (c): requirement 8.0 MJ as eaten, no avoidable waste charged to anyone; the model with avoidable waste 0',
     dict(key='c3', mult=M0, grain=grain_factor(M0), model=R1(cap(1.0, 0.0)), label='c3',
          note='every method reading x %.4f (= 8.0 MJ eaten taken as the whole need); grain x %.4f; model 55.3 (avoidable waste 0)' % (M0, grain_factor(M0)))),
    ('(c4) line (c): requirement the FAO supply, no avoidable waste charged to anyone; the methods unchanged',
     dict(key='c4', mult=1.0, grain=1.0, model=R1(cap(M0, 0.0)), label='c4',
          note="the model's food amount raised to %.4f with avoidable waste 0; model reading %.2f from the evaluator" % (M0, cap(M0, 0.0)))),
])
def readings(v):
    out = collections.OrderedDict()
    for m, lst in PB.items():
        rr = []
        for rd, a, h in lst:
            f = v['grain'] if (m == CB and rd == GRAIN) else v['mult']
            rr.append((rd, a, h * f))
        out[m] = rr
    return out
def gmean(xs): return math.exp(sum(math.log(x) for x in xs) / len(xs))
def sdl(xs): return statistics.pstdev([math.log(x) for x in xs])
def fx(x, d=3): return '' if x is None else round(x, d) + 0.0
def measures(by, model_h, centre='gm', refs_override=None):
    """The distance, share closed and dispersion of harmonised_lines.py for one set of paired readings. model_h: the model's reading on this line (the as-run reference is M_FIX)."""
    cf = gmean if centre == 'gm' else statistics.median
    ca = {m: cf([a for _, a, _ in v]) for m, v in by.items()}; ch = {m: cf([h for _, _, h in v]) for m, v in by.items()}
    refs = collections.OrderedDict([('the corrected model (41.5)', (M_FIX, model_h)),
                                    ('the median of the five method centres', (statistics.median(ca.values()), statistics.median(ch.values()))),
                                    ('the geometric mean of the five method centres', (gmean(ca.values()), gmean(ch.values())))])
    if refs_override: refs = collections.OrderedDict([(k, v) for k, v in refs.items() if k not in refs_override]); refs.update(refs_override)
    res = {'centres': (ca, ch), 'refs': {}}
    for ref, (ra, rh) in refs.items():
        Da = {m: sum(abs(math.log(a / ra)) for _, a, _ in v) / len(v) for m, v in by.items()}
        Dh = {m: sum(abs(math.log(h / rh)) for _, _, h in v) / len(v) for m, v in by.items()}
        res['refs'][ref] = (ra, rh, Da, Dh, (sum(Da.values()) - sum(Dh.values())) / sum(Da.values()))
    xa, xh = list(ca.values()), list(ch.values())
    ra_all = [a for v in by.values() for _, a, _ in v]; rh_all = [h for v in by.values() for _, _, h in v]
    res['disp'] = {}
    for lab, ya, yh in (('the five method centres', xa, xh), ('all paired readings', ra_all, rh_all)):
        sa, sh = sdl(ya), sdl(yh); qa, qh = max(ya) / min(ya), max(yh) / min(yh)
        res['disp'][lab] = (sa, sh, 1 - sh / sa, qa, qh, 1 - math.log(qh) / math.log(qa), min(ya), max(ya), min(yh), max(yh), len(ya))
    return res
HEAD = ['method', 'classification', 'reference', 'as_run', 'harmonised', 'share_closed', 'reference value as run (million)', 'reference value harmonised (million)', 'readings', 'unit', 'note']
def build():
    out = [HEAD]; summ = {}
    for line, v in VARIANTS.items():
        by = readings(v); m = measures(by, v['model']); ca, ch = m['centres']; summ[v['label']] = m
        for mm, lst in by.items():
            for rd, a, h in lst:
                out.append([mm, line, 'reading: ' + rd, fx(a, 1), fx(h, 1), '', '', '', 1, 'million people', v['note'] if v['label'] != 'b' else 'harmonised = column (e) for the footprint and HALF, column (b) for the rest'])
            out.append([mm, line, 'method centre (geometric mean of its paired readings)', fx(ca[mm], 1), fx(ch[mm], 1), '', '', '', len(lst), 'million people', ''])
        for ref, (ra, rh, Da, Dh, tot) in m['refs'].items():
            for mm in by: out.append([mm, line, ref, fx(Da[mm]), fx(Dh[mm]), fx((Da[mm] - Dh[mm]) / Da[mm]), fx(ra, 1), fx(rh, 1), len(by[mm]), 'mean absolute natural log distance', ''])
            out.append(['All five methods, weighted equally', line, ref, fx(sum(Da.values()) / 5), fx(sum(Dh.values()) / 5), fx(tot), fx(ra, 1), fx(rh, 1), sum(len(x) for x in by.values()),
                        'mean absolute natural log distance', 'share closed = (sum of D as run - sum of D harmonised) / sum of D as run'])
        for lab, (sa, sh, shr, qa, qh, qshr, mina, maxa, minh, maxh, n) in m['disp'].items():
            out.append(['Dispersion (no reference point)', line, 'standard deviation of natural logs, ' + lab, fx(sa), fx(sh), fx(shr), '', '', n, 'log units', 'population form (divisor n); share closed = 1 - harmonised / as run'])
            out.append(['Dispersion (no reference point)', line, 'highest over lowest, ' + lab, fx(qa, 2), fx(qh, 2), fx(qshr), '', '', n, 'ratio',
                        'as run %.1f to %.1f; harmonised %.1f to %.1f (million); share closed on the log scale' % (mina, maxa, minh, maxh)])
    return out, summ
# ---------------------------------------------------------------- robustness: B135's core variants, for lines (b), (c1) and (c2)
CORE = [('base case', None), ('energy and protein balance out', EN), ('footprint out', FPm), ('HALF out', HA), ('people per hectare out', PH), ('commodity balance out', CB),
        ('fish reading dropped', 'fish'), ('pasture-alone footprint readings dropped', 'pasture'), ('method centre as the median of its readings', 'median')]
def variant_by(by, how):
    if how is None or how == 'median': return by
    if how in (EN, FPm, HA, PH, CB): return collections.OrderedDict((m, v) for m, v in by.items() if m != how)
    if how == 'fish': return collections.OrderedDict((m, [x for x in v if x[0] != 'fish']) for m, v in by.items())
    if how == 'pasture': return collections.OrderedDict((m, [x for x in v if not (m == FPm and x[0].endswith(', pasture'))]) for m, v in by.items())
def robustness():
    out = [['line', 'variant', 'reference', 'share closed', 'SD of log method centres as run', 'SD of log method centres harmonised', 'narrowing of the SD', 'highest over lowest centre as run', 'highest over lowest centre harmonised']]
    ranges = collections.defaultdict(list)
    for line, v in VARIANTS.items():
        if v['label'] not in ('b', 'c1', 'c2'): continue
        for name, how in CORE:
            by = variant_by(readings(v), how)
            centre = 'median' if how == 'median' else 'gm'
            # the model references: the corrected model as this line has it, and the four published reference points of B135 (31.1, 41.5, 49.2, 53.6) scaled as the line moves the model
            scale = v['model'] / M_FIX
            for refname, mh, ma in (('the corrected model (41.5)', v['model'], M_FIX),
                                    ('the model at its 5th percentile (31.1)', 31.1 * scale, 31.1), ('the model at its 95th percentile (49.2)', 49.2 * scale, 49.2), ('the improved model (53.6)', 53.6 * scale, 53.6)):
                cf = gmean if centre == 'gm' else statistics.median
                Da = sum(sum(abs(math.log(a / ma)) for _, a, _ in x) / len(x) for x in by.values())
                Dh = sum(sum(abs(math.log(h / mh)) for _, _, h in x) / len(x) for x in by.values())
                out.append([v['label'], name, refname, fx((Da - Dh) / Da), '', '', '', '', ''])
                ranges[(v['label'], refname)].append((Da - Dh) / Da)
            for refname in ('the median of the five method centres', 'the geometric mean of the five method centres'):
                m = measures(by, v['model'], centre)
                ra, rh, Da, Dh, tot = m['refs'][refname]
                out.append([v['label'], name, refname, fx(tot), '', '', '', '', '']); ranges[(v['label'], refname)].append(tot)
            if len(by) > 1:
                m = measures(by, v['model'], centre); sa, sh, shr, qa, qh, qshr = m['disp']['the five method centres'][:6]
                out.append([v['label'], name, 'dispersion of the method centres', '', fx(sa), fx(sh), fx(shr), fx(qa, 2), fx(qh, 2)]); ranges[(v['label'], 'spread')].append(shr)
    return out, ranges
# ---------------------------------------------------------------- the check: recompute the share to 41.5 from the reading rows of the csv, independently of the code above
def check(csv_rows, claimed=None):
    """Recompute, from the reading rows written to the csv, the line's share closed to its model reference; compare with the csv's share row (and with a claimed value if given)."""
    ok = True
    for line, v in VARIANTS.items():
        rd = collections.defaultdict(list)
        for r in csv_rows[1:]:
            if r[1] == line and r[2].startswith('reading: '): rd[r[0]].append((float(r[3]), float(r[4])))
        ra, rh = M_FIX, v['model']
        Da = sum(sum(abs(math.log(a / ra)) for a, _ in x) / len(x) for x in rd.values()); Dh = sum(sum(abs(math.log(h / rh)) for _, h in x) / len(x) for x in rd.values())
        got = (Da - Dh) / Da
        row = next(r for r in csv_rows[1:] if r[0].startswith('All five') and r[1] == line and r[2] == 'the corrected model (41.5)')
        want = float(row[5]) if claimed is None or v['label'] != 'c1' else claimed
        good = abs(got - want) < 0.006                                                      # the csv holds readings to one decimal and the share to three
        ok &= good
        print('%s share closed to the model, line %s: recomputed from the readings %.4f, csv/claimed %.4f: %s' % ('ok  ' if good else 'FAIL', v['label'], got, want, 'PASS' if good else 'MISMATCH'))
    return ok
def main():
    out, summ = build()
    # line (b) must be the paper's line (b): compare with harmonised_comparison_lines.csv
    L = [r for r in rows(D + 'harmonised_comparison_lines.csv')[1:] if r[1].startswith('(b)') and r[0].startswith('All five') and 'factor split' not in r[2]]
    for r in L:
        mine = next(x for x in out[1:] if x[0].startswith('All five') and x[1].startswith('(b)') and x[2] == r[2])
        assert mine[3:6] == [str(float(c)) if c != '' else c for c in r[3:6]] or all(abs(float(a) - float(b)) < 1e-9 for a, b in zip(mine[3:6], r[3:6])), (mine, r)
    print('line (b) rebuilt: identical to harmonised_comparison_lines.csv on %d rows' % len(L))
    if DEMO:
        print('EXAMPLE (deliberate wrong value): the line (c1) share closed to the model claimed as 0.385, the figure of line (b)')
        ok = check(out, claimed=0.385); print('EXAMPLE wrong value check: %s' % ('PASS' if ok else 'FAIL (the planted value is rejected)')); sys.exit(0 if not ok else 1)
    assert check(out), 'the share closed does not recompute from the readings'
    rob, ranges = robustness()
    csv.writer(open(D + 'harmonised_line_c.csv', 'w', newline='')).writerows(out)
    csv.writer(open(D + 'harmonised_line_c_robustness.csv', 'w', newline='')).writerows(rob)
    mr = [['food amount (Settings!B9)', 'avoidable waste (Settings!B14)', 'capacity, million people', 'what it is']]
    for (f, l), what in zip(req, ['the model as it is (41.5)', 'no avoidable waste (55.3)', 'c2: food amount x %.4f (supply requirement, own waste)' % M1,
                                  'c4: food amount x %.4f, no avoidable waste' % M0, 'c2 with the evaluator diet energy 7.376 MJ in place of 8.0 (food amount x %.4f)' % M1x,
                                  'c4 with 7.376 MJ in place of 8.0 (food amount x %.4f)' % M0x]):
        mr.append([round(f, 6), l, round(cap(f, l), 3), what])
    csv.writer(open(D + 'harmonised_line_c_model_runs.csv', 'w', newline='')).writerows(mr)
    print('FAO supply %.0f kcal = %.3f MJ; model eaten share on its loss factors s_e = %.4f; M1 = %.4f, M0 = %.4f (with 7.376 MJ: %.4f, %.4f); direct grain %.1f kg, embodied %.1f kg' % (KCAL, S_MJ, S_E, M1, M0, M1x, M0x, U_GRAIN, EMB))
    for lab, m in summ.items():
        ca, ch = m['centres']
        print(lab, 'centres as run %s harmonised %s' % ({k[:12]: round(x, 1) for k, x in ca.items()}, {k[:12]: round(x, 1) for k, x in ch.items()}))
        for ref, (ra, rh, Da, Dh, tot) in m['refs'].items(): print('   %-48s ref %.1f -> %.1f  D %.3f -> %.3f  share closed %.1f%%' % (ref, ra, rh, sum(Da.values()) / 5, sum(Dh.values()) / 5, 100 * tot))
        for k, x in m['disp'].items(): print('   dispersion %-24s SD %.3f -> %.3f (%.1f%% closed); max/min %.2f -> %.2f; harmonised range %.1f to %.1f' % (k, x[0], x[1], 100 * x[2], x[3], x[4], x[8], x[9]))
    for k, x in sorted(ranges.items()): print('robustness', k, '%.1f%% to %.1f%% over %d variants' % (100 * min(x), 100 * max(x), len(x)))
    for r in mr[1:]: print(r)
main()
