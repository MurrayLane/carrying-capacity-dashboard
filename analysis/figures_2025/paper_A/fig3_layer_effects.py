#!/usr/bin/env python3
"""Paper A Figure 3: effect of each of the eight layers on capacity by region, short and long term, average over all 40,320 orderings, corrected method.
Run from anywhere: python3 -I analysis/figures_2025/paper_A/fig3_layer_effects.py [--check [--expect 4.15]]
Data (no number typed in):
  analysis/comparison_2025/capacity_by_cause_corrected_orders.csv   game=eight_layers_land_livestock_one; columns layer, preset, zone, shapley_mean (people)
  analysis/paper_a/movers-3.csv                                     columns zone, preset, cap2011 (the denominator: each effect is shown as % of the region's 2011 capacity)
  analysis/comparison_2025/decomposition_eight_layer_regional_counts.csv  (the counts of regions where each layer is largest, read in the report)
Diverging scale: red lowers capacity, blue raises it, neutral grey is no effect; clipped at 50% for colour, cells over 25% are labelled and a clipped cell shows its true value.
Print size 190 mm wide."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

GAME = 'eight_layers_land_livestock_one'
LAYERS = [('consumption_only', 'Consumption (diet)'), ('red_meat_mix_only', 'Red meat mix'), ('land_and_livestock', 'Land and livestock'), ('crop_yields_only', 'Crop yields'),
          ('organic_update_only', 'Organic update'), ('resilience_update_only', 'Resilience table'), ('fuel_update_only', 'Long-term liquid fuel'),
          ('infrastructure_land_only', 'Infrastructure land'), ('total_change', 'All layers')]
cap = rd('analysis/comparison_2025/capacity_by_cause_corrected_orders.csv')
sh = {(r['preset'], r['zone'], r['layer']): float(r['shapley_mean']) for r in cap if r['game'] == GAME}
base = {(r['preset'], r['zone']): float(r['cap2011']) for r in rd('analysis/paper_a/movers-3.csv')}
rows = regions_by_state()
if '--check' in sys.argv:
    # second route: national consumption effect as the sum of the total change less the other layers, from the nation row
    z = '1'; tot = sh[('short', z, 'total_change')]
    alt = (tot - sum(sh[('short', z, l)] for l, _ in LAYERS[:-1] if l != 'consumption_only')) / 1e6
    check('national short-term consumption layer, million people', alt, sh[('short', z, 'consumption_only')] / 1e6, 4.15, 2)
panels = []
for pr, title in (('short', 'Short term'), ('long', 'Long term')):
    panels.append((title, {z: [100 * sh[(pr, z, l)] / base[(pr, z)] for l, _ in LAYERS] for z, _, _ in rows}))
def fmt(v):
    return f'{v / 1000:+.1f}k' if abs(v) >= 1000 else f'{v:+.0f}'
Z = heatmap_pair('fig3_layer_effects', rows, panels, [n for _, n in LAYERS], 50, div_cmap('red'), 'effect on capacity, % of the region\'s 2011 capacity (colour clipped at 50)', 25, fmt, gap_after=(7,))
caption = ('Effect of each layer on short-term and long-term capacity in each of the 53 regions, 2011 to 2025, corrected method: the average over all 40,320 orderings of the eight layers, '
           'as a percentage of the region\'s 2011 capacity. Blue raises capacity and red lowers it; colour is clipped at 50% and a cell is labelled when the effect is 25% or more, '
           'with its true value if clipped. Regions are grouped by state. The last column is the total change, the sum of the eight layers. '
           'Sources: analysis/comparison_2025/capacity_by_cause_corrected_orders.csv, analysis/paper_a/movers-3.csv.')
register('Figure 3', 'fig3_layer_effects.png; fig3_layer_effects.svg', 'analysis/comparison_2025/capacity_by_cause_corrected_orders.csv; analysis/paper_a/movers-3.csv; analysis/comparison_2025/decomposition_eight_layer_regional_counts.csv',
         'game=eight_layers_land_livestock_one: layer, preset, zone, shapley_mean; movers-3: zone, preset, cap2011', caption, 'CLAIMS_PLACEHOLDER')
print('Figure 3: rows', len(rows), 'cells beyond clip', int((abs(Z) > 50).sum()))
