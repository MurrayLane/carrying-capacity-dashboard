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
    "Figure 1": ("Figure 1. The methods of section 4 mapped by the question each answers, in the four purposes of "
                 "section 7 (columns). Each method has one mark, placed at the purpose where the author's matrix "
                 "(Table 9, with the failure-frame column named in its note) rates it highest and fewest other "
                 "methods share that rating; the author's model is rated well suited to all four and sits where it "
                 "has no other well-suited method beside it. Italic names are not rated in Table 9 and are placed "
                 "from their description in section 4. Mark shape shows whether the method gives a people count "
                 "directly, only by a further step, or not at all; orange is the author's model. Built from "
                 "`analysis/method_tests_2025/method_catalogue.csv` (Table 2)."),
    "Figure 2": ("Figure 2. Each method's reading of Australia on the common 2021 to 2023 data, as run and under "
                 "lines (a), (b) and (c) of section 5.11, beside the model's widened ranges (million people, log "
                 "scale). Every reading is one dot, 19 readings of five methods on each line, including the "
                 "footprint's pasture-only readings; the footprint's printed range in Table 5 leaves those out. "
                 "Line (a) keeps the productivity basis as part of the method, line (b) treats it as an input, and "
                 "line (c) adds one per-person requirement and waste treatment to line (b) (cell c1 of Table S7). "
                 "The grey band is the corrected release's 5th to 95th percentile (31.1 to 49.2) and the hatched "
                 "band the improved release's (37.9 to 60.0); the vertical lines mark each release's base value. "
                 "Built from `harmonised_comparison_lines.csv`, `harmonised_line_c.csv`, "
                 "`results/ranges_2025-fixed_wide.csv` and `results/ranges_2025-improved_wide.csv`."),
    "Figure 3": ("Figure 3. The factor by which each single choice moved the answer of the author's model, one "
                 "at a time (Table 8, panel A; higher capacity over lower, log scale). Single choices are ranked "
                 "by factor; the drought allowance appears twice, with the weather factor on every yield (2.19) and "
                 "on crop output alone (1.03), joined by the bracket. Below the line, not ranked: the diet C upper "
                 "bound (triangle), two bundles of settings (squares) and the spread across the settings drawn "
                 "together (diamonds). Built from `analysis/method_tests_2025/design_choices_panels.csv`."),
}
MESSAGES = {
    "Figure 1": "Methods answer different questions, and the ones that give a people count directly are not the ones that serve every purpose.",
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
    "Figure 2": ["B019", "B046", "B068", "B084", "B112", "B114", "B153", "B159", "B264", "B267", "B268", "B270",
                 "B272", "B273", "B274", "B341", "B342", "B347", "B348", "B357", "B402", "B403"],
    "Figure 3": ["B167", "B168", "B169", "B170", "B177", "B181", "B182", "B183", "B184", "B187", "B213", "B214",
                 "B421", "B422", "B425", "B426"],
    "Table 2": ["B004", "B019", "B046", "B068", "B137", "B153", "B159"],
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
                     "claims rows whose numbers appear": "; ".join(claims)})
    rows.append({"figure": "Table 2", "file": "analysis/figures_2025/paper_B/table_2.md",
                 "source csv": "analysis/method_tests_2025/method_catalogue.csv",
                 "columns": "all", "caption text": "Table 2. The catalogue of methods: family, what it measures, the question it answers, data it needs, whether it gives a people count directly, the Australian reading, and the literature register ids. Built from `analysis/method_tests_2025/method_catalogue.csv`.",
                 "message": "", "claims rows whose numbers appear": "; ".join(claims_for("Table 2"))})
    strip_dashes_ok(*[v for r in rows for v in r.values()])
    with open(HERE / "figures.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(r["figure"], "->", r["claims rows whose numbers appear"])


if __name__ == "__main__":
    main()
