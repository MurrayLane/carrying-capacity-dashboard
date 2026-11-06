#!/usr/bin/env python3
"""Crop areas harvested for the world and five countries, 2011 and 2021-23 (FAOSTAT QCL bulk file), for the people-per-hectare test.
Usage: python3 -I extract_fao_countries.py 'Production_Crops_Livestock_E_All_Data_(Normalized).csv' fao_qcl_countries.csv   (FAO, CC BY 4.0)"""
import csv, sys
src, out = sys.argv[1:3]
with open(src, encoding='latin-1') as fh, open(out, 'w', newline='') as fo:
    w = csv.writer(fo); w.writerow(['Area', 'Item', 'Element', 'Year', 'Unit', 'Value'])
    for x in csv.DictReader(fh):
        if x['Area'] in ('World', 'Australia', 'United States of America', 'India', 'China', 'Brazil') and x['Year'] in ('2011', '2021', '2022', '2023') and x['Element'] in ('Area harvested', 'Production'):
            w.writerow([x[c] for c in ('Area', 'Item', 'Element', 'Year', 'Unit', 'Value')])
