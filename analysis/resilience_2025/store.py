#!/usr/bin/env python3
"""Grain store (SCOPE.md E15): the resilience table for a population that holds a store of grain, and the scenario releases 2025-store-1 and 2025-store-2.
Usage: python3 -I analysis/resilience_2025/store.py ARCHIVE_XLS HISTORIC_XLSX          (repository root; the same two files as resilience.py)

The model's resilience table asks a population to meet its needs in the single worst year of the return period. A population holding a store of s years of consumption is bound instead by the worst
run of s + 1 consecutive years, whose average yield is higher. Here that is done with the model's own method (resilience.py, 'data: ABS to 2024-25': the mean of the three grains, the ratio to the 10-observation
moving reference, ranks read as return periods): the ratios of each run of d = s + 1 consecutive calendar years are averaged, ranked, read at the same anchors and interpolated. store_tables.csv has the 150-year
table of each location for s = 0 to 4 (s = 0 is the model's table, checked to equal tables.csv). The releases replace the table of 2025-improved with the s = 1 and s = 2 tables.
What the table does not model: the cost of holding the store (land is not charged for grain stored), losses in store, or a store that is drawn down and not refilled."""
import csv, importlib.util, json, os, statistics, sys
ROOT = os.getcwd(); sys.argv = [sys.argv[0], sys.argv[1], sys.argv[2]]
spec = importlib.util.spec_from_file_location('resilience', os.path.join(ROOT, 'analysis/resilience_2025/resilience.py')); R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)
s = R.series_from_abs(True); out = [['location', 'store_years'] + list(range(1, 151))]; check = {r[0]: r[2:] for r in csv.reader(open(os.path.join(ROOT, 'analysis/resilience_2025/tables.csv'))) if r[1] == 'data: ABS to 2024-25'}
for loc in R.LOC:
    yrs = sorted(s[loc]); y = [s[loc][t] for t in yrs]; ratio = R.thesis_ratios(y)
    for store in range(0, 5):
        d = store + 1; runs = [statistics.mean(ratio[i:i + d]) for i in range(len(ratio) - d + 1) if yrs[i + d - 1] - yrs[i] == d - 1]
        tab = R.interp(R.anchors_rank(runs)); out.append([loc, store] + [round(v, 6) for v in tab])
        if store == 0:
            assert max(abs(a - float(b)) for a, b in zip(tab, check[loc])) < 1e-5, f'{loc}: the s = 0 table differs from tables.csv'
csv.writer(open(os.path.join(ROOT, 'analysis/resilience_2025/store_tables.csv'), 'w', newline='')).writerows(out)
print('store_tables.csv; factor at 100 years, Australia:', {r[1]: r[101] for r in out[1:] if r[0] == 'Australia'})

def col(n):
    t = ''
    while n: n, r = divmod(n - 1, 26); t = chr(65 + r) + t
    return t
ORDER = ['Australia', 'New South Wales', 'Victoria', 'Queensland', 'South Australia', 'Western Australia', 'Tasmania', 'South Australia']      # sheet rows 3 to 10; the Northern Territory takes South Australia
base = json.load(open(os.path.join(ROOT, 'releases/2025-diet/release.json')));   # the data chain's tip carries every cell override of the layers before it
idx = json.load(open(os.path.join(ROOT, 'releases/index.json')))
for store, rid in ((1, '2025-store-1'), (2, '2025-store-2')):
    rows = {r[0]: r[2:] for r in out[1:] if int(r[1]) == store}
    cells = {f'{col(2 + t)}{3 + i}': float(rows[loc][t - 1]) for i, loc in enumerate(ORDER) for t in range(1, 151)}
    word = 'a year' if store == 1 else f'{store} years'
    rel = {'id': rid, 'label': f'Scenario: a store of {word} of grain (improved method, 2025 data)', 'status': 'current', 'extends': '2025-improved',
           'description': f"A scenario on 2025-improved, not a later layer. The resilience table is the table for a population holding a store of {word} of consumption, which is bound by the worst run of {store + 1} consecutive years instead of the worst single year (analysis/resilience_2025/store.py; the model's method on the ABS series to 2024-25). Only the long-term result changes (the short term uses a time frame of one year, for which the table is 1).",
           'layer': base['layer'], 'vintage': base['vintage'],
           'model': {'file': base['model']['file'], 'cellOverrides': {**base['model']['cellOverrides'], 'resilience': cells}},
           'errata': ['The store is not charged to the model: no land for the grain held, no losses in store, and no refilling after a drawdown. It is a scenario about resilience, not a costed policy.',
                      "The table is built from the grain yields of wheat, oats and barley, as the model's table is; consecutive-year runs are taken from calendar years only."]}
    os.makedirs(os.path.join(ROOT, f'releases/{rid}'), exist_ok=True); json.dump(rel, open(os.path.join(ROOT, f'releases/{rid}/release.json'), 'w'), indent=2)
    if rid not in idx['order']: idx['order'].insert(idx['order'].index('2025-improved') + store, rid)
json.dump(idx, open(os.path.join(ROOT, 'releases/index.json'), 'w'), indent=2); print(idx['order'][:8])
