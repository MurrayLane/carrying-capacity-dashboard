# Results

Generated files; do not edit. They are the one source of the numbers on the dashboard's change pages and in the papers: a paper table is a script over these files, never typed.

* `<release>.csv`: every zone (60) and both presets (short, long) at the release's own defaults. Columns: `release, zone, name, kind, parent, preset, population` (the population the capacity is set against),
  `capacity` (people, rounded), `capacity_per_person` (capacity over population; below 1 is over capacity), `over_capacity` (1 if the population exceeds the capacity), `land_km2`, and the settings that drive the preset
  (`resilience, meategg, redmeat, losses, recycling, organic, fuel, biofuel`).
* `comparison_cells.csv`: the two-by-two of data vintage and method (`methods/README.md`), with the data effect, the method effects and their interaction.
* `releases.json`: each release's label, status, parent, method modules and the SHA-256 of the built `model.json` and `regions.json` it was evaluated from.

Regenerate after any change to a release, module or data file: `cd web && npm run results` (about a minute). The test suite fails if `2011-corrected.csv` or `2025-improved.csv` is stale.

Not in these files: the sensitivity and Monte Carlo ranges (`analysis/sensitivity_2025/`, run on `2025-organic`, not yet on the tip), the decomposition of the change into population, land and yield effects (`analysis/comparison_2025/`) and per-input requirements; these join `results/` when they are rerun on the cells above.
