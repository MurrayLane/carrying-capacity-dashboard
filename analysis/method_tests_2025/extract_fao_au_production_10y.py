#!/usr/bin/env python3
"""Australian production and area harvested for 2014 to 2023, the ten-year production window of Paper B (brief B139, decision 144; R05b issue 12), from the FAOSTAT QCL bulk file.
NOT RUN IN B139: no network. The bulk file is not on disk; it is pinned by hash in qa/fao_bulk_hashes.csv (Production_Crops_Livestock_E_All_Data_(Normalized).zip, sha256 of the zip
c5835418c18f9322e7decbd6800f93a216eaae3cdfa31acb08f0518c0c6d6853, FAO file dated 2025-12-23).
Fetch (Murray or the coordinator), from the repository root:
  curl -L -o /tmp/qcl.zip 'https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_All_Data_(Normalized).zip'
  echo 'c5835418c18f9322e7decbd6800f93a216eaae3cdfa31acb08f0518c0c6d6853  /tmp/qcl.zip' | sha256sum -c -          (a different hash means FAO has revised the file: say so before using it)
  unzip -o /tmp/qcl.zip 'Production_Crops_Livestock_E_All_Data_(Normalized).csv' -d /tmp/qcl
  python3 -I analysis/method_tests_2025/extract_fao_au_production_10y.py '/tmp/qcl/Production_Crops_Livestock_E_All_Data_(Normalized).csv' analysis/method_tests_2025/fao_au_production_2014_2023.csv
  python3 -I analysis/method_tests_2025/production_window_10y.py                (reads that file when it exists and adds the ten-year rows)
Writes the rows of Australia for the items of production_window_10y.py, elements Production and Area harvested, years 2014 to 2023, in the layout of fao_au_production_1997_2023.csv.
Test of this script (B139, scratch, not filed): a synthetic file in the bulk layout (17 items, both elements, 2014 to 2023, invented values) gave 340 rows for 34 item-element pairs; the same file with 2017 removed made it stop and name the missing year.
"""
import csv, sys
ITEMS = ('Cereals, primary', 'Pulses, Total', 'Sugar Crops Primary', 'Oilcrops, Oil Equivalent', 'Roots and Tubers, Total', 'Vegetables Primary', 'Fruit Primary', 'Treenuts, Total', 'Wheat', 'Barley',
         'Meat, Total', 'Beef and Buffalo Meat, primary', 'Sheep and Goat Meat', 'Meat, Poultry', 'Milk, Total', 'Eggs Primary', 'Meat of pig with the bone, fresh or chilled')
YEARS = tuple(str(y) for y in range(2014, 2024))
src, out = sys.argv[1:3]
rows, seen = [], {}
with open(src, encoding='latin-1') as fh:
    for x in csv.DictReader(fh):
        if x['Area'] == 'Australia' and x['Element'] in ('Production', 'Area harvested') and x['Item'] in ITEMS and x['Year'] in YEARS and x['Value'] != '':
            rows.append([x[c] for c in ('Area', 'Item', 'Element', 'Year', 'Unit', 'Value')]); seen.setdefault((x['Item'], x['Element']), set()).add(x['Year'])
short = [(k, sorted(set(YEARS) - v)) for k, v in seen.items() if set(YEARS) - v]
if short or not seen: sys.exit('missing years or no rows: %s' % (short or 'nothing read'))
with open(out, 'w', newline='') as fo:
    w = csv.writer(fo); w.writerow(['Area', 'Item', 'Element', 'Year', 'Unit', 'Value']); w.writerows(sorted(rows, key=lambda r: (r[1], r[2], r[3])))
print('wrote %s: %d rows for %d item-element pairs, years 2014 to 2023' % (out, len(rows), len(seen)))
