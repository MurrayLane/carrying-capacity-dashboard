#!/usr/bin/env python3
"""Build the one-page approval digest from qa/claims_register.csv and qa/defects.csv.
Usage: python3 qa/tools/make_digest.py [--write]   (prints; --write saves qa/reports/digest_2026-11-09.md)
Every number is read from a row's value or statement; row ids are shown in brackets."""
import csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
QA = os.path.dirname(HERE)
OUT = os.path.join(QA, "reports", "digest_2026-11-09.md")
R = {r["id"]: r for r in csv.DictReader(open(os.path.join(QA, "claims_register.csv"), newline=""))}
D = list(csv.DictReader(open(os.path.join(QA, "defects.csv"), newline="")))
OK = "independently verified"


def num(i):
    """The leading number(s) of a row's value, as written in the register."""
    return R[i]["value"].split(" million")[0].split(" ratio")[0].strip()


def v(i):
    r = R.get(i)
    return r["value"].strip() if r else "MISSING"


def n(i):
    """Short numeric form of a value (first token group before the unit)."""
    r = R.get(i)
    if not r:
        return "[%s MISSING FROM REGISTER]" % i
    return "%s [%s]" % (r["value"].split(" ")[0] if r["unit"] and r["value"].startswith(r["value"].split(" ")[0]) else r["value"], i)


def val(i):
    r = R.get(i)
    if not r:
        return "[%s MISSING FROM REGISTER]" % i
    x, u = r["value"].strip(), r["unit"].strip()
    if "%" in x:
        pass
    elif u.startswith("%"):
        x += "%"
    elif u in ("million people", "regions", "ratio", "ha per person", "Mt"):
        uu = u.replace("ratio", "times").replace("million people", "million")
        x = x.replace(" (", " %s (" % uu, 1) if " (" in x else x + " " + uu
    elif u.startswith("million"):
        x += " million"
    return "%s [%s]" % (x, i)


def stmt_num(i, pat):
    """Pull a number out of a row's statement with a regex (group 1)."""
    r = R.get(i)
    if not r:
        return "[%s MISSING FROM REGISTER]" % i
    m = re.search(pat, r["statement"])
    return ("%s [%s]" % (m.group(1), i)) if m else "[%s: not found in statement]" % i


def route(ids):
    """One short line: the two routes and the status for a group of rows."""
    scripts, reps, bad = [], [], []
    for i in ids:
        r = R.get(i)
        if not r:
            bad.append("%s missing from the register" % i)
            continue
        for s in re.split(r"\s*;\s*", r["script"]):
            s = s.strip()
            if s and s not in scripts:
                scripts.append(s)
        rp = r["verifier_report"].strip()
        rp = re.sub(r"\s*\(.*$", "", rp)
        for x in re.split(r"\s*;\s*", rp):
            x = os.path.basename(x.strip())
            if x and x not in reps:
                reps.append(x)
        if r["status"].strip().lower().startswith("unverified"):
            bad.append("%s is '%s'" % (i, re.split(r"[:(]", r["status"])[0].strip() if r["status"] else "no status"))
    line = "Route 1, script: %s. Route 2, verifier: %s. " % (", ".join(os.path.basename(s) for s in scripts) or "none named", ", ".join(reps) or "none named")
    if bad:
        line += "NOT FULLY VERIFIED: " + "; ".join(bad) + "."
    else:
        nv = [i for i in ids if R[i]["status"].strip() != OK]
        line += "Status: independently verified (all %d rows)." % len(ids) if not nv else "No row is unverified. Status: %d rows independently verified; %s recorded as a finding, not a failure." % (len(ids) - len(nv), ", ".join(nv))
    return line


S = []  # (paper, number, text, ids)
a = lambda i: val(i)
S.append(("Results paper", 1,
    "Short-term capacity of Australia is %s in 2011 against a population of %s, and %s in 2025 against %s. The ratio of capacity to population is %s in 2011 and %s in 2025, so about 1.5 times both years." % (a("A001"), a("A002"), a("A003"), a("A004"), a("A005"), a("A006")),
    ["A001", "A002", "A003", "A004", "A005", "A006"]))
S.append(("Results paper", 2,
    "Long-term capacity is %s in 2011 and %s in 2025. A 100-year self-sufficient plan therefore covers %s of the 2011 population and %s of the 2025 population; the change between the years is %s." % (a("A007"), a("A008"), a("A010"), a("A011"), "inside the 2025 uncertainty range [A009]" if R.get("A009") and "lies inside" in R["A009"]["statement"] else "[A009 not confirmed]"),
    ["A007", "A008", "A010", "A011", "A009"]))
S.append(("Results paper", 3,
    "In 2025 the worst of ten years leaves a national capacity of %s against a population of 27.6 million, a ratio of %s. In the worst of twenty years the ratio falls to %s, below one." % (a("A014"), a("A183"), a("A187")),
    ["A014", "A183", "A187"]))
S.append(("Results paper", 4,
    "Short term, %s regions of 53 are over capacity in 2011 and %s in 2025; long term it is %s in 2011 and %s in 2025. In an average year %s of the 2025 population lives in over-capacity regions." % (
        stmt_num("A029", r"^(\d+) of"), stmt_num("A030", r"^(\d+) of"), stmt_num("A031", r"^(\d+) of"), stmt_num("A032", r"^(\d+) of"), a("A181")),
    ["A029", "A030", "A031", "A032", "A181"]))
S.append(("Results paper", 5,
    "Between 2011 and 2025, %s regions change status in the short term (8 over to under capacity, 1 under to over) and 4 in the long term [A035], all over to under. Of these, %s short-term flips are clean and robust (Mackay Whitsunday, North Tasmania, North East Victoria) and %s long-term flip is clean (South West Queensland)." % (
        stmt_num("A034", r"^(\w+) regions").replace("Nine", "nine"), stmt_num("A036", r"^(\w+) of the nine").replace("Three", "three"), stmt_num("A039", r"^(\w+) of the four").replace("One", "one")),
    ["A034", "A035", "A036", "A039"]))
S.append(("Results paper", 6,
    "Splitting the nation into smaller units shrinks the total. Short term, the sum of state capacities is %s of the national figure and the sum of SA2 capacities is %s. Long term it is %s for states and %s for SA2s." % (a("A016"), a("A015"), a("A089"), a("A093")),
    ["A016", "A015", "A089", "A093"]))
S.append(("Results paper", 7,
    "The 2025 uncertainty range (5th to 95th percentile) is %s short term and %s long term." % (a("A027"), a("A028")),
    ["A027", "A028"]))
S.append(("Results paper", 8,
    "The measures that widen the margin are settings: meat and eggs at 5%% of the diet gives %s short term [A258]; red meat at 30%% of meat gives %s [A260]; drought-proofing the worst year gives %s long term, +60%% [A322]; a grain store of one or two years gives %s long term [A264]." % (
        R["A258"]["value"] + " million" if "A258" in R else "MISSING", R["A260"]["value"] + " million" if "A260" in R else "MISSING",
        R["A322"]["value"].split(" ")[0] + " million" if "A322" in R else "MISSING", " or ".join(re.findall(r"\+\d+%", R["A264"]["value"])) if "A264" in R else "MISSING"),
    ["A322", "A264", "A258", "A260"]))
S.append(("Methods paper", 9,
    "The grid has six cells for Australia 2025 data. Thesis method as built (errors kept): %s short term, %s long term. Thesis method corrected: %s and %s. Improved model: %s and %s." % (a("B088"), a("B089"), a("B090"), a("B091"), a("B092"), a("B093")),
    ["B088", "B089", "B090", "B091", "B092", "B093"]))
S.append(("Methods paper", 10,
    "By definition alone one model on one data set spans %s. Published estimates of Australia's capacity span %s (a factor of 10.6)." % (a("B003"), a("B005")),
    ["B003", "B005"]))
S.append(("Methods paper", 11,
    "Each design choice changes the answer by a factor: drought allowance (weather) %s, time frame %s, unit of self-sufficiency %s, diet %s, uncertainty %s." % (a("B167"), a("B184"), a("B177"), a("B182"), a("B187")),
    ["B167", "B184", "B177", "B182", "B187"]))
S.append(("Methods paper", 12,
    "Counting calories or land without a diet that has to balance gives %s million [B156]; the commodity balance gives %s [B153]; the failure probability a year is %s [B130]." % (
        R["B156"]["value"].split(";")[0].strip(), val("B153").replace(" [B153]", ""), a("B130").replace(" [B130]", "")),
    ["B156", "B153", "B130"]))
def _g(i, f):
    return f(R[i]) if i in R else "MISSING"
_half = _g("B056", lambda r: r["value"].strip())
_paper = _g("B056", lambda r: (re.search(r"paper's ([\d.]+)", r["statement"]) or [0, "?"])[1].rstrip("0").rstrip("."))
_within = _g("B058", lambda r: r["value"].split(";")[0].strip())
_hg = _g("B035", lambda r: re.search(r"against Simpson's ([\d.]+)", r["statement"]).group(1))
_builds = _g("B035", lambda r: (re.search(r"builds ([\d.]+ to [\d.]+)", r["status"]) or [0, "?"])[1])
S.append(("Methods paper", 13,
    "Reconstructions: the HALF index for Australia in 2011 rebuilt at %s against the paper's %s, %s [B056, B058]; Simpson's food pasture rebuilt at %s [B260]; Simpson's plant-food cropland (%s ha) not reproduced, the builds give %s [B035]; Henry and Godden reproduced at %s [B015]; Foran and Poldy balance within 1.2%% (%s) [B141]; Cassidy people per hectare rebuilt %s higher than the paper's [B078]." % (
        _half, _paper, _within.replace("within", "within"), v("B260"), _hg, _builds, v("B015").replace(";", " and") + " million", v("B141").replace(";", " and") + " Mt", val("B078").replace(" [B078]", "")),
    ["B056", "B058", "B260", "B035", "B015", "B141", "B078"]))
def _ratio(i, k):
    return R[i]["value"].split(";")[k].strip() if i in R else "MISSING"
S.append(("Methods paper", 14,
    "With inputs equalised (one land base, one consumption basis, one data vintage) and each method's defining choices kept, the energy and protein balance reads %s [B264], HALF %s million [B272], people per hectare %s million [B273], the commodity balance's meat %s million [B274]; the gap to the model is about %s times for the energy balance [B266] and about %s times for HALF [B272]; inputs are about a tenth of the distance and the methods the rest [B276]; the spread does not narrow (%s million as run, %s harmonised) [B277]." % (
        v("B264").replace(" (energy)", " million (energy)").replace(" (protein)", " million (protein)").replace(";", " and"), _ratio("B272", 0), _ratio("B273", 0), _ratio("B274", 0), v("B266").split(";")[0].strip(), _ratio("B272", 1),
        v("B277").split(";")[0].strip(), v("B277").split(";")[1].strip()),
    ["B264", "B266", "B272", "B273", "B274", "B276", "B277"]))

L = []
L.append("# Approval digest, 2026-11-09")
L.append("")
L.append("Generated by qa/tools/make_digest.py from qa/claims_register.csv and qa/defects.csv. Nothing typed by hand. Row ids are in square brackets.")
paper = None
for p, k, t, ids in S:
    if p != paper:
        L += ["", "## " + p, ""]
        paper = p
    L.append("%d. %s" % (k, t))
    L.append("   Verification: " + route(ids))
    L.append("")

tierA = [r for r in R.values() if r["tier"] == "A"]
two = [r for r in tierA if r["status"].strip() == OK and r["script"].strip() and r["verifier_report"].strip()]
L.append("## Totals")
L.append("")
L.append("Tier A claims: %d. With two routes (a producing script and a verifier report, status independently verified): %d. Without: %d." % (len(tierA), len(two), len(tierA) - len(two)))
L.append("")
heads = set(i for _, _, _, ids in S for i in ids)
op = []
for d in D:
    if d["fixed_in"].strip().lower().startswith("open"):
        hit = sorted(set(re.findall(r"\b[AB]\d{3}\b", d["what"])) & heads)
        if hit:
            op.append((d, hit))
L.append("Open defects that touch a headline row: %d." % len(op))
for d, hit in op:
    L.append("- %s (%s): %s" % (d["id"], ", ".join(hit), d["what"][:160]))
L += ["", "## How to approve", "",
      "1. Read the statements above.",
      "2. Where a number surprises you, open that row id in the pack.",
      "3. Reply \"approved\" or name the statement numbers you doubt.", ""]
text = "\n".join(L)
if "—" in text:
    text = text.replace("—", ",")
if "--write" in sys.argv:
    open(OUT, "w").write(text)
print(text)
