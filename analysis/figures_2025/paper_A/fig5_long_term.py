#!/usr/bin/env python3
"""Paper A Figure 5: (a) what each long-term setting is worth for Australia in 2025; (b) long-term capacity over population by region, 2011 and 2025. Corrected method, own yields.
Run from anywhere: python3 -I analysis/figures_2025/paper_A/fig5_long_term.py [--check [--expect 119]]
Data (no number typed in):
  analysis/paper_a/long_term_levers-3.csv   release=2025-fixed, zone=1; lever, alone, without. 'long settings' is the long-term capacity; 'without' is the long-term capacity with that one setting
                                            put back to its short-term value. Panel a shows (without - long) / long as a %, the 'Change' column of Table 6.
  analysis/paper_a/long_term_regions-3.csv  release in (2011-fixed-3, 2025-fixed); zone, name, capacity_long, population, ratio (53 regions = the 53 zones of movers-3.csv)
Panel a: bars from zero, one colour (the settings are nominal). Panel b: dots on a log axis, 2011 blue and 2025 orange, line at 1 (capacity equals population); values below 0.01 are drawn at the axis edge.
Print size 190 mm wide."""
import sys, os, re, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *
from matplotlib.lines import Line2D
NAMES = {'resilience': ('Weather allowance, return period', ' years'), 'meategg': ('Meat and egg share of the diet', ''), 'redmeat': ('Red-meat share of meat', ''), 'activity': ('Activity level', ''),
         'recycling': ('Recycling of food waste, share', ''), 'losses': ('Avoidable waste, share of food', ''), 'organic': ('Organic farming, share of land', ''), 'fuel': ('Liquid fuel', ' litres a person'),
         'biofuel': ('Biofuel share of fuel', ''), 'fibre': ('Fibre need', ' kg a person a year'), 'fibreNat': ('Fibre from natural sources, share', ''), 'fibreWool': ('Fibre from wool, share', '')}
ZERO = ['timber', 'infrastr2', 'nature2']
lev = {r['lever']: r for r in rd('analysis/paper_a/long_term_levers-3.csv') if r['release'] == '2025-fixed' and r['zone'] == '1'}
long_cap = float(lev['long settings']['alone'])
def key(l): return l.split(' (')[0]
items, zero_ok = [], []
for l, r in lev.items():
    k = key(l)
    if k in ('short settings', 'long settings'): continue
    pct = 100 * (float(r['without']) - long_cap) / long_cap
    if k in ZERO: zero_ok.append(abs(pct) < 0.05); continue
    rng = re.search(r'\((.*)\)', l).group(1)
    items.append((NAMES[k][0] + '\n' + rng + NAMES[k][1], pct))
assert len(zero_ok) == 3 and all(zero_ok)
items.append(('Timber, infrastructure area,\nreserve share (no effect)', 0.0))
items.sort(key=lambda t: -t[1])
zones = sorted_zones()
lr = {(r['release'], r['zone']): r for r in rd('analysis/paper_a/long_term_regions-3.csv') if r['zone'] in zones}
assert len(lr) == 106
order = sorted(zones, key=lambda z: (-float(lr[('2025-fixed', z)]['ratio']), int(z)))
names = {z: lr[('2025-fixed', z)]['name'] for z in zones}
H = 196
fig = plt.figure(figsize=(190 * MM, H * MM))
na = len(items); ha = na * 6.8
axa = fig.add_axes([0.205, (H - 14 - ha) / H, 0.235, ha / H]); style_ax(axa, grid='x', left=False)
ys = range(na)
bars = axa.barh(list(ys), [p for _, p in items], height=0.5, color=MUTED, zorder=3)
axa.set_ylim(na - 0.5, -0.5); axa.set_xlim(-135, 160)
axa.set_yticks(list(ys)); axa.set_yticklabels([n for n, _ in items], fontsize=7, linespacing=1.05); axa.tick_params(axis='y', length=0)
axa.axvline(0, color=INK2, lw=0.8, zorder=4)
for y, (_, p) in zip(ys, items):
    axa.text(p + (4 if p >= 0 else -4), y, f'{p:+.0f}%' if abs(p) >= 0.5 else '0%', ha='left' if p >= 0 else 'right', va='center', fontsize=7, color=INK)
axa.set_xticks([-100, -50, 0, 50, 100, 150]); axa.set_xticklabels(['-100', '-50', '0', '50', '100', '150'])
axa.set_xlabel('Change in long-term capacity when the setting is put back\nto its short-term value (% of the long-term capacity)', fontsize=7)
fig.text(0.0, (H - 6) / H, '(a) What each long-term setting is worth, Australia, 2025', fontsize=8, fontweight='bold', va='center')
axb = fig.add_axes([0.665, 20 / H, 0.32, (H - 38) / H]); style_ax(axb, grid='x')
n = len(order); FLOOR = 0.01
axb.set_xscale('log'); axb.set_xlim(FLOOR, 30); axb.set_ylim(n - 0.5, -0.5); axb.minorticks_off()
axb.set_xticks([0.01, 0.1, 1, 10]); axb.set_xticklabels(['0.01', '0.1', '1', '10'])
axb.set_yticks(range(n)); axb.set_yticklabels([reg_label(names[z]) for z in order], fontsize=7); axb.tick_params(axis='y', length=0)
axb.axvline(1, color=INK2, lw=0.8, zorder=2)
for i, z in enumerate(order):
    v11, v25 = max(float(lr[('2011-fixed-3', z)]['ratio']), FLOOR), max(float(lr[('2025-fixed', z)]['ratio']), FLOOR)
    axb.plot([v11, v25], [i, i], color=MUTED, lw=0.5, zorder=2)
    axb.scatter([v11], [i], s=14, color=BLUE, edgecolor=SURFACE, linewidth=0.5, zorder=4); axb.scatter([v25], [i], s=14, color=ORANGE, edgecolor=SURFACE, linewidth=0.5, zorder=5)
axb.set_xlabel('Long-term capacity over population (log scale)')
fig.text(0.46, (H - 6) / H, '(b) Long-term capacity over population by region', fontsize=8, fontweight='bold', va='center')
fig.legend(handles=[Line2D([], [], marker='o', ls='', ms=4.5, color=BLUE, mec=SURFACE, label='2011'), Line2D([], [], marker='o', ls='', ms=4.5, color=ORANGE, mec=SURFACE, label='2025')],
           loc='upper left', bbox_to_anchor=(0.46, (H - 10) / H), ncol=2, frameon=False, fontsize=7)
axb.text(1, -1.6, 'capacity equals population', fontsize=7, color=INK2, ha='center', va='bottom', clip_on=False)
save(fig, 'fig5_long_term')
cap = ('Long-term results, corrected method, own yields. (a) What each long-term setting is worth for Australia in 2025 (grey bars): the change in the long-term capacity when that one setting is put back to its short-term value, '
       'as a percentage of the long-term capacity (the settings are listed with their short-term and long-term values; timber, infrastructure area and the reserve share have no effect). '
       '(b) Long-term capacity over population in each of the 53 regions, 2011 (blue) and 2025 (orange), ordered by the 2025 value, on a log scale; the line at 1 is the status line and values below 0.01 are drawn at the axis edge. '
       'Sources: analysis/paper_a/long_term_levers-3.csv, analysis/paper_a/long_term_regions-3.csv.')
register('Figure 5', 'fig5_long_term.png; fig5_long_term.svg', 'analysis/paper_a/long_term_levers-3.csv; analysis/paper_a/long_term_regions-3.csv',
         'long_term_levers-3: release=2025-fixed, zone=1, lever, alone, without; long_term_regions-3: release, zone, name, ratio', cap, 'A417 A152 A153 A154 A155 A156 A157 A158 A159 A160 A161 A162')
if '--check' in sys.argv:
    # second route: ratio of the two capacities; the plotted value is the width of the weather-allowance bar read from the saved artist
    alt = (float(lev['resilience (1 to 100)']['without']) / float(lev['long settings']['without']) - 1) * 100
    wi = [i for i, (n, _) in enumerate(items) if n.startswith('Weather')][0]
    check('weather allowance put back to 1 year, change on the 2025 long-term capacity, % (read from the plotted bar)', alt, float(bars.patches[wi].get_width()), 119, 0)
print('Figure 5: levers', [(n[:20], round(p)) for n, p in items][:4], 'regions at floor', sum(1 for z in order for y in ('2011-fixed-3', '2025-fixed') if float(lr[(y, z)]['ratio']) < FLOOR))
