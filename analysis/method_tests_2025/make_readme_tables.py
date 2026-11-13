#!/usr/bin/env python3
"""Print every generated table of analysis/method_tests_2025/README.md in markdown.

Run from the repository root:
  python3 -I analysis/method_tests_2025/make_readme_tables.py            # print the tables
  python3 -I analysis/method_tests_2025/make_readme_tables.py --write    # replace them in the README

Each table sits in the README between marker lines
  <!-- generated: analysis/method_tests_2025/make_readme_tables.py <table id> -->
  <!-- end generated -->
and the first line inside names the csv it was built from and the commit (HEAD of the
working copy, read from .git without running git). On a first --write a table that has no
markers yet is found by its header row and wrapped; on later runs the marker block is
replaced in place.

Computed cells come from the csvs in this folder. Figures published by other authors are
read from published_values.csv (column "source" says where each came from); a few labels
that quote a published input (Nix's 70 Mha) stay literal in the label text.
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


PUB = {}
for p in rows("published_values.csv"):
    PUB[(p["table"], p["row"], p["column"])] = p["value"]


def pub(table, row, col):
    return PUB[(table, row, col)]


# ---------------------------------------------------------------- tables
def t_henry_godden():
    src = [l for l in open(os.path.join(HERE, "henry_godden_summary.csv"), newline="")]
    i = next(k for k, l in enumerate(src) if l.startswith("scenario,"))
    sc = list(csv.DictReader(src[i:]))
    land = "intensive land in use assumed (Mha)"
    e, p = "energy: people (million)", "protein: people (million)"
    base, nix, hg = sc[0], sc[1], sc[2]
    body = [
        ["Production as it is, no scale-up", r(base[e], 0), r(base[p], 0)],
        [f"Scaled to Nix's 70 Mha, in-use land taken as 1990-91 sown pasture plus 2025 cropping ({float(nix[land]):g} Mha)", r(nix[e], 0), r(nix[p], 0)],
        [f"Scaled with Henry and Godden's 1990-91 in-use land unchanged ({float(hg[land]):g} Mha)", r(hg[e], 0), r(hg[p], 0)],
    ]
    return ["henry_godden_summary.csv"], md(["", "Energy (million people)", "Protein (million people)"], body)


def t_simpson_fidelity():
    d = {(x["period"], x["item"]): float(x["ha a person"]) for x in rows("simpson_food.csv")}
    per = "1991-92"
    feed = sum(v for (pp, k), v in d.items() if pp == per and k.startswith("crop: feed"))
    plant = sum(v for (pp, k), v in d.items() if pp == per and k.startswith("crop: ") and not k.startswith("crop: feed"))
    past = d[(per, "pasture total")]
    tot = d[(per, "crop plus pasture")]

    def diff(a, s):
        p = (a / s - 1) * 100
        m = abs(p)
        return f"{r(m, 1 if m < 10 else 0)}% {'higher' if p > 0 else 'lower'}"

    T = "simpson_fidelity"
    C = "Simpson (ha a person)"
    names = ["Pasture (beef, sheep, milk)", "Crop land for animal products (feed)", "Crop land for plant foods", "Crop plus pasture"]
    mine = [past, feed, plant, tot]
    body = []
    for n, a in zip(names, mine):
        s = float(pub(T, n, C))
        if a * 2 < s:
            last = b(f"not reproduced ({r(s / a, 1)} times lower)")
        else:
            last = diff(a, s)
        body.append([n, r(a, 3), pub(T, n, C), last])
    return ["simpson_food.csv"], md(["", "Rebuilt here", "Simpson", ""], body)


def t_simpson_application():
    d = {(x["period"], x["item"]): float(x["ha a person"]) for x in rows("simpson_food.csv")}
    a, z = "1991-92", "2021-23"

    def line(label, item, dec, bold_z=False):
        zs = r(d[(z, item)], dec)
        return [label, r(d[(a, item)], dec), b(zs) if bold_z else zs]

    body = [
        line("Crop land, ha a person", "crop land total", 3),
        line("Pasture, ha a person", "pasture total", 3),
        line("Crop plus pasture", "crop plus pasture", 3, True),
        line("People Australia's cropland supports at that footprint (million)", "people the cropland supports at this footprint (million)", 0),
        line("People Australia's pasture supports (million)", "people the pasture supports (million)", 0),
        line("People, crop plus pasture together (million)", "people, crop plus pasture together (million)", 0, True),
    ]
    return ["simpson_food.csv"], md(["", a, z], body)


def t_half_fidelity():
    T = "half_fidelity"
    C = "Paper (HALF, % of world land)"
    h = {(x["period"], x["country"]): x for x in rows("half_index.csv")}
    spec = [("World", "World"), ("United States", "United States of America"), ("India", "India"),
            ("Argentina", "Argentina"), ("Australia", "Australia"), ("New Zealand", "New Zealand")]
    body = []
    for label, key in spec:
        a = float(h[("2011", key)]["HALF % of world land"])
        s = float(pub(T, label, C))
        dv = sg((a / s - 1) * 100, 1) + "%"
        if label == "Australia":
            body.append([b(label), b(r(a, 1)), pub(T, label, C), b(dv)])
        elif label == "New Zealand":
            body.append([label, r(a, 1), pub(T, label, C), b(dv)])
        else:
            body.append([label, r(a, 1), pub(T, label, C), dv])
    return ["half_index.csv"], md(["", "Rebuilt", "Paper", "Difference"], body)


def t_half_application():
    h = {(x["period"], x["country"]): x for x in rows("half_index.csv")}
    spec = [("Australia 2011", "2011", "Australia", False), ("Australia 2021-23", "2021-23", "Australia", True),
            ("United States 2021-23", "2021-23", "United States of America", False),
            ("India 2021-23", "2021-23", "India", False), ("World 2021-23", "2021-23", "World", False)]
    body = []
    for label, per, key, bold in spec:
        x = h[(per, key)]
        cells = [label, r(x["HALF % of world land"], 1), r(x["ha a person"], 2), r(x["animal products"], 2)]
        if bold:
            cells = [b(c) for c in cells]
        body.append(cells)
    return ["half_index.csv"], md(["", "HALF, % of world land", "Hectares a person", "of which animal products"], body)


def t_cassidy_fidelity():
    T = "cassidy_fidelity"
    cols = ["Food %", "Feed %", "Other %", "Delivered %", "People per ha, produced", "People per ha, delivered"]
    c = {(x["period"], x["country"]): x for x in rows("cassidy.csv")}
    spec = [("World", "World", "World, rebuilt (2011)"), ("United States", "United States of America", "United States, rebuilt"),
            ("India", "India", "India, rebuilt"), ("China", "China", "China, rebuilt"), ("Brazil", "Brazil", "Brazil, rebuilt")]
    body = []
    for label, key, rl in spec:
        x = c[("2011", key)]
        body.append([rl, r(x["food %"], 0), r(x["feed %"], 0), r(x["other %"], 0), r(x["delivered % of produced"], 0),
                     r(x["people fed per ha, produced"], 1), r(x["people fed per ha, delivered"], 1)])
        body.append([f"{label}, paper"] + [pub(T, f"{label}, paper", k) for k in cols])
    return ["cassidy.csv"], md([""] + cols, body)


def t_cassidy_application():
    c = {(x["period"], x["country"]): x for x in rows("cassidy.csv")}
    spec = [("Australia", "Australia"), ("World", "World"), ("United States", "United States of America"), ("India", "India")]
    body = []
    for label, key in spec:
        x = c[("2021-23", key)]
        mha = float(x["cropland of these crops (Mha)"])
        mha_s = comma(r(mha, 0)) if mha >= 100 else r(mha, 1)
        deliv = r(x["people fed per ha, delivered"], 1)
        body.append([label, mha_s, f"{r(x['food %'], 0)} / {r(x['feed %'], 0)} / {r(x['other %'], 0)}",
                     r(x["delivered % of produced"], 0), r(x["people fed per ha, produced"], 1),
                     b(deliv) if label == "Australia" else deliv])
    return ["cassidy.csv"], md(["", "Cropland of the 21 crops (Mha)", "Food / feed / other %", "Delivered %",
                                "People per ha, produced", "People per ha, delivered"], body)


def t_fearnside():
    f = {x["release"]: x for x in rows("fearnside_failure_curve.csv")}
    cols = ["capacity, average year", "capacity at 1 in 5 (20%)", "at 1 in 10 (10%)", "at 1 in 20 (5%)", "at 1 in 50 (2%)", "at 1 in 100 (1%)"]
    ret = "failure return period at the population, years (linear in T to log T)"
    prob = "failure probability a year at the population, % (range)"
    body = []
    for label, rel in (("2011 data", "2011-fixed"), ("2025 data", "2025-fixed")):
        x = f[rel]
        lo, hi = sorted(int(v) for v in x[ret].split(" to "))
        body.append([label] + [r(x[k], 1) for k in cols] + [r(x["population (million)"], 1),
                    f"{x[prob]}% (about 1 in {lo} to {hi})"])
    return ["fearnside_failure_curve.csv"], md(["", "Average year (deterministic)", "1 in 5 (20%)", "1 in 10 (10%)", "1 in 20 (5%)",
                                              "1 in 50 (2%)", "1 in 100 (1%)", "Population", "Failure probability a year at the population"], body)


def t_foran_poldy():
    items = rows("foran_poldy_balance.csv")
    req, act = {}, {}
    for x in items:
        key = x["item"]
        if key.startswith("capacity reading 2021-23, their requirement"):
            n, _, v = x["value"].rpartition(": ")
            req[n] = v
        elif key.startswith("capacity reading 2021-23, actual use"):
            n, _, v = x["value"].rpartition(": ")
            act[n.split(" (")[0]] = v
    spec = [("Meat", "meat", "meat", True), ("Grain, direct", "grain, direct", None, False),
            ("Grain with embodied feed grain", "grain with embodied feed grain", "grain with feed grain", False),
            ("Fish", "fish", "fish", False)]
    body = []
    for label, rk, ak, bold in spec:
        a = req[rk]
        z = act.get(ak, "n/a") if ak else "n/a"
        a_s = f"{a} million"
        z_s = f"{z} million" if z != "n/a" else "n/a"
        body.append([label, b(a_s) if bold else a_s, b(z_s) if bold else z_s])
    return ["foran_poldy_balance.csv"], md(["", "On their requirement per person", "On actual 2021-23 use per person"], body)


def t_model_entry():
    m = {x["release"]: x for x in rows("model_entry.csv")}
    spec = [("2025-mirror", "Thesis method as built, errors kept (`2025-mirror`)", False),
            ("2025-fixed", "**Thesis method, corrected** (`2025-fixed`, the baseline entry)", True),
            ("2025-improved", "**Improved** (`2025-improved`)", True)]
    body = []
    for rel, label, bold in spec:
        x = m[rel]
        cells = [
            f"{r(x['short term (million)'], 1)} ({x['short term, 5th to 95th percentile']})",
            f"{r(x['long term (million)'], 1)} ({x['long term, 5th to 95th percentile']})",
            r(x["worst of 10 years"], 1),
            r(x["worst of 100 years"], 1),
        ]
        body.append([label] + ([b(c) for c in cells] if bold else cells))
    return ["model_entry.csv"], md(["Tier", "Short term", "Long term", "Worst of 10 years", "Worst of 100 years"], body)


def t_cross_method():
    f = {x["release"]: x for x in rows("fearnside_failure_curve.csv")}["2025-fixed"]
    reading = "reading for Australia on current data (million people)"
    body = []
    for x in rows("cross_method.csv"):
        name, rd = x["method"], x[reading]
        if name.startswith("Failure probability"):
            rd = (f"{r(f['capacity, average year'], 1)} (average year), {r(f['at 1 in 10 (10%)'], 1)} (1 in 10), "
                  f"{r(f['at 1 in 100 (1%)'], 1)} (1 in 100)")
        if name.startswith("The model"):
            name, rd = b(name), b(rd)
        body.append([name, x["counts"], x["what it leaves out"], rd])
    return ["cross_method.csv", "fearnside_failure_curve"], md(["Method", "What it counts", "What it leaves out", "Reading (million)"], body)


def t_design_choices():
    d = rows("design_choices.csv")
    by = {}
    for x in d:
        by.setdefault(x["design choice"], []).append(x)
    lo, hi, ov = "capacity low (million)", "capacity high (million)", "high over low"

    def ratio(v):
        return r(v, 1 if float(v) >= 2 else 2)

    def one(label, key, compared, whole=False, idx=0):
        # the published-count and energy-count rows are whole numbers (100, 184, 264); every other value has one decimal
        x = by[key][idx]
        f = (lambda v: r(v, 0)) if whole else (lambda v: r(v, 1))
        return [label, compared, r(x[lo], 1), f(x[hi]), ratio(x[ov])]

    def two(label, key, compared, whole=False):
        return one(label, key, compared, whole, idx=1)

    waste_imp = by["Avoidable waste"][1]
    shares = by["Unit of self-sufficiency"][0]["source"].split("shares ", 1)[1]
    shares = re.sub(r"State\b", "states", shares)
    shares = re.sub(r"NRM region\b", "NRM regions", shares)
    exp_hi = r(by["Exports counted"][0][hi], 0)
    body = [
        one("Drought allowance", "Drought allowance", "average year against worst of 5, 10, 20, 50, 100 years"),
        one("Avoidable waste", "Avoidable waste",
            f"12% against none (corrected; improved {r(waste_imp[lo], 1)} to {r(waste_imp[hi], 1)}, {ratio(waste_imp[ov])})"),
        one("Land available", "Land available", "cropland as it is against doubled"),
        one("Unit of self-sufficiency", "Unit of self-sufficiency", f"nation against the sum over SA2s ({shares})"),
        one("Diet", "Diet", "guideline diets from 15% to 5% meat and eggs (improved)"),
        one("Diet, optimised", "Diet (optimised)", "default against nutrition-optimised diet C (improved)"),
        one("Australian settings", "Australian settings", "corrected against improved"),
        one("Time frame", "Time frame", "long-term settings against short-term settings"),
        one("Exports counted", "Exports counted", f"the model against the CSIRO and UQ proportional count ({exp_hi})", True),
        one("Exports counted (energy, FAO energy per kg)", "Exports counted (energy)",
            "the model against the energy count of exports alone, all foods, at FAOSTAT's own food energy per kg", True),
        two("Exports counted (energy, as-traded densities)", "Exports counted (energy)",
            "the model against the energy count of exports alone, all foods, at typed as-traded densities", True),
        one("Uncertainty", "Uncertainty (Monte Carlo)", "Monte Carlo 5th to 95th percentile, 13 uncertain choices"),
    ]
    return ["design_choices.csv"], md(["Design choice", "Compared", "Low", "High", "High over low"], body)


def t_ladder():
    labels = {
        "thesis long-term figure as built (2011 data, error kept)": "The thesis's long-term figure as built (2011 data, biodiesel error kept)",
        "long term, corrected (2025)": "Long term, corrected (2025)",
        "worst of 100 years, short-term diet": "Worst of 100 years, today's diet",
        "worst of 10 years (Jones: 30 to 35)": "Worst of 10 years (the Jones committee's 30 to 35)",
        "average year": "Average year",
        "average year, improved settings": "Average year, improved settings",
        "average year, no avoidable waste": "Average year, no avoidable waste",
        "average year, improved, no avoidable waste": "Average year, improved, no avoidable waste",
        "exports counted as a proportion (CSIRO and UQ 2025)": "Exports counted as a proportion (CSIRO and UQ)",
        "energy count of exports alone, all foods": "Energy count of exports alone",
    }
    body = [[labels[x["step"]], big(x["million people"])] for x in rows("ladder.csv")]
    return ["ladder.csv"], md(["Step", "Million"], body)


def t_gap_attribution():
    g = rows("gap_attribution.csv")

    def pick(method, case, cid, has=""):
        hit = [x for x in g if x["method"] == method and x["case"] == case and x["cause_id"] == cid and has in x["cause"]]
        assert len(hit) == 1, (method, case, cid, has, len(hit))
        return hit[0]

    def within_rounding(x):
        # B93 (decision 88): a residual (published less this test) of no more than half a unit of the published
        # figure's last printed digit carries no information as a share, so the table says "within rounding".
        pub, cur = x["published"], x["current"]
        if not pub or not cur:
            return False
        dec = len(pub.split(".")[1]) if "." in pub else 0
        return abs(float(pub) - float(cur)) <= 0.5 * 10 ** -dec

    def pct(x):
        if within_rounding(x):
            return "within rounding"
        return sg(x["explained % of residual"], 0) + "%" if x["explained % of residual"] else "n/a"

    # B93: the csv holds figures already rounded (-12.5 for -12.48; 32.855 for 32.8546), and rounding them again
    # gave -13% and 32.86. These two cells are printed from the script's unrounded values (gap_check.py, B93).
    unrounded = {
        ("Simpson pasture", "Australia 1991-92, ha a person", "a1", ""): {"explained % of residual": "-12.48"},
        ("Foran and Poldy", "grain 1997-98, Mt", "b", "1996 to 1998"): {"figure": "32.8546"},
    }

    sel = [
        # (method, case, cause id, text the cause contains, label in the table, decimals)
        ("HALF", "Australia 2011", "a", "", "HALF, Australia 2011", "(a) adjustment 1.129 in place of 1.165", 2),
        ("HALF", "Australia 2011", "b1", "", "", "(b) pasture 3,364 Mha as the supplement prints it", 2),
        ("HALF", "Australia 2011", "b2", "", "", "(b) livestock output as printed", 2),
        ("HALF", "Australia 2011", "b3", "", "", "(b) soybean balance as printed", 2),
        ("HALF", "Australia 2011", "b4", "", "", "(b) world land 13,009 Mha", 2),
        ("HALF", "Australia 2011", "b5", "", "", "(b) feed pool and feed cropland as printed (derived)", 2),
        ("HALF", "Australia 2011", "c+", "", "", "(c) processing shares, upper rounding bound", 2),
        ("HALF", "World 2011", "a", "", "HALF, world 2011", "(a) adjustment 1.129", 2),
        ("HALF", "World 2011", "b1", "", "", "(b) pasture 3,364 Mha", 2),
        ("HALF", "World 2011", "b5", "", "", "(b) feed pool and feed cropland as printed (derived)", 2),
        ("HALF", "World 2011", "c+", "", "", "(c) processing shares, upper rounding bound", 2),
        ("HALF", "United States 2011", "a", "", "HALF, United States 2011", "(a) adjustment 1.129", 2),
        ("HALF", "United States 2011", "b1", "", "", "(b) pasture 3,364 Mha", 2),
        ("HALF", "Argentina 2011", "a", "", "HALF, Argentina 2011", "(a) adjustment 1.129", 2),
        ("HALF", "Argentina 2011", "b1", "", "", "(b) pasture 3,364 Mha", 2),
        ("HALF", "India 2011", "a", "", "HALF, India 2011", "(a) adjustment 1.129", 2),
        ("HALF", "India 2011", "b1", "", "", "(b) pasture 3,364 Mha", 2),
        ("Simpson pasture", "Australia 1991-92, ha a person", "a1", "", "Simpson pasture, ha a person", "(a) sheep-meat rate 34.1 (5.5 x 5 x 1.24)", 3),
        ("Simpson pasture", "Australia 1991-92, ha a person", "b-low", "", "", "(b) retail in place of carcase weight (ABS ratios)", 3),
        ("Simpson pasture", "Australia 1991-92, ha a person", "c2", "", "", "(c) all milk on pasture at the world milk rate", 3),
        ("Simpson pasture", "Australia 1991-92, ha a person", "d2", "", "", "(d) calendar 1991, mean of 1990-91 and 1991-92", 3),
        ("Simpson pasture", "Australia 1991-92, ha a person", "e", "mean 1990-91", "", "(e) 1991-92 tonnes over the 1990-91 mean population", 3),
        ("Simpson pasture", "Australia 1991-92, ha a person", "e", "ERP 30 June 1991", "", "(e) 1991-92 tonnes over the population at 30 June 1991", 3),
        ("Henry and Godden", "energy, 1990-91, million people", "b1", "", "Henry and Godden, energy, million", "(b) factor 82/466 unrounded", 2),
        ("Henry and Godden", "energy, 1990-91, million people", "b2+", "", "", "(b) Gifford's projected 82 at its rounding bound, 82.5", 2),
        ("Henry and Godden", "protein, 1990-91, million people", "b1", "", "Henry and Godden, protein, million", "(b) factor 60/294 unrounded", 2),
        ("Henry and Godden", "protein, 1990-91, million people", "b2+", "", "", "(b) Gifford's projected 60 at its rounding bound, 60.5", 2),
        ("Foran and Poldy", "grain 1997-98, Mt", "b", "calendar 1997 alone", "Foran and Poldy, grain 1997-98, Mt", "(b) calendar 1997 alone", 2),
        ("Foran and Poldy", "grain 1997-98, Mt", "b", "1996 to 1998", "", "(b) three-year mean 1996 to 1998", 2),
        ("Foran and Poldy", "grain 1997-98, Mt", "c1", "", "", "(c) wheat plus coarse grains (cereals less rice)", 2),
        ("Foran and Poldy", "meat 1997-98, Mt", "b", "calendar 1998 alone", "Foran and Poldy, meat 1997-98, Mt", "(b) calendar 1998 alone", 2),
        ("Foran and Poldy", "meat 1997-98, Mt", "b", "1997 to 1999", "", "(b) three-year mean 1997 to 1999", 2),
        ("Cassidy", "World, people per ha produced", "a", "1997 to 2003", "Cassidy, world, people a hectare produced", "(a) each crop at its 1997 to 2003 yield", 1),
        ("Cassidy", "World, people per ha delivered", "a", "1997 to 2003", "Cassidy, world, people a hectare delivered", "(a) each crop at its 1997 to 2003 yield", 1),
        ("Cassidy", "World, people per ha delivered", "b2", "", "", "(b) the paper's average feed efficiency (4% over 36%)", 1),
        ("Cassidy", "World, people per ha delivered", "a+b2", "", "", "(a) and (b) together", 1),
        ("Cassidy", "United States, people per ha produced", "a", "1997 to 2003", "Cassidy, United States, produced", "(a) each crop at its 1997 to 2003 yield", 1),
        ("Cassidy", "India, people per ha produced", "a", "1997 to 2003", "Cassidy, India, produced", "(a) each crop at its 1997 to 2003 yield", 1),
        ("Cassidy", "China, people per ha produced", "a", "1997 to 2003", "Cassidy, China, produced", "(a) each crop at its 1997 to 2003 yield", 1),
        ("Cassidy", "Brazil, people per ha produced", "a", "1997 to 2003", "Cassidy, Brazil, produced", "(a) each crop at its 1997 to 2003 yield", 1),
    ]
    body = []
    for method, case, cid, has, lab, cause, d in sel:
        x = {**pick(method, case, cid, has), **unrounded.get((method, case, cid, has), {})}
        first = [b(lab), r(x["current"], d), x["published"]] if lab else ["", "", ""]
        body.append(first + [cause, r(x["figure"], d), pct(x)])
    return ["gap_attribution.csv"], md(["Test (figure)", "This test", "Published", "Cause changed, one at a time", "Figure with that cause", "Share of the residual explained"], body)


def t_harmonised():
    hc = rows("harmonised_comparison.csv")
    A, B = "(a) as the authors would run it (million)", "(b) harmonised (million)"
    C, DF, DI, E = "(c) input effect, b over a", "(d) b over corrected", "(d) b over improved", "(e) local-productivity adjustment, Wackernagel and Rees p. 78 (million)"
    by = {}
    for x in hc:
        by.setdefault(x["method"], []).append(x)

    def num(x):
        return big(x) if float(x) >= 100 else r(x, 1)

    def rng(vals, fmt=num):
        vals = sorted(float(v) for v in vals if v != "")
        if not vals:
            return ""
        lo, hi = fmt(vals[0]), fmt(vals[-1])
        return lo if lo == hi else f"{lo} to {hi}"

    def fac(xs, col):
        return rng([x[col] for x in xs], lambda v: r(v, 2))

    def pick(xs, *keys):
        return [x for x in xs if any(k in x["reading"] for k in keys)]

    body = []
    for name, xs in by.items():
        if name.startswith("Summary"):
            continue
        a = rng([x[A] for x in xs])
        bb = rng([x[B] for x in xs])
        c = fac(xs, C)
        d = f"{fac(xs, DF)} and {fac(xs, DI)}" if fac(xs, DF) else ""
        e = rng([x[E] for x in xs])
        if name.startswith("Energy"):
            en, pr = pick(xs, "energy"), pick(xs, "protein")
            bb = f"{num(en[0][B])} (energy), {num(pr[0][B])} (protein)"
        elif name.startswith("Ecological"):
            cb = pick(xs, "cropland-bound")
            tg = pick(xs, "together")
            pa = pick(xs, ", pasture")
            a = f"{rng([x[A] for x in cb + tg])} (cropland-bound {rng([x[A] for x in cb])}; together {rng([x[A] for x in tg])})"
            bb = f"{rng([x[B] for x in cb + tg])} (cropland-bound {rng([x[B] for x in cb])}; together {rng([x[B] for x in tg])})"
            d = f"{fac(cb + tg, DF)} and {fac(cb + tg, DI)}"
            e = (f"{rng([x[E] for x in cb + tg])} (cropland-bound {rng([x[E] for x in cb])}; together {rng([x[E] for x in tg])}; "
                 f"pasture alone {rng([x[E] for x in pa])}); builds 1 and 3")
        elif name.startswith("Commodity"):
            a = ", ".join(f"{x['reading'].split(' ')[0]} {r(x[A], 0)}" for x in xs)
            bb = ", ".join(f"{x['reading'].split(' ')[0]} {r(x[B], 0)}" for x in xs)
        elif name.startswith("Failure"):
            a = ", ".join(f"{r(x[A], 1)} ({x['reading']})" for x in xs)
            bb, c, d = "blank: the readings are the model's own runs", "", ""
        elif name.startswith("The model"):
            name, a, bb = b(name), b(a), b(bb)
        body.append([name, a, bb, c, d, e])
    return ["harmonised_comparison.csv"], md(["Method", "(a) As the authors would run it", "(b) Harmonised", "(c) Input effect, b over a",
                                            "(d) b over the model, corrected and improved", "(e) Local-productivity adjustment (p. 78)"], body)


# id, header row of the hand-typed table (used once, to find it before markers exist), function
TABLES = [
    ("henry_godden_application", "| | Energy (million people) | Protein (million people) |", t_henry_godden),
    ("simpson_fidelity", "| | Rebuilt here | Simpson | |", t_simpson_fidelity),
    ("simpson_application", "| | 1991-92 | 2021-23 |", t_simpson_application),
    ("half_fidelity", "| | Rebuilt | Paper | Difference |", t_half_fidelity),
    ("half_application", "| | HALF, % of world land | Hectares a person | of which animal products |", t_half_application),
    ("cassidy_fidelity", "| | Food % | Feed % | Other % | Delivered % | People per ha, produced | People per ha, delivered |", t_cassidy_fidelity),
    ("cassidy_application", "| | Cropland of the 21 crops (Mha) | Food / feed / other % | Delivered % | People per ha, produced | People per ha, delivered |", t_cassidy_application),
    ("fearnside_result", "| | Average year (deterministic) | 1 in 5 (20%) |", t_fearnside),
    ("foran_poldy_application", "| | On their requirement per person | On actual 2021-23 use per person |", t_foran_poldy),
    ("model_entry", "| Tier | Short term | Long term | Worst of 10 years | Worst of 100 years |", t_model_entry),
    ("cross_method", "| Method | What it counts | What it leaves out | Reading (million) |", t_cross_method),
    ("design_choices", "| Design choice | Compared | Low | High | High over low |", t_design_choices),
    ("ladder", "| Step | Million |", t_ladder),
    ("gap_attribution", "| Test (figure) | This test | Published | Cause changed, one at a time |", t_gap_attribution),
    ("harmonised_comparison", "| Method | (a) As the authors would run it | (b) Harmonised |", t_harmonised),
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
    built = [(tid, anchor, block(tid, fn)) for tid, anchor, fn in TABLES]
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
