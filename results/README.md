# Results

Generated files; do not edit. They are the one source of the numbers on the dashboard's change pages and in the papers: a paper table is a script over these files, never typed.

* `<release>.csv`: every zone (60) and both presets (short, long) at the release's own defaults. Columns: `release, zone, name, kind, parent, preset, population` (the population the capacity is set against),
  `capacity` (people, rounded), `capacity_per_person` (capacity over population; below 1 is over capacity), `over_capacity` (1 if the population exceeds the capacity), `land_km2`, and the settings that drive the preset
  (`resilience, meategg, redmeat, losses, recycling, organic, fuel, biofuel`).
* `comparison_cells.csv`: the two-by-two of data vintage and method (`methods/README.md`), with the data effect, the method effects and their interaction.
* `method_effects.csv`: the effect of each improved-method module alone and of both together on each data vintage, with their interaction (the modules are those of `2025-improved`).
* `releases.json`: each release's label, status, parent, method modules and the SHA-256 of the built `model.json` and `regions.json` it was evaluated from.

Regenerate after any change to a release, module or data file: `cd web && npm run results` (about a minute). The test suite fails if `2011-corrected.csv` or `2025-improved.csv` is stale.

* `ranges_2025-mirror.csv`, `ranges_2025-improved.csv`: Monte Carlo ranges (1,000 Latin hypercube draws, `analysis/sensitivity_2025/monte_carlo.mjs`, `MC_RELEASE=<id>`) for Australia and the seven state zones: the 5th, 25th, 50th, 75th and 95th percentiles of capacity, the base, and the share of the variance each of ten input choices explains. The draws are in `analysis/sensitivity_2025/monte_carlo_draws_<release>.csv`. They vary the ten input choices only (yield group factors, the meat window, the diet shares, fuel, biofuel, timber, the organic factor and share); resilience, the recycling uptake and the law are not sampled, and the 2011 cells have no ranges.

Not in these files: the decomposition of the change into population, land, yield and other data causes (`analysis/comparison_2025/`, which stays the reference for the data effect) and per-input requirements.
