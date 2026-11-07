# V09 checker report: the regions under a bad year, and the named scenarios (results paper, section 8)

**Tolerance, set before comparing:** counts and names must match exactly. Capacities must agree within 0.5%. Shares and ratios must agree within one unit of the last printed digit (ratios ±0.01, percentages ±1 point, millions ±0.1). Over capacity means population > capacity. "The 53 regions" are the regions of `kind` = region plus the NT (zone 60).

**Deliberate wrong value:** I ran `check.mjs wrong`, which swaps the 2025 1-in-10 target ratio 1.12 for 1.32. My code printed `got 1.12 ... target 1.32 ... MISMATCH false,true,true,true`, so it does catch a wrong value. (The output is in `out_wrong.txt`.)

## A. The drought allowance: holds nationally; "one factor applied to every yield" holds only per state

- **What it scales:** every yield. The `resilience` input is Settings!B8. `Yield!C2` chooses a factor, and all 135 yield rows have the form `=C$2*E<r>*D<r>`, from wheat (row 4) through the livestock rows (95-105, 135-137) to timber (138). So crops, pasture products, livestock, fish and timber are all scaled.
- **Where the factor is stored:** in the `resilience` sheet of `model.json`. It has one row per location (Australia, NSW, Vic, Qld, SA, WA, Tas, NT) and one column per return period, 1 to 150. It is read with `INDEX/MATCH` on Settings!B8.
- **Which factor a zone gets:** `Yield!C2` picks the row from the zone's climate zone (Settings!B2). Zone 1 gets Australia, zones 2-14 NSW, 15-25 Vic, 26-39 Qld, 40-48 SA, 49-55 WA, 56-59 Tas and 60 NT. So it is one factor per state, not one national factor.
  - The Australian factor applies only to the national figure.
  - Each region takes its state's factor. For example, NSW at 1 in 10 is 0.5496 against 0.7424 for Australia.
  - Experiment: Border Rivers-Gwydir at 1 in 10 is 782,339. With all yields times the NSW factor I get 782,339. With all yields times the Australian factor I get 1,056,737.
- **The record:** the factors come from the mean of wheat, oats and barley yields from 1861, divided by a ten-year moving average. I confirmed this from `analysis/long_term_2025/README.md` and `analysis/resilience_2025/README.md`, not from the model itself.
- **2025-fixed Australian factors:**

  | Return period | 5 | 10 | 20 | 50 | 100 |
  |---|---|---|---|---|---|
  | Factor | 0.892291 | **0.742361** | 0.634262 | 0.552352 | 0.455821 |

  The 1-in-10 factor of 0.74 holds.
- **Experiment:** national 2025-fixed short term at resilience 10 is 30,810,607.2. All yields times 0.742361 at resilience 1 gives 30,810,607.2, a relative difference of exactly 0.
  - 2011-fixed: the same, with factor 0.741102 giving 24,684,502.4 both ways.
  - The long-term preset at T=100 also matches yields times 0.455821.
  - Verdict: **holds** for the national capacity.

## B. National and regional, corrected method: holds (all 32 numbers and all 6 extra figures)

Each cell below is national capacity over population / regions over capacity (of 53) / share of the population living in over-capacity regions / sum of the 53 regional capacities over national.

| Release | T = 1 | T = 10 | T = 20 | T = 100 |
|---|---|---|---|---|
| 2011-fixed | 1.49 / 23 / 82% / 0.63 | 1.11 / 24 / 84% / 0.56 | 0.89 / 27 / 87% / 0.53 | 0.68 / 33 / 92% / 0.47 |
| 2025-fixed | 1.50 / 16 / 81% / 0.63 | 1.12 / 21 / 85% / 0.55 | 0.95 / 24 / 89% / 0.51 | 0.69 / 28 / 91% / 0.46 |

Every cell matches its target.

The extra figures also hold:

| Figure | Mine | Stated |
|---|---|---|
| 2025, 1 in 10: sum of regional capacities | 16.896 M | 16.9 M |
| 2025 population | 27.61 M | 27.6 M |
| National capacity, 2011, 1 in 10 | 24.685 M | 24.7 M |
| National capacity, 2011, 1 in 20 | 19.956 M | 20.0 M |
| National capacity, 2025, 1 in 10 | 30.811 M | 30.8 M |
| National capacity, 2025, 1 in 20 | 26.324 M | 26.3 M |

## C. Regions on the edge: holds

- **2025:** five regions are under capacity in an average year and over it at 1 in 10: North East Vic, Burnett Mary, Mackay Whitsunday, Wet Tropics and Rangelands. These are the five named, and no region moves the other way.
- **2011:** one region, Corangamite.

## D. Named scenarios on 2025-improved: holds

- **Reference:** 53.644 M short term and 18.496 M long term. Regions over capacity: 15 short term and **36** long term.
- **Grain stores, by the ratio of `results/<release>.csv` national rows:**
  - `2025-store-1`: short 0.00%, long **+48.27%**.
  - `2025-store-2`: short 0.00%, long +64.21%.
  - The evaluator run on those release folders gives the same figures.
- **Field-crop yields 24% lower, by the evaluator with yields times 0.76:**
  - Rows 4-20 (the 17 cereals, oilseeds, pulses and sugar cane) plus row 94 (cotton): short **-0.26%**, long **-5.34%**. Both match.
  - This is also the set `scenarios/scenarios.json` names for `climate-crops-24`.
  - The 12% case (times 0.88) gives -0.11% and -0.35%.
  - My first guess at the set was different and gave a different answer (see below).

## E. Files under test

**Code and data files.** There are no differences in the numbers.
- `shocks_by_region.csv`: all 648 rows (2 releases × 54 zones × 6 return periods) match my evaluator capacities exactly after rounding. Populations are identical.
- `shocks_summary.csv`: the T = 5 and 50 rows also match my values. For T=5 I get 1.29 / 23 / 82% / 0.61 for 2011 and 1.34 / 20 / 84% / 0.58 for 2025. For T=50 I get 0.82 / 32 / 91% / 0.48 and 0.83 / 26 / 90% / 0.46.
- `scenarios_by_region.csv`: matches `results/scenarios.csv` and my recomputations.
- Two cosmetic points:
  - `shocks_summary.py` divides the over-capacity population by the sum of regional populations, not the national population. This makes no difference: 27,608,201 against 27,608,200 for 2025, and identical for 2011.
  - It prints `1.5` for the 2025 average-year ratio; the README shows `1.50`.

**README "Section 8" prose:**
- **Line 27 does not hold as worded:** "scales every yield ... by one factor from the 150-year record".
  - The model applies the state's factor to each region; only the nation gets the Australian factor.
  - The README's own Limits paragraph (line 71) says this correctly, so line 27 contradicts it.
  - The test it quotes holds, but for the national capacity only. Suggested wording: "by one factor per state (the Australian factor for the nation)".
- Both tables match their numbers.
- Bullet points that hold:
  - "50% to spare" and "about 12%" at 1 in 10 (2011 is 11%).
  - "About 80% ... 85% at 1-in-10 and 91% at 1-in-100, in both vintages". 2011 is 84% and 92%, so this holds within one point, but the exact figures are the 2025 ones.
  - "63% ... 55% (16.9 against 27.6)". This holds for 2025; 2011 at 1 in 10 is 56%.
  - The five names and Corangamite.
  - The reference figures 53.6 / 18.5 / 15 / 36.
  - "-26% at 1 in 10". I get -25.8% on 2025-fixed and -25.6% on 2025-improved, so it holds whichever release is meant.
  - "48% and nine regions out (36 to 27)". This holds, and no region newly tips.
  - "340 litres takes 19% off" (-18.75%).
  - "counts differ (15 and 16)".
- "The short term is bound by pasture-fed meat and dairy": I did not test this directly. A related run of mine supports it: the livestock rows (95-103, 135, 136) times 0.76 cut the improved short term by 23.3%, against 0.26% for field crops.

## Found outside the brief

- **Results that depend on which yields count as field crops.** My first broader set added buckwheat, quinoa, rye, spelt, linseed and sesame (rows 112-115, 122, 125) to rows 4-20 and 94. That gives -0.31% short and **-9.58% long**. Those six rows alone give -1.13% long. The long-term effect is not additive, so the -5.34% depends on exactly which rows are in the set.
  - The paper should name the rows (rows 4-20 and cotton).
- **Near-ties that could flip a count:**
  - 2025, 1 in 10: North Tasmania sits at capacity over population 1.000 (156,413 against 156,393, 20 people). It counts as not over.
  - 2011, 1 in 10: Burnett Mary sits at 1.004.
  - A tiny input change would move the 2025 count of 21 or the "five regions on the edge".

## Rerun

From `/home/user/carrying-capacity-dashboard`:
```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v09
node $S/check.mjs a      # A: factors, scaling experiment, per-state factor
node $S/check.mjs b      # B and C
node $S/check.mjs wrong  # deliberate wrong target -> MISMATCH
node $S/check.mjs d      # D: improved reference, store releases, broad field-crop set
node $S/check.mjs d2     # D: rows 4-20 + 94 at 0.76 and 0.88
node $S/check.mjs e      # E: row-by-row comparison with shocks_by_region.csv
node $S/check.mjs x      # extra: improved 1-in-10, livestock-only shock
```
The outputs are saved as `out_*.txt` in the same folder.

## Files read

- `qa/briefs/_checker_rules_results_wave.md` and `qa/briefs/V09_shocks_by_region.md`
- `web/src/model/evaluator.js`
- `analysis/sensitivity_2025/evaluate.mjs`
- `web/public/data/{2011-fixed,2025-fixed,2025-improved,2011-improved,2025-mirror,2011-corrected,2025-store-1,2025-store-2}/{model.json,regions.json}` (the resilience and Yield sheets)
- Grep hits in `analysis/long_term_2025/README.md`, `analysis/resilience_2025/README.md`, `analysis/method_tests_2025/README.md` and `HANDOFF.md`
- Part D: `results/scenarios.csv`, `results/2025-improved.csv`, `results/2025-store-{1,2}.csv`, the `results/README.md` lines, `scenarios/scenarios.json`, and the `yieldScale` lines of `web/scripts/make-scenarios.mjs`
- Part E: `analysis/paper_a/shocks_by_region.mjs`, `shocks_summary.py`, `shocks_by_region.csv`, `shocks_summary.csv`, `scenarios_by_region.csv`, and `analysis/paper_a/README.md` lines 25-71
