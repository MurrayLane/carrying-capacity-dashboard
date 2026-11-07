# B34 small fixes (X072, X073, X075)

## X072: audit tool dropped the lower end of "N to M"

Cause: the lint mask (`numbers_lint.mask_line`) reads "145 to 147" as a year range and blanks the first number, so register value "145 to 147" (B083) gave only 147.

Change in `qa/tools/manuscript_audit.py`: new regex `RANGE_TO` and function `range_ends(text)` take both ends of any "N to M" from the unmasked register value; `load_register` now builds `nums_v = parse_numbers(value, True) + range_ends(value)`. Statements are unchanged.

Rerun (`python3 -I qa/tools/manuscript_audit.py --write`):

| document | numbers | matched | orphans | matched, status not `independently verified` | matched, weak |
|---|---|---|---|---|---|
| papers/A_results/OUTLINE.md | 92 | 92 | 0 | 29 | 8 |
| papers/A_results/DISCUSSION_MEASURES.md | 103 | 103 | 0 | 59 | 13 |
| papers/B_methods/OUTLINE.md | 169 | 167 | 2 | 144 | 14 |
| papers/B_methods/SECTION7_DRAFT.md | 39 | 39 | 0 | 39 | 9 |
| **all four** | 403 | 401 | 2 | 271 | 44 |

Orphans: 2, the ABS identifiers 7503.0 and 4306.0 (OUTLINE lines 68 and 72). The 145 orphan is gone. Note: the rerun rewrote `manuscript_audit_2026-11-07.md/.csv`; I did not pass `--notes`, so any hand-made spot-check notes appended to the earlier .md are not in the regenerated file.

## X073: benchmark influence in the sensitivity README

Checked `monte_carlo_2025-{fixed,mirror,improved}_all_summary.csv`, column `influence_lbench`, 120 rows each:
- fixed: max 0.0, 0 rows above zero
- mirror: max 0.0, 0 rows above zero
- improved: max 0.012, 101 rows above zero

Reworded in `analysis/sensitivity_2025/README.md` (line 171): "(twelve vary in the corrected and published releases: the long-term benchmark, lbench, has no effect there, because the model has no Settings!BQ4:BQ7 cells and its influence is 0 in every zone; in the improved release the benchmark carries about 1% of the variance, up to 0.012 in 101 of 120 zone rows)".

## X075: the 1,556/1,378 constant

1,556/1,378 = 1.129, the Alexander supplement's cropland-to-harvested adjustment. `half_index.py` does not use that constant. Searched `half_index.py` and the extracts for 1.129, 1,556, 1,378, "harvested", "cropland": no literal 1.129 or 1556/1378 in the script. Lines 6 and 55-57 compute it from FAOSTAT: `adj = cropland / harvested`, with cropland = world Cropland from the land-use extract (x1000) and harvested = summed "Area harvested" of the leaf crops; line 61 multiplies each crop's harvested area by `adj`. The result is 1.165 (README line 98: "adjustment 1.165 (paper 1.129)"). The only hits for 1556/1378 elsewhere are unrelated data values (US maize import 1556; Australian potato food 1378).

What the outline sentence should say: the SI gives the adjustment as 1,556/1,378 (1.129), but the rebuild does not use it; it derives the adjustment from FAOSTAT 2011 cropland over harvested area, which gives 1.165. E.g. "1.129 cropland-to-harvested adjustment (1,556/1,378); the rebuild derives it from FAOSTAT as 1.165". Outline not edited.
