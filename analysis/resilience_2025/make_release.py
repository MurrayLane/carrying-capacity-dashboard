#!/usr/bin/env python3
"""Writes releases/2025-resilience/release.json (the resilience table of 'data: ABS to 2024-25' in tables.csv: the thesis method on the ABS series to 2024-25) and releases/2025-resilience-loo/release.json
(the alternate with the leave-one-out reference, method 'loo reference').
Usage: python3 analysis/resilience_2025/make_release.py          (repository root; run resilience.py first)
The release replaces the model of 2025-organic by the same model with the 1,200 cells of the resilience sheet (rows 3 to 10, years 1 to 150) overridden, and keeps the organic overrides of the Yield sheet."""
import csv, json, os
ROOT = os.getcwd()
TABLES = list(csv.reader(open(os.path.join(ROOT, 'analysis/resilience_2025/tables.csv'))))
def col(n):                                   # 1-based column number to letters
    s = ''
    while n: n, r = divmod(n - 1, 26); s = chr(65 + r) + s
    return s
ORDER = ['Australia', 'New South Wales', 'Victoria', 'Queensland', 'South Australia', 'Western Australia', 'Tasmania', 'South Australia']     # sheet rows 3 to 10; the Northern Territory takes South Australia, as in the thesis
def make(rid, method, extends, label, description, errata, vintage):
    rows = {r[0]: r[2:] for r in TABLES if r[1] == method}
    cells = {f'{col(2 + t)}{3 + i}': round(float(rows[loc][t - 1]), 6) for i, loc in enumerate(ORDER) for t in range(1, 151)}
    parent = json.load(open(os.path.join(ROOT, f'releases/{extends}/release.json')))
    rel = {'id': rid, 'label': label, 'status': 'current', 'extends': extends, 'description': description, 'layer': parent['layer'], 'vintage': vintage,
           'model': {'file': parent['model']['file'], 'cellOverrides': {**parent['model']['cellOverrides'], 'resilience': cells}}, 'errata': errata}
    os.makedirs(os.path.join(ROOT, f'releases/{rid}'), exist_ok=True)
    json.dump(rel, open(os.path.join(ROOT, f'releases/{rid}/release.json'), 'w'), indent=2)
    print('wrote releases/%s/release.json with %d resilience cells' % (rid, len(cells)))

make('2025-resilience', 'data: ABS to 2024-25', '2025-organic', '2025 data, consumption, organic yields and resilience table',
     "Layer 7, a data update of the long-term resilience (climate variability) table. The thesis method (analysis/resilience_2025/) reproduced to machine precision from the archive workbook, run on the ABS historical series of wheat, oats and barley to 2021-22 and the ABS 2022-23 to 2024-25 cubes. Australia's 100-year factor is unchanged (0.456) because the worst year in the record is still 1915; the 5 and 20 year factors, and the Western Australian and South Australian factors, change a little. Only the long-term result moves: the short-term settings use a resilience of one year, which is always 1.",
     ["The method keeps the thesis's choices (unweighted mean of three grains, a reference that includes the year itself, ranks read as return periods), see analysis/resilience_2025/README.md for what they do to the result and for the alternatives not adopted.",
      "NSW is NSW with the ACT in the 2022-23 to 2024-25 cubes and NSW alone in the historical series."], 'ABS grain yields 1861 to 2024-25')
make('2025-resilience-loo', 'loo reference', '2025-resilience', 'Alternate: resilience table with a leave-one-out reference',
     "An alternate to 2025-resilience, not a later layer. The thesis reference for a year's yield is the mean of ten observations that includes the year itself, so a very bad year lowers its own reference and its ratio is closer to 1 than it should be. This release uses a reference made from the 20 other observations nearest in time. Everything else is as in 2025-resilience. Australia's 100-year factor falls from 0.456 to 0.415 and the long-term capacity by about 9% (the states by 7% to 10%); the short term is unchanged.",
     ["A method correction of the thesis table, recorded as an alternate (SCOPE.md D9, E14). It does not address the other choices of the method (three grains, rank-based return periods, no store of grain)."], 'ABS grain yields 1861 to 2024-25, leave-one-out reference')
idx = json.load(open(os.path.join(ROOT, 'releases/index.json')))
for rid, after in (('2025-resilience', '2025-organic'), ('2025-resilience-loo', None)):
    if rid not in idx['order']:
        idx['order'].insert(idx['order'].index('2025-organic') if after else idx['order'].index('2025-resilience') + 1, rid)
json.dump(idx, open(os.path.join(ROOT, 'releases/index.json'), 'w'), indent=2); print('index order', idx['order'][:6])
