#!/usr/bin/env python3
"""Build the reference list for Paper A or Paper B from qa/literature_register.csv.

Usage:  python3 qa/tools/make_references.py A|B

Reads   papers/*/draft/*_claims.csv (column register_id), the paper's section files,
        qa/literature_register.csv.   Never edits them.
Writes  papers/<A_results|B_methods>/draft/references.md  (Elsevier Harvard form).
Prints  counts, CHECK entries, ids with no register row, rows seen only second-hand,
        prose citations with no register id, journal names with no known abbreviation.
Deterministic: no dates, no randomness; two runs give identical output.
"""
import csv, glob, os, re, sys, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTER = os.path.join(ROOT, "qa", "literature_register.csv")
PAPER_DIR = {"A": "A_results", "B": "B_methods"}
SECTION_GLOB = {"A": "A_s*.md", "B": "B_s*.md"}  # plus supplementary.md; draft1 files are older merges, skipped
ID_RE = re.compile(r"^L\d+$")

# ISO 4 / LTWA style abbreviations that are known with confidence. Anything else keeps its full name
# and is listed for a later pass.
ABBR = {
    "Ecological Modelling": "Ecol. Model.",
    "Ecological Economics": "Ecol. Econ.",
    "Ecological Indicators": "Ecol. Indic.",
    "Environmental Research Letters": "Environ. Res. Lett.",
    "Global Environmental Change": "Glob. Environ. Change",
    "Global Food Security": "Glob. Food Secur.",
    "Global Change Biology": "Glob. Change Biol.",
    "Nature Communications": "Nat. Commun.",
    "Nature Climate Change": "Nat. Clim. Change",
    "Nature Sustainability": "Nat. Sustain.",
    "Nature Food": "Nat. Food",
    "Nature Geoscience": "Nat. Geosci.",
    "Nature": "Nature",
    "Science": "Science",
    "Science Advances": "Sci. Adv.",
    "PNAS": "Proc. Natl. Acad. Sci. U.S.A.",
    "The Lancet": "Lancet",
    "Food Security": "Food Secur.",
    "Food Policy": "Food Policy",
    "Land Use Policy": "Land Use Policy",
    "Land": "Land",
    "Water": "Water",
    "Nutrients": "Nutrients",
    "Resources": "Resources",
    "Sustainability": "Sustainability",
    "Heliyon": "Heliyon",
    "Population and Environment": "Popul. Environ.",
    "Agricultural Systems": "Agric. Syst.",
    "Climatic Change": "Clim. Change",
    "Energy Policy": "Energy Policy",
    "Human Ecology": "Hum. Ecol.",
    "BioScience": "BioScience",
    "Technometrics": "Technometrics",
    "Science of the Total Environment": "Sci. Total Environ.",
    "Journal of Cleaner Production": "J. Clean. Prod.",
    "Journal of Rural Studies": "J. Rural Stud.",
    "Journal of Industrial Ecology": "J. Ind. Ecol.",
    "Journal of Business Research": "J. Bus. Res.",
    "Environment and Urbanization": "Environ. Urban.",
    "Animal Production Science": "Anim. Prod. Sci.",
    "Plos Biology": "PLoS Biol.",
    "PLoS Biology": "PLoS Biol.",
    "Weather and Climate Extremes": "Weather Clim. Extrem.",
    "Climate Risk Management": "Clim. Risk Manag.",
    "Reviews of Geophysics": "Rev. Geophys.",
    "Trends in Food Science & Technology": "Trends Food Sci. Technol.",
    "Computers and Electronics in Agriculture": "Comput. Electron. Agric.",
    "Science Advances ": "Sci. Adv.",
    "Environmental Science & Technology": "Environ. Sci. Technol.",
    "International Journal of Life Cycle Assessment": "Int. J. Life Cycle Assess.",
    "Annual Review of Environment and Resources": "Annu. Rev. Environ. Resour.",
    "Frontiers in Ecology and the Environment": "Front. Ecol. Environ.",
    "Renewable Agriculture and Food Systems": "Renew. Agric. Food Syst.",
    "Advances in Nutrition": "Adv. Nutr.",
    "Sustainability Science": "Sustain. Sci.",
    "Methane": "Methane",
    "World": "World",
    "Environmental Impact Assessment Review": "Environ. Impact Assess. Rev.",
    "Frontiers in Nutrition": "Front. Nutr.",
    "Journal of Resources and Ecology": "J. Resour. Ecol.",
    "Scientific Reports": "Sci. Rep.",
    "Sustainable Production and Consumption": "Sustain. Prod. Consum.",
    "Trends in Ecology & Evolution": "Trends Ecol. Evol.",
    "Environmental Science & Policy": "Environ. Sci. Policy",
    "Landscape and Urban Planning": "Landsc. Urban Plan.",
    "Veterinary and Animal Science": "Vet. Anim. Sci.",
    "Australian Geographer": "Aust. Geogr.",
    "Australian Planner": "Aust. Plan.",
    "The Rangeland Journal": "Rangel. J.",
    "Elementa": "Elementa",
    "Environmental and Urbanization": "Environ. Urban.",
    "Sustainability Science ": "Sustain. Sci.",
    "Reliability Engineering and System Safety": "Reliab. Eng. Syst. Saf.",
    "European Journal of Clinical Investigation": "Eur. J. Clin. Invest.",
    "Health Information and Libraries Journal": "Health Inf. Libr. J.",
    "Journal of Graduate Medical Education": "J. Grad. Med. Educ.",
    "Nature Ecology & Evolution": "Nat. Ecol. Evol.",
    "Global Ecology and Conservation": "Glob. Ecol. Conserv.",
    "Nature Food ": "Nat. Food",
    "Review of Marketing and Agricultural Economics": "Rev. Mark. Agric. Econ.",
    "Population and Development Review": "Popul. Dev. Rev.",
    "International Journal of Agricultural Sustainability": "Int. J. Agric. Sustain.",
    "Journal of the Royal Society Interface": "J. R. Soc. Interface",
    "Journal of Population and Sustainability": "J. Popul. Sustain.",
    "The Journal of Population and Sustainability": "J. Popul. Sustain.",
    "Australian Journal of Agricultural and Resource Economics": "Aust. J. Agric. Resour. Econ.",
    "Australian Population Studies": "Aust. Popul. Stud.",
    "Australian Journal of Environmental Management": "Aust. J. Environ. Manag.",
    "International Journal of Urban and Regional Research": "Int. J. Urban Reg. Res.",
}
CORP_WORDS = {"CSIRO", "Treasury", "Department", "Committee", "Commission", "Council", "ABARES", "ABARE",
              "ABS", "FAO", "Centre", "House", "Productivity", "PMSEIC", "Geoscience", "Bureau", "Network",
              "Academy", "Federation", "Foundation", "AUSNUT", "USDA", "IIASA", "UNFPA", "ICAC", "Institute", "Agency", "Australia", "University"}
ARTICLE_NO_JOURNALS = {"Nature Communications", "Environmental Research Letters", "Heliyon", "Elementa",
                       "PLoS Biology", "Science Advances", "Global Ecology and Conservation", "Sustainability",
                       "Land", "Nutrients", "Resources", "Water", "Methane", "Weather and Climate Extremes",
                       "Climate Risk Management", "Journal of the Royal Society Interface", "Global Food Security"}
PLACES = ["Canberra", "Sydney", "Melbourne", "Brisbane", "London", "New York", "Washington", "Rome", "Vancouver"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
STOP = set(MONTHS) | {"The", "In", "On", "Its", "Since", "By", "For", "From", "And", "Of", "At", "To", "A", "An",
                      "Population", "Queensland", "Tasmania", "Australia", "Victoria", "Table", "Figure",
                      "Section", "Version", "Release", "Releases", "Capacity", "Census", "Between", "Until", "After", "Before",
                      "Around", "About", "During", "Under", "Over", "Year", "Years", "Rev", "ABS", "ANZSIC",
                      "NRM", "SA", "SA2", "SA4", "NRM", "Item", "Decision", "Decisions", "Wales", "Zealand", "Strategies", "Baseline",
                      "Strategy", "World", "States", "Argentina", "India", "Brazil", "China", "Africa"}


def fold(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def read_register():
    with open(REGISTER, newline="", encoding="utf-8") as fh:
        return {r["id"]: r for r in csv.DictReader(fh)}


def claim_ids(paper):
    ids = {}
    pat = os.path.join(ROOT, "papers", PAPER_DIR[paper], "draft", "*_claims.csv")
    for f in sorted(glob.glob(pat)):
        with open(f, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                for tok in re.split(r"[;,]", row.get("register_id", "") or ""):
                    tok = tok.strip()
                    if ID_RE.match(tok):
                        ids.setdefault(tok, set()).add(os.path.basename(f))
    return ids


def clean_dash(s):
    return re.sub(r"(?<=\w)\s*-\s*(?=\w)", "\u2013", s) if re.fullmatch(r"\s*\w+\s*-\s*\w+\s*", s) else s


def iso_to_text(iso):
    m = re.match(r"(\d{4})-(\d\d)-(\d\d)$", iso)
    if not m:
        return iso
    return "%d %s %s" % (int(m.group(3)), MONTHS[int(m.group(2)) - 1], m.group(1))


def is_corporate(auth):
    return any(w in CORP_WORDS for w in re.findall(r"[A-Za-z]+", auth))


def split_authors(a):
    """Return (list of names, has_etal, others_note)."""
    a = a.strip(" ,;.")
    etal = False
    m = re.search(r"\band (\d+) others$", a)
    if m:
        etal = True
        a = a[: m.start()].strip(" ,")
    if re.search(r"\bet al\.?$", a):
        etal = True
        a = re.sub(r"\s*\bet al\.?$", "", a).strip(" ,")
    parts = [p.strip() for p in re.split(r",\s*|\s+and\s+|\s*&\s*", a) if p.strip()]
    return parts, etal


def initials_form(name):
    """'L.A. Henry' -> ('Henry', 'L.A.'); 'Henry' -> ('Henry', '')."""
    m = re.match(r"^((?:[A-Z]\.\s?)+)\s*(.+)$", name)
    if m:
        return m.group(2).strip(), m.group(1).replace(" ", "")
    return name, ""


def parse_entry(rid, row):
    title = row["title"].strip()
    kind = row["kind"]
    origin = row["origin"]
    missing = []
    notes = []
    work = title

    # DOI
    doi = None
    m = re.search(r"(?:doi:|https?://(?:dx\.)?doi\.org/)\s*(10\.[^\s,;]+?)[.,;]?(?=\s|$)", work)
    if m:
        doi = m.group(1)
        work = (work[: m.start()] + work[m.end():]).strip()
    else:
        m = re.search(r"https?://(?:dx\.)?doi\.org/(10\.[^\s,;]+)", origin)
        if m:
            doi = m.group(1).rstrip(".")

    # explicit author list with initials, e.g. "(authors L.A. Henry and D.P. Godden)"
    explicit = None
    m = re.search(r"\(authors ([^)]+)\)", work)
    if m:
        explicit = m.group(1)
        work = (work[: m.start()] + work[m.end():]).strip()

    work = re.sub(r"\s*\[[^\]]*\]", "", work)
    work = re.sub(r"\s*\([^()]*(?:A_OUT|B_OUT|PUBLICATIONS|PAPERS\.md|Comparators|models archive|archive)[^()]*\)", "", work)
    work = re.sub(r"\s*\((?:A_OUT|B_OUT|PUBLICATIONS|PAPERS\.md)\b.*$", "", work).strip()
    uw = re.match(r"^(.*?\b(?:19|20)\d\d)\s*\((.*)\)\s*$", work)
    if uw and re.search(r"[\"\u201c]", uw.group(2)):
        work = uw.group(1) + ", " + uw.group(2)
    work = re.sub(r"[;,]?\s*English original.*$", "", work)
    if "to confirm" in work:
        missing.append("title is marked 'to confirm' in the register")
        work = re.sub(r"\([^)]*to confirm[^)]*\)", "", work)

    # quoted title
    qt = None
    fq = re.search(r"[\"\u201c]", work)
    if fq:
        if fq.group(0) == '"':
            qt = re.compile(r'"([^"]+)"').search(work, fq.start())
        else:
            qt = re.compile(r"\u201c([^\u201d]+)\u201d").search(work, fq.start())
    qtitle = None
    qpos = None
    if qt:
        qtitle = qt.group(1).strip().rstrip(",")
        before, after = work[: qt.start()], work[qt.end():]
        qpos = qt.start()
    else:
        before, after = work, ""

    # authors and year
    ym = re.search(r"\(?\b((?:19|20)\d\d)(?:-\d{2,4})?\)?", before)
    year = ytxt = None
    if ym:
        auth_raw = before[: ym.start()].strip(" ,(")
        year = ym.group(1)
        rest_before = before[ym.end():]
        im = re.match(r"\s*\(issue (\d{4})\)", rest_before)
        if im:
            year = im.group(1)
            rest_before = rest_before[im.end():]
        rest_before = re.sub(r"^\s*\((?:online|submitted)[^)]*\)", "", rest_before)
    elif qtitle is not None:
        auth_raw = before.strip(" ,(")
        rest_before = ""
        if "(" in auth_raw and not re.search(r"\bsaved\b", work):
            return fallback(rid, row, "register title not in the usual form; not parsed")
    else:
        rest_before = ""
        am = re.match(r"^([^,\"(\u201c]+)", before)
        auth_raw = am.group(1).strip() if am else before.strip()
        rest_before = before[len(auth_raw):] if am else ""
    auth_raw = re.sub(r"\s*\([^)]*[A-Za-z]{3,}[^)]*\)", "", auth_raw).strip(" ,")
    if qtitle is None:
        # title not quoted: remainder after the year
        rest = rest_before
    else:
        rest = (rest_before + " " + after).strip()

    # authors
    corporate = is_corporate(auth_raw) and not explicit
    if explicit:
        names, etal = split_authors(explicit)
    elif corporate:
        names, etal = [auth_raw], False
    else:
        names, etal = split_authors(auth_raw)
    chk = re.sub(r"\band \d+ others\b", "", auth_raw)
    messy = (len(chk.split()) > 14) or re.search(r"submission|inquiry|calculation|ranking|short form|[;%]|\d", chk, re.I)
    ok = bool(names) and not messy
    fully_ok = ok
    if not ok:
        return fallback(rid, row, "register title not in the usual form; not parsed")

    forms = [initials_form(n) for n in names]
    if corporate:
        author_str = ", ".join(n for n, _ in forms)
        sort_names = [n for n, _ in forms]
    else:
        parts = []
        for n, ini in forms:
            parts.append("%s, %s" % (n, ini) if ini else n)
        author_str = ", ".join(parts)
        sort_names = [n for n, _ in forms]
        if any(not ini for _, ini in forms):
            missing.append("full author list and initials" if etal else "author initials")
        elif etal:
            missing.append("full author list")
    if etal and corporate:
        missing.append("full author list")
    if etal and not corporate:
        author_str += (", et al." if not re.search(r"\band \d+ others", auth_raw) else ", et al.")


    # strip notes and separators from the remainder
    rest = re.sub(r"\.?\s*Gale document \S+", "", rest)
    rest = re.sub(r"\s*\((?:review|Commentary|letter|comment)\)", "", rest)
    rest = rest.strip(" ,;.:")
    kl0 = kind.lower()
    if qtitle and not kl0.startswith(("journal", "conference", "magazine", "book review", "book chapter")) \
            and "thesis" not in kl0 and re.search(r"[A-Za-z]{3,}", rest_before):
        return fallback(rid, row, "register title not in the usual form; not parsed")
    note_only = (not qtitle) and bool(rest) and (rest.startswith("(") or re.search(r"\bcited\b", rest) is not None)

    entry = {"id": rid, "authors": author_str, "sort_names": sort_names, "year": year, "doi": doi,
             "title": qtitle, "kind": kind, "corporate": corporate}
    kl = kind.lower()

    def venue_parse(txt):
        txt2 = re.sub(r"\s*\([^)]*[A-Za-z]{3,}[^)]*\)", "", txt).strip(" ,;.")
        m = re.match(r"^(?P<venue>.*?)\s*(?:\((?P<vy>\d{4})\)\s*)?(?P<vol>[A-Za-z]?\d+)?\s*(?:\((?P<iss>[\w\-\u2013, ]+)\))?"
                     r"\s*(?::\s*(?P<pg>[\w]+(?:\s*[-\u2013]\s*[\w]+)?\+?))?\s*\.?$", txt2)
        return m

    def book_publisher_split(txt):
        return txt

    if kl.startswith("journal") or kl.startswith("conference") or kl.startswith("magazine") or kl.startswith("book review"):
        known = None
        if qtitle is None and rest:
            known = next((k for k in sorted(ABBR, key=len, reverse=True) if rest.lower().startswith(k.lower().strip())), None)
        if qtitle is None and not rest:
            missing += ["title", "journal", "volume", "pages"]
            entry["text"] = None
        else:
            if qtitle is None and note_only and kl.startswith("journal") and not known:
                missing.append("title and journal (register gives only a note)")
                entry["title"] = None
                entry["venue"] = None
                qtitle = ""
                rest = ""
            if qtitle is None and known and kl.startswith("journal"):
                missing.append("title (register gives only the journal)")
                entry["title"] = None
                qtitle = ""
            if qtitle is None:
                # title unquoted and venue unknown: keep the rest as is
                missing.append("title and journal not separated in the register")
                entry["title"] = rest
                entry["venue"] = None
            else:
                m = venue_parse(rest) if rest else None
                venue = vol = iss = pg = None
                if m and m.group("venue"):
                    venue = m.group("venue").strip(" ,.")
                    vol, iss, pg = m.group("vol"), m.group("iss"), m.group("pg")
                    if entry["year"] is None:
                        if m.group("vy"):
                            entry["year"] = m.group("vy")
                        elif vol and re.fullmatch(r"(19|20)\d\d", vol) and not iss:
                            entry["year"] = vol
                    if not vol and m.group("vy") and iss is None:
                        pass
                    if vol and re.fullmatch(r"(19|20)\d\d", vol) and not iss:
                        vol = None
                    if vol is None and m.group("vy") and not iss:
                        pass
                elif rest:
                    venue = rest
                entry.update(venue=venue, vol=vol, iss=iss, pg=pg)
                if not venue:
                    missing.append("journal")
                if venue and not vol and not (kl.startswith("conference")):
                    missing.append("volume")
                if venue and re.search(r"magazine", kl) and not pg:
                    missing.append("pages")
                if not pg and not kl.startswith("magazine"):
                    missing.append("pages or article number")
                elif pg:
                    pg = pg.strip()
                    if pg.endswith("+"):
                        missing.append("end page (register gives '%s')" % pg)
                    elif re.search(r"[-\u2013]", pg):
                        entry["pg"] = re.sub(r"\s*[-\u2013]\s*", "\u2013", pg)
                    else:
                        art = bool(re.search(r"[A-Za-z]|^0", pg)) or (venue in ARTICLE_NO_JOURNALS)
                        entry["article_no"] = art
                        if not art:
                            missing.append("end page (register gives only '%s')" % pg)
                if not doi and kl.startswith("journal"):
                    missing.append("DOI (none in the register; confirm whether one exists)")
        entry["form"] = "journal"
    elif kl.startswith("book chapter"):
        entry["form"] = "chapter"
        eds = book = pubr = pages = None
        m = re.match(r"^pp\.\s*(\d+)\s*[-\u2013]\s*(\d+)\s+in\s+(.+?)\s*\(eds?\),\s*(.+)$", rest)
        if m:
            pages = "%s\u2013%s" % (m.group(1), m.group(2))
            eds = m.group(3)
            book = m.group(4)
        else:
            m = re.match(r"^in\s+(.+?)\s*\(eds?\),\s*(.+?),\s*([^,]+)$", rest)
            if m:
                eds, book, pubr = m.group(1), m.group(2), m.group(3)
            else:
                m = re.match(r"^(.+?)(?::\s*(\d+)\s*[-\u2013]\s*(\d+))?$", rest)
                if m and rest and not rest.lower().startswith("chapter"):
                    book = m.group(1)
                    if m.group(2):
                        pages = "%s\u2013%s" % (m.group(2), m.group(3))
                else:
                    book = None
        entry.update(eds=eds, book=book, pubr=pubr, pg=pages)
        if eds is None:
            missing.append("book editors")
        if not book:
            missing.append("book title (register gives: %s)" % (rest or "nothing"))
        if not pubr:
            missing.append("publisher")
        if not any(p in (rest or "") for p in PLACES):
            missing.append("place of publication")
        if not pages:
            missing.append("page range")
        if qtitle is None:
            missing.append("chapter title")
    elif "thesis" in kl:
        entry["form"] = "thesis"
        tp = work.find("thesis")
        if qpos is not None and 0 <= tp < qpos:
            entry["title"] = None
            qtitle = None
            missing.append("thesis title (register quotes only a section heading)")
        inst = None
        m = re.search(r"PhD thesis,?\s*([^,(]+)", rest or title)
        if m:
            inst = m.group(1).strip()
        entry["inst"] = inst
        if qtitle is None and "thesis title" not in " ".join(missing):
            missing.append("title")
        if not inst:
            missing.append("university")
    elif re.search(r"web|database|data\b", kl) and "report" not in kl and not kl.startswith("statistical"):
        entry["form"] = "web"
        url = origin if origin.startswith("http") else None
        acc = None
        m = re.search(r"saved (\d{4}-\d\d-\d\d)", title)
        if m:
            acc = m.group(1)
        else:
            m = re.search(r"accessed (\d{4}-\d\d-\d\d)", row["dated_or_accessed"])
            if m:
                acc = m.group(1)
        entry.update(url=url, acc=acc, dataset=bool(re.search(r"database|data\b", kl)))
        if url is None:
            missing.append("URL")
        if acc is None:
            missing.append("date accessed")
        if qtitle is None:
            entry["title"] = None if note_only else (rest or None)
            if not rest or note_only:
                missing.append("title")
    elif re.search(r"book$|^book|book /|book \(", kl) and "review" not in kl:
        entry["form"] = "book"
        m = re.match(r"^(.*?),\s*([^,]+)$", rest) if (qtitle is None and not note_only) else None
        if m:
            entry["title"], entry["pubr"] = m.group(1).strip(), m.group(2).strip()
        elif note_only:
            entry["pubr"] = None
            entry["title"] = None
            missing.append("title")
        else:
            entry["pubr"] = rest or None
        missing.append("edition (or confirm first edition)")
        if not entry.get("pubr"):
            missing.append("publisher")
        if not any(p in (rest or "") for p in PLACES):
            missing.append("place of publication")
    else:
        # reports of all kinds
        entry["form"] = "report"
        place = next((p for p in PLACES if p in (rest or "")), None)
        if qtitle is None:
            if not rest or note_only:
                missing.append("title")
                entry["title"] = None
            elif re.search(r"[,(]", rest):
                entry["title"] = rest
                missing.append("title, issuer, series and place not separated in the register")
            else:
                entry["title"] = rest
            entry["issuer"] = auth_raw if corporate else None
        else:
            iss = re.sub(r"\b(?:%s)\b" % "|".join(PLACES), "", rest).strip(" ,;.") if place else rest
            iss = re.sub(r"\s*,\s*(?:,\s*)+", ", ", iss).strip(" ,;.")
            entry["issuer"] = iss or (auth_raw if corporate else None)
            if re.search(r"[\d(;]", iss or ""):
                missing.append("issuer, series and publication details not separated in the register; text kept as is")
        entry["place"] = place
        if not place and "not separated" not in " ".join(missing):
            missing.append("place of publication")
        if not entry.get("issuer") and "not separated" not in " ".join(missing):
            missing.append("issuer")
        if qtitle is None and not entry.get("title"):
            pass

    if entry["year"] is None:
        missing.insert(0, "year")
    entry["missing"] = list(dict.fromkeys(missing))
    return entry


def fallback(rid, row, why):
    names, etal = split_authors(re.split(r"[,(\"]| \d{4}", row["title"], maxsplit=1)[0])
    sort = names[0] if names else row["title"][:20]
    ym = re.search(r"\b((?:19|20)\d\d)\b", row["title"])
    return {"id": rid, "form": "raw", "raw": re.sub(r"\s*\[[^\]]*\]", "", row["title"]).strip(), "sort_names": [sort], "authors": sort,
            "year": ym.group(1) if ym else None, "title": row["title"], "doi": None, "kind": row["kind"],
            "corporate": False, "missing": [why + "; register text printed as is"]}


def abbreviate(name, unknown):
    if name in ABBR:
        return ABBR[name]
    key = name.strip()
    for k, v in ABBR.items():
        if k.strip().lower() == key.lower():
            return v
    unknown.add(name)
    return name


def render(e, ylabel, unknown):
    y = ylabel if e["year"] else "n.d."
    f = e["form"]
    doi = ("https://doi.org/" + e["doi"]) if e.get("doi") else None
    if f == "raw":
        s = e["raw"]
    elif f == "journal":
        parts = ["%s, %s." % (e["authors"], y)]
        if e["title"]:
            t = e["title"].rstrip(" .")
            parts.append(t + ("" if t.endswith(("?", "!")) else "."))
        v = e.get("venue")
        if v:
            vs = abbreviate(v, unknown)
            tail = ""
            if e.get("vol"):
                tail += " " + e["vol"]
            if e.get("iss"):
                tail += " (%s)" % e["iss"]
            if e.get("pg"):
                tail += ", " + e["pg"]
            parts.append(vs + tail + ".")
        if doi:
            parts.append(doi)
        s = " ".join(parts)
    elif f == "chapter":
        parts = ["%s, %s." % (e["authors"], y)]
        if e["title"]:
            parts.append(e["title"].rstrip(".") + ".")
        bk = "In: "
        if e.get("eds"):
            bk += "%s (Eds.), " % e["eds"]
        bk += (e.get("book") or "[book]")
        if e.get("pubr"):
            bk += ". " + e["pubr"]
        if e.get("pg"):
            bk += ", pp. " + e["pg"]
        parts.append(bk + ".")
        if doi:
            parts.append(doi)
        s = " ".join(parts)
    elif f == "thesis":
        parts = ["%s, %s." % (e["authors"], y)]
        if e["title"]:
            parts.append(e["title"].rstrip(".") + ".")
        parts.append("PhD thesis" + (", " + e["inst"] if e.get("inst") else "") + ".")
        if doi:
            parts.append(doi)
        s = " ".join(parts)
    elif f == "web":
        parts = ["%s, %s." % (e["authors"], y)]
        if e.get("title"):
            parts.append(e["title"].rstrip(".") + (" [dataset]" if e.get("dataset") else "") + ".")
        elif e.get("dataset"):
            parts.append("[dataset].")
        if e.get("url"):
            parts.append(e["url"] + (" (accessed %s)." % iso_to_text(e["acc"]) if e.get("acc") else ""))
        elif e.get("acc"):
            parts.append("(accessed %s)." % iso_to_text(e["acc"]))
        s = " ".join(parts)
    elif f == "book":
        parts = ["%s, %s." % (e["authors"], y)]
        if e.get("title"):
            parts.append(e["title"].rstrip(".") + ".")
        if e.get("pubr"):
            parts.append(e["pubr"].rstrip(".") + ".")
        if doi:
            parts.append(doi)
        s = " ".join(parts)
    else:  # report
        parts = ["%s, %s." % (e["authors"], y)]
        if e.get("title"):
            parts.append(e["title"].rstrip(".") + ".")
        tail = ", ".join(x for x in [e.get("issuer"), e.get("place")] if x)
        if tail and tail != e["authors"] and e.get("issuer") != e["authors"]:
            parts.append(tail + ".")
        elif e.get("place"):
            parts.append(e["place"] + ".")
        if doi:
            parts.append(doi)
        s = " ".join(parts)
    s = re.sub(r"\.\.+", ".", s)
    s = re.sub(r"\s+", " ", s).strip()
    if e["missing"]:
        s += " [CHECK: %s]" % "; ".join(e["missing"])
    return s


# ---------- prose scan ----------
NAME = r"(?:(?:van|Van|de|De|den|von|Von|der|le|la|Mc)\s)*[A-Z][A-Za-z'\u2019\-]+"
CIT = re.compile(r"(?<![A-Za-z])(" + NAME + r"(?:(?:,\s" + NAME + r")*(?:\s(?:and|&)\s" + NAME + r")|\set al\.?)?)"
                 r"[\s,]*\(?((?:19|20)\d\d)([a-z]?)\b")


ALIAS = {"dcceew": "department climate change energy environment water"}


def row_authors(row):
    t = re.sub(r"\(authors [^)]+\)", "", row["title"])
    if "submission" in row["kind"]:
        ws = set(fold(w) for w in re.findall(r"[A-Za-z]+", re.split(r"\d\(", t)[0])) - {"and", "et", "al"}
        return ws, "csiro"
    qt = re.search(r"[\"\u201c]", t)
    t = t[: qt.start()] if qt else t
    ym = re.search(r"\b(?:19|20)\d\d\b", t)
    a = t[: ym.start()] if ym else re.split(r"[,(]", t)[0]
    a = re.sub(r"\([^)]*\)", " ", a)
    words = set(fold(w) for w in re.findall(r"[A-Za-z\u00c0-\u017f'\-]+", a)) - {"and", "et", "al", "eds"}
    first = fold(re.findall(r"[A-Za-z\u00c0-\u017f'\-]+", a)[0]) if re.findall(r"[A-Za-z\u00c0-\u017f'\-]+", a) else ""
    return words, first


def row_years(row):
    t = row["title"]
    qt = re.search(r"[\"\u201c]", t)
    head = t[: qt.start()] if qt else t
    ys = set(re.findall(r"\b((?:19|20)\d\d)\b", head[:200]))
    ys |= set(re.findall(r"\(((?:19|20)\d\d)\)|\b((?:19|20)\d\d):", t[len(head):]) and
              [a or b for a, b in re.findall(r"\(((?:19|20)\d\d)\)|\b((?:19|20)\d\d):", t[len(head):])])
    return ys


def scan_prose(paper, register, cited_ids):
    folder = os.path.join(ROOT, "papers", PAPER_DIR[paper], "draft")
    files = sorted(glob.glob(os.path.join(folder, SECTION_GLOB[paper]))) + [os.path.join(folder, "supplementary.md")]
    index = {rid: (row_authors(r), row_years(r)) for rid, r in register.items()}
    found = {}      # citation text -> set of ids
    unmatched = {}  # citation text -> files
    ambiguous = {}
    yearless = {}
    for f in files:
        if not os.path.exists(f):
            continue
        text = open(f, encoding="utf-8").read()
        text = re.sub(r"\bclaim[s]? [A-D]\d+\b", " ", text)
        for m in CIT.finditer(text):
            names, yr, sfx = m.group(1), m.group(2), m.group(3)
            toks = re.findall(NAME, names)
            if not toks:
                continue
            first_tok = toks[0].split()[-1]
            if first_tok in STOP or first_tok.endswith("'s") or first_tok.endswith("\u2019s"):
                continue
            if len(names.split()) == 1 and names in STOP:
                continue
            label = "%s %s%s" % (names, yr, sfx)
            ptoks = set(fold(t.split()[-1]) for t in toks) - {"and", "et", "al"}
            for a in list(ptoks):
                if a in ALIAS:
                    ptoks |= set(ALIAS[a].split())
            first = fold(toks[0].split()[-1])
            scored = []
            for rid, ((words, rfirst), ys) in index.items():
                score = len(ptoks & words)
                if not ys:
                    if score:
                        yearless.setdefault(label, set()).add(rid)
                    continue
                if yr not in ys:
                    continue
                if score:
                    scored.append((score + (0.5 if rfirst == first else 0), rid))
            if not scored:
                unmatched.setdefault(label, set()).add(os.path.basename(f))
                continue
            best = max(s for s, _ in scored)
            ids = sorted(rid for s, rid in scored if s == best)
            # prefer ids already cited in the claims files
            pref = [i for i in ids if i in cited_ids]
            found.setdefault(label, set()).update(pref or ids)
            if len(pref or ids) > 1:
                ambiguous[label] = sorted(pref or ids)
    return found, unmatched, ambiguous, yearless


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in PAPER_DIR:
        sys.exit("usage: make_references.py A|B")
    paper = sys.argv[1]
    register = read_register()
    cited = claim_ids(paper)
    found, unmatched, ambiguous, yearless = scan_prose(paper, register, set(cited))
    prose_ids = set()
    for ids in found.values():
        prose_ids.update(ids)
    prose_only = sorted(prose_ids - set(cited))
    all_ids = sorted(set(cited) | set(prose_only))
    no_row = [i for i in all_ids if i not in register]
    use = [i for i in all_ids if i in register]

    entries = [parse_entry(i, register[i]) for i in use]
    # letters for same authors and year
    groups = {}
    for e in entries:
        groups.setdefault((e["authors"], e["year"]), []).append(e)
    for k, g in groups.items():
        g.sort(key=lambda e: (fold(e["title"] or ""), e["id"]))
        for n, e in enumerate(g):
            e["ylabel"] = (e["year"] or "") + (chr(97 + n) if len(g) > 1 and e["year"] else "")
    entries.sort(key=lambda e: (fold(e["sort_names"][0]), len(e["sort_names"]),
                                [fold(n) for n in e["sort_names"][1:]], e["year"] or "9999",
                                e.get("ylabel", ""), e["id"]))
    unknown = set()
    lines = []
    for e in entries:
        lines.append((e, render(e, e.get("ylabel") or e["year"] or "", unknown)))
    n_check = sum(1 for e, _ in lines if e["missing"])

    out = os.path.join(ROOT, "papers", PAPER_DIR[paper], "draft", "references.md")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("# References\n\n")
        fh.write("<!-- Paper %s: %d entries, %d marked [CHECK]. Built by qa/tools/make_references.py from "
                 "qa/literature_register.csv. Elsevier Harvard form. Do not edit by hand; rerun the script. -->\n\n"
                 % (paper, len(lines), n_check))
        for e, s in lines:
            fh.write("%s <!-- %s -->\n\n" % (s, e["id"]))
    # ---- stdout report ----
    reported = [i for i in use if (register[i]["read_or_reported"].lower().startswith("reported")
                                   or "second-hand" in register[i]["kind"].lower())]
    unread = [i for i in use if re.match(r"(not read|not reached|record only|abstract only)",
                                         register[i]["read_or_reported"].lower())]
    print("Paper %s: %d entries (%d from claims csvs, %d from prose only), %d CHECK" %
          (paper, len(lines), len(cited), len(prose_only), n_check))
    print("Written:", out)
    print("Ids with no register row:", ", ".join(no_row) or "none")
    print("Rows cited only as reported in another work (second-hand):", ", ".join(reported) or "none")
    print("Rows not read in full (abstract only, record only, not read, not reached):", ", ".join(unread) or "none")
    print("Prose-only ids (register row found, no claims-csv id):", ", ".join(prose_only) or "none")
    print("Prose citations with no register row:")
    for k in sorted(unmatched):
        hint = ("  (a register row with the same name but no year exists: %s)" % ", ".join(sorted(yearless[k]))
                if k in yearless else "")
        print("  %s  [%s]%s" % (k, ", ".join(sorted(unmatched[k])), hint))
    print("Prose citations matching more than one register row:")
    for k in sorted(ambiguous):
        print("  %s -> %s" % (k, ", ".join(ambiguous[k])))
    print("Journal names with no known abbreviation:", "; ".join(sorted(unknown)) or "none")
    print("CHECK entries:")
    for e, _ in lines:
        if e["missing"]:
            print("  %s (%s %s): %s" % (e["id"], e["sort_names"][0], e["year"], "; ".join(e["missing"])))


if __name__ == "__main__":
    main()
