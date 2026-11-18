"""Figure 3 of Paper B: the factor by which each single in-model choice moved the answer (Table 8, panel A).

Source csv:  analysis/method_tests_2025/design_choices_panels.csv
Columns:     panel, design choice, low, high, factor (high over low), method and release, kind,
             order among the single choices of panel A (low to high factor)

Panel A rows only. Bars run from a factor of 1 on a log axis (one axis). Rows with a rank in the csv are the single
choices, drawn first, largest factor at the top. Rows without a rank (bundles, the spread of joint draws, the upper
bound) are drawn below a divider, largest first. The shape at the end of each bar gives the kind: circle a single
choice, square a bundle of settings, diamond the spread of joint draws, triangle the upper bound. The two drought
rows, the factor on every yield and on crops only, are orange and joined by a bracket; the other single choices are
blue; the rows outside the ranking are a lighter step of the same blue.

Run:   python3 fig3_design_choices.py             both widths
       python3 fig3_design_choices.py --check     recomputes high over low for the drought row (every yield) from
                                                  the low and high columns and compares it with the printed factor
       python3 fig3_design_choices.py --check --plant 2.91   shows a wrong printed value failing
"""
import sys
import textwrap

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from common import (AXIS, BLUE, BLUE_LIGHT, GRID, INK, INK2, MIN_PT, MUTED, ORANGE, SURFACE, WIDTHS_MM, check_report,
                    mm, parse_args, read_csv, save, setup_style, strip_dashes_ok)

STEM = "fig3_design_choices"
CSV = "analysis/method_tests_2025/design_choices_panels.csv"
ORDER = "order among the single choices of panel A (low to high factor)"
FACTOR = "factor (high over low)"
KIND_SHAPE = {"single": "o", "bundle": "s", "joint": "D", "bound": "^"}
KIND_TEXT = {"single": "Single choice", "bundle": "Bundle of settings", "joint": "Spread of joint draws",
             "bound": "Upper bound, not a realistic diet"}


def kind_of(r):
    k = r["kind"]
    if k.startswith("bundle"):
        return "bundle"
    if k.startswith("spread"):
        return "joint"
    if k.startswith("upper bound"):
        return "bound"
    return "single"


def load():
    rows = [r for r in read_csv(CSV) if r["panel"].startswith("A")]
    names = {}
    for r in rows:
        names[r["design choice"]] = names.get(r["design choice"], 0) + 1
    for r in rows:
        r["f"] = float(r[FACTOR])
        r["kind4"] = kind_of(r)
        rel = r["method and release"]
        lab = r["design choice"]
        if names[r["design choice"]] > 1:
            lab += f", {rel}" + ("" if rel in ("corrected", "improved") else "")
        if r["kind4"] == "joint":
            lab = "Spread over the settings drawn together, " + rel
        r["label"] = lab
        r["rank"] = int(r[ORDER]) if r[ORDER].strip() else None
        r["drought"] = r["design choice"].startswith("Drought allowance")
    ranked = sorted([r for r in rows if r["rank"] is not None], key=lambda r: -r["f"])
    # the csv's own rank must agree with the factor order
    assert [r["rank"] for r in ranked] == sorted([r["rank"] for r in ranked], reverse=True), "rank differs from factor"
    rest = sorted([r for r in rows if r["rank"] is None], key=lambda r: -r["f"])
    return ranked, rest


def draw(ranked, rest, width, planted=None):
    setup_style()
    rows = ranked + rest
    n = len(rows)
    gap = 0.9  # extra space for the divider
    if width == 190:
        left, axw, row_h, top, bot, wrapn = 82.0, 98.0, 5.6, 4.0, 22.0, 52
    else:
        left, axw, row_h, top, bot, wrapn = 44.0, 40.0, 8.8, 3.0, 40.0, 27
    h = top + (n + gap) * row_h + bot
    fig = plt.figure(figsize=(mm(width), mm(h)))
    ax = fig.add_axes([mm(left) / mm(width), mm(bot) / mm(h), mm(axw) / mm(width), mm((n + gap) * row_h) / mm(h)])
    ax.set_xscale("log")
    ax.set_xlim(1, 12)
    ys = [i + (gap if i >= len(ranked) else 0) for i in range(n)]
    ax.set_ylim(n + gap - 0.5, -0.5)
    ax.set_xticks([1, 1.5, 2, 3, 5, 8])
    ax.set_xticklabels(["1", "1.5", "2", "3", "5", "8"])
    ax.xaxis.set_minor_locator(plt.NullLocator())
    ax.grid(axis="x", which="major", zorder=0)
    ax.set_xlabel("Factor, higher over lower (log scale)" if width == 90 else "Factor, higher capacity over lower (log scale)")
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.set_yticks(ys)
    labs = ["\n".join(textwrap.wrap(r["label"], wrapn)) for r in rows]
    strip_dashes_ok(*labs)
    ax.set_yticklabels(labs, color=INK, linespacing=1.05)
    ax.tick_params(axis="y", length=0, pad=4)
    ax.axvline(1, color=AXIS, lw=0.8, zorder=2)
    # divider between ranked and unranked
    yd = len(ranked) - 0.5 + gap / 2
    ax.axhline(yd, color=AXIS, lw=0.6, zorder=1)
    ax.text(1.02, yd + 0.05, "Not ranked", ha="left", va="top", fontsize=MIN_PT, color=INK2)
    printed = {}
    bh = 0.30
    for r, y in zip(rows, ys):
        ranked_row = r["rank"] is not None
        col = ORANGE if r["drought"] else (BLUE if ranked_row else BLUE_LIGHT)
        ax.barh(y, r["f"] - 1, left=1, height=bh, color=col, zorder=3, lw=0)
        ax.plot([r["f"]], [y], marker=KIND_SHAPE[r["kind4"]], ms=5, mfc=col, mec=SURFACE, mew=0.6, ls="none", zorder=4)
        val = r["f"]
        if planted is not None and r["drought"] and r["f"] > 2:
            val = planted
        printed[r["label"]] = val
        ax.text(val * (1.06 if width == 90 else 1.035), y, f"{val:.2f}", va="center", ha="left", fontsize=MIN_PT, color=INK)
    # bracket joining the two drought rows
    yd2 = [y for r, y in zip(rows, ys) if r["drought"]]
    xb = 10.3 if width == 190 else 10.6
    ax.plot([xb - 0.25, xb, xb, xb - 0.25], [yd2[0], yd2[0], yd2[1], yd2[1]], color=ORANGE, lw=0.9, zorder=3,
            clip_on=False)
    ym = sum(yd2) / 2
    if width == 190:
        ax.text(xb * 1.06, ym, "Same\nallowance", ha="left", va="center", fontsize=MIN_PT, color=INK2,
                linespacing=1.1, clip_on=False)
    # legend
    hs = [Line2D([], [], marker=KIND_SHAPE[k], ms=5, mfc=MUTED, mec=MUTED, ls="none", label=KIND_TEXT[k])
          for k in KIND_SHAPE]
    hs += [Line2D([], [], marker="s", ms=6, mfc=ORANGE, mec=ORANGE, ls="none", label="Drought allowance rows"),
           Line2D([], [], marker="s", ms=6, mfc=BLUE_LIGHT, mec=BLUE_LIGHT, ls="none", label="Rows outside the ranking")]
    if width == 90:
        hs.append(Line2D([], [], color=ORANGE, lw=0.9, label="Bracket: same drought allowance"))
    ncol = 2 if width == 190 else 1
    leg = fig.legend(handles=hs, loc="lower left", ncol=ncol, frameon=False, fontsize=MIN_PT,
                     bbox_to_anchor=(mm(1.0) / mm(width), mm(0.5) / mm(h)), handletextpad=0.4, columnspacing=2,
                     labelspacing=0.4, borderaxespad=0.2)
    for t in leg.get_texts():
        t.set_color(INK2)
    return fig, printed


def main():
    a = parse_args()
    ranked, rest = load()
    if a.check:
        _, printed = draw(ranked, rest, 190, a.plant)
        raw = [r for r in read_csv(CSV) if r["panel"].startswith("A")
               and r["design choice"].startswith("Drought allowance, factor on every yield")][0]
        recomputed = float(raw["high"]) / float(raw["low"])  # from the csv's rounded low and high
        key = [k for k in printed if k.startswith("Drought allowance, factor on every yield")][0]
        ok = check_report("Figure 3, drought allowance on every yield, high over low", printed[key], recomputed,
                          tol=0.01)
        sys.exit(0 if ok else 1)
    for w in ([a.width] if a.width else WIDTHS_MM):
        fig, _ = draw(ranked, rest, w)
        print(save(fig, STEM, w))


if __name__ == "__main__":
    main()
