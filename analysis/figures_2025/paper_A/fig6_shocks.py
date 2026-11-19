#!/usr/bin/env python3
"""Paper A Figure 6: exposure to shocks by region, capacity over population at three return periods (average year, 1 in 10, 1 in 20), 2011 and 2025, own yields, corrected method.
Run from anywhere: python3 -I analysis/figures_2025/paper_A/fig6_shocks.py [--check [--expect 21]]
Data (no number typed in):
  analysis/paper_a/shocks_by_region-3.csv        release in (2011-fixed-3, 2025-fixed); zone, name, return_period, capacity, population   (53 zones of movers-3.csv)
  analysis/paper_a/shocks_ranges_wide_zones.csv  preset=short, release=2025-fixed; zone, return_period, capacity_over_population_p5, _p95, _central (19 choices, 2,000 draws): whiskers on the 2025 dots
2011 has no ranges. The return periods 5, 50 and 100 are in shocks_by_region-3.csv and are not drawn (three panels keep the rows legible at 190 mm). The scenarios by region are Figure S6 (fig6s_scenarios.py).
Dots on a log axis, 2011 blue and 2025 orange, line at 1; values below 0.001 are drawn at the axis edge. Print size 190 mm wide."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *
from matplotlib.lines import Line2D
RPS = [('1', 'Average year'), ('10', '1 in 10 years'), ('20', '1 in 20 years')]
zones = sorted_zones()
sh = {(r['release'], r['return_period'], r['zone']): r for r in rd('analysis/paper_a/shocks_by_region-3.csv') if r['zone'] in zones}
assert len(sh) == 2 * 6 * 53
wz = {(r['return_period'], r['zone']): r for r in rd('analysis/paper_a/shocks_ranges_wide_zones.csv') if r['preset'] == 'short' and r['release'] == '2025-fixed' and r['zone'] in zones}
def ratio(rel, rp, z):
    r = sh[(rel, rp, z)]; return float(r['capacity']) / float(r['population'])
over25 = lambda rp: sum(1 for z in zones if ratio('2025-fixed', rp, z) < 1)
order = sorted(zones, key=lambda z: (-ratio('2025-fixed', '1', z), int(z)))
names = {z: sh[('2025-fixed', '1', z)]['name'] for z in zones}
n = len(order); rowh = 3.5; H = n * rowh + 32
fig = plt.figure(figsize=(190 * MM, H * MM)); FLOOR = 1e-3
left, pw, gap = 0.215, 0.23, 0.02
sc25 = {rp: [] for rp, _ in RPS}
for k, (rp, title) in enumerate(RPS):
    ax = fig.add_axes([left + k * (pw + gap), 18 / H, pw, n * rowh / H]); style_ax(ax, grid='x')
    ax.set_xscale('log'); ax.set_xlim(FLOOR, 100); ax.set_ylim(n - 0.5, -0.5); ax.minorticks_off()
    ax.set_xticks([1e-3, 1e-1, 10]); ax.set_xticklabels(['0.001', '0.1', '10'])
    ax.axvline(1, color=INK2, lw=0.8, zorder=2)
    for i, z in enumerate(order):
        v11, v25 = max(ratio('2011-fixed-3', rp, z), FLOOR), max(ratio('2025-fixed', rp, z), FLOOR)
        w = wz[(rp, z)]; lo, hi = max(float(w['capacity_over_population_p5']), FLOOR), max(float(w['capacity_over_population_p95']), FLOOR)
        ax.plot([lo, hi], [i, i], color=ORANGE, lw=0.7, alpha=0.7, zorder=3)
        ax.scatter([v11], [i], s=14, marker='s', color=BLUE, edgecolor=SURFACE, linewidth=0.5, zorder=4); sc25[rp].append(ax.scatter([v25], [i], s=15, marker='o', color=ORANGE, edgecolor=SURFACE, linewidth=0.5, zorder=5))
    ax.set_title(f'{title}\n{over25(rp)} regions over capacity in 2025', loc='left', fontsize=7, fontweight='bold', pad=4, linespacing=1.15)
    if k == 0:
        ax.set_yticks(range(n)); ax.set_yticklabels([reg_label(names[z]) for z in order], fontsize=7); ax.tick_params(axis='y', length=0)
    else: ax.set_yticks([])
fig.text(left + 0.2, 6 / H, 'Capacity over population (log scale; the line at 1 is capacity equal to population)', fontsize=7, color=INK2, ha='left')
fig.legend(handles=[Line2D([], [], marker='s', ls='', ms=4.5, color=BLUE, mec=SURFACE, label='2011 (square)'), Line2D([], [], marker='o', ls='', ms=4.5, color=ORANGE, mec=SURFACE, label='2025 (circle)'),
                    Line2D([], [], color=ORANGE, lw=0.7, alpha=0.7, label='2025, 5th to 95th percentile of the 19-choice range')],
           loc='lower left', bbox_to_anchor=(0.005, 0.0), ncol=3, frameon=False, fontsize=7, columnspacing=1.2)
save(fig, 'fig6_shocks')
caption = caption_for('Figure 6')
register('Figure 6', 'fig6_shocks.png; fig6_shocks.svg; fig6_shocks.pdf', 'analysis/paper_a/shocks_by_region-3.csv; analysis/paper_a/shocks_ranges_wide_zones.csv',
         'shocks_by_region-3: release, zone, name, return_period, capacity, population; shocks_ranges_wide_zones: preset=short, return_period, zone, capacity_over_population_p5, capacity_over_population_p95, capacity_over_population_central', caption, 'A370 A402')
if '--check' in sys.argv:
    # second route: the central ratio in the ranges file; the plotted count is read back from the 2025 circles' offsets in the 1-in-10 panel
    alt = sum(1 for z in zones if float(wz[('10', z)]['capacity_over_population_central']) < 1)
    plotted = sum(1 for c in sc25['10'] if c.get_offsets()[0][0] < 1)
    check('regions over capacity at 1 in 10, 2025 (read from the plotted markers)', alt, plotted, 21, 0)
print('Figure 6: over capacity 2025', {rp: over25(rp) for rp, _ in RPS}, '2011', {rp: sum(1 for z in zones if ratio('2011-fixed-3', rp, z) < 1) for rp, _ in RPS})
