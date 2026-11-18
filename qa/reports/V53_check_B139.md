# V53: blind check of B139 (line (c), the bridge from HALF to the model, Table 8 in three panels, the production window, the production comparison)

Brief: `qa/briefs/V53_check_B139.md`, under `qa/briefs/_checker_rules_results_wave.md`. No git, no subagents, no network. The only repository file written is this report. My scripts are in the session scratch folder `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v53/` (not part of the repository).

Order kept: I derived the line (c) factor and shares, the model runs, the five held-year window ratios and the milk comparison before opening anything of B139's. For the bridge I could not define the seven switches from the records alone (see item 2); I took the builder's switch definitions from the docstring of `bridge_half_to_model.py` and its `bridge_groups.csv`, then wrote my own machine and my own all-orderings average. Those rows are marked "builder's definition".

## Tolerance (set before comparing)

Counts and names exactly; capacities within 0.5%; shares, ratios and factors within one unit of the last printed digit; decomposition terms (million people) within 0.5% of the total change being divided (34.46 million, so 0.17 million).

## Wrong-value example (EXAMPLE only)

`python3 verify_c.py --wrong` feeds my own check the line (c1) share closed as 0.385 (line (b)'s value) in place of the builder's 0.147. Output: `c1 check vs claimed 0.147: MISMATCH (mine 0.1474, claimed 0.385)`. With the true value it prints `MATCH`.

## My figures

**1. Line (c).** Expected direction, written before computing: wider (every method rises toward or past an intake basis while the model stays at 41.5, so the share closed falls from 38.5%; R05b issue 6 and B116 Table S7 say the same).
* Factor. On the records the factor is the FAO supply (3,525 kcal = 14.749 MJ) times an eaten share, over 8.0 MJ. Two constructions are defensible: (i) the model's retail and consumer loss factors applied to the food balance mix, energy-weighted (B116 `intake_variant.csv`: 0.8202) gives **1.5123**; (ii) the same loss factors applied to the model's own diet (evaluator, Base columns H and J, energy-weighted, release `2025-fixed`) gives a gross-up of 1.2549, so 14.749 / (8.0 x 1.2549) = **1.469**. Construction (i) reproduces the builder's 1.512.
* Not every reading takes the factor. Scaling all 19 readings by 1.512 gives share closed to 41.5 13.2%, to the median 16.0% and SD of log centres 0.44; a uniform factor cannot move the median share or the SD from line (b). The builder's 20.0% and 0.48 arise because the commodity balance's grain reading keeps its embodied feed grain (303 kg a person) and so rises only x1.1008 (direct grain 112 kg a person: (112 + 303) / (112 / 1.512 + 303)). With that one exception, from the line (b) readings in `harmonised_comparison_lines.csv`: **share closed to 41.5 14.74%; to the median of centres 19.95%; SD of log centres 0.646 to 0.477; highest over lowest 4.12; per method: energy balance -21.8%, footprint 37.5%, HALF 46.2%, people per hectare -4.6%, commodity balance -18.9%.**
* Model on the FAO supply requirement (evaluator, food amount 1.5123, waste 0.12): **27.945 million**; share closed (as-run distances to 41.5, line distances to the line's model) **14.37% with 27.945, 14.26% with 27.9.**
* No avoidable waste: methods x1.8438 (grain x1.1409), model 55.285: **20.95%**; methods as line (b), model with food 1.8438 and waste 0 (**31.004 million**): **20.73%**.
* Sensitivity the builder half-flags: on 8.0 MJ with construction (ii) the c1 share is **16.4%**; on the evaluator's 7.376 MJ it is 11.7% (ii) or **10.1%** (i). The direction holds in every case; the level is 10 to 16%.

**2. The bridge (builder's definitions; my own machine).** Ends: the evaluator gives the model **41.5035 million** (results/2025-fixed.csv 41,503,537); HALF at Australian productivity from the records is (27.73 + 72.42 Mha) / 1.3184 ha = **75.97** (column (e) 76.0). My machine (people = land over land a person by eleven groups, from `bridge_groups.csv` and B114's `pairing_relaxed_inputs_2025-fixed.csv`) gives 75.966 and 41.505 at the ends; exact Shapley weights over 7! orders, the averages adding to the total change (-34.461). All-orderings averages: **diet -22.64, pasture-fed yield -12.96, cropland yield -6.41, land pool -6.34, non-food land -4.42, waste -17.90, requirement +36.21; requirement and waste as one switch +16.44** (G2: pool -6.17, diet -21.89, cropland yield -6.39, pasture yield -12.53, non-food -3.92). Forward and reverse agree with the csv to 0.01. G3 (k = 91.31) starts at 113.56 and its pool term is -43.22; G4 (k = 145.6) starts at 116.90. One detail matters: non-food pasture (wool) is 4,513.3 m2 at waste 0.12 and 4,594.5 at waste 0 in the evaluator; the builder ties it to the waste switch. With it held at 0.12 my non-food term is -4.38 and waste reverse -13.85 (still inside tolerance).
* **Protein-held variant**, my own LP (minimise 1/N with the model's pool rule, energy and protein at least the diet's, pasture-fed red meat and dairy between 0 and 1, the rest between 1 and the cap): **84.94 / 85.36 / 86.20** at caps 2 / 3 / 5. The LP keeps dairy at 1 and cuts pasture-fed red meat to 0.33; legumes go to the cap and cereals rise. If dairy is not held at or below its amount (treated like the other groups) the reading is 92.4, so the classing of dairy as "down only" is a choice that moves this figure.

**3. Panels and window.**
* Panel A factors against their sources: drought every yield 41.504 / 18.918 = 2.194; crops only 41.504 / 40.450 = 1.026 (`drought_bounds_paper_B.csv`); waste 1.33 and 1.17; land 1.09; unit 2.67; guideline diets 2.14 (`design_choices.csv`); diet A 85.457 / 53.644 = **1.593**, diet B 3.767, diet C 7.872 (`nutrition_lp_2025/variants.csv`, rows fixcap3, famcap3, free with micronutrients); PAL 47.998 / 26.929 = 1.782, improved 61.767 / 35.153 = 1.757, drawn window 41.504 / 32.664 = 1.271 (`pal_one_at_a_time_2025.csv`); pasture output 49.467 / 33.431 = 1.480; bundles 1.29 and 2.66; Monte Carlo 1.58 and 1.58. Order of single choices low to high: 1.03, 1.09, 1.17, 1.27, 1.33, 1.48, 1.59 or 1.60, 1.76, 1.78, 2.14, 2.19, 2.67, 3.77.
* Panel B: 100.0 / 41.5 = 2.41; 183.9 and 263.9 give 4.43 and 6.36; the rebuild (`comparators_2025/proportional_count.csv`) 68.0 to 70.1 gives 1.64 to 1.69, 101.2 to 103.6 gives 2.44 to 2.50, mass 45.9 and 53.9 give 1.11 and 1.30; footprint output over consumption (`harmonised_robustness_footprint.csv`) 2.47, 4.29, 2.06, 3.23, 4.47, 2.97.
* Panel C against `qa/literature_register.csv`: L002 82, 60, 30 (2.00; 1.37); L006 "50 plus" against 30 to 35 (1.43 to 1.67); L015 402 to 807 (2.01); L040 2.04 to 6.08 (2.98); L016 10.1 and 6 (1.68), "up to 70%" (1.7); L017 112.20 and 35.13 (3.19); L023 5.96 and 1.8 (3.31); L244 9.0 and 14.0 (1.56); L035 holds 70 Mha only, the 40.5 is not in the register (1.73 unverified, as the builder flags). Eleven rows.
* Window, five held years (2011, 2020 to 2023; `fao_qcl_countries.csv` and `_2020.csv`): crop production by group cereals +5.19, pulses +15.96, sugar +4.16, vegetables +7.12, fruit +7.92, roots +10.72, tree nuts +23.06% (with oilcrops +23.1 the median of eight is **9.3%**); livestock meat total +2.94, beef -2.36, milk -1.99, eggs +3.69% (median of six with sheep +9.1 and poultry +7.0: **3.3%**). Yield: cereals **+8.39%** as the mean of yearly yields, **+8.95%** as the ratio of mean production to mean area (the builder's convention; median of eight groups 4.2% on it). Evaluator with crop rows / 1.0418 and sheep, milk, cattle meat rows / 1.0909, 0.9801, 0.9764: **41.352** (crops only 41.444, livestock only 41.410). With the livestock median (3.3%) put on every pasture row instead it would be 40.24 (-3.0%).
* Production comparison (`production_comparison_2025.csv`, model inputs spot-checked: wheat 2022-23 41,199,485 t is in `data/abs-2022-25/cube_2022-23.json`; FAOSTAT 41,199,486 t in `fao_qcl_countries.csv`): 26 field-crop rows, largest difference **0.00018%**; 19 fruit and vegetable rows, median absolute difference **13.12%**, largest **59.17%** (almonds); milk **0.09% to 3.52%**. My own blind milk check (Dairy Australia series in `data/2025/livestock_national_series.csv` against FAOSTAT 2021-23): mean 2021-22 to 2023-24 is 8,352 ML, 8,603 kt at 1.03 kg a litre, against 8,661 kt (-0.7%); within the builder's band.

## Comparison table

| Item | Builder | Mine | Verdict |
|---|---|---|---|
| Line (c) factor | 1.512 (every reading) | 1.5123 on construction (i); 1.469 on (ii); grain reading x1.1008 | pass on (i); wording fails (not every reading) |
| c1 share to 41.5 | 14.7% | 14.74% | pass |
| c1 share to median | 20.0% | 19.95% | pass |
| c1 SD of log centres | 0.65 to 0.48 | 0.646 to 0.477 | pass |
| c1 per method (5) | -22, 38, 46, -5, -19% | -21.8, 37.5, 46.2, -4.6, -18.9% | pass |
| c2 model on supply | 27.9; 14.3% | 27.945; 14.37% (14.26% on the rounded 27.9) | pass (uses the rounded reference) |
| c3 / c4 | 21.0% / 20.7% | 20.95% / 20.73% | pass |
| Direction | wider | wider | pass |
| Bridge ends | 75.97; 41.5035 | 75.966; 41.5035 (evaluator) | pass |
| Bridge averages (7) | -22.65, -12.96, -6.41, -6.34, -4.42, -17.90, +36.21 | -22.64, -12.96, -6.41, -6.34, -4.42, -17.90, +36.21 | pass (builder's definitions) |
| Requirement and waste as one | +16.44 | +16.44 | pass (builder's definitions) |
| Protein-held | 85.4 (84.9, 86.2) | 85.36 (84.94, 86.20) | pass |
| Panel A drought, waste, land, unit, diets, PAL, pasture, bundles, MC | as csv | as above | pass |
| Panel A diet A | 1.60 | 1.593 (1.59) | pass at the edge; ratio of rounded figures, as B182's 7.88 (unrounded 7.872) |
| Panel B (13 rows) | as csv | as above | pass |
| Panel C (11 rows) | as csv | as register | pass; L035 row unverified, flagged by builder |
| Window crop production | 9.3% | 9.3% | pass |
| Window yield | 4.2% | 4.2% (ratio of means; 8.39% against 8.95% for cereals on the mean of yearly yields) | pass |
| Window livestock | 3.3% | 3.3% | pass |
| Rescaled model | 41.35 | 41.352 | pass |
| Field crops | 26 to 0.0002% | 26, 0.00018% | pass |
| Fruit and vegetables | median 13.1%, max 59.2% | 13.12%, 59.17% | pass |
| Milk | within 3.5% | 0.09 to 3.52% | pass |

## Claim rows the builder names

* **B276**: holds. 4% and 39% unchanged; line (c) 14.7% (c1), 14.3% (c2, on 27.9; 14.4% on 27.945), 21.0% and 20.7% reproduce. Ask that the row carry the 10 to 16% band (requirement basis 8.0 or 7.376 MJ; loss factors on the food balance mix or the model's diet), since the level depends on those two choices.
* **B277**: holds. c1 0.65 to 0.48 (26%), 6.2 to 4.1; c2 equals line (b).
* **B194**: holds (1.09, 1.17 to 1.33, 1.29 unchanged; 1.03 the crop-only bound).
* **B182**: holds as a value (7.88 on rounded figures, 7.87 unrounded, already noted in the register); new diet A 1.60 (1.59 unrounded) and B 3.77 hold.
* **B185, B186**: hold (2.41; 4.43 to 6.36), now Panel B.
* **B003**: holds in value (18.9 to 55.3); 40.4 on crops only reproduces.
* **B130**: unchanged; not recomputed here (the crop-only companion 40.4 reproduces).
* **B333**: holds as the builder restates it; the diet A entry is 1.59 unrounded.
* **B247**: holds in value; the cause clause must change, because the bridge gives the pool (the pairing-like step) about 18% of the net distance in G1 and 60% in G3.

## Overclaim in the proposed sentences (`README_round2_B139.md`)

1. Line (c), sentence 1: "every method reading is multiplied by 1.51" is not true of the grain-with-feed reading (x1.10), and it is that exception that gives 20% and 0.48. Suggested: "every reading is multiplied by 1.51, except the commodity balance's grain reading, whose embodied feed grain is kept (x1.10)". "Its own retail and consumer loss factors" should add "applied to the food balance mix". "Narrows the spread by 26%" is against as run; against line (b) (0.44) the spread widens, which the sentence should say beside it.
2. Line (c), the single "15%" hides a 10 to 16% band from the 8.0 against 7.376 MJ choice (the builder's flag) and the weighting of the loss factors; one clause would cover it.
3. Bridge: correct on the numbers, but it mixes games: 16.4, 21.9, 12.5, 6.4, 6.2 and 3.9 are G2 values and "36.2" and "17.9" are G1 values. Say so. The requirement in the bridge is 7.376 MJ while line (c) uses 8.0 MJ; the paper should not set the two side by side without that note.
4. Protein-held 85.4: holds, but it depends on dairy being allowed only to fall; letting dairy rise like the other groups gives 92.4. One clause ("pasture-fed red meat and dairy held at or below their amounts") would make it exact.
5. Window: "Against the mean of these years 2021 to 2023 is higher by 9% ... and 3% ..." uses a mean that contains 2021 to 2023 (three of the five years). Against the only held years outside the window (2011 and 2020) crops are 27% higher and the rescaled model is 40.73 (-1.9%). The sentence should give the outside-years figure too, and say that the capacity barely moves because beef and milk, which carry the binding pasture, were below the mean (the livestock median of 3.3% put on all pasture rows would give -3.0%). The six-group livestock median mixes "Meat, Total" with its own parts.
6. Data-claim sentence: true as far as it goes, but meat, the output on the binding land, was not compared (the ABS tables are not on disk). Add "the meat inputs could not be compared".

## What I would do differently

* Report line (c) with both loss-factor weightings and both requirement bases as a band, leading with the builder's c1.
* Put the outside-window comparison (2011 and 2020) first in the window sentence.
* The window fetch: a FAOSTAT QCL bulk file appears to exist in this environment outside the repository (`/tmp/claude-0/fao/`). I did not open or hash it (the rules confine reading to the repository). Murray or the coordinator could check its hash against `qa/fao_bulk_hashes.csv` before fetching again.

## Register rows touched

None.

## Rerun (from the scratch folder above)

`python3 verify_c.py` (and `--wrong`); `node loss2.mjs`; `node run.mjs 2025-fixed '{"food":1.512}'`; `python3 bridge.py`, `python3 bridge.py 91.3089`; `python3 lp.py`; `python3 window.py`; `node win.mjs 1.0418 0.97641 1.09088 0.98014`; `node nf.mjs`.

## Files read

`qa/briefs/V53_check_B139.md`, `_checker_rules_results_wave.md`, `B139_paper_B_third_line_bridge_panels.md`; `qa/reports/R05b_response_plan_B.md` (issues 6, 7, 10), `B116_bases_and_fidelity.md` (section 3); `analysis/method_tests_2025/harmonised_comparison_lines.csv`, `bases.csv`, `intake_variant.csv`, `bases_fidelity.py` (loss lines), `design_choices.csv`, `ladder.csv`, `fao_au_production_1997_2023.csv`, `fao_qcl_countries.csv`, `fao_qcl_countries_2020.csv`, `pal_one_at_a_time_2025.csv`, `harmonised_robustness_footprint.csv`; `analysis/loss_factors_2025/README.md`, `compare.csv`, `effect.csv`; `analysis/resilience_2025/drought_bounds_paper_B.csv`; `analysis/nutrition_lp_2025/README.md` (parts), `variants.csv`; `analysis/pasture_2025/pairing_relaxed.py` (docstring), `pairing_relaxed_inputs_2025-fixed.csv`, `pasture_output_one_at_a_time_2025-fixed.csv`; `analysis/comparators_2025/proportional_count.csv`; `data/2025/livestock_national_series.csv`; `data/abs-2022-25/cube_2022-23.json` (one value); `qa/literature_register.csv` (nine rows); `qa/claims_register.csv` (ten rows); `web/src/model/evaluator.js`, `web/public/data/2025-fixed/`, `results/2025-fixed.csv`. Opened last: `qa/reports/B139_paper_B_third_line_bridge_panels.md`, `README_round2_B139.md`, `harmonised_line_c.csv`, `harmonised_line_c_model_runs.csv`, `harmonised_line_c.py` (grain lines), `bridge_half_to_model.csv`, `bridge_groups.csv`, `bridge_half_to_model.py` (docstring and machine), `b139_model_runs.mjs`, `design_choices_panels.csv`, `production_window_10y.csv`, `production_window_10y.py` (docstring), `extract_fao_au_production_10y.py`, `analysis/comparison_2025/production_comparison_2025.csv`.

## Appendix: the ten-year production window (follow-up)

Same rules and tolerance as above. The bulk file `/tmp/claude-0/fao/Production_Crops_Livestock_E_All_Data_(Normalized).zip` was treated as untrusted data. I computed its sha256 myself: `c5835418c18f9322e7decbd6800f93a216eaae3cdfa31acb08f0518c0c6d6853`, equal to the pin in `qa/fao_bulk_hashes.csv`. I read the csv inside the zip with my own script, `ten.py` in my scratch folder, run as `python3 -I ten.py <zip path>`. I ran nothing from that folder. I derived everything below before opening the builder's ten-year rows, extract and appendix.

**Wrong-value example (EXAMPLE only).** `ten_wrong.py` checks the ten-year median of crop production. Given 0.093 (the five-year figure) as the claimed value it prints `CHECK MISMATCH 0.2082 0.093`. Given 0.208 it prints `MATCH`.

**My figures.** Australia, 2014 to 2023, all ten years present for every item; 2021 to 2023 against the ten-year mean:
* **Crop production:** cereals +24.8, pulses +35.9, sugar -4.5, oilcrops +60.4, roots +16.8, vegetables +9.1, fruit +11.6, tree nuts +40.6% (wheat +31.1, barley +14.7). Median of the eight groups: **+20.8%**.
* **Yield, as the ratio of mean production to mean area:** cereals +23.5, pulses +26.2, sugar +8.2, oilcrops +22.6, roots +2.0, vegetables +1.1, fruit -1.5, tree nuts +6.4%. Median: **+7.3%**. Taking the mean of the yearly yields instead moves cereals to +24.1% but leaves the median at about 7.5%.
* **Livestock:** total meat -1.3, beef -10.9, sheep and goat meat +3.3, poultry +9.7, milk -4.8, eggs +0.6%. Median of the six: **-0.4%**.
* **Factors (window over 2021-23):** crops 0.9319, sheep meat 0.9684, cattle meat 1.1229, milk 1.0500.
* **Evaluator** (release `2025-fixed`, Australia, short term, with my own row scaling as in my first check): **44.134 million** both layers; crops only **41.400**; livestock only **44.251**.
* **Years outside 2021-23 (2011 and 2020):** the livestock median is **+8.7%**.

| Item | Builder | Mine | Verdict |
|---|---|---|---|
| Extract `fao_au_production_2014_2023.csv` | 270 rows, 27 item-element pairs | my 260 rows agree exactly; the extra 10 rows are pig meat, outside the six items | pass |
| Crop production, ten-year median | +20.8% | +20.8% | pass |
| Crop yield, ten-year median | +7.3% | +7.3% | pass |
| Livestock, ten-year median | -0.4% | -0.4% | pass |
| By item (cereals, wheat, pulses, oilcrops, sugar, beef, milk, sheep, poultry, eggs, total meat) | as appendix | identical to 0.1 point | pass |
| Factors crops, sheep, cattle, milk | 0.932, 0.968, 1.123, 1.050 | 0.9319, 0.9684, 1.1229, 1.0500 | pass |
| Rescaled model, both layers | 44.13 | 44.134 | pass |
| Crops only | 41.40 | 41.400 | pass |
| Livestock only | 44.25 | 44.251 | pass |
| Outside years, livestock median | +8.7% | +8.7% | pass |
| `production_window_10y.csv` ten-year rows | as above | match | pass |

**Amended README sentences (`README_round2_B139.md`).**
* **Line (c), sentences 1 and 2: pass.**
  * They now name the grain exception (x1.10).
  * They apply the loss factors to the food balance mix.
  * They say the spread is wider than on line (b).
  * They carry the 10 to 16% band.
* **Bridge: pass, with one rounding to fix.**
  * The two decompositions are now kept apart.
  * The 7.376 against 8.0 MJ note is present.
  * The dairy condition on 85.4 (and 92.4) is stated.
  * Rounding to fix: "lowers the reading by 22.7 million" for the diet in the seven-switch game should read 22.6 or 22.65. The csv prints -22.65 and I get -22.64. Mixing 12.96 with one-decimal figures is cosmetic.
* **Data claim: pass.** It now says the meat inputs could not be compared.
* **Window: fail on wording; the numbers pass.**
  * The sentence says that rescaling to the ten-year window "raises its short-term capacity from 41.5 to 44.1 million (+6%)" and that "the livestock window decides it". This treats FAOSTAT's 2021 to 2023 as the model's own meat window. It is not: the meat window is 2020-21 to 2024-25 (`bases.csv`).
  * The records put 2024-25 cattle meat at 3.00 Mt (`production_comparison_2025.csv`, beef row note), which is well above both FAOSTAT's 2021-23 mean (2.01 Mt) and the ten-year mean (2.26 Mt). So the model's own beef base is probably not below the ten-year mean, and the 1.123 cattle factor, and with it the +6%, probably overstates the effect.
  * The README states the proxy ("2021-23 stands for the model's own windows"), but the paper sentence drops it.
  * Suggested fix: add "taking FAOSTAT's 2021 to 2023 as a proxy for the model's own windows (meat 2020-21 to 2024-25, which includes a record 2024-25), so the +6% is an upper indication, not the model's own window effect". Alternatively, rescale against the model's own meat window once the ABS meat tables are on disk.
  * The rest of the window sentence passes:
    * "contains 2021 to 2023 itself"
    * the outside-years figures (27%; 40.7, -1.9%)
    * the 21% and 7% figures; the "0.4% lower"

**Builder's appendix (B139 report).** Every figure in it passes.

Register rows touched: none.
