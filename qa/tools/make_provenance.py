#!/usr/bin/env python3
"""Provenance map for both papers (decision 78).

Run from anywhere:  python3 qa/tools/make_provenance.py
Reads (never writes):
  papers/A_results/SECTION_SCOPE.md, papers/B_methods/SECTION_SCOPE.md
  qa/claims_register.csv, qa/sources_register.csv, qa/literature_register.csv
Writes:
  qa/provenance_A.md, qa/provenance_B.md

Output is deterministic: no clock, no randomness, fixed sort orders.

How the scopes are read
  * A section starts at a line "## Section N. Title" and ends at the next "## ".
  * The content list (point texts) is the numbered list between the
    "2. Content list" heading and the "3." heading.
  * The evidence table is the first table whose header starts "| Point".
    Each row is  point | claim ids or csv cell | tier note.  The middle cell is
    scanned for claim ids (A123, B123, ranges such as "A354 to A362"),
    literature ids (L123, ranges such as "L148 to L151"), source ids (D43, A04),
    and backticked file names (anything with a known extension, a trailing
    slash, or a bare root file such as LICENSE).
  * The sources table is the first table whose header starts "| Register id".
  * A point whose row yields no id, no file and no "none needed" statement,
    or whose row is malformed, or which has no row at all, is listed under
    "Unparsed".
"""
import csv
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))          # repository root
PARENT = os.path.dirname(ROOT)                          # holds the models repository

SCOPES = {
    "A": ("Paper A (results)", "papers/A_results/SECTION_SCOPE.md"),
    "B": ("Paper B (methods)", "papers/B_methods/SECTION_SCOPE.md"),
}

FILE_EXT = re.compile(r"\.(csv|md|py|mjs|js|ts|json|cff|txt|pdf|yml|yaml|sh)$", re.I)
ROOT_BARE = {"LICENSE"}


# ----------------------------------------------------------------- helpers
def clean(s):
    s = (s or "").replace("—", "-").replace("–", "-")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def cell(s):
    return clean(s).replace("|", "/")


def short(s, n):
    s = clean(s)
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0]
    return cut.rstrip(" ,;:") + "..."


def read_csv(rel):
    with open(os.path.join(ROOT, rel), newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


_basenames = None


def basename_index():
    global _basenames
    if _basenames is None:
        _basenames = {}
        for dp, dn, fn in os.walk(ROOT):
            dn[:] = sorted(d for d in dn if d not in (".git", "node_modules", "__pycache__"))
            for f in sorted(fn):
                _basenames.setdefault(f, []).append(os.path.relpath(os.path.join(dp, f), ROOT))
    return _basenames


def path_exists(p):
    """Return (ok, resolved) for a path named in a scope or register."""
    p = p.strip().strip("`").strip()
    if not p:
        return False, ""
    if "*" in p or "?" in p:
        hits = sorted(glob.glob(os.path.join(ROOT, p)))
        return (bool(hits), os.path.relpath(hits[0], ROOT) if hits else "")
    if os.path.exists(os.path.join(ROOT, p)):
        return True, p
    if os.path.exists(os.path.join(PARENT, p)):
        return True, "../" + p
    if "/" not in p.rstrip("/"):
        hits = basename_index().get(p.rstrip("/"), [])
        if hits:
            return True, hits[0]
    return False, ""


def split_paths(field):
    """Path-like tokens in a register field (semicolon separated, may carry notes)."""
    out = []
    for part in re.split(r";", field or ""):
        part = part.strip()
        if not part:
            continue
        tok = part.split(" ")[0] if (" " in part and FILE_EXT.search(part.split(" ")[0])) else part
        if FILE_EXT.search(tok) or tok.endswith("/") or "/" in tok:
            out.append(tok)
    return out


def expand_ids(text, prefixes, width):
    """All ids with the given prefixes and digit width, ranges expanded, in order."""
    found = []
    pat_range = re.compile(r"\b([%s])(\d{%d})\s+to\s+\1(\d{%d})\b" % (prefixes, width, width))
    pat_one = re.compile(r"\b([%s])(\d{%d})\b" % (prefixes, width))
    tokens = []
    for m in pat_range.finditer(text):
        tokens.append((m.start(), [m.group(1) + str(i).zfill(width)
                                   for i in range(int(m.group(2)), int(m.group(3)) + 1)], m.end()))
    spans = [(t[0], t[2]) for t in tokens]
    for m in pat_one.finditer(text):
        if any(a <= m.start() < b for a, b in spans):
            continue
        tokens.append((m.start(), [m.group(0)], m.end()))
    for _, ids, _ in sorted(tokens, key=lambda t: t[0]):
        for i in ids:
            if i not in found:
                found.append(i)
    return found


# ----------------------------------------------------------------- registers
class Registers:
    def __init__(self):
        self.claims = {r["id"]: r for r in read_csv("qa/claims_register.csv")}
        self.sources = {r["id"]: r for r in read_csv("qa/sources_register.csv")}
        self.lit = {r["id"]: r for r in read_csv("qa/literature_register.csv")}

    # one-word statuses
    @staticmethod
    def claim_word(c):
        st = (c.get("status") or "").lower()
        tier = c.get("tier", "")
        if st.startswith("independently verified"):
            return "two-route" if tier == "A" else "one-route"
        if st.startswith("self-checked"):
            return "one-route"
        return "none"

    @staticmethod
    def source_word(s):
        return "unverified" if (s.get("status") or "").lower().startswith("unverified") else "verified"

    @staticmethod
    def lit_word(l):
        r = (l.get("read_or_reported") or "").lower()
        if "page level" in r or "page-level" in r:
            return "page-level"
        if r.startswith("read"):
            return "read"
        return "weak"

    def lit_file(self, lid):
        """('ok'|'none'|'missing', detail) for a literature row's file."""
        lp = (self.lit[lid].get("local_path") or "").strip()
        if not lp:
            return "none", "no local_path recorded"
        if lp.lower().startswith("not stored"):
            return "none", "register says the file is not stored"
        missing = []
        for part in lp.split(";"):
            part = part.strip()
            if part and not path_exists(part)[0]:
                missing.append(part)
        if missing:
            return "missing", "; ".join(m for m in missing)
        return "ok", ""


# ----------------------------------------------------------------- scope parsing
def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_scope(text):
    lines = text.split("\n")
    sections = []
    cur = None
    for i, l in enumerate(lines):
        m = re.match(r"^## Section (\d+)\.\s*(.*)$", l)
        if m:
            cur = {"num": int(m.group(1)), "title": clean(m.group(2)), "lines": []}
            sections.append(cur)
            continue
        if l.startswith("## "):
            cur = None
            continue
        if cur is not None:
            cur["lines"].append(l)
    for s in sections:
        parse_section(s)
    return sections


def parse_section(s):
    L = s["lines"]
    # content list
    items = {}
    start = None
    for i, l in enumerate(L):
        if re.match(r"^(###\s*2\.|\*\*2\.)\s*Content list", l):
            start = i + 1
            break
    if start is not None:
        for l in L[start:]:
            if re.match(r"^(###\s*3\.|\*\*3\.)", l):
                break
            m = re.match(r"^(\d+)\.\s+(.*)$", l)
            if m:
                items[int(m.group(1))] = clean(re.sub(r"\*\*", "", m.group(2)))
    s["content"] = items
    # tables
    s["evidence"] = []   # (raw point cell, [cells], raw line)
    s["sources_rows"] = []
    s["evidence_found"] = False
    mode = None
    for l in L:
        if l.startswith("|"):
            cells = split_row(l)
            first = cells[0].lower() if cells else ""
            if first == "point":
                mode = "evidence" if not s["evidence_found"] else None
                if mode:
                    s["evidence_found"] = True
                continue
            if first == "register id":
                mode = "sources" if not s["sources_rows"] else None
                continue
            if re.match(r"^:?-{3,}", cells[0] if cells else ""):
                continue
            if mode == "evidence":
                s["evidence"].append(cells)
            elif mode == "sources":
                s["sources_rows"].append(cells)
        else:
            mode = None


PATH_TICK = re.compile(r"`([^`]+)`")


def evidence_items(cell_text):
    """Extract ids and file tokens from an evidence cell."""
    claims = expand_ids(cell_text, "AB", 3)
    lits = expand_ids(cell_text, "L", 3)
    srcs = expand_ids(cell_text, "AD", 2)
    paths = []
    for t in PATH_TICK.findall(cell_text):
        t = t.strip()
        if FILE_EXT.search(t) or t.endswith("/") or t in ROOT_BARE:
            if t not in paths:
                paths.append(t)
    none_needed = bool(re.search(r"\bnone needed\b", cell_text, re.I))
    return claims, lits, srcs, paths, none_needed


# ----------------------------------------------------------------- building a paper map
def build_paper(key, regs):
    label, rel = SCOPES[key]
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        sections = parse_scope(fh.read())

    out = []
    w = out.append
    broken = {"claim_missing": [], "source_missing": [], "path_missing": [],
              "lit_missing_row": [], "lit_nofile": []}
    paper_t = new_tally()
    all_lit_nofile = {}
    unparsed_all = []
    pending_all = []

    w("# Provenance map: %s" % label)
    w("")
    w("Generated by `qa/tools/make_provenance.py` from `%s`, `qa/claims_register.csv`, "
      "`qa/sources_register.csv` and `qa/literature_register.csv`. Do not edit by hand; rerun the script." % rel)
    w("")
    w("**How to read a row.** Each point of a section has a row per fact. A fact is a claim the scope cites "
      "(statement shortened), or a file or register cell the scope names. The chain runs: claim id, tier and "
      "status; output file and locator; script; data source ids with kind and status; the source's own origin; "
      "literature ids with read status.")
    w("")
    w("One-word statuses. Claim: **two-route** (register status independently verified, tier A), **one-route** "
      "(self-checked, or independently verified at tier B or C where one route is the requirement), **none** "
      "(unverified or withdrawn). Source: **verified** or **unverified** (register status). Literature: "
      "**page-level** (read to page level), **read** (read, including targeted reads), **weak** (reported "
      "second-hand, record only, or not reached). Files: **ok** or **MISSING**.")
    w("")
    w("Contents: " + "; ".join("[Section %d](#section-%d)" % (s["num"], s["num"]) for s in sections)
      + "; [Tallies](#tallies); [Broken links](#broken-links); [Unparsed](#unparsed).")
    w("")

    sec_tallies = []
    for s in sections:
        t = new_tally()
        t["section"] = s["num"]
        sec_lines, sec_unparsed, sec_pending = build_section(s, regs, broken, t, all_lit_nofile)
        out.extend(sec_lines)
        unparsed_all.extend(sec_unparsed)
        pending_all.extend(sec_pending)
        sec_tallies.append((s, t))
        merge_tally(paper_t, t)
    paper_t["broken"] = len(set((k, i[0]) for k, v in broken.items() for i in v))

    # tallies
    w("## Tallies")
    w("")
    w("Counts of rows, not of distinct claims, unless the column says distinct.")
    w("")
    w("| Section | Points | Points parsed | Points unparsed | Fact rows | Claim rows: two-route | one-route | none | "
      "Distinct claims | Tier A / B / C (distinct) | Distinct sources: verified / unverified | "
      "Distinct literature: page-level / read / weak | Broken links |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for s, t in sec_tallies:
        w(tally_row("%d. %s" % (s["num"], short(s["title"], 40)), t))
    w(tally_row("**Paper total**", paper_t, total=True))
    w("")

    # broken links
    w("## Broken links")
    w("")
    nb = 0
    w("**Claim ids the scope cites that the claims register lacks.**")
    w("")
    nb += render_broken(w, broken["claim_missing"])
    w("")
    w("**Source ids a cited claim names, or the scope names, that no register holds.**")
    w("")
    nb += render_broken(w, broken["source_missing"])
    w("")
    w("**File paths (scope, or a cited claim's output file or script) that do not exist.**")
    w("")
    nb += render_broken(w, broken["path_missing"])
    w("")
    w("**Literature ids cited that the literature register lacks.**")
    w("")
    nb += render_broken(w, broken["lit_missing_row"])
    w("")
    w("**Literature ids cited whose register row has no file** (no `local_path`, a stored-nowhere note, "
      "or a path that does not resolve in this repository or the sibling models repository).")
    w("")
    nf = 0
    if all_lit_nofile:
        w("| Literature id | Author and year (scope or register) | File state | Detail |")
        w("|---|---|---|---|")
        for lid in sorted(all_lit_nofile):
            st, det, ttl = all_lit_nofile[lid]
            w("| %s | %s | %s | %s |" % (lid, cell(short(ttl, 70)), st, cell(det)))
            nf += 1
    else:
        w("None.")
    w("")
    w("Broken-link counts for this paper: claim ids %d; source ids %d; file paths %d; literature ids absent "
      "from the register %d; literature ids with no file %d."
      % (len(set(b[0] for b in broken["claim_missing"])), len(set(b[0] for b in broken["source_missing"])),
         len(set(b[0] for b in broken["path_missing"])), len(set(b[0] for b in broken["lit_missing_row"])), nf))
    w("")

    # unparsed
    w("## Unparsed")
    w("")
    w("Points whose evidence cell gave no claim id, no file and no \"none needed\" statement, rows that did not "
      "have three cells, and points with no evidence row. Nothing here is counted in the tallies as a fact row.")
    w("")
    if unparsed_all:
        w("| Section | Point | Point text | Evidence cell as written | Why |")
        w("|---|---|---|---|---|")
        for u in unparsed_all:
            w("| %d | %s | %s | %s | %s |" % (u[0], u[1], cell(short(u[2], 90)), cell(short(u[3], 140)), u[4]))
    else:
        w("None.")
    w("")
    if pending_all:
        w("**Rows of a sources table that name no register id** (for example a pending acquisition). They are "
          "not links and are listed so they are not lost.")
        w("")
        w("| Section | Row as written |")
        w("|---|---|")
        for p in pending_all:
            w("| %d | %s |" % (p[0], cell(short(p[1], 160))))
        w("")
    return "\n".join(out) + "\n"


def new_tally():
    return {"section": 0, "points": 0, "parsed": 0, "unparsed": 0, "rows": 0,
            "w2": 0, "w1": 0, "w0": 0, "claims": set(), "tiers": {},
            "src": {}, "lit": {}, "broken": 0}


def merge_tally(a, b):
    for k in ("points", "parsed", "unparsed", "rows", "w2", "w1", "w0", "broken"):
        a[k] += b[k]
    a["claims"] |= b["claims"]
    a["tiers"].update(b["tiers"])
    a["src"].update(b["src"])
    a["lit"].update(b["lit"])


def tally_row(name, t, total=False):
    tiers = {"A": 0, "B": 0, "C": 0}
    for tier in t["tiers"].values():
        if tier in tiers:
            tiers[tier] += 1
    sv = sum(1 for v in t["src"].values() if v == "verified")
    su = sum(1 for v in t["src"].values() if v == "unverified")
    lw = {"page-level": 0, "read": 0, "weak": 0}
    for v in t["lit"].values():
        lw[v] += 1
    return "| %s | %d | %d | %d | %d | %d | %d | %d | %d | %d / %d / %d | %d / %d | %d / %d / %d | %d |" % (
        name, t["points"], t["parsed"], t["unparsed"], t["rows"], t["w2"], t["w1"], t["w0"],
        len(t["claims"]), tiers["A"], tiers["B"], tiers["C"], sv, su,
        lw["page-level"], lw["read"], lw["weak"], t["broken"])


def render_broken(w, items):
    if not items:
        w("None.")
        return 0
    w("| Id or path | Where cited | Detail |")
    w("|---|---|---|")
    seen = set()
    n = 0
    for ident, where, detail in sorted(items):
        key = (ident, where)
        if key in seen:
            continue
        seen.add(key)
        w("| `%s` | %s | %s |" % (cell(ident), cell(where), cell(detail)))
        n += 1
    return n


def build_section(s, regs, broken, t, all_lit_nofile):
    out = []
    w = out.append
    unparsed = []
    pending = []
    num = s["num"]
    snap = {k: len(v) for k, v in broken.items()}
    w("## Section %d" % num)
    w("")
    w("### %s" % s["title"])
    w("")

    # section sources table (literature)
    src_lit = []
    for cells in s["sources_rows"]:
        first = cells[0] if cells else ""
        ids = expand_ids(first, "L", 3)
        if ids:
            for one in ids:
                src_lit.append((one, [one, "" if len(ids) > 1 else (cells[1] if len(cells) > 1 else "")] + cells[2:]))
        else:
            pending.append((num, " | ".join(cells)))

    # evidence rows
    seen_points = set()
    for cells in s["evidence"]:
        pm = re.match(r"^(\d+)$", cells[0]) if cells else None
        if not pm or len(cells) < 2:
            unparsed.append((num, cells[0] if cells else "?", "", " | ".join(cells), "row is not point | cell | note"))
            t["points"] += 1
            t["unparsed"] += 1
            continue
        pt = int(pm.group(1))
        seen_points.add(pt)
        ptext = s["content"].get(pt, "(point text not found in the content list)")
        t["points"] += 1
        ev = cells[1]
        tier_note = cells[2] if len(cells) > 2 else ""
        claims, lits, srcs, paths, none_needed = evidence_items(ev)
        if not (claims or lits or srcs or paths or none_needed):
            unparsed.append((num, str(pt), ptext, ev, "no id, file or 'none needed' found"))
            t["unparsed"] += 1
            # still print the point, so it is not dropped from the map
            w("#### Point %d: %s" % (pt, cell(short(ptext, 110))))
            w("")
            w("Evidence cell: %s. **Unparsed** (see the Unparsed list)." % cell(short(ev, 200)))
            w("")
            continue
        t["parsed"] += 1
        w("#### Point %d: %s" % (pt, cell(short(ptext, 110))))
        w("")
        w("Evidence cell: %s" % cell(short(ev, 220)))
        w("")
        w("| Fact | Claim, tier, status | Output file and locator | Script | Data sources (kind, status) | "
          "Original source (origin) | Literature (read status) |")
        w("|---|---|---|---|---|---|---|")
        rows = 0
        for cid in claims:
            rows += 1
            t["rows"] += 1
            t["claims"].add(cid)
            c = regs.claims.get(cid)
            if c is None:
                broken["claim_missing"].append((cid, "section %d point %d" % (num, pt), "not in claims_register.csv"))
                w("| (claim id not in the register) | `%s` : MISSING | | | | | |" % cid)
                continue
            word = regs.claim_word(c)
            t["tiers"][cid] = c["tier"]
            t["w2" if word == "two-route" else "w1" if word == "one-route" else "w0"] += 1
            fact = short(c["statement"], 100)
            claim_cell = "`%s` : tier %s : **%s**" % (cid, c["tier"], word)
            # output file
            ofiles = split_paths(c["output_file"])
            ocell = []
            for p in ofiles:
                ok, _ = path_exists(p)
                ocell.append("`%s` (%s)" % (p, "ok" if ok else "**MISSING**"))
                if not ok:
                    broken["path_missing"].append((p, "claim %s (output_file), section %d point %d" % (cid, num, pt),
                                                   "named by the claims register"))
            if c["output_locator"]:
                ocell.append("at: " + short(c["output_locator"], 70))
            if not ocell:
                ocell = ["(none recorded)"]
            scell = []
            for p in split_paths(c["script"]):
                ok, _ = path_exists(p)
                scell.append("`%s` (%s)" % (p, "ok" if ok else "**MISSING**"))
                if not ok:
                    broken["path_missing"].append((p, "claim %s (script), section %d point %d" % (cid, num, pt),
                                                   "named by the claims register"))
            if not scell:
                scell = ["(none recorded)"]
            # data sources and literature named by the claim
            ids = [x.strip() for x in re.split(r"[;,]", c["sources"]) if x.strip()]
            msrc = [x.strip() for x in re.split(r"[;,]", c["method_source"]) if x.strip()]
            dcell, origcell, lcell = [], [], []
            for sid in ids:
                if re.match(r"^[AD]\d{2}$", sid):
                    r = regs.sources.get(sid)
                    if r is None:
                        broken["source_missing"].append((sid, "claim %s, section %d point %d" % (cid, num, pt),
                                                         "not in sources_register.csv"))
                        dcell.append("`%s` (**MISSING**)" % sid)
                    else:
                        sw = regs.source_word(r)
                        t["src"][sid] = sw
                        dcell.append("`%s` (%s, %s)" % (sid, short(r["kind"], 30), sw))
                        origcell.append("%s: %s" % (sid, short(r["origin"], 70)))
                elif re.match(r"^L\d{3}$", sid):
                    lcell.append(lit_cell(sid, regs, broken, t, num, pt, all_lit_nofile, "source of claim %s" % cid))
                else:
                    broken["source_missing"].append((sid, "claim %s, section %d point %d" % (cid, num, pt),
                                                     "id not in a known pattern"))
                    dcell.append("`%s` (**unrecognised**)" % sid)
            for sid in msrc:
                if re.match(r"^L\d{3}$", sid) and sid not in ids:
                    lcell.append("method: " + lit_cell(sid, regs, broken, t, num, pt, all_lit_nofile,
                                                        "method source of claim %s" % cid))
            w("| %s | %s | %s | %s | %s | %s | %s |" % (
                cell(fact), claim_cell, cell("<br>".join(ocell)), cell("<br>".join(scell)).replace("&lt;", "<"),
                cell("<br>".join(dcell) or "(none)"), cell("<br>".join(origcell) or "(none)"),
                cell("<br>".join(lcell) or "(none)")))
        # ids the scope names directly
        extra_s = [x for x in srcs if x in regs.sources or x not in regs.lit]
        for sid in srcs:
            r = regs.sources.get(sid)
            rows += 1
            t["rows"] += 1
            if r is None:
                broken["source_missing"].append((sid, "scope section %d point %d" % (num, pt), "not in sources_register.csv"))
                w("| (source named by the scope) | `%s` : MISSING | | | | | |" % sid)
            else:
                sw = regs.source_word(r)
                t["src"][sid] = sw
                w("| Source named by the scope | n/a | n/a | n/a | %s | %s | (none) |" % (
                    cell("`%s` (%s, %s)" % (sid, short(r["kind"], 30), sw)), cell("%s: %s" % (sid, short(r["origin"], 70)))))
        for p in paths:
            rows += 1
            t["rows"] += 1
            ok, res = path_exists(p)
            if not ok:
                broken["path_missing"].append((p, "scope section %d point %d" % (num, pt), "named by the scope"))
            w("| File named by the scope | n/a | %s | n/a | (none) | (none) | (none) |" % cell(
                "`%s` (%s)" % (p, "ok" if ok else "**MISSING**") + (" found as `%s`" % res if ok and res and res != p else "")))
        if lits:
            rows += 1
            t["rows"] += 1
            lc = [lit_cell(l, regs, broken, t, num, pt, all_lit_nofile, "scope") for l in lits]
            w("| Literature named by the scope for this point | n/a | n/a | n/a | (none) | (none) | %s |" % cell("<br>".join(lc)))
        if rows == 0:
            w("| %s | none needed | n/a | n/a | n/a | n/a | n/a |" % cell(short(ptext, 100)))
            t["rows"] += 1
        w("")
        if tier_note:
            w("Scope's own note: %s" % cell(short(tier_note, 220)))
            w("")

    # points in the content list with no evidence row
    for pt in sorted(s["content"]):
        if pt not in seen_points:
            unparsed.append((num, str(pt), s["content"][pt], "(no evidence row)", "point has no row in the evidence table"))
            t["points"] += 1
            t["unparsed"] += 1
            w("#### Point %d: %s" % (pt, cell(short(s["content"][pt], 110))))
            w("")
            w("No evidence row in the scope. **Unparsed** (see the Unparsed list).")
            w("")

    # section sources table
    if src_lit:
        w("#### Sources the scope lists for this section")
        w("")
        w("| Literature id | Author and year (scope) | Register read status | Word | File | Register status |")
        w("|---|---|---|---|---|---|")
        for lid, cells in src_lit:
            ttl = cells[1] if len(cells) > 1 else ""
            l = regs.lit.get(lid)
            if l is None:
                broken["lit_missing_row"].append((lid, "scope section %d sources table" % num, "not in literature_register.csv"))
                w("| `%s` | %s | (not in register) | **MISSING** | | |" % (lid, cell(short(ttl, 50))))
                continue
            lw = regs.lit_word(l)
            t["lit"][lid] = lw
            st, det = regs.lit_file(lid)
            if st != "ok":
                all_lit_nofile[lid] = (st, det, ttl or short(l["title"], 70))
                broken["lit_nofile"].append((lid, "section %d" % num, st))
            w("| `%s` | %s | %s | **%s** | %s | %s |" % (
                lid, cell(short(ttl or l["title"], 50)), cell(short(l["read_or_reported"], 50)), lw,
                "ok" if st == "ok" else "**%s**" % st, cell(short(l["status"], 40))))
        w("")
    new = set()
    for k, v in broken.items():
        for item in v[snap[k]:]:
            new.add((k, item[0]))
    t["broken"] = len(new)
    return out, unparsed, pending


def lit_cell(lid, regs, broken, t, num, pt, all_lit_nofile, why):
    l = regs.lit.get(lid)
    if l is None:
        broken["lit_missing_row"].append((lid, "section %d point %d (%s)" % (num, pt, why), "not in literature_register.csv"))
        return "`%s` (**MISSING**)" % lid
    lw = regs.lit_word(l)
    t["lit"][lid] = lw
    st, det = regs.lit_file(lid)
    if st != "ok":
        all_lit_nofile[lid] = (st, det, short(l["title"], 70))
        broken["lit_nofile"].append((lid, "section %d point %d" % (num, pt), st))
    return "`%s` (%s%s)" % (lid, lw, "" if st == "ok" else ", file: no" if st == "none" else ", file: " + st)


def main():
    regs = Registers()
    for key in ("A", "B"):
        text = build_paper(key, regs)
        dest = os.path.join(ROOT, "qa", "provenance_%s.md" % key)
        with open(dest, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote", os.path.relpath(dest, ROOT))


if __name__ == "__main__":
    sys.exit(main())
