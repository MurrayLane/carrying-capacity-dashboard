#!/usr/bin/env python3
"""SCOPE.md E1, second test: wool is the one livestock product the ABS values by state of the farm (shearing), so its share by state can be set against the state's share of sheep dry sheep equivalents.
Usage: python3 -I analysis/pasture_2025/wool_by_state.py AALDC_Value_of_livestock_and_products_2024-25.xlsx OUT.csv      (repository root; run state_production.py first, it writes the DSE shares)
Wool: local value ($) of 2022-23 to 2024-25, Table 2. Sheep DSE: the 2010 class mix scaled to the state's flock of each year, as the model does (state_production.py). Ratio = wool value per DSE relative to the nation's.
Cattle and sheep 'disposals' are valued where the animals are disposed of (sold, slaughtered, exported), not where they were raised, so they cannot be used for this (they mirror the state of slaughter)."""
import csv, os, sys, openpyxl
val, out = sys.argv[1:3]
wb = openpyxl.load_workbook(val, read_only=True, data_only=True); W = {}
for r in wb['Table 2'].iter_rows(min_row=5, values_only=True):
    if r[2] and str(r[2]).startswith('Wool') and isinstance(r[5], (int, float)): W[r[0]] = sum(r[5:8])
names = {2: 'New South Wales', 15: 'Victoria', 26: 'Queensland', 40: 'South Australia', 49: 'Western Australia', 56: 'Tasmania'}
W['New South Wales'] += W.get('Australian Capital Territory', 0)
tot = sum(W[n] for n in names.values())
dse = {r['state']: float(r['dse_share_pct']) for r in csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'state_production.csv'))) if r['species'] == 'sheep' and r['year'] == '2024-25'}
rows = [['state', 'dse_share_pct_2024_25', 'wool_value_share_pct_2022_25', 'wool_per_dse_relative']]
for z, n in names.items():
    d = dse.get('NSW-ACT' if n == 'New South Wales' else n, 0); s_ = 100 * W[n] / tot; rows.append([n, d, round(s_, 1), round(s_ / d, 2) if d else ''])
csv.writer(open(out, 'w', newline='')).writerows(rows); print('\n'.join(','.join(map(str, r)) for r in rows))
