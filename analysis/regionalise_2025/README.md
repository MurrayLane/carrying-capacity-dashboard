# An ideal localised split of Australia (Murray 2026-11-02)

Question: is there a division of Australia into regions that loses little capacity compared with the nation (the scale effect of `analysis/scale_curve_2025`), and what does it look like?

## Method (`regionalise.mjs`)

Start from the 2,450 SA2s (2020-21 land by the 2011 method, `data/sa2/land_2011_method_by_sa2.csv`) and their adjacency from the ABS ASGS Edition 3 boundaries (`sa2_adjacency.py` writes `data/sa2/adjacency.csv`: 6,729 neighbouring pairs, 13 separate land masses: the mainland with Tasmania apart and 11 islands). The objective is the **sum of the regions' capacities** on the national yield vector (so land mix alone decides; the model is linear in land, so the best possible split loses nothing). Constraints: every region is contiguous; its land is at most a cap (default 650,000 km2, about the largest NRM zone; never below the largest single SA2, 513,000 km2). Greedy agglomeration: merge regions below a minimum land (a tenth of the mean) into the neighbour with the largest capacity gain; then merge the adjacent pair with the largest gain until K regions remain; then move boundary SA2s between regions while the sum rises (contiguity kept). It is a heuristic, so each result is a **lower bound** on the true optimum.

A population floor was tried first and dropped: in the outback it forces regions beyond any area cap (the result was a 3.3 million km2 region).

## Results (2025-fixed, share of the national capacity; `summary.csv`)

| Regions | Land cap per region | Short term | Long term | Reference at the same count |
|---|---|---|---|---|
| 53 | 513,000 km2 (the largest SA2) | 58% | | NRM zones 33%; random groupings of SA2s 68 to 81% |
| 53 | **650,000 km2** | **76%** | 69% | |
| 53 | 1,300,000 km2 | 92% | | |
| 53 | none | 99.9% | | |
| 89 | 650,000 km2 | 63% | 64% | SA4 54%; random 56 to 69% |
| 336 | 650,000 km2 | 49.5% | | SA3 35%; random 34 to 44% |

* **The NRM zones leave a great deal on the table.** At the same number of regions and a land cap of the largest NRM zone, a better drawing keeps 76% against the NRM zones' 33% (short term). At 89 and 336 regions the gains over the ABS SA4s and SA3s are 9 and 14 points.
* **The cap is what binds.** The ideal rises from 58% to 76% to 92% to 100% as the allowed region grows from 0.5 to 0.65 to 1.3 million km2 to unlimited. Rangeland is so large that pairing it with the cropping districts at the edge needs regions of hundreds of thousands of square kilometres.
* **The shape** (`ideal_K53_cap650k.png`, `ideal_K53_cap1300k.png`; fill = cropping share of cropping plus pasture land): the optimiser draws long regions that run from the cropping belts into the arid interior. In the west the south-west cropping belt is paired with the Goldfields and Nullarbor country to its north and east; in South Australia and Victoria the Wimmera and Mallee districts take in the pastoral country behind them; the north, with almost no cropping, stays as large pastoral regions (nothing to pair with).
* **Against random groupings.** At the same number of regions the contiguous optimum is about what a random (non-geographic) grouping gives at 53 and 89 regions and better at 336: geography costs capacity, and the optimiser recovers about as much as a random grouping would have by luck while keeping regions contiguous.
* **Limits.** The sum of capacities ignores population: the optimum leaves cities as tiny regions of their own (11 to 13 regions are under the land floor, mostly islands and urban SA2s), which would not do for a dashboard; population-centred regions (`SCOPE.md` B0a: a centre with its productive hinterland) need a floor that the outback cannot meet within an area cap, so they cost capacity this analysis does not measure. National yields and the short- and long-term defaults throughout; heuristic optimiser (a lower bound); SA2 adjacency uses a 200 m buffer, so it joins SA2s across narrow water.
