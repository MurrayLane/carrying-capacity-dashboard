#!/usr/bin/env python3
"""Paper A Figure 8: the migration map redrawn, population less short-term capacity by region, 2025, proportional circles on region centroids.
Run from anywhere: python3 -I analysis/figures_2025/paper_A/fig8_migration_map.py [--check [--expect 5.38]]
Data (no number typed in):
  analysis/paper_a/movers-3.csv  preset=short: zone, name, pop2025, cap2025 (excess = pop2025 - cap2025, people)
  centroids as in analysis/paper_a/migration_map.py: data/sa2/centroids.csv (SA2 lon, lat), data/nrm2011/land_use_by_sa2_nrm2011_piece.csv (area_km2 weights; the header names are shifted, zone_name holds the SA2 code),
  pipeline/land/zone_to_nrm2011.json (region pieces). The repository holds no region polygons, so each region is a circle at the area-weighted mean of its SA2 centroids; grey dots are all SA2 centroids.
Circle area is proportional to the size of the excess; colour is diverging (red over capacity, blue room to spare, neutral grey at zero), the colour step following the square root of the excess.
Over-capacity circles are labelled with a plus sign and filled; regions with room to spare carry a minus sign in their labels. Print size 190 mm wide."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *
from collections import defaultdict
import numpy as np
from matplotlib.colors import TwoSlopeNorm
from matplotlib.lines import Line2D
zones = json.load(open(os.path.join(ROOT, 'pipeline/land/zone_to_nrm2011.json')))['zones']
code2zone = {str(c): z for z, cs in zones.items() for c in cs}
sa2 = {r['sa2_code']: (float(r['lon']), float(r['lat'])) for r in rd('data/sa2/centroids.csv')}
seen, acc = set(), defaultdict(lambda: [0.0, 0.0, 0.0])
for r in rd('data/nrm2011/land_use_by_sa2_nrm2011_piece.csv'):
    key = (r['zone_name'], r['nrmr_code_2011'])
    if key in seen or r['zone_name'] not in sa2 or r['nrmr_code_2011'] not in code2zone: continue
    seen.add(key); a = float(r['area_km2']); lon, lat = sa2[r['zone_name']]; z = code2zone[r['nrmr_code_2011']]
    acc[z][0] += a * lon; acc[z][1] += a * lat; acc[z][2] += a
cent = {z: (v[0] / v[2], v[1] / v[2]) for z, v in acc.items()}
mov = regions(); assert all(r['zone'] in cent for r in mov)
ex = {r['zone']: float(r['pop2025']) - float(r['cap2025']) for r in mov}; nm = {r['zone']: r['name'] for r in mov}
if '--check' in sys.argv:
    # second route: excess of Port Phillip and Westernport from results/2025-fixed.csv (population less capacity), million
    r = next(x for x in rd('results/2025-fixed.csv') if x['preset'] == 'short' and x['name'] == 'Port Phillip and Westernport')
    check('Port Phillip and Westernport, population less short-term capacity, million', (float(r['population']) - float(r['capacity'])) / 1e6, ex['23'] / 1e6, 5.38, 2)
sq = lambda x: np.sign(x) * np.sqrt(np.abs(x))
vals = np.array(list(ex.values())); lim = float(sq(vals).__abs__().max())
norm = TwoSlopeNorm(vcenter=0, vmin=-lim, vmax=lim); cmap = div_cmap('blue')
SCALE = 1.4e-4
area = lambda x: max(abs(x) * SCALE, 4)
fig, ax = plt.subplots(figsize=(190 * MM, 124 * MM)); ax.set_facecolor(SURFACE)
ax.scatter([p[0] for p in sa2.values()], [p[1] for p in sa2.values()], s=1.6, color='#c3c2b7', linewidths=0, zorder=1)
for z in sorted(ex, key=lambda z: -abs(ex[z])):
    lon, lat = cent[z]
    ax.scatter(lon, lat, s=area(ex[z]), color=cmap(norm(float(sq(ex[z])))), edgecolor=INK2, linewidth=0.4, alpha=0.92, zorder=3)
over_top = sorted(ex, key=lambda z: -ex[z])[:5]; under_top = sorted(ex, key=lambda z: ex[z])[:5]
POS = {'23': (152.0, -43.5), '5': (158.5, -30.5), '36': (158.5, -27.5), '55': (105.0, -27.0), '41': (126.0, -45.0),
       '4': (158.5, -33.5), '7': (158.5, -36.5), '3': (158.5, -24.5), '27': (158.5, -21.5), '53': (105.0, -41.0)}
assert set(POS) == set(over_top) | set(under_top), (over_top, under_top)
for z, (tx, ty) in POS.items():
    lon, lat = cent[z]
    ax.annotate(f'{reg_label(nm[z])}\n{ex[z] / 1e6:+.1f} million', (lon, lat), xytext=(tx, ty), fontsize=7, ha='left', va='center', color=INK, zorder=6,
                arrowprops=dict(arrowstyle='-', color=INK2, lw=0.5, shrinkA=1, shrinkB=2))
ax.set_aspect(1 / math.cos(math.radians(27))); ax.set_xlim(104, 174); ax.set_ylim(-47, -10); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
over = int((vals > 0).sum())
leg = [Line2D([], [], marker='o', ls='', markersize=math.sqrt(area(v)), markerfacecolor=NEUTRAL, markeredgecolor=INK2, markeredgewidth=0.4, label=f'{v / 1e6:g} million') for v in (5e5, 1e6, 5e6)]
l1 = ax.legend(handles=leg, title='Circle area: size of the excess', loc='upper right', bbox_to_anchor=(1.0, 1.0), fontsize=7, title_fontsize=7, frameon=False, labelspacing=1.6, handletextpad=1.4, borderpad=0.2)
l1._legend_box.align = 'left'
cax = fig.add_axes([0.08, 0.1, 0.3, 0.025]); cb = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cax, orientation='horizontal'); cb.outline.set_visible(False)
tk = [t for t in (-1e6, -1e5, 0, 1e5, 1e6, 5e6) if -lim <= float(sq(t)) <= lim]
cb.set_ticks([float(sq(t)) for t in tk]); cb.set_ticklabels([f'{t / 1e6:+g}' if t else '0' for t in tk]); cb.ax.tick_params(labelsize=7, length=2)
cb.set_label('Population less capacity (million people)', fontsize=7, color=INK2, labelpad=2)
save(fig, 'fig8_migration_map')
cap = ('The migration map redrawn: population less short-term capacity in each of the 53 regions, 2025, corrected method, average year. Each region is a circle at the area-weighted mean of its SA2 centroids '
       '(the repository holds no region polygons; grey dots are SA2 centroids). Circle area is proportional to the size of the excess, in people; red is over capacity and blue is room to spare, with a neutral grey at zero '
       'and the colour step following the square root of the excess. Sources: analysis/paper_a/movers-3.csv; centroids from data/sa2/centroids.csv and data/nrm2011/land_use_by_sa2_nrm2011_piece.csv.')
register('Figure 8', 'fig8_migration_map.png; fig8_migration_map.svg', 'analysis/paper_a/movers-3.csv; data/sa2/centroids.csv; data/nrm2011/land_use_by_sa2_nrm2011_piece.csv; pipeline/land/zone_to_nrm2011.json',
         'movers-3: zone, name, preset=short, pop2025, cap2025; centroids: sa2_code, lon, lat; piece file: zone_name (SA2 code), nrmr_code_2011, area_km2', cap, 'CLAIMS_PLACEHOLDER')
print('Figure 8:', len(ex), 'regions,', over, 'over capacity; top over', [(nm[z], round(ex[z] / 1e6, 2)) for z in over_top])
