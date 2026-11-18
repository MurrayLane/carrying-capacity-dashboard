"""Shared helpers for the Paper A figure scripts (B144a). Not run on its own.
Design follows the dataviz skill references: documented categorical slots in fixed order (blue = slot 1, orange = slot 2),
one-hue sequential, two-hue diverging (blue and red) with a neutral grey midpoint, thin marks, hairline solid grid, one axis per chart,
legend for two or more series, text in ink tokens (never in a data colour), surface ring on dots.
Colour convention across the paper: 2011 is blue, 2025 is orange wherever the two years are drawn together."""
import csv, os, sys, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
MM = 1 / 25.4
SURFACE, INK, INK2, MUTED, GRID, AXIS = '#fcfcfb', '#0b0b0b', '#52514e', '#898781', '#e1e0d9', '#c3c2b7'
BLUE, ORANGE, AQUA = '#2a78d6', '#eb6834', '#1baf7a'          # categorical slots 1, 2, 3 (light surface)
NEUTRAL, RED, BLUE_DARK = '#f0efec', '#e34948', '#184f95'      # diverging: neutral grey midpoint, slot 8 red, sequential step 600 blue
YEAR_COL = {2011: BLUE, 2025: ORANGE}
FONTS = ['Liberation Sans', 'DejaVu Sans']

def setup():
    plt.rcParams.update({'font.family': FONTS, 'font.size': 7, 'axes.titlesize': 8, 'axes.labelsize': 7, 'xtick.labelsize': 7, 'ytick.labelsize': 7,
        'legend.fontsize': 7, 'text.color': INK, 'axes.edgecolor': AXIS, 'axes.labelcolor': INK2, 'xtick.color': INK2, 'ytick.color': INK2,
        'axes.facecolor': SURFACE, 'figure.facecolor': SURFACE, 'savefig.facecolor': SURFACE, 'axes.unicode_minus': False, 'svg.fonttype': 'path',
        'axes.linewidth': 0.6, 'xtick.major.width': 0.5, 'ytick.major.width': 0.5, 'xtick.major.size': 2.5, 'ytick.major.size': 2.5, 'lines.solid_capstyle': 'round'})
setup()

def rd(rel):
    with open(os.path.join(ROOT, rel), newline='') as f:
        return list(csv.DictReader(f))

def style_ax(ax, grid=None, left=True):
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.spines['left'].set_color(AXIS); ax.spines['bottom'].set_color(AXIS)
    if not left: ax.spines['left'].set_visible(False)
    if grid: ax.grid(axis=grid, color=GRID, lw=0.5, ls='-', zorder=0)
    ax.set_axisbelow(True)

def div_cmap(negative='red'):
    """Diverging two-hue map with a neutral grey midpoint. negative='red': below zero is red, above is blue; 'blue': the reverse."""
    lo, hi = (RED, BLUE_DARK) if negative == 'red' else (BLUE_DARK, RED)
    return LinearSegmentedColormap.from_list('div_' + negative, [lo, NEUTRAL, hi])

def save(fig, stem):
    for ext, kw in (('png', {'dpi': 300}), ('svg', {})):
        fig.savefig(os.path.join(HERE, f'{stem}.{ext}'), **kw)
    plt.close(fig)

def fmt_int(v): return f'{v:,.0f}'

# ---- the canonical 53 regions: movers-3.csv short rows (52 NRM regions and the Northern Territory)
def regions():
    rows = [r for r in rd('analysis/paper_a/movers-3.csv') if r['preset'] == 'short']
    assert len(rows) == 53, len(rows)
    return rows

def state_names():
    return {r['zone']: r['name'] for r in rd('results/2025-fixed.csv') if r['kind'] == 'state' and r['preset'] == 'short'}

STATE_ORDER = ['NSW-ACT', 'VIC', 'QLD', 'SA', 'WA', 'TAS', 'NT']
def regions_by_state():
    """regions grouped by state (state order fixed, names alphabetical inside a state): list of (zone, name, state_name)."""
    sn = state_names(); out = []
    for r in regions(): out.append((r['zone'], r['name'], sn.get(r['state'], 'NT')))
    return sorted(out, key=lambda t: (STATE_ORDER.index(t[2]), t[1]))

# ---- figures.csv: one row per figure, rewritten in place by each script
FIG_COLS = ['figure', 'file', 'source csv', 'columns', 'caption text', 'claims rows']
def register(figure, files, sources, columns, caption, claims):
    assert chr(0x2014) not in caption and chr(0x2013) not in caption, 'dash in caption'
    path = os.path.join(HERE, 'figures.csv'); rows = []
    if os.path.exists(path):
        with open(path, newline='') as f: rows = [r for r in csv.DictReader(f) if r['figure'] != figure]
    rows.append({'figure': figure, 'file': files, 'source csv': sources, 'columns': columns, 'caption text': caption, 'claims rows': claims})
    rows.sort(key=lambda r: r['figure'])
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, FIG_COLS); w.writeheader(); w.writerows(rows)

# ---- the --check: recompute one printed value from the csv by a second route and fail on a wrong planted value
def check(name, recomputed, plotted, expect_default, digits=1, tol=1e-4):
    """python3 script.py --check [--expect X]: the value recomputed from the csv must equal the value the figure uses and the expected value
    (the number the paper prints), both rounded to `digits`. --expect plants another expected value to show the check failing."""
    exp = expect_default
    if '--expect' in sys.argv: exp = float(sys.argv[sys.argv.index('--expect') + 1])
    ok = round(recomputed, digits) == round(exp, digits) and abs(recomputed - plotted) <= tol * max(1, abs(plotted))
    print(f'check {name}: recomputed {recomputed:.6g}, plotted {plotted:.6g}, expected {exp:g} -> {"OK" if ok else "FAIL"}')
    sys.exit(0 if ok else 1)

def reg_label(name):
    return name.replace(' - ', '-')

# ---- heatmap pair used by Figures 3 and 7: rows = regions grouped by state, two panels (short term, long term)
def heatmap_pair(fname_stem, rows, panels, cols, clip, cmap, cbar_label, label_min, fmt, figh_extra=65, gap_after=()):
    """rows: list of (zone, name, state); panels: [(title, {zone: [values per col]})]; cols: column labels; values clipped to +-clip for colour only.
    A cell is labelled when |value| >= label_min; a clipped cell shows its true value. gap_after: column indexes after which a blank gap is left."""
    import numpy as np
    from matplotlib.colors import TwoSlopeNorm
    n, rowh = len(rows), 3.5
    H = n * rowh + figh_extra
    fig = plt.figure(figsize=(190 * MM, H * MM))
    norm = TwoSlopeNorm(vcenter=0, vmin=-clip, vmax=clip)
    left, width_total = 0.20, 0.715
    pw = (width_total - 0.03) / 2
    axes = []
    for k, (title, vals) in enumerate(panels):
        ax = fig.add_axes([left + k * (pw + 0.03), 28 / H, pw, n * rowh / H]); axes.append(ax)
        # column positions with gaps
        xs, x = [], 0
        for j in range(len(cols)):
            xs.append(x); x += 1 + (0.45 if j in gap_after else 0)
        Z = np.array([[vals[z][j] for j in range(len(cols))] for z, _, _ in rows], float)
        for j, xj in enumerate(xs):
            col = np.clip(Z[:, j], -clip, clip)[:, None]
            ax.pcolormesh([xj, xj + 1], np.arange(n + 1), np.ma.masked_invalid(col), cmap=cmap, norm=norm, edgecolors=SURFACE, linewidth=0.8)
        for i in range(n):
            for j, xj in enumerate(xs):
                v = Z[i, j]
                if np.isfinite(v) and abs(v) >= label_min:
                    txt = fmt(v); inten = abs(np.clip(v, -clip, clip)) / clip
                    ax.text(xj + 0.5, i + 0.5, txt, ha='center', va='center', fontsize=7, color='white' if inten > 0.62 else INK)
        ax.set_xlim(0, xs[-1] + 1); ax.set_ylim(n, 0)
        ax.set_xticks([xj + 0.5 for xj in xs]); ax.set_xticklabels(cols, rotation=50, ha='left', rotation_mode='anchor', fontsize=7)
        ax.xaxis.tick_top(); ax.tick_params(length=0)
        for s in ax.spines.values(): s.set_visible(False)
        fig.text(left + k * (pw + 0.03), (28 + n * rowh + 31) / H, title, ha='left', va='bottom', fontsize=8, fontweight='bold')
        if k == 0:
            ax.set_yticks([i + 0.5 for i in range(n)]); ax.set_yticklabels([reg_label(nm) for _, nm, _ in rows], fontsize=7)
        else:
            ax.set_yticks([])
    # state separators and labels
    last = None
    for i, (_, _, st) in enumerate(rows):
        if st != last:
            if i > 0:
                for ax in axes: ax.axhline(i, color=INK2, lw=0.6)
            last = st
    groups = {}
    for i, (_, _, st) in enumerate(rows): groups.setdefault(st, []).append(i)
    for st, idx in groups.items():
        axes[1].text(1.01, (idx[0] + idx[-1] + 1) / 2, st, transform=axes[1].get_yaxis_transform(), ha='left', va='center', fontsize=7, color=INK2, rotation=-90)
    cax = fig.add_axes([left + 0.2, 14 / H, 0.30, 2.6 / H])
    sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap); cb = fig.colorbar(sm, cax=cax, orientation='horizontal')
    cb.outline.set_visible(False); cb.ax.tick_params(length=2, labelsize=7)
    cb.set_label(cbar_label, fontsize=7, color=INK2)
    save(fig, fname_stem)
    return Z
