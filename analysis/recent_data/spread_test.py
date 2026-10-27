#!/usr/bin/env python3
"""Is the 2020-21 jump in the number of regions growing each crop a trend or an artefact?

Usage: python3 -I spread_test.py DATA_DIR      (DATA_DIR from fetch_recent.py; also needs the 2018-19 SA4 cube, 71210do001_201819.xls)

For wheat, barley, oats, canola and sorghum (area) it prints, per source and year:
  n     regions reporting the crop
  eff   effective number of regions, 1 / sum(share^2): large when the crop is spread evenly, small when a few regions hold it
  top   share of national area held by the 20 largest regions (SA2) or 5 largest (SA4)
  kha   national area, thousand hectares
n depends on the boundaries and on which holdings a source includes; eff and top depend far less on either.
"""
import collections, csv, os, sys
import openpyxl
D = sys.argv[1]
CR = {'Wheat': 'Wheat for grain', 'Barley': 'Barley for grain', 'Oats': 'Oats for grain', 'Canola': 'Canola', 'Sorghum': 'Sorghum'}
API = {'Wheat': 'BroadWheat', 'Barley': 'BroadBarley', 'Oats': 'BroadOats', 'Canola': 'BroadCanola', 'Sorghum': 'BroadSorghum'}

def stats(d, top):
    v = sorted((x for x in d.values() if x and x > 0), reverse=True); t = sum(v)
    if not t: return None
    return dict(n=len(v), eff=round(t * t / sum(x * x for x in v), 1), top=round(sum(v[:top]) / t, 3), kha=round(t / 1e3))

def crop_of(desc):
    desc = str(desc)
    if not desc.rstrip().endswith('Area (ha)'): return None
    return next((k for k, v in CR.items() if v in desc), None)

def collect(rows, digits):
    out = collections.defaultdict(dict)
    for code, desc, est in rows:
        k = crop_of(desc)
        if k and isinstance(est, (int, float)) and len(str(code).split('.')[0]) == digits: out[k][str(code)] = est
    return out

def show(label, tab, top):
    print(label); [print(f'   {k:8s}', stats(tab[k], top)) for k in CR if k in tab]

wb = openpyxl.load_workbook(os.path.join(D, '71210DO001_201920.xlsx'), read_only=True, data_only=True)
show('2019-20 census, SA4 (2016 boundaries)', collect(((r[0], r[2], r[3]) for ws in wb.worksheets[1:] for r in ws.iter_rows(min_row=7, values_only=True)), 3), 5)
try:
    import xlrd
    bk = xlrd.open_workbook(os.path.join(D, '71210do001_201819.xls'))
    show('2018-19 census, SA4 (2016 boundaries)', collect(((r[0], r[2], r[3]) for sh in bk.sheets()[1:] for r in (sh.row_values(i) for i in range(6, sh.nrows))), 3), 5)
except (ImportError, FileNotFoundError): print('2018-19 SA4 skipped (needs xlrd and 71210do001_201819.xls)')
wb = openpyxl.load_workbook(os.path.join(D, 'AGCDCASGS202021.xlsx'), read_only=True, data_only=True)
rows = [(r[0], r[3], r[4]) for r in wb['Table 1'].iter_rows(min_row=8, values_only=True)]
show('2020-21 census, SA4 (2021 boundaries)', collect(rows, 3), 5)
show('2020-21 census, SA2 (2021 boundaries)', collect(rows, 9), 20)
api = list(csv.DictReader(open(os.path.join(D, 'broadacre.csv'))))
for yr in ('2022', '2023', '2024'):
    tab = {k: {x['REGION']: float(x['OBS_VALUE']) for x in api if x['DATAITEM'] == p + '_Area_Total' and x['TIME_PERIOD'].startswith(yr) and x['OBS_VALUE'] != '' and len(x['REGION']) == 9} for k, p in API.items()}
    show(f'{yr}-{int(yr) + 1 - 2000} levy-based, SA2 (2021 boundaries)', tab, 20)
