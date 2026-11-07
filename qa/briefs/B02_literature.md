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

## Task B02: the literature register

Write: `qa/literature_register.csv` (header exactly as the shared schema in `qa/README.md`; ids L001, L002, ...; status `unverified` on every row).

Include one row for every published work, report, inquiry, or article cited or relied on in:
`papers/B_methods/OUTLINE.md`, `papers/B_methods/SECTION7_DRAFT.md`, `papers/A_results/OUTLINE.md`, `papers/A_results/DISCUSSION_MEASURES.md`, `analysis/comparators_2025/README.md` (its register of estimates carries a read/reported/not reached label for each; copy it), `analysis/method_tests_2025/README.md`, `analysis/paper_a/README.md`, `PUBLICATIONS.md`, `ERRATA.md` and `CORRECTION_NOTES.md` (the author's own earlier papers and thesis).

For each: `title` is the full citation as written in the project document (authors, year, title, journal, volume, pages) and where the project gives only a short form, say so in `notes`. `origin` is a DOI or URL if the project document gives one, otherwise `unknown`. `local_path` is the file under `carrying-capacity-models/Literature review/` or `carrying-capacity-models/Comparators/` if the full text is on hand (list the directories and match by title page, never by file name alone), else empty. `sha256` for files on hand. `read_or_reported`: copy the label in the comparators register where it has one; for works with the full text on hand and cited for a specific figure, `read`; for anything else `not reached` unless a project document says it was read. `what_taken` is the specific figure or claim taken from it (one line). `used_by` names the documents that cite it.

Also, in your report (not the register): list works that are cited in two documents with different details (year, title or figure).
