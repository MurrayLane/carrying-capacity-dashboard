#!/usr/bin/env python3
"""Builds the meat-window matrices for the long-window Monte Carlo (MC_WIN_DIR, defect X069): the base window (base_off), the two short windows
(meat_3y, meat_early, kept as a check) and the four full-cycle windows meat_8y (2017-18 to 2024-25), meat_10y (2015-16 to 2024-25), meat_15y (2010-11 to 2024-25)
and meat_20y (2005-06 to 2024-25), with the same yield_variant calls as build_variants.py (crop matrix copied from data/2025, livestock_zone.py with LS_YEARS),
all with LS_SERIES=off.
Inputs: the ABS herd, flock and meat files of analysis/recent_data/fetch_recent.py (ABS_DIR: AALDC_Cattle_herd_series_2005_to_2025.xlsx,
  AALDC_Sheep_flock_series_2005_to_2025.xlsx, 7215009.xlsx to 7215012.xlsx), data/2025/yield_matrix.csv and crop_yields_by_year.json.
Why LS_SERIES=off: the direct build on the current base (series on) cannot make the full-cycle windows, because data/2025/livestock_national_series.csv
  (wool, cattle on feed, milk by state) has figures for 2009-10 and 2020-21 to 2024-25 only; the years 2005-06 to 2019-20 are missing and livestock_zone.py stops.
  With LS_SERIES=off every window, the base window included, uses the placeholders (wool and feedlot grain scaled by the flock and herd, milk by the dairy herd),
  so the windows are consistent with each other but not with the base matrix in rows 96 to 98; make_win.py takes the difference to the base window and adds it to the base matrix.
Usage (repository root): python3 -I analysis/sensitivity_2025/rebuild_off.py OFF_DIR ABS_DIR      then make_win.py OFF_DIR WIN_DIR"""
import os, shutil, subprocess, sys
WORK, ABS = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]); os.makedirs(WORK, exist_ok=True)
ROOT = os.getcwd(); PY = [sys.executable, '-I']
def run(script, env, *args):
    subprocess.run(PY + [os.path.join(ROOT, 'pipeline/yields/recent', script), *args], env={**os.environ, **env}, check=True, stdout=subprocess.DEVNULL, cwd=ROOT)
def yield_variant(vid, ls_env):
    d = os.path.join(WORK, vid); os.makedirs(d, exist_ok=True)
    for f in ('yield_matrix.csv', 'crop_yields_by_year.json'): shutil.copy(os.path.join(ROOT, 'data/2025', f), d)
    run('livestock_zone.py', {**ls_env, 'LS_SERIES': 'off', 'ZY_OUT': d}, ABS)
def yrs(a, b): return ','.join(f'{y - 1}-{str(y)[2:]}' for y in range(a, b + 1))
yield_variant('base_off', {})
yield_variant('meat_3y', {'LS_YEARS': '2022-23,2023-24,2024-25'})
yield_variant('meat_early', {'LS_YEARS': '2020-21,2021-22,2022-23'})
for vid, a in (('meat_8y', 2018), ('meat_10y', 2016), ('meat_15y', 2011), ('meat_20y', 2006)): yield_variant(vid, {'LS_YEARS': yrs(a, 2025)})
print('built in', WORK)
