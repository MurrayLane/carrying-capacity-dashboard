#!/usr/bin/env python3
"""Beef output per animal by state from the ABARES Farm Data Portal (SCOPE.md E1): physical data of beef specialist farms.
Usage: python3 -I analysis/pasture_2025/abares_state_index.py FDP_STATE_CSV OUT.csv          (repository root; FDP_STATE_CSV = fdp-state-historical.csv in the models archive, Livestock/ABARES-NT-WA/)
For each state, mean of 2017 to 2023 per beef-specialist farm: area operated, beef herd at 30 June, beef cattle sold, transferred off farm, beef cattle receipts. Output per animal = (sold + transferred off) x receipts per head sold /
herd, in dollars a head of herd: the value of the cattle a farm sends off per animal it keeps, which carries both turn-off and weight at sale. Index = the state's value over the mean of New South Wales, Victoria and Tasmania
(the temperate south). Transfers are valued at the sale price; ABARES's own turn-off rate counts sold plus transferred off over the herd."""
import csv, sys
src, out = sys.argv[1:3]
D = {}
for x in csv.DictReader(open(src, encoding='utf-8-sig')):
    if x['Industry'] == 'Beef':
        try: D[(x['State'], int(x['Year']), x['Variable'])] = float(x['Value'])
        except ValueError: pass
YS = range(2017, 2024); STATES = ['New South Wales', 'Victoria', 'Tasmania', 'South Australia', 'Queensland', 'Western Australia', 'Northern Territory']
def avg(st, var):
    v = [D[(st, y, var)] for y in YS if (st, y, var) in D]; return sum(v) / len(v)
rows = []
for st in STATES:
    a, h, s, t, r = (avg(st, v) for v in ('Area operated at 30 June (ha)', 'Beef herd at 30 June (no.)', 'Beef cattle sold (no.)', 'Beef cattle transferred off farm (no.)', 'Beef cattle receipts ($)'))
    rows.append(dict(state=st, area_ha=a, herd=h, sold=s, transferred_off=t, receipts=r, turnoff_pct=100 * (s + t) / h, herd_per_1000ha=1000 * h / a, receipts_per_head_sold=r / s, output_value_per_herd_head=(s + t) * (r / s) / h))
ref = sum(x['output_value_per_herd_head'] for x in rows[:3]) / 3
for x in rows: x['index_vs_temperate_south'] = x['output_value_per_herd_head'] / ref
cols = list(rows[0]); w = csv.writer(open(out, 'w', newline='')); w.writerow(cols)
for x in rows: w.writerow([x[c] if isinstance(x[c], str) else round(x[c], 3) for c in cols])
for x in rows: print(x['state'].ljust(20), 'turn-off', round(x['turnoff_pct'], 1), '% output value per head', round(x['output_value_per_herd_head']), 'index', round(x['index_vs_temperate_south'], 2))
