#!/usr/bin/env python3
"""B137 (X116): the land_only_ratio of movers.csv rebuilt on the corrected tier. movers.csv is NOT edited; this writes a new file beside it.
Usage (repository root): python3 -I analysis/comparison_2025/movers_land_ratio_corrected.py
movers.csv carries cap2011, cap2025 and the statuses on the corrected method but land_only_ratio from the published-method decomposition (capacity_by_cause.csv: land-only capacity over 2011 capacity).
The corrected value here is (capacity 2011 + the land layer's forward-walk effect) / capacity 2011, from capacity_by_cause_corrected.csv (the corrected walk of decompose_corrected.mjs).
Flag rule, as movers.csv: land_only_ratio below 0.5 or above 2 (land_definition_effect_flag); the same rule at 0.4 and 2.5 is added (R05a issue 3, R04b question 7).
Writes analysis/comparison_2025/movers_land_ratio_corrected.csv (106 rows: 53 regions, both presets) and prints the summary the X116 row quotes. Checks: the published column of movers.csv is reproduced from capacity_by_cause.csv; cap2011 agrees with the corrected csv."""
import csv, statistics, sys
O = 'analysis/comparison_2025/'
mv = list(csv.DictReader(open(O + 'movers.csv')))
pub = {(r['zone'], r['preset']): r for r in csv.DictReader(open(O + 'capacity_by_cause.csv'))}
cor = {(r['zone'], r['preset']): r for r in csv.DictReader(open(O + 'capacity_by_cause_corrected.csv'))}
fl = lambda x, lo, hi: 'yes' if (x < lo or x > hi) else ''
out = [['zone', 'name', 'preset', 'land_only_ratio_published_method', 'land_only_ratio_corrected_tier', 'difference', 'flag_0.5_2_published', 'flag_0.5_2_corrected', 'flag_0.4_2.5_published', 'flag_0.4_2.5_corrected']]
bad = []
for r in mv:
    k = (r['zone'], r['preset']); p, c = pub[k], cor[k]
    a = float(p['land_only']) / float(p['capacity_2011']); b = (float(c['capacity_2011']) + float(c['land_only'])) / float(c['capacity_2011'])
    if round(a, 2) != float(r['land_only_ratio']): bad.append(('published column not reproduced', r['name'], r['preset']))
    if int(c['capacity_2011']) != int(r['cap2011']): bad.append(('cap2011 differs', r['name'], r['preset']))
    out.append([r['zone'], r['name'], r['preset'], f'{a:.4f}', f'{b:.4f}', f'{b - a:+.4f}', fl(a, .5, 2), fl(b, .5, 2), fl(a, .4, 2.5), fl(b, .4, 2.5)])
if bad: sys.exit('CHECK FAILED: ' + str(bad[:5]))
csv.writer(open(O + 'movers_land_ratio_corrected.csv', 'w', newline='')).writerows(out)
body = out[1:]
for p in ('short', 'long'):
    rows = [x for x in body if x[2] == p]; n = len(rows)
    print(p, 'median published', round(statistics.median(float(x[3]) for x in rows), 3), 'corrected', round(statistics.median(float(x[4]) for x in rows), 3),
          '| flagged at 0.5/2 published', sum(bool(x[6]) for x in rows), 'corrected', sum(bool(x[7]) for x in rows), '| at 0.4/2.5 published', sum(bool(x[8]) for x in rows), 'corrected', sum(bool(x[9]) for x in rows), 'of', n)
big = [x for x in body if abs(float(x[5])) >= 0.005 and x[2] == 'short']
print('short-term regions whose ratio differs by 0.005 or more:', [(x[1], x[3], x[4]) for x in big])
print('flag changes at 0.5/2:', [(x[1], x[2]) for x in body if x[6] != x[7]], '| at 0.4/2.5:', [(x[1], x[2]) for x in body if x[8] != x[9]])
