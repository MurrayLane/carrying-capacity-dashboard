#!/usr/bin/env python3
"""Print every generated table of analysis/paper_a/README.md in markdown.

Run from the repository root:
  python3 -I analysis/paper_a/make_readme_tables.py            # print the tables
  python3 -I analysis/paper_a/make_readme_tables.py --write    # replace them in the README
  python3 -I analysis/paper_a/make_readme_tables.py --write --only named_scenarios,measures   # only these tables

Each table sits in the README between marker lines
  <!-- generated: analysis/paper_a/make_readme_tables.py <table id> -->
  <!-- end generated -->
and the first line inside names the csv it was built from and the commit (HEAD of the
working copy, read from .git without running git). On a first --write a table that has no
markers yet is found by its header row and wrapped; on later runs the marker block is
replaced in place.

Every number in these tables is computed from the csvs in this folder. The README quotes no
figure from another author's paper in a table, so there is no published_values.csv here.
"""
import csv
import os
import re
import sys
from decimal import Decimal, ROUND_HALF_UP

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SCRIPT = os.path.relpath(os.path.abspath(__file__), REPO)
README = os.path.join(HERE, "README.md")


# ---------------------------------------------------------------- helpers
def commit():
    try:
        head = open(os.path.join(REPO, ".git", "HEAD")).read().strip()
        if not head.startswith("ref: "):
            return head[:7]
        ref = head[5:]
        p = os.path.join(REPO, ".git", ref)
        if os.path.exists(p):
            return open(p).read().strip()[:7]
        for line in open(os.path.join(REPO, ".git", "packed-refs")):
            if line.strip().endswith(" " + ref):
                return line.split()[0][:7]
    except OSError:
        pass
    return "unrecorded"


def rows(name):
    with open(os.path.join(HERE, name), newline="") as f:
        return list(csv.DictReader(f))


def r(x, d):
    """Round half up, d decimals, as a string (no sign handling beyond Decimal's)."""
    q = Decimal(1).scaleb(-d)
    s = str(Decimal(repr(float(x))).quantize(q, rounding=ROUND_HALF_UP))
    return s[1:] if s.startswith("-") and float(s) == 0 else s


def sg(x, d):
    s = r(x, d)
    if float(s) == 0:
        return "0"
    return s if s.startswith("-") else "+" + s


def comma(s):
    ip, _, fp = s.partition(".")
    neg = ip.startswith("-")
    ip = ip.lstrip("-")
    ip = f"{int(ip):,}"
    return ("-" if neg else "") + ip + ("." + fp if fp else "")


def big(x):
    """1 decimal, but whole numbers from 100 up (100, 258)."""
    return r(x, 0) if float(x) >= 100 else r(x, 1)


def b(s):
    return f"**{s}**"


def md(header, body):
    def line(cells):
        return "|" + "|".join(f" {c} " if c else " " for c in cells) + "|"

    return [line(header), "|" + "---|" * len(header)] + [line(row) for row in body]




# ---------------------------------------------------------------- tables
def pct(s, d):
    """A csv percentage string such as '9.6%' or '-0.35%' as '+9.6%', rounded to d decimals; zero is '0%'."""
    return sg(float(str(s).rstrip("%")), d) + "%"


def t_flips():
    flips = rows("regional_flips.csv")
    body = []
    for term, label in (("short", "Short term"), ("long", "Long term")):
        x = [f for f in flips if f["term"] == term]
        o11 = sum(f["over 2011"] == "1" for f in x)
        o25 = sum(f["over 2025"] == "1" for f in x)
        fl = [f for f in x if f["flip"]]
        oy = sum(f["flip"] == "over to under" for f in fl)
        uo = sum(f["flip"] == "under to over" for f in fl)
        ftxt = f"{len(fl)} (all over to under)" if uo == 0 else f"{len(fl)} ({oy} over to under, {uo} under to over)"
        art = sum(bool(f["artefact flag"]) for f in fl)
        notrob = sum(f["2025 status robust to the range"] == "no" for f in fl)
        clean = sum(f["clean and robust"] == "yes" for f in fl)
        body.append([label, str(o11), str(o25), ftxt, str(art), str(notrob), b(str(clean))])
    return ["regional_flips.csv"], md(["", "Regions over capacity 2011", "Over capacity 2025", "Flips",
                                       "Land-definition or boundary artefacts", "Not robust to the 2025 range", "**Clean and robust**"], body)


def t_shocks():
    s = {(x["release"], x["return period (years)"]): x for x in rows("shocks_summary.csv")}
    names = {"1": "average year", "10": "1 in 10", "20": "1 in 20", "100": "1 in 100"}
    body = []
    for rel, yr in (("2011-fixed", "2011"), ("2025-fixed", "2025")):
        for rp, nm in names.items():
            x = s[(rel, rp)]
            body.append([yr, nm, r(x["national capacity over population"], 2), str(int(x["regions over capacity (of 53)"])),
                         x["share of population living in over-capacity regions"], r(x["sum over national"], 2)])
    return ["shocks_summary.csv"], md(["", "Return period", "National capacity over population", "Regions over capacity",
                                       "Population living in over-capacity regions", "Sum of regional capacities over national"], body)


def t_scenarios():
    # one column pair per reference release: the improved release (as first computed) and the corrected release (decision 86, B91)
    scr = {(x["reference_release"], x["scenario"], x["term"]): x for x in rows("scenarios_by_region.csv")}
    rels = ("2025-improved", "2025-fixed")
    chg, cnt = "change on reference", "regions over capacity (of 53)"
    # label, scenario ids, decimals for the long-term change, bold the long-term change
    spec = [("Field-crop yields 12% lower", ["climate-crops-12"], 1, False),
            ("Field-crop yields 24% lower", ["climate-crops-24"], 1, False),
            ("Waste at the national target (6%)", ["waste-target-6"], 1, False),
            ("No avoidable waste", ["waste-none"], 1, False),
            ("Recycling none or half", ["recycling-half", "recycling-none"], 1, False),
            ("Liquid fuel 156 litres (electric vehicles)", ["fuel-ev-156"], 1, False),
            ("Liquid fuel 340 litres (CSIRO)", ["fuel-csiro-340"], 1, False),
            ("Grain store of one year", ["grain-store-1"], 0, True),
            ("Grain store of two years", ["grain-store-2"], 0, True)]

    def joined(vals):
        out = []
        for v in vals:
            if v not in out:
                out.append(v)
        return " to ".join(out)

    def cap(rel, term):
        return r(scr[(rel, "reference", term)]["national capacity (million)"], 1)

    body = [["Reference (national capacity, million)", " / ".join(cap(x, "short") for x in rels), " / ".join(cap(x, "long") for x in rels),
             " / ".join(str(int(scr[(x, "reference", "long")][cnt])) for x in rels)]]
    for label, ids, dl, bold in spec:
        short = " / ".join(joined([pct(scr[(x, i, "short")][chg], 1) for i in ids]) for x in rels)
        long_ = " / ".join(joined([pct(scr[(x, i, "long")][chg], dl) for i in ids]) for x in rels)
        counts = " / ".join(joined([str(int(scr[(x, i, "long")][cnt])) for i in ids]) for x in rels)
        body.append([label, short, b(long_) if bold else long_, counts])
    return ["scenarios_by_region.csv"], md(["Scenario", "Short term, improved / corrected", "Long term, improved / corrected",
                                            "Regions over capacity, long term, improved / corrected"], body)


def t_long_term_national():
    lr = rows("long_term_regions.csv")
    body = []
    for rel, label in (("2011-fixed", "2011"), ("2025-fixed", "2025")):
        x = [v for v in lr if v["release"] == rel]
        nat = next(v for v in x if v["kind"] == "nation")
        reg = [v for v in x if v["kind"] != "nation"]
        over = [v for v in reg if float(v["ratio"]) < 1]
        cap, pop = float(nat["capacity_long"]), float(nat["population"])
        regsum = sum(float(v["capacity_long"]) for v in reg)
        popshare = sum(float(v["population"]) for v in over) / sum(float(v["population"]) for v in reg) * 100
        body.append([label, f"{r(cap / 1e6, 1)} / {r(pop / 1e6, 1)} = {r(nat['ratio'], 2)}", str(len(over)), str(len(reg) - len(over)),
                     f"{r(popshare, 0)}%", f"{r(regsum / 1e6, 1)} / {r(cap / 1e6, 1)} = {r(regsum / cap * 100, 0)}%"])
    return ["long_term_regions.csv"], md(["", "Nation, capacity over population", "Regions over capacity (of 53)", "Regions under capacity",
                                          "Population living in over-capacity regions", "Sum of regional capacities over the national"], body)


def t_levers():
    lv = {x["lever"]: x for x in rows("long_term_levers.csv") if x["release"] == "2025-fixed" and x["zone"] == "1"}
    ref = float(lv["long settings"]["alone"])

    def key(prefix):
        return next(k for k in lv if k.startswith(prefix))

    def span(prefix):
        a, c = re.search(r"\(([\d.]+) to ([\d.]+)\)", key(prefix)).groups()
        return comma(a), comma(c)

    def wo(prefix):
        return float(lv[key(prefix)]["without"]) / 1e6

    def withpct(prefix, d=0):
        v = wo(prefix)
        return f"{r(v, 1)} ({sg((v * 1e6 / ref - 1) * 100, d)}%)"

    fa, fb = span("fuel")
    na, nb = span("fibre (")
    ma, mb = span("fibreNat")
    wa, wb = span("fibreWool")
    flat = [wo("timber"), wo("infrastr2"), wo("nature2")]
    assert all(abs(v * 1e6 - ref) < 1 for v in flat), "timber, infrastructure and reserve rows should equal the long-term reference"
    body = [
        ["100-year drought allowance", withpct("resilience")],
        [f"Liquid fuel ({fa} to {fb} litres a person)", withpct("fuel")],
        ["No avoidable waste", withpct("losses")],
        ["Organic farming", withpct("organic")],
        ["Activity level 3", r(wo("activity"), 1)],
        ["Biofuel share", r(wo("biofuel"), 1)],
        [f"Fibre ({na} to {nb})", withpct("fibre (")],
        [f"Fibre from natural sources ({ma} to {mb})", withpct("fibreNat")],
        [f"Fibre from wool ({wa} to {wb})", withpct("fibreWool")],
        ["Red-meat share, meat and egg share", f"{r(wo('redmeat'), 1)} and {r(wo('meategg'), 1)} (both help capacity)"],
        ["Timber, infrastructure area, the 30% reserve", f"{r(flat[0], 1)} (no effect: non-agricultural land absorbs them)"],
    ]
    return ["long_term_levers.csv"], md(["Setting", "Without it (long term becomes)"], body)


def t_measures():
    # measures.csv has two columns both called "change"; read it by position. Column 0 is the release (decision 86, B91):
    # every measure is on 2025-fixed; the grain stores are also on the improved release, where they were built.
    with open(os.path.join(HERE, "measures.csv"), newline="") as f:
        rd = csv.reader(f)
        next(rd)
        allrows = list(rd)
    raw = {row[1]: row for row in allrows if row[0] == "2025-fixed"}
    store = {(row[0], row[1]): row for row in allrows}

    def val(name, term, d):
        row = raw[name]
        v, ch = (row[3], row[4]) if term == "S" else (row[5], row[6])
        return f"{r(v, 1)} ({pct(ch, d)})"

    def two(n1, n2, term, d):
        return val(n1, term, d) + " / " + val(n2, term, d)

    NA = "n/a"
    FC = ("Field-crop yields +10%", "Field-crop yields +20%")
    LV = ("Livestock output +10%", "Livestock output +20%")
    IR = ("Irrigated share of cropland 0.02 (now 0.007)", "Irrigated share of cropland 0.05 (now 0.007)")
    W6 = "Waste at the national target (6%)"
    body = [
        ["Field-crop yields +10% / +20%", "wheat, barley, other field crops, cotton", two(*FC, "S", 1), two(*FC, "L", 1)],
        ["Horticulture yields +10%", "vegetables, fruit, nuts", val("Horticulture yields +10%", "S", 1), val("Horticulture yields +10%", "L", 1)],
        ["**Livestock output +10% / +20%**", "meat, wool and milk per hectare", b(two(*LV, "S", 1)), b(two(*LV, "L", 1))],
        ["All yields +10%", "every food yield", val("All yields +10%", "S", 1), val("All yields +10%", "L", 1)],
        ["**Drought-proofing: the worst year loses half as much**", "long term, the 100-year factor 0.4558 to 0.7279", NA,
         b(val("Drought-proofing: worst year loses half as much", "L", 0))],
        ["Irrigated share of cropland 2% / 5% (now 0.7%)", "more irrigation; water not constrained", two(*IR, "S", 1), two(*IR, "L", 1)],
        [W6, "avoidable waste 0.06", val(W6, "S", 0),
         val(W6, "L", 1)[:-1] + "; the long-term settings assume no avoidable waste, so a 6% target is a step back)"],
        ["No avoidable waste", "avoidable waste 0", val("No avoidable waste", "S", 0), NA],
        ["Full recycling of food waste", "recycling 1", val("Full recycling of food waste", "S", 1), NA + " (already 1)"],
        ["Cropland +25% taken from pasture", "more cropping, less pasture", val("Cropland +25% from pasture", "S", 1), val("Cropland +25% from pasture", "L", 1)],
        ["Cropland doubled from non-agricultural land", "the 1975 CSIRO case", val("Cropland doubled from non-agricultural land", "S", 1),
         val("Cropland doubled from non-agricultural land", "L", 1)],
        ["**Diet: meat and eggs 5% of the diet**", "the meat and egg share", b(val("Diet: meat and eggs 5%", "S", 0)), b(val("Diet: meat and eggs 5%", "L", 0))],
        ["Diet: meat and eggs 7.5%", "", val("Diet: meat and eggs 7.5%", "S", 0), NA + " (already 7.5%)"],
        ["**Diet: red meat 30% of meat (more poultry and pork)**", "red-meat share of meat",
         b(val("Diet: red meat 30% of meat", "S", 0)), b(val("Diet: red meat 30% of meat", "L", 0))],
        ["Liquid fuel 156 litres a person", "electrified transport", val("Liquid fuel 156 litres a person", "S", 1), val("Liquid fuel 156 litres a person", "L", 1)],
        ["**Grain store of one year / two years**", "a buffer against the weather; the store's resilience table on 2025-fixed",
         pct(store[("2025-fixed (resilience table of 2025-store-1)", "Grain store of one year")][4], 0),
         b(" / ".join(f"{r(store[(f'2025-fixed (resilience table of 2025-store-{k})', n)][5], 1)} ({pct(store[(f'2025-fixed (resilience table of 2025-store-{k})', n)][6], 1)})"
                      for k, n in (("1", "Grain store of one year"), ("2", "Grain store of two years"))))],
        ["Grain store, as first computed (improved release, 2025-store-1 / 2025-store-2; reference 18.5)", "",
         pct(store[("2025-store-1", "Grain store of one year")][4], 0),
         " / ".join(f"{r(store[(f'2025-store-{k}', n)][5], 1)} ({pct(store[(f'2025-store-{k}', n)][6], 1)})"
                    for k, n in (("1", "Grain store of one year"), ("2", "Grain store of two years")))],
    ]
    return ["measures.csv"], md(["Measure", "What it does in the model", "Short term", "Long term"], body)


def t_method_effects():
    me = {(x["vintage"], x["term"], x["module"]): x for x in rows("method_effects_summary.csv")}
    spec = [("Beef carcase yield 0.705", "beef-carcase-yield"), ("Biodiesel yield", "biodiesel-yield"),
            ("Australian loss factors", "loss-factors-australia"), ("Dairy on land that can carry it", "dairy-good-land"),
            ("Beef output by state", "regional-beef-output"), ("Reserve pro rata", "reserve-pro-rata"),
            ("Recycling by stage", "recycling-stage"), ("Organic ruminant factor", "organic-ruminant-factor")]

    def cell(x):
        n, lo, hi = (float(x[k]) for k in ("nation (% of published)", "regional min", "regional max"))
        if lo == 0 and hi == 0 and n == 0:
            return "0"
        nat = sg(n, 1)
        if nat == "0" and lo < 0 < hi:
            nat = "0.0"  # rounds to zero nationally but the regions differ, so keep the decimal
        return f"{nat} ({sg(lo, 1)} to {sg(hi, 1)})"

    body = []
    for label, mod in spec:
        s, l = me[("2025", "short", mod)], me[("2025", "long", mod)]
        assert s["tier"] == l["tier"]
        body.append([label, s["tier"], cell(s), cell(l)])
    return ["method_effects_summary.csv"], md(["Module", "Tier", "Short term: nation (regional min to max)", "Long term: nation (regional min to max)"], body)


def t_method_status():
    body = []
    for x in rows("method_status.csv"):
        body.append([f"{x['vintage']} {x['term']} term", x["regions over capacity: published"], x["corrected"], x["improved"],
                     ", ".join(x["regions that change corrected to improved"].split("; "))])
    return ["method_status.csv"], md(["", "Published", "Corrected", "Improved", "Regions that change status, corrected to improved"], body)


# id, header row of the hand-typed table (used once, to find it before markers exist), function
TABLES = [
    ("regional_flips", "| | Regions over capacity 2011 |", t_flips),
    ("shocks_summary", "| | Return period | National capacity over population", t_shocks),
    ("named_scenarios", "| Scenario | Short term, improved / corrected |", t_scenarios),
    ("long_term_national", "| | Nation, capacity over population |", t_long_term_national),
    ("long_term_levers", "| Setting | Without it (long term becomes) |", t_levers),
    ("measures", "| Measure | What it does in the model | Short term | Long term |", t_measures),
    ("method_effects_national", "| Module | Tier | Short term: nation", t_method_effects),
    ("method_status", "| | Published | Corrected | Improved |", t_method_status),
]


def block(tid, fn):
    # A csv named as "x.csv" in the header comment is what the numbers lint treats as the section's
    # anchor file; a table that borrows a few cells from a second csv names it without the extension
    # so that the second csv does not widen the anchor for the rest of the section.
    srcs, lines = fn()
    head = [f"<!-- generated: {SCRIPT} {tid} -->", f"<!-- source: {', '.join(srcs)}; commit: {commit()} -->"]
    return head + lines + ["<!-- end generated -->"]


def replace_in(text, tid, anchor, new):
    marker = re.compile(r"<!-- generated: " + re.escape(SCRIPT) + " " + re.escape(tid) + r" -->\n.*?<!-- end generated -->", re.S)
    if marker.search(text):
        return marker.sub(lambda m: "\n".join(new), text, count=1), "replaced"
    lines = text.split("\n")
    hits = [i for i, l in enumerate(lines) if l.startswith(anchor)]
    if len(hits) != 1:
        raise SystemExit(f"table {tid}: header row found {len(hits)} times, expected 1")
    i = hits[0]
    j = i
    while j < len(lines) and lines[j].startswith("|"):
        j += 1
    return "\n".join(lines[:i] + new + lines[j:]), "wrapped"


def main():
    write = "--write" in sys.argv
    only = sys.argv[sys.argv.index("--only") + 1].split(",") if "--only" in sys.argv else None
    built = [(tid, anchor, block(tid, fn)) for tid, anchor, fn in TABLES if only is None or tid in only]
    if not write:
        for tid, _, blk in built:
            print("\n".join(blk))
            print()
        return
    text = open(README, encoding="utf-8").read()
    for tid, anchor, blk in built:
        text, how = replace_in(text, tid, anchor, blk)
        print(f"{tid}: {how}")
    open(README, "w", encoding="utf-8").write(text)


if __name__ == "__main__":
    main()
