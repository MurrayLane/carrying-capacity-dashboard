# R05a: a reasoned response plan to the second-round referee reports on Paper A (results)

Brief: `qa/briefs/R05a_response_plan_A.md`. Reports answered: `qa/reports/R04a_rereview_A_demographer.md` (the demographer, "R04a") and `qa/reports/R04b_rereview_A_land_systems.md` (the land-systems referee, "R04b"). Draft answered: `papers/A_results/draft/paper_A_draft1.md`, `supplementary.md`, `highlights.md` as assembled after B126a. First-round plan: `qa/reports/R03a_response_plan_A.md` ("R03a"). Decisions read: `qa/DECISIONS.md`, rows 100 to 132 and the standing rows the issues touch. No git, no subagents, no network; this file is the only file written. Where I give a figure of my own that no registered job has produced, it is marked **rough reading** and the file it comes from is named; the scratch scripts sit in the session scratch folder and are not part of the project.

## The outcome in plain words

Both referees again ask for major revision. Of their 18 merged major issues, 6 are new, 10 are first-round issues that the revision answered in part and the referee did not accept, and 2 are first-round issues the revision did not reach. Much of what they ask for is already in the records; four points need new computation, and one of those will very likely change a conclusion.

1. **The regional flip test is narrower than the national range, and on a rough reading the two "clean and robust" short-term flips do not survive the wider one.** The paper tests flips on 13 choices because the widened 19-choice draws stop at zone 45 (defect X140); decision 126 said this would be fixed "only if a referee asks". R04a asks. Scaling each region's 13-choice 5th percentile by its own state's widening (Tasmania 0.774 against 0.896 of base; Queensland 0.786 against 0.934) gives North Tasmania about 150,700 against 156,393 people and Mackay Whitsunday about 146,600 against 153,841 (rough reading, `monte_carlo_draws_2025-fixed_wide_states.csv` and `monte_carlo_draws_2025-fixed_all.csv`). The energy choice alone tips North Tasmania in about 30% of draws. South West Queensland's long-term flip is safe (7,109 people against a long-term capacity of 23,533). The fix and rerun should come first, because the abstract, section 3, section 10 and the fourth conclusion depend on it.
2. **The 2011 to 2025 rise survives a paired test far better than the unpaired comparison suggests.** On the widened draws 13% of 2025 draws fall below the 2011 figure of 33.3 million. When the energy requirement, the largest shared choice, is applied to 2011 as well, only 0.2% of draws show a fall, and the 2025-to-2011 ratio runs 1.09 to 1.61 (1.06 to 1.41 with holdings land in both years) (rough reading, `monte_carlo_draws_2025-fixed_wide.csv`, assuming capacity scales inversely with the food amount). Both referees ask for this paired test. It is worth running properly, because it is likely to strengthen the headline.
3. **The bad-year "improvement" between 2011 and 2025 comes from the change of weather table.** On the 2025 table, 2011 at 1 in 20 reads 1.06 people over capacity against 1.05 in 2025, not 1.12 against 1.05. The 1-in-10 factors are the same in both tables (0.741 and 0.742) (rough reading, `analysis/resilience_2025/tables.csv`). Both referees are right.
4. **Most of what R04b asks about the land system is answered by files that are already held, and the paper should cite them.** The short-term capacity is close to a meat production-to-consumption ratio: `analysis/method_tests_2025/README.md` gives 40 to 41 million from the meat balance against the model's 41.5. The cropland that pasture takes over is credited "square metre for square metre, at pasture's own output" (`analysis/pasture_2025/README.md`, B114). Feedlot grain hectares are in the cattle-meat denominator (`pipeline/yields/livestock.py`, line 63). National red meat output was not depressed in the 2005-06 to 2009-10 window (rough reading of the ABS 7215.0 tables the pipeline reads).
5. **The single 5.8% failure probability does not stand.** Across the 19-choice draws it runs from about 2.3% to 19% a year, 5th to 95th percentile (rough reading). Both referees ask for it to be dropped or ranged.

Where the referees are mistaken, the records say so plainly:
* The 2025 population is not rounded. It is the allocated SA2 sum, 304 people below the ABS total (X108).
* South West Queensland is not at risk.
* The windows are not on opposite phases of meat output: both sit below the decade between them.
* Feedlot output is not credited at a pasture-only yield.
* The "consumption" layer is almost wholly diet: fuel, biofuel and timber move it by 0.2% or less.
* Works citing the earlier papers were listed (`qa/reports/cited_by_openalex_2026-11-07.md`).

---

## What was computed since the first round, and where it is

| Job (check) | What it holds | Bears on |
|---|---|---|
| B110 (V36) | Every 2011 zone population on the ABS series (D31) and allocation; releases `2011-fixed-3`, `2011-improved-3`; ERRATA error 10; flips and shocks rerun | Issue 1 |
| B111 (V37) | All 362,880 orderings; land and livestock as one layer over 40,320 orderings (`capacity_by_cause_corrected_orders.csv`, game `eight_layers_land_livestock_one`); Avon arithmetic | Issues 3, 18 |
| B112 (V38) | Shocked ranges; herd-cycle Monte Carlo (39.4 to 43.8 million); crop-only drought bound (`drought_bounds.csv`) | Issues 2, 6, 7 |
| B114 (V40) | The pasture-crop rule relaxed three ways (82 to 108 million on the diet's energy); the land rule written out | Issues 10, 11, 12 |
| B115 (V41) | 19 choices, 2,000 draws, Sobol indices (`sobol_2025-fixed.csv`) | Issues 4, 5, 9 |
| B120 | `2011-fixed-3` frozen | Issue 1 |
| B123 (V44) | Shocked ranges on the widened draws; state-only widened draws; X140 found | Issues 4, 7 |
| B124, B126a | Text of sections 8 and 9; failure probability derived in S8 | Issues 7, 17 |
| B130 (V46) | Widened draws on the improved release (Paper B) | none for A |

So an issue the files already answer is marked **reword to cite the file** below. "Compute" is used only where no file holds the answer.

---

## Issue 1. The "data years" and the population date; the ERP vintage

**1. The issue.** The capacity inputs refer to roughly 2008 and 2021 to 2023, while the populations are at 30 June 2011 and 2025, and the ERP vintage is not stated (R04a 3.1; R04a question 1; R04a minors 4, 5, 6). R04a: "the paper compares production of roughly 2008 with production of roughly 2021 to 2023, but sets each against a population three to four years later." Round-two status: **(i) new** for the timing point; the vintage part was R03a issue 1, answered by B110 (both years on one ABS series) but still not stated in the paper.

**2. What the records show.**
* The windows are as R04a states (Table S11; `analysis/land_2011/README.md`; `livestock_zone.py`, docstring). R04a is right.
* The ERP series is one ABS flow for both years: `ABS_ANNUAL_ERP_ASGS2021`, 30 June 2011 to 2025 on 2021 SA2s (sources register D31; `data/sa2/population_erp.csv`). So the 2011 regional figures are the post-2021-census series on 2021 SA2s, which answers R04a's question 1 in substance. The 2025 value is the first release for that date; V30a checked it against the ABS Regional population 2024-25 release. The download script is not in the repository and the retrieval date is unknown (D31 notes), so the exact vintage label needs Murray.
* **Mistaken premise (minor 5).** 27,608,200 is not rounded to the hundred. It is the sum of the allocated SA2 ERP: the ABS total for the same 2,450 SA2s is 27,608,504, and 304 people are lost in the allocation (X108, D47).
* Minor 4 is right. The national 2011 row is the thesis's 22,326,388, while the regions sum to 22,336,514 (ERRATA error 10 kept the national row).
* D31 holds ERP for every year from 2011, so a window-midpoint population is available for 2025: 26.02 million at June 2022 and 26.66 million at June 2023, against 27.61 million at June 2025 (rough reading, sum of the SA2 columns less the 5,150 people outside model land). D31 holds nothing before 2011, so the 2011 window midpoint (about 2008) is not in the records.
* The number of straddling SA2s and the population they move (minor 6) are not recorded anywhere.

**3. Does it change a finding?**
* On 2022 and 2023 populations the 2025 margin reads 1.56 to 1.60 against 1.50 (rough reading). The 2011 margin would rise by a similar amount if 2008 growth was similar; the 2008 figure is needed to say so.
* The "about 1.5 in both years" sentence (A005, A328; abstract sentence 4) would read "about 1.5 to 1.6" on midpoint denominators. The change between the years is likely to stay small.
* Resetting the national row to 22,336,514 moves A328 from +23.7% to +23.6%, the 2011 short-term status from 0.670 to 0.671 and the long-term status from 1.454 to 1.455. A005 (1.49) and A011's 2011 share (69%) do not move. No capacity moves: national infrastructure land has no effect on the corrected tier (A373).

**4. The fair response.** Reword and a quick compute.
* Reword: a compact Table S11 in section 2 giving, for each input and year, the reference period, the source and the climate phase (issue 2), and naming the ERP flow and its vintage. Add one sentence defending the design: "As in Lane (2014) and Lane (2017), a data year pairs the most recent production data with the population to be fed at that date; we show the ratio on window-midpoint populations as a check."
* Compute (quick, about 0.3%): the national ratio on midpoint populations for both years, from D31 for 2025 and the ABS national ERP at June 2008 for 2011 (one figure, Murray or a job with network); the count of straddling SA2s and the population they move, from the D47 overlay.
* National row: two defensible options. (a) Reset it to the ABS 22,336,514, so national and regional figures share one base (recommended: both referees' readers will check the sum). (b) Keep the thesis row and say why. (a) changes Tier A rows A328, A005's note and the status rows, so it goes to Murray (CARD).

**5. Dependencies and conflicts.** It feeds issue 2: the same table carries the climate phase. The referees agree; R04b minor 9 asks only which row is used.

---

## Issue 2. The two windows sit on different climate phases

**1. The issue.** The 2011 inputs come from Millennium Drought years and the 2025 inputs from La Niña years, so the change may be weather rather than land (R04b 1; R04b question 4). R04b: "it may largely be a change in the weather." Round-two status: **(ii) answered and not accepted.** R03a issue 3 showed that full-cycle windows move the 2025 base by -0.1% to +0.9%, and the revision added the herd-cycle range (S7, S9). The 2011 window variants R03a proposed were not run, and the paper never states the climate phase.

**2. What the records show.**
* For crops, R04b is right. The 2011 crop yields are 2006-07 to 2009-10, and the season ending 2007 is the 4th-worst of 153 (ratio 0.567, Supplementary Section S4).
* For livestock, which is what binds, the premise does not hold on output. In the ABS 7215.0 tables that `livestock_zone.py` reads, cattle and calf meat averaged 2.13 Mt a year in 2005-06 to 2009-10 and 2.20 Mt in 2020-21 to 2024-25 (+3%). Sheep and lamb meat averaged 0.64 and 0.79 Mt (+24%). Both windows sit below the 2010-11 to 2019-20 cattle mean of 2.30 Mt: in a drought, destocking raises slaughter, and the loss comes in the rebuild years (rough reading, ABS 7215.0 monthly tables summed by financial year).
* Milk fell from 9,084 million litres in 2009-10 to a window mean of 8,446 (-7%), and wool from 343 to a mean of 309 Mkg (`data/2025/livestock_national_series.csv`).
* The beef herd was 0.993 and 1.04 of its 2009-10 size in 2020-21 and 2024-25 (`analysis/reliability_2025/README.md`).
* The regional "livestock gains" in Central West NSW, Lachlan, Namoi and the Border Rivers regions are mostly the grazing-area denominator. Pasture fell 11% to 25% in those zones (`data/2011` against `data/2025-land`), and regional class counts are the 2010 mix scaled by the state's herd change (`livestock_zone.py`), so regional seasons do not enter. On the all-orderings average, land and livestock together are about half of each of those regions' gains, for example 237,139 of 464,456 people in Central West NSW (`capacity_by_cause_corrected_orders.csv`).
* Matched windows on the 2025 side: the 20-year window 2005-06 to 2024-25, which contains the 2011 window years, moves the 2025 base by -0.1% (`analysis/sensitivity_2025/README.md`). The herd-cycle range, 39.4 to 43.8 million, lies wholly above 33.3 (S7).
* The 2011 window cannot be widened from the archive, which holds only 2006 to 2010 (`archive_livestock_inputs.json`).

**3. Does it change a finding?**
* Short term: on the records, no. The direction of A001 to A003 holds on every full-cycle window, and output changed little between the windows.
* Long term: the drought baseline depresses the 2011 crop yields, and the long term is crop-limited at 1 in 100 (S10). A normalised 2011 would therefore raise 2011 long-term capacity, so the fall in the share covered (69% to 57%, A011) would if anything be larger, not smaller.

**4. The fair response.** Rebut the strong form, reword, and a small compute.
* Rebut, in response-letter words: "The 2011 livestock window coincides with the Millennium Drought, but national red-meat output in that window was close to that of the 2025 window and below the decade between them, because drought raises turn-off. The livestock layer's rise is mostly the smaller recorded grazing area, which the land layer takes back, so we now report the two as one layer (issue 3). A 2025 window of 20 years that contains the 2011 years changes the 2025 capacity by -0.1%."
* Reword: state each window's climate phase in the section 2 table (issue 1); say that the crop baseline is a drought baseline and what that does to the long term.
* Compute (small, about 1 to 1.5% with a check): (a) the 2011 release on three-year subsets of the archive years (R03a's matched-length variant, not reached), giving a 2011 range from the window alone; (b) the national output comparison above as a registered table from the ABS files, which also serves issue 3.
* R04b's normalisation "by the cereal ratio of the seasons it covers" is not recommended for livestock: it would apply to meat the very cereal-for-pasture assumption R04b rejects in its issue 5.

**5. Dependencies and conflicts.** It depends on issue 3 (land and livestock as one layer) and feeds issue 5. **Internal tension in R04b**: its issue 1(b) proposes a cereal normalisation that its issue 5 argues against. The response letter should point out the tension without stressing it. R04a does not raise the climate phase.

---

## Issue 3. Land definition, the ABS frame, and the land-livestock identity

**1. The issue.** Part of the pasture fall is a change of ABS definition and collection frame, so the land row, and through the shared denominator the livestock row, mix statistics with land use. Both referees want the land and livestock layers reported as one, an estimate of the definitional part, and an external output check (R04a 3.2; R04b 2; R04a question 4; R04b questions 3 and 7). R04a: "drop 'livestock' from the abstract as a separate cause unless it survives that adjustment." R04b: "name the frame changes (EVAO threshold, frame, category changes) explicitly." Round-two status: **(ii) answered and not accepted.** B111 computed the combined layer and the text gives it (+2.4 million), but the abstract and highlight 2 still name livestock first, the definitional part is not estimated, and the frame change is not named.

**2. What the records show.**
* The combined layer exists both as the sum of the two rows (+2,438,688, A381) and as one layer over 40,320 orderings (+2,456,649, A382). With land and livestock as one layer the short-term ranking is consumption +4.15, land with livestock +2.46, red meat mix +1.43 and crop yields +0.16 million (A385). R04a's request is a file already held: reword to cite it.
* Both years use the same two ABS holdings items. The ABS grazing area was 364 Mha in 2008 and 332 Mha in 2020-21, "after it changed its land-use categories in 2016" (`analysis/land_2011/README.md`).
* **Found by the referee, missed by the audit:** nothing in the records mentions the EVAO scope threshold or the move to a business-register frame. R04b's account (a $5,000 threshold before 2015-16 and $40,000 after) is consistent with how I understand the ABS scope notes, but it needs checking against the ABS explanatory notes. It would matter most in peri-urban zones, which fits the Hawkesbury-Nepean-Sydney cropland halving "on an unchanged boundary" (S5).
* Swan is a boundary case, not a frame case: its 2011 zone carries the pre-Perth-boundary overlay, +9,798 km2 (`land_2011/README.md`, point 1). R04b is partly mistaken there.
* How much of the combined figure the definitional question can reach (rough reading): where pasture binds, capacity is (C+P)/(c+p) (B114, section 1). The area cancels in the pasture term but not in the idle cropland ceded to pasture, which is credited at the higher per-hectare yield. Holding output and diet fixed, the area change alone moves capacity by about +1.3%, about 0.4 million of the 2.4 million. The rest of the combined figure is output: the livestock layer is +16.5% of 2011 capacity, of which the denominator ratio is 1.104, leaving about +5.5%. That agrees with ABS red-meat output +8%, milk -7% and wool -10% (issue 2). This is the external check R04a asks for, and it supports the combined figure.
* Artefact test (R04b question 7). On bounds of 0.4 and 2.5 instead of 0.5 and 2, no flip changes class:
  * The flagged flips stay flagged: Desert Channels 5.7, SA Arid Lands 6.5, Southern Gulf 2.58.
  * The clean flips sit at 1.02, 1.07 and 1.82.
  * 14 of the 53 regions are flagged at 0.5 and 2, and 10 at 0.4 and 2.5 (rough reading, `analysis/paper_a/movers-3.csv`).
* **Found by the audit, still open:** the `land_only_ratio` column is published-method values (X116). Recomputed on the corrected forward walk, every flip's ratio agrees to two decimals except Corangamite's (0.74 against 0.86), and neither value is flagged (rough reading, `capacity_by_cause_corrected_orders.csv` with `results/2011-fixed.csv`).
* The ABARES national land-use maps for 2010-11 and 2020-21 are not held (sources register lists only the CLUM December 2023 raster, D32).

**3. Does it change a finding?** National capacities do not move. The abstract's driver sentence and highlight 2 (A375 and A380 read as causes) should lead with the combined layer (A382, A385). The definitional question reaches at most about 0.4 million of the 2.4 million combined figure (rough reading). The land row alone (A372, -3.06 million) should not be read as land-use change, and the paper should stop reporting it apart.

**4. The fair response.** Reword to cite the file, plus a small compute; one option declined.
* Reword: Table 2 leads with the eight-layer game (land and livestock as one layer), and the nine-layer split goes to the supplement. The abstract and highlight 2 name the diet layers and the combined layer, not livestock. Section 2 names the frame and category changes, citing the ABS explanatory notes (Murray fetches the 2015-16 and 2020-21 notes).
* Compute (small, about 1% with a check): (a) a registered version of the output check (ABS meat, milk and wool in the two windows against the livestock layer's output part); (b) the ceded-cropland residue computed exactly, which bounds the definitional part; (c) X116 closed by rebuilding the land ratio on the corrected tier, with the 0.4 and 2.5 bounds reported in S1.
* Option declined, with reasons: rerunning the land layer on the ABARES national land-use maps (session-size, 4 to 6%, new data acquisition). With land and livestock reported as one layer, the national result is insensitive to the area series, and the regional flags already mark the zones where it matters. Response-letter words: "Because the model's livestock yields divide output by the same grazing area, a change of area definition cancels nationally when the two layers are read together, which the paper now does; the residue is the idle cropland credited at the new yield per hectare, about 0.4 million, which we report."
* A reviewer would likely accept the combined layer plus the bound. R04b may still ask for the ABARES series; the bound is the answer.

**5. Dependencies and conflicts.** It precedes issue 18 (abstract) and feeds issue 2. The referees agree; R04b goes further on the frame and is right to.

---

## Issue 4. The regional robustness test leaves out the choices that carry most national variance

**1. The issue.** The flip test and the "clean and robust" labels use 13 choices, while the land source and energy requirement carry nearly three-fifths of short-term national variance (R04a 3.3; R04a question 3). R04a: "North Tasmania's ... 13-choice 5th percentile is 174,487; scaled by the national 19-choice 5th percentile it would be about 141,000, below its population." Round-two status: **(i) new.** The gap was created by the widening of decision 115 and recorded in decision 126 and A419.

**2. What the records show.**
* R04a is right on the facts. The widened draws were run for the nation and states only, because `monte_carlo.mjs` with `MC_ZONES=all` stops at zone 45, where raster and release land differ by 152 km2 (X140). Decision 126 says the stop is "fixed only if a referee asks", and a referee has now asked.
* Rough reading, by each region's own state widening rather than the national one:
  * Tasmania's 19-choice 5th percentile is 0.774 of base against 0.896 on 13 choices, so North Tasmania's 174,486 becomes about 150,700, below 156,393.
  * Queensland's are 0.786 against 0.934, so Mackay Whitsunday's 174,230 becomes about 146,600, below 153,841.
  * (`monte_carlo_draws_2025-fixed_wide_states.csv`; `monte_carlo_draws_2025-fixed_all.csv`.)
* An independent rough check: North Tasmania tips when the food amount exceeds 187,593 / 156,393 = 1.20. The energy choice is uniform on 1.000 to 1.286, so it tips in about 30% of draws from energy alone, if capacity scales inversely with the food amount. Mackay Whitsunday needs 1.29, just outside the range, so it depends on the other choices.
* **Mistaken premise in part.** South West Queensland is the long-term clean flip. Its 2025 population is 7,109 against a long-term capacity of 23,533 (`regional_flips-3.csv`). The energy requirement is not drawn in the long term (time-frame definition, B115), and Queensland's long-term 5th percentile is 0.868 of base on 19 choices against 0.856 on 13. It is safe.
* The energy choice is shared by both years. Under a high food amount North Tasmania was already over capacity in 2011, so the flip itself disappears; the test is about the 2025 status, but the point holds either way.

**3. Does it change a finding?** Yes, probably:
* A036 (two clean short-term flips) would likely become none.
* A038, A184, A188, A199, A402 and A419 move or are restated.
* The fourth conclusion and the section 10 reading of North Tasmania ("passes the land, boundary and range tests in hand", A056, A343) would change.
* A039 (South West Queensland) stands.
* The abstract does not name the flips (R04a notes this as a gap), so the abstract is not directly touched.

**4. The fair response.** Compute.
* Fix X140 by building the raster-land variant on the release land for zone 45, or relaxing the land check for that zone and recording it. Rerun the 19-choice draws with `MC_ZONES=all`, then `regional_flips.py`, `shocks_ranges.mjs` and the tipping counts on the widened zone ranges. Blind check. About 2.5 to 3.5% of the weekly allowance (B115 with V41 logged about 450,000 Opus tokens).
* R04a's fallback, applying the national widening proportionally, is not recommended as the published method. It is coarser than the state proxy above and would be replaced by the run anyway.
* Response-letter words: "We have run the full 19-choice draws for every region. On them [N] short-term flips keep their 2025 status across the 5th to 95th percentile; the conclusions and section 10 now say so, and the word 'robust' is used only for flips that pass on the full set."

**5. Dependencies and conflicts.** It shares the run with issue 5 (paired draws can use the same machinery) and with issue 7 (regional tipping counts). R04b does not raise it, but its question 7 on bounds is a cousin.

---

## Issue 5. The change between years is not tested

**1. The issue.** The headline is the 2011 to 2025 rise, but 2011 has no range and the 2011 value lies inside the 2025 range; both referees ask for paired draws on the shared choices (R04a 3.4; R04b 6, first part; R04a question 2; R04b question 8). R04b: "Many of the 19 choices ... would apply to both years alike, so the uncertainty of the difference is much smaller than that of either level." Round-two status: **(ii) answered and not accepted.** R03a recommended stating that 2011 has no range, with paired draws as an option (issue 5, option (b)). Decision 115 reworded the sentence to "holds at the base settings ... not a test across the settings". The text does this (9.1), but the abstract does not, and both referees want the computation.

**2. What the records show.**
* R04b's premise is right, and more so since the widening. Of the six added choices, the energy requirement (27% of short-term variance), the loss factors (6%) and avoidable waste (1%) are the same setting in both years. The resilience table, the organic factors and the diet-share ranges have 2011 analogues. The meat window, meat calibration, trend window and fuel proxies are 2025-only.
* R03a's caution, "most sampled choices are 2025 proxies", applied to the 13-choice set and is weaker on 19.
* The land source is a special case. Drawing the raster for 2025 while 2011 stays on holdings compares two sources. A paired test would need a 2011 raster, which is not held. On holdings land only, the 19-choice range is 29.8 to 43.1 million (S7).
* Rough reading, energy paired: if 2011 is scaled by the same food amount as each 2025 draw (capacity inversely proportional to the food amount, which the model's linear structure suggests but which was not tested):
  * the ratio of 2025 to 2011 runs 1.09 to 1.61, 5th to 95th percentile, with a median of 1.33;
  * 0.2% of draws show a fall, against 13% on the unpaired comparison;
  * holdings-land draws alone give 1.06 to 1.41.
  * (`monte_carlo_draws_2025-fixed_wide.csv`, block A.)

**3. Does it change a finding?** On the rough reading it strengthens A001 and A003 and the first conclusion: the rise is very likely to survive pairing. It also changes the right wording of A406, A009 and decision 115's sentence: "inside the spread of settings" becomes "the paired change is positive in nearly all draws". The long-term change (A009, 15.35 to 15.6) is small and will probably stay inside its paired range; say so.

**4. The fair response.** Compute and reword.
* Compute (session-size, about 2.5 to 3.5% with a blind check): run `monte_carlo.mjs` on `2011-fixed-3` with common random numbers for the shared choices (energy, loss factors, waste, organic factors, resilience table, and the diet shares as relative moves). Report the distribution of the paired difference and ratio nationally, and by region on the issue 4 run. The 2025-only choices are reported as 2025 data uncertainty, with the 2011 value's position against them.
* Reword the abstract: "rose from 33.3 to 41.5 million at fixed settings; across the settings both years share, the rise holds in [x]% of paired draws." This needs the paired-draw computation first.
* A decision row is needed, because the audit listed this computation as open with none (audit section 9, item 20).
* Two defensible framings of the land source: (a) pair on holdings land only and report the raster as a separate 2025 definition (recommended: like for like); (b) leave the land draw unpaired. A reviewer would accept (a).

**5. Dependencies and conflicts.** It shares machinery with issue 4 and depends on issue 6 for the shocked version. The referees agree.

---

## Issue 6. The bad-year comparison uses two weather tables

**1. The issue.** 2011 uses the thesis table (0.599 at 20 years) and 2025 the updated one (0.634), so the change at 1 in 20 is mostly the table (R04a 3.5, first part; R04b 6, second part; R04a question 5). Round-two status: **(ii) answered and not accepted.** R03a issue 6 said to state that the tables differ; section 2 and S4 state it, but Table 6, 8.1 and A196 still compare across tables.

**2. What the records show.**
* Both referees are right. The tables are in `analysis/resilience_2025/README.md`, section 2: Australia's thesis factors are 0.741 at 10 years and 0.599 at 20; the updated factors are 0.742 and 0.634.
* Rough reading: national shocked capacity is base times factor exactly (`analysis/paper_a/README.md`), so 2011 on the updated table reads 0.90 people over capacity at 1 in 10 (unchanged) and 1.06 at 1 in 20, against 1.12 on the thesis table and 1.05 in 2025.
* The improvement in section 8.1 ("1.12 in 2011 and 1.05 in 2025") is therefore the table.
* The 1-in-100 factors are identical (0.456), so the long term is unaffected. The resilience layer moves long-term capacity by -7 people (A378).

**3. Does it change a finding?** A196 ("0.89 in 2011, 0.95 in 2025") becomes about 0.95 against 0.95 on one table. Table 6's 2011 rows at 1 in 20, the 2011 tipping counts at 1 in 20 (four regions, B110) and the section 8.2 comparison "three regions to five" move. The abstract and highlights do not quote the 2011 bad-year figures.

**4. The fair response.** Compute (quick) and reword.
* Compute (quick, about 1% with a check): rerun `shocks_by_region.mjs` and `shocks_summary.py` for `2011-fixed-3` with the 2025 resilience table (a release variant or an override), and put the 2011 rows of Table 6 on it. The thesis-table rows go to the supplement as the as-published 2011 basis.
* Reword 8.1: "On one weather table the bad-year multiples are the same in both years; the change in the margin between 2011 and 2025 is an average-year change."
* Two defensible bases for 2011: (a) the 2025 table for both years (recommended: the comparison is then a data comparison); (b) each year with the record as known then. A reviewer would accept (a), with (b) in the supplement.

**5. Dependencies and conflicts.** It feeds issue 7's failure-probability range and issue 5's shocked paired version. The referees agree.

---

## Issue 7. The weather factor itself: cereal on pasture, timing, the old record, and a two-figure failure probability

**1. The issue.**
* A cereal factor applied to pasture-fed output gets the timing and probably the size wrong, against the paper's own single-year evidence.
* The 1-in-20 and 1-in-100 factors rest on a few old seasons.
* The record is assumed stationary, despite Hochman et al. (2017).
* The cereals are not weighted by area.
* State factors may understate regional exposure.
* The failure probability is spurious to two figures.

(R04a 3.5, rest; R04b 5; R04a questions 6 and 10; R04b questions 5 and 6.) R04b: "present the crop-only and all-output results as bounds with equal weight in the abstract." Round-two status: **(ii) answered and not accepted** for the cereal-on-pasture point: the crop-only bound (B112, A398, A399, S10) was computed, but it sits in 8.1 and the supplement, not the abstract. **(iii) not reached** for the sub-period table and the livestock-output drought test R03a proposed. **(i) new** for the precision of the failure probability, which the revision derived (S8).

**2. What the records show.**
* The crop-only bound is held: 41.2 million at 1 in 10 against 30.8 on all output; 24.7 against 15.6 at 1 in 100 in the long term (S10, `drought_bounds.csv`). Reword to cite the file in the abstract.
* The single-year series (S10 paragraph; A317) is unverified (X118, `build_years.py` fails at 2016-17). R04a question 10 asks whether it will be verified: on the records, not unless X118 is fixed.
* An observed livestock check is possible from files the pipeline already reads (rough reading). On ABS red meat output 2004-05 to 2024-25, each year over its ten-observation reference by the resilience method, the worst years are 2021-22 (0.86) and 2020-21 (0.87): the rebuild years after the 2017 to 2019 drought, not the drought years. That is the lag both the paper and R04b describe, milder than the cereal 1-in-10 factor of 0.742. Twenty-two years cannot name a return period.
* The 1-in-100 factor is the midpoint of the 1941 and 1915 seasons (S4), as R04a says. The fitted-tail interval for Australia's 100-year factor is 0.32 to 0.54 (`resilience_2025/README.md`, section 3). No sub-period table exists. Weighting the three grains by area "was not tested" (same README, section 4).
* State factors: the national 1-in-100 factor (0.46) is milder than most states' (NSW 0.30, Victoria 0.22; S6), and regions take their state's factor. R04b's point that sub-state exposure may be deeper still is fair; the ABS historic record is by state, so regional factors cannot be built from it.
* Failure probability (rough reading, each draw's capacity mapped to a return period by the table's own straight-line rule, which reproduces the base 5.8%):
  * 19-choice draws: 2.3% to 19% a year (5th to 95th percentile), median 7.6%;
  * 13-choice draws: 3.9% to 10.6%;
  * herd-cycle draws: 4.8% to 7.3%.
  * (`monte_carlo_draws_2025-fixed_wide.csv`, `_all.csv`, `_herdcycle_all.csv`; `tables.csv`.)

**3. Does it change a finding?**
* The abstract sentence on 1 in 10 and 1 in 20 and highlight 3 (A014, A196, A404) need the crop-only bound beside them.
* The conclusion's "about 5.8% a year, 1 in 17" (A418) becomes a range or goes.
* Section 11's stores and drought-proofing results (A264 to A266) rest on the same factor and are already marked so.
* Sub-period and area-weighted factors could move the 1-in-10 and 1-in-20 statements either way; nothing in the records says which.

**4. The fair response.** Reword now; compute small.
* Reword (no cost): the abstract gives both bounds with equal weight: "with the cereal factor applied to all output, capacity is 30.8 million at 1 in 10; applied to crops alone, 41.2 million." The failure probability is dropped from the conclusions, and 8.1 and S8 give the range across the draws. Highlight 3 names the cereal basis.
* Compute (small, about 1 to 1.5% with a check):
  * (a) `resilience.py` on the record from 1950-51 and from 1970-71, and area-weighted where the historic workbook carries areas (the 1990-only table has 35 seasons and cannot carry a 1-in-20 factor beyond rank 2; report it at 1 in 10 only);
  * (b) the livestock-output ratio above as a registered table, with a one-year-lag variant of the allowance;
  * (c) the failure-probability range as a registered row.
* Two defensible answers on a pasture-side factor. (a) Present the two bounds and the observed livestock ratio, and say no grazing record is used (recommended: no grazing record is held, and AussieGRASS would need data the project does not have). (b) Build a factor from AussieGRASS pasture growth (Murray fetch; session-size). A reviewer would accept (a) if the abstract carries both bounds.
* Fix X118 (small, about 1%) or cut the single-year figures from the supplement. Recommend the fix: it is the only observed check, and R04a asks for it.

**5. Dependencies and conflicts.** It depends on issue 6 (one table) and issue 4 (regional counts). The referees agree; R04b is more specific on timing and weighting.

---

## Issue 8. Projections are invoked but not analysed

**1. The issue.** Section 8.1 sets a 2025 capacity against populations 40 years on in one sentence. R04a asks for capacity held explicitly fixed, the long-term preset against projections, official variants and regional projections (R04a 3.6; R04a question 8). Round-two status: **(ii) answered and not accepted.** R03a issue 8 recommended a short national paragraph (option a); decision 104 took "projections compared with capacity"; the revision added one sentence.

**2. What the records show.**
* The sentence already says "capacity held at 2025 data", so part (a) is half met.
* Part (b) is right: 40.5 / 15.6 = 2.6 on the long-term preset; the paper does not say so.
* Official variants: the Population Statement (L228) and the Intergenerational Report (Treasury 2023) are held; whether they print high and low series was not checked here. ABS Population Projections (3222.0) are not in the registers.
* Regional projections: no official series is published on the 2011 NRM zones. State series (NSW Common Planning Assumptions, Victoria in Future, the Queensland Government Statistician) are on LGA or SA2 geographies and are not held. The D47 allocation could carry them where they are on SA2.

**3. Does it change a finding?** No registered finding. The paragraph would add claims.

**4. The fair response.** Two defensible options.
* (a) Compute a national paragraph (recommended): capacity at base and its paired range, at 1 in 10 on both bounds, and on the long-term preset (2.6 times), against the Statement's and ABS's series with their variants. Capacity is held at 2025 data by assumption, and the decomposition's 24.6% in 14 years is shown as one reason it will not stay fixed. Quick to small, about 0.5 to 1%, plus Murray fetching ABS 3222.0 if no variant table is in L228.
* (b) Cut 1.1's framing to what the paper uses.
* Regional projections: out of scope for this paper, with a sentence. Response-letter words: "No projection series is published on these 53 regions; state series on other geographies could be allocated by the method used for the ERP, which we note as the natural next use of the regional results." A single-state pilot (Queensland, SA2-based) would cost session-size, 3 to 5%, plus fetches; not recommended within the 8,000-word limit (decision 92).
* A reviewer at this journal would accept (a) with the out-of-scope sentence; R04a says as much ("if the authors prefer to keep projections out of scope ... cut back accordingly").

**5. Dependencies and conflicts.** It uses issue 5's paired range and issue 7's bounds. It interacts with issue 9 (age structure of projected populations). R04b raises only the long-term preset (issue 16).

---

## Issue 9. Per-person requirements are fixed while the age structure changes

**1. The issue.** The energy requirement is the same in both years and every region, though the population aged and regional age structures differ widely; ERP counts residents, not workforces or tourists (R04a 3.7; R04a question 7). Round-two status: **(i) new.**

**2. What the records show.**
* R04a is right that the requirement is fixed: a food amount on the sedentary NHMRC diet in both years. The energy choice drawn in 2025 (1.000 to 1.286) is a national activity level, not an age-sex adjustment (S4; B115).
* The NHMRC Nutrient Reference Value tables by age and sex were read for B115 from the archive PDF (Tables 3 and 4). ERP by age and sex is not held: D31 is totals.
* No adjustment exists in the records. Its sign is likely to favour 2025, since older people need less energy, but its size is unknown.

**3. Does it change a finding?** Probably a little: the 2025 capacity could rise by a few per cent relative to 2011, and regional ratios would shift in retirement coasts and mining regions. Nothing in the records gives the size.

**4. The fair response.** Compute (small) nationally; regional out of scope with a bound.
* Compute (about 1 to 1.5%): a mean per-person energy requirement for 2011 and 2025 from ERP by single year of age and sex (national ERP fetch by a job with network, or Murray) and the NRV tables. Apply it as a ratio to both years' capacities and report the change.
* The regional version needs SA2 age-sex ERP (larger fetch). Recommend: report the national adjustment, and the range across regions from the state age-sex tables if they are fetched together.
* A sentence on non-resident populations (Northern Territory, Rangelands, Wet Tropics), as R04a asks.
* A reviewer would accept the national adjustment with the regional point stated.

**5. Dependencies and conflicts.** It touches issue 4 (energy is the choice that tips North Tasmania) and issue 8 (older projected populations). Only R04a raises it.

---

## Issue 10. The scale result: a partition effect, three bases, and the substitution rule untested

**1. The issue.** Both referees say the following:
* The SA2 loss follows from the substitution rule and the partition, not from unit size.
* "Scale curve" invites the wrong reading.
* Three yield bases are in play.
* The rule should be tested by letting some pasture carry crops, especially the arable share of grazing land in the mixed wheat-sheep zone.

(R04a 3.8; R04b 4, second half; R04a question 9; R04b question 2; R04b minor 13.) Round-two status: **(ii) answered and not accepted** for the bases and the mechanism (B117 put the state basis in the main text and named the rule beside the 37%). **(iii) not reached** for the 200-draw random groupings and the rule sensitivity R03a proposed, and for reporting the dairy relaxation already held.

**2. What the records show.**
* Right on the mechanism: "Capacity was exactly proportional to land", and the loss is the mismatch of land types between units (S2; `scale_curve_2025/README.md`).
* Right on bases: the main text still mixes the state basis (curve, 44% for NRM regions), own yields (sections 7, 8 and 11, 63%) and the national yield vector (random groupings, 33%). The random groupings are still five draws (S2).
* A relaxation is already held: dairy on cropland at observed dairy-farm yields takes the SA2 share from 37% to 40% of the unchanged national figure. Relative to its own national figure the SA2 share is 34%, so "the loss from pooling ... is about two thirds under every treatment" (`analysis/pasture_2025/README.md`, `two_pool.csv`).
* B114 relaxes the national pairing (82 to 108 million on the diet's energy) but not the scale curve.
* The GAEZ arable share of grazing land by SA2 is held (`data/sa2/arable_share_gaez_by_sa2.csv`, D54), which is exactly the input R04b names for the mixed zone.
* R04b question 2: cropland carries pasture-fed products "square metre for square metre, at pasture's own output; pasture never grows crops" (B114, section 1). The paper does not say so.

**3. Does it change a finding?** A088 (37%) stands as a model result. Highlight 5 and the abstract need "follows from the rule and the partition". An arable-share sensitivity would give the size of the rule's effect at SA2. On the dairy evidence it is a few points, but grazing land in the mixed zone is a larger area than dairy land, so nothing can be said in advance.

**4. The fair response.** Reword, cite the file, and compute (small).
* Reword: retitle section 5 as the partition effect ("self-sufficiency by unit"), keeping "scale curve" once for continuity with Lane et al. (2015). Put one basis in the main text everywhere: either state yields with own yields as the bound, or the reverse, but the regional sums of sections 7, 8 and 11 must use the same one. The national yield vector goes to the supplement. Report the dairy relaxation in S2. State the cropland-for-pasture rule and its yield in section 6.
* Compute (about 1.5 to 2.5% with a check):
  * (a) 200 or more random groupings at each level on the main-text basis with `ideal_split_test.mjs` (R03a issue 9);
  * (b) the scale curve with the GAEZ arable share of each unit's grazing land allowed to carry crops at the unit's crop yields, nationally and at SA2.
* Two defensible bases for sections 7, 8 and 11: (a) move them to the state basis so the paper has one (recommended: R04a's request; the own-yield figures go to the supplement); (b) keep own yields there and say so in every table caption. A reviewer would accept (a).

**5. Dependencies and conflicts.** It shares the rule statement with issue 12. The referees agree. R04b adds the mixed-farming case, which the arable-share run answers.

---

## Issue 11. Short-term capacity is close to the production-to-consumption ratio of pasture-fed food

**1. The issue.** With pasture binding and livestock yields equal to output over area, short-term capacity largely restates the self-sufficiency ratio of meat and dairy at the current herd. The paper should state the identity and compare it with ABARES or FAOSTAT ratios for both years (R04b 3). Round-two status: **(i) new.**

**2. What the records show.**
* R04b is right, and the records already hold the comparison.
  * The land rule is capacity = (C+P)/(c+p), 3,635,188 km2 over 87,587 m2 a person (B114).
  * The meat balance on mean 2021-23 production gives 40 to 41 million against the model's 41.5 million: "The meat count agrees with the accounting model ... for the same reason: both are bound by pasture-fed meat" (`analysis/method_tests_2025/README.md`, application to current data).
  * Production over food eaten is 3.0 for beef and veal and for mutton and goat, and 1.5 for milk (`analysis/external_anchors_2025/README.md`, `production_scaling.csv`).
* The section 11.7 sentence "the two are not compared directly" understates what the project has done.
* No 2011 counterpart is held: `fao_au_production_1997_2023.csv` holds only 1997, 1998 and 2021 to 2023 rows.

**3. Does it change a finding?** No value moves. It changes what the headline means, as R04b says: the short term is a land-based restatement of pasture-fed self-sufficiency at the current herd and diet. The 2011 counterpart would test the change (A001 to A003) against an independent ratio.

**4. The fair response.** Reword to cite the file; small compute for 2011.
* Reword: section 6 states the identity in two sentences and presents the meat balance and the food-group ratios as an external check ("both are bound by pasture-fed meat"). Section 11.7's FAOSTAT sentence becomes that check.
* Compute (small, about 0.5 to 1%): the same balance on FAOSTAT 2010-12 (the bulk file is kept by hash and URL, decision 81; a job with network re-fetches it), giving the 2011 ratio beside the model's 1.49.
* Response-letter words: "We agree, and now say so in section 6. A commodity balance of meat on 2021-23 production gives 40 to 41 million against the model's 41.5; the agreement is the validation the referee suggests, and the 2011 balance is now beside it."

**5. Dependencies and conflicts.** It supports issue 3 (output change) and issue 2. Only R04b raises it; R04a's external output check (issue 3) is a cousin.

---

## Issue 12. Grain-fed and pasture-fed livestock

**1. The issue.** Cattle meat is classed wholly as pasture-fed. If feedlot output sits in the pasture yield numerator, the pasture yield is inflated and part of the livestock rise is feedlot growth on cropland (R04b 4, first half; R04b question 1). Round-two status: **(iii) not reached.** R03a issue 3 asked the paper to "say what grain finishing does in the model", and the revised text does not.

**2. What the records show.**
* R04b's premise is partly right and partly mistaken. The cattle-meat yield is meat over the beef share of grazing land plus feedlot grain hectares (grain over the mean grain yield) plus feedlot land per head (`pipeline/yields/livestock.py`, line 63). The feed grain follows cattle on feed, 720 to 1,430 thousand head (`livestock_national_series.csv`).
* So feedlot output is in the numerator, and its grain hectares are in the denominator. Feedlot growth does not simply inflate the yield. What is right in the premise: the grain hectares are charged as pasture-type land, because cattle meat is a pasture product in the land rule (S10).
* Nationally, where pasture binds and idle cropland is ceded to pasture, capacity is (C+P)/(c+p) (B114). Moving the feed-grain hectares from the pasture account to the cropland account leaves the pooled land need unchanged, so the national short-term capacity does not move. It matters only where cropland binds.
* Dairy's bought-in feed is not modelled (HANDOFF caveat; `pasture_2025/README.md`, Limits).

**3. Does it change a finding?** Nationally, no (by the land rule). Regionally, possibly in cropland-bound zones; the size is not computed.

**4. The fair response.** Reword and rebut; quick compute.
* Reword: two sentences in section 6 or S1 on how feedlot output and its grain land enter, and the national invariance.
* Rebut, in response-letter words: "Feedlot grain land is already in the cattle-meat yield's denominator. Because idle cropland is ceded to pasture where pasture binds, moving that land to the cropland account changes no national figure; we show the regional effect in the supplement."
* Compute (quick, about 0.5%): the regional sensitivity with feed-grain hectares on the cropland account.

**5. Dependencies and conflicts.** It shares the rule statement with issue 10. Only R04b raises it.

---

## Issue 13. The 2011 NRM boundaries and planning relevance

**1. The issue.** The regions are the NRM regions of 2011, since redrawn in New South Wales (2014) and South Australia (2020). The claim to inform a National Food Plan needs current planning units or SA4s (R04b 7). Round-two status: **(i) new** as framed. R03a (c) answered the boundary-version point: both years are on the 2011 polygons.

**2. What the records show.**
* Both years use the 2011 NRM polygons; five zones' 2011 data carry the older 2010 overlay areas (`land_2011/README.md`). R04b is right that these are not today's administrative regions; the paper does not say so.
* SA4 results are computed (scale curve, 89 units, `results/scale_curve.csv`). They behave better than the NRM partition: 58% against 44% (Table 3).

**3. Does it change a finding?** No.

**4. The fair response.** Reword; optional small compute.
* Reword: section 2 says the 53 regions are a fixed analytical partition (the thesis's), not current administrative regions, and 1.4's planning sentence is softened to match.
* Optional (small, about 0.5 to 1%): a supplementary table of SA4 status in 2025 on the main-text basis, which serves planners and costs a script over files already held. Mapping to current state planning regions is out of scope (new boundaries, new allocation).

**5. Dependencies and conflicts.** None. Only R04b raises it.

---

## Issue 14. The diet layer rests on one FAO series change, and what "consumption" contains

**1. The issue.** FAO beef and veal supply fell from 39.1 to 25.9 kg a person. That is availability, not intake, and 2021-23 was a high-price herd-rebuild period. The change needs a second source and a full-cycle window, and the consumption layer is described as partly non-diet (R04b 8; R04a minors 10, 11). Round-two status: **(i) new** for the corroboration; R03a issue 4 settled what the layer is.

**2. What the records show.**
* The figures are FAO food balance means of 2010-12 against 2021-23 (`analysis/consumption_2025/README.md`).
* The ABS 2011-12 and 2023 nutrition surveys agree on direction for discretionary foods but are "on a different basis" and were used "as a check on direction, not as an input" (same README).
* No ABS Apparent Consumption of Selected Foodstuffs (4316.0) issue for the period and no ABARES or industry consumption series are held (the register holds only the 1991-92 issue of 4306.0, L051).
* The FAOSTAT bulk is kept by hash (decision 81), so other windows can be built.
* On minor 11, R04a is partly mistaken. Fuel, biofuel and timber move the layer by 0.0%, +0.2% and 0.0% (same README, "Proposed values"), so the layer is almost wholly diet. The paper's "so it is not wholly diet" overstates the point.
* The diet shares are drawn in the Monte Carlo (red-meat share low end 0.528). On the herd-cycle draws the red-meat share carries 85% of short-term variance (S8).

**3. Does it change a finding?** If the 2021-23 beef level is a cyclical low, the consumption and red-meat-mix layers (A376, A380; 5.6 million, 68%) are overstated by an unknown share. The herd-cycle range's dependence on the red-meat share shows the size is material.

**4. The fair response.** Reword and small compute; one fetch.
* Reword: "food supply (availability)" wherever the FAO change is described. The consumption layer is described as "the diet shares; fuel, biofuel and timber settings move it by 0.2% or less".
* Compute (small, about 0.5 to 1%): the diet shares on a FAO window spanning the cattle price cycle (for example 2014 to 2023), with the layer recomputed, as a reported variant.
* Fetch (Murray): ABS 4316.0 and an industry domestic consumption series, for a one-line corroboration of direction and size.

**5. Dependencies and conflicts.** It touches issue 5 (diet shares as shared choices) and issue 18 (abstract wording). The referees agree.

---

## Issue 15. Missing literature

**1. The issue.** The paper is not placed in the carrying capacity and population literature or in land-system and agricultural science. Both referees name works (R04a 3.9; R04b 9). Round-two status: **(iii) not reached** for Paper A. R03a issue 13 recommended a paragraph (Cohen, Price, Seidl and Tisdell) and Bryan and Grundy in section 1, and decision 111 took "the literature the referees name added and read". The Paper A revision cut rather than added (B117 notes: literature summaries shortened), and none of these is in `papers/A_results/draft/references.md`.

**2. What the records show.**
* Held and read, not cited in Paper A:
  * Cohen (1995, L049) and Cohen (2017, L106)
  * Price (1999, L048)
  * Seidl and Tisdell (1999, L045)
  * Peters et al. (2016, L015), the ten-diets paper R04b names
  * Zumkehr and Campbell (2015, L103)
  * Fader et al. (2013, L105)
  * Gerten et al. (2020, L083)
  * Bryan et al. (2016, L076)
  * Grundy et al. (2016, L135)
* Fetched but not read: Das Gupta (1993, L257).
* Not held:
  * Pradhan and colleagues on regional self-sufficiency
  * McKeon and colleagues on rangeland drought
  * the crop-livestock mixed-farming literature
  * Kitagawa (1955) and Shapley (1953)
  * the 2010 sustainable population strategy debate
  * ABARES climate-adjusted productivity beyond Hughes and Lawson (2017, L170)
* Kurtz et al. (2020, L104) is cited in S2 only.

**3. Does it change a finding?** No.

**4. The fair response.** Reword and add.
* One paragraph in section 1 placing the paper: Cohen on conditional estimates, Peters 2016 and Zumkehr and Campbell on regional capacity, Fader and Gerten on decoupling and boundaries, Bryan and Grundy on Australian land-use futures. Cite Das Gupta for the decomposition after reading it. About 1% for reading and the reference rebuild, within the word limit by cuts elsewhere (issue 17).
* Murray fetches the works not held (Pradhan, McKeon, Kitagawa, a mixed-farming review). B119's route and decision 82 apply.
* Decision 33 bears on tone. Cohen's critique of single-number estimates is cited for what it says about conditional estimates, not as a contrast with other authors.

**5. Dependencies and conflicts.** It needs words from issue 17. The referees agree, each naming their own field.

---

## Issue 16. The long-term preset: an energy and weather scenario named as a plan

**1. The issue.** "100-year self-sufficiency plan" suggests a time path and a land-system finding. Table 5 shows the figure is set mainly by the weather allowance (34.3 million without it) and the fuel setting (3.7 million with short-term fuel), so it should be framed as one scenario, with a less extreme return period beside it (R04b 10; R04a minor 13; R04a 3.6(b)). Round-two status: **(ii) answered and not accepted.** R03a issue 14 recommended keeping the names with a one-line definition; the definition is in section 2 but not in the abstract or highlights.

**2. What the records show.** Right on every count (Table 5; A011). The long-term settings set at 1 in 20 are not in the records as one figure, but the model's linearity in the factor gives it directly. The weather setting carries 20% of long-term variance and the land source 58% (S8).

**3. Does it change a finding?** A011 (57%) stands. The abstract and highlight 4 wording change. A 1-in-20 share would sit well above 57%: rough reading, about 15.6 × 0.634 / 0.456 = 21.7 million, 79% of the 2025 population, assuming no setting binds differently at 20 years. This needs a model run to register.

**4. The fair response.** Reword and quick compute.
* Reword: "long-term self-sufficiency preset", defined in the abstract as "low meat, organic, no avoidable waste, 210 litres of liquid fuel and the worst year in 100", with the two dominant settings named.
* Compute (quick, about 0.3%): the long-term preset at 1 in 20, registered.
* Two defensible names: (a) "long-term preset" (R04a's suggestion; recommended); (b) keep "100-year plan" for continuity with Lane (2017) in the same journal. A reviewer would accept (b) only with the definition in the abstract; both referees object to "plan".

**5. Dependencies and conflicts.** It uses issue 7 (weather factor) and issue 8 (2.6 times projections). The referees agree.

---

## Issue 17. Presentation

**1. The issue.** The referees list these problems:
* Release codes and file paths in the prose.
* Two inverse ratios.
* Precision to the person.
* Figures still in words (two with "no plotting script exists").
* Workflow language in the supplement ("decision 92", "unverified (the second route is blocked)").
* Section 11 read as a list.
* Mixed units.
* Three names for own yields.
* Repeated parentheses.
* Section numbering.

(R04a 3.10; R04b minors 1, 2, 4, 5, 6, 7, 8, 14.) Round-two status: **(ii) answered and not accepted.** R03a issue 14 and B126a defined a release key in section 2 but kept the codes in captions and text. Figures wait on decision 99 (iii).

**2. What the records show.** All right on the draft as assembled. The two-ratio point goes back to decision 87's convention, and the first-round referee found "people over capacity" read as a count (R03a issue 14). The working language is in `supplementary.md`, line 3 ("decision 92") and the S4 paragraph ("unverified (the second route is blocked)").

**3. Does it change a finding?** No.

**4. The fair response.** Reword (one revision pass).
* Release codes and paths go to the data availability statement and a supplementary key. The text says "2011 data" and "2025 data" on "the corrected method".
* One ratio. Two defensible choices: (a) capacity over population throughout, with "over capacity" defined as below 1 (recommended: it is the ratio population readers expect, and both rounds' referees stumbled on the inverse); (b) people over capacity throughout. Either changes the convention of decision 87's scopes, so it needs Murray.
* Two or three significant figures in the main text; exact figures stay in the supplement and claims files.
* Section 11 moves to the supplement except a one-table summary. This frees the words needed for issues 1, 8, 11 and 15 under decision 92.
* Workflow language goes from the supplement. Units are km2 throughout and "own yields" is the single term. The regions are defined once. Section 1 is renumbered 1.1 to 1.4.
* Figures follow decision 99 once the text is settled. The response letter says the figures are supplied as files.
* Cost: a Sonnet revision of about 1.5 to 2% and a blind Opus read of about 2% (B117 logged 622,000 Sonnet tokens; V45a 327,000 Opus).

**5. Dependencies and conflicts.** This pass carries every reword above. The referees agree.

---

## Issue 18. The abstract and highlights

**1. The issue.** Both referees find the numbers accurate and these overreaches:
* The rise is given without "at fixed settings".
* Livestock is named as a cause.
* The bad-year sentence leads on the all-output factor.
* The 57% is given without its scenario.
* The 37% reads as a finding about Australia.

R04a adds that the flips and the no-trade frame are absent. (R04a section 6; R04b section 6.) Round-two status: **(ii) answered and not accepted.** R03a issue 15's sketches were partly adopted.

**2. What the records show.**
* Right on each point (issues 3, 5, 7, 10 and 16).
* Highlight 3's "ranges include it" is ambiguous, as R04a says.
* Highlight 5 omits the own-yield bound (54%, S6).

**3. Does it change a finding?** The wording of A001, A003, A011, A014, A088, A196, A382 and A385 changes in the abstract and highlights.

**4. The fair response.** Reword, after issues 4 to 7 are computed. Sketch, for Murray's wording:
* "Between the 2011 and 2025 data, at fixed settings, national short-term capacity rose from 33.3 to 41.5 million; across the settings the two years share, the rise holds in [x]% of paired draws."
* "Most of the rise is a diet with less beef in it (5.6 million); more output on a smaller recorded grazing area added 2.4 million."
* "With a cereal-based weather allowance applied to all output, capacity falls to 30.8 million in a 1-in-10 year; applied to crops alone, 41.2 million."
* "A long-term preset of low meat, organic farming, little liquid fuel and the worst year in 100 covers 57% of the 2025 population; the weather and fuel settings set most of that."
* "If every SA2 must feed itself, their capacities sum to 37 to 54% of the national figure, because in the model pasture cannot carry crops."
* "All results are for a closed model with no trade."
* One sentence on the regional flips that survive issue 4.

Highlights follow, at most 85 characters each (decision 97). Keywords add "food security" and "regional population" (R04a minor 22; R04b section 6 adds "livestock" and "scale"; up to seven).

**5. Dependencies and conflicts.** It depends on issues 3, 4, 5, 6, 7, 10 and 16. The referees agree.

---

## Standing decisions that bear on the requests

* **Decisions 113, 118 and 122** govern Paper B (outside raters and the GFN licence; the definition span wording). No Paper A request is ruled out by them.
* **Decision 33** (tone: no emphasis on other authors' shortcomings) bears on issue 15 and on how the corrections to the author's own 2014 to 2017 papers are worded. It rules out no request. Response-letter words for the literature: "We now place the results among regional and national capacity studies (Cohen 1995; Peters et al. 2016; Zumkehr and Campbell 2015; Fader et al. 2013; Gerten et al. 2020) and Australian land-use futures (Bryan et al. 2016; Grundy et al. 2016), stating for each what it measures and on what assumptions, so the reader can see where this model's closed-region, fixed-diet answer sits."
* **Decision 126** is triggered: the zone-45 stop is "fixed only if a referee asks", and R04a 3.3 asks (issue 4).
* **Decision 115** sets the "rise holds" wording; issue 5's paired draws would justify amending it (a decision row).
* **Decision 98** (Elsevier Harvard references) conflicts with R04a minor 19: Population and Environment is a Springer journal. It needs a row amending decision 98 for Paper A, and the declarations moved to Springer's headings.
* **Decision 92** (8,000 words) constrains every addition; issue 17's move of section 11 pays for them.
* **Decision 22** answers R04a minor 16 and R04b minor 3: Murray chose the regions from the candidate list in `analysis/comparison_2025/movers.md`. "From the largest movers" is inaccurate and should read "chosen by the author, one of each type, from a list of large movers".
* **Decision 99** governs the figures; **decision 87** the ratio convention (issue 17).

---

## (a) All issues

Cost is the anticipated share of the weekly allowance on the calibrated basis: HANDOFF, about 1% per 150,000 Opus-weighted logged tokens; CARD, a Sonnet worker a third to a half of an Opus worker of the same length. It includes a blind check where a computation changes a figure. Round-two status: (i) new, (ii) answered and not accepted, (iii) not reached.

| No. | Referee(s) | Status | Verdict on the premise | Response type | Headline effect | Cost |
|---|---|---|---|---|---|---|
| 1 | R04a 3.1, Q1, minors 4 to 6 | (i) | Right on timing; vintage answerable (one ABS flow, 2021 SA2); wrong that 27,608,200 is rounded | Reword; quick compute; national row to Murray | Ratio about 1.5 to 1.6 on midpoint denominators (rough); +23.7% to +23.6% if row reset | Quick, about 0.3% |
| 2 | R04b 1, Q4 | (ii) | Right for crops; not borne out for meat output (both windows below the decade between) | Rebut in part; reword; small compute | None short term; long-term fall in coverage if anything larger | Small, 1 to 1.5% |
| 3 | R04a 3.2, Q4; R04b 2, Q3, Q7 | (ii) | Right; EVAO frame missed by the audit; Swan is boundary, not frame | Reword to cite B111 eight-layer file; small compute; ABARES rerun declined | Driver sentence: combined +2.46 M (A382); definitional reach about 0.4 M (rough) | Small, about 1% |
| 4 | R04a 3.3, Q3 | (i) | Right (X140, decision 126); wrong on South West Qld | Compute | A036 likely 2 to 0 clean short-term flips (rough); A039 stands | Session-size, 2.5 to 3.5% |
| 5 | R04a 3.4, Q2; R04b 6, Q8 | (ii) | Right, more so on 19 choices | Compute and reword | Rise likely holds in nearly all paired draws (rough: 0.2% fall) | Session-size, 2.5 to 3.5% |
| 6 | R04a 3.5, Q5; R04b 6 | (ii) | Right | Compute (quick) and reword | A196: 1 in 20 is 1.06 against 1.05 on one table (rough); improvement gone | Quick, about 1% |
| 7 | R04a 3.5, Q6, Q10; R04b 5, Q5, Q6 | (ii), (iii) | Right; single-year evidence unverified (X118); livestock lag visible in ABS output (rough) | Reword (bounds equal weight; drop 5.8%); small compute | Failure probability 2.3% to 19% (rough); abstract bad-year sentence | Small, 1 to 1.5%; X118 fix about 1% |
| 8 | R04a 3.6, Q8 | (ii) | Right; long-term preset 2.6 times projection unstated | Compute national paragraph; regional out of scope | New claims only | Quick to small, 0.5 to 1% |
| 9 | R04a 3.7, Q7 | (i) | Right; size unknown | Compute nationally | Likely a few per cent in favour of 2025 (unknown) | Small, 1 to 1.5% |
| 10 | R04a 3.8, Q9; R04b 4, Q2, minor 13 | (ii), (iii) | Right; dairy relaxation (37% to 40%) held, not reported | Reword; cite file; small compute | A088 stands; wording and one basis | Small, 1.5 to 2.5% |
| 11 | R04b 3 | (i) | Right; files hold the check (40 to 41 M meat balance) | Reword to cite file; small compute for 2011 | Meaning of the headline, no value | Small, 0.5 to 1% |
| 12 | R04b 4, Q1 | (iii) | Partly wrong: grain hectares in the denominator; nationally invariant by the land rule | Rebut; reword; quick regional compute | None nationally | Quick, about 0.5% |
| 13 | R04b 7 | (i) | Right on administrative relevance; both years on one partition | Reword; optional SA4 table | None | Quick to small, 0 to 1% |
| 14 | R04b 8; R04a minors 10, 11 | (i) | Right on corroboration; wrong that the layer is materially non-diet | Reword; small compute; Murray fetch | Diet layers (A376, A380) possibly overstated, size unknown | Small, 0.5 to 1% |
| 15 | R04a 3.9; R04b 9 | (iii) | Right; most named works held and read but uncited | Reword and add; fetches | None | About 1%, plus fetches |
| 16 | R04b 10; R04a minor 13, 3.6(b) | (ii) | Right | Reword; quick compute (1 in 20) | Abstract and highlight 4 wording; 1-in-20 share about 79% (rough) | Quick, about 0.3% |
| 17 | R04a 3.10; R04b minors | (ii), (iii) | Right | Reword (one pass); figures by decision 99 | None | 3.5 to 4% (revision and blind read) |
| 18 | R04a section 6; R04b section 6 | (ii) | Right | Reword after 3 to 7 | Abstract and highlights | Quick, inside issue 17 |

Counts by kind: **new 6** (issues 1, 4, 9, 11, 13, 14); **answered but not accepted 10** (2, 3, 5, 6, 7, 8, 10, 16, 17, 18); **not reached 2** (12, 15). Issues 7, 10 and 17 also carry first-round parts that were not reached.

All computations and the revision together: roughly 20 to 28% of the weekly allowance, most of it issues 4, 5 and 17. Every change that moves a Tier A value goes to Murray first (CARD).

## (b) The changes that would do most to satisfy both referees, in order

1. Fix X140, run the 19-choice draws for every region, and rewrite the flips, section 10 and the fourth conclusion on what survives. The rough reading says neither clean short-term flip does.
2. Test the change itself. Run paired 2011 and 2025 draws on the shared choices and put 2011's bad years on the 2025 weather table. The abstract then says the rise holds at fixed settings and in [x]% of paired draws, and the 1-in-20 "improvement" is withdrawn.
3. Report land and livestock as one layer everywhere, including the abstract and highlights. State the production-to-consumption identity with the meat balance already on file. Check the combined layer against ABS output, and name the ABS frame and category changes.
4. Give the crop-only and all-output drought bounds equal weight in the abstract. Replace the 5.8% with its range, and add sub-period and area-weighted factor tables and the observed livestock-output ratio.
5. Put a reference-period and source table in section 2 with the ERP vintage. Carry out the presentation pass: codes out, one ratio, two or three figures, section 11 to the supplement, literature paragraph in.

## (c) Where accepting the criticism would be wrong

* Conceding that the 2025 population of 27,608,200 is rounded would be wrong: it is the allocated SA2 sum, 304 below the ABS total (X108, D47).
* Conceding that South West Queensland's flip may fail the widened test would be wrong: 7,109 people against a long-term capacity of 23,533, and the energy choice is not drawn in the long term.
* Conceding that the 2011 window is a depressed livestock-output baseline would be wrong: ABS red-meat output in 2005-06 to 2009-10 was within 8% of the 2025 window, and both sit below the decade between (rough reading). A 20-year window containing the 2011 years moves the 2025 base by -0.1%.
* Conceding that the inland regions' gains are weather-driven output would be wrong: their livestock terms are mostly the grazing-area denominator, and regional class counts follow state herds.
* Conceding that feedlot output is credited at a pasture-only yield would be wrong: feed-grain hectares are in the cattle-meat denominator (`livestock.py`, line 63), and the land rule makes the national figure invariant to which account they sit in.
* Normalising livestock output by the cereal ratio, as R04b 1(b) suggests, would be wrong: it applies to meat the cereal-for-pasture assumption R04b 5 rightly questions.
* Conceding that the consumption layer is materially non-diet would be wrong: fuel, biofuel and timber move it by 0.2% or less.
* Conceding that the 2011 regional ERP may be a pre-rebasing series would be wrong: both years come from one ABS flow on 2021 SA2s (D31).
* Conceding that works citing the earlier papers were not checked would be wrong: they were listed (`cited_by_openalex_2026-11-07.md`). The sentence should say they were listed and one applies the model.
* Conceding that Swan's land fall is a frame change would be wrong: it is the pre-Perth-boundary overlay of the 2011 zone.
* Conceding that a stricter artefact bound changes the flips would be wrong: at 0.4 and 2.5 no flip changes class.

## (d) Questions to the author, with answers from the records

From R04a:

1. ERP vintage, and the rebased series? Both years are from one ABS flow, `ABS_ANNUAL_ERP_ASGS2021`, on 2021 SA2s (D31), so 2011 is the post-2021-census series. The 2025 figure is the first release for that date. The exact release label and retrieval date **need Murray** (the fetch script is not in the repository).
2. Can the choices with 2011 analogues be drawn for 2011? Yes for energy, loss factors, waste, organic factors, resilience table and diet-share ranges; not for the 2025-only proxies. Rough reading with energy paired: a fall in 0.2% of draws. **Needs a computation** (issue 5).
3. Land-source and energy draws by region, and which flips survive? Blocked at zone 45 (X140); decision 126 allows the fix once a referee asks, and R04a has. Rough reading: neither clean short-term flip survives; South West Queensland does. **Needs a computation** (issue 4).
4. How much of the pasture fall is reclassification? Not estimated in the records; the ABS notes **need Murray**. The combined land-and-livestock layer is +2.46 million (A382), of which about 0.4 million is reachable by the definition (rough reading).
5. Bad years with one table? Rough reading: 2011 at 1 in 20 reads 1.06 people over capacity against 1.05 in 2025; 1 in 10 is unchanged (0.90). **Quick computation** to register.
6. 1-in-10 and 1-in-20 factors from 1990 to 2025? Not run; 35 seasons support a 1-in-10 factor only. **Small computation.**
7. Change in mean energy requirement from age structure? Not in the records; NRV tables held, ERP by age and sex not. **Small computation, one fetch.**
8. Regions crossing capacity under regional projections? Not computed; no series on these zones. Out of scope recommended; **needs Murray** if wanted.
9. Scale result if some pasture can carry crops? The dairy relaxation takes SA2 from 37% to 40% (`two_pool.csv`); the arable-share run is **a small computation** on held GAEZ data.
10. Will the single-year series be verified? Not as things stand (X118). A fix is about 1%; otherwise cut it from the supplement. **Needs Murray's choice.**

From R04b:

1. How is cattle on feed used? Feedlot grain follows the cattle-on-feed series; its hectares and feedlot land are in the cattle-meat denominator (`livestock.py`, lines 59 to 63), and the product is charged to pasture.
2. At what yield does cropland carry pasture-fed products? Square metre for square metre at pasture's own output (B114, section 1).
3. Pasture fall: frame and threshold against real change? Not estimated; **needs Murray** (ABS explanatory notes). Nationally the combined layer limits its reach to about 0.4 million (rough reading).
4. Decomposition on equal full-cycle windows in both years? The 2025 side is held (-0.1% to +0.9%; herd-cycle range 39.4 to 43.8 million). The 2011 side cannot span a full cycle from the archive's five years. **Small computation** for three-year subsets.
5. Factor from 1950 or 1970, or area-weighted? Not run; area weighting "was not tested" (`resilience_2025/README.md`). **Small computation.**
6. Why not a grazing-record factor? No grazing record is held. The ABS meat output ratio shows the lag (worst years 2021-22 and 2020-21 at 0.86 and 0.87; rough reading). AussieGRASS **needs Murray**.
7. Flips at bounds of 0.4 and 2.5? No change of class (movers-3.csv; rough reading).
8. Paired difference? As R04a question 2.
9. Irrigated share 0.007? The parameter is irrigated area over all farmland, and ABS Water Use on Australian Farms 2020-21 gives 0.5% (`analysis/irrigation_review/README.md`). **Found by the referee, missed by the audit:** the paper calls it "irrigated share of cropland" (12.3, S6, Table S5), which is wrong; the cropped-land share is 4.6%.

## (e) Minor issues, grouped by kind, with the fix for each kind

* **Structure and numbering** (R04a minors 1, 15, 16; R04b minors 2, 3, 5): renumber section 1 to 1.1 to 1.4. Give one short box on what the bad-year results can bear. State the selection rule from decision 22, "chosen by the author, one of each type, from a list of large movers", and reconcile "five regions", Table 7's seven rows and S5's "four regions". Define "53 regions" once. Quick.
* **Precision and units** (R04a minors 9, 14; R04b minors 1, 7, 14): two or three significant figures in the main text, including Table 2 and the scenario percentages. Units for every Table 5 row (fibre in kg a person a year). km2 throughout, with a sentence on g/m2. Cut the rounding-edge footnote of Table 6. Quick.
* **Wording and accuracy** (R04a minors 2, 3, 7, 8, 11, 12, 17; R04b minors 4, 10, 11, 12):
  * Davies quoted for its own period, or a different quotation.
  * "Work citing them was listed, and one applies the model (Bolleter 2018)".
  * Compare like with like in section 3's net-fall sentence.
  * Give Table 1's overlaps. In the long term SA Arid Lands is both an artefact and not robust, so the row reads 2 + 1 + 1 for 3 flips; in the short term Desert Channels carries both flags.
  * The consumption layer is described as "almost wholly diet".
  * Mark the 2011 SA cells of Table 3 in the table.
  * Keep or cut the FAOSTAT 57% as the identity check (issue 11).
  * One term, "own yields".
  * Make the Lane (2014, p. 3) reconciliation explicit.
  * Give Anderson et al.'s Australian figure alone, if the paper gives it.
  * "Pooling gain of the closed model".
  * The irrigated-share label (question 9 above).
  * Quick.
* **Data statements** (R04a minors 4, 5, 6; R04b minor 9): national row (issue 1); the 2025 figure is an allocated SA2 sum, not a rounding; the count of straddling SA2s (quick compute). Quick.
* **References and journal form** (R04a minors 18 to 21; R04b minor 15):
  * Springer reference and declarations form (needs a row amending decision 98).
  * Soliman Hunter and Taylor cited by section, since the PDF has no printed pages.
  * Bolleter's year checked against the issue and the 2019 DOI (B103's year-disagreement list).
  * "McDougall", checked against the article.
  * Gifford et al. (1975) stays "cited in Henry and Godden (1995)" unless Murray fetches it.
  * The 18 [CHECK] fields in `references.md` completed.
  * Small.
* **Workflow language** (R04a 3.10; R04b minor 8): remove "decision 92" and "unverified (the second route is blocked)" from the supplement. Any figure not verified is either verified (X118) or cut. Quick.

## (f) Register rows touched

None (claims, sources, literature, defects).

**Wrong-value check:** *Example of a response that would concede something the records show to be false (marked as an example, not to be used):* "We accept the referee's point that the 2025 national population of 27,608,200 is rounded to the nearest hundred and have replaced it with the unrounded ABS figure." The records show it is not rounded: it is the sum of the ABS ERP of the 2,450 SA2s allocated to the zones, 27,608,504 less the 304 people lost in the allocation (sources register D47; defect X108).

## (g) Decision table for the author

Cost as a share of the weekly allowance on the HANDOFF calibration (1% per 150,000 Opus-weighted logged tokens; Sonnet a third to a half of Opus, CARD), including a blind check where a figure changes.

| # | Option | Recommendation | Confidence | Cost | Reason |
|---|---|---|---|---|---|
| 1 | Fix X140 and run the 19-choice draws for every region; redo the flip tests and tipping counts; rewrite flips, section 10 and conclusion 4 | Yes | High | 2.5 to 3.5% | R04a's first point; decision 126 anticipates it; the rough reading says the clean short-term flips likely go |
| 2 | Paired 2011 and 2025 draws on the shared choices, land source paired on holdings; amend decision 115's wording on the result | Yes | Medium to high | 2.5 to 3.5% | Both referees' top request; the rough reading suggests it strengthens the headline |
| 3 | 2011 bad years on the 2025 weather table, thesis-table rows to the supplement | Yes | High | About 1% | The 1-in-20 improvement is a table effect on the records |
| 4 | Replace the 5.8% with its range across draws; drop it from the conclusions | Yes | High | About 0.3% | A single figure is not supported (2.3% to 19% on the rough reading) |
| 5 | Factor variants (from 1950-51, from 1970-71, area-weighted) and the observed livestock-output ratio | Yes | Medium | 1 to 1.5% | Both referees ask; the records say area weighting was never tested |
| 6 | Fix X118 (single-year series) or cut it from the supplement | Fix | Medium | About 1% | It is the only observed check on the factor, and R04a asks |
| 7 | Land and livestock as one layer in Table 2, abstract and highlights; output check against ABS; residue bound; X116 closed | Yes | High | About 1% | The file exists (A382); both referees ask |
| 8 | Rerun the land layer on the ABARES national land-use maps | No | Medium | 4 to 6% plus data | Nationally the combined layer makes it second order; the residue bound answers it |
| 9 | State the production-to-consumption identity with the held meat balance; add the 2011 balance | Yes | High | 0.5 to 1% | Turns R04b's challenge into the paper's validation |
| 10 | Section 2 reference-period table with ERP vintage; midpoint-population check; national row reset to 22,336,514 | Yes (row reset: Murray) | Medium | About 0.3% | R04a's second point; the reset moves Tier A rows slightly |
| 11 | National projections paragraph (long-term 2.6 times, variants); regional projections out of scope | Yes | Medium | 0.5 to 1% plus a fetch | R04a's fifth point; regional series are not on these zones |
| 12 | National age-sex energy adjustment and a non-resident sentence | Yes | Medium | 1 to 1.5% plus a fetch | New request; sign likely favours 2025; size unknown |
| 13 | Scale section as partition effect; one basis throughout; 200 random groupings; arable-share relaxation; report the dairy relaxation | Yes | Medium to high | 1.5 to 2.5% | Both referees; the GAEZ input is held |
| 14 | Feedlot sentence and regional sensitivity | Yes | High | About 0.5% | First-round point not reached; nationally invariant |
| 15 | Diet window over the cattle price cycle; Murray fetches ABS 4316.0 and an industry series | Yes | Medium | 0.5 to 1% plus fetches | The diet layers are the largest part of the rise |
| 16 | Long-term preset renamed and defined in the abstract; its value at 1 in 20 | Yes | High | About 0.3% | Both referees object to "plan" |
| 17 | Presentation pass (codes out, one ratio, precision, section 11 to supplement, workflow language out, irrigation label, literature paragraph) | Yes | High | 3.5 to 4% (revision and blind read) | Both referees; pays for the additions under decision 92 |
| 18 | One ratio: capacity over population throughout (amends decision 87's convention) | Yes (Murray) | Medium | Inside 17 | Population readers expect it; both rounds stumbled on the inverse |
| 19 | References and declarations in Springer form (amends decision 98 for Paper A) | Yes | High | About 0.5% | Population and Environment is a Springer journal |
| 20 | Literature: cite the held works; Murray fetches Pradhan, McKeon, Kitagawa and a mixed-farming review | Yes | High | About 1% plus fetches | Decision 111 taken but not reached in Paper A |
| 21 | 2011 three-year window subsets (matched-length check) | Yes | Medium | About 1% | First-round proposal not reached; answers R04b question 4 on the 2011 side |
| 22 | A light third round (both personas, response letter and changed sections only) | Yes, after the blind checks | Medium | About 2% | See (h) |

Together: roughly 20 to 28% of the weekly allowance. Items 1, 2 and 17 are most of it.

## (h) Would a third round be needed?

Yes, but a light one. Both referees set out what would close the paper.
* R04a: "if the authors address 1, 2 and 4 fully and give a reasoned answer on 3 and 5, the paper could then be judged on minor points."
* R04b: five points, each met here by a computation or by a file already held, except a grazing-record weather factor (no record is held, so the answer is equal-weight bounds and the observed output ratio) and the ABARES land series (declined, with a stated bound).

On that measure, the changes above should take both reports to minor points. The reason a further round is still worth having is issue 4. The rough reading says the two flips the paper calls clean and robust will not survive the full set of choices, and that changes a conclusion and the regional story the demographer values most. A referee should see the paper with its regional findings restated. The paired test of issue 5 may in turn strengthen the national headline, which both referees will want to see stated with its range. I would run the third round on the response letter and the changed sections only, after the blind checks of items 1 to 7, at about 2% of the allowance. A full re-review is not needed unless the regional rerun moves more than the flips.
