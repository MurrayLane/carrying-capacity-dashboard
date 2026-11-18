#!/usr/bin/env python3
"""Fills the 'claims rows' column of figures.csv (read-only use of qa/claims_register.csv): a claims row is listed for a figure when its output_file is one of the figure's source csvs
(exact path; the register's output_file may hold several paths separated by semicolons or spaces). Run after the figure scripts: python3 -I analysis/figures_2025/paper_A/finalize_figures_csv.py"""
import sys, os, csv, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *
claims = [r for r in rd('qa/claims_register.csv') if r['paper'] == 'A']
path = os.path.join(HERE, 'figures.csv'); rows = list(csv.DictReader(open(path, newline='')))
for r in rows:
    srcs = [s.strip() for s in r['source csv'].split(';')]
    ids = [c['id'] for c in claims if any(s in re.split(r'[;\s,]+', c['output_file']) for s in srcs)]
    r['claims rows'] = ' '.join(ids) if ids else 'none matched by output_file'
with open(path, 'w', newline='') as f:
    w = csv.DictWriter(f, FIG_COLS); w.writeheader(); w.writerows(rows)
for r in rows: print(r['figure'], len(r['claims rows'].split()), r['claims rows'][:90])
