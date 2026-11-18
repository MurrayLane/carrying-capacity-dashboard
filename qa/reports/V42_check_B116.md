# V42: blind check of B116 (the bases table, fidelity restated, the intake variant)

Brief: `qa/briefs/V42_check_B116.md`, under `qa/briefs/_checker_rules_results_wave.md`. Builder brief `qa/briefs/B116_bases_and_fidelity.md`; builder report `qa/reports/B116_bases_and_fidelity.md`. No git, no subagents, no network. The only repository file written is this report; my code and its outputs are in the scratch folder `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v42/`.

Order kept: my figures were derived from the method scripts and their inputs first. The one look at the builder's report before that was a grep for file names only, to learn which file holds "FAO's waste factor" (the brief says to use "the file the builder names"); it names `analysis/loss_factors_2025/compare.csv`, and the FAO factors themselves are in its neighbour `fao_region2_loss.csv` (Gustavsson et al. 2011, Annex 4, North America and Oceania), which I used.

## Tolerance (stated before comparing)

Counts and names exact. Capacities, index values, hectares and Mt within 0.5%. Shares, ratios and percentage gaps within one unit of the last printed digit. A verdict word must follow the stated rule (decision 109: within published rounding or 2% reproduced; within 10% partly; beyond 10% not reproduced) applied to the figures.

## Wrong-value check (an example)

My comparator (`comp.py`, 41 items) passes all items on the true figures (`mismatches 0`). Fed one deliberate wrong value of my own, HALF Australia with the supplement's world pasture set to 112.88 in place of my 118.88, it prints `FAIL HALF Aus b1 world pasture (WRONG VALUE FED) 118.88 112.88` and `mismatches 1`. So the check can fail.

## My figures

**HALF, rerun on the authors' printed inputs.** I executed the HALF section of `gap_attribution.py` in memory (no bulk file, no csv write) and, separately, reran the whole of `gap_attribution.py` with its write redirected to scratch against the FAOSTAT bulk file whose sha256 the script checks: the result is identical, row for row, to the filed `gap_attribution.csv`.

| HALF 2011 | Published | Current FAOSTAT revision (gap) | Supplement's world pasture, 3,364 Mha (gap) | All printed inputs a+b1-b5 (gap) |
|---|---|---|---|---|
| Australia | 112.20 | 113.125 (+0.82%) | 118.88 (+5.95%) | 121.59 (+8.37%) |
| World | 35.13 | 34.365 (-2.16%) | 35.76 (+1.79%) | 36.10 (+2.76%) |
| United States | 97.73 | 94.55 (-3.25%) | 99.13 (+1.43%) | 101.04 (+3.39%) |
| Argentina | 114.88 | 109.63 (-4.57%) | 115.36 (+0.42%) | 118.36 (+3.03%) |
| India | 15.76 | 14.63 (-7.17%) | 15.07 (-4.38%) | 15.11 (-4.12%) |
| New Zealand | 135.76 | 94.76 (-30.2%) | 99.61 (-26.6%) | 101.88 (-25.0%) |

Cause of Australia's 6 to 8%: current world pasture is 3,182.1 Mha, so the printed 3,364 raises pasture per tonne of ruminant product by 5.72%; Australia's 2011 diet is 1.983 of 2.093 ha a person in animal products (94.7%); bovine meat takes 67.0% of world pasture in this build. R03b's "about 121.5" is 121.59. Read as people (Australia's 2011 cropland plus pasture, 396.12 Mha, over the diet's hectares): 189.3 million at this test, 190.8 at the published figure; the supplement's pasture is worth -9.2 million, all printed inputs -13.2 million.

**Fidelity, other methods** (from the filed outputs of the method scripts, which I reproduced where they can be run without writing: `gap_attribution.py` above; the others read).
* Henry and Godden: 108.91 against 109 (-0.08%), 95.66 against 96 (-0.35%); total rows 205.96 against 206, 187.89 against 188. All within half a unit of the published whole numbers.
* Foran and Poldy: FAOSTAT 1997-98 grain 31.95 against 31.578 Mt (+1.18%), meat 3.471 against 3.514 Mt (-1.22%). This tests their production inputs, not their method output.
* Simpson 1991-92 (published crop for plant foods 0.312, feed 0.095, pasture 1.758, crop plus pasture 2.165). Build 1: 0.1068 (-65.8%), 0.0984 (+3.6%), 1.737 (-1.2%), 1.942 (-10.3%). Build 3 (thesis rates as printed): 0.074 (-76.3%), 0.1156 (+21.7%), 1.7176 (-2.3%), 1.907 (-11.9%). Build 2 (V04): 0.142 (-54.5%), 0.094 (-1.1%), 2.385 (+35.7%), 2.621 (+21.1%). Garden 0.0138 against 0.032 (-56.9%); wool, the thesis rule, 0.127 against 0.854 (-85.1%).
* Cassidy (2011 build against the paper's c. 2000), produced and delivered people a hectare: world 12.33 (+22.0%) and 7.49 (+24.9%); United States 20.97 (+30.2%) and 6.91 (+27.9%); India 8.82 (+35.6%) and 7.86 (+33.3%); China 18.42 (+36.5%) and 11.95 (+42.3%); Brazil 14.15 (+33.5%) and 6.83 (+31.3%). With each crop at its 1997 to 2003 yield: world 10.73 (+6.2%) and 6.54 (+9.0%; 6.39, +6.5%, with the paper's 4%/36% feed efficiency); US 19.28 (+19.7%) and 6.42 (+18.9%); India 7.34 (+13.0%) and 6.60 (+11.8%); China 15.95 (+18.2%) and 10.51 (+25.1%); Brazil 11.23 (+5.9%) and 5.47 (+5.2%). Shares: US feed 41 against 67, US other uses 32 against 6, US delivered 33 against 34, world delivered 61 against 59.
* The thesis rows: `results/2011-thesis.csv` zone 1 gives 40,439,187 and 9,431,487, equal to `baseline/thesis_totals_capacity.csv`; release `2011` gives 40,450,144 and 9,430,960.

**Gap-attribution residuals.** 22 residual cases (the HALF input-comparison row excluded). Within half a unit of the published figure's last digit: 4, all Henry and Godden (energy, protein and both total rows). Residual under 1% of the published figure, outside those 4: one, HALF Australia (0.92 points, 0.82%). Under 5%: also HALF world (2.2%), United States (3.3%), Argentina (4.6%), Simpson pasture (2.3%), Foran and Poldy grain and meat (1.2% each).

**Bases as implemented (read from the code).**
* Henry and Godden as run: no head count; people = output x Gifford's factor (0.1760 a 10^15 J, 15.56 MJ or 3,718 kcal a day; protein 0.2041 a 10^10 g, 134 g a day); production FAO food balance 2021-23 less feed, seed, non-food, losses and (for processed items) processing, exports kept; land: as is, or x 70/59.95 (28.3 Mha 1990-91 sown pasture + 31.65 Mha 2025 cropping) or x 70/45.7. Waste: no retail or household waste term; FAO's pre-retail "Losses" are deducted on the production side.
* Simpson: mass basis; FBS food over the FBS head count, mean 2021-23 (26.20 million); 1991-92 on ABS 4306.0; world yields FAOSTAT (build 1) or the thesis's 1990 yields (build 3); world pasture shared by protein (build 1); land FAOSTAT Australian cropland 31.65 and pasture 331.87 Mha (2021-23 mean). FBS food includes retail and household waste.
* HALF: mass basis; country FBS food over the FBS head count; world cropland from harvested area x cropland/harvested, world pasture, world land; 2011 and 2021-23.
* Cassidy: 2,700 kcal (985,500 a year), no head count; land = harvested area of 21 crops (24.5 Mha 2021-23); uses split over food, feed, processing and other (seed and losses outside the split).
* Foran and Poldy: tonnes; their 2050 requirement over their 2050 populations; actual-use reading divides 2021-23 FBS food by the mean head count of 2021 and 2022 only (26.08 million), although the 2023 figure is in the file (three-year mean 26.20; effect 0.48%).

**Intake variant (FAO's factor, my own script `intake.py`).** Food energy with no FAO group (sugar, alcohol, stimulants, spices, miscellaneous): 19.7% of supply. Supply reading, then intake reading on distribution-and-retail x consumption, then on consumption alone:

| Method | Supply | FAO, both steps | FAO, consumption only | |gap| to 41.5 |
|---|---|---|---|---|
| Energy balance, energy | 145.2 | 169.7 | 166.3 | widens |
| Energy balance, protein | 148.8 | 182.2 | 176.5 | widens |
| Cassidy, this build delivered | 112.9 | 132.0 | 129.3 | widens |
| HALF, Australia 2021-23 | 275.8 | 324.9 (324.8 from 275.7) | 314.0 | widens |
| Simpson build 1, together / cropland-bound | 343.4 / 159.8 | 404.8 / 189.0 | 396.1 / 182.8 | widens |
| Foran and Poldy meat / fish / grain | 41.1 / 12.0 / 126.6 | 48.1 / 19.7 / 137.2 | 46.1 / 17.9 / 136.6 | widens / narrows / widens |

Feeding my script the waste with its sign reversed (`--wrong`) turns every rise into a fall, so the direction test is not built in.

## Comparison, item by item

| Item | Builder | Mine | Pass or fail |
|---|---|---|---|
| HALF Australia, current revision | 113.12 (+0.8%) | 113.125 (+0.82%) | pass |
| HALF Australia, supplement's pasture | 118.88 (+6.0%) | 118.88 (+5.95%) | pass |
| HALF Australia, all printed inputs | 121.59 (+8.4%) | 121.59 (+8.37%) | pass |
| HALF world, US, Argentina, India on printed inputs | 36.10, 101.04, 118.36, 15.11 | same | pass |
| HALF New Zealand | 94.80 (-30.2%), not run on printed inputs | 94.76 (-30.2%); printed inputs 101.88 (-25.0%) | pass (verdict unchanged) |
| Cause: pasture 3,182 against 3,364; +5.7%; animal products 95%; bovine 67% | as stated | 3,182.1; +5.72%; 94.7%; 67.0% | pass |
| People equivalents (396.1 Mha; 189.3 and 190.8; b1 -9.2; all printed -13.2) | as stated | 396.12; 189.26; 190.82; -9.16; -13.18 | pass |
| HALF verdicts (partly for world, Australia, US, Argentina, India; NZ not reproduced) | as stated | follows the rule | pass |
| Henry and Godden four rows, reproduced | 108.9, 95.7, 206.0, 187.9 | 108.91, 95.66, 205.96, 187.89 | pass |
| Simpson pasture, feed, plant, total, garden, wool (gaps and verdicts) | -2.3 partly; +21.6, -76.3, -11.9, -56.9, -85.1 not reproduced | -2.3; +21.7; -76.3; -11.9; -56.9; -85.1 | pass |
| Cassidy produced rows and world delivered (as run and 1997-2003) | as in the report | same | pass |
| Cassidy delivered rows for US, India, China, Brazil | absent from `fidelity.csv` | +27.9 to +42.3% as run; +5.2 to +25.1% on 1997-2003 yields | fail (incomplete: four published components missing; the top of R03b's "22 to 42%" is China delivered, which the table does not hold) |
| Cassidy "printed inputs" column | 1997-2003 yields labelled as the authors' printed inputs | these are current FAOSTAT yields for the paper's years, not printed inputs | fail on the label; the verdict for world and Brazil (partly) rests on it, as run they are not reproduced |
| Cassidy shares | US feed 41 against 67 not reproduced; US delivered 33 against 34, world 61 against 59 partly | same; but US other uses 32 against 6 is not tabulated | pass on the cells; see the wording item below |
| Foran and Poldy | grain +1.2%, meat -1.2%, reproduced | +1.18%, -1.22% | pass (cells); note it tests production inputs only |
| Thesis rows | 40,439,187 and 9,431,487 exact | same | pass |
| Within-rounding count | Henry and Godden only | 4 cases, all Henry and Godden | pass |
| Ill-conditioned rule, report and README Convention paragraph | under 1%: HALF Australia only; shares kept for Simpson (2.3%), Foran and Poldy (1.2%), HALF elsewhere | under 1%: HALF Australia only | pass on the text |
| Ill-conditioned rule, `bases_fidelity.py`, `gap_attribution_readable.csv` and the generated README Table S1 | threshold 5% (column "ill-conditioned (residual under 5% of the figure)"); Table S1 prints HALF world, US, Argentina, Simpson and Foran and Poldy as changes, not shares | the brief and the builder's own text say 1% | **fail**: the code and table contradict the report, the Convention paragraph and the brief; the report's "Simpson and Foran and Poldy still carry shares of hundreds of per cent" is false of the table it generated |
| Units in Table S1 | "points" for Simpson (ha a person) and Foran and Poldy (Mt) | ha and Mt | fail (label) |
| Bases: populations 26.20 and 26.08; none for Henry and Godden and Cassidy as run | as stated | 26.203; 26.079; none | pass |
| Bases: energies 15.6 MJ, 2,700 kcal (11.3 MJ), 3,525 kcal (14.8 MJ), 134 g | as stated | 15.56 MJ, 11.30 MJ, 14.75 MJ, 134.1 g | pass |
| Bases: Henry and Godden "15.6 MJ (3728 kcal)" | 3,728 kcal | 3,718 kcal (15.56 MJ unrounded) | pass within 0.5%; 3,728 is a double rounding |
| Bases: land and years per method | as in `bases.csv` | as read from the code | pass |
| Bases: Henry and Godden waste "no waste charged" | as stated | FAO pre-retail losses are deducted from production | pass with a note (the cell should say so) |
| Bases: model rows (8.0 MJ; 12% avoidable waste) | as stated | not on my route | not checked |
| Intake shares on FAO's factor (cereals 0.715, roots 0.651, oilseeds 0.950, fruit and vegetables 0.634, meat 0.854, fish 0.610, milk 0.846) | as stated | same | pass |
| Intake readings, FAO factor (energy, protein, Cassidy, HALF, Simpson build 1, Foran and Poldy) | 169.7, 182.3, 132.0, 324.3, 404.8 and 189.0, 48.1, 19.7, 137.2 | 169.7, 182.2, 132.0, 324.8, 404.8 and 189.0, 48.1, 19.7, 137.2 | pass (HALF 0.15% apart: item mapping) |
| No-factor share of food energy | 20% | 19.7% | pass |
| "widens" for every reading above the model; fish narrows; meat changes side | as stated | same, on both FAO bases | pass |
| Ranges 3.1 to 11.0 (FAO) and 3.3 to 13.0 (model) times | as stated | 10.94 and 12.95 at the top | pass within one unit; both tops are double-rounded (10.9 and 12.9 from the unrounded values) |
| Intake on the model's loss factors | 177.0, 205.8 and so on | spot check only (fish 0.670 matches "Meat white") | not checked in full |
| 55.3 and 62.9 with no avoidable waste | from `ladder.csv` | `ladder.csv` holds 55.3 and 62.9 | pass |

## Sentences proposed for the paper

* "HALF comes within 1% for Australia and about 2% for the world on current FAOSTAT revisions and within 3 to 8% on the inputs the authors printed": supported (0.82%, 2.16%; 2.76% and 8.37%).
* "Simpson's pasture comes within 2.3%; his plant-food cropland and wool are not reproduced": true but it leaves out that the crop-plus-pasture total (-11.9% on the thesis rates, -10.3% in build 1) and the feed cropland on the thesis rates (+21.7%) are not reproduced; the total is the figure a capacity reading uses. Add them.
* "Cassidy's calorie shares come within a few points except the United States feed share": the US other-use share (32 against 6) is also far off. Say "feed and other-use shares".
* "his people per hectare are reproduced within about 6% for the world and Brazil on the yields of his data years": under decision 109 that is "partly", not "reproduced", and the world delivered figure is 9.0% on the yields alone (6.5% only with the paper's feed efficiency added). Say "come within about 6 to 9%".
* "Readings that rest on a partly reproduced implementation (the footprint, HALF, people per hectare)": the footprint's crop components and total are "not reproduced" in the builder's own table; only its pasture is "partly". Say so.
* The intake paragraph says no more than the figures support, except the double-rounded tops (11.0 and 13.0 should read 10.9 and 12.9).

## Claim rows the builder says move, with my verdict

* B058 (A) and B249 (B), HALF reproduction: after-values (+0.8% and -2.2% current; +8.4% and +2.8% printed; partly) agree with mine. Agree. B058 also holds India "-7.4%", which is -7.17% unrounded (-7.2%); the builder does not list that cell.
* B260 (B), Simpson pasture 1.718, verdict partly under the 2% rule: agree.
* B278 to B284 (B), HALF Australia shares replaced by points and people: values agree with mine (112.74 -0.38 +0.6; 118.88 +5.76 -9.2; 113.15 +0.03 -0.1; 113.11 -0.01 0; 113.20 +0.08 -0.1; 115.88 +2.76 -4.5; 113.15 +0.03 -0.1). Agree.
* Missing from the list, if the generated table stands (5% rule): B285 to B292 (HALF world, United States, Argentina), B295 to B300 (Simpson) and B305 to B309 (Foran and Poldy) hold shares that Table S1 no longer prints. If instead the 1% rule of the brief is applied, the table and csv must be regenerated and these rows do not move. Either way one of the two outputs is wrong.

## What I would do differently, and whether it changes a number

* Intake: FAO's food balance "food" is at retail level, so the distribution-and-retail step partly overlaps what the balance already removes (the builder says so under Limits). I would report consumption-only as the lower bound beside it: energy 166.3, protein 176.5, Cassidy 129.3, HALF 314.0, Simpson 396.1, meat 46.1, fish 17.9, grain 136.6. Numbers move by 2 to 4%; the direction (widens, fish narrows, meat crosses) does not change.
* Fidelity: add the four missing Cassidy delivered rows; label the Cassidy "printed inputs" column "paper's data years" (it changes no number, but the world and Brazil verdicts rest on it); run HALF New Zealand on the printed inputs (101.88, -25.0%; verdict unchanged).
* Gap attribution: pick one threshold and make the code, csv, README table, Convention paragraph and report agree; replace "points" by the figure's unit.
* Foran and Poldy's script divides 2021-23 food by the 2021-22 head count; on the three-year count the per-person use falls 0.48% and the readings rise by the same (meat 41.1 to 41.3). The builder records this in `bases.csv`; it is a defect of `foran_poldy_balance.py`, not of B116.

## Register rows touched

None. `qa/claims_register.csv` was read, not edited.

## Rerun

From `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v42/`: `python3 -I half_check.py`; `python3 -I nz.py`; `python3 -I chk2.py`; `python3 -I intake.py` (add `--wrong` for the reversed-sign check); `python3 -I comp.py` (add `--wrong` for the wrong-value example). Full attribution rerun: `python3 -I ga_rerun.py '/tmp/claude-0/fao/q/Production_Crops_Livestock_E_All_Data_(Normalized).csv'` (writes only `gap_attribution_rerun.csv` in scratch; sorted diff against the filed csv is empty).

Files read: the two briefs and the shared rules; R03b issues 9 and 10; `half_index.py`, `gap_attribution.py` and csv, `simpson_food.py` and csv, `henry_godden.py` and summary, `foran_poldy_balance.py` and csv, `cassidy_people_per_hectare.py`, `cassidy.csv`, `cassidy_matched.csv`, `harmonised_comparison.py` (head) and csv, `published_values.csv`, `second_build_values.csv`, `model_entry.csv`, `ladder.csv`, the FAOSTAT extracts; `analysis/loss_factors_2025/compare.csv`, `fao_region2_loss.csv` and README; `results/2011-thesis.csv`, `results/2011.csv`, `baseline/thesis_totals_capacity.csv`; then (last) the builder's report, `bases.csv`, `fidelity.csv`, `intake_variant.csv`, `gap_attribution_readable.csv`, parts of `bases_fidelity.py` and the README sections it wrote, and `qa/claims_register.csv` (read only).
