#!/usr/bin/env python3
"""Nutrition-constrained diet optimisation inside the model's own accounting (SCOPE.md E11).
Usage: python3 -I analysis/nutrition_lp_2025/optimise.py RELEASE ZONE PRESET OUT.json [MAXSHARE [fixgroups] [capK] [micro]]          (repository root; needs scipy and the built data)

The decision is the diet: grams a day of each of the model's accounting units (composite foods and single foods; server.mjs). The model keeps all its own accounting (ingredient mixes, losses, yields, land, the
allocation of land types, recycling), so the capacity of a diet is the model's capacity, not an approximation. The search is a sequence of linear programs (successive linearisation): at the current diet, the value
of one m2 of cropping and of pasture land is the change of the log of the capacity when the crop-land or pasture-land diet is scaled by 5%; the program then minimises the value of the land a person uses subject to
  * the energy, protein and fibre of the least demanding diet of the model's own family (the Diet sheet's sedentary diets at meat shares 0 to 15%),
  * fat 20 to 35%, protein 10 to 25%, carbohydrate 45 to 65% of energy (AMDR),
  * for each food group, the serves a week between the minimum and maximum of the same family (Diet sheet), so that the diet always has the fruit, vegetables, cereals, dairy and so on of the guidelines,
  * optionally no unit more than MAXSHARE of its group's serves (default 1: free choice; 0.4: some variety), and with 'fixgroups' the serves of each group stay at the default diet's (only the choice of food within each group is free), and with 'capK' no unit above K times its default intake (a unit nobody eats stays at zero),
and the model evaluates the result; the step is halved until the capacity rises. Groups whose shares in the workbook do not sum to one (legumes and the sweeteners group) stay at the default diet.
With 'micro', the diet must also meet the recommended intake of calcium, iron, zinc, iodine, vitamin B12, vitamin A, folate, vitamin C, magnesium and potassium, valued from AUSNUT 2023 by unit_micronutrients.csv (match_ausnut.py); the intakes are checked against the NHMRC table (see RDI below).
What it does NOT constrain: taste, cost, culture; the bioavailability of iron and zinc from plant foods; vitamins D, E and K, selenium and the fatty acids; and without 'micro' no vitamin or mineral."""
import json, subprocess, sys, os
import numpy as np
from scipy.optimize import linprog
rel, zone, preset, outfile = sys.argv[1:5]; MAXSHARE = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0; FIXGROUPS = 'fixgroups' in sys.argv[6:]; MICRO = 'micro' in sys.argv[6:]; CAPMULT = next((float(a[3:]) for a in sys.argv[6:] if a.startswith('cap')), None)
ROOT = os.getcwd()
srv = subprocess.Popen(['node', os.path.join(ROOT, 'analysis/nutrition_lp_2025/server.mjs'), rel, zone, preset], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, cwd=ROOT)
def q(o): srv.stdin.write(json.dumps(o) + '\n'); srv.stdin.flush(); return json.loads(srv.stdout.readline())
U = q({'cmd': 'units'}); DEF = q({'cmd': 'defaultgrams'}); N0 = DEF['capacity']
units = U['units']; groups = {g['row']: g for g in U['groups']}
FIXED = {g['row'] for g in U['groups'] if abs(sum(DEF['shares'][str(r)] for r in g['units']) - 1) > 0.01}      # groups whose X do not sum to one
g0 = np.array([DEF['grams'][str(u['row'])] / 7 for u in units])                                            # grams a day at the default diet
Qv = np.array([u['Q'] for u in units]); idx = {u['row']: i for i, u in enumerate(units)}
P = lambda k: np.array([(u['perGram'][k] if u['perGram'] else 0.0) for u in units])
land, kJ, prot, fat, carb, fib = P('land'), P('kJ'), P('protein'), P('fat'), P('carb'), P('fibre')       # per gram eaten (per week-gram coefficients are the same ratios)
typ = np.array([u['type'] == 'pasture' for u in units])
MK = ['calcium_mg', 'iron_mg', 'zinc_mg', 'iodine_ug', 'b12_ug', 'vitA_re_ug', 'folate_dfe_ug', 'vitC_mg', 'magnesium_mg', 'potassium_mg']
# recommended daily intakes (RDI; AI for potassium) for the adult population, the average of men and women aged 19 to 50, from the NHMRC and NZ Ministry of Health
# Nutrient Reference Values 2006 (v1.2, 2017), checked 2026-10-30 against 'Foundation diets/nutrient-refererence-dietary-intakes.pdf' of the models archive:
# calcium 1,000 (men and women), iron 8 and 18 mg, zinc 14 and 8, iodine 150 ug, B12 2.4 ug, vitamin A 900 and 700 ug RE, folate 400 ug DFE, vitamin C 45 mg,
# magnesium 400 to 420 and 310 to 320, potassium AI 3,800 and 2,800. Adults only: children's and pregnant women's intakes are not weighted in
RDI = dict(calcium_mg=1000, iron_mg=13, zinc_mg=11, iodine_ug=150, b12_ug=2.4, vitA_re_ug=800, folate_dfe_ug=400, vitC_mg=45, magnesium_mg=365, potassium_mg=3300)
mic = {k: np.zeros(len(units)) for k in MK}
if MICRO:
    import csv as _csv
    MR = {int(r['row']): r for r in _csv.DictReader(open(os.path.join(ROOT, 'analysis/nutrition_lp_2025/unit_micronutrients.csv')))}
    for i, u in enumerate(units):
        r = MR[u['row']]
        for k in MK: mic[k][i] = float(r[k])
        if not u['perGram'] or u['perGram']['kJ'] <= 0:                    # no macronutrients in the workbook: take AUSNUT's
            kJ[i], prot[i], fat[i], carb[i], fib[i] = (float(r[c]) / 100 for c in ('ausnut_kJ_per_100g', 'ausnut_protein', 'ausnut_fat', 'ausnut_carb', 'ausnut_fibre'))
FAM = q({'cmd': 'familygrams'})                                                                         # the family of the model's diets, valued with the same unit coefficients as the program
famt = [dict(kJ=float(kJ @ (np.array([f['grams'][str(u['row'])] for u in units]) / 7)), protein=float(prot @ (np.array([f['grams'][str(u['row'])] for u in units]) / 7)), fibre=float(fib @ (np.array([f['grams'][str(u['row'])] for u in units]) / 7))) for f in FAM]
fl = {k: min(t[k] for t in famt) for k in ('kJ', 'protein', 'fibre')}
def capacity(g): return q({'cmd': 'eval', 'grams': {str(u['row']): float(g[i] * 7) for i, u in enumerate(units)}})
def totals(g): return dict(**({k: float(mic[k] @ g) for k in MK} if MICRO else {}), kJ=float(kJ @ g), protein=float(prot @ g), fat=float(fat @ g), carb=float(carb @ g), fibre=float(fib @ g), land_crop=float(land[~typ] @ g[~typ]), land_pasture=float(land[typ] @ g[typ]))
def weights(g):
    base = capacity(g)['capacity']; out = []
    for mask in (~typ, typ):
        g2 = g.copy(); g2[mask] *= 1.05; c = capacity(g2)['capacity']; L = float(land[mask] @ g[mask])
        out.append(max((np.log(base) - np.log(c)) / 0.05 / L, 1e-12) if L > 0 else 1e-12)
    return out[0], out[1], base
def solve(wc, wp, free_rows):
    n = len(units); c = np.where(typ, wp, wc) * land
    A, b = [], []
    A.append(-kJ); b.append(-fl['kJ'] / 1.0)                      # energy floor (kJ a day)
    A.append(-prot); b.append(-fl['protein']); A.append(-fib); b.append(-fl['fibre'])
    A.append(fat * 37 - 0.35 * kJ); b.append(0); A.append(-(fat * 37 - 0.20 * kJ)); b.append(0)
    A.append(prot * 17 - 0.25 * kJ); b.append(0); A.append(-(prot * 17 - 0.10 * kJ)); b.append(0)
    A.append(carb * 17 - 0.65 * kJ); b.append(0); A.append(-(carb * 17 - 0.45 * kJ)); b.append(0)
    if MICRO:
        for k in MK: A.append(-mic[k]); b.append(-RDI[k])
    bounds = [(0, None) if CAPMULT is None else (0, CAPMULT * g0[i]) for i in range(n)]; Aeq, beq = [], []
    for gr, g in groups.items():
        rows = [idx[r] for r in g['units']]; serv = np.zeros(n); serv[rows] = 7 / Qv[rows]                   # serves a week per gram a day
        if gr in FIXED:
            for i in rows: bounds[i] = (g0[i], g0[i])
            continue
        lo, hi = g['serves']
        if FIXGROUPS: lo = hi = float(DEF['serves'][str(gr)])
        A.append(-serv); b.append(-lo); A.append(serv); b.append(hi)
        ms = max(MAXSHARE, 1.05 / len(rows))
        if ms < 1:
            for i in rows: a = np.zeros(n); a[i] = 7 / Qv[i]; a[rows] -= ms * 7 / Qv[rows]; A.append(a); b.append(0.0)      # unit serves <= MAXSHARE x group serves
    r = linprog(c, A_ub=np.array(A), b_ub=np.array(b), bounds=bounds, method='highs')
    return r.x if r.status == 0 else None
g = g0.copy(); best = N0; hist = [{'step': 0, 'capacity': N0, **totals(g)}]
for it in range(1, 9):
    wc, wp, base = weights(g); gl = solve(wc, wp, None)
    if gl is None: print('infeasible'); break
    a = 1.0
    while a > 0.02:
        gn = g + a * (gl - g); c = capacity(gn)['capacity']
        if c > best * 1.0005: break
        a /= 2
    else:
        break
    g, best = gn, c; hist.append({'step': it, 'alpha': a, 'weights': [wc, wp], 'capacity': c, **totals(g)})
    print(it, round(c / 1e6, 2), 'alpha', a, flush=True)
final = capacity(g)
res = {'micro': MICRO, 'rdi': RDI if MICRO else None, 'release': rel, 'zone': zone, 'preset': preset, 'maxshare': MAXSHARE, 'fixgroups': FIXGROUPS, 'cap': CAPMULT, 'capacity_default': N0, 'capacity_optimised': best, 'gain': best / N0, 'floors': fl,
       'default_totals': totals(g0), 'optimised_totals': totals(g), 'history': hist,
       'diet_default': [{'name': units[i]['name'], 'cat': units[i]['cat'], 'g_day': float(g0[i])} for i in range(len(units)) if g0[i] > 0.5],
       'diet_optimised': [{'name': units[i]['name'], 'cat': units[i]['cat'], 'g_day': float(g[i])} for i in range(len(units)) if g[i] > 0.5]}
json.dump(res, open(outfile, 'w'), indent=1); print('default', round(N0 / 1e6, 2), 'optimised', round(best / 1e6, 2), 'x', round(best / N0, 2))
srv.stdin.close()
