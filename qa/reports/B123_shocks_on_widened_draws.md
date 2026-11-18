# B123: shocked ranges on the widened draws; the four loose ends B122 could not reach

Brief: `qa/briefs/B123_shocks_on_widened_draws.md`. No git, no subagents, no network. Written only under `analysis/` and this report. No register row, frozen release, `results/` file or paper was touched. Every existing output is kept; a default rerun of each changed script reproduces its old output byte for byte (checked with `cmp` for `shocks_ranges.csv`, `long_term_levers.csv`, `long_term_regions.csv`, `method_effects_by_region.csv`, `method_effects_summary.csv`, `method_status.csv`, `harmonised_comparison_lines.csv`, and all csv files of `analysis/comparison_2025`).

## 1. Shocked ranges on the widened draws

Files: `analysis/paper_a/shocks_ranges.mjs` (option `--wide`), `shocks_ranges_wide.csv` (24 rows: Australia and the seven states, return periods 1, 10, 20; the columns of `shocks_ranges.csv` plus `share_draws_below_population`), `shocks_ranges_wide_own_table.csv` (same columns, the alternative below), `check_shocks_ranges_wide.py`, `analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide_states.csv` (new draws), README sections in `analysis/paper_a/README.md` and `analysis/sensitivity_2025/README.md`.

**The widened shocked ranges, Australia, short term (millions of people; 5th to 95th percentile of 2,000 draws; central is the release):**

| Return period | Central | Range | Median | People over capacity at p95, central, p5 | Capacity over population p5 to p95 | Share of draws below 27.6 million |
|---|---|---|---|---|---|---|
| Average year | 41.50 | 31.1 to 49.2 | 39.0 | 0.561, 0.665, 0.887 | 1.127 to 1.781 | 0.45% |
| **1 in 10** | 30.81 | **23.1 to 36.5** | 28.9 | 0.756, 0.896, 1.195 | 0.837 to 1.322 | 37.0% |
| **1 in 20** | 26.32 | **19.7 to 31.2** | 24.7 | 0.885, 1.049, 1.399 | 0.715 to 1.130 | 77.65% |

**27.6 million (27,608,200) lies inside both ranges on the widened draws.** On the 13-choice draws it also lay inside (27.0 to 34.0 and 23.0 to 29.0, B112); the herd-cycle result (above balance throughout at 1 in 10) does not carry to the widened range. At the base the nation is above balance at 1 in 10 and below it at 1 in 20, but across the widened range neither statement holds: 37% of the draws are under the population at 1 in 10 and 77.65% at 1 in 20.

**States** (people over capacity at the 95th percentile, central, 5th percentile; share of draws under the population):
* 1 in 10: Queensland is the one state whose population lies inside its range (0.822, 0.951, 1.210; 46.7%). New South Wales and the Australian Capital Territory (1.217, 1.563, 2.076), Victoria (1.408, 1.682, 2.053), South Australia (1.101, 1.320, 1.617), Tasmania (1.464, 2.172, 2.805) and the Northern Territory (1.780, 6.275, 8.436) are over capacity at every point of the range (99.9% to 100% of draws under). Western Australia is just above its range (1.007, 1.236, 1.509; 95.7%).
* 1 in 20: no state has its population inside its range (Queensland 1.035, 1.196, 1.523; 98.05%).

**Which resilience table.** The widened draws carry the choice `restable` (0 the release table of all years, 1 the leave-one-out table; 1,000 draws each, as in the published draws, where V38 found it). It acts on the long term only: every short-term draw is made at resilience 1, so a short-term draw is identical under either value. I applied the release table's factor to every draw, the rule of B112 (Australia 0.742361 at 1 in 10, 0.634262 at 1 in 20; each state's row of `resilience!`). The alternative V38 raised, a draw's own table on its shocked figure (restable 1 gets the leave-one-out factors 0.713504 and 0.602007), is the second file: Australia 22.5 to 35.9 at 1 in 10 (42.0% of draws under 27.6) and 19.1 to 30.5 at 1 in 20 (82.3%); 27.6 inside both. It is a defensible alternative, not an error, and does not change the reading.

**Why a new draws file.** B115's widened file holds Australia only. The state columns need the draws evaluated in the states, so I ran `monte_carlo.mjs` unedited (`MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1`, 2,000 draws, the script's default eight zones). B115's work folder is not on disk; I used a copy of the X054-passing folder of B41 and rebuilt its `land_raster` variant with the land block of `build_variants.py` (the stored one was built on an older land). Validation: the Australian short and long columns equal block A of `monte_carlo_draws_2025-fixed_wide.csv` to the person in all 2,000 draws (maximum difference 0), and all 19 choice columns agree. The 52 regions are not in the draws: with `MC_ZONES=all` the script stops at zone 45 (Northern and Yorke), where the raster land and the release land differ by 152 km2; I did not edit the script. So no regional count (A038, A184, A188, A402) exists on the widened basis.

**Checks.** (a) The release at 10 and 20 years equals average year times factor in all 60 zones to 0.39% at most (the script stops above 0.5%). (b) `check_shocks_ranges_wide.py` recomputes all 192 percentiles and shares in both files from the draws, with the factors read from `analysis/resilience_2025/tables.csv` (rows "data: ABS to 2024-25" and "loo reference"): 192 of 192 agree to one person (shares to 0.0001); it also checks 27 quoted figures. (c) `check_shocks_ranges.py` (B112) still passes. (d) A second run of `shocks_ranges.mjs --wide` is byte-identical.

Reproduce (repository root): `node analysis/paper_a/shocks_ranges.mjs analysis/paper_a/shocks_ranges_wide.csv --wide`; `python3 -I analysis/paper_a/check_shocks_ranges_wide.py`. The draws: `MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 node analysis/sensitivity_2025/monte_carlo.mjs WORK_DIR analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide_states.csv 2000` (about 30 minutes).

## 2. Rerun on the frozen `-3` releases

Scripts changed, each with an option and a default that reproduces the old output: `analysis/paper_a/long_term_and_measures.mjs` (`--release-2011`, `--suffix`), `analysis/paper_a/method_effects_by_region.py` (`--release-2011 FIXED IMPROVED SUFFIX`). Files written: `long_term_levers-3.csv`, `long_term_regions-3.csv`, `method_effects_by_region-3.csv`, `method_effects_summary-3.csv`, `method_status-3.csv`, and `minus3_cell_differences.csv` (every differing cell: file, row, row key, column, old, new; produced by `diff_minus3.py`, 438 cells). The other parts of `long_term_and_measures.mjs` (measures, stores, transfers) are 2025 only and were not rewritten.

Cells that differ from the old output:
* `long_term_levers-3.csv`: 133 cells, all the `release` label (`2011-fixed` to `2011-fixed-3`). No capacity moves.
* `long_term_regions-3.csv`: 54 release labels; 53 populations (every one of the 52 regions and the Northern Territory); 46 ratios. All are in `minus3_cell_differences.csv`. 2011 long term: 18 regions under capacity (17 before), 35 over (36 before), 93.4% of the regions' people in over-capacity regions (93.8% before).
* `method_effects_by_region-3.csv`: 106 population cells and 30 cells of the column "improved (% of published)" (the improved method's capacity moves in 75 of 120 cells on `2011-improved-3`; the corrected method's does not, so "corrected (% of published)" is unchanged). The published capacity and every effect column are the published-method run on 2011-corrected and are not recomputed (no `-3` release of the published method exists), so the improved method's effects that move with the infrastructure area (up to 0.9% of capacity) are the `-2` ones. `method_effects_summary-3.csv` is identical to the old file (0 cells).
* `method_status-3.csv`, 2011 rows (regions over capacity: published, corrected, improved):

| 2011 | Old | `-3`, one population for all three | Published on its own release's population |
|---|---|---|---|
| Short term | 22, 23, 22 | 21, 22, 20 | 22 |
| Long term | 39, 36, 38 | 37, 35, 36 | 39 |
| Corrected to improved, short term | Mackay Whitsunday | Desert Channels; Mackay Whitsunday | |
| Corrected to improved, long term | Western NSW; South East SA | South East SA | |
| Status changes published to corrected (short, long) | 1, 3 | 1, 2 | |

The 2025 rows are unchanged. The `-3` file has one added column, the published count against the published release's own populations (the thesis's). The published method has no `-3` release, so whether "published" means the thesis's populations (22 and 39) or the corrected ones (21 and 37) is a choice for Murray; the register rows carry 22 and 39.

## 3. `decompose_corrected.mjs`

The writer of "Decomposition in every order (B111)" now emits the V37 wording: "the consumption and red-meat-mix layers" with the clause that the consumption layer also carries the fuel, biofuel and timber presets; "-7 people" for an effect that rounds to 0.00 million (the rule: under 5,000 people is printed in people); the long-term sentence "(the sum of the two rows)" for the summed figure and "as one layer" for the combined layer in the eight-layer order. Both section writers also had a fault that added one blank line per run (the slice up to the heading already ended the text); fixed in both.

Rerun (`node decompose_corrected.mjs --average --jobs 3`) from the README as B122 left it: **`README.md` is byte-identical to B122's** (`cmp`), and all csv files of `analysis/comparison_2025` (including `capacity_by_cause_corrected_orders.csv`, 2,400 rows) are byte-identical (md5 before and after). The default mode (B76 section) was also run: its csv is byte-identical; it still drops the hand-added V29 paragraph from the README (X129, not in this brief), so I restored the README before the `--average` run. Not done: a second consecutive `--average` run to demonstrate the blank-line fix directly. One inconsistency kept because B122's text has it: the short-term bullet names the combined layer "land and livestock together" in the eight-layer order, the long-term bullet "as one layer".

## 4. `cross_method_local.csv`

Script `analysis/method_tests_2025/harmonised_lines.py`; files regenerated `cross_method_local.csv` (`harmonised_comparison_lines.csv` unchanged byte for byte); `README.md` of the folder: the two sentences that said the csv prints 103 now say what it prints. The secondary footprint row now takes column (b) of `harmonised_comparison.csv` for builds 1 and 3 (cropland-bound and crop and pasture together; build 3 on the 2021-23 world yields), with the 1990 reading as a qualifier in the text.

Cells changed (row; column; before; after):
* Footprint, secondary: productivity basis "...physical hectares" to "..., on 2021-23 world yields"; reading "103 to 343 (cropland-bound reading 103 to 160; crop and pasture together 268 to 343; three builds...)" to "146.2 to 343.4 (cropland-bound 146.2 to 159.8; crop and pasture together 287.7 to 343.4; builds 1 and 3 on 2021-23 world yields; build 3 on the thesis's 1990 world yields reads 103.1 and 268.4)"; low 103.0 to 146.2; high 343.0 to 343.4; low over corrected 2.48 to 3.52; high over corrected 8.27 (same); low over improved 1.92 to 2.73; high over improved 6.4 to 6.41; source `cross_method.csv` to `harmonised_comparison.csv column (b)`.
* Aggregate, secondary: basis text gains "footprint on 2021-23 world yields (103 at 1990 world yields)"; reading "103.0 to 343.0" to "133.8 to 343.4"; low 103.0 to 133.8; high 343.0 to 343.4; low over corrected 2.48 to 3.22; high over corrected 8.27 (same); low over improved 1.92 to 2.5; high over improved 6.4 to 6.41.
* The HALF secondary row (276) and every primary row are unchanged.

README match: the folder README states 146.2 to 343.4, 3.52 to 8.27 and 2.73 to 6.41 for the footprint and 133.8 to 343.4, 3.2 to 8.3 and 2.5 to 6.4 for the aggregate; these now equal the csv cells.

## 5. `foran_poldy_balance.py`

Fixed: the head count is the mean of 2021, 2022 and 2023 (26.203 million) in place of 2021 and 2022 (26.079), the years of the food use. Regenerated `foran_poldy_balance.csv`. **One cell changed:** "actual food use per person 2021-23 (kg)", fish: 25 to 24 (24.58 to 24.46 unrounded). The other printed cells keep their integers; unrounded, meat 113.4 to 112.8 kg, grain 112.4 to 111.9; the actual-use readings meat 41.07 to 41.27, grain with feed grain 126.59 to 126.75, fish 12.00 to 12.06 (printed 41, 127, 12 before and after).

Claim rows carrying the old figure: **B144** (tier B): "fish 17 kg (25: Australians now eat more fish...)" and its value list "...; 25"; the analysis README line 243 says the same. Rows B147, B149, B151, B153, B154 print integers and do not move.

Not fixed, outside the brief: `bases_fidelity.py` line 68 repeats the 2021-22 head count for the intake readings, so `bases.csv`, the README rows that describe the Foran and Poldy head count (lines 373, 374, 383), and the Foran and Poldy readings in `intake_variant.csv` and `gap_attribution_readable.csv` (41.1, 12.0, 126.6 against 41.3, 12.1, 126.8 on three years) still carry the two-year count. The coordinator needs a job for these.

## Claim rows that move (the register was not edited)

Tier A:

| id | tier | before | after |
|---|---|---|---|
| A014 | A | 30.8 (pending note: range 27.0 to 34.0 or 29.2 to 32.5) | 30.8, widened range 23.1 to 36.5 million; 27.6 inside |
| A183 | A | 1.12 (pending: 0.98 to 1.23 or 1.06 to 1.18) | 1.12, widened range 0.84 to 1.32 (0.837 to 1.322) |
| A187 | A | 0.95 (pending: 0.83 to 1.05 or 0.90 to 1.01) | 0.95, widened range 0.72 to 1.13 (0.715 to 1.130) |
| A196 | A | 0.89; 0.95 (pending: straddles on the 13-choice range; 92% below on the herd-cycle range) | base holds; on the widened range 37.0% of draws are under 27.6 million at 1 in 10 and 77.65% at 1 in 20, so neither "feeds itself at 1 in 10" nor "not at 1 in 20" holds across the range |
| B046 | A | value 103 to 343 (statement already reads 146 to 343, 103 at 1990 yields) | value 146.2 to 343.4, with 103 as the 1990-yield qualifier (the csv now matches the statement) |
| B156 | A | value 103 to 343; 12 to 41 | secondary 133.8 to 343.4 (aggregate), footprint 146.2 to 343.4; 103 qualifier only |

Tier B and C:

| id | tier | before | after |
|---|---|---|---|
| A195 | B | 26.3 (23.0 to 29.0 on the 13-choice range; 25.0 to 27.8 herd-cycle) | 26.3, widened 19.7 to 31.2 |
| A390, A391 | B | 27.0 to 34.0; 23.0 to 29.0 (published 13-choice range) | unchanged; the widened ranges 23.1 to 36.5 and 19.7 to 31.2 are new companions |
| A392 | B | 0.98 to 1.23 and 0.83 to 1.05 (13-choice) | unchanged; widened 0.84 to 1.32 and 0.72 to 1.13 are new companions |
| A143 | B | 18 | 18 (the rerun gives 18 under capacity; B122's value holds) |
| A144 | B | 93 | 93 (93.4%) |
| A151 | B | 13 published; 18; 21 | 18 and 21 hold |
| A308 | B | 22; 22; 20 | 21; 22; 20 with one population for all three; 22; 22; 20 with the published release's own populations: a choice for Murray |
| A309 | B | Desert Channels; Mackay Whitsunday | holds |
| A310 | B | 39; 35; 36 | 37; 35; 36 with one population; 39; 35; 36 with the published release's own populations: a choice for Murray |
| A311 | B | South East SA | holds |
| B247, B350 | B | B247 value "3 to 8; 103 to 343"; B350 133.8 to 343.4, 146.2 to 343.4 | B350 now equals the csv; B247's value "103 to 343" is the 1990-yield reading: 146.2 to 343.4 on current yields (statement already says "146 to 343") |
| B144 | B | fish 25 kg | fish 24 kg |
| A038, A184, A188, A402 | A, A, B, B | regional counts on the 13-choice and herd-cycle ranges | cannot be computed on the widened basis (no regional draws; see section 1) |

Defects that this report closes, for the register job: X130 (generator wording, item 3), X131 (item 4), X137 (item 5, the script; `bases_fidelity.py` still carries the count, above). X129 stays open.

Register rows touched: **none**.

## Files changed

New: `analysis/paper_a/shocks_ranges_wide.csv`, `shocks_ranges_wide_own_table.csv`, `check_shocks_ranges_wide.py`, `long_term_levers-3.csv`, `long_term_regions-3.csv`, `method_effects_by_region-3.csv`, `method_effects_summary-3.csv`, `method_status-3.csv`, `minus3_cell_differences.csv`, `diff_minus3.py`; `analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide_states.csv`.
Edited: `analysis/paper_a/shocks_ranges.mjs`, `long_term_and_measures.mjs`, `method_effects_by_region.py`, `README.md` (two sections appended); `analysis/sensitivity_2025/README.md` (one section appended); `analysis/comparison_2025/decompose_corrected.mjs`; `analysis/method_tests_2025/harmonised_lines.py`, `cross_method_local.csv`, `foran_poldy_balance.py`, `foran_poldy_balance.csv`, `README.md` (two sentences).
Rewritten byte-identical by default reruns: `analysis/comparison_2025/` csv files and `README.md`, `analysis/paper_a/method_effects_by_region.csv`, `method_effects_summary.csv`, `method_status.csv`, `analysis/method_tests_2025/harmonised_comparison_lines.csv`.

## Wrong-value check

`check_shocks_ranges_wide.py` recomputes the 192 percentiles and shares of both widened files from the draws and checks 27 quoted national figures (all pass, exit status 0; the 13-choice check `check_shocks_ranges.py` also passes).

*Example, a deliberate wrong value:* `python3 -I analysis/paper_a/check_shocks_ranges_wide.py wide 10 p5 24.0` replaces the quoted 1-in-10 lower end (23.1) with 24.0 and fails with exit status 1:
`FAIL quoted wide 1-in-10 p5 = 24.0 but the file gives 23.0989`.
