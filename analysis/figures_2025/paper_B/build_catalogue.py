"""Build analysis/method_tests_2025/method_catalogue.csv (Table 2 and the source of Figure 1).

Inputs (all existing in the repository):
  papers/B_methods/draft/paper_B_draft1.md   sections 2 to 4 (families, what each sees, scale) and Table 9
                                             (the author's matrix of six methods against the four purposes)
  qa/literature_register.csv                 register ids (checked to exist)
  analysis/method_tests_2025/cross_method.csv                columns: method, reading for Australia on current data (million people)
  analysis/comparators_2025/proportional_count.csv           columns: weighting, population basis, people supplied in the proportions of domestic use (million)
  analysis/method_tests_2025/harmonised_comparison_lines.csv columns: method, classification, reference, as_run, harmonised

What is typed here is words taken from sections 4 and 7 of the paper (what each method measures, the data it needs,
whether it gives a people count, its scale). No number is typed: every Australian reading is read from the csvs above.

Placement (Figure 1): a method rated in Table 9 sits at the purpose where Table 9 rates it highest and the fewest
other rated methods share that rating (ties to the lowest number). A method Table 9 does not rate (Peters, the
export-inclusive count, optimisation, integrated flow, water-bounded, failure probability, index and planning) sits
where the author's reading of section 4 puts it; the csv column `placement basis` says which, and Figure 1 sets those
names in italic.

Run:  python3 build_catalogue.py          writes the csv and table_2.md
"""
import csv
import re

from common import ROOT, read_csv, strip_dashes_ok

OUT = ROOT / "analysis/method_tests_2025/method_catalogue.csv"
TABLE_MD = ROOT / "analysis/figures_2025/paper_B/table_2.md"

PURPOSES = {
    1: "Food security and drought risk",
    2: "Why national estimates range from 9 to 100 million",
    3: "Regional and local land-use planning",
    4: "Diet change and land use",
}
COLMAP = {"Energy and protein balance": "EP", "Footprint": "FP", "HALF": "HALF", "People per hectare": "PPH",
          "Commodity balance": "CB", "The model": "LDB"}
RANK = {"well ": 2, "partl": 1, "not s": 0}
WORD = {2: "well suited", 1: "partly suited", 0: "not suited"}

# people: "directly", "by a further step", "mixed", "no"
M = [
    dict(key="LDB_P", short="Land and diet balance (Peters)", family="Resource-based land and diet",
         name="Resource-based land and diet balance (Peters, Wilkins and Fick; Peters et al.; Fairlie)",
         section="4.1", col=None, place=4,
         basis_note="Peters's figures are capacities across diet scenarios (Table 8 panel C), so diet change and land use",
         measures="the land a population needs for a stated diet, set against the land available",
         data="land by class, yields, a stated diet", people="directly",
         scale="a region or a country (New York State, the United States, Britain)",
         ids=["L015", "L040", "L041"], reading=None),
    dict(key="LDB_M", short="Land and diet balance (the model)", family="Resource-based land and diet",
         name="Land and diet balance, the author's model (thesis method, corrected and improved)",
         section="4.1 and 5.9", col="LDB",
         measures="the people the land feeds on a stated diet, pairing pasture-fed food with crops and charging land for waste, fuel, fibre and a reserve",
         data="land by class, yields, diet, waste, fuel, fibre and reserve settings, a drought allowance",
         people="directly", scale="national, with regional and small-area (SA2) units",
         ids=["L020", "L012", "L013", "L014"], reading="MODEL"),
    dict(key="EP", short="Energy and protein balance", family="Energy and protein balance",
         name="Energy and protein balance (Gifford; Henry and Godden)", section="4.2 and 5.3", col="EP",
         measures="the food energy and protein of domestic production, with exports counted as food, divided by a consumption factor per person",
         data="production totals, a land base, a consumption factor per person", people="directly",
         scale="national", ids=["L003", "L002"], reading="Energy and protein balance (Gifford; Henry and Godden)"),
    dict(key="CB", short="Commodity balance", family="Commodity balance",
         name="Commodity balance (Foran and Poldy)", section="4.3 and 5.7", col="CB",
         measures="whether domestic production covers the human requirement for each commodity, in tonnes",
         data="production by commodity, a requirement per person", people="by a further step",
         scale="national", ids=["L007"], reading="Commodity balance (Foran and Poldy)"),
    dict(key="EXP", short="Export-inclusive count", family="Export-inclusive count",
         name="Export-inclusive proportional count (CSIRO and University of Queensland)", section="4.4 and 6.1",
         col=None, place=2, basis_note="section 7.3 uses it to show how a published 100 million arises",
         measures="the people fed at home plus the people fed abroad, taken in proportion to the exported share of production",
         data="production, the exported share, the home population", people="directly",
         scale="national", ids=["L010"], reading="EXPORT"),
    dict(key="FP", short="Ecological footprint, food row", family="Ecological footprint",
         name="Ecological footprint, food row (Rees; Wackernagel; Wackernagel and Rees; Simpson; Lenzen and Murray)",
         section="4.5 and 5.4", col="FP",
         measures="the productive land a population appropriates, at world-average productivity, wherever that land lies",
         data="consumption per person, land per tonne of each product, the country's land", people="by a further step",
         scale="any population, from a country to the world; applied to Australia as a nation",
         ids=["L139", "L134", "L050", "L023", "L022"], reading="FOOTPRINT"),
    dict(key="HALF", short="HALF index", family="Land per diet and people per hectare",
         name="HALF index, land per diet (Alexander et al.)", section="4.6 and 5.5", col="HALF",
         measures="the land the world would need if everyone ate a given country's diet, as a share of world land, at world-average production",
         data="a diet by food, world-average yields, world land", people="by a further step",
         scale="country against the world", ids=["L017"], reading="HALF"),
    dict(key="PPH", short="People per hectare", family="Land per diet and people per hectare",
         name="People per hectare of cropland (Cassidy et al.)", section="4.6 and 5.6", col="PPH",
         measures="the people nourished per hectare of cropland, after feed and other uses, on a stated diet energy",
         data="crop production by item, the uses of each crop, cropland area", people="by a further step",
         scale="the world and countries", ids=["L016"], reading="People per hectare (Cassidy)"),
    dict(key="OPT", short="Diet and land-use optimisation", family="Optimisation models",
         name="Optimisation models, diet and land use (Chaudhary and Krishna; Gazan et al.; van Dooren; Gao and Bryan)",
         section="4.7", col=None, place=4,
         basis_note="trade-offs among nutrients, cost and environmental limits are what they see",
         measures="the diet or land use that meets stated limits at least cost or least departure from what is observed",
         data="nutrient and cost tables, land and environmental limits, observed diets", people="no",
         scale="a country (diets) or a fine grid (LUTO's Australian land uses)",
         ids=["L204", "L205", "L207", "L208"], reading=None),
    dict(key="INT", short="Integrated resource-flow models", family="Integrated resource-flow models",
         name="Integrated resource-flow models (Foran and Poldy; Hatfield-Dodds et al.; Bryan et al.; Navarro Garcia)",
         section="4.8", col=None, place=4,
         basis_note="section 4.8 describes national scenario models of Australia that see feedbacks and pressures and give no people count; diet and land use is the closest of the four purposes, and none is a regional planning method",
         measures="stocks and flows of land, water, energy and materials through an economy, with their feedbacks and pressures",
         data="national accounts of land, water, energy and materials, scenario settings", people="no",
         scale="national (Australian scenario models)", ids=["L007", "L075", "L076", "L209"], reading=None),
    dict(key="WAT", short="Water-bounded capacity", family="Water-bounded capacity",
         name="Water-bounded capacity (Khorsandi et al.)", section="4.9", col=None, place=3,
         basis_note="capacity falls as the units become smaller and more local",
         measures="capacity capped by land suitability, water, realistic yields and a share of net primary production, at several spatial scales",
         data="land suitability, water supply, yields, net primary production", people="directly",
         scale="several spatial scales, from the country to small units (Iran)", ids=["L073"], reading=None),
    dict(key="FAIL", short="Failure probability", family="Failure probability",
         name="Failure probability (Fearnside)", section="4.10 and 5.8", col=None, place=1,
         basis_note="the method sees variation between years, which the other families average away; Table 9 does not count the failure view as a method",
         measures="the chance that settlers fail in a year, as a relation to population density, not as one number",
         data="a yield record, a consumption standard, a rule for when a settler fails", people="by a further step",
         scale="a settlement or study area (Fearnside's Brazilian area); here the national model run through the frame",
         ids=["L042"], reading="FAIL"),
    dict(key="IDX", short="Index and planning studies", family="Index methods and planning studies",
         name="Index methods and planning studies (Graymore, Sipe and Rickson; Gutteridge; Noosa and Douglas Shire; Lane 2010)",
         section="4.11", col=None, place=3, basis_note="local planning is what these studies were made for (section 4.11)",
         measures="regional indicators ranked against thresholds, or a footprint set against a carrying capacity for a planning area",
         data="regional indicators and thresholds, local land and population",
         people="mixed: none for Graymore, Sipe and Rickson; Gutteridge sets a footprint against a capacity; the Noosa and Douglas Shire studies are cited only through Lane (2010) and the thesis",
         scale="regional and local planning areas", ids=["L091", "L034", "L038", "L039", "L055"], reading=None),
]


def parse_matrix():
    """Table 9 of the paper draft: purpose number -> {column key: (rank, cell text)}."""
    text = (ROOT / "papers/B_methods/draft/paper_B_draft1.md").read_text(encoding="utf-8")
    lines = [ln for ln in text.splitlines() if ln.startswith("|")]
    hi = [i for i, ln in enumerate(lines) if ln.startswith("| Purpose | Energy and protein balance")]
    assert len(hi) == 1, hi
    header = [c.strip() for c in lines[hi[0]].strip("|").split("|")]
    cols = [COLMAP[c] for c in header[1:]]
    out = {}
    for ln in lines[hi[0] + 2: hi[0] + 6]:
        cells = [c.strip() for c in ln.strip("|").split("|")]
        p = int(re.match(r"(\d)\.", cells[0]).group(1))
        out[p] = {c: (RANK[v[:5]], v) for c, v in zip(cols, cells[1:])}
    assert sorted(out) == [1, 2, 3, 4], out
    return out


def readings():
    cm = {r["method"]: r for r in read_csv("analysis/method_tests_2025/cross_method.csv")}
    ln = read_csv("analysis/method_tests_2025/harmonised_comparison_lines.csv")
    rd = [r for r in ln if r["reference"].startswith("reading")]
    fp = [r for r in rd if r["method"].startswith("Ecological footprint") and r["classification"].startswith("(a)")
          and ("cropland-bound" in r["reference"] or "crop and pasture together" in r["reference"])]
    fp_world = [float(r["harmonised"]) for r in fp]          # 2021-23 world-average yields (146.2 is build 3)
    fp_1990 = [float(r["as_run"]) for r in fp if "build 3" in r["reference"] and "cropland-bound" in r["reference"]][0]
    fp_own = [float(r["harmonised"]) for r in rd if r["method"].startswith("Ecological footprint")
              and r["classification"].startswith("(b)")
              and ("cropland-bound" in r["reference"] or "crop and pasture together" in r["reference"])]
    half_own = [float(r["harmonised"]) for r in rd if r["method"].startswith("HALF") and r["classification"].startswith("(b)")]
    return cm, dict(fp_world=fp_world, fp_1990=fp_1990, fp_own=fp_own, half_own=half_own)


def reading_text(key, cm, d):
    if key is None:
        return "none for Australia"
    col = "reading for Australia on current data (million people)"
    if key == "MODEL":
        return (f"{cm['The model, thesis method corrected'][col]} corrected; "
                f"{cm['The model, improved'][col]} improved (million people)")
    if key == "EXPORT":
        pc = [float(r["people supplied in the proportions of domestic use (million)"])
              for r in read_csv("analysis/comparators_2025/proportional_count.csv")
              if r["weighting"].startswith("energy, FAO kcal per kg") and r["population basis"].startswith("2025")]
        return f"{min(pc):.0f} to {max(pc):.0f} million people, the proportional count rebuilt from the food balance by energy"
    if key == "FOOTPRINT":
        return (f"{min(d['fp_world']):.0f} to {max(d['fp_world']):.0f} million people as run, in world-average hectares on "
                f"2021-23 yields ({d['fp_1990']:.0f} at 1990 world yields); {min(d['fp_own']):.1f} to "
                f"{max(d['fp_own']):.1f} at Australia's own productivity")
    if key == "HALF":
        return f"{cm['HALF index (Alexander)'][col]} million people as run in world-average hectares; {d['half_own'][0]:.1f} at Australia's own productivity"
    if key == "FAIL":
        return cm["Failure probability (Fearnside)"][col] + " million people, the model read through Fearnside's frame"
    r = cm[key][col]
    return r if "million" in r else r + " million people"


def main():
    matrix = parse_matrix()
    cm, d = readings()
    reg = {r["id"]: r for r in read_csv("qa/literature_register.csv")}
    rows = []
    for m in M:
        for i in m["ids"]:
            assert i in reg, f"register id {i} not found"
        qual = ""
        if m["col"]:
            sym = {p: matrix[p][m["col"]][0] for p in matrix}
            best = max(sym.values())
            cands = [p for p in sym if sym[p] == best]

            def rivals(p, m=m, sym=sym):
                return sum(1 for c, (rk, _) in matrix[p].items() if c != m["col"] and rk == sym[p])
            place = min(cands, key=lambda p: (rivals(p), p))
            basis = "Table 9"
            ratings = "; ".join(f"{p} {matrix[p][m['col']][1]}" for p in sorted(matrix))
            cell = matrix[place][m["col"]][1]
            if "," in cell:
                qual = cell.split(",", 1)[1].strip()
        else:
            place = m["place"]
            basis = "author's reading of section 4 (not rated in Table 9): " + m["basis_note"]
            ratings = "not rated in Table 9"
        rows.append({
            "method": m["name"],
            "family": m["family"],
            "what it measures": m["measures"],
            "question it answers (the four purposes)": f"{place} {PURPOSES[place]}" + (f" ({qual})" if qual else ""),
            "data it needs": m["data"],
            "gives a people count directly": m["people"],
            "scale": m["scale"],
            "Australian reading, if any": reading_text(m["reading"], cm, d),
            "literature register ids": ";".join(m["ids"]),
            "short label": m["short"],
            "section": m["section"],
            "primary purpose number": place,
            "placement basis": basis,
            "ratings against the four purposes": ratings,
        })
    order = {m["name"]: i for i, m in enumerate(M)}
    rows.sort(key=lambda r: (r["primary purpose number"], order[r["method"]]))
    strip_dashes_ok(*[v for r in rows for v in r.values() if isinstance(v, str)])
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    head = ["Method", "Family", "What it measures", "Question it answers (purpose)", "Data it needs",
            "People count directly", "Scale", "Australian reading"]
    keys = ["method", "family", "what it measures", "question it answers (the four purposes)", "data it needs",
            "gives a people count directly", "scale", "Australian reading, if any"]
    lines = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for r in rows:
        lines.append("| " + " | ".join(str(r[k]).replace("|", "/") for k in keys) + " |")
    TABLE_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(rows)} rows) and {TABLE_MD}")


if __name__ == "__main__":
    main()
