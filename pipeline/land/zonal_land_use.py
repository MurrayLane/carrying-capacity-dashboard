#!/usr/bin/env python3
"""Area of each land use class in each SA2: a zonal histogram of the ABARES Catchment Scale Land Use raster (December 2023, 50 m, ALUM version 8).

Usage: python3 zonal_land_use.py RASTER.tif POLYGONS OUT_DIR [ID_COL NAME_COL EXTRA_COLS OUT_NAME]
  default layer: SA2_2021_AUST_GDA2020.shp, columns SA2_CODE21 SA2_NAME21 and SA3_CODE21,SA4_CODE21,STE_CODE21 -> land_use_by_sa2.csv
  2011 NRM regions (the thesis zones, archive file NRMR_2011_AUST.mif): ID_COL NRMR_CODE_2011 NAME_COL NRMR_NAME_2011 EXTRA_COLS AREA_ALBERS_SQKM OUT_NAME land_use_by_nrm2011.csv
Needs rasterio, geopandas, numpy, pandas (a virtual environment; not part of the CI).

Writes OUT_DIR/land_use_by_sa2.csv (sa2_code, sa2_name, sa3_code, sa4_code, state, class_code, km2). The class table is the raster's .vat.dbf, copied to data/sa2/clum_classes.csv.
The raster is in GDA94 Australian Albers (EPSG:3577), an equal-area projection, so a 50 m cell is exactly 0.0025 km2. The SA2 polygons are
reprojected to it and burned into the raster block by block; a cell takes the SA2 whose polygon contains its centre. The ABARES raster was itself
cut with the 2021 SA2 mask, so the two layers share their edge. The mapping from classes to the model's five land types is a separate, reviewable
file (land_types.json); nothing here depends on it.
"""
import os, sys, time
import numpy as np, pandas as pd, geopandas as gpd, rasterio
from shapely.geometry import box
from rasterio.features import rasterize
from rasterio.windows import Window
from rasterio.windows import transform as wtransform

raster, shp, out = sys.argv[1:4]; os.makedirs(out, exist_ok=True)
ID, NAME, EXTRA, OUT_NAME = (sys.argv[4:8] + [None] * 4)[:4] if len(sys.argv) > 4 else ('SA2_CODE21', 'SA2_NAME21', 'SA3_CODE21,SA4_CODE21,STE_CODE21', 'land_use_by_sa2.csv')
EXTRA = EXTRA.split(',')
NAMES = ['sa2_code', 'sa2_name', 'sa3_code', 'sa4_code', 'state'] if len(sys.argv) <= 4 else ['zone_code', 'zone_name'] + [c.lower() for c in EXTRA]
CELL_KM2 = 50 * 50 / 1e6
BLOCK = 1024
sa2 = gpd.read_file(shp)
src = rasterio.open(raster)
sa2 = sa2[sa2.geometry.notna() & ~sa2.geometry.is_empty].to_crs(src.crs).reset_index(drop=True)
sa2['idx'] = np.arange(1, len(sa2) + 1)
assert len(sa2) < 65535
K = 1024                                                     # class codes are below 1000
sindex = sa2.sindex
counts = np.zeros((len(sa2) + 1, K), dtype=np.int64)
t0 = time.time()
for row in range(0, src.height, BLOCK):
    h = min(BLOCK, src.height - row); win = Window(0, row, src.width, h)
    a = src.read(1, window=win)
    tr = wtransform(win, src.transform)
    left, top = tr * (0, 0); right, bottom = tr * (src.width, h)
    cand = sa2.iloc[sindex.query(box(left, bottom, right, top), predicate='intersects')]
    if cand.empty: continue
    ids = rasterize(((g, int(i)) for g, i in zip(cand.geometry, cand.idx)), out_shape=(h, src.width), transform=tr, fill=0, dtype='uint16')
    valid = (ids > 0) & (a < K)
    key = ids[valid].astype(np.int64) * K + a[valid].astype(np.int64)
    counts += np.bincount(key, minlength=(len(sa2) + 1) * K).reshape(len(sa2) + 1, K)
    if (row // BLOCK) % 8 == 0: print(f'row {row}/{src.height}  {time.time() - t0:.0f}s', flush=True)
rows = []
for i in range(1, len(sa2) + 1):
    for code in np.nonzero(counts[i])[0]:
        rows.append((sa2.at[i - 1, ID], sa2.at[i - 1, NAME], *[sa2.at[i - 1, c] for c in EXTRA], int(code), round(counts[i, code] * CELL_KM2, 4)))
pd.DataFrame(rows, columns=NAMES + ['class_code', 'km2']).to_csv(os.path.join(out, OUT_NAME), index=False)
print('done', len(rows), 'rows', f'{time.time() - t0:.0f}s')
