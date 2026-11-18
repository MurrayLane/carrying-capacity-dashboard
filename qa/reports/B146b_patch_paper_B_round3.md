# B146b: Paper B and its response letter patched to the third-round reports (R06c, R06d)

Brief: `qa/briefs/B146b_patch_paper_B_round3.md`. No git, no subagents, no network. Written under `papers/B_methods/` and this report only, with one exception that the coordinator must deal with (next section).

## Exception: one file outside the allowed paths was rewritten

To check numbers I ran `python3 qa/tools/numbers_lint.py`. That tool writes `qa/reports/numbers_lint_2026-11-07.csv` on every run, and it replaced the existing file (mtime 2026-11-18 23:29). I have no backup and may not run git. The coordinator should restore it with `git checkout -- qa/reports/numbers_lint_2026-11-07.csv` (or accept the new copy; the tool is deterministic over the repository as it stands, so the content probably differs only where documents changed). I did not run `manuscript_audit.py`. Nothing else outside the allowed paths was written; `paper_B_draft1.md`, `references.md`, the registers and `analysis/` are untouched (draft1 checked byte for byte against a copy taken before the work; the assemble check ran on a scratch copy).

## Counts

* Main text, `python3 qa/tools/wordcount.py B`: **7,948** (cap 7,950; was 7,939). By section: 1: 714, 2: 519, 3: 295, 4: 885, 5: 2,715, 6: 1,324, 7: 651, 8: 468, 9: 377.
* Abstract: **250** words (cap 250).
* Highlights, characters: 76, 84, 84, 83, 77 (cap 85).
* Response letter: **3,417** words (was 2,458); the new "Third round" section is 929 words.
* Supplement: 15,328 words by `wc` (was 14,859; not capped).
* `assemble_draft.py B` ran on a scratch copy: 4 section files, no error. No em dash in any file I wrote (the only dashes found in `papers/B_methods` are en dashes in `references.md`, untouched).

## R06c (ecological economist), point by point

| Point | Fix or stand |
|---|---|
| M1 first part: line (b) comparison, line (a) counterfactual; delete "classification, not a finding" | Done in the abstract, section 1 closing paragraph, 5.11 and 9.1. The sentence "Which line holds is a classification, not a finding" is deleted. 5.11 now reads "Line (b) is the comparison ... Line (a) is a counterfactual sensitivity". |
| M1 second part: pooled reading is this study's aggregation | 5.11: "the footprint's accounting by land type, its pooled reading being this study's sum of the land types with no equivalence factor" (S3.11 holds the arithmetic). |
| M2: edition and date of the public footprint release | Stands for Murray. The project files do not record the edition or date checked. 5.4 now has one sentence: the national accounts were not used (no Australian row in the public release, a licence not sought), so the results concern the 1990s food-row recipe, not the current accounts. That also meets the request to say so once. |
| M3 | Answered in round two; no change. |
| M4: two sentences still draw a finding | Fixed by the Table 9, 7.2, 7.3 and 7.6 changes below. |
| M5 | Answered; no change. |
| M6: the 1.51 conversion assumes land scales with food energy | 5.11, line (c) paragraph: "(for the footprint and HALF, which count mass, this assumes land a person scales in proportion to food energy)". |
| M7 | Answered; no change. |
| M8: rescale the footprint, HALF and energy balance to the ten-year output mean | Not done, and the paper says why (S3.14, 5.1). The rule asked for was "a plain ratio of figures already in `production_window_10y.csv` and the method readings". It is not: those readings scale with output item by item, the csv holds item ratios and group medians but no weights, so a ratio of medians would be a guess. Listed as a compute job (the three recipes on FAOSTAT 2014 to 2023 production). S3.14 gives the direction: cropland-set readings (cropland-bound footprint, 112.5 to 117.0) would fall with crop output, +20.8% against its ten-year mean; the binding-land-type footprint (53.9 to 77.9) rests on livestock output, -0.4% (total meat -1.3%), so it would move little. 5.1 carries one sentence; Table S11's note says no primary row is rescaled. |
| M9: tie to van den Bergh and Rietveld (2004) in the introduction | Done, one clause in section 1 ("pooled 115 such estimates (section 2)"). |
| New 1: "sufficient" pairing | Abstract, highlight 4, 5.14, 7.6, 9.1: see the table under "Both referees". |
| New 2: model "well suited" for food security | Table 9 cell, the Table 9 caption (failure view), 7.1, 7.2, 7.6, S7, Table S15: model and failure view "partly suited" for purpose 1, limit given (weather factor untested on pasture-fed output, which binds). 7.1 and S7 say the lowering was made by the author and the second rater has not seen it; Table S15 gains two rows (the second rater's reasons are copied from `V28_section7_matrix.md`, not invented). |
| New 3: 7.3 credits the model with the exports count | 7.3: "a proportional count of exports, a ratio between methods and not a model run". |
| New 4: classification sentence | As M1. |
| Minor 2: 211 is the 1990-91 energy balance | Abstract: "(the top, the 1990-91 energy balance)". |
| Minor 7, 13, 14: Table 2, Figures 1 to 3, declaration brackets, DOI | Stand; not in this brief's scope and not buildable from the records (no catalogue csv, no plotting scripts, the model names and CRediT name are the author's). Listed for Murray. |
| Minor 15, 16 | 15 declined for the word limit (accepted by the referee). 16: 3.1 already says "The selection record holds no counts by route". |
| New: abstract omits the binding-land-type reading | Abstract: "the footprint at its binding land type reads 53.9 to 77.9". |
| New: Buzby 2010 in Tables S10 and S14 | Replaced by "Muth et al. 2011; Lane 2014, pp. 201 to 202" (as 8.5; Buzby is not in the reference list). |

## R06d (modeller), point by point

| Point | Fix or stand |
|---|---|
| M1: abstract does not say three readings are constructed | Stands for the 250-word cap (sections 4.3, 4.5, 5.5 to 5.7 say it method by method); the referee marked M1 acceptable. |
| M2: meat inputs vs FAOSTAT | 5.1: the meat inputs on the binding land "carry the thesis calibration for cattle and sheep and were not compared with FAOSTAT's; the comparison covers crops and milk (Table S1)". The optional one-input check is not run (decision 145 keeps the model off the FAOSTAT layer). |
| M3, M5, M7 | Accepted by the referee; no change. |
| M4: "sufficient cause" outruns the bridge | Done, with the numbers: at HALF's land exchange rate the pooling rule is 18% of the 34.5 million gap; the pairing closes the gap to HALF only when pasture-fed food is replaced at equal energy (variant 1, 81.7 million, protein 93 to 81 g a day) or equal energy and protein (85.4). In the abstract, highlight 4, 5.14, 7.6, 9.1. |
| M6: authors not contacted; letter bracket | Letter bracket replaced by what 5.2 says ("had not been consulted at the time of writing"). Whether requests were sent is Murray's (decision 143 says they are to go; 5.2 changes when they do). |
| M8: placeholders, brackets, DOI, `qa/` paths, letter notes | `qa/` paths removed from S3.14 (hash now "recorded in the project's data register") and Table S15. Both "[For the author ...]" notes replaced by statements the paper carries. Table 2, Figures 1 to 3, declaration brackets and DOI stand (as above). |
| M9: Mottet et al. 2017 | `qa/literature_register.csv` L122: record only, text not reached, no file on disk. Not cited. For Murray: obtain from https://doi.org/10.1016/j.gfs.2017.01.001. Named in the letter's not-cited list with the DOI. |
| New 1 | As M4. |
| New 2: target on a different requirement basis | 5.10, 5.14, highlight 3: line (c) multiples (readings x 1.512). Footprint 98.0 to 176.9 million (2.36 to 4.26 times the model), HALF 114.9 (2.77), energy and protein balance 219.6 to 225.0 (5.29 to 5.42), all from `harmonised_line_c.csv` rows c1. 5.14: HALF at 114.9 is above variant 1's 81.7, which carries the model's own requirement and waste (with 7.376 MJ in place of 8.0, line (c) HALF would read about 125, still above; recorded in the claims row). |
| New 3: what the short term measures | 6.2: "To first order the short-term figure is national pasture-fed output, exports included, over the diet's pasture-fed food a person; this is why the commodity balance's meat reading, 40 to 41 million, sits on the model's 41.5 (section 5.7)". Claims row cites `analysis/paper_a/meat_balance_identity.csv` (41.27 and 41.17 against 41.504; A443) and notes the identity is first order only (the csv's ratio differs by 4.5% to 4.8%). |
| New 4: S7 "two columns"; letter 14.7% | S7 now says Table 9 has one model column. Letter: "closes 14.7% of the distance to the model". |
| Minor 2 (waste 1.33 against 1.14) | Stands as untraced; no record explains it. Table 8 note states the gap (1.14 is 1 over 0.88) and that the mechanism has not been traced. Compute job for Murray's decision. |
| Minor 3 (S4 "not checked" vs the cliff in 6.5) | The cliff is a computed result (Table S13); only its cause is untraced. S4 says so; 6.5 adds "whose cause is not traced (section S4)". |
| Minor 13 ("balance" names three things) | Table 9 caption and S7 call the model "the land-and-diet model"; "balance" now names only the energy and protein balance and the commodity balance. |
| Minor 14 (kcal without MJ) | S3.11: 2,892 kcal (12.1 MJ), 1,912 kcal (8.0 MJ); arithmetic at 4.184 kJ per kcal. |

## Both referees: the pairing and the multiples

* Abstract: "A bridge from HALF to the model gives the pooling rule 18% of the gap at HALF's land exchange rate; relaxing the pasture-crop pairing closes the gap only if pasture-fed food is replaced at equal energy or protein (81.7 and 85.4 million; protein 93 to 81 g a day in the first)."
* Highlight 4: "The pairing reaches HALF only at equal energy or protein; pooling is 18% of the gap". Highlight 3: "Footprint, HALF: 1.6 to 2.8 times the model; 2.4 to 4.3 on one requirement and waste".
* 5.14 (replaces the "sufficient cause" sentence), 7.6, 9.1 as above. "Sufficient cause" no longer appears in any file I may write (the register rows B247 and B410 still carry it; see below).

## Sentences changed (main text)

Abstract (rewritten); section 1 (closing paragraph; one clause on van den Bergh and Rietveld); 5.1 (meat inputs; the other methods not rescaled); 5.4 (national accounts sentence); 5.10 (line (c) sentence added; failure-view sentence shortened to a pointer); 5.11 (classification paragraph, line (a) and (b) paragraph reordered with (b) first, line (c) assumption, "Which line holds ..." deleted; the Table 5 spread sentence and the median-closure clause cut for the word cap); 5.13 (the three multiples moved to Table S6); 5.14 (bridge sentence shortened to three terms, the closure sentence, line (c) HALF); 6.2 (first-order sentence); 6.5 (cliff cause); 6.10, 6.11, 8.7 (three repeats cut); 7.1 (disclosure of the lowered ratings); 7.2, 7.3, 7.6 (rewritten); 9.1 (rewritten), 9.2 (62.9 removed); Table 8 note (1.33 against 1.14); Table 9 cell and caption. Supplement: S3.11 (MJ), Table S11 (three line (c) rows, note), S3.14 (caveat, hash wording), S4, S7, Table S15 (path out, two rows), Tables S10 and S14 (Buzby out).

Cuts made for the word cap are all repeats or detail held elsewhere (Tables 5, 7, S5, S6); the claims rows for them were removed or re-pointed.

## Claims csvs

Retired fragments removed, changed ones re-worded. New rows: `B_s01-03_claims.csv` B146b-1 to B146b-9; `B_s04-05_claims.csv` B146b-1 to B146b-9; `B_s06-09_claims.csv` B146b-1 to B146b-8; `highlights_claims.csv` highlights 3 and 4 (replaced and added); `supplementary_claims.csv` B146b-1 to B146b-6. Every new number has a row. Open flags: B146b-3 (section 4-5 csv) is an open decision row for Murray (edition and date of the footprint release).

## Register rows that move (not touched; for the register job)

* **B247** (section 7, "the pasture and crop pairing is a sufficient cause of the gap ..."): the cause clause is replaced by the 18% pooling share and the equal-energy or equal-protein closure (81.7 and 85.4).
* **B410** (section 5, same "sufficient cause ... and one of several" wording): same change.
* **B238** (matrix purpose 1): FAIL and LDB move from "well suited" to "partly suited". The brief named B130 and B137; their numbers (5.8 to 6.1% a year; 41.5 to 18.9) do not change, but both should carry a note that the failure view is rated partly suited for food security because the weather factor is untested on pasture-fed output. B238 is the row whose value moves.
* **B242** (counts seven methods): the abstract no longer says "read two ways".
* New rows needed: line (c) readings 98.0 to 176.9, 114.9, 219.6 to 225.0 and their multiples 2.36 to 4.26, 2.77, 5.29 to 5.42; protein 93 to 81 g a day with variant 1; the first-order identity of 6.2 (with A443); the 1.14 against 1.33 waste difference; the Table S15 rows for purpose 1; the kcal to MJ conversions.

## For Murray (decision rows)

1. Edition and date of the public footprint release checked (R06c M2).
2. Mottet et al. 2017: obtain from https://doi.org/10.1016/j.gfs.2017.01.001 (record only, not cited).
3. Table 2, Figures 1 to 3, model names and CRediT name in the declarations, the DOI.
4. Whether the HALF and Cassidy requests have gone out (5.2, letter).
5. Compute jobs, not run: the footprint, HALF and energy balance recipes on ten-year item production (S3.14); a trace of the 1.33 waste factor; the optional FAOSTAT beef and sheep meat input check (R06d M2).
6. `SECTION7_DRAFT.md` (not in this brief's write list) still holds the old purpose 1 rating for the model; Table 9's caption cites it as the source.

## Wrong-value check

EXAMPLE ONLY, not a finding. The builder's note `analysis/method_tests_2025/README_round2_B139.md` gives the diet-composition term of the seven-switch bridge as "22.7 million"; the checker V53 amended it ("should read 22.6 or 22.65"; csv -22.65, checker -22.64). My check compares the paper's figure with the checker's amended one (`scratchpad/wrongvalue.py`, run with `--wrong`):

```
paper text 22.6 vs checker 22.6 -> MATCH (csv 22.65)
builder README figure (EXAMPLE, not used) 22.7 vs checker 22.6 -> MISMATCH (csv 22.65)
```

The paper carries 22.6, the checker's wording.

## Changed files

* `papers/B_methods/draft/B_s01-03.md`, `B_s04-05.md`, `B_s06-09.md`, `B_s10_declarations.md` (drafter note only)
* `papers/B_methods/draft/B_s01-03_claims.csv`, `B_s04-05_claims.csv`, `B_s06-09_claims.csv`, `highlights_claims.csv`, `supplementary_claims.csv`
* `papers/B_methods/draft/highlights.md`, `supplementary.md`
* `papers/B_methods/OUTLINE.md`, `SECTION_SCOPE.md` (one entry each)
* `papers/B_methods/response_letter_round2.md`
* `qa/reports/B146b_patch_paper_B_round3.md` (this report)
* Outside the list by accident: `qa/reports/numbers_lint_2026-11-07.csv` (see the first section).
