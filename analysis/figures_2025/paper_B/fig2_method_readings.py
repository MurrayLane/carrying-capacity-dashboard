"""Figure 2 of Paper B: each method's reading of Australia, as run and under lines (a), (b) and (c), beside the
model's corrected and improved widened ranges.

Source csvs and columns:
  analysis/method_tests_2025/harmonised_comparison_lines.csv   method, classification, reference, as_run, harmonised
        rows whose reference starts "reading" (19 readings of five methods): as run, line (a) harmonised (classification
        starting "(a)"), line (b) harmonised (classification starting "(b)")
  analysis/method_tests_2025/harmonised_line_c.csv             same columns; classification starting "(c1)" is line (c)
        (8.0 MJ as eaten and the model's loss factors, Table 6 and S7); its "(b)" rows are checked equal to line (b)
  results/ranges_2025-fixed_wide.csv and results/ranges_2025-improved_wide.csv
        variant = wide, zone = 1, setting = short: p5, p95, base (people; drawn in million)
  analysis/method_tests_2025/cross_method.csv is the table 3 source for the same readings (as-run text, checked
        against the as_run column of the lines csv for the energy balance: 133.8 to 210.7)

Every reading is one dot (no centre or range is computed); the dots of one method and one line share a sub-row.
Axis: log, million people. Lines are marker shapes and colours (as run grey circle, (a) blue square,
(b) orange diamond, (c) aqua triangle); the model ranges are shaded bands (corrected solid grey, improved hatched).

Run:   python3 fig2_method_readings.py            both widths
       python3 fig2_method_readings.py --check    geometric mean of the energy balance line (a) readings against the
                                                  csv's own "method centre" row
       python3 fig2_method_readings.py --check --plant 150   shows a wrong value failing
"""
import csv
import math
import sys
import textwrap

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

from common import (AQUA, AXIS, BLUE, GRID, INK, INK2, MIN_PT, MUTED, ORANGE, SURFACE, WIDTHS_MM, check_report, mm,
                    parse_args, read_csv, save, setup_style, strip_dashes_ok)

STEM = "fig2_method_readings"
LINES = "analysis/method_tests_2025/harmonised_comparison_lines.csv"
LINEC = "analysis/method_tests_2025/harmonised_line_c.csv"
FIXED = "results/ranges_2025-fixed_wide.csv"
IMPR = "results/ranges_2025-improved_wide.csv"

CONDS = [  # key, legend text, marker, colour, filled
    ("run", "As run on the common data", "o", INK2, True),
    ("a", "Line (a): productivity is part of the method", "s", BLUE, True),
    ("b", "Line (b): productivity is an input", "D", ORANGE, True),
    ("c", "Line (c): (b) plus one requirement and waste", "^", AQUA, True),
]


def short(method):
    return method.split(" (")[0]


def load():
    la = [r for r in read_csv(LINES) if r["reference"].startswith("reading")]
    lc = [r for r in read_csv(LINEC) if r["reference"].startswith("reading")]
    methods = []
    for r in la:
        if r["method"] not in methods:
            methods.append(r["method"])
    data = {m: {k: [] for k, *_ in CONDS} for m in methods}
    for r in la:
        if r["classification"].startswith("(a)"):
            data[r["method"]]["run"].append(float(r["as_run"]))
            data[r["method"]]["a"].append(float(r["harmonised"]))
        elif r["classification"].startswith("(b)"):
            data[r["method"]]["b"].append(float(r["harmonised"]))
    for r in lc:
        if r["classification"].startswith("(c1)"):
            data[r["method"]]["c"].append(float(r["harmonised"]))
        elif r["classification"].startswith("(b)"):
            pass
    # line (b) in the line (c) file must equal line (b) in the lines file
    bc = [float(r["harmonised"]) for r in lc if r["classification"].startswith("(b)")]
    bb = [v for m in methods for v in data[m]["b"]]
    assert bc == bb, "line (b) differs between the two csvs"
    for m in methods:
        n = {k: len(v) for k, v in data[m].items()}
        assert len(set(n.values())) == 1, (m, n)
    bands = {}
    for name, f in (("corrected", FIXED), ("improved", IMPR)):
        r = [x for x in read_csv(f) if x["variant"] == "wide" and x["zone"] == "1" and x["setting"] == "short"][0]
        bands[name] = (float(r["p5"]) / 1e6, float(r["p95"]) / 1e6, float(r["base"]) / 1e6)
    return methods, data, bands


def gmean(v):
    return math.exp(sum(math.log(x) for x in v) / len(v))


def draw(methods, data, bands, width):
    setup_style()
    n = len(methods)
    if width == 190:
        left, axw, row_h, top, bot = 36.0, 150.0, 13.0, 24.0, 11.0
    else:
        left, axw, row_h, top, bot = 24.0, 60.0, 15.5, 37.0, 11.0
    h = top + n * row_h + bot
    fig = plt.figure(figsize=(mm(width), mm(h)))
    ax = fig.add_axes([mm(left) / mm(width), mm(bot) / mm(h), mm(axw) / mm(width), mm(n * row_h) / mm(h)])
    ax.set_xscale("log")
    ax.set_xlim(10, 500)
    ax.set_ylim(n - 0.5, -0.5)
    ax.set_xticks([10, 20, 50, 100, 200, 500])
    ax.set_xticklabels(["10", "20", "50", "100", "200", "500"])
    ax.xaxis.set_minor_locator(plt.NullLocator())
    ax.grid(axis="x", which="major", zorder=0)
    ax.set_xlabel("Million people (log scale)")
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.set_yticks(range(n))
    labs = []
    for m in methods:
        lab = short(m)
        labs.append("\n".join(textwrap.wrap(lab, 28 if width == 190 else 15)))
    strip_dashes_ok(*labs)
    ax.set_yticklabels(labs, color=INK)
    ax.tick_params(axis="y", length=0, pad=4)
    for i in range(1, n):
        ax.axhline(i - 0.5, color=GRID, lw=0.5, zorder=0)
    # model bands
    lo, hi, base = bands["corrected"]
    ax.axvspan(lo, hi, color="#c3c2b7", alpha=0.55, lw=0, zorder=1)
    lo2, hi2, base2 = bands["improved"]
    ax.axvspan(lo2, hi2, facecolor="none", edgecolor=MUTED, hatch="//", lw=0, zorder=1)
    ax.axvline(base, color=INK2, lw=0.6, zorder=2)
    ax.axvline(base2, color=INK2, lw=0.6, zorder=2)
    # dots
    off = {"run": -0.30, "a": -0.10, "b": 0.10, "c": 0.30}
    for i, m in enumerate(methods):
        for k, _, mk, col, _f in CONDS:
            ax.plot(data[m][k], [i + off[k]] * len(data[m][k]), marker=mk, ms=3.8, mfc=col, mec=SURFACE, mew=0.5,
                    ls="none", zorder=4, clip_on=False)
    # band labels above the axes
    ytxt = 1.02
    if width == 190:
        ax.text(lo, -0.62, f"Model, corrected: {lo:.1f} to {hi:.1f}", transform=ax.transData, ha="right", va="bottom",
                fontsize=MIN_PT, color=INK2)
        ax.text(hi2, -0.62, f"Model, improved: {lo2:.1f} to {hi2:.1f}", ha="left", va="bottom", fontsize=MIN_PT,
                color=INK2)
    else:
        ax.text(lo, -0.62, f"Corrected\n{lo:.1f} to {hi:.1f}", ha="right", va="bottom", fontsize=MIN_PT, color=INK2,
                linespacing=1.1)
        ax.text(hi2, -0.62, f"Improved\n{lo2:.1f} to {hi2:.1f}", ha="left", va="bottom", fontsize=MIN_PT, color=INK2,
                linespacing=1.1)
    # legend
    hs = [Line2D([], [], marker=mk, ms=5, mfc=col, mec=col, ls="none", label=t) for _, t, mk, col, _ in CONDS]
    hs += [Patch(facecolor="#c3c2b7", alpha=0.55, label="Model range, corrected release (5th to 95th percentile)"),
           Patch(facecolor="none", edgecolor=MUTED, hatch="//", label="Model range, improved release")]
    ncol = 2 if width == 190 else 1
    leg = fig.legend(handles=hs, loc="upper left", ncol=ncol, frameon=False, fontsize=MIN_PT,
                     bbox_to_anchor=(mm(1.0) / mm(width), 1 - mm(0.8) / mm(h)), handletextpad=0.5, columnspacing=2,
                     labelspacing=0.4, borderaxespad=0)
    for t in leg.get_texts():
        t.set_color(INK2)
    return fig


def main():
    a = parse_args()
    methods, data, bands = load()
    if a.check:
        m = [x for x in methods if x.startswith("Energy")][0]
        printed = round(gmean(data[m]["a"]), 1)
        if a.plant is not None:
            printed = a.plant
        raw = [r for r in read_csv(LINES) if r["method"] == m and r["classification"].startswith("(a)")
               and r["reference"].startswith("method centre")][0]
        ok = check_report("Figure 2, energy balance line (a) centre", printed, float(raw["harmonised"]), tol=0.05)
        sys.exit(0 if ok else 1)
    for w in ([a.width] if a.width else WIDTHS_MM):
        print(save(draw(methods, data, bands, w), STEM, w))


if __name__ == "__main__":
    main()
