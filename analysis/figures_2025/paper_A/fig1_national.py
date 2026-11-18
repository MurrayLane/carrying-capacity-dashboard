#!/usr/bin/env python3
"""Paper A Figure 1: national short-term capacity against population, 2011 and 2025 (corrected method).
Run from anywhere: python3 -I analysis/figures_2025/paper_A/fig1_national.py [--check [--expect 41.5]]
Data (all read from the repository, no number typed in):
  results/2011-fixed-3.csv     rows zone=1, preset=short: population, capacity, capacity_per_person   (2011 base case; 2011 has no sampled range)
  results/2025-fixed.csv       rows zone=1, preset=short: population, capacity, capacity_per_person   (2025 base case)
  results/ranges_2025-fixed_wide.csv  rows zone=1, setting=short, variant=wide (19 choices, 2,000 draws) and variant=existing (13 choices, 1,000 draws): p5, p95
Print size 90 mm wide (single column)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *
from matplotlib.lines import Line2D

def nat(rel):
    return next(r for r in rd(rel) if r['zone'] == '1' and r['preset'] == 'short')
n11, n25 = nat('results/2011-fixed-3.csv'), nat('results/2025-fixed.csv')
rng = {r['variant']: r for r in rd('results/ranges_2025-fixed_wide.csv') if r['zone'] == '1' and r['setting'] == 'short'}
M = 1e6
pts = {2011: (float(n11['population']) / M, float(n11['capacity']) / M), 2025: (float(n25['population']) / M, float(n25['capacity']) / M)}
w19 = (float(rng['wide']['p5']) / M, float(rng['wide']['p95']) / M); w13 = (float(rng['existing']['p5']) / M, float(rng['existing']['p95']) / M)

fig, ax = plt.subplots(figsize=(90 * MM, 80 * MM)); style_ax(ax, grid='both')
xmax, ymax = 32, 54
ax.set_xlim(0, xmax); ax.set_ylim(0, ymax)
ax.plot([0, xmax], [0, xmax], color=MUTED, lw=0.8, zorder=1)
fig.subplots_adjust(left=0.13, right=0.97, top=0.98, bottom=0.33); fig.canvas.draw()
p0, p1 = ax.transData.transform((0, 0)), ax.transData.transform((xmax, xmax))
ang = math.degrees(math.atan2(p1[1] - p0[1], p1[0] - p0[0]))
ax.text(8.5, 8.5, 'capacity equals population', rotation=ang, rotation_mode='anchor', ha='center', va='top', fontsize=7, color=INK2)
# 2025 ranges: 13 choices (thick) inside 19 choices (thin with caps)
x25, y25 = pts[2025]
ax.plot([x25, x25], w19, color=ORANGE, lw=0.8, zorder=2); ax.plot([x25 - 0.5, x25 + 0.5], [w19[0]] * 2, color=ORANGE, lw=0.8); ax.plot([x25 - 0.5, x25 + 0.5], [w19[1]] * 2, color=ORANGE, lw=0.8)
ax.plot([x25, x25], w13, color=ORANGE, lw=3.2, solid_capstyle='butt', alpha=0.45, zorder=2)
sc = {}
for yr, (x, y) in pts.items():
    sc[yr] = ax.scatter([x], [y], s=34, color=YEAR_COL[yr], edgecolor=SURFACE, linewidth=0.9, zorder=4)
ax.text(pts[2011][0] - 1.0, pts[2011][1], f'2011: {pts[2011][1]:.1f} million against {pts[2011][0]:.1f} million\n{pts[2011][1] / pts[2011][0]:.2f} times the population', ha='right', va='center', fontsize=7, color=INK)
ax.text(pts[2025][0] - 1.0, pts[2025][1] + 4.5, f'2025: {pts[2025][1]:.1f} million against {pts[2025][0]:.1f} million\n{pts[2025][1] / pts[2025][0]:.2f} times the population', ha='right', va='center', fontsize=7, color=INK)
ax.set_xlabel('Population (million people)'); ax.set_ylabel('Short-term capacity (million people)')
h = [Line2D([], [], marker='o', ls='', ms=5, color=BLUE, mec=SURFACE, label='2011, no sampled range'),
     Line2D([], [], marker='o', ls='', ms=5, color=ORANGE, mec=SURFACE, label='2025, base case'),
     Line2D([], [], color=ORANGE, lw=0.8, label=f'2025, 5th to 95th percentile, 19 choices ({w19[0]:.1f} to {w19[1]:.1f})'),
     Line2D([], [], color=ORANGE, lw=3.2, alpha=0.45, solid_capstyle='butt', label=f'2025, same, 13 choices ({w13[0]:.1f} to {w13[1]:.1f})')]
ax.legend(handles=h, loc='upper center', bbox_to_anchor=(0.5, -0.2), frameon=False, ncol=1, handlelength=1.6, borderaxespad=0, labelspacing=0.3)
save(fig, 'fig1_national_capacity_population')
cap = ('National short-term capacity against population, Australia, 2011 and 2025, corrected method. Each dot is one year; a dot above the line has capacity above population. '
       'The 2011 value is the base case on the corrected 2011 release; 2011 has no sampled range. The 2025 bars are the 5th to 95th percentile of capacity: '
       'the thin line is the widened range over 19 choices and 2,000 draws, the thick band the earlier range over 13 choices and 1,000 draws. Sources: results/2011-fixed-3.csv, results/2025-fixed.csv, results/ranges_2025-fixed_wide.csv.')
register('Figure 1', 'fig1_national_capacity_population.png; fig1_national_capacity_population.svg',
         'results/2011-fixed-3.csv; results/2025-fixed.csv; results/ranges_2025-fixed_wide.csv',
         'population, capacity, capacity_per_person (zone=1, preset=short); p5, p95 (zone=1, setting=short, variant wide and existing)', cap, 'A001 A003 A163 A027')
if '--check' in sys.argv:
    # second route: capacity = capacity_per_person x population from the 2025 file; the plotted value is read back from the scatter artist's data
    alt = float(n25['capacity_per_person']) * float(n25['population']) / M
    check('2025 national short-term capacity, million (read from the plotted point)', alt, float(sc[2025].get_offsets()[0][1]), 41.5, 1)
print(f'Figure 1: 2011 {pts[2011][1]:.2f} vs {pts[2011][0]:.2f}; 2025 {pts[2025][1]:.2f} vs {pts[2025][0]:.2f}; 19-choice {w19[0]:.2f} to {w19[1]:.2f}; 13-choice {w13[0]:.2f} to {w13[1]:.2f}')
