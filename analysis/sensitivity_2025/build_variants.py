#!/usr/bin/env python3
"""Builds the sensitivity variants of the 2025 results and writes the specification evaluate.mjs reads.

Usage: python3 -I build_variants.py WORK_DIR ABS_DIR          (from this folder's parent repository root: python3 -I analysis/sensitivity_2025/build_variants.py WORK ABS)
  WORK_DIR  where the alternative yield matrices are written (not committed)
  ABS_DIR   the ABS files of analysis/recent_data/fetch_recent.py (livestock_zone.py needs them)
Writes WORK_DIR/variants.json. Then: node analysis/sensitivity_2025/evaluate.mjs WORK_DIR/variants.json analysis/sensitivity_2025/results.csv

One assumption is changed at a time, on the base case (release 2025-organic). Groups:
  crop window / crop rules   the years of ABS crop data and the plausibility rules of zone_yields.py (the matrix is rebuilt, the animal rows too)
  group trend                the factor applied to crops the ABS no longer reports
  meat window                the years of herd and meat data in livestock_zone.py, and the calibration of the ABS meat tables
  land                       the choices of pipeline/land/land_types.json: reserve classes, cropping and pasture measured on the raster instead of the ABS holdings, infrastructure measured
  diet and consumption       the six consumption defaults, each back at its 2011 value or moved by one step
  organic                    the organic factors and baseline
"""
import csv, json, os, re, shutil, subprocess, sys, collections
import xlrd
WORK, ABS = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]); os.makedirs(WORK, exist_ok=True)
ROOT = os.getcwd(); PY = [sys.executable, '-I']
rd = lambda p: list(csv.DictReader(open(os.path.join(ROOT, p))))
variants = []

def run(script, env, *args):
    e = {**os.environ, **env}; subprocess.run(PY + [os.path.join(ROOT, 'pipeline/yields/recent', script), *args], env=e, check=True, stdout=subprocess.DEVNULL, cwd=ROOT)

def yield_variant(vid, group, label, zy_env=None, ls_env=None):
    d = os.path.join(WORK, vid); os.makedirs(d, exist_ok=True)
    if zy_env is not None: run('zone_yields.py', {**zy_env, 'ZY_OUT': d})
    else:
        for f in ('yield_matrix.csv', 'crop_yields_by_year.json'): shutil.copy(os.path.join(ROOT, 'data/2025', f), d)
    run('livestock_zone.py', {**(ls_env or {}), 'ZY_OUT': d}, ABS)
    variants.append({'id': vid, 'group': group, 'label': label, 'matrix': os.path.join(d, 'yield_matrix_livestock.csv')})

# ---- crop window and rules -----------------------------------------------------------------------------------------------------------------
yield_variant('crop_2022', 'crop window', 'crop data of 2022-23 only', {'ZY_YEARS': '2022-23'})
yield_variant('crop_2023', 'crop window', 'crop data of 2023-24 only (the poor year)', {'ZY_YEARS': '2023-24'})
yield_variant('crop_2024', 'crop window', 'crop data of 2024-25 only', {'ZY_YEARS': '2024-25'})
yield_variant('crop_drop_2022', 'crop window', 'drop the record year 2022-23 (mean of 2023-24 and 2024-25)', {'ZY_YEARS': '2023-24,2024-25'})
yield_variant('rules_off', 'crop rules', 'no plausibility cap or floor (only the 10 ha, 10 t and seed rules)', {'ZY_CAP': '1e9', 'ZY_FLOOR': '0'})
yield_variant('rules_strict', 'crop rules', 'strict rules: remove zone yields over 2 or under 0.2 times the national yield', {'ZY_CAP': '2', 'ZY_FLOOR': '0.2'})
# ---- group trend ---------------------------------------------------------------------------------------------------------------------------
trend = json.load(open(os.path.join(ROOT, 'data/abs-2022-25/group_trend.json')))
f25, f21 = {g: v['factor'] for g, v in trend['2025'].items()}, {g: v['factor'] for g, v in trend['2021'].items()}
yield_variant('gt_none', 'group trend', 'crops the ABS no longer reports keep their 2011 yields (factor 1.0)', {'ZY_FACTORS': json.dumps({g: 1.0 for g in f25})})
yield_variant('gt_field_2016', 'group trend', 'field-crop factor from 2016-21 (%.2f) instead of 2022-25 (%.2f)' % (f21['field crops'], f25['field crops']), {'ZY_FACTORS': json.dumps({'field crops': f21['field crops']})})
yield_variant('gt_field_lo', 'group trend', 'field-crop factor 14% lower (the measured error of the rule)', {'ZY_FACTORS': json.dumps({'field crops': f25['field crops'] * 0.86})})
yield_variant('gt_field_hi', 'group trend', 'field-crop factor 14% higher', {'ZY_FACTORS': json.dumps({'field crops': f25['field crops'] * 1.14})})
hort = ('vegetables', 'fruit', 'nuts')
yield_variant('gt_hort_lo', 'group trend', 'vegetable, fruit and nut factors 20% lower (the measured error of the rule is 20 to 22%)', {'ZY_FACTORS': json.dumps({g: f25[g] * 0.8 for g in hort})})
yield_variant('gt_hort_hi', 'group trend', 'vegetable, fruit and nut factors 20% higher', {'ZY_FACTORS': json.dumps({g: f25[g] * 1.2 for g in hort})})
# ---- meat window ---------------------------------------------------------------------------------------------------------------------------
yield_variant('meat_3y', 'meat window', 'meat and herd data of 2022-23 to 2024-25 only (three years, the years of heavy slaughter)', None, {'LS_YEARS': '2022-23,2023-24,2024-25'})
yield_variant('meat_early', 'meat window', 'meat and herd data of 2020-21 to 2022-23 only (before the heavy slaughter)', None, {'LS_YEARS': '2020-21,2021-22,2022-23'})
yield_variant('meat_2025', 'meat window', 'meat and herd data of 2024-25 only', None, {'LS_YEARS': '2024-25'})
yield_variant('meat_nocal', 'meat window', 'ABS meat tables not calibrated to the archive (cattle x1.0 instead of x1.086, sheep x1.0 instead of x1.155)', None, {'LS_CAL': 'off'})

# ---- land ----------------------------------------------------------------------------------------------------------------------------------
M = {int(k): v for k, v in json.load(open(os.path.join(ROOT, 'pipeline/land/zone_to_nrm2011.json')))['zones'].items()}
STATE_OF = {2: range(3, 15), 15: range(16, 26), 26: range(27, 40), 40: range(41, 49), 49: range(50, 56), 56: range(57, 60), 60: [60]}
classes = {int(r['Value']): re.match(r'[\d.]+', r['TERTV8']).group(0).rstrip('.') for r in rd('data/sa2/clum_classes.csv')}
under = lambda c, ps: any(c == p or c.startswith(p + '.') for p in ps)
byclass = collections.defaultdict(lambda: collections.defaultdict(float))                  # NRM code -> class prefix key -> km2
raw = collections.defaultdict(lambda: collections.defaultdict(float))
for r in rd('data/nrm2011/land_use_by_nrm2011.csv'): raw[int(r['zone_code'])][classes[int(r['class_code'])]] += float(r['km2'])
def area(zone, prefixes): return sum(v for c in M[zone] for k, v in raw[c].items() if under(k, prefixes))
def zone_total(fn):
    z = {r: fn(r) for r in M}
    for st, rg in STATE_OF.items():
        if st != 60: z[st] = sum(z[r] for r in rg)
    z[1] = sum(z[s] for s in (2, 15, 26, 40, 49, 56, 60)); return z
base_land = {int(r['regionId']): {k: float(r[k]) for k in ('cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1', 'totalArea')} for r in rd('data/2025-organic/default-inputs-short-term.csv')} if os.path.exists(os.path.join(ROOT, 'data/2025-organic')) else {int(r['regionId']): {k: float(r[k]) for k in ('cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1', 'totalArea')} for r in rd('data/2025-population/default-inputs-short-term.csv')}
def land_variant(vid, label, **overrides):
    land, zp = {}, {}
    for z, b in base_land.items():
        n = {**b, **{k: v[z] for k, v in overrides.items() if z in v}}
        n['nonAg'] = max(0.0, n['totalArea'] - n['cropping'] - n['pasture'] - n['infrastr1'] - n['nature1'])
        land[z] = {k: round(n[k]) for k in ('cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1')}
        share = round(n['nature1'] / n['totalArea'], 2); zp[z] = {'short': {'nature2': share}, 'long': {'nature2': max(0.30, share)}}
    variants.append({'id': vid, 'group': 'land', 'label': label, 'land': land, 'zonePresets': zp})
land_variant('land_res_11', 'reserve = class 1.1 only (nature conservation)', nature1=zone_total(lambda z: area(z, ('1.1',))))
land_variant('land_res_125', 'reserve = classes 1.1 and 1.2.5 (conservation and Indigenous uses)', nature1=zone_total(lambda z: area(z, ('1.1', '1.2.5'))))
CROP, GRAZE = ('3.3', '3.4', '3.5', '3.6', '4.3', '4.4', '4.5', '4.6'), ('2.1', '3.2', '4.2')
land_variant('land_raster', 'cropping and pasture measured on the land-use raster instead of the ABS holdings', cropping=zone_total(lambda z: area(z, CROP)), pasture=zone_total(lambda z: area(z, GRAZE)))
land_variant('land_infra', 'infrastructure measured on the raster (classes 5.3 to 5.7, 5.9) instead of 730 m2 a person', infrastr1=zone_total(lambda z: area(z, ('5.3', '5.4', '5.5', '5.6', '5.7', '5.9'))))

# ---- diet and consumption ------------------------------------------------------------------------------------------------------------------
def pv(vid, group, label, short=None, long=None): variants.append({'id': vid, 'group': group, 'label': label, 'presets': {'short': short or {}, 'long': long or {}}})
pv('diet_meat_13', 'diet and consumption', 'meat and egg share back at 13% (no change since 2011)', {'meategg': 0.13})
pv('diet_meat_up', 'diet and consumption', 'meat and egg share 12.5% (one step above the proxy)', {'meategg': 0.125})
pv('diet_meat_dn', 'diet and consumption', 'meat and egg share 11.5% (one step below the proxy)', {'meategg': 0.115})
pv('diet_red_64', 'diet and consumption', 'red meat share back at 64% (no change since 2011)', {'redmeat': 0.64})
pv('diet_red_up', 'diet and consumption', 'red meat share 62.8% (5 points above the proxy)', {'redmeat': 0.628})
pv('diet_red_dn', 'diet and consumption', 'red meat share 52.8% (5 points below the proxy)', {'redmeat': 0.528})
pv('diet_both_2011', 'diet and consumption', 'both diet shares at 2011 (13% and 64%)', {'meategg': 0.13, 'redmeat': 0.64})
pv('cons_fuel_etc', 'diet and consumption', 'fuel, biofuel and timber at 2011 values (2520 L, 0.5%, 1 m3)', {'fuel': 2520, 'biofuel': 0.005, 'timber': 1.0})
# ---- organic -------------------------------------------------------------------------------------------------------------------------------
ws = xlrd.open_workbook(os.path.join(ROOT, 'model/model.xls')).sheet_by_name('Yield')
rows808 = [r + 1 for r in range(3, 138) if abs(ws.cell_value(r, 6) - 0.8083) < 0.001]
of = json.load(open(os.path.join(ROOT, 'data/2025/organic_factors.json')))['crops']
variants.append({'id': 'org_f2011', 'group': 'organic', 'label': 'organic factors of the five crops back at 2011 values', 'modelCells': {f"G{v['yield_sheet_row']}": v['factor_2011'] for v in of.values()}})
variants.append({'id': 'org_kniss', 'group': 'organic', 'label': 'organic factors of the five crops at the commercial ratios of Kniss et al. alone', 'modelCells': {f"G{v['yield_sheet_row']}": v['kniss_2016'] for v in of.values()}})
variants.append({'id': 'org_def_lo', 'group': 'organic', 'label': 'default organic factor 0.771 (lower end of Ponisio et al. 2015) on the %d rows that use it' % len(rows808), 'modelCells': {f'G{r}': 0.771 for r in rows808}})
variants.append({'id': 'org_def_hi', 'group': 'organic', 'label': 'default organic factor 0.845 (upper end of Ponisio et al. 2015)', 'modelCells': {f'G{r}': 0.845 for r in rows808}})
variants.append({'id': 'org_base_2', 'group': 'organic', 'label': 'organic baseline left at 2% (the constant in Yield!E2 not moved) with the 7% default', 'modelCells': {'E2': '=Settings!B15-0.02'}})
variants.append({'id': 'org_share_2', 'group': 'organic', 'label': 'organic default share 2% and baseline 2% (no change since 2011)', 'presets': {'short': {'organic': 0.02}, 'long': {}}, 'modelCells': {'E2': '=Settings!B15-0.02'}})
variants.append({'id': 'org_share_12', 'group': 'organic', 'label': 'organic default share and baseline 12% (the share of agricultural land the 2026 report gives)', 'presets': {'short': {'organic': 0.12}, 'long': {}}, 'modelCells': {'E2': '=Settings!B15-0.12'}})
json.dump(variants, open(os.path.join(WORK, 'variants.json'), 'w'), indent=1)
print(len(variants), 'variants written to', os.path.join(WORK, 'variants.json'))
