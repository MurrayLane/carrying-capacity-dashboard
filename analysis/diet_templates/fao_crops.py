#!/usr/bin/env python3
"""FAO yields of tropical staples (SCOPE.md E16): yield (kg/ha), area and production, 2019-2023, with the FAO flags, for the Pacific countries and Australia.
Usage: python3 -I analysis/diet_templates/fao_crops.py CSV OUT.csv      (CSV: Production_Crops_Livestock_E_Oceania.csv from https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_Oceania.zip)
Flags: A official figure, E estimated (FAO's own estimate; no official figure), I imputed, M missing."""
import csv, statistics, sys
src, out = sys.argv[1:3]
ITEMS = ['Taro', 'Yams', 'Cassava, fresh', 'Sweet potatoes', 'Bananas', 'Plantains and cooking bananas', 'Coconuts, in shell', 'Oil palm fruit', 'Sugar cane']
AREAS = ['Papua New Guinea', 'Fiji', 'Vanuatu', 'Solomon Islands', 'Samoa', 'Tonga', 'Australia']
YEARS = ['Y2019', 'Y2020', 'Y2021', 'Y2022', 'Y2023']
rows = list(csv.DictReader(open(src, encoding='latin-1'))); w = csv.writer(open(out, 'w', newline=''))
w.writerow(['country', 'item', 'yield_kg_per_ha_2019_23_mean', 'area_ha_2023', 'production_t_2023', 'flags_2019_23', 'official_years'])
for a in AREAS:
    for it in ITEMS:
        by = {r['Element']: r for r in rows if r['Area'] == a and r['Item'] == it}
        y = by.get('Yield')
        if not y: continue
        vals = [float(y[k]) for k in YEARS if y[k] not in ('', None)]; fl = ''.join((y.get(k + 'F') or '-') for k in YEARS)
        if not vals: continue
        ar, pr = by.get('Area harvested'), by.get('Production')
        w.writerow([a, it, round(statistics.mean(vals)), round(float(ar['Y2023'])) if ar and ar['Y2023'] else '', round(float(pr['Y2023'])) if pr and pr['Y2023'] else '', fl, fl.count('A')])
print('wrote', out)
