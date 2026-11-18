#!/usr/bin/env python3
"""B137 item 1: Table 2 of Paper A with land and livestock as ONE layer (the eight-layer game), national, both presets, average over all 8! = 40,320 orderings with the forward and reverse walks.
Usage (repository root): python3 -I analysis/comparison_2025/make_eight_layer_table.py
Reads  analysis/comparison_2025/capacity_by_cause_corrected_orders.csv (B111; game eight_layers_land_livestock_one), results/2011-fixed.csv, results/2011-fixed-3.csv, results/2025-fixed.csv
Writes analysis/comparison_2025/decomposition_eight_layer_table.csv          (national table, as Table 2)
       analysis/comparison_2025/decomposition_eight_layer_regional_counts.csv (which layer is largest, by region, on the average, the forward walk and the reverse walk)
Checks (the script stops if one fails): the eight averages sum to the change within 3 people; forward and reverse sum to the change exactly; capacity 2011 plus the change equals capacity 2025;
2011-fixed and 2011-fixed-3 give the same national capacity; the largest-layer counts over the nine-layer game reproduce the B111 report (26 land and 25 livestock short term)."""
import csv, collections, sys
O = 'analysis/comparison_2025/'
rows = list(csv.DictReader(open(O + 'capacity_by_cause_corrected_orders.csv')))
res = lambda rel: {(r['zone'], r['preset']): r for r in csv.DictReader(open(f'results/{rel}.csv'))}
r11, r113, r25 = res('2011-fixed'), res('2011-fixed-3'), res('2025-fixed')
G8, G9 = 'eight_layers_land_livestock_one', 'nine_layers'
LABEL = {'land_and_livestock': 'Land and livestock together (one layer)', 'infrastructure_land_only': 'Infrastructure land that follows population', 'crop_yields_only': 'Crop yields',
         'consumption_only': 'Consumption (without the organic share)', 'organic_update_only': 'Organic update', 'resilience_update_only': 'Resilience table', 'fuel_update_only': 'Long-term liquid fuel',
         'red_meat_mix_only': 'Red meat mix of the diet'}
g = {(r['game'], r['zone'], r['preset'], r['layer']): r for r in rows}
fails = []
def need(ok, msg):
    if not ok: fails.append(msg)
out = [['row', 'short_average', 'short_forward', 'short_reverse', 'long_average', 'long_forward', 'long_reverse']]
cap = lambda d: [int(d[('1', p)]['capacity']) for p in ('short', 'long')]
c11, c25 = cap(r11), cap(r25); need(cap(r113) == c11, '2011-fixed and 2011-fixed-3 differ nationally')
out.append(['Capacity 2011 (2011-fixed)'] + [c11[0]] * 3 + [c11[1]] * 3)
for L in LABEL:
    line = [LABEL[L]]
    for p in ('short', 'long'):
        r = g[(G8, '1', p, L)]; line += [int(r['shapley_mean']), int(r['forward']), int(r['reverse'])]
    out.append(line)
out.append(['Capacity 2025 (2025-fixed)'] + [c25[0]] * 3 + [c25[1]] * 3)
for j, p in enumerate(('short', 'long')):
    change = c25[j] - c11[j]; tot = g[(G8, '1', p, 'total_change')]; need(int(tot['forward']) == change, f'total change {p}')
    for col in ('shapley_mean', 'forward', 'reverse'):
        s = sum(int(g[(G8, '1', p, L)][col]) for L in LABEL); need(abs(s - change) <= (3 if col == 'shapley_mean' else 0), f'{p} {col} sums to {s}, change {change}')
out.append(['Change in capacity, 2011 to 2025'] + [c25[0] - c11[0]] * 3 + [c25[1] - c11[1]] * 3)
out.append(['Share of the short-term change: land and livestock; consumption plus red meat mix (%)', f"{100*int(g[(G8,'1','short','land_and_livestock')]['shapley_mean'])/(c25[0]-c11[0]):.0f}; {100*(int(g[(G8,'1','short','consumption_only')]['shapley_mean'])+int(g[(G8,'1','short','red_meat_mix_only')]['shapley_mean']))/(c25[0]-c11[0]):.0f}", '', '', '', '', ''])
pop = lambda d, p: float(d[('1', p)]['population']) / float(d[('1', p)]['capacity'])
out.append(['People over capacity, 2011', f"{pop(r11,'short'):.3f}", '', '', f"{pop(r11,'long'):.3f}", '', ''])
out.append(['People over capacity, 2025', f"{pop(r25,'short'):.3f}", '', '', f"{pop(r25,'long'):.3f}", '', ''])
# regional counts: a region is any of the 53 zones that are not Australia or a state zone (zone 60, the Northern Territory, counts as a region)
STATE = {'1', '2', '15', '26', '40', '49', '56'}
zones = sorted({r['zone'] for r in rows} - STATE, key=int); need(len(zones) == 53, 'region count')
def largest(game, zone, p, col):
    cand = [r for r in rows if r['game'] == game and r['zone'] == zone and r['preset'] == p and r['layer'] not in ('total_change', 'land_and_livestock' if game == G9 else '')]
    return max(cand, key=lambda r: abs(float(r[col])))['layer']
cnt = [['game', 'preset', 'walk', 'layer', 'regions_where_largest', 'regions_total']]
tab = {}
for game in (G8, G9):
    for p in ('short', 'long'):
        for walk, col in (('average', 'shapley_mean'), ('forward', 'forward'), ('reverse', 'reverse')):
            c = collections.Counter(largest(game, z, p, col) for z in zones); tab[(game, p, walk)] = {z: largest(game, z, p, col) for z in zones}
            for L, n in sorted(c.items(), key=lambda kv: -kv[1]): cnt.append([game, p, walk, L, n, len(zones)])
need(collections.Counter(tab[(G9, 'short', 'average')].values())['land_only'] == 26 and collections.Counter(tab[(G9, 'short', 'average')].values())['livestock_only'] == 25, 'nine-layer counts do not reproduce B111')
for game in (G8, G9):
    for p in ('short', 'long'):
        for walk in ('forward', 'reverse'):
            d = sum(tab[(game, p, walk)][z] != tab[(game, p, 'average')][z] for z in zones); cnt.append([game, p, walk, f'regions where the {walk} walk names a different largest layer from the average', d, len(zones)])
if fails: sys.exit('CHECK FAILED: ' + '; '.join(fails))
csv.writer(open(O + 'decomposition_eight_layer_table.csv', 'w', newline='')).writerows(out)
csv.writer(open(O + 'decomposition_eight_layer_regional_counts.csv', 'w', newline='')).writerows(cnt)
for r in out: print(r)
for r in cnt:
    if r[0] == G8: print(r)
print('all checks passed')
