#!/usr/bin/env python3
"""Cut the FAOSTAT food balance sheet (new series, 2010 onward) down to Australia and the World, 2021-2023, the elements the method tests need.
Usage: python3 -I analysis/method_tests_2025/extract_fbs.py 'FoodBalanceSheets_E_All_Data_(Normalized).csv' analysis/method_tests_2025/fbs_au_world_2021_23.csv
Source: FAOSTAT Food Balances (2010-), bulk download https://bulks-faostat.fao.org/production/FoodBalanceSheets_E_All_Data_(Normalized).zip (FAO, CC BY 4.0), file dated 14 Oct 2025."""
import csv, sys
src, out = sys.argv[1:3]
KEEP = {'Production','Import quantity','Export quantity','Feed','Seed','Losses','Processing','Other uses (non-food)','Food','Food supply (kcal)','Protein supply quantity (t)','Stock Variation','Total Population - Both sexes'}
with open(src, encoding='latin-1') as fh, open(out, 'w', newline='') as fo:
    r = csv.DictReader(fh); w = csv.writer(fo); w.writerow(['Area','Item','Element','Year','Unit','Value'])
    for x in r:
        if x['Area'] in ('Australia', 'World') and x['Year'] in ('2021', '2022', '2023') and x['Element'] in KEEP:
            w.writerow([x['Area'], x['Item'], x['Element'], x['Year'], x['Unit'], x['Value']])
