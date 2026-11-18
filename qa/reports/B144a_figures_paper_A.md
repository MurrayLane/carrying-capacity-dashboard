# B144a report: the figures of Paper A

Status: eight figures drawn (Figure 6 is split: the main figure plus a supplementary Figure S6 for the scenarios). No paper, claims register, results or tenders-platform file touched; no git; no network.

## Notes for the coordinator

* The dataviz skill file SKILL.md was not at the path named in the brief (the folder holds only references/ and scripts/); I read all five named references (choosing-a-form, color-formula, marks-and-anatomy, anti-patterns, palette) and followed them. The palette validator was not run: categorical slots 1 and 2 only (blue, orange) plus grey; diverging map is blue-dark, neutral grey, red from the palette.
* Size: Figure 1 prints at 90 mm wide; all others at 190 mm wide (53-row figures cannot read at 90 mm). All text is 7 pt or larger at print size (8 pt titles).
* Scenarios by region: `scenarios_by_region.csv` holds national figures and counts only; the per-region values are in `results/scenarios_2025-fixed.csv` (read only), so the scenario panel is the supplementary Figure S6 (`fig6s_scenarios.py`). Figure 6 itself draws three return periods (average year, 1 in 10, 1 in 20; the ones with ranges); 1 in 5, 50 and 100 are in the csv and not drawn.
* Figure 1: the 2011 base has no range; the caption names the 13-choice basis and shows both the 13-choice and the 19-choice 2025 ranges. If "the 13-choice 2011 basis" meant something else, edit the caption text.
* Figure 3 shows each layer as a percentage of the region's 2011 capacity (colour clipped at 50%; 33 cells exceed it, labelled with true values). The draft placeholder says "forward walk"; the brief says all-orderings average, which is what is drawn, so the placeholder text and the paper sentence "on the forward walk" need the patch.
* Figure 4: the partition band exists only for 7 random groups, so it is a shaded range bar at the State level (uniform grouping, state-yield basis, 200 draws), not a band across all levels.
* Figure 7: replaces `plot_method_effects.py` (pale RdBu midpoint, old csv). 10 cells are blank in the csv (Alinytjara Wilurara short term, published capacity zero) and are drawn empty. Column names carry (C) for the two corrections.
* Figure 2 colours: blue and orange mean verdict here (holds / does not hold), not year; shape also differs (diamond vs circle) so it reads in greyscale. Figure 8 colours: red over capacity, blue room to spare.
* Zero or tiny capacities on log axes are drawn at the axis edge (floor stated in each caption): Figure 2 one end value, Figure 5 nine, Figure 6 and S6 a few.
* Claims rows are matched only by `output_file` equal to a source csv (`finalize_figures_csv.py`); the register has no rows for method_effects_by_region-3.csv, so Figure 7 lists none. Treat the lists as candidates, not a verified set.

## Figure list and the message each carries

* Figure 1: Capacity was about 1.5 times the population in both years, and the 2025 range lies wholly above the population.
* Figure 2: Eight short-term flips are arrows that cross the status line, and none is robust and free of a flag.
* Figure 3: Land and livestock and diet layers dominate the regional change, and layer effects reach well beyond 50% in a few regions.
* Figure 4: Capacity summed over smaller units falls steadily to about 37% (short) and 20% (long) at SA2 in 2025.
* Figure 5: The weather allowance and liquid fuel dominate what long-term settings are worth, and the long-term margin is below 1 in many regions where people live.
* Figure 6: More regions fall under capacity as the bad year gets worse, and ranges cross the status line for a few regions.
* Figure 7: Method choices move regions in both directions, and the biodiesel correction mostly raises long-term capacity.
* Figure 8: Over-capacity regions are the capital-city regions; room to spare sits in the inland cropping regions.
* Figure S6: Named scenarios tip only a handful of regions, all in the long term.

## Files written (all under analysis/figures_2025/paper_A/ except this report)

Scripts: `_common.py`, `fig1_national.py`, `fig2_regional_change_flips.py`, `fig3_layer_effects.py`, `fig4_scale_curve.py`, `fig5_long_term.py`, `fig6_shocks.py`, `fig6s_scenarios.py`, `fig7_method_effects.py`, `fig8_migration_map.py`, `finalize_figures_csv.py`.
Outputs (PNG at 300 dpi and SVG each): `fig1_national_capacity_population`, `fig2_regional_change_flips`, `fig3_layer_effects`, `fig4_scale_curve`, `fig5_long_term`, `fig6_shocks`, `fig6s_scenarios`, `fig7_method_effects`, `fig8_migration_map`; plus `figures.csv`.
Rerun: `python3 -I analysis/figures_2025/paper_A/<script>.py` (any directory), then `finalize_figures_csv.py`. Every script header names its csv files and columns.

## Caption text, source csv and claims rows per figure

### Figure 1

Files: fig1_national_capacity_population.png; fig1_national_capacity_population.svg
Source csv: results/2011-fixed-3.csv; results/2025-fixed.csv; results/ranges_2025-fixed_wide.csv
Columns: population, capacity, capacity_per_person (zone=1, preset=short); p5, p95 (zone=1, setting=short, variant wide and existing)

National short-term capacity against population, Australia, 2011 and 2025, corrected method. Each dot is one year; a dot above the line has capacity above population. The 2011 value is the base case on the corrected 2011 release (13-choice basis) and has no range of its own. The 2025 bars are the 5th to 95th percentile of capacity over 2,000 draws: the thin line is the widened 19-choice range, the thick band the earlier 13-choice range. Sources: results/2011-fixed-3.csv, results/2025-fixed.csv, results/ranges_2025-fixed_wide.csv.

Claims rows (by output_file): CLAIMS_PLACEHOLDER

### Figure 2

Files: fig2_regional_change_flips.png; fig2_regional_change_flips.svg
Source csv: analysis/paper_a/movers-3.csv; analysis/paper_a/regional_flips-3_wide.csv
Columns: movers-3: zone, name, cap2011, cap2025, dcap, pop2011, pop2025, dpop, over2011, over2025 (preset=short); regional_flips-3_wide: term=short, flip, artefact flag, 2025 status robust to the range, older 2011 boundary flag

Change in short-term capacity and population by region, 2011 to 2025, corrected method, 53 regions ordered by 2025 capacity over population. Each arrow runs from the 2011 to the 2025 capacity over population on a log scale; the line at 1 is the status line, so an arrow that crosses it is a status flip (bold names). Flips are coloured by the verdict on the 19-choice 2025 ranges (blue: the 2025 status holds in the range; orange: it does not) and open markers carry a land-definition or older 2011 boundary flag. The two columns give the change in capacity and in population in thousand people. Sources: analysis/paper_a/movers-3.csv, analysis/paper_a/regional_flips-3_wide.csv.

Claims rows (by output_file): A041 A042 A043 A057 A067 A339 A420 A421 A422

### Figure 3

Files: fig3_layer_effects.png; fig3_layer_effects.svg
Source csv: analysis/comparison_2025/capacity_by_cause_corrected_orders.csv; analysis/paper_a/movers-3.csv; analysis/comparison_2025/decomposition_eight_layer_regional_counts.csv
Columns: game=eight_layers_land_livestock_one: layer, preset, zone, shapley_mean; movers-3: zone, preset, cap2011

Effect of each layer on short-term and long-term capacity in each of the 53 regions, 2011 to 2025, corrected method: the average over all 40,320 orderings of the eight layers, as a percentage of the region's 2011 capacity. Blue raises capacity and red lowers it; colour is clipped at 50% and a cell is labelled when the effect is 25% or more, with its true value if clipped. Regions are grouped by state. The last column is the total change, the sum of the eight layers. Sources: analysis/comparison_2025/capacity_by_cause_corrected_orders.csv, analysis/paper_a/movers-3.csv.

Claims rows (by output_file): A057 A067 A372 A373 A374 A375 A376 A377 A378 A379 A380 A381 A382 A383 A384 A385 A386 A387 A388 A450

### Figure 4

Files: fig4_scale_curve.png; fig4_scale_curve.svg
Source csv: results/scale_curve.csv; analysis/scale_curve_2025/scale_partition_summary.csv
Columns: scale_curve: release, preset, level, units, sum_capacity, share_of_national, yield_basis=state; scale_partition_summary: release, preset, grouping=uniform, p5, p95

The scale curve: the sum of the units' capacities as a share of the national capacity at each level from the nation to SA2, 2011 and 2025, short and long term, state-yield basis, corrected method. Each unit takes the yields, climate zone and settings of its state and the national diet and waste settings; the number of units is under each level. Circles join the administrative levels; diamonds are the 53 NRM regions. The shaded bar at the State level is the 5th to 95th percentile of the same sum over 200 random groupings of the SA2s into 7 groups, the partition effect without the real state boundaries. The SA levels use 2020-21 land with each year's population. Sources: results/scale_curve.csv, analysis/scale_curve_2025/scale_partition_summary.csv.

Claims rows (by output_file): A015 A016 A017 A018 A074 A075 A076 A077 A078 A079 A080 A081 A082 A083 A084 A085 A086 A087 A088 A089 A090 A091 A092 A093 A094 A095 A096 A097 A098 A099 A100 A101 A102 A103 A104 A105 A106 A107 A108 A109 A111 A120 A458 A459

### Figure 5

Files: fig5_long_term.png; fig5_long_term.svg
Source csv: analysis/paper_a/long_term_levers-3.csv; analysis/paper_a/long_term_regions-3.csv
Columns: long_term_levers-3: release=2025-fixed, zone=1, lever, alone, without; long_term_regions-3: release, zone, name, ratio

Long-term results, corrected method, own yields. (a) What each long-term setting is worth for Australia in 2025: the change in the long-term capacity when that one setting is put back to its short-term value, as a percentage of the long-term capacity (the settings are listed with their short-term and long-term values; timber, infrastructure area and the reserve share have no effect). (b) Long-term capacity over population in each of the 53 regions, 2011 (blue) and 2025 (orange), ordered by the 2025 value, on a log scale; the line at 1 is the status line and values below 0.01 are drawn at the axis edge. Sources: analysis/paper_a/long_term_levers-3.csv, analysis/paper_a/long_term_regions-3.csv.

Claims rows (by output_file): A417

### Figure 6

Files: fig6_shocks.png; fig6_shocks.svg
Source csv: analysis/paper_a/shocks_by_region-3.csv; analysis/paper_a/shocks_ranges_wide_zones.csv
Columns: shocks_by_region-3: release, zone, name, return_period, capacity, population; shocks_ranges_wide_zones: preset=short, return_period, zone, capacity_over_population_p5, capacity_over_population_p95, capacity_over_population_central

Exposure to shocks by region: capacity over population in each of the 53 regions in an average year, at 1 in 10 years and at 1 in 20 years, 2011 (blue) and 2025 (orange), own yields, corrected method, regions ordered by the 2025 average-year value, log scale. The orange line is the 5th to 95th percentile of the region's 2025 capacity over population on the widened 19-choice range; 2011 has no range. A region is over capacity where the dot is left of the line at 1. Values below 0.001 are drawn at the axis edge. The 1-in-5, 1-in-50 and 1-in-100 results are in the csv. Sources: analysis/paper_a/shocks_by_region-3.csv, analysis/paper_a/shocks_ranges_wide_zones.csv.

Claims rows (by output_file): A370 A402

### Figure 7

Files: fig7_method_effects.png; fig7_method_effects.svg
Source csv: analysis/paper_a/method_effects_by_region-3.csv
Columns: vintage=2025; term; zone; name; the eight module columns (% of published); corrected (% of published); improved (% of published)

The effect of each method choice on capacity in each of the 53 regions, 2025 data, short and long term, as a percentage of the published-method capacity (Lane 2014). Each choice is applied alone to the published method. Blue raises capacity and red lowers it; colour is clipped at 40% and cells of 10% or more are labelled with their value. The two corrections, marked (C), are the beef carcase yield and the biodiesel yield; the other six are improvements. The last two columns apply the two corrections together (corrected method) and all eight choices together (improved method). Regions are grouped by state. Source: analysis/paper_a/method_effects_by_region-3.csv.

Claims rows (by output_file): none matched by output_file

### Figure 8

Files: fig8_migration_map.png; fig8_migration_map.svg
Source csv: analysis/paper_a/movers-3.csv; data/sa2/centroids.csv; data/nrm2011/land_use_by_sa2_nrm2011_piece.csv; pipeline/land/zone_to_nrm2011.json
Columns: movers-3: zone, name, preset=short, pop2025, cap2025; centroids: sa2_code, lon, lat; piece file: zone_name (SA2 code), nrmr_code_2011, area_km2

The migration map redrawn: population less short-term capacity in each of the 53 regions, 2025, corrected method, average year. Each region is a circle at the area-weighted mean of its SA2 centroids (the repository holds no region polygons; grey dots are SA2 centroids). Circle area is proportional to the size of the excess, in people; red is over capacity and blue is room to spare, with a neutral grey at zero and the colour step following the square root of the excess. Sources: analysis/paper_a/movers-3.csv; centroids from data/sa2/centroids.csv and data/nrm2011/land_use_by_sa2_nrm2011_piece.csv.

Claims rows (by output_file): A057 A067

### Figure S6

Files: fig6s_scenarios.png; fig6s_scenarios.svg
Source csv: results/scenarios_2025-fixed.csv; analysis/paper_a/scenarios_by_region.csv
Columns: scenarios_2025-fixed: scenario, preset, zone, name, population, capacity; scenarios_by_region: reference_release=2025-fixed, scenario, term, regions that tip over capacity against the reference

Supplementary figure S6. The named scenarios by region, 2025 data, corrected release (each grain store with its own resilience table): capacity over population in each of the 53 regions under each scenario, short and long term, on a log scale; the line at 1 is the status line. Orange dots are regions that are under capacity in the reference and over capacity in the scenario; their names are listed for the long term, and no region tips in the short term. Sources: results/scenarios_2025-fixed.csv, analysis/paper_a/scenarios_by_region.csv.

Claims rows (by output_file): A201 A202 A203 A204 A205 A206 A207 A208 A209 A210 A211 A212 A213 A214 A215 A216 A217 A218 A219 A220 A221 A222 A223 A224 A225 A226 A227 A264

## Checks

All nine scripts pass `--check` (each recomputes one printed value from the csv by a second route):

* Fig 1: 2025 national short-term capacity 41.5 million
* Fig 2: Central West NSW capacity change 464 thousand
* Fig 3: national short-term consumption layer 4.15 million
* Fig 4: 2025 SA2 share 37%
* Fig 5: weather allowance +119%
* Fig 6: 21 regions over capacity at 1 in 10, 2025
* Fig S6: 5 regions tip, fuel-csiro-340, long term
* Fig 7: biodiesel effect South East Queensland, long term, 97.9%
* Fig 8: Port Phillip and Westernport excess 5.38 million

Wrong-value check: `python3 -I analysis/figures_2025/paper_A/fig1_national.py --check --expect 41.9` prints `check 2025 national short-term capacity, million: recomputed 41.5034, plotted 41.5035, expected 41.9 -> FAIL` and exits 1; the correct expected value 41.5 prints OK. The same `--expect` flag plants a wrong value in every script.
