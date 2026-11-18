# R03b: a reasoned response plan to the two referee reports on Paper B (methods)

Brief: `qa/briefs/R03b_response_plan_B.md`. Reports answered: `qa/reports/R02c_review_B_ecological_economist.md` (called EE below) and `qa/reports/R02d_review_B_modeller.md` (called Mod). Draft tested: `papers/B_methods/draft/paper_B_draft1.md`, `supplementary.md`, `highlights.md`, `references.md`. No file other than this report was changed. No register row was touched.

**How to read this.** Each block tests a referee's premise against the records first, then says what would move in the abstract and highlights, then gives the fair response. Where I computed something to test a premise, I did it in my scratch folder from committed csv files only, and I say so: those figures are an analyst's reading, not registered claims, and each needs a builder and a blind check (Card, verification rules) before any of it enters the paper. Costs are given as a share of the weekly allowance on the HANDOFF basis (about 1% per 150,000 Opus-weighted logged tokens); the comparable logged jobs are B58, the harmonised comparison (278,334 tokens, about 1.9%), and V26, its blind check (222,761, about 1.5%).

**The short answer.** Both referees are right that the paper's central sentence, "the gap between the methods is the method", depends on where the line between input and method is drawn, and that the line chosen (decision 35) keeps the productivity basis on the method side. On that line the finding holds even on an anchor-free measure. Moved across the line, it does not: my scratch reading puts the input share near 41%, not 10%, and the spread among the methods narrows by about a third. Both referees are also right that the "three to eight times the model" sentence rests on the footprint and HALF read in mixed units, and that the pairing explanation has not been tested. Several of their factual premises are wrong, and the records say so: the diet is in the Monte Carlo, crop yields and pasture output are in it, the drought record is not treated as stationary, the population mismatch does not enter the readings, and three published counts, not one, are reproduced by an implementation in the records.

Abstract sentences are numbered as the draft's claims file numbers them (`B_s01-03_claims.csv`, section "abstract"): s1 the span; s2 "the spread is produced mainly by what each method counts"; s3 seven methods on one data set; s4 "134 to 343 million, about three to eight times the model"; s5 "Equalising inputs did not narrow the spread ... about 10% of each reading's distance ... the gap between the methods is the method"; s6 the design choices "measured one at a time in the model"; s7 "18.9 to 55.3 million ... a factor of 1.26". Highlights are H1 to H5 in the order of `highlights.md`.

---

## Issue 1. The input and method line decides the headline

**1. The issue.** Holding every method's defining choices fixed and equalising only its other inputs cannot be expected to remove definitional differences, so "the spread does not narrow" confirms the design; and world-average against Australian productivity is a land-productivity input, not part of the method (EE 3.1, first part; Mod M1).

EE: "Equalising data while preserving definitions cannot be expected to remove definitional differences, so 'the spread among the methods does not narrow' (section 5.11) is a confirmation of the design rather than a finding." Mod: "Whether a hectare is valued at world-average or Australian yields is, in the vocabulary of a land-use modeller, an input ... not a property of the accounting identity. Reclassify it and the bulk of the gap moves from 'method' to 'data'."

**2. What the records show.** The referees are right on the premise.
* Decision 35 (`qa/DECISIONS.md`) set the boundary: every method on one population, data year, land base and consumption data, "each keeping its defining choices (productivity basis, diet treatment, exports, item reading, weather record)", with the footprint at Australian productivity "shown as the one sanctioned sensitivity". Murray accepted the framing on the interim table: "equalising inputs removes the spread within each method but not the gap to the model, so the gap is the method". The README's Limits paragraph says the same: "the table measures the input effect and leaves the method effect whole" (`analysis/method_tests_2025/README.md`, harmonised comparison section).
* Mod's narrower point, that little was changed, also holds. In `harmonised_comparison.csv` the "inputs equalised" cell for footprint builds 1 and 2 and for HALF reads "none needed": those builds were on FAOSTAT 2021-23 and the common land and consumption from the start, so their input factor is 1.00. The inputs that did change moved the energy balance by 0.69 to 1.11, people per hectare by 0.59 to 0.77, footprint build 3 by 1.07 to 1.42 and the commodity balance by 0.71 to 1.03.
* My scratch reading of the same csv with the productivity basis moved to the input side (column (e) taken as the harmonised reading where it exists: footprint builds 1 and 3, HALF): the input share of the distance to the corrected model rises from 9.6% to about 41%; the standard deviation of the log readings across the five method means falls from 0.64 as run to 0.45, and the highest over the lowest method mean falls from 6.2 to 3.7. On decision 35's line the same measure is 0.64 as run and 0.69 harmonised, so no narrowing. So the finding is true on the paper's line and false on the referee's line; neither line is wrong, but the paper presents one as if it were the only one.

**3. Does it change a finding?** Yes. Abstract s2 and s5 and H2 and H3 (claims B276, B277) are true only on decision 35's classification. On the alternative the input share is about four times larger (about 41% against 10%) and the spread among methods narrows by roughly a third in log terms. Section 9.1 ("Published estimates differ mainly because of what each method counts") would need the same qualifier. The local-productivity readings themselves (B270, B272: footprint 64.8 to 84.6, HALF 76.0) do not change.

**4. The fair response.** Reword and compute.
* Reword (recommended in every case): state in section 5.11 and the abstract that the harmonisation holds each method's defining choices fixed by design, name the productivity basis as one of them, and give a one-sentence rule for what counts as an input (a quantity the method takes from data that another method could be given) and what counts as the method (a choice that defines what is counted). A response letter could say: "We agree that the result depends on where the line is drawn. The paper drew it at the method's defining choices, and we state that rule before the results and report the attribution under a second classification that treats the productivity basis as an input."
* Compute: extend the summary block of `analysis/method_tests_2025/harmonised_comparison.py` (lines 198 to 208) to write the attribution under both classifications, from the csv it writes; no new method run is needed, because column (e) exists for the readings concerned. Cost: about 1% for the builder and about 1% for a blind check. This shares a job with Issue 2.
* Two defensible headlines follow, and Murray chooses between them, because changing the direction of a paper is always asked (Card) and decision 35 is his: (a) keep "the gap is the method" and qualify it with "on a classification that keeps the productivity basis as part of the method; treated as an input, inputs account for about two fifths"; (b) drop the slogan and lead with the range of shares across classifications. I recommend (b): both referees raise this as their first point, and a reviewer at Ecological Economics will accept a result reported under two stated classifications but is unlikely to accept a slogan that one of them reverses.

**5. Dependencies and conflicts.** Depends on Issue 3 (which footprint and HALF readings are primary) and feeds Issues 2 and 8: once the productivity basis is an input, what remains between the adjusted footprint and HALF and the model is the pairing, which Issue 8 tests. The referees agree.

---

## Issue 2. The 10% statistic: formula, anchor, row set, "each", and a range statistic set by two cells

**1. The issue.** The ratio-scale decomposition behind the 10% is not defined in the paper, is measured as distance from the author's corrected model, depends on the rows chosen (10 to 18%), is not true of "each" reading, and is paired with a range (12 to 343) that two extreme cells fix (EE 3.1, parts b to d, and Q1; Mod M2, Q1).

EE: "The main text does not define the ratio-scale decomposition, the row sets, or why distance from one tested method, rather than dispersion among all of them, is the right quantity." Mod: "'each reading's distance' in the abstract is wrong: the 10% is an aggregate."

**2. What the records show.** Right on every count, with one correction.
* The formula exists in the records but not in the paper or supplement. The README bullet "Equalising the inputs leaves every method on the side of the model where it was" and the script comment at `harmonised_comparison.py` lines 199 to 205 define it: each reading's ratio to the corrected model, a over 41.5, is the input factor (a over b) times the method factor (b over 41.5) exactly; per method, the mean absolute log of each factor over its readings; methods weighted equally; inputs 0.14 and method 1.35, so 9.6% of the two together (10.1% of the distance itself, V26). The referees could not find it because it is not in the submitted files.
* The 10 to 18% comes from V26 (`qa/reports/V26_harmonised_recheck.md`, section B4): "Before opening the files I tried 24 other definitions, which gave 10% to 18%"; dropping rows where a equals b gives 11.6%, and taking Henry and Godden's 45.7 Mha case as its only as-run reading gives about 14 to 17%.
* "Each" is wrong. Per method, from the same csv (my scratch reading of the signed mean logs), the input share runs from 0 for HALF to about a quarter for people per hectare, and for the commodity balance, whose harmonised meat reading sits at the model's figure, most of its small distance is input.
* Anchor: my scratch reading gives 10.9% with the improved model as the anchor and about 20% with the median of the five harmonised method readings as the anchor.
* Anchor-free dispersion: the standard deviation of log method means is 0.64 as run and 0.69 harmonised; over all 21 readings it is 0.70 and 0.75; with the fish and pasture-alone rows removed it is 0.47 and 0.46. So the "does not narrow" result survives an anchor-free measure and the removal of the extreme cells, on decision 35's line (but see Issue 1).
* The range statistic: both ends are single cells. A finding the referees did not make: the text's "12 to 343 million as run" uses the fish reading on actual 2021-23 use (B151, pending gate 4 in B277), which is the harmonised input in all but name, while Table 5 column (a) prints fish as 17. So the as-run and harmonised lows are the same reading, and the text and Table 5 disagree. The fish reading is also a single-year value repeated across 2021 to 2023 (defect X040).

**3. Does it change a finding?** Abstract s5 and H3 (B276): "about 10%" becomes about 10 to 20% across anchors and row sets on decision 35's line, and about 41% on the alternative line. "12 to 343 as run and harmonised" (B277) should give way to a dispersion measure; its message (no narrowing) holds on decision 35's line. Section 9.1 repeats both.

**4. The fair response.** Compute, then reword.
* Compute: in the same extension of `harmonised_comparison.py` as Issue 1, write (i) the formula, (ii) the share under three anchors (corrected model, improved model, cross-method median), (iii) the share on each of V26's row sets, (iv) the standard deviation of log readings as run and harmonised, with and without the model rows and the two extreme cells, and (v) a two-way split on signed log readings (method by input set). Because a over 41.5 equals the product of the two factors exactly, a two-factor Shapley split on signed logs equals the sequential split, so the Shapley form EE asks for costs nothing extra; the difference from the paper's figure is only that the paper averages absolute values. Mod's fuller design (input sets defined in advance: 1990-era against 2021-23 data, FAO against ABS land, intake against supply) needs new method runs for the 1990-era and intake sets and belongs with Issue 10. Cost for (i) to (v): about 1% builder, about 1% blind check (B58 and V26 are the scale; this is smaller).
* Reword: abstract s5 should read, in substance, "On a ratio scale, inputs accounted for 10 to 20% of the methods' distance from the model, depending on the anchor and the rows, with the productivity basis counted as part of each method." Drop "each". Put the formula in section 5.11 in one sentence. Replace "12 to 343 as run and 12 to 343 harmonised" with the dispersion figures, and fix the Table 5 column (a) fish cell or the text so they agree.

**5. Dependencies and conflicts.** Shares the computation with Issue 1; the final figures depend on Issue 1's classification and on Issue 10 if an intake basis is added. The referees agree; Mod asks for more (input sets in advance), EE for less (Shapley or ANOVA); EE's is the cheaper one to satisfy first.

---

## Issue 3. The footprint and HALF capacity readings mix actual and world-average hectares

**1. The issue.** Dividing Australia's physical hectares by a footprint expressed in world-average hectares gives 146 to 343 and 276 million; the footprint's own national accounting would compare like with like, and the paper's own local-productivity adjustment brings the readings to 64.8 to 84.6 and 76.0 million, so "three to eight times" should be "roughly 1.5 to 2 times" (EE 3.2, Q2, Q8; Mod M1 in part, minor 5 to 7).

EE: "That divides physical hectares by world-average hectares ... The column headed '(a) As the authors would run it' in Table 5 therefore does not contain the reading the footprint's authors would produce; column (e) is closer to it."

**2. What the records show.** Right on the units, partly right on the size of the correction.
* The paper says itself (section 4.5) that Wackernagel et al. 1999 put footprint and bio-capacity "both in hectares of world-average productivity, not of the nation's own land (pp. 377, 380, 386)". The capacity readings in Table 3 do not follow that convention. The adjusted readings exist and are verified: B270 (footprint, column (e), build 1 together 64.8, build 3 together 84.6) and B272 (HALF 76.0; V26 notes other defensible readings span 73.7 to 79.3).
* The referee's "roughly 1.5 to 2 times" is true for the footprint and HALF only: 64.8 to 84.6 over 41.5 is 1.56 to 2.04, and HALF is 1.83 (over the improved 53.6: footprint 1.21 to 1.58, HALF 1.42). The energy and protein balance and people per hectare do not use world-average hectares at all: both count Australia's own production or delivered calories. They stay at 134 to 211 and 145 to 183 million as run (3.2 to 5.1 times the corrected model) and 145 to 149 and 111 to 113 harmonised (2.7 to 3.6 times). So "the aggregate methods" fall to about 65 to 211 million, about 1.6 to 5 times, not 1.5 to 2.
* Column (e) counts Australia's output with exports included and does not convert non-food crops, which understates world-average cropland a little (README Limits). It is still the footprint's own adjustment (Wackernagel and Rees 1996, p. 78).
* Mod minor 6 is right that column (a) is not what the authors ran: it is each method's own setup (land-base scaling, consumption factor) on the common 2025 data.
* Current National Footprint Accounts: the records hold no official Australian row. `BLOCKED_SOURCES.md`: the Global Footprint Network's public platform has no Australia; Lin et al. 2018 and Wackernagel et al. 2002 report no Australian row. The comparators README and B223 (unverified, secondary for 2022) hold ratio readings in consistent units: about 27 and 30 million for the 1990s and about 39 million for 2022, all consumption, not food only. These are close to the model, not above it.

**3. Does it change a finding?** Yes. Abstract s4 (B019, B046, B068, B083, B156) and section 7.6 (B247) move from "134 to 343 million, about three to eight times the model" to about 65 to 211 million, about 1.6 to 5 times, with the footprint and HALF at about 1.6 to 2.0 times. Section 5.10's grouping holds. The direction (the aggregate methods read above the model) holds on every basis in the records except the whole-footprint ratios (27 to 39 million), which are not food-only and are unverified.

**4. The fair response.** Reword, with one compute item that is blocked.
* Option (a): make column (e) the primary footprint and HALF capacity reading and show the world-average division as a labelled counterfactual. Option (b): keep the world-average division primary, as decision 35 set it, with the adjustment beside it. I recommend (a). The values exist and are verified, the footprint's own national practice supports it, and an Ecological Economics footprint reader will not accept (b). Murray decides, because decision 35 names the adjustment "the one sanctioned sensitivity" and the abstract value is a Tier A statement (decision 63, gate 4).
* Proposed abstract s4: "Read as capacities with the footprint and HALF at Australia's own productivity, the aggregate methods give about 65 to 211 million, about 1.6 to 5 times the model; the footprint and HALF read 65 to 85 million." Rename column (a) "Each method's own setup, on the common 2025 data". Label every footprint hectare as actual or world-average (EE minor 7).
* Current National Footprint Accounts: out of reach on the records. Needs Murray (a data licence from the Global Footprint Network, which may cost money and is always asked). The paper should say so in one sentence and quote the published Australian footprints and the derived ratios as illustration, as the comparators README recommends.
* Cost: wording and table regeneration, about 0.5% (Sonnet), plus a register job for the restated B156 and B247.

**5. Dependencies and conflicts.** Feeds Issue 1 (the reclassified harmonised readings are column (e)) and Issue 8 (the residual the pairing must explain is the gap to column (e)). Conflicts in direction with Issue 10: moving all methods to an intake basis raises the energy and calorie readings and widens their gap to the model. The referees agree; EE asks for the NFA rows, Mod does not.

---

## Issue 4. The tested methods and the published figures they are meant to explain

**1. The issue.** Most tested methods do not produce a published Australian people count, so the paper explains a span it partly constructs; Table 1 should map each published figure to the method or design choice that reproduces it (EE 3.3, Q4).

EE: "Of the seven methods tested, only the energy and protein balance reproduces a published Australian people count."

**2. What the records show.** Partly right. The mapping the referee asks for exists: `analysis/comparators_2025/harmonisation.csv` has the columns `closest_model_run` and `comparable_to_model` for every published estimate, and Table 1 left them out. Reproduced by an implementation in the records: Henry and Godden's 109 and 96 (the energy balance, from their printed totals, section 5.3); Gifford's 82 and 60 (through Henry and Godden's factors, so by construction); the author's 40.45 and 9.43 million (the thesis method as built, release 2011 mirror, `analysis/sensitivity_2025/README.md`, against the thesis's 40,450,144 and 9,431,487); and the CSIRO and UQ "around 100" (rebuilt from the food balance as 101 to 104 million without feed as a domestic use, 68 to 70 with it, `analysis/comparators_2025/proportional_count.csv`; this rebuild is not in Paper B). Matched in scale, not reproduced: Jones 30 to 35 (the model's 30.8 at 1 in 10). Derived here, with no authors' figure: Foran and Poldy 30 to 32. No method to run: Taylor, Borrie, the National Population Council (judgements, second-hand), PMSEIC (no source), Bellotti (a proportion, which the proportional rebuild could reproduce but has not). So the referee's "only the energy and protein balance" is wrong; three published counts are reproduced and a fourth is reproducible.

**3. Does it change a finding?** Section 1's "The paper finds that the published spread is produced mainly by what each method counts" and abstract s2 overreach for the five figures with no method behind them. No number moves.

**4. The fair response.** Reword, with a small table addition. Add a column to Table 1, "Reproduced by", filled from `harmonisation.csv` and the proportional rebuild, and a note naming the figures no tested method reproduces. Restrict section 1's sentence to "the readings generated here and the published figures that a tested method or design choice reproduces". Consider using the proportional rebuild (101 to 104) in place of the published 100 in Table 6 (see Issue 7). Response letter: "We have added the mapping. Three published counts are reproduced by an implementation (Henry and Godden; the thesis; the CSIRO and UQ count, rebuilt from the food balance), one is matched in scale, and five rest on judgement or carry no method; the claim is restricted accordingly." Cost: about 0.5% (Sonnet table edit and claims rows) plus a check.

**5. Dependencies and conflicts.** Links to Issue 11 (the span) and Issue 7 (the export row). No conflict between referees; Mod does not raise it.

---

## Issue 5. The author's model is privileged in the design

**1. The issue.** The model is the anchor of the comparison, the only method given a sensitivity analysis, scored twice through the failure view, and rated well suited for all four purposes in the author's own Table 7; disclosure does not cure the design (EE 3.4, Q6; Mod M9, M8 part (a), Q9).

EE: "The paper ... states that 'it was tested by the same procedures as every other method' (section 9.5). It was not, in four respects." Mod: "disclosure does not remove the design problem."

**2. What the records show.** Mostly right; two premises need correction.
* Anchor: right (Table 5 column (d), B276, B156).
* Only sensitivity: partly right. No other method has a Monte Carlo, but the records give the others ranges of their own: the energy balance across three land bases (the land base alone moves it 31%, S3.1), three footprint builds (S3.2), two independent Cassidy builds (within 5 to 8%), HALF's defensible local readings of 73.7 to 79.3 (V26), and the commodity balance on two consumption bases. The paper does not present these as sensitivity.
* Failure view counted twice: right, and the paper concedes it (section 5.8: "applied as a test of the idea, not as an independent method"; 7.8; the audit's V32b problem 3). The abstract's "Seven well-known methods" (s3) still counts it.
* Table 7: the "second reader" is V28 (`qa/reports/V28_section7_matrix.md`), a blind checker session on a model, not a person (decision 3; `qa/spend.csv` logs it as an Opus job). It stated its rule before rating (V28 section 1: well suited when the tests show the method sees what the purpose turns on; partly with a stated limit that touches the core; not suited when it cannot see it), rated from the test READMEs and the claims register without seeing the draft, and showed its check could fail (a planted wrong cell). It agreed on 25 of 28 cells; my scratch Cohen's kappa on the two matrices is 0.83. The three differences were judgement calls, all on other methods, all moved them up from "not suited" to "partly", and all were adopted (decision 69). It agreed on all four of the model's cells, while calling the model's regional-planning rating "a judgement call (partly is defensible)". The paper reports none of this. Decision 5 (outside readers: the HALF and Cassidy authors and a land-use planning colleague, "asked after our own checks pass") was approved; the records show no request made, and decision 17 records that Murray chose not to approach Simpson and Lowe.
* Section 9.5's "tested by the same procedures as every other method" does not match the records: the model is the anchor, carries the only Monte Carlo and is the instrument of section 6. The Card's standing decision states the model is "tested and critiqued by the same tests and then built on"; the sentence should say what was done.

**3. Does it change a finding?** No reading moves. The abstract's "Seven well-known methods" (s3, B242) becomes "five published methods and the author's model, read two ways". The model's "well suited" column in Table 7 and section 7.3's justification are at risk if independent raters disagree. The anchor-dependent sentences move with Issue 2.

**4. The fair response.** Reword, with one item for Murray.
* Publish the rubric (V28's rule) in section 7.1 before the table; say the second reader was a blind AI checker given the test records and not the draft, with 25 of 28 agreement and the three differences adopted; label the failure column "the land-and-diet balance, read through Fearnside's frame" or merge it; add a row or note to Table 7 carrying the model's own limits from section 8 (no trade, no herd-cycle risk, unsourced constants). Rewrite 9.5 to: "The model tested here is the author's own. It was run on the same data and checked against its own published figures as the other methods were; it was also the reference for the comparison and the instrument of section 6, which no other method was." Add the neutral anchors of Issue 2 as a column. Present the other methods' build and case ranges as their sensitivity, in one sentence.
* Independent raters: decision 5 asks for outside readers. Needs Murray: whether to ask two named people to rate from the rubric (a few emails, no spend; sending anything outside is always asked). If no independent ratings can be had, move Table 7 to the discussion labelled as the author's view, as EE allows. A reviewer will likely accept the published rubric plus the honest description of the AI second reader plus at least one human rater; disclosure alone is unlikely to satisfy either referee.
* Cost: wording about 0.5%; a repeat of V28 by a second independent checker session for a three-way agreement figure, about 1% (V28 logged 157,589 tokens).

**5. Dependencies and conflicts.** Depends on Issue 2 (neutral anchors) and Issue 6 (the model's own sensitivity). The referees agree; EE offers the fallback of moving Table 7 to the discussion, Mod does not.

---

## Issue 6. Definitions against settings, and how wide the Monte Carlo is

**1. The issue.** The contrast between a definitional span of 18.9 to 55.3 million and a factor of 1.26 "across defensible settings" depends on an unstated rule for what is a definition and what a setting; the Monte Carlo is narrow, author-chosen, dominated by one judged choice, leaves out the uncertainties a modeller puts first, does not state its estimator and reports no interactions; "only 1.26" overstates robustness (EE 3.5, Q5; Mod M4, Q4, Q5).

EE: "Read this way, 'only 1.26' (highlight 5) is a statement about a narrow and author-chosen distribution, not about the robustness of the model." Mod: "The analysis leaves out the uncertainties a land-use modeller would put first: pasture productivity ..., crop yields and their trend ..., the classification of FAOSTAT permanent meadows and pastures, nutrient composition and the energy requirement per person, and structural choices such as the fixed diet."

**2. What the records show.** Right on the rule, the narrowness, the judged ends and "only"; wrong on three specific omissions.
* The rule is not written anywhere. The nearest is section 6's opening: each design choice is "set at the ends the methods of section 4 take". That is a rule (a definition is a choice on which published methods differ; a setting is an uncertain value within one definition), and it can be stated.
* What is drawn (`analysis/sensitivity_2025/monte_carlo.mjs`, header): the meat-and-egg share of the diet (triangular 0.115, 0.12, 0.13) and the red-meat share (0.528, 0.578, 0.64); the field-crop group factor (plus or minus 14%) and the vegetable, fruit and nut factors (plus or minus 20%), the measured errors of the yield-trend rule; the organic yield factor (0.771 to 0.845, Ponisio et al. 2015); fuel, biofuel, timber; the organic share of land; the herd-and-meat data window; and three long-term choices. So EE's "diet ... excluded" is wrong (the observed diet's composition is drawn; alternative diets are not), and Mod's "crop yields" and "pasture productivity" omissions are wrong in part: crop yield measurement error is drawn, and in this model pasture productivity is national meat output shared among zones by dry sheep equivalent (`analysis/pasture_2025/README.md`), so the meat-data window is the pasture-output uncertainty. Not drawn: the waste rate, the energy requirement, conversion factors, climate trends in yields, and the land source.
* The records hold one-at-a-time values for two of the omissions: the land-use raster instead of ABS holdings raises short-term capacity 17.3% and long-term 38.2%; ABS meat tables uncalibrated lower it 7.0% (sensitivity README ranking table). These are larger than most drawn choices.
* Estimator: first-order indices by binning, 20 equal-count bins (3 groups for the meat window), with the binning noise subtracted (`summarise_mc.py`, lines 6 to 7). The first-order shares add to 101 to 104%, so within the drawn ranges the choices act almost separately. Total-order indices are not computed. The paper does not state the estimator.
* Min to max, from the draws (my scratch reading of `monte_carlo_draws_2025-fixed_all.csv`): 34.6 to 47.7 million, a factor of 1.38 (1.45 improved, 1.35 mirror). Within the base meat window alone: 38.7 to 44.8, a factor of 1.16.
* The 1.26 is mostly where the meat data window sits in the herd cycle. The single-year capacity across 2016 to 2025 runs 43.5 to 55.4 million (A317, a factor of 1.27; unverified, and on a different release, so a pointer, not a figure to quote). With full-cycle windows only, the short-term range narrows (42.5 to 52.9 becomes 46.0 to 50.8 on the earlier base, sensitivity README).
* The five judged range ends are stated in S5 and the README. The method references (McKay et al. 1979; Helton and Davis 2003; Saltelli et al. 2008) are "record only" in the register (L235 to L237).

**3. Does it change a finding?** Abstract s7 and H5 (B116, `results/ranges_2025-fixed.csv`): "defensible settings" and "only" go. The factor itself stays 1.26 as a 5th to 95th percentile of the draws; with min to max it is 1.38. A wider analysis with waste drawn would widen it: the waste choice alone moves the answer by 1.33 on the corrected release (Table 6), so a draw across a sourced waste range will add materially. The contrast with the definitions (B003, H4) survives in direction on every reading the records hold, but the gap narrows once waste is treated as uncertain. Q8 (18.9 against 15.6 as the low end of the definitional span) is still open with Murray (digest D3; scope Q8): the draft follows the scope's option (a), the digest recommends 15.6.

**4. The fair response.** Reword in all cases; compute if Murray accepts the cost.
* Reword: state the rule in section 6's first paragraph; replace "defensible settings" with "the settings varied here"; drop "only" from H5; give both the 5th to 95th (1.26) and the min to max (1.38); say that 81% of the variance is one judged choice, the meat data window, which places the data in the herd cycle; state the estimator in S5; list what is not drawn. Response letter: "We have stated the rule. The observed diet's composition and crop and livestock output are drawn; alternative diets are treated as definitions because published methods differ on them, and we say so."
* Compute: widen `monte_carlo.mjs` to draw the waste rate (a sourced Australian range from `analysis/waste_2025`), the land source, the meat-table calibration, an energy requirement range, and a crop-yield trend term from Hochman et al. 2017; compute total-order indices with a Saltelli or Jansen estimator (N times (k plus 2) evaluations; at 1,000 base draws and 17 choices about 19,000 evaluations, which the model's evaluator handles in a single run); report min to max. Cost: about 2 to 2.5% builder, about 1.5% blind check, plus about 0.3% for targeted reads of the three method references (Murray fetches them; QUT links per the Card). Option (b), reword only, costs about 0.3% but Mod will not accept it; EE might. I recommend both.

**5. Dependencies and conflicts.** Shares runs with Issue 7 (a factorial over the in-model choices) and Issue 10 (an energy requirement range). EE wants the diet and waste drawn as uncertain; Mod wants the diet kept as a structural choice but bounded for acceptability (Issue 7). These are compatible once the rule separates the observed diet (a setting) from alternative diets (a definition).

---

## Issue 7. Table 6 compares unlike objects, ignores interactions, and ranks an unconstrained optimum first

**1. The issue.** Table 6 mixes releases, compares the model with external counts in three rows, bundles five choices in the time-frame row, ranks a freely optimised diet as the largest design choice, and treats one-at-a-time factors as orderable although the diet results show strong non-linearity; the ladder cannot support an ordering (EE 3.6; Mod M5, M11 in part).

EE: "In such a model one-at-a-time factors are not additive and their ordering depends on the base point." Mod: "ranking it as the most influential 'design choice' says more about the optimiser than about published estimates."

**2. What the records show.** Right on each count, with records that ease the fix.
* `design_choices.csv` confirms the mixing: the export row's source is `published_values.csv` (the published 100 against the model's 41.5); the two energy-count rows compare exports alone (183.9 and 263.9) with the model's domestic capacity; the time-frame row bundles diet, organic yields, no waste, a 100-year allowance and a 30% reserve (section 6.8); releases switch between corrected and improved.
* Interaction evidence: waste moves the corrected release by 1.33 and the improved by 1.17 (base-point dependence); the diet path is non-monotone (Table S2: 100.4 at 2.5%, 103.3 at 5%, 66.9 at 7.5%; comparators README section 2b gives the half-point steps). Within the Monte Carlo's narrow ranges, interactions are small (first-order shares add to 101 to 104%), which says nothing about the wide design-choice ranges.
* Diet C: right that it has no acceptability bound. The records hold two bounded variants: A (foods swapped within each group, 85.5 million, a factor of 1.60) and B (serves free within the guideline ranges, 202.1 million, 3.77). `analysis/nutrition_lp_2025/README.md` says variant A "is the one to quote" and that C "is not a realistic diet".
* The proportional count has a rebuild from the food balance: 101 to 104 million without feed as a domestic use, 68 to 70 with it (`proportional_count.csv`), which gives the export row a computed basis instead of the published figure.
* The ladder: the paper says "a reading of the spread, not a decomposition" (section 6.10; defect X021). Figure 3's caption figure 223.9 is the midpoint of 183.9 and 263.9 (`ladder.csv`, last row), which the caption does not say.

**3. Does it change a finding?** Section 6.11's ordering ("exports counted by energy (4.4 to 6.4) and the optimised diet (7.88) most") changes: with diet A in place of C the diet rows become 1.60 to 3.77, and the energy-count rows leave the in-model ranking. Abstract s6 ("measured one at a time in the model") is untrue for the export rows. B185 (2.41) and the checklist factors in Table S4 move with the export row. No abstract number other than s6's wording moves.

**4. The fair response.** Reword the table and compute a factorial; out of scope for exports through the model, with a defensible alternative.
* Split Table 6 into three panels: (i) in-model changes on one release (corrected), with the improved value in a second column; (ii) comparisons with external counts (the CSIRO and UQ count and its food-balance rebuild, the energy count of exports), labelled as such; (iii) the Monte Carlo, labelled as a spread of a joint draw. Replace diet C with A and B as the ranked rows and keep C as a stated upper bound. Drop the time-frame row from the ranking or mark it as a bundle. Keep the ladder as illustration only or drop Figure 3's ordering claim; explain 223.9 or replace it with the range.
* Compute: a two-level factorial over the in-model choices (waste, drought allowance, land base, guideline diet at 15% and 5%, release) through `analysis/comparators_2025/rerun.mjs`: 32 runs, two-way interactions reported. Cost about 1.5% builder, about 1% check.
* Exports through the model (Mod's "domestic diet plus an export basket held on the land"): two responses are defensible. (a) Out of scope: the model is self-sufficient by design (section 8.2), so exports are a definition the model does not carry, and the paper should say the export rows are comparisons with external counts. (b) Compute: a new module holding an export basket on the land, session-size, about 2.5 to 3% plus about 1.5% check. I recommend (a) with the food-balance rebuild in panel (ii); a reviewer is likely to accept a clearly labelled comparison more readily than a new export module in a methods paper.
* Abstract s6: "were measured one at a time, in the model where the model carries them and against external counts where it does not."

**5. Dependencies and conflicts.** Shares runs with Issue 6. The span question Q8 and the CSIRO 100 or 90 question Q9 (Issue 11) set two Table 6 cells. The referees agree; Mod adds the acceptability bound and the export module, EE the single release.

---

## Issue 8. The pairing of pasture-fed food with crops is offered as the explanation but not tested

**1. The issue.** Sections 5.11 and 7.6 say the residual gap between the model and the adjusted footprint and HALF "is consistent with the pairing of pasture-fed food with crops", but the pairing was not removed from the model to test it, and it can be (EE 3.7, Q3; Mod M3, Q3).

EE: "Since the model is the author's and the pairing is its distinctive feature, this is the one test the paper most needs." Mod: "Without this, sections 5.11 and 7.6 should not use the pairing as an explanation."

**2. What the records show.** Right that no such run exists (section 5.11; B247's note: "the pairing explanation is the project's interpretation, not tested by removing the pairing from the model"). The records do hold circumstantial evidence:
* The model is bound by pasture-fed food: doubling cropland adds 9% (section 6.4); the commodity balance's meat reading (40 to 41 million) sits at the corrected model's 41.5; Table S2's default diet needs 5.93 ha of pasture and 0.30 ha of cropland a person.
* Within-group substitution, the referee's first suggested test, exists on the improved release: diet variant A (foods swapped within groups, the same food groups) feeds 85.5 million against 53.6, a factor of 1.60 (`analysis/nutrition_lp_2025/variants.csv`; Table S2). That is at or above the adjusted footprint (64.8 to 84.6) and HALF (76.0). It is not a corrected-release run, and it changes the foods, not the land pairing, so it supports "a fixed diet with no substitution" more than "the pairing" as such.
* The footprint's adjustment counts surplus cropland output (much of it exported grain) in the same world-average hectares as pasture; the model does not let cropland stand in for pasture ("pasture cannot grow rice", nutrition README). The pooling is exactly what the pairing forbids, so the explanation is plausible; it is not tested.

**3. Does it change a finding?** Section 5.11's last sentence and section 7.6's interpretation (B247) cannot stay as explanation without the run. If the run closes the gap, the paper gains its strongest causal sentence; if it does not, 5.11 must say the residual is unexplained. EE's substitution point is visible in Table S2 (up to 422 million) and should be said in section 8.4: the fixed diet is the decisive assumption.

**4. The fair response.** Compute; reword until it is done.
* Compute three readings on the corrected release and report them beside column (e): (i) land pooled at a common productivity (the model's diet need converted to world-average hectares with the footprint's own conversion, the same arithmetic as column (e), so a script over `harmonised_comparison.py` outputs and `diet_land.csv`); (ii) diet variant A on the corrected release (`analysis/nutrition_lp_2025/optimise.py`, one variant); (iii) crop-fed protein allowed to replace pasture-fed protein within the meat group (a diet edit through `diet_land.py`). Cost: about 1.5 to 2% builder, about 1 to 1.5% check.
* Reword in any case: 5.11 and 7.6 say "a possible explanation, tested in [new section]" or, if the run is not made, "an interpretation that this paper does not test". Response letter: "We have run the model with the pairing relaxed in three ways; the results are in Table 5, column (f)."

**5. Dependencies and conflicts.** Depends on Issue 3 (the comparison is to column (e)) and Issue 1. The referees agree on the test and differ only in the form; running all three forms satisfies both.

---

## Issue 9. Fidelity and gap attribution are weaker than the summary sentences

**1. The issue.** The summary that residuals "traced, where traceable, to data years, revisions and rounding" hides components that are not reproduced, and Table S1's shares of hundreds of per cent show the attribution is ill-conditioned (EE 3.8; Mod M7, Q8).

EE: "the residuals are tiny relative to the sensitivity to plausible causes, so the attribution is ill-conditioned and cannot be read as tracing the residual to any cause." Mod: "say plainly which test readings in Table 3 rest on an implementation that failed its fidelity check."

**2. What the records show.** Right, and the records add a point the audit did not make.
* The failures the referees list are all in the supplement: footprint plant-food cropland 0.074 to 0.142 ha against 0.312 and wool pasture not reproduced (S3.2); build 2 pasture 36% high; HALF New Zealand 94.8 against 135.76; people per hectare 22 to 42% above the paper and the United States not reproduced (feed share 41% against 67%, S3.4); Australia's HALF residual "not closed by any cause tested" (S3.7). Table S1 prints shares of -621.7, -915.2, -779.0 and -1056.6%.
* The audit's V32b problem 10 replaced the shares by "within rounding" in the prose but left Table S1 as shares. `gap_attribution.csv` holds the adjusted value under every cause (column "figure"), so the table can show values instead of shares with no new run.
* Not flagged in the audit: on the inputs the HALF supplement prints, the reconstruction moves away from the published figure. For Australia 2011, the authors' world pasture (cause b1) gives 118.88 against the published 112.2 (6% high), and all printed inputs together (a+b1-b5) about 121.5 (8% high, my reading from the share and residual). So the 0.8% agreement holds on current FAOSTAT revisions and not on the authors' printed inputs; the attribution says the residual is small, not why.

**3. Does it change a finding?** The abstract's "checked against their authors' published figures" (s3) and sections 1 and 9.1's "traced, where traceable, to data years, revisions and rounding" overreach. On Mod Q8: if the readings that rest on partly reproduced implementations (the footprint, people per hectare) are set aside, the aggregate group is the energy balance (134 to 211) and HALF (276), 3.2 to 6.7 times the corrected model as run; the direction of s4 survives, its top falls from 8.3 to 6.7 (before Issue 3's adjustment).

**4. The fair response.** Reword and regenerate tables; no new method run.
* Add a fidelity column to Table 3 with one word per component (reproduced, partly, not reproduced) and its residual. Mark the Table 3 readings that rest on a partly reproduced implementation. Regenerate Table S1 from `gap_attribution.csv` as adjusted values with the published figure beside them; keep shares only where the residual is larger than the rounding of the published figure. Rewrite 9.1: "Residuals were within rounding for the energy balance, within 1 to 2% for HALF's Australia and world on current FAOSTAT revisions (6 to 8% on the inputs the authors printed), and not closed for the footprint's plant-food cropland, HALF's New Zealand and people per hectare in the United States." Tone (decision 33): the access we had and the assumptions we made, not the authors' work.
* Cost: a table generator for Table S1 (the scope noted none exists), about 0.5 to 1%; a check, about 0.5%.

**5. Dependencies and conflicts.** Feeds Issue 3 (which readings are quotable) and Issue 5 (the decision 5 request to the HALF and Cassidy authors would resolve some of this). The referees agree.

---

## Issue 10. The common bases are mixed: consumption, population, land and vintage

**1. The issue.** The harmonisation uses FAO food supply (3,525 kcal, waste included) while other parts of the paper use 2,700, 2,550 and 2,100 kcal and the model charges waste separately; the per-person food balance uses FAO's 26.20 million and the methods the model's 27.6 million; land and data years differ by method (EE 3.9, Q7; Mod M6, Q6).

EE: "Equalising on food supply both penalises some methods and double-counts waste relative to the model." Mod: "a 5% mismatch that feeds directly into 'people fed'."

**2. What the records show.** Right on consumption, land and vintage; wrong on the population's effect.
* Consumption: the README sets FAO supply as the harmonised basis; the energy count of exports uses 2,100 kcal (`energy_exports.csv`); the model's default diet is 8.0 MJ a day as eaten (`analysis/nutrition_lp_2025/README.md` gives 8.0 MJ for the model's own diet and 8.0 to 9.2 MJ for the optimised ones), with losses charged separately. Henry and Godden's factor implies 15.6 MJ; at 8.8 MJ the energy balance feeds 243 million (S3.1).
* Population: the README says "The population of 27,608,200 (the model's) is an input to none of the harmonised method readings: each method's capacity is its output, and its per-person basis is the food balance's own", and explains why the 2021-23 totals are not divided by the 2025 head count. So the 5% mismatch does not feed into the readings. But section 5.1 says "Every method used one population, the model's 2025 figure of 27.6 million", which contradicts the README and S3; the referees read the paper correctly and the sentence is wrong.
* Land: the energy balance carries forward the 28.3 Mha of 1990-91 sown pasture (S3.1); the SA2 point sits on 2020-21 land (section 6.7). Right.
* Vintage: "the model's 2025 data were taken as the same vintage as FAOSTAT's data for 2021 to 2023" (S3). The model's own windows differ (its meat window is 2020-21 to 2024-25), and the meat-window choice alone moves it by 8.6 to 15.7% (sensitivity README). The FAOSTAT harvest-year offset affects the Cassidy test only (audit section 5).

**3. Does it change a finding?** On an intake basis the energy and calorie readings rise (the energy balance to about 243 million; people per hectare by about 2,700 over 1,910 kcal if put on the model's diet energy), so the gap between those methods and the model widens. The input share in Issue 2 would also rise, because consumption is the largest input effect for people per hectare (0.77). Abstract s4 and s5 move in opposite directions under this change.

**4. The fair response.** Reword, tabulate, and compute one sensitivity.
* Reword section 5.1 to say what the README says about population. Add a table of bases by method (population, energy basis, land classes and years, data years, exports), as run and harmonised; Mod notes it is what the checklist asks of others. Cost about 0.5% (Sonnet, from the README).
* Compute an intake variant in `harmonised_comparison.py`: every per-person energy and protein basis on one requirement (the model's 8.0 MJ, or 8.8 MJ, a stated source), with retail and household waste counted once from the Australian loss factors in `analysis/waste_2025`. Cost about 1 to 1.5% builder, about 1% check. Report it beside the supply basis, as both referees ask.
* Response letter on population: "The per-person bases are the food balance's own, on FAO's head count for the same years; the 2025 population is an input to none of the harmonised readings. Section 5.1 said otherwise and is corrected."

**5. Dependencies and conflicts.** Conflicts in direction with Issue 3 (supply against intake moves the aggregate methods up while local productivity moves the footprint and HALF down). Feeds Issue 2. The referees agree.

---

## Issue 11. The published span rests on two soft ends

**1. The issue.** The abstract and H1 state the span of 9 to 100 million and its factor of 10.6 without the qualification section 1 gives, although the low end is the author's superseded figure, the high end sums to 90 and is called misleading by its own report, and Henry and Godden's 109 lies above it (EE 3.10; Mod minor 1, 2).

EE: "the abstract opens with it and highlight 1 states it without qualification." Mod: "State the selection rule for the span."

**2. What the records show.** Right. Section 1 states both soft ends; Table 1 itself includes Henry and Godden's 109, so the span of Table 1 is not 9.4 to 100. Scope question Q9 (100 or 90) is open with Murray (digest D4: recommended "about 90 million (around 100 in the report's words)" with ratios kept on 100; adopting 90 moves three Tier A ratios, B185, B191, B192). My scratch interquartile range of Table 1: about 33 to 82 million with one figure per row (factor about 2.5), or 36 to 80 with every figure (about 2.2); the rule for picking one figure per row is a choice.

**3. Does it change a finding?** Abstract s1 and H1 (B005, B192). The factor of 10.6 is an identity (100 over 9.4, X021) and leaves the abstract and highlights.

**4. The fair response.** Reword. Option (a): "Published estimates of how many people Australia can feed run from about 9 to more than 100 million", with no factor, and the factor of 10.6 kept only in section 6.10 as the ladder's reading with its ends named. Option (b): report the interquartile range of Table 1 with a stated rule. I recommend (a): it changes no Tier A value, keeps the source's words, and is what a reviewer will accept; (b) adds a new number that needs a rule, a claim row and a check (about 0.5%). H1 is replaced by a highlight on what was done (EE section 6 suggests one). Needs Murray: Q9, and gate 4 for B005's wording.

**5. Dependencies and conflicts.** Depends on Q9. Links to Issue 4. The referees agree.

---

## Issue 12. The failure view: one cereal scalar on every yield, the record, and the release

**1. The issue.** The drought allowance applies a winter-cereal yield index to all yields, pasture and herds included; the record is treated as stationary; the curve rests on six interpolated points; and the failure probability at the 2025 population depends on the release (Mod M8 parts b to d, Q7; EE minor 10).

Mod: "applying a winter-cereal yield index to all yields, pasture and herds included, is a strong assumption ... The record is treated as stationary despite the yield trends cited in section 8.1."

**2. What the records show.** Right on the single scalar and the release; wrong on stationarity.
* `analysis/resilience_2025/README.md`, Limits: "The series is three grains, yield only. Pasture, livestock, horticulture and the correlation of failures between crops are not in it; the factor scales all of the harvest" (also defect X007). Right.
* Stationarity: the factor is each year's yield over a reference that is the mean of the ten observations around it (README section 1), so it is a ratio to a moving local mean, not to a fixed level. The trend in level is removed. A "smoother trend" was listed as not tested. Mod's premise is mistaken on the record; it holds only in the weaker sense that the variability of the ratios is taken as stable.
* Uncertainty of the tail is in the records: a fitted generalised Pareto tail gives a 90% interval of 0.32 to 0.54 for Australia's 100-year factor (README section 3); a leave-one-out reference lowers it 9%.
* Runs of bad years: the store tables give the worst run of 2 to 5 consecutive years (README sections 5 and 6), the nearest thing in the records to serially correlated shocks, though not used in the failure curve.
* Release: S3.6 gives about 1.5% (improved), about 2% (thesis as built) and 5.8 to 6.1% (corrected). The main text gives only the corrected figure (B130). Right.

**3. Does it change a finding?** No abstract number. Table 7's "well suited" for food security (purpose 1) for the failure view and the balance rests partly on this mechanism, so Issue 5's rubric should name the single scalar as a stated limit. Section 5.8 needs the release-dependent probabilities.

**4. The fair response.** Rebut on stationarity, reword on the release, and choose between two responses on the scalar.
* Rebut: "The drought factor is the ratio of each year's yield to the mean of the ten observations around it, so the trend in level is removed; we say so in section 5.8 and report the fitted-tail interval of 0.32 to 0.54 at 100 years."
* Reword: give 1.5%, 2% and 5.8 to 6.1% by release in section 5.8.
* Scalar: (a) out of scope, stated as a limit (no 150-year pasture or livestock series is in the archive); or (b) compute a bound by applying the factor to crops only, with pasture and livestock unshocked, and the reverse, through a release variant (about 1% builder, about 0.7% check). I recommend (b) with (a)'s wording: it costs little and tells the reader how much the assumption matters. Separate serially correlated crop and pasture shocks need data the archive does not hold; say so.

**5. Dependencies and conflicts.** Links to Issue 5 (how the failure view is counted and rated). EE raises only the release point; no conflict.

---

## Issue 13. Literature an Ecological Economics reader expects, and the trade question

**1. The issue.** The core footprint critiques and reviews, the HANPP family, the global food-system modelling literature on how many people domestic or local production can feed, and the open-economy critique are missing or cited second-hand; the self-sufficient design needs an argument in an economics journal (EE 3.11; Mod M10).

EE: "the model is 'self-sufficient by design' (section 8.2), which needs a defence in an economics journal, not only a limitation note." Mod: "That sentence carries much of the paper's framing and needs argument."

**2. What the records show.** Mostly right; one premise is wrong and several works are held but unused.
* Not in the literature register: van den Bergh and Verbruggen 1999, Fiala 2008, Kitzes et al. 2009, Ayres 2000, Haberl et al. 2007, Krausmann et al. 2013, Pradhan et al. 2014, Monfreda et al. 2008, Alexander et al. 2017, Arrow et al. 1995.
* EE says Arrow et al. 1995 is "mentioned but not engaged". It is not mentioned in the draft or the reference list, and not in the register. Cohen 1995 and Chisholm 2000 are cited (sections 1 and 2).
* Held and read but not used as the referees want: Gerten et al. 2020 (L083, "read"), which the paper cites "as reported in" Beltran-Peña et al.; Springmann et al. 2018 (L082, read); Kummu et al. 2020 (L175, read targeted); Gaupp et al. 2019 (L217, read at page level; Mod writes 2020). Borucke et al. 2013 (L125) and Mottet et al. 2017 (L122) are record only.

**3. Does it change a finding?** No number. Section 8.2's framing sentence and section 4's catalogue (no HANPP family) are what move.

**4. The fair response.** Reword and read; one item out of scope.
* Add the works where they bear on an argument: footprint critique and review (van den Bergh and Verbruggen; Fiala; Kitzes et al.; Borucke et al.) in sections 2 and 4.5; Pradhan et al. and Porkka et al. in section 6.7; Alexander et al. 2017 and Kummu et al. 2012 in 6.3; Mottet et al. in 6.2 and the pairing discussion; Gaupp et al. in 8.1; Springmann et al. in 6.5. Cite Gerten et al. 2020 directly. Add HANPP to section 4 as a catalogued family, not tested (running it is out of scope; say so, as for Khorsandi). Replace section 8.2's last sentence with a paragraph on what a capacity figure means in a trading economy, engaging Cohen 1995, Chisholm 2000, van den Bergh and Verbruggen 1999 and Arrow et al. 1995.
* Cost: about 12 targeted reads at about 10,000 Sonnet tokens each plus a merge job, about 1 to 1.5% in all; Murray fetches the paywalled works (full URLs and QUT links in the request, per the Card). The 8,000-word limit (decision 92) means additions displace text or go to the supplement.

**5. Dependencies and conflicts.** The trade paragraph supports Issue 7's choice (a) on exports. The referees overlap and agree; their lists differ, not conflict.

---

## Issue 14. The review falls short of its own standard: counts, works not seen, the archive, the missing table and figures

**1. The issue.** No counts of works found, screened, read or excluded; "well-known methods" undefined; key works, including the author's own papers and the sensitivity references, "not seen; cited from its abstract"; no DOI; Table 2 and Figures 1 to 3 not built (EE 3.12, Q9, Q10; Mod M4 last sentence, M11 first part, minor 3, 4, 14, Q10).

EE: "readers will find it odd that the author's own papers are cited from their abstracts."

**2. What the records show.** Right, and part of it is the paper's own mislabelling.
* Counts: the drafter note to section 3 says no csv holds the selection record. The route records exist: `qa/reports/B14_literature_sweep.csv` (60 rows), `B15_citing_works.csv` (63), `B61_candidate_sources.csv` (79), `B63_candidates.csv` (88), and the literature register (246 rows: 199 read, 16 reported, 12 record only, 10 not reached, 6 abstract only, 3 not read). Counts by route can be built from them, after removing duplicates.
* "Not seen" labels that the register contradicts: Erb et al. 2016 (L084, "read", full text opened), Shepon et al. 2016 (L124, read targeted), Khorsandi et al. 2022 (L073, read at page level), Gerten et al. 2020 (L083, read). The HANDOFF lists this as an open item for Murray. Correctly labelled: the three Monte Carlo references (L235 to L237, record only) and the author's own 2014, 2015 and 2017 papers (L012 to L014: no file in the archive; the register's "read" is unverified). The thesis (L020) is held and read.
* Archive: decision 96 lifts the Zenodo hold and deposits the repository with a DOI ahead of submission; the Card says only Murray releases it.
* Table 2 and the figures: placeholders. Decision 99 puts the figures after the text is settled; Table 2 needs a catalogue csv that does not exist (scope gap 4).

**3. Does it change a finding?** No number. Section 3's credibility and section 1's "the three papers not seen" sentence.

**4. The fair response.** Compute counts, reword labels, and Murray's actions.
* Build a selection table from the four route csvs and the register (found, screened, read, cited, excluded, by route), about 0.5 to 1% (Sonnet). Define "well-known" in section 3 (for example: a method with a published Australian figure, or a family with an Australian application or a citation lineage to the 2010 review; Murray chooses the words).
* Correct the four wrong "not seen" labels (about 0.3%). Read the three Monte Carlo references (Murray fetches).
* Needs Murray: upload his own 2014, 2015 and 2017 papers (decision 9 asked for this) so they can be cited as read; the Zenodo deposit (decision 96); the figures job (decision 99, about 2 to 3%) and a catalogue csv for Table 2 (about 1%).

**5. Dependencies and conflicts.** The figures depend on the settled text of Issues 1 to 8. The referees agree.

---

## Issue 15. Ranges and factors are presented inconsistently

**1. The issue.** Readings in Tables 3 and 5 are ranges across builds and cases, Table 4's are Monte Carlo percentiles, and the tables do not mark which is which; "factor" as higher over lower loses direction; the energy count of exports appears as 184 to 264, as 183.9 and 263.9, and as 223.9 (Mod M11, rest).

Mod: "a signed log ratio would read better and allow additive decomposition."

**2. What the records show.** Right. The 223.9 is the midpoint of 183.9 and 263.9 (`ladder.csv`), unexplained in the Figure 3 caption. The paper says in places that ranges are "not an uncertainty range" (section 5.3) and "not confidence intervals" (6.9), but not in the tables.

**3. Does it change a finding?** No.

**4. The fair response.** Reword: a marker on every range in Tables 3 to 6 (across builds, across cases, Monte Carlo percentiles); low and high columns in Table 6 kept and a signed log ratio added; the 223.9 explained or replaced by the range. Cost: table regeneration, about 0.3%.

**5. Dependencies and conflicts.** Folds into the regeneration of Tables 3, 5 and 6 under Issues 3, 7 and 9. No conflict.

---

## (a) All issues

| # | Referee and number | Verdict on the premise | Response | Headline effect | Cost (share of the weekly allowance) |
|---|---|---|---|---|---|
| 1 | EE 3.1 (first part); Mod M1 | Right: the line decides the result; about 41% inputs on the other line (scratch) | Reword; compute both classifications; Murray chooses the headline | Abstract s2, s5; H2, H3; B276, B277 | about 2% (with Issue 2) |
| 2 | EE 3.1 (b to d), Q1; Mod M2, Q1, Q2 | Right; formula exists in README and script but not the paper; "each" wrong; as-run low and Table 5 disagree | Compute (anchors, row sets, dispersion, signed split); reword | s5, H3: 10% becomes 10 to 20% (decision 35 line) | shared with Issue 1 |
| 3 | EE 3.2, Q2, Q8; Mod M1 part, minor 5 to 7 | Right on units; "1.5 to 2 times" true for footprint and HALF only | Reword (column (e) primary); current NFA blocked, needs Murray | s4: about 65 to 211 million, 1.6 to 5 times; B156, B247 | about 0.5% plus register job |
| 4 | EE 3.3, Q4 | Partly right: three published counts reproduced, not one | Reword; add mapping column from `harmonisation.csv` | s2 and section 1 restricted; no number | about 0.5% |
| 5 | EE 3.4, Q6; Mod M9, M8(a), Q9 | Mostly right; second reader exists (V28, AI, 25 of 28), others have build ranges | Reword (rubric, disclosure, 9.5, failure column); independent raters need Murray | s3 "seven methods"; Table 7 at risk | about 0.5 to 1.5% |
| 6 | EE 3.5, Q5; Mod M4, Q4, Q5 | Right on rule, narrowness, "only"; wrong that diet, crop yields and pasture output are absent | Reword; compute wider global sensitivity with total-order indices | s7, H5: "only" and "defensible" go; 1.26 (5 to 95) and 1.38 (min to max) | about 4% |
| 7 | EE 3.6; Mod M5, M11 part | Right; bounded diets A and B and a proportional rebuild exist | Reword (three panels, diet A and B); compute factorial; exports through model out of scope (recommended) | s6 wording; section 6.11 ordering; B185 | about 2.5% (4% more if exports run) |
| 8 | EE 3.7, Q3; Mod M3, Q3 | Right: untested; diet A (85.5) circumstantial | Compute three relaxed runs; reword until run | 5.11, 7.6, B247 | about 2.5 to 3.5% |
| 9 | EE 3.8; Mod M7, Q8 | Right; HALF Australia 6 to 8% off on the authors' printed inputs (not in the audit) | Reword; regenerate Table S1 as values; fidelity column | s3 "checked"; 1 and 9.1 sentence; s4 top 8.3 to 6.7 without partly reproduced readings | about 1 to 1.5% |
| 10 | EE 3.9, Q7; Mod M6, Q6 | Right on consumption, land, vintage; wrong that population enters the readings | Reword 5.1; basis table; compute intake variant | s4 and s5 move in opposite directions | about 2.5% |
| 11 | EE 3.10; Mod minor 1, 2 | Right | Reword (no factor in abstract or H1); Q9 needs Murray | s1, H1; B005, B192 | under 0.5% |
| 12 | Mod M8 (b to d), Q7; EE minor 10 | Right on scalar and release; wrong on stationarity | Rebut (stationarity); reword (release); compute crop-only bound | Section 5.8; Table 7 purpose 1 | about 1.7% |
| 13 | EE 3.11; Mod M10 | Mostly right; Arrow not mentioned at all; Gerten, Springmann, Kummu, Gaupp held | Read and reword; HANPP catalogued, out of scope to run | No number; 8.2 framing | about 1 to 1.5% plus Murray fetches |
| 14 | EE 3.12, Q9, Q10; Mod M4 refs, M11, minor 3, 4, 14, Q10 | Right; four "not seen" labels contradict the register | Compute counts; relabel; Murray: own papers, DOI, figures | No number | about 1.5% plus figures job 2 to 3% |
| 15 | Mod M11 (rest) | Right; 223.9 is a midpoint | Reword and regenerate tables | None | about 0.3% |

All compute items together come to roughly 20 to 25% of a weekly allowance, builders and blind checks included, before the figures job.

## (b) The changes that would do most to satisfy both referees, in order

1. Report the harmonised comparison under both classifications of the productivity basis, with the formula, three anchors, the row sets and an anchor-free dispersion measure, and rewrite abstract s2 and s5 and H2 and H3 to the range of input shares that results.
2. Make the local-productivity readings the primary footprint and HALF capacities, label the world-average division as a counterfactual, and restate "three to eight times" as about 1.6 to 5 times, with the footprint and HALF at about 1.6 to 2.0.
3. Run the model with the pasture and crop pairing relaxed in three ways on the corrected release and report the readings beside the adjusted footprint and HALF, so that sections 5.11 and 7.6 either gain a tested explanation or say the residual is unexplained.
4. State the rule that separates definitions from settings, widen the Monte Carlo to the waste rate, land source, meat calibration, energy requirement and yield trend with total-order indices and min to max, and drop "defensible" and "only".
5. Remove the model's privilege from the presentation: publish the Table 7 rubric and the V28 agreement with the second reader described as it was, seek independent raters under decision 5, count the methods as five plus the model read two ways, rewrite 9.5, and restate fidelity with Table S1 as adjusted values.

## (c) Where accepting the criticism would be wrong

* Accepting that the 5% population mismatch "feeds directly into people fed" would be wrong: the README states the 2025 population is an input to none of the harmonised readings, so the fix is to correct section 5.1's sentence, not the readings.
* Accepting that the diet is excluded from the Monte Carlo would be wrong: the meat-and-egg share and the red-meat share are drawn (`monte_carlo.mjs`), and only alternative diets and the waste rate are not.
* Accepting that crop yields and pasture productivity are absent from the Monte Carlo would be wrong: the crop-trend factors and the organic factor are drawn, and the meat data window is the model's pasture-output basis and carries 81% of the variance.
* Accepting that the drought record is treated as stationary would be wrong: each year's yield is taken as a ratio to the mean of the ten observations around it.
* Accepting that the aggregate methods fall to "roughly 1.5 to 2 times" the model would be wrong: that holds for the footprint and HALF only, while the energy balance and people per hectare, which count Australia's own production, stay at 2.7 to 5.1 times.
* Accepting that only the energy and protein balance reproduces a published count would be wrong: the thesis's 40.45 and 9.43 million and the CSIRO and UQ count (rebuilt as 101 to 104 million) are reproduced too.
* Accepting that an anchor-free measure would show the spread narrowing would be wrong on the paper's own classification: the standard deviation of log readings is 0.64 as run and 0.69 harmonised (scratch); the narrowing appears only when the productivity basis is reclassified.
* Accepting that the Table 7 second reader had no criteria or agreement would be wrong: V28 stated its rule before rating and agreed on 25 of 28 cells; what is missing is the report of it and the fact that the reader was an AI checker.
* Accepting that moving every method to an intake basis would narrow the gap to the model would be wrong: it raises the energy and calorie readings (243 million for the energy balance at 8.8 MJ) and widens it.
* Conceding that Arrow et al. 1995 is cited but not engaged would be wrong: it is not cited at all, so the response adds it rather than defending a use that does not exist.

## (d) Questions to the author

From EE:
1. The ratio-scale decomposition and its row sets; the share with the cross-method median as reference: the formula is in the README and `harmonised_comparison.py` lines 199 to 208 (mean absolute log input and method factors, methods weighted equally, 0.14 against 1.35); the 10 to 18% is V26's 24 row sets; with the median of the harmonised methods as anchor my scratch reading gives about 20%.
2. Which claims hold with the footprint and HALF in consistent units, and the multiple: footprint 64.8 to 84.6 and HALF 76.0 are 1.6 to 2.0 times the corrected model (B270, B272); the aggregate group becomes about 65 to 211 million, 1.6 to 5 times; "does not narrow" fails if this is counted as an input change.
3. The model with the pairing relaxed: no run exists; the nearest is diet variant A at 85.5 million on the improved release (1.6 times), which reaches the adjusted footprint and HALF; needs the Issue 8 run.
4. Which published figures each method or design choice reproduces: `harmonisation.csv` (closest model run; comparable) and Issue 4: Henry and Godden, the thesis, the CSIRO and UQ count reproduced; Jones matched in scale; five with no method.
5. The definition and setting rule; a Monte Carlo with diet and waste: no rule is written (section 6's "ends the methods take" is the implicit one); the observed diet's shares are drawn, waste is not; the factor would rise above 1.26 (waste alone is 1.33); needs the Issue 6 run.
6. The second reader for Table 7: a blind AI checker session (V28), given the test records and not the draft, rule stated before rating, 25 of 28 agreement (kappa about 0.83, scratch), three differences adopted by decision 69.
7. Why FAO supply and not a requirement, and the readings on a requirement: supply is the one basis every method can take (decision 35); on 8.8 MJ the energy balance reads 243 million (S3.1); a full requirement run does not exist; needs the Issue 10 run.
8. A current National Footprint Accounts food row for Australia: not in any held source (BLOCKED_SOURCES.md); secondary whole-footprint figures give about 39 million for 2022 (B223, unverified); needs Murray (a GFN data licence).
9. Why the author's own papers are cited from abstracts: no file of them is in the archive (L012 to L014); needs Murray (upload, decision 9).
10. A DOI before publication: decision 96 says yes, ahead of submission; needs Murray to release the Zenodo deposit.

From Mod:
1. The formula, row set, anchor and weights for 10% and 18%; the share with the median as anchor: as EE question 1.
2. The share with the productivity basis as an input: about 41% (scratch, from `harmonised_comparison.csv` with column (e) as the harmonised reading); needs the Issue 1 build and check.
3. The model with the pairing relaxed, and whether it closes the 1.5 to 2 times: no run; diet variant A suggests within-group substitution alone spans it on the improved release; needs the Issue 8 run.
4. How pasture productivity is represented and how much of 331.87 Mha is usable; the Monte Carlo with pasture productivity varied: national meat output shared among zones by dry sheep equivalent, over all grazing land in the ABS holdings (`analysis/pasture_2025/README.md`); the meat data window varies it (81% of the variance); the land-use raster instead of holdings adds 17.3% one at a time.
5. The estimator for the variance shares and the total-order indices: first-order indices by binning (`summarise_mc.py`), adding to 101 to 104%; total-order indices are not computed; needs the Issue 6 run.
6. The daily energy of the default diet, and the readings on one energy basis: 8.0 MJ a day as eaten (nutrition README); one-basis readings need the Issue 10 run.
7. Why a winter-cereal scalar on pasture and livestock, and results with separate shocks or a detrended record: the thesis table is a grain record and scales all yields (resilience README, Limits); it is a ratio to a centred ten-year mean; separate shocks are not run; needs the Issue 12 bound run.
8. Which Table 3 readings rest on implementations that failed fidelity, and whether "three to eight times" survives: the footprint (plant-food cropland, wool) and people per hectare (United States) are partly reproduced; without them the aggregate group is 134 to 276 million, 3.2 to 6.7 times as run, so the direction survives.
9. Whether the Table 7 ratings were made before or after the second reader saw the results, and the agreement: the author's draft ratings (`SECTION7_DRAFT.md`) were made from the tests; V28 re-derived them blind without the draft; 25 of 28.
10. A DOI before publication: as EE question 10; needs Murray.

## (e) Minor issues, grouped by kind, with the fix for each kind

* **Wording, units and names** (EE minor 1, 2, 7, 8, 9, 15, 16; Mod minor 11, 12, 15, 16): "Each was offered as such a count"; "the published method" for a figure; "ha a person" and "people a hectare"; 1.32 against 1.318; the 1-in-10 point set against the Monte Carlo of the average year; Table 5 column (e) header without its source; "published release" in S5; the Jones figures said to "bracket" 30.8 in 5.8 and to sit off the curve in 6.6 (keep 6.6's framing); the 6% waste setting introduced without the 12% default; four names for the model. Fix: one editing pass to a short style sheet (per, not a; one precision per quantity; one name for the model, "the land-and-diet model"; release names as in Table 4).
* **Internal provenance in captions and the supplement** (EE minor 5, 6; Mod minor 17): csv and script names in captions, "four cells differ from the csv", "decision 92" and "decision 57". Fix: regenerate `cross_method.csv` and `harmonised_comparison.csv` with the matched Cassidy reading (183, 0.618) and the footprint's yield basis so no caption needs an exception, move provenance to the data statement, and strip decision numbers.
* **Table content** (EE minor 3, 4, 10, 12, 14; Mod minor 6, 7, 8, 9, 10, 18): Table 1 route marked in the figure column and the 9.4 shown in the author's row; Table 3's footprint cell split by build; Table 5 column (a) renamed and one Cassidy basis; footprint exclusions (pasture alone) consistent; the failure probability by release in the main text; a corrected-release column in Table S2 (76.8, 118.0, 112.4); the 2.5% and 5% diets' pasture switch explained from `diet_land.csv`; the SA2 land equality shown; a sign example for Table S1. Fix: one table-regeneration job after Issues 3, 7 and 9, with a claims row for each new cell.
* **Reference list** (EE minor 17): 28 "[CHECK]" notes; Buzby 2010 and Muth 2011 without title or initials; cited works missing (Centre for Population 2026, Świąder et al. 2020, Geoscience Australia and ABARE 2010, Taylor 1937); listed works not cited (among them Poore and Nemecek 2018, Reutter et al. 2017, Bentham et al. 2020, Productivity Commission 2011, Cohen 2017, Tucker 2020); Qiu 2024 ambiguous. Fix: resolve the CHECK notes in `qa/references.csv`, add a cited-against-listed check to `qa/tools/make_references.py`, and rebuild.
* **Citation forms and second-hand labels** (EE minor 13, 18, 19, 20; Mod minor 13): DCCEEW documents cited by title in the text and by department in the list; "CSIRO and UQ" against the full name; "as reported in", "cited through", "known here only third-hand"; Kinnunen and Fader figures as reported; the forward reference for the US loss factors; Fearnside's p. 352 (L042 was read at page level; check the page once more against the file). Fix: one form, "as reported in", for every second-hand citation; author-date throughout; first-use sources.
* **Relevance** (EE minor 11): Willett et al. 2019 on global cropland. Fix: one clause on why a global cropland result does not carry to a pasture-bound one, or drop it.
* **Keywords** (EE minor 21): add "ecological footprint" and "sensitivity analysis"; the limit is seven (decision 97), so they replace two (I suggest "resource accounting" and "self-sufficiency").

## (f) Register rows touched, and the wrong-value check

Register rows touched: none.

Wrong-value check: *Example, deliberately wrong, not to be used:* "We accept the referee's point that the diet is absent from the Monte Carlo and have added the meat-and-egg and red-meat shares as uncertain choices." This would concede something the records show to be false: both shares are drawn in the Monte Carlo (`analysis/sensitivity_2025/monte_carlo.mjs`, triangular 0.115 to 0.13 and 0.528 to 0.64), and the red-meat share carries 16% of the short-term variance in the corrected release (`results/ranges_2025-fixed.csv`, influence 0.163).
