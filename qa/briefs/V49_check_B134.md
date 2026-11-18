# Checker brief V49: blind check of the Paper B drought bound, the pasture and PAL one-at-a-time runs (B134)

You are a blind checker. `qa/briefs/_checker_rules_results_wave.md` applies: state the tolerance first; show one deliberate wrong value failing your own check; open the builder's report and outputs only after you have derived your own figures. Plain language; no em dashes; no time words. No git; no subagents; no network. Write only `qa/reports/V49_check_B134.md`.

The builder's job: `qa/briefs/B134_paper_B_drought_bound_and_pasture.md` (read it first). The builder's report: `qa/reports/B134_paper_B_drought_bound_and_pasture.md` and the files it names (under `analysis/resilience_2025/`, `analysis/method_tests_2025/`, `analysis/pasture_2025/`), to be opened last.

Your own route, with the evaluator (`web/src/model/evaluator.js`) on `2025-fixed`, Australia:
1. Apply the release's drought factors (resilience sheet; 1 in 5, 10, 20, 50, 100) to crop yields only and to every yield, short term and long term; derive the capacities (expected from B112: 41.2, 41.0, 40.4 crop-only against 30.8, 26.3, 18.9 at 1 in 10, 20, 100; long term 24.7 against 15.6 at 1 in 100); the drought factor 41.5 over the 1-in-100 figure on each rule; the share of the fall at 1 in 10 and 1 in 100 that the pasture-fed rows carry; and the failure probability at 27,608,200 by linear and log-linear interpolation on each rule (both-applied expected 5.8 to 6.1%; say what the crop-only curve supports).
2. Pasture output at minus 20% and plus 20% with everything else at base, short term, through the model (scale the pasture-fed animal yields); report capacity and whether pasture binds; compare with the closed form in `analysis/pasture_2025/pairing_relaxed.py` and say what the residual is.
3. The energy requirement at PAL 1.2 and 2.2 (food amount PAL over 1.4) with everything else at base, both presets, corrected release; and short term on `2025-improved`.
4. Then open the builder's files and compare every cell; check the S5 sentences against `sobol_2025-fixed.csv` (meat window 0.24 short and 0.14 long; meat calibration 0.03 and 0.01) and the proposed paper sentences for overclaim.

Report: tolerance; the wrong-value example; your figures; the comparison table (item; builder; yours; pass or fail); the claim rows the builder says move with your verdict (Tier A: B001, B003, B096, B130, B137, B167, B188, B193); anything you would do differently; register rows touched (none).
