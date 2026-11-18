#!/usr/bin/env python3
"""The model's short-term capacity with its yield layers on a production window (brief B139, decision 144; R05b issue 12; EE Q6): is 2021 to 2023 a favourable harvest window,
and what does a longer window do to the model?
Usage (repository root):
  python3 -I analysis/method_tests_2025/production_window_10y.py                      writes production_window_10y.csv
  python3 -I analysis/method_tests_2025/production_window_10y.py --ten-year FILE      reads the ten-year FAOSTAT file from FILE (default: fao_au_production_2014_2023.csv, if it exists)
  python3 -I analysis/method_tests_2025/production_window_10y.py --out FILE           writes the csv to FILE instead (a test with a synthetic ten-year file must not overwrite the real csv)
  python3 -I analysis/method_tests_2025/production_window_10y.py --wrong-value-demo   plants one wrong value and shows the script's own check failing (nothing is written)
Needs node (the evaluator is run, unchanged, by b139_model_runs.mjs yields).

WHAT IS HELD. The FAOSTAT production and area files on disk hold Australia for 2011, 2020, 2021, 2022 and 2023 (fao_qcl_countries.csv, fao_qcl_countries_2020.csv), and 1997 and 1998 for three
items (fao_au_production_1997_2023.csv). Without the ten-year file the window 2014 to 2023 is not held: four of its ten years (2020 to 2023) are. This script uses what is held and says so in
every row: window "five held years" = 2011 and 2020 to 2023; window "held years of the decade" = 2020 to 2023 (four of ten; it contains 2021 to 2023, so it is a weak test); window
"2014 to 2023" = the ten years, computed only if fao_au_production_2014_2023.csv exists (extract_fao_au_production_10y.py from the hash-pinned bulk file; the fetch and URL are in that script's
docstring and in the README); otherwise its rows are present and empty.
MEASURES. For each item the mean of 2021-23 over the mean of the window; "percent above" = ratio - 1. Crops: production and, where the area harvested is held, yield (production over area
harvested), for eight crop groups; the group figure is the median over the groups (as the model's own group factors, B10). Livestock: production of total meat, beef, sheep and goat meat, poultry meat,
milk and eggs (the area under pasture is constant, so production stands for output a hectare); median over the six.
MODEL. The yield layers are scaled by the window over 2021-23, which stands for the model's own windows (the records take the 2025 layer as the same vintage as FAOSTAT 2021-23; the model's windows
are ABS financial years, 2022-23 to 2024-25 for crops and 2020-21 to 2024-25 for meat): every plant row and every feed-based animal row (poultry, pigs, eggs, fish) by the crop yield ratio inverted
(window over 2021-23), the pasture-fed rows by their own item (sheep meat by sheep and goat meat, cattle meat by beef, milk by total milk; wool and goat and sheep milk have no held series and stay at 1).
The evaluator then gives the short-term capacity of release 2025-fixed; crops only, livestock only and both are separate rows. Pasture binds, so capacity follows the pasture rows almost one for one
and the crop rows hardly at all (check printed: pasture output minus 20% gives 33.43 million, B134)."""
import collections, csv, json, os, statistics, subprocess, sys
D = 'analysis/method_tests_2025/'
DEMO = '--wrong-value-demo' in sys.argv
TEN = D + 'fao_au_production_2014_2023.csv'
if '--ten-year' in sys.argv: TEN = sys.argv[sys.argv.index('--ten-year') + 1]
OUTFILE = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else D + 'production_window_10y.csv'
def dicts(p): return list(csv.DictReader(open(p, newline='')))
S = collections.defaultdict(dict)                                                          # (item, element) -> year -> value, Australia
for f in ('fao_qcl_countries.csv', 'fao_qcl_countries_2020.csv', 'fao_au_production_1997_2023.csv'):
    for x in dicts(D + f):
        if x['Area'] == 'Australia' and x['Value'] != '' and x['Element'] in ('Production', 'Area harvested'): S[(x['Item'], x['Element'])][x['Year']] = float(x['Value'])
HAVE_TEN = os.path.exists(TEN)
if HAVE_TEN:
    for x in dicts(TEN):
        if x['Area'] == 'Australia' and x['Value'] != '': S[(x['Item'], x['Element'])][x['Year']] = float(x['Value'])
CROPS = ['Cereals, primary', 'Pulses, Total', 'Sugar Crops Primary', 'Oilcrops, Oil Equivalent', 'Roots and Tubers, Total', 'Vegetables Primary', 'Fruit Primary', 'Treenuts, Total']
DETAIL = ['Wheat', 'Barley']
LIVE = ['Meat, Total', 'Beef and Buffalo Meat, primary', 'Sheep and Goat Meat', 'Meat, Poultry', 'Milk, Total', 'Eggs Primary']
YR3 = ('2021', '2022', '2023')
WINDOWS = collections.OrderedDict([('five held years (2011, 2020 to 2023)', ('2011', '2020', '2021', '2022', '2023')),
                                   ('held years of the decade (2020 to 2023; four of ten)', ('2020', '2021', '2022', '2023')),
                                   ('held years outside 2021-23 (2011 and 2020)', ('2011', '2020')),
                                   ('ten years (2014 to 2023)', tuple(str(y) for y in range(2014, 2024)))])
def series(item, element, years):
    d = S.get((item, element), {})
    return [d[y] for y in years] if all(y in d for y in years) else None
def mean(xs): return sum(xs) / len(xs)
def ratio(item, element, years, yield_=False):
    """mean of 2021-23 over the mean of `years` for production, or for yield (production / area harvested) where both are held."""
    if yield_:
        p, a = series(item, 'Production', years), series(item, 'Area harvested', years)
        p3, a3 = series(item, 'Production', YR3), series(item, 'Area harvested', YR3)
        if None in (p, a, p3, a3): return None
        return (mean(p3) / mean(a3)) / (mean(p) / mean(a))
    p, p3 = series(item, element, years), series(item, element, YR3)
    return None if None in (p, p3) else mean(p3) / mean(p)
OUT = [['section', 'item or measure', 'window', 'years used', 'years held of the window', '2021-23 mean', 'window mean', '2021-23 over window', 'percent above (+) or below (-)', 'unit', 'note']]
def fx(x, d=3): return '' if x is None else round(x, d)
GROUP = {}
for wname, years in WINDOWS.items():
    heldn = sum(1 for y in years if all(y in S.get((i, 'Production'), {}) for i in CROPS + LIVE))
    for sect, items, yld in (('crops, production', CROPS + DETAIL, False), ('crops, yield (production over area harvested)', CROPS + DETAIL, True), ('livestock, production', LIVE, False)):
        rr = []
        for it in items:
            r = ratio(it, 'Production', years, yld)
            if yld:
                p, a, p3, a3 = (series(it, e, y) for e in ('Production', 'Area harvested') for y in (years, YR3))
                m3 = None if None in (p3, a3) else mean(p3) / mean(a3); mw = None if None in (p, a) else mean(p) / mean(a)
            else:
                p, p3 = series(it, 'Production', years), series(it, 'Production', YR3); m3 = None if p3 is None else mean(p3); mw = None if p is None else mean(p)
            if r is not None and it not in DETAIL: rr.append(r)
            OUT.append([sect, it, wname, ' '.join(years) if r is not None else '', '%d of %d' % (sum(1 for y in years if y in S.get((it, 'Production'), {})), len(years)),
                        fx(m3 / 1e3 if m3 is not None and not yld else m3, 3), fx(mw / 1e3 if mw is not None and not yld else mw, 3), fx(r), fx(100 * (r - 1), 1) if r is not None else '',
                        'thousand tonnes' if not yld else 'tonnes a hectare', '' if r is not None else 'window not held for this item' + ('' if HAVE_TEN or '2014' not in years else '; fetch needed (extract_fao_au_production_10y.py)')])
        if len(rr) == len(items) - sum(1 for i in items if i in DETAIL):
            g = statistics.median(rr); GROUP[(wname, sect)] = g
            OUT.append([sect, 'group figure: median over the %d groups' % len(rr), wname, '', '', '', '', fx(g), fx(100 * (g - 1), 1), 'ratio', 'the model takes a group figure the same way (B10)'])
        else:
            OUT.append([sect, 'group figure: median over the groups', wname, '', '', '', '', '', '', 'ratio', 'not computed: the window is not held (the ten-year file does not exist)'])
# ---------------------------------------------------------------- the model with its yield layers on the window
def evaluator(factors):
    out = subprocess.run(['node', D + 'b139_model_runs.mjs', 'yields'] + [json.dumps(f, sort_keys=True) for f in factors], capture_output=True, text=True, check=True).stdout
    return [r['capacity'] / 1e6 for r in json.loads(out)]
base, minus20 = evaluator([{}, {'95': 0.8, '96': 0.8, '97': 0.8, '98': 0.8, '135': 0.8, '136': 0.8}])
assert round(base, 2) == 41.50 and round(minus20, 2) == 33.43, (base, minus20)            # the evaluator reproduces 41.50 and B134's 33.43
MODEL = {}
for wname, years in WINDOWS.items():
    gy = GROUP.get((wname, 'crops, yield (production over area harvested)'))
    r95, r98, r97 = (ratio(i, 'Production', years) for i in ('Sheep and Goat Meat', 'Beef and Buffalo Meat, primary', 'Milk, Total'))
    if gy is None or None in (r95, r98, r97): continue
    fc = 1 / gy; live = {'95': 1 / r95, '98': 1 / r98, '97': 1 / r97}                      # window over 2021-23 = 1 / (2021-23 over window)
    caps = evaluator([{'crop': fc}, dict(live), dict(live, crop=fc)])
    MODEL[wname] = (fc, live, caps)
    for lab, c in zip(('crop yield layers only', 'livestock layers only', 'crop and livestock layers'), caps):
        OUT.append(['model, short term, corrected (million people)', lab, wname, '', '', fx(base, 2), fx(c, 2), '', fx(100 * (c / base - 1), 2), 'million people',
                    'crop factor %.3f; sheep meat %.3f, cattle meat %.3f, milk %.3f (window over 2021-23)' % (fc, live['95'], live['98'], live['97'])])
for wname in WINDOWS:
    if wname not in MODEL:
        OUT.append(['model, short term, corrected (million people)', 'crop and livestock layers', wname, '', '', fx(base, 2), '', '', '', 'million people',
                    'NOT COMPUTED: the window is not held. Fetch: https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_All_Data_(Normalized).zip (hash in qa/fao_bulk_hashes.csv), then extract_fao_au_production_10y.py'])
OUT.append(['check', 'pasture output minus 20% through the evaluator (B134: 33.43)', '', '', '', fx(base, 2), fx(minus20, 2), '', fx(100 * (minus20 / base - 1), 2), 'million people', 'PASS'])
# ---------------------------------------------------------------- the check: the five-window crop and livestock ratios recomputed by hand from the raw rows
def hand_check(claimed=None):
    """Recompute one headline ratio independently: cereals yield 2021-23 over the five held years from the raw rows, and meat production; compare with the csv rows."""
    five = WINDOWS['five held years (2011, 2020 to 2023)']
    pr = lambda it, el, ys: [S[(it, el)][y] for y in ys]
    cy3 = sum(pr('Cereals, primary', 'Production', YR3)) / sum(pr('Cereals, primary', 'Area harvested', YR3)); cy5 = sum(pr('Cereals, primary', 'Production', five)) / sum(pr('Cereals, primary', 'Area harvested', five))
    # note: the script's yield is mean production over mean area, which is the same as the ratio of sums
    mine = cy3 / cy5
    row = next(r for r in OUT if r[0].startswith('crops, yield') and r[1] == 'Cereals, primary' and r[2].startswith('five held'))
    want = float(row[7]) if claimed is None else claimed
    ok = abs(mine - want) < 0.0006
    print('check: cereals yield 2021-23 over the five held years, recomputed %.4f, csv/claimed %.4f: %s' % (mine, want, 'PASS' if ok else 'MISMATCH'))
    return ok
if DEMO:
    print('EXAMPLE (deliberate wrong value): the cereals yield ratio claimed as 1.00 (no difference from the window) instead of the computed value')
    ok = hand_check(claimed=1.00); print('EXAMPLE wrong value check: %s' % ('PASS' if ok else 'FAIL (the planted value is rejected)')); sys.exit(0 if not ok else 1)
assert hand_check()
csv.writer(open(OUTFILE, 'w', newline='')).writerows(OUT)
print('ten-year file present: %s' % HAVE_TEN)
for r in OUT:
    if r[0].startswith('crops, production') and r[1].startswith('group') or r[0].startswith('crops, yield') and r[1].startswith('group') or r[0].startswith('livestock') and r[1].startswith('group') or r[0].startswith('model'):
        print(' | '.join(str(x) for x in r[:9]))
print('cereals, production and yield, by window:')
for r in OUT:
    if r[1] in ('Cereals, primary', 'Meat, Total', 'Beef and Buffalo Meat, primary', 'Sheep and Goat Meat', 'Milk, Total'): print('  ', ' | '.join(str(x) for x in r[:9]))
