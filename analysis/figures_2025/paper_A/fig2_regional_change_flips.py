#!/usr/bin/env python3
"""Paper A Figure 2: change in short-term capacity and population by region, 2011 to 2025, with the status flips marked by test.
Run from anywhere: python3 -I analysis/figures_2025/paper_A/fig2_regional_change_flips.py [--check [--expect 464]]
Data (no number typed in):
  analysis/paper_a/movers-3.csv               preset=short: zone, name, cap2011, cap2025, dcap, pop2011, pop2025, dpop   (53 regions)
  analysis/paper_a/regional_flips-3_wide.csv  term=short: flip, artefact flag, '2025 status robust to the range' (19 choices), older 2011 boundary flag
One panel: a line from each region's 2011 capacity over population (small dot) to its 2025 value (larger marker) on a log axis; the line at 1 is the status line, so a flip crosses it.
Beside it, the change in capacity and in population in thousand people as figures. Print size 190 mm wide."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *
from matplotlib.lines import Line2D

mov = regions()
fl = {r['zone']: r for r in rd('analysis/paper_a/regional_flips-3_wide.csv') if r['term'] == 'short'}
assert len(fl) == 53
recs = []
for r in mov:
    f = fl[r['zone']]
    c11, c25, p11, p25 = float(r['cap2011']), float(r['cap2025']), float(r['pop2011']), float(r['pop2025'])
    assert int(float(f['over 2011'])) == int(float(r['over2011'])) and int(float(f['over 2025'])) == int(float(r['over2025']))   # the two files agree on status
    recs.append(dict(zone=r['zone'], name=r['name'], r11=c11 / p11, r25=c25 / p25, dcap=float(r['dcap']), dpop=float(r['dpop']), flip=f['flip'],
                     robust=f['2025 status robust to the range'] == 'yes', flagged=bool(f['artefact flag'] or f['older 2011 boundary flag'])))
recs.sort(key=lambda d: -d['r25'])
nflip = sum(1 for d in recs if d['flip'])

FLOOR = 1e-3
def signed(v):
    t = round(v / 1e3)
    return '0' if t == 0 else f'{t:+,d}'
n = len(recs); rowh = 3.55
fig = plt.figure(figsize=(190 * MM, (n * rowh + 40) * MM))
ax = fig.add_axes([0.235, 28 / (n * rowh + 40), 0.46, n * rowh / (n * rowh + 40)])
style_ax(ax, grid='x')
ax.set_xscale('log'); ax.set_xlim(FLOOR, 100); ax.set_ylim(n - 0.5, -0.5)
ax.set_xticks([1e-3, 1e-2, 1e-1, 1, 10, 100]); ax.set_xticklabels(['0.001', '0.01', '0.1', '1', '10', '100']); ax.minorticks_off()
ax.set_yticks(range(n)); ax.set_yticklabels([reg_label(d['name']) for d in recs], fontsize=7)
for lab, d in zip(ax.get_yticklabels(), recs):
    if d['flip']: lab.set_fontweight('bold'); lab.set_color(INK)
ax.tick_params(axis='y', length=0)
ax.axvline(1, color=INK2, lw=0.8, zorder=2)
COL = {True: AQUA, False: VIOLET}; MK = {True: 'D', False: 's'}     # verdict colours are slots 3 and 7, apart from the year colours (blue, orange) of Figures 1, 4, 5 and 6
clipped = 0
for i, d in enumerate(recs):
    x0, x1 = max(d['r11'], FLOOR), max(d['r25'], FLOOR); clipped += (d['r25'] < FLOOR) + (d['r11'] < FLOOR)
    c = COL[d['robust']] if d['flip'] else MUTED
    ax.plot([x0, x1], [i, i], color=c, lw=1.0 if d['flip'] else 0.6, zorder=3)
    ax.scatter([x0], [i], s=6, color=c, zorder=4, linewidths=0)                                    # small dot: 2011
    if d['flip']:
        ax.scatter([x1], [i], s=30, marker=MK[d['robust']], facecolor=(SURFACE if d['flagged'] else c), edgecolor=c, linewidth=1.0, zorder=6)   # large marker: 2025
    else:
        ax.scatter([x1], [i], s=14, color=MUTED, edgecolor=SURFACE, linewidth=0.4, zorder=5)
ax.set_xlabel('Short-term capacity over population (log scale; small dot 2011, large marker 2025)')
ax.text(1.0, -1.75, 'capacity equals population', ha='center', va='bottom', fontsize=7, color=INK2, clip_on=False)
tr = ax.get_yaxis_transform()
ax.text(1.16, -1.75, 'Change in\ncapacity', transform=tr, ha='right', va='bottom', fontsize=7, color=INK2, linespacing=1.1, clip_on=False)
ax.text(1.34, -1.75, 'Change in\npopulation', transform=tr, ha='right', va='bottom', fontsize=7, color=INK2, linespacing=1.1, clip_on=False)
ax.text(1.25, n - 0.45, '(thousand people)', transform=tr, ha='center', va='top', fontsize=7, color=INK2, clip_on=False)
for i, d in enumerate(recs):
    ax.text(1.16, i, signed(d['dcap']), transform=tr, ha='right', va='center', fontsize=7, color=INK, clip_on=False)
    ax.text(1.34, i, signed(d['dpop']), transform=tr, ha='right', va='center', fontsize=7, color=INK, clip_on=False)
h = [Line2D([], [], color=MUTED, lw=0.6, marker='o', ms=3.5, label='no change of status (small dot 2011, larger dot 2025)'),
     Line2D([], [], color=AQUA, lw=1.0, marker='D', ms=4.5, label='status flip; 2025 status holds across the 19 choices'),
     Line2D([], [], color=VIOLET, lw=1.0, marker='s', ms=4.5, label='status flip; 2025 status does not hold across the 19 choices'),
     Line2D([], [], color=INK2, lw=0, marker='o', ms=4.5, markerfacecolor=SURFACE, markeredgecolor=INK2, label='open marker: flagged as a land-definition or older 2011 boundary artefact')]
fig.legend(handles=h, loc='lower left', bbox_to_anchor=(0.01, 0.0), frameon=False, ncol=1, handlelength=2.2, labelspacing=0.3, fontsize=7)
save(fig, 'fig2_regional_change_flips')
if '--check' in sys.argv:
    # second route: capacity change from the flips file's own capacity columns; the plotted value is the text drawn in the capacity column for Central West NSW
    f = fl['4']; alt = (float(f['capacity 2025']) - float(f['capacity 2011'])) / 1e3
    row = [d['zone'] for d in recs].index('4')
    txt = [t for t in ax.texts if abs(t.get_position()[1] - row) < 1e-9 and t.get_position()[0] == 1.16][0].get_text()
    check('Central West NSW short-term capacity change, thousand people (read from the plotted text)', alt, float(txt.replace(',', '')), 464, 0, tol=2e-3)
note = f'{nflip} short-term flips; {clipped} end values below {FLOOR:g} drawn at the axis edge'
caption = caption_for('Figure 2')
register('Figure 2', 'fig2_regional_change_flips.png; fig2_regional_change_flips.svg; fig2_regional_change_flips.pdf', 'analysis/paper_a/movers-3.csv; analysis/paper_a/regional_flips-3_wide.csv',
         'movers-3: zone, name, cap2011, cap2025, dcap, pop2011, pop2025, dpop, over2011, over2025 (preset=short); regional_flips-3_wide: term=short, flip, artefact flag, 2025 status robust to the range, older 2011 boundary flag', caption, 'A420 A042 A043 A061')
print('Figure 2:', note, '; top gains', [(d['name'], round(d['dcap'] / 1e3)) for d in sorted(recs, key=lambda d: -d['dcap'])[:3]])
