# V23 report: the 2011 cells and the populations by the original workbook (claims A001, A002, A004, A005, A006, A021, A022)

## Verdict

Every target holds. The original `model/model.xls`, with each release's cells and the Australia inputs written into it and recalculated by LibreOffice, gives the four 2011 capacities. They match the results CSVs to the whole person. The two populations round to the claimed 22.3 and 27.6 million. Both sit slightly below the ABS figures in `data/sa2/population_erp.csv` (-0.06% for 2011 and -0.02% for 2025; see B). The two ratios hold.

## Tolerance and can-fail checks (set before comparing)

- Capacities: within 0.1% of the claim (the brief's tolerance, which is tighter than the shared 0.5%). Against the CSV: within 0.1%, and expected to match to the whole person.
- Populations: they must round to the claimed figure (one decimal, in millions). The CSV population must match exactly.
- Ratios: they must round to the claimed two decimals. `capacity_per_person` must match to its 4 decimals.
- **Deliberate wrong value fed to my comparator:** `cells2011.py wrong` multiplies my 2011-fixed short result by 1.002. It reported `DOES NOT HOLD` (33.374 M against 33.3 M, +0.224%). `compare_c.py wrong` then reported `DIFF` against the CSV (-0.1996%) and a `capacity_per_person` mismatch (1.4948 against 1.4919). The other rows still held.
- **Deliberate wrong cell value (part B can-fail):** in 2011-fixed short I changed Settings!B10 (meat-and-egg share) from 0.13 to 0.14. B76 became 32.795 M against the claimed 33.3 M (-1.52%), which is `DOES NOT HOLD`, and the ratio fell to 1.47. So the route responds to a single cell.

## The route

I reused the V15 workbook route (`v15/orig/model.xlsx`, converted from `model/model.xls`, whose sha256 f14140154e55... equals each release's `source.sha256`; `v15/lo_profile`, which always recalculates on load). I copied `route.py` into my own `code/` folder and repointed it, so my work files are separate. The steps:

1. Write the release layer: every cell where the release's `model.json` differs from the 2011 release's `model.json`. For 2011-fixed this is 10 cells and for 2011-improved 885 cells. In both, the layer is exactly `source.cellOverrides`, with no cell in one and not the other.
2. Write zone 1's `yield` vector from `regions.json` into Yield!F at `yieldRows`.
3. Write Settings!B2:B25 in `INPUT_ORDER`: B2 set to `climateZone` (1), then the land, the preset and the population.
4. Recalculate with LibreOffice headless and read Settings!B76.
5. Scan every recalculated workbook for error cells. There were none.

## A. 2011 cells (Australia)

| Release / preset | Workbook B76 | Claim | Difference | Result |
|---|---|---|---|---|
| 2011-fixed short (A001) | 33,307,813.65 | 33.3 M | +0.023% | holds |
| 2011-fixed long | 15,350,146.07 | 15.35 M | +0.001% | holds |
| 2011-improved short (A021) | 41,690,135.47 | 41.69 M | +0.000% | holds |
| 2011-improved long (A022) | 13,059,979.45 | 13.06 M | -0.000% | holds |

(The 2011-fixed short gap of +0.023% only reflects the claim being rounded to 33.3. Unrounded, the value is 33.308 M.)

## B. Populations and ratios

**Source.** `pipeline/land/README.md` names `data/sa2/population_erp.csv`: "Estimated resident population by SA2, 2011 to 2025 (30 June), ABS Data API `ABS_ANNUAL_ERP_ASGS2021`, on 2021 boundaries". `qa/sources_register.csv` D31 records it as unverified, because the fetch script is not in the repository. Its national sums, over all 2,454 SA2 rows, are:

| | `regions.json` Australia | Claim | ERP 30 June (SA2 sum) | Difference | Result |
|---|---|---|---|---|---|
| 2011-fixed (A002) | 22,326,388 | 22.3 M | 22,340,024 (2011) | -13,636 (-0.061%) | holds (rounds to 22.3) |
| 2025-fixed (A004) | 27,608,200 | 27.6 M | 27,613,654 (2025) | -5,454 (-0.020%) | holds (rounds to 27.6) |

What the differences are:
- **2025:** the 2025 population is the ERP for SA2s that have land rows only. Four SA2s are left out: 108031161 (442 people) and the Other Territories SA2s 901011001, 901021002 and 901041004 (4,708 people). The SA2s with land total 27,608,504. The remaining 304 people are lost when the SA2s are allocated to the 2011 zones (`land_2011_method_zones.csv` zone 1 = 27,608,199.78). So 27.6 M is a derived ABS ERP 30 June 2025 figure, not the ABS national total.
- **2011:** the 2011 figure, 22,326,388, is the 2011 servlet's own input (`data/2011/default-inputs-*.csv`). It is not taken from this ERP file, and it is 13,636 below the file's 30 June 2011 total. The file is the 2021-boundary series, so I cannot say from the repository alone which earlier ABS estimate 22,326,388 was. The claim, 22.3 M, holds either way.
- **The error 6 note in the claims register for A002:** in 2011-fixed, the seven states sum to 22,326,388. So do the 52 NRM regions plus the Northern Territory (zone 60, 229,711). The national figure is therefore consistent with the regional populations after the correction. In the uncorrected 2011 release, the states summed to 20,686,860.
- In 2025-fixed, the 52 regions plus the NT (264,883) sum to 27,608,201, which is 1 above the national figure. That is a rounding effect.

**Ratios (short term, from my own capacities):**

| | Capacity (own) | Population | Ratio | Claim | Result |
|---|---|---|---|---|---|
| 2011 (A005) | 33,307,813.65 | 22,326,388 | 1.4919 | 1.49 | holds |
| 2025 (A006) | 41,503,536.97 (own run of 2025-fixed short through the same route; identical to V15) | 27,608,200 | 1.5033 | 1.50 | holds |

## C. Comparison with `results/` (opened only now)

I compared the zone 1 rows, both presets, of `results/2011-fixed.csv`, `2011-improved.csv` and `2025-fixed.csv`, including my own 2025-fixed long run (15,623,208.99):

- **capacity:** all six rows match my values to the whole person (largest gap 0.00000%).
- **population:** all six match exactly.
- **capacity_per_person:** all six match to 4 decimals.
- **over_capacity:** all six match (0 short, 1 long).
- **Settings columns** (resilience, meategg, redmeat, losses, recycling, organic, fuel, biofuel): all equal the `regions.json` presets I wrote.

**Differences: none** in any of the derivable columns.

## Other findings (not asked)

1. **The `land_km2` column is in millions of km2, not km2.** `web/scripts/results-lib.mjs` line 20 writes `land_km2: Math.round(out.totalLand / 1e6)`. `totalLand` is Settings!B54, which is already in km2 (7,687,574 for Australia in my recalculated workbook). So Australia reads `8` and 104 of the 120 rows in `2025-fixed.csv` read `0`. Either the label or the division is wrong. `results/README.md` lists the column without units. The releases are frozen, so this is a decision for Murray, not something to fix here.
2. **`recycling` differs between the methods in the short preset:** 2011-improved short has recycling 1, while 2011-fixed short has 0. This comes from the release's own `regions.json` presets, and the CSV agrees with them. I am noting it only because the short presets are not identical across the methods.
3. The 2025 population leaves out the Other Territories (Christmas Island, Cocos, Jervis Bay and Norfolk) and one SA2 without land (see B). This is by construction, but "ABS estimated resident population" in prose should be read as "of the mainland and Tasmania zones".

## Commands to rerun

```bash
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v23
cd $S
python3 -I code/cells2011.py          # parts A and B, the ratios and the cell can-fail test; writes work/results.json
python3 -I code/compare_c.py          # part C against results/<release>.csv
python3 -I code/cells2011.py wrong    # deliberate wrong value (+0.2%): must show DOES NOT HOLD; writes work/results_wrong.json
python3 -I code/compare_c.py wrong    # must show DIFF on 2011-fixed short
```

`code/route.py` is V15's route with its paths pointed at `v15/orig/model.xlsx` and `v15/lo_profile`. LibreOffice (`soffice`) and openpyxl are needed. Work files are in `$S/work/` and `$S/work/calc/`.

## Files read

- qa/briefs/_checker_rules_results_wave.md, qa/briefs/V23_2011_cells_workbook.md, qa/reports/V15_workbook_second_route.md
- V15 scratch code (route.py, cases.py, canfail.py, diff.py)
- web/public/data/{2011,2011-fixed,2011-improved,2025-fixed}/model.json and regions.json
- model/model.xls (through V15's converted copy; sha256 checked)
- README.md (top), pipeline/land/README.md, releases/README.md (grep), releases/2025-population/release.json (grep)
- pipeline/land/make_defaults_2025.py and pipeline/land/land_2011_method.py (population lines only)
- data/sa2/population_erp.csv, data/sa2/land_2011_method_by_sa2.csv, data/nrm2011/land_2011_method_zones.csv (zones 1 and 2), data/2011/default-inputs-short-term.csv (first rows)
- qa/sources_register.csv (D31, D47), qa/claims_register.csv (rows A001, A002, A004, A005, A006, A021, A022), ERRATA.md (error 6 lines)
- Part C only: results/2011-fixed.csv, results/2011-improved.csv, results/2025-fixed.csv, results/README.md, web/scripts/results-lib.mjs (the `land_km2` line), web/src/model/evaluator.js (the `totalLand` line)
