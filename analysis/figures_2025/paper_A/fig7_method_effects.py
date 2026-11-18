#!/usr/bin/env python3
"""Paper A Figure 7: the effect of each method choice on each region's capacity, 2025 data, as a percentage of the published-method capacity.
Run from anywhere: python3 -I analysis/figures_2025/paper_A/fig7_method_effects.py [--check [--expect 98]]
Data: analysis/paper_a/method_effects_by_region-3.csv, vintage=2025, term=short and long; columns '<module> (% of published)' for the eight modules plus 'corrected' and 'improved',
and 'capacity published (thousand)'. Diverging scale (blue raises capacity, red lowers it, neutral grey is no change) clipped at 40%; cells of 10% or more are labelled,
a clipped cell shows its true value. Print size 190 mm wide. The older plot_method_effects.py (analysis/paper_a) used the pale-midpoint RdBu map and the non-3 csv; this figure replaces it."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *
MODS = [('beef-carcase-yield', 'Beef carcase (C)'), ('biodiesel-yield', 'Biodiesel (C)'), ('loss-factors-australia', 'Australian losses'),
        ('dairy-good-land', 'Dairy on good land'), ('regional-beef-output', 'Beef output'), ('reserve-pro-rata', 'Reserve pro rata'),
        ('recycling-stage', 'Recycling by stage'), ('organic-ruminant-factor', 'Organic ruminants'), ('corrected', 'Corrected (both C)'), ('improved', 'Improved (all eight)')]
raw = [r for r in rd('analysis/paper_a/method_effects_by_region-3.csv') if r['vintage'] == '2025']
by = {(r['term'], r['zone']): r for r in raw}
rows = regions_by_state()
def val(r, m):
    v = r[f'{m} (% of published)']; return float(v) if v != '' else float('nan')
panels = [(t, {z: [val(by[(k, z)], m) for m, _ in MODS] for z, _, _ in rows}) for k, t in (('short', 'Short term'), ('long', 'Long term'))]
Z, axes = heatmap_pair('fig7_method_effects', rows, panels, [n for _, n in MODS], 40, div_cmap('red'), 'change in capacity, % of the published-method capacity (colour clipped at 40; hatched cells are negative)', 10, lambda v: f'{v:+.0f}', gap_after=(7,))
import numpy as np
blank = [(t, nm) for t, pv in zip(('short', 'long'), [p[1] for p in panels]) for (z, nm, _) in rows for v in pv[z] if v != v]
assert len(blank) == 20 and {nm for _, nm in blank} == {'Alinytjara Wilurara'}, blank
pub0 = float(by[('short', '42')]['capacity published (thousand)']); assert pub0 == 0, pub0
if '--check' in sys.argv:
    # the label drawn for South East Queensland, long term, biodiesel yield (read from the plotted text), against the raw csv line
    line = [l for l in open(os.path.join(ROOT, 'analysis/paper_a/method_effects_by_region-3.csv')) if l.startswith('2025,long,36,')][0]
    alt = float(line.split(',')[6]); row = [t[0] for t in rows].index('36'); col = [m for m, _ in MODS].index('biodiesel-yield')
    txt = [t for t in axes[1].texts if abs(t.get_position()[1] - (row + 0.5)) < 1e-9 and abs(t.get_position()[0] - (col + 0.5)) < 1e-9][0].get_text()
    check('biodiesel-yield effect, South East Queensland, long term, % of published (read from the plotted label)', alt, float(txt), 98, 0, tol=2e-2)
cap = ('The effect of each method choice on capacity in each of the 53 regions, 2025 data, short and long term, as a percentage of the published-method capacity (Lane 2014). Each choice is applied alone to the published method. '
       'Blue raises capacity and red lowers it; colour is clipped at 40% and cells of 10% or more are labelled with their value. The two corrections, marked (C), are the beef carcase yield and the biodiesel yield; the other six are improvements. '
       'The last two columns apply the two corrections together (corrected method) and all eight choices together (improved method). Hatched cells are negative. The Alinytjara Wilurara row is blank because its 2025 published-method capacity is 0 (20 cells). Regions are grouped by state. Source: analysis/paper_a/method_effects_by_region-3.csv.')
register('Figure 7', 'fig7_method_effects.png; fig7_method_effects.svg', 'analysis/paper_a/method_effects_by_region-3.csv',
         'vintage=2025; term; zone; name; the eight module columns (% of published); corrected (% of published); improved (% of published)', cap, 'A294 A295 A296 A297 A298 A299 A300 A301 A302 A303')
print('Figure 7: rows', len(rows), 'blank cells', len(blank), 'cells beyond clip', int((abs(np.nan_to_num(Z)) > 40).sum()))
