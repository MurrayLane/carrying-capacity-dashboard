# R05b: a reasoned response plan to the second-round referee reports on Paper B (methods)

Brief: `qa/briefs/R05b_response_plan_B.md`. Reports answered: `qa/reports/R04c_rereview_B_ecological_economist.md` (called EE below) and `qa/reports/R04d_rereview_B_modeller.md` (called Mod). Draft tested: `papers/B_methods/draft/paper_B_draft1.md`, `supplementary.md`, `highlights.md`, `references.md`, as assembled after B129. First-round plan read: `qa/reports/R03b_response_plan_B.md` (called R03b; its issues are cited as "R03b issue n"). Decisions read: `qa/DECISIONS.md`, rows 100 to 132 in full, and 5, 33, 35, 113, 118 and 122 for what they rule in or out. No file other than this report was changed. No register row was touched.

**How to read this.** Each block tests a referee's premise against the records, says which headline claims would move and by how much, gives the fair response, and says whether the issue is (i) new, (ii) a first-round issue the revision answered and the referee did not accept, or (iii) a first-round issue the revision did not reach. Where I computed something to test a premise, I did it in my scratch folder from committed csv files only (`harmonised_comparison.csv`, the closed form in `analysis/pasture_2025/B114_pairing_relaxed_report.md`, and Table S7), and I mark it "scratch": those figures are an analyst's reading, not registered claims, and each needs a builder and a blind check before it enters the paper. My scratch script reproduces the paper's 4.1%, 38.5%, -4.9%, 16.0%, -8.6% and 31.8% exactly before any variant is run.

**Cost basis.** Costs are shares of the weekly allowance on the HANDOFF basis (about 1% per 150,000 Opus-weighted logged tokens; logged tokens are counted at face value, as R03b did, so Sonnet jobs are if anything overstated). Comparable logged jobs (`qa/spend.csv`): B113 both lines 150,389 tokens (1.0%) and its check V39 134,430 (0.9%); B114 pairing 223,830 (1.5%) and V40 151,509 (1.0%); B115 Monte Carlo 284,366 (1.9%) and V41 170,106 (1.1%); B116 bases and intake 320,428 (2.1%) and V42 241,271 (1.6%); B130 improved draws 193,288 (1.3%) and V46 177,925 (1.2%); B126b patch of Paper B 412,098 (2.7%); V45b blind read of Paper B 349,942 (2.3%); one referee report about 143,000 (1.0%).

**Abstract and highlights.** Abstract sentences are numbered as `B_s01-03_claims.csv` numbers them: s1 the span (B005); s2 five methods plus the model read two ways, "checked ... reproduce them in part"; s3 "about 65 to 211 million, about 1.6 to 5 times ... in world-average hectares, 134 to 343 million, about three to eight times" (B156, B247); s4 "depends on where the line between input and method is drawn"; s5 4.1% and 38.5%, "narrowed that spread by about a third" (B276, B277); s6 81.7 against 41.5 (B352); s7 "Weather and waste take the model from 18.9 to 55.3 million" and 1.58 (B003, B187); s8 "no single method serves every purpose"; s9 the reporting advice. Highlights H1 to H5 in the order of `highlights.md`.

**The short answer.** The revision answered the first round's computing requests: both classifications with three references and reference-free measures (B113), the pairing relaxed (B114), a widened Monte Carlo with total-order indices (B115, B130), the bases, fidelity and intake tables (B116). Both referees accept the direction of each and ask for the next step on it, so most second-round issues are type (ii). Three things in the records answer more of the second round than the paper shows: the footprint's own-productivity reading at the binding land type (53.9 to 77.9 million, B270) is computed and registered; the drought allowance's crop-only bound (B112) shows that the 18.9 million and the 5.8 to 6.1% failure probability come almost wholly from applying a cereal factor to pasture-fed output, which Paper A says and Paper B does not; and the files whose captions say "needs regenerating" have been regenerated (B127, B131). My scratch robustness reading says the line (a) share is near zero on every variant tried (about -1% to 7%), and the line (b) share moves from about 28% to 46% to the model but to about 9% to 36% to the median of the method centres, and to 10.5% without the footprint and HALF. Two referee premises are mistaken on the records: that the land-use source matters although "the two land bases agree to 0.01 Mha" (the 0.01 Mha is FAOSTAT against the ABS holdings; the second land source in the Monte Carlo is the ABARES raster, which counts cropland the holdings do not), and that pasture productivity is outside the uncertainty analysis (in this model pasture output is national meat output shared by dry sheep equivalent, and the meat window and meat calibration that set it are drawn; the supplement's list of undrawn choices says otherwise, which is the paper's error, not the referee's).

---

## Issue 1. The world-average reading is a units mismatch, not the footprint's reading; the two lines are not symmetrical

**1. The issue.** The footprint's world-average reading divides actual hectares by world-average hectares, which its own accounting does not do, so line (b) is the footprint as its authors intend and line (a) a counterfactual, and the abstract should not report the world-average range as the aggregate methods' reading (EE M1, EE minor 1, EE Q1; Mod M1 in part, on HALF).

EE: "Under the footprint's own accounting, that ratio is not defined ... What the paper calls line (b) ... is therefore not an alternative classification but the footprint as its authors intend it." Mod: "On line (b) it becomes 76.0 million only after a further conversion to Australian productivity that HALF's authors never make. In that case the reading belongs to the converter, not the method."

**2. What the records show.** EE is right on the footprint and partly mistaken on the abstract; EE minor 1 is right; Mod is right on HALF.
* The project's own README agrees with EE: the world-average rows of `cross_method_local.csv` are labelled "secondary (a counterfactual: world-average hectares divided into Australia's physical hectares)" (`analysis/method_tests_2025/README.md`, section "Both classifications"). Section 4.5 of the paper cites Wackernagel et al. 1999 (pp. 377, 380, 386) for both sides in world-average hectares. The paper's Table 3 heads the column "Reading in world-average hectares" without the word counterfactual.
* EE says the abstract and section 7.6 "still lead with" the world-average range. They do not: under decision 106 both lead with the own-productivity range (65 to 211 million, 1.6 to 5 times) and give the world-average range second. What is true is that the world-average range is attributed to "the aggregate methods".
* EE minor 1 is right: the secondary aggregate range starts at 133.8 because `harmonised_lines.py` takes the energy and protein balance's primary rows into the secondary group (`sel_w`, rows not in the footprint or HALF); the energy balance has no world-average reading (Table 3, "none: counts Australia's own production"). The footprint's world-average range on 2021-23 yields is 146.2 to 343.4.
* EE Q1, how crop and pasture are pooled: as raw world-average hectares of each type, summed on both sides, with no equivalence factor. Build 1's per-person footprint is 0.198 ha of world-average cropland plus 0.860 of world-average pasture (README, Simpson application table); Australia's output is 22.3 Mha of world-average cropland plus 46.4 Mha of world-average pasture (`harmonised_comparison.csv`, note column); 68.7 over 1.059 gives 64.8. The README records that "Simpson's text gives world-average yields with no weighting, so no equivalence factor applies (checker V07)". The paper does not say this.
* Mod's point on HALF stands on the paper's own words: "Read in the footprint way, which HALF is not" (5.5) and "The authors state that the index is not predictive" (4.6, Alexander et al. 2016, p. 89). HALF is defined at world-average production as a share of world land, so for HALF it is the world-average basis that is the method, and no capacity reading on either line is the authors'.

**3. Does it change a finding?** No number moves; attribution and emphasis do.
* s3: "in world-average hectares, 134 to 343 million, about three to eight times" would go, or become "the footprint's counterfactual in world-average hectares, 146 to 343 million". B156 and B247 restate.
* s4, s5, H2: if line (b) is the faithful comparison for the footprint, the two lines stop being two equally weighted findings and the 38.5% leads. Issue 5 shows how far 38.5% moves on other references.
* With equivalence factors (the national-accounts convention), cropland would weigh more than pasture, so the pooled reading would move from 64.8 toward the cropland-bound 112.5 (direction only; no equivalence factors are held in the records).

**4. The fair response.** Reword, no compute.
* Table 3 and Table S8: rename the column "World-average hectares (counterfactual)"; take the energy balance out of the secondary group so its range reads 146 to 343 (footprint) and 276 (HALF); state in 5.4 and 5.11 how crop and pasture are pooled (summed world-average hectares, no equivalence factors, as in Simpson et al.).
* Section 5.11 and 9.1: present line (b) as the footprint's own accounting (Wackernagel and Rees 1996, p. 78; Wackernagel et al. 1999) and line (a) as the counterfactual of dropping the yield factor; keep both in Table 6. For HALF, say on both lines that any capacity reading is this paper's conversion of an index its authors call not predictive.
* Abstract s3 and H3: drop the world-average range from the abstract, or give it once as "the footprint's counterfactual in world-average hectares, 146 to 343 million". Decision 105 asked for both classifications in the abstract; the reword keeps both, ranked, so it fits decision 105 but changes its symmetry, which is Murray's call.
* Response letter: "We agree that dividing Australia's physical hectares by world-average hectares is not a reading the footprint makes. The own-productivity reading is presented as the footprint's, the world-average reading is labelled a counterfactual, and the abstract no longer attributes it to the aggregate methods. Cropland and pasture are pooled as summed world-average hectares without equivalence factors, as in Simpson et al.; the text says so."
* Cost: about 0.5% inside the patch job, plus a register job for B156, B247 and B347.

**5. Dependencies and conflicts.** Feeds Issues 3 and 5 (the headline share). The referees pull in different directions on HALF: EE treats line (b) as faithful, Mod says HALF's line (b) reading is the converter's. Both are right for their method: line (b) is faithful for the footprint, and neither line is HALF's. Round status: (ii). R03b issue 3 asked for the local readings to be primary and decision 106 did that; EE accepts the change and asks for the counterfactual label and the asymmetry. The aggregation question (EE Q1) is new.

---

## Issue 2. The footprint tested is neither Simpson's food row as reproduced nor the national accounts

**1. The issue.** The footprint carried into the comparison is a partly reproduced rebuild of a 1991-92 food row; a reading from the current National Footprint and Biocapacity Accounts should be the footprint's primary entry (EE M2, EE Q2; Mod M6 in part).

EE: "A reading from published national accounts needs no rebuild and has no fidelity problem." Mod: "The Global Footprint Network's national accounts would also give a current, reproducible footprint for Australia in place of a reconstruction of a 1991-92 paper."

**2. What the records show.** Right that such a reading would be the better benchmark; mistaken that it is published for Australia in a form the project can use.
* `BLOCKED_SOURCES.md`: Murray checked the public data platform (2026-11-01); its country list has no Australia, and the 2025 results table reproduced elsewhere has the same 127 countries without Australia. Lin et al. 2018 (L025) and Wackernagel et al. 2002 (L024) have no Australian row. Borucke et al. 2013 (L125) is "record only".
* The records hold one secondary reading: B223 (Tier B, unverified), "about 39 million for 2022" from secondary Global Footprint Network figures (biocapacity 11.0 over footprint 7.3 global hectares a person), the whole footprint, not the food row; and about 27 and 30 million for the 1990s from Lenzen and Murray's production over consumption land (1.49) and Wackernagel's remainder with Simpson.
* Decision 113: a Global Footprint Network data licence is Murray's call and "not needed to submit". Decision 33 sets the tone for how the gap is described.
* Section S2.5 cites Lin et al. 2018 and Wackernagel et al. 2019 for the accounts, and Wackernagel et al. 1999's 9.0 against 14.0 ha a person for Australia (p. 386).

**3. Does it change a finding?** Not on the records held. If B223's 39 million stood, a national-accounts reading would sit near the corrected model (0.94 times 41.5), which would change the footprint's place in s3 and Table 3; but B223 is unverified, secondary and whole-footprint, so it cannot carry a headline.

**4. The fair response.** Out of scope for a new reading, with a stated reason, plus a small reword.
* Say in 4.5 or S2.5 why the national accounts are not the entry: the public release carries no Australian row; the accounts' food component is not published separately; the test asks what a method gives on common inputs, which needs a recipe that can be run, which the Simpson food row supplies and the licensed accounts do not.
* Report B223 in S2.5 as a secondary, whole-footprint figure with its status, after a one-route check (it is unverified). Its algebra is that of Issue 3 (biocapacity at national yield factors over footprint, times population), so it belongs beside line (b).
* Response letter: "The current national accounts would be the natural benchmark. Their public release carries no Australian row, and a licence is outside this study; we report the secondary whole-footprint figure we could trace (about 39 million for 2022), state its basis, and keep the Simpson rebuild as the runnable recipe, labelled as this study's implementation after Simpson et al."
* Two responses are defensible: (a) the reword above; (b) Murray obtains the licence (decision 113) and a builder adds the reading (about 1% build and 1% check, given the data). I recommend (a): a reviewer will accept a documented absence more readily than a delay, and decision 113 says the licence is not needed to submit.
* Cost: about 0.5% (check of B223 and wording).

**5. Dependencies and conflicts.** Linked to Issue 9 (fidelity labels) and Issue 3 (B223's structure is line (b)'s). The referees agree. Round status: (iii). R03b issue 3 recorded the national-accounts request as "needs Murray"; decision 113 left it with Murray and nothing was added.

---

## Issue 3. The own-productivity readings are land-weighted production-to-consumption ratios, and the binding-land-type reading is left out of the headline

**1. The issue.** At own productivity the footprint reading is the population times a land-weighted ratio of output to consumption, an export-inclusive count; its binding-land-type ("pasture alone") reading of 53.9 to 77.9 million is the footprint's analogue of the pairing and is excluded from the headline range without explanation (EE M3, EE Q3; Mod Q1).

EE: "That reading is the footprint with land types held as separate constraints, the footprint analogue of the pairing, and its low end sits beside the improved model's 53.6."

**2. What the records show.** EE is right on the algebra and on the exclusion, and has found something the audit and the first plan did not.
* The algebra holds on the files. Build 1: 22.3 Mha of world-average cropland over 0.198 ha a person gives 112.5; 46.4 Mha of world-average pasture over 0.860 gives 53.9; pooled, 64.8 (B270). Each is the FAO population (26.20 million) times output over consumption in world-hectare units, because the per-person footprint is FAO consumption over FAO population. The README says the local reading "counts Australian food output, exports included" (Limits). In multiples of the FAO population (scratch): pooled 2.47 (build 1) and 3.23 (build 3); cropland 4.29 and 4.47; pasture 2.06 and 2.97; HALF 2.90. Paper A's draft records the meat surplus on its own basis (4.66 Mt produced against 2.96 Mt eaten in 2021-23, 1.57).
* The exclusion is a script choice, not a stated rule: `harmonised_lines.py` builds the primary footprint row from the cropland-bound and pooled readings "as the primary row, not pasture alone", mirroring the secondary row. But on line (b) the pasture-alone readings are two of the footprint's six paired readings, so they enter the 38.5% while staying out of the 64.8 to 117.0 headline range.
* The minimum over land types, the binding reading EE asks for, is 53.9 (build 1) and 77.9 (build 3): 1.30 and 1.88 times the corrected model, and 1.01 and 1.45 times the improved (53.6). It needs no compute.
* Mod Q1 is answered by the same algebra: the own-productivity reading is output-based, so the pasture area (331.87 Mha, rangelands included) does not enter it; only the world-average readings depend on it. The output is national ruminant output at world pasture per tonne, not by land class.
* One record bears on the numerator: FAOSTAT's food balance books Australia's winter crops a year behind the crops file (audit section 5, X111). The own-productivity numerator is crops-file output for 2021-23 and the denominator food-balance consumption for 2021-23, so the cropland readings mix harvest years a little. The audit traced its effect on the Cassidy test only.

**3. Does it change a finding?** Yes, in framing and in one range.
* s3, H3, B347, Table 3: the footprint's paired reading, 53.9 to 77.9, would sit beside the pooled 64.8 to 84.6; the aggregate group's low end would fall from 64.8 to 53.9 if the binding reading joined the range (1.30 times the corrected model in place of 1.56).
* Section 5.14 and 7.6: "consistent with a feature that the model carries" becomes a statement that the footprint read at its binding land type (53.9 to 77.9) brackets the improved model (53.6) at its low end, which is a stronger and simpler link than variant 1 alone. Issue 7 takes this further.
* Section 8.2: every own-productivity reading is export-inclusive, which Cohen's point (1995, p. 343) bears on, not only the export counts of section 6.1.

**4. The fair response.** Reword, no compute.
* State the algebra in 5.11 in one sentence: "At own productivity the footprint reads the population times the ratio of Australian output to consumption, each in world-average hectares, so it counts exports as the export-inclusive counts do."
* Report the binding-land-type reading as the footprint's paired reading beside the pooled one in Tables 3, 5 and S8, and say why the pooled reading is kept (it is the footprint's convention).
* Response letter: "We agree and have stated the algebra. The binding-land-type reading, 53.9 to 77.9 million, is reported beside the pooled reading as the footprint's paired reading; at its low end it sits beside the improved model's 53.6."
* Cost: about 0.3% inside the patch, plus register rows (B270 holds the values; B347 and B156 restate).

**5. Dependencies and conflicts.** Feeds Issue 7 (the bridge) and Issue 10 (exports through the model: the footprint's own-productivity reading is itself an export factor in a second method, 2.47 pooled against the model's 2.41 for the CSIRO and University of Queensland count). The referees agree; Mod asks for the same bridge from the model's side (Issue 7). Round status: (i) new.

---

## Issue 4. Three of the five comparators are capacities the author constructs, and the fish reading sets a method's centre

**1. The issue.** HALF, people per hectare and the commodity balance give no people count in their authors' hands, so the readings and the closure statistic measure the author's conversions; the fish reading is a single commodity that drives the commodity balance's negative share (Mod M1, EE M5 on the fish reading).

Mod: "separate, in Tables 3 and 5 and in the abstract, the methods that produce a people count ... from those the author converts ... Report the closure statistics on the first group alone, as well as on all five. Drop the fish reading from the method centre, or justify it."

**2. What the records show.** Right that three readings are conversions; partly mistaken on which methods produce a count; the effect on the headline is small.
* The paper says so method by method (4.3, 4.6, 5.5, 5.6). Mod puts the footprint among the methods that produce a count; the records say otherwise: Wackernagel et al. 1999 "give no count of people" (S2.5), and section 4.5 says the footprint "becomes a capacity only when a country's own land is divided by the land a person needs". Of the five, only the energy and protein balance gives a people count in its authors' hands (Henry and Godden 1995, p. 100).
* Scratch, closure on the energy balance and the footprint alone: 1.4% on line (a) and 37.8% on line (b) to 41.5 (45.2% to 53.6); on the three converted methods, 6.3% and 39.1%. Either grouping leaves the headline where it is.
* The fish reading: section S3.5 calls it a single commodity with no substitution, and defect X040 (open) records that FAO's Australian fish production, imports and food use carry one value across 2021 to 2023, so it is a single-year value. Scratch, fish dropped: 5.9% on line (a) and 40.9% on line (b) to 41.5; the spread of method centres narrows by 42% on line (b) in place of 32%. On line (a) the median-reference share moves from -4.9% to -0.5%.

**3. Does it change a finding?** Little. s5 and H2 hold within a few points on either grouping or without fish. s3 and Table 3 change in labelling: the commodity balance's low end (12) moves to 40 if the fish reading leaves the centre, and the method reads 40 to 128.

**4. The fair response.** Reword, with the scratch figures rebuilt in the robustness table of Issue 5.
* Add a column to Tables 3 and 5, "people count given by the method's authors: yes / derived here", and use "this study's capacity reading of" in s3 for the four derived readings.
* Report the closure on the energy balance alone and on the energy balance and footprint, in the robustness table (Issue 5), not as a second headline.
* Move the fish reading out of the commodity balance's centre, report it in the text as the single-commodity reading it is, and cite X040's single-year caveat. Keep it in Table 3 as a reading.
* Response letter: "Only the energy and protein balance gives a people count in its authors' hands; the footprint, HALF, people per hectare and the commodity balance are read as capacities by this study, and the tables say so. The closure on the energy balance and footprint alone is 1.4% and 37.8% on the two lines (37.8% to 41.5), close to the five-method figures. The fish reading is reported separately and no longer sets the commodity balance's centre."
* Cost: inside Issue 5's job and the patch.

**5. Dependencies and conflicts.** Shares the robustness job with Issue 5. Mod and EE agree on the fish reading. Round status: (i) new in its framing; it extends R03b issue 4 (which published figures are reproduced), which the revision did not reach as a mapping column.

---

## Issue 5. The closure statistic is anchored on the model, driven by two methods, and untested for robustness

**1. The issue.** The 4.1% and 38.5% are distances to one point estimate of the author's model, over five equally weighted centres formed in one way, with no interval; reference-free measures should lead and the shares be shown under other references, other centres and with methods left out (EE M5, EE M4 (i), EE Q4; Mod M3, Mod Q2).

EE: "With five methods and no interval, the reader cannot tell whether 4.1% differs from zero or 38.5% from 25% or 50%." Mod: "the 38.5% on line (b) comes almost entirely from the footprint (61%) and HALF (68%) ... it is not a finding about inputs in general."

**2. What the records show.** Right on every count; the revision answered the first-round request (three references and reference-free measures, B113, V39) and the referees accept it but ask for the next step.
* The centre is defined in the README and the script (a method's centre is the geometric mean of its paired readings; counts 6, 6, 1, 3, 3), but not in the main text (Mod Q2 answered).
* Per-method shares are in S3.11 (footprint 61%, HALF 68%, people per hectare 26%, energy balance 8%, commodity balance -15% on line (b)).
* Scratch robustness, distance to the model (share closed, line (a) / line (b)):
  * reference 31.1: 3.3% / 32.6%; 41.5: 4.1% / 38.5%; 49.2: 4.5% / 42.3%; 53.6: 4.7% / 44.4%;
  * each method left out (to 41.5): energy balance out 3.1% / 45.9%; footprint out 6.8% / 31.1%; HALF out 5.6% / 27.7%; people per hectare out -1.1% / 41.5%; commodity balance out 6.2% / 44.3%;
  * fish dropped 5.9% / 40.9%; pasture-alone readings dropped 3.7% / 35.1%; footprint and HALF both out 10.5% on both lines;
  * Henry and Godden's land scale-up classed as method (kept on harmonising): 1.4% / 35.8%.
* Scratch, to the median of the method centres: line (a) -32.1% (commodity balance left out) to -0.5% (fish dropped) across the variants, -4.9% as printed; line (b) 8.6% to 35.5%, 16.0% as printed, 9.4% and 9.6% with HALF or the footprint left out.
* Scratch, spread of method centres (standard deviation of logs, share narrowed on line (b)): 31.8% as printed; 39.9% with median centres in place of geometric means; 42.4% without fish; 23.2% to 47.5% with one method left out, except the commodity balance: without it the spread of centres widens by 11.5%, because the footprint and HALF move below the energy balance and people per hectare. So "narrowed that spread by about a third" (s5, B277) depends on the commodity balance being in the set.

**3. Does it change a finding?** Yes, in how s5 and H2 should be stated.
* Line (a): "4.1%" holds as "about -1% to 7% of the distance to the model, near zero on every variant tried".
* Line (b): to the model, about 28% to 46%; to the centre of the methods, about 9% to 36%; without the footprint and HALF, 10.5%. "Closed 38.5%" should become a range, and the sentence should say the line (b) closure is the productivity conversion of two land indices, as Mod asks.
* "Narrowed that spread by about a third" (s5, B277) should carry its dependence on the commodity balance, or be replaced by the range 23% to 48% with that exception named.

**4. The fair response.** Compute and reword.
* Extend `harmonised_lines.py` with a robustness block: the four model references; leave one method out; fish dropped; pasture-alone dropped; median against geometric-mean centres; the energy balance alone and with the footprint; the land scale-up classed as method. Write `harmonised_robustness.csv`; regenerate Table 6 with the reference-free measures as its first rows and the distance to the model second; add the robustness table to S3.11. Builder about 1% (Sonnet), blind check about 1% (Opus), as B113 and V39.
* Abstract s5 and H2: report line (a) as "about zero on every reference and grouping" and line (b) as a range, naming the footprint and HALF as its source. Mod's suggested highlight ("Converting footprint and HALF to Australian productivity removes most of their gap to the model") is accurate on the records (61% and 68%) and could replace H2 within 85 characters.
* Response letter: "The shares are reported with a robustness table: references at 31.1, 41.5, 49.2 and 53.6 million, each method left out, the fish reading dropped and two ways of forming a method's centre. Line (a) stays near zero throughout; line (b) closes about 28 to 46% of the distance to the model and about 9 to 36% of the distance to the centre of the methods, and almost all of it is the footprint and HALF at Australian productivity. The reference-free measures lead Table 6."
* Cost: about 2% in all.

**5. Dependencies and conflicts.** Takes Issue 4's groupings and Issue 1's choice of which line leads; Issue 6's third line adds a row. The referees agree; both ask for the reference-free measures first. Round status: (ii). R03b issues 1 and 2 asked for the formula, three anchors and an anchor-free measure; B113 delivered them; the referees ask for intervals or a robustness table and for the reference-free measures to lead.

---

## Issue 6. Harmonisation leaves the per-person requirement, the waste basis and the data layer unequalised; why is only productivity classed two ways

**1. The issue.** The methods divide by FAO supply (14.8 MJ) and the model by 8.0 MJ as eaten with waste charged separately, a factor of about 1.85; the model runs on its own layer; Henry and Godden's land scale-up is as much method as world-average hectares; a third line should equalise the per-person requirement and waste for methods and model, and the model should be run on the FAOSTAT layer (EE M6; Mod M2, Mod Q5; EE abstract point 4).

Mod: "The paper picks one input (productivity) to classify two ways. A reader will ask why only that one, when the energy basis, the land scale-up and the waste treatment have equal claim."

**2. What the records show.** Right on the facts; one premise, repeated from the first round, is wrong.
* Bases: Table S5 and `bases.csv` show 15.6 MJ (Henry and Godden's implied factor), 2,700 kcal (Cassidy), 3,525 kcal or 14.8 MJ (harmonised), 8.0 MJ as eaten (the model). 14.8 over 8.0 is 1.85.
* The intake variant (B116, Table S7) moves the methods only, and on FAO's waste factors leaves the per-person need well above 8.0 MJ; 20% of food energy has no factor on FAO's shares and 37% on the model's (S3.10).
* Data layer: the model runs on its ABS-based 2025 layer (meat window 2020-21 to 2024-25; 2020-21 holdings), taken as the same vintage as FAOSTAT 2021-23 (S3). "Common" is true of the land totals (363.5 Mha, FAOSTAT against holdings to 0.01 Mha) and the methods' food balance, not of the model's production.
* Mod repeats the first round's population point ("its population is 27.6 million against FAO's 26.2"). The README and S3.8 say the 27.6 enters no method reading and none of the model's capacities (capacity is land over need a person); it enters the failure probability only. R03b (c) said this, and it holds.
* Scratch, the land scale-up classed as method (Henry and Godden's harmonised readings kept at Nix's 70 Mha): line (a) 1.4%, line (b) 35.8%; spread of centres on line (b) narrows 23.6% in place of 31.8%.
* Direction of a third line from the records: R03b (c) and S3.1 show that putting the energy balance on a plain requirement raises it (243 million at 8.8 MJ against 145.2 on supply), and Table S7 shows every calorie and land reading rises on an intake basis. Equalising the per-person requirement at the model's level would push every method away from the model and the share closed would fall, likely below zero on line (a).

**3. Does it change a finding?** The third line would add a row to Table 6 and probably a negative share; it would not raise 38.5%. s2's "Australian data for 2021 to 2023" and s5 would need "on the methods' supply basis". s3's multiples would rise on an intake basis (3.1 to 10.9 times on FAO's factors, Table S7).

**4. The fair response.** Compute one third line; reword the data claim; out of scope for the model on the FAOSTAT layer.
* Compute: a line (c) in `harmonised_comparison.py`, every method's per-person need set to the model's 8.0 MJ as eaten grossed up by the model's own loss factors (the mass-based footprint and HALF scaled by the same energy ratio), against the model at 41.5 and at 55.3 (no avoidable waste), with shares on both references. Builder about 1.5%, check about 1%. Say in the brief that the expected direction is wider, so no one reads a fall in the share as an error.
* Classification table: one row per input (productivity, per-person requirement, waste, land base and scale-up, data year, population), one column per method, as run and harmonised, with "input" or "method" as decision 35 classed it. It is Table S5 with one column added; about 0.3%.
* Model on the FAOSTAT layer: two responses are defensible. (a) Out of scope: the model's yields and output are zone-level ABS series and FAOSTAT is national, so a FAOSTAT model is a new data layer, session-size (about 4 to 6% with a check); instead tabulate the model's 2025 layer against FAOSTAT 2021-23 production by product group (about 1%) and replace "common data" by "a common land base and food balance; the model on its own ABS layer". (b) Compute the FAOSTAT layer. I recommend (a): the abstract wording in s2 is accurate, and a reviewer is likely to accept a production table showing the two layers agree or by how much.
* Response letter, population: "The model's population enters none of the method readings and none of the model's capacities, which are land over need a person; it enters only the failure probability at the 2025 population (section 5.1)."
* Cost: about 3% in all.

**5. Dependencies and conflicts.** Adds a row to Issue 5's Table 6; uses Issue 10's energy-requirement facts. The referees agree; Mod adds the FAOSTAT layer and the land scale-up. Round status: (ii). R03b issue 10 asked for a basis table and an intake variant; B116 delivered both; the referees accept them and ask for a two-sided third line.

---

## Issue 7. The pairing explanation is a single-variant test that overshoots; a structural bridge is wanted

**1. The issue.** Variant 1 (81.7 million) passes footprint build 1 and HALF and lowers protein, so it is not an attribution; the paper should bridge from HALF or the footprint at Australian productivity to the model feature by feature, in both orders or as an all-orderings average, including the land pooled at world-average hectares test listed as not run (Mod M4, Mod Q6; EE M3 last part).

Mod: "A cause that overshoots two of three targets is not a close attribution; it shows that something else in the model pushes the other way and is not identified."

**2. What the records show.** Partly right.
* The figures are as Mod states: 81.7 closes 173%, 117% and 93% of the gaps to 64.8, 76.0 and 84.6 (Table 7); protein falls from 93.1 to 80.9 g a day (B114 section 6). S3.12 lists three tests proposed and not run, the first being land pooled at world-average hectares.
* Mod reads the three readings as three targets of one cause. On the records they are a span: the footprint's pooled readings run 64.8 to 84.6 and HALF's defensible readings 73.7 to 79.3 (README); 81.7 lies inside the footprint span and 3% above HALF's top. B114 says the adjusted readings "sit between 'pairing kept' and 'pairing removed with the diet free'". "Overshoots two of three" is true of the point readings, not of the spans.
* The footprint side of the bridge exists: the binding-land-type footprint reading (Issue 3) is the footprint with a pairing-like constraint, 53.9 to 77.9, against the pooled 64.8 to 84.6. That is half of Mod's bridge at no cost.
* The machinery for an all-orderings average exists: B111 computed an exact Shapley decomposition over 9! orders for Paper A, and V37 agreed within one person. B114's closed form reproduces the evaluator to 1e-6.
* Mod Q6: no run holds protein with energy by legume substitution. The nearest are variant 1p (87.0, protein 77.3 g) and variant 3 (free allocation at the diet's energy and protein, 172.3 million), which decision 124 cut from the paper and kept in the README; "crop-fed protein within the meat group" is listed as not run.

**3. Does it change a finding?** s6, H4 and 7.6 would move from "relaxing the pairing alone brings the model to 81.7" to a decomposition: how much of the distance from the adjusted footprint or HALF to the model is productivity, pairing, diet and waste, requirement, reserve and non-food land. Without that run, the paper's "the test cannot show it is the only cause" is the accurate sentence and should travel into the abstract with s6.

**4. The fair response.** Compute, at medium cost; reword in the meantime.
* Compute: a bridge from HALF at Australian productivity (76.0) to the corrected model (41.5) through the features Mod lists, using B114's closed form (`pairing_relaxed.py`) and the Shapley routine of B111, with every ordering averaged and the two extreme orders shown; include the land pooled at world-average hectares step from S3.12 and a protein-held variant (legumes for pasture-fed protein). Builder about 2.5% (Opus, as B114), check about 1.5%. Re-admitting variant 3 would amend decision 124 and is Murray's call; the bridge does not need it.
* Reword in any case: s6 and H4 add "a sufficient cause, not shown to be the only one"; 5.14 reports the footprint's binding-land-type reading beside variant 1.
* Response letter: "Variant 1 lies inside the footprint's span of 64.8 to 84.6 million and 3% above HALF's highest defensible reading, so we read it as sufficient, not as an attribution. We have added a feature-by-feature bridge from HALF at Australian productivity to the model, averaged over every ordering, including the land pooled at world-average hectares, and a protein-held variant."
* Cost: about 4%.

**5. Dependencies and conflicts.** Needs Issue 3 (binding reading) and Issue 1 (which line is the footprint's). Mod asks for the bridge; EE asks for "how much of the remaining gap is the pairing and how much is diet, yields and per-person requirement", which is the same object, so the referees agree. Round status: (ii). R03b issue 8 asked for the relaxed runs; B114 ran three, V40 passed the numbers and failed two sentences as overclaiming; the referees accept the runs and ask for an attribution.

---

## Issue 8. The binding constraint, pasture, and its drought response are outside the uncertainty analysis

**1. The issue.** Pasture productivity is listed as undrawn, the two largest drivers are judgement-weighted, the drought allowance applies a cereal factor to a pasture-bound system, and the failure probability (5.8 to 6.1% a year) depends on that assumption (Mod M5, Mod Q3, Q4, Q8; EE Q9 in part).

Mod: "Test the drought allowance against a livestock or pasture-growth series, or state plainly that the failure view does not cover the binding constraint."

**2. What the records show.** Mod is mistaken on pasture productivity as the model builds it, misled by the supplement, and right on the drought allowance, where the records go further than the referee.
* Pasture productivity: `analysis/sensitivity_2025/README.md` (undrawn choices table) says "Pasture productivity | covered | In this model pasture output is national meat shared among zones by dry sheep equivalent, so its uncertainty is the meat window and the meat calibration, both drawn." Section S5 of the paper lists "pasture productivity" among the 23 undrawn choices. The paper contradicts its own README; the referee read the paper correctly.
* What is not drawn is a deviation of national pasture output from the observed meat series (for example, a carrying-capacity range in dry sheep equivalents by land class). Scratch, from B114's closed form (crops need 3,397 m2 and pasture 84,190 m2 a person at 41.5 million): pasture output plus or minus 20% gives about 49.4 and 33.5 million short term, about plus 19% and minus 19% (Mod Q3).
* Drought: B112 (decision 103, Paper A) computed a crop-only bound: with the factor on crops alone and pasture-fed output at its mean, short-term capacity is 41.2 million at 1 in 10, 41.0 at 1 in 20 and 40.4 at 1 in 100, against 30.8, 26.3 and 18.9 with the factor on everything; long term at 1 in 100, 24.7 against 15.6 (`analysis/resilience_2025/drought_bounds.csv`). B112: "The short-term drought results come almost wholly from applying a cereal factor to pasture-fed output." Paper A carries this (its sections 2 and 8, "about 97%"); Paper B does not mention it. The one observed check in the records puts the drought years 2018-19 and 2019-20 near the median of the single-year series and the following year at 0.90 (B112); no livestock series for 1982-83 or 2002-03 is held.
* Failure probability: at 1 in 100 the crop-only bound (40.4) is above the 2025 population (27.6), so on that bound the failure probability at the 2025 population is under 1 in 100 a year, against 5.8 to 6.1% with the factor on everything (inference from the bound; not computed).
* Judgement-weighted drivers: S5 and the README say so (land source, energy requirement, meat window). Mod Q8: the energy window is PAL 1.4 to 1.8 within the NHMRC 1.2 to 2.2. Scratch, assuming capacity varies inversely with the food amount, as the improved release's one-at-a-time run suggests (42.5 at 1.286 against 53.6): PAL 1.2 and 2.2 would give about 48 and 26 million on the corrected release, one at a time.
* EE Q9: the default diet is the NHMRC sedentary pattern (PAL 1.4), 8.0 MJ as eaten; whether it is weighted to Australia's age structure is not stated in the records I read.

**3. Does it change a finding?** Yes, materially, for the weather results.
* s7 and H5: the low end 18.9 rests on the cereal factor applied to pasture-fed output; on the crop-only bound the short-term model at 1 in 100 reads 40.4, and the weather span would shrink from 18.9 to 55.3 to about 40.4 to 55.3.
* Table 8: the drought allowance's factor of 2.19 is 1.03 on the crop-only bound (41.5 over 40.4, scratch).
* B130 (5.8 to 6.1% a year), B134 (26% and 54% lower), B096 (30.8), B157, B245 ("reproduces the Jones committee's 30 to 35 million at a 1-in-10 allowance") all rest on the same rule.
* Table 9, purpose 1 (the failure view well suited): the failure view does not cover the binding constraint, so "well suited" needs that limit beside it.
* Section 6.11's ordering of the 1.58 factor against the definitions depends on which settings are drawn, as Mod says; the pasture-output deviation would add roughly a 19% swing each way.

**4. The fair response.** Reword to cite the files; compute only the small pieces.
* Reword: S5 moves pasture productivity from "undrawn" to "covered through the meat window and calibration", with the README's sentence. Sections 5.8, 6.6, 7.2 and the abstract carry B112's crop-only bound beside every drought figure; 5.8's failure probability carries the caveat in the same sentence, as Mod asks; Table 9's purpose-1 cells add "for crops; not tested on pasture-fed output". About 0.5% in the patch.
* Compute (small): the pasture-output swing of plus or minus 20% one at a time through `pairing_relaxed.py`'s closed form, and the PAL 1.2 and 2.2 ends one at a time through `rerun.mjs`; about 0.5% build and 0.5% check. A full redraw of the Monte Carlo with a pasture-output setting is defensible too (about 3%, as B115 and V41); I recommend the one-at-a-time readings first, because the meat window carries the observed variation.
* Livestock drought test: out of scope unless a livestock output series is fetched (the records hold none for 1982-83 or 2002-03); say so.
* Response letter: "Pasture output in this model is national meat output shared among zones, so its uncertainty is drawn through the meat window and the meat calibration; the supplement wrongly listed it as undrawn and is corrected. On the drought allowance the referee is right: applied to crops alone, the short-term capacity at 1 in 100 is 40.4 million against 18.9, so the weather results rest on applying a cereal factor to pasture-fed output, which is untested. Every drought figure, the failure probability included, carries that bound and caveat."
* Cost: about 1.5%.

**5. Dependencies and conflicts.** Conflicts with decisions 118 and 122, which keep "18.9 to 55.3" in the abstract (see Issue 10). Cross-paper: Paper A carries the bound, so the two papers disagree unless Paper B does too. EE does not raise the drought point; it does not contradict Mod. Round status: (iii) for Paper B. R03b issue 12 asked for a crop-only bound; B112 computed it under decision 103 for Paper A, and the Paper B revision (B118) did not take it in. The pasture-productivity part is (ii): R03b's answer was in the README, but the paper's S5 says the opposite.

---

## Issue 9. Fidelity: the readings that carry the headline rest on implementations that do not reproduce, and the authors were not contacted

**1. The issue.** The footprint's plant-food cropland (66 to 76% low) and people per hectare (22 to 42% high) fail fidelity, but carry s3; the HALF and Cassidy authors were not contacted although their supplements would settle the failures (Mod M6, Mod Q7; EE M2 in part; Mod abstract note 1).

Mod: "Where an implementation stays unreproduced, mark the reading as the author's implementation 'after' the method in every table and in the abstract, not as the method's reading."

**2. What the records show.** Right on the grades; the decision on contacting authors is the project's own and stands unexecuted.
* Grades are as Mod states (Table S6, `fidelity.csv`; decision 128 for Cassidy).
* Decision 5 (2026-11-07, Murray: yes): ask the authors of the HALF and people-per-hectare methods to check the reconstructions before submission, after the project's own checks pass. It has not been carried out. The method-test README says of Simpson "The authors were not consulted (Murray's decision)", and section 5.2 generalises that to all methods. Paper and decision 5 differ for HALF and Cassidy.
* The Cassidy supplement "was not read" (5.6). The literature register holds L016 (the paper), and no supplement row.
* The primary footprint reading at own productivity is pooled; the component that fails worst (plant-food cropland) enters the cropland-bound reading (112.5 to 117.0) and the pooled one. Scratch, without the readings that rest on partly or not reproduced components, R03b found the direction of s3 survives; the same holds with the footprint at own productivity, since the energy balance (reproduced) alone reads 3.2 to 5.1 times.
* HALF's Australian residual on the printed inputs (8.4%) is mostly the world pasture area of the supplement (S3.3), which the authors could confirm.

**3. Does it change a finding?** s2's "the implementations reproduce them in part" is accurate but soft; s3's footprint and Cassidy readings should be labelled "after". No number moves unless an author's reply changes a build.

**4. The fair response.** Reword; act on decision 5.
* Label the footprint, HALF and people-per-hectare readings "this study's implementation after" in Tables 3, 5 and 6 and in s3; s2 reads "reproduce Henry and Godden and the thesis, HALF and Simpson's pasture in part, and not people per hectare or Simpson's plant-food cropland".
* Section 5.2: replace "The authors were not consulted" by what is true per method, and act on decision 5 for HALF and Cassidy (Murray's emails, no spend), with the request built from Table S6.
* Read the Cassidy supplement if it can be fetched (Murray's action; one targeted read, about 0.1%).
* Response letter: "The tables and abstract label these readings as this study's implementations after each method. We have written to the authors of HALF and of Cassidy et al. with the reconstruction and its residuals [outcome to be reported]." (The bracket is for Murray once the replies are in.)
* Cost: about 0.3% plus Murray's emails.

**5. Dependencies and conflicts.** Issue 2 (national accounts) is EE's version for the footprint. The referees agree. Round status: (ii) for the grades (B116 restated fidelity, decision 128), (iii) for contacting authors (R03b issue 5 named decision 5; not done).

---

## Issue 10. Section 6 mixes in-model changes with ratios between methods, the weather-and-waste sentence reads as a range, and the optimised diet tops the order

**1. The issue.** The export rows are not model runs, "Australian settings" and the time frame are bundles, the optimised diet C sets the top, the ladder adds nothing, and "Weather and waste take the model from 18.9 to 55.3 million" reads as a joint range; the export factor should be a model run or leave the ordered table (EE M7, EE Q5; Mod abstract note 3; Mod minor 4, 8; Mod Q9).

EE: "These are two separate one-at-a-time changes in opposite directions from 41.5, not a joint range, and the sentence will be read as a range of the model." Mod: "Is the 7.88 factor for the optimised diet a property of the method or of the solver's freedom?"

**2. What the records show.** Right on each count; R03b recommended the fix and it was not made.
* `design_choices.csv`: the export row's source is the published 100 against the model's 41.5; the energy rows compare exports alone (183.9, 263.9) with the model's domestic capacity. Section 6's opening says each choice was measured "with the author's model on the same 2025 data", which is not true of these rows.
* Diet C: `analysis/nutrition_lp_2025/README.md` says variant A "is the one to quote" and C is not a realistic diet; Table S2 holds A (85.5 million, factor 1.60) and B (202.1, 3.77).
* The weather-and-waste wording is decision 122 (amending 118), taken on the gate 5 digest with V41's note that waste is a setting by section 6.9's rule. EE and Mod read it as Mod's and V41 did.
* Issue 8 bears directly: the 18.9 rests on the cereal factor on pasture-fed output (40.4 on the crop-only bound).
* EE Q5: no model run counts exports. R03b recommended "out of scope" with a food-balance rebuild of the proportional count (`proportional_count.csv`, 101 to 104 million without feed as a domestic use) as a computed comparison.

**3. Does it change a finding?** Yes.
* s7 and H5: the sentence's structure changes, and with Issue 8 the low end carries the crop-only caveat.
* 6.11 and B333, B194, B182: "the optimised diet (7.88) most" becomes diet A and B (1.60 to 3.77) with C as an upper bound; the energy-count export rows leave the in-model ranking; the top of the in-model order becomes the unit (2.67) and time frame (2.66), with the time frame marked a bundle.
* Table S4's "factor measured in section 6" column changes for exports and diet.

**4. The fair response.** Reword and restructure; out of scope for exports through the model; the weather-and-waste wording needs Murray.
* Split Table 8 into panels as R03b proposed: (i) changes made in the model on one release; (ii) comparisons with external counts (the CSIRO and University of Queensland count, its food-balance rebuild, the energy counts of exports); (iii) the Monte Carlo. Mark "Australian settings" and "time frame" as bundles. Replace C by A and B in the ranked rows and give C as an upper bound with the README's caution (Mod Q9). Drop the ladder paragraph of 6.10 and Figure 3's ladder, or keep the ladder as an unordered illustration (EE agrees with the paper that it is not a decomposition). Drop the 2.22 minimum-to-maximum comparison in 6.11 (Mod minor 8). About 0.5% in the patch, plus a small regeneration of `design_choices.csv` (about 0.3%).
* Exports: out of scope (the model is self-sufficient by design, section 8.2), with the rows labelled as comparisons. Issue 3 adds a second-method export factor at no cost: the footprint's own-productivity reading is the population times production over consumption, 2.47 pooled (scratch, to be rebuilt), beside 2.41.
* Weather and waste: a standing decision (122, amending 118) fixes "Weather and waste take the model from 18.9 to 55.3 million". The referees' request would amend it. Recommended wording for Murray: "In the model, a 1-in-100 weather allowance lowers 41.5 million to 18.9 (40.4 with the allowance on crops only), and removing avoidable waste raises it to 55.3." Response letter if Murray keeps decision 122: "The sentence reports the two definitional ends that one model reaches on one data set; the text (section 6.10) states that they are separate one-at-a-time changes from 41.5 million, and the abstract says 'one at a time'." Adding "one at a time" keeps decision 122's figures and most of its words.
* Response letter, exports: "The export rows compare the model with external counts and are presented as such in a separate panel. Running the model with exports would need an export basket held on the land, which the self-sufficient model does not carry; we give instead the food-balance rebuild of the proportional count and the footprint's own-productivity reading, which is itself an export-inclusive ratio (section 5.11)."
* Cost: about 1%.

**5. Dependencies and conflicts.** Depends on Issue 8 (the 18.9) and Issue 3 (the export ratio). Decisions 118 and 122 are engaged. The referees agree. Round status: (iii). R03b issue 7 recommended three panels, diets A and B in place of C and a factorial; no decision row in 100 to 132 took it up, and Table 8 is unchanged in structure.

---

## Issue 11. The author's model holds too many roles: reference, instrument, two columns, rated by the author with an AI second rater

**1. The issue.** Disclosure does not fix the design: the closure is measured to the model, section 6 runs only in the model, the model has two of seven columns and the only "well suited" ratings for purposes 2 and 3, the purpose definitions favour it, and an AI second rater is not independent (EE M4 (ii), (iii), EE Q8; Mod M7; abstract s8; EE minor 18).

EE: "it also saw a rubric (section S7) whose purpose definitions are written in the model's own terms ... A method built on a diet that has to balance from domestic land will satisfy that definition by construction." Mod: "repeat at least the cheapest design choices of section 6 ... in one other method ... Alternatively, present Table 9 explicitly as the author's judgement and remove the rating claims from the abstract."

**2. What the records show.** Right; two premises need precision, and the records answer part of Mod's request.
* The purpose definitions in S7 are "in the second rater's reading" (V28), not the author's; they were written by the AI checker from the test records. EE's point about their terms stands.
* "Every disagreement was resolved toward the other methods" (Mod) is true: all three differences raised other methods from not suited to partly suited (Table S9).
* Mod's request to repeat design choices in another method is largely met by files the paper holds but does not use in this way (scratch ratios from the files):
  * waste: Table S7's intake readings over supply are 1.17 (energy balance), 1.18 (footprint build 1 cropland-bound), 1.18 (HALF), 1.17 (people per hectare), 1.08 (grain), 1.64 (fish), against the model's 1.33 (corrected) and 1.17 (improved);
  * land base: in the energy balance the land scale-up moves the reading by 1.31 (S3.1: 211 over 161) to 1.53 (210.7 over 137.6), against the model's 1.09;
  * exports: the footprint's own-productivity reading is an export ratio of 2.47 pooled (Issue 3).
* That evidence partly supports Mod: in the energy balance the land base matters more than waste, the reverse of the model's order, so Table 8's ordering is the model's structure, as Mod says ("A pasture-bound fixed-diet model will rate land as unimportant ... by construction").
* Decision 113: outside raters are Murray's call and "not needed to submit". Decision 61 set the AI second rating; decision 109 required its disclosure, which 7.1 makes.
* EE (iii): Table 9 keeps two model columns; decision 109 counted "five plus the model read two ways", so the matrix and the count agree, but the columns do double the model's presence.

**3. Does it change a finding?** s8 ("This narrative critical review finds that no single method serves every purpose") would become a statement of the author's judgement, or be restated as the specific mapping (EE minor 18). Section 6.11's ordering would carry "in this model; in the energy balance the land base outranks waste". No number moves.

**4. The fair response.** Reword; outside raters per decision 113.
* Table 9: title it "the author's judgement, with an AI checker's blind second rating"; merge the model's two columns into one with a note that the failure view adds the weather reading for purpose 1 (and Issue 8's limit); move the second-rater purpose definitions to S7 with a sentence that they were written by the checker from the test records and that purpose 1's definition matches the model's own frame.
* Section 6: add a short paragraph and a three-row table, "the same choices in other methods", from Table S7, S3.1 and Issue 3, after a builder rebuilds the three ratios and a check confirms them (about 0.5% each).
* Abstract s8: "The author's rating of the methods against four purposes finds no method well suited to all four except the model, whose ratings are its author's" is honest but long; the shorter option is to drop s8 as a finding and keep s9's advice.
* Outside raters: decision 113 rules them optional. Response letter if Murray does not seek them: "We have not obtained ratings from people outside the project. Table 9 is presented as the author's judgement, checked by a blind second rating by an AI checker session that agreed on 25 of 28 cells; it is no longer reported as a finding in the abstract." If Murray seeks them: two named raters from the rubric, purposes rewritten before rating without reference to any method, Cohen's kappa reported; no spend, Murray's emails, and a delay of uncertain length.
* Cost: about 1.5% (the other-method table with check, and the patch).

**5. Dependencies and conflicts.** Uses Issue 5 (reference-free measures first) and Issue 8 (purpose 1). Decision 113 is engaged. The referees agree; EE prefers removing the model from Table 9, Mod accepts recasting it as the author's judgement; the recast meets both if the abstract claim goes. Round status: (ii). R03b issue 5 asked for the rubric, the disclosure, the count and a rewritten 9.5; B118 did all four; the referees accept the disclosure and say it is not enough.

---

## Issue 12. The data window and the land source: a favourable harvest window, and a land-source driver when the land totals agree

**1. The issue.** 2021 to 2023 may hold unusually large winter crops, which would raise every output-scaled reading while the model uses trend windows; and the land-use source carries 32% (short) and 58% (long) of the model's variance although "the two land bases agree to 0.01 Mha" (EE M8, EE Q6, Q7).

EE: "presumably the raster and the holdings distribute land differently across zones or states, but the reader is not told."

**2. What the records show.** Partly right on the window; mistaken on the land source, though the paper invites the reading.
* Window: the records hold FAOSTAT cereal production of 55.0 Mt (2021), 59.6 (2022) and 43.1 (2023), mean 52.6, against 31.3 and 32.6 in 1997 and 1998 (`fao_au_production_1997_2023.csv`), and ABS wheat, barley and oats of 31.5 to 39.4 Mt for 2010-11 to 2015-16 (`data/abs-history/grain_state.csv`, three crops only). No ten-year FAOSTAT series is extracted. The FAOSTAT bulk files are pinned by hash (`qa/fao_bulk_hashes.csv`), so a series can be extracted once the file is fetched. Two of the three years look high on these partial records; a like-for-like ten-year comparison does not exist.
* The model uses trend windows for crops (field-crop factor 2022-25 1.356, 2016-21 1.289, drawn) and the meat window 2020-21 to 2024-25. Since the model is pasture-bound in the short term, crop windows move it little; the own-productivity footprint is about a third cropland by weight (22.3 of 68.7 world-average Mha in build 1) and the energy balance mostly grain, so those readings would move with the window.
* Land source: the 0.01 Mha agreement is FAOSTAT's land use against the ABS holdings (S3, Table S5). The second source in the Monte Carlo is the ABARES land-use raster, which "counts cropland that holdings data does not" and raises short-term capacity 17.3% and long-term 38.2% one at a time (`analysis/sensitivity_2025/README.md`). The variance share is therefore a difference in cropland area between two sources, larger in the long term because the long term is cropland-bound. The paper's S3.8 sentence ("The land bases agree to 0.01 Mha") sits beside the land-source driver without naming the raster.

**3. Does it change a finding?** The land-source answer changes no finding, only a sentence. The window could lower every output-scaled reading (energy balance, own-productivity footprint and HALF, people per hectare, commodity balance) if 2021-23 is above the decade's mean; by how much is not in the records. It would move s3's 65 to 211 and the line (b) closure.

**4. The fair response.** Rebut the land-source premise with a reword; compute the window as a small sensitivity.
* Reword S3 and S3.8: "FAOSTAT's land use and the ABS holdings agree to 0.01 Mha; the ABARES land-use raster, the second land source drawn in the Monte Carlo, counts more cropland than the holdings, which is why the land source carries most of the long-term variance."
* Compute: extract a ten-year FAOSTAT production series (2014 to 2023) from the hash-pinned bulk file and rerun the energy balance and the own-productivity footprint and HALF on the ten-year mean as one row of the robustness table. Builder about 1% (Sonnet), check about 0.5%; it needs the bulk file fetched (network; coordinator or Murray).
* Response letter, land: "The two totals that agree to 0.01 Mha are FAOSTAT's and the ABS holdings'. The second land source in the uncertainty analysis is the ABARES land-use raster, which counts cropland the holdings do not; the text says so."
* Response letter, window: "We have rerun the output-scaled readings on a ten-year mean of production; [result]."
* Cost: about 1.5% plus the fetch.

**5. Dependencies and conflicts.** The window row joins Issue 5's robustness table. The Paper A land referee (R04b, HANDOFF) raised the climate phase of the data windows for Paper A; the two answers should use one series. Mod does not raise this; no conflict. Round status: (i) new for the window and the land-source question; the vintage part extends R03b issue 10.

---

## Issue 13. Literature the journal's readers expect

**1. The issue.** The footprint debate in Ecological Economics, the carrying-capacity forum, trade-adjusted land footprints, feed-food competition, loss and waste, and food-system studies that vary diet, waste and yield together are missing or second-hand (EE M9; Mod M9).

EE names van den Bergh and Verbruggen 1999, Fiala 2008, Kitzes et al. 2009, Monfreda et al. 2004 or Galli et al. 2007, Borucke et al. 2013, Arrow et al. 1995, Daily and Ehrlich 1992 and Kastner's land embodied in trade. Mod names Mottet et al. 2017, Kummu et al. 2012, Alexander et al. 2017, Springmann et al. 2018, Gerten et al. 2020 read directly, van Zanten et al. 2018, Schader et al. 2015, Fader et al. 2013, Porkka et al. 2013, Kummu et al. 2020 and Arrow et al. 1995.

**2. What the records show.** Right in the main; two works are read and cited second-hand all the same, which the referees did not know.
* B119 (decision 111) fetched what it could and listed the rest for Murray (its section 6): van den Bergh and Verbruggen, Fiala, both Kitzes 2009 papers, Arrow et al. 1995, Borucke, Mottet, Springmann, Kummu 2012, Monfreda 2008, Pradhan 2014; none is read. Porkka 2013 (L255) and Alexander et al. 2017 (L256) were fetched and not read. Schader 2015 (L123) is "read, unverified" and not cited.
* Gerten et al. 2020 (L083) was read by B119 (abstract and p. 3), but S2.9 cites it "in Beltran-Peña, Rosa and D'Odorico 2020". Fader et al. 2013 (L105) was read by B119, but S8 cites it "in Clapp 2017". Both can be cited directly.
* Van den Bergh and Rietveld 2004 is cited in section 2; EE asks for its link to the paper's finding in the introduction.
* Decision 92 (8,000 words) means additions displace text or go to the supplement.

**3. Does it change a finding?** No number. Fiala 2008 and the yield and equivalence factor works bear on Issue 1's framing; Kastner's trade-embodied land and Porkka 2013 on Issue 3 and section 8.2; Springmann 2018 and Gerten 2020 on section 6's ordering (Mod asks whether their decompositions agree with Table 8).

**4. The fair response.** Read and reword; Murray fetches.
* Murray fetches the closed works from B119's list (QUT links given there); targeted reads of about 10 works at about 10,000 Sonnet tokens each plus a merge, about 1 to 1.5%. Cite Gerten and Fader directly at once (wording only). Section 2 gains one paragraph on the Ecological Economics footprint and carrying-capacity debate (Arrow et al. 1995; van den Bergh and Verbruggen; Fiala and the Kitzes reply), section 4.5 the yield and equivalence factor convention (Galli or Monfreda; Borucke), section 8.2 the trade-embodied land work, section 6 a sentence on where Springmann and Gerten's diet, waste and yield variations agree with Table 8.
* Response letter: "We have added and engaged with [list as read]. Where a work reports a decomposition of diet, waste and yield, section 6 says whether its ordering agrees with ours."
* Cost: about 1.5% plus Murray's fetches.

**5. Dependencies and conflicts.** Issue 1 (equivalence factors) and Issue 3 (trade). The referees agree and overlap on Arrow. Round status: (ii) in part (B119 fetched and listed under decision 111), (iii) in part (the named works are unread, Murray's fetches pending).

---

## Issue 14. Presentation: placeholders, regeneration notes in captions, mixed Monte Carlo designs, declarations, DOI

**1. The issue.** Figures 1 to 3 and Table 2 are placeholders; captions say files "need regenerating"; Table 4 mixes a 13-setting mirror range with 19- and 18-setting ranges; references carry "[CHECK]"; the AI declaration and CRediT have brackets; the archive has no DOI; captions carry build provenance (Mod M8; EE minor 6, 7, 8, 13, 14).

**2. What the records show.** Right; part of it is fixed in the files and not in the paper.
* Regenerated since the captions were written: `cross_method_local.csv` prints the improved row's widened range 37.9 to 60.0 (B131); `design_choices.csv` prints both widened Monte Carlo rows (31.1 to 49.2 corrected, 37.9 to 60.0 improved, factor 1.58 each); `bases.csv` prints 3,718 kcal, 22 crop items and no "Burnside" label. The captions of Tables 3, 8 and S5 are stale on those points and can lose their notes.
* Open: `make_readme_tables.py` hard-codes "13 uncertain choices" and "21 crops" (X141), so a README regeneration would reintroduce the old strings.
* Mirror range: no widened mirror run exists (S5, B129 note).
* Table 2 and Figure 1: "no catalogue csv or script exists" (drafter notes); Figures 2 and 3 have no plotting script; decision 99 places figures after the text is settled.
* Declarations: decision 120 (AI declaration drafted for Murray's edit) and the B121 points await Murray; decision 131 lifts the Zenodo hold after R04, so the DOI can be in place before submission.
* Section 3's counts: the drafter notes say no csv holds the selection record (counts by route), so the counts cannot be given (EE minor 16; Mod minor 12).

**3. Does it change a finding?** No.

**4. The fair response.** Do it.
* Strip the regeneration notes from the captions of Tables 3, 8 and S5 (files done), fix X141, and move build provenance to one data-availability note (about 0.3% in the patch).
* Mirror: drop the 13-setting range from Table 4 and state it in S5 (recommended, no cost), or rerun the mirror on the widened design (about 2.5%, as B130 and V46).
* Figures and Table 2: the figures job under decision 99 (about 2 to 3%) and a catalogue csv for Table 2 and Figure 1 (about 0.5%).
* References: resolve the "[CHECK]" notes in `qa/references.csv`; replace "Buzby 2010 (cited in Lane 2014)" by the thesis citation form; Wackernagel and Rees 1996 place and edition (about 0.5%, Sonnet).
* Selection record: build a counts-by-route csv from the four route files and the register (about 0.5 to 1%), as R03b issue 14 proposed.
* DOI and declarations: Murray (decisions 120, 131).
* Cost: about 4 to 5% with the figures job.

**5. Dependencies and conflicts.** Follows the compute items, so captions are written one time. The referees agree. Round status: (iii). R03b issues 14 and 15 named the placeholders, counts, DOI and captions; decisions 99, 120 and 131 schedule them; they are not done.

---

## (a) All issues

| # | Referee and number | Round status | Verdict on the premise | Response | Headline effect | Cost (share of the weekly allowance) |
|---|---|---|---|---|---|---|
| 1 | EE M1, minor 1, Q1; Mod M1 (HALF) | (ii) | Right on the footprint; "still lead" mistaken; minor 1 right; Mod right on HALF | Reword: line (b) the footprint's accounting, world-average labelled counterfactual, pooling stated | s3, s4, s5, H2, H3; B156, B247, B347 | about 0.5% |
| 2 | EE M2, Q2; Mod M6 (part) | (iii) | Right that it is the better benchmark; mistaken that a usable Australian row is published | Out of scope with reason; B223 checked and reported (decision 113) | none on the records | about 0.5% |
| 3 | EE M3, Q3; Mod Q1 | (i) | Right; found what the audit did not | Reword: algebra stated; binding reading 53.9 to 77.9 reported | s3 low end 64.8 to 53.9 if joined; 5.14, 7.6, 8.2 | about 0.3% |
| 4 | Mod M1; EE M5 (fish) | (i) | Right on conversions; footprint not a count either | Reword; groupings in Issue 5's table; fish out of the centre | s3 labels; s5 within a few points | inside Issue 5 |
| 5 | EE M5, M4 (i), Q4; Mod M3, Q2 | (ii) | Right | Compute robustness table; reference-free first; reword s5, H2 | s5: line (a) about -1 to 7%, line (b) about 28 to 46% to the model, 9 to 36% to the centre; B276, B277 | about 2% |
| 6 | EE M6; Mod M2, Q5 | (ii) | Right; population point mistaken (again) | Compute line (c); classification table; FAOSTAT model out of scope with a production table | s2 wording; Table 6 gains a row, likely negative | about 3% |
| 7 | Mod M4, Q6; EE M3 (part) | (ii) | Partly: the readings are spans; bridge wanted | Compute all-orderings bridge with pooled-land step; reword s6, H4 | s6, H4, 5.14, 7.6 | about 4% |
| 8 | Mod M5, Q3, Q4, Q8; EE Q9 | (iii) drought; (ii) pasture | Pasture productivity mistaken (the paper misstates it); drought right, records go further | Reword to cite B112 and the README; small one-at-a-time compute | s7, H5; B003, B130, B134, B096, B245; Table 8 drought 2.19 to about 1.03; Table 9 purpose 1 | about 1.5% |
| 9 | Mod M6, Q7; EE M2 (part) | (ii) grades; (iii) authors | Right; decision 5 unexecuted | Reword "after"; act on decision 5 | s2, s3 labels | about 0.3% plus Murray |
| 10 | EE M7, Q5; Mod note 3, minor 4, 8, Q9 | (iii) | Right | Restructure Table 8; A and B for C; exports out of scope; weather-and-waste wording to Murray (decision 122) | s7, H5; 6.11; B182, B194, B333; Table S4 | about 1% |
| 11 | EE M4 (ii, iii), Q8, minor 18; Mod M7 | (ii) | Right; rubric written by the checker, not the author | Reword Table 9 as the author's judgement; other-method table from files; outside raters per decision 113 | s8 | about 1.5% |
| 12 | EE M8, Q6, Q7 | (i) | Window partly right; land source mistaken | Rebut land with a reword; compute ten-year window | s3 and s5 possibly; S3.8 | about 1.5% plus a fetch |
| 13 | EE M9; Mod M9 | (ii) and (iii) | Right; Gerten and Fader read but cited second-hand | Read and reword; Murray fetches | none | about 1.5% plus Murray |
| 14 | Mod M8; EE minor 6, 7, 8, 13, 14, 16 | (iii) | Right; some files fixed, captions stale | Do it | none | about 4 to 5% with figures |

Counting each issue once, by its main part: new 3 (Issues 3, 4, 12); a first-round issue answered and not accepted 7 (Issues 1, 5, 6, 7, 9, 11, 13); a first-round issue the revision did not reach 4 (Issues 2, 8, 10, 14). Issue 8 is mixed: its pasture-productivity part is type (ii), its drought part, which carries the headline effect, type (iii); Issue 9's contact with the authors and Issue 13's unread works are type (iii) parts of type (ii) issues.

All compute and patch items together: about 15 to 18% for the compute and checks, about 2.7% for one patch job (as B126b), about 2.3% for a blind read (as V45b), about 1.5% for a register job, and 2 to 3% for figures: about 24 to 28% of a weekly allowance.

## (b) The changes that would do most to satisfy both referees, in order

1. Carry B112's crop-only drought bound into Paper B beside every weather figure (18.9, 30.8, 5.8 to 6.1%, the 2.19 factor, Table 9 purpose 1) and correct S5 to say pasture output is drawn through the meat window and calibration.
2. Report the harmonised shares with a robustness table and the reference-free measures first, and restate s5 and H2 as "about zero on line (a); about 28 to 46% of the distance to the model on line (b), almost all of it the footprint and HALF at Australian productivity".
3. Present line (b) as the footprint's own accounting, label the world-average readings a counterfactual, state the production-to-consumption algebra, and report the binding-land-type footprint reading (53.9 to 77.9) beside the pooled one.
4. Restructure section 6 into in-model changes, comparisons with external counts and the Monte Carlo, replace diet C by A and B, add the same choices measured in other methods from Table S7 and S3.1, and recast Table 9 as the author's judgement without a finding in the abstract.
5. Compute the two-sided third line (one per-person requirement and waste for methods and model) and the all-orderings bridge from HALF at Australian productivity to the model.

## (c) Where accepting the criticism would be wrong

* Accepting that pasture productivity is outside the uncertainty analysis would be wrong: the README records it as covered by the meat window and the meat calibration, both drawn, because pasture output is national meat output shared by dry sheep equivalent; the supplement's list is what is wrong.
* Accepting that the land-source driver contradicts land totals that "agree to 0.01 Mha" would be wrong: the agreement is FAOSTAT against the ABS holdings, and the drawn alternative is the ABARES raster, which counts more cropland.
* Accepting that the model's population of 27.6 million enters the comparison would be wrong: it enters no method reading and no model capacity, only the failure probability at the 2025 population.
* Accepting that the footprint gives a people count in its authors' hands, as Mod's grouping implies, would be wrong: Wackernagel et al. 1999 give no count of people, and only the energy and protein balance does.
* Accepting that variant 1 "overshoots two of three targets" as a failure of attribution would be wrong as stated: 81.7 lies inside the footprint's pooled span of 64.8 to 84.6 and 3% above HALF's top defensible reading; the bridge is worth running all the same.
* Accepting that the abstract "still leads with" the world-average range would be wrong: under decision 106 it leads with the own-productivity range.
* Accepting that the purpose definitions in S7 were written by the author in the model's terms would be wrong as to authorship: they are the AI checker's reading (V28); their terms are the fair point.
* Accepting that a third line equalising the per-person requirement would narrow the gap to the model would be wrong: every reading the records hold on an intake or requirement basis rises (Table S7; 243 million for the energy balance at 8.8 MJ).

## (d) Questions to the author

From EE:
1. How crop and pasture are combined: summed world-average hectares on both sides, no equivalence factors (Simpson's convention; V07, method-test README).
2. The footprint from the latest national accounts: not in any held source; the public release has no Australian row (`BLOCKED_SOURCES.md`); a secondary whole-footprint figure gives about 39 million for 2022 (B223, unverified); a licence is Murray's call (decision 113). Needs Murray.
3. Why "pasture alone" is out of the headline range, and whether it is the paired reading: a script choice mirroring the secondary row (`harmonised_lines.py`), while it is inside the line (b) closure; accepting it as the paired reading needs Murray, and the records support it (B270).
4. Shares without fish, with one method left out, on 53.6: scratch: without fish 5.9% and 40.9%; one method out -1.1 to 6.8% and 27.7 to 45.9%; on 53.6, 4.7% and 44.4%; needs Issue 5's build and check.
5. The model with exports counted: no run; recommended out of scope with the food-balance rebuild (101 to 104 million) and the footprint's export ratio as comparisons.
6. Why the land source carries 32% when totals agree: the totals that agree are FAOSTAT and the holdings; the drawn alternative is the raster, which counts more cropland (+17.3% short, +38.2% long one at a time).
7. How representative 2021 to 2023 is, and a ten-year window: cereals 55.0, 59.6 and 43.1 Mt in the three years; no ten-year series is extracted; needs Issue 12's job and a fetch of the hash-pinned FAOSTAT file.
8. Outside raters for Table 9: needs Murray (decision 113).
9. Whether 8.0 MJ represents the whole population: it is the NHMRC sedentary pattern (PAL 1.4), drawn to PAL 1.8; age-structure weighting is not stated in the records read; needs a small check of the workbook's diet basis.

From Mod:
1. How own productivity is computed for pasture, and sensitivity to the arid rangelands: national ruminant output at world pasture per tonne (46.4 Mha world-average in build 1, 72.4 on HALF's rules), not by land class; the pasture area does not enter the own-productivity readings, so the rangelands do not move them.
2. How a method's centre is formed and the readings per method: the geometric mean of its paired readings; 6, 6, 1, 3 and 3 readings (README, both classifications).
3. Pasture productivity by zone, its source, and plus or minus 20%: national meat output shared among zones by dry sheep equivalent (`analysis/pasture_2025/README.md`); scratch from B114's closed form, about 33.5 and 49.4 million short term.
4. Whether the drought allowance scales pasture-fed output, and against observed falls: yes, every yield (B112); crop-only gives 41.2, 41.0 and 40.4 million at 1 in 10, 20 and 100; no livestock series for 1982-83 or 2002-03 is held; the single-year series puts 2018-19 and 2019-20 near the median.
5. Why the model is not run on the FAOSTAT layer: its layer is zone-level ABS; a FAOSTAT layer is a new build (session-size); a production comparison table is recommended instead.
6. Variant 1 with protein held: not run; variant 1p reads 87.0 with less protein, and variant 3 (energy and protein held, free allocation) reads 172.3 but was cut by decision 124; a legume variant is in Issue 7's job.
7. Why the HALF and Cassidy authors were not contacted: decision 5 says they should be, before submission; not done; needs Murray.
8. Which judgement settings to defend, and the widest ranges: six are named in S5; PAL 1.2 to 2.2 would give about 48 to 26 million one at a time (scratch, inverse proportion); needs Issue 8's one-at-a-time run.
9. Whether 7.88 is the method or the solver's freedom, and with a cap: the solver's freedom; the records hold capped variants A (85.5, 1.60) and B (202.1, 3.77), and the nutrition README says A is the one to quote.

## (e) Minor issues, grouped by kind, with the fix for each kind

* **Readings stated inconsistently or without their basis** (EE minor 1, 2, 4, 5, 10, 17; Mod minor 5, 6, 9): the world-average range starts at the energy balance; the 211 is a 1990-91 scale-up; Foran and Poldy's 30 and 77 (1997-98 production, 2050 requirement) against 40 and 41 (2021-23); people per hectare given five ways; 396.1 Mha (2011) against 363.5; Table S2's 0.30 and 5.93 ha against Simpson's 1.758 ha; "release land". Fix: one readings table in S3 listing each reading with its land base, year, pairing and harvest matching, cited from Tables 3, 5 and 7.3; take the energy balance out of the secondary group; state the years at 5.12; add Simpson's 1.758 and Wackernagel et al. 1999's figures beside Table S2.
* **Regeneration notes and production detail in captions** (EE minor 6, 8; Mod M8 part, minor 7): fix as Issue 14; Table 5's "(p. 78)" becomes "Wackernagel and Rees 1996, p. 78" in the caption.
* **Placeholders and declarations** (EE minor 7, 13, 14; Mod M8): figures job (decision 99); catalogue csv for Table 2; AI declaration model names and CRediT name from Murray (decision 120); DOI (decision 131).
* **Span and anchors** (EE minor 3; Mod minor 1): H1 gains "two soft ends"; Mod's alternative span ("10 to 110") would amend decision 118's Q9 reading and B005, so it is Murray's; recommended reply: "Section 1 states that both ends are soft and why; the highlight now says so."
* **Model detail queries** (Mod minor 2, 3, 4, 8): waste's factor of 1.33 against a 1.14 ceiling (the waste README shows about 1.3 million people a percentage point, near linear; the mechanism needs a small check); the non-linear pasture per person between guideline diets (the binding land switches from pasture to cropland below about 5.5%, V19's half-point steps; a sentence in S4); diet C as an upper bound (Issue 10); drop 2.22 (Issue 10).
* **Wording, units and names** (EE minor 9, 11, 12, 15; Mod minor 10, 11, 13, 14, 15, 16): tense of section 6's opening; one competing-interests statement; one primary energy unit (MJ, kcal in brackets); distinct names for the three "balances"; the failure column labelled "the model, failure view"; Kinnunen's crop set named; keep 6.6's framing of the Jones committee and cut 5.8's; trim the abstract. Fix: one editing pass to the style sheet R03b proposed.
* **Review reporting** (EE minor 16; Mod minor 12): counts by route from a selection csv (Issue 14).
* **References** (EE minor 13; Mod minor 17): "[CHECK]" notes, Buzby, Wackernagel and Rees place and edition; Gerten and Fader cited directly (Issue 13).

## (f) Register rows touched, and the wrong-value check

Register rows touched: none.

Wrong-value check: *Example, deliberately wrong, not to be used:* "We accept the referee's point that the footprint's 'pasture alone' readings play no part in the harmonised comparison, and have included them." This would concede something the records show to be false: on line (b) the pasture-alone readings (53.9 and 77.9 million) are two of the footprint's six paired readings in `harmonised_comparison_lines.csv` and enter the 38.5%; they are left out only of the headline range of 64.8 to 117.0 (`harmonised_lines.py`, primary footprint row).

## (g) Decision table for the author

Costs are shares of the weekly allowance on the HANDOFF calibration (1% per 150,000 logged tokens), builders and blind checks included.

| # | Option | Recommendation | Confidence | Cost | Reason |
|---|---|---|---|---|---|
| 1 | Carry the crop-only drought bound (B112) into Paper B at every weather figure; S5 says pasture output is drawn through the meat window and calibration; one-at-a-time pasture output plus or minus 20% and PAL 1.2 and 2.2 | Yes | High | about 1.5% | Paper A says it and Paper B does not; the 18.9 and the failure probability rest on an untested rule; S5 contradicts the README |
| 2 | Robustness table for the shares; reference-free measures lead Table 6; s5 and H2 restated as ranges | Yes | High | about 2% | Both referees ask; my scratch reading says line (a) holds near zero and line (b) is a range driven by two methods |
| 3 | Line (b) presented as the footprint's own accounting, world-average readings as a counterfactual, algebra stated, binding-land-type reading (53.9 to 77.9) beside the pooled one (amends decision 105's symmetry) | Yes | High | about 0.5% plus a register job | No compute; the values are registered (B270); EE's strongest point |
| 4 | Restructure Table 8 into three panels, A and B for C, ladder dropped, other-method factors added; exports through the model out of scope | Yes | Medium | about 1.5% | R03b's proposal not taken; the other-method factors answer Mod M7 from files; an export module is session-size for a comparison a label can carry |
| 5 | Weather-and-waste sentence: state the two changes one at a time (amends decision 122) | Yes, with the crop-only bound in brackets | Medium | none | Both referees read it as a range; the figures stay |
| 6 | Table 9 as the author's judgement, one model column, no finding in the abstract; outside raters optional (decision 113) | Yes to the recast; outside raters at your choice | Medium | about 0.3% (recast) | Meets Mod's stated alternative and most of EE's; raters add delay |
| 7 | Contact the HALF and Cassidy authors (decision 5) | Yes | High | your emails; no spend | Standing decision; settles the fidelity residuals the referees cite |
| 8 | Third line: one per-person requirement and waste for methods and model | Yes | Medium | about 2.5% | Both referees ask; the expected direction (wider) should be stated in advance |
| 9 | Model on the FAOSTAT layer | No; a production comparison table and "common land base and food balance" in s2 | Medium | about 1% (the table) against 4 to 6% | The data claim can be made true by wording; a new layer is a new model input |
| 10 | All-orderings bridge from HALF at Australian productivity to the model, with the pooled-land step and a protein-held variant | Yes | Medium | about 4% | Turns "consistent with" into an attribution; reuses B111 and B114 machinery |
| 11 | Ten-year production window as a robustness row | Yes | Medium | about 1.5% plus a FAOSTAT fetch | Partial records hint that two of the three years are high; one row answers EE Q7 |
| 12 | National accounts reading: B223 checked and reported as secondary; licence not sought (decision 113) | Yes | Medium | about 0.5% | The public release has no Australian row |
| 13 | Literature: fetch and read the listed works; cite Gerten and Fader directly | Yes | High | about 1.5% plus your fetches | Decision 111; both referees; within the word limit by displacement |
| 14 | Presentation: captions cleaned, X141 fixed, mirror range dropped, figures and Table 2, selection counts, references, declarations, DOI | Yes; mirror rerun not needed | High | about 4 to 5% (figures 2 to 3%) | Mod lists it as a condition for one further round |
| 15 | One patch job, a blind read and a register job after items 1 to 14 | Yes | High | about 6.5% | The changes move abstract sentences and Tier A rows (B003, B130, B156, B247, B276, B277) |

**Recommended combined action:** in order of priority, yes to 1, 2, 3, 6, 7, 13 and 14 (wording and small compute, about 10%); yes to 4, 5, 8, 10 and 11 (about 9%); and 15 to close. Rows 5 and 6 (decisions 122 and 113) need an answer before the patch brief is written.

## (h) Whether a third round would be needed

After these changes a third referee round on Paper B is worth running, but a short one: the two Paper B personas only, about 1% each, after the patch, the register job and the blind read. The reason is not that the referees' requests would be left open; it is that several answers move abstract sentences and Tier A values (the drought figures behind s7 and B130, the shares in s5, the world-average range in s3, the section 6 ordering), and two new analyses (the third line and the bridge) produce numbers no referee has seen. Mod states that one further round should suffice if its five points are answered and the presentation is fixed; on this plan all five are answered, four by computation or file and the independence point by recasting Table 9 under decision 113. EE's list is answered in the same way, except the national-accounts reading, which is declined with a reason a referee is likely to accept. If Murray takes only the wording items (1, 3, 5, 6, 12, 14) and declines the compute items, a blind read in the V45b form would serve in place of a referee round, but EE M5, EE M6, Mod M2 and Mod M4 would be answered by argument alone, which both referees have signalled they will not accept.
