# B111: the decomposition in reverse order and as an all-orderings average; land and livestock together (decision 101)

Brief: `qa/briefs/B111_decomposition_orders.md`. No git, no subagents, no network. The claims register and every release were not edited. `capacity_by_cause_corrected.csv` is byte-identical (sha256 50a02e7a...7ed2 before and after). Only `analysis/comparison_2025/` was touched, plus this report. `npm run results` and `build-data.mjs` were not run; the script's hash check found the built data current for all 12 releases.

## 1. The land-livestock overlap is real and is in the code

* `pipeline/yields/recent/livestock_zone.py` line 13 says the grazing land of the 2025 livestock rows is "the 2020-21 ABS grazing area of the zone (the land layer's pasture)". Line 33 reads `pasture` from `data/2025-land/default-inputs-short-term.csv`. Line 87 converts it to hectares, and line 100 sets `b['grazingHa'] = raw_pasture_ha[z]`.
* `pipeline/yields/livestock.py` line 38 makes the zone's grazing land `grazingHa + hayHa`. Line 56 divides milk by the dairy share of that land. Sheep and cattle meat divide by the same land plus their feed-grain and feedlot hectares.
* The 2011 rows divided each archive year's output by that year's grazing area (`archive_livestock_inputs.json`, 2006 to 2010).
* **One zone's arithmetic: Avon (zone 50).**
  * The land layer cuts pasture from 24,368 to 15,309 km2, a ratio of 1.592.
  * The livestock denominator falls from 2,537,931 ha (the mean of the archive years' grazing plus hay) to 1,594,996 ha (2025 pasture plus the 2010 hay), a ratio of 1.591.
  * The milk yield (sheet row 97) rises from 32.75 to 67.54 g/m2. That is 2.062 times, which is 1.591 (area) times 1.296 (output and dairy share).
  * Pasture times milk yield changes only 1.296 times: the area cancels.
  * In the forward walk, Avon's land layer takes -134,628 people in the short term and livestock returns +125,905, together -8,723. In the long term: -68,404 and +52,121, together -16,283.
* For Australia the two ratios are 1.097 (land layer pasture, 3,639,794 to 3,318,689 km2) and 1.104 (livestock denominator).
* Where feed grain is part of a yield's land (meat) or cropland binds, the cancelling is only partial.
* These numbers are written into the README by the script from the files themselves. The script fails if the cited lines move.

## 2. What was built

* **`decompose_corrected.mjs` is extended. Its default run is unchanged.**
  * `--order forward|reverse|<nine layers comma-separated>` prints one order for Australia and the states, checks the sum and writes nothing.
  * `--average [--jobs N]` evaluates **every** ordering: 9! = 362,880, exact, no sampling. It does so in all 60 zones (so all 53 regions too) and both presets.
  * It writes `capacity_by_cause_corrected_orders.csv` and a new README section, "Decomposition in every order (B111)".
* **How the orderings are evaluated.** Each layer is the set of inputs its release changes against the previous release in the chain. Any subset of layers is the `2011-fixed` start with those changes applied. The 512 subsets cover every state any ordering passes through, and give 30,720 distinct evaluations after duplicates are dropped. These run in worker threads (`decompose_orders_worker.mjs`), in about 11 minutes on 4 workers. The enumeration over orderings then takes seconds.
* **Three inputs are shared between layers. Each follows a stated rule:**
  * Non-agricultural land is the remainder of the total area, as `make_defaults_2025.py` builds it. The total is the 2025 total when land is in and the 2011 total otherwise. Checked: the rule reproduces every release's value.
  * The short-term organic share belongs to the organic layer, as in the B76 walk.
  * The animal yield rows belong to livestock. Without livestock they are 2025-yields' 6-figure rewrite of the 2011 rows.
* **csv columns:** layer, preset, forward, reverse, shapley_mean, shapley_sd, zone, then zone_name, game, orderings, shapley_min, shapley_max.
* **The csv's 2,400 rows cover two games:**
  * `nine_layers`: the 9 layers, plus `land_and_livestock` (the per-ordering sum of the two) and `total_change`.
  * `eight_layers_land_livestock_one`: land and livestock as one layer, over all 8! = 40,320 orderings. That layer is first in the forward order and last in the reverse order.
* **SD** is the population standard deviation of the layer's effect over all orderings. Forward and reverse are differences of rounded capacities, as in B76.

## 3. Results, Australia (people)

Short term (total +8,195,723):

| Layer | Forward | Reverse | Average (Shapley) | SD |
|---|---|---|---|---|
| Land | -2,621,910 | -3,546,205 | -3,064,101 | 356,696 |
| Infrastructure land | 0 | 0 | 0 | 0 |
| Crop yields | +115,575 | +220,269 | +162,372 | 33,145 |
| Livestock | +4,703,257 | +6,374,770 | +5,502,789 | 485,892 |
| Consumption | +4,183,947 | +4,090,572 | +4,156,557 | 267,133 |
| Organic, resilience, fuel | 0 | 0 | 0 | 0 |
| Red meat mix | +1,814,854 | +1,056,317 | +1,438,106 | 386,153 |
| Land and livestock together (sum) | +2,081,347 | +2,828,565 | +2,438,688 | 529,754 |
| Land and livestock as one layer (eight-layer) | +2,043,444 | +2,886,869 | +2,456,649 | 365,038 |

Long term (total +273,063):

| Layer | Forward | Reverse | Average (Shapley) | SD |
|---|---|---|---|---|
| Land | -1,208,326 | -1,334,901 | -1,248,192 | 100,008 |
| Infrastructure land | 0 | 0 | 0 | 0 |
| Crop yields | +219,940 | +253,434 | +257,755 | 103,189 |
| Livestock | +599,578 | +743,648 | +628,764 | 113,970 |
| Consumption | 0 | 0 | 0 | 0 |
| Organic update | +172,682 | +180,979 | +173,183 | 17,001 |
| Resilience table | -7 | -7 | -7 | 0 |
| Long-term liquid fuel | +90,858 | +114,983 | +124,764 | 99,739 |
| Red meat mix | +398,338 | +314,927 | +336,796 | 89,563 |
| Land and livestock together (sum) | -608,748 | -591,253 | -619,428 | 125,434 |
| Land and livestock as one layer (eight-layer) | -627,341 | -569,036 | -598,893 | 31,183 |

**Largest layer on the average.**

* **Short term: livestock**, +5.50 million (67% of the change). Read with land, the pair is +2.44 million (30%). The two diet layers, consumption and the red meat mix, account for +5.59 million (68%). With land and livestock as one layer the ranking is: consumption +4.15 million, land and livestock +2.46 million, red meat mix +1.43 million, crop yields +0.16 million.
* **Long term: land**, -1.25 million. With livestock it is -0.62 million (-0.60 million as one layer). With land and livestock as one layer, that pair is still the largest, at -0.60 million. It is followed by the red meat mix +0.36 million, crop yields +0.24, organic +0.18 and fuel +0.10 million.

**How much the order matters.**

* Nationally, livestock moves most between forward and reverse: +4.70 against +6.37 million short term.
* In the regions, the forward walk names a different largest layer from the average in 7 of 53 regions short term and 2 long term.
* The largest forward-reverse gap is land in Swan: -167,976 against -1,120,638 short term.
* Largest layer by the average, by region:
  * Short term: land in 26, livestock in 25.
  * Long term: crop yields in 19, land in 17, livestock in 16.
  * With land and livestock as one layer, that layer is largest in 42 regions short term and 31 long term.
* Infrastructure land moves capacity only in Northern and Yorke (zone 45), as in B76.

## 4. Checks

* **Subset rebuild.** Every forward prefix rebuilds the ten B76 walk states exactly: every region input, yield and workbook cell.
* **Forward matches B76.** The forward effects, start and end equal `capacity_by_cause_corrected.csv` in all 120 cells, to the person (0 mismatches).
* **Forward and reverse sums.** They add to 2025-fixed minus 2011-fixed in whole people in all 240 zone-preset-game groups (0 failures). `--order reverse` run alone reproduces the reverse column.
* **Shapley sums.** The Shapley values add to the unrounded total within 9.3e-10 people (nine layers) and 5.6e-9 (eight), against a tolerance of 1e-6. Rounded, they add to within 3 people (rounding).
* **Two routes to the mean.** The mean over the enumerated orderings equals the subset-formula Shapley value within 1.5e-5 people (tolerance 1e-3).
* **Independent csv read.** A Python read of the new csv against the old one (scratch `check_orders.py`) found 0 failures in 2,400 rows. It checks forward against the old csv, the forward and reverse sums, the sum of the Shapley means, the land-and-livestock sum, and min <= mean <= max.

## 5. Notes for the next jobs

* Not done, because the brief does not ask for it: R03a issue 2's split of livestock into an area part and an output part. That needs a `livestock_zone.py` rerun with the raw ABS files, which are not in the repository.
* Fixed: the default run's README writer used to delete everything after its own section. It now keeps any later `## ` section, so this section survives a default rerun.
* Pre-existing problem, not fixed: a default rerun still drops the hand-added "Organic split, strict chain (V29)" paragraph, because that paragraph sits inside the B76 section.
* Kitagawa (1955) and Das Gupta (1993) are named in the README as the method's lineage. They are not in the literature register (R03a issue 13).

## Files changed

* `analysis/comparison_2025/decompose_corrected.mjs`: extended.
  * `prepare()` split out of `compose()`.
  * `--order` and `--average` modes added, with the README writer for the new section.
  * Usage lines added.
  * The default README writer keeps later sections.
  * The default output is unchanged.
* `analysis/comparison_2025/decompose_orders_worker.mjs`: new.
* `analysis/comparison_2025/capacity_by_cause_corrected_orders.csv`: new, 2,400 rows.
* `analysis/comparison_2025/README.md`: section "Decomposition in every order (B111)" appended. Every earlier byte is unchanged.
* `qa/reports/B111_decomposition_orders.md`: this report.

## Claim rows that move (id; tier; before; after)

No register value moves: the forward walk is reproduced to the person.

**Tier A**

* A354 to A362 (A; forward-walk values): unchanged as values. Before: the statements are read as causes. After: each is "forward walk" beside a new all-orderings average. The register job should add Shapley rows for these. Short and long term:
  * land -3,064,101; -1,248,192
  * crop yields +162,372; +257,755
  * livestock +5,502,789; +628,764
  * consumption +4,156,557; 0
  * organic 0; +173,183
  * resilience 0; -7
  * fuel 0; +124,764
  * red meat mix +1,438,106; +336,796
  * land and livestock together +2,438,688; -619,428 (as one layer +2,456,649; -598,893)
* A357, A358, A362 (A): the driver sentence moves in wording only (decision 101). Before: "livestock, consumption and the red meat mix drove the rise". After: on the average, the diet layers account for +5.59 million and land with livestock for +2.44 million.
* A365 (A; land > livestock > red meat mix > crop yields > organic > fuel; resilience -7): stands. The same ranking holds on the reverse walk and on the average. With land and livestock as one layer it reads: land and livestock > red meat mix > crop yields > organic > fuel.

**Other tiers**

* A072, A073 (B; 8,195,723 and 273,063): unchanged. The totals are reproduced exactly.

Register rows touched: none.

## Wrong-value check

Wrong-value check: EXAMPLE, deliberately wrong. In a scratch copy of `capacity_by_cause_corrected_orders.csv`, Australia's short-term `livestock_only` forward value was raised by 1,000 people, from 4,703,257 to 4,704,257. The csv check then failed with 3 failures:
* Australia short, nine layers: forward sum.
* `livestock_only` forward against the old csv: 4,704,257 against 4,703,257.
* Land and livestock combined, forward.

On the real file it passes with 0 failures.
