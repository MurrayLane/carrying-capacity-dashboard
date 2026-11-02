#!/usr/bin/env python3
"""Figure for the results paper: capacity as a share of the national capacity, as the unit of self-sufficiency shrinks (results/scale_curve.csv).
Usage: python3 -I analysis/scale_curve_2025/plot_scale_curve.py          (repository root; needs matplotlib)
Corrected method (2011-fixed, 2025-fixed), short and long term. Circles: administrative units (Australia, states, SA4, SA3, SA2) joined by a line; diamonds: the NRM regions (catchments), not joined, so
their position against the line shows the boundary effect. Colours: the dataviz skill's validated categorical slots 1 and 2 (light surface); the figure is static (print), the table is results/scale_curve.csv."""
import csv, os
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT = os.getcwd(); OUT = os.path.join(ROOT, 'analysis/scale_curve_2025')
SURFACE, INK, INK2, GRID, BLUE, ORANGE = '#fcfcfb', '#0b0b0b', '#52514e', '#e4e3df', '#2a78d6', '#eb6834'
rows = list(csv.DictReader(open(os.path.join(ROOT, 'results/scale_curve.csv'))))
LEVELS = ['Australia', 'State', 'NRM region', 'SA4', 'SA3', 'SA2']; ADMIN = ['Australia', 'State', 'SA4', 'SA3', 'SA2']
def get(rel, pr, lvl):
    r = next(x for x in rows if x['release'] == rel and x['preset'] == pr and x['level'] == lvl); return float(r['share_of_national']) * 100, int(r['units'])
units = {l: get('2025-fixed', 'short', l)[1] for l in LEVELS}; xs = {l: i for i, l in enumerate(LEVELS)}
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10, 'text.color': INK, 'axes.edgecolor': INK2, 'axes.labelcolor': INK2, 'xtick.color': INK2, 'ytick.color': INK2})
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.6), sharey=True, facecolor=SURFACE)
for ax, (pr, title) in zip(axes, [('short', 'Short term (today\'s consumption and production)'), ('long', 'Long term (low-meat, organic, 100-year drought allowance)')]):
    ax.set_facecolor(SURFACE); ax.set_title(title, fontsize=10, color=INK, loc='left', pad=10)
    for rel, col, lab, dy in (('2011-fixed', BLUE, '2011', 0), ('2025-fixed', ORANGE, '2025', 0)):
        pts = {l: get(rel, pr, l)[0] for l in LEVELS}
        ax.plot([xs[l] for l in ADMIN], [pts[l] for l in ADMIN], color=col, lw=2, solid_capstyle='round', zorder=3)
        ax.scatter([xs[l] for l in ADMIN], [pts[l] for l in ADMIN], s=64, color=col, edgecolor=SURFACE, linewidth=2, zorder=4)
        ax.scatter([xs['NRM region'] + (-0.07 if rel == '2011-fixed' else 0.07)], [pts['NRM region']], s=84, marker='D', color=col, edgecolor=SURFACE, linewidth=2, zorder=4)      # offset so equal values do not hide each other
        ax.text(xs['SA2'] + 0.12, pts['SA2'] + (2.4 if rel == '2025-fixed' else -2.4), f"{lab}  {pts['SA2']:.0f}%", color=INK, va='center', ha='left', fontsize=9.5)
    ax.set_xticks(range(len(LEVELS))); ax.set_xticklabels([f"{l}\n{units[l]:,}" for l in LEVELS], fontsize=8.5)
    ax.set_xlim(-0.3, 6.1); ax.set_ylim(0, 108); ax.set_yticks([0, 25, 50, 75, 100]); ax.set_yticklabels([f'{v}%' for v in (0, 25, 50, 75, 100)])
    ax.grid(axis='y', color=GRID, lw=0.8, zorder=0); ax.set_axisbelow(True)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.spines['left'].set_color(GRID); ax.spines['bottom'].set_color(INK2)
axes[0].set_ylabel('Sum of unit capacities, share of the national capacity', fontsize=9.5)
from matplotlib.lines import Line2D
h = [Line2D([0], [0], color=BLUE, lw=2, marker='o', ms=8, mec=SURFACE, label='2011 data'), Line2D([0], [0], color=ORANGE, lw=2, marker='o', ms=8, mec=SURFACE, label='2025 data'),
     Line2D([0], [0], color=INK2, lw=0, marker='o', ms=8, label='Administrative units (joined)'), Line2D([0], [0], color=INK2, lw=0, marker='D', ms=8, label='NRM regions (catchments)')]
fig.legend(handles=h, loc='lower center', ncol=4, frameon=False, fontsize=9, labelcolor=INK, bbox_to_anchor=(0.5, 0.0))
fig.text(0.5, 0.115, 'Each unit feeds itself from its own land, yields and settings; corrected method. Under each level: the number of units. 2011 SA levels use 2020-21 land with 2011 population.\nThe two diamonds in each panel are the 2011 and 2025 NRM regions, offset slightly so that equal values show.', ha='center', fontsize=8, color=INK2, linespacing=1.5)
fig.subplots_adjust(left=0.085, right=0.985, top=0.9, bottom=0.3, wspace=0.06)
for ext in ('png', 'svg'): fig.savefig(os.path.join(OUT, f'scale_curve.{ext}'), dpi=200, facecolor=SURFACE)
print('written')
