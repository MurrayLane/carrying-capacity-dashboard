#!/usr/bin/env python3
"""World crop and livestock production and land areas, 1990-92 and 2021-23, from two FAOSTAT bulk files, for the footprint and land-per-diet tests.
Usage: python3 -I extract_fao_world.py 'Production_Crops_Livestock_E_All_Data_(Normalized).csv' 'Inputs_LandUse_E_All_Data_(Normalized).csv' fao_world_land_production.csv
Sources: FAOSTAT Crops and livestock products and Land Use bulk downloads (https://bulks-faostat.fao.org/production/), FAO, CC BY 4.0, files dated Dec 2025 and Oct 2025."""
import csv, sys
q, l, out = sys.argv[1:4]
YEARS = {'1990', '1991', '1992', '2021', '2022', '2023'}
with open(out, 'w', newline='') as fo:
    w = csv.writer(fo); w.writerow(['Source', 'Area', 'Item', 'Element', 'Year', 'Unit', 'Value'])
    with open(q, encoding='latin-1') as fh:
        for x in csv.DictReader(fh):
            if x['Area'] == 'World' and x['Year'] in YEARS and x['Element'] in ('Area harvested', 'Production'):
                w.writerow(['QCL', 'World', x['Item'], x['Element'], x['Year'], x['Unit'], x['Value']])
    with open(l, encoding='latin-1') as fh:
        for x in csv.DictReader(fh):
            if x['Area'] in ('World', 'Australia') and x['Year'] in YEARS | {'1991'} and x['Element'] == 'Area' and x['Item'] in ('Cropland', 'Permanent meadows and pastures', 'Agricultural land'):
                w.writerow(['RL', x['Area'], x['Item'], x['Element'], x['Year'], x['Unit'], x['Value']])
