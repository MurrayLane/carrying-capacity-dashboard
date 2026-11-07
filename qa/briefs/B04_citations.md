# Builder brief

You are a builder helper. The coordinator (the main session) wrote this brief and will review your work, so do not try to decide what anything means.

Rules, no exceptions:
* Write only the file(s) named under "Write". Read anything else, change nothing else. Do not run git; the coordinator commits.
* Do not change any result, script or data file. Do not spawn subagents.
* Never invent. If you cannot establish a field, write `unknown` and list it in your report. Copy citations and titles exactly as you find them and record where you found them.
* Every row must rest on something you opened (a file, a page). A path in a row means the file exists: check it.
* Plain, specific notes. No time words (tonight, later, for now, not urgent).
* Repository root: /home/user/carrying-capacity-dashboard (public). The private archive is /home/user/carrying-capacity-models; refer to its files as `carrying-capacity-models/<path>`. Both exist on this machine.

Standing decisions you must not reopen: two papers only; the methods paper tests each method on Australian 2025 data and gives no reproduction gate; corrected values are assumed; the results paper gives 2011 as corrected only. Read `qa/CARD.md` and `qa/README.md` (the schemas) first.
Report format (your final message): (1) what you wrote and the row count; (2) every field or row you could not establish; (3) anything surprising or that looks wrong in the project's own documents; (4) rows a human should check first.

## Task B04: resolve the citation inconsistencies and record identifiers

Write: `qa/literature_register.csv` (update rows in place; keep every column; change `origin`, `dated_or_accessed`, `notes` and, where you establish it, `title`; do not change `status`) and `qa/reports/B04_citation_fixes.md` (your findings, one section per item below, with the evidence: the title page, page or web page you read).

Do not edit any other file. Where a project document (a README, outline, ERRATA or CORRECTION_NOTES) carries a wrong year, journal or series name, list the file, the line and the correction in your report; the coordinator applies them.

Part 1, the nine inconsistencies found by B02 (report each with evidence):
1. Gutteridge study: 2005 or 2006 (the report in `carrying-capacity-models/Literature review/` is dated 12 August 2005; the thesis cites 2005; `analysis/comparators_2025/README.md` says 2006). Also whether the "14 times" ratio appears in the report.
2. Henry and Godden: 1994 (as the Jones inquiry row says) or 1995 (the paper, Vol. 63 No. 1, April 1995).
3. Lane and Dawes 2013: "Urban Environment" (PUBLICATIONS.md) or "Urban Ecosystems" (CORRECTION_NOTES.md). Search the web for the article to settle the journal.
4. ABARE Australian Energy Resource Assessment: 2009 or April 2010; which chapter holds Table 12.12 (400 litres of biodiesel a tonne). The archive files are under `carrying-capacity-models/` (find them).
5. Simpson, Petroeschevsky and Lowe: journal name on the title page.
6. SoFSR (CSIRO and UQ food system report): date, and confirm the page that carries the "feed another 63 million" statement (the file is in `carrying-capacity-models/Comparators/`).
7. Foran and Poldy: the series name on the title page.
8. Lane 2011: the venue.
9. Lane 2017 and the "time-frames paper (ePrints 99790)": the same work or two? Search QUT ePrints 99790.
Part 2, identifiers: for every row whose `origin` is `unknown`, search the web (DOI, publisher page, QUT ePrints, Trove, the National Library catalogue) and record a DOI or stable URL where one exists, with the date you accessed it in `dated_or_accessed`. Record `unknown (searched <date>)` where you find none. Do not download PDFs into either repository.
Part 3, the four "read as cited" rows (L001, L002, L004, L005): try to locate the primary document online (Griffith Taylor; the Borrie National Population Inquiry 1975; the National Population Council 1991; Gifford, Kalma, Aston and Millington 1975, Search 6(6): 212) and record the URL if found; do not change `read_or_reported`.
