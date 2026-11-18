# Round 2, B137: land and livestock as one layer, the identity, the ABS frame, drought factor variants, the single-year series

New files only; nothing existing was edited except rows X116 and X118 of qa/defects.csv. Report: qa/reports/B137_paper_A_layers_identity_factor_variants.md.

| File | What it is | Rerun |
|---|---|---|
| analysis/comparison_2025/decomposition_eight_layer_table.csv | Table 2 on eight layers, national, both presets, average with forward and reverse walks | python3 -I analysis/comparison_2025/make_eight_layer_table.py |
| analysis/comparison_2025/decomposition_eight_layer_regional_counts.csv | Largest layer by region on eight and nine layers, average, forward, reverse | same script |
| analysis/comparison_2025/movers_land_ratio_corrected.csv | X116: land_only_ratio on the corrected tier, 106 rows | python3 -I analysis/comparison_2025/movers_land_ratio_corrected.py |
| analysis/paper_a/meat_balance_identity.csv | Production over consumption of meat (and red meat, milk) against model capacity over population, 2025 and 2011 | python3 -I analysis/paper_a/meat_balance_identity.py [FAO_DIR] |
| analysis/paper_a/definitional_residue.csv | Upper bound on the part of the land and livestock rise a change of grazing-area definition could carry | node analysis/paper_a/definitional_residue.mjs analysis/paper_a/definitional_residue.csv |
| analysis/paper_a/abs_frame_feedlot_and_driver_sentences.csv | Ten sentences for the paper with source rows, pages and what Murray must fetch | written by hand |
| analysis/resilience_2025/drought_factor_variants.csv, livestock_output_ratio.csv | Factors and capacities by variant; observed red meat output ratio | python3 -I analysis/resilience_2025/resilience_variants.py HISTORIC_XLSX ABS_LIVESTOCK_DIR ARCHIVE_XLS |
| analysis/years_2025/ | X118: build_years_fixed.py, rebuild_years.sh, two rebuilt year series | sh analysis/years_2025/rebuild_years.sh ABS_DIR WORK_DIR |

Inputs held outside the repository: the FAOSTAT bulk files (sha256 checked against qa/fao_bulk_hashes.csv), the ABS historic workbook, the ABS livestock products files and the archive resilience workbook. Their paths are arguments.
