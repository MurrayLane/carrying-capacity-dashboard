#!/usr/bin/env python3
"""Download the ABS data beyond 2020-21 that this analysis uses. No login is needed for any of it.

Usage: python3 -I fetch_recent.py OUT_DIR

  Data API (SDMX, CSV)  AG_BROADACRE: SA2 area, levied production, local value, levy-payer counts for 2022-23 to 2024-25
                        AG_HORTICULTURE: avocados, macadamias, bananas, wine grapes by SA2 (area, production, value)
  Release workbooks     Horticulture national and state tables (Hort Innovation estimates, 69 crops, production and value, 2020-21 to 2024-25),
                        broadacre state tables, cattle and sheep series 2005 to 2025, value of livestock products, meat produced (7215009 to 7215012)
  Census cubes          the last census-based cubes, 2018-19 and 2019-20 (SA4) and 2020-21 (ASGS Edition 3, SA2 and SA4)
"""
import os, sys, urllib.request
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36"}
out = sys.argv[1]; os.makedirs(out, exist_ok=True)

def get(url, headers=None, name=None):
    dest = os.path.join(out, name or os.path.basename(url).replace('%20', '_'))
    if os.path.exists(dest): return
    data = urllib.request.urlopen(urllib.request.Request(url, headers={**UA, **(headers or {})}), timeout=300).read()
    open(dest, 'wb').write(data); print(f'{os.path.basename(dest)}: {len(data):,} bytes')

for flow, name in (('AG_BROADACRE', 'broadacre.csv'), ('AG_HORTICULTURE', 'hort.csv')):
    get(f'https://data.api.abs.gov.au/rest/data/ABS,{flow},1.0.1/all?startPeriod=2022&format=csv', {'Accept': 'text/csv'}, name)

AG = 'https://www.abs.gov.au/statistics/industry/agriculture'
for p in ('australian-agriculture-horticulture/2024-25/AAHDC_Aust_Horticulture_202425.xlsx',
          'australian-agriculture-horticulture/2024-25/AAHDC_Hort_Selected_Commodities_202425.xlsx',
          'australian-agriculture-broadacre-crops/2024-25/AABDC_Winter_202425.xlsx',
          'australian-agriculture-broadacre-crops/2024-25/AABDC_Summer_202425.xlsx',
          'australian-agriculture-livestock/2024-25/AALDC_Cattle%20herd%20series_2005_to_2025.xlsx',
          'australian-agriculture-livestock/2024-25/AALDC_Sheep%20flock%20series_2005%20to%202025.xlsx',
          'australian-agriculture-livestock/2024-25/AALDC_Value%20of%20livestock%20and%20products%202024-25.xlsx',
          'agricultural-commodities-australia/2019-20/71210DO001_201920.xlsx',
          *[f'livestock-products/jun-2026/7215{n:03d}.xlsx' for n in (9, 10, 11, 12)],
          'agricultural-commodities-australia/2020-21/AGCDCASGS202021.xlsx'):
    get(f'{AG}/{p}')
