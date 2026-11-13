#!/usr/bin/env python3
"""Crop areas harvested for the world and five countries, 2011 and 2021-23 (FAOSTAT QCL bulk file), for the people-per-hectare test.
Usage: python3 -I extract_fao_countries.py 'Production_Crops_Livestock_E_All_Data_(Normalized).csv' fao_qcl_countries.csv   (FAO, CC BY 4.0)
       python3 -I extract_fao_countries.py 'Production_Crops_Livestock_E_All_Data_(Normalized).csv' fao_qcl_countries_2020.csv --years 2020
         (B93: other years, here the 2020 harvests that harvest matching in cassidy_people_per_hectare.py needs; with --years the bulk file's sha256
          is checked against qa/fao_bulk_hashes.csv, run from the repository root, and an existing output file is never overwritten)"""
import csv, sys, os, hashlib
args = sys.argv[1:]
years = ('2011', '2021', '2022', '2023')
if '--years' in args:
    i = args.index('--years'); years = tuple(args[i + 1].split(',')); del args[i:i + 2]
    want = next(r['sha256_csv'] for r in csv.DictReader(open('qa/fao_bulk_hashes.csv')) if r['file'].startswith('Production_Crops_Livestock'))
    h = hashlib.sha256()
    with open(args[0], 'rb') as fh:
        for blk in iter(lambda: fh.read(1 << 22), b''): h.update(blk)
    assert h.hexdigest() == want, 'the bulk file is not the one hashed in qa/fao_bulk_hashes.csv'
    assert not os.path.exists(args[1]), 'output exists; not overwritten: ' + args[1]
src, out = args[:2]
with open(src, encoding='latin-1') as fh, open(out, 'w', newline='') as fo:
    w = csv.writer(fo); w.writerow(['Area', 'Item', 'Element', 'Year', 'Unit', 'Value'])
    for x in csv.DictReader(fh):
        if x['Area'] in ('World', 'Australia', 'United States of America', 'India', 'China', 'Brazil') and x['Year'] in years and x['Element'] in ('Area harvested', 'Production'):
            w.writerow([x[c] for c in ('Area', 'Item', 'Element', 'Year', 'Unit', 'Value')])
