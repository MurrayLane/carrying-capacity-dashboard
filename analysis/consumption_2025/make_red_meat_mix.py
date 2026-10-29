#!/usr/bin/env python3
"""The mix of red meat in the standard diet, carried forward from 2011 (SCOPE.md E7, item-level diet): writes data/2025/red_meat_mix.json and the release releases/2025-diet/release.json.
Usage: python3 -I analysis/consumption_2025/make_red_meat_mix.py FBS_CSV          (repository root; FBS_CSV: FoodBalanceSheets_E_Oceania_NOFLAG.csv of https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_Oceania.zip)

The model's red meat (Base rows 175 to 178, column V, 'Catag pref') is split beef 69.2%, lamb 17.9%, veal 2.0%, pork 10.9%: the shares of unprocessed red meat in the 1995 National Nutrition Survey foods eaten. The 2011-12
National Nutrition and Physical Activity Survey agrees (beef about 43 g, lamb 10 g, pork 7 g a day: 72%, 17%, 12%; Australian Health Survey, per-occasion means summed), so the split was right for 2011. Beef has since fallen
(FAO food balance sheet, Australia, beef and veal 39.1 to 25.9 kg a person, mean 2010-12 against 2021-23) while mutton and goat are level and pork rose. Murray's rule (2026-10-27): move a default by the change of an open series on the same
basis. Each share is multiplied by the change of its FAO series and the four are renormalised. Veal moves with beef and veal. Processed pork (bacon, ham) is in the FAO pork series and not in the model's pork row; that
is the reason to use the CHANGE of the series rather than its level (the level would make pork 42% of red meat, the fresh pork reported by Australian Pork Limited about 23%)."""
import csv, json, os, subprocess, sys
ROOT = os.getcwd(); src = sys.argv[1]
rows = [r for r in csv.DictReader(open(src, encoding='latin-1')) if r['Area'] == 'Australia' and r['Element'].startswith('Food supply quantity (kg/capita/yr)')]
mean = lambda item, ys: sum(float(next(r for r in rows if r['Item'] == item)[f'Y{y}']) for y in ys) / len(ys)
B, L = (2010, 2011, 2012), (2021, 2022, 2023)
ser = {'beef and veal': 'Bovine Meat', 'mutton and goat': 'Mutton & Goat Meat', 'pork': 'Pigmeat'}
kg = {k: (mean(v, B), mean(v, L)) for k, v in ser.items()}
ratio = {k: kg[k][1] / kg[k][0] for k in kg}
m0 = {175: 0.6922456950886146, 176: 0.17890898284622808, 177: 0.01993170633841729, 178: 0.10891361572674008}    # Base!V175:V178 in the workbook (beef, lamb, veal, pork)
mult = {175: ratio['beef and veal'], 176: ratio['mutton and goat'], 177: ratio['beef and veal'], 178: ratio['pork']}
raw = {r: m0[r] * mult[r] for r in m0}; s = sum(raw.values()); m1 = {r: raw[r] / s for r in raw}
json.dump({'method': __doc__, 'kg_per_person': {k: {'2010-12': v[0], '2021-23': v[1], 'ratio': ratio[k]} for k, v in kg.items()}, 'shares_2011': m0, 'shares_2025': m1}, open(os.path.join(ROOT, 'data/2025/red_meat_mix.json'), 'w'), indent=1)
base = json.loads(subprocess.run(['node', '-e', "import('./web/scripts/releases.mjs').then(m=>console.log(JSON.stringify(m.resolveRelease('2025-fuel').baseModel)))"], capture_output=True, text=True, cwd=ROOT).stdout)
base['cellOverrides'].setdefault('Base', {}).update({f'V{r}': round(m1[r], 6) for r in m1})
rel = {'id': '2025-diet', 'label': '2025 data and the red meat mix of the diet', 'status': 'current', 'extends': '2025-fuel', 'layer': '2011 zones', 'vintage': 'FAO food balance to 2023',
       'description': f"Layer 9, the item-level diet (SCOPE.md E7): the split of red meat among beef, lamb, veal and pork (Base!V175:V178), which the thesis took from the 1995 National Nutrition Survey (beef 69.2%, lamb 17.9%, veal 2.0%, pork 10.9%; the 2011-12 survey agrees), carried forward by the change of the FAO food balance series for Australia between 2010-12 and 2021-23 (beef and veal x{ratio['beef and veal']:.3f}, mutton and goat x{ratio['mutton and goat']:.3f}, pork x{ratio['pork']:.3f}) and renormalised: beef {m1[175]:.1%}, lamb {m1[176]:.1%}, veal {m1[177]:.1%}, pork {m1[178]:.1%}. Beef is the land-hungry red meat, so the shift towards pork and lamb raises capacity (analysis/consumption_2025/README.md).",
       'model': base,
       'errata': ["The FAO pork series includes processed pork (bacon, ham), which the model's pork row does not; the change of the series is used, not its level. Fresh pork is about 10.5 kg of the 27 to 28 kg a person (Australian Pork Limited, quoted by IBISWorld), so the pork share may still be too high if processed pork has grown faster than fresh.",
                  "The remaining item-level shares of the diet (cereals, vegetables, fruit, dairy and the rest) are still the 1995 survey; their leverage on capacity is under 0.1% each (analysis/constants_audit/README.md)."]}
os.makedirs(os.path.join(ROOT, 'releases/2025-diet'), exist_ok=True); json.dump(rel, open(os.path.join(ROOT, 'releases/2025-diet/release.json'), 'w'), indent=2)
print({k: round(v, 3) for k, v in ratio.items()}, {r: round(m1[r], 4) for r in m1})
