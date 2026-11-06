#!/usr/bin/env python3
"""Extract for the HALF index test: world crop areas and production (QCL), the food balance sheet for the world and six countries (FBS), and land areas (RL), for 2011 and 2021-23.
Usage: python3 -I extract_fao_half.py QCL.csv FBS.csv LANDUSE.csv OUT_DIR   (FAOSTAT bulk 'Normalized' files; see extract_fbs.py and extract_fao_world.py for URLs; FAO, CC BY 4.0)"""
import csv, sys, os
qcl, fbs, rl, out = sys.argv[1:5]
YEARS = {'2011', '2021', '2022', '2023'}
CTRY = {'World', 'Australia', 'United States of America', 'India', 'New Zealand', 'Argentina', 'China', 'Brazil'}
def run(src, dest, test, cols):
    with open(src, encoding='latin-1') as fh, open(os.path.join(out, dest), 'w', newline='') as fo:
        w = csv.writer(fo); w.writerow(cols)
        for x in csv.DictReader(fh):
            if test(x): w.writerow([x[c] for c in cols])
cols = ['Area', 'Item', 'Element', 'Year', 'Unit', 'Value']
run(qcl, 'half_qcl_world.csv', lambda x: x['Area'] == 'World' and x['Year'] in YEARS and x['Element'] in ('Area harvested', 'Production'), cols)
run(fbs, 'half_fbs_countries.csv', lambda x: x['Area'] in CTRY and x['Year'] in YEARS and x['Element'] in ('Production', 'Import quantity', 'Export quantity', 'Stock Variation', 'Feed', 'Seed', 'Losses', 'Processing', 'Other uses (non-food)', 'Food', 'Residuals', 'Total Population - Both sexes'), cols)
run(rl, 'half_landuse.csv', lambda x: x['Area'] in ('World', 'Australia') and x['Year'] in YEARS and x['Element'] == 'Area', cols)
