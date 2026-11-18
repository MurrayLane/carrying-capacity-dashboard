#!/usr/bin/env python3
"""Paper A Figure 4: the scale curve, sum of unit capacities as a share of national capacity, 2011 and 2025, short and long term, state-yield basis.
Run from anywhere: python3 -I analysis/figures_2025/paper_A/fig4_scale_curve.py [--check [--expect 37]]
Data (no number typed in):
  results/scale_curve.csv  release in (2011-fixed, 2025-fixed), yield_basis=state; columns level, units, sum_capacity, share_of_national, preset
  analysis/scale_curve_2025/scale_partition_summary.csv  grouping=uniform (7 random groups of SA2s, same state-yield basis), release 2011-fixed-3 / 2025-fixed; p5, p95 -> shaded range at the State level
Circles join the administrative levels; diamonds are the NRM regions (53 catchments, not joined). Layout follows analysis/scale_curve_2025/plot_scale_curve.py. Print size 190 mm wide."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
rows = rd('results/scale_curve.csv'); part = rd('analysis/scale_curve_2025/scale_partition_summary.csv')
LEVELS = ['Australia', 'State', 'NRM region', 'SA4', 'SA3', 'SA2']; ADMIN = ['Australia', 'State', 'SA4', 'SA3', 'SA2']
REL = {2011: ('2011-fixed', '2011-fixed-3'), 2025: ('2025-fixed', '2025-fixed')}
def get(rel, pr, lvl):
    r = next(x for x in rows if x['release'] == rel and x['preset'] == pr and x['level'] == lvl and x['yield_basis'] == 'state'); return float(r['share_of_national']) * 100, int(r['units'])
def band(rel, pr):
    r = next(x for x in part if x['release'] == rel and x['preset'] == pr and x['grouping'] == 'uniform'); return float(r['p5']) * 100, float(r['p95']) * 100
if '--check' in sys.argv:
    # second route: SA2 share = sum over 2,450 SA2 units / national total on the same (SA land) basis, from sum_capacity
    s = {r['level']: float(r['sum_capacity']) for r in rows if r['release'] == '2025-fixed' and r['preset'] == 'short' and r['yield_basis'] == 'state'}
    alt = 100 * s['SA2'] / s['Australia (SA land)']
    check('2025 SA2 sum of capacities as % of national, short term', alt, get('2025-fixed', 'short', 'SA2')[0], 37, 0, tol=2e-3)  # csv share is rounded to 3 decimals
units = {l: get('2025-fixed', 'short', l)[1] for l in LEVELS}; xs = {l: i for i, l in enumerate(LEVELS)}
fig, axes = plt.subplots(1, 2, figsize=(190 * MM, 82 * MM), sharey=True)
for ax, (pr, title) in zip(axes, [('short', 'Short term'), ('long', 'Long term')]):
    style_ax(ax, grid='y'); ax.set_title(title, loc='left', fontsize=8, fontweight='bold')
    for yr in (2011, 2025):
        rel, prel = REL[yr]; col = YEAR_COL[yr]
        pts = {l: get(rel, pr, l)[0] for l in LEVELS}
        lo, hi = band(prel, pr); dx = -0.17 if yr == 2011 else 0.17
        ax.fill_between([xs['State'] + dx - 0.12, xs['State'] + dx + 0.12], lo, hi, color=col, alpha=0.18, linewidth=0, zorder=1)
        ax.plot([xs[l] for l in ADMIN], [pts[l] for l in ADMIN], color=col, lw=1.2, zorder=3)
        ax.scatter([xs[l] for l in ADMIN], [pts[l] for l in ADMIN], s=22, color=col, edgecolor=SURFACE, linewidth=0.8, zorder=4)
        ax.scatter([xs['NRM region'] + (-0.08 if yr == 2011 else 0.08)], [pts['NRM region']], s=26, marker='D', color=col, edgecolor=SURFACE, linewidth=0.8, zorder=4)
        other = get('2011-fixed' if yr == 2025 else '2025-fixed', pr, 'SA2')[0]
        ax.text(xs['SA2'] + 0.15, pts['SA2'] + (4 if pts['SA2'] >= other else -4), f"{yr}: {pts['SA2']:.0f}%", va='center', ha='left', fontsize=7, color=INK)
    ax.set_xticks([xs[l] for l in LEVELS]); ax.set_xticklabels([f'{l}\n{units[l]:,}' for l in LEVELS], fontsize=7)
    ax.set_xlim(-0.4, 6.0); ax.set_ylim(0, 130); ax.set_yticks([0, 25, 50, 75, 100, 125]); ax.set_yticklabels([f'{v}%' for v in (0, 25, 50, 75, 100, 125)])
    ax.axhline(100, color=AXIS, lw=0.8, zorder=2)
axes[0].set_ylabel('Sum of unit capacities, share of national')
h = [Line2D([], [], color=BLUE, lw=1.2, marker='o', ms=4.5, mec=SURFACE, label='2011'), Line2D([], [], color=ORANGE, lw=1.2, marker='o', ms=4.5, mec=SURFACE, label='2025'),
     Line2D([], [], color=INK2, lw=0, marker='o', ms=4.5, label='administrative units (joined)'), Line2D([], [], color=INK2, lw=0, marker='D', ms=4.5, label='NRM regions (catchments)'),
     Patch(facecolor=INK2, alpha=0.2, label='7 random groups of SA2s, 5th to 95th percentile (shaded, at the State level)')]
fig.legend(handles=h, loc='lower center', ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.0), fontsize=7, columnspacing=1.6, handlelength=1.8)
fig.subplots_adjust(left=0.075, right=0.985, top=0.93, bottom=0.30, wspace=0.05)
save(fig, 'fig4_scale_curve')
cap = ('The scale curve: the sum of the units\' capacities as a share of the national capacity at each level from the nation to SA2, 2011 and 2025, short and long term, state-yield basis, corrected method. '
       'Each unit takes the yields, climate zone and settings of its state and the national diet and waste settings; the number of units is under each level. Circles join the administrative levels; diamonds are the 53 NRM regions. '
       'The shaded bar at the State level is the 5th to 95th percentile of the same sum over 200 random groupings of the SA2s into 7 groups, the partition effect without the real state boundaries. '
       'The SA levels use 2020-21 land with each year\'s population. Sources: results/scale_curve.csv, analysis/scale_curve_2025/scale_partition_summary.csv.')
register('Figure 4', 'fig4_scale_curve.png; fig4_scale_curve.svg', 'results/scale_curve.csv; analysis/scale_curve_2025/scale_partition_summary.csv',
         'scale_curve: release, preset, level, units, sum_capacity, share_of_national, yield_basis=state; scale_partition_summary: release, preset, grouping=uniform, p5, p95', cap, 'CLAIMS_PLACEHOLDER')
print('Figure 4:', {(y, pr): round(get(REL[y][0], pr, 'SA2')[0]) for y in (2011, 2025) for pr in ('short', 'long')})
