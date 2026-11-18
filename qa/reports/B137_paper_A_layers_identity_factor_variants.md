# B137: Paper A, land and livestock as one layer, the identity, the ABS frame, drought factor variants, the single-year series (decisions 136, 137)

Brief: qa/briefs/B137_paper_A_layers_identity_factor_variants.md. No network, no subagents. Notes: analysis/paper_a/README_round2_B137.md. One read-only git status was run by mistake (it printed the branch name only); no other git command.

## 1. The identity (item 2)

File: analysis/paper_a/meat_balance_identity.csv. FAOSTAT bulk files checked by hash. The 2021-23 row reproduces R04b: 4.66 Mt produced, 2.96 Mt eaten, ratio 1.57.

| Window | Meat ratio (QCL, food balance) | People fed on the balance | Model capacity over population | Model capacity |
|---|---|---|---|---|
| 2021-23 | 1.575, 1.571 | 41.3, 41.2 million | 1.503 (2025-fixed) | 41.5 million |
| 2010-12 | 1.506, 1.519 | 33.9, 34.2 million | 1.492 (2011-fixed-3) | 33.3 million |

Gap: +0.07 (+4.5 to 4.8%) in 2025 and +0.01 to +0.03 (+1 to 2%) in 2011. Probable causes, not split: the model adds 12% waste and feeds milk and wool from the same land (lowers it); the meat total includes grain-fed pork and poultry (raises the ratio). Rise 2011 to 2025: 20 to 22% on the balance, 25% in the model. Red meat alone is 2.5 (2010-12) and 3.0 (2021-23) times what is eaten; milk 2.0 and 1.5. So milk and total meat sit nearest the model, and the model binds on all pasture-fed food together.

Validation sentence (S4 and S5 in analysis/paper_a/abs_frame_feedlot_and_driver_sentences.csv). It supports the size of short-term capacity and its rise, because pasture-fed output binds. It does not test cropland (cereals are produced at about 19 times what is eaten), regions, or the red meat and dairy split. It is not independent of the livestock layer: the FAOSTAT and ABS tonnes describe the same animals, so the agreement tests the land and diet arithmetic. That last point is from general knowledge of the series and needs confirming in the FAOSTAT metadata.

## 2. Drought factor variants (item 5)

File: analysis/resilience_2025/drought_factor_variants.csv (national, thesis method of resilience.py imported, not edited; the whole-record unweighted row reproduces tables.csv at 1 in 10, 20 and 100). Capacity is short term, 2025-fixed, with the factor on all output (the model's rule) and on crop output only. "Supported" means the rank used is at least 3 (1 in 100 only with at least 149 seasons).

| Series and start | Seasons | 1 in 10 factor; capacity all output; crop only (million) | 1 in 20 factor; capacity all output; crop only | 1 in 100 |
|---|---|---|---|---|
| Unweighted, whole record | 153 | 0.742; 30.81; 41.19 | 0.634; 26.32; 40.99 | 0.456; 18.92; 40.45 |
| Unweighted, from 1950-51 | 75 | 0.762; 31.63; 41.22 | 0.653; 27.11; 41.03 | not supported |
| Unweighted, from 1970-71 | 55 | 0.762; 31.63; 41.22 | 0.594; 24.65; 40.89 | not supported |
| Unweighted, from 1990-91 | 35 | 0.762; 31.63; 41.22 | 0.578 (not supported); 24.00; 40.85 | not supported |
| Area-weighted, whole record | 153 | 0.705; 29.25; 41.13 | 0.638; 26.47; 41.00 | 0.357; 14.80; 39.93 |
| Area-weighted, from 1950-51 | 75 | 0.711; 29.49; 41.14 | 0.638; 26.47; 41.00 | not supported |
| Area-weighted, from 1970-71 | 55 | 0.708; 29.40; 41.13 | 0.585; 24.28; 40.87 | not supported |
| Area-weighted, from 1990-91 | 35 | 0.708; 29.40; 41.13 | 0.577 (not supported); 23.97; 40.85 | not supported |

Reading: the abstract sentence survives every variant. Capacity stays above the 27.6 million population at 1 in 10 (29.2 to 31.6 million) and below it at 1 in 20 on all output (24.3 to 27.1 million, supported rows). Area weighting is the variant that matters: it lowers the 100-year factor from 0.456 to 0.357 (the whole-record 1 in 100 capacity from 18.9 to 14.8 million). The 1-in-10 all-output fall is -24% to -30% against the -26% of A223.

Observed livestock output (analysis/resilience_2025/livestock_output_ratio.csv): ABS Livestock Products 7215009 to 7215012 (quarterly cattle, calves, sheep and lamb meat, tonnes), year to June, on disk in the session scratch folder (the files livestock_zone.py reads). Over 2005 to 2025 (21 years) the worst ratios are 2021-22 (0.856) and 2020-21 (0.868), reproducing R05a; over 1973 to 2025 the worst is 1974 (0.797). Both are milder than the cereal 1-in-10 factor of 0.742. No grazing record is held.

## 3. Item 1, one layer

Files: analysis/comparison_2025/decomposition_eight_layer_table.csv and decomposition_eight_layer_regional_counts.csv. Short term, average over 40,320 orderings (forward; reverse): land and livestock +2,456,649 (+2,043,444; +2,886,869); consumption +4,149,655; red meat mix +1,427,697; crop yields +161,723. Long term: land and livestock -598,893 (-627,341; -569,036). Averages sum to the change within 3 people; forward and reverse sum exactly. On eight layers the average lies between the forward and reverse walks in every row. Largest layer by region (absolute average): land and livestock in 42 of 53 regions short term, 31 long term (crop yields 7 and 20). The forward walk names a different largest layer from the average in 4 (short) and 6 (long) regions; the reverse walk in 2 and 2. Nine-layer counts reproduce B111 (26 land, 25 livestock).

Abstract and highlight sentences are S1 and S2 of the sentence file. Abstract: "Averaged over all orderings of the data layers, the two diet layers, consumption and the red meat mix, add 5.6 million people to short-term capacity, and land and livestock together, which share one grazing area, add 2.5 million." Highlight (83 characters): "Two diet layers add 5.6 million people; land and livestock together add 2.5 million".

## 4. Items 3 and 4: the ABS frame, the residue bound, feedlot

Sentences S6 to S10 (same file). Held in the records: the earlier EVAO level of $5,000 (ABARE Australian commodity statistics 2010, PDF page 42, printed page 25, note a; register A05), the 364 and 332 million hectare grazing areas and the 2016 category change (analysis/land_2011/README.md line 60; registers A11, D14). Not held: the $40,000 level, the Business Register frame and any national figure for the farmland the scope change removed. Murray to fetch the ABS 2015-16 Agricultural Commodities explanatory notes (page pattern used by fetch_abs_current.py: https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/7121.02015-16?OpenDocument, not opened here) and the 2020-21 release notes (https://www.abs.gov.au/statistics/industry/agriculture/agricultural-commodities-australia/2020-21).

Residue bound (analysis/paper_a/definitional_residue.csv): giving 2025-fixed the 2011 grazing area (x1.097) with output and diet fixed lowers short-term capacity by 194,427 people (0.47%), at most 8% of the 2.46 million; long term 48,724. This replaces R05a's rough 0.4 million, which the evaluator does not support.

Feedlot: pipeline/yields/livestock.py line 63 (cattle: grazing share + grain hectares + feedlot hectares in the denominator; sheep lines 44 to 47). The regional sensitivity R05a issue 12 proposes does not exist and was not built (needs zone feedlot inputs from raw ABS files and a change to the model's land accounts); decision row for Murray. National invariance is argued from the land rule, not computed.

## 5. X118 and X116

X118 fixed. Cause: data/2025/livestock_national_series.csv has columns 2009-10 and 2020-21 to 2024-25 only. analysis/years_2025/build_years_fixed.py (a copy; original untouched) runs livestock_zone.py with LS_SERIES=off for 2016-17 to 2019-20. The all-placeholder run reproduces the committed years.csv in 128 of 128 year cells to the person; the committed base row is stale (48,004,473 against 48,265,660 in results/2025-organic.csv). On the series where it is held: short term 43.3 (2020-21) to 55.8 (2024-25) million, long term 10.4 to 13.9; 2016-17 to 2019-20 stay on placeholders until the series is extended (a fetch for Murray). fixed_in set in qa/defects.csv.
X116 fixed as a new file: analysis/comparison_2025/movers_land_ratio_corrected.csv. Median short-term land-only ratio 0.914 against 0.90; flag counts unchanged on both tiers (7 regions, 14 rows, outside 0.5 to 2; 5 regions, 10 rows, outside 0.4 to 2.5); four regions differ by 0.005 or more. Row set in qa/defects.csv.

## Paper patch needs (sentences, not edited)
Abstract driver sentence and highlight 2 (S1, S2); Table 2 replaced by the eight-layer table and the nine-layer table to the supplement (S3); section 6 identity and its limits (S4, S5); section 2 and S1 frame sentences (S6, S7, flagged pending the ABS fetch); S1 residue (S9); feedlot (S10); section 8 factor variants (table above); S10 and the supplement single-year table (X118); movers.md lines 22 and 23 still print published-method values.

## Claim rows that move
No register value moves.
Tier A: A354 to A362 and A365 (nine-layer forward walk): values unchanged; the paper stops leading with them. A363, A364: unchanged.
Tier B and other: A382 (+2,456,649; -598,893) unchanged, now the Table 2 source (decomposition_eight_layer_table.csv). A383, A385 unchanged. New rows needed: eight-layer forward and reverse values (for example crop yields forward 153,478), regional counts 42 and 31, the identity (ratios 1.57, 1.51 to 1.52), the residue 194,427, the factor variants. A317 (B): before "unverified: second route blocked"; after: the second route reproduces 43.5 to 55.4 million (placeholder build) and the series-where-held build reads 43.3 to 55.8; value restatement is a decision. A223 and A014 (A and B): -26% at 1 in 10 and the 1-in-10 and 1-in-20 sentence unchanged; variants give -24% to -30%. A056, A343, A062, A064: no value moves (movers.csv and the state factor tables are untouched).

## Register rows touched
None. qa/defects.csv rows X116 and X118 only.

## Files changed
New: analysis/comparison_2025/{make_eight_layer_table.py, decomposition_eight_layer_table.csv, decomposition_eight_layer_regional_counts.csv, movers_land_ratio_corrected.py, movers_land_ratio_corrected.csv}; analysis/paper_a/{meat_balance_identity.py, meat_balance_identity.csv, definitional_residue.mjs, definitional_residue.csv, abs_frame_feedlot_and_driver_sentences.csv, README_round2_B137.md}; analysis/resilience_2025/{resilience_variants.py, drought_factor_variants_eval.mjs, drought_factor_variants.csv, livestock_output_ratio.csv}; analysis/years_2025/{build_years_fixed.py, rebuild_years.sh, years_rebuilt_placeholders.csv, years_rebuilt_series_where_held.csv}; this report. Edited: qa/defects.csv (X116, X118).

Wrong-value check: EXAMPLE, deliberately wrong. In a scratch copy of capacity_by_cause_corrected_orders.csv, Australia short-term eight-layer crop yields shapley_mean was raised by 1,000 (161,723 to 162,723). make_eight_layer_table.py stopped with "CHECK FAILED: short shapley_mean sums to 8196724, change 8195723". On the real file all checks pass.
