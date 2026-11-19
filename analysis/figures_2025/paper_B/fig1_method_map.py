"""Figure 1 of Paper B: the methods mapped by the question each answers.

Source csv:  analysis/method_tests_2025/method_catalogue.csv  (built by build_catalogue.py)
Columns used: short label; primary purpose number; gives a people count directly (directly, by a further step, mixed, no);
placement basis (anything but "Table 9" is set in italic)

Layout: a two-axis categorical map. Columns are the four purposes of section 7; rows are the methods, sorted by
the purpose they are placed at and then by section order. One mark per method. Shape says whether the method gives
a people count directly (filled circle), only by a further step (open circle) not at all (cross) or mixed (open square); colour marks the
author's model (orange) against the published methods (blue); an italic name means the placement is read from the
description in section 4 because Table 9 does not rate the method. No number is drawn.

Run:   python3 fig1_method_map.py                 draws both widths (190 and 90 mm)
       python3 fig1_method_map.py --check         recomputes the count of marks in purpose 2 from the csv
       python3 fig1_method_map.py --check --plant 9   shows the check failing on a wrong printed value
"""
import csv
import sys
import textwrap

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from common import (AXIS, BLUE, GRID, INK, INK2, MIN_PT, MUTED, ORANGE, ROOT, SURFACE, WIDTHS_MM, check_report, mm,
                    parse_args, read_csv, save, setup_style, strip_dashes_ok)

STEM = "fig1_method_map"
CSV = "analysis/method_tests_2025/method_catalogue.csv"
PURPOSE_HEAD = {
    1: "Food security and drought risk",
    2: "Why national estimates range from 9 to 100 million",
    3: "Regional and local land-use planning",
    4: "Diet change and land use",
}
PEOPLE = {
    "directly": ("o", True, "Gives a people count directly"),
    "by a further step": ("o", False, "Only by a further step (division or conversion)"),
    "mixed": ("s", False, "Mixed: some studies give a count, some do not"),
    "no": ("x", True, "No people count"),
}


def load():
    rows = read_csv(CSV)
    for r in rows:
        r["place"] = int(r["primary purpose number"])
        r["unrated"] = not r["placement basis"].startswith("Table 9")
        if r["gives a people count directly"].startswith("mixed"):
            r["gives a people count directly"] = "mixed"
        r["is_model"] = r["short label"].endswith("(the model)")
    return rows


def draw(rows, width, planted=None):
    setup_style()
    n = len(rows)
    if width == 190:
        left, axw, row_h, top, bot = 60.0, 126.0, 6.0, 20.0, 17.0
    else:
        left, axw, row_h, top, bot = 47.0, 41.0, 5.2, 27.0, 34.0
    h = top + n * row_h + bot
    fig = plt.figure(figsize=(mm(width), mm(h)))
    ax = fig.add_axes([mm(left) / mm(width), mm(bot) / mm(h), mm(axw) / mm(width), mm(n * row_h) / mm(h)])
    ax.set_xlim(0.5, 4.5)
    ax.set_ylim(n - 0.5, -0.5)
    for k in range(5):
        ax.axvline(k + 0.5, color=GRID, lw=0.5, zorder=0)
    for i in range(n):
        ax.axhline(i, color=GRID, lw=0.5, zorder=0)
    ax.axhline(n - 0.5, color=AXIS, lw=0.6)
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_yticks(range(n))
    labels = [r["short label"] for r in rows]
    strip_dashes_ok(*labels)
    ax.set_yticklabels(labels, color=INK)
    for t, r in zip(ax.get_yticklabels(), rows):
        if r["unrated"]:
            t.set_fontstyle("italic")
    ax.tick_params(axis="y", length=0, pad=3)
    ax.set_xticks([])
    # column headers
    wrap = 22 if width == 190 else 99
    for p in range(1, 5):
        if width == 190:
            txt = "\n".join(textwrap.wrap(f"{p}  {PURPOSE_HEAD[p]}", 24))
            ax.text(p, -0.9, txt, ha="center", va="bottom", fontsize=MIN_PT, color=INK2, linespacing=1.15)
        else:
            ax.text(p, -0.9, str(p), ha="center", va="bottom", fontsize=MIN_PT + 1, color=INK, fontweight="bold")
    if width == 90:
        key = "\n".join(f"{p}  {PURPOSE_HEAD[p]}" for p in range(1, 5))
        fig.text(mm(1.5) / mm(width), 1 - mm(2) / mm(h), key, ha="left", va="top", fontsize=MIN_PT, color=INK2,
                 linespacing=1.3)
    # marks
    for i, r in enumerate(rows):
        shape, filled, _ = PEOPLE[r["gives a people count directly"]]
        col = ORANGE if r["is_model"] else BLUE
        ax.plot([r["place"]], [i], marker=shape, ms=6.5 if shape == "o" else 5.5, mfc=col if filled else SURFACE,
                mec=col, mew=1.4, ls="none", zorder=3, clip_on=False)
    printed = sum(1 for r in rows if r["place"] == 2)
    if planted is not None:
        printed = planted
    # legend: shapes and colours
    hs = [Line2D([], [], marker=m, ms=6, mfc=(MUTED if f else SURFACE), mec=MUTED, mew=1.3, ls="none", label=t)
          for (m, f, t) in PEOPLE.values()]
    hs += [Line2D([], [], marker="s", ms=6, mfc=BLUE, mec=BLUE, ls="none", label="Published method"),
           Line2D([], [], marker="s", ms=6, mfc=ORANGE, mec=ORANGE, ls="none", label="The author's model")]
    ncol = 3 if width == 190 else 1
    leg = fig.legend(handles=hs, loc="lower left", ncol=ncol, frameon=False, fontsize=MIN_PT,
                     bbox_to_anchor=(mm(1.5) / mm(width), mm(1.0) / mm(h)), handletextpad=0.4, columnspacing=1.4,
                     labelspacing=0.5, borderaxespad=0.2)
    for t in leg.get_texts():
        t.set_color(INK2)
    fig.text(mm(1.5) / mm(width), mm(bot - 3) / mm(h) - (0 if width == 190 else 0),
             "Italic: not rated in Table 9; placed by the author's reading of section 4" if width == 190 else
             "Italic: not in Table 9; author's reading",
             ha="left", va="top", fontsize=MIN_PT, color=INK2, fontstyle="italic")
    return fig, printed


def main():
    a = parse_args()
    rows = load()
    if a.check:
        # independent recount straight from the raw csv text
        with open(ROOT / CSV, newline="", encoding="utf-8") as fh:
            raw = list(csv.reader(fh))
        hdr = raw[0]
        qi = hdr.index("question it answers (the four purposes)")
        recomputed = sum(1 for r in raw[1:] if r[qi].startswith("2 "))
        _, printed = draw(rows, 190, a.plant)
        ok = check_report("Figure 1, methods placed at purpose 2", printed, recomputed)
        sys.exit(0 if ok else 1)
    for w in ([a.width] if a.width else WIDTHS_MM):
        fig, _ = draw(rows, w)
        print(save(fig, STEM, w))


if __name__ == "__main__":
    main()
