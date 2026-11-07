#!/usr/bin/env python3
"""The methods side by side on common Australian data (Paper B, section 5, figure 2): each method's reading of Australia's capacity on current data, read from the outputs of the individual tests,
and the model's own entry (baseline and improved) from results/.
Usage (repository root): python3 -I analysis/method_tests_2025/cross_method.py   (reads the outputs of the other scripts in this folder, results/ and analysis/comparators_2025/rerun.csv; writes cross_method.csv and model_entry.csv)"""
import csv, collections
D = 'analysis/method_tests_2025/'
def rows(path): return list(csv.reader(open(path)))
# --- the model's own entry
def zone1(path, preset): return next(r for r in csv.DictReader(open(path)) if r['zone'] == '1' and r['preset'] == preset)
def rng(path, setting): r = next(r for r in csv.DictReader(open(path)) if r['zone'] == '1' and r['setting'] == setting); return float(r['p5']) / 1e6, float(r['p95']) / 1e6
R = collections.defaultdict(dict)
for row in rows('analysis/comparators_2025/rerun.csv')[1:]:
    rel, variant, setting, cap = row[0], ','.join(row[1:-2]), row[-2], float(row[-1])
    if variant.startswith('R1'): R[rel][int(setting)] = cap
entry = [['release', 'method tier', 'short term (million)', 'short term, 5th to 95th percentile', 'long term (million)', 'long term, 5th to 95th percentile', 'worst of 10 years', 'worst of 100 years', 'population (million)']]
for rel, tier in (('2025-mirror', 'thesis method as built, errors kept'), ('2025-fixed', 'thesis method, corrected (the baseline entry)'), ('2025-improved', 'improved (built on)')):
    s, l = zone1(f'results/{rel}.csv', 'short'), zone1(f'results/{rel}.csv', 'long')
    ss, ll = rng(f'results/ranges_{rel}.csv', 'short'), rng(f'results/ranges_{rel}.csv', 'long')
    entry.append([rel, tier, round(float(s['capacity']) / 1e6, 1), '%.1f to %.1f' % ss, round(float(l['capacity']) / 1e6, 1), '%.1f to %.1f' % ll, R[rel][10], R[rel][100], round(float(s['population']) / 1e6, 1)])
csv.writer(open(D + 'model_entry.csv', 'w', newline='')).writerows(entry)
# --- each method's reading
hg = {r[0]: r for r in rows(D + 'henry_godden_summary.csv') if r and r[0].startswith(('production as it is', 'in-use land', "Henry and Godden's 1990-91"))}
hg_vals = [float(x) for r in hg.values() for x in (r[3], r[4]) if x not in ('',)]
sf = {r[1]: r[2] for r in rows(D + 'simpson_food.csv') if r[0] == '2021-23'}
half = {r[1]: r for r in rows(D + 'half_index.csv') if r[0] == '2021-23'}
land = {}
for r in csv.DictReader(open(D + 'half_landuse.csv')):
    if r['Area'] == 'Australia' and r['Year'] in ('2021', '2022', '2023') and r['Item'] in ('Cropland', 'Permanent meadows and pastures'): land.setdefault(r['Item'], []).append(float(r['Value']))
ag = sum(sum(v) / len(v) for v in land.values()) / 1000                                  # Mha
half_cap = ag / float(half['Australia'][2])
cas = next(r for r in rows(D + 'cassidy.csv') if r[0] == '2021-23' and r[1] == 'Australia')
fp = {r[0] + '|' + r[1]: r for r in rows(D + 'foran_poldy_balance.csv')}
fe = next(r for r in rows(D + 'fearnside_failure_curve.csv') if r[0] == '2025-fixed')
fix = next(r for r in entry if r[0] == '2025-fixed'); imp = next(r for r in entry if r[0] == '2025-improved')
cm = [['method', 'asks', 'counts', 'what it leaves out', 'reading for Australia on current data (million people)', 'low', 'high', 'fidelity check against its authors']]
cm.append(['Energy and protein balance (Gifford; Henry and Godden)', 'how many could the food energy and protein of production feed', 'calories and protein of production, exports as food, scaled to a land base', 'the diet, the pasture and crop pairing, waste',
           '%.0f to %.0f' % (min(hg_vals), max(hg_vals)), min(hg_vals), max(hg_vals), 'recipe reproduces 109 and 96 from their totals'])
cm.append(['Ecological footprint, food row (Simpson)', 'how much land does the diet appropriate (a capacity only by division)', 'crop and pasture land at world-average productivity', 'productivity of the actual land, pairing, energy land not set against Australian land',
           '%.0f to %.0f' % (float(sf['people the cropland supports at this footprint (million)']), float(sf['people, crop plus pasture together (million)'])), float(sf['people the cropland supports at this footprint (million)']), float(sf['people, crop plus pasture together (million)']), 'pasture 1.2% lower, feed crop 3.6% higher; plant-food crop not reproduced'])
cm.append(['HALF index (Alexander)', 'how much land would the world need if all ate this diet (a capacity only by division)', 'land at world-average production, by diet', 'productivity of the actual land, pairing', '%.0f' % half_cap, round(half_cap), round(half_cap), 'Australia within 0.8%, world within 2.1%, US and Argentina within 5%, India within 8%; New Zealand not reproduced'])
cm.append(['People per hectare (Cassidy)', 'how many people do the crops deliver per hectare', 'cropland calories delivered after feed and biofuel, exports by importers\' use', 'grazing, protein, a balanced diet', '%.0f' % float(cas[10]) + ' (about 190 on all cropland)', float(cas[10]), 190.0, 'world, India, China and Brazil calorie shares within a few points; the US feed share lower (ethanol since 2000); levels 22 to 42% higher (years)'])
cm.append(['Commodity balance (Foran and Poldy)', 'does production cover the human requirement item by item', 'tonnes of grain, meat and fish against a requirement per person', 'land, weather, diet change', '40 to 41 (meat), 12 to 17 (fish), 127 to 128 (grain with feed grain)', 12, 41, 'production within 1.3%; their balance and the 30 and 77 readings reproduced'])
cm.append(['Failure probability (Fearnside)', 'at what density does the chance of failure exceed an acceptable level', 'the harvest in a year of given probability against the diet', 'one criterion; weather as one factor on all yields', '%.1f (average year) to %.1f (1 in 100)' % (float(fe[2]), float(fe[7])), float(fe[7]), float(fe[2]), 'none possible (Brazilian data); idea applied'])
cm.append(['The model, thesis method corrected', 'how many does the land feed on a stated diet, with pasture and crops paired', 'land, yields, diet, waste, fuel, fibre, reserve', 'trade, variability between years beyond the allowance', '%s (%s)' % (fix[2], fix[3]), float(fix[3].split(' to ')[0]), float(fix[3].split(' to ')[1]), 'the baseline entry'])
cm.append(['The model, improved', 'as above, Australian settings', 'as above', 'as above', '%s (%s)' % (imp[2], imp[3]), float(imp[3].split(' to ')[0]), float(imp[3].split(' to ')[1]), 'built on'])
csv.writer(open(D + 'cross_method.csv', 'w', newline='')).writerows(cm)
for r in entry: print(r)
print()
for r in cm: print(r[0], '|', r[4], '|', r[5], r[6])
print('HALF capacity reading: agricultural land %.1f Mha / %s ha per person = %.0f' % (ag, half['Australia'][2], half_cap))
