#!/usr/bin/env python3
"""Re-derives the long-term liquid fuel default (the thesis's 253 L a person) from current sector energy use, with the thesis's own method and cuts.
Usage: python3 -I analysis/fuel_sectors_2025/sector_derivation.py TABLE_F_XLSX          (repository root; TABLE_F_XLSX = carrying-capacity-models/Energy data/australian_energy_statistics_2025_table_f.xlsx)
Writes sectors.csv (petajoules by sector: the thesis's 2008 figures, Table F 2007-08 and 2023-24) and scenarios.csv (litres a person).

The thesis method (archive: prelim models/non-food resource data.xls, sheet biofuel): the year's total liquid fuel in litres (347 million barrels of oil and 294 million litres of biofuel in 2008, 55.46 billion litres)
divided by the population (June 2008, 21.5 million) gives litres a person (2,580); that is shared out by each sector's share of the energy used (Energy in Australia, PJ); the agriculture share is scaled by population / short-term capacity to
leave out the fuel used to grow exported food (2,580 less 58.8 = 2,521 L, the dashboard default); each sector is then kept at a share (agriculture 80%, road, rail, water, other industry 10%, mining 5%, air 0.1%,
lubricants and bitumen 5%); the sum is the long-term default (253 L).
Sector mapping to Table F (checked against the thesis's 2008 figures; LPG is left out, as the thesis does): agriculture = Div. A; road, rail, air = blocks 46, 47, 49; water = Div. I less road, rail, air and other transport
(recent editions report water transport fuel only inside Div. I); mining = Div. B; other industry = Div. C less petroleum refining (1701) and 1709, plus construction, commercial and services, residential; lubricants, bitumen and solvents held at the thesis's
63.8 PJ (Table F stopped reporting bitumen and solvents after 2007-08).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from table_f import load, LIQUID
ROOT = os.getcwd(); yrs, d = load(sys.argv[1]); NOLPG = [f for f in LIQUID if f != 'LPG']
PJ_L = 28.408131496                                                     # million litres a petajoule, as in the thesis sheet
def pj(b, y, rows=NOLPG): i = yrs.index(y); return sum(d[b].get(f, [0] * len(yrs))[i] for f in rows)
def sectors(y):
    road, rail, air, other = (pj(b, y) for b in ('46 Road transport', '47 Rail transport', '49 Air transport', '50-53 Other transport, services and storage'))
    return {'Agriculture': pj('Div. A Agriculture, forestry and fishing', y), 'Road transport': road, 'Rail transport': rail, 'Air transport': air,
            'Water transport': pj('Div. I Transport, postal & warehousing', y) - road - rail - air - other, 'Mining': pj('Div. B Mining', y),
            'Other industry, construction, commercial, residential': pj('Div. C Manufacturing', y) - pj('1701 Petroleum refining', y) - pj('1709 Other petroleum and coal product manufacturing', y)
                 + pj('Div. E Construction', y) + pj('Commercial and services a', y) + pj('Residential', y), 'Lubricants, bitumen, solvents': 63.8}
THESIS = {'Agriculture': 86.9, 'Road transport': 1003.3, 'Rail transport': 34.1, 'Air transport': 230.3, 'Water transport': 60.3, 'Mining': 114.3, 'Other industry, construction, commercial, residential': 182.7, 'Lubricants, bitumen, solvents': 63.8}
KEEP = {'Agriculture': 0.8, 'Road transport': 0.10, 'Rail transport': 0.10, 'Air transport': 0.001, 'Water transport': 0.10, 'Mining': 0.05, 'Other industry, construction, commercial, residential': 0.10, 'Lubricants, bitumen, solvents': 0.05}
s07, s24 = sectors('2007-08'), sectors('2023-24')
with open(os.path.join(ROOT, 'analysis/fuel_sectors_2025/sectors.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['sector', 'thesis_2008_PJ', 'table_f_2007_08_PJ', 'table_f_2023_24_PJ', 'share_kept_long_term']); [w.writerow([k, THESIS[k], round(s07[k], 1), round(s24[k], 1), KEEP[k]]) for k in THESIS]
POP24 = 27.19e6; CAP = 48.0e6                                          # ABS estimated resident population at 30 June 2024; short-term capacity of release 2025-organic
TOTAL24 = None
for r in csv.DictReader(open(os.path.join(ROOT, 'analysis/liquid_fuel_2025/fuel_trend.csv'))):
    if r['year_to_june'] == '2024': TOTAL24 = float(r['all_products_ML']) * 1e6              # all petroleum products sold in the year to June 2024 (Australian Petroleum Statistics), litres
def derive(sect, total_l, pop, domestic, keep=KEEP, road_override=None):
    """-> (litres a person today after removing fuel for exported food, long-term litres a person); road_override = long-term PJ for the road sector."""
    tot_pj = sum(sect.values()); per_p = total_l / pop; today = 0.0; lt = 0.0
    for k, v in sect.items():
        share = v / tot_pj; l = share * per_p * (domestic if k == 'Agriculture' else 1); today += l
        lt += (road_override / tot_pj * per_p if road_override is not None and k == 'Road transport' else l * keep[k])
    return today, lt
rows = [['scenario', 'population_million', 'litres_a_person_today', 'litres_a_person_long_term', 'note']]
t0, l0 = derive(THESIS, 55.46259e9, 21.4985e6, 0.534); rows.append(['thesis as published (2008)', 21.5, round(t0), round(l0, 1), 'reproduces the 2,521 and 253 L of the sheet'])
dom = POP24 / CAP
road = s24['Road transport']; rd = d['46 Road transport']; j = yrs.index('2023-24'); road_diesel = rd['Diesel'][j]; road_petrol = rd['Auto gasoline-unleaded'][j] + rd['Auto gasoline-leaded'][j]
t1, l1 = derive(s24, TOTAL24, POP24, dom); rows.append(['thesis method, 2023-24', 27.19, round(t1), round(l1, 1), 'same cuts; agriculture scaled by population / short-term capacity; total from the Australian Petroleum Statistics'])
t2, l2 = derive(s24, TOTAL24, POP24, dom, road_override=0.10 * road_diesel); rows.append(['road: petrol electrified, diesel kept at 10%', 27.19, round(t2), round(l2, 1), 'light vehicles electric; diesel for heavy vehicles cut as in the thesis'])
t3, l3 = derive(s24, TOTAL24, POP24, dom, road_override=0.0); rows.append(['road: fully electric', 27.19, round(t3), round(l3, 1), 'no liquid fuel on the road'])
k5 = dict(KEEP); k5['Road transport'] = 0.05; t4, l4 = derive(s24, TOTAL24, POP24, dom, keep=k5); rows.append(['road at 5% (the thesis text), 2023-24', 27.19, round(t4), round(l4, 1), 'the text says roads and mining are cut 95%'])
rows = [[str(c).replace(',', ';') for c in r] for r in rows]                       # no commas inside fields, so the node script can split on commas
with open(os.path.join(ROOT, 'analysis/fuel_sectors_2025/scenarios.csv'), 'w', newline='') as f: csv.writer(f).writerows(rows)
print(f'{"sector":55s}{"thesis":>8s}{"07-08":>8s}{"23-24":>8s}'); [print(f'{k:55s}{THESIS[k]:8.1f}{s07[k]:8.1f}{s24[k]:8.1f}') for k in THESIS]
print(f'road 2023-24: petrol {road_petrol:.0f} PJ, diesel {road_diesel:.0f} PJ; total 2023-24 {TOTAL24 / 1e9:.1f} billion litres'); [print(r) for r in rows]
