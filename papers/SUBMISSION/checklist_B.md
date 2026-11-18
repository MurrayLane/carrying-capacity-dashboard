# Submission checklist: Paper B (methods), Ecological Economics

Prepared 2026-11-18 from the drafts as they stood when this file was written. Nothing is submitted, uploaded or sent. "Author" in the Status column means only Murray can supply or confirm it. Journal requirements are those Murray recorded in `papers/B_methods/JOURNAL_REQUIREMENTS.md` (guide for authors read 2026-11-14, https://www.sciencedirect.com/journal/ecological-economics/publish/guide-for-authors); this job read no journal page.

Order of submission: **Paper B first** (this paper), then Paper A (`checklist_A.md`). Paper B's cover letter names Paper A as in preparation or under review; the letter for Paper A then names Paper B as under review.

Article type: Methodological and Ideological Options (decision 94; Analysis is the fallback).

## 1. Counts as the tools give them

Run 2026-11-18 on the files in `papers/B_methods/draft/`. Other builders are editing, so rerun both commands on the submission commit and replace these figures.

| Item | Limit | Count | Tool or method |
|---|---|---|---|
| Main text, prose only | under 8,000 words (project cap 7,950) | **7,934** | `python3 qa/tools/wordcount.py B` (sections 1 to 9: 714, 519, 295, 858, 2,723, 1,324, 656, 468, 377) |
| Main text, characters | none set | 47,011 with spaces; 38,885 without | scratch script applying `wordcount.py`'s own counting rule (the tool prints words only) |
| Main text, if captions and table cells are counted | under 8,000 words if the journal counts them | about 12,800 | scratch count of all text in the numbered sections, captions and tables included |
| Abstract | 250 words at most | **250** (1,447 characters) | whitespace count of the Abstract in `paper_B_draft1.md`; at the limit, so any edit needs a cut |
| Highlights | 3 to 5, at most 85 characters each | 5 bullets: 76, 84, 84, 83, 77 characters | `papers/B_methods/draft/highlights.md` |
| Keywords | 1 to 7, single words preferred | 7 (all but "Australia" are phrases) | same file; Murray's call whether to shorten |
| References | complete, DOIs | 129 entries, 30 marked [CHECK] | `papers/B_methods/draft/references.md` header |
| Tables in the main text | editable text | 9 (Tables 1 to 9) | `paper_B_draft1.md` |
| Figures in the main text | separate files | 3 (Figures 1 to 3) | `analysis/figures_2025/paper_B/figures.csv` |
| Supplementary information | each file cited with a caption | Sections S1 to S8, Tables S1 to S15 about 15,300 words by `wc -w` (markup included) | `papers/B_methods/draft/supplementary.md` |

Risk to settle: the guide gives the 8,000-word maximum without saying whether captions, tables and references count (Murray's note in the requirements file). On the prose rule the paper is under by 66 words; if the editor counts captions and tables it is over by a wide margin. Murray decides whether to ask the editorial office.

## 2. What the journal asks for, and what satisfies it

| # | Item | Satisfied by | Status |
|---|---|---|---|
| 1 | Article type chosen in the portal | decision 94 | author |
| 2 | Title without abbreviations | title in the draft heading: "well-known carrying-capacity methods tested on common Australian data"; the draft heading carries a "Paper B, methods:" label that is not part of the title | author to settle the final title |
| 3 | Author name, affiliation with full postal address, corresponding author and email (published) | none in any file | author: [name], [affiliation with full postal address], [corresponding author email], [ORCID] |
| 4 | Manuscript as Word (.docx, single column) or LaTeX; PDF not accepted as source | the draft is Markdown (`paper_B_draft1.md`); build the Word file from it without the preamble line "First draft, assembled ..." and without the four "Drafter notes (not for the paper)" blocks, which the draft carries at its end | coordinator or author builds the .docx (`/usr/bin/pandoc` is installed on the build machine); check tables and headings after conversion |
| 5 | Abstract, 250 words or fewer, outside the numbering | abstract in the draft (250 words) | done; at the limit |
| 6 | 1 to 7 keywords | `highlights.md` (7) | done |
| 7 | Highlights file, separate, "highlights" in its name, 3 to 5 bullets, each at most 85 characters | `papers/B_methods/draft/highlights.md` holds the bullets and also the keywords | coordinator: save the bullets alone as a separate Word file named with "highlights" |
| 8 | Numbered sections 1, 1.1, 1.1.1 | the draft | done |
| 9 | Tables as editable text with captions, numbered in order, notes below, no vertical rules | Tables 1 to 9 in the draft | check after the Word build |
| 10 | Figures as separate files, numbered, each with a caption; vector as EPS or PDF; bitmaps at least 300 dpi (1,063 pixels single column, 2,244 full page) | section 3 below | vector files are SVG only: EPS or PDF to be made (no converter is installed on the build machine) |
| 11 | Maps: study area only and the boundary note | Paper B has no map | not applicable |
| 12 | Appendices lettered A, B; numbered A.1, B.1 | Paper B uses supplementary sections S1 to S8 instead | none needed |
| 13 | Supplementary material, each file cited in the text with a caption, published as received | `papers/B_methods/draft/supplementary.md`; the main text cites sections and tables of it | coordinator builds the .docx; Tables S1 to S15 carry captions in the file |
| 14 | Declaration of competing interests, in the journal's tool as well as the manuscript | section "Declaration of competing interests" in `papers/B_methods/draft/B_s10_declarations.md` (the model is the author's own) | author enters it in the portal tool |
| 15 | Funding statement | "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors." in `B_s10_declarations.md` | author confirms (no grant, no employer support, no funder paying for the Claude subscription) |
| 16 | Declaration of generative AI use, a section before the reference list, in the journal's form | section "Declaration of generative AI and AI-assisted technologies in the writing process" in `B_s10_declarations.md`; the fuller version is in `papers/DECLARATIONS.md` section 2 | author: the model name and version for Opus and for Sonnet (two bracketed places), and the name and version of the coordinating model (DECLARATIONS.md [CONFIRM]) |
| 17 | CRediT author statement | `B_s10_declarations.md`, "[Author name]: Conceptualization, ..." | author: name |
| 18 | Acknowledgements, a separate section before the references | none in the draft | author: write one, or state none |
| 19 | Research data (Option C): deposit in a repository, link at submission | Zenodo deposit prepared in `deposit/`; statement text in section 4 below | author mints the DOI; then the data statement is patched |
| 20 | References: complete, DOI where one exists, alphabetical then chronological, [dataset] and [software] tags, web references with date accessed, preprints marked | `papers/B_methods/draft/references.md` (Elsevier Harvard form, built by `qa/tools/make_references.py`) | 30 entries carry [CHECK]; `BEFORE_SUBMIT.md` lists them; add the [dataset] entry for the Zenodo deposit |
| 21 | Cover letter, signed | `cover_letter_B.md` | author: name, signature, reviewers |
| 22 | Suggested reviewers (the portal asks) | none | author: [author to supply] |
| 23 | Graphical abstract (optional) | none | author's choice |
| 24 | SSRN preprint (optional, offered at submission) | none | author's choice |
| 25 | MethodsX or Data in Brief co-submission (optional, article charge) | none | author's choice; not required |

## 3. Figure files to upload

Source of captions and file names: `analysis/figures_2025/paper_B/figures.csv`. All PNG files are at 300 dpi, so 2,244 pixels is 190 mm and 1,062 pixels is 90 mm. Upload one set; the full-page set is suggested. The main text cites each figure by number.

| Figure | Upload (PNG, full page) | Pixels | Single-column PNG | Pixels | Vector (SVG only) |
|---|---|---|---|---|---|
| 1 | `analysis/figures_2025/paper_B/fig1_method_map_190mm.png` | 2,244 x 1,358 (190 mm) | `fig1_method_map_90mm.png` | 1,062 x 1,518 (90 mm) | `fig1_method_map_190mm.svg`, `fig1_method_map_90mm.svg` |
| 2 | `analysis/figures_2025/paper_B/fig2_method_readings_190mm.png` | 2,244 x 1,181 (190 mm) | `fig2_method_readings_90mm.png` | 1,062 x 1,482 (90 mm) | `fig2_method_readings_190mm.svg`, `fig2_method_readings_90mm.svg` |
| 3 | `analysis/figures_2025/paper_B/fig3_design_choices_190mm.png` | 2,244 x 1,557 (190 mm) | `fig3_design_choices_90mm.png` | 1,062 x 2,472 (90 mm) | `fig3_design_choices_190mm.svg`, `fig3_design_choices_90mm.svg` |

Table 2 is also built as text: `analysis/figures_2025/paper_B/table_2.md` (it is in the manuscript as a table, not an image). The journal asks for EPS or PDF for vector art: the SVG files need conversion by the author or coordinator. Colour readability for impaired colour vision is a journal requirement; the figure checks V56b are in `qa/reports/V56b_check_figures_B.md`.

## 4. Data availability statement (text to paste; one placeholder)

The draft's section 9.4 ends with a dated sentence ("On 18 November 2026 the archive has no DOI and the author has not deposited it on Zenodo") that becomes false after the deposit. Replace that sentence, and use this text for the portal's research-data field:

> The model, its frozen releases, the data pipeline, the scripts that built every table and figure, and the claims and sources registers are in the repository https://github.com/MurrayLane/carrying-capacity-dashboard, archived at the submission commit (version submission-1) at https://doi.org/[DOI] [dataset]. The releases used are 2025-mirror, 2025-fixed and 2025-improved, identified by hash in `results/releases.json`, and each table names the file it was built from. Code is under the MIT licence; the model workbook, default inputs, 2011 baseline and analysis outputs are under CC BY 4.0, and source data keep their publishers' licences (`LICENSE-DATA.md`).

Reference-list entry to add (journal form; placeholders for the author's name and the DOI): `[Author surname, initials], 2026. Carrying Capacity Dashboard: model, data and results, version submission-1 [dataset]. Zenodo. https://doi.org/[DOI]`.

## 5. Files to assemble for the portal

1. Manuscript (.docx) built from `papers/B_methods/draft/paper_B_draft1.md` minus the preamble and drafter notes, with the title page from item 3 above.
2. Highlights (.docx, separate).
3. Figures 1 to 3 (section 3).
4. Supplementary information (.docx) built from `papers/B_methods/draft/supplementary.md`.
5. Cover letter from `papers/SUBMISSION/cover_letter_B.md`.
6. The DOI of the deposit, for the research-data field.

Do not send `papers/B_methods/response_letter_round2.md`: it answers simulated referee reports (the declaration says so), not a journal's.
