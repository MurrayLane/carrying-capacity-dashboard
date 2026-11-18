# V45a: blind read of the revised Paper A draft

Brief: `qa/briefs/V45a_read_paper_A.md` (headed "V45b" inside the file; same task). Files read: `papers/A_results/draft/paper_A_draft1.md` (main text, abstract), `supplementary.md`, `highlights.md`, `references.md`, the four claims csvs, `qa/claims_register.csv`, `qa/literature_register.csv`, `qa/sources_register.csv`, the checker reports V36 to V42 (V43 and V44 do not exist), the builder reports B110 to B124 where a row named them, and the data files each row names. No git, no subagents, no network. My scripts and scratch output are in the session scratch folder; this report is the only repository file written. I checked that `paper_A_draft1.md` holds every paragraph of `A_s01-04.md`, `A_s05-08.md` and `A_s09-12.md` unchanged (144 paragraphs, 0 missing), so the trace runs on the assembled draft.

## Summary

* **Numbers traced:** 1,763 printed values in the abstract, main text, tables, highlights and supplement (plus 569 years, 90 section or table numbers and 43 page numbers, which the structural rows and the citation check cover). **Fails: 32** (2 wrong value, 10 no claims row, 20 derived and printed in no file). Every derived fail checks on arithmetic.
* **Checker-wording fails:** 6 (listed below), the most serious being that every 19-choice shocked figure rests on B123, which has no checker (V44 does not exist).
* **Tier A rows pending gate 5:** 16 Paper A rows; the draft carries the checker-passed pending value in 10, a different (later, unchecked) value in 3 (A014, A183, A187), a conditional value in 1 (A038), and 2 need register attention (A196 partly, A223 register text).
* **Word count:** `python3 qa/tools/wordcount.py A` prints TOTAL 7943 (limit 7,950): pass. **Abstract:** 246 words (150 to 250): pass. **Highlights:** 5, at 80, 85, 81, 71 and 81 characters: pass on length. **Em dash:** 1, in `references.md` line 43: fail.

**The three most serious fails**

1. **0.72 is wrong; it should be 0.71** (section 8.1 and Table S9, 1-in-20 lower end of capacity over population on the 19-choice draws). `analysis/paper_a/shocks_ranges_wide.csv` line 18 prints 0.715, itself rounded; 19,735,337 / 27,608,200 = 0.7148, which prints 0.71. The value comes from B123, which no checker has passed.
2. **Table 2 and section 4 say the forward and reverse walks "bound" the average; three long-term rows break this.** Crop yields average +257,755 against +219,940 and +253,434; long-term liquid fuel +124,764 against +90,858 and +114,983; land and livestock together -619,428 against -608,748 and -591,253 (`analysis/comparison_2025/capacity_by_cause_corrected_orders.csv`, zone 1, long rows). The claim is true in the short term only.
3. **The headline shocked ranges are unchecked and differ from the register's pending values.** Section 8.1, the abstract sentence on "the full Monte Carlo range" and Table S9's 19-choice column all rest on B123 ("checker pending V44" in the claims csv). Register rows A014, A183 and A187 carry pending gate 5 values on the 13-choice draws (27.0 to 34.0; 0.98 to 1.23; 0.83 to 1.05), checked by V38; the draft prints 23.1 to 36.5, 0.84 to 1.32 and 0.72 to 1.13 instead.

## Tolerance

Exact for every printed number: a printed value passes only when the named file prints it, or prints a value that rounds to it at the printed number of digits (half up). A number the paper derives (a difference, a share, a percentage change) that no file prints is a fail under the brief, even when the arithmetic holds; those are marked "FAIL derived" and the arithmetic is given.

## Wrong-value example (deliberate)

I misread North Tasmania's 5th-percentile short-term capacity in Table 7 as 174,478 (the paper prints 174,487) and searched the two files its row names. `results/ranges_2025-fixed.csv` and `analysis/paper_a/regions_in_depth.csv` each give 0 matches for 174478 and 1 match for 174487 (`results/ranges_2025-fixed.csv` line 114: `57,short,174487,...`). The check can fail. The same route caught one real error: 0.72 (above).

## Method

1. A script split the four files into sentences and table rows, pulled every number, matched each to a row of the section's claims csv (by the row's text fragment, by the table row label, or by the number inside the fragment), resolved the row's named files (paths in the row, the register's `output_file` for an A or B id, the builder and checker reports, the literature register for an L id) and searched them for the printed number or a value that rounds to it.
2. I then opened by hand every source cell for: the abstract; Tables 1 to 7; sections 3, 4 (against `capacity_by_cause_corrected_orders.csv`), 5 (against `results/scale_curve.csv`), 7 (against `long_term_levers.csv`, `long_term_regions.csv`), 8.1 and Table 6 (against `shocks_summary-3.csv`, `shocks_ranges.csv`, `shocks_ranges_wide.csv`), 9.1 (against `results/ranges_2025-fixed*.csv`, `sobol_2025-fixed.csv`), 10 and Table 7 (against `regions_in_depth.csv`, `regional_flips-3.csv`, `ranges_2025-fixed.csv`); Tables S1, S2, S5, S7, S8, S9; every number the script could not place. All of these pass except the fails listed.
3. Limit: in the long tail of the table, a "pass" means the number was found at the stated line of the named file by search. Small integers (counts such as 3 or 53) can match a different cell by coincidence; for those the row's register id or report is the real support. I found no wrong value in the tail, but I did not open every tail cell by hand.

## Fails in the number trace (also first in the trace table)

| Number | Where | Fail | Detail |
|---|---|---|---|
| 0.72 | 8.1 sentence 7; Table S9 row 2 | wrong value | exact 0.7148 prints 0.71; the file's 0.715 was rounded twice. Rewrite: "19.7 to 31.2 million at 1 in 20 (central 26.3; 0.71 to 1.13 times)". |
| 41.5, 33.3, 1 in 10, 1 in 20, 100, 57%, 37% | highlights 1, 3, 4, 5 | no row | no claims csv has highlight rows; add five rows pointing to A001, A003, A196, A011 and A088 (B104 already names them). |
| 153 | 8.1, "ranks its factors in the 153 seasons" | no row | the section 2 and S4 rows carry it; section 8 has none. |
| 1.3, 1.0, 1.0 million | section 3, population growth | derived | not printed; `regional_flips-3.csv` gives +1,282,995, +1,006,997, +991,502. |
| 141 thousand | section 3, Murrumbidgee-ACT | derived | 738,895 - 597,750 = 141,145. |
| 65% to 86% | section 4, forward-walk livestock share | derived | ratio of two cells of `capacity_by_cause_corrected.csv`. |
| 12 points | 5.2 | derived | 0.349 - 0.233 = 11.6 points. |
| Table 5 change column (12 cells, +119% to -25%) | section 7.2 | derived | the file prints the "without" capacity only; every percentage recomputes correctly on 15,623,209. |
| 153,025 | S1 | derived | 905,523 - 752,498. |

Not fails but worth recording: Wiedemann's 32% is printed in the source (p. 113, "rose 32% from 301 to 396 kg") but not in the literature register's `what_taken` for L239; 17.1 years and 5.83% are printed only in B124 (builder, no checker); 37% and 78% of draws are printed in `shocks_ranges_wide.csv` (B123, no checker).

## Checker-wording fails (draft against V36 to V42)

Rows naming B110 (V36), B111 (V37), B112 (V38) and B115 (V41) were compared with the checker's amended wording and value. Paper A rows do not cite B113, B114 or B116 as builder reports (the "B116", "B117" and "B120" in Paper A rows are claims-register ids). Places where the draft does not follow the checker:

1. **No checker for B123 (V44 absent).** Every row for the 19-choice shocked ranges says "checker pending V44": 8.1 sentences 7 and 8 (23.1 to 36.5; 0.84 to 1.32; 19.7 to 31.2; 0.72 to 1.13; "inside both"; 37%, 78%, 0.45%), the abstract sentence "the full Monte Carlo range at each contains the 2025 population", S9 "On the 19-choice range ..." and Table S9's 19-choice column. The checked values are V38's 13-choice ranges. One B123 value is wrong (0.72).
2. **V37 section 7 point 2 ("the consumption and red-meat-mix layers", not "diet").** Section 4 follows it and adds the caveat, but the abstract ("consumption and the red meat mix, a diet with less beef, add 5.6 million") and the conclusions ("the consumption and red-meat-mix layers, the diet with less beef, added 5.6 million") still call both layers the diet. Suggested: "the consumption and red-meat-mix layers, mostly a diet with less beef, add 5.6 million".
3. **V36 section 6 (state the base of the 10% test).** Section 2: "The thesis's own 2011 figures had no recorded source and differed from these by more than 10% in 23 zones." V36 asks for "by more than 10% of the ABS figure", and its 23 is "of the 52 regions other than North East Vic"; with North East Victoria (204,651 against 98,604) the count is 24. Suggested: "differed from them by more than 10% of the ABS figure in 24 zones, North East Victoria among them (section 3)".
4. **V38 proposed sentence 4 (name the grain-fed animals).** 8.1: "Applied to crops alone, with pasture-fed output at its average-year level, national short-term capacity is 41.2 million ...". V38 says the paper should say the grain-fed animals follow crops in this bound (41.2 includes them; plant rows alone give 41.3). Only the Table S10 caption says so. Suggested: "Applied to crops and grain-fed animals alone, with pasture-fed output at its average-year level, ...".
5. **V38 method point 1 (optional): the resilience table is held at the release's in the shocked draws.** Neither 8.1 nor S9 says so; B123's alternative (each draw's own table: 22.5 to 35.9 and 19.1 to 30.5 million) is in the drafter notes only. Suggested for S9: "Each draw takes the release's weather factor; with each draw's own table the ranges are 22.5 to 35.9 and 19.1 to 30.5 million, and 27.6 million lies inside both."
6. **V41 (energy range).** 9.1 calls the top of the energy range "a moderately active population" and S4 says "physical activity levels of 1.4 to 1.8 within a range of 1.2 to 2.2"; V41 notes it did not verify that the release diet corresponds to PAL 1.4. The paper reads as if the base were sedentary by source. Low weight; no number changes.

Followed correctly (no fail): V36 "about 82%" and "about 91%", shares "of the 53 regions' population", the 2011 tipping list of three; V37 "-7 people", "2.5 million when treated as one layer", the walk counts 7, 2, 3, 1; V38 "about 97%", "about 92% of draws" (S9), 21 to 22 regions at 1 in 10 with North Tasmania at balance, the three not-robust flips on the 13-choice ranges; V41 "18 of which vary", interactions "about 3%", 2011 "inside the 2025 range ... not a test of whether the change is real".

## Tier A rows pending gate 5 (for the gate digest)

| Register row | Pending value (checker) | Draft sentence(s) | Carries it? |
|---|---|---|---|
| A009 | 15.35 and 15.6 inside 13.3 to 18.8; 33.3 inside 31.1 to 49.2 (V41) | 7.1 "The 2011 figure lies inside the 2025 range across input choices, 13.3 to 18.8 million; 2011 was not sampled ..."; 9.1 "The 2011 capacities, 33.3 million in the short term and 15.35 million in the long term, lie inside the 2025 ranges, and 2011 was not sampled." | yes |
| A014 | 30.8 with 27.0 to 34.0 (13-choice), 29.2 to 32.5 herd-cycle (V38) | 8.1 "23.1 to 36.5 million at 1 in 10 (central 30.8 ...)"; 8.1 "in a 1-in-10 year (30.8 million)"; 12 "the worst of ten years leaves 30.8 million against 27.6 million"; Table 6; Table S9 | point value yes; headline range no (B123 19-choice range, unchecked); 27.0 to 34.0 appears only in Table S9 as an alternative |
| A027 | 31.1 to 49.2 (V41) | 9.1 "31.1 to 49.2 million people in the short term, a factor of 1.58"; Table S7 | yes |
| A028 | 13.3 to 18.8 (V41) | 7.1; 9.1 "13.3 to 18.8 million in the long term"; Table S7 | yes |
| A031 | 35 (V36) | 3 "In the long term, 35 and 32 regions were over capacity"; Table 1; 7.3; 9.2; Table S4 note | yes |
| A033 | 22 to 16; 35 to 32 (V36) | 3 "22 were over capacity ... in 2011 ... and 16 in 2025"; Table 1 | yes |
| A035 | 3 (V36) | Table 1 "3 (all over to under)"; 7.3 "Three regions changed long-term status" | yes |
| A038 | 2 on the herd-cycle ranges; 3 on the 13-choice ranges (V38, conditional) | 3 "Three are not robust to the 2025 range: Wet Tropics, Rangelands (Western Australia) and Corangamite"; 9.1 | carries 3 on the 13-choice ranges, which the register allows; the gate should note the paper does not adopt the herd-cycle ranges for flips |
| A039 | "One of the three long-term flips is clean and robust: South West Queensland" (V36) | 7.3 "One flip is clean and robust, South West Qld."; 9.1 "Of the three long-term flips, one passes every test"; 12 | yes |
| A165 | about 82% (81.55%) (V36) | Table 6 "about 82%"; 8.2 "about 82% of the population of the 53 regions" | yes |
| A183 | 1.12 with 0.98 to 1.23 or 1.06 to 1.18 (V38) | 8.1 "(central 30.8; 0.84 to 1.32 times the population)"; Table 6 1.12 | point yes; range no (B123 value) |
| A184 | 21 of 53; 21 to 22 across the range (V38) | 8.2 "to 21 at 1 in 10 in 2025"; S9 "21 regions over capacity at the central figure, 21 at the 95th-percentile capacity and 22 at the 5th" | yes |
| A187 | 0.95 with 0.83 to 1.05 or 0.90 to 1.01 (V38) | 8.1 "(central 26.3; 0.72 to 1.13 times)"; Table 6 0.95 | point yes; range no (B123 value, and 0.72 is wrong) |
| A196 | base values hold (1.12; 1.05 people over capacity); ranges as A183, A187; "below 27.6 million in about 92% of draws" on herd-cycle; basis named "a crop-yield weather allowance applied to all output" (V38) | 8.1 "people over capacity was 1.12 in 2011 and 1.05 in 2025"; "At the base settings the margin is above balance at 1 in 10 and below it at 1 in 20 in both data years, but across the spread of settings both outcomes lie inside the range"; abstract "On a cereal-yield weather allowance ..."; S9 "about 92% of draws are below it" | base values and basis yes; main-text range and draw share are the B123 19-choice values (78%), not the pending ones |
| A199 | 5 (2025); 3 (2011): Corangamite, North East Vic, Burnett Mary (V36) | 8.2 "In 2025 five regions ... In 2011 three were (Corangamite, North East Victoria and Burnett Mary)" | yes |
| A223 | register gate 5 note reads "new value -0.3; -26 unchanged in value (gate 4 value -0.2; -26)" | 6 "field-crop yields 24% lower took 0.2% off the short term, against 26% off at a 1-in-10 drought"; Table S2 -0.2% | carries -0.2 (the gate 4 value on 2025-fixed; `scenarios_by_region.csv` line 27 prints -0.2%); the register's gate 5 note prints -0.3 as the "new value" and needs correcting by the coordinator |

## Logic

1. **"The forward and reverse walks bound it" (section 4 and Table 2 caption).** False for three long-term rows (fail 2 above). Rewrite: "The forward and reverse walks are shown beside it; they bracket the average in the short term, but in the long term the average lies outside them for crop yields, liquid fuel and land with livestock."
2. **"The short-term rise holds ... in every single year of data from 2016-17 to 2024-25" (9.1).** The single years are on `2025-organic`, a different release, with 2021-22 missing, unverified (A317, X118), and S4 compares them with "the 2011 value of 40.5 million used there", not 33.3. Rewrite: "On the 2025-organic release, unverified, each of eight single years from 2016-17 to 2024-25 (no 2021-22) gives a capacity above that release's 2011 value (Supplementary Section S4)."
3. **"The corrected tier is lowest in both years" (9.2).** In 2011 only two tiers were run on the ABS populations (35 and 36); the published tier was not rerun. Rewrite: "The corrected tier has the fewest long-term regions over capacity in 2025, and in 2011 it has 35 against 36 on the improved tier (the published tier was not rerun on the 2011 ABS populations)."
4. **Abstract: "because in the model cropland can carry pasture-fed food but pasture cannot carry crops".** Section 6 says the cropland-share test "was run for Australia only, so the rule is not shown for regions". The cause is argued (S2's proportional-land test), not shown at SA2 level. Rewrite: "a loss the model's substitution rule accounts for: cropland can carry pasture-fed food but pasture cannot carry crops."
5. **8.4: "Bad wheat years are also partly correlated across the southern states (Anderson et al. 2019): ENSO and the Indian Ocean Dipole together explain 30 to 41% of wheat variability in Australia and East Africa."** The support is variance explained by climate modes, not a correlation across states. Rewrite: "Bad wheat years share climate drivers: ENSO and the Indian Ocean Dipole together explain 30 to 41% of wheat variability in Australia and East Africa (Anderson et al. 2019), so a widespread drought can hit several states at once."
6. **7.2: "Organic farming and the natural-fibre and wool-fibre shares lower it."** Table 5 shows activity level (+4% without it) and the biofuel share (+3%) lower it too. Rewrite: "Organic farming, the natural-fibre and wool-fibre shares, the activity level and the biofuel share lower it."
7. **Table S8 caption: "alone (first order) and with its interactions (total order)".** Several total-order shares are below the first-order ones (energy 27% and 25%; meat window 24% and 23%; land, long term, 58% and 56%), which the definitions do not allow. Add: "Differences of 1 to 2 points between the two orders are estimator noise."
8. **Abstract against body:** nothing in the abstract is absent from the body. Highlights match the body (highlight 2's "overlap" is section 4's shared grazing area; highlight 3 is 8.1; highlight 5 is 5.1 on state yields).

## Consistency

1. **S4: "Every single year is above the 2011 value of 40.5 million used there."** 2011 is 33.3 million everywhere else; 40.5 million is the 2011 figure of an earlier tier (`results/scale_curve.csv` 2011-corrected 40,450,144). Name it: "the 2011 value on that release's method, 40.5 million (33.3 million on the corrected method)".
2. **SA Arid Lands short-term capacity 2025:** 41 thousand in 5.2 (state-yield basis, A116) against 28,609 in Table 7 and S5 (own yields). 5.2 does not repeat its basis. Rewrite 5.2: "Its capacity on the state-yield basis was 41 thousand people (28,609 on its own yields, Table 7)".
3. **The same symbol for two ratios.** 8.1: "1.11 and 1.12 in a 1-in-10 year" (capacity over population) and, two sentences on, "people over capacity was 1.12 in 2011" (population over capacity, 1-in-20). Section 2 defines status as people over capacity; Table 6 and 8.1 use capacity over population.
4. **Table 6 prints 1.5 for 2025, average year; section 3 prints 1.50** (the file prints 1.5; give 1.50 in the table for a matching precision).
5. **Figure 2 placeholder** names `analysis/population_2011/movers-3.csv`, which does not exist; the file is `analysis/paper_a/movers-3.csv`. The other placeholders match the figure list in `SECTION_SCOPE.md` (Figures 1 to 8); Figures 1, 2, 3, 5 and 6 have no plotting script or image.
6. **Supplementary table numbers** are not in order of first citation: the main text cites S1 (section 2), S6 (5.4), S9 (8.1), S2 (8.3), S3 and S4 (9.2), S5 (11). Every table cited in prose exists and is the table meant (S2 scenarios, S3 method effects, S4 tier counts, S5 measures, S6 both yield bases, S9 shocked ranges).
7. **Store gain printed three ways:** 48.45% (8.3, Table S2), 48% (11.4), 48.4% (Table S5, from `measures.csv`). Consistent only because the unrounded value is between 48.44 and 48.45; a reader rounding 48.45 to one decimal expects 48.5. Use 48.4% in 8.3 and Table S2, or two decimals in Table S5.
8. **Table 2 is on `2011-fixed`, sections 3, 7 and 8 on `2011-fixed-3`.** Section 2 says the capacities are identical, so no number moves, but the caption should say so ("2011-fixed and 2011-fixed-3 give the same capacities").
9. **Citations against `references.md`:** "USDA undated" in sections 2 and S4 against the entry "USDA, 1992"; "CSIRO and University of Queensland 2025" (1.1) against "CSIRO, 2025"; "DCCEEW 2017, 2019, n.d." against entries under "Department of Climate Change, Energy, the Environment and Water"; "Roos et al. 2017" against "Röös". Higgins et al. 2018a is in the list and cited nowhere. Every other prose citation has an entry and every other entry is cited (58 entries).
10. **"as reported in"** appears in prose: section 11, "(Gifford et al. 1975, as reported in Henry and Godden 1995)". Rewrite: "(Gifford et al. 1975, cited in Henry and Godden 1995)" or cite Gifford alone if the source is read. "not seen" appears nowhere in prose.
11. **Reference form.** `references.md` is "Elsevier Harvard form" (decision 98) with abbreviated journal names and year after the authors without brackets; the brief and Population and Environment ask for Springer author-date ("Clapp, J. (2017). Food self-sufficiency ... Food Policy, 66, 88-96."). The list also carries 17 "[CHECK: ...]" markers and an HTML comment on every line. A decision for Murray (decision 98 against the journal).
12. Shocked ranges in 8.1 and Table S9 agree; Table 2 and section 4 prose agree; Table 4 and 7.1 agree; Table 3, Table S6 and 5.1 agree; Table 7 and section 10 and S5 agree.

## Journal checks

| Check | Count | Result |
|---|---|---|
| `python3 qa/tools/wordcount.py A` | TOTAL 7943 (1: 646, 2: 654, 3: 602, 4: 697, 5: 660, 6: 422, 7: 560, 8: 944, 9: 763, 10: 521, 11: 837, 12: 637) | pass (at most 7,950) |
| Abstract length | 246 words | pass (150 to 250) |
| Keywords | 6 (carrying capacity; food self-sufficiency; Australia; land use; regional planning; drought) | pass (journal asks for keywords; decision 97 allows up to 7) |
| Highlights | 5; 80, 85, 81, 71, 81 characters (counted by script) | pass; optional for this journal |
| Em dash in the four files | paper 0, supplement 0, highlights 0, references 1 (line 43, Hendrie et al. 2014 title, an em dash between "Diet" and "Comparing") | fail: replace with a colon as printed by most indexes, or a spaced hyphen |
| Time words | `supplementary.md` line 119, S4: "The recent droughts appear as the seasons ending 2007 ..." | fail: "The droughts of 2002-03, 2006-07 and 2019-20 appear as ..." |
| Decision 33 tone | no sentence judges an author's competence or honesty | pass |
| Draft furniture | `paper_A_draft1.md` opens with "First draft ... Not for circulation" and ends with the drafter notes appendix | strip at assembly |

## The reader's test: three places a referee would be lost

1. **Two ratios, both called a multiple.** Section 2 defines status as people over capacity (above 1 is over); 8.1, Table 6 and the abstract use capacity over population ("about 1.5 times"), and 8.1 then switches back ("as a status ratio, people over capacity was 1.12"). One sentence in section 2: "Two ratios appear: capacity over population, the margin (above 1 the region can feed itself), and its inverse, people over capacity, the status (above 1 the region is over capacity)."
2. **Release names as labels.** `2011-fixed-3`, `2025-fixed`, `2025-mirror`, `2025-improved`, `2025-organic`, `2025-store-1` appear without a key; a referee without the repository cannot tell what "mirror" or "-3" means. One sentence in section 2: "Each release is a frozen input set: 'fixed' is the corrected tier, 'mirror' the published method on 2025 data, 'improved' the improved tier, 'organic' and 'store' named variants, and '-3' the 2011 inputs with the ABS populations."
3. **The Monte Carlo choices and the companion paper.** Sections 2 and 9 speak of "19 sampled choices, of which 18 vary" and "the first 13 choices" and defer the method to "Section 6 of the companion methods paper"; S8 explains a 6.1% figure in "Paper B". The referee never learns what was varied. One sentence in section 9.1: "The choices are the input windows and calibrations (land source, herd and meat window, meat calibration, crop-trend window), the diet and loss settings (meat and egg share, red-meat share, avoidable waste, loss factors, energy requirement) and the long-term settings (resilience table, fuel, organic factors, feeding benchmark); Supplementary Section S4 lists their ranges." And in S8, drop "Paper B" for "a logarithmic reading of the same two anchors gives 16.4 years and 6.1%".

## Register rows touched

None. `qa/claims_register.csv` and every other register were read only.

## Trace table

Fails first (rows 1 to 32), then every other value in reading order. "Printed where" gives the line of the named file where the search found the value, or, for a rounded match, the raw value the claims cell quotes and where the file prints it. Rows with an empty "File" were checked by hand; the cell names the file.

| # | Number | Section | Claims row | File | Printed where | Result |
|---|---|---|---|---|---|---|
| 1 | 1.3 | s3 | A_s01-04_claims.csv:113 |  | not printed; regional_flips-3.csv zone 23 short 4,212,843 to 5,495,838 = +1,282,995 (arithmetic holds) | FAIL derived |
| 2 | 1.0 | s3 | A_s01-04_claims.csv:113 |  | not printed; regional_flips-3.csv populations: Hawkesbury-Nepean-Sydney +1,006,997, South East Qld +991,502 (holds) | FAIL derived |
| 3 | 1.0 | s3 | A_s01-04_claims.csv:113 |  | not printed; regional_flips-3.csv populations: Hawkesbury-Nepean-Sydney +1,006,997, South East Qld +991,502 (holds) | FAIL derived |
| 4 | 141 | s3 | A_s01-04_claims.csv:114 |  | not printed; regional_flips-3.csv zone 10 738,895 - 597,750 = 141,145 (holds) | FAIL derived |
| 5 | 65% | s4 | A_s01-04_claims.csv:164 |  | not printed; ratio of livestock_only to (all_2025 - capacity_2011) in capacity_by_cause_corrected.csv (row cell gives the arithmetic) | FAIL derived |
| 6 | 86% | s4 | A_s01-04_claims.csv:164 |  | not printed; same arithmetic | FAIL derived |
| 7 | 12 | s5 | A_s05-08_claims.csv:20 |  | not printed; scale_curve.csv 2025-fixed long state SA4 0.349 - NRM 0.233 = 11.6 points (holds) | FAIL derived |
| 8 | +119% | s7 | A_s05-08_claims.csv:97 |  | not printed; long_term_levers.csv prints the "without" value only; change on 15,623,209 recomputed and holds | FAIL derived |
| 9 | -76% | s7 | A_s05-08_claims.csv:99 |  | not printed; long_term_levers.csv prints the "without" value only; change on 15,623,209 recomputed and holds | FAIL derived |
| 10 | -17% | s7 | A_s05-08_claims.csv:101 |  | not printed; long_term_levers.csv prints the "without" value only; change on 15,623,209 recomputed and holds | FAIL derived |
| 11 | -1% | s7 | A_s05-08_claims.csv:103 |  | not printed; long_term_levers.csv prints the "without" value only; change on 15,623,209 recomputed and holds | FAIL derived |
| 12 | +22% | s7 | A_s05-08_claims.csv:105 |  | not printed; long_term_levers.csv prints the "without" value only; change on 15,623,209 recomputed and holds | FAIL derived |
| 13 | +4% | s7 | A_s05-08_claims.csv:106 |  | not printed; long_term_levers.csv prints the "without" value only; change on 15,623,209 recomputed and holds | FAIL derived |
| 14 | +3% | s7 | A_s05-08_claims.csv:107 |  | not printed; long_term_levers.csv prints the "without" value only; change on 15,623,209 recomputed and holds | FAIL derived |
| 15 | -29% | s7 | A_s05-08_claims.csv:108 |  | not printed; long_term_levers.csv prints the "without" value only; change on 15,623,209 recomputed and holds | FAIL derived |
| 16 | +26% | s7 | A_s05-08_claims.csv:109 |  | not printed; long_term_levers.csv prints the "without" value only; change on 15,623,209 recomputed and holds | FAIL derived |
| 17 | +46% | s7 | A_s05-08_claims.csv:110 |  | not printed; long_term_levers.csv prints the "without" value only; change on 15,623,209 recomputed and holds | FAIL derived |
| 18 | -6% | s7 | A_s05-08_claims.csv:111 |  | not printed; long_term_levers.csv prints the "without" value only; change on 15,623,209 recomputed and holds | FAIL derived |
| 19 | -25% | s7 | A_s05-08_claims.csv:112 |  | not printed; long_term_levers.csv prints the "without" value only; change on 15,623,209 recomputed and holds | FAIL derived |
| 20 | 0.72 | s8 | A_s05-08_claims.csv:121 |  | shocks_ranges_wide.csv line 18 prints 0.715 (rounded); 19,735,337 / 27,608,200 = 0.7148, which prints 0.71, not 0.72 (double rounding) | FAIL value |
| 21 | 153 | s8 | none |  | no section 8 row for 153 (rows exist for section 2 and S4: B112 s3, V38) | FAIL no row |
| 22 | 153,025 | Supp S1 | supplementary_claims.csv:22 |  | not printed; capacity_by_cause_corrected.csv zone 9 short 905,523 - 752,498 = 153,025 (holds) | FAIL derived |
| 23 | 0.72 | Supp S4 | supplementary_claims.csv:176 |  | as above: exact 0.7148 prints 0.71 | FAIL value |
| 24 | 41.5 | Highlights | none |  | no claims row for highlights in any claims csv (abstract rows A001, A003, A011, A015/A088 carry the same values; B104 lists them) | FAIL no row |
| 25 | 33.3 | Highlights | none |  | no claims row for highlights in any claims csv (abstract rows A001, A003, A011, A015/A088 carry the same values; B104 lists them) | FAIL no row |
| 26 | 1 | Highlights | none |  | no claims row for highlights in any claims csv (abstract rows A001, A003, A011, A015/A088 carry the same values; B104 lists them) | FAIL no row |
| 27 | 10 | Highlights | none |  | no claims row for highlights in any claims csv (abstract rows A001, A003, A011, A015/A088 carry the same values; B104 lists them) | FAIL no row |
| 28 | 1 | Highlights | none |  | no claims row for highlights in any claims csv (abstract rows A001, A003, A011, A015/A088 carry the same values; B104 lists them) | FAIL no row |
| 29 | 20 | Highlights | none |  | no claims row for highlights in any claims csv (abstract rows A001, A003, A011, A015/A088 carry the same values; B104 lists them) | FAIL no row |
| 30 | 100 | Highlights | none |  | no claims row for highlights in any claims csv (abstract rows A001, A003, A011, A015/A088 carry the same values; B104 lists them) | FAIL no row |
| 31 | 57% | Highlights | none |  | no claims row for highlights in any claims csv (abstract rows A001, A003, A011, A015/A088 carry the same values; B104 lists them) | FAIL no row |
| 32 | 37% | Highlights | none |  | no claims row for highlights in any claims csv (abstract rows A001, A003, A011, A015/A088 carry the same values; B104 lists them) | FAIL no row |
| 33 | 53 | Abstract | A_s01-04_claims.csv:4 | analysis/comparison_2025/movers.csv | literal line 8 | pass |
| 34 | 52 | Abstract | A_s01-04_claims.csv:4 | analysis/comparison_2025/movers.csv | literal line 35 | pass |
| 35 | 2,450 | Abstract | A_s01-04_claims.csv:5 | results/scale_curve.csv | literal line 8 | pass |
| 36 | 33.3 | Abstract | A_s01-04_claims.csv:6 | results/comparison_cells.csv | cell value 33.3 in REG:A001; rounded 33307814 x1e-06 line 2 | pass |
| 37 | 41.5 | Abstract | A_s01-04_claims.csv:6 | results/comparison_cells.csv | cell value 41.5 in REG:A003; rounded 41503537 x1e-06 line 2 | pass |
| 38 | 22.3 | Abstract | A_s01-04_claims.csv:7 | results/comparison_cells.csv | cell value 22.3 in REG:A002; rounded 22326388 x1e-06 line 2 | pass |
| 39 | 27.6 | Abstract | A_s01-04_claims.csv:7 | results/comparison_cells.csv | cell value 27.6 in REG:A004; rounded 27608200 x1e-06 line 2 | pass |
| 40 | 1.5 | Abstract | A_s01-04_claims.csv:6 |  | analysis/paper_a/shocks_summary-3.csv lines 2 and 8 (1.49, 1.5); results/2025-fixed.csv capacity_per_person 1.5033 | pass |
| 41 | 5.6 | Abstract | A_s01-04_claims.csv:11 | results/ranges_2025-mirror.csv | cell value +5,594,663 in qa/reports/V37_check_B111.md; rounded 0.056 x100 line 121 | pass |
| 42 | 2.4 | Abstract | A_s01-04_claims.csv:12 | results/ranges_2025-mirror.csv | cell value +2,438,688 in qa/reports/B111_decomposition_orders.md; rounded 2409157 x1e-06 line 5 | pass |
| 43 | 1 | Abstract | A_s01-04_claims.csv:2 |  | structural return period (shocks_summary-3.csv return period column) | pass |
| 44 | 10 | Abstract | A_s01-04_claims.csv:15 |  | structural return period (shocks_summary-3.csv return period column) | pass |
| 45 | 1 | Abstract | A_s01-04_claims.csv:2 |  | structural return period (shocks_summary-3.csv return period column) | pass |
| 46 | 20 | Abstract | A_s01-04_claims.csv:2 |  | structural return period (shocks_summary-3.csv return period column) | pass |
| 47 | 100 | Abstract | A_s01-04_claims.csv:17 | analysis/paper_a/long_term_regions.csv | cell value 100 in REG:A011; rounded 1 x100 line 2 | pass |
| 48 | 57% | Abstract | A_s01-04_claims.csv:17 | analysis/paper_a/long_term_regions.csv | literal line 52 | pass |
| 49 | 37% | Abstract | A_s01-04_claims.csv:18 | results/scale_curve.csv | literal line 165 | pass |
| 50 | 26.5 | s1 | A_s01-04_claims.csv:24 | LIT:L226 | literal line 1 | pass |
| 51 | 40.5 | s1 | A_s01-04_claims.csv:24 | LIT:L226 | literal line 1 | pass |
| 52 | 27.5 | s1 | A_s01-04_claims.csv:25 | LIT:L228 | literal line 1 | pass |
| 53 | 41 | s1 | A_s01-04_claims.csv:26 | LIT:L228 | literal line 1 | pass |
| 54 | 5 | s1 | A_s01-04_claims.csv:28 | LIT:L144 | literal line 1 | pass |
| 55 | 24% | s1 | A_s01-04_claims.csv:30 | results/comparison_cells.csv | literal line 48 | pass |
| 56 | 100 | s1 | A_s01-04_claims.csv:36 | analysis/paper_a/regional_flips.csv | cell value 100 in analysis/paper_a/regional_flips.csv; rounded 1 x100 line 11 | pass |
| 57 | 7 | s1 | A_s01-04_claims.csv:36 | analysis/paper_a/regional_flips.csv | literal line 3 | pass |
| 58 | 8 | s1 | none |  | structural (section number; supplementary_claims.csv "all" row on numbering) | pass |
| 59 | 9 | s1 | A_s01-04_claims.csv:36 | analysis/paper_a/regional_flips.csv | literal line 12 | pass |
| 60 | 5 | s1 | A_s01-04_claims.csv:36 | analysis/paper_a/regional_flips.csv | literal line 66 | pass |
| 61 | 6 | s1 | A_s01-04_claims.csv:35 | papers/A_results/OUTLINE.md | literal line 39 | pass |
| 62 | 102 | s1 | A_s01-04_claims.csv:38 | LIT:L148 | literal line 1 | pass |
| 63 | 964 | s1 | none |  | page range (literature register L148, p. 963) | pass |
| 64 | 25 | s1 | A_s01-04_claims.csv:40 | LIT:L150 | literal line 1 | pass |
| 65 | 21 | s1 | A_s01-04_claims.csv:41 | LIT:L150 | literal line 1 | pass |
| 66 | 27% | s1 | A_s01-04_claims.csv:44 | LIT:L153 | literal line 1 | pass |
| 67 | 71% | s1 | A_s01-04_claims.csv:47 | LIT:L234 | literal line 1 | pass |
| 68 | 1 | s2 | A_s01-04_claims.csv:51 | results/README.md | literal line 6 | pass |
| 69 | 100 | s2 | A_s01-04_claims.csv:53 | analysis/paper_a/long_term_regions.csv | cell value 100 in REG:A010; rounded 1 x100 line 2 | pass |
| 70 | 60 | s2 | A_s01-04_claims.csv:55 | claims register A331 | literal line 1 | pass |
| 71 | 52 | s2 | A_s01-04_claims.csv:56 | analysis/comparison_2025/README.md | literal line 80 | pass |
| 72 | 53 | s2 | A_s01-04_claims.csv:57 | analysis/comparison_2025/movers.csv | literal line 8 | pass |
| 73 | 52 | s2 | A_s01-04_claims.csv:56 | analysis/comparison_2025/README.md | literal line 80 | pass |
| 74 | 30 | s2 | A_s01-04_claims.csv:59 | results/ranges_2025-mirror.csv | literal line 60 | pass |
| 75 | 10% | s2 | A_s01-04_claims.csv:62 | ERRATA.md | literal line 22 | pass |
| 76 | 23 | s2 | A_s01-04_claims.csv:62 | ERRATA.md | literal line 14 | pass |
| 77 | 22,326,388 | s2 | A_s01-04_claims.csv:63 | ERRATA.md | literal line 20 | pass |
| 78 | 53 | s2 | A_s01-04_claims.csv:64 | results/ranges_2025-mirror.csv | literal line 106 | pass |
| 79 | 22,336,514 | s2 | A_s01-04_claims.csv:64 | qa/reports/B110_zone_populations_2011.md | literal line 7 | pass |
| 80 | 10,126 | s2 | A_s01-04_claims.csv:65 | qa/reports/B110_zone_populations_2011.md | literal line 25 | pass |
| 81 | 1 | s2 | A_s01-04_claims.csv:71 | ERRATA.md | literal line 3 | pass |
| 82 | 53 | s2 | A_s01-04_claims.csv:73 | results/ranges_2025-mirror.csv | literal line 106 | pass |
| 83 | 153 | s2 | A_s01-04_claims.csv:76 | results/ranges_2025-fixed.csv | cell value 153 in results/ranges_2025-fixed.csv; rounded 153454 x0.001 line 104 | pass |
| 84 | 1861 | s2 | A_s01-04_claims.csv:76 | qa/reports/B112_shock_ranges.md | literal line 84 | pass |
| 85 | 1 | s2 | A_s01-04_claims.csv:76 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 86 | 10 | s2 | A_s01-04_claims.csv:80 | results/ranges_2025-fixed.csv | literal line 20 | pass |
| 87 | 1 | s2 | A_s01-04_claims.csv:76 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 88 | 20 | s2 | A_s01-04_claims.csv:76 | results/ranges_2025-fixed.csv | literal line 40 | pass |
| 89 | 0.742 | s2 | A_s01-04_claims.csv:78 | results/ranges_2025-fixed.csv | literal line 42 | pass |
| 90 | 0.634 | s2 | A_s01-04_claims.csv:78 | qa/reports/B112_shock_ranges.md | literal line 33 | pass |
| 91 | 0.599 | s2 | A_s01-04_claims.csv:79 | results/ranges_2025-fixed.csv | cell value 0.599 in qa/reports/B112_shock_ranges.md; rounded 598600 x1e-06 line 107 | pass |
| 92 | 20 | s2 | A_s01-04_claims.csv:76 | results/ranges_2025-fixed.csv | literal line 40 | pass |
| 93 | 19 | s2 | A_s01-04_claims.csv:81 | results/ranges_2025-improved.csv | literal line 38 | pass |
| 94 | 18 | s2 | A_s01-04_claims.csv:81 | results/ranges_2025-improved.csv | literal line 36 | pass |
| 95 | 1 | s2 | A_s01-04_claims.csv:85 | results/releases.json | literal line 12 | pass |
| 96 | 33.3 | s3 | A_s01-04_claims.csv:87 | results/comparison_cells.csv | cell value 33.3 in REG:A001; rounded 33307814 x1e-06 line 2 | pass |
| 97 | 22.3 | s3 | A_s01-04_claims.csv:89 | results/comparison_cells.csv | cell value 22.3 in REG:A002; rounded 22326388 x1e-06 line 2 | pass |
| 98 | 41.5 | s3 | A_s01-04_claims.csv:90 | results/comparison_cells.csv | cell value 41.5 in REG:A003; rounded 41503537 x1e-06 line 2 | pass |
| 99 | 27.6 | s3 | A_s01-04_claims.csv:90 | results/comparison_cells.csv | cell value 27.6 in REG:A004; rounded 27608200 x1e-06 line 2 | pass |
| 100 | 1.5 | s3 | A_s01-04_claims.csv:90 |  | as above | pass |
| 101 | 1.49 | s3 | A_s01-04_claims.csv:92 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 102 | 1.50 | s3 | A_s01-04_claims.csv:92 | results/comparison_cells.csv | cell value 1.50 in REG:A006; rounded 1502318 x1e-06 line 30 | pass |
| 103 | 24.6% | s3 | A_s01-04_claims.csv:93 | results/comparison_cells.csv | cell value 24.6 in REG:A328; rounded 24570 x0.001 line 21 | pass |
| 104 | 23.7% | s3 | A_s01-04_claims.csv:93 | results/comparison_cells.csv | cell value 23.7 in REG:A328; rounded 23711 x0.001 line 26 | pass |
| 105 | 53 | s3 | A_s01-04_claims.csv:94 | analysis/comparison_2025/movers.csv | literal line 8 | pass |
| 106 | 52 | s3 | A_s01-04_claims.csv:94 | analysis/comparison_2025/movers.csv | literal line 35 | pass |
| 107 | 22 | s3 | A_s01-04_claims.csv:94 | analysis/comparison_2025/movers.csv | literal line 13 | pass |
| 108 | 16 | s3 | A_s01-04_claims.csv:95 | analysis/paper_a/regional_flips.csv | literal line 49 | pass |
| 109 | 35 | s3 | A_s01-04_claims.csv:96 | analysis/paper_a/regional_flips.csv | literal line 14 | pass |
| 110 | 32 | s3 | A_s01-04_claims.csv:96 | analysis/paper_a/regional_flips.csv | literal line 26 | pass |
| 111 | 2 | s3 | A_s01-04_claims.csv:101 | analysis/comparison_2025/movers.csv | literal line 2 | pass |
| 112 | 0.5 | s3 | A_s01-04_claims.csv:101 | analysis/comparison_2025/movers.csv | literal line 52 | pass |
| 113 | 5 | s3 | A_s01-04_claims.csv:101 | analysis/comparison_2025/movers.csv | literal line 10 | pass |
| 114 | 95 | s3 | A_s01-04_claims.csv:102 |  | structural (percentile label) | pass |
| 115 | 53 | s3 | A_s01-04_claims.csv:94 | analysis/comparison_2025/movers.csv | literal line 8 | pass |
| 116 | 52 | s3 | A_s01-04_claims.csv:94 | analysis/comparison_2025/movers.csv | literal line 35 | pass |
| 117 | 22 | s3 | A_s01-04_claims.csv:122 | analysis/paper_a/regional_flips-3.csv | literal line 59 | pass |
| 118 | 16 | s3 | A_s01-04_claims.csv:123 | analysis/paper_a/regional_flips.csv | literal line 49 | pass |
| 119 | 8 | s3 | A_s01-04_claims.csv:124 | analysis/paper_a/regional_flips.csv | literal line 45 | pass |
| 120 | 7 | s3 | A_s01-04_claims.csv:124 | analysis/paper_a/regional_flips.csv | literal line 3 | pass |
| 121 | 1 | s3 | A_s01-04_claims.csv:122 | analysis/paper_a/regional_flips-3.csv | literal line 11 | pass |
| 122 | 3 | s3 | A_s01-04_claims.csv:122 | analysis/paper_a/regional_flips-3.csv | literal line 5 | pass |
| 123 | 3 | s3 | A_s01-04_claims.csv:122 | analysis/paper_a/regional_flips-3.csv | literal line 5 | pass |
| 124 | 2 | s3 | A_s01-04_claims.csv:122 | analysis/paper_a/regional_flips-3.csv | literal line 2 | pass |
| 125 | 35 | s3 | A_s01-04_claims.csv:128 | analysis/paper_a/regional_flips-3.csv | literal line 14 | pass |
| 126 | 32 | s3 | A_s01-04_claims.csv:129 | analysis/paper_a/regional_flips.csv | literal line 26 | pass |
| 127 | 3 | s3 | A_s01-04_claims.csv:128 | analysis/paper_a/regional_flips-3.csv | literal line 5 | pass |
| 128 | 2 | s3 | A_s01-04_claims.csv:129 | analysis/paper_a/regional_flips.csv | literal line 2 | pass |
| 129 | 1 | s3 | A_s01-04_claims.csv:128 | analysis/paper_a/regional_flips-3.csv | literal line 11 | pass |
| 130 | 1 | s3 | A_s01-04_claims.csv:128 | analysis/paper_a/regional_flips-3.csv | literal line 11 | pass |
| 131 | 143,631 | s3 | A_s01-04_claims.csv:107 | analysis/paper_a/regional_flips-3.csv | literal line 40 | pass |
| 132 | 139,165 | s3 | A_s01-04_claims.csv:107 | analysis/paper_a/regional_flips-3.csv | literal line 40 | pass |
| 133 | 204,651 | s3 | A_s01-04_claims.csv:109 | ERRATA.md | literal line 20 | pass |
| 134 | 98,604 | s3 | A_s01-04_claims.csv:110 | ERRATA.md | literal line 20 | pass |
| 135 | 464 | s3 | A_s01-04_claims.csv:112 | analysis/comparison_2025/movers.csv | cell value 464 in analysis/comparison_2025/movers.csv; rounded 464456 x0.001 line 2 | pass |
| 136 | 456 | s3 | A_s01-04_claims.csv:112 | analysis/comparison_2025/movers.csv | cell value 456 in analysis/comparison_2025/movers.csv; rounded 456182 x0.001 line 3 | pass |
| 137 | 441 | s3 | A_s01-04_claims.csv:112 | analysis/comparison_2025/movers.csv | cell value 441 in analysis/comparison_2025/movers.csv; rounded 441053 x0.001 line 4 | pass |
| 138 | 348 | s3 | A_s01-04_claims.csv:114 | analysis/comparison_2025/movers.csv | cell value +348,336 in analysis/comparison_2025/movers.csv; rounded 348336 x0.001 line 7 | pass |
| 139 | 0.01 | s3 | A_s01-04_claims.csv:117 | analysis/comparison_2025/movers.csv | literal line 11 | pass |
| 140 | 362,880 | s4 | A_s01-04_claims.csv:137 | qa/reports/B111_decomposition_orders.md | literal line 24 | pass |
| 141 | 0.670 | s4 | A_s01-04_claims.csv:141 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 142 | 1.454 | s4 | A_s01-04_claims.csv:141 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 143 | 0.665 | s4 | A_s01-04_claims.csv:142 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 144 | 1.767 | s4 | A_s01-04_claims.csv:142 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 145 | 0 | s4 | A_s01-04_claims.csv:141 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 146 | 362,880 | s4 | A_s01-04_claims.csv:137 | qa/reports/B111_decomposition_orders.md | literal line 24 | pass |
| 147 | 1 | s4 | A_s01-04_claims.csv:168 | analysis/comparison_2025/capacity_by_cause_corrected_orders.csv | literal line 2 | pass |
| 148 | 3 | s4 | A_s01-04_claims.csv:168 | analysis/comparison_2025/capacity_by_cause_corrected_orders.csv | literal line 68 | pass |
| 149 | 33,307,814 | s4 | A_s01-04_claims.csv:169 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 150 | 33,307,814 | s4 | A_s01-04_claims.csv:169 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 151 | 33,307,814 | s4 | A_s01-04_claims.csv:169 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 152 | 15,350,146 | s4 | A_s01-04_claims.csv:169 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 153 | 15,350,146 | s4 | A_s01-04_claims.csv:169 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 154 | 15,350,146 | s4 | A_s01-04_claims.csv:169 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 155 | -3,064,101 | s4 | A_s01-04_claims.csv:170 | qa/reports/B111_decomposition_orders.md | literal line 43 | pass |
| 156 | -2,621,910 | s4 | A_s01-04_claims.csv:170 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 157 | -3,546,205 | s4 | A_s01-04_claims.csv:170 | qa/reports/B111_decomposition_orders.md | literal line 43 | pass |
| 158 | -1,248,192 | s4 | A_s01-04_claims.csv:170 | qa/reports/B111_decomposition_orders.md | literal line 57 | pass |
| 159 | -1,208,326 | s4 | A_s01-04_claims.csv:170 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 160 | -1,334,901 | s4 | A_s01-04_claims.csv:170 | qa/reports/B111_decomposition_orders.md | literal line 57 | pass |
| 161 | 0 | s4 | A_s01-04_claims.csv:171 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 162 | 0 | s4 | A_s01-04_claims.csv:171 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 163 | 0 | s4 | A_s01-04_claims.csv:171 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 164 | 0 | s4 | A_s01-04_claims.csv:171 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 165 | 0 | s4 | A_s01-04_claims.csv:171 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 166 | 0 | s4 | A_s01-04_claims.csv:171 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 167 | +162,372 | s4 | A_s01-04_claims.csv:172 | qa/reports/B111_decomposition_orders.md | literal line 45 | pass |
| 168 | +115,575 | s4 | A_s01-04_claims.csv:172 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 169 | +220,269 | s4 | A_s01-04_claims.csv:172 | qa/reports/B111_decomposition_orders.md | literal line 45 | pass |
| 170 | +257,755 | s4 | A_s01-04_claims.csv:172 | qa/reports/B111_decomposition_orders.md | literal line 59 | pass |
| 171 | +219,940 | s4 | A_s01-04_claims.csv:172 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 172 | +253,434 | s4 | A_s01-04_claims.csv:172 | qa/reports/B111_decomposition_orders.md | literal line 59 | pass |
| 173 | +5,502,789 | s4 | A_s01-04_claims.csv:173 | qa/reports/B111_decomposition_orders.md | literal line 46 | pass |
| 174 | +4,703,257 | s4 | A_s01-04_claims.csv:173 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 175 | +6,374,770 | s4 | A_s01-04_claims.csv:173 | qa/reports/B111_decomposition_orders.md | literal line 46 | pass |
| 176 | +628,764 | s4 | A_s01-04_claims.csv:173 | qa/reports/B111_decomposition_orders.md | literal line 60 | pass |
| 177 | +599,578 | s4 | A_s01-04_claims.csv:173 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 178 | +743,648 | s4 | A_s01-04_claims.csv:173 | qa/reports/B111_decomposition_orders.md | literal line 60 | pass |
| 179 | +4,156,557 | s4 | A_s01-04_claims.csv:174 | qa/reports/B111_decomposition_orders.md | literal line 47 | pass |
| 180 | +4,183,947 | s4 | A_s01-04_claims.csv:174 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 181 | +4,090,572 | s4 | A_s01-04_claims.csv:174 | qa/reports/B111_decomposition_orders.md | literal line 47 | pass |
| 182 | 0 | s4 | A_s01-04_claims.csv:174 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 183 | 0 | s4 | A_s01-04_claims.csv:174 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 184 | 0 | s4 | A_s01-04_claims.csv:174 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 185 | 0 | s4 | A_s01-04_claims.csv:175 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 186 | 0 | s4 | A_s01-04_claims.csv:175 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 187 | 0 | s4 | A_s01-04_claims.csv:175 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 188 | +173,183 | s4 | A_s01-04_claims.csv:175 | qa/reports/B111_decomposition_orders.md | literal line 62 | pass |
| 189 | +172,682 | s4 | A_s01-04_claims.csv:175 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 190 | +180,979 | s4 | A_s01-04_claims.csv:175 | qa/reports/B111_decomposition_orders.md | literal line 62 | pass |
| 191 | 0 | s4 | A_s01-04_claims.csv:176 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 192 | 0 | s4 | A_s01-04_claims.csv:176 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 193 | 0 | s4 | A_s01-04_claims.csv:176 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 194 | -7 | s4 | A_s01-04_claims.csv:176 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 195 | -7 | s4 | A_s01-04_claims.csv:176 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 196 | -7 | s4 | A_s01-04_claims.csv:176 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 197 | 0 | s4 | A_s01-04_claims.csv:177 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 198 | 0 | s4 | A_s01-04_claims.csv:177 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 199 | 0 | s4 | A_s01-04_claims.csv:177 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 200 | +124,764 | s4 | A_s01-04_claims.csv:177 | qa/reports/B111_decomposition_orders.md | literal line 64 | pass |
| 201 | +90,858 | s4 | A_s01-04_claims.csv:177 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 202 | +114,983 | s4 | A_s01-04_claims.csv:177 | qa/reports/B111_decomposition_orders.md | literal line 64 | pass |
| 203 | +1,438,106 | s4 | A_s01-04_claims.csv:178 | qa/reports/B111_decomposition_orders.md | literal line 49 | pass |
| 204 | +1,814,854 | s4 | A_s01-04_claims.csv:178 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 205 | +1,056,317 | s4 | A_s01-04_claims.csv:178 | qa/reports/B111_decomposition_orders.md | literal line 49 | pass |
| 206 | +336,796 | s4 | A_s01-04_claims.csv:178 | qa/reports/B111_decomposition_orders.md | literal line 65 | pass |
| 207 | +398,338 | s4 | A_s01-04_claims.csv:178 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 208 | +314,927 | s4 | A_s01-04_claims.csv:178 | qa/reports/B111_decomposition_orders.md | literal line 65 | pass |
| 209 | 41,503,537 | s4 | A_s01-04_claims.csv:179 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 210 | 41,503,537 | s4 | A_s01-04_claims.csv:179 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 211 | 41,503,537 | s4 | A_s01-04_claims.csv:179 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 212 | 15,623,209 | s4 | A_s01-04_claims.csv:179 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 213 | 15,623,209 | s4 | A_s01-04_claims.csv:179 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 214 | 15,623,209 | s4 | A_s01-04_claims.csv:179 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 215 | +2,438,688 | s4 | A_s01-04_claims.csv:180 | qa/reports/B111_decomposition_orders.md | literal line 50 | pass |
| 216 | +2,081,347 | s4 | A_s01-04_claims.csv:180 | qa/reports/B111_decomposition_orders.md | literal line 50 | pass |
| 217 | +2,828,565 | s4 | A_s01-04_claims.csv:180 | qa/reports/B111_decomposition_orders.md | literal line 50 | pass |
| 218 | -619,428 | s4 | A_s01-04_claims.csv:180 | qa/reports/B111_decomposition_orders.md | literal line 66 | pass |
| 219 | -608,748 | s4 | A_s01-04_claims.csv:180 | qa/reports/B111_decomposition_orders.md | literal line 66 | pass |
| 220 | -591,253 | s4 | A_s01-04_claims.csv:180 | qa/reports/B111_decomposition_orders.md | literal line 66 | pass |
| 221 | 0.670 | s4 | A_s01-04_claims.csv:181 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 222 | 1.454 | s4 | A_s01-04_claims.csv:181 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 223 | 0.665 | s4 | A_s01-04_claims.csv:182 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 224 | 1.767 | s4 | A_s01-04_claims.csv:182 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 225 | 8.2 | s4 | A_s01-04_claims.csv:144 | results/comparison_cells.csv | cell value +8,195,723 in results/comparison_cells.csv; rounded 8195723 x1e-06 line 2 | pass |
| 226 | 5.5 | s4 | A_s01-04_claims.csv:145 | results/ranges_2025-mirror.csv | cell value +5.50 in qa/reports/B111_decomposition_orders.md; rounded 0.055 x100 line 11 | pass |
| 227 | 67% | s4 | A_s01-04_claims.csv:145 | results/ranges_2025-mirror.csv | cell value 67.1 in qa/reports/V37_check_B111.md; rounded 0.666 x100 line 32 | pass |
| 228 | 4.2 | s4 | A_s01-04_claims.csv:146 | results/ranges_2025-mirror.csv | cell value +4,156,557 in qa/reports/B111_decomposition_orders.md; rounded 0.042 x100 line 23 | pass |
| 229 | 1.4 | s4 | A_s01-04_claims.csv:146 | results/ranges_2025-mirror.csv | cell value +1,438,106 in qa/reports/B111_decomposition_orders.md; rounded 0.014 x100 line 4 | pass |
| 230 | 3.1 | s4 | A_s01-04_claims.csv:147 | results/ranges_2025-mirror.csv | cell value -3,064,101 in qa/reports/B111_decomposition_orders.md; rounded 0.031 x100 line 7 | pass |
| 231 | 0.2 | s4 | A_s01-04_claims.csv:147 | results/ranges_2025-mirror.csv | cell value +162,372 in qa/reports/B111_decomposition_orders.md; rounded 25 x0.01 line 1 | pass |
| 232 | 5.6 | s4 | A_s01-04_claims.csv:148 | results/ranges_2025-mirror.csv | cell value 5.59 in qa/reports/B111_decomposition_orders.md; rounded 0.056 x100 line 121 | pass |
| 233 | 68% | s4 | A_s01-04_claims.csv:148 | results/ranges_2025-mirror.csv | cell value 68.3 in qa/reports/V37_check_B111.md; rounded 0.683 x100 line 51 | pass |
| 234 | 0.64 | s4 | A_s01-04_claims.csv:149 | results/2011-fixed-3.csv | literal line 2 | pass |
| 235 | 0.578 | s4 | A_s01-04_claims.csv:149 | results/2025-fixed.csv | literal line 2 | pass |
| 236 | 39.1 | s4 | A_s01-04_claims.csv:150 | analysis/consumption_2025/README.md | literal line 19 | pass |
| 237 | 25.9 | s4 | A_s01-04_claims.csv:150 | analysis/consumption_2025/README.md | literal line 19 | pass |
| 238 | 4.7 | s4 | A_s01-04_claims.csv:152 | results/ranges_2025-mirror.csv | cell value +4,703,257 in qa/reports/B111_decomposition_orders.md; rounded 0.047 x100 line 3 | pass |
| 239 | 6.4 | s4 | A_s01-04_claims.csv:152 | results/ranges_2025-mirror.csv | cell value +6,374,770 in qa/reports/B111_decomposition_orders.md; rounded 0.064 x100 line 15 | pass |
| 240 | 1.8 | s4 | A_s01-04_claims.csv:152 | results/ranges_2025-mirror.csv | cell value +1,814,854 in qa/reports/B111_decomposition_orders.md; rounded 1788893 x1e-06 line 6 | pass |
| 241 | 1.1 | s4 | A_s01-04_claims.csv:152 | results/ranges_2025-mirror.csv | cell value +1,056,317 in qa/reports/B111_decomposition_orders.md; rounded 1053016 x1e-06 line 18 | pass |
| 242 | 2.4 | s4 | A_s01-04_claims.csv:154 | results/ranges_2025-mirror.csv | cell value +2,438,688 in qa/reports/B111_decomposition_orders.md; rounded 2409157 x1e-06 line 5 | pass |
| 243 | 30% | s4 | A_s01-04_claims.csv:154 | results/ranges_2025-mirror.csv | literal line 60 | pass |
| 244 | 2.5 | s4 | A_s01-04_claims.csv:154 | results/ranges_2025-mirror.csv | cell value +2,456,649 in qa/reports/B111_decomposition_orders.md; rounded 2455752 x1e-06 line 5 | pass |
| 245 | 3.8 | s4 | A_s01-04_claims.csv:155 | analysis/comparison_2025/capacity_by_cause_corrected.csv | cell value +3,802,283 in REG:A358; rounded 3800 x0.001 line 34 | pass |
| 246 | 0.4 | s4 | A_s01-04_claims.csv:155 | analysis/comparison_2025/capacity_by_cause_corrected.csv | cell value 358 in analysis/comparison_2025/capacity_by_cause_corrected.csv; rounded 398338 x1e-06 line 3 | pass |
| 247 | 0.27 | s4 | A_s01-04_claims.csv:157 | results/comparison_cells.csv | cell value +273,063 in results/comparison_cells.csv; rounded 273063 x1e-06 line 3 | pass |
| 248 | -1.25 | s4 | A_s01-04_claims.csv:158 | analysis/comparison_2025/capacity_by_cause_corrected.csv | cell value -1,248,192 in qa/reports/B111_decomposition_orders.md; rounded -1246 x0.001 line 73 | pass |
| 249 | -0.62 | s4 | A_s01-04_claims.csv:159 | results/ranges_2025-mirror.csv | literal line 89 | pass |
| 250 | 0.63 | s4 | A_s01-04_claims.csv:160 | results/ranges_2025-mirror.csv | cell value +628,764 in qa/reports/B111_decomposition_orders.md; rounded 634033 x1e-06 line 56 | pass |
| 251 | 0.34 | s4 | A_s01-04_claims.csv:160 | results/ranges_2025-mirror.csv | literal line 55 | pass |
| 252 | 0.26 | s4 | A_s01-04_claims.csv:160 | results/ranges_2025-mirror.csv | cell value +257,755 in qa/reports/B111_decomposition_orders.md; rounded 0.255 x1 line 10 | pass |
| 253 | 0.17 | s4 | A_s01-04_claims.csv:160 | results/ranges_2025-mirror.csv | cell value +173,183 in qa/reports/B111_decomposition_orders.md; rounded 0.171 x1 line 7 | pass |
| 254 | 0.12 | s4 | A_s01-04_claims.csv:160 | results/ranges_2025-mirror.csv | literal line 101 | pass |
| 255 | -7 | s4 | A_s01-04_claims.csv:161 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 256 | 53 | s4 | A_s01-04_claims.csv:162 | analysis/comparison_2025/movers.csv | literal line 8 | pass |
| 257 | 52 | s4 | A_s01-04_claims.csv:162 | analysis/comparison_2025/movers.csv | literal line 35 | pass |
| 258 | 7 | s4 | A_s01-04_claims.csv:163 | results/ranges_2025-mirror.csv | literal line 14 | pass |
| 259 | 53 | s4 | A_s01-04_claims.csv:162 | analysis/comparison_2025/movers.csv | literal line 8 | pass |
| 260 | 2 | s4 | A_s01-04_claims.csv:162 | analysis/comparison_2025/movers.csv | literal line 2 | pass |
| 261 | 3 | s4 | A_s01-04_claims.csv:162 | analysis/comparison_2025/movers.csv | literal line 5 | pass |
| 262 | 1 | s4 | A_s01-04_claims.csv:163 | results/ranges_2025-mirror.csv | literal line 2 | pass |
| 263 | 7 | s5 | A_s05-08_claims.csv:2 | results/scale_curve.csv | literal line 3 | pass |
| 264 | 53 | s5 | A_s05-08_claims.csv:2 | results/scale_curve.csv | literal line 4 | pass |
| 265 | 52 | s5 | A_s05-08_claims.csv:2 |  | A048 | pass |
| 266 | 89 | s5 | A_s05-08_claims.csv:2 | results/scale_curve.csv | literal line 6 | pass |
| 267 | 336 | s5 | A_s05-08_claims.csv:2 | results/scale_curve.csv | literal line 7 | pass |
| 268 | 2,450 | s5 | A_s05-08_claims.csv:2 | results/scale_curve.csv | literal line 8 | pass |
| 269 | 75% | s5 | A_s05-08_claims.csv:6 | results/scale_curve.csv | cell value 0.754 in results/scale_curve.csv; rounded 0.754 x100 line 115 | pass |
| 270 | 44% | s5 | A_s05-08_claims.csv:6 | results/scale_curve.csv | cell value 0.440 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 271 | 58% | s5 | A_s05-08_claims.csv:6 | results/scale_curve.csv | cell value 0.581 in results/scale_curve.csv; rounded 0.579 x100 line 88 | pass |
| 272 | 44% | s5 | A_s05-08_claims.csv:6 | results/scale_curve.csv | cell value 0.440 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 273 | 37% | s5 | A_s05-08_claims.csv:6 | results/scale_curve.csv | literal line 165 | pass |
| 274 | 77% | s5 | A_s05-08_claims.csv:7 | results/scale_curve.csv | cell value 0.771 in results/scale_curve.csv; rounded 0.771 x100 line 31 | pass |
| 275 | 44% | s5 | A_s05-08_claims.csv:6 | results/scale_curve.csv | cell value 0.440 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 276 | 60% | s5 | A_s05-08_claims.csv:7 | results/scale_curve.csv | cell value 0.597 in results/scale_curve.csv; rounded 0.597 x100 line 17 | pass |
| 277 | 46% | s5 | A_s05-08_claims.csv:7 | results/scale_curve.csv | cell value 0.463 in results/scale_curve.csv; rounded 0.462 x100 line 20 | pass |
| 278 | 40% | s5 | A_s05-08_claims.csv:7 | results/scale_curve.csv | literal line 25 | pass |
| 279 | 20% | s5 | A_s05-08_claims.csv:9 | results/scale_curve.csv | cell value 0.198 in results/scale_curve.csv; rounded 2011 x0.01 line 2 | pass |
| 280 | 33.3 | s5 | A_s05-08_claims.csv:11 | results/scale_curve.csv | cell value 33307814 in results/scale_curve.csv; rounded 33307814 x1e-06 line 30 | pass |
| 281 | 25.7 | s5 | A_s05-08_claims.csv:11 | results/scale_curve.csv | cell value 25677412 in results/scale_curve.csv; rounded 25677412 x1e-06 line 31 | pass |
| 282 | 53 | s5 | A_s05-08_claims.csv:11 | results/scale_curve.csv | literal line 4 | pass |
| 283 | 14.7 | s5 | A_s05-08_claims.csv:11 | results/scale_curve.csv | cell value 14,723,989 in results/scale_curve.csv; rounded 14723989 x1e-06 line 39 | pass |
| 284 | 53 | s5 | A_s05-08_claims.csv:14 | results/scale_curve.csv | literal line 4 | pass |
| 285 | 336 | s5 | A_s05-08_claims.csv:14 | results/scale_curve.csv | literal line 7 | pass |
| 286 | 44% | s5 | A_s05-08_claims.csv:14 | results/scale_curve.csv | cell value 0.440 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 287 | 44% | s5 | A_s05-08_claims.csv:14 | results/scale_curve.csv | cell value 0.440 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 288 | 89 | s5 | A_s05-08_claims.csv:15 | results/scale_curve.csv | literal line 6 | pass |
| 289 | 58% | s5 | A_s05-08_claims.csv:15 | results/scale_curve.csv | cell value 0.581 in results/scale_curve.csv; rounded 0.579 x100 line 88 | pass |
| 290 | 44% | s5 | A_s05-08_claims.csv:14 | results/scale_curve.csv | cell value 0.440 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 291 | 326,000 | s5 | A_s05-08_claims.csv:18 | claims register A116 | literal line 1 | pass |
| 292 | 221 | s5 | A_s05-08_claims.csv:18 | claims register A116 | literal line 1 | pass |
| 293 | 41 | s5 | A_s05-08_claims.csv:19 | claims register A116 | literal line 1 | pass |
| 294 | 406 | s5 | A_s05-08_claims.csv:19 | claims register A116 | literal line 1 | pass |
| 295 | 23% | s5 | A_s05-08_claims.csv:20 | results/scale_curve.csv | literal line 32 | pass |
| 296 | 35% | s5 | A_s05-08_claims.csv:20 | results/scale_curve.csv | cell value 0.349 in results/scale_curve.csv; rounded 0.349 x100 line 49 | pass |
| 297 | 53 | s5 | A_s05-08_claims.csv:22 | analysis/regionalise_2025/summary.csv | literal line 2 | pass |
| 298 | 76% | s5 | A_s05-08_claims.csv:22 | analysis/regionalise_2025/summary.csv | cell value 0.757 in analysis/regionalise_2025/summary.csv; rounded 0.757 x100 line 2 | pass |
| 299 | 69% | s5 | A_s05-08_claims.csv:22 | analysis/regionalise_2025/summary.csv | cell value 0.694 in analysis/regionalise_2025/summary.csv; rounded 0.694 x100 line 8 | pass |
| 300 | 66.1% | s5 | A_s05-08_claims.csv:23 | qa/reports/V31d_claims.md | cell value 0.661 in qa/reports/V31d_claims.md; rounded 0.661 x100 line 139 | pass |
| 301 | 76% | s5 | A_s05-08_claims.csv:22 | analysis/regionalise_2025/summary.csv | cell value 0.757 in analysis/regionalise_2025/summary.csv; rounded 0.757 x100 line 2 | pass |
| 302 | 69% | s5 | A_s05-08_claims.csv:22 | analysis/regionalise_2025/summary.csv | cell value 0.694 in analysis/regionalise_2025/summary.csv; rounded 0.694 x100 line 8 | pass |
| 303 | 30.7 | s5 | A_s05-08_claims.csv:26 | results/scale_curve.csv | cell value 30685903 in results/scale_curve.csv; rounded 30685903 x1e-06 line 33 | pass |
| 304 | 33.3 | s5 | A_s05-08_claims.csv:26 | results/scale_curve.csv | cell value 33307814 in results/scale_curve.csv; rounded 33307814 x1e-06 line 30 | pass |
| 305 | 75% | s5 | A_s05-08_claims.csv:28 | results/scale_curve.csv | cell value 0.754 in results/scale_curve.csv; rounded 0.754 x100 line 115 | pass |
| 306 | 54% | s5 | A_s05-08_claims.csv:28 | results/scale_curve.csv | cell value 0.539 in results/scale_curve.csv; rounded 0.542 x100 line 36 | pass |
| 307 | 17 | s5 | A_s05-08_claims.csv:29 | results/scale_curve.csv | cell value 16.5 in REG:A108; rounded 16642649 x1e-06 line 36 | pass |
| 308 | 37% | s5 | A_s05-08_claims.csv:29 | results/scale_curve.csv | literal line 165 | pass |
| 309 | 54% | s5 | A_s05-08_claims.csv:28 | results/scale_curve.csv | cell value 0.539 in results/scale_curve.csv; rounded 0.542 x100 line 36 | pass |
| 310 | 8 | s5 | A_s05-08_claims.csv:30 | papers/A_results/SECTION_SCOPE.md | literal line 14 | pass |
| 311 | 44% | s5 | A_s05-08_claims.csv:30 | papers/A_results/SECTION_SCOPE.md | literal line 346 | pass |
| 312 | 1 | s5 | A_s05-08_claims.csv:34 | results/scale_curve.csv | literal line 2 | pass |
| 313 | 100% | s5 | A_s05-08_claims.csv:34 | results/scale_curve.csv | cell value 1.000 in results/scale_curve.csv; rounded 1 x100 line 2 | pass |
| 314 | 100% | s5 | A_s05-08_claims.csv:34 | results/scale_curve.csv | cell value 1.000 in results/scale_curve.csv; rounded 1 x100 line 2 | pass |
| 315 | 100% | s5 | A_s05-08_claims.csv:34 | results/scale_curve.csv | cell value 1.000 in results/scale_curve.csv; rounded 1 x100 line 2 | pass |
| 316 | 100% | s5 | A_s05-08_claims.csv:34 | results/scale_curve.csv | cell value 1.000 in results/scale_curve.csv; rounded 1 x100 line 2 | pass |
| 317 | 7 | s5 | A_s05-08_claims.csv:35 | results/scale_curve.csv | literal line 3 | pass |
| 318 | 77% | s5 | A_s05-08_claims.csv:35 | results/scale_curve.csv | cell value 0.771 in results/scale_curve.csv; rounded 0.771 x100 line 31 | pass |
| 319 | 44% | s5 | A_s05-08_claims.csv:35 | results/scale_curve.csv | cell value 0.436 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 320 | 75% | s5 | A_s05-08_claims.csv:35 | results/scale_curve.csv | cell value 0.754 in results/scale_curve.csv; rounded 0.754 x100 line 115 | pass |
| 321 | 49% | s5 | A_s05-08_claims.csv:35 | results/scale_curve.csv | cell value 0.491 in results/scale_curve.csv; rounded 0.491 x100 line 8 | pass |
| 322 | 53 | s5 | A_s05-08_claims.csv:36 | results/scale_curve.csv | literal line 4 | pass |
| 323 | 44% | s5 | A_s05-08_claims.csv:36 | results/scale_curve.csv | cell value 0.442 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 324 | 20% | s5 | A_s05-08_claims.csv:36 | results/scale_curve.csv | cell value 0.197 in results/scale_curve.csv; rounded 2011 x0.01 line 2 | pass |
| 325 | 44% | s5 | A_s05-08_claims.csv:36 | results/scale_curve.csv | cell value 0.442 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 326 | 23% | s5 | A_s05-08_claims.csv:36 | results/scale_curve.csv | literal line 32 | pass |
| 327 | 89 | s5 | A_s05-08_claims.csv:37 | results/scale_curve.csv | literal line 6 | pass |
| 328 | 60% | s5 | A_s05-08_claims.csv:37 | results/scale_curve.csv | cell value 0.597 in results/scale_curve.csv; rounded 0.597 x100 line 17 | pass |
| 329 | 32% | s5 | A_s05-08_claims.csv:37 | results/scale_curve.csv | literal line 130 | pass |
| 330 | 58% | s5 | A_s05-08_claims.csv:37 | results/scale_curve.csv | cell value 0.581 in results/scale_curve.csv; rounded 0.579 x100 line 88 | pass |
| 331 | 35% | s5 | A_s05-08_claims.csv:37 | results/scale_curve.csv | cell value 0.349 in results/scale_curve.csv; rounded 0.349 x100 line 49 | pass |
| 332 | 336 | s5 | A_s05-08_claims.csv:38 | results/scale_curve.csv | literal line 7 | pass |
| 333 | 46% | s5 | A_s05-08_claims.csv:38 | results/scale_curve.csv | cell value 0.463 in results/scale_curve.csv; rounded 0.462 x100 line 20 | pass |
| 334 | 23% | s5 | A_s05-08_claims.csv:38 | results/scale_curve.csv | literal line 32 | pass |
| 335 | 44% | s5 | A_s05-08_claims.csv:38 | results/scale_curve.csv | cell value 0.439 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 336 | 24% | s5 | A_s05-08_claims.csv:38 | results/scale_curve.csv | literal line 151 | pass |
| 337 | 2,450 | s5 | A_s05-08_claims.csv:39 | results/scale_curve.csv | literal line 8 | pass |
| 338 | 40% | s5 | A_s05-08_claims.csv:39 | results/scale_curve.csv | literal line 25 | pass |
| 339 | 18% | s5 | A_s05-08_claims.csv:39 | results/scale_curve.csv | cell value 0.180 in results/scale_curve.csv; rounded 18298878 x1e-06 line 8 | pass |
| 340 | 37% | s5 | A_s05-08_claims.csv:39 | results/scale_curve.csv | literal line 165 | pass |
| 341 | 20% | s5 | A_s05-08_claims.csv:39 | results/scale_curve.csv | cell value 0.198 in results/scale_curve.csv; rounded 2011 x0.01 line 2 | pass |
| 342 | 141,000 | s6 | A_s05-08_claims.csv:44 | analysis/scale_curve_2025/README.md | literal line 84 | pass |
| 343 | 10% | s6 | A_s05-08_claims.csv:43 | qa/reports/V31b_claims.md | literal line 50 | pass |
| 344 | 10% | s6 | A_s05-08_claims.csv:43 | qa/reports/V31b_claims.md | literal line 50 | pass |
| 345 | 99% | s6 | A_s05-08_claims.csv:43 | qa/reports/V31b_claims.md | literal line 3 | pass |
| 346 | 221 | s6 | A_s05-08_claims.csv:46 | claims register A116 | literal line 1 | pass |
| 347 | 3.49 | s6 | A_s05-08_claims.csv:48 | analysis/scale_curve_2025/README.md | literal line 84 | pass |
| 348 | 3.32 | s6 | A_s05-08_claims.csv:48 | analysis/scale_curve_2025/README.md | literal line 84 | pass |
| 349 | 175,000 | s6 | A_s05-08_claims.csv:49 | analysis/scale_curve_2025/README.md | literal line 84 | pass |
| 350 | 141,000 | s6 | A_s05-08_claims.csv:49 | analysis/scale_curve_2025/README.md | literal line 84 | pass |
| 351 | 1.96 | s6 | A_s05-08_claims.csv:50 | qa/reports/V31d_claims.md | literal line 32 | pass |
| 352 | 24% | s6 | A_s05-08_claims.csv:52 | analysis/paper_a/scenarios_by_region.csv | literal line 4 | pass |
| 353 | 0.2% | s6 | A_s05-08_claims.csv:52 | analysis/paper_a/scenarios_by_region.csv | literal line 27 | pass |
| 354 | 26% | s6 | A_s05-08_claims.csv:52 |  | claims register A223 output_locator "30.8 / 41.5 - 1 = -25.8%"; V38 "-25.8% at 1 in 10" | pass |
| 355 | 1 | s6 | A_s05-08_claims.csv:49 | analysis/scale_curve_2025/README.md | literal line 9 | pass |
| 356 | 10 | s6 | A_s05-08_claims.csv:52 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 357 | 2.5% | s6 | A_s05-08_claims.csv:53 | analysis/comparators_2025/diet_land.csv | literal line 4 | pass |
| 358 | 118.0 | s6 | A_s05-08_claims.csv:53 | claims register B216 | literal line 1 | pass |
| 359 | 112.4 | s6 | A_s05-08_claims.csv:53 | claims register B216 | literal line 1 | pass |
| 360 | 103.6 | s6 | A_s05-08_claims.csv:54 | analysis/comparators_2025/diet_land.csv | literal line 3 | pass |
| 361 | 65% | s6 | A_s05-08_claims.csv:57 | LIT:L115 | literal line 1 | pass |
| 362 | 100 | s7 | A_s05-08_claims.csv:59 | analysis/paper_a/long_term_levers.csv | literal line 4 | pass |
| 363 | 7.5% | s7 | A_s05-08_claims.csv:61 | analysis/paper_a/long_term_levers.csv | cell value 0.075 in analysis/paper_a/long_term_levers.csv; rounded 0.075 x100 line 5 | pass |
| 364 | 12% | s7 | A_s05-08_claims.csv:61 | analysis/paper_a/long_term_levers.csv | cell value 0.12 in analysis/paper_a/long_term_levers.csv; rounded 0.12 x100 line 9 | pass |
| 365 | 2,360 | s7 | A_s05-08_claims.csv:62 | analysis/paper_a/long_term_levers.csv | literal line 144 | pass |
| 366 | 210 | s7 | A_s05-08_claims.csv:62 | analysis/paper_a/long_term_levers.csv | literal line 144 | pass |
| 367 | 3 | s7 | A_s05-08_claims.csv:62 | analysis/paper_a/long_term_levers.csv | literal line 7 | pass |
| 368 | 30% | s7 | A_s05-08_claims.csv:63 |  | analysis/paper_a/long_term_levers.csv lever "nature2 (0.26 to 0.3)" | pass |
| 369 | 400 | s7 | A_s05-08_claims.csv:64 | LIT:L060 | literal line 1 | pass |
| 370 | 15.35 | s7 | A_s05-08_claims.csv:65 | results/comparison_cells.csv | cell value 15.35 in REG:A007; rounded 15350146 x1e-06 line 3 | pass |
| 371 | 15.6 | s7 | A_s05-08_claims.csv:65 | results/comparison_cells.csv | cell value 15.6 in REG:A008; rounded 15623209 x1e-06 line 3 | pass |
| 372 | 69% | s7 | A_s05-08_claims.csv:66 | analysis/paper_a/long_term_regions.csv | cell value 0.688 in analysis/paper_a/long_term_regions.csv; rounded 0.688 x100 line 2 | pass |
| 373 | 57% | s7 | A_s05-08_claims.csv:66 | analysis/paper_a/long_term_regions.csv | literal line 52 | pass |
| 374 | 0.27 | s7 | A_s05-08_claims.csv:67 | results/comparison_cells.csv | cell value 273063 in results/comparison_cells.csv; rounded 273063 x1e-06 line 3 | pass |
| 375 | 5.28 | s7 | A_s05-08_claims.csv:67 | results/comparison_cells.csv | cell value +5.28 in REG:A013; rounded 5280 x0.001 line 119 | pass |
| 376 | 13.3 | s7 | A_s05-08_claims.csv:68 | results/comparison_cells.csv | cell value 13.3 in REG:A009; rounded 13269 x0.001 line 33 | pass |
| 377 | 18.8 | s7 | A_s05-08_claims.csv:68 | results/comparison_cells.csv | cell value 18.8 in REG:A009; rounded 18778 x0.001 line 24 | pass |
| 378 | 3 | s7 | A_s05-08_claims.csv:92 | analysis/paper_a/long_term_regions.csv | literal line 3 | pass |
| 379 | 15.35 | s7 | A_s05-08_claims.csv:96 | analysis/paper_a/long_term_regions.csv | cell value 15350146 in analysis/paper_a/long_term_regions.csv; rounded 15350146 x1e-06 line 2 | pass |
| 380 | 15.6 | s7 | A_s05-08_claims.csv:96 | analysis/paper_a/long_term_regions.csv | cell value 15623209 in analysis/paper_a/long_term_regions.csv; rounded 0.156 x100 line 30 | pass |
| 381 | 22.3 | s7 | A_s05-08_claims.csv:98 | analysis/paper_a/long_term_regions.csv | cell value 22326388 in analysis/paper_a/long_term_regions.csv; rounded 22326388 x1e-06 line 2 | pass |
| 382 | 27.6 | s7 | A_s05-08_claims.csv:98 | analysis/paper_a/long_term_regions.csv | cell value 27608200 in analysis/paper_a/long_term_regions.csv; rounded 27608200 x1e-06 line 56 | pass |
| 383 | 100 | s7 | A_s05-08_claims.csv:100 | analysis/paper_a/long_term_regions.csv | cell value 100 in REG:A010; rounded 1 x100 line 2 | pass |
| 384 | 69% | s7 | A_s05-08_claims.csv:100 | analysis/paper_a/long_term_regions.csv | cell value 0.688 in analysis/paper_a/long_term_regions.csv; rounded 0.688 x100 line 2 | pass |
| 385 | 57% | s7 | A_s05-08_claims.csv:100 | analysis/paper_a/long_term_regions.csv | literal line 52 | pass |
| 386 | 93% | s7 | A_s05-08_claims.csv:102 | results/2011-fixed-3.csv | cell value 93.41 in REG:A144; rounded 0.9331 x100 line 68 | pass |
| 387 | 94% | s7 | A_s05-08_claims.csv:102 |  | long_term_regions.csv 2025-fixed: over-capacity regions hold 93.8% of the 53 regions' population (recomputed); A326 | pass |
| 388 | 33% | s7 | A_s05-08_claims.csv:104 | analysis/paper_a/long_term_regions.csv | literal line 31 | pass |
| 389 | 38% | s7 | A_s05-08_claims.csv:104 | analysis/paper_a/long_term_regions.csv | literal line 36 | pass |
| 390 | 34.3 | s7 | A_s05-08_claims.csv:70 | analysis/paper_a/long_term_levers.csv | cell value 34274878 in analysis/paper_a/long_term_levers.csv; rounded 34274878 x1e-06 line 137 | pass |
| 391 | 15.6 | s7 | A_s05-08_claims.csv:70 | analysis/paper_a/long_term_levers.csv | cell value 15.6 in REG:A152; rounded 15616131 x1e-06 line 15 | pass |
| 392 | 3.7 | s7 | A_s05-08_claims.csv:71 | analysis/paper_a/long_term_levers.csv | cell value 3705376 in analysis/paper_a/long_term_levers.csv; rounded 3698784 x1e-06 line 38 | pass |
| 393 | 23 | s7 | A_s05-08_claims.csv:73 | analysis/paper_a/long_term_levers.csv | literal line 13 | pass |
| 394 | 11.5 | s7 | A_s05-08_claims.csv:73 | analysis/paper_a/long_term_levers.csv | literal line 13 | pass |
| 395 | 30% | s7 | A_s05-08_claims.csv:76 |  | analysis/paper_a/long_term_levers.csv lever "nature2 (0.26 to 0.3)" | pass |
| 396 | 15.6 | s7 | A_s05-08_claims.csv:93 | analysis/paper_a/long_term_levers.csv | cell value 15.6 in REG:A008; rounded 15616131 x1e-06 line 15 | pass |
| 397 | 1 | s7 | A_s05-08_claims.csv:93 | analysis/paper_a/long_term_levers.csv | literal line 2 | pass |
| 398 | 15.6 | s7 | A_s05-08_claims.csv:95 | results/comparison_cells.csv | cell value 15.6 in REG:A008; rounded 15623209 x1e-06 line 3 | pass |
| 399 | 1 | s7 | A_s05-08_claims.csv:97 | analysis/paper_a/long_term_levers.csv | literal line 2 | pass |
| 400 | 100 | s7 | A_s05-08_claims.csv:97 | analysis/paper_a/long_term_levers.csv | literal line 4 | pass |
| 401 | 34.3 | s7 | A_s05-08_claims.csv:97 | analysis/paper_a/long_term_levers.csv | cell value 34274878 in analysis/paper_a/long_term_levers.csv; rounded 34274878 x1e-06 line 137 | pass |
| 402 | 2,360 | s7 | A_s05-08_claims.csv:99 | analysis/paper_a/long_term_levers.csv | literal line 144 | pass |
| 403 | 210 | s7 | A_s05-08_claims.csv:99 | analysis/paper_a/long_term_levers.csv | literal line 144 | pass |
| 404 | 3.7 | s7 | A_s05-08_claims.csv:99 | analysis/paper_a/long_term_levers.csv | cell value 3705376 in analysis/paper_a/long_term_levers.csv; rounded 3698784 x1e-06 line 38 | pass |
| 405 | 0.12 | s7 | A_s05-08_claims.csv:101 | analysis/paper_a/long_term_levers.csv | literal line 9 | pass |
| 406 | 0 | s7 | A_s05-08_claims.csv:101 | analysis/paper_a/long_term_levers.csv | literal line 5 | pass |
| 407 | 13.0 | s7 | A_s05-08_claims.csv:101 | analysis/paper_a/long_term_levers.csv | cell value 12975247 in analysis/paper_a/long_term_levers.csv; rounded 0.13 x100 line 5 | pass |
| 408 | 0 | s7 | A_s05-08_claims.csv:103 | analysis/paper_a/long_term_levers.csv | literal line 5 | pass |
| 409 | 1 | s7 | A_s05-08_claims.csv:103 | analysis/paper_a/long_term_levers.csv | literal line 2 | pass |
| 410 | 15.4 | s7 | A_s05-08_claims.csv:103 | analysis/paper_a/long_term_levers.csv | cell value 15434761 in analysis/paper_a/long_term_levers.csv; rounded 15350146 x1e-06 line 3 | pass |
| 411 | 0.07 | s7 | A_s05-08_claims.csv:105 | analysis/paper_a/long_term_levers.csv | literal line 69 | pass |
| 412 | 1 | s7 | A_s05-08_claims.csv:105 | analysis/paper_a/long_term_levers.csv | literal line 2 | pass |
| 413 | 19.0 | s7 | A_s05-08_claims.csv:105 | analysis/paper_a/long_term_levers.csv | cell value 19036647 in analysis/paper_a/long_term_levers.csv; rounded 0.19 x100 line 102 | pass |
| 414 | 1 | s7 | A_s05-08_claims.csv:106 | analysis/paper_a/long_term_levers.csv | literal line 2 | pass |
| 415 | 3 | s7 | A_s05-08_claims.csv:106 | analysis/paper_a/long_term_levers.csv | literal line 7 | pass |
| 416 | 16.2 | s7 | A_s05-08_claims.csv:106 | analysis/paper_a/long_term_levers.csv | cell value 16195875 in analysis/paper_a/long_term_levers.csv; rounded 16195875 x1e-06 line 140 | pass |
| 417 | 0.0023 | s7 | A_s05-08_claims.csv:107 | analysis/paper_a/long_term_levers.csv | literal line 145 | pass |
| 418 | 1 | s7 | A_s05-08_claims.csv:107 | analysis/paper_a/long_term_levers.csv | literal line 2 | pass |
| 419 | 16.1 | s7 | A_s05-08_claims.csv:107 | analysis/paper_a/long_term_levers.csv | cell value 16106693 in analysis/paper_a/long_term_levers.csv; rounded 16106693 x1e-06 line 145 | pass |
| 420 | 23 | s7 | A_s05-08_claims.csv:108 | analysis/paper_a/long_term_levers.csv | literal line 13 | pass |
| 421 | 11.5 | s7 | A_s05-08_claims.csv:108 | analysis/paper_a/long_term_levers.csv | literal line 13 | pass |
| 422 | 11.1 | s7 | A_s05-08_claims.csv:108 | analysis/paper_a/long_term_levers.csv | cell value 11064149 in analysis/paper_a/long_term_levers.csv; rounded 11064149 x1e-06 line 146 | pass |
| 423 | 0.5 | s7 | A_s05-08_claims.csv:109 | analysis/paper_a/long_term_levers.csv | literal line 6 | pass |
| 424 | 1 | s7 | A_s05-08_claims.csv:109 | analysis/paper_a/long_term_levers.csv | literal line 2 | pass |
| 425 | 19.7 | s7 | A_s05-08_claims.csv:109 | analysis/paper_a/long_term_levers.csv | cell value 19677292 in analysis/paper_a/long_term_levers.csv; rounded 19677292 x1e-06 line 147 | pass |
| 426 | 0.12 | s7 | A_s05-08_claims.csv:110 | analysis/paper_a/long_term_levers.csv | literal line 9 | pass |
| 427 | 0.9 | s7 | A_s05-08_claims.csv:110 | analysis/paper_a/long_term_levers.csv | literal line 15 | pass |
| 428 | 22.8 | s7 | A_s05-08_claims.csv:110 | analysis/paper_a/long_term_levers.csv | cell value 22831774 in analysis/paper_a/long_term_levers.csv; rounded 22793 x0.001 line 124 | pass |
| 429 | 0.578 | s7 | A_s05-08_claims.csv:111 | analysis/paper_a/long_term_levers.csv | literal line 139 | pass |
| 430 | 0.5 | s7 | A_s05-08_claims.csv:111 | analysis/paper_a/long_term_levers.csv | literal line 6 | pass |
| 431 | 14.7 | s7 | A_s05-08_claims.csv:111 | analysis/paper_a/long_term_levers.csv | cell value 14721800 in analysis/paper_a/long_term_levers.csv; rounded 14721800 x1e-06 line 139 | pass |
| 432 | 0.12 | s7 | A_s05-08_claims.csv:112 | analysis/paper_a/long_term_levers.csv | literal line 9 | pass |
| 433 | 0.075 | s7 | A_s05-08_claims.csv:112 | analysis/paper_a/long_term_levers.csv | literal line 5 | pass |
| 434 | 11.7 | s7 | A_s05-08_claims.csv:112 | analysis/paper_a/long_term_levers.csv | cell value 11650001 in analysis/paper_a/long_term_levers.csv; rounded 11650001 x1e-06 line 138 | pass |
| 435 | 0.8 | s7 | A_s05-08_claims.csv:113 | analysis/paper_a/long_term_levers.csv | literal line 149 | pass |
| 436 | 5 | s7 | A_s05-08_claims.csv:113 | analysis/paper_a/long_term_levers.csv | literal line 16 | pass |
| 437 | 730 | s7 | A_s05-08_claims.csv:113 | analysis/paper_a/long_term_levers.csv | literal line 17 | pass |
| 438 | 500 | s7 | A_s05-08_claims.csv:113 | analysis/paper_a/long_term_levers.csv | literal line 17 | pass |
| 439 | 0.26 | s7 | A_s05-08_claims.csv:113 | analysis/paper_a/long_term_levers.csv | literal line 151 | pass |
| 440 | 0.3 | s7 | A_s05-08_claims.csv:113 | analysis/paper_a/long_term_levers.csv | literal line 18 | pass |
| 441 | 15.6 | s7 | A_s05-08_claims.csv:113 | analysis/paper_a/long_term_levers.csv | cell value 15623209 in analysis/paper_a/long_term_levers.csv; rounded 15616131 x1e-06 line 15 | pass |
| 442 | 0% | s7 | A_s05-08_claims.csv:113 | analysis/paper_a/long_term_levers.csv | literal line 5 | pass |
| 443 | 0.12 | s7 | A_s05-08_claims.csv:78 | analysis/paper_a/long_term_regions.csv | cell value 0.12 in analysis/paper_a/long_term_regions.csv; rounded 12 x0.01 line 12 | pass |
| 444 | 0.26 | s7 | A_s05-08_claims.csv:78 | analysis/paper_a/long_term_regions.csv | cell value 0.26 in REG:A149; rounded 0.256 x1 line 52 | pass |
| 445 | 53 | s7 | A_s05-08_claims.csv:82 | analysis/comparison_2025/movers.csv | literal line 8 | pass |
| 446 | 52 | s7 | A_s05-08_claims.csv:82 | analysis/comparison_2025/movers.csv | literal line 35 | pass |
| 447 | 35 | s7 | A_s05-08_claims.csv:80 | analysis/paper_a/regional_flips-3.csv | literal line 14 | pass |
| 448 | 32 | s7 | A_s05-08_claims.csv:80 | analysis/paper_a/regional_flips-3.csv | literal line 26 | pass |
| 449 | 18 | s7 | A_s05-08_claims.csv:81 | results/2011-fixed-3.csv | literal line 36 | pass |
| 450 | 21 | s7 | A_s05-08_claims.csv:81 | results/2011-fixed-3.csv | literal line 42 | pass |
| 451 | 3 | s7 | A_s05-08_claims.csv:80 | analysis/paper_a/regional_flips-3.csv | literal line 5 | pass |
| 452 | 1 | s7 | A_s05-08_claims.csv:78 | analysis/paper_a/long_term_regions.csv | literal line 2 | pass |
| 453 | 93% | s7 | A_s05-08_claims.csv:88 | results/2011-fixed-3.csv | cell value 93.41 in REG:A144; rounded 0.9331 x100 line 68 | pass |
| 454 | 94% | s7 | A_s05-08_claims.csv:88 |  | long_term_regions.csv 2025-fixed: over-capacity regions hold 93.8% of the 53 regions' population (recomputed); A326 | pass |
| 455 | 33% | s7 | A_s05-08_claims.csv:89 | analysis/paper_a/long_term_regions.csv | literal line 31 | pass |
| 456 | 38% | s7 | A_s05-08_claims.csv:89 | analysis/paper_a/long_term_regions.csv | literal line 36 | pass |
| 457 | 20% | s7 | A_s05-08_claims.csv:90 | results/scale_curve.csv | cell value 0.197 in results/scale_curve.csv; rounded 2011 x0.01 line 2 | pass |
| 458 | 23% | s7 | A_s05-08_claims.csv:90 | results/scale_curve.csv | literal line 32 | pass |
| 459 | 53 | s8 | A_s05-08_claims.csv:115 |  | A048 (structural count) | pass |
| 460 | 52 | s8 | A_s05-08_claims.csv:115 |  | A048 (structural count) | pass |
| 461 | 1 | s8 | A_s05-08_claims.csv:116 | claims register A200 | literal line 1 | pass |
| 462 | 10 | s8 | A_s05-08_claims.csv:116 | claims register A200 | literal line 1 | pass |
| 463 | 1.5 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 8 | pass |
| 464 | 1.11 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 465 | 1.12 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 10 | pass |
| 466 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 467 | 10 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 468 | 30.8 | s8 | A_s05-08_claims.csv:120 | analysis/comparators_2025/rerun.csv | cell value 30.81 in analysis/comparators_2025/rerun.csv; rounded 30.81 x1 line 44 | pass |
| 469 | 27.6 | s8 | A_s05-08_claims.csv:122 | qa/reports/B123_shocks_on_widened_draws.md | literal line 11 | pass |
| 470 | 0.68 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 7 | pass |
| 471 | 0.69 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 13 | pass |
| 472 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 473 | 100 | s8 | A_s05-08_claims.csv:165 | analysis/paper_a/shocks_summary-3.csv | literal line 7 | pass |
| 474 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 475 | 20 | s8 | A_s05-08_claims.csv:118 | analysis/paper_a/shocks_summary.csv | literal line 5 | pass |
| 476 | 1.12 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 10 | pass |
| 477 | 1.05 | s8 | A_s05-08_claims.csv:118 | claims register A196 | literal line 1 | pass |
| 478 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 479 | 10 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 480 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 481 | 20 | s8 | A_s05-08_claims.csv:118 | analysis/paper_a/shocks_summary.csv | literal line 5 | pass |
| 482 | 5 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 3 | pass |
| 483 | 95 | s8 | A_s05-08_claims.csv:117 |  | structural (percentile label) | pass |
| 484 | 19 | s8 | A_s05-08_claims.csv:120 | analysis/comparators_2025/rerun.csv | literal line 15 | pass |
| 485 | 23.1 | s8 | A_s05-08_claims.csv:120 | qa/reports/B123_shocks_on_widened_draws.md | literal line 14 | pass |
| 486 | 36.5 | s8 | A_s05-08_claims.csv:120 | analysis/comparators_2025/rerun.csv | cell value 36.5 in qa/reports/B123_shocks_on_widened_draws.md; rounded 36.45 x1 line 31 | pass |
| 487 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 488 | 10 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 489 | 30.8 | s8 | A_s05-08_claims.csv:120 | analysis/comparators_2025/rerun.csv | cell value 30.81 in analysis/comparators_2025/rerun.csv; rounded 30.81 x1 line 44 | pass |
| 490 | 0.84 | s8 | A_s05-08_claims.csv:120 | qa/reports/B123_shocks_on_widened_draws.md | literal line 83 | pass |
| 491 | 1.32 | s8 | A_s05-08_claims.csv:120 | qa/reports/B123_shocks_on_widened_draws.md | literal line 83 | pass |
| 492 | 19.7 | s8 | A_s05-08_claims.csv:121 | qa/reports/B123_shocks_on_widened_draws.md | literal line 15 | pass |
| 493 | 31.2 | s8 | A_s05-08_claims.csv:121 | qa/reports/B123_shocks_on_widened_draws.md | literal line 15 | pass |
| 494 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 495 | 20 | s8 | A_s05-08_claims.csv:118 | analysis/paper_a/shocks_summary.csv | literal line 5 | pass |
| 496 | 26.3 | s8 | A_s05-08_claims.csv:121 | analysis/comparators_2025/rerun.csv | cell value 26.32 in analysis/comparators_2025/rerun.csv; rounded 26.32 x1 line 45 | pass |
| 497 | 1.13 | s8 | A_s05-08_claims.csv:121 | qa/reports/B123_shocks_on_widened_draws.md | literal line 84 | pass |
| 498 | 27.6 | s8 | A_s05-08_claims.csv:122 | qa/reports/B123_shocks_on_widened_draws.md | literal line 11 | pass |
| 499 | 37% | s8 | A_s05-08_claims.csv:123 | analysis/comparators_2025/rerun.csv | literal line 43 | pass |
| 500 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 501 | 10 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 502 | 78% | s8 | A_s05-08_claims.csv:123 | qa/reports/B123_shocks_on_widened_draws.md | cell value 77.65 in qa/reports/B123_shocks_on_widened_draws.md; rounded 77.65 x1 line 15 | pass |
| 503 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 504 | 20 | s8 | A_s05-08_claims.csv:118 | analysis/paper_a/shocks_summary.csv | literal line 5 | pass |
| 505 | 0.45% | s8 | A_s05-08_claims.csv:123 | analysis/comparators_2025/rerun.csv | cell value 0.45 in analysis/comparators_2025/rerun.csv; rounded 44.92 x0.01 line 28 | pass |
| 506 | 13 | s8 | A_s05-08_claims.csv:121 | qa/reports/B123_shocks_on_widened_draws.md | literal line 17 | pass |
| 507 | 13 | s8 | A_s05-08_claims.csv:121 | qa/reports/B123_shocks_on_widened_draws.md | literal line 17 | pass |
| 508 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 509 | 20 | s8 | A_s05-08_claims.csv:118 | analysis/paper_a/shocks_summary.csv | literal line 5 | pass |
| 510 | 5.8% | s8 | A_s05-08_claims.csv:127 |  | qa/reports/R03a_response_plan_A.md issue 11 ("about 1 in 17, 5.8%"); B124 line 18 (5.83%) | pass |
| 511 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 512 | 17 | s8 | A_s05-08_claims.csv:127 | results/comparison_cells.csv | literal line 34 | pass |
| 513 | 41.5 | s8 | A_s05-08_claims.csv:128 | results/comparison_cells.csv | cell value 41.5 in REG:A003; rounded 41503537 x1e-06 line 2 | pass |
| 514 | 40.5 | s8 | A_s05-08_claims.csv:128 | results/comparison_cells.csv | cell value 40.5 in LIT:L226; rounded 40450144 x1e-06 line 2 | pass |
| 515 | 41 | s8 | A_s05-08_claims.csv:128 | results/comparison_cells.csv | literal line 82 | pass |
| 516 | 1 | s8 | A_s05-08_claims.csv:128 | results/comparison_cells.csv | literal line 2 | pass |
| 517 | 10 | s8 | A_s05-08_claims.csv:128 | results/comparison_cells.csv | literal line 20 | pass |
| 518 | 30.8 | s8 | A_s05-08_claims.csv:128 | results/comparison_cells.csv | cell value 30.8 in analysis/paper_a/shocks_summary.csv; rounded 30780 x0.001 line 26 | pass |
| 519 | 97% | s8 | A_s05-08_claims.csv:129 |  | qa/reports/V38_check_B112.md verdict item 4 ("about 97%") | pass |
| 520 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 521 | 10 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 522 | 41.2 | s8 | A_s05-08_claims.csv:130 | results/ranges_2025-fixed.csv | cell value 41.19 in qa/reports/B112_shock_ranges.md; rounded 41230792 x1e-06 line 2 | pass |
| 523 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 524 | 10 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 525 | 30.8 | s8 | A_s05-08_claims.csv:130 | results/ranges_2025-fixed.csv | cell value 30.81 in qa/reports/B112_shock_ranges.md; rounded 0.308 x100 line 55 | pass |
| 526 | 1 | s8 | A_s05-08_claims.csv:117 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 527 | 100 | s8 | A_s05-08_claims.csv:131 | results/ranges_2025-fixed.csv | cell value 100 in results/ranges_2025-fixed.csv; rounded 1 x100 line 2 | pass |
| 528 | 24.7 | s8 | A_s05-08_claims.csv:131 | qa/reports/B112_shock_ranges.md | literal line 10 | pass |
| 529 | 15.6 | s8 | A_s05-08_claims.csv:131 | results/ranges_2025-fixed.csv | cell value 15.62 in qa/reports/B112_shock_ranges.md; rounded 15638330 x1e-06 line 3 | pass |
| 530 | 3 | s8 | A_s05-08_claims.csv:156 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 531 | 53 | s8 | A_s05-08_claims.csv:156 | analysis/paper_a/shocks_summary-3.csv | literal line 1 | pass |
| 532 | 81.55% | s8 | A_s05-08_claims.csv:156 | qa/reports/V36_check_B110.md | literal line 35 | pass |
| 533 | 91.48% | s8 | A_s05-08_claims.csv:156 | qa/reports/V36_check_B110.md | literal line 38 | pass |
| 534 | 33.3 | s8 | A_s05-08_claims.csv:162 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 535 | 22.3 | s8 | A_s05-08_claims.csv:162 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 536 | 1.49 | s8 | A_s05-08_claims.csv:162 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 537 | 82% | s8 | A_s05-08_claims.csv:162 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 538 | 21.0 | s8 | A_s05-08_claims.csv:162 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 539 | 0.63 | s8 | A_s05-08_claims.csv:162 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 540 | 1 | s8 | A_s05-08_claims.csv:163 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 541 | 10 | s8 | A_s05-08_claims.csv:163 | analysis/paper_a/shocks_summary-3.csv | literal line 4 | pass |
| 542 | 24.7 | s8 | A_s05-08_claims.csv:163 | analysis/paper_a/shocks_summary-3.csv | literal line 4 | pass |
| 543 | 22.3 | s8 | A_s05-08_claims.csv:163 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 544 | 1.11 | s8 | A_s05-08_claims.csv:163 | analysis/paper_a/shocks_summary-3.csv | literal line 4 | pass |
| 545 | 85% | s8 | A_s05-08_claims.csv:163 | analysis/paper_a/shocks_summary-3.csv | literal line 4 | pass |
| 546 | 13.9 | s8 | A_s05-08_claims.csv:163 | analysis/paper_a/shocks_summary-3.csv | literal line 4 | pass |
| 547 | 0.56 | s8 | A_s05-08_claims.csv:163 | analysis/paper_a/shocks_summary-3.csv | literal line 4 | pass |
| 548 | 1 | s8 | A_s05-08_claims.csv:164 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 549 | 20 | s8 | A_s05-08_claims.csv:164 | analysis/paper_a/shocks_summary-3.csv | literal line 5 | pass |
| 550 | 20.0 | s8 | A_s05-08_claims.csv:164 | analysis/paper_a/shocks_summary-3.csv | literal line 5 | pass |
| 551 | 22.3 | s8 | A_s05-08_claims.csv:164 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 552 | 0.89 | s8 | A_s05-08_claims.csv:164 | analysis/paper_a/shocks_summary-3.csv | literal line 5 | pass |
| 553 | 88% | s8 | A_s05-08_claims.csv:164 | analysis/paper_a/shocks_summary-3.csv | literal line 5 | pass |
| 554 | 10.6 | s8 | A_s05-08_claims.csv:164 | analysis/paper_a/shocks_summary-3.csv | literal line 5 | pass |
| 555 | 0.53 | s8 | A_s05-08_claims.csv:164 | analysis/paper_a/shocks_summary-3.csv | literal line 5 | pass |
| 556 | 1 | s8 | A_s05-08_claims.csv:165 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 557 | 100 | s8 | A_s05-08_claims.csv:165 | analysis/paper_a/shocks_summary-3.csv | literal line 7 | pass |
| 558 | 15.2 | s8 | A_s05-08_claims.csv:165 | analysis/paper_a/shocks_summary-3.csv | literal line 7 | pass |
| 559 | 22.3 | s8 | A_s05-08_claims.csv:165 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 560 | 0.68 | s8 | A_s05-08_claims.csv:165 | analysis/paper_a/shocks_summary-3.csv | literal line 7 | pass |
| 561 | 91% | s8 | A_s05-08_claims.csv:165 | analysis/paper_a/shocks_summary-3.csv | literal line 7 | pass |
| 562 | 7.2 | s8 | A_s05-08_claims.csv:165 | analysis/paper_a/shocks_summary-3.csv | literal line 7 | pass |
| 563 | 0.47 | s8 | A_s05-08_claims.csv:165 | analysis/paper_a/shocks_summary-3.csv | literal line 7 | pass |
| 564 | 41.5 | s8 | A_s05-08_claims.csv:158 | analysis/paper_a/shocks_summary.csv | literal line 8 | pass |
| 565 | 27.6 | s8 | A_s05-08_claims.csv:158 | analysis/paper_a/shocks_summary.csv | literal line 8 | pass |
| 566 | 1.5 | s8 | A_s05-08_claims.csv:158 | analysis/paper_a/shocks_summary.csv | literal line 8 | pass |
| 567 | 81% | s8 | A_s05-08_claims.csv:158 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 568 | 26.0 | s8 | A_s05-08_claims.csv:158 | analysis/paper_a/shocks_summary.csv | literal line 8 | pass |
| 569 | 0.63 | s8 | A_s05-08_claims.csv:158 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 570 | 1 | s8 | A_s05-08_claims.csv:159 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 571 | 10 | s8 | A_s05-08_claims.csv:159 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 572 | 30.8 | s8 | A_s05-08_claims.csv:159 | analysis/paper_a/shocks_summary.csv | literal line 10 | pass |
| 573 | 27.6 | s8 | A_s05-08_claims.csv:159 | analysis/paper_a/shocks_summary.csv | literal line 8 | pass |
| 574 | 1.12 | s8 | A_s05-08_claims.csv:159 | analysis/paper_a/shocks_summary.csv | literal line 10 | pass |
| 575 | 85% | s8 | A_s05-08_claims.csv:159 | analysis/paper_a/shocks_summary.csv | literal line 10 | pass |
| 576 | 16.9 | s8 | A_s05-08_claims.csv:159 | analysis/paper_a/shocks_summary.csv | literal line 10 | pass |
| 577 | 0.55 | s8 | A_s05-08_claims.csv:159 | analysis/paper_a/shocks_summary.csv | literal line 10 | pass |
| 578 | 1 | s8 | A_s05-08_claims.csv:160 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 579 | 20 | s8 | A_s05-08_claims.csv:160 | analysis/paper_a/shocks_summary.csv | literal line 5 | pass |
| 580 | 26.3 | s8 | A_s05-08_claims.csv:160 | analysis/paper_a/shocks_summary.csv | literal line 11 | pass |
| 581 | 27.6 | s8 | A_s05-08_claims.csv:160 | analysis/paper_a/shocks_summary.csv | literal line 8 | pass |
| 582 | 0.95 | s8 | A_s05-08_claims.csv:160 | analysis/paper_a/shocks_summary.csv | literal line 11 | pass |
| 583 | 89% | s8 | A_s05-08_claims.csv:160 | analysis/paper_a/shocks_summary.csv | literal line 11 | pass |
| 584 | 13.4 | s8 | A_s05-08_claims.csv:160 | analysis/paper_a/shocks_summary.csv | literal line 11 | pass |
| 585 | 0.51 | s8 | A_s05-08_claims.csv:160 | analysis/paper_a/shocks_summary.csv | literal line 11 | pass |
| 586 | 1 | s8 | A_s05-08_claims.csv:161 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 587 | 100 | s8 | A_s05-08_claims.csv:161 | analysis/paper_a/shocks_summary.csv | literal line 7 | pass |
| 588 | 18.9 | s8 | A_s05-08_claims.csv:161 | analysis/paper_a/shocks_summary.csv | literal line 13 | pass |
| 589 | 27.6 | s8 | A_s05-08_claims.csv:161 | analysis/paper_a/shocks_summary.csv | literal line 8 | pass |
| 590 | 0.69 | s8 | A_s05-08_claims.csv:161 | analysis/paper_a/shocks_summary.csv | literal line 13 | pass |
| 591 | 91% | s8 | A_s05-08_claims.csv:161 | analysis/paper_a/shocks_summary.csv | literal line 6 | pass |
| 592 | 8.7 | s8 | A_s05-08_claims.csv:161 | analysis/paper_a/shocks_summary.csv | literal line 13 | pass |
| 593 | 0.46 | s8 | A_s05-08_claims.csv:161 | analysis/paper_a/shocks_summary.csv | literal line 12 | pass |
| 594 | 82% | s8 | A_s05-08_claims.csv:133 | analysis/paper_a/shocks_summary.csv | literal line 3 | pass |
| 595 | 53 | s8 | A_s05-08_claims.csv:133 | analysis/paper_a/shocks_summary.csv | literal line 1 | pass |
| 596 | 81% | s8 | A_s05-08_claims.csv:133 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 597 | 16 | s8 | A_s05-08_claims.csv:135 | analysis/paper_a/shocks_summary.csv | literal line 8 | pass |
| 598 | 21 | s8 | A_s05-08_claims.csv:135 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 599 | 1 | s8 | A_s05-08_claims.csv:133 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 600 | 10 | s8 | A_s05-08_claims.csv:135 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 601 | 22 | s8 | A_s05-08_claims.csv:134 | analysis/paper_a/shocks_summary-3.csv | literal line 2 | pass |
| 602 | 25 | s8 | A_s05-08_claims.csv:133 |  | analysis/paper_a/shocks_summary-3.csv line 4 (25 regions at 1 in 10, 2011) | pass |
| 603 | 1 | s8 | A_s05-08_claims.csv:133 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 604 | 10 | s8 | A_s05-08_claims.csv:135 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 605 | 1 | s8 | A_s05-08_claims.csv:133 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 606 | 20 | s8 | A_s05-08_claims.csv:133 | analysis/paper_a/shocks_summary.csv | literal line 5 | pass |
| 607 | 1 | s8 | A_s05-08_claims.csv:133 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 608 | 10 | s8 | A_s05-08_claims.csv:135 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 609 | 63% | s8 | A_s05-08_claims.csv:143 |  | shocks_summary.csv line 8 sum over national 0.63 | pass |
| 610 | 55% | s8 | A_s05-08_claims.csv:144 |  | shocks_summary.csv line 10 sum over national 0.55 | pass |
| 611 | 1 | s8 | A_s05-08_claims.csv:144 | analysis/paper_a/shocks_summary.csv | literal line 2 | pass |
| 612 | 10 | s8 | A_s05-08_claims.csv:144 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 613 | 16.9 | s8 | A_s05-08_claims.csv:144 | analysis/paper_a/shocks_summary.csv | literal line 10 | pass |
| 614 | 27.6 | s8 | A_s05-08_claims.csv:144 | analysis/paper_a/shocks_summary.csv | literal line 8 | pass |
| 615 | 44% | s8 | A_s05-08_claims.csv:145 |  | results/scale_curve.csv 2025-fixed short NRM state 0.440 | pass |
| 616 | 41.5 | s8 | A_s05-08_claims.csv:146 | analysis/paper_a/scenarios_by_region.csv | literal line 25 | pass |
| 617 | 15.6 | s8 | A_s05-08_claims.csv:146 | analysis/paper_a/scenarios_by_region.csv | literal line 24 | pass |
| 618 | 6% | s8 | A_s05-08_claims.csv:147 | analysis/paper_a/scenarios_by_region.csv | literal line 22 | pass |
| 619 | 16.4% | s8 | A_s05-08_claims.csv:148 | analysis/paper_a/measures.csv | literal line 12 | pass |
| 620 | 8.15% | s8 | A_s05-08_claims.csv:148 | analysis/paper_a/scenarios_by_region.csv | literal line 44 | pass |
| 621 | 48.45% | s8 | A_s05-08_claims.csv:149 | analysis/paper_a/scenarios_by_region.csv | literal line 32 | pass |
| 622 | 64.47% | s8 | A_s05-08_claims.csv:149 | analysis/paper_a/scenarios_by_region.csv | literal line 34 | pass |
| 623 | 30 | s8 | A_s05-08_claims.csv:153 | papers/A_results/SECTION_SCOPE.md | literal line 12 | pass |
| 624 | 41% | s8 | A_s05-08_claims.csv:153 | papers/A_results/SECTION_SCOPE.md | literal line 481 | pass |
| 625 | 53 | s9 | A_s09-12_claims.csv:5 | analysis/paper_a/regional_flips.csv | literal line 8 | pass |
| 626 | 52 | s9 | A_s09-12_claims.csv:5 | analysis/paper_a/regional_flips.csv | literal line 35 | pass |
| 627 | 2,000 | s9 | A_s09-12_claims.csv:6 | results/ranges_2025-improved.csv | cell value 2,000 in qa/reports/B115_monte_carlo_widened.md; rounded 20 x100 line 40 | pass |
| 628 | 19 | s9 | A_s09-12_claims.csv:6 | results/ranges_2025-improved.csv | literal line 38 | pass |
| 629 | 18 | s9 | A_s09-12_claims.csv:6 | results/ranges_2025-improved.csv | literal line 36 | pass |
| 630 | 1,000 | s9 | A_s09-12_claims.csv:7 | analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md | literal line 7 | pass |
| 631 | 13 | s9 | A_s09-12_claims.csv:7 | analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md | literal line 7 | pass |
| 632 | 12 | s9 | A_s09-12_claims.csv:7 | analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md | literal line 8 | pass |
| 633 | 5 | s9 | A_s09-12_claims.csv:9 | results/ranges_2025-improved.csv | literal line 1 | pass |
| 634 | 95 | s9 | A_s09-12_claims.csv:19 | results/ranges_2025-fixed.csv | literal line 1 | pass |
| 635 | 31.1 | s9 | A_s09-12_claims.csv:8 | results/ranges_2025-improved.csv | cell value 31.1 in qa/reports/B115_monte_carlo_widened.md; rounded 31061 x0.001 line 26 | pass |
| 636 | 49.2 | s9 | A_s09-12_claims.csv:8 | qa/reports/B115_monte_carlo_widened.md | literal line 33 | pass |
| 637 | 1.58 | s9 | A_s09-12_claims.csv:9 | results/ranges_2025-improved.csv | cell value 1.58 in qa/reports/B115_monte_carlo_widened.md; rounded 1581098 x1e-06 line 54 | pass |
| 638 | 26.2 | s9 | A_s09-12_claims.csv:9 | results/ranges_2025-improved.csv | cell value 26.2 in qa/reports/B115_monte_carlo_widened.md; rounded 26194 x0.001 line 117 | pass |
| 639 | 58.1 | s9 | A_s09-12_claims.csv:9 | qa/reports/B115_monte_carlo_widened.md | literal line 34 | pass |
| 640 | 2.22 | s9 | A_s09-12_claims.csv:9 | qa/reports/B115_monte_carlo_widened.md | literal line 34 | pass |
| 641 | 13.3 | s9 | A_s09-12_claims.csv:10 | results/ranges_2025-improved.csv | cell value 13.3 in qa/reports/B115_monte_carlo_widened.md; rounded 0.133 x100 line 21 | pass |
| 642 | 18.8 | s9 | A_s09-12_claims.csv:10 | results/ranges_2025-improved.csv | cell value 18.8 in qa/reports/B115_monte_carlo_widened.md; rounded 18757 x0.001 line 65 | pass |
| 643 | 32% | s9 | A_s09-12_claims.csv:11 | results/ranges_2025-improved.csv | literal line 64 | pass |
| 644 | 27% | s9 | A_s09-12_claims.csv:11 | results/ranges_2025-improved.csv | literal line 54 | pass |
| 645 | 24% | s9 | A_s09-12_claims.csv:11 | results/ranges_2025-improved.csv | literal line 48 | pass |
| 646 | 13 | s9 | A_s09-12_claims.csv:10 | results/ranges_2025-improved.csv | literal line 26 | pass |
| 647 | 39.4 | s9 | A_s09-12_claims.csv:13 | results/ranges_2025-fixed.csv | cell value 39.4 in qa/reports/B112_shock_ranges.md; rounded 0.394 x100 line 10 | pass |
| 648 | 43.8 | s9 | A_s09-12_claims.csv:13 | results/ranges_2025-fixed.csv | cell value 43.8 in qa/reports/B112_shock_ranges.md; rounded 0.438 x100 line 45 | pass |
| 649 | 13.9 | s9 | A_s09-12_claims.csv:13 | results/ranges_2025-fixed.csv | cell value 13.9 in qa/reports/B112_shock_ranges.md; rounded 0.139 x100 line 65 | pass |
| 650 | 16.2 | s9 | A_s09-12_claims.csv:13 | results/ranges_2025-fixed.csv | cell value 16.2 in qa/reports/B112_shock_ranges.md; rounded 0.162 x100 line 30 | pass |
| 651 | 85% | s9 | A_s09-12_claims.csv:14 | results/ranges_2025-fixed.csv | cell value 84.7 in qa/reports/B112_shock_ranges.md; rounded 0.851 x100 line 6 | pass |
| 652 | 33.3 | s9 | A_s09-12_claims.csv:15 | results/comparison_cells.csv | cell value 33.3 in REG:A009; rounded 33307814 x1e-06 line 2 | pass |
| 653 | 15.35 | s9 | A_s09-12_claims.csv:15 | results/comparison_cells.csv | cell value 15.35 in REG:A009; rounded 15350146 x1e-06 line 3 | pass |
| 654 | 5 | s9 | A_s09-12_claims.csv:19 | results/ranges_2025-fixed.csv | literal line 1 | pass |
| 655 | 95 | s9 | A_s09-12_claims.csv:19 | results/ranges_2025-fixed.csv | literal line 1 | pass |
| 656 | 0.115 | s9 | A_s09-12_claims.csv:27 | analysis/sensitivity_2025/README.md | literal line 175 | pass |
| 657 | 0.528 | s9 | A_s09-12_claims.csv:27 | analysis/sensitivity_2025/README.md | literal line 175 | pass |
| 658 | 0.30 | s9 | A_s09-12_claims.csv:29 | analysis/sensitivity_2025/README.md | literal line 84 | pass |
| 659 | 16.0% | s9 | A_s09-12_claims.csv:34 | analysis/paper_a/method_effects_summary.csv | literal line 3 | pass |
| 660 | +20.7% | s9 | A_s09-12_claims.csv:36 | analysis/paper_a/method_effects_summary.csv | literal line 10 | pass |
| 661 | +97.9% | s9 | A_s09-12_claims.csv:37 | analysis/paper_a/method_effects_by_region.csv | literal line 86 | pass |
| 662 | +20.2% | s9 | A_s09-12_claims.csv:38 | analysis/paper_a/method_effects_summary.csv | literal line 9 | pass |
| 663 | 15 | s9 | A_s09-12_claims.csv:39 | analysis/paper_a/method_status.csv | literal line 2 | pass |
| 664 | 16 | s9 | A_s09-12_claims.csv:39 | analysis/paper_a/method_status.csv | literal line 2 | pass |
| 665 | 15 | s9 | A_s09-12_claims.csv:39 | analysis/paper_a/method_status.csv | literal line 2 | pass |
| 666 | 36 | s9 | A_s09-12_claims.csv:42 | analysis/paper_a/method_status.csv | literal line 3 | pass |
| 667 | 32 | s9 | A_s09-12_claims.csv:40 | analysis/paper_a/method_status.csv | literal line 3 | pass |
| 668 | 36 | s9 | A_s09-12_claims.csv:42 | analysis/paper_a/method_status.csv | literal line 3 | pass |
| 669 | 35 | s9 | A_s09-12_claims.csv:41 | results/ranges_2025-mirror.csv | literal line 70 | pass |
| 670 | 36 | s9 | A_s09-12_claims.csv:42 | analysis/paper_a/method_status.csv | literal line 3 | pass |
| 671 | 3 | s9 | A_s09-12_claims.csv:42 | analysis/paper_a/method_status.csv | literal line 5 | pass |
| 672 | 36 | s9 | A_s09-12_claims.csv:42 | analysis/paper_a/method_status.csv | literal line 3 | pass |
| 673 | 4.25 | s9 | A_s09-12_claims.csv:43 | results/method_effects.csv | cell value 4,254,317 in results/method_effects.csv; rounded -425 x0.01 line 89 | pass |
| 674 | 7.13 | s9 | A_s09-12_claims.csv:43 | claims register A314 | literal line 1 | pass |
| 675 | -2.88 | s9 | A_s09-12_claims.csv:43 | results/method_effects.csv | cell value -2,878,974 in results/method_effects.csv; rounded -2878974 x1e-06 line 122 | pass |
| 676 | 4.35 | s9 | A_s09-12_claims.csv:44 | results/method_effects.csv | cell value 4,349,487 in results/method_effects.csv; rounded -4349 x0.001 line 24 | pass |
| 677 | 1.15 | s9 | A_s09-12_claims.csv:44 | results/method_effects.csv | cell value 1.15 in REG:A314; rounded -115 x0.01 line 73 | pass |
| 678 | +3.20 | s9 | A_s09-12_claims.csv:44 | results/method_effects.csv | cell value +3,196,028 in results/method_effects.csv; rounded 3196028 x1e-06 line 123 | pass |
| 679 | 53 | s10 | A_s09-12_claims.csv:47 | analysis/paper_a/regional_flips.csv | literal line 8 | pass |
| 680 | 52 | s10 | A_s09-12_claims.csv:47 | analysis/paper_a/regional_flips.csv | literal line 35 | pass |
| 681 | 3 | s10 | A_s09-12_claims.csv:47 |  | release label 2011-fixed-3 (structural) | pass |
| 682 | 95 | s10 | A_s09-12_claims.csv:49 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 683 | 48,520 | s10 | A_s09-12_claims.csv:49 | analysis/paper_a/regions_in_depth.csv | literal line 2 | pass |
| 684 | 5,401,609 | s10 | A_s09-12_claims.csv:49 | analysis/paper_a/regions_in_depth.csv | literal line 2 | pass |
| 685 | 0.491 | s10 | A_s09-12_claims.csv:50 | qa/reports/V31c_claims.md | literal line 135 | pass |
| 686 | 0.5 | s10 | A_s09-12_claims.csv:51 |  | A037 note (flag rule: land_only_ratio below 0.5) | pass |
| 687 | 0.482 | s10 | A_s09-12_claims.csv:52 | claims register A344 | literal line 1 | pass |
| 688 | 2.431 | s10 | A_s09-12_claims.csv:53 | claims register A344 | literal line 1 | pass |
| 689 | 1 | s10 | A_s09-12_claims.csv:53 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 690 | 100 | s10 | A_s09-12_claims.csv:53 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 691 | 1.604 | s10 | A_s09-12_claims.csv:53 | claims register A344 | literal line 1 | pass |
| 692 | 40% | s10 | A_s09-12_claims.csv:54 | LIT:L155 | literal line 1 | pass |
| 693 | 0.14 | s10 | A_s09-12_claims.csv:55 | analysis/paper_a/long_term_regions.csv | cell value 0.14 in REG:A149; rounded 14 x0.01 line 14 | pass |
| 694 | 1 | s10 | A_s09-12_claims.csv:53 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 695 | 100 | s10 | A_s09-12_claims.csv:53 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 696 | 508,513 | s10 | A_s09-12_claims.csv:56 | analysis/paper_a/regions_in_depth.csv | literal line 8 | pass |
| 697 | 6.5 | s10 | A_s09-12_claims.csv:57 | analysis/paper_a/movers-3.csv | literal line 55 | pass |
| 698 | 139,165 | s10 | A_s09-12_claims.csv:63 | analysis/paper_a/regions_in_depth.csv | literal line 10 | pass |
| 699 | 187,593 | s10 | A_s09-12_claims.csv:63 | analysis/paper_a/regions_in_depth.csv | literal line 10 | pass |
| 700 | 143,631 | s10 | A_s09-12_claims.csv:63 | analysis/paper_a/regional_flips-3.csv | literal line 40 | pass |
| 701 | 156,393 | s10 | A_s09-12_claims.csv:63 | analysis/paper_a/regions_in_depth.csv | literal line 10 | pass |
| 702 | 5 | s10 | A_s09-12_claims.csv:63 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 703 | 174,487 | s10 | A_s09-12_claims.csv:64 | analysis/paper_a/regions_in_depth.csv | literal line 10 | pass |
| 704 | 1 | s10 | A_s09-12_claims.csv:63 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 705 | 10 | s10 | A_s09-12_claims.csv:63 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 706 | 1.000 | s10 | A_s09-12_claims.csv:65 | analysis/paper_a/regions_in_depth.csv | cell value 1.000 in analysis/paper_a/regions_in_depth.csv; rounded 1 x1 line 1 | pass |
| 707 | 1 | s10 | A_s09-12_claims.csv:63 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 708 | 100 | s10 | A_s09-12_claims.csv:53 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 709 | 1.253 | s10 | A_s09-12_claims.csv:65 | claims register A343 | literal line 1 | pass |
| 710 | 36,954 | s10 | A_s09-12_claims.csv:67 | analysis/paper_a/regions_in_depth.csv | literal line 11 | pass |
| 711 | 58,798 | s10 | A_s09-12_claims.csv:67 | analysis/paper_a/regions_in_depth.csv | literal line 11 | pass |
| 712 | 3 | s10 | none |  | release label 2011-fixed-3 (structural) | pass |
| 713 | 5 | s10 | A_s09-12_claims.csv:64 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 714 | 95 | s10 | A_s09-12_claims.csv:49 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 715 | 1 | s10 | A_s09-12_claims.csv:56 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 716 | 100 | s10 | A_s09-12_claims.csv:56 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 717 | 5,401,609 | s10 | A_s09-12_claims.csv:71 | analysis/paper_a/regions_in_depth.csv | literal line 2 | pass |
| 718 | 46,572 | s10 | A_s09-12_claims.csv:71 | analysis/paper_a/regions_in_depth.csv | literal line 2 | pass |
| 719 | 42,815 | s10 | A_s09-12_claims.csv:71 | analysis/paper_a/regions_in_depth.csv | literal line 2 | pass |
| 720 | 48,520 | s10 | A_s09-12_claims.csv:71 | analysis/paper_a/regions_in_depth.csv | literal line 2 | pass |
| 721 | 13,986 | s10 | A_s09-12_claims.csv:71 | analysis/paper_a/regions_in_depth.csv | literal line 2 | pass |
| 722 | 6,106 | s10 | A_s09-12_claims.csv:71 | analysis/paper_a/regions_in_depth.csv | literal line 3 | pass |
| 723 | 121,808 | s10 | A_s09-12_claims.csv:72 | analysis/paper_a/regions_in_depth.csv | literal line 4 | pass |
| 724 | 905,523 | s10 | A_s09-12_claims.csv:72 | analysis/paper_a/regions_in_depth.csv | literal line 4 | pass |
| 725 | 801,061 | s10 | A_s09-12_claims.csv:72 | analysis/paper_a/regions_in_depth.csv | literal line 4 | pass |
| 726 | 991,917 | s10 | A_s09-12_claims.csv:72 | analysis/paper_a/regions_in_depth.csv | literal line 4 | pass |
| 727 | 271,935 | s10 | A_s09-12_claims.csv:72 | analysis/paper_a/regions_in_depth.csv | literal line 4 | pass |
| 728 | 151,868 | s10 | A_s09-12_claims.csv:72 | analysis/paper_a/regions_in_depth.csv | literal line 5 | pass |
| 729 | 738,895 | s10 | A_s09-12_claims.csv:73 | analysis/paper_a/regions_in_depth.csv | literal line 6 | pass |
| 730 | 1,533,929 | s10 | A_s09-12_claims.csv:73 | analysis/paper_a/regions_in_depth.csv | literal line 6 | pass |
| 731 | 1,360,739 | s10 | A_s09-12_claims.csv:73 | analysis/paper_a/regions_in_depth.csv | literal line 6 | pass |
| 732 | 1,683,767 | s10 | A_s09-12_claims.csv:73 | analysis/paper_a/regions_in_depth.csv | literal line 6 | pass |
| 733 | 460,650 | s10 | A_s09-12_claims.csv:73 | analysis/paper_a/regions_in_depth.csv | literal line 6 | pass |
| 734 | 303,975 | s10 | A_s09-12_claims.csv:73 | analysis/paper_a/regions_in_depth.csv | literal line 7 | pass |
| 735 | 69,727 | s10 | A_s09-12_claims.csv:74 | analysis/paper_a/regions_in_depth.csv | literal line 8 | pass |
| 736 | 1,080,065 | s10 | A_s09-12_claims.csv:74 | analysis/paper_a/regions_in_depth.csv | literal line 8 | pass |
| 737 | 1,032,863 | s10 | A_s09-12_claims.csv:74 | analysis/paper_a/regions_in_depth.csv | literal line 8 | pass |
| 738 | 1,113,424 | s10 | A_s09-12_claims.csv:74 | analysis/paper_a/regions_in_depth.csv | literal line 8 | pass |
| 739 | 508,513 | s10 | A_s09-12_claims.csv:74 | analysis/paper_a/regions_in_depth.csv | literal line 8 | pass |
| 740 | 506,614 | s10 | A_s09-12_claims.csv:74 | analysis/paper_a/regions_in_depth.csv | literal line 9 | pass |
| 741 | 156,393 | s10 | A_s09-12_claims.csv:75 | analysis/paper_a/regions_in_depth.csv | literal line 10 | pass |
| 742 | 187,593 | s10 | A_s09-12_claims.csv:75 | analysis/paper_a/regions_in_depth.csv | literal line 10 | pass |
| 743 | 174,487 | s10 | A_s09-12_claims.csv:75 | analysis/paper_a/regions_in_depth.csv | literal line 10 | pass |
| 744 | 196,161 | s10 | A_s09-12_claims.csv:75 | analysis/paper_a/regions_in_depth.csv | literal line 10 | pass |
| 745 | 124,822 | s10 | A_s09-12_claims.csv:75 | analysis/paper_a/regions_in_depth.csv | literal line 10 | pass |
| 746 | 58,798 | s10 | A_s09-12_claims.csv:75 | analysis/paper_a/regions_in_depth.csv | literal line 11 | pass |
| 747 | 8,049 | s10 | A_s09-12_claims.csv:76 | analysis/paper_a/regions_in_depth.csv | literal line 12 | pass |
| 748 | 28,609 | s10 | A_s09-12_claims.csv:76 | analysis/paper_a/regions_in_depth.csv | literal line 12 | pass |
| 749 | 27,016 | s10 | A_s09-12_claims.csv:76 | analysis/paper_a/regions_in_depth.csv | literal line 12 | pass |
| 750 | 30,939 | s10 | A_s09-12_claims.csv:76 | analysis/paper_a/regions_in_depth.csv | literal line 12 | pass |
| 751 | 10,108 | s10 | A_s09-12_claims.csv:76 | analysis/paper_a/regions_in_depth.csv | literal line 12 | pass |
| 752 | 8,217 | s10 | A_s09-12_claims.csv:76 | analysis/paper_a/regions_in_depth.csv | literal line 13 | pass |
| 753 | 59,255 | s10 | A_s09-12_claims.csv:77 | analysis/paper_a/regions_in_depth.csv | literal line 14 | pass |
| 754 | 384,476 | s10 | A_s09-12_claims.csv:77 | analysis/paper_a/regions_in_depth.csv | literal line 14 | pass |
| 755 | 360,755 | s10 | A_s09-12_claims.csv:77 | analysis/paper_a/regions_in_depth.csv | literal line 14 | pass |
| 756 | 402,602 | s10 | A_s09-12_claims.csv:77 | analysis/paper_a/regions_in_depth.csv | literal line 14 | pass |
| 757 | 135,844 | s10 | A_s09-12_claims.csv:77 | analysis/paper_a/regions_in_depth.csv | literal line 14 | pass |
| 758 | 139,828 | s10 | A_s09-12_claims.csv:77 | analysis/paper_a/regions_in_depth.csv | literal line 15 | pass |
| 759 | 41.5 | s11 | A_s09-12_claims.csv:78 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 760 | 15.6 | s11 | A_s09-12_claims.csv:78 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 761 | 0 | s11 | A_s09-12_claims.csv:79 | papers/A_results/DISCUSSION_MEASURES.md | literal line 12 | pass |
| 762 | 2.4% | s11 | A_s09-12_claims.csv:80 | analysis/paper_a/measures.csv | literal line 11 | pass |
| 763 | 8.7% | s11 | A_s09-12_claims.csv:82 | analysis/paper_a/measures.csv | literal line 16 | pass |
| 764 | 45.1 | s11 | A_s09-12_claims.csv:82 | analysis/paper_a/measures.csv | literal line 16 | pass |
| 765 | 17.0 | s11 | A_s09-12_claims.csv:82 | analysis/paper_a/measures.csv | literal line 16 | pass |
| 766 | 10% | s11 | A_s09-12_claims.csv:83 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 767 | 45.5 | s11 | A_s09-12_claims.csv:83 | analysis/paper_a/measures.csv | literal line 6 | pass |
| 768 | +9.7% | s11 | A_s09-12_claims.csv:83 | analysis/paper_a/measures.csv | literal line 6 | pass |
| 769 | 17.1 | s11 | A_s09-12_claims.csv:83 | analysis/paper_a/measures.csv | literal line 6 | pass |
| 770 | +9.4% | s11 | A_s09-12_claims.csv:83 | analysis/paper_a/measures.csv | literal line 6 | pass |
| 771 | 20% | s11 | A_s09-12_claims.csv:84 | analysis/paper_a/measures.csv | literal line 4 | pass |
| 772 | 49.6 | s11 | A_s09-12_claims.csv:84 | analysis/paper_a/measures.csv | literal line 7 | pass |
| 773 | +19.4% | s11 | A_s09-12_claims.csv:84 | analysis/paper_a/measures.csv | literal line 7 | pass |
| 774 | 18.6 | s11 | A_s09-12_claims.csv:84 | analysis/paper_a/measures.csv | literal line 7 | pass |
| 775 | +18.8% | s11 | A_s09-12_claims.csv:84 | analysis/paper_a/measures.csv | literal line 7 | pass |
| 776 | 0.39 | s11 | A_s09-12_claims.csv:86 | LIT:L239 | literal line 1 | pass |
| 777 | 0.72 | s11 | A_s09-12_claims.csv:86 | LIT:L239 | literal line 1 | pass |
| 778 | 32% | s11 | A_s09-12_claims.csv:87 |  | Wiedemann et al. 2015 p. 113 prints "rose 32% from 301 to 396 kg"; literature register L239 what_taken gives 301 to 396 kg only | pass (source) |
| 779 | 301 | s11 | A_s09-12_claims.csv:87 | LIT:L239 | literal line 1 | pass |
| 780 | 396 | s11 | A_s09-12_claims.csv:87 | LIT:L239 | literal line 1 | pass |
| 781 | 5% | s11 | A_s09-12_claims.csv:117 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 782 | 76.8 | s11 | A_s09-12_claims.csv:88 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 783 | +85.0% | s11 | A_s09-12_claims.csv:88 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 784 | 19.6 | s11 | A_s09-12_claims.csv:88 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 785 | +25.7% | s11 | A_s09-12_claims.csv:88 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 786 | 30% | s11 | A_s09-12_claims.csv:89 | analysis/paper_a/measures.csv | literal line 19 | pass |
| 787 | 64.6 | s11 | A_s09-12_claims.csv:89 | analysis/paper_a/measures.csv | literal line 19 | pass |
| 788 | +55.6% | s11 | A_s09-12_claims.csv:89 | analysis/paper_a/measures.csv | literal line 19 | pass |
| 789 | 18.5 | s11 | A_s09-12_claims.csv:89 | analysis/paper_a/measures.csv | literal line 19 | pass |
| 790 | +18.6% | s11 | A_s09-12_claims.csv:89 | analysis/paper_a/measures.csv | literal line 7 | pass |
| 791 | 6% | s11 | A_s09-12_claims.csv:91 | analysis/paper_a/measures.csv | literal line 12 | pass |
| 792 | 12.3 | s11 | A_s09-12_claims.csv:91 | LIT:L230 | literal line 1 | pass |
| 793 | 7.3 | s11 | none |  | A_s09-12_claims.csv:93; literature register L231 "Total 7.3 Mt food waste 2016/17" (printed p. 3) | pass |
| 794 | 7.6 | s11 | A_s09-12_claims.csv:94 | LIT:L242 | literal line 1 | pass |
| 795 | 6% | s11 | A_s09-12_claims.csv:91 | analysis/paper_a/measures.csv | literal line 12 | pass |
| 796 | 48% | s11 | A_s09-12_claims.csv:95 |  | A_s09-12_claims.csv:96; analysis/paper_a/measures.csv grain store row 48.4%; scenarios_by_region.csv line 32 48.45% | pass |
| 797 | 23.2 | s11 | A_s09-12_claims.csv:96 | analysis/paper_a/measures.csv | literal line 21 | pass |
| 798 | 64% | s11 | A_s09-12_claims.csv:96 | analysis/paper_a/measures.csv | literal line 19 | pass |
| 799 | 25.7 | s11 | A_s09-12_claims.csv:96 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 800 | 16 | s11 | A_s09-12_claims.csv:98 | analysis/paper_a/store_years.csv | literal line 2 | pass |
| 801 | 100 | s11 | A_s09-12_claims.csv:98 | analysis/paper_a/store_years.csv | cell value 100 in analysis/paper_a/store_equivalence.csv; rounded -1 x100 line 2 | pass |
| 802 | 10 | s11 | A_s09-12_claims.csv:98 | analysis/paper_a/store_years.csv | literal line 4 | pass |
| 803 | +64% | s11 | A_s09-12_claims.csv:96 | analysis/paper_a/measures.csv | literal line 19 | pass |
| 804 | +60% | s11 | A_s09-12_claims.csv:100 | results/scenarios.csv | literal line 120 | pass |
| 805 | 11.5 | s11 | A_s09-12_claims.csv:101 | claims register A318 | literal line 1 | pass |
| 806 | 100 | s11 | A_s09-12_claims.csv:103 | analysis/paper_a/measures.csv | literal line 9 | pass |
| 807 | 0.46 | s11 | A_s09-12_claims.csv:103 | analysis/paper_a/measures.csv | cell value 0.456 in results/ranges_2025-fixed.csv; rounded 45.5 x0.01 line 6 | pass |
| 808 | 0.73 | s11 | A_s09-12_claims.csv:103 | analysis/paper_a/measures.csv | cell value 0.73 in REG:A322; rounded 0.7279 x1 line 9 | pass |
| 809 | 60% | s11 | A_s09-12_claims.csv:104 |  | analysis/paper_a/measures.csv drought-proofing row 59.7% | pass |
| 810 | 24.9 | s11 | A_s09-12_claims.csv:104 | analysis/paper_a/measures.csv | literal line 9 | pass |
| 811 | 100 | s11 | A_s09-12_claims.csv:103 | analysis/paper_a/measures.csv | literal line 9 | pass |
| 812 | 1.60 | s11 | A_s09-12_claims.csv:107 | claims register A273 | literal line 1 | pass |
| 813 | 53 | s11 | A_s09-12_claims.csv:107 | analysis/paper_a/shocks_summary.csv | literal line 1 | pass |
| 814 | 52 | s11 | A_s09-12_claims.csv:108 | analysis/paper_a/regional_flips.csv | literal line 35 | pass |
| 815 | 15.5 | s11 | A_s09-12_claims.csv:109 | results/comparison_cells.csv | cell value 15.5 in REG:A274; rounded 15543 x0.001 line 58 | pass |
| 816 | 41.5 | s11 | A_s09-12_claims.csv:109 | analysis/paper_a/shocks_summary.csv | literal line 8 | pass |
| 817 | 26.0 | s11 | A_s09-12_claims.csv:109 | analysis/paper_a/shocks_summary.csv | literal line 8 | pass |
| 818 | 9.6 | s11 | A_s09-12_claims.csv:110 | claims register A274 | literal line 1 | pass |
| 819 | 4.66 | s11 | A_s09-12_claims.csv:112 | analysis/method_tests_2025/foran_poldy_balance.csv | literal line 12 | pass |
| 820 | 2.96 | s11 | A_s09-12_claims.csv:112 | claims register A315 | literal line 1 | pass |
| 821 | 57% | s11 | A_s09-12_claims.csv:112 | claims register A315 | literal line 1 | pass |
| 822 | 1.50 | s11 | A_s09-12_claims.csv:113 | results/comparison_cells.csv | cell value 1.50 in REG:A006; rounded 1502318 x1e-06 line 30 | pass |
| 823 | 93% | s11 | A_s09-12_claims.csv:114 | LIT:L224 | literal line 1 | pass |
| 824 | 5% | s11 | A_s09-12_claims.csv:117 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 825 | 11 | s12 | A_s09-12_claims.csv:122 | LIT:L180 | literal line 1 | pass |
| 826 | 28% | s12 | A_s09-12_claims.csv:122 | LIT:L180 | literal line 1 | pass |
| 827 | 100 | s12 | A_s09-12_claims.csv:122 | LIT:L180 | literal line 1 | pass |
| 828 | 33% | s12 | A_s09-12_claims.csv:123 | analysis/scale_curve_2025/diet_scale.csv | literal line 11 | pass |
| 829 | 45% | s12 | A_s09-12_claims.csv:123 | analysis/scale_curve_2025/diet_scale.csv | literal line 21 | pass |
| 830 | +62% | s12 | A_s09-12_claims.csv:124 | qa/reports/V31d_claims.md | literal line 119 | pass |
| 831 | 15.0% | s12 | A_s09-12_claims.csv:125 | LIT:L183 | literal line 1 | pass |
| 832 | 25% | s12 | A_s09-12_claims.csv:125 | LIT:L183 | literal line 1 | pass |
| 833 | 5% | s12 | A_s09-12_claims.csv:126 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 834 | 2.4% | s12 | A_s09-12_claims.csv:126 | analysis/paper_a/measures.csv | literal line 11 | pass |
| 835 | 20% | s12 | A_s09-12_claims.csv:127 | LIT:L187 | literal line 1 | pass |
| 836 | 2 | s12 | A_s09-12_claims.csv:127 | LIT:L187 | literal line 1 | pass |
| 837 | 1 | s12 | A_s09-12_claims.csv:130 | LIT:L176 | literal line 1 | pass |
| 838 | 41.5 | s12 | A_s09-12_claims.csv:129 | analysis/paper_a/long_term_levers.csv | cell value 41.5 in REG:A323; rounded 41503537 x1e-06 line 135 | pass |
| 839 | 9.7 | s12 | A_s09-12_claims.csv:129 |  | analysis/paper_a/long_term_levers.csv 2025-fixed zone 1 lever "biofuel (0.0023 to 1)" alone 9717436 | pass |
| 840 | 61 | s12 | A_s09-12_claims.csv:130 | LIT:L176 | literal line 1 | pass |
| 841 | 90 | s12 | A_s09-12_claims.csv:130 | LIT:L176 | literal line 1 | pass |
| 842 | 33.3 | s12 | A_s09-12_claims.csv:132 | results/comparison_cells.csv | cell value 33.3 in REG:A001; rounded 33307814 x1e-06 line 2 | pass |
| 843 | 41.5 | s12 | A_s09-12_claims.csv:132 | results/comparison_cells.csv | cell value 41.5 in REG:A003; rounded 41503537 x1e-06 line 2 | pass |
| 844 | 5.6 | s12 | A_s09-12_claims.csv:133 | results/ranges_2025-mirror.csv | cell value 5.59 in qa/reports/B111_decomposition_orders.md; rounded 0.056 x100 line 121 | pass |
| 845 | 2.4 | s12 | A_s09-12_claims.csv:134 | results/ranges_2025-mirror.csv | cell value +2,438,688 in qa/reports/B111_decomposition_orders.md; rounded 2409157 x1e-06 line 5 | pass |
| 846 | 0.2 | s12 | A_s09-12_claims.csv:135 | results/ranges_2025-mirror.csv | cell value +162,372 in qa/reports/B111_decomposition_orders.md; rounded 25 x0.01 line 1 | pass |
| 847 | 0.670 | s12 | A_s09-12_claims.csv:136 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 848 | 0.665 | s12 | A_s09-12_claims.csv:136 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 2 | pass |
| 849 | 1.454 | s12 | A_s09-12_claims.csv:136 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 850 | 1.767 | s12 | A_s09-12_claims.csv:136 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 3 | pass |
| 851 | 100 | s12 | A_s09-12_claims.csv:137 | analysis/paper_a/long_term_regions.csv | cell value 100 in REG:A010; rounded 1 x100 line 2 | pass |
| 852 | 69% | s12 | A_s09-12_claims.csv:137 |  | analysis/paper_a/long_term_regions.csv line 2 ratio 0.688 | pass |
| 853 | 57% | s12 | A_s09-12_claims.csv:137 | analysis/paper_a/long_term_regions.csv | literal line 52 | pass |
| 854 | 30.8 | s12 | A_s09-12_claims.csv:138 | analysis/paper_a/shocks_summary.csv | literal line 10 | pass |
| 855 | 27.6 | s12 | A_s09-12_claims.csv:138 | analysis/paper_a/shocks_summary.csv | literal line 8 | pass |
| 856 | 1.05 | s12 | A_s09-12_claims.csv:139 | qa/reports/B112_shock_ranges.md | literal line 7 | pass |
| 857 | 1 | s12 | A_s09-12_claims.csv:132 | results/comparison_cells.csv | literal line 2 | pass |
| 858 | 20 | s12 | A_s09-12_claims.csv:138 | analysis/paper_a/shocks_summary.csv | literal line 5 | pass |
| 859 | 5.8% | s12 | A_s09-12_claims.csv:140 | analysis/method_tests_2025/fearnside_failure_curve.csv | literal line 3 | pass |
| 860 | 1 | s12 | A_s09-12_claims.csv:132 | results/comparison_cells.csv | literal line 2 | pass |
| 861 | 17 | s12 | A_s09-12_claims.csv:140 | analysis/method_tests_2025/fearnside_failure_curve.csv | literal line 3 | pass |
| 862 | 37% | s12 | A_s09-12_claims.csv:133 | results/ranges_2025-mirror.csv | literal line 74 | pass |
| 863 | 8,000 | Supp front | supplementary_claims.csv:5 | qa/DECISIONS.md | literal line 121 | pass |
| 864 | 92 | Supp front | supplementary_claims.csv:5 | qa/DECISIONS.md | literal line 116 | pass |
| 865 | 3 | Supp front | supplementary_claims.csv:6 | results/2011-fixed-3.csv | literal line 2 | pass |
| 866 | 1 | Supp front | supplementary_claims.csv:6 | results/2011-fixed-3.csv | literal line 2 | pass |
| 867 | 1 | Supp front | supplementary_claims.csv:7 | results/2011-fixed-3.csv | literal line 2 | pass |
| 868 | 100 | Supp front | supplementary_claims.csv:7 | results/2011-fixed-3.csv | literal line 3 | pass |
| 869 | 1 | Supp front | supplementary_claims.csv:7 | results/2011-fixed-3.csv | literal line 2 | pass |
| 870 | 100 | Supp front | supplementary_claims.csv:7 | results/2011-fixed-3.csv | literal line 3 | pass |
| 871 | 0.13 | Supp front | supplementary_claims.csv:8 | analysis/paper_a/long_term_levers.csv | literal line 5 | pass |
| 872 | 0.075 | Supp front | supplementary_claims.csv:8 | analysis/paper_a/long_term_levers.csv | literal line 5 | pass |
| 873 | 0.12 | Supp front | supplementary_claims.csv:8 | analysis/paper_a/long_term_levers.csv | literal line 9 | pass |
| 874 | 0.075 | Supp front | supplementary_claims.csv:8 | analysis/paper_a/long_term_levers.csv | literal line 5 | pass |
| 875 | 0.64 | Supp front | supplementary_claims.csv:9 | analysis/paper_a/long_term_levers.csv | literal line 6 | pass |
| 876 | 0.5 | Supp front | supplementary_claims.csv:9 | analysis/paper_a/long_term_levers.csv | literal line 6 | pass |
| 877 | 0.578 | Supp front | supplementary_claims.csv:9 | analysis/paper_a/long_term_levers.csv | literal line 139 | pass |
| 878 | 0.5 | Supp front | supplementary_claims.csv:9 | analysis/paper_a/long_term_levers.csv | literal line 6 | pass |
| 879 | 0.12 | Supp front | supplementary_claims.csv:10 | analysis/paper_a/long_term_levers.csv | literal line 9 | pass |
| 880 | 0 | Supp front | supplementary_claims.csv:10 | analysis/paper_a/long_term_levers.csv | literal line 5 | pass |
| 881 | 0.12 | Supp front | supplementary_claims.csv:10 | analysis/paper_a/long_term_levers.csv | literal line 9 | pass |
| 882 | 0 | Supp front | supplementary_claims.csv:10 | analysis/paper_a/long_term_levers.csv | literal line 5 | pass |
| 883 | 0 | Supp front | supplementary_claims.csv:11 |  | results/2011-fixed-3.csv and results/2025-fixed.csv zone 1, column recycling | pass |
| 884 | 1 | Supp front | supplementary_claims.csv:11 |  | results/2011-fixed-3.csv and results/2025-fixed.csv zone 1, column recycling | pass |
| 885 | 0 | Supp front | supplementary_claims.csv:11 |  | results/2011-fixed-3.csv and results/2025-fixed.csv zone 1, column recycling | pass |
| 886 | 1 | Supp front | supplementary_claims.csv:11 |  | results/2011-fixed-3.csv and results/2025-fixed.csv zone 1, column recycling | pass |
| 887 | 0.02 | Supp front | supplementary_claims.csv:12 | analysis/paper_a/long_term_levers.csv | literal line 10 | pass |
| 888 | 1 | Supp front | supplementary_claims.csv:12 | analysis/paper_a/long_term_levers.csv | literal line 2 | pass |
| 889 | 0.07 | Supp front | supplementary_claims.csv:12 | analysis/paper_a/long_term_levers.csv | literal line 69 | pass |
| 890 | 1 | Supp front | supplementary_claims.csv:12 | analysis/paper_a/long_term_levers.csv | literal line 2 | pass |
| 891 | 2,520 | Supp front | supplementary_claims.csv:13 | analysis/paper_a/long_term_levers.csv | literal line 11 | pass |
| 892 | 253 | Supp front | supplementary_claims.csv:13 | analysis/paper_a/long_term_levers.csv | literal line 11 | pass |
| 893 | 2,360 | Supp front | supplementary_claims.csv:13 | analysis/paper_a/long_term_levers.csv | literal line 144 | pass |
| 894 | 210 | Supp front | supplementary_claims.csv:13 | analysis/paper_a/long_term_levers.csv | literal line 144 | pass |
| 895 | 0.005 | Supp front | supplementary_claims.csv:14 | analysis/paper_a/long_term_levers.csv | literal line 12 | pass |
| 896 | 1 | Supp front | supplementary_claims.csv:14 | analysis/paper_a/long_term_levers.csv | literal line 2 | pass |
| 897 | 0.0023 | Supp front | supplementary_claims.csv:14 | analysis/paper_a/long_term_levers.csv | literal line 145 | pass |
| 898 | 1 | Supp front | supplementary_claims.csv:14 | analysis/paper_a/long_term_levers.csv | literal line 2 | pass |
| 899 | 170 | Supp S1 | supplementary_claims.csv:15 | analysis/comparison_2025/movers.csv | cell value 170 in analysis/comparison_2025/movers.csv; rounded 170101 x0.001 line 11 | pass |
| 900 | 6 | Supp S1 | supplementary_claims.csv:15 | analysis/comparison_2025/movers.csv | literal line 10 | pass |
| 901 | 1.72 | Supp S1 | supplementary_claims.csv:16 | analysis/paper_a/regional_flips-3.csv | cell value 1,716,318 in analysis/paper_a/regional_flips-3.csv; rounded 1716318 x1e-06 line 11 | pass |
| 902 | 2.27 | Supp S1 | supplementary_claims.csv:16 | analysis/paper_a/regional_flips-3.csv | cell value 2,269,447 in analysis/paper_a/regional_flips-3.csv; rounded 2269447 x1e-06 line 11 | pass |
| 903 | 356,807 | Supp S1 | supplementary_claims.csv:19 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 8 | pass |
| 904 | 1,333,553 | Supp S1 | supplementary_claims.csv:19 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 8 | pass |
| 905 | 1,798,009 | Supp S1 | supplementary_claims.csv:19 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 8 | pass |
| 906 | 21% | Supp S1 | supplementary_claims.csv:21 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 11 | pass |
| 907 | 97,458 | Supp S1 | supplementary_claims.csv:22 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 18 | pass |
| 908 | -167,976 | Supp S1 | supplementary_claims.csv:23 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 110 | pass |
| 909 | 170,101 | Supp S1 | supplementary_claims.csv:23 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 110 | pass |
| 910 | -1,120,638 | Supp S1 | supplementary_claims.csv:24 | qa/reports/B111_decomposition_orders.md | literal line 78 | pass |
| 911 | 62,789 | Supp S1 | supplementary_claims.csv:25 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 66 | pass |
| 912 | 38,290 | Supp S1 | supplementary_claims.csv:25 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 66 | pass |
| 913 | 34,818 | Supp S1 | supplementary_claims.csv:26 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 67 | pass |
| 914 | 658 | Supp S1 | supplementary_claims.csv:26 | analysis/comparison_2025/capacity_by_cause_corrected.csv | literal line 67 | pass |
| 915 | 53 | Supp S1 | supplementary_claims.csv:29 | analysis/comparison_2025/movers.csv | literal line 8 | pass |
| 916 | 26 | Supp S1 | supplementary_claims.csv:27 | results/ranges_2025-mirror.csv | literal line 52 | pass |
| 917 | 25 | Supp S1 | supplementary_claims.csv:27 | results/ranges_2025-mirror.csv | literal line 1 | pass |
| 918 | 19 | Supp S1 | supplementary_claims.csv:28 | results/ranges_2025-mirror.csv | literal line 38 | pass |
| 919 | 17 | Supp S1 | supplementary_claims.csv:28 | results/ranges_2025-mirror.csv | literal line 34 | pass |
| 920 | 16 | Supp S1 | supplementary_claims.csv:28 | results/ranges_2025-mirror.csv | literal line 32 | pass |
| 921 | 42 | Supp S1 | supplementary_claims.csv:30 | results/ranges_2025-mirror.csv | literal line 84 | pass |
| 922 | 31 | Supp S1 | supplementary_claims.csv:30 | results/ranges_2025-mirror.csv | literal line 62 | pass |
| 923 | 7 | Supp S1 | supplementary_claims.csv:28 | results/ranges_2025-mirror.csv | literal line 14 | pass |
| 924 | 2 | Supp S1 | supplementary_claims.csv:27 | results/ranges_2025-mirror.csv | literal line 4 | pass |
| 925 | 3 | Supp S1 | supplementary_claims.csv:29 | analysis/comparison_2025/movers.csv | literal line 5 | pass |
| 926 | 1 | Supp S1 | supplementary_claims.csv:28 | results/ranges_2025-mirror.csv | literal line 2 | pass |
| 927 | 24,368 | Supp S1 | supplementary_claims.csv:33 | qa/reports/B111_decomposition_orders.md | literal line 11 | pass |
| 928 | 15,309 | Supp S1 | supplementary_claims.csv:33 | qa/reports/B111_decomposition_orders.md | literal line 11 | pass |
| 929 | 1.592 | Supp S1 | supplementary_claims.csv:33 | qa/reports/B111_decomposition_orders.md | literal line 11 | pass |
| 930 | 1,594,996 | Supp S1 | supplementary_claims.csv:34 | qa/reports/B111_decomposition_orders.md | literal line 12 | pass |
| 931 | 2,537,931 | Supp S1 | supplementary_claims.csv:35 | qa/reports/B111_decomposition_orders.md | literal line 12 | pass |
| 932 | 1.591 | Supp S1 | supplementary_claims.csv:35 | results/ranges_2025-mirror.csv | cell value 1.591 in qa/reports/B111_decomposition_orders.md; rounded 1591288 x1e-06 line 22 | pass |
| 933 | 32.75 | Supp S1 | supplementary_claims.csv:36 | qa/reports/B111_decomposition_orders.md | literal line 13 | pass |
| 934 | 67.54 | Supp S1 | supplementary_claims.csv:36 | qa/reports/B111_decomposition_orders.md | literal line 13 | pass |
| 935 | 2.062 | Supp S1 | supplementary_claims.csv:36 | qa/reports/B111_decomposition_orders.md | literal line 13 | pass |
| 936 | 1.591 | Supp S1 | supplementary_claims.csv:35 | results/ranges_2025-mirror.csv | cell value 1.591 in qa/reports/B111_decomposition_orders.md; rounded 1591288 x1e-06 line 22 | pass |
| 937 | 1.296 | Supp S1 | supplementary_claims.csv:36 | qa/reports/B111_decomposition_orders.md | literal line 13 | pass |
| 938 | 1.296 | Supp S1 | supplementary_claims.csv:36 | qa/reports/B111_decomposition_orders.md | literal line 13 | pass |
| 939 | 134,628 | Supp S1 | supplementary_claims.csv:38 | qa/reports/B111_decomposition_orders.md | literal line 15 | pass |
| 940 | 125,905 | Supp S1 | supplementary_claims.csv:38 | qa/reports/B111_decomposition_orders.md | literal line 15 | pass |
| 941 | -8,723 | Supp S1 | supplementary_claims.csv:38 | qa/reports/B111_decomposition_orders.md | literal line 15 | pass |
| 942 | -68,404 | Supp S1 | supplementary_claims.csv:39 | qa/reports/B111_decomposition_orders.md | literal line 15 | pass |
| 943 | +52,121 | Supp S1 | supplementary_claims.csv:39 | qa/reports/B111_decomposition_orders.md | literal line 15 | pass |
| 944 | -16,283 | Supp S1 | supplementary_claims.csv:39 | qa/reports/B111_decomposition_orders.md | literal line 15 | pass |
| 945 | 1.097 | Supp S1 | supplementary_claims.csv:40 | qa/reports/B111_decomposition_orders.md | literal line 16 | pass |
| 946 | 3,639,794 | Supp S1 | supplementary_claims.csv:40 | qa/reports/B111_decomposition_orders.md | literal line 16 | pass |
| 947 | 3,318,689 | Supp S1 | supplementary_claims.csv:40 | qa/reports/B111_decomposition_orders.md | literal line 16 | pass |
| 948 | 1.104 | Supp S1 | supplementary_claims.csv:40 | qa/reports/B111_decomposition_orders.md | literal line 16 | pass |
| 949 | 17.6% | Supp S2 | supplementary_claims.csv:42 | claims register A115 | literal line 1 | pass |
| 950 | 25.3% | Supp S2 | supplementary_claims.csv:42 | claims register A115 | literal line 1 | pass |
| 951 | 1.2% | Supp S2 | supplementary_claims.csv:43 | claims register A115 | literal line 1 | pass |
| 952 | 4.8% | Supp S2 | supplementary_claims.csv:43 | claims register A115 | literal line 1 | pass |
| 953 | 2.0% | Supp S2 | supplementary_claims.csv:43 | claims register A115 | literal line 1 | pass |
| 954 | 5.1% | Supp S2 | supplementary_claims.csv:43 | claims register A115 | literal line 1 | pass |
| 955 | 406 | Supp S2 | supplementary_claims.csv:45 | claims register A116 | literal line 1 | pass |
| 956 | 1.7 | Supp S2 | supplementary_claims.csv:45 | claims register A116 | literal line 1 | pass |
| 957 | 41 | Supp S2 | supplementary_claims.csv:46 | claims register A116 | literal line 1 | pass |
| 958 | 132 | Supp S2 | supplementary_claims.csv:46 | claims register A116 | literal line 1 | pass |
| 959 | 646,000 | Supp S2 | supplementary_claims.csv:47 | claims register A117 | literal line 1 | pass |
| 960 | 937 | Supp S2 | supplementary_claims.csv:47 | claims register A117 | literal line 1 | pass |
| 961 | 241 | Supp S2 | supplementary_claims.csv:47 | claims register A117 | literal line 1 | pass |
| 962 | 511 | Supp S2 | supplementary_claims.csv:48 | claims register A117 | literal line 1 | pass |
| 963 | 1.5 | Supp S2 | supplementary_claims.csv:48 | claims register A117 | literal line 1 | pass |
| 964 | 1,000 | Supp S2 | supplementary_claims.csv:49 | claims register A118 | literal line 1 | pass |
| 965 | 2% | Supp S2 | supplementary_claims.csv:49 | claims register A118 | literal line 1 | pass |
| 966 | 71% | Supp S2 | supplementary_claims.csv:49 | claims register A118 | literal line 1 | pass |
| 967 | 8 | Supp S2 | supplementary_claims.csv:49 | claims register A118 | literal line 1 | pass |
| 968 | 72% | Supp S2 | supplementary_claims.csv:49 | claims register A118 | literal line 1 | pass |
| 969 | 18 | Supp S2 | supplementary_claims.csv:49 | claims register A118 | literal line 1 | pass |
| 970 | 51% | Supp S2 | supplementary_claims.csv:49 | claims register A118 | literal line 1 | pass |
| 971 | 3 | Supp S2 | supplementary_claims.csv:46 |  | analysis/scale_curve_2025/README.md line 38 ("in the SA4s three units hold 51%") | pass |
| 972 | 1.96 | Supp S2 | supplementary_claims.csv:50 | claims register A119 | literal line 1 | pass |
| 973 | 3.67 | Supp S2 | supplementary_claims.csv:50 | claims register A119 | literal line 1 | pass |
| 974 | 4.50 | Supp S2 | supplementary_claims.csv:50 | claims register A119 | literal line 1 | pass |
| 975 | 0.5 | Supp S2 | supplementary_claims.csv:51 | claims register A121 | literal line 1 | pass |
| 976 | 0.1 | Supp S2 | supplementary_claims.csv:51 | claims register A121 | literal line 1 | pass |
| 977 | 0.01 | Supp S2 | supplementary_claims.csv:51 | claims register A121 | literal line 1 | pass |
| 978 | 100.0% | Supp S2 | supplementary_claims.csv:51 | claims register A121 | literal line 1 | pass |
| 979 | 53 | Supp S2 | supplementary_claims.csv:53 | claims register A122 | literal line 1 | pass |
| 980 | 68 | Supp S2 | supplementary_claims.csv:53 | claims register A122 | literal line 1 | pass |
| 981 | 81% | Supp S2 | supplementary_claims.csv:53 | claims register A122 | literal line 1 | pass |
| 982 | 33% | Supp S2 | supplementary_claims.csv:53 | claims register A123 | literal line 1 | pass |
| 983 | 53 | Supp S2 | supplementary_claims.csv:53 | claims register A122 | literal line 1 | pass |
| 984 | 52 | Supp S2 | supplementary_claims.csv:53 |  | A048 | pass |
| 985 | 54% | Supp S2 | supplementary_claims.csv:55 | claims register A123 | literal line 1 | pass |
| 986 | 56 | Supp S2 | supplementary_claims.csv:55 | claims register A122 | literal line 1 | pass |
| 987 | 69% | Supp S2 | supplementary_claims.csv:55 | claims register A122 | literal line 1 | pass |
| 988 | 35% | Supp S2 | supplementary_claims.csv:55 | claims register A123 | literal line 1 | pass |
| 989 | 34 | Supp S2 | supplementary_claims.csv:55 | claims register A122 | literal line 1 | pass |
| 990 | 44% | Supp S2 | supplementary_claims.csv:55 | claims register A122 | literal line 1 | pass |
| 991 | 53 | Supp S2 | supplementary_claims.csv:53 | claims register A122 | literal line 1 | pass |
| 992 | 650,000 | Supp S2 | supplementary_claims.csv:56 | analysis/regionalise_2025/summary.csv | literal line 2 | pass |
| 993 | 1 | Supp S2 | supplementary_claims.csv:62 | results/scale_curve.csv | literal line 2 | pass |
| 994 | 100% | Supp S2 | supplementary_claims.csv:62 | results/scale_curve.csv | cell value 1.000 in results/scale_curve.csv; rounded 1 x100 line 2 | pass |
| 995 | 100% | Supp S2 | supplementary_claims.csv:62 | results/scale_curve.csv | cell value 1.000 in results/scale_curve.csv; rounded 1 x100 line 2 | pass |
| 996 | 100% | Supp S2 | supplementary_claims.csv:62 | results/scale_curve.csv | cell value 1.000 in results/scale_curve.csv; rounded 1 x100 line 2 | pass |
| 997 | 100% | Supp S2 | supplementary_claims.csv:62 | results/scale_curve.csv | cell value 1.000 in results/scale_curve.csv; rounded 1 x100 line 2 | pass |
| 998 | 100% | Supp S2 | supplementary_claims.csv:62 | results/scale_curve.csv | cell value 1.000 in results/scale_curve.csv; rounded 1 x100 line 2 | pass |
| 999 | 100% | Supp S2 | supplementary_claims.csv:62 | results/scale_curve.csv | cell value 1.000 in results/scale_curve.csv; rounded 1 x100 line 2 | pass |
| 1000 | 100% | Supp S2 | supplementary_claims.csv:62 | results/scale_curve.csv | cell value 1.000 in results/scale_curve.csv; rounded 1 x100 line 2 | pass |
| 1001 | 100% | Supp S2 | supplementary_claims.csv:62 | results/scale_curve.csv | cell value 1.000 in results/scale_curve.csv; rounded 1 x100 line 2 | pass |
| 1002 | 7 | Supp S2 | supplementary_claims.csv:63 | results/scale_curve.csv | literal line 3 | pass |
| 1003 | 77% | Supp S2 | supplementary_claims.csv:63 | results/scale_curve.csv | cell value 0.771 in results/scale_curve.csv; rounded 0.771 x100 line 31 | pass |
| 1004 | 44% | Supp S2 | supplementary_claims.csv:63 | results/scale_curve.csv | cell value 0.436 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 1005 | 75% | Supp S2 | supplementary_claims.csv:63 | results/scale_curve.csv | cell value 0.754 in results/scale_curve.csv; rounded 0.754 x100 line 115 | pass |
| 1006 | 49% | Supp S2 | supplementary_claims.csv:63 | results/scale_curve.csv | cell value 0.491 in results/scale_curve.csv; rounded 0.491 x100 line 8 | pass |
| 1007 | 77% | Supp S2 | supplementary_claims.csv:63 | results/scale_curve.csv | cell value 0.771 in results/scale_curve.csv; rounded 0.771 x100 line 31 | pass |
| 1008 | 44% | Supp S2 | supplementary_claims.csv:63 | results/scale_curve.csv | cell value 0.436 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 1009 | 75% | Supp S2 | supplementary_claims.csv:63 | results/scale_curve.csv | cell value 0.754 in results/scale_curve.csv; rounded 0.754 x100 line 115 | pass |
| 1010 | 49% | Supp S2 | supplementary_claims.csv:63 | results/scale_curve.csv | cell value 0.491 in results/scale_curve.csv; rounded 0.491 x100 line 8 | pass |
| 1011 | 53 | Supp S2 | supplementary_claims.csv:64 | results/scale_curve.csv | literal line 4 | pass |
| 1012 | 44% | Supp S2 | supplementary_claims.csv:64 | results/scale_curve.csv | cell value 0.442 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 1013 | 20% | Supp S2 | supplementary_claims.csv:64 | results/scale_curve.csv | cell value 0.197 in results/scale_curve.csv; rounded 2011 x0.01 line 2 | pass |
| 1014 | 44% | Supp S2 | supplementary_claims.csv:64 | results/scale_curve.csv | cell value 0.442 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 1015 | 23% | Supp S2 | supplementary_claims.csv:64 | results/scale_curve.csv | literal line 32 | pass |
| 1016 | 63% | Supp S2 | supplementary_claims.csv:64 | results/scale_curve.csv | literal line 90 | pass |
| 1017 | 33% | Supp S2 | supplementary_claims.csv:64 | results/scale_curve.csv | cell value 0.333 in results/scale_curve.csv; rounded 0.334 x100 line 22 | pass |
| 1018 | 63% | Supp S2 | supplementary_claims.csv:64 | results/scale_curve.csv | literal line 90 | pass |
| 1019 | 38% | Supp S2 | supplementary_claims.csv:64 | results/scale_curve.csv | literal line 74 | pass |
| 1020 | 89 | Supp S2 | supplementary_claims.csv:65 | results/scale_curve.csv | literal line 6 | pass |
| 1021 | 60% | Supp S2 | supplementary_claims.csv:65 | results/scale_curve.csv | cell value 0.597 in results/scale_curve.csv; rounded 0.597 x100 line 17 | pass |
| 1022 | 32% | Supp S2 | supplementary_claims.csv:65 | results/scale_curve.csv | literal line 130 | pass |
| 1023 | 58% | Supp S2 | supplementary_claims.csv:65 | results/scale_curve.csv | cell value 0.581 in results/scale_curve.csv; rounded 0.579 x100 line 88 | pass |
| 1024 | 35% | Supp S2 | supplementary_claims.csv:65 | results/scale_curve.csv | cell value 0.349 in results/scale_curve.csv; rounded 0.349 x100 line 49 | pass |
| 1025 | 82% | Supp S2 | supplementary_claims.csv:65 | results/scale_curve.csv | cell value 0.823 in results/scale_curve.csv; rounded 0.823 x100 line 34 | pass |
| 1026 | 43% | Supp S2 | supplementary_claims.csv:65 | results/scale_curve.csv | cell value 0.426 in results/scale_curve.csv; rounded 0.430 x100 line 18 | pass |
| 1027 | 80% | Supp S2 | supplementary_claims.csv:65 | results/scale_curve.csv | literal line 76 | pass |
| 1028 | 52% | Supp S2 | supplementary_claims.csv:65 | results/scale_curve.csv | cell value 0.519 in results/scale_curve.csv; rounded 0.519 x100 line 132 | pass |
| 1029 | 336 | Supp S2 | supplementary_claims.csv:66 | results/scale_curve.csv | literal line 7 | pass |
| 1030 | 46% | Supp S2 | supplementary_claims.csv:66 | results/scale_curve.csv | cell value 0.463 in results/scale_curve.csv; rounded 0.462 x100 line 20 | pass |
| 1031 | 23% | Supp S2 | supplementary_claims.csv:66 | results/scale_curve.csv | literal line 32 | pass |
| 1032 | 44% | Supp S2 | supplementary_claims.csv:66 | results/scale_curve.csv | cell value 0.439 in results/scale_curve.csv; rounded 0.442 x100 line 39 | pass |
| 1033 | 24% | Supp S2 | supplementary_claims.csv:66 | results/scale_curve.csv | literal line 151 | pass |
| 1034 | 64% | Supp S2 | supplementary_claims.csv:66 | results/scale_curve.csv | literal line 34 | pass |
| 1035 | 35% | Supp S2 | supplementary_claims.csv:66 | results/scale_curve.csv | cell value 0.349 in results/scale_curve.csv; rounded 0.349 x100 line 49 | pass |
| 1036 | 64% | Supp S2 | supplementary_claims.csv:66 | results/scale_curve.csv | literal line 34 | pass |
| 1037 | 40% | Supp S2 | supplementary_claims.csv:66 | results/scale_curve.csv | literal line 25 | pass |
| 1038 | 2,450 | Supp S2 | supplementary_claims.csv:67 | results/scale_curve.csv | literal line 8 | pass |
| 1039 | 40% | Supp S2 | supplementary_claims.csv:67 | results/scale_curve.csv | literal line 25 | pass |
| 1040 | 18% | Supp S2 | supplementary_claims.csv:67 | results/scale_curve.csv | cell value 0.180 in results/scale_curve.csv; rounded 18298878 x1e-06 line 8 | pass |
| 1041 | 37% | Supp S2 | supplementary_claims.csv:67 | results/scale_curve.csv | literal line 165 | pass |
| 1042 | 20% | Supp S2 | supplementary_claims.csv:67 | results/scale_curve.csv | cell value 0.198 in results/scale_curve.csv; rounded 2011 x0.01 line 2 | pass |
| 1043 | 54% | Supp S2 | supplementary_claims.csv:67 | results/scale_curve.csv | cell value 0.542 in results/scale_curve.csv; rounded 0.542 x100 line 36 | pass |
| 1044 | 28% | Supp S2 | supplementary_claims.csv:67 | results/scale_curve.csv | literal line 39 | pass |
| 1045 | 54% | Supp S2 | supplementary_claims.csv:67 | results/scale_curve.csv | cell value 0.542 in results/scale_curve.csv; rounded 0.542 x100 line 36 | pass |
| 1046 | 32% | Supp S2 | supplementary_claims.csv:67 | results/scale_curve.csv | literal line 130 | pass |
| 1047 | 41.5 | Supp S3 | supplementary_claims.csv:68 | analysis/paper_a/scenarios_by_region.csv | literal line 25 | pass |
| 1048 | 15.6 | Supp S3 | supplementary_claims.csv:68 | analysis/paper_a/scenarios_by_region.csv | literal line 24 | pass |
| 1049 | 2% | Supp S3 | supplementary_claims.csv:69 | analysis/paper_a/scenarios_by_region.csv | literal line 12 | pass |
| 1050 | 340 | Supp S3 | supplementary_claims.csv:70 | analysis/paper_a/scenarios_by_region.csv | literal line 6 | pass |
| 1051 | 1.8% | Supp S3 | supplementary_claims.csv:70 |  | scenarios_by_region.csv line 28 -1.83% | pass |
| 1052 | 18.8% | Supp S3 | supplementary_claims.csv:70 | analysis/paper_a/scenarios_by_region.csv | cell value 18.8 in REG:A226; rounded -18.75 x1 line 6 | pass |
| 1053 | 1 | Supp S3 | supplementary_claims.csv:71 | analysis/paper_a/scenarios_by_region.csv | literal line 6 | pass |
| 1054 | 2 | Supp S3 | supplementary_claims.csv:71 | analysis/paper_a/scenarios_by_region.csv | literal line 12 | pass |
| 1055 | 156 | Supp S3 | supplementary_claims.csv:71 | analysis/paper_a/scenarios_by_region.csv | literal line 8 | pass |
| 1056 | 41.5 | Supp S3 | supplementary_claims.csv:72 | analysis/paper_a/scenarios_by_region.csv | literal line 25 | pass |
| 1057 | 15.6 | Supp S3 | supplementary_claims.csv:72 | analysis/paper_a/scenarios_by_region.csv | literal line 24 | pass |
| 1058 | 12% | Supp S3 | supplementary_claims.csv:73 | analysis/paper_a/scenarios_by_region.csv | literal line 2 | pass |
| 1059 | -0.09% | Supp S3 | supplementary_claims.csv:73 | analysis/paper_a/scenarios_by_region.csv | literal line 25 | pass |
| 1060 | -0.28% | Supp S3 | supplementary_claims.csv:73 | analysis/paper_a/scenarios_by_region.csv | literal line 24 | pass |
| 1061 | 24% | Supp S3 | supplementary_claims.csv:74 | analysis/paper_a/scenarios_by_region.csv | literal line 4 | pass |
| 1062 | -0.2% | Supp S3 | supplementary_claims.csv:74 | analysis/paper_a/scenarios_by_region.csv | literal line 27 | pass |
| 1063 | -0.65% | Supp S3 | supplementary_claims.csv:74 | analysis/paper_a/scenarios_by_region.csv | literal line 26 | pass |
| 1064 | 6% | Supp S3 | supplementary_claims.csv:75 | analysis/paper_a/scenarios_by_region.csv | literal line 22 | pass |
| 1065 | +16.4% | Supp S3 | supplementary_claims.csv:75 | analysis/paper_a/scenarios_by_region.csv | literal line 45 | pass |
| 1066 | -8.15% | Supp S3 | supplementary_claims.csv:75 | analysis/paper_a/scenarios_by_region.csv | literal line 44 | pass |
| 1067 | +33.21% | Supp S3 | supplementary_claims.csv:76 | analysis/paper_a/scenarios_by_region.csv | literal line 43 | pass |
| 1068 | 0% | Supp S3 | supplementary_claims.csv:76 | analysis/paper_a/scenarios_by_region.csv | literal line 2 | pass |
| 1069 | 0% | Supp S3 | supplementary_claims.csv:77 | analysis/paper_a/scenarios_by_region.csv | literal line 2 | pass |
| 1070 | -1.21% | Supp S3 | supplementary_claims.csv:77 | analysis/paper_a/scenarios_by_region.csv | literal line 38 | pass |
| 1071 | +1.7% | Supp S3 | supplementary_claims.csv:78 | analysis/paper_a/scenarios_by_region.csv | literal line 37 | pass |
| 1072 | -0.28% | Supp S3 | supplementary_claims.csv:78 | analysis/paper_a/scenarios_by_region.csv | literal line 24 | pass |
| 1073 | 156 | Supp S3 | supplementary_claims.csv:79 | analysis/paper_a/scenarios_by_region.csv | literal line 8 | pass |
| 1074 | 0% | Supp S3 | supplementary_claims.csv:79 | analysis/paper_a/scenarios_by_region.csv | literal line 2 | pass |
| 1075 | +0.78% | Supp S3 | supplementary_claims.csv:79 | analysis/paper_a/scenarios_by_region.csv | literal line 30 | pass |
| 1076 | 340 | Supp S3 | supplementary_claims.csv:80 | analysis/paper_a/scenarios_by_region.csv | literal line 6 | pass |
| 1077 | 0% | Supp S3 | supplementary_claims.csv:80 | analysis/paper_a/scenarios_by_region.csv | literal line 2 | pass |
| 1078 | -1.83% | Supp S3 | supplementary_claims.csv:80 | analysis/paper_a/scenarios_by_region.csv | literal line 28 | pass |
| 1079 | 0% | Supp S3 | supplementary_claims.csv:81 | analysis/paper_a/scenarios_by_region.csv | literal line 2 | pass |
| 1080 | +48.45% | Supp S3 | supplementary_claims.csv:81 | analysis/paper_a/scenarios_by_region.csv | literal line 32 | pass |
| 1081 | 0% | Supp S3 | supplementary_claims.csv:82 | analysis/paper_a/scenarios_by_region.csv | literal line 2 | pass |
| 1082 | +64.47% | Supp S3 | supplementary_claims.csv:82 | analysis/paper_a/scenarios_by_region.csv | literal line 34 | pass |
| 1083 | 1,000 | Supp S4 | supplementary_claims.csv:83 | analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md | literal line 7 | pass |
| 1084 | 13 | Supp S4 | supplementary_claims.csv:83 | analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md | literal line 7 | pass |
| 1085 | 81% | Supp S4 | supplementary_claims.csv:87 | results/ranges_2025-fixed.csv | cell value 0.806 in results/ranges_2025-fixed.csv; rounded 0.806 x100 line 2 | pass |
| 1086 | 36% | Supp S4 | supplementary_claims.csv:88 | results/ranges_2025-fixed.csv | literal line 72 | pass |
| 1087 | 13 | Supp S4 | supplementary_claims.csv:83 | analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md | literal line 7 | pass |
| 1088 | 2,000 | Supp S4 | supplementary_claims.csv:89 | results/ranges_2025-improved.csv | cell value 2,000 in qa/reports/B115_monte_carlo_widened.md; rounded 20 x100 line 40 | pass |
| 1089 | 19 | Supp S4 | supplementary_claims.csv:89 | results/ranges_2025-improved.csv | literal line 38 | pass |
| 1090 | 13 | Supp S4 | supplementary_claims.csv:83 | analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md | literal line 7 | pass |
| 1091 | 12% | Supp S4 | supplementary_claims.csv:90 | analysis/waste_2025/README.md | literal line 7 | pass |
| 1092 | 14% | Supp S4 | supplementary_claims.csv:90 | analysis/waste_2025/README.md | literal line 25 | pass |
| 1093 | 0 | Supp S4 | supplementary_claims.csv:83 | analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md | literal line 20 | pass |
| 1094 | 1 | Supp S4 | supplementary_claims.csv:83 | analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md | literal line 7 | pass |
| 1095 | 0 | Supp S4 | supplementary_claims.csv:83 | analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md | literal line 20 | pass |
| 1096 | 1 | Supp S4 | supplementary_claims.csv:83 | analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md | literal line 7 | pass |
| 1097 | 1.000 | Supp S4 | supplementary_claims.csv:94 | results/ranges_2025-improved.csv | cell value 1.000 in qa/reports/B115_monte_carlo_widened.md; rounded 1 x1 line 2 | pass |
| 1098 | 1.286 | Supp S4 | supplementary_claims.csv:94 | qa/reports/B115_monte_carlo_widened.md | literal line 20 | pass |
| 1099 | 1.4 | Supp S4 | supplementary_claims.csv:94 |  | qa/reports/V41_check_B115.md sources table (PAL 1.4 to 1.8 within 1.2 to 2.2) | pass |
| 1100 | 1.8 | Supp S4 | supplementary_claims.csv:94 |  | qa/reports/V41_check_B115.md sources table (PAL 1.4 to 1.8 within 1.2 to 2.2) | pass |
| 1101 | 1.2 | Supp S4 | supplementary_claims.csv:94 |  | qa/reports/V41_check_B115.md sources table (PAL 1.4 to 1.8 within 1.2 to 2.2) | pass |
| 1102 | 2.2 | Supp S4 | supplementary_claims.csv:94 |  | qa/reports/V41_check_B115.md sources table (PAL 1.4 to 1.8 within 1.2 to 2.2) | pass |
| 1103 | 19 | Supp S4 | supplementary_claims.csv:89 | results/ranges_2025-improved.csv | literal line 38 | pass |
| 1104 | 5 | Supp S4 | supplementary_claims.csv:159 | results/ranges_2025-fixed.csv | literal line 1 | pass |
| 1105 | 95 | Supp S4 | none |  | structural (percentile label) | pass |
| 1106 | 41.5 | Supp S4 | none |  | results/ranges_2025-fixed.csv line 2 base 41503537 | pass |
| 1107 | 15.6 | Supp S4 | none |  | results/ranges_2025-fixed.csv line 3 base 15623209 | pass |
| 1108 | 5 | Supp S4 | supplementary_claims.csv:160 | results/ranges_2025-improved.csv | literal line 1 | pass |
| 1109 | 95 | Supp S4 | supplementary_claims.csv:163 |  | structural (percentile label) | pass |
| 1110 | 5 | Supp S4 | supplementary_claims.csv:160 | results/ranges_2025-improved.csv | literal line 1 | pass |
| 1111 | 95 | Supp S4 | supplementary_claims.csv:163 |  | structural (percentile label) | pass |
| 1112 | 13 | Supp S4 | supplementary_claims.csv:160 | results/ranges_2025-improved.csv | literal line 26 | pass |
| 1113 | 1,000 | Supp S4 | supplementary_claims.csv:160 | results/ranges_2025-improved.csv | cell value 1,000 in results/ranges_2025-improved.csv; rounded 10 x100 line 20 | pass |
| 1114 | 36.3 | Supp S4 | supplementary_claims.csv:160 | results/ranges_2025-improved.csv | cell value 36.33 in qa/reports/V41_check_B115.md; rounded 0.363 x100 line 26 | pass |
| 1115 | 45.8 | Supp S4 | supplementary_claims.csv:160 | results/ranges_2025-improved.csv | cell value 45.76 in qa/reports/V41_check_B115.md; rounded 4582 x0.01 line 27 | pass |
| 1116 | 1.26 | Supp S4 | supplementary_claims.csv:160 | qa/reports/B115_monte_carlo_widened.md | literal line 31 | pass |
| 1117 | 34.6 | Supp S4 | supplementary_claims.csv:160 | results/ranges_2025-improved.csv | cell value 34.60 in qa/reports/V41_check_B115.md; rounded 0.346 x100 line 86 | pass |
| 1118 | 47.7 | Supp S4 | supplementary_claims.csv:160 | results/ranges_2025-improved.csv | cell value 47.65 in qa/reports/V41_check_B115.md; rounded 0.477 x100 line 9 | pass |
| 1119 | 1.38 | Supp S4 | supplementary_claims.csv:160 | qa/reports/B115_monte_carlo_widened.md | literal line 32 | pass |
| 1120 | 13.4 | Supp S4 | supplementary_claims.csv:160 | qa/reports/B115_monte_carlo_widened.md | literal line 31 | pass |
| 1121 | 16.5 | Supp S4 | supplementary_claims.csv:160 | results/ranges_2025-improved.csv | cell value 16.52 in qa/reports/V41_check_B115.md; rounded 16472 x0.001 line 65 | pass |
| 1122 | 1.23 | Supp S4 | supplementary_claims.csv:160 | qa/reports/B115_monte_carlo_widened.md | literal line 31 | pass |
| 1123 | 12.9 | Supp S4 | supplementary_claims.csv:160 | results/ranges_2025-improved.csv | cell value 12.94 in qa/reports/V41_check_B115.md; rounded 0.129 x100 line 25 | pass |
| 1124 | 16.9 | Supp S4 | supplementary_claims.csv:160 | results/ranges_2025-improved.csv | cell value 16.90 in qa/reports/V41_check_B115.md; rounded 1686 x0.01 line 111 | pass |
| 1125 | 1.31 | Supp S4 | supplementary_claims.csv:160 | qa/reports/B115_monte_carlo_widened.md | literal line 32 | pass |
| 1126 | 19 | Supp S4 | supplementary_claims.csv:161 | results/ranges_2025-improved.csv | literal line 38 | pass |
| 1127 | 2,000 | Supp S4 | supplementary_claims.csv:161 | results/ranges_2025-improved.csv | cell value 2,000 in qa/reports/B115_monte_carlo_widened.md; rounded 20 x100 line 40 | pass |
| 1128 | 31.1 | Supp S4 | supplementary_claims.csv:161 | results/ranges_2025-improved.csv | cell value 31.12 in qa/reports/V41_check_B115.md; rounded 31061 x0.001 line 26 | pass |
| 1129 | 49.2 | Supp S4 | supplementary_claims.csv:161 | qa/reports/B115_monte_carlo_widened.md | literal line 33 | pass |
| 1130 | 1.58 | Supp S4 | supplementary_claims.csv:161 | results/ranges_2025-improved.csv | cell value 1.58 in qa/reports/B115_monte_carlo_widened.md; rounded 1581098 x1e-06 line 54 | pass |
| 1131 | 26.2 | Supp S4 | supplementary_claims.csv:161 | results/ranges_2025-improved.csv | cell value 26.16 in qa/reports/V41_check_B115.md; rounded 26194 x0.001 line 117 | pass |
| 1132 | 58.1 | Supp S4 | supplementary_claims.csv:161 | qa/reports/B115_monte_carlo_widened.md | literal line 34 | pass |
| 1133 | 2.22 | Supp S4 | supplementary_claims.csv:161 | qa/reports/B115_monte_carlo_widened.md | literal line 34 | pass |
| 1134 | 13.3 | Supp S4 | supplementary_claims.csv:161 | results/ranges_2025-improved.csv | cell value 13.31 in qa/reports/V41_check_B115.md; rounded 0.133 x100 line 21 | pass |
| 1135 | 18.8 | Supp S4 | supplementary_claims.csv:161 | results/ranges_2025-improved.csv | cell value 18.77 in qa/reports/V41_check_B115.md; rounded 18757 x0.001 line 65 | pass |
| 1136 | 1.41 | Supp S4 | supplementary_claims.csv:161 | qa/reports/B115_monte_carlo_widened.md | literal line 33 | pass |
| 1137 | 12.4 | Supp S4 | supplementary_claims.csv:161 | results/ranges_2025-improved.csv | cell value 12.42 in qa/reports/V41_check_B115.md; rounded 0.124 x100 line 64 | pass |
| 1138 | 19.9 | Supp S4 | supplementary_claims.csv:161 | qa/reports/B115_monte_carlo_widened.md | literal line 34 | pass |
| 1139 | 1.60 | Supp S4 | supplementary_claims.csv:161 | results/ranges_2025-improved.csv | cell value 1.60 in qa/reports/B115_monte_carlo_widened.md; rounded 0.016 x100 line 52 | pass |
| 1140 | 19 | Supp S4 | supplementary_claims.csv:162 | results/ranges_2025-improved.csv | literal line 38 | pass |
| 1141 | 1,000 | Supp S4 | supplementary_claims.csv:162 | results/ranges_2025-improved.csv | cell value 1,000 in results/ranges_2025-improved.csv; rounded 10 x100 line 20 | pass |
| 1142 | 29.8 | Supp S4 | supplementary_claims.csv:162 | results/ranges_2025-improved.csv | cell value 29.8 in qa/reports/B115_monte_carlo_widened.md; rounded 29750 x0.001 line 26 | pass |
| 1143 | 43.1 | Supp S4 | supplementary_claims.csv:162 | qa/reports/B115_monte_carlo_widened.md | literal line 56 | pass |
| 1144 | 1.45 | Supp S4 | supplementary_claims.csv:162 | results/ranges_2025-improved.csv | cell value 1.45 in qa/reports/B115_monte_carlo_widened.md; rounded 1447434 x1e-06 line 54 | pass |
| 1145 | 13.0 | Supp S4 | supplementary_claims.csv:162 | results/ranges_2025-improved.csv | cell value 13.0 in qa/reports/V41_check_B115.md; rounded 13 x1 line 26 | pass |
| 1146 | 16.2 | Supp S4 | supplementary_claims.csv:162 | results/ranges_2025-improved.csv | cell value 16.2 in qa/reports/V41_check_B115.md; rounded 16170 x0.001 line 13 | pass |
| 1147 | 1.24 | Supp S4 | supplementary_claims.csv:162 | qa/reports/V41_check_B115.md | literal line 37 | pass |
| 1148 | 13 | Supp S4 | supplementary_claims.csv:163 | results/ranges_2025-fixed.csv | literal line 26 | pass |
| 1149 | 1,000 | Supp S4 | supplementary_claims.csv:163 | results/ranges_2025-fixed.csv | cell value 1,000 in REG:B112; rounded 10 x100 line 20 | pass |
| 1150 | 39.4 | Supp S4 | supplementary_claims.csv:163 | results/ranges_2025-fixed.csv | cell value 39.4 in qa/reports/B112_shock_ranges.md; rounded 0.394 x100 line 10 | pass |
| 1151 | 43.8 | Supp S4 | supplementary_claims.csv:163 | results/ranges_2025-fixed.csv | cell value 43.8 in qa/reports/B112_shock_ranges.md; rounded 0.438 x100 line 45 | pass |
| 1152 | 13.9 | Supp S4 | supplementary_claims.csv:163 | results/ranges_2025-fixed.csv | cell value 13.9 in qa/reports/B112_shock_ranges.md; rounded 0.139 x100 line 65 | pass |
| 1153 | 16.2 | Supp S4 | supplementary_claims.csv:163 | results/ranges_2025-fixed.csv | cell value 16.2 in qa/reports/B112_shock_ranges.md; rounded 0.162 x100 line 30 | pass |
| 1154 | 19 | Supp S4 | supplementary_claims.csv:98 |  | structural (column label; 19 choices per B115, V41) | pass |
| 1155 | 39.0 | Supp S4 | supplementary_claims.csv:98 | results/ranges_2025-improved.csv | cell value 39.0 in qa/reports/B115_monte_carlo_widened.md; rounded 39 x1 line 78 | pass |
| 1156 | 15.8 | Supp S4 | supplementary_claims.csv:98 | results/ranges_2025-improved.csv | cell value 15.8 in qa/reports/B115_monte_carlo_widened.md; rounded 0.158 x100 line 72 | pass |
| 1157 | 29.8 | Supp S4 | supplementary_claims.csv:100 | results/ranges_2025-improved.csv | cell value 29.8 in qa/reports/B115_monte_carlo_widened.md; rounded 29750 x0.001 line 26 | pass |
| 1158 | 43.1 | Supp S4 | supplementary_claims.csv:100 | qa/reports/B115_monte_carlo_widened.md | literal line 56 | pass |
| 1159 | 5 | Supp S4 | supplementary_claims.csv:98 | results/ranges_2025-improved.csv | literal line 1 | pass |
| 1160 | 95 | Supp S4 | supplementary_claims.csv:101 |  | structural (percentile label) | pass |
| 1161 | 1.58 | Supp S4 | supplementary_claims.csv:101 | results/ranges_2025-improved.csv | cell value 1.58 in qa/reports/B115_monte_carlo_widened.md; rounded 1581098 x1e-06 line 54 | pass |
| 1162 | 2.14 | Supp S4 | supplementary_claims.csv:101 | analysis/method_tests_2025/design_choices.csv | literal line 7 | pass |
| 1163 | 2.19 | Supp S4 | supplementary_claims.csv:101 | analysis/method_tests_2025/design_choices.csv | literal line 2 | pass |
| 1164 | 2.41 | Supp S4 | supplementary_claims.csv:101 | analysis/method_tests_2025/design_choices.csv | literal line 11 | pass |
| 1165 | 6.36 | Supp S4 | supplementary_claims.csv:101 | analysis/method_tests_2025/design_choices.csv | literal line 13 | pass |
| 1166 | 2.66 | Supp S4 | supplementary_claims.csv:101 | analysis/method_tests_2025/design_choices.csv | literal line 10 | pass |
| 1167 | 2.67 | Supp S4 | supplementary_claims.csv:101 | analysis/method_tests_2025/design_choices.csv | literal line 6 | pass |
| 1168 | 1.33 | Supp S4 | supplementary_claims.csv:101 | analysis/method_tests_2025/design_choices.csv | literal line 3 | pass |
| 1169 | 1.09 | Supp S4 | supplementary_claims.csv:101 | analysis/method_tests_2025/design_choices.csv | literal line 5 | pass |
| 1170 | 8 | Supp S4 | supplementary_claims.csv:98 | results/ranges_2025-improved.csv | literal line 16 | pass |
| 1171 | 10 | Supp S4 | supplementary_claims.csv:102 | results/ranges_2025-fixed.csv | literal line 20 | pass |
| 1172 | 15 | Supp S4 | supplementary_claims.csv:98 | results/ranges_2025-improved.csv | literal line 30 | pass |
| 1173 | 20 | Supp S4 | supplementary_claims.csv:102 | results/ranges_2025-fixed.csv | literal line 40 | pass |
| 1174 | 19 | Supp S4 | supplementary_claims.csv:89 | results/ranges_2025-improved.csv | literal line 38 | pass |
| 1175 | 42,000 | Supp S4 | none |  | qa/reports/V41_check_B115.md (B116 row: "42,000 runs: holds") | pass |
| 1176 | 1% | Supp S4 | supplementary_claims.csv:164 | analysis/sensitivity_2025/sobol_2025-fixed.csv | literal line 9 | pass |
| 1177 | 32% | Supp S4 | supplementary_claims.csv:165 | results/ranges_2025-improved.csv | literal line 64 | pass |
| 1178 | 33% | Supp S4 | supplementary_claims.csv:165 | results/ranges_2025-improved.csv | literal line 66 | pass |
| 1179 | 58% | Supp S4 | supplementary_claims.csv:165 | results/ranges_2025-improved.csv | literal line 116 | pass |
| 1180 | 56% | Supp S4 | supplementary_claims.csv:165 | results/ranges_2025-improved.csv | literal line 112 | pass |
| 1181 | 27% | Supp S4 | supplementary_claims.csv:166 | results/ranges_2025-improved.csv | literal line 54 | pass |
| 1182 | 25% | Supp S4 | supplementary_claims.csv:166 | results/ranges_2025-improved.csv | literal line 1 | pass |
| 1183 | 0% | Supp S4 | supplementary_claims.csv:166 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1184 | 0% | Supp S4 | supplementary_claims.csv:166 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1185 | 24% | Supp S4 | supplementary_claims.csv:167 | results/ranges_2025-improved.csv | literal line 48 | pass |
| 1186 | 23% | Supp S4 | supplementary_claims.csv:167 | results/ranges_2025-improved.csv | literal line 46 | pass |
| 1187 | 14% | Supp S4 | supplementary_claims.csv:167 | results/ranges_2025-improved.csv | literal line 28 | pass |
| 1188 | 14% | Supp S4 | supplementary_claims.csv:167 | results/ranges_2025-improved.csv | literal line 28 | pass |
| 1189 | 6% | Supp S4 | supplementary_claims.csv:168 | results/ranges_2025-improved.csv | literal line 12 | pass |
| 1190 | 6% | Supp S4 | supplementary_claims.csv:168 | results/ranges_2025-improved.csv | literal line 12 | pass |
| 1191 | 0% | Supp S4 | supplementary_claims.csv:168 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1192 | 0% | Supp S4 | supplementary_claims.csv:168 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1193 | 4% | Supp S4 | supplementary_claims.csv:169 | results/ranges_2025-improved.csv | literal line 8 | pass |
| 1194 | 5% | Supp S4 | supplementary_claims.csv:169 | results/ranges_2025-improved.csv | literal line 1 | pass |
| 1195 | 0% | Supp S4 | supplementary_claims.csv:169 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1196 | 0% | Supp S4 | supplementary_claims.csv:169 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1197 | 3% | Supp S4 | supplementary_claims.csv:170 | results/ranges_2025-improved.csv | literal line 6 | pass |
| 1198 | 3% | Supp S4 | supplementary_claims.csv:170 | results/ranges_2025-improved.csv | literal line 6 | pass |
| 1199 | 1% | Supp S4 | supplementary_claims.csv:170 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1200 | 1% | Supp S4 | supplementary_claims.csv:170 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1201 | 1% | Supp S4 | supplementary_claims.csv:171 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1202 | 1% | Supp S4 | supplementary_claims.csv:171 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1203 | 0% | Supp S4 | supplementary_claims.csv:171 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1204 | 0% | Supp S4 | supplementary_claims.csv:171 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1205 | 0% | Supp S4 | supplementary_claims.csv:172 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1206 | 0% | Supp S4 | supplementary_claims.csv:172 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1207 | 20% | Supp S4 | supplementary_claims.csv:172 | results/ranges_2025-improved.csv | literal line 40 | pass |
| 1208 | 20% | Supp S4 | supplementary_claims.csv:172 | results/ranges_2025-improved.csv | literal line 40 | pass |
| 1209 | 0% | Supp S4 | supplementary_claims.csv:173 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1210 | 0% | Supp S4 | supplementary_claims.csv:173 | results/ranges_2025-improved.csv | literal line 2 | pass |
| 1211 | 4% | Supp S4 | supplementary_claims.csv:173 | results/ranges_2025-improved.csv | literal line 8 | pass |
| 1212 | 4% | Supp S4 | supplementary_claims.csv:173 | results/ranges_2025-improved.csv | literal line 8 | pass |
| 1213 | 3% | Supp S4 | supplementary_claims.csv:104 | qa/reports/V41_check_B115.md | literal line 101 | pass |
| 1214 | 85% | Supp S4 | supplementary_claims.csv:105 | results/ranges_2025-fixed.csv | cell value 84.7 in qa/reports/B112_shock_ranges.md; rounded 0.851 x100 line 6 | pass |
| 1215 | 16% | Supp S4 | supplementary_claims.csv:105 | results/ranges_2025-fixed.csv | literal line 32 | pass |
| 1216 | 1% | Supp S4 | supplementary_claims.csv:105 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1217 | 106% | Supp S4 | supplementary_claims.csv:106 | results/ranges_2025-fixed.csv | cell value 106 in results/ranges_2025-fixed.csv; rounded 105754 x0.001 line 37 | pass |
| 1218 | 81% | Supp S4 | supplementary_claims.csv:107 | results/ranges_2025-fixed.csv | cell value 81.3 in qa/reports/B112_shock_ranges.md; rounded 0.806 x100 line 2 | pass |
| 1219 | 14% | Supp S4 | supplementary_claims.csv:107 | results/ranges_2025-fixed.csv | literal line 28 | pass |
| 1220 | 2% | Supp S4 | supplementary_claims.csv:107 | results/ranges_2025-fixed.csv | literal line 4 | pass |
| 1221 | 1 | Supp S4 | supplementary_claims.csv:174 | analysis/paper_a/shocks_ranges_wide.csv | literal line 2 | pass |
| 1222 | 10 | Supp S4 | supplementary_claims.csv:174 | analysis/paper_a/shocks_ranges_wide.csv | literal line 9 | pass |
| 1223 | 1 | Supp S4 | supplementary_claims.csv:174 | analysis/paper_a/shocks_ranges_wide.csv | literal line 2 | pass |
| 1224 | 20 | Supp S4 | supplementary_claims.csv:174 | analysis/paper_a/shocks_ranges_wide.csv | literal line 18 | pass |
| 1225 | 5 | Supp S4 | supplementary_claims.csv:144 | analysis/paper_a/method_effects_by_region.csv | literal line 4 | pass |
| 1226 | 95 | Supp S4 | none |  | structural (percentile label) | pass |
| 1227 | 27.6 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | cell value 27.6 in qa/reports/B123_shocks_on_widened_draws.md; rounded 27608200 x1e-06 line 2 | pass |
| 1228 | 19 | Supp S4 | supplementary_claims.csv:174 |  | structural (column label; 19 choices per B115, V41) | pass |
| 1229 | 13 | Supp S4 | supplementary_claims.csv:174 | analysis/paper_a/shocks_ranges.csv | literal line 12 | pass |
| 1230 | 19 | Supp S4 | supplementary_claims.csv:174 | analysis/paper_a/shocks_ranges_wide.csv | literal line 2 | pass |
| 1231 | 19 | Supp S4 | none |  | structural (column label; 19 choices per B115, V41) | pass |
| 1232 | 13 | Supp S4 | supplementary_claims.csv:163 | results/ranges_2025-fixed.csv | literal line 26 | pass |
| 1233 | 1 | Supp S4 | supplementary_claims.csv:175 | analysis/comparators_2025/rerun.csv | literal line 2 | pass |
| 1234 | 10 | Supp S4 | supplementary_claims.csv:175 | analysis/comparators_2025/rerun.csv | literal line 4 | pass |
| 1235 | 0.742 | Supp S4 | supplementary_claims.csv:175 | qa/reports/B123_shocks_on_widened_draws.md | cell value 0.742 in qa/reports/B123_shocks_on_widened_draws.md; rounded 0.742361 x1 line 23 | pass |
| 1236 | 30.8 | Supp S4 | supplementary_claims.csv:175 | analysis/comparators_2025/rerun.csv | cell value 30.8 in analysis/comparators_2025/rerun.csv; rounded 30.81 x1 line 44 | pass |
| 1237 | 23.1 | Supp S4 | supplementary_claims.csv:175 | qa/reports/B123_shocks_on_widened_draws.md | literal line 14 | pass |
| 1238 | 36.5 | Supp S4 | supplementary_claims.csv:175 | analysis/comparators_2025/rerun.csv | cell value 36.5 in qa/reports/B123_shocks_on_widened_draws.md; rounded 36.45 x1 line 31 | pass |
| 1239 | 0.84 | Supp S4 | supplementary_claims.csv:175 | qa/reports/B123_shocks_on_widened_draws.md | literal line 83 | pass |
| 1240 | 1.32 | Supp S4 | supplementary_claims.csv:175 | qa/reports/B123_shocks_on_widened_draws.md | literal line 83 | pass |
| 1241 | 27.0 | Supp S4 | supplementary_claims.csv:175 | qa/reports/B123_shocks_on_widened_draws.md | literal line 17 | pass |
| 1242 | 34.0 | Supp S4 | supplementary_claims.csv:175 | qa/reports/B123_shocks_on_widened_draws.md | literal line 17 | pass |
| 1243 | 0.98 | Supp S4 | supplementary_claims.csv:175 | qa/reports/B123_shocks_on_widened_draws.md | literal line 83 | pass |
| 1244 | 1.23 | Supp S4 | supplementary_claims.csv:175 | qa/reports/B123_shocks_on_widened_draws.md | literal line 83 | pass |
| 1245 | 29.2 | Supp S4 | supplementary_claims.csv:175 | qa/reports/B123_shocks_on_widened_draws.md | literal line 82 | pass |
| 1246 | 32.5 | Supp S4 | supplementary_claims.csv:175 | qa/reports/B123_shocks_on_widened_draws.md | literal line 82 | pass |
| 1247 | 1.06 | Supp S4 | supplementary_claims.csv:175 | qa/reports/B123_shocks_on_widened_draws.md | literal line 83 | pass |
| 1248 | 1.18 | Supp S4 | supplementary_claims.csv:175 | qa/reports/B123_shocks_on_widened_draws.md | literal line 83 | pass |
| 1249 | 1 | Supp S4 | supplementary_claims.csv:176 | analysis/comparators_2025/rerun.csv | literal line 2 | pass |
| 1250 | 20 | Supp S4 | supplementary_claims.csv:176 | analysis/comparators_2025/rerun.csv | literal line 5 | pass |
| 1251 | 0.634 | Supp S4 | supplementary_claims.csv:176 | qa/reports/B123_shocks_on_widened_draws.md | cell value 0.634 in qa/reports/B123_shocks_on_widened_draws.md; rounded 0.634262 x1 line 23 | pass |
| 1252 | 26.3 | Supp S4 | supplementary_claims.csv:176 | analysis/comparators_2025/rerun.csv | cell value 26.3 in analysis/comparators_2025/rerun.csv; rounded 26.32 x1 line 45 | pass |
| 1253 | 19.7 | Supp S4 | supplementary_claims.csv:176 | qa/reports/B123_shocks_on_widened_draws.md | literal line 15 | pass |
| 1254 | 31.2 | Supp S4 | supplementary_claims.csv:176 | qa/reports/B123_shocks_on_widened_draws.md | literal line 15 | pass |
| 1255 | 1.13 | Supp S4 | supplementary_claims.csv:176 | qa/reports/B123_shocks_on_widened_draws.md | literal line 84 | pass |
| 1256 | 23.0 | Supp S4 | supplementary_claims.csv:176 | qa/reports/B123_shocks_on_widened_draws.md | literal line 17 | pass |
| 1257 | 29.0 | Supp S4 | supplementary_claims.csv:176 | qa/reports/B123_shocks_on_widened_draws.md | literal line 17 | pass |
| 1258 | 0.83 | Supp S4 | supplementary_claims.csv:176 | qa/reports/B123_shocks_on_widened_draws.md | literal line 84 | pass |
| 1259 | 1.05 | Supp S4 | supplementary_claims.csv:176 | qa/reports/B123_shocks_on_widened_draws.md | literal line 84 | pass |
| 1260 | 25.0 | Supp S4 | supplementary_claims.csv:176 | qa/reports/B123_shocks_on_widened_draws.md | literal line 93 | pass |
| 1261 | 27.8 | Supp S4 | supplementary_claims.csv:176 | qa/reports/B123_shocks_on_widened_draws.md | literal line 93 | pass |
| 1262 | 0.90 | Supp S4 | supplementary_claims.csv:176 |  | qa/reports/R03a_response_plan_A.md line 151 ("43.5, 0.90 of the median") | pass |
| 1263 | 1.01 | Supp S4 | supplementary_claims.csv:176 | qa/reports/B123_shocks_on_widened_draws.md | literal line 84 | pass |
| 1264 | 19 | Supp S4 | supplementary_claims.csv:108 |  | structural (column label; 19 choices per B115, V41) | pass |
| 1265 | 27.6 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | cell value 27.6 in qa/reports/B123_shocks_on_widened_draws.md; rounded 27608200 x1e-06 line 2 | pass |
| 1266 | 37% | Supp S4 | supplementary_claims.csv:108 |  | shocks_ranges_wide.csv line 10 share_draws_below_population 0.3700; B123; no checker (V44 absent) | pass (builder only) |
| 1267 | 1 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 2 | pass |
| 1268 | 10 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 9 | pass |
| 1269 | 78% | Supp S4 | supplementary_claims.csv:108 |  | shocks_ranges_wide.csv line 18 0.7765; B123; no checker (V44 absent) | pass (builder only) |
| 1270 | 1 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 2 | pass |
| 1271 | 20 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 18 | pass |
| 1272 | 0.45% | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | cell value 0.45 in analysis/paper_a/shocks_ranges_wide.csv; rounded 0.0045 x100 line 2 | pass |
| 1273 | 13 | Supp S4 | supplementary_claims.csv:109 | results/ranges_2025-fixed.csv | literal line 26 | pass |
| 1274 | 1 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 2 | pass |
| 1275 | 10 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 9 | pass |
| 1276 | 27.6 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | cell value 27.6 in qa/reports/B123_shocks_on_widened_draws.md; rounded 27608200 x1e-06 line 2 | pass |
| 1277 | 1 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 2 | pass |
| 1278 | 20 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 18 | pass |
| 1279 | 92% | Supp S4 | supplementary_claims.csv:110 | qa/reports/V38_check_B112.md | literal line 114 | pass |
| 1280 | 13 | Supp S4 | supplementary_claims.csv:109 | results/ranges_2025-fixed.csv | literal line 26 | pass |
| 1281 | 19 | Supp S4 | supplementary_claims.csv:108 |  | structural (column label; 19 choices per B115, V41) | pass |
| 1282 | 1 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 2 | pass |
| 1283 | 10 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 9 | pass |
| 1284 | 21 | Supp S4 | supplementary_claims.csv:112 | results/ranges_2025-fixed.csv | literal line 42 | pass |
| 1285 | 21 | Supp S4 | supplementary_claims.csv:112 | results/ranges_2025-fixed.csv | literal line 42 | pass |
| 1286 | 95 | Supp S4 | supplementary_claims.csv:112 |  | structural (percentile label) | pass |
| 1287 | 22 | Supp S4 | supplementary_claims.csv:112 | results/ranges_2025-fixed.csv | literal line 44 | pass |
| 1288 | 5 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 1 | pass |
| 1289 | 1 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 2 | pass |
| 1290 | 20 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 18 | pass |
| 1291 | 24 | Supp S4 | supplementary_claims.csv:113 | results/ranges_2025-fixed.csv | literal line 48 | pass |
| 1292 | 1 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 2 | pass |
| 1293 | 20 | Supp S4 | supplementary_claims.csv:108 | analysis/paper_a/shocks_ranges_wide.csv | literal line 18 | pass |
| 1294 | 1860 | Supp S4 | supplementary_claims.csv:117 | qa/reports/B112_shock_ranges.md | literal line 84 | pass |
| 1295 | 153 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | cell value 153 in results/ranges_2025-fixed.csv; rounded 153454 x0.001 line 104 | pass |
| 1296 | 1861 | Supp S4 | supplementary_claims.csv:116 | qa/reports/B112_shock_ranges.md | literal line 84 | pass |
| 1297 | 1866 | Supp S4 | supplementary_claims.csv:116 | qa/reports/B112_shock_ranges.md | literal line 84 | pass |
| 1298 | 1871 | Supp S4 | supplementary_claims.csv:116 | qa/reports/B112_shock_ranges.md | literal line 84 | pass |
| 1299 | 1875 | Supp S4 | supplementary_claims.csv:116 | qa/reports/B112_shock_ranges.md | literal line 84 | pass |
| 1300 | 153 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | cell value 153 in results/ranges_2025-fixed.csv; rounded 153454 x0.001 line 104 | pass |
| 1301 | 1 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1302 | 1 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1303 | 3 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 6 | pass |
| 1304 | 5 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 1 | pass |
| 1305 | 10 | Supp S4 | supplementary_claims.csv:119 | results/ranges_2025-fixed.csv | literal line 20 | pass |
| 1306 | 20 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 40 | pass |
| 1307 | 30 | Supp S4 | supplementary_claims.csv:119 | results/ranges_2025-fixed.csv | literal line 60 | pass |
| 1308 | 50 | Supp S4 | supplementary_claims.csv:119 | results/ranges_2025-fixed.csv | literal line 1 | pass |
| 1309 | 150 | Supp S4 | supplementary_claims.csv:119 | qa/reports/B112_shock_ranges.md | literal line 84 | pass |
| 1310 | 1 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1311 | 10 | Supp S4 | supplementary_claims.csv:119 | results/ranges_2025-fixed.csv | literal line 20 | pass |
| 1312 | 0.742 | Supp S4 | supplementary_claims.csv:124 | results/ranges_2025-fixed.csv | literal line 42 | pass |
| 1313 | 15 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 30 | pass |
| 1314 | 1 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1315 | 20 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 40 | pass |
| 1316 | 0.634 | Supp S4 | supplementary_claims.csv:124 | qa/reports/B112_shock_ranges.md | literal line 33 | pass |
| 1317 | 8 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 16 | pass |
| 1318 | 1896 | Supp S4 | supplementary_claims.csv:122 | qa/reports/B112_shock_ranges.md | literal line 84 | pass |
| 1319 | 1 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1320 | 100 | Supp S4 | supplementary_claims.csv:119 | results/ranges_2025-fixed.csv | cell value 100 in results/ranges_2025-fixed.csv; rounded 1 x100 line 2 | pass |
| 1321 | 0.456 | Supp S4 | supplementary_claims.csv:123 | results/ranges_2025-fixed.csv | literal line 36 | pass |
| 1322 | 50 | Supp S4 | supplementary_claims.csv:119 | results/ranges_2025-fixed.csv | literal line 1 | pass |
| 1323 | 3 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 6 | pass |
| 1324 | 0.552 | Supp S4 | supplementary_claims.csv:123 | qa/reports/B112_shock_ranges.md | literal line 84 | pass |
| 1325 | 150 | Supp S4 | supplementary_claims.csv:119 | qa/reports/B112_shock_ranges.md | literal line 84 | pass |
| 1326 | 0.359 | Supp S4 | supplementary_claims.csv:123 | results/ranges_2025-fixed.csv | literal line 70 | pass |
| 1327 | 0.567 | Supp S4 | supplementary_claims.csv:125 | results/ranges_2025-fixed.csv | literal line 74 | pass |
| 1328 | 4 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 8 | pass |
| 1329 | 0.578 | Supp S4 | supplementary_claims.csv:125 | results/ranges_2025-fixed.csv | cell value 0.578 in qa/reports/B112_shock_ranges.md; rounded 578366 x1e-06 line 38 | pass |
| 1330 | 0.762 | Supp S4 | supplementary_claims.csv:125 | qa/reports/B112_shock_ranges.md | literal line 84 | pass |
| 1331 | 16 | Supp S4 | supplementary_claims.csv:125 | results/ranges_2025-fixed.csv | literal line 32 | pass |
| 1332 | 0.599 | Supp S4 | supplementary_claims.csv:126 | results/ranges_2025-fixed.csv | cell value 0.599 in qa/reports/B112_shock_ranges.md; rounded 598600 x1e-06 line 107 | pass |
| 1333 | 20 | Supp S4 | supplementary_claims.csv:116 | results/ranges_2025-fixed.csv | literal line 40 | pass |
| 1334 | 1 | Supp S4 | supplementary_claims.csv:178 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1335 | 10 | Supp S4 | supplementary_claims.csv:178 | results/ranges_2025-fixed.csv | literal line 20 | pass |
| 1336 | 0.742 | Supp S4 | supplementary_claims.csv:178 | results/ranges_2025-fixed.csv | literal line 42 | pass |
| 1337 | 41.50 | Supp S4 | supplementary_claims.csv:178 | results/ranges_2025-fixed.csv | cell value 41,503,537 in results/ranges_2025-fixed.csv; rounded 41503537 x1e-06 line 2 | pass |
| 1338 | 30.81 | Supp S4 | supplementary_claims.csv:178 | qa/reports/B112_shock_ranges.md | literal line 22 | pass |
| 1339 | 41.19 | Supp S4 | supplementary_claims.csv:178 | qa/reports/B112_shock_ranges.md | literal line 90 | pass |
| 1340 | 41.32 | Supp S4 | supplementary_claims.csv:178 | qa/reports/B112_shock_ranges.md | literal line 90 | pass |
| 1341 | 1 | Supp S4 | supplementary_claims.csv:179 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1342 | 20 | Supp S4 | supplementary_claims.csv:179 | results/ranges_2025-fixed.csv | literal line 40 | pass |
| 1343 | 0.634 | Supp S4 | supplementary_claims.csv:179 | qa/reports/B112_shock_ranges.md | literal line 33 | pass |
| 1344 | 41.50 | Supp S4 | supplementary_claims.csv:179 | results/ranges_2025-fixed.csv | cell value 41.50 in qa/reports/B112_shock_ranges.md; rounded 41503537 x1e-06 line 2 | pass |
| 1345 | 26.32 | Supp S4 | supplementary_claims.csv:179 | qa/reports/B112_shock_ranges.md | literal line 33 | pass |
| 1346 | 40.99 | Supp S4 | supplementary_claims.csv:179 | qa/reports/B112_shock_ranges.md | literal line 91 | pass |
| 1347 | 41.20 | Supp S4 | supplementary_claims.csv:179 | results/ranges_2025-fixed.csv | cell value 41,201,815 in qa/reports/V38_check_B112.md; rounded 0.412 x100 line 11 | pass |
| 1348 | 1 | Supp S4 | supplementary_claims.csv:180 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1349 | 100 | Supp S4 | supplementary_claims.csv:180 | results/ranges_2025-fixed.csv | cell value 100 in results/ranges_2025-fixed.csv; rounded 1 x100 line 2 | pass |
| 1350 | 0.456 | Supp S4 | supplementary_claims.csv:180 | results/ranges_2025-fixed.csv | literal line 36 | pass |
| 1351 | 41.50 | Supp S4 | supplementary_claims.csv:180 | results/ranges_2025-fixed.csv | cell value 41.50 in qa/reports/B112_shock_ranges.md; rounded 41503537 x1e-06 line 2 | pass |
| 1352 | 18.92 | Supp S4 | supplementary_claims.csv:180 | qa/reports/B112_shock_ranges.md | literal line 92 | pass |
| 1353 | 40.45 | Supp S4 | supplementary_claims.csv:180 | qa/reports/B112_shock_ranges.md | literal line 92 | pass |
| 1354 | 40.88 | Supp S4 | supplementary_claims.csv:180 | qa/reports/B112_shock_ranges.md | literal line 92 | pass |
| 1355 | 1 | Supp S4 | supplementary_claims.csv:181 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1356 | 100 | Supp S4 | supplementary_claims.csv:181 | results/ranges_2025-fixed.csv | cell value 100 in results/ranges_2025-fixed.csv; rounded 1 x100 line 2 | pass |
| 1357 | 0.456 | Supp S4 | supplementary_claims.csv:181 | results/ranges_2025-fixed.csv | literal line 36 | pass |
| 1358 | 34.27 | Supp S4 | supplementary_claims.csv:181 | qa/reports/B112_shock_ranges.md | literal line 93 | pass |
| 1359 | 15.62 | Supp S4 | supplementary_claims.csv:181 | results/ranges_2025-fixed.csv | cell value 15,623,209 in results/ranges_2025-fixed.csv; rounded 15623209 x1e-06 line 3 | pass |
| 1360 | 24.68 | Supp S4 | supplementary_claims.csv:181 | qa/reports/B112_shock_ranges.md | literal line 93 | pass |
| 1361 | 24.68 | Supp S4 | supplementary_claims.csv:181 | qa/reports/B112_shock_ranges.md | literal line 93 | pass |
| 1362 | -0.8% | Supp S4 | supplementary_claims.csv:127 | results/ranges_2025-fixed.csv | cell value -0.75 in qa/reports/V38_check_B112.md; rounded 75 x0.01 line 1 | pass |
| 1363 | 1 | Supp S4 | supplementary_claims.csv:127 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1364 | 10 | Supp S4 | supplementary_claims.csv:127 | results/ranges_2025-fixed.csv | literal line 20 | pass |
| 1365 | -2.5% | Supp S4 | supplementary_claims.csv:127 | results/ranges_2025-fixed.csv | cell value -2.54 in qa/reports/V38_check_B112.md; rounded 2457335 x1e-06 line 5 | pass |
| 1366 | 1 | Supp S4 | supplementary_claims.csv:127 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1367 | 100 | Supp S4 | supplementary_claims.csv:127 | results/ranges_2025-fixed.csv | cell value 100 in results/ranges_2025-fixed.csv; rounded 1 x100 line 2 | pass |
| 1368 | 97% | Supp S4 | supplementary_claims.csv:128 | qa/reports/V38_check_B112.md | literal line 12 | pass |
| 1369 | 1 | Supp S4 | supplementary_claims.csv:127 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1370 | 10 | Supp S4 | supplementary_claims.csv:127 | results/ranges_2025-fixed.csv | literal line 20 | pass |
| 1371 | 28% | Supp S4 | supplementary_claims.csv:129 | results/ranges_2025-fixed.csv | literal line 56 | pass |
| 1372 | 1 | Supp S4 | supplementary_claims.csv:127 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1373 | 100 | Supp S4 | supplementary_claims.csv:127 | results/ranges_2025-fixed.csv | cell value 100 in results/ranges_2025-fixed.csv; rounded 1 x100 line 2 | pass |
| 1374 | 54% | Supp S4 | supplementary_claims.csv:129 | results/ranges_2025-fixed.csv | literal line 108 | pass |
| 1375 | 48.8 | Supp S4 | supplementary_claims.csv:130 | analysis/reliability_2025/README.md | literal line 14 | pass |
| 1376 | 48.3 | Supp S4 | supplementary_claims.csv:130 | analysis/reliability_2025/README.md | literal line 16 | pass |
| 1377 | 48.5 | Supp S4 | supplementary_claims.csv:130 | analysis/reliability_2025/README.md | literal line 22 | pass |
| 1378 | 43.5 | Supp S4 | supplementary_claims.csv:131 | analysis/reliability_2025/README.md | literal line 17 | pass |
| 1379 | 0.90 | Supp S4 | supplementary_claims.csv:131 |  | qa/reports/R03a_response_plan_A.md line 151 ("43.5, 0.90 of the median") | pass |
| 1380 | 40.5 | Supp S4 | supplementary_claims.csv:132 | analysis/reliability_2025/README.md | literal line 46 | pass |
| 1381 | -21.5% | Supp S4 | supplementary_claims.csv:135 | analysis/paper_a/method_effects_by_region.csv | literal line 36 | pass |
| 1382 | -16.4% | Supp S4 | supplementary_claims.csv:135 | analysis/paper_a/method_effects_by_region.csv | literal line 7 | pass |
| 1383 | -15.4% | Supp S4 | supplementary_claims.csv:135 | analysis/paper_a/method_effects_by_region.csv | literal line 24 | pass |
| 1384 | +95.8% | Supp S4 | supplementary_claims.csv:137 | analysis/paper_a/method_effects_by_region.csv | literal line 78 | pass |
| 1385 | +83.5% | Supp S4 | supplementary_claims.csv:137 | analysis/paper_a/method_effects_by_region.csv | literal line 106 | pass |
| 1386 | +0.1% | Supp S4 | supplementary_claims.csv:138 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1387 | -27.3% | Supp S4 | supplementary_claims.csv:139 | analysis/paper_a/method_effects_summary.csv | literal line 9 | pass |
| 1388 | +22.1% | Supp S4 | supplementary_claims.csv:139 | analysis/paper_a/method_effects_summary.csv | literal line 9 | pass |
| 1389 | -27.3% | Supp S4 | supplementary_claims.csv:139 | analysis/paper_a/method_effects_summary.csv | literal line 9 | pass |
| 1390 | -15.5% | Supp S4 | supplementary_claims.csv:140 | analysis/paper_a/method_effects_by_region.csv | literal line 35 | pass |
| 1391 | +22.1% | Supp S4 | supplementary_claims.csv:139 | analysis/paper_a/method_effects_summary.csv | literal line 9 | pass |
| 1392 | +22.0% | Supp S4 | supplementary_claims.csv:141 | analysis/paper_a/method_effects_by_region.csv | literal line 7 | pass |
| 1393 | +22.0% | Supp S4 | supplementary_claims.csv:141 | analysis/paper_a/method_effects_by_region.csv | literal line 7 | pass |
| 1394 | 53% | Supp S4 | supplementary_claims.csv:142 | analysis/paper_a/method_effects_by_region.csv | literal line 48 | pass |
| 1395 | +11.2% | Supp S4 | supplementary_claims.csv:143 | analysis/paper_a/method_effects_summary.csv | literal line 6 | pass |
| 1396 | +0.8% | Supp S4 | supplementary_claims.csv:143 | analysis/paper_a/method_effects_summary.csv | literal line 6 | pass |
| 1397 | +22.6% | Supp S4 | supplementary_claims.csv:143 | analysis/paper_a/method_effects_summary.csv | literal line 6 | pass |
| 1398 | -5.8% | Supp S4 | supplementary_claims.csv:144 | analysis/paper_a/method_effects_by_region.csv | literal line 49 | pass |
| 1399 | -9.7% | Supp S4 | supplementary_claims.csv:144 | analysis/paper_a/method_effects_by_region.csv | literal line 19 | pass |
| 1400 | -1.1% | Supp S4 | supplementary_claims.csv:144 | analysis/paper_a/method_effects_by_region.csv | literal line 56 | pass |
| 1401 | +0.1% | Supp S4 | supplementary_claims.csv:144 | analysis/paper_a/method_effects_by_region.csv | literal line 5 | pass |
| 1402 | 29.1% | Supp S4 | supplementary_claims.csv:145 | analysis/paper_a/method_effects_by_region.csv | literal line 81 | pass |
| 1403 | 18.2% | Supp S4 | supplementary_claims.csv:145 | analysis/paper_a/method_effects_by_region.csv | literal line 63 | pass |
| 1404 | 0% | Supp S4 | supplementary_claims.csv:144 | analysis/paper_a/method_effects_by_region.csv | literal line 2 | pass |
| 1405 | -7.4% | Supp S4 | supplementary_claims.csv:146 | analysis/paper_a/method_effects_summary.csv | literal line 7 | pass |
| 1406 | +9.9% | Supp S4 | supplementary_claims.csv:146 | analysis/paper_a/method_effects_summary.csv | literal line 7 | pass |
| 1407 | -16.0 | Supp S4 | supplementary_claims.csv:149 | analysis/paper_a/method_effects_summary.csv | literal line 3 | pass |
| 1408 | -21.5 | Supp S4 | supplementary_claims.csv:149 | analysis/paper_a/method_effects_summary.csv | literal line 3 | pass |
| 1409 | 0.0 | Supp S4 | supplementary_claims.csv:149 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1410 | 0.0 | Supp S4 | supplementary_claims.csv:149 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1411 | -7.7 | Supp S4 | supplementary_claims.csv:149 | analysis/paper_a/method_effects_summary.csv | literal line 11 | pass |
| 1412 | 0.0 | Supp S4 | supplementary_claims.csv:149 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1413 | +0.1 | Supp S4 | supplementary_claims.csv:151 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1414 | 0.0 | Supp S4 | supplementary_claims.csv:151 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1415 | +6.9 | Supp S4 | supplementary_claims.csv:151 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1416 | +20.7 | Supp S4 | supplementary_claims.csv:151 | analysis/paper_a/method_effects_summary.csv | literal line 10 | pass |
| 1417 | +3.4 | Supp S4 | supplementary_claims.csv:151 | analysis/paper_a/method_effects_summary.csv | literal line 10 | pass |
| 1418 | +97.9 | Supp S4 | supplementary_claims.csv:151 | analysis/paper_a/method_effects_summary.csv | literal line 10 | pass |
| 1419 | +11.2 | Supp S4 | supplementary_claims.csv:153 | analysis/paper_a/method_effects_summary.csv | literal line 6 | pass |
| 1420 | +0.8 | Supp S4 | supplementary_claims.csv:153 | analysis/paper_a/method_effects_summary.csv | literal line 6 | pass |
| 1421 | +22.6 | Supp S4 | supplementary_claims.csv:153 | analysis/paper_a/method_effects_summary.csv | literal line 6 | pass |
| 1422 | 0.0 | Supp S4 | supplementary_claims.csv:153 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1423 | 0.0 | Supp S4 | supplementary_claims.csv:153 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1424 | 0.0 | Supp S4 | supplementary_claims.csv:153 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1425 | +20.2 | Supp S4 | supplementary_claims.csv:154 | analysis/paper_a/method_effects_summary.csv | literal line 9 | pass |
| 1426 | -27.3 | Supp S4 | supplementary_claims.csv:139 | analysis/paper_a/method_effects_summary.csv | literal line 9 | pass |
| 1427 | +22.1 | Supp S4 | supplementary_claims.csv:139 | analysis/paper_a/method_effects_summary.csv | literal line 9 | pass |
| 1428 | +3.0 | Supp S4 | supplementary_claims.csv:154 | analysis/paper_a/method_effects_summary.csv | literal line 17 | pass |
| 1429 | -12.4 | Supp S4 | supplementary_claims.csv:154 | analysis/paper_a/method_effects_summary.csv | literal line 17 | pass |
| 1430 | +53.1 | Supp S4 | supplementary_claims.csv:154 | analysis/paper_a/method_effects_summary.csv | literal line 17 | pass |
| 1431 | 0.0 | Supp S4 | supplementary_claims.csv:155 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1432 | -7.4 | Supp S4 | supplementary_claims.csv:155 | analysis/paper_a/method_effects_summary.csv | literal line 7 | pass |
| 1433 | +9.9 | Supp S4 | supplementary_claims.csv:155 | analysis/paper_a/method_effects_summary.csv | literal line 7 | pass |
| 1434 | 0.0 | Supp S4 | supplementary_claims.csv:155 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1435 | -5.0 | Supp S4 | supplementary_claims.csv:155 | analysis/paper_a/method_effects_summary.csv | literal line 15 | pass |
| 1436 | +3.9 | Supp S4 | supplementary_claims.csv:155 | analysis/paper_a/method_effects_summary.csv | literal line 15 | pass |
| 1437 | -1.1 | Supp S4 | supplementary_claims.csv:156 | analysis/paper_a/method_effects_summary.csv | literal line 4 | pass |
| 1438 | -5.4 | Supp S4 | supplementary_claims.csv:156 | analysis/paper_a/method_effects_summary.csv | literal line 4 | pass |
| 1439 | 0.0 | Supp S4 | supplementary_claims.csv:156 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1440 | -5.8 | Supp S4 | supplementary_claims.csv:156 | analysis/paper_a/method_effects_summary.csv | literal line 12 | pass |
| 1441 | -29.1 | Supp S4 | supplementary_claims.csv:156 | analysis/paper_a/method_effects_summary.csv | literal line 12 | pass |
| 1442 | 0.0 | Supp S4 | supplementary_claims.csv:156 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1443 | +0.1 | Supp S4 | supplementary_claims.csv:157 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1444 | 0.0 | Supp S4 | supplementary_claims.csv:157 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1445 | +4.3 | Supp S4 | supplementary_claims.csv:157 | analysis/paper_a/method_effects_summary.csv | literal line 5 | pass |
| 1446 | -9.7 | Supp S4 | supplementary_claims.csv:157 | analysis/paper_a/method_effects_summary.csv | literal line 13 | pass |
| 1447 | -18.2 | Supp S4 | supplementary_claims.csv:157 | analysis/paper_a/method_effects_summary.csv | literal line 13 | pass |
| 1448 | -1.5 | Supp S4 | supplementary_claims.csv:157 | analysis/paper_a/method_effects_summary.csv | literal line 13 | pass |
| 1449 | 0.0 | Supp S4 | supplementary_claims.csv:158 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1450 | 0.0 | Supp S4 | supplementary_claims.csv:158 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1451 | 0.0 | Supp S4 | supplementary_claims.csv:158 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1452 | 0.0 | Supp S4 | supplementary_claims.csv:158 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1453 | 0.0 | Supp S4 | supplementary_claims.csv:158 | analysis/paper_a/method_effects_summary.csv | literal line 2 | pass |
| 1454 | +7.6 | Supp S4 | supplementary_claims.csv:158 | analysis/paper_a/method_effects_summary.csv | literal line 16 | pass |
| 1455 | 53 | Supp S4 | supplementary_claims.csv:148 |  | A048 | pass |
| 1456 | 35 | Supp S4 | supplementary_claims.csv:182 | results/ranges_2025-mirror.csv | literal line 70 | pass |
| 1457 | 3 | Supp S4 | supplementary_claims.csv:148 | analysis/paper_a/method_status.csv | literal line 5 | pass |
| 1458 | 36 | Supp S4 | supplementary_claims.csv:182 | analysis/paper_a/method_status.csv | literal line 3 | pass |
| 1459 | 3 | Supp S4 | supplementary_claims.csv:148 | analysis/paper_a/method_status.csv | literal line 5 | pass |
| 1460 | 15 | Supp S4 | supplementary_claims.csv:150 | analysis/paper_a/method_status.csv | literal line 2 | pass |
| 1461 | 16 | Supp S4 | supplementary_claims.csv:150 | analysis/paper_a/method_status.csv | literal line 2 | pass |
| 1462 | 15 | Supp S4 | supplementary_claims.csv:150 | analysis/paper_a/method_status.csv | literal line 2 | pass |
| 1463 | 36 | Supp S4 | supplementary_claims.csv:152 | analysis/paper_a/method_status.csv | literal line 3 | pass |
| 1464 | 32 | Supp S4 | supplementary_claims.csv:152 | analysis/paper_a/method_status.csv | literal line 3 | pass |
| 1465 | 36 | Supp S4 | supplementary_claims.csv:152 | analysis/paper_a/method_status.csv | literal line 3 | pass |
| 1466 | 3 | Supp S5 | supplementary_claims.csv:183 | analysis/paper_a/regions_in_depth.csv | literal line 12 | pass |
| 1467 | 3 | Supp S5 | supplementary_claims.csv:183 | analysis/paper_a/regions_in_depth.csv | literal line 12 | pass |
| 1468 | 66,198 | Supp S5 | supplementary_claims.csv:185 | analysis/paper_a/regions_in_depth.csv | literal line 2 | pass |
| 1469 | 46,572 | Supp S5 | supplementary_claims.csv:185 | analysis/paper_a/regions_in_depth.csv | literal line 2 | pass |
| 1470 | 4,394,612 | Supp S5 | supplementary_claims.csv:185 | analysis/population_2011/zone_population_2011_comparison.csv | literal line 4 | pass |
| 1471 | 5,401,609 | Supp S5 | supplementary_claims.csv:185 | analysis/paper_a/regions_in_depth.csv | literal line 2 | pass |
| 1472 | 7,186 | Supp S5 | supplementary_claims.csv:186 | analysis/paper_a/regions_in_depth.csv | literal line 3 | pass |
| 1473 | 6,106 | Supp S5 | supplementary_claims.csv:186 | analysis/paper_a/regions_in_depth.csv | literal line 3 | pass |
| 1474 | 95 | Supp S5 | supplementary_claims.csv:195 |  | structural (percentile label) | pass |
| 1475 | 48,520 | Supp S5 | supplementary_claims.csv:187 | analysis/paper_a/regions_in_depth.csv | literal line 2 | pass |
| 1476 | 0.491 | Supp S5 | supplementary_claims.csv:188 | qa/reports/V31c_claims.md | literal line 135 | pass |
| 1477 | 0.5 | Supp S5 | supplementary_claims.csv:189 |  | A037 note | pass |
| 1478 | 389 | Supp S5 | supplementary_claims.csv:190 | analysis/paper_a/regions_in_depth.csv | literal line 2 | pass |
| 1479 | 191 | Supp S5 | supplementary_claims.csv:190 | analysis/paper_a/regions_in_depth.csv | literal line 2 | pass |
| 1480 | 25% | Supp S5 | supplementary_claims.csv:191 | LIT:L151 | literal line 1 | pass |
| 1481 | 752,498 | Supp S5 | supplementary_claims.csv:192 | analysis/comparison_2025/movers.csv | literal line 12 | pass |
| 1482 | 905,523 | Supp S5 | supplementary_claims.csv:192 | analysis/comparison_2025/movers.csv | literal line 12 | pass |
| 1483 | 105,924 | Supp S5 | supplementary_claims.csv:192 | analysis/population_2011/zone_population_2011_comparison.csv | literal line 8 | pass |
| 1484 | 121,808 | Supp S5 | supplementary_claims.csv:192 | analysis/comparison_2025/movers.csv | literal line 12 | pass |
| 1485 | 0.482 | Supp S5 | supplementary_claims.csv:193 | claims register A344 | literal line 1 | pass |
| 1486 | 2.431 | Supp S5 | supplementary_claims.csv:194 | claims register A344 | literal line 1 | pass |
| 1487 | 1 | Supp S5 | supplementary_claims.csv:185 | analysis/population_2011/zone_population_2011_comparison.csv | literal line 18 | pass |
| 1488 | 100 | Supp S5 | supplementary_claims.csv:194 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 1489 | 1.604 | Supp S5 | supplementary_claims.csv:194 | claims register A344 | literal line 1 | pass |
| 1490 | 1,185,593 | Supp S5 | supplementary_claims.csv:195 | analysis/comparison_2025/movers.csv | literal line 7 | pass |
| 1491 | 1,533,929 | Supp S5 | supplementary_claims.csv:195 | analysis/comparison_2025/movers.csv | literal line 7 | pass |
| 1492 | 597,750 | Supp S5 | supplementary_claims.csv:195 | analysis/population_2011/zone_population_2011_comparison.csv | literal line 9 | pass |
| 1493 | 738,895 | Supp S5 | supplementary_claims.csv:195 | analysis/comparison_2025/movers.csv | literal line 7 | pass |
| 1494 | +17.8% | Supp S5 | supplementary_claims.csv:196 | analysis/paper_a/method_effects_by_region.csv | literal line 8 | pass |
| 1495 | +17.9% | Supp S5 | supplementary_claims.csv:196 | analysis/paper_a/method_effects_by_region.csv | literal line 9 | pass |
| 1496 | -15.0% | Supp S5 | supplementary_claims.csv:196 | analysis/paper_a/method_effects_by_region.csv | literal line 8 | pass |
| 1497 | 40% | Supp S5 | supplementary_claims.csv:197 | LIT:L155 | literal line 1 | pass |
| 1498 | 20% | Supp S5 | supplementary_claims.csv:185 | analysis/population_2011/zone_population_2011_comparison.csv | literal line 18 | pass |
| 1499 | 2 | Supp S5 | supplementary_claims.csv:185 | analysis/population_2011/zone_population_2011_comparison.csv | literal line 1 | pass |
| 1500 | 1.3 | Supp S5 | supplementary_claims.csv:199 | LIT:L171 | literal line 1 | pass |
| 1501 | 971,132 | Supp S5 | supplementary_claims.csv:200 | analysis/comparison_2025/movers.csv | literal line 19 | pass |
| 1502 | 1,080,065 | Supp S5 | supplementary_claims.csv:200 | analysis/comparison_2025/movers.csv | literal line 19 | pass |
| 1503 | 60,913 | Supp S5 | supplementary_claims.csv:200 | analysis/population_2011/zone_population_2011_comparison.csv | literal line 45 | pass |
| 1504 | 69,727 | Supp S5 | supplementary_claims.csv:200 | analysis/comparison_2025/movers.csv | literal line 19 | pass |
| 1505 | 0.14 | Supp S5 | supplementary_claims.csv:201 | analysis/paper_a/long_term_regions.csv | cell value 0.14 in REG:A149; rounded 14 x0.01 line 14 | pass |
| 1506 | 1 | Supp S5 | supplementary_claims.csv:200 | analysis/population_2011/zone_population_2011_comparison.csv | literal line 18 | pass |
| 1507 | 100 | Supp S5 | supplementary_claims.csv:194 | analysis/paper_a/regions_in_depth.csv | literal line 1 | pass |
| 1508 | 508,513 | Supp S5 | supplementary_claims.csv:202 | analysis/paper_a/regions_in_depth.csv | literal line 8 | pass |
| 1509 | -7.63% | Supp S5 | supplementary_claims.csv:203 | LIT:L170 | literal line 1 | pass |
| 1510 | -4.71% | Supp S5 | supplementary_claims.csv:203 | LIT:L170 | literal line 1 | pass |
| 1511 | 2,164 | Supp S5 | supplementary_claims.csv:204 | analysis/paper_a/movers-3.csv | literal line 55 | pass |
| 1512 | 28,609 | Supp S5 | supplementary_claims.csv:204 | analysis/paper_a/movers-3.csv | literal line 55 | pass |
| 1513 | 10,613 | Supp S5 | supplementary_claims.csv:204 | analysis/population_2011/zone_population_2011_comparison.csv | literal line 42 | pass |
| 1514 | 8,049 | Supp S5 | supplementary_claims.csv:204 | analysis/paper_a/movers-3.csv | literal line 55 | pass |
| 1515 | 31,361 | Supp S5 | supplementary_claims.csv:205 | ERRATA.md | literal line 22 | pass |
| 1516 | 6.5 | Supp S5 | supplementary_claims.csv:206 | analysis/paper_a/movers-3.csv | literal line 55 | pass |
| 1517 | 7,194 | Supp S5 | supplementary_claims.csv:207 | claims register A041 | literal line 1 | pass |
| 1518 | 9,031 | Supp S5 | supplementary_claims.csv:207 | claims register A041 | literal line 1 | pass |
| 1519 | 8,049 | Supp S5 | supplementary_claims.csv:204 | analysis/paper_a/movers-3.csv | literal line 55 | pass |
| 1520 | 217,967 | Supp S5 | supplementary_claims.csv:208 | analysis/comparison_2025/movers.csv | literal line 10 | pass |
| 1521 | 384,476 | Supp S5 | supplementary_claims.csv:208 | analysis/comparison_2025/movers.csv | literal line 10 | pass |
| 1522 | 57,595 | Supp S5 | supplementary_claims.csv:208 | analysis/population_2011/zone_population_2011_comparison.csv | literal line 39 | pass |
| 1523 | 59,255 | Supp S5 | supplementary_claims.csv:208 | analysis/comparison_2025/movers.csv | literal line 10 | pass |
| 1524 | 10% | Supp S6 | supplementary_claims.csv:209 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1525 | 20% | Supp S6 | supplementary_claims.csv:209 | analysis/paper_a/measures.csv | literal line 4 | pass |
| 1526 | 0.1% | Supp S6 | supplementary_claims.csv:209 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1527 | 0.2% | Supp S6 | supplementary_claims.csv:209 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1528 | 0.3% | Supp S6 | supplementary_claims.csv:209 | analysis/paper_a/measures.csv | literal line 4 | pass |
| 1529 | 10% | Supp S6 | supplementary_claims.csv:209 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1530 | 0.2% | Supp S6 | supplementary_claims.csv:209 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1531 | 10% | Supp S6 | supplementary_claims.csv:209 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1532 | 10.0% | Supp S6 | supplementary_claims.csv:211 | analysis/paper_a/measures.csv | literal line 8 | pass |
| 1533 | 0.02 | Supp S6 | supplementary_claims.csv:212 | analysis/paper_a/measures.csv | literal line 10 | pass |
| 1534 | 0.05 | Supp S6 | supplementary_claims.csv:212 | analysis/paper_a/measures.csv | literal line 11 | pass |
| 1535 | 0.007 | Supp S6 | supplementary_claims.csv:212 | analysis/paper_a/measures.csv | literal line 10 | pass |
| 1536 | 0.7% | Supp S6 | supplementary_claims.csv:212 | analysis/paper_a/measures.csv | literal line 10 | pass |
| 1537 | 2.4% | Supp S6 | supplementary_claims.csv:212 | analysis/paper_a/measures.csv | literal line 11 | pass |
| 1538 | 25% | Supp S6 | supplementary_claims.csv:213 | analysis/paper_a/measures.csv | literal line 15 | pass |
| 1539 | 10% | Supp S6 | supplementary_claims.csv:209 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1540 | 99% | Supp S6 | supplementary_claims.csv:214 | qa/reports/V31b_claims.md | literal line 3 | pass |
| 1541 | 7.5% | Supp S6 | supplementary_claims.csv:215 | analysis/paper_a/measures.csv | literal line 17 | pass |
| 1542 | 48.2 | Supp S6 | supplementary_claims.csv:215 | analysis/paper_a/measures.csv | literal line 17 | pass |
| 1543 | +16.2% | Supp S6 | supplementary_claims.csv:215 | analysis/paper_a/measures.csv | literal line 17 | pass |
| 1544 | 55.3 | Supp S6 | supplementary_claims.csv:216 | analysis/paper_a/measures.csv | literal line 13 | pass |
| 1545 | +33.2% | Supp S6 | supplementary_claims.csv:216 | analysis/paper_a/measures.csv | literal line 13 | pass |
| 1546 | 2.2% | Supp S6 | supplementary_claims.csv:216 | analysis/paper_a/measures.csv | literal line 14 | pass |
| 1547 | 156 | Supp S6 | supplementary_claims.csv:217 | analysis/paper_a/measures.csv | literal line 20 | pass |
| 1548 | +0.1% | Supp S6 | supplementary_claims.csv:217 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1549 | +0.8% | Supp S6 | supplementary_claims.csv:217 | analysis/paper_a/measures.csv | literal line 20 | pass |
| 1550 | 11.5 | Supp S6 | supplementary_claims.csv:218 | claims register A318 | literal line 1 | pass |
| 1551 | 3.1 | Supp S6 | supplementary_claims.csv:218 | claims register A318 | literal line 1 | pass |
| 1552 | 112 | Supp S6 | supplementary_claims.csv:218 | analysis/method_tests_2025/foran_poldy_balance.csv | literal line 3 | pass |
| 1553 | 8.4 | Supp S6 | supplementary_claims.csv:218 | claims register A318 | literal line 1 | pass |
| 1554 | 303 | Supp S6 | supplementary_claims.csv:218 | analysis/method_tests_2025/foran_poldy_balance.csv | literal line 8 | pass |
| 1555 | 1.60 | Supp S6 | supplementary_claims.csv:219 | claims register A273 | literal line 1 | pass |
| 1556 | 1.82 | Supp S6 | supplementary_claims.csv:220 | claims register A273 | literal line 1 | pass |
| 1557 | 1 | Supp S6 | supplementary_claims.csv:219 |  | release label 2025-store-1 (structural) | pass |
| 1558 | 10 | Supp S6 | supplementary_claims.csv:220 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 1559 | 2.60 | Supp S6 | supplementary_claims.csv:221 | claims register A273 | literal line 1 | pass |
| 1560 | 3.00 | Supp S6 | supplementary_claims.csv:221 | claims register A273 | literal line 1 | pass |
| 1561 | 20.7 | Supp S6 | supplementary_claims.csv:222 | analysis/paper_a/transfers.csv | literal line 2 | pass |
| 1562 | 19.1 | Supp S6 | supplementary_claims.csv:222 | analysis/paper_a/transfers.csv | literal line 2 | pass |
| 1563 | 1 | Supp S6 | supplementary_claims.csv:219 |  | release label 2025-store-1 (structural) | pass |
| 1564 | 10 | Supp S6 | supplementary_claims.csv:220 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 1565 | 21.5 | Supp S6 | supplementary_claims.csv:223 | analysis/paper_a/transfers.csv | literal line 4 | pass |
| 1566 | 10.8 | Supp S6 | supplementary_claims.csv:223 | analysis/paper_a/transfers.csv | literal line 4 | pass |
| 1567 | 1000 | Supp S6 | supplementary_claims.csv:224 | LIT:L173 | literal line 1 | pass |
| 1568 | 3.45 | Supp S6 | supplementary_claims.csv:226 | claims register A316 | literal line 1 | pass |
| 1569 | 1 | Supp S6 | supplementary_claims.csv:230 |  | release label 2025-store-1 (structural) | pass |
| 1570 | 10 | Supp S6 | supplementary_claims.csv:220 | analysis/paper_a/shocks_summary.csv | literal line 4 | pass |
| 1571 | 2.95 | Supp S6 | supplementary_claims.csv:226 | claims register A316 | literal line 1 | pass |
| 1572 | 1 | Supp S6 | supplementary_claims.csv:230 |  | release label 2025-store-1 (structural) | pass |
| 1573 | 20 | Supp S6 | supplementary_claims.csv:230 | analysis/reliability_2025/years.csv | literal line 66 | pass |
| 1574 | 593 | Supp S6 | supplementary_claims.csv:227 | claims register A319 | literal line 1 | pass |
| 1575 | 641 | Supp S6 | supplementary_claims.csv:227 | claims register A319 | literal line 1 | pass |
| 1576 | 12 | Supp S6 | supplementary_claims.csv:228 | analysis/method_tests_2025/foran_poldy_balance.csv | literal line 19 | pass |
| 1577 | 17 | Supp S6 | supplementary_claims.csv:230 | analysis/reliability_2025/years.csv | literal line 18 | pass |
| 1578 | 4.4 | Supp S6 | supplementary_claims.csv:229 | claims register A320 | literal line 1 | pass |
| 1579 | 43.5 | Supp S6 | supplementary_claims.csv:230 | analysis/reliability_2025/years.csv | cell value 43.5 in REG:A317; rounded 43482098 x1e-06 line 82 | pass |
| 1580 | 55.4 | Supp S6 | supplementary_claims.csv:230 | analysis/reliability_2025/years.csv | cell value 55.4 in REG:A317; rounded 55369977 x1e-06 line 130 | pass |
| 1581 | 100 | Supp S6 | supplementary_claims.csv:231 | analysis/resilience_2025/tables.csv | literal line 1 | pass |
| 1582 | 0.46 | Supp S6 | supplementary_claims.csv:233 | analysis/resilience_2025/tables.csv | cell value 0.46 in analysis/resilience_2025/tables.csv; rounded 46 x0.01 line 1 | pass |
| 1583 | 0.30 | Supp S6 | supplementary_claims.csv:231 | analysis/resilience_2025/tables.csv | cell value 0.30 in analysis/resilience_2025/tables.csv; rounded 30 x0.01 line 1 | pass |
| 1584 | 0.22 | Supp S6 | supplementary_claims.csv:231 | analysis/resilience_2025/tables.csv | cell value 0.22 in analysis/resilience_2025/tables.csv; rounded 22 x0.01 line 1 | pass |
| 1585 | 0.35 | Supp S6 | supplementary_claims.csv:231 | analysis/resilience_2025/tables.csv | cell value 0.35 in analysis/resilience_2025/tables.csv; rounded 35 x0.01 line 1 | pass |
| 1586 | 0.35 | Supp S6 | supplementary_claims.csv:231 | analysis/resilience_2025/tables.csv | cell value 0.35 in analysis/resilience_2025/tables.csv; rounded 35 x0.01 line 1 | pass |
| 1587 | 0.47 | Supp S6 | supplementary_claims.csv:232 | analysis/resilience_2025/tables.csv | cell value 0.47 in analysis/resilience_2025/tables.csv; rounded 47 x0.01 line 1 | pass |
| 1588 | 0.67 | Supp S6 | supplementary_claims.csv:232 | analysis/resilience_2025/tables.csv | cell value 0.67 in analysis/resilience_2025/tables.csv; rounded 67 x0.01 line 1 | pass |
| 1589 | 94% | Supp S6 | supplementary_claims.csv:234 |  | as above; A326 | pass |
| 1590 | 1 | Supp S6 | none |  | release label 2025-store-1 (structural) | pass |
| 1591 | 2 | Supp S6 | supplementary_claims.csv:236 |  | release label 2025-store-2 (structural) | pass |
| 1592 | 156 | Supp S6 | supplementary_claims.csv:236 | analysis/paper_a/measures.csv | literal line 20 | pass |
| 1593 | +0.1% | Supp S6 | supplementary_claims.csv:236 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1594 | 0% | Supp S6 | supplementary_claims.csv:236 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1595 | +0.78% | Supp S6 | supplementary_claims.csv:236 | analysis/paper_a/scenarios_by_region.csv | literal line 30 | pass |
| 1596 | +0.8% | Supp S6 | supplementary_claims.csv:236 | analysis/paper_a/measures.csv | literal line 20 | pass |
| 1597 | 41.5 | Supp S6 | supplementary_claims.csv:237 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1598 | 15.6 | Supp S6 | supplementary_claims.csv:237 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1599 | +10% | Supp S6 | supplementary_claims.csv:238 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1600 | 41.5 | Supp S6 | supplementary_claims.csv:238 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1601 | +0.1% | Supp S6 | supplementary_claims.csv:238 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1602 | 15.7 | Supp S6 | supplementary_claims.csv:238 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1603 | +0.2% | Supp S6 | supplementary_claims.csv:238 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1604 | +20% | Supp S6 | supplementary_claims.csv:239 | analysis/paper_a/measures.csv | literal line 4 | pass |
| 1605 | 41.5 | Supp S6 | supplementary_claims.csv:238 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1606 | +0.1% | Supp S6 | supplementary_claims.csv:238 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1607 | 15.7 | Supp S6 | supplementary_claims.csv:238 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1608 | +0.3% | Supp S6 | supplementary_claims.csv:239 | analysis/paper_a/measures.csv | literal line 4 | pass |
| 1609 | +10% | Supp S6 | supplementary_claims.csv:240 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1610 | 41.5 | Supp S6 | supplementary_claims.csv:240 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1611 | 0.0% | Supp S6 | supplementary_claims.csv:240 | analysis/paper_a/measures.csv | literal line 5 | pass |
| 1612 | 15.6 | Supp S6 | supplementary_claims.csv:240 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1613 | +0.2% | Supp S6 | supplementary_claims.csv:240 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1614 | +10% | Supp S6 | supplementary_claims.csv:241 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1615 | 45.5 | Supp S6 | supplementary_claims.csv:241 | analysis/paper_a/measures.csv | literal line 6 | pass |
| 1616 | +9.7% | Supp S6 | supplementary_claims.csv:241 | analysis/paper_a/measures.csv | literal line 6 | pass |
| 1617 | 17.1 | Supp S6 | supplementary_claims.csv:241 | analysis/paper_a/measures.csv | literal line 6 | pass |
| 1618 | +9.4% | Supp S6 | supplementary_claims.csv:241 | analysis/paper_a/measures.csv | literal line 6 | pass |
| 1619 | +20% | Supp S6 | supplementary_claims.csv:242 | analysis/paper_a/measures.csv | literal line 4 | pass |
| 1620 | 49.6 | Supp S6 | supplementary_claims.csv:242 | analysis/paper_a/measures.csv | literal line 7 | pass |
| 1621 | +19.4% | Supp S6 | supplementary_claims.csv:242 | analysis/paper_a/measures.csv | literal line 7 | pass |
| 1622 | 18.6 | Supp S6 | supplementary_claims.csv:242 | analysis/paper_a/measures.csv | literal line 7 | pass |
| 1623 | +18.8% | Supp S6 | supplementary_claims.csv:242 | analysis/paper_a/measures.csv | literal line 7 | pass |
| 1624 | +10% | Supp S6 | supplementary_claims.csv:243 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1625 | 45.7 | Supp S6 | supplementary_claims.csv:243 | analysis/paper_a/measures.csv | literal line 8 | pass |
| 1626 | +10.0% | Supp S6 | supplementary_claims.csv:243 | analysis/paper_a/measures.csv | literal line 8 | pass |
| 1627 | 17.2 | Supp S6 | supplementary_claims.csv:243 | analysis/paper_a/measures.csv | literal line 8 | pass |
| 1628 | +10.0% | Supp S6 | supplementary_claims.csv:243 | analysis/paper_a/measures.csv | literal line 8 | pass |
| 1629 | 41.5 | Supp S6 | supplementary_claims.csv:244 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1630 | 0.0% | Supp S6 | supplementary_claims.csv:244 | analysis/paper_a/measures.csv | literal line 5 | pass |
| 1631 | 24.9 | Supp S6 | supplementary_claims.csv:244 | analysis/paper_a/measures.csv | literal line 9 | pass |
| 1632 | +59.7% | Supp S6 | supplementary_claims.csv:244 | analysis/paper_a/measures.csv | literal line 9 | pass |
| 1633 | 0.02 | Supp S6 | supplementary_claims.csv:245 | analysis/paper_a/measures.csv | literal line 10 | pass |
| 1634 | 0.007 | Supp S6 | supplementary_claims.csv:245 | analysis/paper_a/measures.csv | literal line 10 | pass |
| 1635 | 41.8 | Supp S6 | supplementary_claims.csv:245 | analysis/paper_a/measures.csv | literal line 10 | pass |
| 1636 | +0.7% | Supp S6 | supplementary_claims.csv:245 | analysis/paper_a/measures.csv | literal line 10 | pass |
| 1637 | 15.7 | Supp S6 | supplementary_claims.csv:245 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1638 | +0.7% | Supp S6 | supplementary_claims.csv:245 | analysis/paper_a/measures.csv | literal line 10 | pass |
| 1639 | 0.05 | Supp S6 | supplementary_claims.csv:246 | analysis/paper_a/measures.csv | literal line 11 | pass |
| 1640 | 0.007 | Supp S6 | supplementary_claims.csv:245 | analysis/paper_a/measures.csv | literal line 10 | pass |
| 1641 | 42.5 | Supp S6 | supplementary_claims.csv:246 | analysis/paper_a/measures.csv | literal line 11 | pass |
| 1642 | +2.4% | Supp S6 | supplementary_claims.csv:246 | analysis/paper_a/measures.csv | literal line 11 | pass |
| 1643 | 16.0 | Supp S6 | supplementary_claims.csv:246 | analysis/paper_a/measures.csv | literal line 11 | pass |
| 1644 | +2.4% | Supp S6 | supplementary_claims.csv:246 | analysis/paper_a/measures.csv | literal line 11 | pass |
| 1645 | 6% | Supp S6 | supplementary_claims.csv:247 | analysis/paper_a/measures.csv | literal line 12 | pass |
| 1646 | 48.3 | Supp S6 | supplementary_claims.csv:247 | analysis/paper_a/measures.csv | literal line 12 | pass |
| 1647 | +16.4% | Supp S6 | supplementary_claims.csv:247 | analysis/paper_a/measures.csv | literal line 12 | pass |
| 1648 | 14.3 | Supp S6 | supplementary_claims.csv:247 | analysis/paper_a/measures.csv | literal line 12 | pass |
| 1649 | -8.2% | Supp S6 | supplementary_claims.csv:247 | analysis/paper_a/measures.csv | literal line 12 | pass |
| 1650 | 55.3 | Supp S6 | supplementary_claims.csv:248 | analysis/paper_a/measures.csv | literal line 13 | pass |
| 1651 | +33.2% | Supp S6 | supplementary_claims.csv:248 | analysis/paper_a/measures.csv | literal line 13 | pass |
| 1652 | 15.6 | Supp S6 | supplementary_claims.csv:248 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1653 | 0.0% | Supp S6 | supplementary_claims.csv:248 | analysis/paper_a/measures.csv | literal line 5 | pass |
| 1654 | 42.4 | Supp S6 | supplementary_claims.csv:249 | analysis/paper_a/measures.csv | literal line 14 | pass |
| 1655 | +2.2% | Supp S6 | supplementary_claims.csv:249 | analysis/paper_a/measures.csv | literal line 14 | pass |
| 1656 | 15.6 | Supp S6 | supplementary_claims.csv:249 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1657 | 0.0% | Supp S6 | supplementary_claims.csv:249 | analysis/paper_a/measures.csv | literal line 5 | pass |
| 1658 | +25% | Supp S6 | supplementary_claims.csv:250 | analysis/paper_a/measures.csv | literal line 15 | pass |
| 1659 | 41.5 | Supp S6 | supplementary_claims.csv:250 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1660 | 0.0% | Supp S6 | supplementary_claims.csv:250 | analysis/paper_a/measures.csv | literal line 5 | pass |
| 1661 | 15.6 | Supp S6 | supplementary_claims.csv:250 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1662 | 0.0% | Supp S6 | supplementary_claims.csv:250 | analysis/paper_a/measures.csv | literal line 5 | pass |
| 1663 | 45.1 | Supp S6 | supplementary_claims.csv:251 | analysis/paper_a/measures.csv | literal line 16 | pass |
| 1664 | +8.7% | Supp S6 | supplementary_claims.csv:251 | analysis/paper_a/measures.csv | literal line 16 | pass |
| 1665 | 17.0 | Supp S6 | supplementary_claims.csv:251 | analysis/paper_a/measures.csv | literal line 16 | pass |
| 1666 | +8.7% | Supp S6 | supplementary_claims.csv:251 | analysis/paper_a/measures.csv | literal line 16 | pass |
| 1667 | 7.5% | Supp S6 | supplementary_claims.csv:252 | analysis/paper_a/measures.csv | literal line 17 | pass |
| 1668 | 48.2 | Supp S6 | supplementary_claims.csv:252 | analysis/paper_a/measures.csv | literal line 17 | pass |
| 1669 | +16.2% | Supp S6 | supplementary_claims.csv:252 | analysis/paper_a/measures.csv | literal line 17 | pass |
| 1670 | 15.6 | Supp S6 | supplementary_claims.csv:252 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1671 | 0.0% | Supp S6 | supplementary_claims.csv:252 | analysis/paper_a/measures.csv | literal line 5 | pass |
| 1672 | 5% | Supp S6 | supplementary_claims.csv:252 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 1673 | 76.8 | Supp S6 | supplementary_claims.csv:253 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 1674 | +85.0% | Supp S6 | supplementary_claims.csv:253 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 1675 | 19.6 | Supp S6 | supplementary_claims.csv:253 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 1676 | +25.7% | Supp S6 | supplementary_claims.csv:253 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 1677 | 30% | Supp S6 | supplementary_claims.csv:254 | analysis/paper_a/measures.csv | literal line 19 | pass |
| 1678 | 64.6 | Supp S6 | supplementary_claims.csv:254 | analysis/paper_a/measures.csv | literal line 19 | pass |
| 1679 | +55.6% | Supp S6 | supplementary_claims.csv:254 | analysis/paper_a/measures.csv | literal line 19 | pass |
| 1680 | 18.5 | Supp S6 | supplementary_claims.csv:254 | analysis/paper_a/measures.csv | literal line 19 | pass |
| 1681 | +18.6% | Supp S6 | supplementary_claims.csv:254 | analysis/paper_a/measures.csv | literal line 7 | pass |
| 1682 | 156 | Supp S6 | supplementary_claims.csv:255 | analysis/paper_a/measures.csv | literal line 20 | pass |
| 1683 | 41.5 | Supp S6 | supplementary_claims.csv:255 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1684 | +0.1% | Supp S6 | supplementary_claims.csv:255 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1685 | 15.7 | Supp S6 | supplementary_claims.csv:255 | analysis/paper_a/measures.csv | literal line 3 | pass |
| 1686 | +0.8% | Supp S6 | supplementary_claims.csv:255 | analysis/paper_a/measures.csv | literal line 20 | pass |
| 1687 | 1 | Supp S6 | supplementary_claims.csv:220 |  | release label 2025-store-1 (structural) | pass |
| 1688 | 41.5 | Supp S6 | supplementary_claims.csv:256 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1689 | 0.0% | Supp S6 | supplementary_claims.csv:256 | analysis/paper_a/measures.csv | literal line 5 | pass |
| 1690 | 23.2 | Supp S6 | supplementary_claims.csv:256 | analysis/paper_a/measures.csv | literal line 21 | pass |
| 1691 | +48.4% | Supp S6 | supplementary_claims.csv:256 | analysis/paper_a/measures.csv | literal line 21 | pass |
| 1692 | 2 | Supp S6 | none |  | release label 2025-store-2 (structural) | pass |
| 1693 | 41.5 | Supp S6 | supplementary_claims.csv:257 | analysis/paper_a/measures.csv | literal line 2 | pass |
| 1694 | 0.0% | Supp S6 | supplementary_claims.csv:257 | analysis/paper_a/measures.csv | literal line 5 | pass |
| 1695 | 25.7 | Supp S6 | supplementary_claims.csv:257 | analysis/paper_a/measures.csv | literal line 18 | pass |
| 1696 | +64.5% | Supp S6 | supplementary_claims.csv:257 | analysis/paper_a/measures.csv | literal line 22 | pass |
| 1697 | 37% | Supp S7 | supplementary_claims.csv:258 | analysis/scale_curve_2025/diet_scale.csv | literal line 30 | pass |
| 1698 | 33% | Supp S7 | supplementary_claims.csv:259 | analysis/scale_curve_2025/diet_scale.csv | literal line 11 | pass |
| 1699 | 2.5% | Supp S7 | supplementary_claims.csv:260 | analysis/scale_curve_2025/diet_scale.csv | literal line 3 | pass |
| 1700 | 45% | Supp S7 | supplementary_claims.csv:259 | analysis/scale_curve_2025/diet_scale.csv | literal line 21 | pass |
| 1701 | 2.5% | Supp S7 | supplementary_claims.csv:260 | analysis/scale_curve_2025/diet_scale.csv | literal line 3 | pass |
| 1702 | 95% | Supp S7 | supplementary_claims.csv:260 | analysis/scale_curve_2025/diet_scale.csv | literal line 27 | pass |
| 1703 | +62% | Supp S7 | supplementary_claims.csv:261 | qa/reports/V31d_claims.md | literal line 119 | pass |
| 1704 | 53.6 | Supp S7 | supplementary_claims.csv:261 | qa/reports/V31d_claims.md | literal line 119 | pass |
| 1705 | 86.9 | Supp S7 | supplementary_claims.csv:261 | qa/reports/V31d_claims.md | literal line 119 | pass |
| 1706 | 7% | Supp S7 | supplementary_claims.csv:262 | claims register A141 | literal line 1 | pass |
| 1707 | 60 | Supp S8 | supplementary_claims.csv:264 | claims register A331 | literal line 1 | pass |
| 1708 | 135 | Supp S8 | supplementary_claims.csv:265 |  | qa/sources_register.csv D56 ("135 Yield sheet rows x 60 zones") | pass |
| 1709 | 30 | Supp S8 | supplementary_claims.csv:274 | results/ranges_2025-mirror.csv | literal line 60 | pass |
| 1710 | 5.4 | Supp S8 | none |  | qa/reports/V36_check_B110.md section 3 point 1 ("CLUM 5.4") | pass |
| 1711 | 30 | Supp S8 | supplementary_claims.csv:274 | results/ranges_2025-mirror.csv | literal line 60 | pass |
| 1712 | 22,326,388 | Supp S8 | supplementary_claims.csv:275 | ERRATA.md | literal line 20 | pass |
| 1713 | 53 | Supp S8 | none |  | A048 | pass |
| 1714 | 22,336,514 | Supp S8 | none |  | qa/reports/V36_check_B110.md section 3 ("sum to 22,336,514") | pass |
| 1715 | 27,608,200 | Supp S8 | none |  | results/2025-fixed.csv zone 1 population 27608200 | pass |
| 1716 | 3,639,794 | Supp S8 | supplementary_claims.csv:276 | analysis/land_2011/README.md | literal line 12 | pass |
| 1717 | 3,318,689 | Supp S8 | supplementary_claims.csv:276 | analysis/land_2011/README.md | literal line 54 | pass |
| 1718 | 8 | Supp S8 | supplementary_claims.csv:277 | analysis/sensitivity_2025/README.md | literal line 34 | pass |
| 1719 | 50 | Supp S8 | supplementary_claims.csv:277 | analysis/sensitivity_2025/README.md | literal line 19 | pass |
| 1720 | 0.599 | Supp S8 | supplementary_claims.csv:282 | results/ranges_2025-fixed.csv | cell value 0.599 in qa/reports/B112_shock_ranges.md; rounded 598600 x1e-06 line 107 | pass |
| 1721 | 20 | Supp S8 | supplementary_claims.csv:282 | results/ranges_2025-fixed.csv | literal line 40 | pass |
| 1722 | 1860 | Supp S8 | none |  | sources register / B112 section 3 (ABS Historic Agricultural Commodities 1860 to 2022) | pass |
| 1723 | 153 | Supp S8 | none |  | qa/reports/V38_check_B112.md (153 seasons); B112 section 3 | pass |
| 1724 | 0.634 | Supp S8 | supplementary_claims.csv:269 | qa/reports/B112_shock_ranges.md | literal line 33 | pass |
| 1725 | 20 | Supp S8 | supplementary_claims.csv:282 | results/ranges_2025-fixed.csv | literal line 40 | pass |
| 1726 | 3 | Supp S8 | supplementary_claims.csv:283 | results/scale_curve.csv | literal line 7 | pass |
| 1727 | 2,450 | Supp S8 | none |  | results/scale_curve.csv units 2450 (A104) | pass |
| 1728 | 336 | Supp S8 | supplementary_claims.csv:283 | results/scale_curve.csv | literal line 7 | pass |
| 1729 | 89 | Supp S8 | supplementary_claims.csv:283 | results/scale_curve.csv | literal line 6 | pass |
| 1730 | 27,608,200 | Supp S8 | supplementary_claims.csv:268 |  | results/2025-fixed.csv zone 1 population 27608200 | pass |
| 1731 | 27,608,200 | Supp S8 | supplementary_claims.csv:268 |  | results/2025-fixed.csv zone 1 population 27608200 | pass |
| 1732 | 41,503,537 | Supp S8 | supplementary_claims.csv:268 | results/comparison_cells.csv | literal line 2 | pass |
| 1733 | 0.665 | Supp S8 | supplementary_claims.csv:268 |  | analysis/paper_a/shocks_ranges.csv line 2 population_over_capacity_central 0.665 | pass |
| 1734 | 0.742 | Supp S8 | supplementary_claims.csv:269 | results/ranges_2025-fixed.csv | literal line 42 | pass |
| 1735 | 10 | Supp S8 | supplementary_claims.csv:269 | results/ranges_2025-fixed.csv | literal line 20 | pass |
| 1736 | 0.634 | Supp S8 | supplementary_claims.csv:269 | qa/reports/B112_shock_ranges.md | literal line 33 | pass |
| 1737 | 20 | Supp S8 | supplementary_claims.csv:269 | results/ranges_2025-fixed.csv | literal line 40 | pass |
| 1738 | 0.665 | Supp S8 | supplementary_claims.csv:268 |  | analysis/paper_a/shocks_ranges.csv line 2 population_over_capacity_central 0.665 | pass |
| 1739 | 10 | Supp S8 | supplementary_claims.csv:269 | results/ranges_2025-fixed.csv | literal line 20 | pass |
| 1740 | 10 | Supp S8 | supplementary_claims.csv:269 | results/ranges_2025-fixed.csv | literal line 20 | pass |
| 1741 | 0.742 | Supp S8 | supplementary_claims.csv:269 | results/ranges_2025-fixed.csv | literal line 42 | pass |
| 1742 | 0.665 | Supp S8 | supplementary_claims.csv:268 |  | analysis/paper_a/shocks_ranges.csv line 2 population_over_capacity_central 0.665 | pass |
| 1743 | 0.742 | Supp S8 | supplementary_claims.csv:269 | results/ranges_2025-fixed.csv | literal line 42 | pass |
| 1744 | 0.634 | Supp S8 | supplementary_claims.csv:269 | qa/reports/B112_shock_ranges.md | literal line 33 | pass |
| 1745 | 17.1 | Supp S8 | supplementary_claims.csv:270 |  | B124 line 18 prints 17.14 years; drafter arithmetic; no checker report (B124 itself says the row needs a checker) | pass (builder only) |
| 1746 | 5.8% | Supp S8 | supplementary_claims.csv:271 | analysis/method_tests_2025/fearnside_failure_curve.csv | literal line 3 | pass |
| 1747 | 1 | Supp S8 | supplementary_claims.csv:269 | results/ranges_2025-fixed.csv | literal line 2 | pass |
| 1748 | 17 | Supp S8 | supplementary_claims.csv:270 |  | R03a issue 11 prints "about 1 in 17"; B124 line 18 | pass |
| 1749 | 5.8 | Supp S8 | supplementary_claims.csv:271 | analysis/method_tests_2025/fearnside_failure_curve.csv | literal line 3 | pass |
| 1750 | 6.1% | Supp S8 | supplementary_claims.csv:272 | analysis/method_tests_2025/fearnside_failure_curve.csv | literal line 3 | pass |
| 1751 | 10 | Supp S8 | supplementary_claims.csv:269 | results/ranges_2025-fixed.csv | literal line 20 | pass |
| 1752 | 20 | Supp S8 | supplementary_claims.csv:269 | results/ranges_2025-fixed.csv | literal line 40 | pass |
| 1753 | 30.81 | Supp S8 | supplementary_claims.csv:272 | analysis/method_tests_2025/fearnside_failure_curve.csv | literal line 3 | pass |
| 1754 | 26.32 | Supp S8 | supplementary_claims.csv:272 | analysis/method_tests_2025/fearnside_failure_curve.csv | literal line 3 | pass |
| 1755 | 16.4 | Supp S8 | supplementary_claims.csv:272 | qa/reports/B124_paper_A_widened_shocks_and_trim.md | literal line 24 | pass |
| 1756 | 6.1% | Supp S8 | supplementary_claims.csv:272 | analysis/method_tests_2025/fearnside_failure_curve.csv | literal line 3 | pass |
| 1757 | 17.1 | Supp S8 | supplementary_claims.csv:270 |  | B124 line 18 prints 17.14 years; drafter arithmetic; no checker report (B124 itself says the row needs a checker) | pass (builder only) |
| 1758 | 5.8% | Supp S8 | supplementary_claims.csv:271 | analysis/method_tests_2025/fearnside_failure_curve.csv | literal line 3 | pass |
| 1759 | 5.8% | Supp S8 | supplementary_claims.csv:271 | analysis/method_tests_2025/fearnside_failure_curve.csv | literal line 3 | pass |
| 1760 | 22 | Supp S9 | supplementary_claims.csv:284 | LIT:L224 | literal line 1 | pass |
| 1761 | 40 | Supp S9 | supplementary_claims.csv:284 | LIT:L224 | literal line 1 | pass |
| 1762 | 40 | Supp S9 | supplementary_claims.csv:284 | LIT:L224 | literal line 1 | pass |
| 1763 | 60 | Supp S9 | supplementary_claims.csv:286 | LIT:L136 | literal line 1 | pass |
