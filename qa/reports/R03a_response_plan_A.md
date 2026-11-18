# R03a: a reasoned response plan to the two referee reports on Paper A (results)

Brief: `qa/briefs/R03a_response_plan_A.md`. Reports answered: `qa/reports/R02a_review_A_demographer.md` (referee A, a demographer, "R02a") and `qa/reports/R02b_review_A_land_systems.md` (referee B, land systems, "R02b"). Draft answered: `papers/A_results/draft/paper_A_draft1.md`, `supplementary.md`, `highlights.md`.

## The outcome in plain words

Both referees ask for major revision, and on the main points they are mostly right, but not always for the reason they give. Four of their concerns are confirmed by the records, and one of them goes further than either referee saw:

1. **The land and livestock layers are two halves of one sum.** The 2025 livestock yields are output divided by the 2020-21 grazing area of the land layer (`pipeline/yields/recent/livestock_zone.py`, docstring line 13 and line 100). The land layer takes 2.6 million off for less recorded grazing land; the livestock layer hands most of it back because the same output now sits on fewer hectares. Together they add +2.1 million in the short term, not "livestock +4.7 million". The abstract's driver sentence has to change: on the records, the largest part of the rise is the diet with less beef in it (consumption +4.2 and red meat mix +1.8 million).
2. **The 1-in-10 and 1-in-20 findings do not hold across the published 2025 range.** National shocked capacity is exactly the average-year capacity times the national factor (`analysis/paper_a/README.md`, "reproduces the national 1-in-10 capacity exactly"), so the range scales too: 26.9 to 34.0 million at 1 in 10 and 23.0 to 29.0 at 1 in 20, both straddling the 27.6 million population.
3. **The 2011 regional populations are not on the 2025 footing, in many more zones than the two copies already found.** `analysis/population_2011/zone_population_2011.csv` already holds the ABS 30 June 2011 figure for every zone, allocated exactly as 2025 is. 23 of the other 52 zones differ from the model's 2011 figure by more than 10%, three by a factor of about three. The audit looked for copies, and V33 looked at Victoria only; this pattern was not reported. A scratch rerun of the flip screen with these figures changes no short-term flip and removes one long-term flip (Northern and Yorke), so the regional findings survive. The paper still has to say so.
4. **The paper is not self-contained.** Table S1 is not built, the "full model in the supplementary information" is not there, figures 5 and 6 have no script, and the failure probability comes from Paper B. All of this is fixable from the records.

Where the referees are wrong, the records say so clearly: the long-term fall in regions over capacity is not a tier effect (it is a fall of 3, 4 and 2 regions on the published, corrected and improved tiers taken separately); the herd cycle does not reverse the rise (windows that span a full cycle move the 2025 base by -0.1% to +0.9%); the organic penalty has a source (Ponisio et al. 2015); pigs, poultry and feedlot grain are already charged to grain land; ABARES gives the export share by volume, as the paper says; and the main text is 7,850 words, not 10,000.

The detail follows, issue by issue, then the tables the brief asks for. Every figure is from a file named beside it. Where I give a rough reading of my own (not a registered result), it is marked "rough reading".

---

## Issue 1. Population inputs: source, vintage and method differ between the years

**1. The issue.** The two years' populations are undocumented and were built by different methods, and the flip screen tests capacity only (R02a major 1; R02b 3.4; R02a questions 1 and 2; R02b questions 6 and 10). R02a: "The paper never states the source, reference date or vintage of either population." R02b: "rebuild 2011 and 2025 regional populations by the same method from ABS ERP by SA2 ... on one boundary version."

**2. What the records show.** The referees are right on the premise and the records go further than they knew.

* 2025: ABS estimated resident population at 30 June 2025, ABS Data API flow `ABS_ANNUAL_ERP_ASGS2021`, on 2021 SA2 boundaries (sources register D31), allocated to the zones by residential land, CLUM class 5.4 (D47). Australia 27,608,200, 304 below the ERP of the same 2,450 SA2s (defect X108, cause not traced). None of this is in the paper.
* 2011: the thesis's own regional figures, summing to 22,326,388 (D44; `analysis/land_2011/README.md`, infrastructure row). Their source, release and allocation method are not recorded anywhere in the project.
* The like-for-like figures already exist: `analysis/population_2011/zone_population_2011.csv` gives the ERP at 30 June 2011, from the same D31 series and the same allocation as 2025, for every zone (built by `ne_vic_population.py` for B90). Nationally it gives 22,336,514, within 0.05% of the model's 22,326,388.
* Zone by zone the two 2011 figures disagree widely. Excluding North East Victoria (already corrected), 23 of 52 zones differ by more than 10%, and 12 have ratios outside 0.8 to 1.25: Western NSW 3.01 times the ERP figure, SA Arid Lands 2.955, Alinytjara Wilurara 2.564, Border Rivers Maranoa-Balonne 1.513, Desert Channels 1.509, Northern and Yorke 1.447, Border Rivers-Gwydir 1.444; Eyre Peninsula 0.719, Glenelg Hopkins 0.805, South West WA 0.807. Two of these are older-boundary zones (`analysis/land_2011/README.md`); Western NSW, SA Arid Lands and Border Rivers-Gwydir are not.
* A third copy exists that the paper does not mention: Fitzroy and Wet Tropics share 230,982 (ERRATA error 9, defect X124, not corrected; digest D1 waits on Murray).
* After the North East Victoria fix the 53 regions sum to 22,220,341 against the national 22,326,388 (audit section 9, item 2, digest D2, open for Murray).
* **Found by the referees, missed by the audit:** the general divergence above. B90 searched for exact copies; V33 (finding 1) compared only the Victorian zones. Nobody reported the column `default_over_erp` across all zones.
* **Rough reading (scratch, not a result):** I replaced every 2011 regional population in `analysis/paper_a/regional_flips.csv` with the ERP route of `zone_population_2011.csv` and kept every capacity. Short term: 22 regions over capacity in 2011 either way, and the same eight flips. Long term: 36 becomes 35, because Northern and Yorke (ERP 86,691 against a capacity of 89,933) is under capacity in 2011; it stops being a flip, leaving three. The two clean short-term flips survive (North Tasmania 143,631 against 139,165; Mackay Whitsunday 134,322 against 125,339), and so does the clean long-term flip (South West Qld 8,444 against 6,848). This ignores the infrastructure land that follows population (730 m2 a person), which moves capacity only where a zone has little non-agricultural land.
* SA Arid Lands: on the same method its population falls from 10,613 to 8,049 (24%), not from 31,361 (74%). The supplement's "both changes are matters of definition" is right, and the record can now show it.

**3. Does it change a finding?** No national headline moves: 22.3 million and the 1.49 ratio (A002, A005) hold to the printed digit on the ERP route. A031 (36 regions over capacity in 2011, long term) would become 35 and Table 1's long-term row would read 4 flips to 3 if the ERP route is adopted; the abstract does not quote either. Table 4 and Table 6 population shares (A144, A197) move at most a point. The short-term flip classification (A029, A033, A034, A036, all pending gate 4) does not move.

**4. The fair response.** Compute and reword.
* Compute: a method module like `north-east-vic-population` that sets all 53 regional 2011 populations to the ERP route (and their infrastructure land), applied in a new 2011 release; rerun `regional_flips.py`, `shocks_by_region.mjs`, `shocks_summary.py`, `long_term_and_measures.mjs`, `regions_in_depth.py`, `method_status.csv`; blind check. Inputs exist. This also settles ERRATA 9 and digest D2 without choosing which zone carries the copy. Cost on the calibrated basis (HANDOFF: about 1% of the weekly allowance per 150,000 Opus-weighted tokens; B90 and V33 together logged about 500,000): about 3 to 4% of the weekly allowance.
* Reword: a short data paragraph (or supplementary table) giving, for each year, source, reference date, series, geography and allocation; the 2011 figure stated as the thesis's regional figures, with the ERP check. Add the population test to the flip screen as a fourth column. Move the ERRATA content the paper relies on into the supplement and cite no unpublished file.
* Two defensible options: (a) adopt the ERP route for both years (recommended: one method, like for like, and it is what both referees ask for); (b) keep the thesis figures and report the ERP route as a test column. A reviewer would accept (a) readily and (b) only with the test column shown.

**5. Dependencies and conflicts.** Feeds Table 1, Table 4, Table 6, Table 7, section 7 counts and issue 7 (tier counts). Changes Tier A rows, so it goes to Murray (CARD, "always asked"). The referees agree.

---

## Issue 2. The land layer, and its identity with the livestock layer

**1. The issue.** The national land effect (-2.6 million short term, -1.2 million long term) may be a change of data definition, and the land and livestock layers may be two halves of one identity (R02a major 2; R02b 3.1; R02a question 3; R02b questions 1 and 2). R02b: "if half the livestock effect is the land artefact reversed, the attribution is wrong."

**2. What the records show.**
* Source and method are the same in both years, contrary to R02b's guess of a change of mapping product. Both years use two ABS holdings items, "Land mainly used for agriculture: crops" and "Total grazing": a five-year mean of 2005-06 to 2009-10 (four years for grazing) for 2011 and the single year 2020-21 for 2025 (`analysis/land_2011/README.md`, both tables). National cropping 305,997 to 316,499 km2 (+3%); pasture 3,639,794 to 3,318,689 km2 (-9%). The README says the pasture fall "is the ABS's ... after it changed its land-use categories in 2016". So R02a is right that part of it is definitional, and R02b is right about the ABS redesign, but the CLUM raster enters only the reserve and total area, which do not enter national capacity (`analysis/sensitivity_2025/README.md`, reserve and infrastructure bullet).
* The window differs: a five-year mean against one year. The paper does not say so.
* **The identity is real and is in the code.** The 2025 livestock yields divide 2025 output by "the 2020-21 ABS grazing area of the zone (the land layer's pasture)" (`livestock_zone.py`, line 13; line 100 sets `grazingHa` from `data/2025-land`). The 2011 yields divided each year's output by that year's grazing area, 385 to 351 million ha, mean 366 (`pipeline/yields/archive_livestock_inputs.json`). Nationally, where pasture binds, capacity is roughly area times output per hectare, so the area cancels: the walk counts the area change twice, once down in land and once up in livestock.
* **Rough reading:** 366 against 332 million ha is a ratio of 1.10, so about 10 of the livestock layer's 15 points (4.7 million on a base of 30.8 million) come from the smaller denominator, roughly 3 million, and roughly 1.5 million from output. The records hold the exact sum: land plus livestock is -2,621,910 + 4,703,257 = +2,081,347 short term and -608,748 long term (`capacity_by_cause_corrected.csv`, zone 1). This was not seen by B76, V29 or the audit.
* At regional level the identity also holds for pasture-bound zones (a zone's meat is national meat times its DSE share over its own pasture, `analysis/pasture_2025/README.md`, "What the model assumes"), so the land-definition flag (land alone over 2 or under 0.5) measures a change that the livestock layer partly reverses where pasture binds. Where cropland binds (SA Arid Lands, by `analysis/scale_curve_2025/README.md`) it does not.
* R02a's request to "re-run 2011 land on the 2020-21 classification" cannot be done as posed (there is no 2011 grazing area on the post-2016 categories), but the identity makes it largely unnecessary nationally.
* The land-source choice that does matter is documented: measuring land on the raster instead of ABS holdings would raise the 2025 short term by 17.3% (`analysis/sensitivity_2025/README.md`, ranking table). The paper does not mention it.

**3. Does it change a finding?** Yes, the attribution. A354 (land) and A357 (livestock) stand as computed, but the abstract's "Livestock, consumption and the red meat mix of the diet drove the rise" and highlight 2 read the walk as cause. On the records, land and livestock together add 2.1 million of the 8.2 million, and the two diet layers add 6.0 million (A358, A362). The conclusion's first point ("Livestock added 4.7 million ... land took away 2.6 million") needs the same treatment. National capacities (A001, A003, A007, A008) do not move. The long-term land effect (A354, -1.2 million, the "largest" long-term layer by B76) shrinks to -0.6 million when read with livestock.

**4. The fair response.** Reword, then compute.
* Reword (no cost): report land and livestock as one pair ("less recorded grazing land and more output per hectare of it: +2.1 million"), state the identity in one sentence, state the land source, items and windows for both years, and the ABS category change.
* Compute (small): split the livestock layer into an area part and an output part by running `livestock_zone.py` with the 2011 mean grazing area as the denominator, as an extra step of `decompose_corrected.mjs`; blind check. About 1 to 2% of the weekly allowance.
* Two options for R02b's (a) "national areas beside the ABS census and ABARES totals": the records already are the ABS totals (SA2 sums equal the national figures, `land_2011/README.md`), so a one-line statement answers it; an ABARES comparison adds little and is not recommended.

**5. Dependencies and conflicts.** Precedes issue 4 (any symmetric decomposition should use the split, or it will divide the identity between two layers by arithmetic). Interacts with issue 1 (infrastructure land). The referees agree; R02b goes further and is right to.

---

## Issue 3. The livestock gain: herd cycle, carcase weight and grain finishing

**1. The issue.** The livestock rise may reflect where the 2025 window sits in the cattle cycle, heavier carcases and feedlot finishing, not pasture productivity; the 2011 window is not stated (R02a major 3; R02b 3.2; R02a question 4; R02b questions 3, 4, 7 and 8). R02a: "That range, 11.9 million, is larger than the whole 2011 to 2025 change of 8.2 million."

**2. What the records show.**
* The 2011 window is recorded: five-year mean, archive years 2006 to 2010, that is 2005-06 to 2009-10 (`archive_livestock_inputs.json`; "the 2011 rows were a five-year mean", `livestock_zone.py` docstring). The paper does not state it. Its herd-cycle phase is not assessed anywhere in the records.
* R02a is right that the single-year range (43.5 to 55.4 million, `analysis/reliability_2025/README.md`) is wider than the change, and that it is on `2025-organic`. It is also unverified: A317's second route is blocked because `build_years.py` fails at 2016-17 (defect X118).
* **What the referees did not see:** windows that span a full herd cycle move the 2025 short-term base very little: 2010-11 to 2024-25 +0.9%, 2017-18 to 2024-25 +0.9%, 2015-16 to 2024-25 +0.6%, and 2005-06 to 2024-25 (which contains the 2011 window years) -0.1% (`analysis/sensitivity_2025/README.md`, ranking table, on `2025-organic`). The three-year windows are the outliers: early -8.6%, late +6.6%. And every single year 2016-17 to 2024-25 is above 2011 on the published tier ("The statement that capacity has risen does not depend on which years are chosen", reliability README). Rough reading on the corrected tier, by proportion: the single years span about 37.6 to 47.9 million, all above 33.3.
* Carcase weight and turn-off: the records show output rising with a flat herd ("cattle meat produced was 2.10 million tonnes in 2020-21 ... and 3.00 million tonnes in 2024-25 with almost the same beef herd (0.993 and 1.04 of its 2009-10 size)", reliability README). Carcase weights by year are not in the records. B81 read Wiedemann et al. (2015): carcase weight +13.5% over 30 years, and the gain "mostly feedlot finishing", with arable land for feed up from 0.2 to 1.7 million ha (B81, flags for A11.1).
* Grain finishing: R02b's premise that "the model credits all beef output to the pasture area" is partly wrong. The cattle meat yield divides meat by its share of grazing land plus feedlot grain hectares (grain over the mean grain yield) plus feedlot land per head (`pipeline/yields/livestock.py`, cattle block); feedlot grain follows cattle on feed, 720 to 1,430 thousand head (`data/2025/livestock_national_series.csv`). Pigs and poultry are charged on grain yields over a feed conversion ratio. What is right in the premise: the feedlot hectares sit inside one cattle-meat yield, so they are charged with the pasture-type product, and dairy's bought-in feed is not modelled (HANDOFF caveat on the dairy module).
* Regional class counts are the 2010 mix scaled by the state's herd change (`livestock_zone.py` docstring), so shifts within a state are not seen.
* R02b questions 7 and 8 have answers in `capacity_by_cause_corrected.csv`. North Tasmania (+48,428): livestock +27,456, crop yields +14,021, land +10,347, red meat mix -3,133; Tasmanian milk rose from 677 million litres in 2009-10 to between 887 and 961 million litres a year in 2020-21 to 2024-25 (`livestock_national_series.csv`). Mackay Whitsunday (+73,775): livestock +41,512, consumption +17,050, red meat mix +10,053, land +2,657, crop yields +2,503; pasture binds there despite the cane.

**3. Does it change a finding?** The direction of the short-term rise (A001, A003) is safe on the records; its size is not pinned to better than roughly 4 to 15 million across single years (rough reading). The driver sentence (A357) moves as in issue 2. A317 should not reach the main text until X118 is fixed.

**4. The fair response.** Rebut the strong form, compute the rest.
* Rebut, in response-letter words: "The 2011 window is the five-year mean of 2005-06 to 2009-10. Windows of 8, 10, 15 and 20 years that span the herd cycle change the 2025 short-term capacity by -0.1% to +0.9%, the 20-year window including the 2011 years; every single year from 2016-17 to 2024-25 gives a higher capacity than 2011. The direction of the change does not depend on the window; its size does, and we now report it across windows."
* Compute: (a) the full-cycle windows on `2025-fixed` (the `rebuild_off.py` and `make_win.py` route of fault X069 exists); (b) fix X118 by the same route and move the single-year series to `2025-fixed`; (c) 2011 window variants from the five archive years (three-year subsets), so both years are shown on matched window lengths. About 2 to 3% of the weekly allowance in all, plus a blind check.
* Reword: state both windows; say what grain finishing does in the model; add B81's caution that a livestock-output gain "is not free of feed-land cost" (it is not in section 11.1).
* Carcase-weight series by year: needs data Murray would fetch (ABS 7215.0 livestock products; search: https://www.google.com/search?q=ABS+7215.0+livestock+products+carcase+weight , a search).

**5. Dependencies and conflicts.** The window basis drives issue 5's ranges (the meat window explains 81% of the short-term variance). Depends on issue 2 for wording. The referees agree.

---

## Issue 4. The decomposition: order, causal language and what "consumption" is

**1. The issue.** The cumulative walk gives one ordering's answer, its interaction row is zero by construction, and "consumption" is unexplained (R02a major 4; R02b 3.1(c); R02a questions 5 and 6). R02a: "The abstract's 'Livestock, consumption and the red meat mix of the diet drove the rise' is one ordering's answer."

**2. What the records show.**
* Right: the interaction row is a sum-check residual, "0 everywhere" by design (`analysis/comparison_2025/README.md`, corrected-tier section). Only one order was run on the corrected tier.
* Missed by both referees: a second, order-free decomposition exists on the published tier (`decompose.mjs`, `capacity_by_cause.csv`): each layer applied alone to the 2011 data. Short term, land -3.18, crop yields +0.21, livestock +6.31, consumption +4.56 million on 40.45, interaction -0.35 million of +7.55 million. As shares of the starting capacity the layers are nearly the same alone as in the corrected walk (land -7.9% both; livestock +15.6% alone against +15.3% in the walk; consumption +11.3% against +11.8%). Rough reading: in the short term the order moves each layer by a few hundred thousand, not millions. In the long term the published one-at-a-time run gives a different picture (crop yields +2.4 million largest, land +0.3) from the corrected walk (land -1.2 largest), so there the tier and perhaps the order matter and nothing in the records separates them.
* "Consumption" is diet composition, not food requirement: the meat-and-egg share 13% to 12% and the red-meat share 64% to 57.8%, carried forward by FAO food supply 2010-12 against 2021-23 (beef and veal per head -34%), plus fuel, biofuel and timber settings that do not move capacity (`analysis/consumption_2025/README.md`). The red meat mix layer is the split of red meat among beef, lamb, veal and pork (beef 69.2% to 59.5%; HANDOFF). The energy need per person is unchanged. R02b's "lower per-capita consumption" is right for beef, wrong if read as less food.
* The "3.8 million and 0.4 million" split is a bookkeeping of the organic share between two layers (V29), not an order effect.
* The audit had already noted the narrative problem (V32a problem 3: "Narrative credits production, the decomposition credits diet").

**3. Does it change a finding?** The abstract and highlight driver sentence (A357, A358, A362) changes in wording; with issue 2, the honest ranking is: the diet with less beef (6.0 million), then land and livestock together (2.1 million), then crop yields (0.1 million). The long-term layer ranking (B76's "land largest") is the least secure statement and should not be headlined.

**4. The fair response.** Compute and reword.
* Compute: extend `decompose_corrected.mjs` to the reverse order and to a Shapley average. Only five layers are non-zero short term and six long term, so 32 to 64 evaluations per zone and preset; the layers change separate inputs, so subsets can be assembled. Run it after the issue 2 split. Blind check as V29. About 2% of the weekly allowance.
* Reword: drop the interaction row (both referees); give the walk order in the caption; explain consumption in one sentence; use "accounts for" rather than "drove"; cite Kitagawa (1955) or Das Gupta (1993) for the method (not in the literature register; Murray to fetch: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Standardization%20and%20Decomposition%20of%20Rates%20Das%20Gupta&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT , a library search).
* A reviewer would accept the forward walk kept in the main text with the Shapley range per layer in the table.

**5. Dependencies and conflicts.** Depends on issue 2. No disagreement between the referees.

---

## Issue 5. Uncertainty: asymmetric, missing from the headlines, and not an uncertainty analysis

**1. The issue.** The 2011 results have no range, the shocked figures and shares carry none, the Monte Carlo samples judgement choices rather than data, and input data error is not sampled (R02a major 5; R02b 3.7; R02a questions 7 and 11; R02b question 9). R02a's rough reading: "the 1-in-10 capacity at the 5th percentile would be about 26.9 million ... and the 1-in-20 capacity at the 95th percentile about 29.0 million".

**2. What the records show.**
* R02a's rough reading is exact, not rough. National shocked capacity is the average-year capacity times the national factor (`analysis/paper_a/README.md`, shocks paragraph; 41,503,537 x 0.742 = 30.8 million and x 0.634 = 26.3 million, Table 6). Every draw scales the same way, so the 2025 range at 1 in 10 is 26.9 to 34.0 million and at 1 in 20 23.0 to 29.0 million, against 27.6 million people. The abstract's "above balance in a 1-in-10 year and below it in a 1-in-20 year" holds at the base only.
* What both referees missed: the width that does this comes from the three-way meat window, which includes the two three-year windows. With full-cycle windows the short-term range on `2025-organic` narrows from 42.5 to 52.9 to 46.0 to 50.8 million (`analysis/sensitivity_2025/README.md`, fault X069 rerun), and the README itself says "A window that covers the herd cycle is the better basis for a published range". Rough reading, scaled to `2025-fixed` by proportion: about 39.5 to 43.6 million, so about 29.3 to 32.4 at 1 in 10 (above 27.6 throughout) and about 25.1 to 27.7 at 1 in 20 (below or at balance). On that basis the abstract's statement would very nearly hold. This is a reading, not a result.
* The 57% share has a range from the published figures: 13.4 to 16.5 million over 27.6, about 49% to 60%. The 69% has none.
* The project agrees the ranges are not confidence intervals: "The ranges are what we can defend ... not confidence intervals" (`sensitivity_2025/README.md`, Limits). Five judgement ends are stated in section 9.1 already.
* Data error is not sampled, as R02b says; the land-source choice (+17.3%) and the calibration of the ABS meat tables (-7.0%) are outside the ranges (same README, "What the ranges leave out").
* A paired range for the change: most of the 13 sampled choices are proxies made necessary by bringing 2011 forward (the group trend for crops the ABS stopped reporting, FAO proxies for the diet shares); they have no 2011 counterpart. Only a few apply to both years (meat window within the year's own data, the leave-one-out resilience table, red-meat share). The audit had listed this computation as open with no decision row (audit section 9, item 20).

**3. Does it change a finding?** Yes. A196 (pending gate 4) and highlight 3 must carry the range or the basis. A011 (57%) gains a range. A027 and A028 would change if the published range moves to full-cycle windows, which is a Tier A change for Murray. A009 is already worded as not a test.

**4. The fair response.** Compute and reword.
* Quick: a script over `results/ranges_2025-fixed.csv` that writes the shocked national and regional ranges for Table 6 and the share ranges for Table 4 (the numbers rule forbids typing them). Under 0.5% of the weekly allowance.
* Session-size: rerun the full Monte Carlo on `2025-fixed` with full-cycle windows in place of the three-way choice (fault X069 route), folded into the freeze run Murray's rule already plans ("run once when a paper's numbers are frozen"). About 1.5 to 2.5%.
* Optional, two defensible answers to the paired range: (a) sample the shared choices in both years with common draws (about 2 to 3%, needs a decision row); (b) say plainly that the 2011 inputs are fixed measurements and the change carries the 2025 range only. Recommend (b) plus a sentence on which choices could be shared; a reviewer will accept (b) if the abstract says the 2011 values have no range.
* Reword: "sensitivity ranges over sampled input and method choices"; the abstract says the 1-in-10 and 1-in-20 statements are at the base settings and gives the range.
* ABS relative standard errors by region (R02b): out of scope for this paper; say so in the limits.

**5. Dependencies and conflicts.** Depends on issue 3 (window basis) and issue 6 (factor). The referees agree.

---

## Issue 6. The drought allowance: a cereal factor applied to pasture and livestock

**1. The issue.** Every yield, including pasture-fed products, is scaled by a factor from wheat, oats and barley, untested for livestock, and it alone generates the bad-year findings; the trend fit and the stationarity are not shown (R02a major 6; R02b 3.3; R02a question 8; R02b question 5). R02b: "applying Victoria's 100-year factor of 0.22 to Corangamite's or West Gippsland's dairy output is not credible without evidence."

**2. What the records show.**
* Right: the factor is untested for pasture or livestock; the resilience README says so ("Pasture, livestock, horticulture ... are not in it; the factor scales all of the harvest").
* The "trend" is not a fitted trend: each year's yield over the mean of the ten observations from five before to four after; ranked ratios; anchors at 1 to 150 years (`analysis/resilience_2025/README.md`, section 1). This local reference partly answers R02b's point about mixing eras. A 1990 sub-period table has not been run.
* The fitted-tail interval for the national 100-year factor is 0.32 to 0.54 (same README, section 3); none exists for 10 and 20 years.
* **An observed partial test is in the records and neither the paper nor the referees use it.** The single-year series (`analysis/reliability_2025/README.md`, `2025-organic`, each year's crops, herds and meat) gives the 2017 to 2019 drought years near the median (2018-19 48.8, 2019-20 48.3 against a median of 48.5 million) and the low year after them (2020-21, 43.5, 0.90 of the median) as the herd rebuilt. That is the lag R02b describes, and the worst year (0.90) is milder than the national 1-in-10 factor (0.742). Eight years cannot name a return period (README, Limits), and A317 is unverified (X118).
* Missed by both referees: the 2011 and 2025 shocked figures use different tables. 2011 uses the thesis table (0.599 at 20 years), 2025 the updated one (0.634) (resilience README, section 2). Part of the 1-in-20 change from 1.12 to 1.05 (Table 6) is that table update (+5.8%), not the data.
* National findings use the Australian factor; R02b's Corangamite point applies to the regional rows of Table 6 and section 8.2, where each region takes its state's factor.

**3. Does it change a finding?** The abstract's sixth sentence and highlight 3 (A196), section 8 and Table 6 rest on the factor. The one observed check suggests the factor is harsher than the single drought year for livestock output, so if anything the 1-in-10 and 1-in-20 capacities are low, with a lagged fall the factor does not describe. No figure moves without the compute.

**4. The fair response.** Reword and compute (small); rebut nothing that is true.
* Reword: name the basis in the abstract and highlight ("a crop-yield weather allowance applied to all output"); add the single-year evidence as the only observed check; say the regional rows use state factors; say the 2011 and 2025 tables differ.
* Compute (small, about 1%): (a) a livestock-output drought test from the ABS meat tables already fetched for the window runs (back to 2005-06), the ratio of each year's output to its own ten-year reference, by the resilience method, for 2006-07, 2018-19 and 2019-20, and a lagged variant (output at trend in the drought year, reduced in the next) as R02b asks; (b) the resilience table on 1990 to 2025 only, with `resilience.py`, beside the 150-year table. Pasture-growth indices such as AussieGRASS would need Murray to fetch them (search: https://www.google.com/search?q=AussieGRASS+pasture+growth+data+download , a search). Records before 2005-06 for 2002-03 are not held.
* If the tests are not run, both referees would accept presenting the drought results as a crop-yield scenario with the abstract softened. That is the fallback.

**5. Dependencies and conflicts.** Feeds issue 5 and issue 12 (store, drought-proofing, A264, A322). The referees agree; R02b is more specific.

---

## Issue 7. The method tier and the long-term regional count

**1. The issue.** The long-term count of regions over capacity in 2025 is 36, 32 and 36 by tier, so the corrected tier is "the outlier" and "the long-term 'net fall of 4' may be largely a tier effect"; the reporting tier is not justified; the tier is not a flip test (R02a major 7; R02a question 9).

**2. What the records show.**
* The 2025 counts are right (Table S4; `analysis/paper_a/method_status.csv`).
* The inference is wrong. R02a compares 2025 on the published and improved tiers with 2011 on the corrected tier. Like for like, the 2011 long-term counts are 39 (published), 36 (corrected) and 38 (improved) (`method_status.csv`, 2011 rows), so the fall from 2011 to 2025 is 3, 4 and 2 regions on the three tiers. The corrected tier is lowest in both years; it is not an outlier in the change. Caveat: the 2011 rows of `method_status.csv` were not rerun on `2011-fixed-2` (audit section 9, item 19); North East Victoria is over capacity in the long term on any population, so the long-term counts are unaffected.
* The reason for the corrected tier is a standing decision: "Results paper (A): 2011 to 2025 by region, on the corrected releases" (`qa/CARD.md`), because the corrected tier fixes errors against the thesis's own sources with no judgement, while the improved tier adds judgement-based changes (HANDOFF, release chain). The paper does not say this; it points to the companion paper.
* The tier test of the flips was already listed as an open computation (audit section 9, item 20). The paper names the two known cases (Corangamite, Mackay Whitsunday).
* The module interactions (-2.88 and +3.20 million, section 9.2) are right as stated.

**3. Does it change a finding?** No. Section 7.3's count (A031, 36 to 32) stands, subject to issue 1. The "cropping belts feed themselves" narrative is about named regions with ratios of 0.12 to 0.26, not about the six tier-sensitive regions.

**4. The fair response.** Rebut and reword, plus a quick compute.
* Rebut, in response-letter words: "Taken within each tier, the long-term count falls on all three: from 39 to 36 regions on the published method, 36 to 32 on the corrected and 38 to 36 on the improved. The corrected tier is lower in both years; the fall is not a tier effect. We now report the long-term counts on all three tiers in both years."
* Reword: one paragraph in section 2 on why the corrected tier reports (errors corrected without judgement; the improved tier as a sensitivity).
* Compute (quick, about 0.5 to 1%): rerun `method_status.csv` on `2011-fixed-2` and add the tier as a fourth flip test, per region.

**5. Dependencies and conflicts.** Follows issue 1. Only R02a raises it.

---

## Issue 8. Population projections set up in the introduction and not used

**1. The issue.** Section 1.1 quotes the Intergenerational Reports and the 2025 Population Statement but never sets capacity against projected population; Davies and McDonald are not connected to results (R02a major 8; R02a question 10; R02b minor 3).

**2. What the records show.** Right. The projections are read (L228: 28 million by the end of 2025-26 and 41 million by 2065-66, Table 1, p. 1; Treasury 2023, 40.5 million in 2062-63). The 2025 short-term capacity (41.5 million) is almost exactly the 2065-66 projection, as R02a says. No projection is used after section 1.1. McDonald (2017) is about employment, as the paper itself says.

**3. Does it change a finding?** No finding moves; a sentence is added or section 1.1 is cut.

**4. The fair response.** Two defensible options.
* (a) Compute a short national paragraph (recommended): capacity at the base and at 1 in 10, with the issue 5 ranges, against the Statement's medium path and the Intergenerational Report's projection, with vintage and assumptions, and the plain caveat that capacity is held at 2025 data. Small, about 0.5% (the dates come from L228 Table 1 by a script, not by hand). Regional projections on NRM geography are out of scope: say so, since no official projection series is published on these zones.
* (b) Cut section 1.1 to what the paper uses.
* Either way cut McDonald and shorten Davies (both referees). A reviewer at this journal would favour (a).

**5. Dependencies and conflicts.** Uses issue 5's ranges. R02b only wants the cut, which (a) also does.

---

## Issue 9. The scale curve as a property of the model's fixed-proportion rule

**1. The issue.** The scale loss follows from the asymmetric substitution rule and the partition, not from Australian land as such; the 37% has no basis named; the cropland-share test sits oddly beside Lane (2014, p. 3); the random grouping rests on five draws (R02a major 9; R02b 3.5).

**2. What the records show.**
* Right on the mechanism; the paper's own section 6 and S2 say it ("Capacity was exactly proportional to land"; the loss "is entirely the mismatch of crop and pasture land between units", `analysis/scale_curve_2025/README.md`).
* Right on five draws (S2; scale_curve README, "five draws each").
* Partly answered already: a relaxation of the rule exists. Moving dairy onto cropland at observed dairy-farm yields takes the SA2 sum from 37% to 40% of the unchanged national capacity (`analysis/pasture_2025/README.md`, `two_pool.csv`). The scale loss survives it.
* R02b's premise that monogastric meat should be "allocated explicitly to cropland" is already the model: pigs, poultry and fish are grain yields over feed conversion ratios (`livestock.py`, docstring and last block).
* R02b's point that arid pasture "carries little food in any case" is partly met: the model's arid yields agree with ABARES beef receipts by region (SA Northern Pastoral 0.24 against 0.19; `pasture_2025/README.md`, "Regions, not states"). The loss arises because the pasture area is very large, not because its yield is credited too high.
* Lane (2014, p. 3) reconciles directly: the diet needs about 141,000 km2 of food cropland against 3.63 million km2 of cropland and pasture (section 6), so cropland only binds below a share of a few per cent. The national test starts at 10%. Regions such as SA Arid Lands (221 km2 of cropland to 326,000 of pasture) sit far below, which is where cropland share decides capacity. The paper quotes both statements back to back without saying this.
* Improved pasture area by zone is held (`data/2025/pasture_quality_by_zone.csv`), a start on R02b's "pasture area by productivity class".

**3. Does it change a finding?** A088 (37%) stands; the abstract must name its basis and mechanism. Highlight 5 likewise. The rough size of the rule's effect on record: 3 points at SA2 under the dairy relaxation.

**4. The fair response.** Reword, plus a small compute.
* Reword: abstract "37% on state yields (54% on each unit's own yields), a consequence of the model's rule that cropland can carry pasture products but not the reverse"; one sentence reconciling Lane (2014, p. 3); report the dairy-on-cropland sensitivity in S2.
* Compute (about 1%): 200 or more random groupings at each level with `ideal_split_test.mjs`, on the basis chosen in issue 10; the cropland-share test for three or four regions; a pasture-by-class table from the file above.
* Rebut the monogastric point in one sentence.

**5. Dependencies and conflicts.** Shares the random-grouping run with issue 10. No disagreement; R02b asks for more sensitivity.

---

## Issue 10. Three yield bases make sections 5 and 8 hard to follow

**1. The issue.** 33%, 44% and 63% for the same 53 regions, 54% and 58% for the same SA4s, a 2011 reference of 30.7 against 33.3 million; one basis should lead (R02b 3.6; R02a major 9, last point; R02a abstract paragraph).

**2. What the records show.** Right on the count of figures (Table 3; S2; section 8.2). The national yield vector (33%) appears only because the random grouping was run on it (scale_curve README, "How good could a split be?"). The two main bases are deliberate bounds: "the state basis ignores local yield differences (conservative) and the dominant-zone basis gives each SA unit the yields of one zone (generous for units that span several). The truth for SA2 lies between" (scale_curve README). The local basis is not consistent across levels, which is why the curve uses the state basis.

**3. Does it change a finding?** No values; the abstract's 37% gains its pair (A088, A098).

**4. The fair response.** Two defensible options.
* (a) Keep both bases as bounds, name both wherever one appears, put the national yield vector in the supplement only, and rerun the random groupings on the state basis (recommended: it keeps what the README shows is true, that neither basis is the answer).
* (b) R02b's: local basis in the main text, others in the supplement. Accepting (b) outright would drop the conservative bound and present the generous one alone.
* A reconciling table of all bases in the supplement satisfies both referees. Cost shared with issue 9.

**5. Dependencies and conflicts.** R02b prefers the local basis; R02a asks only for one basis named. Recommendation (a) with a reconciling table meets both.

---

## Issue 11. Not self-contained: Table S1, the model, the data, the figures and Paper B

**1. The issue.** Table S1 is "not built", section 2 points to a model description the supplement does not hold, data sources are never listed by source and year, figures are placeholders, and the failure probability and Monte Carlo come from an unpublished companion paper (R02b 3.8; R02a major 10, first point; R02a major 2, Table S1; R02a minor 11; R02a minor 20).

**2. What the records show.** All right. Table S1 is a placeholder (supplement; drafter note 7; N-A2, decision 66). Section 2 says "The full model ... are in the supplementary information"; the supplement holds regional detail only. Figures 5 and 6: "no plotting script exists". Decision 99 already plans the figures by script. The archive DOI waits on the Zenodo hold (decision 96). The sources register holds every data source with origin and date (D31, D44, D46, D47, D51 and others), so the data table can be generated.
* The failure probability can be derived here in one line from the paper's own numbers: balance needs a factor of 27.6/41.5 = 0.665, which lies between the 10-year (0.742) and 20-year (0.634) anchors; straight-line interpolation, the table's own rule, gives about 1 in 17, about 5.8% a year. No dependence on Paper B is needed.
* The submission order is a standing decision: the methods paper goes first (`qa/CARD.md`), so Paper B can be cited as submitted, with a preprint.

**3. Does it change a finding?** No.

**4. The fair response.** Compute (small) and reword.
* Build Table S1 by script from `results/2011-fixed.csv` and `results/2025-fixed.csv` settings columns; a data-source table generated from the sources register; a short model summary in the supplement with a pointer to Lane (2014), Lane et al. (2014) and the repository. About 1 to 2%.
* Derive the failure probability in section 8.1 as above; describe the Monte Carlo in four sentences here (Latin hypercube, 1,000 draws, 13 choices, the five judgement ends) and cite Paper B as submitted.
* Figures per decision 99. The DOI per decision 96 (Murray).

**5. Dependencies and conflicts.** The data table is where issue 1 and issue 2's source statements go. The referees agree.

---

## Issue 12. Claims for measures stronger than the evidence

**1. The issue.** The abstract presents one-at-a-time, cost-free model settings as measures that "widen the margin"; a livestock-output gain has no mechanism; the store is free; the feed grain figure is a 2050 scenario value (R02b 3.9; R02a abstract paragraph; R02a minor 14).

**2. What the records show.** Right. Section 11.7 and S6 concede one at a time, no cost, no feasibility; "The store is free in the model" is in 11.4, not the abstract. The 303 kg a person is "a 2050 base-case figure of Foran and Poldy (2002) applied here to the 2025 population", not printed in the source but derived (drafter notes; L007). One point both referees miss: the store's capacity effects (+48%, +64%) come from the resilience tables of a population holding a store (`analysis/resilience_2025/README.md`, section 6) and do not use the 303 kg; only the 11.5 Mt tonnage sentence does. B81 had flagged that a livestock gain is mostly feedlot finishing and "not free of feed-land cost"; the draft omits it.

**3. Does it change a finding?** The abstract's last sentence and A275, A264, A322 in wording only; the store percentages stand.

**4. The fair response.** Reword: "In the model, the settings that move capacity most are ..."; the abstract says one at a time and free of cost; 11.1 adds the feed-land caution and the feedlot pathway; 11.4's tonnage uses current feed grain use or is cut. Current feed grain use needs Murray to fetch an ABARES figure (search: https://www.google.com/search?q=ABARES+domestic+feed+grain+use+Australia , a search). Quick.

**5. Dependencies and conflicts.** Depends on issue 6 (stores and drought-proofing rest on the factor). The referees agree.

---

## Issue 13. Literature and references

**1. The issue.** Little engagement with the carrying-capacity literature and with Australian land-use outlook work; no ABS population source; no small-area estimation literature; no source for the organic penalty; a cited work missing from the list; seventeen listed works not cited (R02a major 10; R02b 3.10; R02a minor 17; R02b minor 16).

**2. What the records show.**
* Cohen (1995), Price (1999) and Seidl and Tisdell (1999) are held and read (L049, L048, L045), used by Paper B; adding a paragraph to Paper A is cheap. Bryan et al. (2016, L076), Grundy et al. (2016, L135) and the Australian National Outlook (L090, L100) are held.
* The organic penalty has a source in the records, contrary to R02b: Ponisio et al. (2015) 0.808 (0.771 to 0.845), Kniss et al. (2016) 0.80, Seufert et al. (2012) about 0.75 (`analysis/organic_2025/README.md`). The paper does not cite them.
* CSIRO and University of Queensland 2025 (L010) is read and cited in section 1.1 but missing from `references.md`: a gap in the reference build.
* The seventeen uncited entries are confirmed by the drafter notes ("Scope sources not cited, to keep section 11 within its budget"); they entered the list because the claims files name them (decision 98).
* `references.md` carries 20 "[CHECK]" entries (R02b says 19).
* Wilson and Rees (2005), Kitagawa or Das Gupta, and AussieGRASS are not in the register.

**3. Does it change a finding?** No.

**4. The fair response.** Reword and add: a short paragraph placing the paper in the carrying-capacity debate (Cohen, Price, Seidl and Tisdell); Bryan and Grundy in section 1; Ponisio and Kniss at the organic setting in section 7; D31 cited as the ABS population source; L010 into the list; the uncited entries cut from the list by rebuilding it from the cited text; the [CHECK] fields completed. Acquisitions for Murray: Wilson and Rees 2005 (https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,Recent%20developments%20in%20population%20projection%20methodology%3A%20a%20review&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT , a library search). About 1% of the weekly allowance for the reading and the reference rebuild.

**5. Dependencies and conflicts.** Issue 4's citation; issue 6's data. The referees agree.

---

## Issue 14. Presentation: release codes, terminology, length of sections 10 to 12

**1. The issue.** Release identifiers and file paths in nearly every paragraph; "people over capacity" reads as a count; "short term" and "long term" are presets, not horizons; the title's "corrected releases" is jargon; sections 10 to 12 mix results, literature and policy (R02a major 11; R02b 3.8, first point; both abstract paragraphs).

**2. What the records show.** Right. The ratio convention ("people over capacity, above 1 is over") was set across both papers (decision 87); its label can change without changing the convention. The presets carry the thesis's and Lane (2017)'s names in this journal.

**3. Does it change a finding?** No.

**4. The fair response.** Reword.
* Plain labels ("2011 data, corrected method") defined once in a table in section 2; release codes and paths to the data availability statement; "population-to-capacity ratio" for the measure.
* Presets, two options: (a) keep "short term" and "long term" with a one-line definition in section 2 and the abstract (recommended: continuity with Lane 2017 in the same journal); (b) rename to "current conditions" and "100-year plan". A reviewer would accept (a) if the definition is in the abstract.
* Title: drop "on the corrected releases". Shorten section 12's literature summaries. Quick to small, a Sonnet edit, about 0.5%.

**5. Dependencies and conflicts.** None. The referees agree.

---

## Issue 15. The abstract and highlights

**1. The issue.** Both referees find the national numbers accurate (R02a checked 1.49, 1.50, 69%, 57% and the 1-in-20 status; R02b reproduced Table 2 and Table 6) and four overreaches: the driver sentence, the 1-in-10 and 1-in-20 sentence, the 37% without basis, and the measures sentence; R02a adds that "a bound, not a policy goal" does not follow from the 37% and that "population changes status only" is true by construction (R02a section 6; R02b section 6).

**2. What the records show.** All four are right, and issues 2 and 5 show the first two are worse than the referees thought. "Therefore" in the abstract links the 37% to section 12.1's literature argument, which does not rest on it. "Population changes status, not capacity" is the model's construction (`analysis/comparison_2025/README.md`: "Population does not enter capacity"). Highlight 4 is accurate (R02b).

**3. Does it change a finding?** Wording of A357, A358, A362, A196, A088, A275 in the abstract and highlights.

**4. The fair response.** Reword. A sketch of the four sentences, for Murray's wording: "Most of the rise came from a diet with less beef in it; more meat and milk per hectare of a smaller recorded grazing area added the rest." "At the base settings capacity is above the population in a 1-in-10 year and below it in a 1-in-20 year, on a weather allowance drawn from cereal yields; across the 2025 sensitivity range both are close to balance." "When every SA2 must feed itself, their capacities sum to 37% of national capacity on state yields and 54% on local yields, because in the model cropland can carry pasture products but pasture cannot carry crops." "One at a time and free of cost in the model, the settings that move capacity most are ...". Drop "therefore". Highlights: the same, plus one regional result (R02a), within 85 characters (decision 97).

**5. Dependencies and conflicts.** Depends on issues 2, 4, 5, 6, 9 and 12. The referees agree.

---

## (a) All issues

Cost is the anticipated share of the weekly allowance on the calibrated basis (HANDOFF: about 1% per 150,000 Opus-weighted logged tokens; CARD calibration for worker lengths), including a blind check where a computation changes a figure. "Quick", "small", "session-size" as the house rule asks.

| No. | Referee(s) | Verdict on the premise | Response type | Headline effect | Cost |
|---|---|---|---|---|---|
| 1 | R02a 1; R02b 3.4 | Right, and wider than they knew (23 of 52 zones off by more than 10%; error 9) | Compute and reword | None national; 2011 long-term count 36 to 35, long-term flips 4 to 3 (rough reading); short-term flips unchanged | Session-size, 3 to 4% |
| 2 | R02a 2; R02b 3.1 | Right on definition (ABS 2016 categories); wrong on a change of mapping product; identity confirmed in code | Reword, then compute | Driver sentence: land and livestock together +2.1 M, not livestock +4.7 M | Reword quick; compute small, 1 to 2% |
| 3 | R02a 3; R02b 3.2 | Partly right: window not stated, range on another release, carcase and feedlot unseparated; wrong that the cycle may explain the rise (full-cycle windows -0.1% to +0.9%) | Rebut in part, compute | Direction safe; size spans roughly 4 to 15 M across single years (rough reading) | Small to session-size, 2 to 3% |
| 4 | R02a 4; R02b 3.1(c) | Right; an order-free run on the published tier shows small short-term order effects; consumption is diet composition | Compute and reword | Driver ranking: diet 6.0 M, land with livestock 2.1 M | Small, 2% |
| 5 | R02a 5; R02b 3.7 | Right; R02a's rough shocked range is exact; the width comes from the three-year windows | Compute and reword | 1-in-10 and 1-in-20 statements hold at base only (26.9 to 34.0; 23.0 to 29.0 M); 57% becomes 49% to 60% | Quick for shocked ranges (under 0.5%); full-cycle Monte Carlo 1.5 to 2.5% |
| 6 | R02a 6; R02b 3.3 | Right that it is untested; the one observed check suggests the factor is harsh for a single year and misses the lag; 2011 and 2025 tables differ | Reword and compute | Abstract sentence 6 and highlight 3 name their basis | Small, about 1% |
| 7 | R02a 7 | Counts right, inference wrong: falls of 3, 4 and 2 within each tier | Rebut, reword, quick compute | None | Quick, 0.5 to 1% |
| 8 | R02a 8; R02b minor 3 | Right | Compute (national paragraph) or cut; regional projections out of scope | None | Small, about 0.5% |
| 9 | R02a 9; R02b 3.5 | Right on mechanism and draws; monogastric premise wrong; dairy relaxation already on record (37% to 40%) | Reword and small compute | 37% named with basis and mechanism | Small, about 1% |
| 10 | R02b 3.6; R02a 9 | Right on confusion; the two bases are bounds by design | Reword (both bases as bounds), compute shared with 9 | None | Shared with 9 |
| 11 | R02b 3.8; R02a 10, 2 | Right | Compute (S1, data table, summary) and reword (derive failure probability here) | None | Small, 1 to 2%; figures per decision 99 |
| 12 | R02b 3.9; R02a abstract | Right; store percentages do not use the 303 kg | Reword | Abstract last sentence | Quick |
| 13 | R02a 10; R02b 3.10 | Right except the organic penalty, which has a source | Reword and add | None | About 1%, plus Murray's fetches |
| 14 | R02a 11; R02b 3.8 | Right | Reword | None | Quick to small, about 0.5% |
| 15 | Both, section 6 | Right, and issues 2 and 5 make two points sharper | Reword | Abstract and highlights | Quick |

All computations together: roughly 17 to 25% of the weekly allowance, most of it issues 1, 3, 4 and 5. Every change that moves a Tier A value comes to Murray first (CARD).

## (b) The changes that would do most to satisfy both referees, in order

1. Rewrite the driver statement in the abstract, highlights, section 4 and the conclusions so that land and livestock are reported together (+2.1 million) and the diet with less beef in it (+6.0 million) is named as the largest part, with the identity stated and a Shapley range per layer.
2. Carry the sensitivity range into every shocked figure and share, rerun the published range on full-cycle meat windows, and state that the 1-in-10 and 1-in-20 findings hold at the base settings on a cereal-based allowance, with the single-year drought evidence beside it.
3. Put both years' populations on the ABS 30 June ERP footing by the same allocation, state source, date and series, and add a population test to the flip screen (the records already hold the 2011 figures for every zone).
4. Make the paper self-contained: Table S1, a data-source table for both years, a model summary, the failure probability derived here, plain labels in place of release codes.
5. Name the yield basis and the substitution rule with every scale figure, report the 2011 and 2025 windows and land items, and say what grain finishing and the drought factor do in the model.

## (c) Where accepting the criticism would be wrong

* Conceding that the long-term fall in regions over capacity is a tier effect would be wrong: within each tier the count falls by 3, 4 and 2 regions (`method_status.csv`).
* Conceding that the herd cycle may explain the rise would be wrong: full-cycle windows move the 2025 base by -0.1% to +0.9% and every single year 2016-17 to 2024-25 exceeds 2011 (sensitivity and reliability READMEs).
* Conceding that the land layer changed mapping product (ABARES or ALUM versions) would be wrong: both years use the same two ABS holdings items, and the raster enters only reserve and area, which do not move national capacity.
* Conceding that the model credits pig, poultry and feedlot output to pasture would be wrong: pigs and poultry are charged on grain yields, and feedlot grain hectares are in the cattle-meat yield (`livestock.py`).
* Conceding that the organic penalty has no source would be wrong: Ponisio et al. (2015) and Kniss et al. (2016) set it (`analysis/organic_2025/README.md`); the paper should cite them.
* Conceding that NRM boundaries differ between the years would be wrong: both years are on the 2011 NRM polygons, and only five zones' 2011 data carry the older overlay areas (`analysis/land_2011/README.md`).
* Conceding that a paired Monte Carlo is straightforward would be wrong: most sampled choices are 2025 proxies with no 2011 counterpart, so mirrored draws would invent a 2011 uncertainty.
* Conceding R02b's local basis as the sole main-text basis would be wrong: the README shows the two bases are the conservative and generous bounds, and the truth lies between.
* Conceding the export share is "by value" would be wrong: ABARES gives 71% by volume, p. 5 (L234).
* Conceding a length overrun would be wrong: the main text is 7,850 prose words by `qa/tools/wordcount.py A` (tables and captions excluded), under the 8,000 of decision 92.
* Conceding that the 2021 Intergenerational Report claim lacks a page would be wrong: the draft cites p. 13, the printed page found on disk (drafter note 5).

## (d) Questions to the author, with answers from the records

From R02a:

1. Which population series? 2025: ABS ERP at 30 June 2025, flow `ABS_ANNUAL_ERP_ASGS2021`, 2021 SA2s (D31). 2011: the thesis's regional figures, source and vintage not recorded; whether preliminary or rebased **needs Murray**. The same ERP series gives 22,336,514 for 30 June 2011.
2. How allocated, and how large the effect of one method? 2025 by residential land (D47); 2011 unrecorded. On the ERP route for 2011 (`zone_population_2011.csv`), no short-term status changes and one long-term flip goes (Northern and Yorke), a rough reading.
3. How much of the -2.6 million land effect survives one classification? Nationally most of it is handed back by the livestock layer, which divides output by the same grazing area; land and livestock together add +2.1 million. Not computed exactly.
4. What livestock window for 2011, and a cycle-matched change? 2005-06 to 2009-10, five-year mean; cycle phase not assessed; full-cycle 2025 windows move the base -0.1% to +0.9%. A matched pair **needs a computation**.
5. A Shapley decomposition? Not run; the published-tier one-at-a-time run suggests short-term layers move by a few hundred thousand.
6. What is the consumption layer? Diet composition from FAO food supply: meat and eggs 13% to 12%, red meat 64% to 57.8% (beef per head -34%); food requirements unchanged.
7. Do the 1-in-10 and 1-in-20 findings hold at the 5th and 95th percentiles? No: 26.9 to 34.0 and 23.0 to 29.0 million against 27.6 (exact scaling).
8. Any evidence that pasture-fed output falls by the cereal factor? Only the single-year series: drought years near the median, the low year after them at 0.90 (published tier, unverified A317).
9. Why the corrected tier? A standing decision (CARD): it corrects errors against the thesis's own sources without judgement.
10. When does the projected population reach the capacities? Not computed; the Statement's 41 million in 2065-66 is about the 41.5 million short-term capacity; dates **need a small computation**; regional projections out of scope.
11. Can 2011 be sampled? Only for the few shared choices; **needs Murray** (audit section 9, item 20).

From R02b:

1. Land sources and areas? ABS holdings "crops" and "total grazing": 2005-06 to 2009-10 mean against 2020-21; cropland 305,997 to 316,499 km2, pasture 3,639,794 to 3,318,689 km2; these are the ABS totals.
2. Yields as output over the same area? Yes (`livestock_zone.py`, lines 13 and 100); size of the cancellation not computed, roughly two thirds of the livestock layer.
3. 2011 window and herd, slaughter and carcase comparison? 2005-06 to 2009-10; beef herd 0.993 to 1.04 of 2009-10 in 2020-21 and 2024-25, cattle meat 2.10 to 3.00 Mt; carcase weights **need data** Murray would fetch (search: https://www.google.com/search?q=ABS+7215.0+livestock+products+carcase+weight , a search).
4. Grain-finished beef and dairy feed? Feedlot grain hectares and feedlot land are in the cattle-meat yield; pigs and poultry on grain; dairy bought-in feed not modelled.
5. Factor against observed output, and a lagged variant? Not run; the single-year series shows the lag; **needs a computation**.
6. Why does SA Arid Lands fall by three quarters? The 2011 figure is the thesis's (2.955 times the ERP route); on one method it falls 24% (10,613 to 8,049); no short-term flip changes.
7. North Tasmania's gain? Livestock +27,456, crop yields +14,021, land +10,347; Tasmanian milk 677 to about 900 million litres; the model has no water limit, so irrigation enters only through observed yields.
8. Mackay Whitsunday? Livestock +41,512 of +73,775; crop yields +2,503; pasture binds there in the short term.
9. Can 2011 be sampled? As R02a question 11.
10. Boundary version per region? All 53 on the 2011 NRM polygons in both years; five zones' 2011 data carry the 2010 overlay areas (Desert Channels, SA Murray Darling Basin, Alinytjara Wilurara, Swan, Northern and Yorke).

## (e) Minor issues, grouped by kind, with the fix for each kind

* **Numbering and structure** (R02a minor 1, 13; R02b minor 1, 19): renumber section 1 (1.1 to 1.4); state the selection rule precisely (decision 22 names the regions; section 10 gives the types), naming the Murray and Murrumbidgee-ACT pair as one type; move Figure 8 to the supplement since its conclusion is not re-tested. Quick.
* **Precision and units** (R02a minor 7, 21; R02b minor 6, 7, 10): two decimals for ratios and one precision per row in Tables 4 and 6; km² in place of km2; units for every Table 5 setting (fibre in kg a person a year; timber in m3 a person; infrastructure in m2 a person; reserve as a share); one sentence on what the biofuel share is of. Quick.
* **Definitions and clarity** (R02a minor 2, 4, 5, 6, 10, 12, 15; R02b minor 8, 9, 13, 14, 17, 18): define the ratio algebraically; say in Table 1's note that categories overlap and add a per-region flip table to the supplement; drop the interaction row of Table 2; explain the meat-share non-linearity in one sentence (capacity rises with meat until pasture is used, then falls as cropland is drawn into grazing; `scale_curve_2025/README.md`); one form "population X against capacity Y"; say Desert Channels carries both flags; say what share of total waste the 6% setting covers; "57% above domestic food use"; national against regional pasture use; one sentence on the module interaction; rename the 15.5 million cross-reference. Quick.
* **Source checks** (R02a minor 3, 16; R02b minor 4, 5, 11, 12): the Treasury page and the ABARES "by volume" are already right (rebut); Soliman Hunter has no printed pages, cite the section or "unpaginated"; state the crop window (2022-23 to 2024-25; "two very good winter-crop years" are 2022-23 and 2024-25, `comparison_2025/README.md`), which answers R02b's ABARES point; give Anderson et al.'s Australian finding alone; reconcile or cut the export-inclusive paragraph (decision 46 already confines it to section 8). Quick.
* **References** (R02a minor 17, 18, 19; R02b minor 15, 16): rebuild the list from cited text only; add L010; match suffixes (Hughes 2022a, Grafton 2018b, Röös, n.d., FAOSTAT, DCCEEW); complete the 20 [CHECK] fields; check Bolleter's year against its 2019 DOI. Small.
* **Supplement and data** (R02a minor 8, 9, 11, 20; R02b minor 2, 20): name which release supplies each Table 6 column (`2011-fixed` and `2011-fixed-2` are identical nationally); state the ASGS 2021 edition and why the counts are 89, 336 and 2,450 (the record names the 2021 SA2s, D31, but not the SA4 and SA3 counts: a one-line check); the failure probability derived here (issue 11); the DOI by decision 96; word count already 7,850; one spelling of each region name with a state list in the supplement. Quick to small.

## (f) Register rows touched

None (claims, sources, literature, defects).

**Wrong-value check:** *Example of a response that would concede something the records show to be false (marked as an example, not to be used):* "We accept that the long-term fall in regions over capacity is an artefact of reporting the corrected tier; on the published and improved methods there is no fall between 2011 and 2025." The records show a fall on every tier: 39 to 36 (published), 36 to 32 (corrected) and 38 to 36 (improved), `analysis/paper_a/method_status.csv`.
