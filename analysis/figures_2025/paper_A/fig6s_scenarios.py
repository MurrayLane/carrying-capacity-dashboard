#!/usr/bin/env python3
"""Paper A Figure S6 (supplementary, companion to Figure 6): the named scenarios by region, 2025 data, corrected release.
Run from anywhere: python3 -I analysis/figures_2025/paper_A/fig6s_scenarios.py [--check [--expect 5]]
Why supplementary: Figure 6 already carries 53 rows by three return periods with ranges; adding eleven scenarios would overload it.
Data (no number typed in):
  results/scenarios_2025-fixed.csv  zone, name, preset, scenario, population, capacity (the per-region values; scenarios_by_region.csv holds only the national figures and the counts, which the check reads)
  scenarios/scenarios.json  id, label (the scenario definitions quoted in the caption)
  analysis/paper_a/scenarios_by_region.csv  reference_release=2025-fixed rows: 'regions that tip over capacity against the reference' (compared with the count recomputed here)
Each row is one scenario; each dot a region's capacity over population on a log axis (line at 1). Orange dots are regions that tip over capacity against the reference row.
Print size 190 mm wide."""
import sys, os, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *
zones = sorted_zones()
import json
labels = {x['id']: x['label'] for x in json.load(open(os.path.join(ROOT, 'scenarios/scenarios.json')))['scenarios']}
sc = [r for r in rd('results/scenarios_2025-fixed.csv') if r['zone'] in zones]
data = {(r['scenario'], r['preset'], r['zone']): (float(r['capacity']), float(r['population']), r['name']) for r in sc}
scen = sorted({r['scenario'] for r in sc} - {'reference'})
order = ['reference'] + scen
def tip(s, pr):
    out = []
    for z in zones:
        c, p, nm = data[(s, pr, z)]; c0 = data[('reference', pr, z)][0]
        if c < p and c0 >= p: out.append(nm)
    return sorted(out)
hotpts = {}
n = len(order); rowh = 10.5; H = n * rowh + 36; FLOOR = 0.01
fig = plt.figure(figsize=(190 * MM, H * MM))
pw = 0.31
for k, (pr, title) in enumerate((('short', 'Short term'), ('long', 'Long term'))):
    ax = fig.add_axes([0.155 + k * (pw + 0.02), 20 / H, pw, n * rowh / H]); style_ax(ax, grid='x')
    ax.set_xscale('log'); ax.set_xlim(FLOOR, 60); ax.set_ylim(n - 0.5, -0.5); ax.minorticks_off(); ax.set_xticks([0.01, 0.1, 1, 10]); ax.set_xticklabels(['0.01', '0.1', '1', '10'])
    ax.axvline(1, color=INK2, lw=0.8, zorder=2)
    ax.set_title(title, loc='left', fontsize=8, fontweight='bold', pad=4)
    for i, s in enumerate(order):
        t = set(tip(s, pr)) if s != 'reference' else set()
        for z in zones:
            c, p, nm = data[(s, pr, z)]; v = max(c / p, FLOOR)
            hot = nm in t
            h_ = ax.scatter([v], [i], s=12 if hot else 6, color=ORANGE if hot else MUTED, alpha=1 if hot else 0.55, edgecolor=SURFACE if hot else 'none', linewidth=0.5, zorder=4 if hot else 3)
            if hot: hotpts.setdefault((s, pr), []).append(h_)
    if k == 0:
        ax.set_yticks(range(n)); ax.set_yticklabels([s.replace('-', ' ') for s in order], fontsize=7); ax.tick_params(axis='y', length=0)
    else: ax.set_yticks([])
    ax.set_xlabel('Capacity over population (log scale)', fontsize=7)
fig.text(0.835 - 0.0, (20 + n * rowh + 4) / H, 'Regions that tip over\ncapacity against the\nreference, long term', fontsize=7, fontweight='bold', va='bottom', ha='left')
for i, s in enumerate(order):
    nm = tip(s, 'long') if s != 'reference' else []
    txt = '\n'.join(textwrap.wrap(', '.join(nm), 26)) if nm else 'none'
    fig.text(0.835, (20 + (n - i - 0.5) * rowh) / H, txt, fontsize=7, va='center', ha='left', color=INK if nm else MUTED)
fig.text(0.155, 2 / H, 'Grey dots: the 53 regions. Orange dots: regions under capacity in the reference and over it in the scenario.', fontsize=7, color=INK2)
save(fig, 'fig6s_scenarios')
defs = '; '.join(f'{k}: {labels[k]}' for k in order if k in labels and k != 'reference')
cap = ('Supplementary figure S6. The named scenarios by region, 2025 data, corrected release (each grain store with its own resilience table): capacity over population in each of the 53 regions under each scenario, '
       'short and long term, on a log scale; the line at 1 is the status line. Orange dots are regions that are under capacity in the reference and over capacity in the scenario; their names are listed for the long term, '
       'and no region tips in the short term. Scenario definitions (scenarios/scenarios.json, run on the corrected release; the reference is the corrected 2025 release at its defaults): ' + defs + '. Sources: results/scenarios_2025-fixed.csv, analysis/paper_a/scenarios_by_region.csv.')
register('Figure S6', 'fig6s_scenarios.png; fig6s_scenarios.svg', 'results/scenarios_2025-fixed.csv; scenarios/scenarios.json; analysis/paper_a/scenarios_by_region.csv',
         'scenarios_2025-fixed: scenario, preset, zone, name, population, capacity; scenarios_by_region: reference_release=2025-fixed, scenario, term, regions that tip over capacity against the reference', cap, 'derived: the regional values are in no register row; national and count rows A201 to A227 and A264')
if '--check' in sys.argv:
    rows_ = [r for r in rd('analysis/paper_a/scenarios_by_region.csv') if r['reference_release'] == '2025-fixed' and r['scenario'] == 'fuel-csiro-340' and r['term'] == 'long']
    alt = float(rows_[0]['regions that tip over capacity against the reference'])
    check('regions that tip over capacity, fuel-csiro-340, long term (read from the plotted orange dots)', alt, len(hotpts[('fuel-csiro-340', 'long')]), 5, 0)
print('Figure S6 tippers long', {s: len(tip(s, 'long')) for s in scen}, 'short', sum(len(tip(s, 'short')) for s in scen))
