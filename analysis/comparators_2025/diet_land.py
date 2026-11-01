#!/usr/bin/env python3
"""Land per person of ten Australian diets, for the like-for-like comparison with Peters et al. 2016 (candidate paper 5; their table is land per person for ten US diets).
Usage: python3 -I analysis/comparators_2025/diet_land.py [RELEASE]          (repository root; needs the built data)
The model's own family of nutritionally adequate diets (Diet sheet, sedentary activity, red meat 57.8% of meat) at meat and egg shares 15, 12, 10, 7.5, 5, 2.5 and 0%, valued with the model's land
per gram (nutrition model, server.mjs), and the three optimised diets of the nutrition model (variants A, B, C, Australia, short term, ten micronutrients; `analysis/nutrition_lp_2025/variants.csv` run).
Land per person is the land of the food (cropland and pasture, hectares a year, avoidable waste excluded because the unit coefficients count the diet as eaten); capacity is the model's own, per diet."""
import json, subprocess, sys, os, csv
REL = sys.argv[1] if len(sys.argv) > 1 else '2025-improved'
srv = subprocess.Popen(['node', 'analysis/nutrition_lp_2025/server.mjs', REL, '1', 'short'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
def q(o): srv.stdin.write(json.dumps(o) + '\n'); srv.stdin.flush(); return json.loads(srv.stdout.readline())
U = q({'cmd': 'units'}); units = U['units']; FAM = q({'cmd': 'familygrams'}); DEF = q({'cmd': 'defaultgrams'})
pasture = {u['row']: u['type'] == 'pasture' for u in units}; land = {u['row']: (u['perGram']['land'] if u['perGram'] else 0.0) for u in units}
kJ = {u['row']: (u['perGram']['kJ'] if u['perGram'] else 0.0) for u in units}
def row(name, gweek):                                                    # gweek: grams a week of each unit row (string keys)
    c = sum(land[int(r)] * g / 7 for r, g in gweek.items() if not pasture[int(r)]) * 365 / 1e4; p = sum(land[int(r)] * g / 7 for r, g in gweek.items() if pasture[int(r)]) * 365 / 1e4
    cap = q({'cmd': 'eval', 'grams': {str(r): float(g) for r, g in gweek.items()}})['capacity']
    return [name, round(cap / 1e6, 1), round(c, 2), round(p, 2), round(c + p, 2)]
rows = [['diet', 'people_fed_million', 'cropland_ha_per_person_year', 'pasture_ha_per_person_year', 'total_ha_per_person_year']]
rows.append(row('The model\'s default diet (12% meat and eggs, 57.8% red)', DEF['grams']))
print(len(FAM), 'family diets; keys', list(FAM[0].keys())[:6])
for f in FAM:
    m = f.get('meat')
    if m is not None and round(m * 100, 1) in (15.0, 12.0, 10.0, 7.5, 5.0, 2.5, 0.0): rows.append(row(f'Guideline diet, {m * 100:g}% meat and eggs', f['grams']))
for k, tag in (('1_short_micro_fixcap3', 'A: foods swapped within groups'), ('1_short_micro_famcap3', 'B: serves free in the guideline range'), ('1_short_micro_free', 'C: free choice')):
    fn = os.path.join(os.environ.get('VARDIR', '/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/var55'), k + '.json')
    if os.path.exists(fn):
        r = json.load(open(fn)); g = {str(k2): v * 7 for k2, v in r['g_vec'].items()}; rows.append(row('Optimised ' + tag, g))
csv.writer(open('analysis/comparators_2025/diet_land.csv', 'w', newline='')).writerows(rows)
for r in rows: print(r)
