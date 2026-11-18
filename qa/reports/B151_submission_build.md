# B151 report: the submission build

## What was written

* `qa/tools/build_submission.sh` (new). Run from the repository root: `bash qa/tools/build_submission.sh`.
* `papers/A_results/draft/acknowledgements_and_statements.md` and `papers/B_methods/draft/acknowledgements_and_statements.md` (new; no names).
* One edit each to `analysis/figures_2025/paper_A/_common.py` and `paper_B/common.py`: the shared `save` helper also writes a PDF beside the PNG and SVG (same size; fonts as Type 42 through `rc_context`; creation and modification dates left out so reruns match). Every figure script calls that helper, so no script needed its own edit.
* 15 new figure PDFs beside the PNG and SVG files (9 for Paper A including S6, 6 for Paper B, both widths).
* `papers/SUBMISSION/build/{A,B}/` and `build/_work/` (intermediate reference lists and logs).
* This report.

No section file, claims csv, register or `figures.csv` was edited.

## Figures

All 15 scripts were rerun (`build_catalogue.py` and `make_figures_csv.py` were not). Every PNG and SVG is byte-identical to its copy taken before the rerun (cmp, 0 differences, 19 files in A and the B set), and both `figures.csv` files and `table_2.md` are unchanged (Paper A's scripts rewrite `figures.csv` on each run; the content came out the same). The 15 PDFs open: `%PDF` header, `pdfinfo` reads one page each at the expected size (for example 538.6 x 663.7 pt for Figure 2 of A, 255.1 x 226.8 for Figure 1), and `pdffonts` shows embedded TrueType (CID) fonts. PyMuPDF (`fitz`) is not installed; `pdfinfo` was used.

## Counts the build prints

| Item | Paper A | Paper B |
|---|---|---|
| Main text words (`wordcount.py`, prose only) | 7,939 | 7,934 |
| Abstract | 245 words, 1,478 characters | 250 words, 1,447 characters |
| Highlights (Ecological Economics, limit 85) | not asked | 76, 84, 84, 83, 77 characters, 5 bullets |
| Keywords | 7 (`keywords.txt`) | 7 (in the manuscript under the abstract) |

These equal the figures in the two checklists.

## Placeholders ("[") left in the built files

* Paper A (`paper_A.md`): `[Author name]` (CRediT), 2 x `[author to supply]` (Acknowledgements, Data availability), `[to be added at release]` (archive DOI in the main-text data statement), 18 reference entries with `[CHECK ...]` (20 occurrences counted per bracket text: place of publication 7, book editors 3, not seen 2, author form 1, DOI 1, publisher 2, year 1), and two footnote markers `[^1]` and a bracketed thesis description, which are not placeholders. `Supplement_A.md`: the `[Supplementary Figure S1: ...]` line.
* Paper B (`paper_B.md`): `[Author name]`, 2 x `[author to supply]`, the two bracketed model names and versions in the AI declaration, 2 x `[dataset]` (reference tags, not placeholders), `[0195:RTLTWP]` (part of a DOI), and `[CHECK ...]` on the reference entries (place of publication 10 and 2 more of that kind, plus not seen, URL and date accessed, author initials, volume, year and others; the full list is in the script's output). `Supplement_B.md`: none.
* `highlights.txt` and `keywords.txt`: none.

## Docx sizes

`paper_A.docx` 42,046 bytes; `Supplement_A.docx` 34,733; `paper_B.docx` 57,422; `Supplement_B.docx` 45,882. All four open as zip archives (testzip). Default pandoc styles.

## Idempotence

A second run gave identical SHA-256 sums for every file under `build/` (docx zip timestamps and `core.xml` dates are fixed in the script).

## How the build composes each manuscript

Order: title, abstract, keywords line, numbered sections, then the statements file, then the reference list. Reference lists go to `build/_work/` through `--out`, so `papers/*/draft/references.md` are not touched by the build. `assemble_draft.py --submission` does write `papers/<paper>/draft/paper_<P>_submission.md`, as it always does.

Decision for the author: the section files `A_s13_declarations.md` and `B_s10_declarations.md` are picked up by `assemble_draft.py`, so the assembled submission already ends with a declarations block. To keep each statement once, the build cuts that block (from `## Declarations` in A, from `## Declaration of generative AI` in B) and appends the new statements file instead. The new files carry the same text as those blocks (the text of `papers/DECLARATIONS.md`, with B's competing-interest wording as revised in `B_s10_declarations.md`, since the first version in DECLARATIONS.md no longer matches the paper), plus the headings the brief lists. I kept the CRediT statement in both files because both journals ask for one and the section files' copy is cut. Acknowledgements and Data availability are `[author to supply]` as briefed; the data statement text itself is still in main-text section 9.4 (B) and the closing "Data and code availability" paragraph (A), so the portal field text in each checklist is still to be pasted. If those section files change, the statements files must be changed by hand to match.

## What the journals ask for that the build cannot supply

Author name, affiliation with postal address, corresponding email, ORCID, final title (title page); the archive DOI and the data-availability text; the two model names and versions (B); acknowledgements; suggested reviewers; the signed cover letters (the build does not touch them); the tables and figures as the journals' portals want them (figure captions are in the manuscript text but the figures are not embedded in the docx); Paper A's Figure S1 (placeholder only, 170 dpi source); EPS (the journals prefer EPS or PDF; PDF is now supplied, no EPS); Springer's rules for Paper A, which no file holds (keyword count, anonymised review, where the AI declaration goes, figure widths; Figures 2 to 8 are 190 mm); whether Ecological Economics counts captions and tables in the 8,000 words (about 12,800 if so); 30 and 18 `[CHECK]` reference entries; the Paper A reference list uses the Springer author-date form as recorded in the tool, unconfirmed against the guidelines. Highlights for Paper A are not built, since the brief asks only for Ecological Economics.

Other builders: `papers/*/draft/references.md` and `qa/*.csv` show as modified in the working tree; this build did not write them.

## Wrong-value check (example, deliberately planted)

Wrong-value check: Paper B main-text words copied from `checklist_B.md` row 1: 7,934; the build's own count: 7,934 (equal, so the check passes). As an example of the comparison failing, the project cap 7,950 copied in its place would differ from 7,934 by 16 and be flagged. This is an example, not a finding.
