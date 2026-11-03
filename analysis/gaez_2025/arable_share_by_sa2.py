#!/usr/bin/env python3
"""Share of each SA2 that is arable on GAEZ v4 (Murray 2026-11-03: is improved pasture able to be used for crops?). For every 5 arc minute cell, the share of the cell assessed as very suitable, suitable or moderately
suitable (variable sx2Hr, rainfed, high input, 1981-2010; 0 to 10000) for wheat, barley and rapeseed, the largest of the three; the SA2's value is the mean over the cells whose centre lies in it (the nearest
cell for SA2s with none). Applied to the SA2's improved pasture it gives the share of that pasture on arable land: a regional rule from a model, not a measurement of what farmers do.
Usage: python3 -I analysis/gaez_2025/arable_share_by_sa2.py TIF_DIR SA2_SHAPEFILE.shp          (repository root; needs numpy, tifffile, geopandas). Writes data/sa2/arable_share_gaez_by_sa2.csv."""
import sys, os, csv
import numpy as np, tifffile, geopandas as gpd
from shapely.geometry import Point
D, shp = sys.argv[1:3]
arr = np.max([tifffile.imread(os.path.join(D, f'sx2Hr_{c}.tif')).astype(float) for c in ('whe', 'brl', 'rsd')], axis=0)
arr = np.where(arr < 0, np.nan, arr) / 10000.0
g = gpd.read_file(shp); cc = next(c for c in g.columns if c.upper().startswith('SA2_CODE')); g[cc] = g[cc].astype(str)
keep = {r['sa2_code'] for r in csv.DictReader(open('data/sa2/land_2011_method_by_sa2.csv'))}; g = g[g[cc].isin(keep)].to_crs(4326).reset_index(drop=True)
rows, cols = np.where(np.isfinite(arr[int((90 - (-9)) * 12):int((90 - (-45)) * 12), int((112 + 180) * 12):int((155 + 180) * 12)]))
r0, c0 = int((90 - (-9)) * 12), int((112 + 180) * 12)
lat = 90 - (rows + r0 + 0.5) / 12; lon = (cols + c0 + 0.5) / 12 - 180; val = arr[rows + r0, cols + c0]
pts = gpd.GeoDataFrame({'v': val}, geometry=[Point(x, y) for x, y in zip(lon, lat)], crs=4326)
j = gpd.sjoin(pts, g[[cc, 'geometry']], predicate='within'); m = j.groupby(cc)['v'].mean()
need = g[~g[cc].isin(m.index)].copy()
if len(need):
    cen = need.copy(); cen['geometry'] = need.to_crs(3577).geometry.representative_point().to_crs(4326)
    nj = gpd.sjoin_nearest(cen[[cc, 'geometry']], pts.to_crs(4326), how='left'); m = m.combine_first(nj.set_index(cc)['v'])
with open('data/sa2/arable_share_gaez_by_sa2.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['sa2_code', 'arable_share_gaez']); [w.writerow([c, round(float(m.get(c, np.nan)), 4)]) for c in g[cc]]
imp = {r['sa2_code']: float(r['improved_km2']) for r in csv.DictReader(open('data/sa2/improved_pasture_by_sa2.csv'))}
num = sum(float(m.get(c, 0) or 0) * imp.get(c, 0) for c in g[cc]); den = sum(imp.get(c, 0) for c in g[cc])
print(len(g), 'SA2s;', len(need), 'with no cell centre (nearest cell used); national arable share of improved pasture:', round(num / den, 3), '| mean over all SA2s:', round(float(np.nanmean(m.values)), 3))
