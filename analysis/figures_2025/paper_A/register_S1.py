#!/usr/bin/env python3
"""Supplementary Figure S1: registers the 300 dpi map in figures.csv; it does not redraw it.
The files figS1_regions.png (300 dpi), figS1_regions.svg and figS1_regions.pdf are drawn by analysis/regionalise_2025/map_regions.py from the ABS ASGS Edition 3 (2021) SA2 shapefile
(data/asgs_sa2_2021/, sources register id D59). From the repository root:
python3 -I analysis/regionalise_2025/map_regions.py data/asgs_sa2_2021/extracted/SA2_2021_AUST_GDA2020.shp data/regions/ideal_2025-fixed_short_K53_cap650k.csv analysis/figures_2025/paper_A/figS1_regions.png 650000 --dpi 300
Run from anywhere: python3 -I analysis/figures_2025/paper_A/register_S1.py
Check: python3 -I analysis/figures_2025/paper_A/register_S1.py --check [--expect N]  (the number of regions in the regions csv, counted here, must equal the 53 the figure draws and the expected value)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *
REGIONS_CSV = 'data/regions/ideal_2025-fixed_short_K53_cap650k.csv'
if '--check' in sys.argv:
    n = len({r['region'] for r in rd(REGIONS_CSV)})
    check('Figure S1 region count', n, 53, 53, digits=0)
cap = [l for l in open(os.path.join(ROOT, 'papers/A_results/draft/supplementary.md'), encoding='utf-8').read().split('\n') if l.startswith('Supplementary Figure S1.')][0]
cap = cap.replace(' The image is 1,100 by 1,021 pixels at 170 dpi, a lower resolution than the other figures (Section S11 names the file).', '')
cap += ' Sources: ' + REGIONS_CSV + ', data/sa2/land_2011_method_by_sa2.csv, analysis/regionalise_2025/summary.csv; boundaries from the ABS ASGS Edition 3 (2021) SA2 shapefile, data/asgs_sa2_2021/SA2_2021_AUST_SHP_GDA2020.zip (sources register D59).'
register('Figure S1', 'figS1_regions.png (300 dpi); figS1_regions.svg; figS1_regions.pdf',
         REGIONS_CSV + '; data/sa2/land_2011_method_by_sa2.csv; analysis/regionalise_2025/summary.csv; boundaries data/asgs_sa2_2021/SA2_2021_AUST_SHP_GDA2020.zip (D59)',
         'ideal csv: sa2_code, region; land csv: sa2_code, cropping_km2, pasture_km2', cap, 'A124 A347 A348 A349')
print('Figure S1 registered (300 dpi png, svg, pdf)')
