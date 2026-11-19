"""Write figures.csv: figure; file; source csv; columns; caption text; claims rows whose numbers appear.

Claims rows are chosen by reading the register's statements against the numbers each figure prints (the register's
values are mostly text, so a numeric match is unreliable); every id is asserted to exist as a paper B row. The qa file
is only read.
Run after build_catalogue.py and the three figure scripts:  python3 make_figures_csv.py
"""
import csv
import math

from common import HERE, ROOT, read_csv, strip_dashes_ok
import fig2_method_readings as f2
import fig3_design_choices as f3

CAPTIONS = {
    'Figure 1': "Figure 1. The methods of section 4 mapped by the question each answers, in the four purposes of section 7 (columns). Each method has one mark. A method rated in Table 9 sits at the purpose where Table 9 rates it highest and the fewest other rated methods share that rating. The author's model is the exception: by that rule it would sit at purpose 2 or 3, where it alone is well suited, but it is placed at purpose 1, the purpose it was built for, where Table 9 rates it partly suited (it is well suited at the other three). Names in italic are not rated in Table 9 (the Peters land and diet balance, failure probability, the export-inclusive count, optimisation, integrated resource-flow, water-bounded capacity, and index and planning studies); they are the author's reading of section 4, not ratings. Mark shape shows whether the method gives a people count directly, only by a further step, not at all, or is mixed (the planning studies); orange is the author's model.",
    'Figure 2': "Figure 2. Each method's reading of Australia on the common 2021 to 2023 data, as run and under lines (a), (b) and (c) of section 5.11, beside the model's widened ranges (million people, log scale). Every reading is one dot: 19 readings of five methods on each line, including the footprint's pasture-only readings (Table 5's line (b) column prints those at Australia's own productivity, 53.9 to 77.9; as run they are 316.9 and 385.7). The commodity-balance row runs 12 to 128 because grain with feed grain (127 to 128) is plotted but never binds, so the commodity balance's capacity range is 12 to 41. Line (a) keeps the productivity basis as part of the method, line (b) treats it as an input, and line (c) adds one per-person requirement and waste treatment to line (b) (cell c1 of Table S7). The grey band is the corrected release's 5th to 95th percentile (31.1 to 49.2) and the hatched band the improved release's (37.9 to 60.0); the vertical lines mark each release's base value. Coinciding readings overplot (the energy balance's six readings take two values and people per hectare's three take two), so about 14 marks are visible on each line against 19 readings.",
    'Figure 3': 'Figure 3. The factor by which each single choice moved the answer of the author\'s model, one at a time (Table 8, panel A; higher capacity over lower, log scale). Single choices are ranked by factor; the drought allowance appears twice, with the weather factor on every yield (2.19) and on crop output alone (1.03), a note beside the 1.03 row reading "same allowance as the 2.19 row". Below the line, not ranked: the diet C upper bound (triangle), two bundles of settings (squares) and the spread across the settings drawn together (diamonds).',
}
MESSAGES = {
    "Figure 1": "The methods answer different questions, so a figure from one method is not an answer to the question another asks.",
    "Figure 2": "As run, every aggregate method reads well above the model's ranges, and the footprint and HALF come down toward them only when productivity is counted as an input (line b).",
    "Figure 3": "The weather allowance moves the model by 2.19 on every yield but only 1.03 on crops alone, and diet, the unit and the allowance outrank waste and land.",
}
SOURCES = {
    "Figure 1": (["analysis/method_tests_2025/method_catalogue.csv"],
                 "short label; primary purpose number; gives a people count directly; placement basis"),
    "Figure 2": (["analysis/method_tests_2025/harmonised_comparison_lines.csv",
                  "analysis/method_tests_2025/harmonised_line_c.csv",
                  "results/ranges_2025-fixed_wide.csv", "results/ranges_2025-improved_wide.csv"],
                 "method; classification; reference; as_run; harmonised (lines csvs); variant, zone, setting, p5, p95, base (ranges csvs)"),
    "Figure 3": (["analysis/method_tests_2025/design_choices_panels.csv"],
                 "panel; design choice; low; high; factor (high over low); method and release; kind; order among the single choices of panel A"),
}


def printed_numbers():
    out = {"Figure 1": [], "Figure 2": [], "Figure 3": []}
    methods, data, bands = f2.load()
    for m in methods:
        for v in data[m].values():
            out["Figure 2"] += [round(x, 1) for x in v] + [round(x) for x in v]
    for lo, hi, base in bands.values():
        out["Figure 2"] += [round(lo, 1), round(hi, 1), round(base, 1)]
    ranked, rest = f3.load()
    out["Figure 3"] = [round(r["f"], 2) for r in ranked + rest]
    return out


CLAIMS = {
    # chosen by reading the register's statements against the numbers each figure prints; every id is checked to exist
    "Figure 1": [],
    "Figure 2": ["B019", "B044", "B046", "B068", "B084", "B112", "B114", "B153", "B159", "B264", "B267", "B268",
                 "B270", "B272", "B273", "B274", "B347", "B348", "B357"],
    "Figure 3": ["B114", "B167", "B168", "B169", "B170", "B177", "B181", "B182", "B183", "B184", "B187", "B213",
                 "B214", "B333", "B412", "B421", "B422", "B425", "B426"],
    "Table 2": ["B004", "B019", "B046", "B068", "B137", "B153", "B159"],
}
# printed numbers with no register row of their own, and where each comes from
NAMED = {
    "Figure 1": "none: no number is drawn",
    "Figure 2": ("line (c) readings (8.0 MJ as eaten, the model's loss factors; 19 dots): no register row carries them "
                 "singly, so they are cells of analysis/method_tests_2025/harmonised_line_c.csv, rows whose "
                 "classification starts (c1) and reference starts reading, column harmonised; the Table 6 and S7 "
                 "shares are B402 and B403, not drawn here"),
    "Figure 3": ("3.77, 1.60, 1.48 and 1.76 are in B412 (and B333 orders them); 1.60 also B213, 3.77 also B214 "
                 "(the diet readings 85.5 and 202.1 over 53.6), 1.48 also B425, 1.76 also B426 and "
                 "pal_one_at_a_time_2025.csv, improved row; 1.27 is the drawn-window row of design_choices_panels.csv "
                 "(B333); 1.58 for both releases is B187 and B390"),
    "Table 2": "",
}


def claims_for(fig):
    have = {r["id"] for r in read_csv("qa/claims_register.csv", skip_comments=False) if r["paper"] == "B"}
    missing = [i for i in CLAIMS[fig] if i not in have]
    assert not missing, (fig, missing)
    return CLAIMS[fig]


def main():
    nums = printed_numbers()
    rows = []
    for fig, stem in (("Figure 1", "fig1_method_map"), ("Figure 2", "fig2_method_readings"),
                      ("Figure 3", "fig3_design_choices")):
        files = [f"analysis/figures_2025/paper_B/{stem}_{w}mm.{e}" for w in (190, 90) for e in ("png", "svg")]
        src, cols = SOURCES[fig]
        claims = claims_for(fig)
        rows.append({"figure": fig, "file": "; ".join(files), "source csv": "; ".join(src), "columns": cols,
                     "caption text": CAPTIONS[fig], "message": MESSAGES[fig],
                     "claims rows whose numbers appear": "; ".join(claims), "printed numbers with no register row of their own": NAMED[fig]})
    rows.append({"figure": "Table 2", "file": "analysis/figures_2025/paper_B/table_2.md",
                 "source csv": "analysis/method_tests_2025/method_catalogue.csv",
                 "columns": "all", "caption text": 'Table 2. The catalogue of methods: family, what it measures, the question it answers, data it needs, whether it gives a people count directly, scale, and the Australian reading.',
                 "message": "", "claims rows whose numbers appear": "; ".join(claims_for("Table 2")), "printed numbers with no register row of their own": ""})
    strip_dashes_ok(*[v for r in rows for v in r.values()])
    with open(HERE / "figures.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(r["figure"], "->", r["claims rows whose numbers appear"])


if __name__ == "__main__":
    main()
