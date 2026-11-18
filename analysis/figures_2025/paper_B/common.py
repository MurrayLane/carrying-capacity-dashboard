"""Shared style, sizes and helpers for the Paper B figures (B144b).

Design follows the dataviz reference: categorical colours in the fixed order of
the reference palette (blue, orange, aqua), one hue light to dark for the
single-series bars, hairline grid, thin marks, no dual axes, a legend for two
or more series, shape as the second channel so every figure reads in greyscale.
Light surface only: these are print figures.
"""
import csv
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager as fm  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]  # repository root

# Palette (palette.md, light column)
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
BLUE = "#2a78d6"      # categorical slot 1
ORANGE = "#eb6834"    # slot 2
AQUA = "#1baf7a"      # slot 3
BLUE_LIGHT = "#86b6ef"  # sequential step 250, the lightest step that clears 2:1

WIDTHS_MM = (190, 90)  # double and single column
MIN_PT = 7.0           # smallest text at print size


def mm(v):
    return v / 25.4


def setup_style():
    names = {f.name for f in fm.fontManager.ttflist}
    for cand in ("Inter", "Liberation Sans", "DejaVu Sans"):
        if cand in names:
            family = cand
            break
    plt.rcParams.update({
        "font.family": family,
        "font.size": MIN_PT,
        "axes.labelsize": MIN_PT + 0.5,
        "xtick.labelsize": MIN_PT,
        "ytick.labelsize": MIN_PT,
        "legend.fontsize": MIN_PT,
        "axes.unicode_minus": False,
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "axes.edgecolor": AXIS,
        "axes.linewidth": 0.6,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "text.color": INK,
        "axes.labelcolor": INK2,
        "grid.color": GRID,
        "grid.linewidth": 0.5,
        "grid.linestyle": "-",
        "svg.fonttype": "path",
        "svg.hashsalt": "paperB",
        "pdf.fonttype": 42,
    })


def read_csv(rel, skip_comments=True):
    path = ROOT / rel
    with open(path, newline="", encoding="utf-8") as fh:
        lines = [ln for ln in fh if not (skip_comments and ln.startswith("#"))]
    return list(csv.DictReader(lines))


def save(fig, stem, width_mm):
    out = HERE
    png = out / f"{stem}_{width_mm}mm.png"
    svg = out / f"{stem}_{width_mm}mm.svg"
    fig.savefig(png, dpi=300)
    fig.savefig(svg, metadata={"Date": None})
    with plt.rc_context({"pdf.fonttype": 42}):
        fig.savefig(out / f"{stem}_{width_mm}mm.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(fig)
    return [png.name, svg.name]


def check_report(name, printed, recomputed, tol=1e-9):
    """Print a check line; return True when the printed value equals the recomputed one."""
    ok = abs(printed - recomputed) <= tol
    print(f"{name}: printed {printed!r} vs recomputed {recomputed!r} -> {'PASS' if ok else 'FAIL'}")
    return ok


def parse_args(argv=None):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="recompute one printed value from the csv and fail if it differs")
    ap.add_argument("--plant", type=float, default=None,
                    help="with --check: replace the printed value by this wrong one, to show the check failing")
    ap.add_argument("--width", type=int, choices=WIDTHS_MM, default=None,
                    help="draw one width only (default: both 190 and 90 mm)")
    return ap.parse_args(argv)


def strip_dashes_ok(*texts):
    bad = [t for t in texts if chr(0x2014) in t or chr(0x2013) in t]
    if bad:
        raise SystemExit(f"em or en dash in label: {bad}")
