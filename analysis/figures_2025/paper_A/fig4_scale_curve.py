#!/usr/bin/env python3
"""Paper A Figure 4: the scale curve, sum of unit capacities as a share of national capacity, 2011 and 2025, short and long term, state-yield basis.
Run from anywhere: python3 -I analysis/figures_2025/paper_A/fig4_scale_curve.py [--check [--expect 37]]
Data (no number typed in):
  results/scale_curve.csv  release in (2011-fixed, 2025-fixed), yield_basis=state; columns level, units, sum_capacity, share_of_national, preset
  analysis/scale_curve_2025/scale_partition_summary.csv  grouping=uniform (7 random groups of SA2s, same state-yield basis), release 2011-fixed-3 / 2025-fixed; p5, p95 -> shaded range at the State level
Circles join the administrative levels; diamonds are the NRM regions (the 53 regions, not joined). Layout follows analysis/scale_curve_2025/plot_scale_curve.py. Print size 190 mm wide."""
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
def band(rel, pr, grouping='uniform'):
    r = next(x for x in part if x['release'] == rel and x['preset'] == pr and x['grouping'] == grouping); return float(r['p5']) * 100, float(r['p95']) * 100
units = {l: get('2025-fixed', 'short', l)[1] for l in LEVELS}; xs = {l: i for i, l in enumerate(LEVELS)}
fig, axes = plt.subplots(1, 2, figsize=(190 * MM, 82 * MM), sharey=True)
for ax, (pr, title) in zip(axes, [('short', 'Short term'), ('long', 'Long term')]):
    style_ax(ax, grid='y'); ax.set_title(title, loc='left', fontsize=8, fontweight='bold')
    for yr in (2011, 2025):
        rel, prel = REL[yr]; col = YEAR_COL[yr]
        pts = {l: get(rel, pr, l)[0] for l in LEVELS}
        dx = -0.30 if yr == 2011 else 0.12
        lo, hi = band(prel, pr)                                                    # state-yield basis (the basis of the curve)
        ax.fill_between([xs['State'] + dx - 0.05, xs['State'] + dx + 0.05], lo, hi, color=col, alpha=0.30, linewidth=0, zorder=1)
        lo2, hi2 = band(prel, pr, 'uniform_national_yield_reference')              # national-yield reference: the land-mix effect alone
        ax.fill_between([xs['State'] + dx + 0.10, xs['State'] + dx + 0.20], lo2, hi2, facecolor='none', edgecolor=col, hatch='/////', linewidth=0, zorder=1)
        ln = ax.plot([xs[l] for l in ADMIN], [pts[l] for l in ADMIN], color=col, lw=1.2, zorder=3)[0]
        if yr == 2025 and pr == 'short': line25 = ln
        ax.scatter([xs[l] for l in ADMIN], [pts[l] for l in ADMIN], s=22, color=col, edgecolor=SURFACE, linewidth=0.8, zorder=4)
        ax.scatter([xs['NRM region'] + (-0.08 if yr == 2011 else 0.08)], [pts['NRM region']], s=26, marker='D', color=col, edgecolor=SURFACE, linewidth=0.8, zorder=4)
        other = get('2011-fixed' if yr == 2025 else '2025-fixed', pr, 'SA2')[0]
        ax.text(xs['SA2'] + 0.15, pts['SA2'] + (4 if pts['SA2'] >= other else -4), f"{yr}: {pts['SA2']:.0f}%", va='center', ha='left', fontsize=7, color=INK)
    ax.set_xticks([xs[l] for l in LEVELS]); ax.set_xticklabels([f'{l}\n{units[l]:,}' for l in LEVELS], fontsize=7)
    ax.set_xlim(-0.4, 6.0); ax.set_ylim(0, 130); ax.set_yticks([0, 25, 50, 75, 100, 125]); ax.set_yticklabels([f'{v}%' for v in (0, 25, 50, 75, 100, 125)])
    ax.axhline(100, color=AXIS, lw=0.8, zorder=2)
axes[0].set_ylabel('Sum of unit capacities, share of national')
h = [Line2D([], [], color=BLUE, lw=1.2, marker='o', ms=4.5, mec=SURFACE, label='2011'), Line2D([], [], color=ORANGE, lw=1.2, marker='o', ms=4.5, mec=SURFACE, label='2025'),
     Line2D([], [], color=INK2, lw=0, marker='o', ms=4.5, label='administrative units (joined)'), Line2D([], [], color=INK2, lw=0, marker='D', ms=4.5, label='NRM regions (not joined)'),
     Patch(facecolor=INK2, alpha=0.3, label='53 regions in 7 random groups, state-yield basis, 5th to 95th percentile (solid bar at State)'),
     Patch(facecolor='none', edgecolor=INK2, hatch='/////', label='same groups on the national-yield reference (hatched bar at State)')]
fig.legend(handles=h, loc='lower center', ncol=2, frameon=False, bbox_to_anchor=(0.5, 0.0), fontsize=7, columnspacing=1.6, handlelength=1.8)
fig.subplots_adjust(left=0.075, right=0.985, top=0.93, bottom=0.36, wspace=0.05)
save(fig, 'fig4_scale_curve')
caption = caption_for('Figure 4')
register('Figure 4', 'fig4_scale_curve.png; fig4_scale_curve.svg; fig4_scale_curve.pdf', 'results/scale_curve.csv; analysis/scale_curve_2025/scale_partition_summary.csv',
         'scale_curve: release, preset, level, units, sum_capacity, share_of_national, yield_basis=state; scale_partition_summary: release, preset, grouping=uniform, p5, p95', caption, 'A015 A016 A017 A018 A074 A075 A120 A458 A459')
if '--check' in sys.argv:
    # second route: SA2 sum over the national total on the same (SA land) basis, from sum_capacity; the plotted value is the end of the plotted 2025 short-term line
    t = {r['level']: float(r['sum_capacity']) for r in rows if r['release'] == '2025-fixed' and r['preset'] == 'short' and r['yield_basis'] == 'state'}
    check('2025 SA2 sum of capacities as % of national, short term (read from the plotted line)', 100 * t['SA2'] / t['Australia (SA land)'], float(line25.get_ydata()[-1]), 37, 0, tol=2e-3)
print('Figure 4:', {(y, pr): round(get(REL[y][0], pr, 'SA2')[0]) for y in (2011, 2025) for pr in ('short', 'long')})
