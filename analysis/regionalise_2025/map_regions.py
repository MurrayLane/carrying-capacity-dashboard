#!/usr/bin/env python3
"""Map of an optimised regionalisation (data/regions/ideal_*.csv): region outlines over Australia, each region filled by its share of cropping land in its cropping plus pasture land (one sequential hue), so the
pairing of rangeland with cropping districts is visible. Usage: python3 -I analysis/regionalise_2025/map_regions.py SHAPEFILE.shp REGIONS.csv OUT.png        (needs geopandas, matplotlib)"""
import sys, csv
import geopandas as gpd, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
shp, reg, out = sys.argv[1:4]
g = gpd.read_file(shp); cc = next(c for c in g.columns if c.upper().startswith('SA2_CODE')); g[cc] = g[cc].astype(str)
region = {r['sa2_code']: r['region'] for r in csv.DictReader(open(reg))}
land = {r['sa2_code']: (float(r['cropping_km2']), float(r['pasture_km2'])) for r in csv.DictReader(open('data/sa2/land_2011_method_by_sa2.csv'))}
g = g[g[cc].isin(region)].copy(); g['region'] = g[cc].map(region)
g = g.to_crs(3577); g['geometry'] = g.geometry.simplify(2000)
d = g.dissolve(by='region'); d['crop'] = [sum(land[c][0] for c in g[g.region == i][cc]) for i in d.index]; d['past'] = [sum(land[c][1] for c in g[g.region == i][cc]) for i in d.index]
d['share'] = d.crop / (d.crop + d.past).clip(lower=1)
SURFACE, INK2 = '#fcfcfb', '#52514e'
cmap = LinearSegmentedColormap.from_list('seq', ['#e8f0fb', '#2a78d6', '#0b2f66'])
fig, ax = plt.subplots(figsize=(8.5, 7.2), facecolor=SURFACE); ax.set_facecolor(SURFACE)
d.plot(ax=ax, column='share', cmap=cmap, vmin=0, vmax=0.5, edgecolor=SURFACE, linewidth=0.6)
d.boundary.plot(ax=ax, color=INK2, linewidth=0.35)
ax.set_xlim(-2.1e6, 2.3e6); ax.set_ylim(-5.3e6, -1.0e6); ax.axis('off')
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, 0.5)); cb = fig.colorbar(sm, ax=ax, shrink=0.5, pad=0.01); cb.set_label('Cropping share of cropping plus pasture land', color=INK2); cb.ax.tick_params(colors=INK2)
ax.set_title(f'{len(d)} regions chosen to maximise the sum of capacities (contiguous, land cap {int(float(sys.argv[4]) if len(sys.argv) > 4 else 0):,} km2)' if len(sys.argv) > 4 else f'{len(d)} regions chosen to maximise the sum of capacities', loc='left', fontsize=10.5, color='#0b0b0b')
fig.savefig(out, dpi=170, facecolor=SURFACE, bbox_inches='tight'); print('written', len(d), 'regions')
