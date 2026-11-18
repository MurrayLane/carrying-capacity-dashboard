# B127: register follow-ups from B125, B126a and B126b; analysis files regenerated to the widened range

Brief: `qa/briefs/B127_register_and_regen_after_patches.md`. No subagents, no network. One slip to disclose: I ran `git status` once (read only, nothing changed) before I took in the "no git" rule. Written: `qa/claims_register.csv`, `qa/references.csv`, `qa/defects.csv`, `analysis/method_tests_2025/` (`cross_method.py`, `design_choices.py`, `bases_fidelity.py`, `cassidy_people_per_hectare.py`, `README.md` and the csv files those scripts write), `papers/A_results/SECTION_SCOPE.md` (two cells), both `references.md` (by `make_references.py`), this report. No paper section file, frozen release or `results/` file touched. No em dash in anything I wrote.

Checks: register 805 lines, 18 columns on every row, CRLF kept, only the rows listed in section 1 differ from before (all other rows go through the csv writer unchanged; the file round-trips byte-identical). `references.csv` 190 rows, 21 columns, CRLF kept, only the ten rows listed in section 2 differ. `defects.csv` 140 lines, 8 columns, one line appended. `bases_fidelity.py --check`: 0 mismatches. Tier A: `value` and `statement` of every Tier A row are untouched (edits made only to `notes`; A187, A205, A223, B083, B273, B274, B276).

## 1. Claims register: every row changed (id; before; after)

Each row has a `B127 2026-11-18 (from B12x): before; after` note.

| Id | Tier | Before | After |
|---|---|---|---|
| A187 | A | notes: pending text "widened range of 0.72 to 1.13 (0.715 to 1.130)" | notes: "0.71 to 1.13 (the csv prints 0.715 to 1.130; the 0.715 is already rounded)"; B127 note: 19,735,337 / 27,608,200 = 0.7148, which prints 0.71. Value 0.95 and statement unchanged |
| A411 | B | statement and value "0.72 to 1.13" (1 in 20, capacity over population, widened) | "0.71 to 1.13" in both; same arithmetic noted. A411 is the Tier B row that carries the widened 1-in-20 ratio range |
| A223 | A | notes: gate 5 pending "new value -0.3; -26 unchanged in value" | "new value -0.2; -26"; B127 note cites `scenarios_by_region.csv` line 27 (2025-fixed, climate-crops-24, short), column `change on reference` = -0.2%. The statement still prints -0.3 (Tier A, the coordinator's at gate 5) |
| A205 | A | no note on the -0.2 cell | B127 note: same cell, -0.2%, gate 4 note already right. Value -0.26% (improved reference) unchanged |
| B276 | A | pending text only | B127 note: 0.59 is the file's figure (`harmonised_comparison.csv` Summary row note and the Cassidy all-cropland row 0.594; README lines 561, 569); 0.62 (0.618) appears only in B273's notes and the B93 report; if gate 4 approves B084 (183) and B273 (0.618), the csv files regenerate first and the low end would read 0.62 |
| B273 | A | notes: "(factor 0.618) ... so the factor from 183 to 112.9 is 0.618" | "(factor about 0.62: B93 prints 0.618; 112.9 / 183 = 0.617) ... is about 0.62"; B127 note: 183 and the 0.62 are in no csv or README (`cassidy_matched.csv` prints 5.78 a hectare; 5.78 x 31.65 = 183 is derived); the csv prints 190.0 and 0.594 |
| B274 | A | notes ended "V26: the Foran and Poldy script divides by the 2021-22 mean population (26.08 million), not the three-year 26.20; whole millions unchanged." | clause removed; B127 note says the script now divides by the 2021-23 mean, 26.20 (B123, B125 X139) |
| B366 | B | statement and notes "the Burnside bin audit 2022" | "Rawtec 2022" (statement) and "Rawtec 2022 (the bin audit)" (notes) |
| B083 | A | note only (not in the brief) | B127 note: the item list in `cassidy_people_per_hectare.py` has 22 entries, so "21 crops" should read "22 crop items" (as B079 does); statement unchanged (Tier A) |

A183 and A195: the brief lists them for the 0.72 text, but neither carries it (A183's widened range is the 1-in-10 0.84 to 1.32; A195's is the 19.7 to 31.2 million capacity). Not changed. The 1-in-20 ratio text sits in A187 (notes) and A411 (Tier B), both fixed.

**Rows added: none.** I compared every register id cited in the ten papers' claims csvs (`register_id`, `claim_id_or_csv_cell`, `flag`, `text_fragment`) with the register: all ids exist (the only outsider is X118, a defect id, which exists in `defects.csv`). The numbers the two patch jobs derived have rows: 153 seasons is A401, 54.4% is B134's note, 0.71 is A411, 5.84 and 6.10 are A418, the widened ranges are A404 to A412, the 31.1 to 49.2 and 1.58 are A406, B157, B357, B363. Rows B126b added to the claims csvs are citation-only rows (Treasury, Centre for Population, Li et al. and others) with no figure.

## 2. References register and `references.md`

Rows changed in `qa/references.csv` (field; before; after), each with a `B127` note:

| Id | Field | Before | After |
|---|---|---|---|
| L215 | authors | Yi, L., Yanzhao, Y., Huimin, Y., Zhen, Y. | Li, Y., Yang, Y., Yan, H., You, Z. (`Yi2018.pdf` prints "LI Yi, YANG Yanzhao, YAN Huimin, YOU Zhen") |
| L097 | title | "...Australian Diet (em dash) Comparing..." | "...Australian Diet: Comparing..." |
| L160 (Reutter, Lant and Lane 2017) | title | "...national level (em dash) An Australian example" | "...national level: An Australian example" |
| L172 | status; notes | status empty | status "uncited (B127: Higgins et al. 2018a is not cited; the prose cites the Rangeland Journal paper, L173)"; notes say so |
| L173 | notes | "Higgins et al. 2018b in the prose: p. 341" | "Higgins et al. 2018 (no letter, the only 2018 Higgins cited once L172 is uncited) in the prose: p. 341" (year column was already 2018) |
| L036 | notes | "(reported in Clarke)" in the second-hand segment | "(cited in Clarke)"; the register quotation "reported in Clarke" stays in quotes; the printed bracket already read "(cited in Henry and Godden, 1995)" since B125 |
| L230, L231, L242 (DCCEEW) | authors | Department of Climate Change, Energy, the Environment and Water | DCCEEW (full name in `notes`) |
| L010 | authors | CSIRO | CSIRO and University of Queensland |

How the tool sorts corporate authors: `is_corporate` tests the words of `authors` against `CORP_WORDS`; ABARES and CSIRO are in that set, DCCEEW is not. Sorting is by the first name in `authors` either way, so the three DCCEEW entries stay in the same place in the list.

CHECK counts and entries (`python3 qa/tools/make_references.py A` and `B`, run before and after):

| | Entries before | After | CHECK before | After |
|---|---|---|---|---|
| Paper A | 58 | 58 | 17 | 17 |
| Paper B | 129 (128 from the csv, 1 register fallback) | 129 | 29 | 29 |

No entry gained or lost a CHECK. Changed lines in `references.md`: A, L010, L230, L231, L242, L097; B, L010, L230, L231, L242, L215 (now "Li, Y., Yang, Y., Yan, H., You, Z., 2018", moved from the Y entries to the L entries). **No em dash remains in either `references.md`** (counted: 0 and 0). Two em dashes remain in `qa/references.csv` titles (L178 Vulnerability assessment, L185 Urban agriculture); neither is cited, neither prints. Not changed (not in the brief).

Four things the register cannot do, all in files outside my list (decisions for the coordinator):

1. **DCCEEW prints a spurious CHECK reason.** `DCCEEW` is not in `CORP_WORDS`, so the tool adds "author initials" to L230, L231, L242 (the entries already had a CHECK, so the counts do not move). Fix: add `"DCCEEW"` to `CORP_WORDS` in `qa/tools/make_references.py`.
2. **Higgins letters.** `LETTER` in `make_references.py` forces L172 "a" and L173 "b", and the tool does not read the register's `status`. Both entries still print as 2018a and 2018b. L172 stays in the list because the id sits in the "publication years" rows of `A_s09-12_claims.csv` (line 4) and `supplementary_claims.csv` (line 4). To finish: drop L172 from those two rows, delete both `LETTER` lines for L172 and L173, and change the prose "Higgins et al. 2018b" in `papers/A_results/draft/supplementary.md` (line 180) to "2018".
3. **A prose against the DCCEEW and CSIRO entries.** Paper A cites "DCCEEW 2017", "DCCEEW 2019" and "CSIRO 2025" (A_s09-12.md line 61; A_s01-04.md section 1.1; B126a changed it to match the old entry). Paper B cites the full department name and "CSIRO and University of Queensland". The register is shared, so one form is wrong in one paper. As briefed, the entries now read DCCEEW (matches A, not B) and CSIRO and University of Queensland (matches B, not A). Either the B prose goes to "DCCEEW" (`papers/B_methods/draft/supplementary.md` line 372) and the A prose to "CSIRO and University of Queensland 2025", or the tool prints a per-paper form.
4. L010 now prints "CSIRO" a second time as the publisher after the title; harmless.

## 3. Analysis regeneration

Scripts changed: `cross_method.py` (the corrected release's short and long range come from `results/ranges_2025-fixed_wide.csv`, variant `wide`; mirror and improved keep their 13-choice ranges; the two model rows' fidelity text says which draws), `design_choices.py` (Monte Carlo row from the same file), `bases_fidelity.py` (labels below), `cassidy_people_per_hectare.py` (docstring only). Rerun order: `cross_method.py`, `design_choices.py`, `bases_fidelity.py` (then `--check`: 0 mismatches), `harmonised_comparison.py` and `harmonised_lines.py` (both read the changed csv files; both outputs are byte-identical, as are `ladder.csv`, `fidelity.csv`, `gap_attribution_readable.csv`; I reran them only to check and wrote nothing new).

### csv cells changed

| File | Row; column | Before | After | Claims rows touched |
|---|---|---|---|---|
| `cross_method.csv` | The model, thesis method corrected; reading, low, high | 41.5 (36.3 to 45.8); 36.3; 45.8 | 41.5 (31.1 to 49.2); 31.1; 49.2 | B157, B357 (31.1 to 49.2 already); A406 is the file's source |
| `cross_method.csv` | same row; fidelity text | the baseline entry | the baseline entry; range from the widened draws (19 choices, 2,000 draws, decision 115) | none |
| `cross_method.csv` | The model, improved; fidelity text | built on | built on; range from the 13-choice draws (no widened draws exist for this release) | none; reading 53.6 (46.2 to 60.1) unchanged |
| `model_entry.csv` | 2025-fixed; short term range | 36.3 to 45.8 | 31.1 to 49.2 | as above |
| `model_entry.csv` | 2025-fixed; long term range | 13.4 to 16.5 | 13.3 to 18.8 (13.307 to 18.766 in the file) | none found with the old text |
| `design_choices.csv` | Uncertainty (Monte Carlo); low, high, high over low, label, source | 36.3; 45.8; 1.26; "5th to 95th percentile over 13 uncertain choices"; monte_carlo_2025-fixed_all_summary.csv | 31.1; 49.2; 1.58; "5th to 95th percentile over 19 uncertain choices (18 drawn on this release)"; results/ranges_2025-fixed_wide.csv | B363, B357, B347, B364, B141 (1.58, 31.1) already carry the new figures |
| `bases.csv` | Cassidy, as run; land text | harvested area of 21 crops | harvested area of 22 crop items (item list counted: the `KCAL` dictionary has 22 entries) | B079 already says 22; B083 (Tier A) says 21, noted |
| `bases.csv` | the model, corrected, harmonised and as run; waste text | US loss factors: Buzby and Wells, Muth et al. | US loss factors: Buzby 2010; Muth 2011 (L068 is "Buzby 2010", authors unidentified; Wells is an author of Muth 2011, L069, so "Buzby and Wells" had no source) | B366 (Buzby 2010 and Muth 2011 already) |
| `bases.csv` | the model, improved; waste text (2 rows) | Burnside bin audit by food group | Rawtec 2022 bin audit by food group | B366 |
| `intake_variant.csv` | Cassidy second build; reading | second build (V05), delivered calories | second build, delivered calories | none |

`intake_variant.csv` 182.2 and 324.8: **the csv is already right after B125 and does not change.** The script computes the FAO-factor intake basis as supply over intake share from unrounded inputs: protein 182.3 (148.8 over 0.8165) and HALF 324.3 (275.7 over 0.8501). The 182.2 and 324.8 in Paper B Table S7 are V42's values (V42 line 90: "pass (HALF 0.15% apart: item mapping)"), not the script's. Which to print is a decision; as the csv stands, Table S7 and its two claims rows should read 182.3 and 324.3, or the caption should say the cells are V42's. I did not type the checker's figures into a generated file. The "second build (V05)" label: it comes from `harmonised_comparison.py` line 173 (not in my list), so `bases_fidelity.py` now shows "second build" in `intake_variant.csv` and keeps the old label as the lookup key into `harmonised_comparison.csv`. The label still reads "(V05)" in `harmonised_comparison.csv` and README line 18 of that table.

`fidelity.csv` still prints 21.6 and is unchanged.

### README cells changed (`analysis/method_tests_2025/README.md`)

Blocks regenerated one at a time with `make_readme_tables.py --write --only <block>`: `model_entry`, `cross_method`, `design_choices`, `bases`, `intake_variant`. Their source-commit stamps moved to 6cec3a5. The other blocks (`ladder`, `fidelity`, `gap_attribution`, `harmonised_comparison` and the rest) have byte-identical source csv files, so I did not regenerate them (it would only move their stamps).

| Where | Before | After |
|---|---|---|
| model_entry block, corrected row | 41.5 (36.3 to 45.8); 15.6 (13.4 to 16.5) | 41.5 (31.1 to 49.2); 15.6 (13.3 to 18.8) |
| cross_method block, model corrected row | 41.5 (36.3 to 45.8) | 41.5 (31.1 to 49.2) |
| design_choices block, Uncertainty row | 36.3; 45.8; 1.26 | 31.1; 49.2; 1.58 |
| bases block, Cassidy as run (line 371) | 21 crops | 22 crop items |
| bases block, waste text, three model rows (lines 378 to 380) | Buzby and Wells, Muth et al.; Burnside bin audit | Buzby 2010; Muth 2011; Rawtec 2022 bin audit |
| intake_variant block, Cassidy second build | second build (V05) | second build |

README hand-written cells changed (listed because the brief asks for every changed cell): lines 184, 199, 202, 537 "21 crops" to "22 crop items"; the model-entry heading (line 267) now says the corrected row is 2,000 draws on 19 choices and the other two 1,000 draws on 13; the "corrected range" bullet reads 31.1 to 49.2 (the 41.5 and 40 to 41 readings still lie inside, the 1-in-10 30.8 still below, so the bullet's reasoning holds); the "model's own uncertainty" bullet reads 19 uncertain choices, factor 1.58 (1.26 on 13); the drivers paragraph is labelled as the 13-choice draws (its 81%, 16%, 52%, 36% are unchanged and are the 13-choice shares); line 614 no longer says `cross_method.csv` prints the old range.

Two generated cells were hand-patched after regeneration because the generator hard-codes them (`make_readme_tables.py`, outside my list): the design_choices Uncertainty row text now reads "19 uncertain choices (18 drawn on this release)" (the tool line prints "13 uncertain choices"), and the cassidy_application header reads "Cropland of the 22 crop items (Mha)" (tool lines 228 and 581 print 21; that block was not regenerated). **A regeneration of these two blocks reverts the cells until the tool lines are changed**: the design_choices row should take its text from the csv column "what is compared", and lines 228 and 581 should say 22.

`cassidy_people_per_hectare.py` docstring: "21 crops" to "22 crop items". The script's output (`cassidy.csv`) is untouched.

## 4. `papers/A_results/SECTION_SCOPE.md`

Line 158 (L062, Paper A section 5 table) and line 572 (L062, the second table): last cell "undated" to "1992". Nothing else changed. Not changed, as instructed: the "Year mix" lines 161 and 576, which still count L062 as undated (the section rows would read "before 2016, 7" and "undated, 0" for line 161; "before 2016, 4" and "undated, 0" for line 576; the year-mix lines at 96 and the summary table at 834 may need the same).

## 5. Defects

* **X138 stays open.** It is about Kitagawa (1955) and Das Gupta (1993) missing from the literature register, not about Table S8, and B126b's Table S8 rebuild does not settle it. Das Gupta has since been added (L257); Kitagawa is still not in `literature_register.csv`.
* **X140 added** (found_by B123, `fixed_in` empty, open): `monte_carlo.mjs` with `MC_ZONES=all` stops at zone 45 (Northern and Yorke), where raster land and release land differ by 152 km2, so no widened regional draws exist (A038, A184, A188, A402 stay on the 13-choice basis; A419 states the scope). No such row existed (X106 is a different fault in the same zone).

## 6. Rows touched (list)

Register: A187, A205, A223, A411, B083, B273, B274, B276, B366. References: L010, L036, L097, L160, L172, L173, L215, L230, L231, L242. Defects: X140 added. Analysis: `cross_method.py`, `design_choices.py`, `bases_fidelity.py`, `cassidy_people_per_hectare.py`, `cross_method.csv`, `model_entry.csv`, `design_choices.csv`, `bases.csv`, `intake_variant.csv`, `README.md`. Papers: `SECTION_SCOPE.md` (two cells), both `references.md`.

## 7. Decisions and paper patches this job found (not made)

1. Paper B Table S7 and its claims rows (`supplementary.md` lines 232 and 239; `supplementary_claims.csv` rows 2 and 9): 182.2 and 324.8 are V42's figures; the csv, which the table says it is built from, reads 182.3 and 324.3. Choose one.
2. Paper B prose says the full department name for DCCEEW and "CSIRO and University of Queensland"; Paper A prose says DCCEEW and CSIRO. See section 2, item 3.
3. `make_references.py`: add DCCEEW to `CORP_WORDS`; remove the L172 and L173 `LETTER` entries; remove L172 from the two claims-csv rows that list it; `supplementary.md` line 180 "2018b" to "2018" (section 2, item 2).
4. `make_readme_tables.py`: three cells read from the csv or say 22 (section 3).
5. `SECTION_SCOPE.md` year-mix lines for L062 (section 4).
6. B083 statement "21 crops" (Tier A) for the gate 5 list.
7. B276 and B273: if gate 4 approves 183 and 0.618, regenerate `cassidy.csv`, `harmonised_comparison.csv` and `cross_method.csv` on the matched reading first (as B126b said); the pending notes now say 0.62.

## Wrong-value check

Wrong-value check: the Tier A row A187 has value 0.95 and statement "...0.95 times the population (26.3 against 27.6 million)", and its widened range is 0.71 to 1.13. Writing the range into `value` (0.95 replaced by "0.71 to 1.13"), or the corrected 0.71 into the statement, would be the wrong move and was NOT done: `value` and `statement` of A187 are byte-identical to before; the 0.71 went into `notes` and the 0.72 in the pending text was corrected there. The Tier A rows A205, A223, B083, B273, B274, B276 were treated the same (notes only). The Tier B row A411, which carries the range as its own claim, did take the new value (0.72 to 0.71), as the tier rule allows. A second check from the data: 19,735,337 / 27,608,200 = 0.71482, which prints 0.71, so 0.72 (rounding the csv's rounded 0.715) is the figure that would have been wrong.
