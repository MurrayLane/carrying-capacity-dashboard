# B150: the submission packages and the deposit package prepared

Nothing was uploaded, tagged, sent or published. No git command, no subagent, no network. Written only under `papers/SUBMISSION/` and this report. No draft, register or analysis file was edited.

## Files written

* `papers/SUBMISSION/checklist_A.md` (Population and Environment)
* `papers/SUBMISSION/checklist_B.md` (Ecological Economics)
* `papers/SUBMISSION/cover_letter_A.md` (339 words), `cover_letter_B.md` (368 words)
* `papers/SUBMISSION/deposit/README_deposit.md`, `deposit/metadata.json` (valid JSON; description 899 characters)
* `papers/SUBMISSION/BEFORE_SUBMIT.md`
* this report

## Counts (run 2026-11-18)

| | Paper A | Paper B |
|---|---|---|
| `wordcount.py` main text, words | 7,939 | 7,934 |
| main text characters (scratch script, the tool's own rule) | 45,748 with spaces, 37,670 without | 47,011 with spaces, 38,885 without |
| main text if captions and table cells count (scratch) | about 10,300 | about 12,800 |
| abstract, words | 245 (limit 150 to 250) | 250 (limit 250) |
| highlights, characters | 83, 83, 84, 81, 80 | 76, 84, 84, 83, 77 (limit 85) |
| keywords | 7 | 7 |
| references / marked [CHECK] | 57 / 18 | 129 / 30 |
| main tables / figures | 9 / 8 | 9 / 3 |
| figure files | 8 main PNG at 300 dpi (Figure 1 is 90 mm, 1,062 px; the rest 190 mm, 2,244 px), plus S6; SVG beside each | 3 figures, each as 190 mm and 90 mm PNG and SVG |

## Placeholders (all left open)

Author name, affiliation with full postal address, corresponding email and ORCID (title pages, CRediT in both declarations files, `metadata.json` creators); final titles; editor name and date in the letters; suggested reviewers "[author to supply]"; companion paper status in each letter; archive DOI and the two paper DOIs; `[submission commit hash]`; the Opus and Sonnet model names and versions in Paper B's AI declaration; the three `[CONFIRM]` items in `papers/DECLARATIONS.md` (coordinating model, thesis wording, funding); the Figure S1 placeholder line in Paper A's supplement; 18 and 30 reference entries marked [CHECK]. The letters and metadata also contain the existing repository URL (it carries the account handle) copied from `CITATION.cff` and the drafts.

## Anything the journals ask for that the project cannot yet supply

* Population and Environment's guidelines are not on disk: keyword count, anonymised review, figure widths, where the AI declaration goes, and how supplements are cited are marked "recalled" in `checklist_A.md` and need Murray's check at the URL.
* Word or LaTeX source: both drafts and supplements are Markdown. `/usr/bin/pandoc` exists; no conversion was made (outside the write scope). The preamble line and the drafter-notes blocks must be left out.
* Vector figures: SVG only; Ecological Economics asks for EPS or PDF. No converter is installed.
* A separate highlights file for Ecological Economics (the project file also holds keywords).
* Acknowledgements section (Ecological Economics asks for one); ethics statement for Springer; the Paper A supplement's Figure S1 (170 dpi, no caption row).
* The word limit may count captions and tables: on that count both papers are well over 8,000.
* Archive DOI, author details, reviewers, model versions: author only.
* The two response letters answer simulated referee reports and are not for a journal; flagged in both checklists.

## Wrong-value check (example)

A count deliberately copied from an earlier report: B146b (`qa/reports/B146b_patch_paper_B_round3.md`) gives Paper B's main text as "**7,948**". `python3 qa/tools/wordcount.py B` printed `TOTAL 7934` on 2026-11-18, so the copied value fails against the tool by 14 words. The 7,948 is superseded: B147b (`qa/reports/B147b_figures_into_paper_B.md`) records the fall to 7,934 (the old Table 2 placeholder line had been counted as prose). `checklist_B.md` carries 7,934. This is an example of the check, not a defect in a file.

No em dashes in any file written (checked with grep).
