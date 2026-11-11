# B80: Paper A section 4 scope on the corrected ordering; claim rows for the layer effects (decision 68)

## Files written
* `qa/claims_register.csv`: 12 rows added (A354 to A365), nothing else touched.
* `analysis/comparison_2025/README.md`: one paragraph added at the end, after the "Corrected-tier decomposition" check paragraph.
* `papers/A_results/SECTION_SCOPE.md`: the section 4 block and the section 4 row of the whole-paper table.
* This report.

## New claim rows
All Tier A, paper A, section 4, script `analysis/comparison_2025/decompose_corrected.mjs`, output `analysis/comparison_2025/capacity_by_cause_corrected.csv` (zone 1, Australia). Route 1 is that script's csv cell; route 2 is V29's independent script (`qa/reports/V29_decomposition_second_route.md`, section 10). The routes agree to the person. Status: independently verified (B76, V29; awaiting Murray's gate digest). Layer rows depend on A072; A073.

| Id | Layer | Short | Long |
|---|---|---|---|
| A354 | Land (2025-land) | -2,621,910 | -1,208,326 |
| A355 | Infrastructure land (2025-population) | 0 | 0 |
| A356 | Crop yields (2025-yields) | 115,575 | 219,940 |
| A357 | Livestock (2025-livestock) | 4,703,257 | 599,578 |
| A358 | Consumption without the organic share (2025-consumption) | 4,183,947 | 0 |
| A359 | Organic update | 0 | 172,682 |
| A360 | Resilience table | 0 | -7 |
| A361 | Long-term fuel | 0 | 90,858 |
| A362 | Red meat mix (2025-diet, layer 9) | 1,814,854 | 398,338 |

* A363, population status in 2011 (column `population_over_capacity_2011`): 0.670 short, 1.454 long.
* A364, population status in 2025 (column `population_over_capacity_2025`): 0.665 short, 1.767 long. Depends on A363.
* A365, long-term ordering: land > livestock > red meat mix > crop yields > organic > fuel; resilience -7. Depends on A354 to A362.

Choices to note:
* The README population table carries three ratios. I took the two that match the scope's named columns (2011 and 2025). The third, 2011 people over 2025 capacity (0.538 and 1.429), has no row; scope gap 2 says so.
* The short-term consumption and organic values are the builder's split. A358 and A359 notes give the strict-chain split (+3,802,283 and +381,664, same sum).
* A072 and A073 were not changed: their notes record no routes, only the published-chain description, so there was nothing to add. That note is now out of date (it says the decomposition is on the published chain); I left it as the brief said.

## Section 4 scope block, before and after
* Purpose: before, causes taken "one at a time", long term through crop yields and fuel; after, layers added in turn on the corrected releases, red meat mix included, long term led by land.
* Content list: before, point 4 "crop yields largest, then fuel; land small" and point 5 "causes do not add, interaction reported"; after, point 4 is the corrected ordering with resilience -7, point 5 is the exact-sum walk with no interaction term and order dependence, the red meat mix and infrastructure land are named, and point 2 records N-A4 taken.
* Evidence table: before, points 2 to 6 had no claim rows and cited the published-tier csv; after, they cite A363, A364, A354 to A362, A365 and the corrected csv. Point 6 (regions) still has no row.
* Tables and figures: before, Figure 3 and Table 3 from `capacity_by_cause.csv`; after, from `capacity_by_cause_corrected.csv`, with no script for Figure 3 (gap kept) and none that builds Table 3.
* Gaps: before, 1 the rerun on the corrected tier, 2 no claim rows; after, 1 no script for Figure 3 or Table 3, 2 no claim rows for the regional pattern or the third ratio. Count stays 2.
* Open decisions: N-A4 now marked taken, option (a); decision 68 named as the gate.
* Word budget: 500 unchanged; dependencies updated.
* Whole-paper table, section 4 row: decisions "none; N-A4" became "68; N-A4 taken (a)"; gaps stay 2. The Total row of that table (decision counts) was not edited, as the brief limits me to the section 4 row; it may need a recount by the owner.

## README line
"Organic split, strict chain (V29)": on the release chain as built, short-term consumption is +3,802,283 and organic +381,664; the sum is the same +4,183,947; no total, long-term value or ordering changes. Note: `decompose_corrected.mjs` replaces this README section when rerun, so the paragraph would be dropped unless the script is given the line.

## Checks
* Register parses: 698 rows, every row has 18 columns.
* Row count: 686 before, 698 after (+12). The old 686 rows are byte-identical (new file starts with the old content).
* Line endings: register stays CRLF (698 of 698 lines); scope and README stay LF.
* No em dashes in any of the four files.
* Scope diff touches only the section 4 block and the section 4 table row (827 lines before and after).
* Not run: any pipeline script (no git, no network, no subagents).

Wrong-value check: EXAMPLE ONLY, not a finding. If A365 were typed with crop yields ahead of livestock, or if A356 were given as 220,940 (the value V29's deliberate wrong run produced) with livestock 598,578, the csv cell (219,940 and 599,578) would disagree and V29's comparison would show 2 mismatches in the Australia long row.
