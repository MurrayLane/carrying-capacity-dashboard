#!/usr/bin/env python3
"""Paper A, sections 3 and 9: which regions moved between under and over capacity between 2011 and 2025 (corrected method), and which of those flips are real.
Usage (repository root): python3 -I analysis/paper_a/regional_flips.py   (reads analysis/comparison_2025/movers.csv and results/ranges_2025-fixed.csv; writes regional_flips.csv)

The 53 regions (52 NRM regions and the Northern Territory), short and long term, corrected method (2011-fixed against 2025-fixed). A flip is a change in the sign of (population - capacity).
Three tests of whether a flip is a finding: (1) the land-definition and boundary flags of movers.csv (the capacity change is mostly the land layer or an older 2011 boundary: land_only_ratio outside 0.5 to 2, or the five older 2011 zones);
(2) robust to the 2025 uncertainty range: the 2025 status holds across the 5th to 95th percentile of the Monte Carlo draws (2011 results have no ranges, their inputs were not sampled);
(3) both. 'Clean and robust' flips are the ones Paper A may report."""
import csv
movers = list(csv.DictReader(open('analysis/comparison_2025/movers.csv')))
rg = {(r['zone'], r['setting']): r for r in csv.DictReader(open('results/ranges_2025-fixed.csv'))}
out = [['zone', 'name', 'state', 'term', 'population 2011', 'population 2025', 'capacity 2011', 'capacity 2025', 'over 2011', 'over 2025', 'flip', 'artefact flag', '2025 status robust to the range', 'clean and robust', 'older 2011 boundary flag']]
for m in movers:
    k = (m['zone'], m['preset']); r = rg.get(k)
    p25 = float(m['pop2025']); over25 = int(m['over2025'])
    robust = ''
    if r:
        p5, p95 = float(r['p5']), float(r['p95'])
        robust = 'yes' if ((over25 and p95 < p25) or ((not over25) and p5 > p25)) else 'no'
    flip = 'over to under' if int(m['over2011']) and not over25 else ('under to over' if (not int(m['over2011'])) and over25 else '')
    art = 'land definition' if m['land_definition_effect_flag'] else ('older 2011 boundary' if m['boundary_older_2011'] else '')
    out.append([m['zone'], m['name'], m['state'], m['preset'], m['pop2011'], m['pop2025'], m['cap2011'], m['cap2025'], m['over2011'], m['over2025'], flip, art, robust, 'yes' if flip and not art and robust == 'yes' else ('' if not flip else 'no'), 'older 2011 boundary' if m['boundary_older_2011'] else ''])
csv.writer(open('analysis/paper_a/regional_flips.csv', 'w', newline='')).writerows(out)
for term in ('short', 'long'):
    rows = [r for r in out[1:] if r[3] == term]; fl = [r for r in rows if r[10]]
    print(term, 'regions:', len(rows), ' over capacity 2011:', sum(int(r[8]) for r in rows), ' 2025:', sum(int(r[9]) for r in rows), ' flips:', len(fl))
    for r in fl: print('  ', r[1], '|', r[10], '| artefact:', r[11] or '-', '| robust:', r[12], '| clean and robust:', r[13])
    print('  clean and robust:', sum(1 for r in fl if r[13] == 'yes'), ' artefact:', sum(1 for r in fl if r[11]), ' not robust:', sum(1 for r in fl if r[12] == 'no'))
