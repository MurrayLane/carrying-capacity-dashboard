# Decisions for Murray (quality plan and coordinator)

Written 2026-11-07 in the format Murray's other project uses for decisions: plain language first, one numbered row each, a recommendation, a confidence, a cost and a reason. Answered 2026-11-07: **yes to all seven recommendations.** Row 1 is acted on once steps 0 and 1 are done and the first round has a measured cost.

**In plain words.** The papers must be right before they are published. The plan is for helper sessions to check the work first, and for you to check their checking. These are the choices that set how that runs. "Coordinator" means the session that plans the checks, writes instructions to the helpers and tells you what is verified. "Builder" is a helper that writes scripts. "Checker" is a helper that redoes a piece of work without seeing the first answer.

| # | Decision | Options | Recommended | Confidence | Cost | Why |
|---|---|---|---|---|---|---|
| 1 | Where the coordinator runs and on which model | Cloud session in this project on Fable / cloud on Opus / your machine on Fable / no standing coordinator (this chat does it) | Cloud session in this project, on Fable, started once the registers are built | Medium | Quick to start, reversible; weekly allowance use not yet measured, the first checking round measures it | The registers live in this project; a cloud session is disposable and keeps the work away from TenderFolio's server and secrets; Fable gives the best judgement and uses little because it reads reports, not data. Medium because I cannot yet see how fast it uses the allowance |
| 2 | Stop the coordinator editing the work itself: deny editing in the code, data, results, releases, methods and analysis folders; it may still edit the quality folder and the plan files (decisions, handoff, publication plan) | Yes / No, rely on the written rule | Yes | High | Quick, reversible; I would test that a folder-limited setting really works before relying on it | TenderFolio's coordinator broke its own "never edit" rule twice with the rule written down. The coordinator judges the work, so it must not be able to change the work. Its own reply showed that blocking all editing would stop it keeping notes and plans, so the block is by folder |
| 3 | Which model does the independent checks | Opus / Sonnet / Fable / choose after the first round | Opus for checkers, Sonnet for builders | Medium | Opus uses the shared weekly allowance several times faster than Sonnet, but checks are small jobs; reviewed after round one using the log of what each check caught | Checking is where judgement matters, and a checker from a different model than the builder is more independent. Medium because nobody has measured which model catches more here |
| 4 | Three levels of checking: headline claims by two independent routes, supporting claims by one, context read once | Three levels / everything by two routes / one route for all | Three levels | High | The headline list is probably a few dozen claims, counted when the register is built | Everything twice costs several times more for little extra protection on minor claims; one route leaves the numbers readers will quote with a single point of failure |
| 5 | Ask outside people to check before submission: the authors of the HALF and people-per-hectare methods check our reconstructions, and a land-use planning colleague reads the methods paper | Both / planning reader only / neither | Both, asked after our own checks pass so the request is short | Medium | Your time and a few emails; no spend; the authors may disagree with a reconstruction, which is the point | AI checks cannot judge whether a critique of someone's method is fair; their reaction before publication costs far less than after |
| 6 | Publish the claims and sources registers with the archive | Registers only / registers and the defect log / neither | Registers only | Medium | Quick; reversible until release | Readers can trace every number, which is part of the quality claim; the defect log is working notes, not evidence for readers |
| 7 | Go ahead with steps 0 and 1: build the two registers, a one-page card of standing decisions and never-do rules that the coordinator re-reads after every compaction, and the automatic checks that flag stale or typed numbers (no result changes); a yes leads to the first checking round on the methods paper's headline numbers | Yes / not yet | Yes | High | Step 0 session-size, step 1 small, Sonnet builders; allowance share unmeasured, the first job reports it | They change no results and every later step depends on them; stale figures and hand-typed tables are what have already cost us |

**Recommended combined action:** yes to 7 first; yes to 2, 3 and 4 so the checks start with the rules in place; 1 is settled once step 7 is done and the first round has a measured cost; 5 and 6 are needed only before submission.

*Reply "yes" to take all recommendations. A bare "yes" always means every row's Recommended option (`CARD.md`).*

## Answered 2026-11-07 (second table): yes to all three

| # | Decision | Taken | Done |
|---|---|---|---|
| 8 | Freeze the six paper releases now (Gate 0) | Yes | 0ede432: 2011-fixed, 2011-improved, 2025-mirror, 2025-fixed, 2025-improved locked and frozen; 2011-corrected already was; tests 32 of 32 pass |
| 9 | Murray adds his own published papers and thesis chapters to the private archive | Yes | Murray's action; waiting on the upload |
| 10 | Keep the builder's relabelling of secondary-source figures from read to reported | Yes | kept |

## Answered 2026-11-07 (third table): yes

| # | Decision | Taken | Done |
|---|---|---|---|
| 11 | Fix the HALF implementation, state the fat treatment, reconcile with the independent rebuild to 2% | Yes | B11 running |

## Answered 2026-11-07 (fourth table): yes

| # | Decision | Taken | Done |
|---|---|---|---|
| 12 | Simpson and Cassidy rows as ranges across the two readings | Yes | B13 running |

## Answered 2026-11-07 (fifth table)

| # | Decision | Taken | Done |
|---|---|---|---|
| 13 | One reading of the weekly usage figure | Replaced by the measured rates from Murray's other coordinator (card, calibration 2026-11-07) | done |
| 14 | Inference tests on Simpson's conventions | Yes | V07 running |

## Open (2026-11-07, evening)

| # | Decision | Status |
|---|---|---|
| 15 | Google Scholar cited-by and keyword exports | closed: the cited-by lists were obtained from OpenAlex (qa/reports/cited_by_openalex_2026-11-07.md) |
| 16 | The pasture-productivity page of Wackernagel and Rees 1996 | closed 2026-11-08 with a finding: the 1996 book names its sources (FAO for crops, agricultural handbooks for pasture) but prints no rate (B44); Wackernagel's 1994 UBC thesis, supplied by Murray, prints them (B45, `qa/reports/B45_wackernagel_thesis.md`): pasture from Ensminger 1978, 1.24 cattle/ha; sheep meat 34 kg/ha/yr (p. 285); wool 10.5 gross, 14.2 kg/ha net; FAO 1990 world crop yields (Table A2.2, pp. 295 to 296). Simpson's 1.758 ha of food pasture comes out at 1.713 (2.6% short) if all red meat is charged at the sheep rate with no dairy on pasture; his 0.312 ha of plant-food crop stays unreproduced (0.071 to 0.094 on the thesis yields); his 0.854 ha of wool pasture implies 12 kg of clean wool a person, not plausible |
| 17 | A note to Simpson and Lowe | closed 2026-11-08: Murray decided not to approach the authors; the Simpson figures are reconstructed from the published sources alone (decision 32) and reported as reproduced or not reproduced on that basis |
| 26 | The eighth method test (Khorsandi 2022): catalogue only, or run it (scope in qa/reports/B21_khorsandi_scope.md) | taken 2026-11-07: catalogue only (Murray: yes to all) |
| 27 | Monte Carlo ranges: fix the group-factor offset (X054, brief B22) and rerun the full Monte Carlo for 2025-fixed, 2025-mirror and 2025-improved (1,000 draws, all zones), replacing the committed ranges and the headline range values (A027, A028, A009) | taken 2026-11-07: yes (B22, then the rerun) |
| 28 | Drought-proofing measure (X057, X058): recompute by changing the 100-year factor (0.4558 to 0.7279) and widen the livestock rows to every animal product; the measure becomes about +60%, not +57% (A240, A241, A322) | taken 2026-11-07: yes (B25) |
| 29 | Scale curve long term (X062 to X064): evaluate each unit under its state's climate zone, regenerate results/scale_curve.csv and the README, recheck the three diagnosis scripts; the long-term shares fall (2025: 49, 23, 35, 24, 20% instead of 70, 35, 49, 36, 30; claims A079 to A083, A089 to A093) | taken 2026-11-07: yes (B26) |
| 30 | Diet C (nutrition-optimised) is stale (X082): re-optimise A, B and C on the current improved release with the repository's chain, on the corrected server (decision 31), make diet_land.py read them from the repository, regenerate the design-choice table and the README; diet C moves from 248.7 to about 384 million (factor about 7, was 4.65); Tier A B180, B182 | taken 2026-11-07: yes (B39, after the server fix) |
| 31 | Diet route (X083, X085): adopt the direct route (the meat-and-egg, red-meat and activity settings, as the thesis and workbook define a diet); fix the server's write-back (beans once into V169; Other as the mean of its sub-groups); regenerate diet_land.csv (guideline rows 103.6, 100.4, 103.3, 66.9, 58.8, 53.6, 48.3) and the Diet design choice (48.3, 103.3, 2.14); withdraw "a little meat beats none" for the improved release (comparators 2b, B216, SECTION7_DRAFT line 38), keeping it for the fixed release where it holds | taken 2026-11-07: yes (B39) |
| 32 | Add a third Simpson build on the thesis rates (all red meat at 34 kg/ha, no dairy on pasture; plant crop at the FAO 1990 world yields of Table A2.2) to simpson_food.py, regenerate the Simpson row of the cross-method table and the README, and state the reconstruction as "pasture reproduced within 3% at a sourced rate; plant crop not reproduced" (Tier A rows B033 to B046) | taken 2026-11-08: yes (B47, then V22) |
| 33 | Tone of the methods paper: no emphasis on other authors' methodological shortcomings; state the access we had and the assumptions we made, and report reproduced or not reproduced on that basis | taken 2026-11-08 (Murray's direction); recorded on the card |
| 34 | Gap attribution for each method test: vary the candidate causes of each residual one at a time, report how much each explains, change no output, state the attribution in the README and the papers | taken 2026-11-08: yes (B49, then V25) |
| 35 | Harmonised comparison for Paper B section 5: every method on one population, data year, land base and consumption data, each keeping its defining choices (productivity basis, diet treatment, exports, item reading, weather record); the authors'-own readings kept beside it; the footprint at Australian productivity shown as the one sanctioned sensitivity (Wackernagel and Rees 1996 p. 78) | taken 2026-11-09: yes (B58, then V26); Murray accepted the framing on the interim table ("equalising inputs removes the spread within each method but not the gap to the model, so the gap is the method"), figures to be quoted only after V26 |
| 36 | Literature for the reviews (B61, `qa/reports/B61_lit_review_scope.md`): Murray sources the ten priority works (list in the report, section e) and his own copy of the 2010 Land Use Policy review, which is missing from the archive | taken 2026-11-09: yes (Murray's action; the ten links are in the chat of 2026-11-09 and in the report) |
| 37 | A reading pass over the classic concept papers already in the archive but not read in this project (Hardin, Seidl and Tisdell, Sayre, Meyer and Ausubel, Price, Cohen 1995, Peters 2007, Fairlie, Rees 1992 and 1996, Hopfenberg, Gilland, Chisholm), into the register, so Paper B section 2 rests on read sources | taken 2026-11-09: yes (B62); kept short, the section leads with the post-2016 debate (recency rule) |
| 38 | After the acquisitions arrive, a second sweep for the thin points of Paper A (Australian population debate 2011 to 2025, food security in Australian planning, drought and climate effects on farming, the evidence behind each measure) with the candidate list of B61 as the start | taken 2026-11-09: yes, run now and recency-weighted (B63) |
| 39 | Gifford, Kalma, Aston and Millington 1975 (Search 6(6)) is not held by QUT: cite it second-hand through Henry and Godden 1995, saying so in the paper; no document-delivery or Trove request | Yes (Murray, 2026-11-10: "1. second hand") | register L002 noted; drafting rule for Paper B section 4 |
| 40 | Wiedemann feedlot paper (L157) cited as 2017 (volume 57) | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 41 | LUTO (Gao 2017, L208) sits under optimisation models in Paper B section 4, not resource-flow models | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 42 | Paper B section 3 states the selection rule (works from 2011 by publication year; earlier works for lineage only; exclusions named) and cites Grant and Booth for the review type, Greenhalgh for the narrative style | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 43 | Paper B section 2 takes in the post-2016 planetary-boundaries and overshoot debate in one paragraph, saying 'planetary limits' where the authors do | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 44 | Waste: the 6% setting is described as halving the retail-and-consumer share (UN target scope); every tonnage carries its year (7.3 Mt 2016-17 baseline; 7.6 Mt 2018-19 update) | Yes, reworded by decision 72 (B83 found the national goal is whole-chain) | see B72 to B75 and the drafting briefs |
| 45 | Outline subsections numbered so register labels (A11.5, B8.2 and so on) resolve (B72) | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 46 | Lawrence 2013's 22 million at home plus 40 million abroad quoted only in Paper A section 8, with source and a line that its basis differs from the model's | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 47 | Livestock past trend 1990 to 2010: Murray fetches Wiedemann 2015a via QUT; if not held, the trend is dropped | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 48 | Grain store sizes (one and two years) are stated as the model's own scenarios; no Australian source | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 49 | Seven rows read from open copies without pages (L144, L146, L164, L165, L182, L185, L191) get a targeted page-level read before drafting (B73) | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 50 | Government documents (Intergenerational Reports, Centre for Population, 2023 food security inquiry, National Food Waste Strategy and Baseline, Future Drought Fund review) fetched from government sites, registered and read as grey literature (B74) | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 51 | 'The states do not fail together' reworded at drafting to carry Anderson 2019 (bad wheat years partly correlated across the southern states) | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 52 | Paper A section 1 names its three context points; drought wording says 'yield potential since 1990' (Hochman) and 'simulated profit since 2001' (Hughes), each sourced | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 53 | Farm diesel share (84%) stays a model statement, with the NFF figure cited as quoted in Soliman Hunter 2021 | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 54 | write_readme.py and summarise_mc.py strings fixed so a rerun keeps B69's wording (13.9%; thirteen choices) (B75) | Yes (Murray, 2026-11-11: "yes") | see B72 to B75 and the drafting briefs |
| 55 | Journals: Paper B to Land Use Policy, Paper A to Population and Environment (word limits to be checked by Murray) | Yes (Murray, 2026-11-11: "yes") | see V28, B76 to B78 |
| 56 | Paper B section 2: Rockström et al. 2009 acquired by Murray via QUT for the planetary-limits paragraph | Yes (Murray, 2026-11-11: "yes") | see V28, B76 to B78 |
| 57 | Paper B section 4: the diet-optimisation family renamed 'optimisation models (diet and land use)' (LUTO fits); foodshed studies treated as the spatial form of resource-based land and diet | Yes (Murray, 2026-11-11: "yes") | see V28, B76 to B78 |
| 58 | Paper B section 5: no 2011 check column; the harmonised comparison is the check | Yes (Murray, 2026-11-11: "yes") | see V28, B76 to B78 |
| 59 | Paper B section 6 scale points: nation, states, SA2 sum | Yes (Murray, 2026-11-11: "yes") | see V28, B76 to B78 |
| 60 | Claim B243 reworded to the checklist items that moved the answer more than 1.2 times (the land base moved it 1.09) | Yes (Murray, 2026-11-11: "yes") | see V28, B76 to B78 |
| 61 | Paper B section 7 matrix: a blind checker re-derives the 28 ratings from the tests (V28) | Yes (Murray, 2026-11-11: "yes") | see V28, B76 to B78 |
| 62 | Paper A section 4 decomposition rerun on the corrected releases; population reported as a status change, not a cause (B76) | Yes (Murray, 2026-11-11: "yes") | see V28, B76 to B78 |
| 63 | Stale claim rows A119, A124, A140, A225, A314, A333 re-derived from their analysis files and corrected; any Tier A value change comes back to Murray before it is made (B77) | Yes (Murray, 2026-11-11: "yes") | see V28, B76 to B78 |
| 64 | Nine Paper B rows read from open copies without pages (L202, L207, L211 to L214, L217, L219, L220) get a page-level read (B78) | Yes (Murray, 2026-11-11: "yes") | see V28, B76 to B78 |
| 65 | Gap-attribution figures registered as claims; L050 (Wackernagel and Rees 1996) marked read from the filed scan (B77, B78) | Yes (Murray, 2026-11-11: "yes") | see V28, B76 to B78 |
| 66 | Paper A section questions N-A1 to N-A11 taken as the scoper recommends in papers/A_results/SECTION_SCOPE.md | Yes (Murray, 2026-11-11: "yes") | see V28, B76 to B78 |
| 67 | Monte Carlo method references (Latin hypercube: McKay et al. 1979 or Helton and Davis 2003; variance shares: Saltelli et al. 2008) registered (B78) | Yes (Murray, 2026-11-11: "yes") | see V28, B76 to B78 |
| 68 | Corrected-tier decomposition (B76) blind-checked by a second route (V29) before Paper A section 4's scope is rewritten to the corrected ordering (B80) | Yes (Murray, 2026-11-11: "yes") | V29, B79, B80 |
| 69 | Section 7 matrix: 'partly' for HALF and Cassidy on explaining the 9 to 100 million range and for the footprint on regional planning (V28's reasons) | Yes (Murray, 2026-11-11: "yes") | V29, B79, B80 |
| 70 | Section 7 draft's reasons: 134 to 343 million corrected to 103 to 343 (B79) | Yes (Murray, 2026-11-11: "yes") | V29, B79, B80 |
| 71 | Two stale lines logged as defects and fixed: scale-curve README line on the contiguous split; the published-tier decompose.mjs comment on land and population layers (B79) | Yes (Murray, 2026-11-11: "yes") | V29, B79, B80 |
| 72 | Waste wording (replaces decision 44): the model's 6% setting halves the model's retail-and-consumer loss share, mirroring UN Target 12.3; Australia's own goal (National Food Waste Strategy 2017, p. 8 printed) is whole-chain halving by 2030; the 2016-17 Baseline is 7.3 Mt (L231) and the later 7.6 Mt estimate is the 2021 Feasibility Study (L242), each named with year and source. Applies to `analysis/waste_2025/README.md` lines 65 to 70 and the Paper A scope A11.3 block (B84). The Baseline final report and the Feasibility Study stay optional | Yes (Murray, 2026-11-11: "Yes") | B84 |
| 73 | Provenance audit scope: the facts the two section scopes cite (476 claims, 36 data sources, 179 literature rows), not every register row | Yes (Murray, 2026-11-13: "Yes") | see the briefs named |
| 74 | P1 Sources: blind checkers open each of the 36 data sources behind the cited claims, confirm file, hash and origin, and check a sample of pipeline values against the source (V30a to V30c) | Yes (Murray, 2026-11-13: "Yes") | see the briefs named |
| 75 | P2 Claims: second route for the 209 one-route cited claims, grouped by analysis folder; text facts checked against their documents (V31 series; second half) | Yes (Murray, 2026-11-13: "Yes") | see the briefs named |
| 76 | P3 Literature: page-level reads for the 48 rows read before the page rule and reads for the 13 weak rows (B85 series) | Yes (Murray, 2026-11-13: "Yes") | see the briefs named |
| 77 | P4 Logic: one Opus checker per paper tests that each section's evidence supports its point, with no contradiction within or between the papers (V32a, V32b; second half) | Yes (Murray, 2026-11-13: "Yes") | see the briefs named |
| 78 | P5 Provenance map: a generated per-paper trace (fact to claim to output cell to script to data row to original source, with each link's status) and a gate 4 digest (B86 tool now; digest after P2 and P4) | Yes (Murray, 2026-11-13: "Yes") | see the briefs named |
| 79 | Pacing: first half now (P1, P3, P5 tool); second half (P2, P4, digest) on Murray's word | Yes (Murray, 2026-11-13: "Yes") | see the briefs named |
| 80 | Register tidy from V30a to V30c: source statuses to verified, stale hash and row count corrected, origins recorded, defects logged (B87) | Yes (Murray, 2026-11-13: "Yes") | see the briefs named |
| 81 | External copies: the four ABS NRM cubes stored in the archive (data/abs_cubes); FAOSTAT bulk files kept by hash and URL (B87) | Yes (Murray, 2026-11-13: "Yes") | see the briefs named |
| 82 | Cited literature rows with no file: Murray fetches the number-bearing ones from a list with QUT links; the rest stay cited as reported | Yes (Murray, 2026-11-13: "Yes") | see the briefs named |
| 83 | Second half of the audit: claims second route (V31a to V31e, then merge B89), logic check per paper (V32a, V32b), gate 4 digest | Yes (Murray, 2026-11-13: "Yes") | see the briefs named |

## Answered 2026-11-07 (sixth table): yes to all

| # | Decision | Taken | Done |
|---|---|---|---|
| 18 | Fresh coordinator session from HANDOFF.md and the card | Yes | Murray's action; HANDOFF carries the queue |
| 19 | Generated README tables | Yes | B16 running |
| 20 | Results-paper checking wave (Opus, 4 to 6 checks, 2 to 3 points) | Yes | queued after B16 (the checkers should read generated tables); the fresh session briefs it |
| 21 | Reading list into the register | Yes | B17 running |
| 22 | Regions for section 10: Hawkesbury-Nepean-Sydney, Murray and Murrumbidgee, Avon, North Tasmania, SA Arid Lands with Eyre Peninsula | Yes | B18 running |
| 23 | Correction notes sent before the methods paper is submitted | Yes | Murray's action when ready; drafts in CORRECTION_NOTES.md |

## Answered 2026-11-07 (seventh table): yes to both

| # | Decision | Taken | Done |
|---|---|---|---|
| 24 | Khorsandi's method into the catalogue now; an eighth test scoped after the Paper A wave | Yes | outline section 4 updated; scoping queued in HANDOFF |
| 25 | Institutional copies of Giampietro and Saltelli 2014, Sobels 2010, Ridoutt 2017, Bryan 2016, Chapman and Byron 2018 to the archive | Yes | Murray's action |
