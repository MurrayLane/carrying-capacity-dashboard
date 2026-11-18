# B124: Paper A carries the widened shocked ranges; failure probability reconciled; trimmed to 7,950

Brief: `qa/briefs/B124_paper_A_widened_shocks_and_trim.md`. No git, no subagents, no network. Written only under `papers/A_results/` and this report. `paper_A_draft1.md`, `references.md`, Paper B and every register were not touched (the assembled draft is therefore stale until the coordinator reassembles).

## 1. Sentences changed (before; after)

**Section 8.1 (`draft/A_s05-08.md`).**
Before: "At the base settings the margin is above balance at 1 in 10 and below it at 1 in 20 in both data years, but the settings decide the sign. Across the 5th to 95th percentile of the original 13-choice range, 2025 capacity is 27.0 to 34.0 million at 1 in 10 (central 30.8) and 23.0 to 29.0 million at 1 in 20 (central 26.3). The population of 27.6 million lies inside both, and the 19-choice range of section 9 is wider at both ends. With the meat window restricted to the four windows that span a full herd cycle, the ranges narrow to 29.2 to 32.5 million at 1 in 10, above the population in every draw, and 25.0 to 27.8 million at 1 in 20, below it in about 92% of draws."
After: "At the base settings the margin is above balance at 1 in 10 and below it at 1 in 20 in both data years, but across the spread of settings both outcomes lie inside the range. The 5th to 95th percentile of 2025 capacity on the 19 choices of section 9 is 23.1 to 36.5 million at 1 in 10 (central 30.8; 0.84 to 1.32 times the population) and 19.7 to 31.2 million at 1 in 20 (central 26.3; 0.72 to 1.13 times). The population of 27.6 million lies inside both: 37% of the draws are below it at 1 in 10 and 78% at 1 in 20, against 0.45% in an average year. The ranges on the 13-choice draws and on the four full herd-cycle meat windows are in Supplementary Table S9. The regional tipping counts of section 9 stand on the 13-choice zone ranges, because the widened draws are national and state only."
The "1 in 20 is not a threshold" and failure-probability sentences are unchanged. I did not add "in every year's data" to the base-settings sentence: B123 gives no shocked figure by data year, so nothing supports it (the single-year check A317 is about capacity, flagged unverified). The sentence says "at the base settings", as before. Coordinator: say if you want the phrase.

**Supplement Table S9 and its caption and paragraph (`draft/supplementary.md`).** A 19-choice column is added (23.1 to 36.5 (0.84 to 1.32); 19.7 to 31.2 (0.72 to 1.13)) beside the 13-choice and herd-cycle columns, and the caption names the 19-choice range as the headline and the others as labelled alternatives. Before: "On the 13-choice range 27.6 million lies inside both ranges. ... The 19-choice range is wider than the 13-choice range at both ends (31.1 against 36.3 and 49.2 against 45.8), so 27.6 million lies inside its shocked ranges as well. By region, ..." After: "On the 19-choice range 27.6 million lies inside both ranges: 37% of the draws are below it at 1 in 10 and 78% at 1 in 20, against 0.45% in an average year. It also lies inside both 13-choice ranges. On the four full-cycle windows every draw at 1 in 10 is above 27.6 million, and at 1 in 20 about 92% of draws are below it. The regional counts that follow are on the 13-choice zone ranges, because the 19-choice draws are national and state only. By region, ..." No other number changed.

**Drafter notes** (not counted): conflicts 1, 3 and 6 rewritten (the shocked 19-choice figures exist; the own-table alternative 22.5 to 35.9 and 19.1 to 30.5 is B123's, not printed; the failure probability is reconciled); a B124 block appended. `SECTION_SCOPE.md` (lines 14, 476, 867) and `OUTLINE.md` (line 8, headline) refreshed.

## 2. Failure probability

**Paper A (B117, supplement S8).** Weather factor needed to feed 27,608,200 people: 27,608,200 / 41,503,537 = 0.6652. The model's resilience table gives 0.742361 at 10 years and 0.634262 at 20 years and interpolates in a straight line in the return period, so T = 10 + 10 x (0.742361 - 0.6652) / (0.742361 - 0.634262) = 17.14 years; 1/T = 5.83%. Release 2025-fixed, return periods 10 and 20, straight line in T.

**Paper B (5.8 to 6.1%; claim B130).** `analysis/method_tests_2025/fearnside_failure_curve.py`, row 2025-fixed of `fearnside_failure_curve.csv` ("17 to 16" years; "5.8 to 6.1" %). Same release (2025-fixed), same population (27.6082 million), same bracket (capacity 30.81 million at 10 years, 26.32 at 20; `analysis/comparators_2025/rerun.csv`). The script reads the return period two ways: linear in T gives f = (30.81 - 27.6082) / (30.81 - 26.32) = 0.7131, T = 17.13 years, 5.84%; linear in log T gives T = exp(ln 10 + 0.7131 ln 2) = 16.39 years, 6.10%. Paper B prints the pair as a range. I recomputed both (5.837% and 6.100%).

**So the two figures agree:** 5.8% is Paper A's figure and the lower end of Paper B's; 6.1% is Paper B's logarithmic reading. Neither is wrong. Paper A uses the straight-line reading because it is the rule of the model's own table. **No B job is needed for the figure;** if Paper B is to be tidied, its S3.6 could say "linear in the return period, 5.8%; linear in its logarithm, 6.1%" (optional).

**Sentence written (supplement S8, inserted before "It rests on the cereal factor"):** "Paper B reports 5.8 to 6.1% because it also reads the capacities at 10 and 20 years (30.81 and 26.32 million) linearly in the logarithm of the return period, which gives 16.4 years and 6.1%; reading them linearly in the return period, the rule of the model's own table, gives 17.1 years and 5.8%, the figure used here, so the two papers agree and 5.8% is the lower end of Paper B's range." New claim row in `supplementary_claims.csv` (S8, needs a checker). Main text (8.1, 12) keeps "about 5.8% a year, 1 in 17".

## 3. Trim

Words by `python3 qa/tools/wordcount.py A`: **before 8,080** (B117's count; 8,105 after the widened sentences were added) **after 7,943** (limit 7,950). Per section after: 1: 646, 2: 654, 3: 602, 4: 697, 5: 660, 6: 422, 7: 560, 8: 948, 9: 763, 10: 521, 11: 837, 12: 637.

Cut or shortened (no number outside the tables or supplement was removed; every removed figure remains in a table or the supplement):
* Section 2, weather-allowance paragraph: "Each region takes its state's factor (section 8)." (section 8's opening says it).
* Section 2, last paragraph: "The regional ranges that test the flips come from the first 13 choices (12 vary)." (9.1 and 8.1 say it).
* Section 3: "The count of regions over capacity is therefore not a finding on its own." (the sentence before says it); ", so the national margin held its multiple" (the next sentence says it); in the cautions, "Five zones carry older 2011 boundaries." (section 12 says it) and "The land-definition flag is a fixed threshold at 2 and 0.5 times." (the test is stated above with both thresholds).
* Section 8.1: the 15th-worst and 8th-worst ranks replaced by "(section 2; Supplementary Section S4 ranks its factors in the 153 seasons)" (S4 carries the ranks and their claim rows); "(18.9 million in 2025)" after the 1-in-100 ratios (Table 6 carries it); "This holds capacity fixed and projects nothing." (the sentence before says so).
* Section 8.2: "The share rose to 85% at 1 in 10 in both years and to about 91% at 1 in 100 in 2011 and 91% in 2025." replaced by "Table 6 gives the shares at each return period."
* Section 8.3: "The grain stores applied the resilience tables of the frozen store releases (...), so they rest on the same cereal factor." (section 2 names the store releases; 11.4 says both rest on the cereal factor).
* Section 9: "Supplementary Section S4 gives the shares of the variance." (9.1 cites it earlier).
* Section 10: "Those four regions show what the counts mean on the ground."
* Section 11: "The store is free in the model." (the section opening says each measure is free of cost); in 11.7 "Each measure was applied alone, so the effects are not additive" shortened to "The effects are not additive" (the opening says each was applied alone).

Claims rows removed for cut fragments: 4 in `A_s01-04_claims.csv`, 12 in `A_s05-08_claims.csv` (replaced by 7 new rows for the widened sentences), 1 in `A_s09-12_claims.csv` (one wording changed). No caveat the checkers asked for was cut (the cereal factor, the crop-only bound, the 13-choice zone ranges, the flip-test limits stay).

## 4. Register rows the coordinator must change

| id | before | after |
|---|---|---|
| A014 | 30.8 (pending note 27.0 to 34.0 or 29.2 to 32.5) | 30.8; range 23.1 to 36.5 million on the 19 choices (B123; 23.0989 to 36.5018) |
| A183 | 1.12 (pending 0.98 to 1.23) | 1.12; capacity over population 0.84 to 1.32 (0.837 to 1.322) |
| A187 | 0.95 (pending 0.83 to 1.05) | 0.95; 0.72 to 1.13 (0.715 to 1.130) |
| A195 | 26.3 (23.0 to 29.0; 25.0 to 27.8) | 26.3; 19.7 to 31.2 |
| A196 | 0.89; 0.95 (pending: straddles on the 13-choice range; 92% below on herd-cycle) | base holds; across the spread of settings both outcomes lie inside the range: 37.0% of draws below 27.6 million at 1 in 10, 77.65% (78%) at 1 in 20, 0.45% in an average year |
| A390, A391, A392 | the 13-choice ranges | unchanged; now cited in Supplementary Table S9 as labelled alternatives |
| A038, A184, A188, A402 | regional counts on the 13-choice zone ranges | unchanged; the text says they stand on the 13-choice zone ranges (no regional widened draws, B123) |
| new | none | the 0.45% and 37% and 78% shares; the 8,7 to 8,10 sentences (ranges, inside both, Table S9 pointer, regional counts basis); the S8 sentence on Paper B's log reading (derivation by the drafter, needs a checker) |
| B130 (Paper B) | 5.8 to 6.1% | no change; its basis is the two interpolation rules above |
| A027/A028 | widened national average-year range | no change |

All widened-range claim rows say "checker pending V44".

## 5. Files changed

`papers/A_results/draft/A_s01-04.md`, `A_s05-08.md`, `A_s09-12.md`, `supplementary.md`; `A_s01-04_claims.csv`, `A_s05-08_claims.csv`, `A_s09-12_claims.csv`, `supplementary_claims.csv`; `papers/A_results/SECTION_SCOPE.md`, `OUTLINE.md`; this report. Not changed: `highlights.md` (its line "Base capacity is above population at 1 in 10, below at 1 in 20; ranges include it" still holds), `paper_A_draft1.md`, `references.md`.

## Wrong-value check

*Example, a deliberate wrong value:* the 13-choice lower end at 1 in 10, 27.0 million, quoted as if it were the widened figure. Against `analysis/paper_a/shocks_ranges_wide.csv` (Australia, short term, return period 10) the file gives p5 = 23,098,884, that is 23.1 million; 27.0 does not match, so the check fails (MISMATCH). The widened figures in the text match the file: 1 in 10 p5 23.1, p95 36.5, capacity over population 0.837 to 1.322, share below the population 0.3700; 1 in 20 p5 19.7, p95 31.2, 0.715 to 1.130, 0.7765; average year 0.0045. (`check_shocks_ranges_wide.py` takes no arguments here, so I read the file directly.)
