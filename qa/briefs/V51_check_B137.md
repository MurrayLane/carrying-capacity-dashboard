# Checker brief V51: blind check of the eight-layer table, the meat identity, the drought factor variants and the residue bound (B137)

You are a blind checker. `qa/briefs/_checker_rules_results_wave.md` applies: state the tolerance first; show one deliberate wrong value failing your own check; open the builder's report and outputs only after you have derived your own figures. Plain language; no em dashes; no time words. No git; no subagents; no network. Write only `qa/reports/V51_check_B137.md`.

The builder's job: `qa/briefs/B137_paper_A_layers_identity_factor_variants.md` (read it first). The builder's report: `qa/reports/B137_paper_A_layers_identity_factor_variants.md` and the files it names (new files under `analysis/comparison_2025/`, `analysis/paper_a/`, `analysis/resilience_2025/`, `analysis/years_2025/`), to be opened last.

Your own route:
1. From `analysis/comparison_2025/capacity_by_cause_corrected_orders.csv` (eight-layer rows), derive the national all-orderings averages, forward and reverse values, both presets, and the count of regions where land-and-livestock is the largest layer (expected from V37: +2,456,649 short term, -598,893 long term; 42 and 31 regions).
2. From the FAOSTAT bulk files on disk (the builder names them; find them under `data/` or the archive) derive Australia's meat production and meat eaten (food supply) for 2021-23 and 2010-12, the ratio, and the people fed at the model's per-person meat intake; compare with model capacity over population (41.5 over 27.6 and 33.3 over 22.3).
3. With `analysis/resilience_2025/resilience.py`'s method on the ABS cereal series (the historic workbook the project holds), derive the 1-in-10 and 1-in-20 factors from 1950-51, 1970-71 and 1990-91 starts, unweighted and area-weighted where areas exist; evaluate national short-term capacity under each with the evaluator (`web/src/model/evaluator.js`, release `2025-fixed`); state whether capacity at 1 in 10 is above 27,608,200 in every variant.
4. Residue bound: run `2025-fixed` with the 2011 grazing area and output and diet fixed (the builder's `definitional_residue.mjs` describes the setting: derive it yourself from the release files) and report the change in short-term capacity (builder: -194,427).
5. X118: run the builder's `analysis/years_2025/build_years_fixed.py` and confirm it reproduces `years.csv` on placeholders in all 128 cells; report the base-row staleness (48,004,473 against 48,265,660).
Then compare every cell you can reach and the proposed sentences (`abs_frame_feedlot_and_driver_sentences.csv`) for overclaim.

Report: tolerance; wrong-value example; your figures; comparison table (item; builder; yours; pass or fail); claim rows the builder names (A382, A317, A223, A014) with your verdict; anything you would do differently; register rows touched (none).
