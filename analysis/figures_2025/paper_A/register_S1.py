#!/usr/bin/env python3
"""Supplementary Figure S1: registers the existing image in figures.csv; it does not redraw it.
The image analysis/regionalise_2025/ideal_K53_cap650k.png (1,100 by 1,021 pixels, 170 dpi) is drawn by analysis/regionalise_2025/map_regions.py, which needs the ABS ASGS SA2 boundary shapefile
(argument SHAPEFILE.shp). No shapefile is in the repository or on this machine and there is no network, so the image cannot be regenerated at 300 dpi here, and no PDF is made (a PDF of the 170 dpi
raster would add no resolution). To regenerate where the shapefile is held: python3 -I analysis/regionalise_2025/map_regions.py SHAPEFILE.shp data/regions/ideal_2025-fixed_short_K53_cap650k.csv OUT.png 650000
after raising dpi=170 to 300 in that script (outside this folder, so not edited here).
Run from anywhere: python3 -I analysis/figures_2025/paper_A/register_S1.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *
cap = [l for l in open(os.path.join(ROOT, 'papers/A_results/draft/supplementary.md'), encoding='utf-8').read().split('\n') if l.startswith('Supplementary Figure S1.')][0]
cap += ' Sources: data/regions/ideal_2025-fixed_short_K53_cap650k.csv, data/sa2/land_2011_method_by_sa2.csv, analysis/regionalise_2025/summary.csv; boundaries from the ABS ASGS SA2 shapefile (not held in the repository).'
register('Figure S1', 'analysis/regionalise_2025/ideal_K53_cap650k.png (existing image, 170 dpi; not regenerated here)',
         'data/regions/ideal_2025-fixed_short_K53_cap650k.csv; data/sa2/land_2011_method_by_sa2.csv; analysis/regionalise_2025/summary.csv',
         'ideal csv: sa2_code, region; land csv: sa2_code, cropping_km2, pasture_km2', cap, 'A124 A347 A348 A349')
print('Figure S1 registered (image not regenerated: no SA2 shapefile)')
