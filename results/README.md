# Results

Generated files; do not edit. They are the one source of the numbers on the dashboard's change pages and in the papers: a paper table is a script over these files, never typed.

* `<release>.csv`: every zone (60) and both presets (short, long) at the release's own defaults. Columns: `release, zone, name, kind, parent, preset, population` (the population the capacity is set against),
  `capacity` (people, rounded), `capacity_per_person` (capacity over population; below 1 is over capacity), `over_capacity` (1 if the population exceeds the capacity), `land_km2`, and the settings that drive the preset
  (`resilience, meategg, redmeat, losses, recycling, organic, fuel, biofuel`).
* `comparison_cells.csv`: the grid of data vintage (2011, 2025) by method tier (published, corrected, improved; `methods/README.md`) with the corrections, the improvements and the data as steps of one path from the published 2011 result to the improved 2025 result, and the data effect on each tier.
* `method_effects.csv`: the effect of each method module alone and in sequence (the corrections first, then the improvements) on each data vintage, the capacity after the corrections and after all of them, and the interaction (the modules are those of `2025-improved`).
* `scenarios.csv`: the named scenarios of `scenarios/scenarios.json` (waste at the national target or none, recycling none or half, long-term fuel 156 or 340 litres, a grain store of one or two years, field-crop yields 12% or 24% lower) for every zone and both presets, with the change from the reference (the improved release at its defaults). A scenario is a release plus settings overrides, not a method change; it is not a forecast.
* `releases.json`: each release's label, status, parent, method modules and the SHA-256 of the built `model.json` and `regions.json` it was evaluated from.

Regenerate after any change to a release, module or data file: `cd web && npm run results` (about a minute). The test suite fails if `2011-corrected.csv` or `2025-improved.csv` is stale.

* `ranges_2025-mirror.csv`, `ranges_2025-improved.csv`: Monte Carlo ranges (1,000 Latin hypercube draws, `analysis/sensitivity_2025/monte_carlo.mjs`, `MC_RELEASE=<id> MC_LONG=1 MC_ZONES=all`) for all 60 zones: the 5th, 25th, 50th, 75th and 95th percentiles of capacity, the base, and the share of the variance each of ten input choices explains. The draws are in `analysis/sensitivity_2025/monte_carlo_draws_<release>.csv`. They vary thirteen choices (yield group factors, the meat window, the diet shares, fuel, biofuel, timber, the organic factor and share, and the long-term resilience table, long-term fuel and feeding benchmark); the law, the grain store and the time frame are scenario switches and are not sampled, and the 2011 cells have no ranges. The draws are in `analysis/sensitivity_2025/monte_carlo_draws_<release>_all.csv`.
* `likely_range_2025-mirror.csv`, `likely_range_2025-improved.csv`: the quick range of 34 model runs (`rss_check.py`, within 10% of the Monte Carlo width) for every zone and preset at the release's defaults, and whether the population is robustly over capacity, robustly under, or uncertain (inside the range): the data for the dashboard's map classes (DELIVERY.md).

Not in these files: the decomposition of the change into population, land, yield and other data causes (`analysis/comparison_2025/`, which stays the reference for the data effect) and per-input requirements.
