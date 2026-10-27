#!/usr/bin/env python3
"""Liquid fuel sold per person in Australia by financial year, from the Australian Petroleum Statistics (the file consumption_proxies.py uses).
Usage: python3 -I analysis/liquid_fuel_2025/fuel_trend.py APS_XLSX          (repository root; APS_XLSX as downloaded by analysis/consumption_2025/consumption_proxies.py)
Writes analysis/liquid_fuel_2025/fuel_trend.csv: megalitres sold in the year to June, and litres per person (ABS estimated resident population at 30 June, data/sa2/population_erp.csv, to 2025)."""
import csv, datetime, os, sys
import openpyxl
ROOT = os.getcwd()
rows = list(openpyxl.load_workbook(sys.argv[1], read_only=True, data_only=True)['Sales of products'].iter_rows(values_only=True)); h = list(rows[0])
COLS = {'petrol': 'Automotive gasoline total (ML)', 'diesel': 'Diesel oil: total (ML)', 'jet': 'Aviation turbine fuel total (ML)', 'lpg_automotive': 'LPG Automotive use (ML)', 'all_products': 'Total (ML)'}
fy = {}
for r in rows[1:]:
    if isinstance(r[0], datetime.datetime):
        y = r[0].year + (1 if r[0].month >= 7 else 0); d = fy.setdefault(y, {'months': 0, **{k: 0.0 for k in COLS}}); d['months'] += 1
        for k, c in COLS.items():
            if isinstance(r[h.index(c)], (int, float)): d[k] += r[h.index(c)]
pop = {}
for r in csv.DictReader(open(os.path.join(ROOT, 'data/sa2/population_erp.csv'))):
    for y in range(2011, 2026): pop[y] = pop.get(y, 0.0) + float(r[str(y)] or 0)
with open(os.path.join(ROOT, 'analysis/liquid_fuel_2025/fuel_trend.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['year_to_june', 'months', 'population'] + [f'{k}_ML' for k in COLS] + [f'{k}_L_per_person' for k in COLS])
    for y in sorted(fy):
        d = fy[y]
        if d['months'] < 12: continue
        p = pop.get(y); w.writerow([y, d['months'], round(p) if p else ''] + [round(d[k], 1) for k in COLS] + [round(d[k] * 1e6 / p) if p else '' for k in COLS])
print('wrote fuel_trend.csv')
