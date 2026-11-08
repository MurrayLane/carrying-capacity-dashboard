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
| 16 | The pasture-productivity page of Wackernagel and Rees 1996 | in progress: p. 82 (Table 3.3) received 2026-11-08 and filed in the archive; pages 63 to 81 (Box 3.3, p. 80) and 96 still to come |
| 17 | A note to Simpson and Lowe, after 16 | open |
| 26 | The eighth method test (Khorsandi 2022): catalogue only, or run it (scope in qa/reports/B21_khorsandi_scope.md) | taken 2026-11-07: catalogue only (Murray: yes to all) |
| 27 | Monte Carlo ranges: fix the group-factor offset (X054, brief B22) and rerun the full Monte Carlo for 2025-fixed, 2025-mirror and 2025-improved (1,000 draws, all zones), replacing the committed ranges and the headline range values (A027, A028, A009) | taken 2026-11-07: yes (B22, then the rerun) |
| 28 | Drought-proofing measure (X057, X058): recompute by changing the 100-year factor (0.4558 to 0.7279) and widen the livestock rows to every animal product; the measure becomes about +60%, not +57% (A240, A241, A322) | taken 2026-11-07: yes (B25) |
| 29 | Scale curve long term (X062 to X064): evaluate each unit under its state's climate zone, regenerate results/scale_curve.csv and the README, recheck the three diagnosis scripts; the long-term shares fall (2025: 49, 23, 35, 24, 20% instead of 70, 35, 49, 36, 30; claims A079 to A083, A089 to A093) | taken 2026-11-07: yes (B26) |
| 30 | Diet C (nutrition-optimised) is stale (X082): re-optimise A, B and C on the current improved release with the repository's chain, on the corrected server (decision 31), make diet_land.py read them from the repository, regenerate the design-choice table and the README; diet C moves from 248.7 to about 384 million (factor about 7, was 4.65); Tier A B180, B182 | taken 2026-11-07: yes (B39, after the server fix) |
| 31 | Diet route (X083, X085): adopt the direct route (the meat-and-egg, red-meat and activity settings, as the thesis and workbook define a diet); fix the server's write-back (beans once into V169; Other as the mean of its sub-groups); regenerate diet_land.csv (guideline rows 103.6, 100.4, 103.3, 66.9, 58.8, 53.6, 48.3) and the Diet design choice (48.3, 103.3, 2.14); withdraw "a little meat beats none" for the improved release (comparators 2b, B216, SECTION7_DRAFT line 38), keeping it for the fixed release where it holds | taken 2026-11-07: yes (B39) |

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
