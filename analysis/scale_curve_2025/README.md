# Scale curve (section of the results paper; Murray 2026-11-02: run it on 2011 and 2025 data and include it generally)

How capacity falls as the unit of self-sufficiency shrinks: the sum of capacities of units of a given size, each feeding itself from its own land, as a share of the national capacity. `web/scripts/make-scale-curve.mjs` writes `results/scale_curve.csv` for the six cells of the comparison grid (`npm run results`); `plot_scale_curve.py` draws the figure (`scale_curve.png` and `.svg`; `--log` spaces the levels by the logarithm of the number of units; `--local` draws the local-yield basis). Corrected method, share of national capacity:

| Level | Units | 2011 short | 2011 long | 2025 short | 2025 long | 2025 short, local yields | 2025 long, local yields |
|---|---|---|---|---|---|---|---|
| Australia | 1 | 100% | 100% | 100% | 100% | 100% | 100% |
| State | 7 | 77% | 59% | 75% | 70% | 75% | 70% |
| NRM region | 53 | 44% | 29% | 44% | 35% | 63% | 51% |
| SA4 | 89 | 60% | 44% | 58% | 49% | 80% | 64% |
| SA3 | 336 | 46% | 33% | 44% | 36% | 64% | 51% |
| SA2 | 2,450 | 40% | 26% | 37% | 30% | 54% | 42% |

The first four columns are the figure of the paper (**state yield basis**: every unit takes the yields and the irrigation and nature-reserve settings of its state's zone). The last two are the sensitivity (**local basis**: a unit takes the yields of its own NRM zone, or of the NRM zone holding most of its cropland for SA units).

## Reading it

* **The loss is large at every scale and monotone along the administrative levels.** On the 2025 data the states sum to 75% of the national short-term capacity, SA4 to 58%, SA3 to 44% and SA2 to 37%; the long term falls further (70%, 49%, 36%, 30%). The same shape holds in 2011 (77%, 60%, 46%, 40% short term), so the 2015 finding (national 40, states 28, regions 23 million) survives the corrections and extends to SA2.
* **The NRM regions (catchments) lose as much as the 336 SA3s with only 53 units** (44% against 44%, short term, 2025), and far more than the 89 SA4s (58%): the boundary matters as well as the number of units. NRM catchments cut cities from their hinterlands where SA3 and SA4 areas keep them together. This is the boundary effect the earlier plan wanted to separate from the scale effect (`SCOPE.md` B0); it holds on the one consistent yield basis.
* **Why an earlier version rose at SA4 (an artefact, now explained).** The first figure gave each SA unit the yields of its dominant NRM zone but used the state's own (state-wide average) yields at the state level, so the SA4 level, whose units are larger than most zones, got better yields than the states and rose from 75% to 80%. Tested on 2025-fixed (`yield_assignment_test.mjs`): with the parent state's yields at every level the curve is 75, 58, 44, 37%; with the national yield vector 76, 54, 35, 28%; with each unit's dominant-zone yields, even the states exceed the nation (109%). A whole state does not have the yields of its best zone, so that basis overstates large units and is a sensitivity only.
* **Yield differences within states are worth about 17 points at SA2 level (37% to 54%, short term).** That is the gap between the two bases and is a bound: the state basis ignores local yield differences (conservative) and the dominant-zone basis gives each SA unit the yields of one zone (generous for units that span several). The truth for SA2 lies between.
* **The sum of capacities is not guaranteed monotone.** The ASGS levels are nested (SA2 within SA3 within SA4 within the state), but the model's capacity is not additive: it depends on the unit's land mix, its population (infrastructure per person) and its yield vector, so only a consistent yield basis gives a clean curve.

## Method and limits

* Zone levels (Australia, state) use the release's own zones; the NRM level uses the NRM zones (own yields on the local basis, the parent state's on the state basis). SA4, SA3 and SA2 use land by the 2011 method on 2020-21 data (`data/sa2/land_2011_method_by_sa2.csv`, which sums to the national zone's land) and the ERP of the release's vintage year. The SA group has its own national reference ("Australia (SA land)"), equal to the national capacity for the 2025 cells; for the 2011 cells the 2020-21 land differs from the 2011 land (30.7 against 33.3 million short term), so the 2011 SA shares are against their own reference and are not exactly comparable with the zone levels (there is no 2011 land by SA2).
* Units are administrative (ABS) boundaries, so scale and boundary effects are together; cities are units with almost no land, which is the point, but they dominate the SA2 level (2,140 to 2,270 of 2,450 SA2s are over capacity in every cell). The other settings (diet, waste, resilience) are the national defaults in every unit, as in the 2015 paper.
* Rejected on the way: the national yield vector for every unit (understates the regional sum, 10.8 against 21.0 million on the 2011 zones) and the cropland-weighted mean of the zone yield vectors (inflates the yields of crops grown in a few zones; the national unit reached 77 million, not 33).
