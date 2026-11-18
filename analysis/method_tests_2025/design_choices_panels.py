#!/usr/bin/env python3
"""Table 8 of Paper B in three panels (brief B139, decision 144; R05b issue 10; EE M7, Mod M7, Mod Q9).
Usage (repository root):
  python3 -I analysis/method_tests_2025/design_choices_panels.py                      writes design_choices_panels.csv
  python3 -I analysis/method_tests_2025/design_choices_panels.py --wrong-value-demo   plants one wrong value and shows the script's own check failing (nothing is written)
Panel A  changes made in the model, one setting or definition at a time (the drought factor on both rules: every yield, the model's own rule, and crops only, the bound of B134), corrected release
         unless the row says improved; the two bundles ("Australian settings", "time frame") are marked as bundles; diets A and B are the ranked diet rows and diet C an upper bound; the Monte
         Carlo is the last rows, labelled a spread of joint draws.
Panel B  ratios between methods (not changes in the model): the CSIRO and University of Queensland proportional count and its food-balance rebuild, the energy counts of exports, and the footprint's
         own-productivity ratio of output to consumption (which counts exports as those counts do). Each row says so in the "kind" column.
Panel C  the other methods' own factors where their papers give them, taken from the literature register (qa/literature_register.csv): the numbers typed here are checked against the register's
         "what_taken" text, and the register's id and status are copied from the file. A "same choice here" column gives this study's factor for the same kind of choice.
The ladder (ladder.csv, Figure 3's ladder) is dropped from Table 8; ladder.csv and design_choices.csv are untouched. Reads, read only: design_choices.csv, ladder.csv, model_entry.csv,
analysis/comparators_2025/diet_land.csv and proportional_count.csv, analysis/resilience_2025/drought_bounds_paper_B.csv, pal_one_at_a_time_2025.csv,
analysis/pasture_2025/pasture_output_one_at_a_time_2025-fixed.csv, harmonised_robustness_footprint.csv, qa/literature_register.csv. Factors are high over low, as in the paper (a factor, not a ratio of people to capacity)."""
import csv, sys
D = 'analysis/method_tests_2025/'
DEMO = '--wrong-value-demo' in sys.argv
def dicts(p): return list(csv.DictReader(open(p, newline='')))
DC = {(r['design choice'], r['what is compared'][:24], r['method and release']): r for r in dicts(D + 'design_choices.csv')}
def dc(choice, what, rel):
    ks = [k for k in DC if k[0] == choice and k[1] == what[:24] and k[2] == rel]; assert len(ks) == 1, (choice, what, rel, ks); return DC[ks[0]]
HEAD = ['panel', 'design choice', 'what is compared', 'low', 'high', 'unit', 'factor (high over low)', 'factor, largest (where the source gives a range)', 'method and release', 'kind', 'moved from (existing Table 8 row)',
        'same choice in this study (factor)', 'source', 'register id', 'register status', 'note', 'order among the single choices of panel A (low to high factor)']
rows = [HEAD]
def add(panel, choice, what, lo, hi, unit, rel, kind, moved, same, source, rid='', status='', note='', fmax=None, factor=None):
    f = hi / lo if factor is None else factor
    rd = lambda x: round(x, 1) if (unit == 'million people' and x >= 10) else round(x, 2)
    rows.append([panel, choice, what, rd(lo), rd(hi), unit, round(f, 2),
                 '' if fmax is None else round(fmax, 2), rel, kind, moved, same, source, rid, status, note, ''])
# ---------------------------------------------------------------- Panel A
A, SRC = 'A: changes made in the model, one at a time', ''
r = dc('Drought allowance', 'average year; worst year of 5, 10, 20, 50, 100', 'corrected')
DB = {(x['release'], x['preset'], x['return_period']): x for x in dicts('analysis/resilience_2025/drought_bounds_paper_B.csv')}
d100 = DB[('2025-fixed', 'short', '100')]
mean_, both_, crop_ = float(d100['mean_year_capacity']) / 1e6, float(d100['both_applied']) / 1e6, float(d100['crop_only']) / 1e6
assert abs(both_ - float(r['capacity low (million)'])) < 0.05 and abs(mean_ - float(r['capacity high (million)'])) < 0.05
add(A, 'Drought allowance, factor on every yield (the model\'s rule)', 'worst year of 100 against the average year', both_, mean_, 'million people', 'corrected', 'definition', 'Drought allowance', '',
    'design_choices.csv; drought_bounds_paper_B.csv (B134)', note='the factor taken from the wheat, oats and barley record is applied to pasture-fed output, which no livestock series has tested')
add(A, 'Drought allowance, factor on crops only (bound)', 'worst year of 100 against the average year, pasture-fed output at its mean', crop_, mean_, 'million people', 'corrected', 'definition (bound)', 'new row (B134)', '',
    'drought_bounds_paper_B.csv (B134)', note='95% of the fall of the first row comes from applying the cereal factor to pasture-fed output')
for rel, nm in (('corrected', 'corrected'), ('improved', 'improved')):
    r = dc('Avoidable waste', '12% (default) against none' if rel == 'corrected' else '12% against none', rel)
    add(A, 'Avoidable waste', '12% against none', float(r['capacity low (million)']), float(r['capacity high (million)']), 'million people', rel, 'setting', 'Avoidable waste (%s)' % rel, '', 'design_choices.csv', factor=float(r['high over low']),
        note='a setting by the rule of section 6.9; the sentence of the abstract states it one at a time beside the drought allowance (decision 146)')
r = dc('Land available', 'cropland as it is against doubled out of non-agricultural land', 'corrected')
add(A, 'Land available', 'cropland as it is against doubled out of non-agricultural land', float(r['capacity low (million)']), float(r['capacity high (million)']), 'million people', 'corrected', 'definition', 'Land available', '', 'design_choices.csv', factor=float(r['high over low']))
r = dc('Unit of self-sufficiency', 'nation; sum over states, NRM regions, SA4, SA3, SA2 (state yield basis)', 'corrected')
add(A, 'Unit of self-sufficiency', 'nation against the sum over SA2s (state yield basis)', float(r['capacity low (million)']), float(r['capacity high (million)']), 'million people', 'corrected', 'definition', 'Unit of self-sufficiency', '', 'design_choices.csv', factor=float(r['high over low']))
r = dc('Diet', 'guideline diets from 15% to 5% meat and eggs', 'improved')
add(A, 'Diet, guideline diets', 'guideline diets from 15% to 5% meat and eggs', float(r['capacity low (million)']), float(r['capacity high (million)']), 'million people', 'improved', 'definition', 'Diet', '', 'design_choices.csv (diet_land.csv)', factor=float(r['high over low']),
    note='not monotone in the meat share: a dip at 2.5% and a cliff between 5% (103.3) and 7.5% (66.9)')
DL = {x['diet']: float(x['people_fed_million']) for x in dicts('analysis/comparators_2025/diet_land.csv')}
dflt = DL["The model's default diet (12% meat and eggs, 57.8% red)"]
add(A, 'Diet, optimised A', 'default diet against nutrition-optimised diet A (foods swapped within groups, ten micronutrients)', dflt, DL['Optimised A: foods swapped within groups'], 'million people', 'improved', 'definition', 'Diet (optimised), split',
    '', 'diet_land.csv; analysis/nutrition_lp_2025/README.md', note='the diet the nutrition README says is the one to quote')
add(A, 'Diet, optimised B', 'default diet against nutrition-optimised diet B (serves free in the guideline range, ten micronutrients)', dflt, DL['Optimised B: serves free in the guideline range'], 'million people', 'improved', 'definition',
    'Diet (optimised), split', '', 'diet_land.csv; analysis/nutrition_lp_2025/README.md', note='B and C would not be adequate without fortification or supplements (micronutrients B12 and others, README)')
r = dc('Diet (optimised)', 'default diet against nutrition-optimised diet C (ten micronutrients)', 'improved')
assert abs(float(r['capacity high (million)']) - DL['Optimised C: free choice']) < 0.05
add(A, 'Diet, optimised C (an upper bound)', 'default diet against nutrition-optimised diet C (free choice, ten micronutrients)', float(r['capacity low (million)']), float(r['capacity high (million)']), 'million people', 'improved',
    'upper bound, not a realistic diet', 'Diet (optimised)', '', 'design_choices.csv; diet_land.csv', factor=float(r['high over low']), note='0.06 ha of cropland and 0.13 ha of pasture a person; a land-efficiency bound the README says is not a realistic diet; it is outside the ranked rows')
PAL = {(x['release'], x['preset'], x['pal']): float(x['capacity']) / 1e6 for x in dicts(D + 'pal_one_at_a_time_2025.csv')}
for rel in ('2025-fixed', '2025-improved'):
    add(A, 'Energy requirement (PAL 1.2 to 2.2)', 'the NHMRC range, 6.9 MJ against 12.6 MJ a day, everything else at base', PAL[(rel, 'short', '2.2')], PAL[(rel, 'short', '1.2')], 'million people',
        'corrected' if rel == '2025-fixed' else 'improved', 'setting (drawn only in part)', 'new row (B134)', '', 'pal_one_at_a_time_2025.csv (B134)', note='the Monte Carlo draws PAL 1.4 to 1.8 only')
add(A, 'Energy requirement, the drawn window (PAL 1.4 to 1.8)', 'the window the Monte Carlo draws, 8.0 MJ against 10.3 MJ a day', PAL[('2025-fixed', 'short', '1.8')], PAL[('2025-fixed', 'short', '1.4')], 'million people', 'corrected',
    'setting (drawn)', 'new row (B134)', '', 'pal_one_at_a_time_2025.csv (B134)')
PO = {(x['preset'], x['pasture_output_factor']): float(x['capacity']) / 1e6 for x in dicts('analysis/pasture_2025/pasture_output_one_at_a_time_2025-fixed.csv')}
add(A, 'Pasture output (minus 20% to plus 20%)', 'national pasture-fed output 20% below and 20% above, everything else at base', PO[('short', '0.8')], PO[('short', '1.2')], 'million people', 'corrected', 'setting (not drawn)', 'new row (B134)', '',
    'pasture_output_one_at_a_time_2025-fixed.csv (B134)', note='pasture binds at both ends; a bound, not a range with a probability')
r = dc('Australian settings', 'thesis method corrected against improved', 'short term')
add(A, 'Australian settings (a bundle)', 'thesis method corrected against improved: beef by state, dairy land, loss factors and more at once', float(r['capacity low (million)']), float(r['capacity high (million)']), 'million people', 'short term',
    'bundle of settings', 'Australian settings', '', 'design_choices.csv', factor=float(r['high over low']), note='not one change; kept out of the single-choice order')
r = dc('Time frame', 'long-term settings against short-term settings', 'corrected')
add(A, 'Time frame (a bundle)', 'long-term settings against short-term settings: diet, organic yields, waste, a 100-year allowance and a 30% reserve at once', float(r['capacity low (million)']), float(r['capacity high (million)']),
    'million people', 'corrected', 'bundle of settings', 'Time frame', '', 'design_choices.csv', factor=float(r['high over low']), note='not one change; kept out of the single-choice order')
for rel in ('corrected', 'improved'):
    r = [x for x in dicts(D + 'design_choices.csv') if x['design choice'] == 'Uncertainty (Monte Carlo)' and x['method and release'] == rel][0]
    add(A, 'Uncertainty (Monte Carlo)', '5th to 95th percentile over %s uncertain settings, varied together' % ('19 (18 drawn)' if rel == 'corrected' else '18'), float(r['capacity low (million)']), float(r['capacity high (million)']),
        'million people', rel, 'spread of joint draws, not one at a time', 'Uncertainty (Monte Carlo)', '', 'design_choices.csv (results/ranges_2025-%s_wide.csv)' % ('fixed' if rel == 'corrected' else 'improved'), factor=float(r['high over low']))
# ---------------------------------------------------------------- Panel B
B = 'B: ratios between methods (not changes in the model)'
M_FIX = float(next(x for x in dicts(D + 'model_entry.csv') if x['release'] == '2025-fixed')['short term (million)'])
r = dc('Exports counted', 'the model against the CSIRO and UQ proportional count (27 at home + 63 abroad)', 'published count')
add(B, 'Exports counted: the CSIRO and University of Queensland proportional count', 'the model against the published count (27 at home plus 63 abroad)', float(r['capacity low (million)']), float(r['capacity high (million)']), 'million people',
    'published count', 'ratio between a published count and the model, not a model run', 'Exports counted', '', 'design_choices.csv (published_values.csv)', factor=float(r['high over low']), note='the model is self-sufficient by design (section 8.2) and carries no export basket')
PC = dicts('analysis/comparators_2025/proportional_count.csv')
def pc(weight, feed, basis): return float(next(x for x in PC if x['weighting'] == weight and x['domestic use'] == feed and x['population basis'] == basis)['people supplied in the proportions of domestic use (million)'])
B25 = '2025 (results/2025-fixed.csv)'
add(B, 'Exports counted: the proportional count rebuilt from the food balance, feed a domestic use', 'the model against production over domestic use times the 2025 population, FAO energy per kg (68.0 to 70.1)', M_FIX,
    pc('energy, FAO kcal per kg (Australia first)', 'with feed', B25), 'million people', 'food balance rebuild', 'ratio between a rebuilt count and the model, not a model run', 'new row (R05b)', '',
    'proportional_count.csv', fmax=pc('energy, FAO kcal per kg (world first)', 'with feed', B25) / M_FIX)
add(B, 'Exports counted: the proportional count rebuilt from the food balance, feed not a domestic use', 'the model against production over domestic use times the 2025 population, FAO energy per kg (101.2 to 103.6)', M_FIX,
    pc('energy, FAO kcal per kg (Australia first)', 'without feed', B25), 'million people', 'food balance rebuild', 'ratio between a rebuilt count and the model, not a model run', 'new row (R05b)', '',
    'proportional_count.csv', fmax=pc('energy, FAO kcal per kg (world first)', 'without feed', B25) / M_FIX)
add(B, 'Exports counted: the proportional count rebuilt by mass, feed a domestic use', 'the model against production over domestic use by mass times the 2025 population', M_FIX, pc('mass', 'with feed', B25), 'million people',
    'food balance rebuild', 'ratio between a rebuilt count and the model, not a model run', 'new row (R05b)', '', 'proportional_count.csv')
add(B, 'Exports counted: the proportional count rebuilt by mass, feed not a domestic use', 'the model against production over domestic use by mass times the 2025 population', M_FIX, pc('mass', 'without feed', B25), 'million people',
    'food balance rebuild', 'ratio between a rebuilt count and the model, not a model run', 'new row (R05b)', '', 'proportional_count.csv')
for what, key in (('FAO\'s own food energy per kg', 'FAO balance energy'), ('typed as-traded densities', 'as-traded densities')):
    r = [x for x in dicts(D + 'design_choices.csv') if x['design choice'] == 'Exports counted (energy)' and ('FAO' in x['what is compared'] if key.startswith('FAO') else 'as-traded' in x['what is compared'])][0]
    add(B, 'Exports counted by energy (%s)' % what, 'the model against exports alone as an energy count, all foods', float(r['capacity low (million)']), float(r['capacity high (million)']), 'million people', 'energy count',
        'ratio between an energy count of exports and the model, not a model run', 'Exports counted (energy)', '', 'design_choices.csv (energy_exports.csv)', factor=float(r['high over low']), note='exports alone, so not a count of the people the model feeds')
FPR = dicts(D + 'harmonised_robustness_footprint.csv')
def fpr(build, land): return next(x for x in FPR if x['build'] == build and x['land type'] == land)
for build in ('build 1', 'build 3'):
    for land in ('crop and pasture together', 'cropland-bound', 'pasture'):
        x = fpr(build, land)
        add(B, 'Footprint\'s own-productivity ratio of output to consumption (%s, %s)' % (build, land), 'Australia\'s output over its consumption, each in world-average hectares: the export-inclusive ratio the footprint reads at Australian productivity',
            float(x['consumption (Mha, world-average)']), float(x['output (Mha, world-average) = reading x footprint']), 'ratio of hectares', 'footprint, own productivity',
            'ratio inside one method, counts exports as the proportional count does', 'new row (B135, R05b)', '2.41 (the proportional count over the model)', 'harmonised_robustness_footprint.csv', factor=float(x['output over consumption']),
            note='the two columns are consumption and output in Mha; the factor is the ratio printed there (%s)' % x['output over consumption'])
# ---------------------------------------------------------------- Panel C
C = "C: the other methods' own factors, from their papers (literature register)"
REG = {x['id']: x for x in dicts('qa/literature_register.csv')}
def regcheck(rid, *needles):
    t = REG[rid]['what_taken']
    for n in needles: assert n in t, ('register %s does not hold %r' % (rid, n), t)
    return REG[rid]['status'], REG[rid]['read_or_reported']
def addc(choice, what, lo, hi, rid, needles, same, note='', fmax=None, unit='as printed by the paper', kind='the paper\'s own factor'):
    st, rd = regcheck(rid, *needles)
    add(C, choice, what, lo, hi, unit, 'as in the paper', kind, 'new row (R05b, Mod M7)', same, 'qa/literature_register.csv ' + rid, rid, '%s; %s' % (st, rd), note, fmax)
addc('Gifford et al. 1975: exports', 'all production eaten at home against half of the protein exported (protein count, million people)', 30, 60, 'L002', ('60 million (protein)', '30 million if half the protein is exported'),
     'exports 2.41 to 6.36 (panel B); the model carries none', 'read in Henry and Godden 1995, Table 1, p. 98', unit='million people')
addc('Gifford et al. 1975: which nutrient binds', 'protein count against energy count, all production eaten at home (million people)', 60, 82, 'L002', ('82 million (food energy)', '60 million (protein)'),
     'the model\'s diet holds both; its protein is never the binding constraint', 'read in Henry and Godden 1995, Table 1, p. 98', unit='million people')
addc('House of Representatives committee 1994: a margin for bad seasons', 'subsistence capacity of 50 plus million against 30 to 35 million with a margin for a run of bad seasons (low shown at 35, the top of the margin)', 35, 50, 'L006', ('50 plus million', '30-35 million'),
     'drought allowance 2.19 (every yield) and 1.03 (crops only), panel A', 'a stated margin, not a return period (section 6.6); the factor uses 35, the largest factor (column H) uses 30', fmax=50 / 30, unit='million people')
addc('Peters et al. 2016: ten diets, United States', 'the ten diet scenarios, people on US agricultural land (million)', 402, 807, 'L015', ('402 to 807 million',),
     'guideline diets 2.14; optimised A 1.60, B 3.77 (panel A)', 'closed system, no trade', unit='million people')
addc('Peters, Wilkins and Fick 2007: 42 diets, New York State', 'capacity on 2.03 Mha across 42 diets (million people)', 2.04, 6.08, 'L040', ('2.04 to 6.08 million',),
     'guideline diets 2.14; optimised A 1.60, B 3.77 (panel A)', 'the register holds the short form only; the abstract rounds to 2.0 to 6.2', unit='million people')
addc('Cassidy et al. 2013: calories produced against delivered', 'world people nourished a hectare, delivered against as produced', 6.0, 10.1, 'L016', ('6 people per hectare delivered', '10.1 as produced'),
     'diet and feed: guideline diets 2.14 (panel A)', 'crop calories lost to feed and other uses; the United States 5.4 against 16.1 is a factor of 2.98', unit='people per hectare')
addc('Cassidy et al. 2013: crops fed to people', 'calories and people nourished if crops fed people directly, up to 70% more (4 billion people)', 1.0, 1.7, 'L016', ('up to 70% more calories',),
     'diet 2.14 to 3.77 (panel A)', 'the paper\'s own figure, a ratio of 1.7', unit='ratio')
addc('Alexander et al. 2016: Australia against the world', 'HALF index, percentage of world land, 2011: the world against Australia', 35.13, 112.20, 'L017', ('112.20', '35.13'),
     'diet 1.60 to 7.88 (panel A)', 'the index of the diet, not a capacity; on the paper\'s basis (supplementary Table S5)', unit='percentage of world land')
addc('Simpson et al. 2000: footprint against the world average', 'Australia\'s footprint against the world average, ha a person (1991-92)', 1.8, 5.96, 'L023', ('5.96', 'world average 1.8'),
     'not a capacity; the footprint\'s own-productivity reading is 1.56 to 2.82 times the model (Table 3)', 'sea products excluded; fair share 1.3 gives 4.6', unit='ha a person')
addc('Wackernagel et al. 1999: biocapacity against footprint', 'Australia, 1993 data: footprint 9.0 against bio-capacity 14.0 ha a person (world-average hectares)', 9.0, 14.0, 'L244', ('9.0', '14.0'),
     'not a capacity in people; no Australian capacity in people is printed', 'Table 4, p. 386; the paper prints no Australian capacity in people', unit='ha a person')
addc('Gifford et al. 1975: land taken as intensive', 'intensive land scaled from 40.5 to 70 Mha (the factor Paper B section 6.4 cites)', 40.5, 70, 'L035', ('70 Mha',),
     'land 1.09 (panel A)', 'UNVERIFIED in the register: L035 holds the 70 Mha only; the 40.5 is the draft sentence of section 6.4 (Henry and Godden 1995, p. 99, not in the register); a register entry is needed before this row is printed', unit='Mha')
# ---------------------------------------------------------------- check: every factor in the written rows recomputes from its own low and high
def check(rr, planted=None):
    ok = True; n = 0
    for r_ in rr[1:]:
        lo, hi, f = float(r_[3]), float(r_[4]), float(r_[6])
        if planted and r_[1].startswith(planted[0]): f = planted[1]
        want = hi / lo
        tol = 0.011 * max(1.0, want) if r_[5] == 'million people' else 0.011 * max(1.0, want)
        if abs(f - want) > tol:
            ok = False; print('FAIL %s | %s: factor %.2f, recomputed %.3f from low %.3f and high %.3f' % (r_[0][:1], r_[1][:60], f, want, lo, hi))
        n += 1
    print('check: %d rows, every factor recomputed from low and high: %s' % (n, 'PASS' if ok else 'FAIL'))
    return ok
SINGLE = [r_ for r_ in rows[1:] if r_[0].startswith('A:') and not r_[9].startswith(('bundle', 'upper', 'spread'))]
for n, r_ in enumerate(sorted(SINGLE, key=lambda x: float(x[6])), 1): r_[-1] = n
def main():
    if DEMO:
        print('EXAMPLE (deliberate wrong value): the factor of diet A planted as 3.77 (diet B\'s) instead of 1.60')
        ok = check(rows, planted=('Diet, optimised A', 3.77)); print('EXAMPLE wrong value check: %s' % ('PASS' if ok else 'FAIL (the planted value is rejected)')); sys.exit(0 if not ok else 1)
    assert check(rows)
    csv.writer(open(D + 'design_choices_panels.csv', 'w', newline='')).writerows(rows)
    for p in ('A', 'B', 'C'):
        print('Panel', p)
        for r_ in rows[1:]:
            if r_[0].startswith(p + ':'): print('  %-90s %8s %8s %6s %6s | %s' % (r_[1][:90], r_[3], r_[4], r_[6], r_[7], r_[9][:50]))
main()
