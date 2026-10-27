#!/usr/bin/env python3
"""Reads Australian Energy Statistics Table F1 (AUS sheet): liquid fuel consumed by industry, in petajoules, by financial year.
Usage as a module: from table_f import load; years, data = load(path)        data[block][fuel] = list of values aligned with years; blocks are the industry headings of the sheet."""
import openpyxl
LIQUID = ['LPG', 'Auto gasoline-leaded', 'Auto gasoline-unleaded', 'Aviation gasoline', 'Aviation turbine fuel', 'Kerosene and Heating oil', 'Diesel', 'Fuel oil',
          'Petroleum products nec', 'Solvents', 'Lubricants and greases', 'Bitumen']
def load(path):
    rows = list(openpyxl.load_workbook(path, read_only=True, data_only=True)['AUS'].iter_rows(values_only=True))
    lab = lambda r: next((v for v in r if isinstance(v, str)), None)
    c0 = next(c for c, v in enumerate(rows[5]) if isinstance(v, str)); years = [v for v in rows[5][c0:] if isinstance(v, str)]; n = len(years)
    data = {}
    for i, r in enumerate(rows):
        if i + 1 < len(rows) and lab(rows[i + 1]) == 'Fuels consumed' and lab(r):
            blk = {}; j = i + 2
            while j < len(rows) and lab(rows[j]) != 'Derived fuels produced':
                l = lab(rows[j])
                if l and l not in blk:
                    blk[l] = [float(v) if isinstance(v, (int, float)) else 0.0 for v in (list(rows[j]) + [None] * n)[c0:c0 + n]]       # blank years count as zero
                j += 1
            data[lab(r).strip()] = blk
    return years, data
