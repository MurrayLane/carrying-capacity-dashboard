# B143a: patch of Paper A to the blind read V54a

Brief: `qa/briefs/B143a_patch_paper_A_to_V54a.md`. Input: `qa/reports/V54a_read_paper_A.md`. No git, no subagents, no network (one read-only `git status` was run by mistake at the start; nothing else of git was touched). Written only under `papers/A_results/` and this report. `paper_A_draft1.md` is not touched: it is stale until the coordinator reruns `assemble_draft.py A`. `references.md`, the registers, `qa/tools/` and `analysis/` are not touched.

## 1. Word counts

`python3 qa/tools/assemble_draft.py A` and `python3 qa/tools/wordcount.py A` were run on a scratch copy (assemble ran: 4 section files, 4 drafter-notes blocks moved to the appendix, 0 em dashes in the assembled file).

* TOTAL 7,937 (limit 7,950). Sections 1 to 12: 608, 913, 597, 829, 654, 543, 537, 1,089, 838, 461, 198, 670.
* Abstract 247 words (limit 150 to 250), by whitespace count.
* Highlights: 5 bullets, 79, 83, 84, 81 and 85 characters (limit 85).
* To pay for the added sentences, words were cut from sections 5 (the 2011 curve values given in Table 4, the dairy sentence of 5.4 that the supplement carries, the "read for its shape" sentence), 7 (the direction sentences of 7.2 that Table 6 shows by sign), 8, 11 (the store-equals-16-years clause, kept in S6) and the abstract (the preset list and the question).

## 2. Every V54a fail, in its order, with the fix or why it stands

### Number and trace fails (section 4.1)

* **F1 (Table 7, 2011, 1 in 10, sum of regional capacities).** Fixed: 13.7 becomes 13.8. `analysis/paper_a/shocks_2011_on_2025_table.csv`, basis `2011_on_2025_table`, 52 region rows plus zone 60: 13,750,254, which rounds half up to 13.8. Row restated, flag "derived: sums of file cells".
* **F2 (Table 7, 2011, 1 in 100, sum over national).** Fixed: 0.46 becomes 0.47 (7,064,412 / 15,182,401 = 0.4653). Table S14 already printed 0.47 for the thesis-table ratio.
* **F3 (S10, 8.31 MJ).** Fixed: 8.30 MJ (file 8.3020, ratio 1.0377; V52 line 205).
* **F4 (S10, 3.8% below).** Fixed: 8.0 MJ is 3.6% below the mean (8.0 / 8.3020 = 0.9636). New sentence: "The mean requirement of the 2010 population at the NHMRC reference body weights, 8.30 MJ a day (8.04 to 8.40 on other adult body sizes), is 1.038 times the model's fixed 8.0 MJ, which is 3.6% below it". Row flagged derived.
* **F5 (7.3 "Avon and four others").** Fixed: "South Coast WA, Avon and three others had four to eight times". From `analysis/paper_a/long_term_regions.csv` (2025-fixed region rows, capacity_long over population): 8.07, 7.27, 7.11, 6.10, 4.60; the next is 3.86. Row cites the file and is flagged derived.
* **F6 (33 and 28 million).** Row path fixed to `analysis/paper_a/meat_balance_identity.csv` for the 1.57, 1.51, 1.50 and 1.49. The 33 and 28 million (33.4 and 28.1 in S10) are in no data file: they now have their own rows, marked "derived (checker value)", citing V51 section 2 line 46 and the evaluator inputs it names. The sentences stand.
* **F7 (Table S13).** Row now cites `analysis/resilience_2025/drought_factor_variants.csv` (all 24 cells), with V51 sections 2 and 3.
* **F8 (1.54 to 1.65).** Fixed in section 2: "1.51 to 1.65 times the population (1.54 to 1.65 on the production windows; 1.58 on the livestock window)". The 1.51 is the fuel window (1.5148) that Table 1 lists. Row cites the column `capacity_over_population_at_midpoint_2025_short`.
* **F9 to F12 (Bolleter p. 123; Poore and Nemecek p. 990; ABARES 2026b p. 5 and 2026a p. 2; Lane 2014 p. 3).** Live rows restored, each with its register id and page (L146 p. 123; L115 p. 990, with L116 and L117 for the same sentence; L234 p. 5; L241 p. 2; L020 p. 3). Checked afterwards: every reference-list entry that the prose cites has a live row; the only entries with none are L216 (Cottrell et al.) and L246 (FAOSTAT 2025), both uncited (section 4 below).
* **F13 (Avon 15,950 and 25,379 km2).** Rows restored with km2: V37 section 4 gives 1,594,996 ha and 2,537,931 ha; dividing by 100 gives 15,949.96 and 25,379.31. Flagged as a unit conversion.
* **F14 (S1: 42 and 31 regions, 7 and 20; 4, 6, 2, 2).** New rows citing `analysis/comparison_2025/decomposition_eight_layer_regional_counts.csv` and V51 line 35 (and the nine-layer counts, 7, 2, 3, 1). The two walk-count sentences in S1 are now one passage (see logic 11 and consistency 11).
* **F15 (5.3 million in 14 years).** New row: derived, 27,608,200 less 22,336,514 = 5,271,686.
* **F16 (stale live rows).** Retired: "3,16 Three are not robust" (A038 on 13 choices); "3, Table 1, Short term: 2 clean and robust" and every other old "Table 1" row (the table is now Table 2, covered by the B141a row 209); "4, Table 2 People over capacity 0.670 / 1.454" and the whole old nine-layer "Table 2" block (Table S12 carries it); "10,6 48,520"; "10,20 5th percentile 174,487"; the old "10, Table 7 rows 2 to 8" with the 13-choice ranges (replaced by seven new Table 8 rows from `regions_in_depth.csv` and `ranges_2025-fixed_wide_zones.csv`); "12,22 0.670 to 0.665"; "12,25 two short-term flips pass"; and "8,24 Mackay Whitsunday is a clean and robust flip", which contradicted the text.
* **F17 (Table S16, 14.54 and 13.30).** Stands. The draft prints the checker's values (V52 lines 65 and 68: 14.543, 13.304); the builder file `analysis/paper_a/window_subsets_2011.csv` gives 14,562,798 and 13,305,083 (14.56 and 13.31), and the crops-only columns are in V52 section 2 only. Tolerance rule: the checker's value is taken. The row says so and is flagged for the analysis job (section 5).
* **F18 (179 to 182 of 200).** Fixed in wording: "about 180 of the 200 random groupings keep more than the states do" in 5.3 and S2. The file prints 19 below the real states (181 above); V52 gives 179 and 182 on its two seeds. Row cites both.

### Checker-wording fails (section 5)

* **W1** The abstract, highlight 2 and the conclusions now say "the consumption and red-meat-mix layers"; the gloss "the diet with less beef" is removed from section 4.
* **W2** Abstract, highlight 3 and conclusion 3 say "crops and grain-fed animals only, 41.2 million".
* **W3** Abstract and conclusion 1 give 39.1 million with 39.7 on unrounded inputs.
* **W4** S10 as F3 and F4.
* **W5** Section 9.1: "Other range ends rest on the author's judgement too: the low ends of the meat-and-egg share (0.115) and the red-meat share (0.528), the equal weight on the leave-one-out resilience table, and the low end of the long-term feeding benchmark (0.30, no effect on the corrected method)." The paragraph above it already names the land-source and energy-level judgements, so no count is stated. OUTLINE.md and SECTION_SCOPE.md no longer say "five".
* **W6** S4: the avoidable-waste comparison (1.33) is dropped; the span of the land available (1.09) stays.
* **W7** S4: "with a fifty-fifty choice of resilience table added at the shock the ranges are 22.5 to 35.9 and 19.1 to 30.5 million".
* **W8** Section 2: "differed from the ABS figure by more than 10% of that figure in 24 of the 53 regions".
* **W9** Section 3 now carries "(shares that depend on the equal chances given to the two land sources; section 9)".
* **W10** Section 8.1: "(on the leave-one-out reference one variant, 27.4 million, falls 0.6% below it)". Row cites V51 line 65 (no data file).

### Tier A rows (section 6): register job, listed in section 4 below.

### Logic and consistency (section 7)

* **1** Abstract: "none is both robust across 19 sampled choices and free of an artefact flag (SA Arid Lands keeps its status across the range and fails only on the land-definition flag); one long-term flip passes both".
* **2** Conclusion 3: "at 1 in 10 and at 1 in 20 the range across the 19 choices contains the population". Row records the 1-in-100 range, 31.1 to 49.2 million times 0.456 = 14.2 to 22.4 million, wholly below 27.6 (derived, not printed).
* **3** 7.3 "Avon and three others" (F5).
* **4** Abstract: "37% of the national figure on state yields (54% on own yields)".
* **5** Abstract: "covers 57% of the 2025 population; weather and fuel settings explain most of the shortfall".
* **6** 9.1: "Long-term capacity changed little".
* **7** 8.1: "Neither bound is preferred; a drought's effect on pasture-fed output lies between them."
* **8** Section 8.1 caveat added (W10).
* **9** Section 2 (F8).
* **10** S10 (F3, F4).
* **11** S1: "On nine layers, with land and livestock apart, the forward walk differs in 7 and 2 regions and the reverse walk in 3 and 1" follows the eight-layer counts.
* **12** Table S1 note "Table 6"; S2 and S5 "Table 8".
* **13** "(Figure 5)" in 7.3 and "(Figure 6)" in 8.2. All eight figures and all 25 tables are now cited and resolve (checked by script: every Table N, Table SN, Figure N and Supplementary Section SN cited exists, and every one is cited).
* **14** North Tasmania "14%" in sections 3 and 10 (13.5% in the claims row).
* **15** Section 4 and S10: "3.64 million km2 (mean of four years to 2009-10)", from `reference_periods.csv` (pasture window of four years).
* **16** S2: "On the national yield vector the SA4s, at 54%" (`analysis/scale_curve_2025/README.md` line 45; Table S6 prints 58% and 80% on the other bases).
* **17** As F18.
* **18** Stray comma removed.
* **19** One term, "choices", for the sampled settings and data choices (abstract, 5.x, 8.1, conclusions). "Settings" is kept for the preset's own settings.
* **20** "not as the NRM regions of 2025".
* **21** Stands, text unchanged. The model parameter is irrigated area over all farmland (`analysis/irrigation_review/README.md`; R05a (d) point 9), so "irrigated share of all farmland" in Table 9 and 12.3 is right. The label "Irrigated share of cropland" in `analysis/paper_a/measures.csv` comes from `long_term_and_measures.mjs` line 55 and is the wrong one; it is listed for the analysis job.

### References and journal checks (section 8)

* Word count and abstract: see section 1.
* **Keywords: 7, left and flagged.** `papers/DECLARATIONS.md` says no copy of Population and Environment's guidelines is held, and `papers/B_methods/JOURNAL_REQUIREMENTS.md` (1 to 7) is for the other journal. The author should check https://link.springer.com/journal/11111/submission-guidelines (Springer's usual instruction is 4 to 6).
* Em dashes: none in any file I wrote (grep over the section files, supplement, highlights, csvs, OUTLINE and SECTION_SCOPE).
* "today's": removed (consistency 20). No "current" or "latest" remains undated.
* "CSIRO 2025" now reads "CSIRO and University of Queensland 2025", as the entry prints (references.md is now in Springer form: "CSIRO and University of Queensland (2025)").
* Corporate authors otherwise already match the entries (Treasury, Centre for Population, House of Representatives Standing Committee on Agriculture, PMSEIC, DCCEEW, Productivity Commission, Geoscience Australia and ABARE).
* "Saltelli (2010)" becomes "Saltelli et al. (2010)" (Table S8 caption); a live row now carries L247 and L248.
* **Not applicable to Paper A, checked:** Beltran-Peña 2020, the Borrie 1975 inquiry, Muth et al. 2011 and the Schön and Böhringer entry are not cited in Paper A and are in none of its lists; "evaluator", "PAL", "DSE" and "share closed" do not occur in Paper A. No "Name Year" sentence subject occurs in Paper A (script over all four text files).

### Reader's test (section 9)

All three sentences added: the 13-choice set (section 2: "An earlier set of 13 of them, without the land source, the energy requirement and four other data choices, is kept for comparison in Supplementary Section S4"); the forward and reverse walks (section 4: the eight layers in order, and "in reverse (the opposite order)"); the 2066 and 2068 years (8.1: "Extending the slope of each projection's last printed segment, the Intergenerational Report would reach it in 2066 and the Population Statement in 2068"). The Table 3 caption no longer says "release chain". Also added from the brief: the thesis-error clause in footnote 1 ("ERRATA.md in the repository lists ten errors ...; this paper corrects the biodiesel yield, which counted a seed's oil content twice (error 1), the beef carcase-to-retail yield of 1.0 (error 2) and the 2011 populations (errors 6 and 8 to 10)"), and SA2, SA3, SA4 and NRM defined at first use (abstract, 1.2, section 2, section 5).

## 3. Claims csvs, flagged rows, internal labels

* **Rows:** A_s01-04 217 to 148; A_s05-08 182 to 158; A_s09-12 158 to 125; supplementary 302 to 311; highlights 5 to 5; declarations 4 to 4. All 209 rows that carried "superseded by B141a" were either restated (text and file updated to the current sentence or table row, flag cleared) or retired (the text is gone, or a live row already covers it). No "superseded" flag remains.
* **Table rows** of Tables 4 to 7 were renumbered (3 to 4, 4 to 5, 5 to 6, 6 to 7) and each fragment reset to the current table row. The 2011 rows of Table 7 now cite `shocks_2011_on_2025_table_summary.csv` and `shocks_2011_on_2025_table.csv`, not the thesis-table file.
* **Flags:** the strings "restate or retire", "open" and "register-change" do not occur in any Paper A csv. "[gate 4]" and "[gate 5]" are now "gate 5 approved 2026-11-18" (decisions 121 and 132; `qa/GATES.md`). The remaining flags are informative: "new row for the register job", "unchecked row", "derived ...", "unverified (A317, X118)", and the four declarations "unfilled" rows (the author's).
* **Internal labels:** none in the prose or captions (grep for B-numbers, V-numbers, R-numbers, decision numbers, A/L ids, "register", "checker", [CHECK]: only "sources register" in the Table S11 caption). They live in the csvs.
* **Supplementary table order: not renumbered.** The claims register (`qa/claims_register.csv`) and several reports cite Table S numbers, so a renumber by script over the four files and the csvs would break the register, which is B142's to edit now. Left as is. Every Table S reference resolves.

## 4. Register job's list

**The 5 Tier A rows V54a names (draft value against register value):**

| Row | Register value | Draft prints | Supporting report and checker |
|---|---|---|---|
| A036 | 2 (Mackay Whitsunday; North Tasmania clean and robust) | 0 of the 8 short-term flips are both robust and free of an artefact flag; Table 2 short term 0 | B132 sections 3 and 4; V47 comparison table |
| A038 | 2 (herd-cycle) or 3 (13-choice) not robust | 7 do not keep their 2025 status; Table 2 short term 7 | B132; V47 |
| A184 | 21 (21 to 22 across the range) | 19 and 26 regions at the 95th and 5th percentile; 21 to 24 in a single draw (median 23) | B132; V47 |
| A196 | 0.89 (2011); 0.95 (2025) | 0.89 on the thesis table, 0.95 on the 2025 table; Table 7 0.95 | B133 section 1; V48 section 4 (0.946, 0.894, 0.953) |
| A009 | "15.35 and 15.6 within 13.3 to 18.8" | "not established: 26% of paired draws fall" | B133; V48 |

Also moved: A328 (Tier B) prints 23.7%, the draft 23.6% (B138, V52); A220 (Tier A) same value, but the draft states the corrected release with the store table.

**Seven listed but uncited references:** Cottrell et al. 2019 (L216); FAOSTAT 2025 (L246); Higgins et al. 2018a (L172); Kastner et al. 2012 (L080); Khorsandi et al. 2022 (L073); Khorsandi et al. 2023 (L074); Summerhayes and Baker 2026a (L150). Consequence: the prose still cites "Higgins et al. 2018b" (S6) and "Summerhayes and Baker 2026b" (1.3); once the a-entries are dropped, the b suffixes should go and those two citations change to "2018" and "2026". I did not change them, so the prose matches the list as it stands.

**Entries:** CSIRO and University of Queensland 2025 (L010): the prose now cites it as the entry prints; keep the entry in that form or change both together. ABARE 2010 (L053): the entry had no title (references.md now shows "Australian commodity statistics 2010"); S10 cites it for p. 25 note a and the claims row now carries L053 with that page; confirm the title and place against the source. The declarations still carry [CONFIRM] markers and references.md still carries [CHECK] markers (author's).

**Register rows:** the new rows marked "new row for the register job" in the five csvs (about 60) need register ids; the restated rows keep their ids.

## 5. For other jobs (not done here)

* `analysis/paper_a/measures.csv` and `long_term_and_measures.mjs` line 55: label "Irrigated share of cropland" should read all farmland (consistency 21).
* F17: reconcile `window_subsets_2011.csv` (14.56, 13.31) with V52 (14.543, 13.304) and put the crops-only columns of Table S16 in a data file.
* F18: the builder file prints 181; the paper now says "about 180".
* 33.4 and 28.1 million (meat balance at the model's own requirement), and the leave-one-out 27.4 million: no data file prints them (V51 only); the analysis job could add them to `meat_balance_identity.csv` and `drought_factor_variants.csv`.
* `qa/tools/assemble_draft.py`: the assembled header still says sentences marked [gate 4] await Murray's gate 4 approval; gate 4 lapsed into gate 5, approved 2026-11-18.
* `paper_A_draft1.md` must be reassembled from the patched section files.

## 6. Wrong-value check

Example, marked as such (the paper itself carries the corrected value): Table 7, 2011, 1 in 10, sum of regional capacities, was printed 13.7 before this patch. Left at that value, the check against the file sum catches it: `shocks_2011_on_2025_table.csv`, 52 region rows plus zone 60 = 13,750,254, which rounds half up to 13.8, not 13.7. The second cell, sum over national at 1 in 100, printed 0.46 against 7,064,412 / 15,182,401 = 0.4653, which prints 0.47. The check can fail, and it did on both.

## 7. Changed files

* `papers/A_results/draft/A_s01-04.md`, `A_s05-08.md`, `A_s09-12.md`
* `papers/A_results/draft/supplementary.md`, `highlights.md`
* `papers/A_results/draft/A_s01-04_claims.csv`, `A_s05-08_claims.csv`, `A_s09-12_claims.csv`, `supplementary_claims.csv`, `highlights_claims.csv`
* `papers/A_results/OUTLINE.md`, `papers/A_results/SECTION_SCOPE.md` (the "five range ends" statement)
* `qa/reports/B143a_patch_paper_A_to_V54a.md` (this report)

Not changed: `A_s13_declarations.md` and its csv, `references.md`, `paper_A_draft1.md`, `DISCUSSION_MEASURES.md`.
