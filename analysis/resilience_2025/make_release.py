#!/usr/bin/env python3
"""Writes releases/2025-resilience/release.json: the resilience table of 'data: ABS to 2024-25' (tables.csv; the thesis method on the ABS series to 2024-25).
Usage: python3 analysis/resilience_2025/make_release.py          (repository root; run resilience.py first)
The release replaces the model of 2025-organic by the same model with the 1,200 cells of the resilience sheet (rows 3 to 10, years 1 to 150) overridden, and keeps the organic overrides of the Yield sheet."""
import csv, json, os
ROOT = os.getcwd(); METHOD = 'data: ABS to 2024-25'
rows = {r[0]: r[2:] for r in csv.reader(open(os.path.join(ROOT, 'analysis/resilience_2025/tables.csv'))) if r[1] == METHOD}
def col(n):                                   # 1-based column number to letters
    s = ''
    while n: n, r = divmod(n - 1, 26); s = chr(65 + r) + s
    return s
ORDER = ['Australia', 'New South Wales', 'Victoria', 'Queensland', 'South Australia', 'Western Australia', 'Tasmania', 'South Australia']     # sheet rows 3 to 10; the Northern Territory takes South Australia, as in the thesis
cells = {f'{col(2 + t)}{3 + i}': round(float(rows[loc][t - 1]), 6) for i, loc in enumerate(ORDER) for t in range(1, 151)}
parent = json.load(open(os.path.join(ROOT, 'releases/2025-organic/release.json')))
rel = {'id': '2025-resilience', 'label': '2025 data, consumption, organic yields and resilience table', 'status': 'current', 'extends': '2025-organic',
       'description': "Layer 7, a data update of the long-term resilience (climate variability) table. The thesis method (analysis/resilience_2025/) reproduced to machine precision from the archive workbook, run on the ABS historical series of wheat, oats and barley to 2021-22 and the ABS 2022-23 to 2024-25 cubes. Australia's 100-year factor is unchanged (0.456) because the worst year in the record is still 1915; the 5 and 20 year factors, and the Western Australian and South Australian factors, change a little. Only the long-term result moves: the short-term settings use a resilience of one year, which is always 1.",
       'layer': parent['layer'], 'vintage': 'ABS grain yields 1861 to 2024-25',
       'model': {'file': parent['model']['file'], 'cellOverrides': {**parent['model']['cellOverrides'], 'resilience': cells}},
       'errata': ["The method keeps the thesis's choices (unweighted mean of three grains, a reference that includes the year itself, ranks read as return periods), see analysis/resilience_2025/README.md for what they do to the result and for the alternatives not adopted.",
                  "NSW is NSW with the ACT in the 2022-23 to 2024-25 cubes and NSW alone in the historical series."]}
os.makedirs(os.path.join(ROOT, 'releases/2025-resilience'), exist_ok=True)
json.dump(rel, open(os.path.join(ROOT, 'releases/2025-resilience/release.json'), 'w'), indent=2)
idx = json.load(open(os.path.join(ROOT, 'releases/index.json')))
if '2025-resilience' not in idx['order']: idx['order'].insert(idx['order'].index('2025-organic'), '2025-resilience'); json.dump(idx, open(os.path.join(ROOT, 'releases/index.json'), 'w'), indent=2)
print('wrote releases/2025-resilience/release.json with', len(cells), 'resilience cells; index order', idx['order'][:5])
