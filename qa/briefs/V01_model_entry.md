# Verifier brief V01: the model's own entry (the methods paper's headline numbers)

You are an independent checker. You receive the requirement and a recipe, and nothing else: no earlier finding, no explanation of what the numbers are supposed to be. If you come across a document that states the expected result, do not read it as evidence; produce the evidence yourself.

Hard limits: read only. Never edit, create, move or delete a file inside /home/user/carrying-capacity-dashboard or /home/user/carrying-capacity-models. Write your working files only under /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v01/ (create it). Do not run git commands that change anything (git log, git show and git status are fine). Do not spawn subagents. Do not use the network. Plain language in the report; no time words (tonight, later, for now).

## Requirement
For Australia (zone 1) on each of the three frozen releases `2025-mirror`, `2025-fixed` and `2025-improved`, establish independently:
R1. the short-term and long-term capacity (people) that the model produces at the release's own default settings;
R2. that each release's recorded input hashes match the files on disk (the release is locked);
R3. the 5th and 95th percentiles of the Monte Carlo draws for the short term and the long term, computed by you from the raw draws, not from any summary file.
Report each value you obtain, and whether it holds against the recipe's own outputs.

## Recipe
1. Releases live in `releases/<id>/release.json`; the resolver and lock logic are in `web/scripts/releases.mjs` and `web/scripts/lock-release.mjs` (read them; do not run lock-release). For R2, recompute the sha256 of every file listed under `inputs` in each release.json and compare with the recorded value.
2. The built model for a release is `web/public/data/<id>/model.json` and `web/public/data/<id>/regions.json`; `results/releases.json` records a sha256 of each built file. For R1, confirm those hashes, then evaluate the model yourself with the evaluator in `web/src/model/evaluator.js` (an ES module; see `analysis/comparators_2025/rerun.mjs` for the three lines that load a release and call `evaluate`, and copy only that pattern, not its scenarios). Evaluate zone 1 with `R.land`, `R.presets.short` (then `R.presets.long`) and `population: R.population`. Report `capacity` to the nearest person for each release and preset.
3. Compare your R1 values with `results/<id>.csv` (zone 1, preset short and long, column `capacity`). Report the difference, if any.
4. For R3, the draws are `analysis/sensitivity_2025/monte_carlo_draws_<id>_all.csv` (one row per draw per zone and setting; read the header to find the capacity column and the zone and setting columns). For zone 1 and each setting, compute the 5th and 95th percentiles of the capacity over the 1,000 draws (state the percentile definition you use; use the nearest-rank or linear interpolation method and say which). Compare with `results/ranges_<id>.csv` (zone 1, `p5` and `p95`). Report both and the difference.
5. State clearly anything that could make your check pass without being right (for example, if the draws file and the ranges file could have been produced from the same error), and anything you could not do.

## Report format
For each of R1, R2, R3 and each release: `holds`, `does not hold`, or `cannot determine`, the values you obtained, the values in the recipe's outputs, and the difference. Then a short list of what would have made the check fail and whether it was capable of failing. Then anything surprising.
