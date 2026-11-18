#!/usr/bin/env python3
"""Paper A Figure 3: effect of each of the eight layers on capacity by region, short and long term, average over all 40,320 orderings, corrected method.
Run from anywhere: python3 -I analysis/figures_2025/paper_A/fig3_layer_effects.py [--check [--expect 302]]
Data (no number typed in):
  analysis/comparison_2025/capacity_by_cause_corrected_orders.csv   game=eight_layers_land_livestock_one; columns layer, preset, zone, shapley_mean (people)
  analysis/paper_a/movers-3.csv                                     columns zone, preset, cap2011 (the denominator: each effect is shown as % of the region's 2011 capacity)
  analysis/comparison_2025/decomposition_eight_layer_regional_counts.csv  (the counts of regions where each layer is largest, read in the report)
Diverging scale: red lowers capacity, blue raises it, neutral grey is no effect, negative cells hatched; clipped at 50% for colour, cells of 25% or more are labelled (percent, true value if clipped).
Print size 190 mm wide."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

GAME = 'eight_layers_land_livestock_one'
LAYERS = [('consumption_only', 'Consumption (diet)'), ('red_meat_mix_only', 'Red meat mix'), ('land_and_livestock', 'Land and livestock'), ('crop_yields_only', 'Crop yields'),
          ('organic_update_only', 'Organic update'), ('resilience_update_only', 'Resilience table'), ('fuel_update_only', 'Long-term liquid fuel'),
          ('infrastructure_land_only', 'Infrastructure land')]
cap = rd('analysis/comparison_2025/capacity_by_cause_corrected_orders.csv')
sh = {(r['preset'], r['zone'], r['layer']): float(r['shapley_mean']) for r in cap if r['game'] == GAME}
base = {(r['preset'], r['zone']): float(r['cap2011']) for r in rd('analysis/paper_a/movers-3.csv')}
rows = regions_by_state()
panels = []
for pr, title in (('short', 'Short term'), ('long', 'Long term')):
    panels.append((title, {z: [100 * sh[(pr, z, l)] / base[(pr, z)] for l, _ in LAYERS] for z, _, _ in rows}))
def fmt(v):
    return f'{v:+,.0f}%'
Z, axes = heatmap_pair('fig3_layer_effects', rows, panels, [n for _, n in LAYERS], 50, div_cmap('red'), 'effect on capacity, % of the region\'s 2011 capacity (colour clipped at 50; hatched cells are negative)', 25, fmt)
caption = ('Effect of each layer on short-term and long-term capacity in each of the 53 regions, 2011 to 2025, corrected method: the average over all 40,320 orderings of the eight layers, '
           'as a percentage of the region\'s 2011 capacity. Blue raises capacity and red lowers it; colour is clipped at 50% and a cell is labelled when the effect is 25% or more, '
           'with its true value if clipped. Regions are grouped by state. Hatched cells are negative, so the sign reads in greyscale. '
           'Sources: analysis/comparison_2025/capacity_by_cause_corrected_orders.csv, analysis/paper_a/movers-3.csv.')
register('Figure 3', 'fig3_layer_effects.png; fig3_layer_effects.svg', 'analysis/comparison_2025/capacity_by_cause_corrected_orders.csv; analysis/paper_a/movers-3.csv; analysis/comparison_2025/decomposition_eight_layer_regional_counts.csv',
         'game=eight_layers_land_livestock_one: layer, preset, zone, shapley_mean; movers-3: zone, preset, cap2011', caption, 'A450')
if '--check' in sys.argv:
    # a labelled cell read back from the plotted text (Southern Gulf, land and livestock, short term), against the csv recomputed from the raw rows by a second route
    z = '38'; alt = 100 * float([r for r in cap if r['game'] == GAME and r['preset'] == 'short' and r['zone'] == z and r['layer'] == 'land_and_livestock'][0]['shapley_mean']) / float([r for r in rd('analysis/paper_a/movers-3.csv') if r['preset'] == 'short' and r['zone'] == z][0]['cap2011'])
    row = [t[0] for t in rows].index(z); col = [l for l, _ in LAYERS].index('land_and_livestock')
    txt = [t for t in axes[0].texts if abs(t.get_position()[1] - (row + 0.5)) < 1e-9 and abs(t.get_position()[0] - (col + 0.5)) < 1e-9][0].get_text()
    check('Southern Gulf land and livestock effect, short term, % of 2011 capacity (read from the plotted label)', alt, float(txt.replace('%', '').replace(',', '')), 302, 0, tol=2e-3)
print('Figure 3: rows', len(rows), 'cells beyond clip', int((abs(Z) > 50).sum()))
