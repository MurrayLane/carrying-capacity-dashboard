#!/usr/bin/env python3
"""Improved (modified or irrigated) pasture by SA2 and zone, and the observed milk output per km2 of improved pasture (Murray 2026-11-03: dairy only on land that can support it at its known yield).
Usage: python3 -I analysis/pasture_2025/pasture_quality.py          (repository root)
Improved pasture share of an SA2: CLUM classes 3.2.x (grazing modified pastures) and 4.2.x (irrigated modified pastures) over those plus 2.1.0 (grazing native vegetation), applied to the model's pasture area
of the SA2 (ABS grazing land, data/sa2/land_2011_method_by_sa2.csv). Zone areas by the SA2 to zone allocation (total area share of the NRM pieces); milk by zone: the 2010 archive figure times the change of the
state's milk (Dairy Australia, data/2025/livestock_national_series.csv; mean of 2022-23 to 2024-25 over 2009-10). Writes data/sa2/improved_pasture_by_sa2.csv and data/2025/pasture_quality_by_zone.csv."""
import csv, json, collections, os
ROOT = os.getcwd(); rd = lambda p: list(csv.DictReader(open(os.path.join(ROOT, p))))
MOD = {'320', '321', '322', '323', '324', '325', '420', '421', '422', '423', '424'}; NAT = {'210'}
mod, nat = collections.defaultdict(float), collections.defaultdict(float)
for r in rd('data/sa2/land_use_by_sa2.csv'):
    if r['class_code'] in MOD: mod[r['sa2_code']] += float(r['km2'])
    elif r['class_code'] in NAT: nat[r['sa2_code']] += float(r['km2'])
land = {r['sa2_code']: r for r in rd('data/sa2/land_2011_method_by_sa2.csv')}
frac = {s: (mod[s] / (mod[s] + nat[s]) if mod[s] + nat[s] > 0 else 0.0) for s in land}
with open('data/sa2/improved_pasture_by_sa2.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['sa2_code', 'pasture_km2', 'improved_share_clum', 'improved_km2'])
    for s, r in land.items(): w.writerow([s, round(float(r['pasture_km2']), 3), round(frac[s], 4), round(frac[s] * float(r['pasture_km2']), 3)])
natP = sum(float(r['pasture_km2']) for r in land.values()); natI = sum(frac[s] * float(land[s]['pasture_km2']) for s in land)
print(f'national: pasture {natP:,.0f} km2, improved {natI:,.0f} km2 ({natI / natP * 100:.1f}%); CLUM modified {sum(mod.values()):,.0f} km2 against native {sum(nat.values()):,.0f}')
# SA2 -> zone allocation by total area of the NRM pieces
ZONE_OF = {}
for z, codes in json.load(open('pipeline/land/zone_to_nrm2011.json'))['zones'].items():
    for c in codes: ZONE_OF[c] = int(z)
tot = collections.defaultdict(lambda: collections.defaultdict(float))
for r in rd('data/nrm2011/land_use_by_sa2_nrm2011_piece.csv'):
    n = int(r['nrmr_code_2011'])
    if n in ZONE_OF: tot[r['zone_name']][ZONE_OF[n]] += float(r['km2'])
zone_impr = collections.defaultdict(float); zone_past = collections.defaultdict(float)
for s, d in tot.items():
    if s not in land: continue
    T = sum(d.values())
    for z, v in d.items(): zone_impr[z] += frac[s] * float(land[s]['pasture_km2']) * v / T; zone_past[z] += float(land[s]['pasture_km2']) * v / T
# milk by zone
base = json.load(open('pipeline/yields/archive_livestock_inputs.json'))['years']['2010']['regions']
ser = {r['series']: r for r in rd('data/2025/livestock_national_series.csv')}
def ratio(key):
    r = ser.get(key);
    if not r: return 1.0
    return (sum(float(r[y]) for y in ('2022-23', '2023-24', '2024-25')) / 3) / float(r['2009-10'])
STATE_KEY = {1: 'milk_NSW', 2: 'milk_Vic', 3: 'milk_Qld', 4: 'milk_SA', 5: 'milk_WA', 6: 'milk_Tas'}
state_of = {}
for code, zs in {1: range(3, 15), 2: range(16, 26), 3: range(27, 40), 4: range(41, 49), 5: range(50, 56), 6: range(57, 60), 7: [60]}.items():
    for z in zs: state_of[z] = code
for z, code in {2: 1, 15: 2, 26: 3, 40: 4, 49: 5, 56: 6, 60: 7}.items(): state_of[z] = code
names = {int(r['regionId']): r['regionName'] for r in rd('data/2025-land/default-inputs-short-term.csv')}
rows = []
for z in sorted(base, key=int):
    z = int(z)
    if z == 1: continue
    mk = (base[str(z)].get('milkTonnes') or 0) * ratio(STATE_KEY.get(state_of.get(z), ''))
    rows.append(dict(zone=z, name=names.get(z, ''), state=state_of.get(z, ''), pasture_km2=round(zone_past.get(z, 0), 1), improved_km2=round(zone_impr.get(z, 0), 1), improved_share=round(zone_impr.get(z, 0) / zone_past[z], 4) if zone_past.get(z) else '', milk_tonnes_2025=round(mk), milk_g_per_m2_improved=round(mk * 1e6 / (zone_impr[z] * 1e6), 2) if zone_impr.get(z, 0) > 0 and mk else ''))
with open('data/2025/pasture_quality_by_zone.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
reg = [r for r in rows if r['zone'] not in (2, 15, 26, 40, 49, 56, 60)]
top = sorted([r for r in reg if r['milk_tonnes_2025']], key=lambda r: -r['milk_tonnes_2025'])
tm = sum(r['milk_tonnes_2025'] for r in reg); print(f'regions: milk {tm / 1e6:.2f} Mt (Dairy Australia national about 8 to 9 Mt)')
print('zone                         state  milk kt  improved km2  pasture km2  improved share  milk g per m2 of improved pasture')
for r in top[:14]: print(f"{r['name'][:28]:28} {r['state']!s:>3} {r['milk_tonnes_2025'] / 1e3:8.0f} {r['improved_km2']:12.0f} {r['pasture_km2']:12.0f} {r['improved_share']!s:>14} {r['milk_g_per_m2_improved']!s:>12}")
dz = [r for r in top if r['milk_g_per_m2_improved'] != '']; acc = 0; sel = []
for r in dz:
    sel.append(r); acc += r['milk_tonnes_2025']
    if acc >= 0.9 * tm: break
print(f'zones holding 90% of the milk: {len(sel)}; their milk per m2 of improved pasture (production-weighted): {sum(r["milk_tonnes_2025"] for r in sel) / sum(r["improved_km2"] for r in sel):.1f} g/m2 (all regions {tm / sum(r["improved_km2"] for r in reg):.1f})')
