#!/usr/bin/env python3
"""GAEZ v4 attainable yields of the tropical staples for northern Australia and the Pacific (SCOPE.md E16 / E12).
Usage: python3 -I analysis/gaez_2025/gaez_yields.py [DIR_WITH_TIFS]       (repository root; needs numpy and tifffile; downloads the GeoTIFFs if DIR is empty)

Source: FAO/IIASA GAEZ v4 theme 4 (res05), climate 1981-2010 (CRUTS 3.2 historical), high input level, with CO2 fertilisation, variable yxH{r,a} =
'average attainable yield of the best occurring suitability class in the grid cell' (all land, not only today's cropland), r rainfed, a irrigated; 5 arc minute grid.
https://gaez.fao.org ; files https://s3.eu-west-1.amazonaws.com/data.gaezdev.aws.fao.org/res05/CRUTS32/Hist/8110H/yxHr_<crop>.tif
Units: kg dry weight per hectare (the User's Guide); sugarcane in kg sugar, oil palm in kg oil. Fresh weight = dry weight / (1 - moisture), moisture from AUSNUT 2023 (below).
Output: gaez_yields.csv, one row per region and crop; the validation against FAO yields of the Pacific countries is in gaez_vs_fao.csv."""
import os, sys, csv, urllib.request
import numpy as np, tifffile
D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tifs')
os.makedirs(D, exist_ok=True)
CROPS = {'csv': 'Cassava', 'spo': 'Sweet potato', 'yam': 'Yam', 'ban': 'Banana', 'con': 'Coconut', 'olp': 'Oil palm', 'suc': 'Sugarcane'}
MOIST = {'csv': 0.620, 'spo': 0.760, 'yam': 0.689, 'ban': 0.758}       # AUSNUT 2023 raw peeled: cassava 62.0, sweet potato 76 (orange 81.0, white 71.1), taro 68.9 used for yam (no AUSNUT yam), Cavendish banana 75.8
REG = {                                                          # lon_min, lon_max, lat_min, lat_max (land cells with a value >= 0 only)
    'Northern Territory Top End': (129.0, 137.0, -16.0, -11.0),
    'Kimberley (WA)': (124.0, 129.5, -18.5, -13.5),
    'Cape York and north Queensland coast': (141.5, 146.5, -19.5, -10.5),
    'Papua New Guinea (mainland and islands)': (141.0, 156.0, -11.5, -1.0),
    'Fiji': (177.0, 180.0, -19.5, -16.0),
    'Vanuatu': (166.5, 170.5, -20.5, -13.0),
    'Solomon Islands': (155.5, 162.5, -11.5, -6.5)}
BASE = 'https://s3.eu-west-1.amazonaws.com/data.gaezdev.aws.fao.org/res05/CRUTS32/Hist/8110H/'
def load(v, c):
    f = os.path.join(D, f'{v}_{c}.tif')
    if not os.path.exists(f): urllib.request.urlretrieve(f'{BASE}{v}_{c}.tif', f)
    return tifffile.imread(f).astype(float)
def box(a, b):                                                    # 5 arc minute grid: column = (lon + 180) * 12, row = (90 - lat) * 12
    lo, hi, la0, la1 = b; return a[int((90 - la1) * 12):int((90 - la0) * 12), int((lo + 180) * 12):int((hi + 180) * 12)]
rows = [['region', 'crop', 'water', 'land_cells', 'share_suitable', 'mean_dw_kg_ha', 'p90_dw_kg_ha', 'mean_fresh_t_ha', 'p90_fresh_t_ha', 'unit']]
RES = {}
for c, name in CROPS.items():
    for v, water in (('yxHr', 'rainfed'), ('yxHa', 'irrigated')):
        a = load(v, c)
        for r, b in REG.items():
            x = box(a, b); land = x[x >= 0]
            if not land.size: continue
            s = land[land > 0]
            m = float(s.mean()) if s.size else 0.0; p = float(np.percentile(s, 90)) if s.size else 0.0
            f = 1 / (1 - MOIST[c]) if c in MOIST else None
            unit = 'kg sugar/ha' if c == 'suc' else 'kg oil/ha' if c == 'olp' else 'kg DW/ha' + (' (fresh weight by AUSNUT moisture)' if f else ' (no fresh conversion)')
            RES[(r, c, water)] = (m * f / 1000 if f else None)
            rows.append([r, name, water, int(land.size), round(s.size / land.size, 3), round(m), round(p), round(m * f / 1000, 1) if f else '', round(p * f / 1000, 1) if f else '', unit])
csv.writer(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gaez_yields.csv'), 'w', newline='')).writerows(rows)
# validation against FAO yields (actual, 2019-23 mean; analysis/diet_templates/tropical_crops_fao.csv)
FAO = {}
for r in csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../diet_templates/tropical_crops_fao.csv'))):
    FAO[(r['country'], r['item'])] = float(r['yield_kg_per_ha_2019_23_mean']) / 1000
MAP = {'csv': 'Cassava, fresh', 'spo': 'Sweet potatoes', 'yam': 'Yams', 'ban': 'Bananas'}
ctry = {'Papua New Guinea (mainland and islands)': 'Papua New Guinea', 'Fiji': 'Fiji', 'Vanuatu': 'Vanuatu', 'Solomon Islands': 'Solomon Islands'}
vr = [['country', 'crop', 'gaez_rainfed_fresh_t_ha', 'fao_actual_t_ha', 'actual_over_potential']]
for r, cn in ctry.items():
    for c, item in MAP.items():
        g = RES.get((r, c, 'rainfed')); f = FAO.get((cn, item))
        if g and f: vr.append([cn, CROPS[c], round(g, 1), round(f, 1), round(f / g, 2)])
csv.writer(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gaez_vs_fao.csv'), 'w', newline='')).writerows(vr)
print(len(rows) - 1, 'rows;', len(vr) - 1, 'validation rows')
