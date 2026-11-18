#!/usr/bin/env python3
"""The bridge from HALF at Australian productivity (76.0 million) to the corrected model (41.5 million), feature by feature, averaged over every ordering
(brief B139, decision 144; R05b issue 7; Mod M4, Mod Q6, EE M3).
Usage (repository root):
  python3 -I analysis/method_tests_2025/bridge_half_to_model.py                      writes bridge_half_to_model.csv and bridge_groups.csv
  python3 -I analysis/method_tests_2025/bridge_half_to_model.py --wrong-value-demo   plants one wrong value and shows the script's own check failing (nothing is written)
Needs node (the model's diet by food group is read from the evaluator, unchanged, by b139_model_runs.mjs). Reads, read only: harmonised_comparison.py (run in memory up to the
line that writes its csv, as bases_fidelity.py does, to take HALF's own accounting and Australia's output in world-average hectares), half_index.py (through it), fbs_au_world_2021_23.csv,
harmonised_comparison.csv (the HALF reading), results/2025-fixed.csv (the model's capacity), analysis/pasture_2025/pairing_relaxed.csv (B114, for the cross-check).

ONE MACHINE FOR BOTH ENDS. People = land / land a person, with land a person built food group by food group in the model's own eleven groups (cereals, dairy, fruit, legumes, pasture-fed
red meat, crop-fed red meat, white meat and eggs, nuts and seeds, vegetables, oils, sweeteners and drinks) and Australian square metres. Two complete worlds are written in this form:
  the model world   energy kJ a day, cropland and pasture m2 a person a year from the evaluator (the diet of Settings!C33:D46, as B114 reads it), at the model's avoidable waste (0.12) and at 0;
  the HALF world    energy of the food balance items HALF counts (FAO supply of those items, 13.60 MJ a day), and the land HALF charges them, in world-average hectares, split into cropland and
                    pasture (ruminants take all pasture, and the feed cropland that remains, by feed need: half_index.py), converted to Australian m2 with Australia's own productivity,
                    kappa = Australia's 2021-23 output in world-average hectares over its hectares (cropland 27.7 over 31.65 Mha, pasture 72.4 over 331.87 Mha: the figures of column (e)).
The machine reproduces both ends exactly (checked): all features model-like gives the evaluator's 41.5035 million; all features HALF-like gives HALF's local-productivity reading, 75.97 million
(100.15 Mha of world-average hectares over the diet's 1.318 world-average hectares a person; column (e) prints 76.0).
SEVEN SWITCHES, each HALF-like or model-like:
  P   the land pool.  HALF: one pool in world-average hectares, so an Australian cropland m2 is worth kappa_c / kappa_p = 4.01 pasture m2 and there is no cap (the ratio of Australian output to the
      diet, each in world-average hectares: the land pooled at world-average hectares of S3.12, a test the records list as not run).  Model: the model's rule (Settings!C57:D62): cropland share capped at the existing
      cropland, idle cropland ceded to pasture m2 for m2 at pasture's own output.
  R   the per-person requirement.  HALF: 13.60 MJ a day (the supply of the items HALF counts).  Model: 7.376 MJ a day, the diet the model's land is computed from (the records also say 8.0 MJ as
      eaten: the 0.62 MJ difference is drinks and other items outside the land accounting; the ratio 13.60 over 7.376 is 1.843 against 14.75 over 8.0 = 1.844, the Mod M2 factor).
  W   waste.  HALF: none charged on top of the supply, which holds retail and household waste.  Model: its own retail and consumer loss factors (avoidable waste 12%), group by group
      (the ratio of the model's cropland or pasture need at waste 0 to its need at 12%, from the evaluator).
  C   the diet composition.  HALF: the Australian food balance mix of the items HALF counts.  Model: the guideline diet at 12% meat and eggs.
  Yc  the yield layer for cropland (land a kJ, by group): HALF's world-average land a tonne at Australia's productivity; the model's ABS-based yields.
  Yp  the yield layer for pasture-fed output (land a kJ, by group): HALF shares all world pasture among ruminants by feed need; the model divides grazing land by dry sheep equivalents and sets
      pasture-fed output from the national meat, milk and wool series.
  N   non-food land (wool, crop fibre, biofuel; timber and infrastructure are on other land and never bind).  HALF: none (food only).  Model: its needs.
A state is a choice of HALF-like or model-like for each switch; its capacity is computed by the machine. Forward = the switch's effect when every other switch is HALF-like; reverse = its
effect when every other is model-like; all-orderings average = its mean effect over all 7! = 5,040 orders (exact, no sampling; the sum of the averages is the total change, checked).
Effects are in million people, from HALF toward the model, so a negative number is a switch that lowers capacity on the way to the model. Share = average over total change (shares are
not bounded by 100%: switches that raise capacity are offset by those that lower it). A second column gives the same on the log scale (ratio effects).
VARIANTS OF THE POOLED-LAND SWITCH (games G3 and G4): the pool is the same formula with another exchange rate k between a cropland m2 and a pasture m2, so the realisation of the pooling is
the exchange rate. G1 uses HALF's own, 4.01. G3 uses B114's variant 1, the crop-equivalent energy rate (cropland foods give 91.3 times the food energy a m2 of pasture-fed foods gives; energy
held, protein not held: 81.70 million for the model alone, reproduced here). G4 is G3 with the protein of the diet held: a linear program over the eleven groups at the model's own pool rule, pasture-fed
groups between 0 and their present amount, every other group between 1 and 3 times its present amount (B114's guard), energy and protein at least the diet's (93.1 g a day), maximise people; its
capacity is turned into the exchange rate that gives it. G3 and G4 end points are not HALF's 76.0 (they are the HALF world with the pooling that exchange rate gives); the difference is printed, not attributed.
WHAT THE RECORDS CANNOT SEPARATE (also in the csv notes):
  * R from W. FAO's food supply holds retail and household waste and no record gives the split; the two switches are separated here only through the model's own loss factors, and their
    opposite signs (the model's lower requirement raises capacity, charging waste lowers it) mean the pair is the robust number: game G2 treats them as one switch.
  * Within Yp. HALF's land a tonne for ruminants is a joint allocation (all world pasture, shared by feed need); the model's is national output over dry-sheep-equivalent land. The difference mixes
    the allocation rule, the data (FAOSTAT world totals against ABS and AWI national series) and the conversion from world-average to Australian productivity, none separable item by item.
  * Within C. The Australian food balance diet and the model's guideline diet differ in the pattern (meat, oils and sugar shares) and in what is counted as food (HALF counts 46 items, the model eleven
    groups; drinks and sweeteners meet in one group); no record splits the two.
  * The protein floor. HALF carries no protein constraint and the model's diet is a fixed guideline pattern, not an optimised one, so the floor never binds in G1; it binds only when food is
    substituted between land types (G3 against G4).
  * Land base and population: FAOSTAT's 363.52 Mha and the ABS holdings agree to 0.01 Mha and no population enters either capacity, so neither is a switch. Exports: HALF's numerator is Australia's
    whole output in world-average hectares, so exports enter through kappa (in P and Yp) and cannot be separated from pasture productivity.
Deterministic: no randomness, no clock; every number from the files named above and the evaluator."""
import collections, contextlib, csv, io, itertools, json, math, subprocess, sys
import numpy as np
from scipy.optimize import linprog
D = 'analysis/method_tests_2025/'
DEMO = '--wrong-value-demo' in sys.argv
YR = ('2021', '2022', '2023')
def dicts(p): return list(csv.DictReader(open(p, newline='')))
# ---------------------------------------------------------------- HALF's accounting, from the scripts that wrote Table 5 (run in memory, nothing rewritten)
src = open(D + 'harmonised_comparison.py').read(); marker = "csv.writer(open(D + 'harmonised_comparison.csv'"
assert src.count(marker) == 1
ns = {'__name__': 'b139_harmonised_comparison'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(src[:src.index(marker)], D + 'harmonised_comparison.py', 'exec'), ns)
H, O_CROP, O_PAST, HALF_AU = ns['H'], ns['eq_croph'], ns['eq_pasth'], ns['half_au']                  # world-average Mha of Australian output; ha a person (rounded, as filed)
w = H['world'](YR); F = H['F']; yv = H['yv']
pop = yv(F.get(('Australia', 'Population', 'Total Population - Both sexes'), {}), YR)
FB = collections.defaultdict(dict)
for r in dicts(D + 'fbs_au_world_2021_23.csv'):
    try: FB[(r['Area'], r['Item'], r['Element'])][r['Year']] = float(r['Value'])
    except ValueError: pass
def fbs(i, e): return sum(FB[('Australia', i, e)].get(y, 0.0) for y in YR)
GT = fbs('Grand Total', 'Food supply (kcal)'); KCAL_DAY = GT * 1e6 / (fbs('Population', 'Total Population - Both sexes') * 1000) / 365
GROUPS = ['cereals', 'dairy', 'fruit', 'legumes', 'red_meat_pasture_fed', 'red_meat_crop_fed', 'white_meat_eggs', 'nuts_seeds', 'vegetables', 'oils', 'sweeteners']
GRP = {}
for i in ('Wheat and products', 'Rice and products', 'Maize and products', 'Rye and products', 'Oats', 'Sorghum and products', 'Cereals, other', 'Barley and products', 'Millet and products'): GRP[i] = 'cereals'
for i in ('Milk - Excluding Butter', 'Butter, Ghee', 'Cream'): GRP[i] = 'dairy'
GRP['Fruits - Excluding Wine'] = 'fruit'
for i in ('Beans', 'Peas', 'Pulses, Other and products'): GRP[i] = 'legumes'
for i in ('Bovine Meat', 'Mutton & Goat Meat', 'Meat, Other'): GRP[i] = 'red_meat_pasture_fed'
GRP['Pigmeat'] = 'red_meat_crop_fed'
for i in ('Poultry Meat', 'Eggs'): GRP[i] = 'white_meat_eggs'
for i in ('Treenuts', 'Groundnuts', 'Soyabeans', 'Rape and Mustardseed', 'Coconuts - Incl Copra', 'Olives (including preserved)', 'Sunflower seed', 'Sesame seed', 'Cottonseed', 'Palm kernels', 'Oilcrops, Other'): GRP[i] = 'nuts_seeds'
for i in ('Vegetables', 'Cassava and products', 'Potatoes and products', 'Sweet potatoes', 'Yams', 'Roots, Other'): GRP[i] = 'vegetables'
for i in ('Soyabean Oil', 'Rape and Mustard Oil', 'Sunflowerseed Oil', 'Cottonseed Oil', 'Groundnut Oil', 'Coconut Oil', 'Palm Oil', 'Olive Oil', 'Sesameseed Oil', 'Oilcrops Oil, Other', 'Maize Germ Oil', 'Palmkernel Oil'): GRP[i] = 'oils'
for i in ('Sugar (Raw Equivalent)', 'Sweeteners, Other', 'Beer', 'Sugar beet', 'Sugar cane', 'Sugar non-centrifugal'): GRP[i] = 'sweeteners'
past_frac = {p: w['past_share'][p] / w['animal_area'][p] for p in w['past_share']}                  # share of a ruminant product's land that is pasture (the rest is its feed cropland)
EH, cH, pH = collections.defaultdict(float), collections.defaultdict(float), collections.defaultdict(float); n_items = 0; energy_unmapped = 0.0
for item, lp in w['lpt'].items():
    food = yv(F.get(('Australia', item, 'Food'), {}), YR)
    if food == 0: continue
    assert item in GRP, 'HALF counts an item the bridge does not map: ' + item
    ha = food / pop * lp / 1000                                                                     # world-average ha a person
    pf = past_frac.get(item, past_frac['Milk - Excluding Butter'] if item in ('Butter, Ghee', 'Cream') else 0.0)
    pH[GRP[item]] += ha * pf; cH[GRP[item]] += ha * (1 - pf); n_items += 1
    EH[GRP[item]] += fbs(item, 'Food supply (kcal)') / GT * KCAL_DAY * 4.184                       # kJ a day
HALF_HA = sum(cH.values()) + sum(pH.values())
assert abs(HALF_HA - HALF_AU) < 6e-4, (HALF_HA, HALF_AU)                                           # the diet's land is the 1.318 ha HALF prints
# ---------------------------------------------------------------- the model world, from the evaluator
mg = json.loads(subprocess.run(['node', D + 'b139_model_runs.mjs', 'groups', '0.12', '0'], capture_output=True, text=True, check=True).stdout)
M12, M0 = mg
assert M12['losses'] == 0.12 and M0['losses'] == 0.0
C_KM2, P_KM2 = M12['land_km2']['cropland'], M12['land_km2']['pasture']; CM2, PM2 = C_KM2 * 1e6, P_KM2 * 1e6
def arr(M, k): return {g['name']: g[k] for g in M['groups']}
EM, QM = arr(M12, 'energy_kj'), arr(M12, 'protein_g'); cM12, pM12, cM0, pM0 = arr(M12, 'cropland_m2'), arr(M12, 'pasture_m2'), arr(M0, 'cropland_m2'), arr(M0, 'pasture_m2')
assert all(abs(arr(M0, 'energy_kj')[g] - EM[g]) < 1e-9 for g in GROUPS), 'the diet as eaten must not depend on the waste setting'
S_G = {g: (cM0[g] / cM12[g] if cM12[g] > 0 else (pM0[g] / pM12[g] if pM12[g] > 0 else 1.0)) for g in GROUPS}   # eaten share of the model's loss factors, group by group
YMc, YMp = {g: cM0[g] / EM[g] for g in GROUPS}, {g: pM0[g] / EM[g] for g in GROUPS}                # m2 per (kJ a day), waste 0 (land a kJ supplied)
KAPPA_C, KAPPA_P = O_CROP * 1e4 / C_KM2, O_PAST * 1e4 / P_KM2                                        # world-average ha of output per Australian ha
YHc = {g: cH[g] * 1e4 / KAPPA_C / EH[g] for g in GROUPS}; YHp = {g: pH[g] * 1e4 / KAPPA_P / EH[g] for g in GROUPS}
ETOT_M, ETOT_H = sum(EM.values()), sum(EH.values())
SIG_M, SIG_H = {g: EM[g] / ETOT_M for g in GROUPS}, {g: EH[g] / ETOT_H for g in GROUPS}
K_W = KAPPA_C / KAPPA_P
NF = {0.12: M12['nonfood'], 0.0: M0['nonfood']}
def capacity(s, k=K_W):
    """s: dict switch -> 'H' (HALF-like) or 'M' (model-like); k: the exchange rate of the pool when P is HALF-like. Million people."""
    Et = ETOT_H if s['R'] == 'H' else ETOT_M; sg = SIG_H if s['C'] == 'H' else SIG_M
    c = p = 0.0
    for g in GROUPS:
        e = Et * sg[g]; f = 1 / S_G[g] if s['W'] == 'M' else 1.0
        c += e * (YHc[g] if s['Yc'] == 'H' else YMc[g]) * f; p += e * (YHp[g] if s['Yp'] == 'H' else YMp[g]) * f
    if s['N'] == 'M':
        n = NF[0.12 if s['W'] == 'M' else 0.0]; c += n['cropland_m2']; p += n['pasture_m2']
    if s['P'] == 'M': return min((CM2 + PM2) / (c + p), CM2 / c) / 1e6
    return (PM2 + k * CM2) / (p + k * c) / 1e6
ALL_M = {f: 'M' for f in ('P', 'R', 'W', 'C', 'Yc', 'Yp', 'N')}; ALL_H = {f: 'H' for f in ALL_M}
# ---------------------------------------------------------------- the end points and the cross-checks
CHECKS = []
def chk(label, got, want, tol):
    ok = abs(got - want) <= tol; CHECKS.append((label, got, want, ok)); return ok
RES = next(r for r in dicts('results/2025-fixed.csv') if r['zone'] == '1' and r['preset'] == 'short'); MODEL_CAP = float(RES['capacity']) / 1e6
HC = dicts(D + 'harmonised_comparison.csv'); HALF_E = float(next(r for r in HC if r['method'].startswith('HALF'))[list(HC[0].keys())[10]])
chk('machine, all features model-like, against the evaluator and results/2025-fixed.csv', capacity(ALL_M), MODEL_CAP, 1e-6 * MODEL_CAP)
chk('machine, all features HALF-like, against column (e) of harmonised_comparison.csv (76.0, one decimal)', capacity(ALL_H), HALF_E, 0.05)
chk('machine, all features HALF-like, against Australia output over the diet (%.2f + %.2f Mha over %.4f ha)' % (O_CROP, O_PAST, HALF_HA), capacity(ALL_H), (O_CROP + O_PAST) / HALF_HA, 1e-6)
# k of B114's variant 1: cropland foods' energy a m2 over pasture-fed foods' energy a m2, in the diet's own groups
def k_energy():
    cm = [g for g in GROUPS if cM12[g] > 0]; pm = [g for g in GROUPS if pM12[g] > 0]
    return (sum(EM[g] for g in cm) / sum(cM12[g] for g in cm)) / (sum(EM[g] for g in pm) / sum(pM12[g] for g in pm))
K_E = k_energy()
chk('crop-equivalent energy rate k against B114 (91.3)', K_E, 91.3, 0.05)
def one_off(feat, k=K_W):
    s = dict(ALL_M); s[feat] = 'H'; return capacity(s, k)
B114 = {(r['variant'], r['preset']): float(r['capacity_million']) for r in dicts('analysis/pasture_2025/pairing_relaxed.csv')}
chk('the pooled-land switch alone at k = %.1f against B114 variant 1 (81.70)' % K_E, one_off('P', K_E), B114[('1', 'short')], 0.006)
# the protein-held pooled step: the linear program of B114 at the model's own pool rule (k = 1), pasture-fed groups down only, every other group 1 to 3 times, energy and protein held
def protein_held(cap=3.0):
    n = len(GROUPS); c = np.array([cM12[g] for g in GROUPS]); p = np.array([pM12[g] for g in GROUPS]); e = np.array([EM[g] for g in GROUPS]); q = np.array([QM[g] for g in GROUPS])
    nf = NF[0.12]; Ckm, Pkm = C_KM2, P_KM2
    A_ub = [list(c) + [-Ckm], list(p + c) + [-(Pkm + Ckm)], list(-e) + [0], list(-q) + [0]]
    b_ub = [-nf['cropland_m2'], -(nf['pasture_m2'] + nf['cropland_m2']), -sum(e) * (1 - 1e-12), -sum(q) * (1 - 1e-12)]
    bounds = [(0, 1) if pM12[g] > 0 else (1, cap) for g in GROUPS] + [(1e-9, None)]
    res = linprog([0] * n + [1], A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs'); assert res.status == 0, res.message
    s = res.x[:n]; N = 1 / res.x[n]
    assert (s @ c + nf['cropland_m2']) * N <= Ckm * (1 + 1e-7) and (s @ e) >= sum(e) * (1 - 1e-7) and (s @ q) >= sum(q) * (1 - 1e-7), 'the protein-held solution breaks a constraint'
    return N, s
N_Q, S_Q = protein_held()
CAP_SENS = {cp: protein_held(cp)[0] for cp in (2.0, 3.0, 5.0)}                                      # sensitivity of the protein-held capacity to the cap on the substituting groups
c0 = sum(cM12.values()) + NF[0.12]['cropland_m2']; p0 = sum(pM12.values()) + NF[0.12]['pasture_m2']
K_Q = (PM2 - N_Q * 1e6 * p0) / (N_Q * 1e6 * c0 - CM2)                                              # the exchange rate whose pooled formula gives the program's capacity
chk('protein-held program: the exchange rate K_Q reproduces its capacity', (PM2 + K_Q * CM2) / (p0 + K_Q * c0) / 1e6, N_Q, 1e-6)
# ---------------------------------------------------------------- the games and the all-orderings average
def game(features, merge=None, k=K_W):
    """features: list of switch names; merge: dict name -> tuple of switches that move together. Returns per-feature forward, reverse, average, sd, log average, plus start and end."""
    merge = merge or {}; sw = lambda f: merge.get(f, (f,))
    cache = {}
    def state(mask):
        s = {x: 'H' for x in ALL_M}
        for f in mask:
            for x in sw(f): s[x] = 'M'
        return s
    def v(mask, log=False):
        key = (frozenset(mask), log)
        if key not in cache:
            x = capacity(state(mask), k); cache[key] = math.log(x) if log else x
        return cache[key]
    out = {f: {'avg': 0.0, 'log': 0.0, 'sq': 0.0} for f in features}; n = 0
    for order in itertools.permutations(features):
        m = set()
        for f in order:
            a, b = v(m), v(m | {f}); la, lb = v(m, True), v(m | {f}, True); m = m | {f}
            out[f]['avg'] += b - a; out[f]['log'] += lb - la; out[f]['sq'] += (b - a) ** 2
        n += 1
    full = set(features)
    for f in features:
        out[f]['avg'] /= n; out[f]['log'] /= n; out[f]['sd'] = math.sqrt(max(out[f]['sq'] / n - out[f]['avg'] ** 2, 0.0))
        out[f]['fwd'] = v({f}) - v(set()); out[f]['rev'] = v(full) - v(full - {f})
    return out, v(set()), v(full), n, v
def shapley_subsets(features, v):
    """The same average by the subset-weight formula, independently of the enumeration of orders."""
    n = len(features); res = {}
    for f in features:
        others = [x for x in features if x != f]; tot = 0.0
        for r in range(n):
            wgt = math.factorial(r) * math.factorial(n - r - 1) / math.factorial(n)
            for S in itertools.combinations(others, r): tot += wgt * (v(set(S) | {f}) - v(set(S)))
        res[f] = tot
    return res
FEATS = ['P', 'R', 'W', 'C', 'Yc', 'Yp', 'N']
LABEL = {'P': 'the land pool (one pool in world-average hectares against the model rule)', 'R': 'the per-person requirement (13.60 MJ against 7.376 MJ a day)', 'W': "waste (none on top of the supply against the model's loss factors)",
         'C': 'the diet composition (Australian food balance mix against the guideline diet)', 'Yc': 'the yield layer, cropland', 'Yp': 'the yield layer, pasture-fed output', 'N': 'non-food land (wool, fibre, biofuel)',
         'RW': 'the per-person requirement and waste together'}
GAMES = [('G1 primary: pool at world-average hectares (k = %.2f)' % K_W, FEATS, None, K_W),
         ('G2 requirement and waste as one switch (k = %.2f)' % K_W, ['P', 'RW', 'C', 'Yc', 'Yp', 'N'], {'RW': ('R', 'W')}, K_W),
         ('G3 pool by energy substitution, protein not held (B114 variant 1; k = %.1f)' % K_E, FEATS, None, K_E),
         ('G4 pool by substitution with protein held (k = %.1f)' % K_Q, FEATS, None, K_Q)]
def build():
    out = [['bridge', 'feature', 'forward (million people)', 'reverse (million people)', 'all-orderings average (million people)', 'share of the total change', 'SD over orderings (million)', 'average on the log scale', 'note']]
    keep = {}
    for name, feats, merge, k in GAMES:
        res, v0, v1, n, v = game(feats, merge, k); keep[name] = (res, v0, v1, n, v)
        tot = v1 - v0
        assert abs(sum(r['avg'] for r in res.values()) - tot) < 1e-9, 'the averages do not add to the total change'
        sub = shapley_subsets(feats, v)
        assert all(abs(sub[f] - res[f]['avg']) < 1e-9 for f in feats), 'orders and subset weights disagree'
        for f in feats:
            r = res[f]
            note = {'P': 'forward and reverse by the exchange rate k of the pool when HALF-like', 'R': 'opposite in sign to W: the pair is the robust number (G2)', 'W': 'not separable from R in the records (FAO supply holds the waste)',
                    'Yp': 'allocation rule, data and productivity conversion not separable', 'C': 'pattern and what counts as food not separable'}.get(f, '')
            out.append([name, LABEL[f], round(r['fwd'], 2), round(r['rev'], 2), round(r['avg'], 2), round(r['avg'] / tot, 3), round(r['sd'], 2), round(r['log'], 3), note])
        out.append([name, 'start: every switch HALF-like', '', '', round(v0, 2), '', '', round(math.log(v0), 3), 'HALF at Australian productivity (column (e): %.1f)' % HALF_E if k == K_W else 'not HALF\'s 76.0: the HALF world with the pooling that exchange rate gives; difference to 76.0 is %.1f and is not attributed' % (v0 - HALF_E)])
        out.append([name, 'end: every switch model-like', '', '', round(v1, 2), '', '', round(math.log(v1), 3), 'the corrected model (results/2025-fixed.csv: %.2f)' % MODEL_CAP])
        out.append([name, 'total change, start to end', '', '', round(tot, 2), 1.0, '', round(math.log(v1 / v0), 3), '%d orderings, exact' % n])
    for cp, nq in CAP_SENS.items(): out.append(['protein-held program', 'capacity with the substituting groups capped at %.0f times their present amount (million)' % cp, '', '', round(nq, 2), '', '', '', 'energy and protein at least the diet\'s (93.1 g a day); pasture-fed groups down only; B114 variant 1 reads 81.70 with protein 80.9 g'])
    for lab, got, want, ok in CHECKS: out.append(['checks', lab, '', '', round(got, 4), '', '', '', 'against %.4f: %s' % (want, 'PASS' if ok else 'FAIL')])
    return out, keep
def groups_table():
    rows = [['group', 'HALF energy (kJ a day)', 'HALF cropland (world-average ha a person)', 'HALF pasture (world-average ha a person)', 'HALF cropland (Australian m2 a person)', 'HALF pasture (Australian m2 a person)',
             'model energy (kJ a day)', 'model protein (g a day)', 'model cropland m2 a person, waste 12%', 'model pasture m2 a person, waste 12%', 'model cropland m2, waste 0', 'model pasture m2, waste 0', 'eaten share of the model loss factors']]
    for g in GROUPS:
        rows.append([g, round(EH[g], 1), round(cH[g], 5), round(pH[g], 5), round(cH[g] * 1e4 / KAPPA_C, 1), round(pH[g] * 1e4 / KAPPA_P, 1), round(EM[g], 1), round(QM[g], 2), round(cM12[g], 1), round(pM12[g], 1),
                     round(cM0[g], 1), round(pM0[g], 1), round(S_G[g], 4)])
    rows.append(['total or constant', round(ETOT_H, 1), round(sum(cH.values()), 5), round(sum(pH.values()), 5), '', '', round(ETOT_M, 1), round(sum(QM.values()), 2), '', '', '', '',
                 'kappa cropland %.4f, pasture %.4f (world-average ha of output per Australian ha); k = %.3f; k energy %.2f; k protein-held %.2f (capacity %.2f million)' % (KAPPA_C, KAPPA_P, K_W, K_E, K_Q, N_Q)])
    return rows
def main():
    out, keep = build()
    if DEMO:
        # the check of the script: the primary game's average for the land pool, recomputed by the subset-weight formula, must equal the csv's value; a planted value does not
        res, v0, v1, n, v = keep[GAMES[0][0]]
        sub = shapley_subsets(FEATS, v)
        planted = round(res['P']['avg'], 2) * 2
        print('EXAMPLE (deliberate wrong value): the land pool switch claimed as %.2f million (twice the value) instead of %.2f' % (planted, res['P']['avg']))
        ok = abs(sub['P'] - planted) < 0.006
        print('EXAMPLE wrong value check: subset-weight formula %.4f, claimed %.2f: %s' % (sub['P'], planted, 'PASS' if ok else 'FAIL (the planted value is rejected)'))
        sys.exit(0 if not ok else 1)
    assert all(ok for _, _, _, ok in CHECKS), [c for c in CHECKS if not c[3]]
    csv.writer(open(D + 'bridge_half_to_model.csv', 'w', newline='')).writerows(out)
    csv.writer(open(D + 'bridge_groups.csv', 'w', newline='')).writerows(groups_table())
    for r in out: print(' | '.join(str(x) for x in r[:8]))
    print('K_W %.3f K_E %.2f K_Q %.2f; protein-held program capacity %.2f million; kappa %.4f %.4f; HALF energy %.0f kJ, model %.0f kJ, ratio %.4f' % (K_W, K_E, K_Q, N_Q, KAPPA_C, KAPPA_P, ETOT_H, ETOT_M, ETOT_H / ETOT_M))
    print('protein-held program group multiples:', {g: round(x, 2) for g, x in zip(GROUPS, S_Q)})
main()
