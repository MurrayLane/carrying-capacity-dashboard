#!/usr/bin/env python3
"""The methods side by side on common Australian data (Paper B, section 5, figure 2): each method's reading of Australia's capacity on current data, read from the outputs of the individual tests,
and the model's own entry (baseline and improved) from results/.
Usage (repository root): python3 -I analysis/method_tests_2025/cross_method.py   (reads the outputs of the other scripts in this folder, published_values.csv, second_build_values.csv (the independent rebuilds' figures, V04 and V05),
results/ and analysis/comparators_2025/rerun.csv; writes cross_method.csv and model_entry.csv). Every reading, low and high, and every fidelity text is built from those files; nothing is typed."""
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
# --- each method's reading, read from its output; the second builds' figures from second_build_values.csv; fidelity texts built from the numbers
import math, re
PUB = {(r['table'], r['row'], r['column']): float(r['value']) for r in csv.DictReader(open(D + 'published_values.csv'))}
SB = {(r['method'], r['quantity']): float(r['value']) for r in csv.DictReader(open(D + 'second_build_values.csv'))}
def sb(method, start): return next(v for (m, q), v in SB.items() if m == method and q.startswith(start))
def gap(a, b): return (a / b - 1) * 100                                                   # %, rebuilt over published
def within1(g): return '%.1f' % abs(g)                                                   # one gap, one decimal
def within0(*gs): return '%d' % math.ceil(max(abs(g) for g in gs) - 1e-9)                 # several gaps, whole percent, rounded up
NEAR = 5.0                                                                                # a reconstruction within 5% counts as reproduced
def lowhigh(g): return ('%.1f%% low' if abs(g) < 10 else '%.0f%% low') % abs(g) if g < 0 else ('%.1f%% high' if abs(g) < 10 else '%.0f%% high') % g
def two_builds(name, g1, g2):
    ok = [abs(g) <= NEAR for g in (g1, g2)]
    if all(ok): return f'{name} reproduced by both builds'
    if not any(ok): return f'{name} not reproduced by either'
    gin, gout = (g1, g2) if ok[0] else (g2, g1)
    return f'{name} matched by one reading ({lowhigh(gin)}) and not the other ({lowhigh(gout)})'
# Henry and Godden: the 243 row (plain 8.8 MJ requirement) is left out by this filter; the reading is the three land-base scenarios
hg = {r[0]: r for r in rows(D + 'henry_godden_summary.csv') if r and r[0].startswith(('production as it is', 'in-use land', "Henry and Godden's 1990-91"))}
hg_vals = [float(x) for r in hg.values() for x in (r[3], r[4]) if x not in ('',)]
hg_chk = next(r for r in rows(D + 'henry_godden_summary.csv') if r and r[0].startswith('Henry and Godden 1990-91 totals'))
hg_pub = next(r for r in rows(D + 'henry_godden_summary.csv') if r and r[0] == 'published Table 5')
hg_ok = all(round(float(a)) == round(float(b)) for a, b in zip(hg_chk[1:3], hg_pub[1:3]))
hg_fid = 'recipe %s %s and %s from their totals' % ('reproduces' if hg_ok else 'does not reproduce', hg_pub[1], hg_pub[2])
# Simpson: this build from simpson_food.csv, the second build from second_build_values.csv
sf = {r[1]: float(r[2]) for r in rows(D + 'simpson_food.csv')[1:] if r[0] == '2021-23'}
sf91 = {r[1]: float(r[2]) for r in rows(D + 'simpson_food.csv')[1:] if r[0] == '1991-92'}
s_crop = (sb('simpson_food', 'people the cropland'), sf['people the cropland supports at this footprint (million)'])
s_both = (sb('simpson_food', 'people, crop plus pasture'), sf['people, crop plus pasture together (million)'])
s_lo, s_hi = round(min(s_crop + s_both)), round(max(s_crop + s_both))
s_read = '%d to %d (cropland-bound reading %d to %d; crop and pasture together %d to %d; two readings of an unstated pasture rule)' % (
    s_lo, s_hi, round(min(s_crop)), round(max(s_crop)), round(min(s_both)), round(max(s_both)))
feed91 = sum(v for k, v in sf91.items() if k.startswith('crop: feed for'))
T = 'simpson_fidelity'; C = 'Simpson (ha a person)'
s_fid = '; '.join([
    two_builds('feed crop', gap(feed91, PUB[(T, 'Crop land for animal products (feed)', C)]), gap(sb('simpson_food', 'crop land for animal products'), PUB[(T, 'Crop land for animal products (feed)', C)])),
    two_builds('pasture', gap(sf91['pasture total'], PUB[(T, 'Pasture (beef, sheep, milk)', C)]), gap(sb('simpson_food', 'pasture'), PUB[(T, 'Pasture (beef, sheep, milk)', C)])),
    two_builds('plant-food crop', gap(sf91['crop land total'] - feed91, PUB[(T, 'Crop land for plant foods', C)]), gap(sb('simpson_food', 'crop land for plant foods'), PUB[(T, 'Crop land for plant foods', C)]))])
# HALF
half = {r[1]: r for r in rows(D + 'half_index.csv') if r[0] == '2021-23'}
half11 = {r[1]: float(r[5]) for r in rows(D + 'half_index.csv')[1:] if r[0] == '2011'}
land = {}
for r in csv.DictReader(open(D + 'half_landuse.csv')):
    if r['Area'] == 'Australia' and r['Year'] in ('2021', '2022', '2023') and r['Item'] in ('Cropland', 'Permanent meadows and pastures'): land.setdefault(r['Item'], []).append(float(r['Value']))
ag = sum(sum(v) / len(v) for v in land.values()) / 1000                                  # Mha
crop_mha = sum(land['Cropland']) / len(land['Cropland']) / 1000
half_cap = ag / float(half['Australia'][2])
T = 'half_fidelity'; C = 'Paper (HALF, % of world land)'
hgap = {k: gap(half11[c], PUB[(T, k, C)]) for k, c in (('World', 'World'), ('United States', 'United States of America'), ('India', 'India'), ('Argentina', 'Argentina'), ('Australia', 'Australia'), ('New Zealand', 'New Zealand'))}
half_fid = 'Australia within %s%%, world within %s%%, US and Argentina within %s%%, India within %s%%; New Zealand %s' % (
    within1(hgap['Australia']), within1(hgap['World']), within0(hgap['United States'], hgap['Argentina']), within0(hgap['India']),
    'not reproduced' if abs(hgap['New Zealand']) > 10 else 'within %s%%' % within0(hgap['New Zealand']))
# Cassidy: this build from cassidy.csv, the second build from second_build_values.csv
cas = {r[1]: r for r in rows(D + 'cassidy.csv') if r[0] == '2021-23'}
c_del, c_ppl, c_mha = float(cas['Australia'][9]), float(cas['Australia'][10]), float(cas['Australia'][2])
c_del2, c_ppl2 = sb('cassidy', "Australia 2021-23, people per ha delivered"), sb('cassidy', "Australia 2021-23, people per ha delivered") * sb('cassidy', "Australia 2021-23, cropland")
c_all = c_ppl / c_mha * crop_mha                                                          # this build's rate on all cropland
c_read = '%.1f to %.1f people a hectare delivered; %d to %d million (about %d on all cropland)' % (
    min(c_del, c_del2), max(c_del, c_del2), round(min(c_ppl, c_ppl2)), round(max(c_ppl, c_ppl2)), round(c_all, -1))
c_aus = max(abs(gap(float(cas['Australia'][8]), sb('cassidy', 'Australia 2021-23, people per ha produced'))), abs(gap(c_del, c_del2)))
c_wld = max(abs(gap(float(cas['World'][8]), sb('cassidy', 'World 2021-23, people per ha produced'))), abs(gap(float(cas['World'][9]), sb('cassidy', 'World 2021-23, people per ha delivered'))))
c_fid = "world and Australia within %d%% to %d%% between two builds; the export-allocation choice moves Australia up to %s a hectare" % (
    round(min(c_aus, c_wld)), round(max(c_aus, c_wld)), sb('cassidy', 'export-allocation'))
# Foran and Poldy
fp = rows(D + 'foran_poldy_balance.csv')[1:]
def num(s): return float(re.findall(r'[\d.]+', s.rsplit(':', 1)[-1])[0])
def fpv(item_start, value_start): return num(next(r[1] for r in fp if r[0].startswith(item_start) and r[1].startswith(value_start)))
f_meat = (fpv('capacity reading 2021-23, their', 'meat'), fpv('capacity reading 2021-23, actual', 'meat'))
f_fish = (fpv('capacity reading 2021-23, their', 'fish'), fpv('capacity reading 2021-23, actual', 'fish'))
f_grain = (fpv('capacity reading 2021-23, their', 'grain with'), fpv('capacity reading 2021-23, actual', 'grain with'))
rg = lambda p: '%d to %d' % (min(p), max(p))
f_read = '%s (meat), %s (fish), %s (grain with feed grain)' % (rg(f_meat), rg(f_fish), rg(f_grain))
f_lo, f_hi = round(min(f_meat + f_fish)), round(max(f_meat + f_fish))
prod = [float(x) for x in re.findall(r'[\d.]+', next(r[1] for r in fp if r[0].startswith('fidelity: FAO 1997-98')))]
f_prod = max(abs(gap(prod[0], prod[1])), abs(gap(prod[2], prod[3])))
bal = dict(re.findall(r'(grain|meat|fish) ([\d.]+)', next(r[1] for r in fp if r[0].startswith('fidelity: their balance'))))
bal_ok = float(bal['grain']) > 1 and float(bal['meat']) > 1 and float(bal['fish']) < 1             # their conclusion: positive except fish
cr = next(r for r in fp if r[0].startswith('fidelity: capacity reading on 1997-98'))
m30, g77 = float(re.search(r'meat (\d+)', cr[1]).group(1)), float(re.search(r'grain with feed grain (\d+)', cr[1]).group(1))
reg = [float(x) for x in re.findall(r'\d+', cr[2])]                                       # the register's 30 to 32 and 76 to 80
read_ok = reg[0] <= m30 <= reg[1] and reg[2] <= g77 <= reg[3]
f_fid = 'production within %s%%; their balance %s and the %d and %d readings %s' % (
    within1(f_prod), '' if bal_ok else 'not reproduced', m30, g77, 'reproduced' if read_ok else 'not reproduced')
f_fid = f_fid.replace('balance  and', 'balance and')
fe = next(r for r in rows(D + 'fearnside_failure_curve.csv') if r[0] == '2025-fixed')
fix = next(r for r in entry if r[0] == '2025-fixed'); imp = next(r for r in entry if r[0] == '2025-improved')
cm = [['method', 'asks', 'counts', 'what it leaves out', 'reading for Australia on current data (million people)', 'low', 'high', 'fidelity check against its authors']]
cm.append(['Energy and protein balance (Gifford; Henry and Godden)', 'how many could the food energy and protein of production feed', 'calories and protein of production, exports as food, scaled to a land base', 'the diet, the pasture and crop pairing, waste',
           '%.0f to %.0f' % (min(hg_vals), max(hg_vals)), min(hg_vals), max(hg_vals), hg_fid])
cm.append(['Ecological footprint, food row (Simpson)', 'how much land does the diet appropriate (a capacity only by division)', 'crop and pasture land at world-average productivity', 'productivity of the actual land, pairing, energy land not set against Australian land',
           s_read, s_lo, s_hi, s_fid])
cm.append(['HALF index (Alexander)', 'how much land would the world need if all ate this diet (a capacity only by division)', 'land at world-average production, by diet', 'productivity of the actual land, pairing', '%.0f' % half_cap, round(half_cap), round(half_cap), half_fid])
cm.append(['People per hectare (Cassidy)', 'how many people do the crops deliver per hectare', 'cropland calories delivered after feed and biofuel, exports by importers\' use', 'grazing, protein, a balanced diet', c_read, round(min(c_ppl, c_ppl2)), int(round(c_all, -1)), c_fid])
cm.append(['Commodity balance (Foran and Poldy)', 'does production cover the human requirement item by item', 'tonnes of grain, meat and fish against a requirement per person', 'land, weather, diet change', f_read, f_lo, f_hi, f_fid])
cm.append(['Failure probability (Fearnside)', 'at what density does the chance of failure exceed an acceptable level', 'the harvest in a year of given probability against the diet', 'one criterion; weather as one factor on all yields',
           '%.1f (average year), %.1f (1 in 10), %.1f (1 in 100)' % (float(fe[2]), float(fe[4]), float(fe[7])), float(fe[7]), float(fe[2]), 'none possible (Brazilian data); idea applied'])
cm.append(['The model, thesis method corrected', 'how many does the land feed on a stated diet, with pasture and crops paired', 'land, yields, diet, waste, fuel, fibre, reserve', 'trade, variability between years beyond the allowance', '%s (%s)' % (fix[2], fix[3]), float(fix[3].split(' to ')[0]), float(fix[3].split(' to ')[1]), 'the baseline entry'])
cm.append(['The model, improved', 'as above, Australian settings', 'as above', 'as above', '%s (%s)' % (imp[2], imp[3]), float(imp[3].split(' to ')[0]), float(imp[3].split(' to ')[1]), 'built on'])
csv.writer(open(D + 'cross_method.csv', 'w', newline='')).writerows(cm)
for r in entry: print(r)
print()
for r in cm: print(r[0], '|', r[4], '|', r[5], r[6])
print('HALF capacity reading: agricultural land %.1f Mha / %s ha per person = %.0f' % (ag, half['Australia'][2], half_cap))
