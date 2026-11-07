# V15 report: the six headline capacities by a second route (the original workbook in LibreOffice)

## Verdict

All targets hold. The original `model/model.xls`, with each release's cell values and the preset inputs written into it and recalculated by LibreOffice, gives the same capacities as `results/<release>.csv`. The largest gap is 0.001% (Rangelands, which is a rounding effect on a small number). The calibration against the 2011 servlet matches to the cent.

## Tolerance and can-fail check (fixed before comparing)

- The brief's tolerance is 0.1% on each capacity. I also checked that each result, rounded to 3 decimals in millions, equals the figure stated in the brief.
- For calibration, results had to equal the servlet's two decimals exactly.
- To show the comparator can fail, I raised my 2025-fixed long result by 0.2% before comparing (`compare.py work wrong`). It reported `DOES NOT HOLD` (+0.200%; 15.654 M against the claimed 15.623 M), and every other row still held.

## The route

1. I copied `model/model.xls` (sha256 f14140154e55..., the same as `source.sha256`) to my scratch folder and converted it to .xlsx with `soffice --headless --convert-to xlsx`.
2. I opened it with openpyxl, keeping the formulas, and wrote three things:
   - **The release layer:** every cell where the release's `model.json` differs from the 2011 release's `model.json`.
   - **The yields:** the zone's `regions.json` `yield` vector, written to Yield!F at the rows in `yieldRows` (4 to 138).
   - **The inputs:** Settings!B2:B25 in `INPUT_ORDER`, with B2 set to `climateZone`, then the land, the preset and the population.
3. I recalculated with LibreOffice headless, using a private profile set to always recalculate on load (`OOXMLRecalcMode=0`).
4. I read Settings!B76 ("Population carrying capacity", `=B62`), which is the cell the evaluator returns as `capacity` (`s(75,1)`).

**Proof that LibreOffice recalculated.** The original file's cached B76 is 3,331,225.95, cached with biofuel at 1. After writing the short preset (biofuel 0.005), B76 read 40,450,143.64, the servlet's value. Settings!B26 (`=SUM(B3:B7)`) also read correctly.

**Function support.** I scanned every recalculated workbook for error cells (#NAME?, #VALUE!, Err:5xx and the like) and found none. LibreOffice evaluated every function the workbook and the overrides use, so the `formulas` fallback was not needed. It also could not have been installed, because the shared rules forbid network access.

## A. Calibration (unmodified workbook, 2011 default inputs, Australia)

Inputs came from `data/2011/default-inputs-{short,long}-term.csv`, zone 1. Only Settings!B2:B25 was written; the workbook's own LOOKUP yield table was left in place.

| Preset | Workbook route | `baseline/baseline_2011.csv` | Result |
|---|---|---|---|
| short | 40,450,143.64 | 40,450,143.64 | holds (exact) |
| long | 9,430,960.22 | 9,430,960.22 | holds (exact) |

I also wrote the 2011 `regions.json` inputs and yield vector for zone 1 into Yield!F, which is what the route does for 2025. The results were identical, and the 2011 `regions.json` inputs equal the CSV defaults.

## B. The six cases (Australia, zone 1)

| Release / preset | Workbook route | Claim (brief) | `results` CSV | Difference | Result |
|---|---|---|---|---|---|
| 2025-mirror short | 49,389,413.71 (49.389 M) | 49.389 | 49,389,414 | -0.00000% | holds |
| 2025-mirror long | 14,146,846.90 (14.147 M) | 14.147 | 14,146,847 | -0.00000% | holds |
| 2025-fixed short | 41,503,536.97 (41.504 M) | 41.504 | 41,503,537 | -0.00000% | holds |
| 2025-fixed long | 15,623,208.99 (15.623 M) | 15.623 | 15,623,209 | -0.00000% | holds |
| 2025-improved short | 53,643,731.36 (53.644 M) | 53.644 | 53,643,731 | +0.00000% | holds |
| 2025-improved long | 18,496,333.63 (18.496 M) | 18.496 | 18,496,334 | -0.00000% | holds |

Two more zones, 2025-fixed long term:

| Zone | Workbook route | `results/2025-fixed.csv` | Difference | Result |
|---|---|---|---|---|
| 2, NSW-ACT (the CSV's name for New South Wales) | 2,457,621.55 | 2,457,622 | -0.00002% | holds |
| 52, Rangelands (parent 49, WA) | 49,386.50 | 49,387 | -0.00100% | holds |

## C. Can-fail test on the workbook route (2025-fixed short, Australia)

- **Meat-and-egg share 0.12 changed to 0.13:** 40.254 M against the claimed 41.504 M (-3.01%). This is a mismatch, so the route moves.
- **Population raised by 10%:** 41.504 M, unchanged. Capacity in this workbook does not depend on the current population (Settings!B25 only feeds the "current as a share of capacity" outputs). That is expected, but it means population is not a useful input for a can-fail test. The meat-and-egg share is.

## D. Cells the release writes that the route did not write

The route wrote every cell of every release layer. For 2025-mirror, 2025-fixed and 2025-improved, the layer is exactly `source.cellOverrides`: 1,202, 1,212 and 2,087 cells written, across the Yield, resilience, Base, Settings and Recycle sheets. `cellOverrides` lists 8 more cells, resilience!C3:C10, whose values equal the original workbook's. Writing them changes nothing, so they need no write. Settings!B2:B25 and Yield!F4:F138 were written from `regions.json`.

I deliberately did not write some cells that every release's `model.json` (2011 included) differs on from `model.xls`. These are the JavaScript port's own structural edits, and keeping the original is the point of a second route:

- **27 LOOKUP formulas rewritten as INDEX/MATCH:** Diet!C1 and C3:C20, and resilience!B3:B10. I kept the original LOOKUP.
- **Settings!C52:** `0.00000000001` written as `1e-11`. The two are the same value.
- **The Yield!H1:BO138 per-zone yield table (8,220 cells), dropped in `model.json`:** I kept it. No formula outside Yield!F refers to it, and Yield!F4:F138 is overwritten with the release's yield vector.
- **Yield!F1:** blanked in `model.json`. I kept the original.

The calibration and all eight comparisons agree with these cells left in their original form. So the port's rewrites do not change the result in these cases.

## Other findings

- The comparison with the brief's millions (3 decimals) and the CSV integers is consistent: the CSV stores capacities rounded to whole people.
- The brief's zone 2 "New South Wales" is named `NSW-ACT` in the CSV and in `regions.json`.

## Commands to rerun (from the scratch folder)

```bash
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v15
mkdir -p $S/orig && cp /home/user/carrying-capacity-dashboard/model/model.xls $S/orig/
(cd $S/orig && soffice --headless --convert-to xlsx model.xls --outdir $S/orig)
# $S/lo_profile/user/registrymodifications.xcu sets OOXMLRecalcMode=0 (always recalculate)
cd $S
python3 -I code/diff.py orig/model.xlsx 2011 2025-mirror 2025-fixed 2025-improved   # cell diffs against the original
python3 -I code/calibrate.py          # part A
python3 -I code/cases.py              # part B, writes work/results.json
python3 -I code/compare.py work       # comparison against results/<release>.csv
python3 -I code/compare.py work wrong # deliberate wrong value: must show DOES NOT HOLD
python3 -I code/canfail.py            # part C
```

Code: `$S/code/route.py`, `diff.py`, `calibrate.py`, `cases.py`, `compare.py`, `canfail.py`. Work files are in `$S/work/` and `$S/work/calc/`.

## Files read

- qa/briefs/_checker_rules_results_wave.md, qa/briefs/V15_workbook_second_route.md
- web/src/model/evaluator.js (top: `INPUT_ORDER`, the cell map, the `capacity` cell)
- web/scripts/releases.mjs (the first 150 lines)
- releases/2025-fixed/release.json
- web/public/data/{2011,2025-mirror,2025-fixed,2025-improved}/model.json and regions.json
- model/model.xls
- baseline/README.md, baseline/baseline_2011.csv, baseline/baseline_2011.json (the Australia cases)
- data/2011/default-inputs-{short,long}-term.csv
- results/{2025-mirror,2025-fixed,2025-improved}.csv (opened last, rows for zones 1, 2 and 52 only)

I did not read qa/reports/V01_model_entry.md.
