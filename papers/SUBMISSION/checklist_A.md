# Submission checklist: Paper A (results), Population and Environment

Prepared 2026-11-18 from the drafts as they stood when this file was written. Nothing is submitted, uploaded or sent. "Author" in the Status column means only Murray can supply or confirm it.

**Source of the journal's requirements.** No copy of the journal's guidelines is on disk and this job had no network. The requirements recorded in `qa/DECISIONS.md` (decisions 92 and 140) and `papers/DECLARATIONS.md` are: Research Article, main text under 8,000 words, abstract 150 to 250 words, Springer author-date references, guidelines at https://link.springer.com/journal/11111/submission-guidelines for Murray to confirm. Rows marked "recalled" below come from general knowledge of Springer journals, not from the guidelines, and must be checked at that URL.

Order of submission: Paper B first (`checklist_B.md`), then Paper A. Paper A's cover letter names Paper B as under review at Ecological Economics.

## 1. Counts as the tools give them

Run 2026-11-18 on the files in `papers/A_results/draft/`. Other builders are editing, so rerun on the submission commit and replace these figures.

| Item | Limit | Count | Tool or method |
|---|---|---|---|
| Main text, prose only | under 8,000 words (project cap 7,950) | **7,939** | `python3 qa/tools/wordcount.py A` (sections 1 to 12: 705, 921, 563, 891, 665, 609, 516, 1,055, 779, 365, 198, 672) |
| Main text, characters | none set | 45,748 with spaces; 37,670 without | scratch script applying `wordcount.py`'s own counting rule (the tool prints words only) |
| Main text, if captions and table cells are counted | under 8,000 words if the journal counts them | about 10,300 | scratch count of all text in the numbered sections, captions and tables included |
| Abstract | 150 to 250 words | **245** (1,478 characters) | whitespace count of the Abstract in `paper_A_draft1.md` |
| Highlights | not asked by Springer journals as far as recalled; file exists | 5 bullets of 83, 83, 84, 81, 80 characters | `papers/A_results/draft/highlights.md` |
| Keywords | recalled: Springer asks for about 4 to 6 | 7 | same file; shorten if the guidelines say so |
| References | Springer author-date | 57 entries, 18 marked [CHECK] | `papers/A_results/draft/references.md` header |
| Tables in the main text | editable | 9 (Tables 1 to 9) | `paper_A_draft1.md` |
| Figures in the main text | separate files | 8 (Figures 1 to 8) | `analysis/figures_2025/paper_A/figures.csv` |
| Supplementary information | cited in the text | Sections S1 to S12, Tables S1 to S17, Figure S6 and a placeholder for Figure S1; about 10,300 words by `wc -w` (markup included) | `papers/A_results/draft/supplementary.md` |

Risk to settle: it is not known whether the journal's 8,000 words include captions, tables and references. On the prose rule the paper is under by 61 words.

## 2. What the journal asks for, and what satisfies it

| # | Item | Satisfied by | Status |
|---|---|---|---|
| 1 | Article type: Research Article | decision 92 | author selects in the system |
| 2 | Title | draft heading: "Australia's carrying capacity 2011 to 2025 by region on the corrected releases"; the heading carries a "Paper A, results:" label that is not part of the title | author to settle the final title |
| 3 | Title page: author, affiliation, corresponding author email, ORCID | none in any file | author: [name], [affiliation], [corresponding author email], [ORCID] |
| 4 | Whether review is anonymised (recalled: check) | the text names the author's own earlier papers and the repository URL | author: if the journal asks for an anonymised manuscript, the title page goes in a separate file and self-references and the repository link need handling |
| 5 | Manuscript as Word or LaTeX (recalled) | the draft is Markdown (`paper_A_draft1.md`); build the Word file without the preamble line "First draft, assembled ..." and without the four "Drafter notes (not for the paper)" blocks | coordinator or author builds the .docx (`/usr/bin/pandoc` is installed on the build machine) |
| 6 | Abstract, 150 to 250 words | abstract in the draft (245 words) | done |
| 7 | Keywords | `highlights.md` (7) | confirm the number allowed |
| 8 | Tables as editable text, numbered, cited | Tables 1 to 9 | check after the Word build |
| 9 | Figures as separate files with captions; resolution and format as the journal says (recalled: 300 dpi, TIFF or EPS, single column about 84 mm, double column about 174 mm) | section 3 below | check widths: Figures 2 to 8 are 190 mm wide, which may exceed the double-column width; vector files are SVG only |
| 10 | Supplementary material (Springer calls it Electronic Supplementary Material and cites it as "Online Resource"; recalled) | `papers/A_results/draft/supplementary.md`; the text cites "Supplementary Section S11" and similar | coordinator builds the .docx; author checks the journal's citing form |
| 11 | Statements and Declarations: funding, competing interests, data availability, ethics, author contributions (recalled) | `papers/A_results/draft/A_s13_declarations.md` and the "Declarations" block of the draft hold the AI declaration, competing interests, funding and CRediT in the Elsevier form | author: confirm headings against the guidelines; ethics statement not drafted (a draft for the author to confirm: "Not applicable: the study uses published statistics and no human or animal subjects.") |
| 12 | Declaration of generative AI use (recalled: Springer asks for it in the Methods section, not in the acknowledgements, and does not accept AI as an author) | `A_s13_declarations.md`; fuller text in `papers/DECLARATIONS.md` section 2 | author: place it as the journal asks; name and version of the models (DECLARATIONS.md [CONFIRM name and version]); Paper A's own AI text does not carry bracketed model names, Paper B's does, so keep the two consistent |
| 13 | Competing interests | `A_s13_declarations.md` (the model is the author's own; Paper A variant) | author confirms the thesis wording (DECLARATIONS.md [CONFIRM]) |
| 14 | Funding | the standard no-grant sentence in `A_s13_declarations.md` | author confirms |
| 15 | CRediT statement | `A_s13_declarations.md`, "[Author name]: ..." | author: name |
| 16 | Data availability, with the archive DOI | section 4 below | author mints the DOI |
| 17 | References in Springer author-date form, DOIs | `papers/A_results/draft/references.md` | 18 entries carry [CHECK]; `BEFORE_SUBMIT.md` lists them; add the [dataset] entry for the Zenodo deposit |
| 18 | Cover letter | `cover_letter_A.md` | author: name, signature, reviewers |
| 19 | Suggested reviewers | none | author: [author to supply] |

## 3. Figure files to upload

Captions and sources: `analysis/figures_2025/paper_A/figures.csv`. PNG files are at 300 dpi, so 2,244 pixels is 190 mm and 1,062 pixels is 90 mm. Vector versions are SVG (same name, `.svg`); no EPS or PDF exists.

| Figure | PNG file in `analysis/figures_2025/paper_A/` | Pixels | Width |
|---|---|---|---|
| 1 | `fig1_national_capacity_population.png` | 1,062 x 944 | 90 mm |
| 2 | `fig2_regional_change_flips.png` | 2,244 x 2,765 | 190 mm |
| 3 | `fig3_layer_effects.png` | 2,244 x 2,958 | 190 mm |
| 4 | `fig4_scale_curve.png` | 2,244 x 968 | 190 mm |
| 5 | `fig5_long_term.png` | 2,244 x 2,314 | 190 mm |
| 6 | `fig6_shocks.png` | 2,244 x 2,568 | 190 mm |
| 7 | `fig7_method_effects.png` | 2,244 x 2,958 | 190 mm |
| 8 | `fig8_migration_map.png` | 2,244 x 1,464 | 190 mm |
| S6 (supplement) | `fig6s_scenarios.png` | 2,244 x 1,789 | 190 mm |
| S1 (supplement) | `analysis/regionalise_2025/ideal_K53_cap650k.png` | 1,100 x 1,021 | about 164 mm at 170 dpi, below 300 dpi |

Open for Figure S1: the supplement carries only a bracketed placeholder line for it ("[Supplementary Figure S1: the best contiguous split ...]"), the file is not in `figures.csv`, has no caption of the figure builders' kind, and is 170 dpi. Either the supplement is built with the file as it is, or a figure job remakes it. Figure 8 is a map: the journal may ask for the usual boundary note; none is in the caption.

## 4. Data availability statement (text to paste; one placeholder)

The draft's closing paragraph "Data and code availability" ends with "The claims and sources registers are published with the archive (DOI: [to be added at release])." Replace that sentence with the first sentence below; the rest of the paragraph stands.

> The repository at the commit tagged submission-1, with the claims and sources registers, is archived at https://doi.org/[DOI] [dataset].

The full statement then reads: the repository https://github.com/MurrayLane/carrying-capacity-dashboard holds the model, its releases, the data pipeline and the results files that generate every table and figure; Supplementary Section S11 keys release names to the files behind each table and figure; the archive DOI is as above. Code is MIT; model workbook, default inputs, baseline and analysis outputs are CC BY 4.0; source data keep their publishers' licences (`LICENSE-DATA.md`).

Reference-list entry to add, in Springer author-date form (placeholders for the author's name and the DOI): `[Author surname, initials] (2026) Carrying Capacity Dashboard: model, data and results, version submission-1 [dataset]. Zenodo. https://doi.org/[DOI]`.

## 5. Files to assemble for the system

1. Manuscript (.docx) from `papers/A_results/draft/paper_A_draft1.md`, minus preamble and drafter notes, with a title page.
2. Figures 1 to 8 (section 3).
3. Supplementary information (.docx) from `papers/A_results/draft/supplementary.md`, with Figure S6 and Figure S1 placed.
4. Highlights, only if the journal accepts them: `papers/A_results/draft/highlights.md`.
5. Cover letter from `papers/SUBMISSION/cover_letter_A.md`.
6. The DOI of the deposit.

Do not send `papers/A_results/response_letter_round2.md`: it answers simulated referee reports, not a journal's. Corrections notes to the earlier journals go after Paper A is accepted (decision 117), one letter per journal, drafted from `ERRATA.md` and `CORRECTION_NOTES.md`; none is part of this submission.
