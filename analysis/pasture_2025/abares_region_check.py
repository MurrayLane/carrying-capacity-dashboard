#!/usr/bin/env python3
"""Does the model's beef per hectare agree with ABARES at the level of regions? (SCOPE.md E1.)
Usage: python3 -I analysis/pasture_2025/abares_region_check.py FDP_REGIONAL_CSV OUT.csv          (repository root; FDP_REGIONAL_CSV = fdp-regional-historical.csv, models archive Livestock/ABARES-NT-WA/; needs the built data)
ABARES region: beef receipts per hectare operated (all broadacre farms of the region, mean 2017 to 2023). Model: the cattle meat yield of the matching zones (pasture-area weighted), kg per hectare, in releases 2025-diet (before the regional beef
module) and 2025-improved (after). Both are shown relative to the first pair, QLD West and South West. The matching of ABARES regions to the model's NRM zones is approximate and listed here."""
import csv, json, sys
src, out = sys.argv[1:3]
D = {}
for x in csv.DictReader(open(src, encoding='utf-8-sig')):
    try: D[(x['ABARES region'], int(x['Year']), x['Variable'])] = float(x['Value'])
    except ValueError: pass
avg = lambda r, v: (lambda a: sum(a) / len(a) if a else None)([D[(r, y, v)] for y in range(2017, 2024) if (r, y, v) in D])
PAIRS = [('QLD West and South West', [32, 37]), ('QLD Cape York and the Gulf', [30, 35, 38]), ('QLD Charleville - Longreach', [32]), ('QLD Central North', [28]), ('SA Northern Pastoral', [46]), ('WA Pilbara and Central Pastoral', [52]), ('WA The Kimberley', [52]),
         ('NT Alice Springs Districts', [60]), ('NT Barkly Tablelands', [60]), ('NT Victoria River District - Katherine', [60]), ('NSW Far West', [14, 8]), ('NSW Tablelands (Northern Central and Southern)', [13, 4]), ('VIC Southern and Eastern Victoria', [17, 24]), ('TAS Tasmania', [57, 59])]
load = lambda rel: json.load(open(f'web/public/data/{rel}/regions.json'))
A, B = load('2025-improved'), load('2025-diet'); k = A['yieldRows'].index(98); rows = [['abares_region', 'model_zones', 'receipts_per_ha', 'model_kg_per_ha_before', 'model_kg_per_ha_after', 'receipts_relative', 'model_relative_after']]; base = None
for r, zs in PAIRS:
    rc, a = avg(r, 'Beef cattle receipts ($)'), avg(r, 'Area operated at 30 June (ha)')
    if not rc: continue
    w = [A['regions'][str(z)]['land']['pasture'] for z in zs]
    my = lambda R: sum(R['regions'][str(z)]['yield'][k] * 10 * wi for z, wi in zip(zs, w)) / sum(w)
    after, before = my(A), my(B); base = base or (rc / a, after)
    rows.append([r, '+'.join(map(str, zs)), round(rc / a, 1), round(before, 1), round(after, 1), round(rc / a / base[0], 2), round(after / base[1], 2)])
csv.writer(open(out, 'w', newline='')).writerows(rows); [print(x) for x in rows]
