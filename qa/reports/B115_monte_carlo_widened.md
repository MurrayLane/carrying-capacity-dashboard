# B115: the Monte Carlo widened, with total-order indices, and the rule separating definitions from settings (decision 108)

Builder report. Brief: `qa/briefs/B115_monte_carlo_widened.md`. Release: `2025-fixed` (the corrected 2025 release), Australia, both presets. No register row, frozen release or existing output file was edited.

## 1. The rule, as written in `analysis/sensitivity_2025/README.md`

**A definition is a choice that changes what the number means:** what is counted (exports or not), the unit of self-sufficiency, the time frame (the short-term or long-term bundle), the diet standard (observed, guideline or optimised) and the weather the capacity is for (an average year or the worst in N). Published methods differ on them; each is reported as a separate reading and never drawn.
**A setting is a choice of value within one meaning:** a loss factor, a yield window, a calibration, a measured share, a requirement. It is drawn over the range its sources give; where no source gives an end or a weight, it is the author's judgement and is said to be.

The README lists all 19 sampled choices under one heading (range, distribution, source, preset) and 23 unsampled ones with the reason for each. The unsampled ones include the definitions, the improved-line modules other than the loss factors, and the settings left out for a stated reason: the crop data window, the plausibility rules, the five crops' organic factors, the reserve and infrastructure, thin-zone yield error, the wool, milk and feedlot series, textiles and fibre, the workbook's processing constants, the climate trend, FAOSTAT pastures, pasture productivity and nutrient composition.

## 2. The choices added (the existing 13 kept as they were)

| Choice | Range and distribution | Source of the range |
|---|---|---|
| Avoidable waste (short term) | uniform 12% to 14% | `analysis/waste_2025/README.md`: the FIAL 2021 baseline over the FAO supply allows "roughly 12 to 14%" |
| Retail and consumer loss factors | uniform weight 0 to 1 between the thesis's US factors and `methods/loss-factors-australia` (474 Base cells) | Buzby 2010, Muth 2011; FIAL 2021 Table 5, Burnside bin audit 2022 |
| Land-use source | ABS holdings or the ABARES land-use raster, equal chances | the two sources (`build_variants.py`, `land_raster`); **equal chances are my judgement** |
| Meat calibration | uniform weight 0 to 1 between the ABS tables as published and the archive's 2010 level (cattle x1.086, sheep x1.155) | ABS 7215.0 against the archive. The archive is above ABS in every year 2006 to 2010, cattle by 4.6% to 8.6% and sheep by 12.4% to 16.9%; I recomputed this from the ABS files and `archive_livestock_inputs.json` |
| Energy requirement per person (short term) | food amount uniform 1.000 to 1.286 on the sedentary NHMRC diet: PAL 1.4 to 1.8 | NHMRC Nutrient Reference Values, dietary energy, Tables 3 and 4 ("sedentary ... to moderate activity"; read from the archive PDF). **The upper end, a moderately active population, is a judgement on which part of the NHMRC range applies** |
| Crop-yield trend window | uniform between the field-crop factor of 2022-25 (1.356) and of 2016-21 (1.289) | `data/abs-2022-25/group_trend.json` |

The long-term avoidable waste (0%), activity (high) and food amount belong to the time-frame definition, so they are not drawn.

## 3. The new range and indices

2,000 Latin hypercube draws of 19 choices (block A), and 42,000 runs in all for the indices. Australia, millions of people:

| | Short term | Long term |
|---|---|---|
| Existing (13 choices, 1,000 draws): 5th to 95th percentile | 36.3 to 45.8, factor 1.26 | 13.4 to 16.5, factor 1.23 |
| Existing: min to max | 34.6 to 47.7, factor 1.38 | 12.9 to 16.9, factor 1.31 |
| **Widened: 5th to 95th percentile** | **31.1 to 49.2, factor 1.58** | **13.3 to 18.8, factor 1.41** |
| **Widened: min to max** | **26.2 to 58.1, factor 2.22** | **12.4 to 19.9, factor 1.60** |
| Widened: median (release base) | 39.0 (41.5) | 15.8 (15.6) |

The first-order index uses Saltelli (2010) with f(B) centred; the total-order index uses Jansen (1999). The intervals are 95% bootstrap intervals over 1,000 resamples. Short term, first order and total order:
* land source: 32% and 33%
* energy requirement: 27% and 25%
* meat window: 24% and 23%
* loss factors: 6% and 6%
* red meat share: 4% and 5%
* meat calibration: 3% and 3%
* avoidable waste: 1% and 1%

Long term:
* land source: 58% and 56%
* resilience table: 20% and 20%
* meat window: 14% and 14%
* organic yield factor: 4% and 4%
* meat calibration: 1% and 1%

The first-order shares add to 97% (short term) and 96% (long term), and each total-order index is within two points of its first-order index, so interactions carry about 3% to 4% of the variance. The full table is in `analysis/sensitivity_2025/sobol_2025-fixed.csv`.

Readings that matter for the paper:
* **The widening comes from judged choices.** The three largest short-term drivers each rest on a judgement: the land source (equal chances), the energy requirement (the PAL 1.8 end) and the meat window (equal chances). With holdings land only, the short-term range is 29.8 to 43.1 (factor 1.45).
* **The base is not central.** Four new choices have the release at one end of their range, so the median falls below the base.
* **Against 2011.** The corrected 2011 short-term figure, 33.3, now lies inside the 2025 range (31.1 to 49.2); on the existing range it lay below the 5th percentile. Section 6's "the short-term increase since 2011 holds" therefore no longer holds on the widened range, and Paper A's robustness reading depends on which range it adopts.
* **Against the definitions.** The 5th to 95th factor (1.58) is still below every definitional row: guideline diets 2.14, drought allowance 2.19, exports 2.41 to 6.36, time frame 2.66, unit 2.67. It is above avoidable waste (1.33) and land available (1.09). The min to max factor (2.22) passes the guideline diets and the drought allowance.

## 4. Sentences for the paper

* **In place of "defensible" (abstract, section 6.9, 6.10, section 9):** "Across the settings varied here (19 choices of value within one definition, each drawn over the range its source gives, four with ends or weights that are the author's judgement), the model's corrected short-term capacity runs from 31.1 to 49.2 million (5th to 95th percentile, a factor of 1.58; 26.2 to 58.1 from lowest to highest draw, a factor of 2.22)."
* **In place of "only 1.26" (highlight 5):** "Across the settings varied here the same model moves by a factor of 1.58 (5th to 95th percentile); every definition moves it further."
* **Abstract s7:** "By definition alone the model spans 18.9 to 55.3 million; across the settings varied here it moves by a factor of 1.58 (5th to 95th percentile) to 2.22 (lowest to highest draw)."
* **Section 6.9, estimator and drivers:** "The draws are a Latin hypercube of 2,000 runs; first-order and total-order indices use the Saltelli (2010) and Jansen (1999) estimators over 42,000 runs. The choices act almost separately: interactions carry about 4% of the variance. Three choices carry four-fifths of the short-term variance: the source of the land areas (32%), the energy requirement per person (27%) and the window of herd and meat data (24%). Each rests on a judgement (equal chances between two land sources and between three windows, and a moderately active population at the top of the energy range)."
* **Section 6, the rule (first paragraph):** "A definition changes what the number means: what is counted, the unit of self-sufficiency, the time frame, the diet standard and the weather allowed for. A setting is a value within one meaning, such as a loss factor, a yield window or a calibration. Definitions are reported one at a time; settings are drawn together."
* **Section 6.9, against 2011 (if Murray adopts the widened range):** "On the widened range the corrected 2011 short-term figure (33.3 million) lies inside the 2025 range, so the short-term change since 2011 is within the uncertainty of the settings."

Whether the paper quotes the widened range in Table 4 and in the abstract, or keeps 36.3 to 45.8 and adds the widened range beside it, is Murray's decision. These sentences assume the widened range replaces the existing one.

## 5. Files changed

* `analysis/sensitivity_2025/monte_carlo.mjs`: options added, each off by default:
  * `MC_ZONES=national`
  * `MC_WIDE=1` (the six choices, with checks of their inputs)
  * the `sobol N [PART NPARTS]` mode

  **With none of them the output is byte-identical to the unmodified script.** I compared it with `cmp` on four runs: 30 plain draws on 2025-organic, 20 draws on 2025-fixed with `MC_LONG`, the one-at-a-time runs, and a fixed run over all 60 zones. The draw function was refactored without changing what it consumes from the generator.
* `analysis/sensitivity_2025/README.md`: new section at the end (the rule, the two lists, the run, the checks, the result); the earlier text is unchanged byte for byte.
* New files:
  * `analysis/sensitivity_2025/sobol_wide.py`
  * `analysis/sensitivity_2025/check_wide.py`
  * `analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv` (42,000 runs)
  * `analysis/sensitivity_2025/sobol_2025-fixed.csv`
  * `analysis/sensitivity_2025/monte_carlo_2025-fixed_wide.md`
  * `results/ranges_2025-fixed_wide.csv`
  * this report
* Not touched: `results/ranges_2025-fixed.csv` and every other ranges file, `design_choices.csv` (its Monte Carlo row is a later job), the papers, the claims register, and B112's files (`ranges_2025-fixed_herdcycle.csv`, drought bounds).

## 6. Claim rows that move (for a later register job; none edited)

Tier A:
* B112; A; 36.3 to 45.8; 31.1 to 49.2 (if the widened range replaces Table 4's corrected range)
* B159; A; 41.5 (36.3 to 45.8); 41.5 (31.1 to 49.2) (same condition)
* B187; A; 1.26 over 13 choices; 1.58 over 19 choices (5th to 95th), 2.22 (min to max)
* B188; A; "1.26 against 2.2 ... 6.4"; "1.58 (2.22 min to max) against 2.14 (diet), 2.2 ... 6.4"
* A027 and A028; A; 36.3 to 45.8 and 13.4 to 16.5; 31.1 to 49.2 and 13.3 to 18.8, only if Paper A adopts the widened range (it reads the same `ranges_2025-fixed.csv`)

Tier B and C:
* B113; B; 13.4 to 16.5; 13.3 to 18.8 (same condition as B112)
* B116; C; 13 choices, 1,000 draws; 19 choices, 2,000 draws (42,000 runs for the indices)
* B117; B; meat window 81% of short-term variance; 24% first order, 23% total order (the land source 32% and 33% is now largest)
* B120; B; meat window 36% of long-term variance; 14% first order, 14% total
* B157; B; "outside the corrected range (36.3 to 45.8)"; Fearnside's 30.8 is still outside, now just below 31.1
* B253; B; 12 of 13 vary; 18 of 19 vary

Do not move (their releases were not rerun): B110, B111, B114, B115 (mirror and improved).

**Register rows touched: none.**

## 7. Limits

* National only. Zone ranges were not drawn with the six new choices.
* The six new choices are drawn independently. The waste rate and the loss factors may be correlated in reality; that is not modelled.
* The land raster variant carries the 2025-organic land base, which I checked equal to 2025-fixed's land in infrastructure, reserve and total area.

## 8. Wrong-value check

`python3 analysis/sensitivity_2025/check_wide.py` recomputes the range from the draws file.
* The true figures pass (exit 0): `short:p5=31.1 short:p95=49.2 short:r595=1.58 short:rminmax=2.22 long:p5=13.3 long:p95=18.8`
* **Example of a deliberate wrong value:** the run below quotes the old figures against the widened draws and exits 1.

```
$ python3 analysis/sensitivity_2025/check_wide.py short:p5=36.3 short:r595=1.26
short:p5: quoted 36.3, the draws give 31.1
short:r595: quoted 1.26, the draws give 1.58
```
