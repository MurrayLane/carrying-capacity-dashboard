#!/usr/bin/env python3
"""manuscript_audit: tie every number in the four manuscript documents to the claims register.

Run from the repository root:   python3 -I qa/tools/manuscript_audit.py [--write]
Options (all optional):
  --docs a.md b.md ...   documents to audit (default: the four below)
  --register path.csv    claims register (default qa/claims_register.csv)
  --write                write qa/reports/manuscript_audit_2026-11-07.csv and .md; without it,
                         print the summary and the orphan list
  --notes file.md        text appended to the .md report (the hand-made spot checks)
  --out-base path        report path without extension (default qa/reports/manuscript_audit_2026-11-07)

What it does
  1. Finds every number in each document with qa/tools/numbers_lint.py's own machinery (the
     same masks for code, urls, paths, dates, years, ids, citations, section and table numbers;
     the same NUMBER pattern; single-digit integers without a percent sign are not scanned).
     Numbers under 1 are listed (numbers_lint calls them ambiguous) and matched like the rest.
     Each number is shown with its sentence (or table cell) and its section.
  Written zeros ("0", "0%") are not listed: they match every row.
  2. Reads the numbers out of each register row's `value` and `statement` the same way
     (single digits included, since a register value can be a bare 9).
  3. Matches a document number x, written with d decimals, to a register number r when x equals
     r (or one of its scaled forms) rounded half up to d decimals:
        r itself                         41.5 against 41.50, 41.5
        r / 1e3, r / 1e6                 41.5 against 41,503,537
        r * 100 (document has a %)       75% against 0.754
        r / 100 (document under 1, register number written with %)   0.75 against 75%
     match_kind is exact (equal), rounded, or scaled (needed a scaled form).
  4. Several rows can match. Candidates are ordered by: same paper, same section, word overlap
     between the document sentence and the register statement, then match kind. The first is
     the matched row; all are listed (up to 8) in `candidates`.
  5. A number with no candidate is an orphan: a claim the register lacks.
  `basis` says whether the match came from the register `value` or only the `statement`.
  `strength` is strong when the match is exact and the word overlap with the top row is at least
  0.3, or when at most 3 rows hold the number and either the overlap is at least 0.15 or the match
  is exact and in `value`; otherwise weak (a rounded or scaled match among more than 3 rows is weak)
  (a common number such as 10, 100 or 5% lands on many rows and on unrelated statements).
  Weak matches still count as matched, as the brief defines it; the report counts and lists them.
  `n_candidates` is the number of rows that hold the number.
  The paper of a document is A or B from its folder; the section is the numbered section the
  line sits in (bold "**N.**" paragraphs after "## Sections"; "Headline" before it; section 7 for
  SECTION7_DRAFT.md and 11 for DISCUSSION_MEASURES.md; otherwise the heading text).
"""
import argparse
import csv
import importlib.util
import os
import re
import sys
from decimal import Decimal, ROUND_HALF_UP

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DOCS = [
    "papers/A_results/OUTLINE.md",
    "papers/A_results/DISCUSSION_MEASURES.md",
    "papers/B_methods/OUTLINE.md",
    "papers/B_methods/SECTION7_DRAFT.md",
]
DEFAULT_REGISTER = "qa/claims_register.csv"
DEFAULT_OUT = "qa/reports/manuscript_audit_2026-11-07"
FIXED_SECTION = {"SECTION7_DRAFT.md": "7", "DISCUSSION_MEASURES.md": "11"}
VERIFIED = "independently verified"
MAX_CANDIDATES = 8
KIND_RANK = {"exact": 0, "rounded": 1, "scaled": 2}
FUTURE_YEAR = re.compile(r"(?<![\w.,])20[3-9]\d(?![\w]|[.,]\d)")  # bare years past the lint range, e.g. 2050
STOP = set("the and for with that this from are was were has have its not but all one two per than into over under "
           "each only both when what which their they them been being more most less also any can may would should "
           "million people".split())


def load_lint():
    spec = importlib.util.spec_from_file_location("numbers_lint", os.path.join(HERE, "numbers_lint.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


L = load_lint()


def words(text):
    return {w for w in re.findall(r"[a-z]{4,}", text.lower()) if w not in STOP}


def overlap(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / float(min(len(a), len(b)))


def rounded(v, d):
    q = Decimal(1).scaleb(-d)
    return Decimal(repr(v)).quantize(q, rounding=ROUND_HALF_UP)


def parse_numbers(text, include_single):
    """Numbers in text after lint's masking: list of (value, decimals, pct, start, raw)."""
    work, _ = L.mask_line(text)
    work = FUTURE_YEAR.sub(lambda m: " " * len(m.group(0)), work)
    out = []
    for mo in L.NUMBER.finditer(work):
        intpart, frac, pct = mo.group(1), mo.group(2), mo.group(3)
        if not include_single and not frac and "," not in intpart and len(intpart) < 2 and not pct:
            continue
        value = float(intpart.replace(",", "") + (frac or ""))
        if value == 0:
            continue  # a written zero ("0%") carries no figure to match
        out.append((value, len(frac) - 1 if frac else 0, bool(pct), mo.start(), mo.group(0).strip()))
    return out


RANGE_TO = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+)(\.\d+)?(\s?%)?\s+to\s+(\d{1,3}(?:,\d{3})+|\d+)(\.\d+)?(\s?%)?(?![\d])")


def range_ends(text):
    """Both ends of a register value written "N to M". The lint mask reads some of these as a year
    range and blanks the first number, so the ends are taken from the unmasked text."""
    out = []
    for mo in RANGE_TO.finditer(text):
        for ip, fr, pc in ((mo.group(1), mo.group(2), mo.group(3)), (mo.group(4), mo.group(5), mo.group(6))):
            v = float(ip.replace(",", "") + (fr or ""))
            if v != 0:
                out.append((v, len(fr) - 1 if fr else 0, bool(pc), mo.start(), ip))
    return out


def sentence_at(line, pos):
    """The sentence (or table cell) of the line that holds character position pos."""
    if line.lstrip().startswith("|"):
        cells, start = [], 0
        for mo in re.finditer(r"\|", line):
            cells.append((start, mo.start()))
            start = mo.end()
        cells.append((start, len(line)))
        for a, b in cells:
            if a <= pos <= b:
                cell = line[a:b].strip()
                if len(cell) < 25:
                    return clean(line)
                return clean(cell)
        return clean(line)
    cuts = [0] + [m.end() for m in re.finditer(r"(?<=[.!?;])\s+(?=[A-Z0-9(*\"'`])", line)] + [len(line) + 1]
    for a, b in zip(cuts, cuts[1:]):
        if a <= pos < b:
            return clean(line[a:b])
    return clean(line)


def clean(s):
    s = re.sub(r"^\s*(?:[*\-+>]\s+|\d+[.)]\s+)+", "", s)
    s = s.replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", s).strip()


def load_register(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            nums_v = parse_numbers(r["value"], True) + range_ends(r["value"])
            nums_s = parse_numbers(r["statement"], True)
            rows.append({
                "id": r["id"], "paper": r["paper"], "section": r["section"], "status": r["status"],
                "statement": r["statement"], "value": r["value"],
                "vnums": [(n[0], n[2]) for n in nums_v], "snums": [(n[0], n[2]) for n in nums_s],
                "words": words(r["statement"]),
            })
    return rows


def forms(r, r_pct, x_pct, x_value):
    """Scaled forms of register number r: (value, scaled?)."""
    f = [(r, False)]
    if r >= 1e3:
        f.append((r / 1e3, True))
    if r >= 1e6:
        f.append((r / 1e6, True))
    if x_pct and r <= 1.0:
        f.append((r * 100.0, True))
    if x_value < 1.0 and r_pct and r >= 1.0:
        f.append((r / 100.0, True))
    return f


def number_match(x, d, pct, rr):
    """Return match kind ('exact', 'rounded', 'scaled') or None."""
    best = None
    r, r_pct = rr
    for v, scaled in forms(r, r_pct, pct, x):
        if rounded(v, d) == rounded(x, d) and (d > 0 or v >= 0):
            if abs(v - x) < 1e-9:
                k = "scaled" if scaled else "exact"
            else:
                k = "scaled" if scaled else "rounded"
            if best is None or KIND_RANK[k] < KIND_RANK[best]:
                best = k
    return best


def section_tracker(doc):
    """Return a function mapping each (0-based) line index to the section label."""
    base = os.path.basename(doc)
    fixed = FIXED_SECTION.get(base)
    labels = []
    cur = "Headline"
    insecs = False
    with open(doc, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().split("\n")
    for line in lines:
        if fixed:
            labels.append(fixed)
            continue
        h = re.match(r"(#{1,6})\s+(.*)", line)
        if h:
            title = h.group(2).strip()
            if h.group(1) == "##":
                if title.lower().startswith("sections"):
                    insecs = True
                    cur = "Sections"
                else:
                    insecs = False
                    cur = "Figures" if title.lower().startswith("figures") else title[:30]
        elif insecs:
            m = re.match(r"\*\*(\d+)\.", line)
            if m:
                cur = m.group(1)
        labels.append(cur)
    return lines, labels


def audit_doc(doc, reg):
    paper = "A" if "/A_" in doc else "B"
    lines, labels = section_tracker(doc)
    out = []
    in_fence = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for value, d, pct, pos, raw in parse_numbers(line, False):
            sent = sentence_at(line, pos)
            sw = words(sent)
            cands = []
            for r in reg:
                kind = None
                basis = None
                for src, tag in ((r["vnums"], "value"), (r["snums"], "statement")):
                    for rn in src:
                        k = number_match(value, d, pct, rn)
                        if k and (kind is None or KIND_RANK[k] < KIND_RANK[kind]):
                            kind, basis = k, tag
                    if kind:
                        break  # value basis wins over statement
                if kind:
                    ov = overlap(sw, r["words"])
                    cands.append({"row": r, "kind": kind, "basis": basis, "ov": ov,
                                  "paper": r["paper"] == paper, "sec": r["section"] == labels[i]})
            cands.sort(key=lambda c: (not c["paper"], not c["sec"], -round(c["ov"], 2), KIND_RANK[c["kind"]],
                                      c["basis"] != "value"))
            out.append({"document": doc, "paper": paper, "section": labels[i], "line": i + 1, "number": raw,
                        "sentence": sent, "cands": cands})
    return out


def finish(rec):
    c = rec["cands"]
    if not c:
        rec.update(result="orphan", row_id="", status="", kind="", basis="", strength="", overlap="")
    else:
        t = c[0]
        strong = (t["kind"] == "exact" and t["ov"] >= 0.3) or (len(c) <= 3 and (
            t["ov"] >= 0.15 or (t["kind"] == "exact" and t["basis"] == "value")))
        rec.update(result="matched", row_id=t["row"]["id"], status=t["row"]["status"], kind=t["kind"],
                   basis=t["basis"], strength="strong" if strong else "weak", overlap="%.2f" % t["ov"])
    rec["cand_text"] = "; ".join("%s(%s/%s/%s%s%s)" % (
        x["row"]["id"], x["kind"], x["basis"], "p" if x["paper"] else "-", "s" if x["sec"] else "-",
        "") for x in c[:MAX_CANDIDATES]) + (" +%d more" % (len(c) - MAX_CANDIDATES) if len(c) > MAX_CANDIDATES else "")
    return rec


def summarise(recs, docs):
    rows = []
    for d in docs:
        rs = [r for r in recs if r["document"] == d]
        m = [r for r in rs if r["result"] == "matched"]
        rows.append((d, len(rs), len(m), len(rs) - len(m),
                     sum(1 for r in m if r["status"] != VERIFIED),
                     sum(1 for r in m if r["strength"] == "weak")))
    return rows


def table(rows):
    head = "| document | numbers | matched | orphans | matched, status not `independently verified` | matched, weak |\n|---|---|---|---|---|---|\n"
    tot = [sum(r[i] for r in rows) for i in range(1, 6)]
    body = "".join("| %s | %d | %d | %d | %d | %d |\n" % r for r in rows)
    return head + body + "| **all four** | %d | %d | %d | %d | %d |\n" % tuple(tot)


def main():
    ap = argparse.ArgumentParser(description="Tie every manuscript number to the claims register.")
    ap.add_argument("--docs", nargs="+", default=DEFAULT_DOCS)
    ap.add_argument("--register", default=DEFAULT_REGISTER)
    ap.add_argument("--out-base", default=DEFAULT_OUT)
    ap.add_argument("--notes", help="markdown file appended to the .md report (the hand-made spot checks)")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    reg = load_register(a.register)
    recs = []
    for d in a.docs:
        if not os.path.isfile(d):
            print("MISSING document: %s" % d, file=sys.stderr)
            continue
        recs.extend(finish(r) for r in audit_doc(d, reg))
    docs = [d for d in a.docs if os.path.isfile(d)]
    summ = summarise(recs, docs)
    orphans = [r for r in recs if r["result"] == "orphan"]
    notver = [r for r in recs if r["result"] == "matched" and r["status"] != VERIFIED]

    if a.write:
        os.makedirs(os.path.dirname(a.out_base) or ".", exist_ok=True)
        with open(a.out_base + ".csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["document", "line", "section", "number", "sentence", "result", "row_id", "status",
                        "match_kind", "basis", "strength", "overlap", "n_candidates", "candidates"])
            for r in recs:
                w.writerow([r["document"], r["line"], r["section"], r["number"], r["sentence"], r["result"],
                            r["row_id"], r["status"], r["kind"], r["basis"], r["strength"], r["overlap"],
                            len(r["cands"]), r["cand_text"]])
        print("wrote %s.csv (%d rows)" % (a.out_base, len(recs)))
        with open(a.out_base + ".md", "w", encoding="utf-8") as fh:
            fh.write("# Manuscript audit, 2026-11-07\n\nEvery number in the four manuscript documents, tied to `qa/claims_register.csv` "
                     "by `qa/tools/manuscript_audit.py`. Full list: the .csv beside this file. Numbers are those "
                     "`numbers_lint.py` scans (single-digit integers without a percent sign are not); a number is "
                     "matched when a register `value` or `statement` holds it after the rounding and scaling rules "
                     "in the tool header.\n\n")
            fh.write("## Summary\n\n" + table(summ) + "\n")
            fh.write("## Orphans (%d)\n\n" % len(orphans))
            for r in orphans:
                fh.write("* `%s:%d` (%s, section %s) **%s**: %s\n" % (
                    os.path.basename(r["document"]), r["line"], r["paper"], r["section"], r["number"], r["sentence"]))
            fh.write("\n## Matched, status not `independently verified` (%d)\n\n" % len(notver))
            by = {}
            for r in notver:
                by.setdefault(r["status"], []).append(r)
            for st in sorted(by, key=lambda s: -len(by[s])):
                fh.write("### %s (%d)\n\n" % (st, len(by[st])))
                for r in by[st]:
                    fh.write("* `%s:%d` **%s** -> %s: %s\n" % (os.path.basename(r["document"]), r["line"],
                                                                 r["number"], r["row_id"], r["sentence"][:200]))
                fh.write("\n")
            if a.notes:
                with open(a.notes, encoding="utf-8") as nf:
                    fh.write("\n" + nf.read())
        print("wrote %s.md" % a.out_base)
    print(table(summ))
    print("orphans: %d" % len(orphans))
    if not a.write:
        for r in orphans:
            print("%s:%d [%s %s] %s | %s" % (os.path.basename(r["document"]), r["line"], r["paper"], r["section"],
                                              r["number"], r["sentence"][:160]))


if __name__ == "__main__":
    main()
