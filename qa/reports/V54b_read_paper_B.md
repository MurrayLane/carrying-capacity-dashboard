# V54b: blind read of the Paper B draft after the second-round patch

Brief: `qa/briefs/V54b_read_paper_B.md` (its heading says V45b; the file name and my instructions say V54b, so this report is V54b). No git, no subagents, no network. The only repository file written is this report. My scripts are in the session scratch folder `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/tr/` (`trace.py`, `run.py`, `strict.py`, `tab.py`, `table.py`), not in the repository. I read the whole of `paper_B_draft1.md` (to the end of the declarations), `supplementary.md`, `highlights.md` and `references.md` before writing anything. I did not open the earlier reader report `V45b_read_paper_B.md`, so as to stay blind to it.

## Tolerance

Exact for every printed number: a printed number passes when a value in the file the claims row names, rounded to the printed number of decimals, equals it (so 41.5035 in a file supports a printed 41.5, and 41.3 in a file fails a printed 41.1). The sign is compared separately by hand where it matters. Shares were accepted either as percentages or as fractions (0.215 supports 21.5%), and millions either as millions or as people (41,503,537 supports 41.5). Years, page numbers, section, table, figure, item and purpose numbers, and QA identifiers (B, V, L, D numbers) were not traced as numbers. Highlights have no claims csv, so each highlight number is a fail by the brief's rule.

Limit of the method: the match is automatic over every number, and a match is accepted from any file the row names (or the register row, or the literature register row it names). Small integers and common values can therefore pass by coincidence. To catch that, I ran three stricter passes: (i) every cell of Tables 3 to 8 and S1 to S14 against the csv its caption names, (ii) every pass that came only from a QA report re-checked against the csv the same row names, and (iii) the arithmetic of every ratio, factor and share in Tables 4 to 8, S1, S6 and S13 recomputed from the printed figures. Those passes found the stale values listed under "file disagrees".

## Wrong-value example (EXAMPLE only)

I fed my file check the Table 7 panel A short-term reading of variant 1 deliberately misread as 81.07 in place of the printed 81.70. Against `analysis/pasture_2025/pairing_relaxed.csv` it returned no match (`81.07 None`); with the printed value it matched the cell `81.70` (line 3, `2025-fixed,1,short,81.70`).

## Counts

* Numbers traced: 2,482 (2,475 occurrences in the main text, abstract, tables and supplement, plus 7 in the highlights).
* Pass: 2,369.
* Fail: 113. Of these, 88 have no claims row (81 in the text, 7 in the highlights), 10 have a row whose named file does not print the number, and 15 are printed with a value the named file contradicts or does not hold.
* Claims rows still flagged in the csvs: 199 rows carry "[B141b: fragment no longer in the text as worded; restate or retire]", "[open: Q8/Q9]", "[gate 4]" or "[register row to add or change]" (B_s01-03 26, B_s04-05 68, B_s06-09 72, supplementary 33). Several draft sentences rest on replacement B141b rows while the stale row sits beside them; the stale rows should be retired so that the csv carries one row a number.

## Fails, the most serious first

### Values the named file contradicts (15)

1. **Table S7, commodity balance rows, all nine cells.** The table prints meat 41.1 (0.99), 48.1 (1.16), 58.1 (1.4); fish 12.0 (0.29), 19.7 (0.47), 17.9 (0.43); grain with embodied feed grain 126.6 (3.05), 137.2 (3.31), 138.1 (3.33). `analysis/method_tests_2025/intake_variant.csv` (lines 14 to 16), which the caption names, prints meat 41.3, 48.3, 58.4 (1.41); fish 12.1, 19.8 (0.48), 18.0; grain 126.8, 137.3, 138.2. The printed values are the ones in V42's table (line 55), from before the csv was regenerated. The Table 5 note ("Table S7, which carries 126.6") carries the same stale value. Fix: retype the three rows from the csv and change the Table 5 note to 126.8.
2. **Table S5 and section S3.8, Foran and Poldy head count.** The supplement prints "the 2021-22 mean, 26.08 million" (S3.8) and, in Table S5, "the actual-use reading divides FAO food use by the 2021-22 mean head count (26.08 million)" and "(the method script; under 0.5% from the three-year 26.20) (26.08 million)". `analysis/method_tests_2025/bases.csv` (the Foran and Poldy rows) says "the 2021-23 mean head count" and 26.2. This is the cause of item 1: the commodity balance was rerun on 26.2. Fix: regenerate Table S5 from `bases.csv` and drop the 26.08 clause in S3.8.
3. **Table S8, binding land type row.** The caption says "every cell is read from the file as the file stands", but `cross_method_local.csv` has no binding-type row with multiples; the 1.30 to 1.88 and 1.01 to 1.45 are arithmetic (53.9/41.5 = 1.30, 77.9/41.5 = 1.88, 53.9/53.6 = 1.01, 77.9/53.6 = 1.45), true but not printed there. Fix: name `harmonised_robustness_footprint.csv` and section S3.11 as the source of that row, or drop "every cell" from the caption.

### A row whose named file does not print the number (10)

| Number | Where | Row | File named | What is wrong |
|---|---|---|---|---|
| 14.75 MJ | Table 7 note (main line 284) | 5/B141b-1 | `bases.csv` | the csv prints 3,525 kcal; 14.75 is the conversion; `README_round2_B139.md` prints 14.75 but the row does not name it |
| 34.5 | 7.6 (line 438), 9.1 (line 484) | 7/B141b-12 | "as 5.14 rows" | no file named; the value traces through 5/B141b rows to `bridge_half_to_model.csv` (-34.46) |
| 28, 46, 87, 10, 16 | 9.1 (line 484) | 9/B141b-15 | "as 5.11 rows" | no file named; values trace through the 5.11 rows to `harmonised_robustness.csv`, V50 and `harmonised_line_c.csv` |
| 40.4 | 9.2 (line 488) | 9/B141b-16 | "as 6.10" | no file named; `drought_bounds_paper_B.csv` prints 40449636 |
| 331.87 | Table S11 land row (supp line 329) | S3/B141b-16 | `production_comparison_2025.csv` | that csv does not print the pasture area; `bases.csv` does |

### No claims row (88)

Grouped; the values are mostly right, but by the brief's rule each is a fail until a row exists.

* **Highlights (7 numbers):** 9 and 100 (highlight 1), 1.6 and 2.8 (3), 18.9, 40.4 and 55.3 (5). There is no `highlights_claims.csv` for Paper B (Paper A has one). The values match body rows (abstract rows B005, B141b-9, B141b-10; 5/B141b-13 and Table S8).
* **Unit conversions:** 11.3 MJ (4.6, 5.6), 10.7 MJ (4.10), 8.0 MJ (5.11 paragraph on line (c), twice); the old rows 4/27 and 4/41 are flagged "restate or retire".
* **6.6:** the Jones committee's "30 to 35 million" (row only in section 1).
* **S2.4:** "some 40 million people outside Australia (p. 15)" (the row is in B_s04-05, 4/17, flagged stale).
* **S2.9:** Gerten's "2,355 kcal" (the literature register L-row prints it; no supplementary row).
* **S3.6:** the every-yield companions 37.0, 30.8, 26.3, 22.9, 18.9 and the return periods (100, four times); `drought_bounds_paper_B.csv` prints 37033233, 30810607, 26324116, 22924562, 18918184, so only the row is missing.
* **S3.7:** 396.1 Mha and the adjustment 1.129 in the prose (Table S1 rows cover the table, not the prose; the main-text row 5/66 is flagged stale).
* **S3.11:** "-4% ... 46%" (line 263); the whole paragraph on line (b) dependence (27.7, 45.9, 10.5, 87, 35.8); the line (c) clauses 14.75, 1.10, 7.376, 0.62, 31.0, 2,892 and 1,912 (row B141b-14 covers 1.512, 0.8202, 303 kg and the shares only); the nine-variant sentence (3.2, 23.6, 27.7, 45.9, 12.5, 39.7, 9.4, 35.5; printed in `README_round2_B139.md`).
* **S3.12:** 46 items, 13.60 MJ, 41.5035, 75.97, 5,040, -34.46, the six-switch shares (-48%, 64%), 4.9%, k = 4.01, 93.1 g, 1.61, 0.33, and the line (c) note's 7.376, 13.60, 14.75 and 1.84 (row B141b-15 covers the six-switch values and k = 91.3 and 145.6 only). All are in `bridge_half_to_model.csv`, `README_round2_B139.md` or V53.
* **S3.14:** 44.1, 40.7, the cattle tonnages 3.00, 2.26 and 2.01 Mt, and the by-item line (24.8, 23.5, 35.9, 60.4, -4.5, -10.9, -4.8, 9.7, -1.3); `production_window_10y.csv` and the V53 appendix print them; row B141b-17 lists only the table values and factors.
* **S4:** 5.33 and 6.68 ha in the prose (Table S2 has them; the prose row B141b-18 stops at 4.58).
* **S7:** "9 to 100 million" in the purpose list.
* **S8:** the export energy count (2,100 kcal; 87 to 128; 184 to 264) and Fearnside's 23,600 ha; their rows are in B_s06-09 (6/5, 7/15), flagged "restate or retire", and the supplementary csv has none.

## Checker-wording check (step 2)

I compared every sentence whose row names B110 to B141b with the checker reports V36 to V53 and their appendices.

Places where the draft keeps the builder's wording or value against the checker:

1. **Table S7 and Table S5 against V42 / the regenerated csvs** (above): the draft keeps values the checked csv no longer prints. This is the reverse case (V42's value, the csv moved after it) and needs either a new check of the rerun or the old values restored in the csv.
2. **V50 on the highlight:** V50 asks that the "close most of their gap" highlight say it holds under the own-productivity classification. Highlight 2 begins "If productivity is an input", which meets it. Pass.
3. **V53, diet A:** V53 passes 1.60 "at the edge" (1.593 unrounded). Section 6.11 ranks the Monte Carlo's 1.58 below diet A (1.60); on unrounded figures 1.583 against 1.593 the order holds. Pass, but the margin is a hundredth.

Places that follow the checker (pass): line (c) names the grain exception (x1.10), applies the loss factors to the food balance mix, says the spread is wider than on line (b) and carries the 10% to 16% band (V53 items 1 and 2); the bridge keeps the two games apart, gives the diet as 22.6, notes 7.376 against 8.0 MJ and states the dairy condition on 85.4 and 92.4 (V53 appendix); the production-window sentence carries the proxy caveat and the record 2024-25 cattle year (V53 appendix); meat inputs "could not be compared" (V53 item 6); "most of it" and "about 87%" in place of "almost all" (V50); -1% to 8% in place of -1% to 7%, and 5% to 36% (9% to 36% without the scale-up) to the median (V50 item 4); "spread of method centres" for the third (V39); variant 1 stated with its 93% to build 3 (V40); "19 settings, 18 of which vary" (V41); intake tops 10.9 and 12.9 (V42); the footprint's counterfactual as 146 to 343, not 134 to 343 (V44 and B141b); pasture output as an illustration, not a bound, and "short term" on the failure probability (V49 items 1, 2 and 4); "almost all" for the short-term drought fall (V38, V49 item 3, with 93% to 98% in S3.6).

## Tier A pending sentences (step 3)

Register rows at Tier A whose register value or statement differs from what the draft prints. The round-two values are not yet in `qa/claims_register.csv`.

| Register row (Tier A) | Register holds | Draft prints, and where | Supported by |
|---|---|---|---|
| B276 | 4% (line a); 39% (line b) | abstract and section 1: "-1% to 8% across references" and "28% to 46%"; 5.11: 4.1% and 38.5% base, -1% to 8% and 28% to 46% across variants; 9.1 the same; line (c) 14.7% (10% to 16%) in abstract, 5.11, 9.1, Table 6 | B135, checked V50 (`harmonised_robustness.csv`, Table S13); B139, checked V53 (`harmonised_line_c.csv`) |
| B277 | spread narrows by about a third (0.65 to 0.44) | 5.11 and 9.1 add "which depends on the commodity balance" (widens 12% without it; 23% to 48% with any other method out) and the line (c) 0.65 to 0.48 | B135, checked V50; B139, checked V53 |
| B156 | 65 to 211 (primary); 133.8 to 343.4 (secondary) | abstract and 5.10: counterfactual "146 to 343" (footprint) and HALF 276, "about 3.5 to 8 times" | B046 (146.2 to 343.4), Table S8; B123, checked V44; B141b |
| B003 | 18.9 to 55.3 as a span | abstract, 6.10, 9.2, highlight 5: two one-at-a-time changes, with 40.4 on crops only and 62.9 improved; "not a joint range" | B134, checked V49 (`drought_bounds_paper_B.csv` 40,449,636); decision 146 as cited in the row |
| B194 | land matters least (1.09, the smallest factor) | 6.11 and Table 8 panel A: the crop-only drought bound (1.03) and the land base (1.09) move it least | B134, checked V49; B139, checked V53 ("B194 holds ... 1.03 the crop-only bound") |
| B187 | 1.58 (2.22 from minimum to maximum) | abstract and 9.2 drop the 2.22 | B141b (row 9/B141b-16 "the 2.22 sentence is dropped"); value 1.58 unchanged |
| B005 | 9.4 to 100 (a factor of 10.6) | 6.10 gives 9.4 to 100 without the 10.6; the ladder rows B189 to B192 (Tier A) are no longer in the paper | B141b; row 6/50 still carries 10.6, flagged stale |
| B130 | 5.8 to 6.1 on the corrected method | 5.8 adds "short-term" and "below 1% on crops alone" | B134, checked V49 |
| B137 | 18.92 to 41.5 | 5.8, Tables 3 to 5 add 41.2 and 40.4 on crops only | B134, checked V49 |

## Logic fails (step 4), with a suggested rewrite

1. **Abstract, section 1 and 9.1: the two lines are given ranges on different bases.** Line (a) is "-1% to 8% across references" (Table S13 row "to the model at 31.1, 41.5, 49.2 and 53.6": -1.2% to 7.8%), but line (b) is "28% to 46%", which is Table S13's range to 41.5 only; on the same references line (b) is 23.2% to 52.8%. The reader compares two ranges that are not alike. Rewrite: "With productivity part of the method, equalising closes about none of the distance to the model (-1% to 7% across variants, -1% to 8% across model references); as an input, it closes 28% to 46% across variants (23% to 53% across model references), most of it the footprint and HALF."
2. **5.10, last sentence:** "its 1-in-10 point, 30.8 million (41.2 on crops only), lies just below the corrected range of 31.1 to 49.2 million". The 41.2 is not below the range. Rewrite: "its 1-in-10 point with the factor on every yield, 30.8 million, lies just below the corrected range of 31.1 to 49.2 million; with the factor on crops only it is 41.2, inside it."
3. **7.3:** "one model run under the choices of section 6 spans 15.5 to 62.9 million". Section 6 and Table 8 panel A also run the model at 103.3 (guideline 5%), 202.1 (diet B) and 422.3 (diet C). Rewrite: "one model run under the choices of section 6 spans 15.5 to 62.9 million on the default diet (to 202.1 with optimised diet B), and a proportional count of exports reaches the published 100 million."
4. **Abstract and highlight 4 against the body:** the abstract says the bridge "finds the pasture-crop pairing one of several causes of the gap"; the body (5.14, 7.6, 9.1) says "a sufficient cause of the gap, not shown to be the only one", and the bridge has no switch called the pairing (its nearest is the pool rule, 18% of the gap). "One of several causes" says the bridge identifies the pairing as a cause; it attributes 18% to the pool rule. Rewrite (abstract): "A bridge from HALF to the model spreads the gap over seven features, the pool rule that stands for the pasture-crop pairing taking 18%; relaxing the pairing alone is enough to close the gap." Highlight 4 (77 characters is fine): "The pasture-crop pairing is enough to close the gap to HALF, but not the only cause" (83 characters).
5. **6.10:** "The spread across the settings varied together is narrower than the span between the two ends" sits beside "two changes in opposite directions, not a joint range". Comparing a joint 5th to 95th spread with a span the same paragraph says is not a joint range claims more than it shows. Rewrite: "The spread across the settings varied together (a factor of 1.58) is smaller than the drought allowance alone (2.19) and larger than waste alone (1.33)."
6. **5.4 and Table 3:** "Crop land for feed is 21.6% high on the thesis rates (not reproduced), though builds 1 and 2 come within 4%". The grade rule says a component is graded on the authors' printed inputs where one exists; that is applied, but a reader sees "within 4%" and "not reproduced" side by side. Add "graded on the printed rates" after "not reproduced". Minor.

"Every ordering" (5.14) is supported: 5,040 = 7! orderings, averaged exactly (V53). "The same" claims: none found that hide a difference.

Abstract against body: everything in the abstract is in the body; the abstract's "-1% to 8%" and "28% to 46%" issue is item 1.

Highlights, counted by script: 76, 84, 82, 77, 77 characters; five highlights, all at most 85. They match the body except highlight 4 (item 4 above).

## Consistency fails (step 5), with a suggested rewrite

1. **Table S7 against the csv and Table 5 note against Table S7:** see the stale-value fails (126.6 against 126.8).
2. **Table 3 against Table 1, commodity balance:** Table 3's fidelity cell says "the 30 and 77 readings are derived here"; Table 1 and 5.7 give "30 to 32 (meat) and 76 to 80 (grain with feed grain)". Rewrite Table 3's cell: "the 30 to 32 and 76 to 80 readings of Table 1 are derived here".
3. **Table 2 and Figures 1 to 3 do not exist.** Section 4 cites Table 2 and Figure 1, 5.10 Figure 2, section 6 Figure 3; all four are placeholders ("not built", "no plotting script"). The placeholders agree with each other and with the drafter notes, but a submitted paper cites tables and figures that are missing.
4. **Supplementary table order.** Tables appear as S1, S10, S5, S6, S7, S13, S14, S8, S11, S12, S2, S3a, S3, S4, S9; the journal numbers supplementary tables in order of first citation. Renumber.
5. **S3.4 against S3.7:** "people a hectare run 22% to 42% above" (S3.4, Table S6) and "Cassidy's rows (22% to 37%)" (S3.7) are both right for their own sets (Table S6 all rows; Table S1 the rows attributed), but read as one quantity. Add "in Table S1" after "Cassidy's rows".
6. **Main text Table 3 caption and Table 5 caption:** the crops-only 41.2 and 40.4 in Table 5's failure-view row come from `drought_bounds_paper_B.csv`, which Table 3's caption names and Table 5's does not. Add the file to Table 5's caption.
7. **Internal labels in the paper:** Table 6 caption, Table 7 note, Table 8 caption, S3.6, S3.11, S3.12, S3.13, S3.14, S5 and S7 print "B139, checked V53", "B134, checked V49", "B135, checked V50", "V19", "decision 113". These are repository identifiers a referee cannot use. Move them to the claims csvs.

Table numbers cited in prose: Table 7 panel B is the bridge and Table 8 has three panels, as B141b made them; S-tables run to S14 with S3a; every cited table exists except Table 2. Pass otherwise.

"Not seen" and "reported in" do not appear in the prose (grep of the main text to the declarations and of the supplement). Pass.

### Citations and references

* **Cited in the prose but not matched in `references.md`:**
  * "National Population Inquiry 1975 (Borrie)" in Table 1 has no entry. Taylor 1922 and National Population Council 1992, also second-hand through the Jones committee, do have entries.
  * "Schön and Böhringer 2023" (S2.6) against the entry "Schon, Bohringer, 2023": the entry lacks the umlauts and the initials.
* **Author-date form that does not match its entry:**
  * "Saltelli (2010)" (S5) should be "Saltelli et al. (2010)".
  * "Muth 2011" (Table S5 and Table S3a) should be "Muth et al. 2011", as in 8.5.
  * "ABS 2011" (Table S3a) cites an entry headed "Australian Bureau of Statistics, 2011", while "ABS, 1994" is headed "ABS". Use one author form.
  * "FIAL 2021" (Tables S3a and S5) cites the entry "Food Innovation Australia Limited, 2021".
  * "NHMRC" (Table S3a, Table 8) has no year; the entry is National Health and Medical Research Council 2006.
  * "USDA Handbook 697" (8.5) has no year; the entry is USDA 1992.
  * "Nix's estimate" (6.4, S2.2, S3.1) has no author-date citation; the entry is "Nix, n.d.".
* **In `references.md` but not cited anywhere in the prose:** Beltran-Peña et al. 2020. Remove it or cite it.
* **Elsevier Harvard form:** sections 4, 5.3 to 5.8, S2 and S3 use the bare form as a sentence subject ("Foran and Poldy 2002 set", "Wackernagel 1994 set out", "Khorsandi et al. 2022 combine", "Alexander et al. 2016 define"). Elsevier Harvard writes "Foran and Poldy (2002) set". Sections 1, 2, 6 and 8 already do.
* `references.md` carries 29 entries marked [CHECK] (its own header count), some of which show in the published list (for example Chisholm 2000, "[CHECK: volume; author surname spelling]").

## Journal checks (step 6)

* `python3 qa/tools/wordcount.py B`: **TOTAL 7916** (sections: 673, 519, 306, 912, 2691, 1344, 592, 500, 379). At most 7,950: pass, with 34 words to spare.
* Abstract: **250 words** (whitespace count of the abstract paragraph). At most 250: pass, at the limit.
* Keywords: 7 (carrying capacity; food security; land use; Australia; method comparison; ecological footprint; sensitivity analysis). Pass.
* Em dash (U+2014): grep count 0 in each of `paper_B_draft1.md`, `supplementary.md`, `highlights.md`, `references.md`. Pass. (En dashes appear only in page ranges in `references.md`, as Elsevier style uses.)
* Time words: none of "recently", "currently", "now", "to date", "at present", "so far", "yet", "still", "latest", "soon". Undated "current" remains in 5.4 ("on current yields"), 5.5 ("the current FAOSTAT revision"), Table 3 ("146 to 343 on current yields", "on current data", "5 to 25% on current yields"), S3.3, S3.4, S3.9 and Table S6 ("current FAOSTAT yields"); "today's" in Table S4 item 3. Fail, minor. Rewrite: "on 2021-23 yields", "the FAOSTAT revision read for this paper (2025)", "whether it is the observed diet or a stated alternative".
* Decision 33 tone: no sentence passes a verdict on another author's competence or honesty. "Errors" is used only of the author's own thesis method; "misleading" is the CSIRO and University of Queensland report's word about its own measure; "seriously flawed" is Price's quoted word about the concept. Pass.

## Three places a referee who has not seen Paper A or the repository would be lost

1. **"The thesis method as built, errors kept" and "corrected" (sections 1, 5.9, Table 4).** The paper never says what the errors were or how big each is, yet the corrected release is the reference of the whole comparison. One sentence for 5.9 that names the corrected errors (the register's B160, for example, names a biodiesel error) and gives their combined effect on the short-term figure, 49.4 to 41.5 million, with the place in the archive's errata where each is set out.
2. **The model's own vocabulary: "the evaluator" (S3.11, S3.12), "SA2" (6.7), "PAL" (Table 8, S5), "dry sheep equivalent" (S5), "zone 1" (Table S2, S3), "mirror release".** None is defined. One sentence in 5.9: "The model is run by a script (the evaluator) on Australia's small statistical areas (SA2s) grouped into zones, with energy needs set by physical activity level (PAL) and pasture output in dry sheep equivalents (DSE), the grazing unit of Australian pastures."
3. **Lines (a), (b) and (c) and "the distance to the model".** The abstract and section 1 give shares closed (-1% to 8%, 28% to 46%, 10% to 16%) before the reader learns, in 5.11, that a share is the fall in a mean absolute log ratio. One sentence in section 1 after the first figures: "A share closed is how much equalising the inputs reduces the average log ratio between each method's readings and the model's 41.5 million; 0% means no closer, 100% means level with the model."

## Trace table

Every traced number, grouped by line, row and file; fails first. "file value" is the value found, before rounding. Main-text line numbers are those of `papers/B_methods/draft/paper_B_draft1.md`; supplement line numbers those of `supplementary.md`.

Highlights (no claims csv): 9 and 100 (highlight 1), 1.6 and 2.8 (highlight 3), 18.9, 40.4 and 55.3 (highlight 5): **FAIL: no claims row**; each value matches a body row (B005; Table S8 1.56 to 2.82 with HALF 1.83; abstract rows B141b-9 and B141b-10).

| Numbers (file value) | Section | Claims row | File | Printed where | Result |
|---|---|---|---|---|---|
| 11.3 | main 4.6 | none | none | paper_B_draft1.md line 108 | FAIL: no claims row |
| 10.7 | main 4.10 | none | none | paper_B_draft1.md line 124 | FAIL: no claims row |
| 11.3 | main 5.6 | none | none | paper_B_draft1.md line 172 | FAIL: no claims row |
| 8.0, 8.0 | main 5.11 | none | none | paper_B_draft1.md line 231 | FAIL: no claims row |
| 35 | main 6.6 | none | none | paper_B_draft1.md line 326 | FAIL: no claims row |
| 40 | supp S2.4 | none | none | supplementary.md line 37 | FAIL: no claims row |
| 2,355 | supp S2.9 | none | none | supplementary.md line 57 | FAIL: no claims row |
| 100, 37.0, 30.8, 26.3, 22.9, 18.9, 100, 100, 100 | supp S3.6 | none | none | supplementary.md line 110 | FAIL: no claims row |
| 396.1 | supp S3.7 | none | none | supplementary.md line 114 | FAIL: no claims row |
| 1.129 | supp S3.7 | none | none | supplementary.md line 116 | FAIL: no claims row |
| 46 | supp S3.11 | none | none | supplementary.md line 263 | FAIL: no claims row |
| 27.7, 45.9, 10.5, 87, 35.8 | supp S3.11 | none | none | supplementary.md line 279 | FAIL: no claims row |
| 14.75, 1.10, 7.376, 0.62, 31.0, 2,892, 1,912 | supp S3.11 | none | none | supplementary.md line 281 | FAIL: no claims row |
| 3.2, 23.6, 27.7, 45.9, 12.5, 39.7, 9.4, 35.5 | supp S3.11 | none | none | supplementary.md line 293 | FAIL: no claims row |
| 46, 13.60, 41.5035, 75.97, 5,040, -34.46 | supp S3.12 | none | none | supplementary.md line 313 | FAIL: no claims row |
| -48, 64, 4.9 | supp S3.12 | none | none | supplementary.md line 315 | FAIL: no claims row |
| 4.01, 93.1, 1.61, 0.33 | supp S3.12 | none | none | supplementary.md line 317 | FAIL: no claims row |
| 46, 7.376, 13.60, 14.75, 1.84 | supp S3.12 | none | none | supplementary.md line 319 | FAIL: no claims row |
| 44.1, 40.7 | supp S3.14 | none | none | supplementary.md line 341 | FAIL: no claims row |
| 3.00, 2.26, 2.01 | supp S3.14 | none | none | supplementary.md line 343 | FAIL: no claims row |
| 24.8, 23.5, 35.9, 60.4, -4.5, -10.9, -4.8, 9.7, -1.3 | supp S3.14 | none | none | supplementary.md line 354 | FAIL: no claims row |
| 5.33, 6.68 | supp S4 | none | none | supplementary.md line 358 | FAIL: no claims row |
| 100 | supp S7 | none | none | supplementary.md line 441 | FAIL: no claims row |
| 2,100, 87, 128, 184, 264 | supp S8 | none | none | supplementary.md line 461 | FAIL: no claims row |
| 23,600 | supp S8 | none | none | supplementary.md line 471 | FAIL: no claims row |
| 14.75 | main 5.14 | 5/B141b-1 | analysis/method_tests_2025/bases.csv | paper_B_draft1.md line 284 | FAIL: row's file does not carry it |
| 34.5 | main 7.6 | 7/B141b-12 | none | paper_B_draft1.md line 438 | FAIL: row's file does not carry it |
| 28, 46, 87, 10, 16 | main 9.1 | 9/B141b-15 | none | paper_B_draft1.md line 484 | FAIL: row's file does not carry it |
| 34.5 | main 9.1 | 7/B141b-12 | none | paper_B_draft1.md line 484 | FAIL: row's file does not carry it |
| 40.4 | main 9.2 | 9/B141b-16 | none | paper_B_draft1.md line 488 | FAIL: row's file does not carry it |
| 331.87 | supp S3.13 | S3/B141b-16 | analysis/comparison_2025/production_comparison_2025.csv;('REG', 'B139');('REG', 'B139');qa/reports/B139_paper_B_third_line_bridge_panels.md;qa/reports/V53_check_B139.md;qa/reports/V53_check_B139.md;qa | supplementary.md line 329 | FAIL: row's file does not carry it |
| 26.08 | supp S3.8 | S3/54 | named csv prints a different value or no such cell (see fails) | supplementary.md line 182 | FAIL: file disagrees |
| 26.08 | supp S3.8 | S3/54 | named csv prints a different value or no such cell (see fails) | supplementary.md line 183 | FAIL: file disagrees |
| 41.1, 48.1, 58.1 | supp S3.10 | S3/Table S7 row 12 | named csv prints a different value or no such cell (see fails) | supplementary.md line 255 | FAIL: file disagrees |
| 12.0, 17.9 | supp S3.10 | S3/Table S7 row 13 | named csv prints a different value or no such cell (see fails) | supplementary.md line 256 | FAIL: file disagrees |
| 19.7 | supp S3.10 | S3/65 | named csv prints a different value or no such cell (see fails) | supplementary.md line 256 | FAIL: file disagrees |
| 126.6, 137.2 | supp S3.10 | S3/67 | named csv prints a different value or no such cell (see fails) | supplementary.md line 257 | FAIL: file disagrees |
| 138.1 | supp S3.10 | S3/Table S7 row 14 | named csv prints a different value or no such cell (see fails) | supplementary.md line 257 | FAIL: file disagrees |
| 1.30, 1.88, 1.01, 1.45 | supp S3.11 | S3/B141b-11 | named csv prints a different value or no such cell (see fails) | supplementary.md line 301 | FAIL: file disagrees |
| 9 (9), 100 (100), -1 (100), 100 (100) | main Abstract | abstract/1 | register B005 | paper_B_draft1.md line 9 | pass |
| 65 (64.8), 211 (211134), 1.6 (1.56), 5 (5.08), 343 (343.4), 5 (5.08) | main Abstract | abstract/3 | analysis/method_tests_2025/cross_method_local.csv | paper_B_draft1.md line 9 | pass |
| 146 (146.2) | main Abstract | abstract/B141b-2 | analysis/method_tests_2025/cross_method_local.csv | paper_B_draft1.md line 9 | pass |
| 8 (8), 41.5 (41.5) | main Abstract | abstract/3 | qa/reports/B113_harmonised_both_lines.md | paper_B_draft1.md line 9 | pass |
| 28 (0.278), 46 (0.464) | main Abstract | abstract/B141b-5 | analysis/method_tests_2025/harmonised_robustness.csv | paper_B_draft1.md line 9 | pass |
| 10 (10), 16 (16) | main Abstract | abstract/B141b-7 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 9 | pass |
| 18.9 (18.9), 55.3 (55.3) | main Abstract | abstract/7 | register B003 | paper_B_draft1.md line 9 | pass |
| 40.4 (4.04496e+07) | main Abstract | abstract/B141b-9 | analysis/resilience_2025/drought_bounds_paper_B.csv | paper_B_draft1.md line 9 | pass |
| 1.58 (1.58) | main Abstract | abstract/7 | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 9 | pass |
| 95 (95) | main Abstract | abstract/7 | qa/reports/B115_monte_carlo_widened.md | paper_B_draft1.md line 9 | pass |
| 9 (9), 100 (100), 109 (109), 9 (9), 100 (100) | main 1. | 1/1 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 13 | pass |
| 9.4 (9.4) | main 1. | 1/1 | register B005 | paper_B_draft1.md line 13 | pass |
| 14.1 (14.1) | main 1. | 1/4 | register B089 | paper_B_draft1.md line 13 | pass |
| 14 (14) | main 1. | 1/4 | register B006 | paper_B_draft1.md line 13 | pass |
| 27 (0.27), 63 (63) | main 1. | 1/5 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 13 | pass |
| 90 (90) | main 1. | 1/6 | register B162 | paper_B_draft1.md line 13 | pass |
| 10 (10) | main 1. | 1/4 | results/2011-thesis.csv | paper_B_draft1.md line 17 | pass |
| 480 (480) | main 1. | 1/10 | qa/literature_register.csv | paper_B_draft1.md line 17 | pass |
| 50 (50) | main 1. | 1/11 | register B197 | paper_B_draft1.md line 17 | pass |
| 30 (30) | main 1. | 1/7 | literature register L010 | paper_B_draft1.md line 17 | pass |
| 35 (35) | main 1. | 1/11 | register B196 | paper_B_draft1.md line 17 | pass |
| -1 (1.08) | main 1. | 1/1 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 25 | pass |
| 8 (8.4) | main 1. | 1/Table 1 note | literature register L006 | paper_B_draft1.md line 25 | pass |
| 28 (0.278), 46 (0.464) | main 1. | 1/B141b-12 | analysis/method_tests_2025/harmonised_robustness.csv | paper_B_draft1.md line 25 | pass |
| 65 (65), 20 (2050) | main 1. | 1/Table 1, Taylor 1922 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 31 | pass |
| 82 (82), 60 (60), 1970 (1970) | main 1. | 1/Table 1, Gifford et al. 1975 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 32 | pass |
| 50 (50) | main 1. | 1/11 | register B197 | paper_B_draft1.md line 33 | pass |
| 60 (60) | main 1. | 1/Table 1, Gifford et al. 1975 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 33 | pass |
| 50 (50) | main 1. | 1/11 | register B197 | paper_B_draft1.md line 34 | pass |
| 50 (50), 50 (50) | main 1. | 1/11 | register B197 | paper_B_draft1.md line 35 | pass |
| 30 (30), 30 (30) | main 1. | 1/7 | literature register L010 | paper_B_draft1.md line 35 | pass |
| 35 (35), 35 (35) | main 1. | 1/11 | register B196 | paper_B_draft1.md line 35 | pass |
| 109 (109) | main 1. | 1/1 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 36 | pass |
| 96 (96) | main 1. | 1/Table 1, Henry and Godden 1995 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 36 | pass |
| 30 (30) | main 1. | 1/7 | literature register L010 | paper_B_draft1.md line 37 | pass |
| 32 (32), 76 (76), 80 (80) | main 1. | 1/Table 1, Foran and Poldy 2002 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 37 | pass |
| 60 (60) | main 1. | 1/Table 1, Gifford et al. 1975 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 38 | pass |
| 40 (39.9), 40 (39.9), 23 (23), 12 (12) | main 1. | 1/Table 1, Lane, Dawes and Grace 2014, 2015; Lane 2017 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 39 | pass |
| 9 (9), 100 (100) | main 1. | 1/1 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 39 | pass |
| 61 (61), 36.6 (36.6) | main 1. | 1/Table 1, Bellotti 2017 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 40 | pass |
| 100 (100) | main 1. | 1/1 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 41 | pass |
| 27 (0.27), 63 (63) | main 1. | 1/5 | analysis/comparators_2025/harmonisation.csv | paper_B_draft1.md line 41 | pass |
| 69 (69) | main 2. | 2/15 | register B334 | paper_B_draft1.md line 53 | pass |
| 115 (115) | main 2. | 2/15 | register B335 | paper_B_draft1.md line 53 | pass |
| 7.7 (7.7) | main 2. | 2/15 | register B336 | paper_B_draft1.md line 53 | pass |
| 2,700 (2700) | main 4.6 | 4/27 | register B087 | paper_B_draft1.md line 108 | pass |
| 2,550 (2550) | main 4.10 | 4/41 | register B122 | paper_B_draft1.md line 124 | pass |
| 31.65 (31.65), 331.87 (331.87) | main 5.1 | 5/3 | register B045 | paper_B_draft1.md line 136 | pass |
| 363.5 (363.5) | main 5.1 | 5/3 | register B262 | paper_B_draft1.md line 136 | pass |
| 0.01 (1) | main 5.1 | 5/B141b-2 | analysis/comparison_2025/production_comparison_2025.csv | paper_B_draft1.md line 136 | pass |
| 14.8 (14.8) | main 5.1 | 5/B141b-1 | analysis/method_tests_2025/bases.csv | paper_B_draft1.md line 136 | pass |
| 3,525 (3525), 120.7 (120.7) | main 5.1 | 5/4 | register B263 | paper_B_draft1.md line 136 | pass |
| 26.20 (26.2) | main 5.1 | 5/5 | analysis/method_tests_2025/bases.csv | paper_B_draft1.md line 136 | pass |
| 4 (400.5) | main 5.1 | 5/34 | analysis/method_tests_2025/cassidy.csv | paper_B_draft1.md line 136 | pass |
| 21 (21) | main 5.1 | 5/34 | register B083 | paper_B_draft1.md line 136 | pass |
| 0.4 (35.9) | main 5.1 | 5/B141b-5 | analysis/method_tests_2025/production_window_10y.csv | paper_B_draft1.md line 136 | pass |
| 6 (6) | main 5.1 | 5/22 | literature register L017 | paper_B_draft1.md line 136 | pass |
| 2 (2) | main 5.2 | 5/29 | literature register L016 | paper_B_draft1.md line 140 | pass |
| 10 (10), 10 (10) | main 5.2 | 5/42 | register B134 | paper_B_draft1.md line 140 | pass |
| 108.9 (108.9), 95.7 (95.7) | main 5.3 | 5/12 | register B015 | paper_B_draft1.md line 146 | pass |
| 109 (109), 96 (96) | main 5.3 | 5/12 | register B008 | paper_B_draft1.md line 146 | pass |
| 134 (133.8), 211 (210.7) | main 5.3 | 5/14 | register B019 | paper_B_draft1.md line 148 | pass |
| 1.758 (1.758), 0.095 (0.095), 0.312 (0.312) | main 5.4 | 5/15 | register B032 | paper_B_draft1.md line 152 | pass |
| 3 (3) | main 5.4 | 5/21 | register B046 | paper_B_draft1.md line 154 | pass |
| 1.718 (1.718) | main 5.4 | 5/17 | register B260 | paper_B_draft1.md line 154 | pass |
| 1.758 (1.758) | main 5.4 | 5/15 | register B032 | paper_B_draft1.md line 154 | pass |
| 2.3 (2.3) | main 5.4 | 5/17 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 154 | pass |
| 21.6 (21.6) | main 5.4 | 5/18 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 154 | pass |
| 1 (1), 2 (2) | main 5.4 | 5/29 | literature register L016 | paper_B_draft1.md line 154 | pass |
| 4 (400.5) | main 5.4 | 5/34 | analysis/method_tests_2025/cassidy.csv | paper_B_draft1.md line 154 | pass |
| 11.9 (11.9495) | main 5.4 | 5/19 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 154 | pass |
| 64.8 (64.8), 64.8 (64.8), 84.6 (84.6) | main 5.4 | 5/Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 156 | pass |
| 117.0 (117) | main 5.4 | 5/20 | analysis/method_tests_2025/cross_method_local.csv | paper_B_draft1.md line 156 | pass |
| 146 (146.2), 343 (343.4), 103 (103), 3 (3) | main 5.4 | 5/21 | register B046 | paper_B_draft1.md line 156 | pass |
| 6 (6) | main 5.5 | 5/22 | literature register L017 | paper_B_draft1.md line 160 | pass |
| 2.2 (2.165), 34.4 (34.37), 35.13 (35.13), 0.8 (0.8), 113.1 (113.12), 112.20 (112.2), 2.8 (2.8), 8.4 (8.4), 121.6 (121.59) | main 5.5 | 5/23 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 162 | pass |
| 94.8 (94.8), 135.76 (135.76) | main 5.5 | 5/25 | register B057 | paper_B_draft1.md line 162 | pass |
| 1.32 (1.32), 81.0 (81) | main 5.5 | 5/27 | register B063 | paper_B_draft1.md line 164 | pass |
| 363.5 (363.5) | main 5.5 | 5/3 | register B262 | paper_B_draft1.md line 164 | pass |
| 1.318 (1.318), 276 (276) | main 5.5 | 5/28 | register B068 | paper_B_draft1.md line 164 | pass |
| 76.0 (76) | main 5.5 | 5/Table 5 row 4 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 164 | pass |
| 61 (61), 59 (59), 67 (67) | main 5.6 | 5/31 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 170 | pass |
| 41 (41), 41 (41) | main 5.6 | 5/32 | register B079 | paper_B_draft1.md line 170 | pass |
| 22 (22), 42 (42), 22 (22) | main 5.6 | 5/32 | register B078 | paper_B_draft1.md line 170 | pass |
| 6.0 (6) | main 5.6 | 5/33 | register B081 | paper_B_draft1.md line 172 | pass |
| 7.9 (7.9) | main 5.6 | 5/33 | register B082 | paper_B_draft1.md line 172 | pass |
| 22 (22) | main 5.6 | 5/32 | register B078 | paper_B_draft1.md line 172 | pass |
| 147 (147) | main 5.6 | 5/34 | register B083 | paper_B_draft1.md line 172 | pass |
| 2,700 (2700) | main 5.6 | 5/34 | register B087 | paper_B_draft1.md line 172 | pass |
| 145 (145) | main 5.6 | 5/34 | register B259 | paper_B_draft1.md line 172 | pass |
| 1.2 (1.2) | main 5.7 | 5/37 | register B326 | paper_B_draft1.md line 178 | pass |
| 30 (29.88) | main 5.7 | 5/44 | analysis/method_tests_2025/fearnside_failure_curve.csv | paper_B_draft1.md line 180 | pass |
| 32 (3182) | main 5.7 | 5/31 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 180 | pass |
| 76 | main 5.7 | 5/B141b-9 | harmonisation.csv row "Foran and Poldy 2002" ("76 to 80"), via the Table 1 row the claims row names (checked by hand) | paper_B_draft1.md line 180 | pass |
| 80 | main 5.7 | 5/B141b-9 | harmonisation.csv row "Foran and Poldy 2002" ("76 to 80"), via the Table 1 row (checked by hand) | paper_B_draft1.md line 180 | pass |
| 40 (40) | main 5.7 | 5/38 | register B146 | paper_B_draft1.md line 180 | pass |
| 41 (41) | main 5.7 | 5/32 | register B079 | paper_B_draft1.md line 180 | pass |
| 128 (128) | main 5.7 | 5/38 | register B148 | paper_B_draft1.md line 180 | pass |
| 127 (127), 12 (11.64) | main 5.7 | 5/38 | analysis/method_tests_2025/foran_poldy_balance.csv | paper_B_draft1.md line 180 | pass |
| 17 (17) | main 5.7 | 5/38 | register B150 | paper_B_draft1.md line 180 | pass |
| 150 (150) | main 5.8 | 5/40 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 186 | pass |
| 41.5 (41.5) | main 5.8 | 5/41 | register B137 | paper_B_draft1.md line 188 | pass |
| 30.8 (30.81), 10 (10), 26 (25.8) | main 5.8 | 5/42 | register B134 | paper_B_draft1.md line 188 | pass |
| 1 (1), 1 (1), 1 (1), 1 (1), 1 (1) | main 5.8 | 5/29 | literature register L016 | paper_B_draft1.md line 188 | pass |
| 18.9 (18.92), 54 (53.64) | main 5.8 | 5/42 | analysis/method_tests_2025/fearnside_failure_curve.csv | paper_B_draft1.md line 188 | pass |
| 100 (1), 100 (1) | main 5.8 | 5/12 | literature register L003 | paper_B_draft1.md line 188 | pass |
| 41.2 (4.11915e+07), 40.4 (4.04496e+07) | main 5.8 | 5/B141b-10 | analysis/resilience_2025/drought_bounds_paper_B.csv | paper_B_draft1.md line 188 | pass |
| 5.8 (5.8), 6.1 (6.1), 16 (16) | main 5.8 | 5/43 | register B130 | paper_B_draft1.md line 188 | pass |
| 17 (17) | main 5.8 | 5/38 | register B150 | paper_B_draft1.md line 188 | pass |
| 65 (64.8), 1.6 (1.56), 1.56 (1.56), 2.82 (2.82), 1.83 (1.83) | main 5.10 | 5/48 | analysis/method_tests_2025/cross_method_local.csv | paper_B_draft1.md line 196 | pass |
| 211 (210.7) | main 5.10 | 5/14 | register B019 | paper_B_draft1.md line 196 | pass |
| 5 (5) | main 5.10 | 5/Table 4 caption | analysis/method_tests_2025/model_entry.csv | paper_B_draft1.md line 196 | pass |
| 64.8 (64.8), 53.9 (53.9), 77.9 (77.9) | main 5.10 | 5/Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 196 | pass |
| 117.0 (117) | main 5.10 | 5/20 | analysis/method_tests_2025/cross_method_local.csv | paper_B_draft1.md line 196 | pass |
| 76.0 (76) | main 5.10 | 5/Table 5 row 4 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 196 | pass |
| 146 (146.2), 343 (343.4) | main 5.10 | 5/21 | register B046 | paper_B_draft1.md line 196 | pass |
| 276 (276) | main 5.10 | 5/28 | register B068 | paper_B_draft1.md line 196 | pass |
| 3.5 (3.5) | main 5.10 | 5/77 | qa/reports/B114_pairing_relaxed.md | paper_B_draft1.md line 196 | pass |
| 8 (8) | main 5.10 | 5/Table 3 row 5 | analysis/method_tests_2025/cross_method.csv | paper_B_draft1.md line 196 | pass |
| 12 (11.64) | main 5.10 | 5/38 | analysis/method_tests_2025/foran_poldy_balance.csv | paper_B_draft1.md line 196 | pass |
| 41 (41) | main 5.10 | 5/32 | register B079 | paper_B_draft1.md line 196 | pass |
| 1 (1) | main 5.10 | 5/29 | literature register L016 | paper_B_draft1.md line 196 | pass |
| 10 (10), 30.8 (30.81) | main 5.10 | 5/42 | register B134 | paper_B_draft1.md line 196 | pass |
| 41.2 (4.11915e+07) | main 5.10 | 5/B141b-10 | analysis/resilience_2025/drought_bounds_paper_B.csv | paper_B_draft1.md line 196 | pass |
| 31.1 (3.11154e+07), 49.2 (4.91698e+07) | main 5.10 | 5/51 | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 196 | pass |
| 21.6 (21.6) | main 5.10 | 5/18 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 198 | pass |
| -11.9 (11.9495) | main 5.10 | 5/19 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 198 | pass |
| 8.4 (8.4) | main 5.10 | 5/23 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 198 | pass |
| 2,000 (20) | main 5.10 | 5/Table 4 row 4 | qa/reports/B130_widened_draws_improved.md | paper_B_draft1.md line 198 | pass |
| 31.1 (3.11154e+07), 49.2 (4.91698e+07) | main 5.10 | 5/51 | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 198 | pass |
| 19 (19) | main 5.10 | 5/Table 6 caption | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 198 | pass |
| 37.9 (3.79033e+07), 60.0 (5.99707e+07), 18 (1.8474e+07) | main 5.10 | 5/Table 4 row 4 | results/ranges_2025-improved_wide.csv | paper_B_draft1.md line 198 | pass |
| 103 (103), 343 (343.4), 146 (146.2), 3 (3) | main 5.10 | 5/21 | register B046 | paper_B_draft1.md line 198 | pass |
| 183 (1.83) | main 5.10 | 5/Table 3 row 5 | analysis/method_tests_2025/cross_method_local.csv | paper_B_draft1.md line 198 | pass |
| 134 (133.8), 211 (210.7) | main 5.10 | 5/14 | register B019 | paper_B_draft1.md line 202 | pass |
| 109 (109), 96 (96) | main 5.10 | 5/12 | register B008 | paper_B_draft1.md line 202 | pass |
| 64.8 (64.8), 64.8 (64.8), 84.6 (84.6), 53.9 (53.9), 77.9 (77.9) | main 5.10 | 5/Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 203 | pass |
| 117.0 (117) | main 5.10 | 5/20 | analysis/method_tests_2025/cross_method_local.csv | paper_B_draft1.md line 203 | pass |
| 146 (146.2), 343 (343.4), 103 (103), 103 (103), 343 (343.4) | main 5.10 | 5/21 | register B046 | paper_B_draft1.md line 203 | pass |
| 160 (160), 268 (268) | main 5.10 | 5/Table 3 row 3 | analysis/method_tests_2025/cross_method.csv | paper_B_draft1.md line 203 | pass |
| 2.3 (2.3) | main 5.10 | 5/17 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 203 | pass |
| 21.6 (21.6) | main 5.10 | 5/18 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 203 | pass |
| 11.9 (11.9495) | main 5.10 | 5/19 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 203 | pass |
| 76.0 (76) | main 5.10 | 5/Table 5 row 4 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 204 | pass |
| 276 (276) | main 5.10 | 5/28 | register B068 | paper_B_draft1.md line 204 | pass |
| 0.8 (0.8), 2.2 (2.165), 8.4 (8.4), 2.8 (2.8) | main 5.10 | 5/23 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 204 | pass |
| 5.8 (5.8) | main 5.10 | 5/43 | register B130 | paper_B_draft1.md line 205 | pass |
| 6.0 (6) | main 5.10 | 5/33 | register B081 | paper_B_draft1.md line 205 | pass |
| 145 (145) | main 5.10 | 5/34 | register B259 | paper_B_draft1.md line 205 | pass |
| 147 (147) | main 5.10 | 5/34 | register B083 | paper_B_draft1.md line 205 | pass |
| 190 (190), 8 (8) | main 5.10 | 5/Table 3 row 5 | analysis/method_tests_2025/cross_method.csv | paper_B_draft1.md line 205 | pass |
| 22 (22), 42 (42) | main 5.10 | 5/32 | register B078 | paper_B_draft1.md line 205 | pass |
| 5 (5), 5 (5) | main 5.10 | 5/Table 4 caption | analysis/method_tests_2025/model_entry.csv | paper_B_draft1.md line 205 | pass |
| 25 (24.9) | main 5.10 | 5/32 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 205 | pass |
| 40 (40) | main 5.10 | 5/38 | register B146 | paper_B_draft1.md line 206 | pass |
| 41 (41) | main 5.10 | 5/32 | register B079 | paper_B_draft1.md line 206 | pass |
| 12 (11.64), 127 (127) | main 5.10 | 5/38 | analysis/method_tests_2025/foran_poldy_balance.csv | paper_B_draft1.md line 206 | pass |
| 17 (17) | main 5.10 | 5/38 | register B150 | paper_B_draft1.md line 206 | pass |
| 128 (128) | main 5.10 | 5/38 | register B148 | paper_B_draft1.md line 206 | pass |
| 1.2 (1.2) | main 5.10 | 5/37 | register B326 | paper_B_draft1.md line 206 | pass |
| 30 (29.88) | main 5.10 | 5/44 | analysis/method_tests_2025/fearnside_failure_curve.csv | paper_B_draft1.md line 206 | pass |
| 77 (77) | main 5.10 | 5/Table 3 row 6 | analysis/method_tests_2025/cross_method.csv | paper_B_draft1.md line 206 | pass |
| 41.5 (41.5) | main 5.10 | 5/41 | register B137 | paper_B_draft1.md line 207 | pass |
| 30.8 (30.81), 10 (10) | main 5.10 | 5/42 | register B134 | paper_B_draft1.md line 207 | pass |
| 1 (1), 1 (1) | main 5.10 | 5/29 | literature register L016 | paper_B_draft1.md line 207 | pass |
| 18.9 (18.92) | main 5.10 | 5/42 | analysis/method_tests_2025/fearnside_failure_curve.csv | paper_B_draft1.md line 207 | pass |
| 100 (1) | main 5.10 | 5/12 | literature register L003 | paper_B_draft1.md line 207 | pass |
| 41.2 (4.11915e+07), 40.4 (4.04496e+07) | main 5.10 | 5/B141b-10 | analysis/resilience_2025/drought_bounds_paper_B.csv | paper_B_draft1.md line 207 | pass |
| 41.5 (41.5) | main 5.10 | 5/41 | register B137 | paper_B_draft1.md line 208 | pass |
| 31.1 (3.11154e+07), 49.2 (4.91698e+07) | main 5.10 | 5/51 | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 208 | pass |
| 53.6 (5.36437e+07), 37.9 (3.79033e+07), 60.0 (5.99707e+07) | main 5.10 | 5/Table 4 row 4 | results/ranges_2025-improved_wide.csv | paper_B_draft1.md line 209 | pass |
| 5 (5), 95 (95) | main 5.10 | 5/Table 4 caption | analysis/method_tests_2025/model_entry.csv | paper_B_draft1.md line 211 | pass |
| 2,000 (20) | main 5.10 | 5/Table 4 row 4 | qa/reports/B130_widened_draws_improved.md | paper_B_draft1.md line 211 | pass |
| 19 (19) | main 5.10 | 5/Table 6 caption | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 211 | pass |
| 18 (1.8474e+07) | main 5.10 | 5/Table 4 row 4 | results/ranges_2025-improved_wide.csv | paper_B_draft1.md line 211 | pass |
| 13 (1.33072e+07) | main 5.10 | 5/Table 4 caption | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 211 | pass |
| 10 (10) | main 5.10 | 5/42 | register B134 | paper_B_draft1.md line 211 | pass |
| 100 (1) | main 5.10 | 5/12 | literature register L003 | paper_B_draft1.md line 211 | pass |
| 41.2 (4.11915e+07), 40.4 (4.04496e+07) | main 5.10 | 5/B141b-10 | analysis/resilience_2025/drought_bounds_paper_B.csv | paper_B_draft1.md line 211 | pass |
| 53.2 (5.31523e+07), 52.0 (5.19903e+07) | main 5.10 | 5/Table 4 note | analysis/resilience_2025/drought_bounds_paper_B.csv | paper_B_draft1.md line 211 | pass |
| 10 (10) | main 5.10 | 5/42 | register B134 | paper_B_draft1.md line 213 | pass |
| 100 (1) | main 5.10 | 5/12 | literature register L003 | paper_B_draft1.md line 213 | pass |
| 49.4 (49.4), 14.1 (14.1), 36.66 (36.66), 22.51 (22.51), 27.6 (27.6) | main 5.10 | 5/Table 4 row 2 | analysis/method_tests_2025/model_entry.csv | paper_B_draft1.md line 215 | pass |
| 41.5 (41.5) | main 5.10 | 5/41 | register B137 | paper_B_draft1.md line 216 | pass |
| 31.1 (3.11154e+07), 49.2 (4.91698e+07) | main 5.10 | 5/51 | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 216 | pass |
| 15.6 (15.6), 13.3 (13.3), 18.8 (18.8), 30.81 (30.81) | main 5.10 | 5/Table 4 row 3 | analysis/method_tests_2025/model_entry.csv | paper_B_draft1.md line 216 | pass |
| 18.92 (18.92) | main 5.10 | 5/42 | analysis/method_tests_2025/fearnside_failure_curve.csv | paper_B_draft1.md line 216 | pass |
| 27.6 (27.6) | main 5.10 | 5/Table 4 row 2 | analysis/method_tests_2025/model_entry.csv | paper_B_draft1.md line 216 | pass |
| 53.6 (5.36437e+07), 37.9 (3.79033e+07), 60.0 (5.99707e+07), 18.5 (1.8474e+07), 15.7 (1.56659e+07), 22.1 (2.20548e+07) | main 5.10 | 5/Table 4 row 4 | results/ranges_2025-improved_wide.csv | paper_B_draft1.md line 217 | pass |
| 39.93 (39.93), 24.68 (24.68) | main 5.10 | 5/Table 4 row 4 | analysis/method_tests_2025/model_entry.csv | paper_B_draft1.md line 217 | pass |
| 27.6 (27.6) | main 5.10 | 5/Table 4 row 2 | analysis/method_tests_2025/model_entry.csv | paper_B_draft1.md line 217 | pass |
| 145.2 (145.2), 148.8 (148.8) | main 5.11 | 5/53 | register B264 | paper_B_draft1.md line 223 | pass |
| 110.9 (110.9), 112.9 (112.9) | main 5.11 | 5/53 | register B273 | paper_B_draft1.md line 223 | pass |
| 1 (1), 1 (1) | main 5.11 | 5/29 | literature register L016 | paper_B_draft1.md line 225 | pass |
| 3 (3) | main 5.11 | 5/21 | register B046 | paper_B_draft1.md line 225 | pass |
| 4.29 (4.29), 2.06 (2.06), 2.47 (2.47) | main 5.11 | 5/B141b-16 | analysis/method_tests_2025/harmonised_robustness_footprint.csv | paper_B_draft1.md line 225 | pass |
| 0.646 (0.646), 0.702 (0.702), 6.22 (6.22), 6.95 (6.95) | main 5.11 | 5/60 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 227 | pass |
| 0.440 (0.44), 3.70 (3.7) | main 5.11 | 5/61 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 227 | pass |
| 19 (19) | main 5.11 | 5/Table 6 caption | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 227 | pass |
| 12 (11.64) | main 5.11 | 5/38 | analysis/method_tests_2025/foran_poldy_balance.csv | paper_B_draft1.md line 227 | pass |
| 23 (23) | main 5.11 | 5/4 | register B263 | paper_B_draft1.md line 227 | pass |
| 48 (0.475) | main 5.11 | 5/B141b-19 | analysis/method_tests_2025/harmonised_robustness.csv | paper_B_draft1.md line 227 | pass |
| 41.5 (41.5) | main 5.11 | 5/41 | register B137 | paper_B_draft1.md line 227 | pass |
| 4.1 (0.041) | main 5.11 | 5/60 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 229 | pass |
| -1 (1) | main 5.11 | 5/29 | literature register L016 | paper_B_draft1.md line 229 | pass |
| 8 (8) | main 5.11 | 5/Table 3 row 5 | analysis/method_tests_2025/cross_method.csv | paper_B_draft1.md line 229 | pass |
| 31.1 (3.11154e+07) | main 5.11 | 5/51 | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 229 | pass |
| 53.6 (5.36437e+07) | main 5.11 | 5/Table 4 row 4 | results/ranges_2025-improved_wide.csv | paper_B_draft1.md line 229 | pass |
| 38.5 (0.385) | main 5.11 | 5/61 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 229 | pass |
| 28 (0.278), 46 (0.464), 36 (0.358), 9 (0.093), 36 (0.358) | main 5.11 | 5/B141b-21 | analysis/method_tests_2025/harmonised_robustness.csv | paper_B_draft1.md line 229 | pass |
| 5 (5) | main 5.11 | 5/Table 4 caption | analysis/method_tests_2025/model_entry.csv | paper_B_draft1.md line 229 | pass |
| 10.5 (0.105) | main 5.11 | 5/B141b-22 | analysis/method_tests_2025/harmonised_robustness.csv | paper_B_draft1.md line 229 | pass |
| 87 (0.8724) | main 5.11 | 5/B141b-22 | results/2025-fixed.csv | paper_B_draft1.md line 229 | pass |
| 1.51 (1.512) | main 5.11 | 5/B141b-23 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 231 | pass |
| 1.10 (1.1) | main 5.11 | 5/B141b-23 | qa/reports/V53_check_B139.md | paper_B_draft1.md line 231 | pass |
| 14.7 (0.147), 20 (0.196), 0.65 (64.8), 0.48 (0.477), 0.44 (44.3) | main 5.11 | 5/B141b-24 | analysis/method_tests_2025/harmonised_line_c.csv | paper_B_draft1.md line 231 | pass |
| 26 (25.8), 10 (10) | main 5.11 | 5/42 | register B134 | paper_B_draft1.md line 231 | pass |
| 7.376 (7.376) | main 5.11 | 5/B141b-25 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 231 | pass |
| 16 (16) | main 5.11 | 5/43 | register B130 | paper_B_draft1.md line 231 | pass |
| 38 (38.5) | main 5.11 | 5/B141b-26 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 231 | pass |
| 46 (0.464) | main 5.11 | 5/B141b-21 | analysis/method_tests_2025/harmonised_robustness.csv | paper_B_draft1.md line 231 | pass |
| 134 (133.8), 211 (210.7) | main 5.11 | 5/14 | register B019 | paper_B_draft1.md line 237 | pass |
| 145.2 (145.2), 148.8 (148.8) | main 5.11 | 5/53 | register B264 | paper_B_draft1.md line 237 | pass |
| 0.69 (69.4), 1.11 (1.112), 3.50 (3.5), 3.59 (3.59) | main 5.11 | 5/Table 5 row 2 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 237 | pass |
| 103 (103), 343 (343.4), 103 (103), 343 (343.4), 343 (343.4), 343 (343.4), 3 (3) | main 5.11 | 5/21 | register B046 | paper_B_draft1.md line 238 | pass |
| 160 (160), 268 (268), 160 (160) | main 5.11 | 5/Table 3 row 3 | analysis/method_tests_2025/cross_method.csv | paper_B_draft1.md line 238 | pass |
| 139 (139.4), 139 (139.4), 278 (2.78), 1.00 (1), 1.42 (1.419), 3.36 (3.36), 8.27 (8.27), 64.8 (64.8), 117 (117), 113 (112.9), 117 (117), 64.8 (64.8), 84.6 (84.6), 53.9 (53.9), 77.9 (77.9) | main 5.11 | 5/Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 238 | pass |
| 1 (1) | main 5.11 | 5/29 | literature register L016 | paper_B_draft1.md line 238 | pass |
| 276 (276) | main 5.11 | 5/28 | register B068 | paper_B_draft1.md line 239 | pass |
| 275.8 (275.8), 6.65 (6.65), 76.0 (76) | main 5.11 | 5/Table 5 row 4 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 239 | pass |
| 1.00 (1) | main 5.11 | 5/Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 239 | pass |
| 145 (145) | main 5.11 | 5/34 | register B259 | paper_B_draft1.md line 240 | pass |
| 190 (190) | main 5.11 | 5/Table 3 row 5 | analysis/method_tests_2025/cross_method.csv | paper_B_draft1.md line 240 | pass |
| 111 (1.112), 0.59 (59.3), 0.77 (0.766), 2.67 (2.67), 2.72 (2.72) | main 5.11 | 5/Table 5 row 5 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 240 | pass |
| 113 (112.9) | main 5.11 | 5/Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 240 | pass |
| 40 (40) | main 5.11 | 5/38 | register B146 | paper_B_draft1.md line 241 | pass |
| 17 (17) | main 5.11 | 5/38 | register B150 | paper_B_draft1.md line 241 | pass |
| 128 (128) | main 5.11 | 5/38 | register B148 | paper_B_draft1.md line 241 | pass |
| 41 (41) | main 5.11 | 5/32 | register B079 | paper_B_draft1.md line 241 | pass |
| 12 (11.64), 127 (127) | main 5.11 | 5/38 | analysis/method_tests_2025/foran_poldy_balance.csv | paper_B_draft1.md line 241 | pass |
| 0.71 (71.4), 1.03 (103.1), 0.29 (287.7), 3.06 (3.06) | main 5.11 | 5/Table 5 row 6 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 241 | pass |
| 41.5 (41.5) | main 5.11 | 5/41 | register B137 | paper_B_draft1.md line 242 | pass |
| 30.8 (30.81), 10 (10) | main 5.11 | 5/42 | register B134 | paper_B_draft1.md line 242 | pass |
| 1 (1), 1 (1) | main 5.11 | 5/29 | literature register L016 | paper_B_draft1.md line 242 | pass |
| 18.9 (18.92) | main 5.11 | 5/42 | analysis/method_tests_2025/fearnside_failure_curve.csv | paper_B_draft1.md line 242 | pass |
| 100 (1) | main 5.11 | 5/12 | literature register L003 | paper_B_draft1.md line 242 | pass |
| 41.2 (4.11915e+07), 40.4 (4.04496e+07) | main 5.11 | 5/B141b-10 | analysis/resilience_2025/drought_bounds_paper_B.csv | paper_B_draft1.md line 242 | pass |
| 41.5 (41.5), 41.5 (41.5) | main 5.11 | 5/41 | register B137 | paper_B_draft1.md line 243 | pass |
| 1.00 (1), 1.00 (1) | main 5.11 | 5/Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 243 | pass |
| 53.6 (5.36437e+07), 53.6 (5.36437e+07) | main 5.11 | 5/Table 4 row 4 | results/ranges_2025-improved_wide.csv | paper_B_draft1.md line 244 | pass |
| 1.00 (1) | main 5.11 | 5/Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 244 | pass |
| 1.29 (1.29) | main 5.11 | 5/Table 5 row 9 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 244 | pass |
| 190 (190) | main 5.11 | 5/Table 3 row 5 | analysis/method_tests_2025/cross_method.csv | paper_B_draft1.md line 246 | pass |
| 0.594 (0.594) | main 5.11 | 5/Table 5 row 5 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 246 | pass |
| 112.9 (112.9) | main 5.11 | 5/53 | register B273 | paper_B_draft1.md line 246 | pass |
| 183 (1.83) | main 5.11 | 5/Table 3 row 5 | analysis/method_tests_2025/cross_method_local.csv | paper_B_draft1.md line 246 | pass |
| 3.06 (3.06) | main 5.11 | 5/Table 5 row 6 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 246 | pass |
| 3.05 (3.05) | main 5.11 | 5/Table 5 note | analysis/method_tests_2025/intake_variant.csv | paper_B_draft1.md line 246 | pass |
| 126.6 (126.6) | main 5.11 | 5/Table 5 note | qa/reports/B126b_patch_paper_B.md | paper_B_draft1.md line 246 | pass |
| 8.0 (8) | main 5.11 | 5/Table 6 caption | qa/reports/B113_harmonised_both_lines.md | paper_B_draft1.md line 248 | pass |
| 19 (19), 164.7 (164.7), 147.0 (147), 82.0 (82), 150.3 (150.3), 135.8 (135.8), 83.6 (83.6), 9.6 (0.096), 41.3 (0.413) | main 5.11 | 5/Table 6 caption | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 248 | pass |
| 2 (2) | main 5.11 | 5/29 | literature register L016 | paper_B_draft1.md line 248 | pass |
| 41.5 (41.5) | main 5.11 | 5/41 | register B137 | paper_B_draft1.md line 248 | pass |
| -1.1 (108.912) | main 5.11 | 5/18 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 248 | pass |
| 6.8 (682) | main 5.11 | 5/Table 6 caption | qa/reports/B126b_patch_paper_B.md | paper_B_draft1.md line 248 | pass |
| 27.7 (27.7) | main 5.11 | 5/Table 6 caption | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 248 | pass |
| 45.9 (45.9) | main 5.11 | 5/Table 6 line (c) | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 248 | pass |
| 0.646 (0.646), 0.702 (0.702), -8.6 (0.086), 0.646 (0.646), 0.646 (0.646) | main 5.11 | 5/60 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 252 | pass |
| 0.440 (0.44) | main 5.11 | 5/61 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 252 | pass |
| 31.8 (0.318) | main 5.11 | 5/Table 6 caption | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 252 | pass |
| 0.477 (0.477) | main 5.11 | 5/B141b-24 | analysis/method_tests_2025/harmonised_line_c.csv | paper_B_draft1.md line 252 | pass |
| 26.2 (26.2) | main 5.11 | 5/5 | analysis/method_tests_2025/bases.csv | paper_B_draft1.md line 252 | pass |
| 6.22 (6.22), 6.95 (6.95), 6.22 (6.22), 6.22 (6.22) | main 5.11 | 5/60 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 253 | pass |
| -6.0 (6) | main 5.11 | 5/33 | register B081 | paper_B_draft1.md line 253 | pass |
| 3.70 (3.7) | main 5.11 | 5/61 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 253 | pass |
| 28.4 (0.284) | main 5.11 | 5/Table 6 caption | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 253 | pass |
| 4.12 (4.12) | main 5.11 | 5/Table 6 line (c) | analysis/method_tests_2025/harmonised_line_c.csv | paper_B_draft1.md line 253 | pass |
| 22.6 (22.65) | main 5.11 | 5/B141b-30 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 253 | pass |
| 19 (19), -7.0 (6.95) | main 5.11 | 5/Table 6 caption | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 254 | pass |
| 0.718 (0.718), 0.718 (0.718), 0.604 (0.604), 15.9 (0.159), 0.718 (0.718) | main 5.11 | 5/61 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 254 | pass |
| 0.768 (0.768) | main 5.11 | 5/Table 6 row 6 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 254 | pass |
| 0.599 (0.599), 16.6 (0.166) | main 5.11 | 5/Table 6 line (c) | analysis/method_tests_2025/harmonised_line_c.csv | paper_B_draft1.md line 254 | pass |
| 19 (19), -11.2 (0.112) | main 5.11 | 5/Table 6 caption | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 255 | pass |
| 22.69 (22.69), 22.69 (22.69), 12.40 (12.4), 19.4 (0.194), 22.69 (22.69), 12.40 (12.4), 19.4 (0.194) | main 5.11 | 5/61 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 255 | pass |
| 32.14 (32.14) | main 5.11 | 5/Table 6 row 7 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 255 | pass |
| 41.5 (41.5) | main 5.11 | 5/41 | register B137 | paper_B_draft1.md line 256 | pass |
| 1.411 (1.411), 1.353 (1.353), 1.411 (1.411), 0.867 (0.867), 1.411 (1.411) | main 5.11 | 5/Table 6 row 1 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 256 | pass |
| 4.1 (0.041) | main 5.11 | 5/60 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 256 | pass |
| 38.5 (0.385) | main 5.11 | 5/61 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 256 | pass |
| 1.203 (1.203) | main 5.11 | 5/Table 6 line (c) | analysis/method_tests_2025/harmonised_line_c.csv | paper_B_draft1.md line 256 | pass |
| 14.7 (0.147) | main 5.11 | 5/B141b-24 | analysis/method_tests_2025/harmonised_line_c.csv | paper_B_draft1.md line 256 | pass |
| 0.530 (0.53), 0.556 (0.556), 0.530 (0.53), 0.445 (0.445), 0.530 (0.53) | main 5.11 | 5/Table 6 row 2 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 257 | pass |
| -4.9 (0.049) | main 5.11 | 5/62 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 257 | pass |
| 16.0 (16) | main 5.11 | 5/Table 4 row 2 | analysis/method_tests_2025/model_entry.csv | paper_B_draft1.md line 257 | pass |
| 0.424 (0.424), 20.0 (0.2) | main 5.11 | 5/Table 6 line (c) | analysis/method_tests_2025/harmonised_line_c.csv | paper_B_draft1.md line 257 | pass |
| 0.535 (0.535), 0.569 (0.569), 0.535 (0.535), 0.443 (44.3), 0.535 (0.535) | main 5.11 | 5/Table 6 row 3 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 258 | pass |
| -6.3 (0.063), 17.2 (0.172) | main 5.11 | 5/62 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 258 | pass |
| 0.424 (0.424), 20.7 (0.207) | main 5.11 | 5/Table 6 line (c) | analysis/method_tests_2025/harmonised_line_c.csv | paper_B_draft1.md line 258 | pass |
| 5 (5) | main 5.12 | 5/Table 4 caption | analysis/method_tests_2025/model_entry.csv | paper_B_draft1.md line 262 | pass |
| 0.92 (92), 5.76 (5.76), 9.2 (9.17), 396.1 (396.12) | main 5.12 | 5/66 | analysis/method_tests_2025/gap_attribution_readable.csv | paper_B_draft1.md line 262 | pass |
| 363.5 (363.5) | main 5.12 | 5/3 | register B262 | paper_B_draft1.md line 262 | pass |
| 2.7 (2.72), 9.3 (9.29), 3.1 (3.07), 10.9 (10.95), 3.3 (3.3), 12.9 (12.95) | main 5.13 | 5/72 | analysis/method_tests_2025/intake_variant.csv | paper_B_draft1.md line 266 | pass |
| 1 (1), 2 (2) | main 5.14 | 5/29 | literature register L016 | paper_B_draft1.md line 270 | pass |
| 3.5 (3.5), 4.0 (4) | main 5.14 | 5/77 | qa/reports/B114_pairing_relaxed.md | paper_B_draft1.md line 270 | pass |
| 1 (1), 2 (2) | main 5.14 | 5/29 | literature register L016 | paper_B_draft1.md line 272 | pass |
| 81.7 (81.7), 93 (93.1), 81 (80.9) | main 5.14 | 5/79 | analysis/pasture_2025/pairing_relaxed.csv | paper_B_draft1.md line 272 | pass |
| 64.8 (64.8), 84.6 (84.6), 53.9 (53.9), 77.9 (77.9) | main 5.14 | 5/Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 272 | pass |
| 76.0 (76) | main 5.14 | 5/Table 5 row 4 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 272 | pass |
| 107.7 (107.69), 0.5 (45), 0.6 (561), 0.6 (561) | main 5.14 | 5/81 | analysis/pasture_2025/pairing_relaxed.csv | paper_B_draft1.md line 272 | pass |
| 4.2 (4.2) | main 5.14 | 5/81 | qa/reports/B114_pairing_relaxed.md | paper_B_draft1.md line 272 | pass |
| 82 (81.7), 108 (107.69) | main 5.14 | 5/84 | analysis/pasture_2025/pairing_relaxed.csv | paper_B_draft1.md line 272 | pass |
| 134 (133.8) | main 5.14 | 5/14 | register B019 | paper_B_draft1.md line 272 | pass |
| 343 (343.4) | main 5.14 | 5/21 | register B046 | paper_B_draft1.md line 272 | pass |
| 53.6 (5.36437e+07) | main 5.14 | 5/Table 4 row 4 | results/ranges_2025-improved_wide.csv | paper_B_draft1.md line 272 | pass |
| 76.0 (76) | main 5.14 | 5/Table 5 row 4 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 274 | pass |
| 41.5 (41.5) | main 5.14 | 5/41 | register B137 | paper_B_draft1.md line 274 | pass |
| 34.5 (34.46) | main 5.14 | 5/B141b-29 | analysis/method_tests_2025/bridge_half_to_model.csv | paper_B_draft1.md line 274 | pass |
| 22.6 (22.65), 13.0 (13), 6.4 (6.36), 4.4 (4.42), 17.9 (17.9), 36.2 (36.21) | main 5.14 | 5/B141b-30 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 274 | pass |
| 6.3 (0.063) | main 5.14 | 5/62 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 274 | pass |
| 18 (1.8474e+07) | main 5.14 | 5/Table 4 row 4 | results/ranges_2025-improved_wide.csv | paper_B_draft1.md line 274 | pass |
| 60 (60), 113.6 (113.6) | main 5.14 | 5/B141b-31 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 274 | pass |
| 1 (1) | main 5.14 | 5/29 | literature register L016 | paper_B_draft1.md line 274 | pass |
| 85.4 (85.4) | main 5.14 | 5/B141b-32 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 274 | pass |
| 41.5 (41.5) | main 5.14 | 5/41 | register B137 | paper_B_draft1.md line 276 | pass |
| 100 (1) | main 5.14 | 5/12 | literature register L003 | paper_B_draft1.md line 276 | pass |
| 1 (1) | main 5.14 | 5/29 | literature register L016 | paper_B_draft1.md line 278 | pass |
| 64.8 (64.8), 84.6 (84.6) | main 5.14 | 5/Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 278 | pass |
| 76.0 (76) | main 5.14 | 5/Table 5 row 4 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 278 | pass |
| 3 (3) | main 5.14 | 5/21 | register B046 | paper_B_draft1.md line 278 | pass |
| 41.50 (41.5), 15.62 (15.62) | main 5.14 | 5/Table 7 row 1 | analysis/pasture_2025/pairing_relaxed.csv | paper_B_draft1.md line 280 | pass |
| 1 (1) | main 5.14 | 5/29 | literature register L016 | paper_B_draft1.md line 281 | pass |
| 81.70 (81.7), 93 (93.1) | main 5.14 | 5/79 | analysis/pasture_2025/pairing_relaxed.csv | paper_B_draft1.md line 281 | pass |
| 21.87 (21.87), 173 (173) | main 5.14 | 5/Table 7 row 2 | analysis/pasture_2025/pairing_relaxed.csv | paper_B_draft1.md line 281 | pass |
| 117 (117) | main 5.14 | 5/Table 5 row 3 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 281 | pass |
| 2 (2) | main 5.14 | 5/29 | literature register L016 | paper_B_draft1.md line 282 | pass |
| 3.79 (3.79), 12.0 (12), 21.90 (21.9), 284 (284), 192 (192), 154 (154) | main 5.14 | 5/Table 7 row 3 | analysis/pasture_2025/pairing_relaxed.csv | paper_B_draft1.md line 282 | pass |
| 3.5 (3.5), 4.0 (4) | main 5.14 | 5/77 | qa/reports/B114_pairing_relaxed.md | paper_B_draft1.md line 282 | pass |
| 107.69 (107.69) | main 5.14 | 5/81 | analysis/pasture_2025/pairing_relaxed.csv | paper_B_draft1.md line 282 | pass |
| 76.0 (76) | main 5.14 | 5/Table 5 row 4 | analysis/method_tests_2025/harmonised_comparison.csv | paper_B_draft1.md line 284 | pass |
| 41.5 (41.5) | main 5.14 | 5/41 | register B137 | paper_B_draft1.md line 284 | pass |
| 100 (1) | main 5.14 | 5/12 | literature register L003 | paper_B_draft1.md line 284 | pass |
| 16.4 (16.44), 7.376 (7.376) | main 5.14 | 5/B141b-25 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 284 | pass |
| 13.60 (13.6) | main 5.14 | 5/Table 7 row 3 | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 284 | pass |
| 8.0 (8) | main 5.14 | 5/Table 7 row 1 | qa/reports/B114_pairing_relaxed.md | paper_B_draft1.md line 284 | pass |
| 1.84 (184) | main 5.14 | 5/Table 7 row 3 | qa/reports/B126b_patch_paper_B.md | paper_B_draft1.md line 284 | pass |
| 5,040 (5040) | main 5.14 | 5/Table 7 panel B | analysis/method_tests_2025/bridge_half_to_model.csv | paper_B_draft1.md line 286 | pass |
| -6.99 (699) | main 5.14 | 5/Table 7 row 3 | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 288 | pass |
| -5.41 (5.41) | main 5.14 | 5/Table 7 panel B | analysis/method_tests_2025/bridge_half_to_model.csv | paper_B_draft1.md line 288 | pass |
| -6.34 (6.34) | main 5.14 | 5/B141b-30 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 288 | pass |
| 18 (1.8474e+07) | main 5.14 | 5/Table 4 row 4 | results/ranges_2025-improved_wide.csv | paper_B_draft1.md line 288 | pass |
| 13.60 (13.6) | main 5.14 | 5/Table 7 row 3 | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 289 | pass |
| 7.376 (7.376) | main 5.14 | 5/B141b-25 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 289 | pass |
| 64.06 (64.06), 18.43 (18.43) | main 5.14 | 5/Table 7 panel B | analysis/method_tests_2025/bridge_half_to_model.csv | paper_B_draft1.md line 289 | pass |
| 36.21 (36.21) | main 5.14 | 5/B141b-30 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 289 | pass |
| -105 (105) | main 5.14 | 5/Table 7 row 1 | analysis/pasture_2025/pairing_relaxed.csv | paper_B_draft1.md line 289 | pass |
| -20.69 (20.69), -13.78 (13.78) | main 5.14 | 5/Table 7 panel B | analysis/method_tests_2025/bridge_half_to_model.csv | paper_B_draft1.md line 290 | pass |
| -17.90 (17.9) | main 5.14 | 5/B141b-30 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 290 | pass |
| 52 (52) | main 5.14 | 5/Table 7 row 1 | results/ranges_2025-improved.csv | paper_B_draft1.md line 290 | pass |
| -27.24 (27.24) | main 5.14 | 5/Table 7 panel B | analysis/method_tests_2025/bridge_half_to_model.csv | paper_B_draft1.md line 291 | pass |
| -19.96 (1996) | main 5.14 | 5/Table 7 row 3 | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 291 | pass |
| -22.65 (22.65) | main 5.14 | 5/B141b-30 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 291 | pass |
| 66 (66.18) | main 5.14 | 5/Table 7 row 1 | analysis/pasture_2025/pairing_relaxed.csv | paper_B_draft1.md line 291 | pass |
| -12.66 (12.66) | main 5.14 | 5/Table 7 panel B | analysis/method_tests_2025/bridge_half_to_model.csv | paper_B_draft1.md line 292 | pass |
| -0.67 (672637) | main 5.14 | 5/Table 7 row 1 | results/ranges_2025-improved.csv | paper_B_draft1.md line 292 | pass |
| -6.41 (6.41) | main 5.14 | 5/B141b-30 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 292 | pass |
| 19 (19) | main 5.14 | 5/Table 6 caption | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 292 | pass |
| -16.91 (16.91), -10.53 (10.53) | main 5.14 | 5/Table 7 panel B | analysis/method_tests_2025/bridge_half_to_model.csv | paper_B_draft1.md line 293 | pass |
| -12.96 (12.96) | main 5.14 | 5/B141b-30 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 293 | pass |
| 38 (38.5) | main 5.14 | 5/B141b-26 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 293 | pass |
| -5.88 (5.88) | main 5.14 | 5/Table 7 panel B | analysis/method_tests_2025/bridge_half_to_model.csv | paper_B_draft1.md line 294 | pass |
| -2.32 (2.3168) | main 5.14 | 5/Table 7 row 3 | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 294 | pass |
| -4.42 (4.42) | main 5.14 | 5/B141b-30 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 294 | pass |
| 13 (1.33072e+07) | main 5.14 | 5/Table 4 caption | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 294 | pass |
| 75.97 (75.97), -34.46 (34.46) | main 5.14 | 5/B141b-29 | analysis/method_tests_2025/bridge_half_to_model.csv | paper_B_draft1.md line 295 | pass |
| 41.50 (41.5) | main 5.14 | 5/Table 7 row 1 | analysis/pasture_2025/pairing_relaxed.csv | paper_B_draft1.md line 295 | pass |
| 100 (1) | main 5.14 | 5/12 | literature register L003 | paper_B_draft1.md line 295 | pass |
| 100 (1) | main 6.1 | 6/4 | register B162 | paper_B_draft1.md line 306 | pass |
| 68 (68), 104 (103.6) | main 6.1 | 6/B141b-1 | analysis/comparators_2025/proportional_count.csv | paper_B_draft1.md line 306 | pass |
| 41.5 (41.5) | main 6.1 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 306 | pass |
| 2.41 (2.41) | main 6.1 | 6/6 | register B185 | paper_B_draft1.md line 306 | pass |
| 1.6 (1.58) | main 6.1 | 6/B141b-2 | analysis/method_tests_2025/design_choices_panels.csv | paper_B_draft1.md line 306 | pass |
| 2.5 (2.5) | main 6.1 | 6/21 | register B216 | paper_B_draft1.md line 306 | pass |
| 4.4 (4.43), 6.4 (6.36) | main 6.1 | 6/6 | register B186 | paper_B_draft1.md line 306 | pass |
| 2.47 (2.47) | main 6.1 | 6/B141b-3 | analysis/method_tests_2025/harmonised_robustness_footprint.csv | paper_B_draft1.md line 306 | pass |
| 1 (143) | main 6.1 | 6/26 | literature register L006 | paper_B_draft1.md line 306 | pass |
| 41.5 (41.5) | main 6.2 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 310 | pass |
| 53.6 (53.64), 1.29 (1.29) | main 6.2 | 6/9 | register B183 | paper_B_draft1.md line 310 | pass |
| 12 (12), 55.3 (55.3), 1.33 (1.33) | main 6.3 | 6/11 | register B168 | paper_B_draft1.md line 314 | pass |
| 41.5 (41.5) | main 6.3 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 314 | pass |
| 53.6 (53.64) | main 6.3 | 6/9 | register B183 | paper_B_draft1.md line 314 | pass |
| 62.9 (62.9), 1.17 (1.17) | main 6.3 | 6/12 | register B169 | paper_B_draft1.md line 314 | pass |
| 70 (70), 70 (70) | main 6.4 | 6/13 | analysis/waste_2025/README.md | paper_B_draft1.md line 318 | pass |
| 40.5 (40.5), 1.73 (1.73) | main 6.4 | 6/15 | register B232 | paper_B_draft1.md line 318 | pass |
| 41.5 (41.5) | main 6.4 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 318 | pass |
| 45.1 (45.12), 1.09 (1.09) | main 6.4 | 6/17 | register B170 | paper_B_draft1.md line 318 | pass |
| 9 (8.7) | main 6.4 | 6/18 | register B109 | paper_B_draft1.md line 318 | pass |
| 58.3 (58.31) | main 6.4 | 6/18 | register B107 | paper_B_draft1.md line 318 | pass |
| 15 (15), 48.3 (48.3) | main 6.5 | 6/19 | register B178 | paper_B_draft1.md line 322 | pass |
| 5 (5), 103.3 (103.3), 5 (5), 103.3 (103.3) | main 6.5 | 6/19 | analysis/comparators_2025/diet_land.csv | paper_B_draft1.md line 322 | pass |
| 2.14 (2.14) | main 6.5 | 6/19 | register B181 | paper_B_draft1.md line 322 | pass |
| 53.6 (53.64) | main 6.5 | 6/9 | register B183 | paper_B_draft1.md line 322 | pass |
| 85.5 (85.5), 1.60 (1.6), 202.1 (202.1), 3.77 (3.77) | main 6.5 | 6/B141b-4 | analysis/method_tests_2025/design_choices_panels.csv | paper_B_draft1.md line 322 | pass |
| 422.3 (422.3) | main 6.5 | 6/20 | register B180 | paper_B_draft1.md line 322 | pass |
| 7.88 (7.88) | main 6.5 | 6/20 | register B182 | paper_B_draft1.md line 322 | pass |
| 2.5 (2.5), 7.5 (7.5), 66.9 (66.9) | main 6.5 | 6/21 | register B216 | paper_B_draft1.md line 322 | pass |
| 50 (50), 23 (23.2), 30 (29.9), 19 (19.1), 25 (24.7), 30 (29.9) | main 6.6 | 6/24 | register B199 | paper_B_draft1.md line 326 | pass |
| 100 (1), 100 (1), 100 (1), 100 (1) | main 6.6 | 6/4 | register B162 | paper_B_draft1.md line 326 | pass |
| 41.5 (41.5) | main 6.6 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 326 | pass |
| 18.9 (18.9), 2.19 (2.19) | main 6.6 | 6/25 | register B167 | paper_B_draft1.md line 326 | pass |
| 41.2 (4.11915e+07), 41.0 (4.09877e+07), 40.4 (4.04496e+07), 10 (10), 20 (20), 1.03 (1.026), 24.7 (2.46819e+07) | main 6.6 | 6/B141b-5 | analysis/resilience_2025/drought_bounds_paper_B.csv | paper_B_draft1.md line 326 | pass |
| 1 (143), 1 (143), 1 (143), 1 (143), 1 (143) | main 6.6 | 6/26 | literature register L006 | paper_B_draft1.md line 326 | pass |
| 15.6 (15.6) | main 6.6 | 6/37 | register B184 | paper_B_draft1.md line 326 | pass |
| 41.5 (41.5) | main 6.7 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 330 | pass |
| 75 (0.754) | main 6.7 | 6/29 | register B171 | paper_B_draft1.md line 330 | pass |
| 37 (0.374) | main 6.7 | 6/29 | register B175 | paper_B_draft1.md line 330 | pass |
| 15.5 (15.5) | main 6.7 | 6/30 | register B176 | paper_B_draft1.md line 330 | pass |
| 2.67 (2.67) | main 6.7 | 6/31 | register B177 | paper_B_draft1.md line 330 | pass |
| 54 (0.539) | main 6.7 | 6/33 | register A098 | paper_B_draft1.md line 330 | pass |
| 100 (1) | main 6.8 | 6/4 | register B162 | paper_B_draft1.md line 334 | pass |
| 30 (29.9) | main 6.8 | 6/24 | register B199 | paper_B_draft1.md line 334 | pass |
| 15.6 (15.6), 2.66 (2.66) | main 6.8 | 6/37 | register B184 | paper_B_draft1.md line 334 | pass |
| 41.5 (41.5) | main 6.8 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 334 | pass |
| 2,000 (20) | main 6.9 | 6/41 | analysis/sensitivity_2025/sobol_2025-fixed.csv | paper_B_draft1.md line 338 | pass |
| 19 (19.1) | main 6.9 | 6/24 | register B199 | paper_B_draft1.md line 338 | pass |
| 18 (18) | main 6.9 | 6/41 | qa/reports/B115_monte_carlo_widened.md | paper_B_draft1.md line 338 | pass |
| 31.1 (3.11154e+07), 49.2 (4.91698e+07), 1.58 (1.58), 13.3 (1.33072e+07), 18.8 (1.87656e+07) | main 6.9 | 6/41 | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 338 | pass |
| 5 (5) | main 6.9 | 6/19 | analysis/comparators_2025/diet_land.csv | paper_B_draft1.md line 338 | pass |
| 95 (94635) | main 6.9 | 6/41 | results/ranges_2025-fixed.csv | paper_B_draft1.md line 338 | pass |
| 39.0 (3.89946e+07) | main 6.9 | 6/43 | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 338 | pass |
| 32 (0.3186), 27 (0.2706), 24 (0.237) | main 6.9 | 6/45 | analysis/sensitivity_2025/sobol_2025-fixed.csv | paper_B_draft1.md line 338 | pass |
| 20 (20) | main 6.9 | 6/B141b-5 | analysis/resilience_2025/drought_bounds_paper_B.csv | paper_B_draft1.md line 338 | pass |
| 33.4 (3.3431e+07), 49.5 (4.94666e+07) | main 6.9 | 6/B141b-7 | analysis/pasture_2025/pasture_output_one_at_a_time_2025-fixed.csv | paper_B_draft1.md line 338 | pass |
| 41.5 (41.5) | main 6.10 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 342 | pass |
| 100 (1), 100 (1) | main 6.10 | 6/4 | register B162 | paper_B_draft1.md line 342 | pass |
| 18.9 (18.9) | main 6.10 | 6/25 | register B167 | paper_B_draft1.md line 342 | pass |
| 40.4 (4.04496e+07) | main 6.10 | 6/B141b-5 | analysis/resilience_2025/drought_bounds_paper_B.csv | paper_B_draft1.md line 342 | pass |
| 55.3 (55.3) | main 6.10 | 6/11 | register B168 | paper_B_draft1.md line 342 | pass |
| 62.9 (62.9) | main 6.10 | 6/12 | register B169 | paper_B_draft1.md line 342 | pass |
| 9.4 (9.4) | main 6.10 | 6/50 | register B005 | paper_B_draft1.md line 342 | pass |
| 1.03 (1.026), 20 (20) | main 6.11 | 6/B141b-5 | analysis/resilience_2025/drought_bounds_paper_B.csv | paper_B_draft1.md line 348 | pass |
| 1.09 (1.09) | main 6.11 | 6/17 | register B170 | paper_B_draft1.md line 348 | pass |
| 1.58 (1.58) | main 6.11 | 6/41 | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 348 | pass |
| 1.17 (1.17) | main 6.11 | 6/12 | register B169 | paper_B_draft1.md line 348 | pass |
| 1.33 (1.33) | main 6.11 | 6/11 | register B168 | paper_B_draft1.md line 348 | pass |
| 1.27 (1.27), 1.48 (1.48) | main 6.11 | 6/B141b-10 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 348 | pass |
| 1.60 (1.6), 3.77 (3.77) | main 6.11 | 6/B141b-4 | analysis/method_tests_2025/design_choices_panels.csv | paper_B_draft1.md line 348 | pass |
| 2.14 (2.14) | main 6.11 | 6/19 | register B181 | paper_B_draft1.md line 348 | pass |
| 2.19 (2.19) | main 6.11 | 6/25 | register B167 | paper_B_draft1.md line 348 | pass |
| 2.67 (2.67) | main 6.11 | 6/31 | register B177 | paper_B_draft1.md line 348 | pass |
| 1.29 (1.29) | main 6.11 | 6/9 | register B183 | paper_B_draft1.md line 348 | pass |
| 2.66 (2.66) | main 6.11 | 6/37 | register B184 | paper_B_draft1.md line 348 | pass |
| 7.88 (7.88) | main 6.11 | 6/20 | register B182 | paper_B_draft1.md line 348 | pass |
| 100 (1) | main 6.11 | 6/4 | register B162 | paper_B_draft1.md line 356 | pass |
| 40.4 (4.04496e+07), 1.03 (1.026) | main 6.11 | 6/B141b-5 | analysis/resilience_2025/drought_bounds_paper_B.csv | paper_B_draft1.md line 356 | pass |
| 41.5 (41.5) | main 6.11 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 356 | pass |
| 41.5 (41.5) | main 6.11 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 357 | pass |
| 45.1 (45.12), 1.09 (1.09) | main 6.11 | 6/17 | register B170 | paper_B_draft1.md line 357 | pass |
| 12 (12) | main 6.11 | 6/11 | register B168 | paper_B_draft1.md line 358 | pass |
| 53.6 (53.64) | main 6.11 | 6/9 | register B183 | paper_B_draft1.md line 358 | pass |
| 62.9 (62.9), 1.17 (1.17) | main 6.11 | 6/12 | register B169 | paper_B_draft1.md line 358 | pass |
| 1.4 (1.4), 1.8 (1.8) | main 6.11 | 6/46 | qa/reports/B115_monte_carlo_widened.md | paper_B_draft1.md line 359 | pass |
| 8.0 (8), 10.3 (10.3) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 359 | pass |
| 32.7 (0.327) | main 6.11 | 6/Table 8 row 13 | qa/reports/V41_check_B115.md | paper_B_draft1.md line 359 | pass |
| 41.5 (41.5) | main 6.11 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 359 | pass |
| 1.27 (1.27) | main 6.11 | 6/B141b-10 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 359 | pass |
| 12 (12), 55.3 (55.3), 1.33 (1.33) | main 6.11 | 6/11 | register B168 | paper_B_draft1.md line 360 | pass |
| 41.5 (41.5) | main 6.11 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 360 | pass |
| 20 (20), 20 (20) | main 6.11 | 6/B141b-5 | analysis/resilience_2025/drought_bounds_paper_B.csv | paper_B_draft1.md line 361 | pass |
| 33.4 (3.3431e+07), 49.5 (4.94666e+07) | main 6.11 | 6/B141b-7 | analysis/pasture_2025/pasture_output_one_at_a_time_2025-fixed.csv | paper_B_draft1.md line 361 | pass |
| 1.48 (1.48) | main 6.11 | 6/B141b-10 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 361 | pass |
| 53.6 (53.64) | main 6.11 | 6/9 | register B183 | paper_B_draft1.md line 362 | pass |
| 85.5 (85.5), 1.60 (1.6) | main 6.11 | 6/B141b-4 | analysis/method_tests_2025/design_choices_panels.csv | paper_B_draft1.md line 362 | pass |
| 1.2 (1.23), 2.2 (2.2) | main 6.11 | 6/46 | qa/reports/B115_monte_carlo_widened.md | paper_B_draft1.md line 363 | pass |
| 6.9 (6.9) | main 6.11 | 6/47 | qa/reports/B126b_patch_paper_B.md | paper_B_draft1.md line 363 | pass |
| 12.6 (12.6) | main 6.11 | 6/Table 8 panels | analysis/method_tests_2025/design_choices_panels.csv | paper_B_draft1.md line 363 | pass |
| 35.2 (3525), 61.8 (0.618) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 363 | pass |
| 1.76 (1.76) | main 6.11 | 6/B141b-10 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 363 | pass |
| 1.2 (1.23), 2.2 (2.2) | main 6.11 | 6/46 | qa/reports/B115_monte_carlo_widened.md | paper_B_draft1.md line 364 | pass |
| 6.9 (6.9) | main 6.11 | 6/47 | qa/reports/B126b_patch_paper_B.md | paper_B_draft1.md line 364 | pass |
| 12.6 (12.6) | main 6.11 | 6/Table 8 panels | analysis/method_tests_2025/design_choices_panels.csv | paper_B_draft1.md line 364 | pass |
| 26.9 (26.929) | main 6.11 | 6/B141b-10 | qa/reports/V53_check_B139.md | paper_B_draft1.md line 364 | pass |
| 48.0 (48) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 364 | pass |
| 1.78 (1.78) | main 6.11 | 6/B141b-10 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 364 | pass |
| 15 (15), 48.3 (48.3) | main 6.11 | 6/19 | register B178 | paper_B_draft1.md line 365 | pass |
| 5 (5), 103.3 (103.3) | main 6.11 | 6/19 | analysis/comparators_2025/diet_land.csv | paper_B_draft1.md line 365 | pass |
| 2.14 (2.14) | main 6.11 | 6/19 | register B181 | paper_B_draft1.md line 365 | pass |
| 100 (1) | main 6.11 | 6/4 | register B162 | paper_B_draft1.md line 366 | pass |
| 18.9 (18.9), 2.19 (2.19) | main 6.11 | 6/25 | register B167 | paper_B_draft1.md line 366 | pass |
| 41.5 (41.5) | main 6.11 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 366 | pass |
| 15.5 (15.5) | main 6.11 | 6/30 | register B176 | paper_B_draft1.md line 367 | pass |
| 41.5 (41.5) | main 6.11 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 367 | pass |
| 2.67 (2.67) | main 6.11 | 6/31 | register B177 | paper_B_draft1.md line 367 | pass |
| 53.6 (53.64) | main 6.11 | 6/9 | register B183 | paper_B_draft1.md line 368 | pass |
| 202.1 (202.1), 3.77 (3.77) | main 6.11 | 6/B141b-4 | analysis/method_tests_2025/design_choices_panels.csv | paper_B_draft1.md line 368 | pass |
| 41.5 (41.5) | main 6.11 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 369 | pass |
| 53.6 (53.64), 1.29 (1.29) | main 6.11 | 6/9 | register B183 | paper_B_draft1.md line 369 | pass |
| 15.6 (15.6), 2.66 (2.66) | main 6.11 | 6/37 | register B184 | paper_B_draft1.md line 370 | pass |
| 41.5 (41.5) | main 6.11 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 370 | pass |
| 0.06 (55.3) | main 6.11 | 6/Figure 3 placeholder | analysis/method_tests_2025/ladder.csv | paper_B_draft1.md line 371 | pass |
| 0.13 (13) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 371 | pass |
| 53.6 (53.64) | main 6.11 | 6/9 | register B183 | paper_B_draft1.md line 371 | pass |
| 422.3 (422.3) | main 6.11 | 6/20 | register B180 | paper_B_draft1.md line 371 | pass |
| 7.88 (7.88) | main 6.11 | 6/20 | register B182 | paper_B_draft1.md line 371 | pass |
| 5 (5) | main 6.11 | 6/19 | analysis/comparators_2025/diet_land.csv | paper_B_draft1.md line 372 | pass |
| 95 (94635) | main 6.11 | 6/41 | results/ranges_2025-fixed.csv | paper_B_draft1.md line 372 | pass |
| 19 (19.1) | main 6.11 | 6/24 | register B199 | paper_B_draft1.md line 372 | pass |
| 18 (18) | main 6.11 | 6/41 | qa/reports/B115_monte_carlo_widened.md | paper_B_draft1.md line 372 | pass |
| 31.1 (3.11154e+07), 49.2 (4.91698e+07), 1.58 (1.58) | main 6.11 | 6/41 | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 372 | pass |
| 5 (5) | main 6.11 | 6/19 | analysis/comparators_2025/diet_land.csv | paper_B_draft1.md line 373 | pass |
| 95 (94635) | main 6.11 | 6/41 | results/ranges_2025-fixed.csv | paper_B_draft1.md line 373 | pass |
| 18 (18) | main 6.11 | 6/41 | qa/reports/B115_monte_carlo_widened.md | paper_B_draft1.md line 373 | pass |
| 37.9 (37.9), 60.0 (60) | main 6.11 | 6/Figure 3 placeholder | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 373 | pass |
| 1.58 (1.58) | main 6.11 | 6/41 | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 373 | pass |
| 27 (0.2706) | main 6.11 | 6/45 | analysis/sensitivity_2025/sobol_2025-fixed.csv | paper_B_draft1.md line 379 | pass |
| 63 (62.9), 100.0 (100) | main 6.11 | 6/Figure 3 placeholder | analysis/method_tests_2025/ladder.csv | paper_B_draft1.md line 379 | pass |
| 41.5 (41.5) | main 6.11 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 379 | pass |
| 2.41 (2.41) | main 6.11 | 6/6 | register B185 | paper_B_draft1.md line 379 | pass |
| 68.0 (68), 70.1 (70.1), 101.2 (101.2), 103.6 (103.6) | main 6.11 | 6/B141b-1 | analysis/comparators_2025/proportional_count.csv | paper_B_draft1.md line 380 | pass |
| 1.64 (1.64), 2.50 (2.5) | main 6.11 | 6/B141b-2 | analysis/method_tests_2025/design_choices_panels.csv | paper_B_draft1.md line 380 | pass |
| 1.69 (1.69), 2.44 (2.44) | main 6.11 | 6/B141b-10 | qa/reports/V53_check_B139.md | paper_B_draft1.md line 380 | pass |
| 45.9 (45.9) | main 6.11 | 6/B141b-10 | qa/reports/B139_paper_B_third_line_bridge_panels.md | paper_B_draft1.md line 381 | pass |
| 53.9 (0.539), 1.11 (110.9), 1.30 (129.7) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 381 | pass |
| 41.5 (41.5) | main 6.11 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 382 | pass |
| 183.9 (183.9) | main 6.11 | 6/5 | register B165 | paper_B_draft1.md line 382 | pass |
| 4.43 (4.43) | main 6.11 | 6/B141b-2 | analysis/method_tests_2025/design_choices_panels.csv | paper_B_draft1.md line 382 | pass |
| 41.5 (41.5) | main 6.11 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 383 | pass |
| 263.9 (263.9) | main 6.11 | 6/5 | register B165 | paper_B_draft1.md line 383 | pass |
| 6.36 (6.36) | main 6.11 | 6/B141b-2 | analysis/method_tests_2025/design_choices_panels.csv | paper_B_draft1.md line 383 | pass |
| 1 (143) | main 6.11 | 6/26 | literature register L006 | paper_B_draft1.md line 384 | pass |
| 4.29 (4.29) | main 6.11 | 6/B141b-10 | qa/reports/V53_check_B139.md | paper_B_draft1.md line 384 | pass |
| 2.06 (205.962) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 384 | pass |
| 2.47 (2.47) | main 6.11 | 6/B141b-3 | analysis/method_tests_2025/harmonised_robustness_footprint.csv | paper_B_draft1.md line 384 | pass |
| 3 (3) | main 6.11 | 6/44 | analysis/sensitivity_2025/sobol_2025-fixed.csv | paper_B_draft1.md line 385 | pass |
| 4.47 (4.47), 2.97 (2.97) | main 6.11 | 6/B141b-10 | qa/reports/V53_check_B139.md | paper_B_draft1.md line 385 | pass |
| 3.23 (323) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 385 | pass |
| 30 (29.9) | main 6.11 | 6/24 | register B199 | paper_B_draft1.md line 391 | pass |
| 60 (60) | main 6.11 | 7/19 | register B243 | paper_B_draft1.md line 391 | pass |
| 2.0 (2011) | main 6.11 | 6/Figure 3 placeholder | analysis/method_tests_2025/ladder.csv | paper_B_draft1.md line 391 | pass |
| 60 (60) | main 6.11 | 7/19 | register B243 | paper_B_draft1.md line 392 | pass |
| 82 (81.7), 1.37 (137.2) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 392 | pass |
| 50 (50), 30 (29.9), 50 (50) | main 6.11 | 6/24 | register B199 | paper_B_draft1.md line 393 | pass |
| 35 (35), 35 (35) | main 6.11 | 6/Figure 3 placeholder | analysis/method_tests_2025/ladder.csv | paper_B_draft1.md line 393 | pass |
| 1.43 (143) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 393 | pass |
| 1.67 (1.67) | main 6.11 | 6/B141b-10 | qa/reports/V53_check_B139.md | paper_B_draft1.md line 393 | pass |
| 402 (402), 807 (807) | main 6.11 | 6/B141b-10 | qa/reports/V53_check_B139.md | paper_B_draft1.md line 394 | pass |
| 2.01 (2011) | main 6.11 | 6/Figure 3 placeholder | analysis/method_tests_2025/ladder.csv | paper_B_draft1.md line 394 | pass |
| 42 (41.5) | main 6.11 | 6/Figure 3 placeholder | analysis/method_tests_2025/ladder.csv | paper_B_draft1.md line 395 | pass |
| 2.03 (2.03), 2.04 (204) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 395 | pass |
| 6.08 (6.08), 2.98 (2.98) | main 6.11 | 6/B141b-10 | qa/reports/V53_check_B139.md | paper_B_draft1.md line 395 | pass |
| 6.0 (6), 10.1 (10.1) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 396 | pass |
| 1.68 (1.68) | main 6.11 | 6/B141b-10 | qa/reports/V53_check_B139.md | paper_B_draft1.md line 396 | pass |
| 1.0 (100) | main 6.11 | 6/Figure 3 placeholder | analysis/method_tests_2025/ladder.csv | paper_B_draft1.md line 397 | pass |
| 1.7 (165), 1.7 (165) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 397 | pass |
| 35.13 (35.13), 112.2 (112.2) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 398 | pass |
| 3.19 (3.19) | main 6.11 | 6/B141b-10 | qa/reports/V53_check_B139.md | paper_B_draft1.md line 398 | pass |
| 1.8 (1.8) | main 6.11 | 6/46 | qa/reports/B115_monte_carlo_widened.md | paper_B_draft1.md line 399 | pass |
| 5.96 (5.96) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 399 | pass |
| 3.31 (3.31) | main 6.11 | 6/B141b-10 | qa/reports/V53_check_B139.md | paper_B_draft1.md line 399 | pass |
| 9.0 (9), 14.0 (14) | main 6.11 | 6/Figure 3 placeholder | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 400 | pass |
| 1.56 (1.56) | main 6.11 | 9/4 | analysis/method_tests_2025/cross_method_local.csv | paper_B_draft1.md line 400 | pass |
| 40.5 (40.5), 40.5 (40.5), 1.73 (1.73) | main 6.11 | 6/15 | register B232 | paper_B_draft1.md line 401 | pass |
| 70 (70), 70 (70), 70 (70) | main 6.11 | 6/13 | analysis/waste_2025/README.md | paper_B_draft1.md line 401 | pass |
| 70 (70) | main 6.11 | 6/13 | analysis/waste_2025/README.md | paper_B_draft1.md line 403 | pass |
| 40.5 (40.5) | main 6.11 | 6/15 | register B232 | paper_B_draft1.md line 403 | pass |
| 25 (25), 28 (28) | main 7.1 | 7/5 | qa/reports/V28_section7_matrix.md | paper_B_draft1.md line 409 | pass |
| 1 (0.8) | main 7.1 | 7/Table 9 row 1 | papers/B_methods/SECTION7_DRAFT.md | paper_B_draft1.md line 415 | pass |
| 2 (2) | main 7.1 | 7/11 | register B239 | paper_B_draft1.md line 416 | pass |
| 9 (9), 100 (1) | main 7.1 | 7/Table 9 row 2 | papers/B_methods/SECTION7_DRAFT.md | paper_B_draft1.md line 416 | pass |
| 3 (3) | main 7.1 | 7/Table 9 row 3 | papers/B_methods/SECTION7_DRAFT.md | paper_B_draft1.md line 417 | pass |
| 4 (4) | main 7.1 | 7/Table 9 row 4 | papers/B_methods/SECTION7_DRAFT.md | paper_B_draft1.md line 418 | pass |
| 15.5 (15.5) | main 7.3 | 7/11 | register B176 | paper_B_draft1.md line 426 | pass |
| 62.9 (62.9) | main 7.3 | 7/11 | analysis/method_tests_2025/ladder.csv | paper_B_draft1.md line 426 | pass |
| 100 (1) | main 7.3 | 7/Table 9 row 2 | papers/B_methods/SECTION7_DRAFT.md | paper_B_draft1.md line 426 | pass |
| 30 (30), 32 (32) | main 7.3 | 7/11 | register B222 | paper_B_draft1.md line 426 | pass |
| 2.4 (2.4) | main 7.5 | 7/16 | register B067 | paper_B_draft1.md line 434 | pass |
| 1.09 (1.09) | main 7.7 | 6/17 | register B170 | paper_B_draft1.md line 442 | pass |
| 31 (30.81) | main 7.7 | 7/24 | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 442 | pass |
| 100 (1), 11 (11), 28 (28) | main 8.2 | 8/8 | literature register L180 | paper_B_draft1.md line 458 | pass |
| 0.43 (0.43), 16 (15.9) | main 8.3 | 8/10 | register B047 | paper_B_draft1.md line 462 | pass |
| 3.8 (3.79), 3.5 (3.5), 4.0 (4) | main 8.4 | 8/14 | qa/reports/B114_pairing_relaxed.md | paper_B_draft1.md line 466 | pass |
| 12 (11.9495) | main 8.4 | 8/20 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 466 | pass |
| 107.7 (107.69), 41.5 (41.5) | main 8.4 | 8/14 | analysis/pasture_2025/pairing_relaxed.csv | paper_B_draft1.md line 466 | pass |
| 697 (697) | main 8.5 | 8/15 | ERRATA.md | paper_B_draft1.md line 470 | pass |
| 0.312 (0.312) | main 8.6 | 8/20 | register B035 | paper_B_draft1.md line 474 | pass |
| 0.074 (0.074), 0.142 (14.2) | main 8.6 | 8/20 | analysis/method_tests_2025/fidelity.csv | paper_B_draft1.md line 474 | pass |
| 0.854 (0.854) | main 8.6 | 8/20 | register B261 | paper_B_draft1.md line 474 | pass |
| -1 (1) | main 9.1 | 9/4 | analysis/pasture_2025/pairing_relaxed.csv | paper_B_draft1.md line 484 | pass |
| 8 (8) | main 9.1 | 6/50 | qa/reports/V45b_read_paper_B.md | paper_B_draft1.md line 484 | pass |
| 38.5 (0.385) | main 9.1 | 9/3 | analysis/method_tests_2025/harmonised_comparison_lines.csv | paper_B_draft1.md line 484 | pass |
| 41.5 (41.5) | main 9.2 | 6/6 | analysis/method_tests_2025/design_choices.csv | paper_B_draft1.md line 488 | pass |
| 100 (1) | main 9.2 | 9/6 | register B162 | paper_B_draft1.md line 488 | pass |
| 18.9 (18.9), 55.3 (55.3) | main 9.2 | 9/6 | register B003 | paper_B_draft1.md line 488 | pass |
| 62.9 (62.9) | main 9.2 | 9/6 | register B108 | paper_B_draft1.md line 488 | pass |
| 1.58 (1.58) | main 9.2 | 9/7 | results/ranges_2025-fixed_wide.csv | paper_B_draft1.md line 488 | pass |
| 5 (5.08) | main 9.2 | 9/4 | analysis/method_tests_2025/cross_method_local.csv | paper_B_draft1.md line 488 | pass |
| 95 (95) | main 9.2 | 9/7 | qa/reports/B115_monte_carlo_widened.md | paper_B_draft1.md line 488 | pass |
| 4.0 (4) | main 9.4 | 9/14 | LICENSE-DATA.md | paper_B_draft1.md line 496 | pass |
| 18 (18) | main 9.4 | 9/13 | qa/reports/B126b_patch_paper_B.md | paper_B_draft1.md line 496 | pass |
| 6 (6) | supp S1 | S3/28 | register B073 | supplementary.md line 11 | pass |
| 70 (70) | supp S2.2 | S2/7 | register B010 | supplementary.md line 29 | pass |
| 60 (60) | supp S2.4 | S6/1 | register B243 | supplementary.md line 37 | pass |
| 66 (66) | supp S2.4 | S2/11 | literature register L105 | supplementary.md line 37 | pass |
| 9.0 (9) | supp S2.5 | S2/13 | register B337 | supplementary.md line 41 | pass |
| 14.0 (14) | supp S2.5 | S2/13 | register B338 | supplementary.md line 41 | pass |
| 3.4 (3.4) | supp S2.9 | S2/B141b-2 | literature register L083 | supplementary.md line 57 | pass |
| 10.2 (10.2), 10.2 (10.2) | supp S2.9 | S2/37 | literature register L083 | supplementary.md line 57 | pass |
| 363.5 (363.5), 0.01 (1) | supp S3 | S3/2 | register B262 | supplementary.md line 65 | pass |
| 17.3 (17.3), 38.2 (38.2) | supp S3 | S3/B141b-4 | analysis/sensitivity_2025/README.md | supplementary.md line 65 | pass |
| 26.20 (26.2) | supp S3 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 65 | pass |
| 404 (404), 10 (10), 306 (306), 10 (10) | supp S3.1 | S3/3 | register B012 | supplementary.md line 69 | pass |
| 0.1760 (0.176) | supp S3.1 | S3/4 | register B014 | supplementary.md line 69 | pass |
| 0 (0) | supp S3.1 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 69 | pass |
| 70 (70), 45.7 (45.7) | supp S3.1 | S3/5 | register B013 | supplementary.md line 69 | pass |
| 134 (133.8), 138 (137.6), 134 (133.8) | supp S3.1 | S3/8 | register B016 | supplementary.md line 71 | pass |
| 211 (210.7), 211 (210.7), 205 (204.9), 211 (210.7) | supp S3.1 | S3/8 | register B018 | supplementary.md line 71 | pass |
| 161 (160.6), 156 (156), 59.95 (59.95) | supp S3.1 | S3/8 | register B017 | supplementary.md line 71 | pass |
| 70 (70), 45.7 (45.7) | supp S3.1 | S3/5 | register B013 | supplementary.md line 71 | pass |
| 28.3 (28.3) | supp S3.1 | S3/9 | register B027 | supplementary.md line 71 | pass |
| 31 (31) | supp S3.1 | S3/10 | register B022 | supplementary.md line 71 | pass |
| 15.6 (15.6), 8.8 (8.8), 8.8 (8.8) | supp S3.1 | S3/11 | register B023 | supplementary.md line 71 | pass |
| 243 (243.2) | supp S3.1 | S3/11 | register B024 | supplementary.md line 71 | pass |
| 4306.0 (4306) | supp S3.2 | S3/12 | literature register L051 | supplementary.md line 75 | pass |
| 1 (1.2) | supp S3.2 | S3/17 | register B033 | supplementary.md line 75 | pass |
| 2 (1.758) | supp S3.2 | S3/17 | register B256 | supplementary.md line 75 | pass |
| 3 (3) | supp S3.2 | S3/19 | analysis/method_tests_2025/simpson_food.csv | supplementary.md line 75 | pass |
| 34 (34) | supp S3.2 | S3/15 | register B260 | supplementary.md line 75 | pass |
| 3 (3), 3 (3), 0.074 (0.074), 0.142 (14.2), 0.312 (0.312), 3 (3) | supp S3.2 | S3/19 | analysis/method_tests_2025/simpson_food.csv | supplementary.md line 77 | pass |
| 1.718 (1.7176), 1.758 (1.758), 2.3 (2.3) | supp S3.2 | S3/16 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 77 | pass |
| 1 (1.2), 1.737 (1.737), 1 (1.2), 1 (1.2) | supp S3.2 | S3/17 | register B033 | supplementary.md line 77 | pass |
| 1.2 (1.2) | supp S3.2 | S3/37 | register B326 | supplementary.md line 77 | pass |
| 2 (1.758), 2.385 (2.385), 36 (36), 2 (1.758) | supp S3.2 | S3/17 | register B256 | supplementary.md line 77 | pass |
| 0.116 (115.88), 21.6 (21.6), 0.098 (97.73), 0.094 (0.094), 0.095 (0.095) | supp S3.2 | S3/18 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 77 | pass |
| 2.165 (2.165) | supp S3.2 | S3/Table S6 row 8 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 77 | pass |
| 10.3 (10.3), 11.9 (11.9495), 0.014 (14.2), 0.032 (31.578), 0.127 (0.127), 0.854 (0.854) | supp S3.2 | S3/20 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 77 | pass |
| 66 (66), 90 (90) | supp S3.3 | S3/22 | register B061 | supplementary.md line 81 | pass |
| 2.2 (2.2) | supp S3.3 | S3/42 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 81 | pass |
| 0.8 (0.8), 3.3 (3.3), 4.6 (4.6), 7.2 (7.2), 30.2 (30.2), 2.8 (2.8), 8.4 (8.4), 3.4 (3.4), 3.0 (3), 4.1 (4.1), 8.4 (8.4) | supp S3.3 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 81 | pass |
| 3,364 (3364), 3,182 (3182), 118.88 (118.88), 6.0 (6), 5.7 (5.7), 121.59 (121.59) | supp S3.3 | S3/25 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 81 | pass |
| 94.7 (94.7) | supp S3.3 | S3/25 | qa/reports/V42_check_B116.md | supplementary.md line 81 | pass |
| 2 (1.758) | supp S3.3 | S3/17 | register B256 | supplementary.md line 81 | pass |
| 61 (61), 59 (59) | supp S3.4 | S3/27 | register B257 | supplementary.md line 85 | pass |
| 33 (33.3) | supp S3.4 | S3/27 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 85 | pass |
| 34 (34) | supp S3.4 | S3/15 | register B260 | supplementary.md line 85 | pass |
| 41 (41), 67 (67), 6 (6), 41 (41) | supp S3.4 | S3/28 | register B073 | supplementary.md line 85 | pass |
| 32 (3182) | supp S3.4 | S3/28 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 85 | pass |
| 22 (22), 22 (22) | supp S3.4 | S3/29 | analysis/method_tests_2025/cassidy_people_per_hectare.py | supplementary.md line 85 | pass |
| 42 (42), 25 (24.9) | supp S3.4 | S3/29 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 85 | pass |
| 5 (5.18), 5 (5.18) | supp S3.4 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 85 | pass |
| 1,061 (1061.4), 947 (947) | supp S3.4 | S3/29 | register B079 | supplementary.md line 85 | pass |
| 8 (8) | supp S3.4 | S3/30 | register B258 | supplementary.md line 85 | pass |
| 5.8 (5.78) | supp S3.4 | S3/33 | analysis/method_tests_2025/cassidy_matched.csv | supplementary.md line 87 | pass |
| 31.65 (31.65) | supp S3.4 | S3/33 | register B084 | supplementary.md line 87 | pass |
| 183 (183), 190 (190) | supp S3.4 | S3/33 | analysis/method_tests_2025/README.md | supplementary.md line 87 | pass |
| 3,525 (3525) | supp S3.4 | S3/34 | register B263 | supplementary.md line 89 | pass |
| 2,700 (2700) | supp S3.4 | S3/34 | register B087 | supplementary.md line 89 | pass |
| 0.766 (0.766) | supp S3.4 | S3/34 | register B273 | supplementary.md line 89 | pass |
| 22 (22), 22 (22) | supp S3.4 | S3/29 | analysis/method_tests_2025/cassidy_people_per_hectare.py | supplementary.md line 95 | pass |
| 11.3 (11.3) | supp S3.4 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 95 | pass |
| 2,700 (2700) | supp S3.4 | S3/34 | register B087 | supplementary.md line 95 | pass |
| 24.5 (24.5), 147 (147.4) | supp S3.4 | S3/B141b-6 | analysis/method_tests_2025/cassidy.csv | supplementary.md line 95 | pass |
| 145 (144.8) | supp S3.4 | S3/B141b-6 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 96 | pass |
| 5.8 (5.78) | supp S3.4 | S3/33 | analysis/method_tests_2025/cassidy_matched.csv | supplementary.md line 97 | pass |
| 6.0 (6) | supp S3.4 | S3/25 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 97 | pass |
| 31.65 (31.65) | supp S3.4 | S3/33 | register B084 | supplementary.md line 98 | pass |
| 190 (190) | supp S3.4 | S3/33 | analysis/method_tests_2025/README.md | supplementary.md line 98 | pass |
| 31.65 (31.65) | supp S3.4 | S3/33 | register B084 | supplementary.md line 99 | pass |
| 183 (183) | supp S3.4 | S3/33 | analysis/method_tests_2025/README.md | supplementary.md line 99 | pass |
| 3,525 (3525) | supp S3.4 | S3/34 | register B263 | supplementary.md line 100 | pass |
| 14.8 (14.8) | supp S3.4 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 100 | pass |
| 24.5 (24.5) | supp S3.4 | S3/B141b-6 | analysis/method_tests_2025/cassidy.csv | supplementary.md line 100 | pass |
| 112.9 (112.9) | supp S3.4 | S3/Table S7 row 10 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 100 | pass |
| 110.9 (110.9) | supp S3.4 | S3/Table S7 row 11 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 100 | pass |
| 31.578 (31.578), 3.514 (3.514), 0.223 (0.223) | supp S3.5 | S3/35 | register B140 | supplementary.md line 104 | pass |
| 31.95 (31.95), 3.47 (3.47) | supp S3.5 | S3/37 | register B141 | supplementary.md line 104 | pass |
| 1.2 (1.2), 1.2 (1.2) | supp S3.5 | S3/37 | register B326 | supplementary.md line 104 | pass |
| 52.6 (52.56), 4.66 (4.66), 0.29 (0.29) | supp S3.5 | S3/38 | register B145 | supplementary.md line 104 | pass |
| 0.24 (0.24) | supp S3.6 | S3/40 | register B121 | supplementary.md line 108 | pass |
| 1 (1.2), 1 (1.2) | supp S3.6 | S3/17 | register B033 | supplementary.md line 108 | pass |
| 5.8 (5.78) | supp S3.6 | S3/33 | analysis/method_tests_2025/cassidy_matched.csv | supplementary.md line 108 | pass |
| 6.1 (6.1) | supp S3.6 | S3/42 | register B130 | supplementary.md line 108 | pass |
| 16 (15.6) | supp S3.6 | S3/Table S5 row 16 | analysis/method_tests_2025/bases.csv | supplementary.md line 108 | pass |
| 17 (17) | supp S3.6 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 108 | pass |
| 1.5 (1.5) | supp S3.6 | S3/42 | register B132 | supplementary.md line 108 | pass |
| 2 (1.758) | supp S3.6 | S3/17 | register B256 | supplementary.md line 108 | pass |
| 41.4 (4.144e+07), 41.2 (4.11915e+07), 41.0 (4.09877e+07), 40.8 (4.07822e+07), 40.4 (4.04496e+07), 24.7 (2.46819e+07) | supp S3.6 | S3/B141b-7 | analysis/resilience_2025/drought_bounds_paper_B.csv | supplementary.md line 110 | pass |
| 1 (1.2), 1 (1.2), 1 (1.2), 1 (1.2), 1 (1.2), 1 (1.2), 1 (1.2) | supp S3.6 | S3/17 | register B033 | supplementary.md line 110 | pass |
| 5 (5.18), 5 (5.18) | supp S3.6 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 110 | pass |
| 10 (10) | supp S3.6 | S3/3 | register B012 | supplementary.md line 110 | pass |
| 20 (20), 20 (20) | supp S3.6 | S3/65 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 110 | pass |
| 50 (0.5) | supp S3.6 | S5/12 | qa/reports/V41_check_B115.md | supplementary.md line 110 | pass |
| 15.6 (15.6) | supp S3.6 | S3/11 | register B023 | supplementary.md line 110 | pass |
| 27.6 (27.6082) | supp S3.6 | S3/42 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 110 | pass |
| 93 (92.8) | supp S3.6 | S3/B141b-8 | qa/reports/V49_check_B134.md | supplementary.md line 110 | pass |
| 98 (98) | supp S3.6 | S3/35 | register B140 | supplementary.md line 110 | pass |
| 53.5 (53.5), 53.2 (53.2), 52.8 (52.8), 52.5 (52.5), 52.0 (52) | supp S3.6 | S3/B141b-9 | qa/reports/B134_paper_B_drought_bound_and_pasture.md | supplementary.md line 110 | pass |
| 0.1 (5) | supp S3.6 | S3/Table S6 caption | analysis/method_tests_2025/fidelity.csv | supplementary.md line 110 | pass |
| 0.4 (41.5) | supp S3.6 | S3/B141b-9 | register B134 | supplementary.md line 110 | pass |
| 5 (5.18), 5 (5.18) | supp S3.7 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 114 | pass |
| 0.8 (0.8), 3.3 (3.3), 4.6 (4.6), 7.2 (7.2) | supp S3.7 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 114 | pass |
| 2.2 (2.2) | supp S3.7 | S3/42 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 114 | pass |
| 2.3 (2.3) | supp S3.7 | S3/16 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 114 | pass |
| 1.2 (1.2) | supp S3.7 | S3/37 | register B326 | supplementary.md line 114 | pass |
| 22 (22) | supp S3.7 | S3/29 | analysis/method_tests_2025/cassidy_people_per_hectare.py | supplementary.md line 114 | pass |
| 37 (0.372) | supp S3.7 | S3/47 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 114 | pass |
| 0.92 (92) | supp S3.7 | S3/48 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 116 | pass |
| -0.38 (0.38), 0.6 (57), 5.76 (5.76), -9.2 (9.17), 8.47 (8.47), -13.2 (1317.52) | supp S3.7 | S3/49 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 116 | pass |
| 0.040 (4), 0.060 (60.45), 0.071 (70.5) | supp S3.7 | S3/51 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 116 | pass |
| 57 | supp S3.7 | S3/51 | analysis/method_tests_2025/README.md ("57% of 1991-92 milk consumption") (checked by hand) | supplementary.md line 116 | pass |
| 5 (5.18) | supp S3.7 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 118 | pass |
| 100 (1) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 118 | pass |
| 5 (5.18) | supp S3.7 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 120 | pass |
| 113.12 (113.12), 112.2 (112.2) | supp S3.7 | S3/Table S1 row 2 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 122 | pass |
| -0.92 (92) | supp S3.7 | S3/48 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 122 | pass |
| 0.8 (0.8) | supp S3.7 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 122 | pass |
| 1.129 (1.129), 1.165 (1.165), 112.74 (112.74) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 122 | pass |
| -0.38 (0.38), 0.6 (57) | supp S3.7 | S3/49 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 122 | pass |
| 3,364 (3364), 118.88 (118.88) | supp S3.7 | S3/25 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 123 | pass |
| 5.76 (5.76), -9.2 (9.17) | supp S3.7 | S3/49 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 123 | pass |
| 113.15 (113.15) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 124 | pass |
| 0.03 (2.5) | supp S3.7 | S5/B141b-20 | analysis/resilience_2025/drought_bounds_paper_B.csv | supplementary.md line 124 | pass |
| -0.1 (5) | supp S3.7 | S3/Table S6 caption | analysis/method_tests_2025/fidelity.csv | supplementary.md line 124 | pass |
| 113.11 (113.11) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 125 | pass |
| -0.01 (1) | supp S3.7 | S3/2 | register B262 | supplementary.md line 125 | pass |
| 0 (0) | supp S3.7 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 125 | pass |
| 13,009 (13009), 113.20 (113.2), 0.08 (8) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 126 | pass |
| -0.1 (5) | supp S3.7 | S3/Table S6 caption | analysis/method_tests_2025/fidelity.csv | supplementary.md line 126 | pass |
| 115.88 (115.88), 2.76 (2.76), -4.5 (4.5) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 127 | pass |
| 113.15 (113.15) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 128 | pass |
| 0.03 (2.5) | supp S3.7 | S5/B141b-20 | analysis/resilience_2025/drought_bounds_paper_B.csv | supplementary.md line 128 | pass |
| -0.1 (5) | supp S3.7 | S3/Table S6 caption | analysis/method_tests_2025/fidelity.csv | supplementary.md line 128 | pass |
| 121.59 (121.59) | supp S3.7 | S3/25 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 129 | pass |
| 8.47 (8.47), -13.2 (1317.52) | supp S3.7 | S3/49 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 129 | pass |
| 34.37 (34.37), 35.13 (35.13), 0.76 (0.76), 1.129 (1.129), 34.06 (34.06), -0.31 (0.31) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 130 | pass |
| 2.2 (2.2) | supp S3.7 | S3/42 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 130 | pass |
| 3,364 (3364) | supp S3.7 | S3/25 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 131 | pass |
| 35.76 (35.76), 1.39 (1.39) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 131 | pass |
| 34.88 (34.88), 0.51 (50.5) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 132 | pass |
| 34.38 (34.38) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 133 | pass |
| 0.01 (1) | supp S3.7 | S3/2 | register B262 | supplementary.md line 133 | pass |
| 36.10 (36.1), 1.73 (1.7296) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 134 | pass |
| 94.55 (94.55), 97.73 (97.73), 3.18 (3.18) | supp S3.7 | S3/Table S1 row 3 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 135 | pass |
| 3.3 (3.3) | supp S3.7 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 135 | pass |
| 1.129 (1.129), 94.10 (94.1), -0.45 (45) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 135 | pass |
| 3,364 (3364) | supp S3.7 | S3/25 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 136 | pass |
| 99.13 (99.13) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 136 | pass |
| 4.58 (4.58) | supp S3.7 | S4/B141b-18 | analysis/comparators_2025/diet_land.csv | supplementary.md line 136 | pass |
| 109.63 (109.63), 114.88 (114.88), 5.25 (5.25) | supp S3.7 | S3/Table S1 row 4 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 137 | pass |
| 4.6 (4.6) | supp S3.7 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 137 | pass |
| 1.129 (1.129), 109.34 (109.34) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 137 | pass |
| -0.29 (0.29) | supp S3.7 | S3/38 | register B145 | supplementary.md line 137 | pass |
| 3,364 (3364) | supp S3.7 | S3/25 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 138 | pass |
| 115.36 (115.36), 5.73 (5.73) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 138 | pass |
| 14.63 (14.63), 15.76 (15.76), 1.13 (112.59) | supp S3.7 | S3/Table S1 row 5 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 139 | pass |
| 7.2 (7.2) | supp S3.7 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 139 | pass |
| 1.129 (1.129), 14.42 (14.42) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 139 | pass |
| -19 (19.2771) | supp S3.7 | S3/Table S6 row 19 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 139 | pass |
| 3,364 (3364) | supp S3.7 | S3/25 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 140 | pass |
| 15.07 (15.07), 39 (39) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 140 | pass |
| 1.718 (1.7176), 1.758 (1.758), 2.3 (2.3) | supp S3.7 | S3/16 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 141 | pass |
| 0.040 (4) | supp S3.7 | S3/51 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 141 | pass |
| 34.1 (34.06), 1.713 (1.7126), -0.005 (5) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 141 | pass |
| 5.5 | supp S3.7 | S4/B141b-18 | gap_attribution_readable.csv ("5.5 x 5 x 1.24") (checked by hand) | supplementary.md line 141 | pass |
| 5 (5.18) | supp S3.7 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 141 | pass |
| 1.24 (1.24) | supp S3.7 | S5/16 | qa/reports/V41_check_B115.md | supplementary.md line 141 | pass |
| 1.291 (1.2913), -0.426 (0.4263) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 142 | pass |
| 1.788 (1.7883) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 143 | pass |
| 0.071 (70.5) | supp S3.7 | S3/51 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 143 | pass |
| 1.778 (1.7779) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 144 | pass |
| 0.060 (60.45) | supp S3.7 | S3/51 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 144 | pass |
| 1.740 (1.7403), 0.023 (0.0227) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 145 | pass |
| 30 (30.2) | supp S3.7 | S3/Table S6 row 30 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 146 | pass |
| 1.730 (1.7296), 0.012 (1.165) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 146 | pass |
| 108.91 (108.912), 82 (81.5), 466 (466), 108.89 (108.891) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 147 | pass |
| 109 (108.912) | supp S3.7 | S3/58 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 147 | pass |
| 0.088 (8.8168) | supp S3.7 | S3/Table S1 row 7 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 147 | pass |
| 0.1 (5) | supp S3.7 | S3/Table S6 caption | analysis/method_tests_2025/fidelity.csv | supplementary.md line 147 | pass |
| 82 (81.5), 82.5 (82.5), 109.55 (109.555) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 148 | pass |
| 95.66 (95.6635), 0.34 (34.06), 294 (294), 95.65 (95.6549) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 149 | pass |
| 96 (95.6635) | supp S3.7 | S3/Table S1 row 9 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 149 | pass |
| 0.4 (41.5) | supp S3.7 | S3/B141b-9 | register B134 | supplementary.md line 149 | pass |
| 60 (0.595) | supp S3.7 | S3/B141b-15 | analysis/method_tests_2025/bridge_half_to_model.csv | supplementary.md line 149 | pass |
| 60 (0.595) | supp S3.7 | S3/B141b-15 | analysis/method_tests_2025/bridge_half_to_model.csv | supplementary.md line 150 | pass |
| 60.5 (60.45), 96.45 (96.452) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 150 | pass |
| 31.95 (31.95) | supp S3.7 | S3/37 | register B141 | supplementary.md line 151 | pass |
| 31.578 (31.578) | supp S3.7 | S3/35 | register B140 | supplementary.md line 151 | pass |
| -0.37 (0.372), 31.28 (31.28), -0.67 (0.671) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 151 | pass |
| 1.2 (1.2) | supp S3.7 | S3/37 | register B326 | supplementary.md line 151 | pass |
| 32.85 (32.855), 0.91 (91) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 152 | pass |
| 30.59 (30.591), -1.36 (1.3554) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 153 | pass |
| 3.47 (3.47) | supp S3.7 | S3/37 | register B141 | supplementary.md line 154 | pass |
| 3.514 (3.514) | supp S3.7 | S3/35 | register B140 | supplementary.md line 154 | pass |
| 0.043 (43) | supp S3.7 | S3/Table S1 row 12 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 154 | pass |
| 1.2 (1.2) | supp S3.7 | S3/37 | register B326 | supplementary.md line 154 | pass |
| 3.60 (3.601), 0.13 (13.3) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 154 | pass |
| 3.53 (3.527), 0.06 (5.5) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 155 | pass |
| 12.3 (12.325), -2.23 (2.225), 10.7 (10.7268) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 156 | pass |
| 10.1 (10.1) | supp S3.7 | S3/Table S1 row 13 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 156 | pass |
| 22.0 (22) | supp S3.7 | S3/29 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 156 | pass |
| 72 (7215) | supp S3.7 | S5/Table S3a row 4 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 156 | pass |
| 7.5 (7.5) | supp S3.7 | S4/Table S2 row 5 | analysis/comparators_2025/diet_land.csv | supplementary.md line 157 | pass |
| 6.0 (6) | supp S3.7 | S3/25 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 157 | pass |
| -1.49 (1.4939), 24.9 (24.9), 64 (64) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 157 | pass |
| 6.5 (6.5) | supp S3.7 | S3/Table S1 row 17 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 157 | pass |
| 4 (400.5) | supp S3.7 | S3/27 | analysis/method_tests_2025/cassidy.csv | supplementary.md line 158 | pass |
| 36 (36) | supp S3.7 | S3/17 | register B256 | supplementary.md line 158 | pass |
| 7.3 (7.3) | supp S3.7 | S3/B141b-17 | qa/reports/B139_paper_B_third_line_bridge_panels.md | supplementary.md line 158 | pass |
| 12 (12) | supp S3.7 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 158 | pass |
| 6.4 (6.3911) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 159 | pass |
| 74 (74) | supp S3.7 | S5/Table S3a row 4 | qa/reports/V41_check_B115.md | supplementary.md line 159 | pass |
| 21.0 (21) | supp S3.7 | S3/B141b-14 | analysis/method_tests_2025/README_round2_B139.md | supplementary.md line 160 | pass |
| 16.1 (16.1) | supp S3.7 | S3/Table S1 row 15 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 160 | pass |
| -4.87 (4.8666), 19.3 (19.2771) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 160 | pass |
| 30.2 (30.2) | supp S3.7 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 160 | pass |
| 35 (0.35) | supp S3.7 | S3/Table S8 caption | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 160 | pass |
| 8.8 (8.8) | supp S3.7 | S3/11 | register B023 | supplementary.md line 161 | pass |
| 6.5 (6.5) | supp S3.7 | S3/Table S1 row 17 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 161 | pass |
| -2.32 (2.3168), 64 (64) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 161 | pass |
| 35.6 (35.6) | supp S3.7 | S5/16 | qa/reports/V41_check_B115.md | supplementary.md line 161 | pass |
| 7.3 (7.3) | supp S3.7 | S3/B141b-17 | qa/reports/B139_paper_B_third_line_bridge_panels.md | supplementary.md line 161 | pass |
| 18.4 (18.4226), -4.92 (4.9226) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 162 | pass |
| 13.5 (13.5) | supp S3.7 | S3/Table S1 row 19 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 162 | pass |
| 36.5 (36.46) | supp S3.7 | S3/47 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 162 | pass |
| 16.0 (16) | supp S3.7 | S5/Table S3 row 4 | results/ranges_2025-mirror.csv | supplementary.md line 162 | pass |
| 50 (0.5) | supp S3.7 | S5/12 | qa/reports/V41_check_B115.md | supplementary.md line 162 | pass |
| 14.1 (14.1) | supp S3.7 | S3/B141b-17 | qa/reports/B139_paper_B_third_line_bridge_panels.md | supplementary.md line 163 | pass |
| 10.6 (10.6) | supp S3.7 | S3/Table S1 row 21 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 163 | pass |
| -3.55 (3.546), 33.5 (33.45), 11.2 (0.1119), 82 (81.5) | supp S3.7 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 163 | pass |
| 27.6 (27.6082) | supp S3.8 | S3/42 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 168 | pass |
| 26.20 (26.2) | supp S3.8 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 168 | pass |
| 26.08 (26.08) | supp S3.8 | S3/54 | qa/reports/B116_bases_and_fidelity.md | supplementary.md line 168 | pass |
| 15.6 (15.6) | supp S3.8 | S3/11 | register B023 | supplementary.md line 168 | pass |
| 3,718 (3718), 11.3 (11.3), 14.8 (14.8), 8.0 (8) | supp S3.8 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 168 | pass |
| 2,700 (2700) | supp S3.8 | S3/34 | register B087 | supplementary.md line 168 | pass |
| 3,525 (3525) | supp S3.8 | S3/34 | register B263 | supplementary.md line 168 | pass |
| 12 (12) | supp S3.8 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 168 | pass |
| 0.01 (1) | supp S3.8 | S3/2 | register B262 | supplementary.md line 168 | pass |
| 363.52 (363.52) | supp S3.8 | S3/57 | analysis/method_tests_2025/bases.csv | supplementary.md line 168 | pass |
| 15.6 (15.6) | supp S3.8 | S3/11 | register B023 | supplementary.md line 170 | pass |
| 3,718 (3718) | supp S3.8 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 170 | pass |
| 82 (82), 82 (82), 466 (466), 294 (294) | supp S3.8 | S3/Table S5 row 1 | analysis/method_tests_2025/bases.csv | supplementary.md line 174 | pass |
| 60 (0.595), 60 (0.595) | supp S3.8 | S3/B141b-15 | analysis/method_tests_2025/bridge_half_to_model.csv | supplementary.md line 174 | pass |
| 15.6 (15.6), 15.6 (15.6), 8.8 (8.8) | supp S3.8 | S3/11 | register B023 | supplementary.md line 174 | pass |
| 3,718 (3718) | supp S3.8 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 174 | pass |
| 0.1760 (0.176) | supp S3.8 | S3/4 | register B014 | supplementary.md line 174 | pass |
| 10 (10) | supp S3.8 | S3/3 | register B012 | supplementary.md line 174 | pass |
| 15 (0.154) | supp S3.8 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 174 | pass |
| 134 (133.8) | supp S3.8 | S3/8 | register B016 | supplementary.md line 174 | pass |
| 70 (70), 45.7 (45.7) | supp S3.8 | S3/5 | register B013 | supplementary.md line 174 | pass |
| 59.95 (59.95) | supp S3.8 | S3/8 | register B017 | supplementary.md line 174 | pass |
| 28.3 (28.3) | supp S3.8 | S3/9 | register B027 | supplementary.md line 174 | pass |
| 31.65 (31.65) | supp S3.8 | S3/33 | register B084 | supplementary.md line 174 | pass |
| 27.61 (27.61), 3525 (3525), 120.7 (120.7) | supp S3.8 | S3/Table S5 row 1 | analysis/method_tests_2025/bases.csv | supplementary.md line 175 | pass |
| 26.2 (2.61605e+07) | supp S3.8 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 175 | pass |
| 14.8 (14.8) | supp S3.8 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 175 | pass |
| 363.52 (363.52) | supp S3.8 | S3/57 | analysis/method_tests_2025/bases.csv | supplementary.md line 175 | pass |
| 4306.0 (4306) | supp S3.8 | S3/12 | literature register L051 | supplementary.md line 176 | pass |
| 26.2 (2.61605e+07) | supp S3.8 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 176 | pass |
| 1 (1.2), 1 (1.2) | supp S3.8 | S3/17 | register B033 | supplementary.md line 176 | pass |
| 2 (1.758) | supp S3.8 | S3/17 | register B256 | supplementary.md line 176 | pass |
| 3 (3), 3 (3), 3 (3) | supp S3.8 | S3/19 | analysis/method_tests_2025/simpson_food.csv | supplementary.md line 176 | pass |
| 31.65 (31.65) | supp S3.8 | S3/33 | register B084 | supplementary.md line 176 | pass |
| 331.87 (331.87) | supp S3.8 | S3/Table S5 row 1 | analysis/method_tests_2025/bases.csv | supplementary.md line 176 | pass |
| 27.61 (27.61) | supp S3.8 | S3/Table S5 row 1 | analysis/method_tests_2025/bases.csv | supplementary.md line 177 | pass |
| 26.2 (2.61605e+07) | supp S3.8 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 177 | pass |
| 3 (3) | supp S3.8 | S3/19 | analysis/method_tests_2025/simpson_food.csv | supplementary.md line 177 | pass |
| 26.2 (2.61605e+07) | supp S3.8 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 178 | pass |
| 363.52 (363.52) | supp S3.8 | S3/57 | analysis/method_tests_2025/bases.csv | supplementary.md line 178 | pass |
| 27.61 (27.61) | supp S3.8 | S3/Table S5 row 1 | analysis/method_tests_2025/bases.csv | supplementary.md line 179 | pass |
| 26.2 (2.61605e+07) | supp S3.8 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 179 | pass |
| 2,700 (2700), 2,700 (2700), 2,700 (2700) | supp S3.8 | S3/34 | register B087 | supplementary.md line 180 | pass |
| 11.3 (11.3) | supp S3.8 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 180 | pass |
| 985,500 (985500), 24.5 (24.5) | supp S3.8 | S3/Table S5 row 1 | analysis/method_tests_2025/bases.csv | supplementary.md line 180 | pass |
| 22 (22) | supp S3.8 | S3/29 | analysis/method_tests_2025/cassidy_people_per_hectare.py | supplementary.md line 180 | pass |
| 31.65 (31.65) | supp S3.8 | S3/33 | register B084 | supplementary.md line 180 | pass |
| 190 (190), 183 (183) | supp S3.8 | S3/33 | analysis/method_tests_2025/README.md | supplementary.md line 180 | pass |
| 27.61 (27.61), 3525 (3525), 24.5 (24.5) | supp S3.8 | S3/Table S5 row 1 | analysis/method_tests_2025/bases.csv | supplementary.md line 181 | pass |
| 26.2 (2.61605e+07) | supp S3.8 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 181 | pass |
| 14.8 (14.8) | supp S3.8 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 181 | pass |
| 25.1 (25.1) | supp S3.8 | S3/29 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 182 | pass |
| 0.5 (45) | supp S3.8 | S3/74 | analysis/pasture_2025/pairing_relaxed.csv | supplementary.md line 183 | pass |
| 26.20 (26.2) | supp S3.8 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 183 | pass |
| 27.61 (27.61), 331.87 (331.87), 150 (150) | supp S3.8 | S3/Table S5 row 1 | analysis/method_tests_2025/bases.csv | supplementary.md line 184 | pass |
| 8.0 (8) | supp S3.8 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 184 | pass |
| 31.65 (31.65) | supp S3.8 | S3/33 | register B084 | supplementary.md line 184 | pass |
| 27.61 (27.61), 331.87 (331.87) | supp S3.8 | S3/Table S5 row 1 | analysis/method_tests_2025/bases.csv | supplementary.md line 186 | pass |
| 8.0 (8) | supp S3.8 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 186 | pass |
| 31.65 (31.65) | supp S3.8 | S3/33 | register B084 | supplementary.md line 186 | pass |
| 363.52 (363.52) | supp S3.8 | S3/57 | analysis/method_tests_2025/bases.csv | supplementary.md line 186 | pass |
| 0.01 (1) | supp S3.8 | S3/2 | register B262 | supplementary.md line 186 | pass |
| 12 (12) | supp S3.8 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 186 | pass |
| 27.61 (27.61) | supp S3.8 | S3/Table S5 row 1 | analysis/method_tests_2025/bases.csv | supplementary.md line 187 | pass |
| 12 (12) | supp S3.8 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 187 | pass |
| 27.61 (27.61), 331.87 (331.87) | supp S3.8 | S3/Table S5 row 1 | analysis/method_tests_2025/bases.csv | supplementary.md line 188 | pass |
| 8.0 (8) | supp S3.8 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 188 | pass |
| 31.65 (31.65) | supp S3.8 | S3/33 | register B084 | supplementary.md line 188 | pass |
| 363.52 (363.52) | supp S3.8 | S3/57 | analysis/method_tests_2025/bases.csv | supplementary.md line 188 | pass |
| 0.01 (1) | supp S3.8 | S3/2 | register B262 | supplementary.md line 188 | pass |
| 27.61 (27.61) | supp S3.8 | S3/Table S5 row 1 | analysis/method_tests_2025/bases.csv | supplementary.md line 189 | pass |
| 2 (1.758) | supp S3.9 | S3/17 | register B256 | supplementary.md line 194 | pass |
| 10 (10), 10 (10) | supp S3.9 | S3/3 | register B012 | supplementary.md line 194 | pass |
| 21.6 (21.6) | supp S3.9 | S3/18 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 194 | pass |
| 32 (3182) | supp S3.9 | S3/28 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 194 | pass |
| 6 (6) | supp S3.9 | S3/28 | register B073 | supplementary.md line 194 | pass |
| 21.6 (21.6) | supp S3.9 | S3/18 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 196 | pass |
| 109 (108.912) | supp S3.9 | S3/58 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 200 | pass |
| 108.9 (108.912) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 200 | pass |
| -0.1 (5) | supp S3.9 | S3/Table S6 caption | analysis/method_tests_2025/fidelity.csv | supplementary.md line 200 | pass |
| 96 (95.6635) | supp S3.9 | S3/Table S1 row 9 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 201 | pass |
| 95.7 (95.6635) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 201 | pass |
| -0.4 (41.5) | supp S3.9 | S3/B141b-9 | register B134 | supplementary.md line 201 | pass |
| 206 (2.06) | supp S3.9 | S3/Table S1 row 8 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 202 | pass |
| 206.0 (205.962) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 202 | pass |
| 0 (0) | supp S3.9 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 202 | pass |
| 188 (187.888) | supp S3.9 | S3/Table S1 row 10 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 203 | pass |
| 187.9 (187.888) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 203 | pass |
| -0.1 (5) | supp S3.9 | S3/Table S6 caption | analysis/method_tests_2025/fidelity.csv | supplementary.md line 203 | pass |
| 1.758 (1.758), 1.718 (1.7176), -2.3 (2.3) | supp S3.9 | S3/16 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 204 | pass |
| 1.737 (1.737) | supp S3.9 | S3/17 | register B033 | supplementary.md line 204 | pass |
| -1.2 (1.2) | supp S3.9 | S3/37 | register B326 | supplementary.md line 204 | pass |
| 0.095 (0.095), 0.098 (97.73), 0.116 (115.88), 21.6 (21.6) | supp S3.9 | S3/18 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 205 | pass |
| 3.6 (3.6) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 205 | pass |
| 0.312 (0.312), 0.074 (0.074) | supp S3.9 | S3/19 | analysis/method_tests_2025/simpson_food.csv | supplementary.md line 206 | pass |
| 0.107 (0.1068), -65.8 (65.8), -76.3 (76.3) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 206 | pass |
| 2.165 (2.165) | supp S3.9 | S3/Table S6 row 8 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 207 | pass |
| 1.942 (1.942), -10.3 (10.3), 1.907 (1.9072), -11.9 (11.9495) | supp S3.9 | S3/20 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 207 | pass |
| 0.032 (31.578), 0.014 (14.2), -56.9 (56.9) | supp S3.9 | S3/20 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 208 | pass |
| 0.854 (0.854), 0.127 (0.127), -85.1 (85.1) | supp S3.9 | S3/20 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 209 | pass |
| 35.13 (35.13), 34.37 (34.37) | supp S3.9 | S3/Table S1 row 1 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 210 | pass |
| -2.2 (2.2) | supp S3.9 | S3/42 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 210 | pass |
| 36.10 (36.1) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 210 | pass |
| 2.8 (2.8) | supp S3.9 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 210 | pass |
| 112.20 (112.2) | supp S3.9 | S3/Table S6 row 12 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 211 | pass |
| 113.12 (113.12) | supp S3.9 | S3/Table S1 row 2 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 211 | pass |
| 0.8 (0.8), 8.4 (8.4) | supp S3.9 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 211 | pass |
| 121.59 (121.59) | supp S3.9 | S3/25 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 211 | pass |
| 97.73 (97.73), 94.55 (94.55) | supp S3.9 | S3/Table S1 row 3 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 212 | pass |
| -3.3 (3.3), 3.4 (3.4) | supp S3.9 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 212 | pass |
| 101.04 (101.04) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 212 | pass |
| 114.88 (114.88), 109.63 (109.63) | supp S3.9 | S3/Table S1 row 4 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 213 | pass |
| -4.6 (4.6), 3.0 (3) | supp S3.9 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 213 | pass |
| 118.36 (118.36) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 213 | pass |
| 15.76 (15.76), 14.63 (14.63) | supp S3.9 | S3/Table S1 row 5 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 214 | pass |
| -7.2 (7.2), -4.1 (4.1) | supp S3.9 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 214 | pass |
| 15.11 (15.11) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 214 | pass |
| 135.76 (135.76) | supp S3.9 | S3/Table S6 row 16 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 215 | pass |
| 94.80 (94.8) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 215 | pass |
| -30.2 (30.2) | supp S3.9 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 215 | pass |
| 10.1 (10.1) | supp S3.9 | S3/Table S1 row 13 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 216 | pass |
| 12.3 (12.325), 10.7 (0.1068), 6.2 (6.2) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 216 | pass |
| 22.0 (22) | supp S3.9 | S3/29 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 216 | pass |
| 6.0 (6) | supp S3.9 | S3/25 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 217 | pass |
| 7.5 (7.5) | supp S3.9 | S4/Table S2 row 5 | analysis/comparators_2025/diet_land.csv | supplementary.md line 217 | pass |
| 24.9 (24.9) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 217 | pass |
| 6.5 (6.5) | supp S3.9 | S3/Table S1 row 17 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 217 | pass |
| 9.0 (9) | supp S3.9 | S2/13 | register B337 | supplementary.md line 217 | pass |
| 16.1 (16.1) | supp S3.9 | S3/Table S1 row 15 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 218 | pass |
| 21.0 (21) | supp S3.9 | S3/B141b-14 | analysis/method_tests_2025/README_round2_B139.md | supplementary.md line 218 | pass |
| 30.2 (30.2) | supp S3.9 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 218 | pass |
| 19.3 (19.2771) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 218 | pass |
| 19.7 (19.7) | supp S3.9 | S3/65 | qa/reports/B116_bases_and_fidelity.md | supplementary.md line 218 | pass |
| 5.4 (5.44) | supp S3.9 | S3/Table S1 row 16 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 219 | pass |
| 6.9 (6.908), 27.9 (27.9), 6.4 (6.4193), 18.9 (18.9) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 219 | pass |
| 6.5 (6.5) | supp S3.9 | S3/Table S1 row 17 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 220 | pass |
| 8.8 (8.8) | supp S3.9 | S3/11 | register B023 | supplementary.md line 220 | pass |
| 35.6 (35.6) | supp S3.9 | S5/16 | qa/reports/V41_check_B115.md | supplementary.md line 220 | pass |
| 7.3 (7.3) | supp S3.9 | S3/B141b-17 | qa/reports/B139_paper_B_third_line_bridge_panels.md | supplementary.md line 220 | pass |
| 13.0 (13) | supp S3.9 | S5/16 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 220 | pass |
| 5.9 (5.9) | supp S3.9 | S3/Table S1 row 18 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 221 | pass |
| 7.9 (7.8643), 33.3 (33.3), 6.6 (6.5951) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 221 | pass |
| 11.8 (0.118) | supp S3.9 | S5/Table S3 row 4 | results/ranges_2025-mirror.csv | supplementary.md line 221 | pass |
| 13.5 (13.5) | supp S3.9 | S3/Table S1 row 19 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 222 | pass |
| 18.4 (18.4226), 18.2 (18.2) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 222 | pass |
| 36.5 (36.46) | supp S3.9 | S3/47 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 222 | pass |
| 16.0 (16) | supp S3.9 | S5/Table S3 row 4 | results/ranges_2025-mirror.csv | supplementary.md line 222 | pass |
| 8.4 (8.4) | supp S3.9 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 223 | pass |
| 11.9 (11.9495) | supp S3.9 | S3/20 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 223 | pass |
| 42.3 (42.3), 25.1 (25.1) | supp S3.9 | S3/29 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 223 | pass |
| 10.5 (10.5124) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 223 | pass |
| 10.6 (10.6) | supp S3.9 | S3/Table S1 row 21 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 224 | pass |
| 14.1 (14.1) | supp S3.9 | S3/B141b-17 | qa/reports/B139_paper_B_third_line_bridge_panels.md | supplementary.md line 224 | pass |
| 33.5 (33.5), 11.2 (11.2266) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 224 | pass |
| 5.9 (5.9) | supp S3.9 | S3/Table S1 row 18 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 224 | pass |
| 5.2 (5.2), 5.2 (5.2) | supp S3.9 | S3/29 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 225 | pass |
| 6.8 (6.8265), 31.3 (31.3) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 225 | pass |
| 5.5 | supp S3.9 | S4/B141b-18 | fidelity.csv Brazil delivered, 5.4711 (checked by hand) | supplementary.md line 225 | pass |
| 67 (67) | supp S3.9 | S3/28 | register B073 | supplementary.md line 226 | pass |
| 41.0 (4.09877e+07) | supp S3.9 | S3/B141b-7 | analysis/resilience_2025/drought_bounds_paper_B.csv | supplementary.md line 226 | pass |
| -38.8 (38.8) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 226 | pass |
| 34 (34) | supp S3.9 | S3/15 | register B260 | supplementary.md line 227 | pass |
| 33.0 (33), -2.9 (2.9) | supp S3.9 | S3/27 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 227 | pass |
| 59 (59) | supp S3.9 | S3/27 | register B257 | supplementary.md line 228 | pass |
| 61.0 (61) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 228 | pass |
| 3.4 (3.4) | supp S3.9 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 228 | pass |
| 31.578 (31.578) | supp S3.9 | S3/35 | register B140 | supplementary.md line 229 | pass |
| 31.950 (31.95) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 229 | pass |
| 1.2 (1.2) | supp S3.9 | S3/37 | register B326 | supplementary.md line 229 | pass |
| 3.514 (3.514) | supp S3.9 | S3/35 | register B140 | supplementary.md line 230 | pass |
| 3.471 (3.471) | supp S3.9 | S3/Table S1 row 12 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 230 | pass |
| -1.2 (1.2) | supp S3.9 | S3/37 | register B326 | supplementary.md line 230 | pass |
| 0.24 (0.24), 0.24 (0.24) | supp S3.9 | S3/40 | register B121 | supplementary.md line 231 | pass |
| 40,439,187 (4.04392e+07), 40,439,187 (4.04392e+07) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 232 | pass |
| 0 (0) | supp S3.9 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 232 | pass |
| 9,431,487 (9.43149e+06), 9,431,487 (9.43149e+06) | supp S3.9 | S3/Table S6 row 1 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 233 | pass |
| 0 (0) | supp S3.9 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 233 | pass |
| 4 (400.5) | supp S3.10 | S3/27 | analysis/method_tests_2025/cassidy.csv | supplementary.md line 238 | pass |
| 0.715 (0.715), 0.651 (0.651), 0.634 (0.634), 0.846 (0.846) | supp S3.10 | S3/64 | qa/reports/V42_check_B116.md | supplementary.md line 238 | pass |
| 0.950 (95), 0.610 (61) | supp S3.10 | S3/64 | qa/reports/B116_bases_and_fidelity.md | supplementary.md line 238 | pass |
| 0.854 (0.854) | supp S3.10 | S3/20 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 238 | pass |
| 20 (20) | supp S3.10 | S3/65 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 238 | pass |
| 37 (0.372) | supp S3.10 | S3/47 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 238 | pass |
| 0.82 (81.5) | supp S3.10 | S3/46 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 238 | pass |
| 0.86 (0.8554) | supp S3.10 | S3/67 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 238 | pass |
| 0.92 (92) | supp S3.10 | S3/48 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 238 | pass |
| 55.3 (55.3) | supp S3.10 | S3/68 | analysis/method_tests_2025/ladder.csv | supplementary.md line 238 | pass |
| 2 (1.758) | supp S3.10 | S3/17 | register B256 | supplementary.md line 238 | pass |
| 182.3 (182.3) | supp S3.10 | S3/Table S7 row 2 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 240 | pass |
| 324.3 (324.3), 275.7 (275.7) | supp S3.10 | S3/Table S7 row 9 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 240 | pass |
| 275.8 (275.8) | supp S3.10 | S3/Table S8 row 7 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 240 | pass |
| 145.2 (145.2), 3.5 (3.5), 169.7 (169.7), 4.09 (4.09), 177.0 (177), 4.26 (4.26) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 244 | pass |
| 148.8 (148.8), 182.3 (182.3), 205.8 (205.8) | supp S3.10 | S3/Table S7 row 2 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 245 | pass |
| 3.59 (3.59), 4.39 (4.39), 4.96 (4.96) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 245 | pass |
| 1 (1.2) | supp S3.10 | S3/17 | register B033 | supplementary.md line 246 | pass |
| 159.8 (159.8), 189.0 (189), 207.7 (207.7) | supp S3.10 | S3/Table S7 row 3 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 246 | pass |
| 3.85 (3.85), 4.55 (4.55) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 246 | pass |
| 5.0 (5) | supp S3.10 | S2/13 | literature register L244 | supplementary.md line 246 | pass |
| 1 (1.2) | supp S3.10 | S3/17 | register B033 | supplementary.md line 247 | pass |
| 385.7 (385.7), 454.2 (454.2), 537.4 (537.4) | supp S3.10 | S3/Table S7 row 4 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 247 | pass |
| 9.29 (9.29), 10.95 (10.95), 12.95 (12.95) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 247 | pass |
| 1 (1.2) | supp S3.10 | S3/17 | register B033 | supplementary.md line 248 | pass |
| 343.4 (343.4), 404.8 (404.8), 472.1 (472.1) | supp S3.10 | S3/Table S7 row 5 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 248 | pass |
| 8.27 (8.27) | supp S3.10 | S3/Table S8 row 6 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 248 | pass |
| 9.75 (9.75), 11.38 (11.38) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 248 | pass |
| 3 (3) | supp S3.10 | S3/19 | analysis/method_tests_2025/simpson_food.csv | supplementary.md line 249 | pass |
| 146.2 (146.2), 172.5 (172.5), 192.9 (192.9) | supp S3.10 | S3/Table S7 row 6 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 249 | pass |
| 3.52 (3.52) | supp S3.10 | S3/Table S8 row 6 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 249 | pass |
| 4.16 (4.16), 4.65 (4.65) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 249 | pass |
| 3 (3) | supp S3.10 | S3/19 | analysis/method_tests_2025/simpson_food.csv | supplementary.md line 250 | pass |
| 316.9 (316.9), 370.9 (370.9), 430.2 (430.2) | supp S3.10 | S3/Table S7 row 7 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 250 | pass |
| 7.64 (7.64), 8.94 (8.94), 10.37 (10.37) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 250 | pass |
| 3 (3) | supp S3.10 | S3/19 | analysis/method_tests_2025/simpson_food.csv | supplementary.md line 251 | pass |
| 287.7 (287.7), 337.1 (337.1), 388.6 (388.6) | supp S3.10 | S3/Table S7 row 8 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 251 | pass |
| 6.93 (6.93), 8.12 (8.12), 9.36 (9.36) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 251 | pass |
| 275.7 (275.7), 324.3 (324.3), 375.8 (375.8) | supp S3.10 | S3/Table S7 row 9 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 252 | pass |
| 6.64 (6.64), 7.82 (7.82), 9.05 (9.05) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 252 | pass |
| 112.9 (112.9), 132.0 (132), 137.6 (137.6) | supp S3.10 | S3/Table S7 row 10 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 253 | pass |
| 2.72 (2.72), 3.32 (3.32) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 253 | pass |
| 3.18 (3.18) | supp S3.10 | S3/Table S1 row 3 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 253 | pass |
| 110.9 (110.9), 129.7 (129.7), 135.2 (135.2) | supp S3.10 | S3/Table S7 row 11 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 254 | pass |
| 2.67 (2.67), 3.12 (3.12), 3.26 (3.26) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 254 | pass |
| 0.99 (0.99), 1.16 (1.16) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 255 | pass |
| 1.4 (1.4) | supp S3.10 | S3/42 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 255 | pass |
| 0.29 (0.29) | supp S3.10 | S3/38 | register B145 | supplementary.md line 256 | pass |
| 0.47 (472.1), 0.43 (0.43) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 256 | pass |
| 3.05 (3.05), 3.31 (3.31), 3.33 (3.33) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 257 | pass |
| 41.5 (41.5), 41.5 (41.5), 41.5 (41.5) | supp S3.10 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 258 | pass |
| 1.0 (1), 1.0 (1), 1.0 (1) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 258 | pass |
| 53.6 (53.6), 53.6 (53.6), 53.6 (53.6) | supp S3.10 | S3/Table S7 row 16 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 259 | pass |
| 1.29 (1.29), 1.29 (1.29), 1.29 (1.29) | supp S3.10 | S3/Table S7 row 1 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 259 | pass |
| 41.5 (41.5), 0 (0), 68 (0.681), 26 (0.261), -15 (0.154), -15 (0.154), 17 (17), 12 (12) | supp S3.11 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 263 | pass |
| -4 (400.5) | supp S3.11 | S3/27 | analysis/method_tests_2025/cassidy.csv | supplementary.md line 263 | pass |
| 61 (61) | supp S3.11 | S3/27 | register B257 | supplementary.md line 263 | pass |
| 38 (38.5) | supp S3.11 | S3/B141b-10 | qa/reports/B139_paper_B_third_line_bridge_panels.md | supplementary.md line 263 | pass |
| -5 (5.18) | supp S3.11 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 263 | pass |
| 8 (8), 8 (8) | supp S3.11 | S3/30 | register B258 | supplementary.md line 263 | pass |
| -22 (22) | supp S3.11 | S3/29 | analysis/method_tests_2025/cassidy_people_per_hectare.py | supplementary.md line 263 | pass |
| -19 (19.2771) | supp S3.11 | S3/Table S6 row 19 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 263 | pass |
| 2 (1.758) | supp S3.11 | S3/17 | register B256 | supplementary.md line 263 | pass |
| 26.20 (26.2) | supp S3.11 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 265 | pass |
| 1 (1.2) | supp S3.11 | S3/17 | register B033 | supplementary.md line 265 | pass |
| 5.19 (5.19), 22.28 (22.28), 4.29 (4.29), 112.5 (112.5), 22.53 (22.53), 46.35 (46.35), 2.06 (2.06), 27.72 (27.72), 68.56 (68.56), 2.47 (2.47), 4.47 (4.47), 2.97 (2.97), 3.23 (3.23) | supp S3.11 | S3/B141b-12 | analysis/method_tests_2025/harmonised_robustness_footprint.csv | supplementary.md line 265 | pass |
| 53.9 (53.9), 77.9 (77.9), 53.9 (53.9), 77.9 (77.9) | supp S3.11 | S3/B141b-11 | register B270 | supplementary.md line 265 | pass |
| 64.8 (64.8), 117.0 (117), 64.8 (64.8), 117.0 (117), 1.56 (1.56), 2.82 (2.82), 1.21 (1.21), 2.18 (2.18) | supp S3.11 | S3/Table S8 row 1 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 265 | pass |
| 3 (3) | supp S3.11 | S3/19 | analysis/method_tests_2025/simpson_food.csv | supplementary.md line 265 | pass |
| 84.6 (84.6) | supp S3.11 | S3/Table S8 row 2 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 265 | pass |
| 1.30 (1.3), 1.88 (1.88) | supp S3.11 | S3/B141b-11 | qa/reports/B135_shares_robustness.md | supplementary.md line 265 | pass |
| 1.01 (0.0101) | supp S3.11 | S3/B141b-11 | results/2025-fixed.csv | supplementary.md line 265 | pass |
| 1.45 (1.45) | supp S3.11 | S3/B141b-11 | analysis/method_tests_2025/harmonised_robustness.csv | supplementary.md line 265 | pass |
| 41.5 (41.5) | supp S3.11 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 271 | pass |
| -1.1 (0.011), 6.8 (0.068), 27.7 (0.277), 45.9 (0.459) | supp S3.11 | S3/B141b-13 | analysis/method_tests_2025/harmonised_robustness.csv | supplementary.md line 271 | pass |
| 31.1 (3.11154e+07), 49.2 (4.91698e+07) | supp S3.11 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 272 | pass |
| 41.5 (41.5) | supp S3.11 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 272 | pass |
| 53.6 (53.6) | supp S3.11 | S3/Table S7 row 16 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 272 | pass |
| -1.2 (1.2) | supp S3.11 | S3/37 | register B326 | supplementary.md line 272 | pass |
| 7.8 (0.078), 23.2 (0.232) | supp S3.11 | S3/B141b-13 | analysis/method_tests_2025/harmonised_robustness.csv | supplementary.md line 272 | pass |
| 52.8 (52.8) | supp S3.11 | S3/B141b-9 | qa/reports/B134_paper_B_drought_bound_and_pasture.md | supplementary.md line 272 | pass |
| -32.1 (32.14), 35.5 (0.355), 9.4 (9.41), 35.5 (0.355) | supp S3.11 | S3/B141b-13 | analysis/method_tests_2025/harmonised_robustness.csv | supplementary.md line 273 | pass |
| -0.5 (45) | supp S3.11 | S3/74 | analysis/pasture_2025/pairing_relaxed.csv | supplementary.md line 273 | pass |
| 5.4 (5.44) | supp S3.11 | S3/Table S1 row 16 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 273 | pass |
| -27.4 (0.274) | supp S3.11 | S3/B141b-13 | analysis/method_tests_2025/harmonised_robustness.csv | supplementary.md line 274 | pass |
| 1.4 (1.4) | supp S3.11 | S3/42 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 274 | pass |
| 5.9 (5.9) | supp S3.11 | S3/Table S1 row 18 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 274 | pass |
| 32.0 (3.20068e+07) | supp S3.11 | S5/Table S3 row 7 | results/ranges_2025-improved_wide.csv | supplementary.md line 274 | pass |
| 41.5 (41.5) | supp S3.11 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 275 | pass |
| 8.2 (0.082), 8.2 (0.082) | supp S3.11 | S3/B141b-13 | analysis/method_tests_2025/harmonised_robustness.csv | supplementary.md line 275 | pass |
| 41.5 (41.5) | supp S3.11 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 276 | pass |
| 10.5 (0.105), 10.5 (0.105) | supp S3.11 | S3/B141b-13 | analysis/method_tests_2025/harmonised_robustness.csv | supplementary.md line 276 | pass |
| 7.7 (0.077), 48 (0.475), 11.5 (0.115), 31.8 (0.318) | supp S3.11 | S3/B141b-13 | analysis/method_tests_2025/harmonised_robustness.csv | supplementary.md line 277 | pass |
| -8.6 (8.6) | supp S3.11 | S5/Table S3a row 4 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 277 | pass |
| 23 (23) | supp S3.11 | S3/33 | analysis/method_tests_2025/cassidy_matched.csv | supplementary.md line 277 | pass |
| 31.1 (3.11154e+07) | supp S3.11 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 279 | pass |
| 1.4 (1.4) | supp S3.11 | S3/42 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 279 | pass |
| 0.8202 (0.8202), 1.512 (1.512), 303 (303), 14.7 (14.7), 16.4 (16.44), 11.7 (11.7), 21.0 (21), 20.7 (20.7) | supp S3.11 | S3/B141b-14 | analysis/method_tests_2025/README_round2_B139.md | supplementary.md line 281 | pass |
| 8.0 (8), 8.0 (8) | supp S3.11 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 281 | pass |
| 10.1 (10.1) | supp S3.11 | S3/Table S1 row 13 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 281 | pass |
| 10 (10) | supp S3.11 | S3/3 | register B012 | supplementary.md line 281 | pass |
| 16 (15.6) | supp S3.11 | S3/Table S5 row 16 | analysis/method_tests_2025/bases.csv | supplementary.md line 281 | pass |
| 55.3 (55.3) | supp S3.11 | S3/68 | analysis/method_tests_2025/ladder.csv | supplementary.md line 281 | pass |
| 41.5 (41.5) | supp S3.11 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 283 | pass |
| 41.5 (41.5) | supp S3.11 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 287 | pass |
| 38.5 (38.5), 17.2 (17.2), 0.65 (0.65), 0.44 (0.44), 31.8 (31.8) | supp S3.11 | S3/B141b-14 | analysis/method_tests_2025/README_round2_B139.md | supplementary.md line 287 | pass |
| 16.0 (16) | supp S3.11 | S5/Table S3 row 4 | results/ranges_2025-mirror.csv | supplementary.md line 287 | pass |
| 8.0 (8) | supp S3.11 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 288 | pass |
| 1.512 (1.512), 1.10 (1.1), 14.7 (14.7), 20.0 (20), 20.7 (20.7), 0.65 (0.65) | supp S3.11 | S3/B141b-14 | analysis/method_tests_2025/README_round2_B139.md | supplementary.md line 288 | pass |
| 41.5 (41.5) | supp S3.11 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 288 | pass |
| 0.48 (48.1) | supp S3.11 | S3/54 | qa/reports/B116_bases_and_fidelity.md | supplementary.md line 288 | pass |
| 26.2 (2.61605e+07) | supp S3.11 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 288 | pass |
| 27.9 (27.9), 14.3 (14.3), 17.2 (17.2), 0.65 (0.65), 0.44 (0.44), 31.8 (31.8) | supp S3.11 | S3/B141b-14 | analysis/method_tests_2025/README_round2_B139.md | supplementary.md line 289 | pass |
| 16.0 (16) | supp S3.11 | S5/Table S3 row 4 | results/ranges_2025-mirror.csv | supplementary.md line 289 | pass |
| 8.0 (8) | supp S3.11 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 290 | pass |
| 1.844 (1.844), 21.0 (21), 20.9 (20.9), 0.65 (0.65), 0.50 (0.5), 23.3 (23.3) | supp S3.11 | S3/B141b-14 | analysis/method_tests_2025/README_round2_B139.md | supplementary.md line 290 | pass |
| 55.3 (55.3) | supp S3.11 | S3/68 | analysis/method_tests_2025/ladder.csv | supplementary.md line 290 | pass |
| 21.7 (21.7) | supp S3.11 | S3/18 | qa/reports/V42_check_B116.md | supplementary.md line 290 | pass |
| 31.0 (31), 20.7 (20.7), 17.2 (17.2), 0.65 (0.65), 0.44 (0.44), 31.8 (31.8) | supp S3.11 | S3/B141b-14 | analysis/method_tests_2025/README_round2_B139.md | supplementary.md line 291 | pass |
| 16.0 (16) | supp S3.11 | S5/Table S3 row 4 | results/ranges_2025-mirror.csv | supplementary.md line 291 | pass |
| 41.5 (41.5) | supp S3.11 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 295 | pass |
| 53.6 (53.6) | supp S3.11 | S3/Table S7 row 16 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 295 | pass |
| 103.1 (103.1), 268.4 (268.4) | supp S3.11 | S3/Table S8 caption | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 295 | pass |
| 64.8 (64.8), 117.0 (117), 1.56 (1.56), 2.82 (2.82), 1.21 (1.21), 2.18 (2.18) | supp S3.11 | S3/Table S8 row 1 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 299 | pass |
| 64.8 (64.8), 1.56 (1.56), 1.21 (1.21) | supp S3.11 | S3/Table S8 row 1 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 300 | pass |
| 84.6 (84.6), 2.04 (2.04), 1.58 (1.58) | supp S3.11 | S3/Table S8 row 2 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 300 | pass |
| 1 (1.2) | supp S3.11 | S3/17 | register B033 | supplementary.md line 301 | pass |
| 3 (3) | supp S3.11 | S3/19 | analysis/method_tests_2025/simpson_food.csv | supplementary.md line 301 | pass |
| 53.9 (53.9), 77.9 (77.9) | supp S3.11 | S3/B141b-11 | register B270 | supplementary.md line 301 | pass |
| 76.0 (0.76), 1.83 (1.83), 1.42 (1.42) | supp S3.11 | S3/Table S8 row 3 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 302 | pass |
| 133.8 (133.8), 210.7 (210.7), 3.22 (3.22), 5.08 (5.08), 3.93 (3.93) | supp S3.11 | S3/Table S8 row 4 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 303 | pass |
| 2.5 (2.5) | supp S3.11 | S3/Table S8 row 8 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 303 | pass |
| 64.8 (64.8), 1.56 (1.56), 1.6 (1.56), 1.21 (1.21) | supp S3.11 | S3/Table S8 row 1 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 304 | pass |
| 210.7 (210.7), 5.08 (5.08), 3.93 (3.93) | supp S3.11 | S3/Table S8 row 4 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 304 | pass |
| 5 (5.18) | supp S3.11 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 304 | pass |
| 146.2 (146.2) | supp S3.11 | S3/Table S7 row 6 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 305 | pass |
| 343.4 (343.4) | supp S3.11 | S3/Table S7 row 5 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 305 | pass |
| 3.52 (3.52), 8.27 (8.27), 2.73 (2.73), 6.41 (6.41) | supp S3.11 | S3/Table S8 row 6 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 305 | pass |
| 276.0 (276), 6.65 (6.65), 5.15 (5.15) | supp S3.11 | S3/Table S8 row 7 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 306 | pass |
| 146.2 (146.2) | supp S3.11 | S3/Table S7 row 6 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 307 | pass |
| 343.4 (343.4) | supp S3.11 | S3/Table S7 row 5 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 307 | pass |
| 3.52 (3.52), 8.27 (8.27), 2.73 (2.73), 6.41 (6.41) | supp S3.11 | S3/Table S8 row 6 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 307 | pass |
| 1 (1.2) | supp S3.12 | S3/17 | register B033 | supplementary.md line 311 | pass |
| 2 (1.758) | supp S3.12 | S3/17 | register B256 | supplementary.md line 311 | pass |
| 0.5 (45), 0.5 (45) | supp S3.12 | S3/74 | analysis/pasture_2025/pairing_relaxed.csv | supplementary.md line 311 | pass |
| 0.6 (57) | supp S3.12 | S3/49 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 311 | pass |
| 4.2 (4.2) | supp S3.12 | S3/74 | qa/reports/B114_pairing_relaxed.md | supplementary.md line 311 | pass |
| 0.12 (121491) | supp S3.12 | S5/B141b-20 | analysis/resilience_2025/drought_bounds_paper_B.csv | supplementary.md line 313 | pass |
| 0 (0) | supp S3.12 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 313 | pass |
| 1 (1.2) | supp S3.12 | S3/17 | register B033 | supplementary.md line 313 | pass |
| 9 (8.8) | supp S3.12 | S3/Table S5 row 9 | analysis/method_tests_2025/bases.csv | supplementary.md line 313 | pass |
| 16.44 (16.44), -21.89 (21.89), -12.53 (12.53), -6.39 (6.39), -6.17 (6.17), -3.92 (3.92) | supp S3.12 | S3/B141b-15 | analysis/method_tests_2025/bridge_half_to_model.csv | supplementary.md line 315 | pass |
| 36 (36) | supp S3.12 | S3/17 | register B256 | supplementary.md line 315 | pass |
| 19 (19.2771) | supp S3.12 | S3/Table S6 row 19 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 315 | pass |
| 18 (18) | supp S3.12 | S3/Table S6 row 18 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 315 | pass |
| 11 (11.3) | supp S3.12 | S3/Table S5 row 11 | analysis/method_tests_2025/bases.csv | supplementary.md line 315 | pass |
| 9.2 (9.17) | supp S3.12 | S3/49 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 315 | pass |
| 76.0 (0.76), 76.0 (0.76) | supp S3.12 | S3/Table S8 row 3 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 317 | pass |
| 41.5 (41.5), 0 (0) | supp S3.12 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 317 | pass |
| 91.3 (91.3), 113.6 (113.56), -43.2 (43.23), 60 (0.595), 85.4 (85.36), 84.9 (84.94), 86.2 (86.2), 145.6 (145.6), 116.9 (116.91) | supp S3.12 | S3/B141b-15 | analysis/method_tests_2025/bridge_half_to_model.csv | supplementary.md line 317 | pass |
| 1 (1.2), 1 (1.2) | supp S3.12 | S3/17 | register B033 | supplementary.md line 317 | pass |
| 3 (3), 3 (3) | supp S3.12 | S3/19 | analysis/method_tests_2025/simpson_food.csv | supplementary.md line 317 | pass |
| 2 (1.758) | supp S3.12 | S3/17 | register B256 | supplementary.md line 317 | pass |
| 5 (5.18) | supp S3.12 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 317 | pass |
| 92.4 (92.4) | supp S3.12 | S3/B141b-15 | qa/reports/B139_paper_B_third_line_bridge_panels.md | supplementary.md line 317 | pass |
| 363.52 (363.52) | supp S3.12 | S3/57 | analysis/method_tests_2025/bases.csv | supplementary.md line 319 | pass |
| 0.01 (1) | supp S3.12 | S3/2 | register B262 | supplementary.md line 319 | pass |
| 8.0 (8) | supp S3.12 | S3/55 | analysis/method_tests_2025/bases.csv | supplementary.md line 319 | pass |
| 31.65 (31.65) | supp S3.13 | S3/33 | register B084 | supplementary.md line 329 | pass |
| 363.52 (363.52) | supp S3.13 | S3/57 | analysis/method_tests_2025/bases.csv | supplementary.md line 329 | pass |
| 0.00 (0) | supp S3.13 | S3/B141b-16 | analysis/comparison_2025/production_comparison_2025.csv | supplementary.md line 329 | pass |
| 26 (0.261) | supp S3.13 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 330 | pass |
| 0.0002 (0.0002), 94 (94) | supp S3.13 | S3/B141b-16 | analysis/comparison_2025/production_comparison_2025.csv | supplementary.md line 330 | pass |
| 18 (18) | supp S3.13 | S3/Table S6 row 18 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 331 | pass |
| 19 (19.2771) | supp S3.13 | S3/Table S6 row 19 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 331 | pass |
| 13.1 (13.1), 59.2 (59.2) | supp S3.13 | S3/B141b-16 | analysis/comparison_2025/production_comparison_2025.csv | supplementary.md line 331 | pass |
| 6 (6) | supp S3.13 | S3/28 | register B073 | supplementary.md line 331 | pass |
| 0.1 (5) | supp S3.13 | S3/Table S6 caption | analysis/method_tests_2025/fidelity.csv | supplementary.md line 332 | pass |
| 3.5 (3.522) | supp S3.13 | S3/B141b-16 | analysis/comparison_2025/production_comparison_2025.csv | supplementary.md line 332 | pass |
| 2.8 (2.8) | supp S3.13 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 333 | pass |
| 352,737 (352737), 343 (343) | supp S3.13 | S3/B141b-16 | analysis/comparison_2025/production_comparison_2025.csv | supplementary.md line 333 | pass |
| -13 (13) | supp S3.13 | S3/Table S5 row 13 | qa/reports/B116_bases_and_fidelity.md | supplementary.md line 333 | pass |
| 7 (7.3) | supp S3.13 | S3/Table S5 row 7 | qa/reports/B116_bases_and_fidelity.md | supplementary.md line 333 | pass |
| 1.086 (1.086), 1.155 (1.155), 21.8 (21.752) | supp S3.13 | S3/B141b-16 | analysis/comparison_2025/production_comparison_2025.csv | supplementary.md line 334 | pass |
| 7.6 (7.6) | supp S3.13 | S8/10 | literature register L242 | supplementary.md line 334 | pass |
| 363.52 (363.52) | supp S3.13 | S3/57 | analysis/method_tests_2025/bases.csv | supplementary.md line 337 | pass |
| 0.01 (1) | supp S3.13 | S3/2 | register B262 | supplementary.md line 337 | pass |
| 4 (400.5) | supp S3.13 | S3/27 | analysis/method_tests_2025/cassidy.csv | supplementary.md line 337 | pass |
| 21 (21) | supp S3.14 | S3/29 | analysis/method_tests_2025/bases.csv | supplementary.md line 341 | pass |
| 7 (7.3) | supp S3.14 | S3/Table S5 row 7 | qa/reports/B116_bases_and_fidelity.md | supplementary.md line 341 | pass |
| 0.4 (41.5) | supp S3.14 | S3/B141b-9 | register B134 | supplementary.md line 341 | pass |
| 27 (27), 6 (6) | supp S3.14 | S3/28 | register B073 | supplementary.md line 341 | pass |
| 41.5 (41.5) | supp S3.14 | S3/70 | analysis/method_tests_2025/harmonised_comparison_lines.csv | supplementary.md line 341 | pass |
| 11 (11.3) | supp S3.14 | S3/Table S5 row 11 | analysis/method_tests_2025/bases.csv | supplementary.md line 341 | pass |
| 5 (5.18) | supp S3.14 | S3/2 | analysis/method_tests_2025/harmonised_comparison.csv | supplementary.md line 341 | pass |
| -1.9 (1.9) | supp S3.14 | S3/B141b-17 | qa/reports/B139_paper_B_third_line_bridge_panels.md | supplementary.md line 341 | pass |
| 41.4 (4.144e+07) | supp S3.14 | S3/B141b-7 | analysis/resilience_2025/drought_bounds_paper_B.csv | supplementary.md line 341 | pass |
| 6 (6) | supp S3.14 | S3/28 | register B073 | supplementary.md line 343 | pass |
| 41.50 (4.15035e+07) | supp S3.14 | S5/15 | results/ranges_2025-fixed_wide.csv | supplementary.md line 345 | pass |
| 8 (8) | supp S3.14 | S3/30 | register B258 | supplementary.md line 349 | pass |
| 20.8 (20.8), 9.3 (9.3), 27.2 (27.2) | supp S3.14 | S3/B141b-17 | qa/reports/B139_paper_B_third_line_bridge_panels.md | supplementary.md line 349 | pass |
| 7.3 (7.3), 14.1 (14.1) | supp S3.14 | S3/B141b-17 | qa/reports/B139_paper_B_third_line_bridge_panels.md | supplementary.md line 350 | pass |
| 4.2 (4.2) | supp S3.14 | S3/74 | qa/reports/B114_pairing_relaxed.md | supplementary.md line 350 | pass |
| 6 (6) | supp S3.14 | S3/28 | register B073 | supplementary.md line 351 | pass |
| -0.4 (41.5) | supp S3.14 | S3/B141b-9 | register B134 | supplementary.md line 351 | pass |
| 3.3 (3.3) | supp S3.14 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 351 | pass |
| 8.7 (8.7) | supp S3.14 | S3/B141b-17 | qa/reports/B139_paper_B_third_line_bridge_panels.md | supplementary.md line 351 | pass |
| 44.13 (44.13), 6.3 (6.3), 41.40 (41.4), 44.25 (44.25), 41.35 (41.35), -0.37 (0.37), 40.73 (40.73), -1.9 (1.9) | supp S3.14 | S3/B141b-17 | qa/reports/B139_paper_B_third_line_bridge_panels.md | supplementary.md line 352 | pass |
| 31.1 (3.11154e+07) | supp S3.14 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 354 | pass |
| 3.3 (3.3) | supp S3.14 | S3/24 | analysis/method_tests_2025/fidelity.csv | supplementary.md line 354 | pass |
| 0.6 (57) | supp S3.14 | S3/49 | analysis/method_tests_2025/gap_attribution_readable.csv | supplementary.md line 354 | pass |
| 0.932 (0.932), 0.968 (0.968), 1.123 (1.123), 1.050 (1.05) | supp S3.14 | S3/B141b-17 | qa/reports/B139_paper_B_third_line_bridge_panels.md | supplementary.md line 354 | pass |
| 103.6 (103.6), 103.3 (103.3), 5 (5), 5 (5), 5 (5) | supp S4 | S4/1 | analysis/comparators_2025/diet_land.csv | supplementary.md line 358 | pass |
| 2.5 (2.5), 118.0 (118), 112.4 (112.4), 2.5 (2.5) | supp S4 | S4/2 | register B216 | supplementary.md line 358 | pass |
| 76.8 (76.8) | supp S4 | S4/3 | register A258 | supplementary.md line 358 | pass |
| 2.29 (2.29), 4.58 (4.58) | supp S4 | S4/B141b-18 | analysis/comparators_2025/diet_land.csv | supplementary.md line 358 | pass |
| 7.5 (7.5), 7.5 (7.5) | supp S4 | S4/Table S2 row 5 | analysis/comparators_2025/diet_land.csv | supplementary.md line 358 | pass |
| 10 (10) | supp S4 | S4/Table S2 row 6 | analysis/comparators_2025/diet_land.csv | supplementary.md line 358 | pass |
| 15 (15) | supp S4 | S4/Table S2 row 7 | analysis/comparators_2025/diet_land.csv | supplementary.md line 358 | pass |
| 5.5 | supp S4 | S4/B141b-18 | qa/reports/V19_diet_route.md ("a cliff after 5.5% (101.1, then 89.7 at 6%") (checked by hand) | supplementary.md line 358 | pass |
| 101.1, 89.7 | supp S4 | S4/B141b-18 | qa/reports/V19_diet_route.md (checked by hand) | supplementary.md line 358 | pass |
| 6 (5.93) | supp S4 | S4/3 | analysis/comparators_2025/diet_land.csv | supplementary.md line 358 | pass |
| 1 (1.484) | supp S4 | S4/Table S2 row 11 | analysis/nutrition_lp_2025/variants.csv | supplementary.md line 360 | pass |
| 12 (12), 57.8 (57.8) | supp S4 | S4/Table S2 row 1 | analysis/comparators_2025/diet_land.csv | supplementary.md line 364 | pass |
| 53.6 (53.6) | supp S4 | S3/Table S7 row 16 | analysis/method_tests_2025/intake_variant.csv | supplementary.md line 364 | pass |
| 0.3 (0.3), 6.23 (6.23) | supp S4 | S4/1 | analysis/comparators_2025/diet_land.csv | supplementary.md line 364 | pass |
| 5.93 | supp S4 | S4/B141b-19 | analysis/comparators_2025/diet_land.csv (5.93) (checked by hand) | supplementary.md line 364 | pass |
| 0 (0.3), 103.6 (103.6), 0.0 (0.3) | supp S4 | S4/1 | analysis/comparators_2025/diet_land.csv | supplementary.md line 365 | pass |
| 0.27 (27.28), 0.27 (27.28) | supp S4 | S5/B141b-20 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 365 | pass |
| 2.5 (2.5) | supp S4 | S4/2 | register B216 | supplementary.md line 366 | pass |
| 100.4 (100.4), 0.28 (0.28), 0.0 (0.3), 0.28 (0.28) | supp S4 | S4/1 | analysis/comparators_2025/diet_land.csv | supplementary.md line 366 | pass |
| 5 (5), 103.3 (103.3), 2.58 (2.58) | supp S4 | S4/1 | analysis/comparators_2025/diet_land.csv | supplementary.md line 367 | pass |
| 0.29 (0.29) | supp S4 | S3/38 | register B145 | supplementary.md line 367 | pass |
| 2.29 (2.29) | supp S4 | S4/B141b-18 | analysis/comparators_2025/diet_land.csv | supplementary.md line 367 | pass |
| 7.5 (7.5) | supp S4 | S4/Table S2 row 5 | analysis/comparators_2025/diet_land.csv | supplementary.md line 368 | pass |
| 66.9 (66.9), 0.3 (0.3), 4.88 (4.88) | supp S4 | S4/1 | analysis/comparators_2025/diet_land.csv | supplementary.md line 368 | pass |
| 4.58 (4.58) | supp S4 | S4/B141b-18 | analysis/comparators_2025/diet_land.csv | supplementary.md line 368 | pass |
| 10 (10) | supp S4 | S4/Table S2 row 6 | analysis/comparators_2025/diet_land.csv | supplementary.md line 369 | pass |
| 58.8 (58.8), 0.3 (0.3), 5.33 (5.33), 5.63 (5.63) | supp S4 | S4/1 | analysis/comparators_2025/diet_land.csv | supplementary.md line 369 | pass |
| 15 (15) | supp S4 | S4/Table S2 row 7 | analysis/comparators_2025/diet_land.csv | supplementary.md line 370 | pass |
| 48.3 (48.3), 0.3 (0.3), 6.68 (6.68), 6.98 (6.98) | supp S4 | S4/1 | analysis/comparators_2025/diet_land.csv | supplementary.md line 370 | pass |
| 85.5 (85.5), 0.28 (0.28), 3.46 (3.46), 3.74 (3.74) | supp S4 | S4/1 | analysis/comparators_2025/diet_land.csv | supplementary.md line 371 | pass |
| 202.1 (202.1), 1.06 (1.06) | supp S4 | S4/1 | analysis/comparators_2025/diet_land.csv | supplementary.md line 372 | pass |
| 0.14 (14) | supp S4 | S5/B141b-20 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 372 | pass |
| 1.2 (1.2) | supp S4 | S3/37 | register B326 | supplementary.md line 372 | pass |
| 422.3 (422.3), 0.06 (5.93), 0.13 (0.13), 0.19 (0.19) | supp S4 | S4/1 | analysis/comparators_2025/diet_land.csv | supplementary.md line 373 | pass |
| 300.6 (3.0055e+08) | supp S4 | S4/Table S2 row 11 | analysis/nutrition_lp_2025/variants.csv | supplementary.md line 374 | pass |
| 532.9 (5.32857e+08) | supp S4 | S4/Table S2 row 11 | analysis/nutrition_lp_2025/variants.csv | supplementary.md line 375 | pass |
| 1.758 | supp S4 | S4/B141b-19 | register B032 statement (1.758) (checked by hand) | supplementary.md line 377 | pass |
| 5.93 | supp S4 | S4/B141b-19 | analysis/comparators_2025/diet_land.csv (5.93) (checked by hand) | supplementary.md line 377 | pass |
| 9.0 (9), 14.0 (14) | supp S4 | S4/B141b-19 | analysis/method_tests_2025/design_choices_panels.csv | supplementary.md line 377 | pass |
| 19 (0.194) | supp S5 | S5/7 | analysis/sensitivity_2025/sobol_2025-fixed.csv | supplementary.md line 381 | pass |
| 23 (23) | supp S5 | S5/5 | analysis/sensitivity_2025/README.md | supplementary.md line 381 | pass |
| 0.24 (0.24), 0.21 (0.21), 33.4 (33.43), -19.4 (19.4), 49.5 (49.47), 19.2 (19.2) | supp S5 | S5/B141b-20 | qa/reports/B134_paper_B_drought_bound_and_pasture.md | supplementary.md line 383 | pass |
| 95 (95) | supp S5 | S5/9 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 383 | pass |
| 0.27 (27.28), 0.14 (14), 0.16 (16) | supp S5 | S5/B141b-20 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 383 | pass |
| 0.12 (121491), 0.03 (2.5), 0.02 (1.577), 0.04 (36.6), 0.01 (0.892291), 0.01 (0.892291), 0.02 (1.577), 20 (20), 20 (20), 20 (20), 20 (20) | supp S5 | S5/B141b-20 | analysis/resilience_2025/drought_bounds_paper_B.csv | supplementary.md line 383 | pass |
| 41.5 (4.15035e+07) | supp S5 | S5/15 | results/ranges_2025-fixed_wide.csv | supplementary.md line 383 | pass |
| 2,000 (20), 19 (0.194), 19 (0.194), 2,000 (20) | supp S5 | S5/7 | analysis/sensitivity_2025/sobol_2025-fixed.csv | supplementary.md line 385 | pass |
| 42,000 (420) | supp S5 | S5/7 | analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv | supplementary.md line 385 | pass |
| 18 (18), 0.4 (36.3), 18 (18), 18 (18) | supp S5 | S5/7 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 385 | pass |
| 40,000 (40000) | supp S5 | S5/7 | qa/reports/B130_widened_draws_improved.md | supplementary.md line 385 | pass |
| 1,000 (1000), 13 (13), 1,000 (1000) | supp S5 | S5/8 | register B116 | supplementary.md line 385 | pass |
| 95 (95), 3 (3) | supp S5 | S5/9 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 385 | pass |
| 97 (97) | supp S5 | S5/10 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 385 | pass |
| 13 (13) | supp S5 | S5/8 | register B116 | supplementary.md line 387 | pass |
| 0.115 (0.115) | supp S5 | S5/12 | register B250 | supplementary.md line 387 | pass |
| 0.528 (0.528) | supp S5 | S5/12 | register B251 | supplementary.md line 387 | pass |
| 50 (0.5), 50 (0.5) | supp S5 | S5/12 | qa/reports/V41_check_B115.md | supplementary.md line 387 | pass |
| 1.4 (1.4), 1.8 (1.8), 1.4 (1.4), 1.8 (1.8) | supp S5 | S5/Table S3a row 5 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 387 | pass |
| 1.2 (1.23), 2.2 (2.2), 1.2 (1.23), 2.2 (2.2) | supp S5 | S5/14 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 387 | pass |
| 48.0 (48) | supp S5 | S5/B141b-21 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 387 | pass |
| 26.9 (26.93), -35.1 (35.15), 32.7 (32.7), 1.27 (1.27), 61.8 (61.77) | supp S5 | S5/B141b-21 | qa/reports/B134_paper_B_drought_bound_and_pasture.md | supplementary.md line 387 | pass |
| 41.5 (4.15035e+07), 41.5 (4.15035e+07) | supp S5 | S5/15 | results/ranges_2025-fixed_wide.csv | supplementary.md line 387 | pass |
| 15.6 (1.56232e+07) | supp S5 | S5/Table S3 row 2 | results/ranges_2025-fixed_wide.csv | supplementary.md line 387 | pass |
| 1.78 (1.779) | supp S5 | S5/B141b-21 | analysis/resilience_2025/drought_bounds_paper_B.csv | supplementary.md line 387 | pass |
| 35.2 (35.153) | supp S5 | S5/B141b-21 | qa/reports/V49_check_B134.md | supplementary.md line 387 | pass |
| 53.6 (5.36437e+07) | supp S5 | S5/Table S3 row 7 | results/ranges_2025-improved_wide.csv | supplementary.md line 387 | pass |
| 12 (12), 14 (14), 12 (12), 14 (14), 12 (12) | supp S5 | S5/Table S3a row 1 | analysis/waste_2025/README.md | supplementary.md line 393 | pass |
| 0 (0.5) | supp S5 | S5/Table S3a row 2 | methods/loss-factors-australia/method.json | supplementary.md line 394 | pass |
| 1 (0.528) | supp S5 | S5/10 | analysis/sensitivity_2025/sobol_2025-fixed.csv | supplementary.md line 394 | pass |
| 474 (474) | supp S5 | S5/Table S3a row 2 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 394 | pass |
| 17.3 (17.3), 38.2 (38.2) | supp S5 | S3/B141b-4 | analysis/sensitivity_2025/README.md | supplementary.md line 395 | pass |
| 0 (0.5) | supp S5 | S5/Table S3a row 2 | methods/loss-factors-australia/method.json | supplementary.md line 396 | pass |
| 1 (0.528) | supp S5 | S5/10 | analysis/sensitivity_2025/sobol_2025-fixed.csv | supplementary.md line 396 | pass |
| 7215.0 (7.21501e+06) | supp S5 | S5/Table S3a row 4 | pipeline/yields/recent/livestock_zone.py | supplementary.md line 396 | pass |
| 1.000 (1), 1.286 (1.286), 1.4 (1.4), 1.8 (1.8) | supp S5 | S5/Table S3a row 5 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 397 | pass |
| 1.356 (1.35557), 1.289 (1.28891) | supp S5 | S5/Table S3a row 6 | data/abs-2022-25/group_trend.json | supplementary.md line 398 | pass |
| 39.0 (3.89946e+07), 41.5 (4.15035e+07) | supp S5 | S5/15 | results/ranges_2025-fixed_wide.csv | supplementary.md line 400 | pass |
| 29.8 (29.8), 43.1 (43.1), 1.45 (1.45), 13.0 (13) | supp S5 | S5/16 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 400 | pass |
| 16.2 (16.2), 1.24 (1.24), 35.6 (35.6), 51.2 (51.2), 1.44 (1.44), 15.3 (15.3), 19.1 (19.1), 1.25 (1.25) | supp S5 | S5/16 | qa/reports/V41_check_B115.md | supplementary.md line 400 | pass |
| 48.1 (4.81005e+07) | supp S5 | S5/15 | results/ranges_2025-improved_wide.csv | supplementary.md line 400 | pass |
| 53.6 (5.36437e+07) | supp S5 | S5/Table S3 row 7 | results/ranges_2025-improved_wide.csv | supplementary.md line 400 | pass |
| 5 (5) | supp S5 | S5/Table S3a row 2 | methods/loss-factors-australia/method.json | supplementary.md line 402 | pass |
| 95 (95) | supp S5 | S5/9 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 402 | pass |
| 1 (0.528) | supp S5 | S5/10 | analysis/sensitivity_2025/sobol_2025-fixed.csv | supplementary.md line 402 | pass |
| 5 (5) | supp S5 | S5/Table S3a row 2 | methods/loss-factors-australia/method.json | supplementary.md line 404 | pass |
| 95 (95) | supp S5 | S5/9 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 404 | pass |
| 19 (0.194), 2,000 (20) | supp S5 | S5/7 | analysis/sensitivity_2025/sobol_2025-fixed.csv | supplementary.md line 406 | pass |
| 31.1 (3.11154e+07), 49.2 (4.91698e+07), 26.2 (2.61605e+07), 58.1 (5.81426e+07), 0.25 (0.253), 0.06 (0.064), 0.06 (0.064), 0.05 (0.049) | supp S5 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 406 | pass |
| 41.5 (4.15035e+07) | supp S5 | S5/15 | results/ranges_2025-fixed_wide.csv | supplementary.md line 406 | pass |
| 0.32 (0.3186), 0.33 (0.3268), 0.23 (23) | supp S5 | S5/Table S3 row 1 | analysis/sensitivity_2025/sobol_2025-fixed.csv | supplementary.md line 406 | pass |
| 0.27 (27.28) | supp S5 | S5/B141b-20 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 406 | pass |
| 0.24 (0.24) | supp S5 | S5/B141b-20 | qa/reports/B134_paper_B_drought_bound_and_pasture.md | supplementary.md line 406 | pass |
| 0.04 (36.6) | supp S5 | S5/B141b-20 | analysis/resilience_2025/drought_bounds_paper_B.csv | supplementary.md line 406 | pass |
| 19 (0.194), 2,000 (20) | supp S5 | S5/7 | analysis/sensitivity_2025/sobol_2025-fixed.csv | supplementary.md line 407 | pass |
| 13.3 (1.33072e+07), 18.8 (1.87656e+07), 12.4 (1.2422e+07), 19.9 (1.98984e+07), 15.6 (1.56232e+07) | supp S5 | S5/Table S3 row 2 | results/ranges_2025-fixed_wide.csv | supplementary.md line 407 | pass |
| 0.58 (58), 0.56 (0.5628) | supp S5 | S5/Table S3 row 1 | analysis/sensitivity_2025/sobol_2025-fixed.csv | supplementary.md line 407 | pass |
| 0.20 (0.204), 0.20 (0.204) | supp S5 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 407 | pass |
| 0.14 (14), 0.14 (14) | supp S5 | S5/B141b-20 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 407 | pass |
| 0.04 (36.6), 0.04 (36.6) | supp S5 | S5/B141b-20 | analysis/resilience_2025/drought_bounds_paper_B.csv | supplementary.md line 407 | pass |
| 13 (13) | supp S5 | S5/8 | register B116 | supplementary.md line 408 | pass |
| 43.4 (4344), 54.3 (5.4251e+07), 49.4 (4.93894e+07), 0.821 (0.821), 0.152 (151968) | supp S5 | S5/Table S3 row 3 | results/ranges_2025-mirror.csv | supplementary.md line 408 | pass |
| 13 (13) | supp S5 | S5/8 | register B116 | supplementary.md line 409 | pass |
| 11.8 (0.118), 16.0 (16), 14.1 (1.41468e+07) | supp S5 | S5/Table S3 row 4 | results/ranges_2025-mirror.csv | supplementary.md line 409 | pass |
| 0.481 (0.481), 0.236 (0.236), 0.136 (135505) | supp S5 | S5/Table S3 row 3 | results/ranges_2025-mirror.csv | supplementary.md line 409 | pass |
| 13 (13) | supp S5 | S5/8 | register B116 | supplementary.md line 410 | pass |
| 36.3 (0.363), 45.8 (4579) | supp S5 | S5/Table S3 row 5 | results/ranges_2025-fixed.csv | supplementary.md line 410 | pass |
| 41.5 (4.15035e+07) | supp S5 | S5/15 | results/ranges_2025-fixed_wide.csv | supplementary.md line 410 | pass |
| 0.806 (0.806), 0.163 (0.163) | supp S5 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 410 | pass |
| 13 (13) | supp S5 | S5/8 | register B116 | supplementary.md line 411 | pass |
| 13.4 (1.33863e+07), 16.5 (0.165) | supp S5 | S5/Table S3 row 6 | results/ranges_2025-fixed.csv | supplementary.md line 411 | pass |
| 15.6 (1.56232e+07) | supp S5 | S5/Table S3 row 2 | results/ranges_2025-fixed_wide.csv | supplementary.md line 411 | pass |
| 0.521 (0.521), 0.363 (0.363), 0.086 (0.086) | supp S5 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 411 | pass |
| 18 (18) | supp S5 | S5/7 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 412 | pass |
| 2,000 (20) | supp S5 | S5/7 | analysis/sensitivity_2025/sobol_2025-fixed.csv | supplementary.md line 412 | pass |
| 37.9 (3.79033e+07), 60.0 (5.99707e+07), 32.0 (3.20068e+07), 69.5 (6.94725e+07), 53.6 (5.36437e+07) | supp S5 | S5/Table S3 row 7 | results/ranges_2025-improved_wide.csv | supplementary.md line 412 | pass |
| 0.33 (0.3268), 0.35 (0.3493) | supp S5 | S5/Table S3 row 1 | analysis/sensitivity_2025/sobol_2025-fixed.csv | supplementary.md line 412 | pass |
| 0.30 (0.003), 0.30 (0.003), 0.22 (0.223), 0.25 (0.253), 0.06 (0.064), 0.06 (0.064) | supp S5 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 412 | pass |
| 18 (18) | supp S5 | S5/7 | qa/reports/B115_monte_carlo_widened.md | supplementary.md line 413 | pass |
| 2,000 (20) | supp S5 | S5/7 | analysis/sensitivity_2025/sobol_2025-fixed.csv | supplementary.md line 413 | pass |
| 15.7 (1.56659e+07), 22.1 (2.20548e+07), 15.1 (1.50572e+07), 23.0 (2.29763e+07), 18.5 (1.8474e+07) | supp S5 | S5/Table S3 row 8 | results/ranges_2025-improved_wide.csv | supplementary.md line 413 | pass |
| 0.63 (634033), 0.66 (660820) | supp S5 | S5/Table S3 row 3 | results/ranges_2025-mirror.csv | supplementary.md line 413 | pass |
| 0.20 (0.204), 0.20 (0.204) | supp S5 | S5/Table S3 row 1 | results/ranges_2025-fixed_wide.csv | supplementary.md line 413 | pass |
| 0.14 (14) | supp S5 | S5/B141b-20 | analysis/method_tests_2025/fearnside_failure_curve.csv | supplementary.md line 413 | pass |
| 0.15 (0.1472) | supp S5 | S5/Table S3 row 1 | analysis/sensitivity_2025/sobol_2025-fixed.csv | supplementary.md line 413 | pass |
| 2 (2), 8 (8) | supp S6 | S6/2 | register B243 | supplementary.md line 417 | pass |
| 1.2 (1.2) | supp S6 | S6/3 | register B243 | supplementary.md line 417 | pass |
| 1.33 (1.33), 1.17 (1.17), 1.09 (1.09) | supp S6 | S6/4 | register B243 | supplementary.md line 417 | pass |
| 1.03 (1.03) | supp S6 | S6/B141b-22 | analysis/method_tests_2025/design_choices_panels.csv | supplementary.md line 417 | pass |
| 1 (1.2) | supp S6 | S6/2 | register B243 | supplementary.md line 423 | pass |
| 2 (2) | supp S6 | S6/2 | register B243 | supplementary.md line 424 | pass |
| 2.41 (2.41), 1.6 (1.58), 4.43 (4.43), 6.36 (6.36) | supp S6 | S6/Table S4 row 2 | analysis/method_tests_2025/design_choices.csv | supplementary.md line 424 | pass |
| 2.5 (2.5) | supp S6 | S4/2 | register B216 | supplementary.md line 424 | pass |
| 3 (2.67) | supp S6 | S6/Table S4 row 3 | analysis/method_tests_2025/design_choices.csv | supplementary.md line 425 | pass |
| 2.14 (2.14) | supp S6 | S6/Table S4 row 2 | analysis/method_tests_2025/design_choices.csv | supplementary.md line 425 | pass |
| 1.60 (1.6), 3.77 (3.77), 7.88 (7.88) | supp S6 | S6/B141b-22 | analysis/method_tests_2025/design_choices_panels.csv | supplementary.md line 425 | pass |
| 4 (4.43) | supp S6 | S6/Table S4 row 4 | analysis/method_tests_2025/design_choices.csv | supplementary.md line 426 | pass |
| 1.17 (1.17), 1.33 (1.33) | supp S6 | S6/4 | register B243 | supplementary.md line 426 | pass |
| 5 (5) | supp S6 | S6/Table S4 row 5 | analysis/method_tests_2025/design_choices.csv | supplementary.md line 427 | pass |
| 2.19 (2.19), 1.03 (1.03) | supp S6 | S6/B141b-22 | analysis/method_tests_2025/design_choices_panels.csv | supplementary.md line 427 | pass |
| 6 (6.36) | supp S6 | S6/Table S4 row 6 | analysis/method_tests_2025/design_choices.csv | supplementary.md line 428 | pass |
| 1.09 (1.09) | supp S6 | S6/4 | register B243 | supplementary.md line 428 | pass |
| 7 (7) | supp S6 | S6/Table S4 row 7 | register B243 | supplementary.md line 429 | pass |
| 2.67 (2.67) | supp S6 | S6/Table S4 row 2 | analysis/method_tests_2025/design_choices.csv | supplementary.md line 429 | pass |
| 8 (8) | supp S6 | S6/2 | register B243 | supplementary.md line 430 | pass |
| 2.66 (2.66) | supp S6 | S6/Table S4 row 2 | analysis/method_tests_2025/design_choices.csv | supplementary.md line 430 | pass |
| 9 (9) | supp S6 | S6/2 | register B243 | supplementary.md line 431 | pass |
| 10 (10) | supp S6 | S3/3 | register B012 | supplementary.md line 432 | pass |
| 11 (11) | supp S6 | S8/2 | register B166 | supplementary.md line 433 | pass |
| 12 (12) | supp S6 | S6/2 | register B243 | supplementary.md line 434 | pass |
| 1 (1) | supp S7 | S7/15 | qa/reports/V28_section7_matrix.md | supplementary.md line 440 | pass |
| 2 (2) | supp S7 | S7/15 | qa/reports/V28_section7_matrix.md | supplementary.md line 441 | pass |
| 9 (9) | supp S7 | S6/2 | register B243 | supplementary.md line 441 | pass |
| 3 (3) | supp S7 | S7/16 | qa/reports/V28_section7_matrix.md | supplementary.md line 442 | pass |
| 4 (4) | supp S7 | S7/16 | qa/reports/V28_section7_matrix.md | supplementary.md line 443 | pass |
| 28 (28), 28 (28), 25 (25), 28 (28) | supp S7 | S7/16 | qa/reports/V28_section7_matrix.md | supplementary.md line 447 | pass |
| 24 (24) | supp S7 | S7/15 | qa/reports/V28_section7_matrix.md | supplementary.md line 447 | pass |
| 25 (25), 28 (28), 7 (7), 7 (7), 7 (7), 7 (7) | supp S7 | S7/16 | qa/reports/V28_section7_matrix.md | supplementary.md line 449 | pass |
| 2 (2) | supp S7 | S7/15 | qa/reports/V28_section7_matrix.md | supplementary.md line 455 | pass |
| 276 (276) | supp S7 | S3/Table S8 row 7 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 455 | pass |
| 76.0 (0.76) | supp S7 | S3/Table S8 row 3 | analysis/method_tests_2025/cross_method_local.csv | supplementary.md line 455 | pass |
| 2 (2) | supp S7 | S7/15 | qa/reports/V28_section7_matrix.md | supplementary.md line 456 | pass |
| 145 (145) | supp S7 | S7/17 | qa/reports/V28_section7_matrix.md | supplementary.md line 456 | pass |
| 190 (190), 183 (183) | supp S7 | S3/33 | analysis/method_tests_2025/README.md | supplementary.md line 456 | pass |
| 3 (3) | supp S7 | S7/16 | qa/reports/V28_section7_matrix.md | supplementary.md line 457 | pass |
| 8.8 (8.8) | supp S8 | S3/11 | register B023 | supplementary.md line 461 | pass |
| 11 (11), 26 (26), 67 (67), 78 (78) | supp S8 | S8/2 | register B166 | supplementary.md line 461 | pass |
| 2.61 (2.61), 5.96 (5.96), 44 (43.8) | supp S8 | S8/4 | register B050 | supplementary.md line 463 | pass |
| 8.1 (8.1), 13.6 (13.6) | supp S8 | S8/5 | register B051 | supplementary.md line 463 | pass |
| 6 (6) | supp S8 | S3/28 | register B073 | supplementary.md line 465 | pass |
| 7.3 (7.3) | supp S8 | S8/9 | literature register L231 | supplementary.md line 465 | pass |
| 7.6 (7.6) | supp S8 | S8/10 | literature register L242 | supplementary.md line 465 | pass |
| 2.03 (2.03) | supp S8 | S8/12 | literature register L040 | supplementary.md line 467 | pass |
| 0 (0), 2 (2) | supp S8 | S8/14 | literature register L081 | supplementary.md line 469 | pass |
| 16 (16) | supp S8 | S8/20 | literature register L105 | supplementary.md line 479 | pass |
## Register rows touched

None.

## Rerun

From the repository root, with the scratch folder above: `python3 <scratch>/tr/run.py` (writes `res.json` in the scratch folder), then `python3 <scratch>/tr/strict.py`, `python3 <scratch>/tr/tab.py` and `python3 <scratch>/tr/table.py`. `python3 qa/tools/wordcount.py B` for the word count.
