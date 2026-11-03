#!/usr/bin/env python3
"""Second source for the improved-pasture share, by zone: the ABS 2007-08 'improved pasture' and 'other grazing land' as a share of the area of holding, by NRM region (the 2011 model's own data,
models archive Yield data/NRM07-08/land use07-08.xls; column number = zone id). Compares it with the CLUM-based share used by the dairy-good-land module (data/2025/pasture_quality_by_zone.csv) and re-derives the observed milk yield on
improved pasture on the ABS basis. Why: CLUM classes 0.15% of Queensland's pasture as modified pasture (Queensland's own land-use layer agrees: 1,502 km2 of 'Grazing modified pastures'), which the ABS contradicts
(23% of Queensland's holdings improved pasture, 24.5% of its grazing land).
Usage: python3 -I analysis/pasture_2025/abs_improved_check.py XLS          (repository root; needs xlrd). Writes data/2025/abs_improved_pasture_2007_08_by_zone.csv."""
import sys, csv, xlrd, os
wb = xlrd.open_workbook(sys.argv[1]); sh = wb.sheet_by_index(0)
num = lambda v: v if isinstance(v, float) else None
rows = {}
for c in range(1, 61):
    imp, oth = num(sh.cell_value(2, c)), num(sh.cell_value(3, c))
    rows[c] = dict(zone=c, name=sh.cell_value(0, c), holding_000ha=num(sh.cell_value(1, c)), improved_pct_of_holding=imp, other_grazing_pct_of_holding=oth,
                   abs_improved_share_of_grazing=round(((imp or 0) / ((imp or 0) + oth)), 4) if oth else 0.0)
q = {int(r['zone']): r for r in csv.DictReader(open('data/2025/pasture_quality_by_zone.csv'))}
g = {int(r['zone']): r for r in csv.DictReader(open('data/2025/dairy_good_land_by_zone.csv'))}
for z, r in rows.items():
    r['clum_improved_share'] = g[z]['improved_share'] if z in g else ''
    r['pasture_km2_model'] = g[z]['pasture_km2'] if z in g else ''
with open('data/2025/abs_improved_pasture_2007_08_by_zone.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[1].keys())); w.writeheader(); w.writerows(rows.values())
STATE = {2: range(3, 15), 15: range(16, 26), 26: range(27, 40), 40: range(41, 49), 49: range(50, 56), 56: range(57, 60)}
print('state     pasture km2   CLUM improved   ABS 2007-08 improved (km2, share of grazing)')
tot_clum = tot_abs = 0
for s, ch in list(STATE.items()) + [(60, [60])]:
    zs = [s] if s == 60 else list(ch)
    p = sum(float(g[z]['pasture_km2']) for z in zs); cl = sum(float(g[z]['improved_km2']) for z in zs)
    ab = sum(float(g[z]['pasture_km2']) * rows[z]['abs_improved_share_of_grazing'] for z in zs)
    tot_clum += cl; tot_abs += ab
    print(f"{rows[s]['name']:8} {p:12,.0f} {cl:12,.0f} ({cl / p:5.1%}) {ab:12,.0f} ({ab / p:5.1%})")
print(f'total   {"":12} {tot_clum:12,.0f} {"":9} {tot_abs:12,.0f}')
# observed milk per m2 of ABS-improved pasture, regions holding 90% of the milk (as pasture_quality.py)
reg = [z for z in range(1, 61) if z not in (1, 2, 15, 26, 40, 49, 56, 60)]
milk = {z: float(q[z]['milk_tonnes_2025'] or 0) for z in reg}; tm = sum(milk.values())
impA = {z: float(g[z]['pasture_km2']) * rows[z]['abs_improved_share_of_grazing'] for z in reg}
cand = sorted([z for z in reg if impA[z] > 0 and milk[z] > 0], key=lambda z: -milk[z]); acc = 0; sel = []
for z in cand:
    sel.append(z); acc += milk[z]
    if acc >= 0.9 * tm: break
print(f'ABS basis: zones holding 90% of the milk: {len(sel)}; milk per m2 of improved pasture {sum(milk[z] for z in sel) / sum(impA[z] for z in sel):.1f} g/m2 (all regions {tm / sum(impA[z] for z in reg):.1f}); CLUM basis 73')
