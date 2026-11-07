#!/usr/bin/env python3
"""Section 10: the 2015 migration map redrawn on current data. Excess population = population minus capacity,
2025 corrected release (results/2025-fixed.csv), short term (average year), for the 53 regions.
Usage (repository root): python3 -I analysis/paper_a/migration_map.py   (writes migration_map.png at dpi 140 and migration_map.svg)
The repository holds no region polygons, so each region is a proportional circle at its centroid: the area-weighted mean of the SA2
centroids (data/sa2/centroids.csv) over the pieces of the region (data/nrm2011/land_use_by_sa2_nrm2011_piece.csv), regions merged as in
pipeline/land/zone_to_nrm2011.json. Grey dots are the SA2 centroids, drawn only to show the shape of the continent.
Circle area is proportional to the size of the excess; colour is a diverging two-hue scale with a neutral midpoint at zero (red over capacity,
blue under capacity); the colour step follows the square root of the excess so small regions are not all neutral."""
import csv, json, math
from collections import defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from matplotlib.lines import Line2D
import numpy as np

def rd(f): return list(csv.DictReader(open(f)))
zones = json.load(open('pipeline/land/zone_to_nrm2011.json'))['zones']
code2zone = {str(c): z for z, cs in zones.items() for c in cs}
sa2 = {r['sa2_code']: (float(r['lon']), float(r['lat'])) for r in rd('data/sa2/centroids.csv')}
seen, acc = set(), defaultdict(lambda: [0.0, 0.0, 0.0])
for r in rd('data/nrm2011/land_use_by_sa2_nrm2011_piece.csv'):
    key = (r['zone_name'], r['nrmr_code_2011'])  # the header names are shifted: zone_name holds the SA2 code
    if key in seen or r['zone_name'] not in sa2 or r['nrmr_code_2011'] not in code2zone: continue
    seen.add(key); a = float(r['area_km2']); lon, lat = sa2[r['zone_name']]
    z = code2zone[r['nrmr_code_2011']]; acc[z][0] += a * lon; acc[z][1] += a * lat; acc[z][2] += a
cent = {z: (v[0] / v[2], v[1] / v[2]) for z, v in acc.items()}
res = {r['zone']: r for r in rd('results/2025-fixed.csv') if r['preset'] == 'short'}
missing = [z for z in zones if z not in cent]
assert not missing, missing
data = {z: (res[z]['name'], float(res[z]['population']) - float(res[z]['capacity'])) for z in zones}
ex = np.array([v[1] for v in data.values()])
sq = lambda x: np.sign(x) * np.sqrt(np.abs(x))
norm = TwoSlopeNorm(vcenter=0, vmin=float(sq(ex.min())), vmax=float(sq(ex.max())))
cmap = plt.get_cmap('RdBu_r')
SCALE = 3.2e-4  # marker area (points squared) per person of excess
def area(x): return max(abs(x) * SCALE, 9)

fig, ax = plt.subplots(figsize=(11, 9.4))
ax.scatter([p[0] for p in sa2.values()], [p[1] for p in sa2.values()], s=1.2, color='#d9d9d9', zorder=1, linewidths=0)
order = sorted(data, key=lambda z: -abs(data[z][1]))  # big circles first so small ones stay visible
for z in order:
    name, x = data[z]; lon, lat = cent[z]
    ax.scatter(lon, lat, s=area(x), color=cmap(norm(float(sq(x)))), edgecolor='#444', linewidth=0.5, alpha=0.9, zorder=3)
CASES = {'5': (158.5, -33.0, 'left'), '10': (158.5, -37.0, 'left'), '9': (158.5, -41.0, 'left'),
         '57': (154.0, -46.0, 'left'), '50': (112.5, -37.0, 'left'), '46': (131.0, -19.5, 'center'), '43': (126.0, -39.0, 'center')}
for z, (tx, ty, ha) in CASES.items():
    name, x = data[z]; lon, lat = cent[z]
    ax.annotate(f'{name}\n{x:+,.0f} people', (lon, lat), xytext=(tx, ty), fontsize=7.5, ha=ha, va='center', zorder=5,
                arrowprops=dict(arrowstyle='-', color='#333', lw=0.6, shrinkB=2), bbox=dict(boxstyle='round,pad=0.25', fc='white', ec='#999', lw=0.5))
ax.set_aspect(1 / math.cos(math.radians(27))); ax.set_xlim(110, 172); ax.set_ylim(-48, -9)
ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
ax.set_title('Excess population by region, 2025: population minus short-term capacity, average year (corrected method)', fontsize=11, loc='left')
cb = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='horizontal', fraction=0.035, pad=0.02, aspect=45)
ticks = [-1e6, -1e5, 0, 1e5, 1e6, 5e6]
ticks = [t for t in ticks if sq(ex.min()) <= sq(t) <= sq(ex.max())]
cb.set_ticks([float(sq(t)) for t in ticks]); cb.set_ticklabels([f'{t:+,.0f}' if t else '0' for t in ticks], fontsize=7)
cb.set_label('population minus capacity (people); blue is room to spare, red is over capacity; colour step follows the square root', fontsize=8)
legend = [Line2D([], [], marker='o', ls='', markersize=math.sqrt(area(v)), markerfacecolor='#bbb', markeredgecolor='#444', label=f'{v:,.0f}') for v in (1e5, 1e6, 5e6)]
leg = ax.legend(handles=legend, title='Circle area: size of the excess (people)', loc='upper left', fontsize=7.5, title_fontsize=8, frameon=False, labelspacing=2.2, borderpad=1, handletextpad=2.5, borderaxespad=0.2)
over = int((ex > 0).sum())
fig.text(0.02, 0.06, f'53 regions (52 NRM regions and the Northern Territory); {over} over capacity. Circles sit at the area-weighted mean of SA2 centroids within each region (no polygons in the repository);\n'
         'grey dots are SA2 centroids. Source: results/2025-fixed.csv. The SA Arid Lands change since 2011 is a land-definition artefact (the 2025 figure shown here is the corrected-method value).', fontsize=6.5, va='top')
fig.savefig('analysis/paper_a/migration_map.png', dpi=140, bbox_inches='tight'); fig.savefig('analysis/paper_a/migration_map.svg', bbox_inches='tight')
top = sorted(data.values(), key=lambda t: -t[1])[:8]
print('ok', len(data), 'over', over); print([(n, int(x)) for n, x in top])
print('most under', [(n, int(x)) for n, x in sorted(data.values(), key=lambda t: t[1])[:5]])
