#!/usr/bin/env python3
"""Milk per hectare of the land dairy farms actually use, by state: the 'known yield' for the dairy-good-land module (replaces the milk per m2 of improved pasture, which mixed dairy with beef and sheep pasture and
rested on a land-use layer that cannot find dairy land in Queensland: analysis/pasture_2025/README.md).
Usage: python3 -I analysis/pasture_2025/dairy_farm_yield.py          (repository root). Writes data/2025/dairy_farm_yield_by_state.csv and data/2025/dairy_farm_yield_by_zone.csv.
Figures are copied from the sources below (read from the PDFs on 2026-11-03; page figures where the text layer was unreadable, read from the page image):
 * Milk volume and farm numbers by state, 2025 (financial year): Dairy Australia, Farm business production 2025 (states), from Levies Revenue Services.
 * Milk solids sold per usable hectare (kg MS/ha), 'Whole farm analysis, Physical parameters', Dairy Farm Monitor Project annual reports (Dairy Australia, state agencies): Victoria 2024-25 (Northern Victoria 1,053,
   South West Victoria 585, Gippsland 890), NSW 2024-25 (state 702), South Australia 2024-25 (581), Western Australia 2024-25 (445), Tasmania 2023-24 (1,120; the 2024-25 report was not found).
   Usable area = hectares managed less land of no value to livestock (house, sheds); it includes the milking platform, the young stock and the farm's own forage and crop land; it excludes land that grows purchased feed.
 * Queensland: the Queensland Dairy Accounting Scheme 2025 (QDAS, 2024-25, 55 farms): milk per farm and usable area per farm in four groups (South Queensland grazing 13 farms, PMR 21, TMR 9, North Queensland grazing and PMR 12).
 * Litres per kg MS: the state's own labour-efficiency pair (litres/FTE over kg MS/FTE) in its report where it was read (Tasmania 12.13, South Australia 13.21, Western Australia 13.72); 13.3 elsewhere (Victoria, NSW).
 * Milk density 1.03 kg a litre. Homegrown feed as a share of metabolisable energy consumed (the share of the herd's feed grown on the usable area): Victoria 53 to 62%, NSW 55%, SA 50%, WA 62%, Tasmania 58%."""
import csv, os
LKG_DEFAULT = 13.3; DENS = 1.03
MILK_ML = {'NSW': 1090, 'VIC': 5407, 'QLD': 277, 'SA': 416, 'WA': 331, 'TAS': 927}; FARMS = {'NSW': 429, 'VIC': 2573, 'QLD': 244, 'SA': 160, 'WA': 108, 'TAS': 279}
# Victoria: Dairy Australia regions give the milk of Gippsland (1,871 ML) and Western Victoria (1,907); the rest of Victoria's 5,407 ML is taken as the Murray (northern) region.
vic_milk = {'GIPPS': 1871, 'SWV': 1907}; vic_milk['NV'] = MILK_ML['VIC'] - sum(vic_milk.values())
vic_kgms = {'GIPPS': 890, 'SWV': 585, 'NV': 1053}
vic_state_kgms = sum(vic_milk.values()) / sum(vic_milk[r] / vic_kgms[r] for r in vic_milk)           # milk-weighted harmonic mean: total milk over total usable hectares
KGMS = {'NSW': (702, 13.3), 'VIC': (vic_state_kgms, 13.3), 'SA': (581, 13.21), 'WA': (445, 13.72), 'TAS': (1120, 12.13)}
HOMEGROWN = {'NSW': 0.55, 'VIC': (53 * vic_milk['NV'] + 59 * vic_milk['SWV'] + 62 * vic_milk['GIPPS']) / MILK_ML['VIC'] / 100, 'SA': 0.50, 'WA': 0.62, 'TAS': 0.58}
# QDAS 2024-25 groups: (farms, milk L per farm, usable ha per farm)
qd = [(13, 1190807, 229), (21, 1731955, 238), (9, 3104792, 595), (12, 1614240, 277)]
qld_l_ha = sum(n * m for n, m, a in qd) / sum(n * a for n, m, a in qd)
rows = []
for s in ['NSW', 'VIC', 'QLD', 'SA', 'WA', 'TAS']:
    if s == 'QLD': l_ha = qld_l_ha; src = 'QDAS 2025 (55 farms: milk per farm over usable area per farm, farm-weighted)'; kgms = ''; hg = ''
    else:
        k, lkg = KGMS[s]; l_ha = k * lkg; kgms = round(k, 1); hg = round(HOMEGROWN[s], 3); src = 'DFMP annual report ' + ('2023-24' if s == 'TAS' else '2024-25')
    t_ha = l_ha * DENS / 1000
    rows.append(dict(state=s, milk_ML_2025=MILK_ML[s], farms_2025=FARMS[s], kgMS_per_usable_ha=kgms, homegrown_feed_share=hg, milk_litres_per_ha=round(l_ha), milk_t_per_ha=round(t_ha, 2), milk_g_per_m2=round(t_ha * 100, 1),
                     usable_area_km2=round(MILK_ML[s] * 1e6 / l_ha / 100, 0), source=src))
tot_area = sum(r['usable_area_km2'] for r in rows); tot_milk = sum(r['milk_ML_2025'] for r in rows)
nat = tot_milk * 1e6 * DENS / (tot_area * 1e6) * 1e3 / 1e3        # g/m2: litres * 1.03 kg / m2
nat_g = tot_milk * 1e6 * DENS * 1000 / (tot_area * 1e6)
rows.append(dict(state='AUS', milk_ML_2025=tot_milk, farms_2025=sum(FARMS.values()), kgMS_per_usable_ha='', homegrown_feed_share='', milk_litres_per_ha=round(tot_milk * 1e6 / (tot_area * 100)), milk_t_per_ha=round(nat_g / 100, 2),
                 milk_g_per_m2=round(nat_g, 1), usable_area_km2=tot_area, source='milk-weighted over the six states; the Northern Territory has no commercial dairy industry and takes this value'))
os.makedirs('data/2025', exist_ok=True)
with open('data/2025/dairy_farm_yield_by_state.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
# zones: a zone takes its state's yield; the national row and the Northern Territory take the milk-weighted national yield
Y = {r['state']: r['milk_g_per_m2'] for r in rows}
STATE_OF = {1: 'AUS', 60: 'AUS'}
for st, rng in {'NSW': [2] + list(range(3, 15)), 'VIC': [15] + list(range(16, 26)), 'QLD': [26] + list(range(27, 40)), 'SA': [40] + list(range(41, 49)), 'WA': [49] + list(range(50, 56)), 'TAS': [56] + list(range(57, 60))}.items():
    for z in rng: STATE_OF[z] = st
names = {int(r['regionId']): r['regionName'] for r in csv.DictReader(open('data/2025-land/default-inputs-short-term.csv'))}
with open('data/2025/dairy_farm_yield_by_zone.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['zone', 'name', 'state', 'milk_g_per_m2'])
    for z in sorted(names): w.writerow([z, names[z], STATE_OF[z], Y[STATE_OF[z]]])
for r in rows: print(f"{r['state']:4} milk {r['milk_ML_2025']:6} ML  farms {r['farms_2025']:5}  {r['milk_litres_per_ha']:6,} L/ha = {r['milk_g_per_m2']:7.1f} g/m2  usable area {r['usable_area_km2']:8,.0f} km2   {r['source'][:60]}")
