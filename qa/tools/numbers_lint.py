#!/usr/bin/env python3
"""numbers_lint: find numbers typed into documents that no current output csv contains.

Run from the repository root:   python3 -I qa/tools/numbers_lint.py
Options (all optional):
  --docs a.md b.md ...      documents to scan (default list below)
  --trusted dir1 dir2 ...   directories whose .csv files are trusted (default list below)
  --out path.csv            report path (default qa/reports/numbers_lint_2026-11-07.csv)

Purpose: a figure typed into a paper outline or README that is not in a generated output
file is either a quotation (another author's number), arithmetic in prose, or stale. The
tool cannot tell which; it lists them so a person can.

Trusted values
  Every numeric cell of every .csv under the trusted directories (column name kept).
  Identifier columns are left out (zone, parent, year, id, rank, release, preset, n and any
  column ending "code" or "_id"): a zone number is not a measurement and would match
  almost any small integer.
  Each value v is also matched as v/1e3 (when v >= 1e3) and v/1e6 (when v >= 1e6)
  (41503537 is found as 41.5 and 41.504),
  and, where 0 <= v <= 1 (a share), as v*100 (0.754 is found as 75 and 75.4). Absolute
  values are used, so a written "5" matches -5. Rounding to 0, 1 and 2 decimals is not
  stored as extra values: matching uses a tolerance, which covers every rounding.

Stale values
  --stale v1 v2 ... (or DEFAULT_STALE in this file) lists values known to be superseded.
  A document number equal to a stale value gets status "stale". Rules:
    - same decimals: the number must be written with at least as many decimals as the stale
      value and equal it within half a unit of its last digit ("45.7" and "45.70" match
      45.7; "41" never matches 40.8, "6%" never matches 6.34);
    - anchored beats stale: a number found in a csv the document names (anchor "section" or
      "document") is "found", not "stale", even when it equals a stale value;
    - context tests: 21.0 is stale only on a line containing "worst year" or "100"; 45.7 is
      not stale on a line containing "Mha", "Henry" or "in-use" (Henry and Godden's land).
  A stale hit is a prompt to check, not proof.
  Text cells in trusted csvs (such as "35.9 to 45.1") contribute every number in them.

Matching
  Because the trusted set is dense (hundreds of thousands of cells), a short number such
  as 404 or 2,290 lands near some unrelated cell by chance. A plain "equal to any trusted
  value" test cannot fail, so a match counts as found only when it is anchored:
    (a) scoped: the value is in a csv whose file name is written in the same section
        (anchor "section"; a section runs from a markdown heading to the next one) or
        anywhere in the document (anchor "document"), and at most 5 distinct values of
        those named files lie within the tolerance (more means the named files are too
        dense for the match to say anything); or
    (b) specific (anchor "specific"): no scoped file matches, but at most 3 distinct
        trusted values anywhere lie within the tolerance.
  Anything else is "not found"; its matched_file and matched_value then hold the nearest
  unanchored candidate, prefixed "weak:", so a person can see what it might be.
  Tolerance: a number written with d decimals matches a trusted value within 0.5 * 10^-d
  (half a unit in the last written digit). Deviation from a strict reading: an integer
  written with trailing zeros (for example 1,160,000 or 2,290) is read as rounded to its
  last non-zero digit, so the tolerance is half a unit of that digit.
  The matched_value of a found row ends with the count of distinct trusted values inside
  the tolerance anywhere in the trusted set.
  ambiguous: the magnitude is under 1, or the number is an integer under 10 (including
  a percentage such as 5%). These are not matched; they are reported, not failed.

What is scanned
  Decimals, integers of two or more digits, integers with thousands separators and
  percentages, on every line outside fenced code blocks.

Skip rules (status "skipped"; the rule name is written to matched_value as skip:<rule>)
  code      inline code spans between backticks, and fenced code blocks
  url       http(s) addresses
  doi       DOIs (10.xxxx/...)
  path      file paths and file names (anything ending .csv .py .md .json .xlsx .pdf .txt ...)
  hash      commit hashes and checksums (7 or more hex characters with a digit and a letter)
  date      yyyy-mm-dd, "12 March 2025", "March 2025"
  yearrange year ranges such as 2021-23, 1990-91, 2011-2025, 2021 to 23
  id        identifiers such as 2025-fixed, 2011-thesis
  citation  volume(issue), volume(issue):pages, pp. 12-34, vol. 12, no. 3, page ranges
            after a colon (12:345-367)
  section   a section or list number at the start of a line (1., 5.2, **6.**), and
            references such as "section 7", "Table 3", "Figure 2", "chapter 6", "step 2"
  tokens    token counts (12k tokens, 1,200 tokens)
  size      file sizes (30 KB, 4.1 MB)
  power     powers of ten written 10^15
  year      a bare year from 1860 to 2030
  A number inside a skipped span is not linted. One skipped row is written per span.
"""
import argparse
import bisect
import csv
import os
import re
import sys

DEFAULT_DOCS = [
    "papers/B_methods/OUTLINE.md",
    "papers/B_methods/SECTION7_DRAFT.md",
    "papers/A_results/OUTLINE.md",
    "papers/A_results/DISCUSSION_MEASURES.md",
    "analysis/method_tests_2025/README.md",
    "analysis/paper_a/README.md",
    "analysis/comparators_2025/README.md",
    "HANDOFF.md",
]
DEFAULT_TRUSTED = [
    "results",
    "analysis/method_tests_2025",
    "analysis/paper_a",
    "analysis/comparators_2025",
    "analysis/sensitivity_2025",
    "analysis/scale_curve_2025",
]
MAX_POOL_HITS = 5  # distinct values within tolerance across the named files
# Values known to be superseded (pre-dairy-module improved figures, old nutrition bounds).
# A value given as (number, regex) is stale only when the line matches the regex.
DEFAULT_STALE = [120.9, 84.2, 265, 98.2, 119.3, 103.0, 1.37, 95.4, 20.9, (45.7, r"^(?!.*(?:Mha|Henry|in-use))"), 34.0, 49.7, 54.7, 40.8, 29.2, 25.4, (21.0, r"worst year|100"), 7.4, 7.11,
                 7.57, 7.84, 6.93, 6.34, 3.86, 1.38, 268, 458, 69.0, 195, 387, 108.2, 192.7,
                 384.2, 43.2, 45.6, 48.5, 52.7, 82.3, 67.7, 14.6, 36.8, 12.6]
DEFAULT_OUT = "qa/reports/numbers_lint_2026-11-07.csv"

MONTHS = (r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|"
          r"Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)")
YEAR = r"(?:18[6-9]\d|19\d\d|20[0-2]\d|2030)"

# Masking rules, applied in this order. Each is (name, compiled regex).
MASKS = [
    ("code", re.compile(r"`[^`]*`")),
    ("url", re.compile(r"https?://[^\s)>\]]+")),
    ("doi", re.compile(r"\b10\.\d{4,9}/[^\s)>\]]+")),
    ("path", re.compile(r"[\w./~-]*[\w-]+\.(?:csv|py|md|json|xlsx|xls|pdf|txt|tif|tiff|zip|gz|sh|html|R|docx)\b")),
    ("path", re.compile(r"(?<![\w])[\w.-]+/[\w./-]*\d[\w./-]*")),
    ("hash", re.compile(r"\b(?=[0-9a-f]*\d)(?=[0-9a-f]*[a-f])[0-9a-f]{7,64}\b")),
    ("date", re.compile(r"\b\d{4}-\d{2}-\d{2}\b")),
    ("date", re.compile(r"\b\d{1,2}\s+" + MONTHS + r"\.?,?\s+" + YEAR + r"\b")),
    ("date", re.compile(r"\b" + MONTHS + r"\.?\s+(?:\d{1,2},?\s+)?" + YEAR + r"\b")),
    ("yearrange", re.compile(r"\b" + YEAR + r"\s*(?:[-–—/]|to)\s*(?:" + YEAR + r"|\d{2})\b")),
    ("id", re.compile(r"\b" + YEAR + r"-[A-Za-z][\w-]*")),
    ("citation", re.compile(r"\b\d+\(\d+\)\s*[:,]?\s*\d+(?:\s*[-–]\s*\d+)?")),
    ("citation", re.compile(r"\bpp?\.\s*\d+(?:\s*[-–]\s*\d+)?", re.I)),
    ("citation", re.compile(r"\b(?:vol|volume|no|issue|nr)\.?\s*\d+", re.I)),
    ("citation", re.compile(r"(?<=:)\s?\d+\s*[-–]\s*\d+\b")),
    ("tokens", re.compile(r"\b\d[\d,.]*\s*[kKmM]?\s*tokens?\b")),
    ("size", re.compile(r"\b\d[\d,.]*\s*(?:KB|MB|GB|TB|kB|KiB|MiB|GiB)\b")),
    ("power", re.compile(r"\b10\s*\^\s*-?\d+")),
    ("section", re.compile(r"\b(?:sections?|tables?|figures?|figs?\.?|chapters?|steps?|appendix|rows?|claims?)\s+\d+(?:\.\d+)*", re.I)),
    ("year", re.compile(r"(?<![\w.,])" + YEAR + r"(?![\w]|[.,]\d)")),
]
LINE_START_SECTION = re.compile(r"^(\s*(?:[*\-+>]\s+)*(?:\*\*|__)?\s*)(\d+(?:\.\d+)*[.)]?)(?=\s|\*\*)")
TEXT_NUM = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)")
NUMBER = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+)(\.\d+)?(\s?%)?(?![\d])")


ID_COLUMNS = {"zone", "parent", "year", "id", "rank", "index", "release", "preset", "row", "n"}


def is_id_column(col):
    """Identifier columns (zone numbers, years, FAO codes) are not measurements."""
    c = col.strip().lower()
    return c in ID_COLUMNS or c.endswith(" code") or c.endswith("_code") or c.endswith("_id")


def load_trusted(dirs):
    """Return (sorted values, parallel list of (file, column, raw cell)) and file count."""
    best = {}
    perfile = {}
    nfiles = 0
    ncells = 0
    for d in dirs:
        for root, _, files in os.walk(d):
            for fn in sorted(files):
                if not fn.lower().endswith(".csv"):
                    continue
                path = os.path.join(root, fn)
                nfiles += 1
                with open(path, newline="", encoding="utf-8", errors="replace") as fh:
                    rd = csv.reader(fh)
                    try:
                        header = next(rd)
                    except StopIteration:
                        continue
                    seen = set()
                    fbest = {}
                    for row in rd:
                        for j, cell in enumerate(row):
                            c = cell.strip().replace(",", "") if cell.count(",") and re.fullmatch(r"-?\d{1,3}(,\d{3})+(\.\d+)?", cell.strip()) else cell.strip()
                            if not c:
                                continue
                            col = header[j] if j < len(header) else "col%d" % j
                            if is_id_column(col):
                                continue
                            try:
                                nums = [(abs(float(c)), c)]
                            except ValueError:
                                # text cell such as "35.9 to 45.1": each number in it is a value
                                nums = [(float(m.replace(",", "")), c) for m in TEXT_NUM.findall(c)]
                            for v, c in nums:
                              if v != v or v == float("inf"):
                                continue
                              key = (v, col)
                              if key in seen:
                                continue
                              seen.add(key)
                              ncells += 1
                              variants = [(v, "")]
                              if v >= 1e3:
                                  variants.append((v / 1e3, "/1e3"))
                              if v >= 1e6:
                                  variants.append((v / 1e6, "/1e6"))
                              if v <= 1.0:
                                  variants.append((v * 100.0, "*100"))
                              for val, how in variants:
                                  if val not in best:
                                      best[val] = (path, col, c + how)
                                  if val not in fbest:
                                      fbest[val] = (path, col, c + how)
                    fv = sorted(fbest)
                    perfile[path] = (fv, [fbest[x] for x in fv])
    vals = sorted(best)
    meta = [best[v] for v in vals]
    return vals, meta, perfile, nfiles, ncells


def decimals_and_tol(intpart, frac, pct):
    """Tolerance: half a unit in the last written digit (see header for trailing zeros)."""
    if frac:
        d = len(frac) - 1
        return 0.5 * 10 ** (-d)
    digits = intpart.replace(",", "")
    stripped = digits.rstrip("0")
    if len(digits) >= 2 and stripped != digits and stripped != "":
        unit = 10 ** (len(digits) - len(stripped))
        return 0.5 * unit
    return 0.5


def lookup(vals, meta, x, tol):
    """Return the nearest trusted value within tol of x, or None."""
    i = bisect.bisect_left(vals, x - tol - 1e-12)
    best = None
    while i < len(vals) and vals[i] <= x + tol + 1e-12:
        dist = abs(vals[i] - x)
        if best is None or dist < best[0]:
            best = (dist, i)
        i += 1
    if best is None:
        return None
    n = bisect.bisect_right(vals, x + tol + 1e-12) - bisect.bisect_left(vals, x - tol - 1e-12)
    return vals[best[1]], meta[best[1]], n


CSV_NAME = re.compile(r"`([^`\s]*?\.csv)`|\b([\w.-]+\.csv)\b")
DIR_NAME = re.compile(r"(?<![\w/])(results|analysis/\w+)(?=/)")


def scope_files(lines, perfile, doc):
    """For each line, the set of trusted csv paths anchored by its section (or the doc's folder)."""
    by_base = {}
    for p in perfile:
        by_base.setdefault(os.path.basename(p), []).append(p)
    # sections: split at markdown headings
    starts = [i for i, l in enumerate(lines) if re.match(r"#{1,6}\s", l)]
    bounds = [0] + [i for i in starts if i > 0] + [len(lines)]
    def named(text, files):
        for mo in CSV_NAME.finditer(text):
            name = os.path.basename(mo.group(1) or mo.group(2))
            files.update(by_base.get(name, []))
        return files

    docfiles = named("\n".join(lines), set())
    out = [None] * len(lines)
    for a, b in zip(bounds, bounds[1:]):
        files = named("\n".join(lines[a:b]), set())
        for i in range(a, b):
            out[i] = (files, docfiles)
    return out


def mask_line(line):
    """Return (masked line, list of (rule, span text)). Masked spans are blanked with spaces."""
    skipped = []
    m = LINE_START_SECTION.match(line)
    work = line
    if m:
        s, e = m.start(2), m.end(2)
        skipped.append(("section", line[s:e]))
        work = line[:s] + " " * (e - s) + line[e:]
    for name, rx in MASKS:
        def repl(mo, name=name):
            txt = mo.group(0)
            if re.search(r"\d", txt):
                skipped.append((name, txt.strip()))
            return " " * len(txt)
        work = rx.sub(repl, work)
    return work, skipped


def scan_doc(path, vals, meta, perfile, stale_list=()):
    rows = []
    in_fence = False
    with open(path, encoding="utf-8", errors="replace") as fh:
        alllines = fh.read().split("\n")
    scopes = scope_files(alllines, perfile, path)
    if True:
        for ln, line in enumerate(alllines, 1):
            scope, docscope = scopes[ln - 1]
            ctx = re.sub(r"\s+", " ", line.strip())[:160]
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                if re.search(r"\d", line):
                    rows.append((path, ln, "(fenced code block)", ctx, "skipped", "", "skip:code"))
                continue
            work, skipped = mask_line(line)
            for rule, txt in skipped:
                rows.append((path, ln, txt[:60], ctx, "skipped", "", "skip:" + rule))
            for mo in NUMBER.finditer(work):
                intpart, frac, pct = mo.group(1), mo.group(2), mo.group(3)
                text = mo.group(0).strip()
                if not frac and "," not in intpart and len(intpart) < 2 and not pct:
                    continue  # single-digit integers are not scanned
                value = float(intpart.replace(",", "") + (frac or ""))
                is_int = not frac
                stale_sv = None
                if stale_list and value >= 1:
                    wdec = len(frac) - 1 if frac else 0
                    stol = 0.5 * 10 ** (-wdec)
                    for sv, rx, sdec in stale_list:
                        # same number of decimals (or more, as 45.70 for 45.7), within half a unit
                        if wdec >= sdec and abs(value - sv) <= stol + 1e-9 and (rx is None or re.search(rx, line, re.I)):
                            stale_sv = sv
                            break
                if value < 1 or (is_int and value < 10):
                    rows.append((path, ln, text, ctx, "ambiguous", "", ""))
                    continue
                tol = decimals_and_tol(intpart, frac, pct)
                hit = lookup(vals, meta, value, tol)
                n = hit[2] if hit else 0
                anchored = None
                how = ""
                for label, pool in (("section", scope), ("document", docscope)):
                    npool = 0
                    for f in sorted(pool):
                        fv, fm = perfile[f]
                        h = lookup(fv, fm, value, tol)
                        if h:
                            npool += h[2]
                            if anchored is None or abs(h[0] - value) < abs(anchored[0] - value):
                                anchored = h
                    if anchored is not None and npool > MAX_POOL_HITS:
                        anchored = None
                    if anchored is not None:
                        how = label
                        break
                if anchored is None and hit is not None and n <= 3:
                    anchored = hit
                    how = "specific"
                if stale_sv is not None and how not in ("section", "document"):
                    rows.append((path, ln, text, ctx, "stale", "", "superseded value %s" % stale_sv))
                elif anchored is not None:
                    tv, (f, col, cell), _ = anchored
                    rows.append((path, ln, text, ctx, "found", "%s [%s]" % (f, col),
                                 "%s (cell %s; anchor %s; %d distinct trusted values within tolerance)" % (round(tv, 6), cell, how, n)))
                elif hit is not None:
                    tv, (f, col, cell), _ = hit
                    rows.append((path, ln, text, ctx, "not found", "weak:%s [%s]" % (f, col),
                                 "weak:%s (cell %s; %d distinct trusted values within tolerance)" % (round(tv, 6), cell, n)))
                else:
                    rows.append((path, ln, text, ctx, "not found", "", ""))
    return rows


def main():
    ap = argparse.ArgumentParser(description="Find typed numbers absent from current output csvs.")
    ap.add_argument("--docs", nargs="+", default=DEFAULT_DOCS)
    ap.add_argument("--trusted", nargs="+", default=DEFAULT_TRUSTED)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--stale", nargs="*", default=None,
                    help="superseded values; replaces the default list (empty list turns the check off)")
    a = ap.parse_args()
    def ndec(x):
        t = str(x)
        return len(t.split(".")[1]) if "." in t else 0
    if a.stale is None:
        stale_list = []
        for x in DEFAULT_STALE:
            v, rx = x if isinstance(x, tuple) else (x, None)
            stale_list.append((float(v), rx, ndec(v)))
    else:
        stale_list = [(float(x), None, ndec(x)) for x in a.stale]

    vals, meta, perfile, nfiles, ncells = load_trusted(a.trusted)
    print("trusted: %d csv files, %d distinct numeric cells, %d lookup values" % (nfiles, ncells, len(vals)))
    allrows = []
    summary = []
    for d in a.docs:
        if not os.path.isfile(d):
            print("MISSING document: %s" % d, file=sys.stderr)
            summary.append((d, None))
            continue
        rows = scan_doc(d, vals, meta, perfile, stale_list)
        allrows.extend(rows)
        c = {"stale": 0, "found": 0, "not found": 0, "ambiguous": 0, "skipped": 0}
        for r in rows:
            c[r[4]] += 1
        summary.append((d, c))
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    with open(a.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["document", "line", "number", "context", "status", "matched_file", "matched_value"])
        w.writerows(allrows)
    print("%-48s %6s %7s %9s %10s %8s" % ("document", "stale", "found", "not found", "ambiguous", "skipped"))
    for d, c in summary:
        if c is None:
            print("%-48s %s" % (d, "MISSING"))
        else:
            print("%-48s %6d %7d %9d %10d %8d" % (d, c["stale"], c["found"], c["not found"], c["ambiguous"], c["skipped"]))
    print("report: %s (%d rows)" % (a.out, len(allrows)))


if __name__ == "__main__":
    main()
