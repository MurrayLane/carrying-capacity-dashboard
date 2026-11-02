# Scale curve prototype (candidate for the results paper)

Question (Murray, 2026-11-02): is it worth including an SA2 scale, to show how smaller units degrade total capacity? `scale_curve.mjs` evaluates the model for units of shrinking size, **every unit on the same national yields and the same settings**, so that only the land mix and the population of the unit differ. Land: the 2011 land method on 2020-21 data per SA2 (`data/sa2/land_2011_method_by_sa2.csv`, sums to the national zone's land); population: 2025 ERP; units: Australia, states (9 codes including other territories), SA4, SA3, SA2. Release `2025-fixed` (corrected method), `scale_curve_2025-fixed.csv`.

| Level | Units | Short term: sum of capacities | Share of national | Units over capacity | Long term: sum | Share |
|---|---|---|---|---|---|---|
| Australia | 1 | 41.5 million | 100% | 0 | 15.6 million | 100% |
| State | 9 | 31.5 | 76% | 6 | 10.5 | 67% |
| SA4 | 89 | 22.3 | 54% | 70 | 7.6 | 49% |
| SA3 | 336 | 14.5 | 35% | 281 | 4.9 | 31% |
| SA2 | 2,450 | 11.5 | 28% | 2,194 | 3.8 | 24% |

* **The loss is large and the curve flattens.** Each unit has to feed its population on its own land mix, so a region of pasture alone, or a city with no hinterland, adds almost nothing, however much the national total has to spare. Most of the loss is by SA4; SA2 adds a further 7 points in the short term.
* **No SA2 yields are needed.** Holding the yield vector at the national value isolates the land-mix effect and avoids the noise of SA2 crop yields (unreliable below SA3). A version with regional yields is a different (and larger) task.
* **Limits.** Units are administrative (ABS) boundaries, so this is the scale effect plus the boundary effect together; separating them needs the landscape regions (B0a). Small units are dominated by cities with almost no land. The settings (diet, waste, resilience) are the national defaults in every unit, as in the 2015 paper. Not yet run on the 2011 data and zones.
