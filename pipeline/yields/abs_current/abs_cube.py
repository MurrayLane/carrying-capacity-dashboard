"""Read the ABS Agricultural Commodities NRM cubes (2015-16 to 2020-21) into one tidy structure.

cube(year) -> {region_code: {'label': str, 'items': {commodity_code: (estimate, flag, businesses)}}}
Estimates are floats (the ABS prints some years with thousands separators), None where the ABS withholds a figure.
flag is the ABS reliability symbol as text: '' (relative standard error under 10%), '^' (10 to 25%), '*' (25 to 50%), '**' (over 50%, "too unreliable
 for general use"). 2020-21 has no symbols (its NRM figures are area-apportioned from SA2), so flag is None there.
Item descriptions: descriptions(year) -> {commodity_code: text}.
"""
import csv, io, os
YEARS = ('2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21')


def num(x):
    if x is None: return None
    x = str(x).replace(',', '').strip()
    if x in ('', '-', 'np', 'NP', 'na', 'NA', '..'): return None
    try: return float(x)
    except ValueError: return None


def _rows(path, year):
    if path.endswith('.xlsx'):
        import openpyxl
        ws = openpyxl.load_workbook(path, read_only=True)['Table 1']
        for r in ws.iter_rows(values_only=True): yield list(r)
    else:
        raw = open(path, encoding='latin1').read()
        for r in csv.reader(io.StringIO(raw)): yield r


def read_cube(folder, year):
    path = os.path.join(folder, f'{year}_NRM.' + ('xlsx' if year == '2020-21' else 'csv'))
    cube, desc, header = {}, {}, None
    for r in _rows(path, year):
        if header is None:
            if r and str(r[0]).strip() == 'Region code': header = [str(x).strip().lower() for x in r]
            continue
        if not r or r[0] in (None, '') or len(r) < 5: continue
        code = str(r[0]).strip()
        if not code.lstrip('-').isdigit(): continue
        row = dict(zip(header, r))
        est_key = next(k for k in header if k.startswith('estimate') and 'relative' not in k)
        rse_key = next((k for k in header if k.startswith('estimate') and 'relative' in k), None)
        bus_key = next((k for k in header if k.startswith('number of agricultural businesses') and 'relative' not in k), None)
        reg = cube.setdefault(int(code), {'label': str(row['region label']).strip(), 'items': {}})
        c = str(row['commodity code']).strip()
        reg['items'][c] = (num(row[est_key]), (str(row[rse_key]).strip() if row[rse_key] is not None else '') if rse_key else None, num(row[bus_key]) if bus_key else None)
        desc[c] = str(row['commodity description']).strip()
    return cube, desc
