# V32a: logic and consistency of Paper A (results)

Checker brief: `qa/briefs/V32a_logic_A.md` (decision 77). Blind check of argument, not arithmetic. Read: `papers/A_results/SECTION_SCOPE.md` (all twelve section blocks), `papers/A_results/OUTLINE.md`, `papers/A_results/DISCUSSION_MEASURES.md`, `qa/claims_register.csv` (every claim id cited in the scope, read by statement, value, unit, release and status as the register stands), `qa/literature_register.csv` (each cited row's `what_taken` and `notes`), `qa/DECISIONS.md` (rows 1 to 83), and `papers/B_methods/SECTION_SCOPE.md` with the Paper B claim rows it cites where the same figure or method appears. Where a register note pointed at a data file, I opened the file to see whether the point holds (`results/*.csv`, `analysis/paper_a/regional_flips.csv`, `analysis/comparison_2025/README.md`, `results/releases.json`, `baseline/baseline_2011.csv`). Nothing was recomputed beyond reading cells.

**A general note on the scope's evidence tables.** The "Tier and routes" columns of `SECTION_SCOPE.md` were written before V31. Many rows they mark as unchecked are `independently verified (V31x)` in the register (for example A012, A328, A329, A049, A061, A072, A073, A106), and a few rows the drafter will lean on are still `unverified` in the register (A095 to A097, A113, A126 to A132, A136 to A139, A208 to A216, A231, A232, A243, A244, A309, A310, A317). Gap lists that name already-closed defects (section 5 gap 2 on A119; section 9 gap 3 on A314; section 12 gap 2 on A140) are stale. Verdicts below use the register as it stands.

Verdict key: **S** supported; **P** partly (what is missing); **N** not supported.

---

## Section 1. Introduction

| Pt | Support | Notes |
|---|---|---|
| 1 | P | L144 Davies p. 149 calls the growth "unplanned", but the same row records that p. 150 says growth "is in fact highly managed"; quoting only the first reading misstates the source. L147 McDonald measures employment, not population (its own row says so). L099 Productivity Commission: register status `unverified`, B85 "not reached: no file". The government framing is pending B74. The "came back with rapid growth" claim rests on two academic rows that each carry a caveat. |
| 2 | S | A002, A004 (two routes), A012 (24%, V31d). |
| 3 | S | Pointer only; L003, L007, L010 (B85 page level) carry it. See cross-paper item X2. |
| 4 | S | L148 ("nine documents set food security as a goal, none in Queensland or federal"), L149, L150 support "only patchily". |
| 5 | P | Decision 52's wording is quoted, but the lead clause "climate since 1990 has worked against Australian cropping" is stronger than L153, whose row says "national actual yields stayed flat" and the 27% is "simulated water-limited yield potential". L152 is "simulated, not observed, profits" over 2001 to 2020. L154 is the Murray-Darling Basin, not the nation. No row measures 2011 to 2025 itself (gap 3). |
| 6 | S | L013, L014 as the earlier findings (register `unverified`, read). |
| 7 | P | A334 is a description; "what those papers left open" is asserted, and the scope's own gap 4 says the citing-works list is unread. |
| 8 | P | The five questions come from OUTLINE.md, whose question 1 asks "how much of the change is population, land use or yield". Decision 62 and N-A4 (a) say population is a status change, not a cause; section 4 point 2 follows the decision. The question text contradicts it. |

Consistency: point 8 against section 4 point 2 and decision 62. Cross-paper: X2 (the author's long-term figure). Logic: the purpose ("why a regional answer matters to planners") follows from point 4; point 7 is asserted.

## Section 2. Method and data in brief

| Pt | Support | Notes |
|---|---|---|
| 1 | S | `results/README.md` definition. |
| 2 | P | L059 is an unpublished manuscript (gap 1). |
| 3 | S | Settings columns. |
| 4 | P | A048 and A331 say 52 NRM regions plus the Northern Territory; section 5 uses A104 and A107, "53 NRM regions". Say "53 regions (52 NRM regions and the Northern Territory)" everywhere. |
| 5 | S | Releases and hashes. |
| 6 | P | "The paper reports the corrected releases" is not what sections 8 to 12 do: the named scenarios and grain stores are on the improved release (A201 to A227, A264 to A266), the method effects are measured on the published base (A278 to A303), the herd-cycle range is on `2025-organic` (A317), the diet-swap result is improved (A134). The grain-store releases `2025-store-1` and `2025-store-2` have status `current`, not `frozen`, in `results/releases.json`, though decision 8 froze six paper releases. |
| 7 | P | A200's statement says "regions of one state tip together"; its own note says the five that tip in 2025 are in three states, "so not all of one state". Applying the wheat-oats-barley factor to pasture-fed output is untested (A223 note; section 8 gap 3) and should be named here. |
| 8 | P | A336 and A045 hold. The Monte Carlo has thirteen sampled choices of which twelve vary in 2025 (B253); see X3. |

Consistency: point 6 against sections 8, 9, 11 and 12. Logic: the claim that the 2011 to 2025 change "is a data change" holds for the corrected chain only; the section should say which other bases appear and where.

## Section 3. The short-term picture, 2011 to 2025

| Pt | Support | Notes |
|---|---|---|
| 1 | S | A001 to A006, A163, A179. |
| 2 | S | A328 (capacity +24.6%, population +23.7%). |
| 3 | S | A029 to A033, A043. |
| 4 | P | See problem 1 and problem 4. **North East Vic's 2011 population is 204,651, identical to the person with Goulburn Broken's** in `baseline/baseline_2011.csv` and in every 2011 release (`results/2011-fixed.csv` rows 38 and 44); it falls to 114,355 in 2025 (-44%) while Goulburn Broken goes 204,651 to 207,455. The flip (over in 2011 at 204,651 against 105,525; under in 2025) is driven by that input. **Mackay Whitsunday** is under capacity in 2011 on the improved release (148,175 against 137,252 people in `results/2011-improved.csv`; A309, register `unverified`), so its flip does not hold across tiers. North Tasmania's 2011 status is 0.96 (corrected) and 0.99 (improved) of balance with no 2011 range. |
| 5 | P | A329 holds as a direction, but its own note records that Murrumbidgee-ACT gains both capacity and people. The section 4 walk shows most of the national capacity gain came from the consumption layer (+4.18 million) and the red meat mix (+1.81 million), which are diet settings applied everywhere, not production placed inland. "Capacity grew inland" is supported; "production grew inland" (OUTLINE arc 2, A329 statement) is not shown. |
| 6 | P | A044 counts Swan as over capacity in both years; A049 and A052 say Swan's 2011 value is a boundary artefact "usable for 2025 alone". "The coast is mixed" is checkable only against the README's named examples (A044 note). |
| 7 | S | A046, A047, A045, A049 to A066 state the cautions. Logic: A047 ("the test of an artefact is on capacity, not on whether the population change is real") is stated as a caution but problem 1 shows it is the test that fails. |

Consistency: point 5 against section 4 point 3 (where the gain came from); point 6 (Swan over in both years) against point 7 (Swan 2011 is an artefact). Logic: the purpose says each flip must pass "the land-definition, boundary and range tests"; no test of the population input or of the method tier is applied, and the three "clean and robust" flips do not all survive those two.

## Section 4. What drove the change

| Pt | Support | Notes |
|---|---|---|
| 1 | S | A072, A073 (V31d). The A072 note still describes the published-tier decomposition as current; refresh it. |
| 2 | S | A363, A364 (Tier A, B76 and V29; "awaiting Murray's gate digest"). |
| 3 | S | A354 to A362 short-term values; the split of the organic share is a stated builder choice (A358 note). |
| 4 | S | A365; the ordering is "of this walk's order". |
| 5 | S | Sum check: the layers add to +8,195,723 and +273,063, equal to A072 and A073. |
| 6 | P | No claim row for the regional pattern (gap 2). |
| 7 | P | The caveats are those of the published-tier README paragraph, which was written when crop yields were the largest long-term cause ("roughly doubled against the drought years of 2006-2010"). On the corrected walk crop yields are +0.12 million short term and +0.22 million long term, so the caveat about very good crop years weighs little. L153 Hochman is cited "why the drought years of 2006 to 2010 make the 2011 crop yields low", but its row reports simulated potential 1990 to 2015 with flat actual yields; it does not say that. |

Consistency: this section contradicts the OUTLINE question 1 and takeaway (section 1 point 8; problem 3). Logic: the purpose follows from the points; the ratio convention here (people over capacity, above 1 is over) is the reverse of sections 3, 7, 8 and 10 (problem 7).

## Section 5. The scale curve

| Pt | Support | Notes |
|---|---|---|
| 1 | S | A104, A111. |
| 2 | S | A015 to A018, A074 to A078, A084 to A088. |
| 3 | S | A079 to A083, A089 to A093 (decision 29 values), A120. |
| 4 | P | A106's statement quotes the 2015 published figures "(national 40, states 28, regions 23 million)" as surviving the corrections; its V31d note says the corrected values are 33.3, 25.7 and 21.0 (L013's register row says 25.6). The 21.0 for regions is on each zone's own yields, whereas the curve of points 1 to 3 is on the state-yield basis (NRM 44%). The "survives" sentence therefore sets a published figure and a different yield basis beside the curve. It also sits awkwardly with the standing rule "2011 as corrected only, no reconciliation table". |
| 5 | S | A107, A114, A115. |
| 6 | P | A116 gives SA Arid Lands 41 thousand on the state-yield basis; section 10 (A057) gives 28.6 thousand for the same zone on its own yields. A119 now reads 4.50 (gap 2 is closed). |
| 7 | P | A124: the short and long figures are from two different splits, each optimised for its own term; the short split scores 0.661 in the long term. "A better drawing keeps 76% and 69%" must say two splits, heuristic, lower bounds. A122's ranges are spreads across five draws, not uncertainty. |
| 8 | P | A095, A096, A097 are `unverified`; A113 is `unverified: rejected method not committed` (77 not reproduced, nearest 73.0). The local-basis NRM share (A095, 63%) is the figure sections 7, 8 and 11 actually use (problem 2), and it is unverified. |

Consistency: the NRM-sum share here (44% short, 23% long) contradicts section 7 point 6 (33% and 38%), section 8 point 5 (0.63) and section 11 point 8 (national 1.60 times the regional sum). Cross-paper: values agree with B171 to B177 (B172, B173 self-checked on the B side). Logic: the purpose "the 2015 finding survives the corrections" is stronger than A106 supports on a like-for-like basis.

## Section 6. The mechanism

| Pt | Support | Notes |
|---|---|---|
| 1 | P | A346 "holds for Australia only"; regions not tested; the flat range is 5% or 8% to 100%, not 10% to 99%. "The reading comes from an evaluator test", no saved output. |
| 2 | P | A345 and A324 support pasture binding nationally. A223 sets -0.3% (improved release) against -26% (corrected release); the contrast also depends on the model applying the grain factor to pasture, which is untested. |
| 3 | P | No claim row for the diet grid (gap 1). A258 (+85% at 5%) is a different quantity. B216 says the rise-then-fall holds on the corrected release only; on the improved release no meat is the highest point (X7). |
| 4 | P | A116 is on the state-yield basis; the diet-grid result for SA Arid Lands has no row. |
| 5 | S | A285, A296, A301 (on the published base, as stated). |

Logic: the section explains a mechanism that is release-dependent without saying so; name the release in points 3 and 4.

## Section 7. The long term

| Pt | Support | Notes |
|---|---|---|
| 1 | S | A160, A161. |
| 2 | P | Problem 5. A009 compares the 2011 point (no range) with the 2025 Monte Carlo spread. A008's note still carries the superseded range "14.3 to 17.8" and A003's "35.9 to 45.1" (decision 27 replaced them with 13.4 to 16.5 and 36.3 to 45.8). |
| 3 | S | A152 to A159, A162. A161 records three fibre levers (wool fibre +46%, natural fibre +26%, fibre -29%) absent from the README table, larger than several listed; the top two still hold. |
| 4 | S | A031, A032, A143, A146, A149 to A151 (A150 notes Northern Gulf carries a land-definition flag). |
| 5 | S | A035, A039, A040, A041 (artefact and non-robust sets overlap; 1 + 3 + 2 is not 4). |
| 6 | P | "About a third": 33% in 2011, 38% in 2025 (A145, A148); 38% is nearer two fifths. These shares are on each zone's own yields; section 5's NRM long-term share is 20% and 23%. |
| 7 | S | A306, A312. |

Cross-paper: X1, X2. Logic: "the plan covers a smaller share of a larger population" follows from A010, A011, A013.

## Section 8. Shocks and food security by region

| Pt | Support | Notes |
|---|---|---|
| 1 | P | A200 statement against its own note (three states). |
| 2 | S | A163, A167, A171, A179, A183, A187, A014, A196, A175, A191, A195. |
| 3 | P | A197 says "85% at a 1-in-10 year and 91% at a 1-in-100 year, in both vintages"; 2011 is 84% and 92% (A169, A177). Counts are reported bare, which N-A3 (decision 66) rules out for section 3 on the ground that "a bare count would overstate what changed". |
| 4 | P | A199's five 2025 regions include North East Victoria (problem 1) and Wet Tropics and Rangelands, whose 2025 average-year status is "not robust to the range" in `regional_flips.csv`. None of the flip tests is applied to this count. |
| 5 | P | A166 to A198: 0.63, 0.55, 0.51, 0.46 hold on own-zone yields; section 5 gives 44% for the same partition (problem 2). A198 writes "55% (16.9 against a population of 27.6 million)", which mixes a share of capacity with a population. |
| 6 | P | A208 to A216 are `unverified`. All are on the improved release, so the waste scenario reads +8.67% short and -4.14% long here and +16.4% and -8.2% in section 11 (A246, A247, corrected). A225's note still says drought-proofing "+57%" (decision 28 made it +60%). The grain-store releases are not frozen. |
| 7 | P | L154 is the Murray-Darling Basin, not the nation. L218 supports "ENSO and IOD explain 30 to 41% of wheat variability"; decision 51 asks for "partly correlated across the southern states"; "correlated" alone is stronger than the source. DISCUSSION_MEASURES D5 still reads "because the states do not fail together". |
| 8 | P | The scope writes "22 million at home plus 40 million abroad, PMSEIC as reported by Lawrence". L136 (PMSEIC, full text) says 60 million and "some 40 million" abroad and "does not add the two"; the 22 is Lawrence's own figure (L224 p. 30, "no base year stated"). Attribute 22 plus 40 to Lawrence, Richards and Lyons, citing PMSEIC for the 40 only. |

Consistency: point 6 against section 11 point 4 (same named measure, two values); open-decisions list cites decision 44, which decision 72 replaced. Cross-paper: X9. Logic: "regional self-sufficiency fails sooner than national" is supported on own-zone yields, but the purpose's "more regions sit on the edge in 2025 than in 2011" rests on an untested count (point 4).

## Section 9. How sure are the regional results

| Pt | Support | Notes |
|---|---|---|
| 1 | P | "Thirteen input choices": twelve vary in 2025 (B253; A342 note says the benchmark is constant at 0.4 in 2025-fixed). |
| 2 | P | Problem 5. |
| 3 | P | Robustness is tested on the 2025 range only (A045). The method tier is not a test in the flip classification, though A305 and A309 show Corangamite (2025) and Mackay Whitsunday (2011) change status between corrected and improved. |
| 4 | P | Two of five ends have no claim row (gap 2). The long-term benchmark end (A342) has no effect in 2025-fixed, so listing it as one of five active judgements overstates. The judgement ends drive most of the width: the meat window alone explains 81% of short-term variance (B117) and 36% of long-term (B120); the resilience table 52% of long-term (B119), and its 50/50 weight is a judgement end. |
| 5 | S | A278, A279, A286, A287, A294, A295, A302. |
| 6 | S | A280 to A285, A288 to A293, A296 to A301, A303 (base 2025-mirror per V31c). |
| 7 | P | A304 to A307 verified; A308 verified; A309 and A310 `unverified`. |
| 8 | S | A314 as corrected (interaction -2.88 and +3.20 million). Gap 3 is closed. |

Cross-paper: X3, X4, X5. Logic: "a reader can rely on" the regional results is stronger than the evidence while flips are untested against tier and the range width rests mostly on judgement ends without rows.

## Section 10. Regions in depth

| Pt | Support | Notes |
|---|---|---|
| 1 | S | A071 (V31b). |
| 2 | S | A050, A051 (0.491, below the 0.5 rule), A069. A046's note records that `movers.md` calls Hawkesbury "a usable case" with no flag; fix that file's line so the two agree. |
| 3 | S | A053, A054, A344. |
| 4 | S | A055, A149. |
| 5 | S | A056, A343, A036. The 2011 status is 0.96 of balance with no range (see section 3 point 4). |
| 6 | P | SA Arid Lands population moves 31,361 to 8,049 (A067) because the 2025 allocation method differs; the change is a land artefact and a population-method change together. |
| 7 | P | Most cells of `regions_in_depth.csv` have no claim row. |
| 8 | N | No claim row; ERRATA.md records that the 2015 map's verbal conclusion was "not re-tested"; the map inherits the North East Vic population (problem 1). |

## Section 11. Discussion: what would widen the margin

| Pt | Support | Notes |
|---|---|---|
| 1 | P | A275 "field crops, irrigation, more cropland 0 to 2.4%" (OUTLINE "0 to 2%") omits cropland doubled from non-agricultural land, +8.7% (A254, A255). A276 and A327 corrected and verified. |
| 2 | P | The 1990 to 2010 trend comes from L156 Mayberry quoting Wiedemann 2015a (second-hand: the row says "quoted from Wiedemann 2015a"). Decision 47 says fetch 2015a or drop the trend; citing the quotation is neither option. |
| 3 | S | A258 to A261, A256, A257. See X8 on the label "5% meat and eggs". |
| 4 | S | Decision 72 wording; A246 to A251 (A247's mismatch note is resolved in DISCUSSION_MEASURES). |
| 5 | S | A240, A241, A322 (+59.7% printed as +60%). |
| 6 | P | A264 to A266 are on the improved release (base 18.5); drought-proofing is on the corrected release (base 15.6); the frame's "the two largest measures" compares them. A265 and A266 are interpolated with no output file. A318 uses Foran and Poldy's 303 kg, "a 2050 base-case figure applied to the 2025 population" (a projection read as a current rate). Store releases not frozen. |
| 7 | P | A231, A232, A243, A244 `unverified`; "more cropland does almost nothing" holds for cropland from pasture (0%) but not from non-agricultural land (+8.7%). |
| 8 | P | The multiplier 1.60 and the recovery of 15.5 million rest on own-zone yields (problem 2). OUTLINE's "10 to 15 million" should read "about 10 to 16" (15.5 and 9.6). "Recovers" is an upper bound: it assumes products move between regions without loss or cost. |
| 9 | P | A315 equates the FAO meat surplus (1.575) with "the model's 1.5 times", two different measures. A316 applies the capacity factor to meat, which its note says is untested. A317 is `unverified` (second route blocked, X118) and on `2025-organic` (48.0 million), not the corrected release. DISCUSSION_MEASURES D5 prints SA 0.36 and WA 0.49; A321 corrected these to 0.35 and 0.47 (the old values are the thesis archive rows). |
| 10 | S | A277. |

Consistency: point 4 against section 8 point 6; point 1 against A254. Cross-paper: X6, X8, X10. Logic: the frame "a measure is worth what it does to the binding constraint" follows; the ranking of measures crosses releases (point 6).

## Section 12. Limitations and conclusions

| Pt | Support | Notes |
|---|---|---|
| 1 | S | A337, DISCUSSION.md. |
| 2 | S | L179, L180, L181, L182. |
| 3 | P | A126 to A132 and A136 to A139 are `unverified`. A134 says the swaps raise capacity "by about half"; V31d found +62% (+59% with micronutrients), "about three fifths". A132 shows the SA2 share of same-diet national capacity stays 33% to 45%, so diet raises the level at every scale but does not close the scale loss; "diet recovers most of what small units lose" should say "against today's national figure". |
| 4 | P | A243, A244 `unverified`. |
| 5 | S | A153, A323 (as corrected). |
| 6 | P | Rests on A036 (problems 1 and 4). No section 4 claim is cited for question 1, and question 1's wording names population as a cause (section 1 point 8). |
| 7 | S | None needed. |

---

## Summary table

| Section | Points | S / P / N | Contradictions (within Paper A or with DECISIONS.md) | Cross-paper disagreements |
|---|---|---|---|---|
| 1 Introduction | 8 | 4 / 4 / 0 | Q1 wording against decision 62 and section 4 point 2 | X2 |
| 2 Method and data | 8 | 3 / 5 / 0 | "Reports the corrected releases" against sections 8, 9, 11, 12; store releases unfrozen against decision 8; "52" against "53 NRM regions" (section 5) | X3 |
| 3 Short term | 7 | 4 / 3 / 0 | Point 5 against section 4 point 3; Swan in A044 against A049/A052; N-A3 rule applied here but not in section 8 | none |
| 4 Drivers | 7 | 5 / 2 / 0 | Against OUTLINE Q1 and takeaway; ratio convention against sections 3, 7, 8, 10 | none |
| 5 Scale curve | 8 | 4 / 4 / 0 | NRM sum 44% / 23% against sections 7, 8, 11 (63%, 33 to 38%, 1.60x); SA Arid Lands 41 against 28.6 thousand (section 10); A106 against the "2011 corrected only" rule | none (values agree with B171 to B177) |
| 6 Mechanism | 5 | 1 / 4 / 0 | A223 crosses releases | X7 |
| 7 Long term | 7 | 5 / 2 / 0 | Point 6 against section 5 | X1, X2 |
| 8 Shocks | 8 | 1 / 7 / 0 | Waste scenario against section 11; A200 statement against its note; A197 "both vintages" against A169/A177; decision 44 cited, replaced by 72; DISCUSSION_MEASURES D5 against decision 51 | X9 |
| 9 How sure | 8 | 3 / 5 / 0 | Flip robustness untested against tier while A305/A309 show tier flips | X3, X4, X5 |
| 10 Regions in depth | 8 | 5 / 2 / 1 | `movers.md` "no flag" for Hawkesbury against A051 | none |
| 11 Measures | 10 | 3 / 7 / 0 | Waste against section 8; "more cropland 0 to 2%" against A254; drought-proofing (corrected) ranked with stores (improved); D5 values against A321; trend source against decision 47 | X6, X8, X10 |
| 12 Limitations | 7 | 4 / 3 / 0 | Q1 against decision 62 | none |
| **Total** | **91** | **42 / 48 / 1** | | **10 listed below** |

## The ten most important problems, in order

1. **North East Victoria's 2011 population is a copy of Goulburn Broken's.** Both are 204,651 to the person in `baseline/baseline_2011.csv` and every 2011 release; North East Vic then "falls" 44% to 114,355 while its neighbour rises 1%. One of the three "clean and robust" short-term flips (A036, Tier A), one of the five regions that tip at 1 in 10 in 2025 (A199, Tier A), the 2011 over-capacity counts (A029, A164, A165), the net fall (A033, A043), section 10 and the conclusions (section 12 point 6) depend on it. The flip tests check capacity only (A047). *Fix:* new computation. Trace the 2011 North East Vic population to the thesis and the ABS 2011 ERP, correct the input or log it as an error in ERRATA.md, rerun `regional_flips.py`, `shocks_by_region.mjs` and the counts, and add a population-input check to the flip classification (for example, flag a region whose population change departs from its ABS SA2-based change by more than a set share). Then a register change for every dependent row.

2. **"The regions' share of national capacity" has two values in one paper.** Section 5 gives NRM regions 44% short term and 23% long term in 2025 on the state-yield basis (A085, A090; 44% and 20% in 2011). Sections 7, 8 and 11 give 63% short (A166, A182), 33% and 38% long (A145, A148) and "national 1.60 times the regional sum" (A273), on each zone's own yields. The only register row on that basis for the scale curve, A095 (63%), is `unverified`. *Fix:* wording and register. Name the yield basis at every regional sum; say in section 5 that the zone results of sections 7 to 11 are on the local basis, with section 5's state basis the conservative bound; verify A095 and A100.

3. **The narrative credits production; the decomposition credits diet.** OUTLINE's arc and takeaway ("production grew in step with people", "it held because production grew where the people are not") and A329's statement against section 4: of the +8.2 million short-term gain, consumption (+4.18) and the red meat mix (+1.81) are diet settings applied everywhere (73% between them), livestock adds +4.70, crop yields +0.12, land -2.62. OUTLINE question 1 still lists population as a cause, against decision 62. *Fix:* wording. Rewrite the takeaway and question 1 ("how much of the change is land, yields, livestock and diet; population changes status, not capacity") and section 3's purpose to "capacity grew inland, partly through diet change that applies everywhere".

4. **The "clean and robust" flips are not tested against the method tier.** Mackay Whitsunday is under capacity in 2011 on the improved release (148,175 against 137,252; A309, `unverified`), so it does not flip there; Corangamite changes between tiers in 2025 (A305). With problem 1, only North Tasmania passes every test, and its 2011 status is 0.96 of balance with no 2011 range. *Fix:* new computation (status of each flip under published, corrected and improved, both years) and wording of A036, A039 and section 3 point 4; verify A309 and A310.

5. **"The long-term change lies inside the uncertainty range" does not test change.** A009 sets the 2011 point (no range) inside the 2025 5th to 95th percentile; the spread comes from input choices shared by both years, so a change can be real though smaller than the spread. Most of the width is judgement: the meat window explains 81% of short-term and 36% of long-term variance (B117, B120), the resilience table 52% of long-term (B119), and the meat window and the 50/50 resilience weight have no claim rows. *Fix:* wording ("smaller than the spread across input choices for 2025") or a new computation (a paired Monte Carlo of the 2011 to 2025 difference with the shared choices drawn once); add the two missing claim rows.

6. **Releases are mixed across sections while section 2 says the paper is on the corrected releases.** The same waste scenario is +8.67% and -4.14% in section 8 (improved, A207, A208) and +16.4% and -8.2% in section 11 (corrected, A246, A247); the "two largest measures" set drought-proofing (+60%, corrected) beside a two-year store (+64%, improved); A223 contrasts -0.3% (improved) with -26% (corrected); A317 is on `2025-organic`; the store releases are `current`, not frozen (decision 8). *Fix:* new computation (named scenarios and stores on `2025-fixed`, or every figure stated with its release) and freeze `2025-store-1` and `2025-store-2` before print.

7. **Two opposite ratio conventions.** Section 4 uses people over capacity (A363, A364: above 1 is over); sections 3, 7, 8 and 10 use capacity over people (A005, A149, A343, A344: below 1 is over). A reader meets 1.454 and 0.69 for the same kind of statement. *Fix:* wording; choose one convention for the paper and restate the rows in it.

8. **A106 quotes published figures as the corrected finding.** "The 2015 finding (national 40, states 28, regions 23 million) survives the corrections"; the corrected values are 33.3, 25.7 and 21.0 (A106 note), with 25.6 in L013's row, and the 21.0 is on own-zone yields, not the curve's state basis. Quoting the published 2015 values (and A151's "13 of 60") also edges toward the reconciliation the standing rule excludes. *Fix:* register change (A106 statement to the corrected values and basis; settle 25.6 against 25.7) and wording.

9. **Section 8 reports regional tipping counts without the tests section 3 requires.** A199's five 2025 regions include North East Vic (problem 1) and two whose 2025 average-year status is not robust to the range; A197 says "both vintages" where 2011 differs by one point; A200's statement contradicts its note. N-A3 (decision 66) says a bare count overstates what changed. *Fix:* new computation (apply the land, boundary, range and tier tests to the 1-in-10 status changes) and wording of A197, A199, A200.

10. **Literature rows asked to say more than they do.** L153 is cited in section 4 for low 2011 yields after the 2006 to 2010 drought; it reports simulated potential 1990 to 2015 with flat actual yields. Section 1 point 5's "climate has worked against cropping" is stronger than "yield potential". Section 8 point 8 attributes "22 plus 40 million" to PMSEIC, whose report gives 60 and 40 and does not add them. Section 11 point 2 uses Mayberry's quotation of Wiedemann 2015a, which decision 47 does not allow. L099 and L072 are "not reached". *Fix:* wording (drop L153 from section 4 or cite it for the climate trend only; "yield potential since 1990"; attribute 22 plus 40 to Lawrence, Richards and Lyons; drop or source the livestock trend per decision 47) and register (L099 status; L072 acquisition or describe the 340-litre setting without it).

Smaller items for the drafting brief: A134 "about half" should be "about three fifths"; OUTLINE "10 to 15 million" should be "about 10 to 16"; A145 and A148 "about a third" should be "a third to two fifths"; DISCUSSION_MEASURES D5 to 0.35 and 0.47 and decision 51 wording; A003 and A008 notes carry pre-rerun ranges; A225 note "+57%"; A124 names two splits; A113 not to be quoted; section 8 open decisions to cite 72, not 44; `movers.md` Hawkesbury flag line; the scope's evidence-table statuses refreshed from the register.

## Cross-paper disagreements (Paper A scope against Paper B scope and its cited rows)

| # | Topic | Paper A | Paper B | Kind |
|---|---|---|---|---|
| X1 | Corrected value of the thesis long-term figure | 2011 corrected long term 15.35 million (A007); 15.6 is 2025 data (A008) | B189: "1.7 from the thesis long-term figure to its corrected value (9.4 to 15.6)", release `2011-thesis; 2025-fixed` | value and release: B sets a 2025 figure as the correction of a 2011 one (15.35/9.43 = 1.63, not 1.66) |
| X2 | The author's long-term figure | 15.35 to 15.6 million, corrected; 2011 shown as corrected only | Section 1 point 1: "9 to 14 million" among the four figures (published method: 9.4 thesis, 14.1 `2025-mirror`) | wording: B must say "published method" wherever 9 to 14 appears, or readers of both papers see two different long-term figures for one model |
| X3 | Monte Carlo choices | Section 9 point 1: "thirteen input choices"; point 4 lists the 0.30 benchmark as one of five judgement ends | B253: 13 sampled, 12 vary in 2025; B252: the 0.30 end "has no effect in 2025" | wording |
| X4 | Red-meat low end 0.528 | A341: share of meat (unit corrected by V31d) | B251: "share of diet" | unit |
| X5 | Status of the same judgement-end rows | A341, A342 `independently verified with notes` (A342: benchmark drawn in 2025-improved) | B251, B252 `self-checked`, without the improved-release note | register status and wording |
| X6 | Waste tonnages and the decision applied | Section 11 point 4: decision 72; 7.6 Mt is the 2021 Feasibility Study (L242) | Section 6 binds decision 44; gap 2 names "the 2018-19 feasibility study"; decision 44 itself said "7.6 Mt 2018-19 update" | year and source: B follows the superseded decision |
| X7 | Little meat against none | Section 6 point 3 states the rise-then-fall as the model's mechanism | B216: holds on the corrected release only; on the improved release no meat is highest | wording: A must name the release |
| X8 | "5% meat and eggs" | A258: 76.8 million (corrected, measure applied alone) | B179: 103.3 million (improved, guideline diet, direct route of decision 31) | same label, different release and diet route; each paper should name both |
| X9 | Where the national margin fails | A196 and DISCUSSION_MEASURES B: "the margin vanishes at 1 in 20" | B130: failure probability 5.8 to 6.1% a year, about 1 in 16 to 17 | compatible values, but A's wording implies 1 in 20 is the threshold |
| X10 | 15.5 million | A274: what trade between regions recovers (41.5 minus the regional sum 26.0) | B176: the sum over SA2s (15.5 against 41.5) | same number, different meaning; word each so they cannot be confused |

Agreements checked: Monte Carlo ranges (A027, A028 = B112, B113: 36.3 to 45.8 and 13.4 to 16.5); scale shares (A084 to A088 = B171 to B175); 1-in-10 capacity 30.8 (A014 = B245); worst of 100 years 18.9 (A195 = B137, B167); Lawrence's figure confined to Paper A section 8 (decision 46, both scopes).

## Register rows touched

None.

## Wrong-value check

*Example, marked as such.* Section 5 point 4 ("the 2015 finding survives the corrections and extends to SA2") cites A106, a Tier B row whose status reads `independently verified with notes (V31d)`. Read by id and status alone, the point passes. Read by statement and value, the row quotes "national 40, states 28, regions 23 million", the published-method figures; the corrected figures in its note are 33.3, 25.7 and 21.0, and the regions figure is on a different yield basis from the curve the point extends. A drafter following the id would print the published 2015 numbers as the corrected finding.
