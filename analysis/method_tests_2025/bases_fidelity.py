#!/usr/bin/env python3
"""Bases, fidelity and the intake variant of the method tests (brief B116; decisions 109 and 110; R03b issues 9 and 10).
Usage (repository root):
  python3 -I analysis/method_tests_2025/bases_fidelity.py            # write the four csvs below
  python3 -I analysis/method_tests_2025/bases_fidelity.py --check [DIR] # recompute and compare with the csvs in DIR (default this folder); exit 1 on any mismatch
Reads (nothing here is written by another script of this folder): gap_attribution.csv, published_values.csv, second_build_values.csv, simpson_food.csv,
half_index.csv, half_landuse.csv, cassidy.csv, henry_godden_summary.csv, fbs_au_world_2021_23.csv, fao_au_production_1997_2023.csv, ladder.csv, model_entry.csv,
harmonised_comparison.csv (a cross-check of the supply-basis readings only), analysis/loss_factors_2025/fao_region2_loss.csv and compare.csv,
baseline/thesis_totals_capacity.csv, results/2011-thesis.csv, results/2011.csv, results/2025-fixed.csv, web/public/data/2025-fixed/regions.json.
simpson_food.py and half_index.py are run in memory up to the line that writes their csv (as harmonised_comparison.py does), so their csvs are not rewritten.
Writes:
  bases.csv                      one row per method and basis (as run; harmonised): population, energy, protein, land, data years, waste
  fidelity.csv                   one row per method and component: the authors' figure, the rebuild as run and on the authors' printed inputs, the gap, a verdict
  intake_variant.csv             every harmonised reading on an intake basis (food supply less retail and household waste) and whether the gap to the model widens
  gap_attribution_readable.csv   gap_attribution.csv restated: residual as a share of the figure, "within rounding", and ill-conditioned shares as absolute changes
Verdict rule (decision 109): |gap| within the rounding of the published figure or within 2% = reproduced; within 10% = partly; beyond 10% = not reproduced.
Ill-conditioned (B116): a residual under 1% of the published figure; its shares are printed as the absolute change (and, for HALF Australia, people).
Deterministic: no randomness, no clock; every number is computed from the files named above."""
import collections, contextlib, csv, io, json, math, os, sys
D = 'analysis/method_tests_2025/'
YR = ('2021', '2022', '2023')
def dicts(path): return list(csv.DictReader(open(path, newline='')))
def rows(path): return list(csv.reader(open(path, newline='')))
def run_upto(script, marker):
    src = open(D + script).read()
    assert src.count(marker) == 1, (script, marker)
    ns = {'__name__': 'b116_' + script[:-3]}
    with contextlib.redirect_stdout(io.StringIO()): exec(compile(src[:src.index(marker)], D + script, 'exec'), ns)
    return ns
def rnd(x, d):
    if x is None or x == '': return ''
    return round(x, d) + 0.0

# ================================================================ common inputs
FB = collections.defaultdict(dict)
for r in dicts(D + 'fbs_au_world_2021_23.csv'):
    try: FB[(r['Area'], r['Item'], r['Element'])][r['Year']] = float(r['Value'])
    except ValueError: pass
def fbs(item, el, area='Australia'): return sum(FB[(area, item, el)].get(y, 0.0) for y in YR)          # three years summed
pop_fbs = fbs('Population', 'Total Population - Both sexes') * 1000                                       # persons x 3 years
kcal_day = fbs('Grand Total', 'Food supply (kcal)') * 1e6 / pop_fbs / 365
prot_day = fbs('Grand Total', 'Protein supply quantity (t)') * 1e6 / pop_fbs / 365
LU = collections.defaultdict(dict)
for r in dicts(D + 'half_landuse.csv'):
    if r['Area'] == 'Australia': LU[r['Item']][r['Year']] = float(r['Value']) / 1000                  # Mha
fao_crop = sum(LU['Cropland'][y] for y in YR) / 3
fao_past = sum(LU['Permanent meadows and pastures'][y] for y in YR) / 3
LAND = fao_crop + fao_past
LAND11 = LU['Cropland']['2011'] + LU['Permanent meadows and pastures']['2011']
z1 = json.load(open('web/public/data/2025-fixed/regions.json'))['regions']
z1 = z1['1'] if '1' in z1 else next(v for v in z1.values() if v.get('id') == 1)
abs_crop, abs_past = z1['land']['cropping'] / 1e4, z1['land']['pasture'] / 1e4
POP_MODEL = float(next(r for r in dicts('results/2025-fixed.csv') if r['zone'] == '1' and r['preset'] == 'short')['population'])
ME = {r['release']: r for r in dicts(D + 'model_entry.csv')}
M_FIX, M_IMP = float(ME['2025-fixed']['short term (million)']), float(ME['2025-improved']['short term (million)'])
LAD = {r['step']: float(r['million people']) for r in dicts(D + 'ladder.csv')}
M_FIX_NW, M_IMP_NW = LAD['average year, no avoidable waste'], LAD['average year, improved, no avoidable waste']
HG = rows(D + 'henry_godden_summary.csv')
HG_E = float(next(r for r in HG if r and r[0] == 'TOTAL')[1]); HG_P = float(next(r for r in HG if r and r[0] == 'TOTAL')[2])    # PJ; 1e10 g
HG_MJ = float(next(r for r in HG if r and r[0].startswith('implied energy per person'))[3])
HG_FE, HG_FP = 82 / 466, 60 / 294          # Henry and Godden Table 4: Gifford et al.'s projected populations (million) over the scaled output (1e15 J; 1e10 g)
hg_prot_implied = 1e10 / (HG_FP * 1e6) / 365                                                             # g a person a day
CAS = {(r['period'], r['country']): r for r in dicts(D + 'cassidy.csv')}
cas_au = CAS[('2021-23', 'Australia')]
SB = {r['quantity']: float(r['value']) for r in dicts(D + 'second_build_values.csv')}
def sb(start): return next(v for k, v in SB.items() if k.startswith(start))
fp_pop = sum(FB[('Australia', 'Population', 'Total Population - Both sexes')][y] for y in ('2021', '2022')) / 2 / 1000   # million, as foran_poldy_balance.py
S = run_upto('simpson_food.py', "csv.writer(open('analysis/method_tests_2025/simpson_food.csv'")
H = run_upto('half_index.py', "csv.writer(open('analysis/method_tests_2025/half_index.csv'")

# ================================================================ 1. bases.csv
B_HEAD = ['method', 'basis', 'population basis', 'population (million)', 'energy a person a day', 'energy source', 'protein basis', 'land basis', 'land year',
          'production data years', 'consumption data years', 'waste treatment']
FAO_SUPPLY = 'FAO food supply includes retail and household waste (FAO losses are removed only up to retail), so waste sits inside the per-person need'
def bases():
    hp = 'FAO head count 2021-23 (food balance), the food balance\'s own per-person basis; the model\'s %.2f million enters no harmonised method reading' % (POP_MODEL / 1e6)
    pf = round(pop_fbs / 3e6, 2)
    kc = '%.0f kcal (%.1f MJ)' % (kcal_day, kcal_day * 4.184 / 1000)
    pr = '%.1f g, FAO food supply 2021-23' % prot_day
    out = [B_HEAD]
    m = 'Energy and protein balance (Gifford; Henry and Godden)'
    out.append([m, 'as run', 'none at run time: people = output x a consumption factor; the factors are Gifford et al.\'s projected populations (82 and 60 million) over the scaled output (Henry and Godden Table 4)', '',
                '%.1f MJ (%.0f kcal), implied by the factor 82/466' % (HG_MJ, HG_MJ * 1000 / 4.184), 'Gifford et al. 1975 through Henry and Godden 1995; henry_godden_summary.csv',
                '%.0f g a day implied by the factor 60/294; protein counted alone' % hg_prot_implied,
                'food production of the land in use, scaled to Nix\'s 70 Mha over 45.7 Mha (1990-91 in use) or over 59.95 Mha (1990-91 sown pasture 28.3 carried forward plus 2025 cropping 31.65); or production as it is',
                '1990-91 in-use land; 2025 cropping', 'FAO food balance 2021-23 (production less feed, seed, non-food, losses, processing; exports counted as food)', 'none: the consumption factor of 1975',
                'no waste charged; the factor (%.1f MJ, nearly twice a plain 8.8 MJ requirement) holds any waste implicitly' % HG_MJ])
    out.append([m, 'harmonised', hp, pf, kc, 'FAO food balance 2021-23, Grand Total food supply', pr, 'production of the land as it is, no scale-up (Australia\'s %.2f Mha of agricultural land)' % LAND,
                '2021-23', 'FAO food balance 2021-23', 'FAO food balance 2021-23', FAO_SUPPLY])
    m = 'Ecological footprint, food row (Simpson)'
    out.append([m, 'as run', 'per-person food use: FAO head count 2021-23 (food balance); 1991-92 fidelity on ABS 4306.0', pf, 'none: a mass basis (kg of each food)', '',
                'build 1 shares world pasture by edible protein (world protein a kg, FAO 2021-23); builds 2 and 3 do not use protein',
                'Australia\'s cropland %.2f and permanent meadows and pastures %.2f Mha (FAOSTAT), each at world-average productivity (build 1 FAOSTAT 2021-23 world yields; build 3 the thesis\'s printed 1990 world yields)' % (fao_crop, fao_past),
                '2021-23 mean', 'FAOSTAT world yields 2021-23 (build 3: FAO 1990 as printed by Wackernagel 1994)', 'FAO food balance 2021-23 (food use, kg a person)', FAO_SUPPLY])
    out.append([m, 'harmonised', hp, pf, 'none: a mass basis', '', 'as run', 'as run; build 3 on FAOSTAT 2021-23 world yields of the same rows', '2021-23 mean', 'FAOSTAT 2021-23', 'FAO food balance 2021-23', FAO_SUPPLY])
    m = 'HALF index (Alexander)'
    out.append([m, 'as run', 'per-person food use: FAO head count 2021-23 (food balance); the index itself uses world population and world land', pf, 'none: a mass basis', '', 'none',
                'world cropland (harvested area x cropland-to-harvested adjustment) and world pasture at world-average production; the capacity reading divides Australia\'s %.2f Mha of cropland and pasture by the diet\'s hectares' % LAND,
                '2021-23 mean', 'FAOSTAT world production and land 2021-23', 'FAO food balance 2021-23 (food, the diet)', FAO_SUPPLY])
    out.append([m, 'harmonised', hp, pf, 'none: a mass basis', '', 'none', 'as run (already on the harmonised inputs)', '2021-23 mean', 'FAOSTAT 2021-23', 'FAO food balance 2021-23', FAO_SUPPLY])
    m = 'People per hectare (Cassidy)'
    out.append([m, 'as run', 'none in the rate; capacity = delivered calories over a per-person diet', '', '2,700 kcal (11.3 MJ)', 'Cassidy et al. 2013, p. 5: 985,500 kcal a year', 'none (calories only)',
                'harvested area of 21 crops, %s Mha (2021-23); the 190 million reading applies the rate to all %.2f Mha of cropland' % (cas_au['cropland of these crops (Mha)'], fao_crop),
                '2021-23 mean', 'FAOSTAT crops and food balance 2021-23', 'the paper\'s 2,700 kcal (c. 2000)', 'the paper\'s 2,700 kcal is a per-person allowance; it does not say whether waste is inside it. Delivered calories are food balance calories, so the numerator includes food that is wasted'])
    out.append([m, 'harmonised', hp, pf, kc, 'FAO food balance 2021-23, Grand Total food supply', 'none (calories only)', 'the delivered calories of the cropland as it is (%s Mha harvested)' % cas_au['cropland of these crops (Mha)'],
                '2021-23 mean', 'FAOSTAT 2021-23', 'FAO food balance 2021-23', FAO_SUPPLY])
    m = 'Commodity balance (Foran and Poldy)'
    out.append([m, 'as run', 'their 2050 requirement over their 2050 base-case population (25.1 million); the actual-use reading divides FAO food use by the 2021-22 mean head count', round(fp_pop, 2),
                'none: tonnes of grain, meat and fish', '', 'none', 'none: production only (FAOSTAT 2021-23 cereals and meat; food balance fish)', '',
                'FAOSTAT 2021-23', 'Foran and Poldy 2002, Table 2.5 (2050 requirements); FAO food balance 2021-23 for actual use', 'their requirement is a supply-level requirement (no waste term); FAO food use includes retail and household waste'])
    out.append([m, 'harmonised', 'FAO food use per person on the 2021-22 mean head count (the method script; under 0.5%% from the three-year %.2f)' % pf, round(fp_pop, 2), 'none', '', 'none', 'none', '', 'FAOSTAT 2021-23', 'FAO food balance 2021-23', FAO_SUPPLY])
    m = 'Failure probability (Fearnside)'
    out.append([m, 'as run', 'the model\'s 2025 population (failure probability at the population)', round(POP_MODEL / 1e6, 2), 'the model\'s default diet, 8.0 MJ as eaten', 'analysis/nutrition_lp_2025/README.md',
                'the model\'s diet', 'the model\'s land (ABS holdings 2020-21: cropping %.2f, pasture %.2f Mha)' % (abs_crop, abs_past), '2020-21', 'the model\'s 2025 data layer; 150-year wheat, oats and barley yield record',
                'the model\'s diet', 'as the model: losses charged separately'])
    out.append([m, 'harmonised', 'no equalised input (the readings are the model\'s own runs)', '', '', '', '', '', '', '', '', ''])
    for m, w in (('The model, thesis method corrected', 'avoidable retail and consumer waste 12% of food (US loss factors: Buzby and Wells, Muth et al.), charged separately; inedible parts, cooking and processing losses fixed'),
                 ('The model, improved', 'as corrected, with Australian loss factors (FIAL 2021 retail, Burnside bin audit by food group; analysis/loss_factors_2025), charged separately')):
        out.append([m, 'as run', 'the model\'s 2025 population (an input to the model rows only)', round(POP_MODEL / 1e6, 2), '8.0 MJ a day as eaten (the default diet)', 'analysis/nutrition_lp_2025/README.md',
                    'the diet\'s protein, met with the diet', 'ABS agricultural holdings: cropping %.2f and pasture %.2f Mha (equal to FAOSTAT\'s %.2f to 0.01 Mha)' % (abs_crop, abs_past, LAND),
                    '2020-21 holdings; 2023 land-use raster', 'the model\'s 2025 data layer (ABS series; meat window 2020-21 to 2024-25)', 'the model\'s diet (intake)', w])
        out.append([m, 'harmonised', 'as run (the reference)', round(POP_MODEL / 1e6, 2), 'as run', '', 'as run', 'as run', 'as run', 'the 2025 data taken as the same vintage as FAOSTAT 2021-23', 'as run', w])
    return out

# ================================================================ 2. fidelity.csv
F_HEAD = ['method', 'component', 'unit', "authors' figure", "authors' source", 'rebuild as run', 'basis of the rebuild as run', 'gap as run (%)',
          "rebuild on the authors' printed inputs", "basis of the printed-input rebuild", 'gap on printed inputs (%)', 'gap within published rounding',
          'verdict', 'verdict basis', 'cause or note']
def decimals(s): return len(s.split('.')[1]) if '.' in s else 0
def verdict(pub_s, val):
    if val is None: return None
    pub = float(pub_s); gap = 100 * (val - pub) / pub
    within_round = abs(val - pub) <= 0.5 * 10 ** -decimals(pub_s)
    if within_round or abs(gap) <= 2: return 'reproduced', within_round
    return ('partly' if abs(gap) <= 10 else 'not reproduced'), within_round
GA = dicts(D + 'gap_attribution.csv')
def ga(method, case, cid, has=''):
    hit = [x for x in GA if x['method'] == method and x['case'] == case and x['cause_id'] == cid and has in x['cause']]
    assert len(hit) == 1, (method, case, cid, has, len(hit)); return hit[0]
PUB = {(r['table'], r['row'], r['column']): r['value'] for r in dicts(D + 'published_values.csv')}
def fid_row(method, comp, unit, pub_s, src, run, run_basis, printed=None, printed_basis='', note=''):
    pub = float(pub_s)
    g_run = None if run is None else 100 * (run - pub) / pub
    g_pr = None if printed is None else 100 * (printed - pub) / pub
    basis_val, vb = (printed, "printed inputs") if printed is not None else (run, 'as run')
    v = verdict(pub_s, basis_val)
    return [method, comp, unit, pub_s, src, rnd(run, 4), run_basis, rnd(g_run, 1), rnd(printed, 4), printed_basis, rnd(g_pr, 1),
            '' if v is None else ('yes' if v[1] else 'no'), 'not checked' if v is None else v[0], vb if v is not None else '', note]
def fidelity():
    out = [F_HEAD]
    m = 'Energy and protein balance (Gifford; Henry and Godden)'
    for case, comp, pub_s in (('energy, 1990-91, million people', 'energy, 1990-91', '109'), ('protein, 1990-91, million people', 'protein, 1990-91', '96'),
                              ('energy, 1990-91 total incl. wool and cotton, million people', 'energy, total row incl. wool and cotton', '206'),
                              ('protein, 1990-91 total incl. wool and cotton, million people', 'protein, total row incl. wool and cotton', '188')):
        x = ga('Henry and Godden', case, 'c')
        out.append(fid_row(m, comp, 'million people', pub_s, 'Henry and Godden 1995, Table 5', None, '', float(x['current']),
                           'their printed totals (Table 2) x 70/45.7 x their printed factors (0.1760, 0.2041)',
                           note='arithmetic on their printed totals; the production totals are not rebuilt (item energy and protein factors are not published); residual %s' % x['note']))
    m = 'Ecological footprint, food row (Simpson)'
    sf = {(r[0], r[1]): float(r[2]) for r in rows(D + 'simpson_food.csv')[1:]}
    pl3, fe3, ga3, pa3 = S['pl3t'], S['fe3'], S['ga3'], S['pa3']
    b2 = lambda k: sb(k)
    SRC = 'Simpson, Petroeschevsky and Lowe 2000, food row 1991-92 (published_values.csv)'
    for comp, pub_s, run, p3, other in (
            ('pasture (food row)', PUB[('simpson_fidelity', 'Pasture (beef, sheep, milk)', 'Simpson (ha a person)')], sf[('1991-92', 'pasture total')], pa3,
             'build 2 %.3f (%+.1f%%); build 1 shares world pasture by protein, build 2 by production x FCR' % (b2('pasture (beef, sheep, milk), second build'), 100 * (b2('pasture (beef, sheep, milk), second build') / 1.758 - 1))),
            ('crop land for animal products (feed)', PUB[('simpson_fidelity', 'Crop land for animal products (feed)', 'Simpson (ha a person)')],
             sum(sf[('1991-92', 'crop: feed for ' + k)] for k in ('poultry', 'pork', 'eggs')), fe3,
             'build 2 %.3f; build 3 at the Table A2.4 food energies gives 0.086 (-9%%), so 0.095 lies inside the range the thesis rates give' % b2('crop land for animal products (feed), second build')),
            ('crop land for plant foods', PUB[('simpson_fidelity', 'Crop land for plant foods', 'Simpson (ha a person)')],
             sum(v for (p, k), v in sf.items() if p == '1991-92' and k.startswith('crop: ') and not k.startswith('crop: feed')), pl3,
             'build 2 %.3f; no reading tested (total grain use, total cropland ratios, the Canadian figure scaled) reaches 0.312' % b2('crop land for plant foods, second build')),
            ('crop plus pasture', PUB[('simpson_fidelity', 'Crop plus pasture', 'Simpson (ha a person)')], sf[('1991-92', 'crop plus pasture')], pl3 + fe3 + pa3,
             'build 2 2.621; the shortfall is the plant-food crop')):
        out.append(fid_row(m, comp + ', 1991-92', 'ha a person', pub_s, SRC, run, 'build 1: FAOSTAT 1990-92 world yields, ABS 4306.0 1991-92 consumption', p3,
                           "build 3: Wackernagel 1994 thesis rates as printed, ABS 4306.0 1991-92 consumption", note=other))
    out.append(fid_row(m, 'garden, 1991-92', 'ha a person', '0.032', 'Simpson et al. 2000, food row (README)', None, '', ga3, 'build 3: fruit and vegetables at the thesis garden rate of 15 t/ha',
                       note='builds 1 and 2 count fruit and vegetables in crop land'))
    out.append(fid_row(m, 'wool pasture (clothing row), 1991-92', 'ha a person', '0.854', 'Simpson et al. 2000, Table 1 row 42', None, '',
                       sf[('1991-92 tests (thesis rates)', "wool: the thesis's own consumption rule (world 0.373 kg a person x OECD factor 5 = 1.8 kg) at 14.2 kg/ha (ha)")],
                       "the thesis's own wool rule at 14.2 kg/ha net", note='a per-person share of Australian production gives 2.529 ha (net rate); no source used holds an Australian wool consumption figure'))
    m = 'HALF index (Alexander)'
    hi = {(r['period'], r['country']): r for r in dicts(D + 'half_index.csv')}
    for case, row_name in (('World 2011', 'World'), ('Australia 2011', 'Australia'), ('United States 2011', 'United States'), ('Argentina 2011', 'Argentina'), ('India 2011', 'India')):
        pub_s = PUB[('half_fidelity', row_name, 'Paper (HALF, % of world land)')]
        cur = float(ga('HALF', case, 'a')['current'])
        allp = float(ga('HALF', case, 'a+b1-b5')['figure'])
        b1 = float(ga('HALF', case, 'b1')['figure'])
        note = 'world pasture as printed (b1) alone gives %.2f (%+.1f%%)' % (b1, 100 * (b1 / float(pub_s) - 1))
        if row_name == 'Australia':
            b5 = float(ga('HALF', case, 'b5')['figure'])
            note = ('the 6 to 8%%: on current FAOSTAT revisions the rebuild is %+.1f%%; with the world pasture the supplement prints (3,364 Mha against 3,182 in the current revision) it is %.2f (%+.1f%%), '
                    'because every tonne of ruminant product then carries %.1f%% more pasture and animal products are %.0f%% of Australia\'s 2011 HALF; the feed pool and feed cropland as printed (b5) '
                    'add the rest (%.2f alone; all printed inputs together %.2f, %+.1f%%). The world, United States, Argentina and India move toward their published figures with the same inputs, '
                    'Australia away from its own; what offsets them in the authors\' Australian figure is not identified (untested candidates: the 2015 food balance\'s Australian diet; the bovine '
                    'share of pasture, 59%% in the paper against 67%% here)') % (100 * (cur / float(pub_s) - 1), b1, 100 * (b1 / float(pub_s) - 1), 100 * (3364 / 3182.08 - 1),
                                                                                   100 * float(hi[('2011', 'Australia')]['animal products']) / float(hi[('2011', 'Australia')]['ha a person']), b5, allp, 100 * (allp / float(pub_s) - 1))
        out.append(fid_row(m, row_name + ', 2011', '% of world land', pub_s, 'Alexander et al. 2016 (published_values.csv)', cur, 'FAOSTAT 2011, current revision', allp,
                           'the paper\'s and supplement\'s printed inputs together: adjustment 1.129, pasture 3,364 Mha, livestock output, soybean balance, world land 13,009 Mha, feed pool and feed cropland (a+b1-b5)', note=note))
    pub_s = PUB[('half_fidelity', 'New Zealand', 'Paper (HALF, % of world land)')]
    out.append(fid_row(m, 'New Zealand, 2011', '% of world land', pub_s, 'Alexander et al. 2016 (published_values.csv)', float(hi[('2011', 'New Zealand')]['HALF % of world land']), 'FAOSTAT 2011, current revision',
                       note='not run on printed inputs; cause not known (milk treatment, the new food balance\'s dairy accounting or the omitted commodities are candidates)'))
    m = 'People per hectare (Cassidy)'
    for case, comp, pub_s, cid in (('World, people per ha produced', 'world, people a hectare produced', '10.1', 'a'), ('World, people per ha delivered', 'world, people a hectare delivered', '6.0', 'a+b2'),
                                   ('United States, people per ha produced', 'United States, people a hectare produced', '16.1', 'a'), ('India, people per ha produced', 'India, people a hectare produced', '6.5', 'a'),
                                   ('China, people per ha produced', 'China, people a hectare produced', '13.5', 'a'), ('Brazil, people per ha produced', 'Brazil, people a hectare produced', '10.6', 'a')):
        x = ga('Cassidy', case, cid, '1997 to 2003' if cid == 'a' else '')
        out.append(fid_row(m, comp, 'people a hectare', pub_s, 'Cassidy et al. 2013 (published_values.csv)', float(x['current']), 'FAOSTAT 2011', float(x['figure']),
                           'each crop at its 1997 to 2003 yield (the paper\'s data years), 2011 area and uses' + (', with the paper\'s average feed efficiency (4% over 36%)' if cid == 'a+b2' else ''),
                           note='closest rebuild on the paper\'s inputs; crop set (21 against 41 crops), old against new food balance and typed crop energies untested'))
    for ctry, lab, col, pub_row, pub_col in (('United States of America', 'United States, feed share of calories', 'feed %', 'United States, paper', 'Feed %'),
                                             ('United States of America', 'United States, delivered share', 'delivered % of produced', 'United States, paper', 'Delivered %'),
                                             ('World', 'world, delivered share', 'delivered % of produced', 'World, paper', 'Delivered %')):
        out.append(fid_row(m, lab, '% of calories', PUB[('cassidy_fidelity', pub_row, pub_col)], 'Cassidy et al. 2013 (published_values.csv)', float(CAS[('2011', ctry)][col]), 'FAOSTAT 2011 (whole per cent)',
                           note='the US feed share is lower and other uses higher, as expected from the rise of maize ethanol between 2000 and 2011' if 'feed' in lab else ''))
    m = 'Commodity balance (Foran and Poldy)'
    for case, comp, pub_s in (('grain 1997-98, Mt', 'grain production 1997-98', '31.578'), ('meat 1997-98, Mt', 'meat production 1997-98', '3.514')):
        x = ga('Foran and Poldy', case, 'b', 'calendar 1997 alone')
        out.append(fid_row(m, comp, 'Mt', pub_s, 'Foran and Poldy 2002, Table 2.5 (their ABS figures)', float(x['current']), 'FAOSTAT, mean of calendar 1997 and 1998',
                           note='their balance on their own numbers (grain 11.6, meat 1.21, fish 0.51) reproduces their conclusion, positive except fish'))
    out.append(['Failure probability (Fearnside)', 'Trans-Amazon study area (0.24 persons a hectare)', 'persons a hectare', '0.24', 'Fearnside 1985 and 1990', '', 'none: applied to Australia only (Murray\'s rule)', '',
                '', '', '', '', 'not checked', '', 'no fidelity check is possible on Australian data; the readings are the model\'s own failure curve'])
    th = {(r['preset'], r['regionId']): float(r['capacity']) for r in dicts('baseline/thesis_totals_capacity.csv')}
    rt = {r['preset']: float(r['capacity']) for r in dicts('results/2011-thesis.csv') if r['zone'] == '1'}
    r11 = {r['preset']: float(r['capacity']) for r in dicts('results/2011.csv') if r['zone'] == '1'}
    for preset, lab in (('short', 'Australia, short term (thesis results, Table 16)'), ('long', 'Australia, long term (thesis results, Table 16)')):
        pub_s = '%.0f' % th[(preset, '1')]
        out.append(fid_row('The model (thesis method as built)', lab, 'people', pub_s, 'thesis results workbook (baseline/thesis_totals_capacity.csv); the thesis p. 280 prints 9,431,487 and "over 40 million"',
                           rt[preset], 'release 2011-thesis (the June 2012 model and defaults)',
                           note='release 2011 (the October 2012 model) gives %.0f (%+.3f%%)' % (r11[preset], 100 * (r11[preset] / th[(preset, '1')] - 1))))
    return out

# ================================================================ 3. intake_variant.csv
# FAO's waste factor: Gustavsson et al. (FAO 2011), Annex 4, North America and Oceania, the two steps after the food balance's food supply: distribution and retail, and consumption.
# The food balance removes losses only up to retail, so these two steps are what its food supply still holds (distribution may overlap a little with FAO's own losses: stated).
FR2 = {r['group']: r for r in dicts('analysis/loss_factors_2025/fao_region2_loss.csv')}
def fao_share(g): return (1 - float(FR2[g]['distribution_retail_pct']) / 100) * (1 - float(FR2[g]['consumption_pct']) / 100)
FAO_GROUP = {'cereal': 'Cereals', 'roots': 'Roots and tubers', 'pulses': 'Oilseeds and pulses', 'nuts_seeds': 'Oilseeds and pulses', 'oils': 'Oilseeds and pulses',
             'veg': 'Fruits and vegetables', 'fruit': 'Fruits and vegetables', 'red_meat': 'Meat', 'white_meat': 'Meat', 'eggs': 'Meat', 'dairy': 'Milk', 'fish': 'Fish and seafood'}
# The model's own retail (I) and consumer (G) loss factors, corrected tier (US: Buzby 2010, Muth 2011), category means from analysis/loss_factors_2025/compare.csv.
MC = {r['category']: r for r in dicts('analysis/loss_factors_2025/compare.csv')}
def mshare(*cats):
    s = [(1 - float(MC[c]['model_retail_I']) / 100) * (1 - float(MC[c]['model_consumer_G']) / 100) for c in cats]
    return sum(s) / len(s)
MODEL_CAT = {'cereal': ('Cereal whole', 'Cereal ref'), 'roots': ('Vege starch',), 'pulses': ('Legume',), 'nuts_seeds': ('Nut & seed',), 'veg': ('Vege green', 'Vege orange', 'Vege other'),
             'fruit': ('Fruit',), 'red_meat': ('Meat red',), 'white_meat': ('Meat white',), 'eggs': ('Meat white',), 'fish': ('Meat white',), 'dairy': ('Dairy High', 'Dairy Med', 'Dairy Low')}
def share(cat, basis):
    if basis == 'fao': return fao_share(FAO_GROUP[cat]) if cat in FAO_GROUP else 1.0
    return mshare(*MODEL_CAT[cat]) if cat in MODEL_CAT else 1.0
NO_FACTOR = {'fao': 'sugar and sweeteners, alcoholic beverages, stimulants, spices, miscellaneous (no FAO group)',
             'model': 'vegetable oils, sugar and sweeteners, alcoholic beverages, stimulants, spices, miscellaneous (no model category in compare.csv)'}
# food balance items -> category (the leaves the method scripts use, and the group totals for energy and protein)
CAT = {}
for i in ('Wheat and products', 'Barley and products', 'Maize and products', 'Oats', 'Rice and products', 'Rye and products', 'Sorghum and products', 'Millet and products', 'Cereals, other', 'Cereals - Excluding Beer'): CAT[i] = 'cereal'
for i in ('Cassava and products', 'Potatoes and products', 'Roots, Other', 'Sweet potatoes', 'Yams', 'Starchy Roots'): CAT[i] = 'roots'
for i in ('Beans', 'Peas', 'Pulses, Other and products', 'Pulses', 'Soyabeans'): CAT[i] = 'pulses'
for i in ('Treenuts', 'Groundnuts', 'Rape and Mustardseed', 'Sunflower seed', 'Sesame seed', 'Cottonseed', 'Coconuts - Incl Copra', 'Oilcrops, Other', 'Palm kernels', 'Olives (including preserved)', 'Oilcrops'): CAT[i] = 'nuts_seeds'
for i in ('Coconut Oil', 'Cottonseed Oil', 'Groundnut Oil', 'Maize Germ Oil', 'Oilcrops Oil, Other', 'Olive Oil', 'Palm Oil', 'Palmkernel Oil', 'Rape and Mustard Oil', 'Sesameseed Oil',
          'Soyabean Oil', 'Sunflowerseed Oil', 'Vegetable Oils'): CAT[i] = 'oils'
CAT.update({'Vegetables': 'veg', 'Fruits - Excluding Wine': 'fruit', 'Bovine Meat': 'red_meat', 'Mutton & Goat Meat': 'red_meat', 'Pigmeat': 'red_meat', 'Meat, Other': 'red_meat',
            'Offals': 'red_meat', 'Offals, Edible': 'red_meat', 'Fats, Animals, Raw': 'red_meat', 'Poultry Meat': 'white_meat', 'Eggs': 'eggs', 'Milk - Excluding Butter': 'dairy',
            'Butter, Ghee': 'dairy', 'Cream': 'dairy', 'Fish, Seafood': 'fish', 'Aquatic Products, Other': 'fish', 'Fish, Body Oil': 'fish', 'Fish, Liver Oil': 'fish'})
# the whole diet by group, with Meat and Animal fats split into their items so each item takes its own category
DIET = ['Cereals - Excluding Beer', 'Starchy Roots', 'Sugar Crops', 'Sugar & Sweeteners', 'Pulses', 'Treenuts', 'Oilcrops', 'Vegetable Oils', 'Vegetables', 'Fruits - Excluding Wine', 'Stimulants',
        'Spices', 'Alcoholic Beverages', 'Bovine Meat', 'Mutton & Goat Meat', 'Pigmeat', 'Poultry Meat', 'Meat, Other', 'Offals', 'Butter, Ghee', 'Cream', 'Fats, Animals, Raw', 'Fish, Body Oil',
        'Fish, Liver Oil', 'Eggs', 'Milk - Excluding Butter', 'Fish, Seafood', 'Aquatic Products, Other', 'Miscellaneous']
def diet_share(el, basis):
    tot = fbs('Grand Total', el); parts = sum(fbs(i, el) for i in DIET)
    assert abs(parts - tot) / tot < 1e-3, (el, parts, tot)
    unassigned = sum(fbs(i, el) for i in DIET if CAT.get(i) is None or share(CAT[i], basis) == 1.0) / tot
    return sum(fbs(i, el) * share(CAT.get(i, 'none'), basis) for i in DIET) / tot, unassigned
I_HEAD = ['method', 'reading', 'supply basis (harmonised, million)', 'supply basis over the corrected model', 'intake share, FAO waste factor', 'intake basis, FAO waste factor (million)',
          'intake over the corrected model, FAO waste factor', 'intake share, model loss factors', 'intake basis, model loss factors (million)', 'intake over the corrected model, model loss factors',
          'intake over the corrected model with no avoidable waste (%.1f), FAO waste factor' % M_FIX_NW, 'gap to the corrected model', 'note']
def gap_word(s, i):
    a, b = abs(math.log(s / M_FIX)), abs(math.log(i / M_FIX))
    return 'widens' if b > a + 1e-9 else ('narrows' if b < a - 1e-9 else 'unchanged')
def intake():
    out = [I_HEAD]; checks = []
    HC = {(r['method'], r['reading']): r for r in dicts(D + 'harmonised_comparison.csv')}
    def emit(method, reading, sup, s_f, s_m, note, hc_key=None):
        i_f, i_m = sup / s_f, sup / s_m
        if hc_key:
            hb = HC.get(hc_key, {}).get('(b) harmonised (million)', '')
            checks.append((method, reading, sup, hb))
        out.append([method, reading, rnd(sup, 1), rnd(sup / M_FIX, 2), rnd(s_f, 4), rnd(i_f, 1), rnd(i_f / M_FIX, 2), rnd(s_m, 4), rnd(i_m, 1), rnd(i_m / M_FIX, 2),
                    rnd(i_f / M_FIX_NW, 2), gap_word(sup, i_f) + ('' if gap_word(sup, i_f) == gap_word(sup, i_m) else ' (model loss factors: %s)' % gap_word(sup, i_m)), note])
    # energy and protein balance; Cassidy (calories)
    ke_f, ue_f = diet_share('Food supply (kcal)', 'fao'); ke_m, ue_m = diet_share('Food supply (kcal)', 'model')
    kp_f, up_f = diet_share('Protein supply quantity (t)', 'fao'); kp_m, up_m = diet_share('Protein supply quantity (t)', 'model')
    hg_e = HG_E * 1e15 / (kcal_day * 365 * 4184) / 1e6; hg_p = HG_P * 1e10 / (prot_day * 365) / 1e6
    NM = 'Energy and protein balance (Gifford; Henry and Godden)'
    emit(NM, 'energy, production as it is', hg_e, ke_f, ke_m, 'intake %.0f kcal (FAO factor) and %.0f kcal (model factors) a day against the supply of %.0f; food energy with no factor %.0f%% (FAO) and %.0f%% (model) of the supply'
         % (kcal_day * ke_f, kcal_day * ke_m, kcal_day, 100 * ue_f, 100 * ue_m), (NM, 'energy, production as it is'))
    emit(NM, 'protein, production as it is', hg_p, kp_f, kp_m, 'intake %.1f g (FAO factor) and %.1f g (model factors) a day against the supply of %.1f' % (prot_day * kp_f, prot_day * kp_m, prot_day),
         (NM, 'protein, production as it is'))
    # footprint build 1 and build 3
    NM = 'Ecological footprint, food row (Simpson)'
    CK = {'beef': 'red_meat', 'sheep': 'red_meat', 'pork': 'red_meat', 'poultry': 'white_meat', 'eggs': 'eggs', 'milk': 'dairy', 'cereals': 'cereal', 'potatoes': 'roots', 'veg': 'veg',
          'fruit': 'fruit', 'sugar': 'sugar', 'oil': 'oils', 'nuts': 'nuts_seeds', 'pulses': 'pulses'}
    def b1(basis):
        c = {k: v * share(CK[k], basis) for k, v in S['C21'].items()} if basis else S['C21']
        cr, pa, _ = S['footprint'](c, S['Y21']); return sum(cr.values()), sum(pa.values())
    (c0, p0), (cf, pf_), (cm, pm) = b1(None), b1('fao'), b1('model')
    for lab, f in (('build 1, cropland-bound', lambda c, p: fao_crop / c), ('build 1, pasture', lambda c, p: fao_past / p), ('build 1, crop and pasture together', lambda c, p: LAND / (c + p))):
        emit(NM, lab, f(c0, p0), f(c0, p0) / f(cf, pf_), f(c0, p0) / f(cm, pm), 'footprint run in memory with each food\'s use times its intake share', (NM, lab))
    THESIS_TO_FAO = {'16 wheat': 'Wheat', '17 rice': 'Rice', '19 barley': 'Barley', '20 corn': 'Maize (corn)', '21 rye': 'Rye', '22 oats': 'Oats', '23 millet + other cereals': 'Millet',
                     '24 sorghum': 'Sorghum', '15 cereals': 'Cereals, primary', '26 potatoes': 'Potatoes', '31 pulses 32-36,39 (?)': 'Pulses, Total', '67 sugar cane + sugar trade': 'Sugar cane',
                     '38 ground nuts': 'Groundnuts, excluding shelled', 'treenuts, total': 'Treenuts, Total', '49 vegetables and melons': 'Vegetables Primary', 'palm oil': None}
    ty_1990 = S['ty']
    S['ty'] = lambda it: S['oil_yield'](S['Y21']) if THESIS_TO_FAO[it] is None else S['yield_kg_per_ha'](THESIS_TO_FAO[it], S['Y21'])   # as harmonised_comparison.py
    def b3(basis):
        c = {k: v * share(CK[k], basis) for k, v in S['C21'].items()} if basis else S['C21']
        g = {k: v * (share('cereal', basis) if basis else 1) for k, v in S['G21'].items()}
        n = {k: v * (share('nuts_seeds', basis) if basis else 1) for k, v in (('38 ground nuts', S['fbs']('Groundnuts')), ('treenuts, total', S['fbs']('Treenuts')))}
        pl, fe, gd, pa = S['build3'](c, g, n); return sum(pl.values()) + fe + gd, pa
    (c0, p0), (cf, pf_), (cm, pm) = b3(None), b3('fao'), b3('model')
    S['ty'] = ty_1990
    for lab, f in (('build 3 (thesis rates), cropland-bound', lambda c, p: fao_crop / c), ('build 3 (thesis rates), pasture', lambda c, p: fao_past / p),
                   ('build 3 (thesis rates), crop and pasture together', lambda c, p: LAND / (c + p))):
        emit(NM, lab, f(c0, p0), f(c0, p0) / f(cf, pf_), f(c0, p0) / f(cm, pm), 'build 3 on 2021-23 world yields (the harmonised reading); red meat on pasture at the sheep-meat rate', (NM, lab))
    out.append([NM, 'build 2 (V04)', '', '', '', '', '', '', '', '', '', '', 'not re-run: the second build is used as filed (second_build_values.csv), so no intake reading'])
    # HALF
    NM = 'HALF index (Alexander)'
    w = H['world'](YR); Fh = H['F']; yv = H['yv']
    pop = yv(Fh.get(('Australia', 'Population', 'Total Population - Both sexes'), {}), YR)
    def hal(basis):
        tot = 0.0
        for item, lp in w['lpt'].items():
            food = yv(Fh.get(('Australia', item, 'Food'), {}), YR)
            if food == 0: continue
            tot += food / pop * lp / 1000 * (share(CAT.get(item, 'none'), basis) if basis else 1)
        return tot
    h0, hf, hm = hal(None), hal('fao'), hal('model')
    emit(NM, "agricultural land over the diet's land a person", LAND / h0, hf / h0, hm / h0, 'diet %.3f ha a person on supply, %.3f (FAO factor) and %.3f (model factors) on intake' % (h0, hf, hm),
         (NM, "agricultural land over the diet's land a person"))
    # Cassidy
    NM = 'People per hectare (Cassidy)'
    c_ppl = float(cas_au['people fed by delivered calories (million)'])
    c_ppl2 = sb('Australia 2021-23, people per ha delivered') * sb('Australia 2021-23, cropland')
    for lab, a in (('this build, delivered calories', c_ppl), ('second build (V05), delivered calories', c_ppl2)):
        sup = a * 2700 / kcal_day
        emit(NM, lab, sup, ke_f, ke_m, 'the food balance energy at its intake share, as for the energy balance', (NM, lab))
    # Foran and Poldy
    NM = 'Commodity balance (Foran and Poldy)'
    Q = collections.defaultdict(dict)
    for r in dicts(D + 'fao_au_production_1997_2023.csv'): Q[r['Item']][r['Year']] = float(r['Value']) / 1e6
    prod = {'meat': sum(Q['Meat, Total'][y] for y in YR) / 3, 'grain': sum(Q['Cereals, primary'][y] for y in YR) / 3, 'fish': fbs('Fish, Seafood', 'Production') / 3 / 1000}
    GR = ['Wheat and products', 'Barley and products', 'Maize and products', 'Oats', 'Rice and products', 'Rye and products', 'Sorghum and products', 'Millet and products', 'Cereals, other']
    MEAT = ['Bovine Meat', 'Mutton & Goat Meat', 'Pigmeat', 'Poultry Meat', 'Meat, Other']
    assert abs(sum(fbs(i, 'Food') for i in MEAT) - fbs('Meat', 'Food')) / fbs('Meat', 'Food') < 1e-3
    def use(basis):
        sh = (lambda c: share(c, basis)) if basis else (lambda c: 1.0)
        return {'meat': sum(fbs(i, 'Food') * sh(CAT[i]) for i in MEAT) / 3 / fp_pop, 'grain': sum(fbs(i, 'Food') * sh('cereal') for i in GR) / 3 / fp_pop,
                'fish': fbs('Fish, Seafood', 'Food') * sh('fish') / 3 / fp_pop}                  # 1000 t / million = kg a person
    emb = 7.6 / 25.1 * 1000                                                                       # their embodied feed grain, kg a person (base case), kept as in the harmonised reading
    u0, uf, um = use(None), use('fao'), use('model')
    for lab, k in (('meat', 'meat'), ('fish', 'fish'), ('grain with embodied feed grain', 'grain')):
        e = emb if k == 'grain' else 0.0
        cap = lambda u: prod[k] * 1000 / (u[k] + e)
        emit(NM, lab, cap(u0), cap(u0) / cap(uf), cap(u0) / cap(um), 'unrounded (the harmonised csv holds whole millions)' + ('; their embodied feed grain (%.0f kg a person) kept, so only direct grain falls' % emb if k == 'grain' else ''),
             (NM, lab))
    out.append(['Failure probability (Fearnside)', 'all readings', '', '', '', '', '', '', '', '', '', '', 'the model\'s own runs: the model charges its losses itself, so there is no supply basis to convert'])
    for lab, v in (('The model, thesis method corrected', M_FIX), ('The model, improved', M_IMP)):
        out.append([lab, 'short term, average year', rnd(v, 1), rnd(v / M_FIX, 2), '', rnd(v, 1), rnd(v / M_FIX, 2), '', rnd(v, 1), rnd(v / M_FIX, 2), '', 'reference',
                    'unchanged: the model\'s diet is intake (8.0 MJ as eaten) and its waste is charged separately; with no avoidable waste it reads %.1f (corrected) and %.1f (improved)' % (M_FIX_NW, M_IMP_NW)])
    return out, checks

# ================================================================ 4. gap_attribution_readable.csv
G_HEAD = ['method', 'case', 'cause_id', 'cause', 'figure', 'current', 'published', 'residual (published - current)', 'residual as % of the published figure', 'residual within published rounding',
          'ill-conditioned (residual under 1% of the figure)', 'change from this test (figure - current)', 'change in people (million)', 'printed share', 'note']
HALF_AU_PEOPLE = 'HALF Australia 2011 read as a capacity: Australia\'s 2011 cropland and pasture (%.2f Mha) over the diet\'s hectares (%.3f ha a person at %.2f%% of world land); people scale as 1 over the index'
def readable():
    out = [G_HEAD]
    w11 = H['world'](('2011',))
    ha11, _, _ = H['half'](w11, 'Australia', ('2011',))
    for x in GA:
        if not x['current'] or not x['published']:
            out.append([x['method'], x['case'], x['cause_id'], x['cause'], x['figure'], x['current'], x['published'], x['residual (published - current)'], '', '', '', '', '', '', x['note']]); continue
        cur, pub = float(x['current']), float(x['published'])
        res = pub - cur
        within = abs(res) <= 0.5 * 10 ** -decimals(x['published'])
        ill = abs(res) / pub < 0.01
        fig = float(x['figure']) if x['figure'] else None
        ch = None if fig is None else fig - cur
        people = None; note = x['note']
        if x['method'] == 'HALF' and x['case'] == 'Australia 2011' and fig is not None:
            base = LAND11 / ha11
            people = base * (cur / fig - 1)
            note = HALF_AU_PEOPLE % (LAND11, ha11, cur) + '; at this test %.1f million, at the published figure %.1f' % (base, base * cur / pub)
        elif x['case'].endswith('million people') and fig is not None:
            people = ch
        if within: printed = 'within rounding'
        elif ill:
            printed = '' if ch is None else ('%+.2f' % ch) + ('' if people is None else ' (%+.1f million people)' % people)
        else:
            printed = '' if not x['explained % of residual'] else '%+.0f%%' % float(x['explained % of residual'])
        out.append([x['method'], x['case'], x['cause_id'], x['cause'], x['figure'], x['current'], x['published'], x['residual (published - current)'], rnd(100 * res / pub, 2),
                    'yes' if within else 'no', 'yes' if ill else 'no', rnd(ch, 4), rnd(people, 2), printed, note])
    return out

# ================================================================ write, or check
def build():
    i, checks = intake()
    return {'bases.csv': bases(), 'fidelity.csv': fidelity(), 'intake_variant.csv': i, 'gap_attribution_readable.csv': readable()}, checks
def norm(t): return [[str(c) for c in r] for r in t]
def main():
    tables, checks = build()
    if '--check' in sys.argv:
        k = sys.argv.index('--check'); where = sys.argv[k + 1] if len(sys.argv) > k + 1 else D
        bad = 0
        for name, t in tables.items():
            disk = rows(os.path.join(where, name))
            want = norm(t)
            for n, (a, b) in enumerate(zip(disk, want)):
                for j, (u, v) in enumerate(zip(a, b)):
                    if u != v:
                        bad += 1; print('MISMATCH %s row %d column "%s": file %r, recomputed %r' % (name, n, want[0][j] if j < len(want[0]) else j, u, v))
            if len(disk) != len(want): bad += 1; print('MISMATCH %s: %d rows in the file, %d recomputed' % (name, len(disk), len(want)))
        print('check: %d mismatches' % bad)
        sys.exit(1 if bad else 0)
    for name, t in tables.items():
        csv.writer(open(D + name, 'w', newline='')).writerows(t)
        print('wrote %s (%d rows)' % (D + name, len(t) - 1))
    for method, reading, sup, hb in checks:
        ok = hb != '' and abs(sup - float(hb)) <= (0.51 if method.startswith('Commodity') else 0.11)
        print('%s supply basis %s / %s: %.2f against harmonised_comparison.csv (b) %s' % ('ok  ' if ok else 'DIFF', method, reading, sup, hb))
if __name__ == '__main__':
    main()
