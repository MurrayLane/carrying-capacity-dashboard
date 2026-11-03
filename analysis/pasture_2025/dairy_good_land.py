#!/usr/bin/env python3
"""Per-zone land for the dairy-good-land method module: the share of each zone's pasture that is improved pasture (CLUM modified or irrigated pasture) and the share that is improved pasture
with arable capability (improved pasture times the GAEZ arable share of the SA2). Dairy is placed on good land = cropland + the arable improved pasture (Murray 2026-11-03).
Usage: python3 -I analysis/pasture_2025/dairy_good_land.py          (repository root)
Shares, not areas, are written, so they apply to the pasture of a zone in any release (the 2011 zones carry the thesis's land, the 2025 zones the 2020-21 land). SA2 to zone allocation as in
pasture_quality.py (total area share of the NRM pieces). State rows are pasture-weighted from their regions (the Northern Territory is its own zone); the national row from the states.
Writes data/2025/dairy_good_land_by_zone.csv: zone, name, pasture_km2, improved_km2, arable_improved_km2, improved_share, arable_improved_share (a=GAEZ, wheat, barley, rapeseed), arable_improved_share_broad (GAEZ, any field crop incl. sorghum, maize, sugar cane, cotton, soy, sunflower, groundnut); the bounds are 0 and improved_share."""
import csv, json, collections, os
ROOT = os.getcwd(); rd = lambda p: list(csv.DictReader(open(os.path.join(ROOT, p))))
imp = {r['sa2_code']: (float(r['pasture_km2']), float(r['improved_km2'])) for r in rd('data/sa2/improved_pasture_by_sa2.csv')}
ar = {r['sa2_code']: float(r['arable_share_gaez'] or 0) for r in rd('data/sa2/arable_share_gaez_by_sa2.csv')}
ar2 = {r['sa2_code']: float(r['arable_share_gaez'] or 0) for r in rd('data/sa2/arable_share_gaez_broad_by_sa2.csv')}      # any field crop incl. the tropical ones (sensitivity)
ZONE_OF = {int(c): int(z) for z, codes in json.load(open('pipeline/land/zone_to_nrm2011.json'))['zones'].items() for c in codes}
tot = collections.defaultdict(lambda: collections.defaultdict(float))
for r in rd('data/nrm2011/land_use_by_sa2_nrm2011_piece.csv'):
    n = int(r['nrmr_code_2011'])
    if n in ZONE_OF: tot[r['zone_name']][ZONE_OF[n]] += float(r['km2'])
P, I, A, A2 = (collections.defaultdict(float) for _ in range(4))
for s, d in tot.items():
    if s not in imp: continue
    T = sum(d.values()); p, i = imp[s]
    for z, v in d.items(): P[z] += p * v / T; I[z] += i * v / T; A[z] += i * ar.get(s, 0.0) * v / T; A2[z] += i * ar2.get(s, 0.0) * v / T
CHILDREN = {2: range(3, 15), 15: range(16, 26), 26: range(27, 40), 40: range(41, 49), 49: range(50, 56), 56: range(57, 60)}
for st, ch in CHILDREN.items():
    for D in (P, I, A, A2): D[st] = sum(D[c] for c in ch)
for D in (P, I, A, A2): D[1] = sum(D[s] for s in (2, 15, 26, 40, 49, 56, 60))
names = {int(r['regionId']): r['regionName'] for r in rd('data/2025-land/default-inputs-short-term.csv')}
with open('data/2025/dairy_good_land_by_zone.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['zone', 'name', 'pasture_km2', 'improved_km2', 'arable_improved_km2', 'improved_share', 'arable_improved_share', 'arable_improved_share_broad'])
    for z in sorted(names):
        w.writerow([z, names[z], round(P[z], 1), round(I[z], 1), round(A[z], 1), round(I[z] / P[z], 4) if P[z] else 0, round(A[z] / P[z], 4) if P[z] else 0, round(A2[z] / P[z], 4) if P[z] else 0])
print(f"national: pasture {P[1]:,.0f} km2, improved {I[1]:,.0f} ({I[1] / P[1] * 100:.1f}%), arable improved {A[1]:,.0f} ({A[1] / I[1] * 100:.0f}% of improved)")
