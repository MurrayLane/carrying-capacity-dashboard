"""Build analysis/method_tests_2025/method_catalogue.csv (Table 2 and the source of Figure 1).

Inputs (all existing in the repository):
  papers/B_methods/draft/paper_B_draft1.md   sections 2 to 4 (families, what each sees), section 7 (the four purposes)
  papers/B_methods/SECTION7_DRAFT.md         the author's matrix of method against purpose (Table 9 and the failure-frame column)
  qa/literature_register.csv                 register ids (checked to exist; titles printed)
  analysis/method_tests_2025/cross_method.csv                columns: method, reading for Australia on current data (million people)
  analysis/comparators_2025/proportional_count.csv           columns: weighting, population basis, people supplied in the proportions of domestic use (million)
  analysis/method_tests_2025/harmonised_comparison_lines.csv columns: method, classification, reference, harmonised
                                              (the footprint and HALF readings at Australia's own productivity, line (b))

What is typed here is words taken from the paper's sections 4 and 7 (what each method measures, the data it needs,
whether it gives a people count). No number is typed: every Australian reading is read from the two csvs above.

Run:  python3 build_catalogue.py          writes the csv and table_2.md
"""
import csv
import re
import sys

from common import ROOT, read_csv, strip_dashes_ok

OUT = ROOT / "analysis/method_tests_2025/method_catalogue.csv"
TABLE_MD = ROOT / "analysis/figures_2025/paper_B/table_2.md"

PURPOSES = {
    1: "Food security and drought risk",
    2: "Why national estimates range from 9 to 100 million",
    3: "Regional and local land-use planning",
    4: "Diet change and land use",
}
RATING_WORD = {"●": "well suited", "◐": "partly suited", "○": "not suited"}
RATING_RANK = {"●": 2, "◐": 1, "○": 0}

# method key -> (short label, family, full name, section, matrix column or None, measures, question_text, data, people, ids, own-question)
# people: "directly", "by a further step", "no"
M = [
    dict(key="LDB_P", short="Land and diet balance (Peters)", family="Resource-based land and diet",
         name="Resource-based land and diet balance (Peters, Wilkins and Fick; Peters et al.; Fairlie)",
         section="4.1", col="LDB",
         measures="the land a population needs for a stated diet, set against the land available",
         data="land by class, yields, a stated diet",
         people="directly",
         ids=["L015", "L040", "L041"], reading=None),
    dict(key="LDB_M", short="Land and diet balance (the model)", family="Resource-based land and diet",
         name="Land and diet balance, the author's model (thesis method, corrected and improved)",
         section="4.1 and 5.9", col="LDB",
         measures="the people the land feeds on a stated diet, pairing pasture-fed food with crops and charging land for waste, fuel, fibre and a reserve",
         data="land by class, yields, diet, waste, fuel, fibre and reserve settings, a drought allowance",
         people="directly",
         ids=["L020", "L012", "L013", "L014"], reading="MODEL"),
    dict(key="EP", short="Energy and protein balance", family="Energy and protein balance",
         name="Energy and protein balance (Gifford; Henry and Godden)",
         section="4.2 and 5.3", col="EP",
         measures="the food energy and protein of domestic production, with exports counted as food, divided by a consumption factor per person",
         data="production totals, a land base, a consumption factor per person",
         people="directly",
         ids=["L003", "L002"], reading="Energy and protein balance (Gifford; Henry and Godden)"),
    dict(key="CB", short="Commodity balance", family="Commodity balance",
         name="Commodity balance (Foran and Poldy)",
         section="4.3 and 5.7", col="CB",
         measures="whether domestic production covers the human requirement for each commodity, in tonnes",
         data="production by commodity, a requirement per person",
         people="by a further step",
         ids=["L007"], reading="Commodity balance (Foran and Poldy)"),
    dict(key="EXP", short="Export-inclusive count", family="Export-inclusive count",
         name="Export-inclusive proportional count (CSIRO and University of Queensland)",
         section="4.4 and 6.1", col=None,
         measures="the people fed at home plus the people fed abroad, taken in proportion to the exported share of production",
         data="production, the exported share, the home population",
         people="directly",
         ids=["L010"], reading="EXPORT", place=2,
         basis_note="section 7.3 uses it to show how a published 100 million arises"),
    dict(key="FP", short="Ecological footprint, food row", family="Ecological footprint",
         name="Ecological footprint, food row (Rees; Wackernagel; Wackernagel and Rees; Simpson; Lenzen and Murray)",
         section="4.5 and 5.4", col="FP",
         measures="the productive land a population appropriates, at world-average productivity, wherever that land lies",
         data="consumption per person, land per tonne of each product, the country's land",
         people="by a further step",
         ids=["L139", "L134", "L050", "L023", "L022"], reading="FOOTPRINT"),
    dict(key="HALF", short="HALF index", family="Land per diet and people per hectare",
         name="HALF index, land per diet (Alexander et al.)",
         section="4.6 and 5.5", col="HALF",
         measures="the land the world would need if everyone ate a given country's diet, as a share of world land, at world-average production",
         data="a diet by food, world-average yields, world land",
         people="by a further step",
         ids=["L017"], reading="HALF"),
    dict(key="PPH", short="People per hectare", family="Land per diet and people per hectare",
         name="People per hectare of cropland (Cassidy et al.)",
         section="4.6 and 5.6", col="PPH",
         measures="the people nourished per hectare of cropland, after feed and other uses, on a stated diet energy",
         data="crop production by item, the uses of each crop, cropland area",
         people="by a further step",
         ids=["L016"], reading="People per hectare (Cassidy)"),
    dict(key="OPT", short="Diet and land-use optimisation", family="Optimisation models",
         name="Optimisation models, diet and land use (Chaudhary and Krishna; Gazan et al.; van Dooren; Gao and Bryan)",
         section="4.7", col=None,
         measures="the diet or land use that meets stated limits at least cost or least departure from what is observed",
         data="nutrient and cost tables, land and environmental limits, observed diets",
         people="no",
         ids=["L204", "L205", "L207", "L208"], reading=None, place=4,
         basis_note="trade-offs among nutrients, cost and environmental limits are what they see"),
    dict(key="INT", short="Integrated resource-flow models", family="Integrated resource-flow models",
         name="Integrated resource-flow models (Foran and Poldy; Hatfield-Dodds et al.; Bryan et al.; Navarro Garcia)",
         section="4.8", col=None,
         measures="stocks and flows of land, water, energy and materials through an economy, with their feedbacks and pressures",
         data="national accounts of land, water, energy and materials, scenario settings",
         people="no",
         ids=["L007", "L075", "L076", "L209"], reading=None, place=3,
         basis_note="national scenario models of Australian land use"),
    dict(key="WAT", short="Water-bounded capacity", family="Water-bounded capacity",
         name="Water-bounded capacity (Khorsandi et al.)",
         section="4.9", col=None,
         measures="capacity capped by land suitability, water, realistic yields and a share of net primary production, at several spatial scales",
         data="land suitability, water supply, yields, net primary production",
         people="directly",
         ids=["L073"], reading=None, place=3,
         basis_note="capacity falls as the units become smaller and more local"),
    dict(key="FAIL", short="Failure probability", family="Failure probability",
         name="Failure probability (Fearnside)",
         section="4.10 and 5.8", col="FAIL",
         measures="the chance that settlers fail in a year, as a relation to population density, not as one number",
         data="a yield record, a consumption standard, a rule for when a settler fails",
         people="by a further step",
         ids=["L042"], reading="FAIL"),
    dict(key="IDX", short="Index and planning studies", family="Index methods and planning studies",
         name="Index methods and planning studies (Graymore, Sipe and Rickson; Gutteridge; Noosa and Douglas Shire; Lane 2010)",
         section="4.11", col=None,
         measures="regional indicators ranked against thresholds, or a footprint set against a carrying capacity for a planning area",
         data="regional indicators and thresholds, local land and population",
         people="no",
         ids=["L091", "L034", "L038", "L039", "L055"], reading=None, place=3,
         basis_note="local planning is what these studies were made for (section 4.11)"),
]


def parse_matrix():
    """Rows: purpose number -> {column: symbol}, from SECTION7_DRAFT.md."""
    text = (ROOT / "papers/B_methods/SECTION7_DRAFT.md").read_text(encoding="utf-8")
    lines = [ln for ln in text.splitlines() if ln.startswith("|")]
    header = [c.strip() for c in lines[0].strip("|").split("|")]
    cols = header[1:]
    out = {}
    for ln in lines[2:]:
        cells = [c.strip() for c in ln.strip("|").split("|")]
        m = re.match(r"\*\*(\d)\.", cells[0])
        if not m:
            continue
        out[int(m.group(1))] = dict(zip(cols, cells[1:]))
    assert sorted(out) == [1, 2, 3, 4], out
    return out


def readings():
    cm = {r["method"]: r for r in read_csv("analysis/method_tests_2025/cross_method.csv")}
    ln = read_csv("analysis/method_tests_2025/harmonised_comparison_lines.csv")
    b = [r for r in ln if r["classification"].startswith("(b)") and r["reference"].startswith("reading")]
    fp_own = [float(r["harmonised"]) for r in b
              if r["method"].startswith("Ecological footprint")
              and ("cropland-bound" in r["reference"] or "crop and pasture together" in r["reference"])]
    half_own = [float(r["harmonised"]) for r in b if r["method"].startswith("HALF")]
    return cm, fp_own, half_own


def reading_text(key, cm, fp_own, half_own):
    if key is None:
        return "none for Australia"
    if key == "MODEL":
        c = cm["The model, thesis method corrected"]["reading for Australia on current data (million people)"]
        i = cm["The model, improved"]["reading for Australia on current data (million people)"]
        return f"{c} corrected; {i} improved (million people)"
    if key == "EXPORT":
        pc = [float(r["people supplied in the proportions of domestic use (million)"]) for r in read_csv("analysis/comparators_2025/proportional_count.csv")
              if r["weighting"].startswith("energy, FAO kcal per kg") and r["population basis"].startswith("2025")]
        return f"{min(pc):.0f} to {max(pc):.0f} million people, the proportional count rebuilt from the food balance by energy"
    if key == "FOOTPRINT":
        return (f"{cm['Ecological footprint, food row (Simpson)']['reading for Australia on current data (million people)'].split(' (')[0]}"
                f" million people as run in world-average hectares; {min(fp_own):.1f} to {max(fp_own):.1f} at Australia's own productivity")
    if key == "HALF":
        r = cm["HALF index (Alexander)"]["reading for Australia on current data (million people)"]
        return f"{r} million people as run in world-average hectares; {half_own[0]:.1f} at Australia's own productivity"
    if key == "FAIL":
        return cm["Failure probability (Fearnside)"]["reading for Australia on current data (million people)"] + " million people, the model read through Fearnside's frame"
    r = cm[key]["reading for Australia on current data (million people)"]
    return r if "million" in r else r + " million people"


def main():
    matrix = parse_matrix()
    cm, fp_own, half_own = readings()
    reg = {r["id"]: r for r in read_csv("qa/literature_register.csv")}
    rows = []
    for m in M:
        for i in m["ids"]:
            assert i in reg, f"register id {i} not found"
        # primary purpose: the purpose at the method's best rating in the author's matrix where the fewest
        # other methods share that rating; ties go to the lowest number
        if m["col"]:
            sym = {p: matrix[p][m["col"]] for p in matrix}
            best = max(RATING_RANK[s] for s in sym.values())
            cands = [p for p in sym if RATING_RANK[sym[p]] == best]
            def rivals(p):
                return sum(1 for c, v in matrix[p].items() if c != m["col"] and v == sym[p])
            place = min(cands, key=lambda p: (rivals(p), p))
            basis = ("author's matrix (Table 9)" if m["col"] not in ("FAIL",) else
                     "author's matrix, failure-frame column named in the Table 9 note")
            if m["key"] == "LDB_P":
                basis = "author's matrix, rated as the same family as the model (SECTION7_DRAFT.md)"
            ratings = "; ".join(f"{p} {RATING_WORD[sym[p]]}" for p in sorted(sym))
        else:
            place = m["place"]
            basis = "this catalogue's reading of section 4 (not rated in Table 9): " + m["basis_note"]
            ratings = "not rated"
        rd = reading_text(m["reading"], cm, fp_own, half_own)
        rows.append({
            "method": m["name"],
            "family": m["family"],
            "what it measures": m["measures"],
            "question it answers (the four purposes)": f"{place} {PURPOSES[place]}",
            "data it needs": m["data"],
            "gives a people count directly": m["people"],
            "Australian reading, if any": rd,
            "literature register ids": ";".join(m["ids"]),
            "short label": m["short"],
            "section": m["section"],
            "primary purpose number": place,
            "placement basis": basis,
            "ratings against the four purposes": ratings,
        })
    # order: by primary purpose, then paper order
    order = {m["name"]: i for i, m in enumerate(M)}
    rows.sort(key=lambda r: (r["primary purpose number"], order[r["method"]]))
    strip_dashes_ok(*[v for r in rows for v in r.values() if isinstance(v, str)])
    fields = list(rows[0].keys())
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    # Table 2 as markdown rows (the patch pastes these)
    head = ["Method", "Family", "What it measures", "Question it answers (purpose)", "Data it needs",
            "People count directly", "Australian reading", "Register ids"]
    keys = ["method", "family", "what it measures", "question it answers (the four purposes)", "data it needs",
            "gives a people count directly", "Australian reading, if any", "literature register ids"]
    lines = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for r in rows:
        lines.append("| " + " | ".join(str(r[k]).replace("|", "/") for k in keys) + " |")
    TABLE_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(rows)} rows) and {TABLE_MD}")
    for i in sorted({i for m in M for i in m['ids']}):
        print(" ", i, reg[i]["title"][:80])


if __name__ == "__main__":
    main()
