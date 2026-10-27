#!/usr/bin/env python3
"""Turn the ABS Data API tables (2022-23 to 2024-25) into cubes in the layout the yield pipeline reads (pipeline/yields/yields.py).

Usage: python3 -I build_recent_cubes.py API_DIR OUT_DIR      (API_DIR holds broadacre.csv and hort.csv from analysis/recent_data/fetch_recent.py)

Writes OUT_DIR/regions.json and OUT_DIR/cube_<year>.json. A cube is
  {"year", "rows": {"Wheat (ha)": [...], "Wheat (t)": [...]}, "unreliable": [["Wheat (ha)", col], ...]}
with one value per column (column 0 unused, as in the archive cubes), None where the ABS has no figure. Columns: 1 Australia (the sum of the
states), 2 to 10 the states and territories as the ABS publishes them, then the SA2s of ASGS Edition 3. Hectares and tonnes, the model's units.

Crops and sources (the ABS publishes no others with both area and production after 2020-21):
  AG_BROADACRE      Total crop area (ha) and levied production (t): wheat, oats, barley, sorghum, maize, rice, sugar cane, canola, chickpeas,
                    faba beans (model row Field beans), field peas, lentils. Cotton has area but no production; triticale, soybeans, sunflower and
                    mung beans are not published.
  AG_HORTICULTURE   Total crop area (ha) and production (t): avocados, bananas, macadamias (in-shell). Wine grapes have crush but no area.
Levied production is what levy payers produced; at national level it matches the published production (wheat 2022-23: SA2 sum 41,199,482 t
against 41,199,486 t published).
`unreliable` lists a cell when its area or tonnes is under 10, the thesis's stated minimum (section 8.1 step 8); the API carries no reliability symbols.
"""
import csv, json, os, sys
out = sys.argv[2]; api = sys.argv[1]; os.makedirs(out, exist_ok=True)
MIN_HA, MIN_T = 10.0, 10.0
STATES = {'1': 'New South Wales', '2': 'Victoria', '3': 'Queensland', '4': 'South Australia', '5': 'Western Australia', '6': 'Tasmania', '7': 'Northern Territory', '8': 'Australian Capital Territory', '9': 'Other Territories'}
# model row -> (API prefix, area item, production item)
CROPS = {
    'Wheat': ('Broad', 'BroadWheat_Area_Total', 'BroadWheat_Prod_Levy'), 'Oats': ('Broad', 'BroadOats_Area_Total', 'BroadOats_Prod_Levy'),
    'Barley': ('Broad', 'BroadBarley_Area_Total', 'BroadBarley_Prod_Levy'), 'Sorghum': ('Broad', 'BroadSorghum_Area_Total', 'BroadSorghum_Prod_Levy'),
    'Maize': ('Broad', 'BroadMaize_Area_Total', 'BroadMaize_Prod_Levy'), 'Rice': ('Broad', 'BroadRice_Area_Total', 'BroadRice_Prod_Levy'),
    'Sugar cane': ('Broad', 'BroadSugarcane_Area_Total', 'BroadSugarcane_Prod_Levy'), 'Canola': ('Broad', 'BroadCanola_Area_Total', 'BroadCanola_Prod_Levy'),
    'Chickpeas': ('Broad', 'BroadChickpeas_Area_Total', 'BroadChickpeas_Prod_Levy'), 'Field beans': ('Broad', 'BroadFababeans_Area_Total', 'BroadFababeans_Prod_Levy'),
    'Field peas': ('Broad', 'BroadFieldpeas_Area_Total', 'BroadFieldpeas_Prod_Levy'), 'Lentils': ('Broad', 'BroadLentils_Area_Total', 'BroadLentils_Prod_Levy'),
    'Avocados': ('Hort', 'HortAvocados_Area_Total', 'HortAvocados_Prod'), 'Bananas': ('Hort', 'HortBananas_Area_Total', 'HortBananas_Prod'),
    'Macadamias': ('Hort', 'HortMacadamias_Area_Total', 'HortMacadamias_Prod_Inshell'),
}
data = {}                                   # (item, year) -> {region: value}
for f in ('broadacre.csv', 'hort.csv'):
    for r in csv.DictReader(open(os.path.join(api, f))):
        if r['OBS_VALUE'] == '': continue
        y0 = int(r['TIME_PERIOD'][:4]); year = f'{y0}-{(y0 + 1) % 100:02d}'
        data.setdefault((r['DATAITEM'], year), {})[r['REGION']] = float(r['OBS_VALUE'])
years = sorted({y for _, y in data})
sa2 = sorted({reg for d in data.values() for reg in d if len(reg) == 9})
cols = [('0', 'Australia', 'nation')] + [(c, n, 'state') for c, n in STATES.items()] + [(c, c, 'sa2') for c in sa2]
json.dump({'source': 'ABS Data API AG_BROADACRE and AG_HORTICULTURE 1.0.1, SA2 ASGS Edition 3',
           'regions': [{'column': i + 1, 'code': c, 'label': n, 'kind': k} for i, (c, n, k) in enumerate(cols)]}, open(os.path.join(out, 'regions.json'), 'w'), indent=1)
for year in years:
    rows, unreliable = {}, []
    for crop, (_, ai, pi) in CROPS.items():
        for label, item in ((f'{crop} (ha)', ai), (f'{crop} (t)', pi)):
            d = data.get((item, year))
            if d is None: continue
            vals = [None] * (len(cols) + 1)
            for i, (code, _, kind) in enumerate(cols[1:], start=2):
                v = d.get(code)
                if v is not None: vals[i] = v
            vals[1] = sum(v for v in vals[2:11] if v) or None                          # Australia = the states
            rows[label] = vals
        a, t = rows.get(f'{crop} (ha)'), rows.get(f'{crop} (t)')
        if a and t:
            for c in range(1, len(cols) + 1):
                if (a[c] is not None and a[c] < MIN_HA) or (t[c] is not None and t[c] < MIN_T): unreliable += [[f'{crop} (ha)', c], [f'{crop} (t)', c]]
    json.dump({'year': year, 'rows': rows, 'unreliable': unreliable}, open(os.path.join(out, f'cube_{year}.json'), 'w'))
    print(year, len(rows), 'rows,', len(unreliable) // 2, 'cells under the minimum')
