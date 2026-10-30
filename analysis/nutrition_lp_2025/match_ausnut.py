#!/usr/bin/env python3
"""Micronutrients for the model's accounting units from AUSNUT 2023 (SCOPE.md E11, stage 2).
Usage: python3 -I analysis/nutrition_lp_2025/match_ausnut.py AUSNUT_PROFILES_XLSX OUT.csv          (repository root; AUSNUT_PROFILES_XLSX = 'AUSNUT 2023 - Food nutrient profiles.xlsx' in the models archive,
                                                                                                     Foundation diets/AUSNUT2023/; needs the built data and openpyxl)
The workbook has energy, protein, fat, carbohydrate and fibre for each unit and nothing else. Each unit is matched to the three AUSNUT 2023 foods of the right food group whose energy, protein, fat, carbohydrate and
fibre per 100 g are closest to the unit's own (the same food as eaten, raw or cooked, is the one whose macronutrients agree), and the unit takes the mean of their micronutrients per gram. Words of the unit's name
that appear in the food's name count in the food's favour. The match is reported with its distance so that a poor match can be seen; units whose macronutrients the workbook lacks (cheeses) take AUSNUT's macronutrients as
well. Food groups are the first two digits of the AUSNUT survey ID (12 cereals, 13 cereal-based, 14 fats and oils, 15 fish, 16 fruit, 17 eggs, 18 meat, 19 milk products, 20 substitutes, 22 seeds and nuts, 24 vegetables, 25 legumes, 27 sugar,
28 confectionery, 11 and 29 drinks, 31 miscellaneous)."""
import csv, json, os, re, subprocess, sys
import openpyxl
src, out = sys.argv[1:3]; ROOT = os.getcwd()
srv = subprocess.Popen(['node', os.path.join(ROOT, 'analysis/nutrition_lp_2025/server.mjs'), '2025-improved', '1', 'short'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, cwd=ROOT)
srv.stdin.write('{"cmd":"units"}\n'); srv.stdin.flush(); U = json.loads(srv.stdout.readline())['units']; srv.stdin.close()
ws = openpyxl.load_workbook(src, read_only=True, data_only=True)['Food nutrient profiles']; R = list(ws.iter_rows(values_only=True)); H = list(R[2]); foods = [r for r in R[3:] if r[0]]
col = {h: i for i, h in enumerate(H)}
MICRO = {'calcium_mg': 'Calcium (Ca) (mg)', 'iron_mg': 'Iron (Fe) (mg)', 'zinc_mg': 'Zinc (Zn) (mg)', 'iodine_ug': 'Iodine (I) (ug)', 'b12_ug': 'Cobalamin (B12) (ug)', 'vitA_re_ug': 'Vitamin A retinol equivalents (ug)',
         'folate_dfe_ug': 'Dietary folate equivalents (ug)', 'vitC_mg': 'Vitamin C (mg)', 'magnesium_mg': 'Magnesium (Mg) (mg)', 'potassium_mg': 'Potassium (K) (mg)', 'thiamin_mg': 'Thiamin (B1) (mg)', 'riboflavin_mg': 'Riboflavin (B2) (mg)'}
MAC = {'kJ': 'Energy with dietary fibre (kJ)', 'protein': 'Protein (g)', 'fat': 'Total fat (g)', 'carb': 'Available carbohydrate, without sugar alcohols (g)', 'fibre': 'Dietary fibre (g)'}
num = lambda v: float(v) if isinstance(v, (int, float)) else 0.0
F = [dict(id=str(r[0]), grp=int(str(r[0])[:2]), name=str(r[3]), mac={k: num(r[col[v]]) for k, v in MAC.items()}, mic={k: num(r[col[v]]) for k, v in MICRO.items()}) for r in foods]
GROUPS = {'Cereal whole': [12, 13], 'Cereal ref': [12, 13], 'Dairy High': [19, 20], 'Dairy Med': [19, 20], 'Dairy Low': [19, 20], 'Fruit': [16], 'Legume': [25], 'Meat red': [18], 'Meat white': [18, 15, 17, 25], 'Nut & seed': [22],
          'Vege green': [24], 'Vege orange': [24], 'Vege other': [24], 'Vege starch': [24], 'Fat & oil': [14], 'Other': [11, 27, 28, 29, 31], 'Lacto-ovo': [17, 19, 25, 12, 13, 20, 24]}
STOP = {'wm', 'ref', 'reg', 'red', 'fat', 'whole', 'various', 'total', 'low', 'high', 'med', 'regular', 'the', 'and', 'of', 'or'}
def words(s): return {w for w in re.findall(r'[a-z]{3,}', s.lower()) if w not in STOP}
def dist(u, f):
    d = 0.0
    for k, sc in (('kJ', 150.0), ('protein', 4.0), ('fat', 4.0), ('carb', 8.0), ('fibre', 2.0)): d += ((u[k] * 100 - f['mac'][k]) / sc) ** 2
    return d ** 0.5
rows = []; hdr = ['row', 'category', 'unit', 'model_kJ_per_100g', 'model_protein', 'model_fat', 'model_carb', 'model_fibre', 'match_distance', 'matches'] + list(MICRO) + ['ausnut_kJ_per_100g', 'ausnut_protein', 'ausnut_fat', 'ausnut_carb', 'ausnut_fibre']
for u in U:
    pg = u['perGram']; has = bool(pg and pg['kJ'] > 0)
    uw = words(u['name'])
    cand = [f for f in F if f['grp'] in GROUPS[u['cat']]]
    if has:
        ranked = sorted(cand, key=lambda f: dist(pg, f) - 8.0 * len(uw & words(f['name'])))
    else:                                                     # no macronutrients in the workbook: by name only
        ranked = sorted(cand, key=lambda f: -len(uw & words(f['name'])) + 0.001 * len(f['name']))
    top = ranked[:3]; mic = {k: sum(f['mic'][k] for f in top) / len(top) / 100.0 for k in MICRO}                  # per gram
    d = dist(pg, top[0]) if has else None
    rows.append([u['row'], u['cat'], u['name'], round(pg['kJ'] * 100) if has else '', round(pg['protein'] * 100, 1) if has else '', round(pg['fat'] * 100, 1) if has else '', round(pg['carb'] * 100, 1) if has else '', round(pg['fibre'] * 100, 1) if has else '',
                 round(d, 2) if d is not None else 'no macros', ' | '.join(f['name'][:48] for f in top)] + [round(mic[k], 5) for k in MICRO] + [round(sum(f['mac'][k] for f in top) / len(top), 2) for k in MAC])
csv.writer(open(out, 'w', newline='')).writerows([hdr] + rows)
ds = sorted(float(r[8]) for r in rows if r[8] != 'no macros'); print(len(rows), 'units;', 'median distance', round(ds[len(ds) // 2], 2), '90th', round(ds[int(len(ds) * 0.9)], 2), '; no macros:', sum(1 for r in rows if r[8] == 'no macros'))
for r in sorted(rows, key=lambda r: -(float(r[8]) if r[8] != 'no macros' else 99))[:14]: print(r[1].ljust(12), r[2][:34].ljust(34), r[8], '->', r[9][:90])
