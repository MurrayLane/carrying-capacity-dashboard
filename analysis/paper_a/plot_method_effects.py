#!/usr/bin/env python3
"""Paper A figure 7: the effect of each method choice on each region's capacity (2025 data), short and long term, as a share of the published-method capacity.
Usage (repository root): python3 -I analysis/paper_a/plot_method_effects.py   (reads method_effects_by_region.csv; writes method_effects_heatmap.png and .svg)
Diverging scale, two hues with a neutral midpoint at no change, clipped at +-40%; cells with a change of 10% or more are labelled; rows are ordered by the effect of the improved method as a whole."""
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
rows = list(csv.DictReader(open('analysis/paper_a/method_effects_by_region.csv')))
MODS = ['beef-carcase-yield', 'biodiesel-yield', 'loss-factors-australia', 'dairy-good-land', 'regional-beef-output', 'reserve-pro-rata', 'recycling-stage', 'organic-ruminant-factor']
LAB = {'beef-carcase-yield': 'Beef carcase\nyield (C)', 'biodiesel-yield': 'Biodiesel\nyield (C)', 'loss-factors-australia': 'Australian loss\nfactors', 'dairy-good-land': 'Dairy on\ngood land', 'regional-beef-output': 'Beef output\nby state', 'reserve-pro-rata': 'Reserve\npro rata', 'recycling-stage': 'Recycling\nby stage', 'organic-ruminant-factor': 'Organic\nruminant factor'}
fig, axes = plt.subplots(1, 2, figsize=(15, 15), sharey=True, gridspec_kw={'wspace': 0.08})
order = [r['name'] for r in sorted([r for r in rows if r['vintage'] == '2025' and r['term'] == 'short'], key=lambda r: float(r['improved (% of published)'] or 0))]
im = None
for ax, term in zip(axes, ('short', 'long')):
    d = {r['name']: r for r in rows if r['vintage'] == '2025' and r['term'] == term}
    data = [[float(d[n][f'{m} (% of published)'] or 0) if d[n][f'{m} (% of published)'] != '' else 0.0 for m in MODS] for n in order]
    im = ax.imshow(data, cmap='RdBu', norm=TwoSlopeNorm(vcenter=0, vmin=-40, vmax=40), aspect='auto')
    ax.set_xticks(range(len(MODS)), [LAB[m] for m in MODS], fontsize=7, rotation=35, ha='left')
    ax.xaxis.tick_top(); ax.set_title('Short term' if term == 'short' else 'Long term', fontsize=11, pad=58, loc='left')
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            if abs(v) >= 10: ax.text(j, i, f'{v:+.0f}', ha='center', va='center', fontsize=6.5, color='white' if abs(v) > 28 else '#222')
    ax.set_yticks(range(len(order)), order, fontsize=7); ax.tick_params(length=0)
    for s in ax.spines.values(): s.set_visible(False)
fig.suptitle('Effect of each method choice on each region\'s capacity, alone, as % of the published-method capacity', fontsize=12, y=0.955)
fig.colorbar(im, ax=axes, orientation='horizontal', fraction=0.025, pad=0.03, label='change in capacity, % of published (clipped at 40)')
fig.text(0.01, 0.005, '2025 data, 52 NRM regions and the Northern Territory. (C) marks the two corrections; the rest are improvements. Rows ordered by the improved method as a whole, short term. Source: results/method_effects.csv.', fontsize=7)
fig.savefig('analysis/paper_a/method_effects_heatmap.png', dpi=140, bbox_inches='tight'); fig.savefig('analysis/paper_a/method_effects_heatmap.svg', bbox_inches='tight')
print('ok', len(order))
