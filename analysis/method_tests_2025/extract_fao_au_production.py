#!/usr/bin/env python3
"""Australian production of cereals, meat and pulses for 1997, 1998 and 2021-23 (FAOSTAT QCL bulk file), for the method tests that compare the two ends of the series.
Usage: python3 -I extract_fao_au_production.py 'Production_Crops_Livestock_E_All_Data_(Normalized).csv' fao_au_production_1997_2023.csv
Source: FAOSTAT Crops and livestock products, bulk download https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_All_Data_(Normalized).zip (FAO, CC BY 4.0), file dated 2025-12-23."""
import csv, sys
src, out = sys.argv[1:3]
with open(src, encoding='latin-1') as fh, open(out, 'w', newline='') as fo:
    w = csv.writer(fo); w.writerow(['Area', 'Item', 'Element', 'Year', 'Unit', 'Value'])
    for x in csv.DictReader(fh):
        if x['Area'] == 'Australia' and x['Element'] == 'Production' and x['Item'] in ('Cereals, primary', 'Meat, Total', 'Pulses, Total') and x['Year'] in ('1997', '1998', '2021', '2022', '2023'):
            w.writerow([x[c] for c in ('Area', 'Item', 'Element', 'Year', 'Unit', 'Value')])
