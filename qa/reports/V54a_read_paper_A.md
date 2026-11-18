# V54a: blind read of Paper A after the second-round patch (B141a)

Files read: `papers/A_results/draft/paper_A_draft1.md` (main text, abstract, declarations; the drafter-notes appendix read but not judged as paper text), `supplementary.md`, `highlights.md`, `references.md`; the claims csvs `A_s01-04_claims.csv`, `A_s05-08_claims.csv`, `A_s09-12_claims.csv`, `highlights_claims.csv`, `supplementary_claims.csv`; `qa/claims_register.csv` (read only); the builder reports B110 to B123, B132, B133, B137, B138 and the checker reports V36 to V38, V40, V41, V44, V47, V48, V51, V52 (V39 and V42 scanned; they bear on Paper B). Data files opened are named in the trace table. No git, no subagents, no network. The draft was read in full before any report was opened.

## 1. Tolerance

Exact for every printed number: the file value, rounded half up to the precision the paper prints, must equal the printed figure. A ratio or share printed from two file cells is recomputed from the unrounded cells. Where a claims row names both a data file and a checker report and the two differ, the draft passes if it prints the checker's value, and the difference is noted.

## 2. Wrong-value example

I read Table 3's long-term liquid fuel average as +0.09 million (my eye took the forward-walk column). `analysis/comparison_2025/decomposition_eight_layer_table.csv` line 9, column `long_average`, holds 103,056, which prints +0.10; +0.09 is the forward walk (90,858). The check therefore fails a misread value, and the draft's +0.10 passes. The same procedure caught the real fails below (for example Table 7's 2011 sum of 13.7, which the file gives as 13,750,254).

## 3. Counts

* Numeric tokens in the abstract, main text, highlights and supplement (excluding four-digit years and headings): about 2,520 (main text and abstract 1,054; supplement 1,457; highlights 11).
* Traced to a named data file or checker report cell by cell: about 1,050 (every main-text and supplementary table except Tables S3 and S8, which were traced to register rows and V41; the abstract; the highlights; every number in sections 2 to 11 prose; S1, S2, S4 prose, S5, S6, S9, S10). The rest (section and table numbers, literature page numbers, settings repeated from traced tables, and register-only rows in S3, S6 and Table S3) were matched to a claims row and a register value only.
* Fails: 16 number or trace fails, F1 to F16, with two further notes, F17 and F18 (section 4); 10 checker-wording fails (section 5); 5 Tier A rows pending (section 6); 21 logic and consistency fails (section 7); 5 reference-list fails and one unconfirmed keyword count (section 8).

## 4. Trace table

Fails first. "Row" is the claims csv row (file short name, section, sentence). "Printed where" is the line, column or cell of the source.

### 4.1 Fails

| # | Number | Section | Claims row | File | Printed where | Verdict |
|---|---|---|---|---|---|---|
| F1 | 13.7 (2011, 1 in 10, sum of regional capacities, 2025 table) | Table 7 | A_s05-08 "Table 7, B141a" (derived: sums of checked cells) | `analysis/paper_a/shocks_2011_on_2025_table.csv`, basis `2011_on_2025_table`, return period 10, 52 region rows plus NT (zone 60) | sum 13,750,254 | **fail**: prints 13.8 |
| F2 | 0.46 (2011, 1 in 100, sum over national) | Table 7 | same row | same file, return period 100: sum 7,064,412; national 15,182,401 | 0.4653 | **fail**: prints 0.47 (Table S14 prints 0.47 for the same ratio on the thesis table) |
| F3 | 8.31 MJ (age-sex mean requirement, 2010) | S10 | supplementary "S10, B141a" (B138 item 3; V52 section 5) | `analysis/population_2011/age_sex_energy.csv`, row `national_mean` 2010 | 8.3020; ratio 1.0377 | **fail**: the file and the builder print 8.30; V52 line 205 says "8.30 MJ (1.038) is reproduced"; 1.038 times 8.0 is 8.30, not 8.31 |
| F4 | 3.8% below | S10 | same row | same file; B138 line 113 | 8.0 / 8.302 = 0.9636 | **fail**: 8.0 MJ is 3.6% below the mean (B138 prints 3.6%); the mean is 3.8% above 8.0 |
| F5 | "South Coast WA, Avon and four others, had four to eight times" | 7.3 | A_s05-08 "7, B141a" (derived: inverse of A-rows 0.12 to 0.26) | `analysis/paper_a/long_term_regions.csv`, 2025-fixed regions | South Coast WA 8.07, Avon 7.27, Border Rivers-Maranoa-Balonne 7.11, Western NSW 6.10, Border Rivers-Gwydir 4.60, then Northern Agricultural 3.86 | **fail**: three others reach four times, not four |
| F6 | 33 and 28 million (meat balance at the model's own meat requirement) | 6; S10 (33.4, 28.1) | A_s05-08 "6, B141a" | row names `analysis/comparison_2025/meat_balance_identity.csv`, which does not exist; the file is `analysis/paper_a/meat_balance_identity.csv` and does not carry 33.4 or 28.1 | only in V51 line 46 | **fail** (row names the wrong path; the data file does not carry the number) |
| F7 | Table S13 cells (0.762; 31.63, 0.705; 29.25 and the rest) | S4, Table S13 | supplementary "S4, B141a" (Table S13) | row names `analysis/comparison_2025/decomposition_eight_layer_table.csv`, which holds none of them | the values are in `analysis/resilience_2025/drought_factor_variants.csv` (all 24 rows match) | **fail** on the citation; values pass on the right file |
| F8 | 1.54 to 1.65 (capacity over population at window centres) | 2 | A_s01-04 "2, B141a" (B138 item 1; V52 section 4) | `analysis/population_2011/reference_periods.csv`, column `capacity_over_population_at_midpoint_2025_short` | 1.6173, 1.6173, 1.5416, 1.6506, 1.576, 1.5955 and, for fuel, 1.5148 | **fail as printed**: Table 1 lists the fuel window (0.5 years), whose ratio prints 1.51; the range is 1.51 to 1.65 across Table 1, 1.54 to 1.65 only for the production windows V52 used |
| F9 | Bolleter 2018, p. 123 | 1.2 | only row (A_s01-04 line 32) flagged superseded | literature register L146 | | **fail** (no live row) |
| F10 | Poore and Nemecek 2018, p. 990 | 6 | only row (A_s05-08 line 57) superseded | L115 | | **fail** (no live row) |
| F11 | 71% of production by volume (ABARES 2026b, p. 5); ABARES 2026a p. 2 | 1.4 | rows A_s01-04 lines 47 to 49 superseded | L234, L241 | | **fail** (no live row) |
| F12 | Lane (2014, p. 3) | 6 | row A_s05-08 line 42 superseded | L020 | | **fail** (no live row) |
| F13 | 15,950 km2 and 25,379 km2 (Avon denominators) | S1 | rows supplementary lines 34 and 35 superseded (they carried ha) | V37 section 4 (1,594,996 ha; 2,537,931 ha) | values right after the ha to km2 change | **fail** (no live row) |
| F14 | 42 and 31 regions; crop yields 7 and 20; forward differs in 4 and 6, reverse in 2 and 2 | S1 | S1 row 30 superseded; no B141a row for S1 | `analysis/comparison_2025/decomposition_eight_layer_regional_counts.csv` (42, 7; 31, 20); V51 line 35 (4, 6; 2, 2) | values right | **fail** (no live row) |
| F15 | 5.3 million people added in 14 years | 1.1 | no row | arithmetic: 27,608,200 less 22,336,514 = 5,271,686 | value right | **fail** (no row) |
| F16 | Stale live rows that contradict the draft | 3, 9, 10, 12 | A_s01-04 "3,16 Three are not robust" (A038), "3, Table 1, Short term: 2 clean and robust" (A036), "4, Table 2 People over capacity 0.670 / 1.454"; A_s09-12 "10,6 ... 48,520", "10,20 5th percentile 174,487", "10, Table 7 rows 2 to 8" (13-choice ranges, e.g. 42,815 to 48,520), "12,22 0.670 to 0.665", "12,25 two short-term flips pass" | none of these values is in the draft | | **fail** (rows not flagged superseded; the register job would carry wrong values) |
| F17 | Table S16, two long-term cells, crops and animal products: 14.54 (2006, 2008, 2010) and 13.30 (2007, 2008, 2010) | S10 | supplementary "S10, B141a" (B138 item 6; V52 section 2) | `analysis/paper_a/window_subsets_2011.csv` gives 14,562,798 and 13,305,083 (14.56, 13.31); V52 lines 65 and 68 give 14.543 and 13.304 | | **note, pass on the checker**: the draft prints V52's values, not the builder file's. The crops-only columns exist only in V52 section 2, not in any data file |
| F18 | 179 to 182 of 200 groupings | 5.3; S2 | A_s05-08 "5, B141a" (B138 item 4; V52 section 3) | `analysis/scale_curve_2025/scale_partition_summary.csv`, row `uniform_national_yield_reference`: "19 of 200 draws are below the real states" (181 above); size-matched 14 (186 above) | V52 line 84: 179 and 182 (its two seeds) | **note, pass on the checker**: the file prints 181; the draft prints the checker's two seeds |

### 4.2 Passes (by block)

| Number(s) | Section | Claims row | File | Printed where | Verdict |
|---|---|---|---|---|---|
| 33.3; 41.5; 22.3; 27.6 | Abstract, 3, highlights | A001, A003, A002, A004 | `results/2011-fixed-3.csv`, `results/2025-fixed.csv` zone 1 | 33,307,814; 41,503,537; 22,336,514 (regions sum, reference_periods.csv line 2); 27,608,200 | pass |
| 1.49; 1.50; 24.6%; 23.6% | 3, 4 | A_s01-04 "3, B141a" | `reference_periods.csv` line 2; `reference_periods_national_row.csv` lines 2, 14 | 1.4912; 1.5033; 41,503,537 / 33,307,814 = 1.2461; 0.236012 | pass |
| 0.69; 0.57; 69%; 57% | 4, 7.1, abstract | A010, A011 | `reference_periods_national_row.csv` line 11; `reference_periods.csv` 0.5659 | 0.687222; 0.5659 | pass |
| Table 1 distances 3.5, 3.25, 3.5, 3.5, 3.5, 0, 0.5; 4.5, 4.5, 1.5, 6.5, 2.5, 3.0, 0.5 | 2 | A_s01-04 "2, B141a" | `reference_periods.csv` columns `gap_midpoint_*` | lines 3 to 10 | pass |
| 304 below; 10,126; 22,336,514 | 2 | A_s01-04 "2, B141a" | `reference_periods.csv` line 2 note; `reference_periods_national_row.csv` | 22,336,514 less 22,326,388 = 10,126 | pass |
| 2,000 paired draws, none falls; 26%; 52%; 6.5 to 8.4; 2.3 to 16.5; 1.9 to 9.6; 13%; -0.9 to +3.4 | Abstract, 9.1, 7.1 | A_s09-12 "9, B141a" | `results/paired_change_2011-2025.csv` lines 2 to 6 | 0 falls; 0.2610; 0.5220; 6,545,900 to 8,445,247; 2,316,001 to 16,476,848; 1,867,704 to 9,640,074; 0.1315; -873,091 to 3,396,465 | pass |
| Table 3, all 60 cells; 5.6 million (68%); 8.2; 0.27 | 4, abstract, highlights | A_s01-04 "4, B141a" (B137; V51) | `analysis/comparison_2025/decomposition_eight_layer_table.csv` lines 2 to 13 | e.g. 2,456,649; 4,149,655 + 1,427,697 = 5,577,352 (68%); 8,195,723; 273,063 | pass; "average lies between the walks in every row" checked row by row |
| 42 and 31 regions; 7 and 20 | 4 | A_s01-04 "4, B141a" | `decomposition_eight_layer_regional_counts.csv` lines 2, 3, 11, 12 | 42, 7, 31, 20 | pass |
| 39.1 (39.7); 2.4; about 30% (22%); 17% to 19%; 39.1 to 25.9 kg | 4, abstract | A_s01-04 "4, B141a" | `analysis/diet_2025/diet_window.csv` rows 2014-23 and 2021-23, Australia short | 39,082,575; 39,691,820; 41,503,537; beef 39.11 and 25.88 | pass |
| Table S15, all 37 cells | S10 | supplementary "S10, B141a" | `diet_window.csv` zone 1 rows | e.g. 2017-19: 27.30, 39,960,555, 40,580,198 | pass |
| 0.19 million (8%); 194,427 (0.47%); 48,724; 1.097 | 4, S10 | A_s01-04 "4, B141a" | `analysis/paper_a/definitional_residue.csv` | 194,427; 0.47; 7.9; 48,724; 1.09676 | pass |
| 32.7 to 34.0; 22% to 27%; 1% to 17% | 4, S10 | A_s01-04 "4, B141a" | `analysis/paper_a/window_subsets_2011.csv` Australia rows | 32,714,415 to 34,019,601; ratios 1.2200 to 1.2687 | pass |
| Table 2: 22, 16, 8 (7 and 1), 3, 7, 0; 35, 32, 3, 2, 2, 1 | 3 | A_s01-04 "Table 2, B141a" | `analysis/paper_a/regional_flips-3_wide.csv` | counted from columns `over 2011`, `over 2025`, `flip`, `artefact flag`, `2025 status robust to the range`, `clean and robust` | pass |
| 136,000; 149,000; 154,000; 156,000; 15,500; 7,110; 17,200 to 24,800 | 3, 9.1 | A_s01-04 "3, B141a"; A_s09-12 "9, B141a" | `results/ranges_2025-fixed_wide_zones.csv` zones 34, 57, 37 | 135,581; 148,681; 153,841; 156,393; min 15,477; 7,109; 17,239 to 24,761 | pass |
| 29% and 14% (13.5%); 27% and none; 16% and 43% | 3, 9.1, 10 | A_s09-12 "9, B141a" | B132 line 52; V47 line 148 | 29.4%, 13.5%; 26.9%, 0; 16.2%, 42.6% | pass |
| 464, 456, 441 thousand; 1.3, 1.0, 1.0 million | 3 | A061; A_s01-04 "3,26" | `regional_flips-3_wide.csv` short rows | 464,456; 456,182; 441,053; 1,282,995; 1,006,997; 991,502 | pass |
| Table 4 and Table S6, all 84 cells; 30.7; 25.7; 14.7; 17 points | 5 | A_s05-08 Table 4 rows; A074 to A109 | `results/scale_curve.csv` 2011-fixed and 2025-fixed rows | e.g. 2025 short state 0.374 (SA2), 0.539 own; 2011 SA3 0.463; long SA3 0.245 (24%) | pass |
| 91%; 76%; 33% | 5.3, S2 | A_s05-08 "5, B141a" | `scale_partition_summary.csv` row `uniform_national_yield_reference` | 0.9052; 0.7577; 0.3270 | pass |
| 85% and 58% (state-basis medians) | S2 | supplementary "S2, B141a" | same file (0.8544); 58% in V52 line 88 only | | pass on the file and V52 |
| 37.4% to 40.3% (39.0%); 34.6% | 5.4, S2 | supplementary "S2, B141a" | `analysis/pasture_2025/two_pool.csv` SA2 row | 37.4, 40.3, 39.0; 40.3 / 116.4 | pass |
| 3.49; 3.32; 175,000; 141,000; 10% to 99% | 6 | A345, A346 | register A345, A346 | | pass on the register |
| 1.57; 1.51; 1.50; 1.49; 41.2 to 41.3; 33.9 to 34.2; 2.5 and 3.0; 2.0 and 1.5 | 6, S10 | A_s05-08 "6, B141a" | `analysis/paper_a/meat_balance_identity.csv` (real path) | 1.575, 1.571; 1.506, 1.519; 41.27, 41.17; 33.87, 34.16; 2.462, 2.972; 2.039, 1.479 | pass on the real file (see F6 for the path and for 33 and 28) |
| Table 5 and Table 6, all 36 cells; 21.7; 79% | 7 | A152 to A161; A_s05-08 "7, B141a" | `analysis/paper_a/long_term_levers.csv` zone 1; `long_term_regions.csv` | e.g. 34,274,878 (+119%); 3,705,376 (-76%); 22,831,774 (+46%); 34,274,878 x 0.634262 = 21.74 million, / 27,608,200 = 0.787 | pass |
| Table S1, all 32 cells | S front | supplementary Table S1 rows | `results/2011-fixed-3.csv`, `results/2025-fixed.csv` zone 1 | e.g. 2,520 and 253; 2,360 and 210; 0.005 and 0.0023 | pass |
| 0.742; 0.634; 0.456; 0.599; 153 seasons | 2, S4 | A_s01-04 "2,22"; B112, V38 | `analysis/resilience_2025/drought_bounds.csv` factor column; V38 | 0.742361; 0.634262; 0.455821 | pass |
| Table S10 all 24 cells; 41.2; 30.8; 24.7; 15.6; -0.8%; -2.5%; 28%; 54% | 8.1, S4, abstract, highlights | A_s05-08 "8,15"; supplementary Table S10 rows | `drought_bounds.csv` | 41,191,546; 30,810,607; 24,681,948; 15,623,209; 40,449,636 | pass |
| 23.1 to 36.5; 19.7 to 31.2; 0.84 to 1.32; 0.71 to 1.13; 37%; 78%; 0.45% | 8.1, S4 | A_s05-08 "8,7"; A014, A183, A187 | `analysis/paper_a/shocks_ranges_wide.csv` Australia rows | 23,098,884 to 36,501,763; 19,735,337 to 31,186,554; 0.837; 19,735,337 / 27,608,200 = 0.7148; 0.3700; 0.7765 | pass |
| Table S9 13-choice and herd-cycle cells | S4 | A390 to A392 | `analysis/paper_a/shocks_ranges.csv` | 26,972,109 to 33,973,336 (0.977 to 1.231); 24,959,665 to 27,806,836 (0.904 to 1.007) | pass |
| 22.5 to 35.9; 19.1 to 30.5 | S4 | supplementary S4 | V44 item 1 (22,497,730 to 35,936,047; 19,070,192 to 30,458,271) | | pass (see checker-wording W7 on the label) |
| 29.2 to 31.6; 1 in 20 below in every supported variant; Table S13 | 8.1, S4 | A_s05-08 "8, B141a" | `drought_factor_variants.csv` | 29,247,461 to 31,629,202; 24.28 to 27.11 | pass |
| 0.66 to 0.70; 27.4; 0.6% | S4 | supplementary "S4, B141a" | V51 line 65 | 0.661 to 0.702; 27,438,890 | pass |
| 2.3% to 19.4% (7.6%); 2.4% to 19.5% (8.0%); 5.8%; 17.1; 6.1%; 16.4; 9 draws | 8.1, S8 | A_s05-08 "8, B141a" | `analysis/paper_a/failure_probability_range.csv` | 0.0233, 0.0759, 0.1935; 0.0239, 0.0802, 0.1954; 0.0584, 17.1; 0.0610, 16.4; 9 | pass |
| 2066; 2068; 2034; 2.6; 1.8 | 8.1 | A_s05-08 "8, B141a" | `analysis/paper_a/projections_against_capacity.csv` | 2066, 2068; 2034.2, 2034.1; 2.592; 1.767 | pass |
| Table 7, 2025 rows, all 28 cells; 2011 average-year row; 2011 1-in-10 and 1-in-20 rows except F1 | 8.1 | A_s05-08 Table 7 rows | `analysis/paper_a/shocks_summary-3.csv` 2025-fixed rows; `shocks_2011_on_2025_table.csv` | e.g. 16,895,921 (16.9), 0.55; 21,125,881 (21.1), 0.946; 10,945,398 (10.9), 0.518 | pass |
| Table S14, all 15 cells | S4 | supplementary "S4, B141a" | `shocks_summary-3.csv` 2011-fixed-3 rows | 24.7, 1.11, 85%, 13.9, 0.56 and the rest | pass |
| 19 and 26; 21 to 24 (23); seven and four inside; five tipping regions in three states | 8.2, S4 | A_s05-08 "8.2, B141a" | V47 comparison table; `ranges_2025-fixed_wide_zones.csv` (Burnett Mary p5 415,639 above 372,757; North East Vic 102,805 below 114,355) | | pass |
| 31.1 to 49.2 (1.58); 13.3 to 18.8; 39.4 to 43.8; 13.9 to 16.2; 32%, 27%, 24%; 85% | 9.1 | A027, A028; A_s09-12 "9,3" to "9,6" | `results/paired_change_2011-2025.csv` cap2025 columns; V41; V38 | 31,115,433 to 49,169,829; 13,307,157 to 18,765,604 | pass |
| Table S7 all cells; 39.0 and 15.8 medians | S4 | supplementary Table S7 rows | V41 "Ranges"; `paired_change` holdings row (29,826,800 to 43,119,512) | | pass |
| 15, 16, 15; 36, 32, 36; 37, 35, 36; 21, 22, 20; 22 and 39 | 9.2, S4 | A304, A306, A308, A310 | register | | pass on the register |
| -16.0%; +20.7%; +97.9%; +20.2%; Table S3 | 9.2, S4 | A279, A286, A295, A285 and the Table S3 rows | register | | pass on the register |
| Table 8, all 49 cells; 144,000; 5.40 million; 0.491; 2.08; 0.41; 0.62; 7.3; 1.000; 0.80; 139,000 to 188,000; 144,000 to 156,000 | 10 | A_s09-12 "10, B141a" | `analysis/paper_a/regions_in_depth.csv`; `ranges_2025-fixed_wide_zones.csv` zones 5, 9, 10, 50, 57, 46, 43; `regional_flips-3_wide.csv` | e.g. Avon 889,922 to 1,326,694; Murrumbidgee 1,533,929 / 738,895 = 2.076; North Tasmania 156,413 / 156,393 = 1.0001 | pass |
| S5 populations and capacities (4,394,612; 105,924; 597,750; 60,913; 10,613; 57,595; 66,198 to 46,572 and the rest) | S5 | supplementary S5 rows | `regional_flips-3_wide.csv` short rows; `regions_in_depth.csv` | | pass |
| S1 figures: 170 to 6 thousand; 1.72 to 2.27 million; 356,807; 21%; 97,458; 153,025; -167,976; 62,789; 38,290; 34,818; 658 | S1 | supplementary S1 rows | `analysis/comparison_2025/capacity_by_cause_corrected.csv` zones 4, 9, 10, 33, 55 | | pass |
| Table 9 and Table S5, all cells; 15.5; 1.60, 1.82, 2.60, 3.00 | 11, S6 | A_s09-12 "11, B141a"; S6 rows | `analysis/paper_a/measures.csv`; register A273, A274 | e.g. 48.3 (16.4%), 14.3 (-8.2%); 23.2 (48.4%) | pass |
| Table S2, all 22 cells | S3 | supplementary S3 rows | register A202 to A226 | | pass on the register |
| Table S12, all 66 cells | S12 | supplementary "S12, B141a" | V37 section 5; register A354 to A362, A376, A380 | | pass |
| Highlights 1 to 5 | highlights | highlights_claims rows 1 to 5 | as the abstract rows above; `results/scale_curve.csv` (0.374, 0.539) | | pass on value (see W1, W2) |

## 5. Checker-wording fails (draft uses the builder's or an unamended wording)

* **W1 (V37 section 7, point 2).** V37: "'The diet layers ... +5.59 million' says a little more than the figures ... Better: 'the consumption and red-meat-mix layers'." The draft keeps "two diet layers" in the abstract ("two diet layers add 5.6 million") and highlight 2 ("Two diet layers add 5.6 million people"), and section 4 adds the gloss "the diet with less beef". The section 4 sentence that would justify "diet" ("Fuel, biofuel and timber settings move the consumption layer by 0.2% or less") rests on R05a only, with no checker. Rewrite: "the consumption and red-meat-mix layers add 5.6 million".
* **W2 (V38, proposed sentence 4).** "41.2 uses the definition that includes grain-fed animals ... the paper should name the grain-fed animals as following crops." Section 8.1 does; the abstract ("applied to crops alone, 41.2 million"), highlight 3 ("crops only, 41.2") and conclusion 3 ("on crops alone the 1-in-10 figure is 41.2 million") do not. Rewrite: "applied to crops and grain-fed animals only, 41.2 million".
* **W3 (V52, point 2).** "The paper must give 39.1 and 39.7 together." The abstract and conclusion 1 give 39.1 alone. Rewrite: "on a ten-year diet window the 2025 figure is 39.1 million (39.7 on unrounded inputs)".
* **W4 (V52, point 5, and B138).** V52 confirms "8.30 MJ (1.038)"; the supplement prints 8.31 MJ and "3.8% below" (B138: 3.6% below). See F3, F4.
* **W5 (V41, comparison table).** V41 fails a count of judgement ends ("The README table marks five as judgement (meat, meategg, redmeat, restable, land), and the builder's report adds energy, making six"). Section 9.1 still says "Five range ends rest on the author's judgement" and lists a set that leaves out the land source and the energy level, which the paragraph above names as judgements. Rewrite: "Several range ends rest on the author's judgement: the equal chances of the two land sources and of the three meat windows, the activity level of 1.8, the low ends of the meat-and-egg share (0.115) and the red-meat share (0.528), the equal weight on the leave-one-out resilience table, and the low end of the long-term feeding benchmark (0.30, no effect on the corrected method)."
* **W6 (V41, line 114).** V41 notes that waste set to zero "is a setting, not a definition" under the new rule. Supplementary Section S4 still sets the 1.58 factor "above those of avoidable waste (1.33)" among the definition spans, while S4 itself draws waste (12% to 14%) as a setting. Drop the avoidable-waste comparison or name it as the setting's span.
* **W7 (V44, point 1).** "It is better described as 'a fifty-fifty choice of resilience table added at the shock', not 'each draw's own table'." Supplementary Section S4 still says "with each draw's own resilience table the ranges are 22.5 to 35.9 and 19.1 to 30.5 million". Rewrite: "with a fifty-fifty choice of resilience table added at the shock, the ranges are ...".
* **W8 (V36, section 6).** "Suggest 'by more than 10% of the ABS figure'." Section 2 says "differed from the ABS figures by more than 10% in 24 of the 53 regions" without naming the base (on the release figure the count is lower). Rewrite: "by more than 10% of the ABS figure".
* **W9 (V47, wording point on the shares).** "The 29.4% and 13.5% shares rest on the equal-chance land-source judgement ... One clause saying so would keep the shares from reading as probabilities." Sections 9.1 and 10 carry the clause; section 3 ("29% and 14% of the 2,000 draws put them over capacity") does not. Add "(shares that depend on the equal chances given to the two land sources)".
* **W10 (V51, "What I would do differently").** "Name the loo reference result next to the drought-factor variants." The caveat is in the Table S13 note, but the main-text claim it qualifies (8.1, "above the population in every variant") stands without it. Add "(one leave-one-out variant falls 0.6% below; Supplementary Table S13)".

Checked and taken: V36 "about 82%" and "share of the regions' population"; V38 "almost all (about 97%)" and "below it in about 92% of draws"; V47 "its 2025 status holds in every draw" and conclusion 4; V48 section 9.1 sentence, "nearly the same", "almost all the table", one precision for the failure range, the anchors named; V51 S3 ("every row of Table 3"), S4 (consistency check, all meat, 33 and 28 million), S9 ("about 0.19 million ... upper bound"; "mostly output"), S10 ("not credited to pasture alone"); V52 points 1, 3, 4, 6, 7; V41 "18 of which vary" and "about 3%".

## 6. Tier A rows where the draft prints a different value from the register (round-two values not yet applied)

| Register row (Tier A) | Register value | Draft sentences | Report and checker supporting the draft |
|---|---|---|---|
| A036 | 2: Mackay Whitsunday; North Tasmania (clean and robust) | Abstract: "Of eight short-term status flips none is robust across 19 sampled settings"; section 3: "On the full set of 19 choices none of the eight flips is both free of an artefact flag and robust to the range"; Table 2, "Robust and free of an artefact flag", short term 0; section 9.1: "none is both free of an artefact flag and robust"; conclusion 4: "no short-term flip is both robust across 19 settings and free of an artefact flag" | B132 sections 3 and 4; V47 comparison table (holds) |
| A038 | 2 (herd-cycle ranges); 3 (13-choice ranges) | Section 3: "Seven do not keep their 2025 status across the range"; Table 2, short term 7; section 9.1: "Seven do not keep their 2025 status" | B132; V47 |
| A184 | 21 (21 to 22 across the range) | Section 8.2: "Taking each region at its own 95th or 5th percentile ... gives 19 and 26 regions over capacity at 1 in 10; in a single draw the number is 21 to 24 (median 23)"; conclusion 4: "21 to 24 in a single draw"; Supplementary S4: "19 with every region at its 95th-percentile capacity and 26 at its 5th" | B132; V47 |
| A196 | 0.89 (2011); 0.95 (2025) | Section 8.1: "in 2011 0.89 on the thesis weather table but 0.95 on the 2025 table"; Table 7, 2011, 1 in 20: 0.95; conclusion 3: "capacity is 0.95 times the population in a 1-in-20 year in both years on one weather table" | B133 section 1; V48 section 4 (0.946, 0.894, 0.953) |
| A009 | "15.35 and 15.6 within 13.3 to 18.8" (statement: the change lies inside the 2025 range) | Abstract: "the long-term change is not established, since 26% of paired draws fall"; section 7.1 and section 9.1: "The long-term change is not established: 26% of paired draws show a fall" | B133; V48 (A009: "add the paired result") |

Not Tier A but moved: A328 (Tier B) prints 23.7%; the draft prints 23.6% (B138, V52). A220 (Tier A) has the same value (48%) but its statement says "on the improved reference"; the draft states the corrected release with the store table (section 8.3, Table 9).

## 7. Logic and consistency fails

Logic (says more than the figures):

1. **Abstract:** "Of eight short-term status flips none is robust across 19 sampled settings." SA Arid Lands keeps its 2025 status across the range (section 3; `regional_flips-3_wide.csv`: robust yes, land-definition flag). Rewrite: "none is both robust across 19 sampled settings and free of an artefact flag".
2. **Conclusion 3:** "across the settings varied the range at each return period contains the population". At 1 in 100 the range is 31.1 to 49.2 times 0.456, 14.2 to 22.4 million, wholly below 27.6; in an average year it is wholly above. Rewrite: "at 1 in 10 and at 1 in 20 the range across the settings varied contains the population".
3. **Section 7.3:** "South Coast WA, Avon and four others, had four to eight times their population". Three others (F5). Rewrite: "South Coast WA, Avon and three others had four to eight times".
4. **Abstract against body and highlight 5:** the abstract gives "capacities sum to 37% of the national figure" with no basis; section 5.4 says 37% is the conservative bound and "the truth for SA2s lies between 37% and 54%"; highlight 5 says "37 to 54%". Rewrite the abstract clause: "capacities sum to 37% of the national figure on state yields (54% on each SA2's own yields)".
5. **Abstract:** "covers 57% of the 2025 population, mostly through its weather and fuel settings" reads as if weather and fuel produce the coverage. Rewrite: "covers 57% of the 2025 population; its weather and fuel settings account for most of the shortfall".
6. **Section 9.1:** "Capacity changed little (paired difference -0.9 to +3.4 million) while the population rose 24%." This is the long term only; short-term capacity rose by 2.3 to 16.5 million. Rewrite: "Long-term capacity changed little ...".
7. **Section 8.1:** "The two bounds are given equal weight." No figure or rule gives them weights. Rewrite: "Neither bound is preferred; a drought's effect on pasture-fed output lies between them."
8. **Section 8.1:** "above the population in every variant" (see W10).
9. **Section 2:** "capacity is 1.54 to 1.65 times the population" against the centres of "the 2025 windows" leaves out the fuel window that Table 1 lists (1.51). Rewrite: "1.51 to 1.65 (1.54 to 1.65 on the production windows; 1.58 on the livestock window)".
10. **S10:** "The model's fixed 8.0 MJ a day is 3.8% below the mean requirement ... (8.31 MJ, 1.038 times 8.0)". Rewrite: "The mean requirement of the 2010 population at the NHMRC reference body weights, 8.30 MJ a day, is 1.038 times the model's fixed 8.0 MJ (8.0 MJ is 3.6% below it)".

Consistency:

11. **S1:** two adjacent sentences give different counts for the same described quantity: "the forward walk names a different largest layer from the average in 4 and 6 regions, the reverse walk in 2 and 2. The forward walk names a different largest layer from the average in 7 regions in the short term and 2 in the long term, and the reverse walk in 3 and 1." The first is the eight-layer game, the second the nine-layer game (V51 line 35). Rewrite the second: "On nine layers, with land and livestock apart, the forward walk differs in 7 and 2 regions and the reverse walk in 3 and 1."
12. **Table numbers after B141a:** Table S1 note says the other long-term settings "are those of Table 5"; the settings are in Table 6. S2 ("28,609 and 384,476 on their own yields, Table 7") and the S5 opening ("on each region's own yields (Table 7)") mean the regions-in-depth table, now Table 8. Section 5.2 correctly says Table 8.
13. **Figures 5 and 6** have placeholders but no sentence in the prose cites them. Add "(Figure 5)" to section 7.2 or 7.3 and "(Figure 6)" to section 8.2.
14. **Section 3 against section 10:** North Tasmania's share of draws over capacity is printed "14%" in section 3 and "13.5%" in section 10. Use one precision.
15. **Section 4 and S10:** the 2011 grazing area is "3.64 million km2 in 2008"; Table 1 and Table S11 define it as the mean of 2005-06 and 2007-08 to 2009-10. Rewrite: "from 3.64 million km2 (mean of four years to 2009-10) to 3.32 million in 2020-21".
16. **S2:** "The SA4s, at 54%" is on the national yield vector; Table S6 prints SA4 58% (state yields) and 80% (own yields), and the section's opening says figures are on the state-yield basis "unless named otherwise". Name the basis in that sentence.
17. **Section 5.3 and S2:** "the states keep less than 179 to 182 of the 200 random groupings" is hard to read and quotes the checker's two seeds where the file prints 181 (F18). Rewrite: "about 180 of the 200 random groupings keep more than the states do".
18. **Section 4:** "taking 0.60 million off on the average,." (stray comma before the full stop).
19. **Section 4 and abstract terms:** the abstract and conclusions speak of "settings" ("seven settings both years share", "19 settings") where sections 2 and 9 speak of "sampled choices". One term throughout.
20. **Section 2 time word:** "not as today's administrative regions". Rewrite: "not as the NRM regions of 2025".
21. **Section 11 table label against the data file:** Table 9 and section 12.3 say "irrigated share of all farmland"; `measures.csv` labels the measure "Irrigated share of cropland 0.05 (now 0.007)". The claims row says "label corrected" without a checker. Either the file label or the text is wrong; confirm which.

Checked and consistent: Table 3 against section 4 prose; the average between the walks in every Table 3 row; Table 2 against sections 3, 7.3 and 9.1; section 8.1 shocked ranges against Supplementary Table S9 (19-choice column identical); Table 7 2011 1-in-20 and 1-in-10 against Table S14 and section 8.1; Table 5 against Table S6 own-yield NRM long cells; S6 against Table 9; Table S2 against Table S5 (the 156-litre note); S12 caption ("average can lie outside both") against its cells; the release-code key in S11 and its files (every file named exists).

## 8. References and journal checks

* **Word count:** `python3 qa/tools/wordcount.py A` prints TOTAL 7925 (sections 614, 824, 593, 800, 698, 552, 584, 1063, 844, 466, 218, 669). Pass (at most 7,950).
* **Abstract:** 249 words. Pass (150 to 250), one word from the limit.
* **Highlights:** 5 bullets, 79, 83, 80, 81 and 69 characters. Pass on count and length; highlights 2 and 3 fail on wording (W1, W2). Highlights match the body otherwise.
* **Keywords:** 7. The repository holds no Paper A requirement for Population and Environment (only `papers/B_methods/JOURNAL_REQUIREMENTS.md`, for the other journal: 1 to 7). Springer's usual instruction is 4 to 6; to be confirmed against the journal's page before submission. Highlights are an Elsevier item and may not be asked for.
* **Em dash:** none in `paper_A_draft1.md`, `supplementary.md`, `highlights.md` or `references.md` (grep count 0 each). En dashes (34) appear only in `references.md`, in titles and page ranges.
* **Time words:** "today's" in section 2 (item 20 above). "Latest" is tied to dated windows (2021-23; "each latest window") and passes.
* **Decision 33 tone:** no sentence calls an author wrong, careless or misleading. Pass.
* **"not seen" and "reported in":** none in the prose. "not seen" appears twice in `references.md` ([CHECK] notes on Jansen 1999 and Saltelli 2010); remove before submission.
* **Reference form (fail):** the list is built "Elsevier Harvard form" with abbreviated journal titles ("Popul. Environ.", "Ecol. Model.") and the year after the authors without brackets. Population and Environment uses Springer author-date (for example "Lane, M., Dawes, L., & Grace, P. (2015). Scalar considerations ... Population and Environment, 36(3), 356–371."). Regenerate in that form.
* **Cited but not listed:** none. Every author-date citation in the prose and supplement has an entry.
* **Listed but not cited (fail):** Cottrell et al. 2019; FAOSTAT 2025 (the prose names FAOSTAT without a year, so it is not an author-date citation); Higgins et al. 2018a; Kastner et al. 2012; Khorsandi et al. 2022; Khorsandi et al. 2023; Summerhayes and Baker 2026a. With 2018a and 2026a gone, the "b" suffixes on Higgins et al. 2018b and Summerhayes and Baker 2026b should go too.
* **Entry against prose (fail):** the prose cites "CSIRO 2025" (section 1.1); the entry is "CSIRO and University of Queensland, 2025".
* **Incomplete entry (fail):** "ABARE / ABARE, 2010. [CHECK: title; place of publication]" has no title; S10 cites it for a page and note ("ABARE 2010, p. 25, note a").
* **[CHECK] markers:** 18 remain in `references.md`; [CONFIRM] markers remain in the declarations.

## 9. The reader's test: three places a referee without Paper B or the repository would be lost

1. **Section 3, "The two flips that were clean and robust on 13 choices"** (also conclusion 4 and section 9.1). The main text never says what the 13 choices are or why there were two sets. One sentence in section 2 or 9.1: "An earlier, narrower set of 13 sampled choices (the meat window, diet shares and resilience table, without the land source, energy requirement and four other data choices) is kept for comparison in Supplementary Section S4."
2. **Section 4, "the forward walk (the order of the release chain)"** and Table 3's "forward" and "reverse" columns. "Release chain" is a repository term. One sentence: "The forward walk adds the 2025 layers in the order in which the data were brought forward (land and livestock, crop yields, consumption, organic share, resilience table, fuel, red meat mix, infrastructure land); the reverse walk takes them in the opposite order."
3. **Section 8.1, "On straight lines between printed points their last growth reaches it in 2066 and 2068."** A reader cannot tell that these years lie beyond both projections' printed horizons and are an extension of the last printed segment. One sentence: "Neither projection reaches 41.5 million within its printed years; extending the slope of each projection's last printed segment, the Intergenerational Report would reach it in 2066 and the Population Statement in 2068."

## 10. Register rows touched

None. `qa/claims_register.csv` and the claims csvs were read only. The only file written is this report.
