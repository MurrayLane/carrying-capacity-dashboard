#!/usr/bin/env python3
"""SA2 adjacency from the ABS ASGS Edition 3 (2021) SA2 digital boundaries, for the contiguity constraint of the regionalisation (analysis/regionalise_2025).
Usage: python3 -I analysis/regionalise_2025/sa2_adjacency.py SHAPEFILE.shp          (repository root; needs geopandas)
Source file: https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip
Writes data/sa2/adjacency.csv (sa2_a, sa2_b: polygons that share a boundary or lie within 200 m across a narrow water gap) and data/sa2/centroids.csv (sa2_code, lon, lat). Only the SA2s of data/sa2/land_2011_method_by_sa2.csv are kept."""
import sys, csv, os
import geopandas as gpd
shp = sys.argv[1]
g = gpd.read_file(shp)
code_col = next(c for c in g.columns if c.upper().startswith('SA2_CODE'))
keep = {r['sa2_code'] for r in csv.DictReader(open('data/sa2/land_2011_method_by_sa2.csv'))}
g[code_col] = g[code_col].astype(str); g = g[g[code_col].isin(keep)].reset_index(drop=True)
print(len(g), 'of', len(keep), 'SA2s matched to the boundaries')
miss = sorted(keep - set(g[code_col])); print('unmatched:', len(miss), miss[:10])
gm = g.to_crs(3577)                                                      # GDA94 Australian Albers, metres
geom = gm.geometry.simplify(200)                                         # 200 m: enough for adjacency, light to compute
buf = geom.buffer(200)
sidx = gm.sindex; pairs = set()
for i, b in enumerate(buf):
    for j in sidx.query(b, predicate='intersects'):
        if j > i and b.intersects(geom.iloc[j]): pairs.add((i, j))
codes = list(g[code_col])
with open('data/sa2/adjacency.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['sa2_a', 'sa2_b']); [w.writerow([codes[i], codes[j]]) for i, j in sorted(pairs)]
cent = gm.geometry.representative_point().to_crs(4326)
with open('data/sa2/centroids.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['sa2_code', 'lon', 'lat']); [w.writerow([c, round(p.x, 4), round(p.y, 4)]) for c, p in zip(codes, cent)]
# connected components (islands)
import collections
adj = collections.defaultdict(set)
for i, j in pairs: adj[i].add(j); adj[j].add(i)
seen, comps = set(), []
for s in range(len(codes)):
    if s in seen: continue
    st, c = [s], 0
    while st:
        x = st.pop()
        if x in seen: continue
        seen.add(x); c += 1; st.extend(adj[x] - seen)
    comps.append(c)
print(len(pairs), 'adjacent pairs; connected components:', len(comps), 'largest', max(comps), 'sizes of the others', sorted(comps)[:-1][-12:])
