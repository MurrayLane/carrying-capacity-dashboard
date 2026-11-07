# V18 checker report: the cross-method table (methods paper, section 5)

## Tolerance and the can-fail test

I set the tolerance before comparing:
- Counts and names must match exactly.
- Capacities must agree within 0.5%, or to the printed rounding.
- Shares and ratios must agree within one unit of the last printed digit.

**Deliberate wrong value.** My script `derive.py` takes `--perturb NAME` and multiplies one input by 1.10. Every perturbation I ran made the script print `MISMATCH` on the figures that depend on that input, and on no others:

| Perturbed input | Figure | Derived | Stated |
|---|---|---|---|
| `half_au11` (Australia HALF 2011) | Australia HALF 2011 | 124.41 | 113.1 |
| | Gap to paper | +10.9% | +0.8% |
| `half_ha` (Australia ha a person) | Ha a person | 1.45 | 1.32 |
| | Footprint reading | 250.7 | 276 |
| `cassidy_world` | Lowest Cassidy gap | 25.0% | 22% |
| `cassidy_crop` | Cassidy on all cropland | 209.5 | 190 |
| `pop` (2025 population) | Failure probability a year | 9.1 to 9.3% | 5.8 to 6.1% |
| `grain` | Grain with feed grain | 140.7 / 139.4 | 128 / 127 |
| `meat` | Meat | 44.4 / 45.4 | 40 / 41 |
| `model_2025-fixed` | Model base | 45.65 | 41.5 |
| `model_2025-improved` | Model base | 59.01 | 53.6 |

The two model figures are printed but have no automatic test; I compared them by reading.

## A. Each row of the table from its method output

| Claim | Verdict | My value |
|---|---|---|
| HALF 2011: Australia within 0.8% (113.1 against 112.2) | holds | 113.1 against 112.20 = +0.80% |
| HALF 2011: world within 2.1% | holds | 34.4 against 35.13 = -2.08% |
| Australia 2021-23 HALF 81.0, 1.32 ha a person | holds | 81.0; 1.318 ha |
| Footprint reading about 276 million (B068) | holds, with a rounding note (below) | 363.519 / 1.318 = 275.8 |
| Cassidy people per hectare rebuilt 22 to 42% higher than the paper (B078) | holds | +21.8% to +41.7% |
| Cassidy scaled to all 31.65 Mha of cropland about 190 million (B084) | holds | 190.4 |
| Failure-probability view 41.5 (average year) to 18.9 (1 in 100) | holds | 41.50 and 18.92 |
| Failure probability at the 2025 population 5.8 to 6.1%, about 1 in 16 to 17 (B130) | holds | 5.84% to 6.10% |
| Commodity balance: meat 40 to 41, fish 12 to 17, grain with feed grain 127 to 128 (B153) | holds | see below |
| Methods without a balancing diet 134 to 343, commodity balance 12 to 41 (B156) | holds | 133.8 to 343.4; 12.1 to 41.3 |
| Model corrected 41.5 (36.3 to 45.8) (B159) | holds | 41.50 (36.33 to 45.76) |
| Model improved 53.6 (46.2 to 60.1) (B159) | holds | 53.64 (46.18 to 60.12) |

Working for the rows that need it:

- **Footprint reading (B068).** The land is 363.519 Mha, the FAOSTAT "Agricultural land" for Australia, 2021-23 mean, from `half_landuse.csv`. That equals cropland 31.650 plus permanent meadows and pastures 331.869.
  - **Is 1.32 the right denominator?** Yes in substance. It is the total HALF hectares a person, animal products 1.215 plus crops 0.103. Using only the animal-products column would be wrong.
  - **But the rounded figure does not give 276.** 363.5 / 1.32 = 275.4, which rounds to 275. The 276 comes only from the unrounded 1.318 (275.8). The table's 276 is right because `cross_method.py` divides by 1.318. Any sentence that writes the sum out as "363.5 / 1.32" should show 1.318.
- **Cassidy gaps (B078).** The paper's figures come from `published_values.csv` (cassidy_fidelity rows). Rebuilt over paper, produced / delivered:
  - World: 1.218 / 1.250
  - United States: 1.304 / 1.278
  - India: 1.354 / 1.339
  - China: 1.363 / 1.417
  - Brazil: 1.330 / 1.308
- **Cassidy on all cropland (B084).** 147.4 / 24.5 × 31.65 = 190.4; 6.0 × 31.65 = 189.9. On the second build's 5.77 a hectare it would be about 183. That figure is not in the table.
- **Failure probability (B130).** The 2025-fixed capacity points from `rerun.csv` R1 are 41.50, 37.03, 30.81, 26.32, 22.92 and 18.92 million. The population is 27.6082 million (`results/2025-fixed.csv`, nation, short). It falls between the 1-in-10 point (30.81) and the 1-in-20 point (26.32).
  - Linear in T: return period 17.13 years, 5.84% a year.
  - Linear in log T: return period 16.39 years, 6.10% a year.
- **Commodity balance (B153).** I rebuilt this from the FAOSTAT extracts:
  - Production, 2021-23 mean: grain 52.562 Mt (QCL "Cereals, primary"), meat 4.656 Mt (QCL "Meat, Total"), fish 0.295 Mt (FBS "Fish, Seafood").
  - Requirement per person: Foran and Poldy's base-case figures (2.713, 2.893 and 0.439 Mt; feed grain 7.6 Mt), divided by 25.1 million.
  - Actual use: FBS food use over the FBS population.

  | Item | On their requirement | On actual use |
  |---|---|---|
  | Meat | 40.40 | 41.27 |
  | Fish | 16.87 | 12.06 |
  | Grain with feed grain | 127.93 | 126.74 |
  | Grain, direct | 486.3 | n/a |
- **Range without a balancing diet (B156).** The values going in:
  - Henry and Godden: 133.8 to 243.2
  - Simpson crop and pasture: 343.4
  - HALF: 275.8
  - Cassidy: 147.4, and 190.4 on all cropland

  The commodity-balance range 12 to 41 covers the fish and meat readings only. Grain (127 to 128, direct 486) is deliberately outside it.
- **Model entry (B159).** The figures come from `results/ranges_2025-*.csv`, zone 1, short: base, p5 and p95.

## B. Can-fail and consistency

**My own derivations all move with their inputs** (see the table at the top).

**Under-test script: three rows do not move.** I ran a copy of `cross_method.py` on perturbed copies of its inputs in scratch (`pert/`):
- `half_index.csv` Australia 1.318 changed to 1.500: the HALF row moved 276 to 242, as it should.
- `cassidy.csv` Australia changed to 9.0 a hectare and 250 million: **the Cassidy row did not move.**
- `simpson_food.csv` 343.4 changed to 500 and 159.8 to 99: **the Simpson row did not move.**
- `foran_poldy_balance.csv` meat changed 40 to 60 and fish 17 to 30: **the Foran and Poldy row did not move.**

`cross_method.py` reads `simpson_food.csv` (`sf`), `cassidy.csv` (`cas`) and `foran_poldy_balance.csv` (`fp`), then never uses them. Those three rows, their low and high columns, and every "fidelity check" text are typed as string literals.

The unchanged `cross_method.py`, run with its outputs sent to scratch, reproduces the committed `cross_method.csv` and `model_entry.csv` byte for byte.

**Traceability.** Every figure in the table traces to a method output or a results file, except:
- **Simpson low 140 and the readings "140 to 160" and "307 to 343".** 140 and 307 are not in `simpson_food.csv`, which has 159.8, 385.7 and 343.4. They come from the second build (V04), quoted only in the README Simpson section. 160 and 343 are 159.8 and 343.4 typed by hand.
- **Cassidy "5.8" a hectare and "145" million (also the low column 145).** These are not in `cassidy.csv`, which has 6.0 and 147.4. They come from the V05 second build (5.77 × 25.1), quoted only in the README Cassidy section. "147" and "about 190" are hand-typed; they agree with `cassidy.csv` (190.4 derived).
- **Foran and Poldy "40 to 41, 12 to 17, 127 to 128", low 12, high 41.** These agree with `foran_poldy_balance.csv` but are hand-typed, not read.
- **All "fidelity check" texts.** Examples: "production within 1.3%", "within 5% to 8% between two builds", "pasture ... 1.2% low ... 36% high". These are typed. Where a method output carries the figure, it agrees: production gaps +1.2% / -1.1%; HALF United States -3.3%, Argentina -4.6%, India -7.4%; Henry and Godden 108.9 / 95.7 against 109 / 96.

## C. Differences in the files under test

Files: `cross_method.py`, `cross_method.csv`, `model_entry.csv`, and the README section "The model's own entry, and the methods side by side".

1. **Three rows are not read from their method outputs** (part B). A change to the Simpson, Cassidy or Foran and Poldy outputs would leave the table stale without any warning. This is the main finding.
2. **The README says the model's range contains Fearnside's 1-in-10 point. It does not.** The claim is "The model's range contains ... Fearnside's average-year and 1-in-10 points (41.5 and 30.8)".
   - The corrected Monte Carlo range is 36.3 to 45.8, so 30.8 is outside it.
   - The improved range, 46.2 to 60.1, contains none of these points.
   - The claim holds for 40, 41 and 41.5 on the corrected range only.
3. **"Its long term (15.6, improved 18.5) sits on Fearnside's 1-in-100 point (18.9)" is loose.**
   - Improved 18.5: 2% below 18.9, and 18.9 is inside its range of 15.9 to 19.4. This part holds.
   - Corrected 15.6: 17% below 18.9, and 18.9 is outside its range of 13.4 to 16.5. This part does not hold.
4. **The Fearnside row text differs between the CSV and the README.**
   - The CSV reads "41.5 (average year) to 18.9 (1 in 100)".
   - The README reads "41.5 (average year), 30.8 (1 in 10), 18.9 (1 in 100)".
   - `make_readme_tables.py` rebuilds that cell from `fearnside_failure_curve.csv` (lines 288-300). The numbers are consistent, but the README is not a copy of the CSV. The source comment also names `fearnside_failure_curve` without `.csv`.
5. **The Henry and Godden reading "134 to 211" excludes the 243.2 row** (plain 8.8 MJ requirement) of `henry_godden_summary.csv`, by its row filter. This is consistent with the claimed 134 to 343, but the exclusion is not stated in the table.
6. **README numbers checked and found to hold:**
   - Model entry, all cells: mirror 49.4 (43.4 to 54.3), 14.1 (11.8 to 16.0), 36.7 and 22.5; fixed 41.5 (36.3 to 45.8), 15.6 (13.4 to 16.5), 30.8 and 18.9; improved 53.6 (46.2 to 60.1), 18.5 (15.9 to 19.4), 39.9 and 24.7. Population 27.6.
   - "1,000 draws, 13 uncertain choices": `results/README.md` says so, and there are 13 influence columns.
   - 134 to 343, and "two and a half to eight times the model": 134 / 53.6 = 2.5 and 343 / 41.5 = 8.3.
   - 12 to 41.
   - 55.3 no avoidable waste (`rerun.csv` 2025-fixed R3 55.29) and 62.9 improved (62.92).
   - "About 12 million short term and 3 long term" (12.1 and 2.9).
   - The commodity balance and Fearnside readings as in part A.
   - The HALF fidelity text: within 0.8% and 2.1%; United States and Argentina within 5%; India within 8%.
7. **"The 9 to 100 million spread of published estimates" cannot be determined** from the inputs named. No source for it is in this section.

## Other findings

- The land figure in `half_landuse.csv` is identical in 2021, 2022 and 2023 (31,650 and 331,869 thousand ha), as is FBS fish production (295 kt). FAOSTAT appears to carry the 2021 value forward, so "2021-23 mean" is in effect 2021 for land and fish.
- `simpson_food.csv` uses the same 31.65 and 331.87 Mha, so the Simpson and HALF readings share one land base.

## Commands to rerun

From `/home/user/carrying-capacity-dashboard`, with `S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v18`:

```
python3 -I $S/derive.py                      # derivations + tolerance tests
python3 -I $S/derive.py --perturb meat       # also: half_au11 half_ha cassidy_world cassidy_crop pop grain model_2025-fixed model_2025-improved
python3 -I $S/cross_method_copy.py && diff $S/cross_method.csv analysis/method_tests_2025/cross_method.csv && diff $S/model_entry.csv analysis/method_tests_2025/model_entry.csv
python3 -I $S/pert/cm_pert.py                # under-test script on perturbed input copies in $S/pert/m
```

## Files read

- Inputs:
  - `qa/briefs/_checker_rules_results_wave.md` and `qa/briefs/V18_cross_method_table.md`
  - In `analysis/method_tests_2025/`: `henry_godden_summary.csv`, `simpson_food.csv`, `half_index.csv`, `half_landuse.csv`, `cassidy.csv`, `fearnside_failure_curve.csv`, `foran_poldy_balance.csv`, `fao_au_production_1997_2023.csv`, `fbs_au_world_2021_23.csv` and `published_values.csv`
  - README sections HALF, Cassidy, Fearnside and Foran and Poldy (for the paper figures)
  - `results/2025-fixed.csv`, `results/2025-improved.csv`, `results/2025-mirror.csv` (nation rows)
  - `results/ranges_2025-{fixed,improved,mirror}.csv`
  - `results/README.md` (one line)
  - `analysis/comparators_2025/rerun.csv`
- Under test (part C): `analysis/method_tests_2025/cross_method.py`, `cross_method.csv`, `model_entry.csv`, README lines 224-261, and `make_readme_tables.py` (grep only).
- Not read: `qa/reports/V02_*` to `V06_*`.

No repository file was changed. All writes are in `$S`.
