# Approval digest, 2026-11-18: gate 6 (the second-round computations)

Reply "yes" to take every recommendation, or name the number of any statement or decision you query. Every figure below was computed by a builder (B132 to B139) and reproduced by a blind checker on its own route (V47 to V53); the full table with ids is `qa/reports/B142_register_round2.md` section 1. The register holds the old values until you approve; the patched drafts already carry the new ones. Two patch jobs (B143a, B143b) and the Paper B response letter are still finishing; nothing below depends on them.

## A. Paper A
1. **Regional flips.** On the 19-choice regional draws none of the eight short-term flips is both robust and free of an artefact flag: SA Arid Lands keeps its 2025 status across the range but carries a land-definition flag; Mackay Whitsunday (5th percentile 135,581 against 153,841 people) and North Tasmania (148,681 against 156,393) do not. South West Queensland's long-term flip holds in every draw (17,239 to 24,761 against 7,109). Rows A036 (2 to 0), A038 (7 not robust), A184 (tipping 21 central, 19 to 26 with each region at its own end), A199.
2. **The change tested.** In none of 2,000 paired draws is 2025 short-term capacity below 2011's (difference 2.3 to 16.5 million; 6.5 to 8.4 on the shared choices alone); long term the change is not established (26% of paired draws fall). With 2011's bad years on the 2025 weather table, capacity over population at 1 in 20 is 0.95 against 0.95 in 2025, so almost all the apparent improvement was the table. The 5.8% failure probability becomes 2.3% to 19.4% a year (median 7.6%). Rows A196, A009, A430, A431.
3. **One layer; the identity; the diet window.** Land and livestock together add 2.5 million short term and the two diet layers 5.6 (A449). The meat production-to-consumption ratio (1.57 against the model's 1.50; 1.51 against 1.49 in 2011) is a consistency check, not a validation. On a ten-year diet window capacity reads 39.1 million (39.7 unrounded), worth about 2.4 million or 30% of the rise (A462; decision 149). The national 2011 row becomes the regional sum (A363: 0.671; 1.455).

## B. Paper B
4. **The drought bound at every weather figure.** 18.9 million at 1 in 100 with the cereal factor on every yield, 40.4 on crops alone; the drought factor 2.19 against 1.03; the failure probability 5.8 to 6.1% against below 1%. The "18.9 to 55.3" sentence states the two changes one at a time. Rows B001, B003, B096, B130, B137, B167, B188, B193, B194.
5. **The shares as ranges.** Line (a) about -1% to 8% across references and variants, near zero throughout; line (b) 28% to 46% to the model (5% to 36% to the median), mostly the productivity conversion of the footprint and HALF; "narrows by a third" depends on the commodity balance. Line (c), with one energy requirement and waste for all, closes 14.7% (band 10% to 16%). The binding-land-type footprint reading 53.9 to 77.9 million (1.30 to 1.88 times the model) sits beside the pooled 64.8 to 117.0. Rows B276, B277, B046, B156, B402.
6. **The bridge and the panels.** From HALF at Australian productivity (76.0) to the model (41.5) the all-orderings steps are diet -22.6 million, pasture-fed yield -13.0, cropland yield -6.4, land pool -6.3, non-food land -4.4, waste -17.9, requirement +36.2; the pool step is 18% of the gap on HALF's own pooling. Table 8 is three panels; 7.88 is an upper bound (diet C) with diets A and B at 1.60 and 3.77. Rows B182, B185, B186, B187, B005.

## Decisions
| # | Decision | Recommendation | Confidence | Cost | Reason |
|---|---|---|---|---|---|
| D1 | Statements 1 to 6: the 30 Tier A rows marked "pending gate 6" take their new values | Yes | High (every value two-route) | None | The drafts already carry them |
| D2 | Paper A literature paragraph (R05a issue 15): the response letter answers two referee points as out of scope for the word limit; add a 150-word paragraph placing the paper among recent carrying-capacity and land-system work, cut elsewhere | Add it | Medium | Half a point | Both Paper A referees asked; the works are on disk |
| D3 | A317 (single-year series): restate its range to 43.3 to 55.8 million on the rebuilt series (V51 passed the rebuild) or keep 43.5 to 55.4 with a supplement note | Restate | Medium | None | The second route now exists |
| D4 | Paper A keywords: 7 against Springer's usual 4 to 6 | Cut to 6 | High | None | Journal form |
| D5 | Crop-only drought companions for the 2011 and mirror releases (B134 computed 2025 only) | Not computed; Paper B says the bound is shown on the 2025 corrected release | Medium | Saves a quarter point | The point is made once |
| D6 | The long-term preset at 1 in 20 (21.7 million, 79% of the population) is arithmetic on checked cells, not a model run (A467, unverified) | One quarter-point check job, else cut the figure | Medium | Quarter point | A printed figure needs two routes |
| D7 | Table 9 outside raters (decision 143 left it to you) | Not before submission; offer in the cover letter | Medium | None | The recast table makes no finding |
| D8 | Zenodo deposit (decision 131) after the light third round R06 | Yes | High | None | Order of work stands |

Reply yes to take all recommendations.

## Your tasks
1. Send the two author emails when you are ready: `papers/CORRESPONDENCE/halff_authors_draft.md` (Alexander et al. 2016) and `cassidy_authors_draft.md`; addresses are in the corresponding-author notes on each paper's first page.
2. Read the drafts once the two patch jobs land (I will say when): `papers/A_results/draft/paper_A_draft1.md`, `papers/B_methods/draft/paper_B_draft1.md`, and the response letters `papers/A_results/response_letter_round2.md` and `papers/B_methods/response_letter_round2.md`.
3. Fetches (full URLs in `qa/reports/B138_paper_A_smaller_computations.md` and `B137_...md`): ERP at 30 June 2007 and 2008 https://www.abs.gov.au/statistics/people/population/historical-population/latest-release ; ERP by age and sex at 30 June 2011 and 2025 https://www.abs.gov.au/statistics/people/population/national-state-and-territory-population/latest-release ; ABS 4316.0 https://www.abs.gov.au/statistics/health/health-conditions-and-risks/apparent-consumption-selected-foodstuffs-australia/latest-release ; ABS 3222.0 https://www.abs.gov.au/statistics/people/population/population-projections-australia/latest-release ; the ABS 2015-16 and 2020-21 agricultural census explanatory notes (B137 report, section on the ABS frame); and the nine closed works in `qa/reports/B142_register_round2.md` section 5.
4. `papers/DECLARATIONS.md` edits and the Population and Environment submission guidelines check: https://link.springer.com/journal/11111/submission-guidelines

Files: `qa/claims_register.csv` (rows with "pending gate 6"); reports B132 to B143b, V47 to V54b, R05a, R05b, R07a in `qa/reports/`; `qa/DECISIONS.md` 133 to 150.
