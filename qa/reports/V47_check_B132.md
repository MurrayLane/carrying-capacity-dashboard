# V47: blind check of B132 (the 19-choice draws for every zone, the flip tests and the tipping counts)

Brief: `qa/briefs/V47_check_B132.md`; rules `qa/briefs/_checker_rules_results_wave.md`. No git, no subagents, no network. My scripts and draws are in the session scratch folder (`/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v47/`). The only repository file written is this report. No register row, release, `results/` file, analysis file or script was changed.

**Order of work.** My six zones were fixed by the brief before I opened anything. I derived items 1 and 2 for those zones, the factors for item 3 and my tipping counts for those zones before I opened the builder's report, the draws file, `regional_flips-3_wide.csv`, `shocks_ranges_wide_zones.csv` or the edited `monte_carlo.mjs`. At step 2, as the brief allows, I opened `results/ranges_2025-fixed_wide_zones.csv` for the zones I did not run. Of that file I saw only its first four lines (Australia and NSW-ACT) before my own comparison ran.

**How I drew without the builder's script.** I did not open the edited `monte_carlo.mjs`. Instead I used the copy of the script that V44 had run (`scratchpad/v44/copyA/...`, dated before B132). It has the 19 choices of B115 and the X140 stop at zone 45. I made my own copy (`mc_v47.mjs`) with three changes: a zone list (`V47_ZONES`), my own seed (`V47_SEED=47132`), and my own handling of zone 45 (below). The work folder is B41's (`scratchpad/b41/work`), which passes the X054 check and holds `meat_nocal`, `gt_field_2016` and `land_raster`. The model is `web/src/model/evaluator.js` on `2025-fixed`. At the base values my copy gives the release in all 14 zone-and-term results I ran (Australia 41,503,537 and 15,623,209; for example North Tasmania 187,593 and 58,798).

## Tolerance (set before comparing)

* Counts and region names: exact.
* Zone percentiles (my 500 draws against the builder's 2,000): the difference must be within 2 combined standard errors, where the combined error is my bootstrap standard error (2,000 resamples) times sqrt(1 + 500/2000). The builder's 2,000-draw error is taken as half of mine.
* Status across the range (over or under at p5 and p95): exact.
* Byte checks: `cmp` identical.
* Draw-by-draw values (my evaluation of the builder's own parameter rows): within 0.01%. The parameters are printed to 5 decimals, so exact agreement is not expected.

## Wrong-value examples

* `cmp_zones.py` compares my zone percentiles with the builder's file. I fed it a deliberately wrong builder value, North Tasmania's short-term p5 set to 156,393 in place of the file's value. It fails: `57 North Tasmania short p5 builder 156,393 mine 150,506 diff +5,887 (+3.91%) tol 2,845 FAIL`.
* I changed one digit of the Australian column (49882749 to 49882750) and the `cmp` of item 4 reports `differ: char 7, line 1` (exit 1).
* A real error of my own was caught the same way. My first tipping count gave 20, 19 and 25 at 1 in 10 against the builder's 21, 19 and 26. The cause: I took each zone's drought factor as capacity at 1 in 10 over capacity in an average year. For Alinytjara Wilurara, whose capacity is 0, that ratio is 0/0, so the region dropped out of my count. With the SA table factor for that zone (0.701394 and 0.509433), my counts equal the builder's (below).

## My figures

### Item 1. Zone ranges (500 draws, seed 47132, 19 choices, both presets)

Linear percentiles, with my bootstrap standard error in brackets. Short term is the average year.

| Zone | Preset | p5 | p50 | p95 | min to max | Population | Draws over capacity |
|---|---|---|---|---|---|---|---|
| North Tasmania (57) | short | 150,506 (1,272) | 199,990 (5,671) | 261,812 (1,868) | 133,650 to 296,343 | 156,393 | 12.0% |
| North Tasmania | long | 50,487 (719) | 68,454 (1,044) | 91,632 (1,033) | 44,230 to 107,327 | | 100% |
| Mackay Whitsunday (34) | short | 132,836 (1,708) | 165,834 (1,284) | 200,541 (1,591) | 117,736 to 224,123 | 153,841 | 28.8% |
| Mackay Whitsunday | long | 49,695 (407) | 57,461 (379) | 65,963 (377) | 44,009 to 69,280 | | 100% |
| South West Qld (37) | short | 70,927 (371) | 87,294 (719) | 107,187 (936) | 66,291 to 123,130 | 7,109 | 0% |
| South West Qld | long | 17,152 (94) | 20,719 (186) | 24,818 (169) | 15,790 to 27,461 | | 0% |
| Northern and Yorke (45) | short | 271,000 (1,423) | 316,919 (1,581) | 363,404 (2,230) | 244,506 to 394,132 | 92,250 | 0% |
| Northern and Yorke | long | 83,281 (283) | 89,330 (285) | 95,658 (260) | 81,181 to 98,146 | | 72.6% |
| Corangamite (16) | short | 404,593 (3,570) | 493,120 (5,012) | 609,995 (5,199) | 363,808 to 660,866 | 496,373 | 51.2% |
| Corangamite | long | 44,714 (369) | 52,320 (321) | 62,068 (725) | 39,164 to 69,457 | | 100% |
| Rangelands (52) | short | 24,402 (185) | 71,718 (42,881) | 156,170 (1,017) | 22,441 to 175,106 | 157,948 | 96.4% |
| Rangelands | long | 8,858 (37) | 26,807 (16,810) | 50,957 (239) | 8,477 to 53,021 | | 100% |
| Australia (same draws) | short | 31.36 m | 39.09 m | 48.86 m | 26.36 to 55.00 m | 27.61 m | 0.4% |
| Australia | long | 13.35 m | 15.72 m | 18.69 m | 12.67 to 19.61 m | | 100% |

North Tasmania's and Rangelands' medians have very large errors because their draws fall into two groups, one for each land source. Rangelands on the raster land has cropping of 185 km2 against 937 on holdings.

**Zone 45 and the 152 km2.** On the release, zone 45's holdings land totals 33,599 km2 (cropping 13,876, pasture 19,723, non-agricultural 0). The raster variant totals 33,447 (14,587, 14,949, 3,911). I built the raster entry on the release total: I kept the raster cropping and pasture and set non-agricultural land to 4,063 (3,911 + 152). Infrastructure and reserve agree, so I left the reserve-share check in force. The reason for this choice: under the other route (relaxing the check), a raster draw would carry 152 km2 less land than a holdings draw, and that would read as a land-source effect.

I also ran the other route on the same 500 draws. The short term is identical in every draw, because non-agricultural land does not enter the short-term figure. The long term differs in the 250 raster draws by up to 0.44%; p5, p50 and p95 move from 83,281, 89,330 and 95,658 to 82,961, 89,208 and 95,460. Zone 45's long-term status (under capacity at the base, 94,288 against 92,250) is unsettled under either route.

**The national figure is not changed by my choice.** Australia (zone 1) uses its own raster row, which already equals the release total (difference 0). On 300 draws with the default seed, the pre-B132 script on Australia alone and my copy on Australia plus zone 45 give identical Australian columns in every draw. My 500-draw national range (31.36 to 48.86 m short; 13.35 to 18.69 m long) agrees with B115's 2,000-draw range (31.12 to 49.17; 13.31 to 18.77) within sampling error.

### Item 2. Status across the range, and the flips

Each of my six zones, judged on my own ranges (the base status is from `results/2025-fixed.csv`):

| Zone | Short term: 2025 status; holds across p5 to p95? | Long term: 2025 status; holds? |
|---|---|---|
| North Tasmania | under; **no** (p5 150,506 < 156,393) | over; yes |
| Mackay Whitsunday | under; **no** (p5 132,836 < 153,841) | over; yes |
| South West Qld | under; yes | under; **yes** (p5 17,152, min 15,790 > 7,109) |
| Northern and Yorke | under; yes | under; **no** (p5 83,281 < 92,250) |
| Corangamite | over; **no** (p95 609,995 > 496,373) | over; yes |
| Rangelands | under; **no** (the whole 5th to 95th range, 24,402 to 156,170, lies below 157,948) | over; yes |

The flips come from `regional_flips-3.csv` (2011-fixed-3 to 2025-fixed): 8 short-term and 3 long-term. My ranges cover five of them (four short-term ones plus South West Qld long). For the other six I used the builder's zone file.

| Flip | Range used | 2025 status keeps across p5 to p95? |
|---|---|---|
| Wet Tropics, short | builder: 232,918 to 366,733 against 285,138 | no |
| Desert Channels, short (land flag) | builder: 2,666 to 92,723 against 10,875 | no |
| Mackay Whitsunday, short | mine | no |
| Rangelands, short | mine | no |
| North Tasmania, short | mine | no |
| Southern Gulf, short (land flag) | builder: 3,555 to 49,279 against 27,303 | no |
| Corangamite, short (under to over) | mine | no |
| SA Arid Lands, short (land flag) | builder: 9,888 to 29,639 against 8,049 | yes |
| Desert Channels, long (land flag) | builder: 867 to 27,992 against 10,875 | no |
| South West Qld, long | mine | yes |
| SA Arid Lands, long (land flag) | builder: 3,122 to 8,814 against 8,049 | no |

**Short term: 1 of 8 keeps its status (SA Arid Lands, land-definition flag); 0 are clean and robust. Long term: 1 of 3 keeps it (South West Qld); 1 is clean and robust.** These counts are the same whether my ranges or the builder's are used for my zones.

* North Tasmania: my p5 is 150,506 (error 1,272) against 156,393, which is 4.6 standard errors below the population.
* Mackay Whitsunday: my p5 is 132,836 (error 1,708) against 153,841.
* South West Queensland, long term: 17,152 to 24,818 (median 20,719, lowest of 500 draws 15,790) against 7,109.

Both short-term failures depend on the land-source judgement. North Tasmania is over capacity in 24.0% of my holdings draws and 0% of my raster draws. Mackay Whitsunday is over in 13.6% and 44.0%.

### Item 3. Tipping counts (short term, 53 regions)

**The rule.** Each zone's factor is the evaluator's capacity at return period 10 or 20 divided by its average-year capacity. It equals the release-table factor and is the same whatever the land, food amount and waste. The one exception is zone 45: the evaluator ratio is 0.703071 and 0.511437 against the SA table's 0.701394 and 0.509433, a difference of 0.24% and 0.39%, which moves no count. Alinytjara Wilurara has capacity 0 and takes the SA table factor.

Counts of regions over capacity, using my ranges for my six zones and the builder's for the other 47:

| | Central (base) | At each region's p95 | At each region's p5 | Population inside its range | One draw, all regions (p5, p50, p95) |
|---|---|---|---|---|---|
| Average year | 16 | 15 | 23 | 8 | 17, 18, 21 |
| 1 in 10 | 21 | 19 | 26 | 7 | 21, 23, 24 |
| 1 in 20 | 24 | 22 | 26 | 4 | 24, 24, 25 |

The single-draw column is computed from the builder's all-zones draws file with my factors, because only that file holds every region in each draw. The names inside the range are the same as the builder's. So are the tipping regions:
* at the central figure: North East Vic, Burnett Mary, Mackay Whitsunday, Wet Tropics, Rangelands;
* at p95: Corangamite, North East Vic, Mackay Whitsunday, Wet Tropics;
* at p5: Murrumbidgee - ACT, Burnett Mary, SA Arid Lands.

Every count is identical with my six zones taken from the builder's file instead.

### Item 4. National and state draws unchanged

* The Australia columns (and the 19 choice columns) of `monte_carlo_draws_2025-fixed_wide_all.csv`, written as text, are `cmp`-identical to block A of `monte_carlo_draws_2025-fixed_wide.csv` sorted by draw (2,000 rows).
* The 16 national and state columns equal `monte_carlo_draws_2025-fixed_wide_states.csv` in every draw (0 cells differ).
* The edited `monte_carlo.mjs` differs from the pre-B132 copy only in the X140 block (plus B130's earlier loss-factor lines). Its fix is the same as mine: non-agricultural land 4,063 km2.

**The draws themselves.** I evaluated every tenth parameter row of the builder's draws file (200 rows) with my copy for my seven zones. Every value agrees within 0.011%; zone 45 long agrees to 1 person, so the builder's zone 45 handling equals mine.

## Comparison table

| Item | Builder | Mine | Verdict |
|---|---|---|---|
| X140 handling, zone 45 | raster cropping and pasture, non-ag from release total (4,063) | same | pass |
| National draws unchanged (cmp with block A) | identical | identical | pass |
| State draws unchanged | identical | identical (0 cells) | pass |
| North Tasmania short p5, p50, p95 | 148,681; 197,928; 262,636 | 150,506; 199,990; 261,812 | pass |
| North Tasmania long | 49,679; 68,163; 93,561 | 50,487; 68,454; 91,632 | pass |
| Mackay Whitsunday short | 135,581; 165,062; 199,304 | 132,836; 165,834; 200,541 | pass |
| Mackay Whitsunday long | 48,996; 57,774; 66,042 | 49,695; 57,461; 65,963 | pass |
| South West Qld short | 71,265; 86,760; 107,070 | 70,927; 87,294; 107,187 | pass |
| South West Qld long | 17,239; 20,632; 24,761 | 17,152; 20,719; 24,818 | pass |
| Northern and Yorke short p5 | 274,751 | 271,000 (tol 3,182) | **fail at my tolerance; sampling (see note)** |
| Northern and Yorke short p50, p95 | 316,258; 363,496 | 316,919; 363,404 | pass |
| Northern and Yorke long | 83,415; 89,368; 95,800 | 83,281; 89,330; 95,658 | pass |
| Corangamite short | 402,859; 494,156; 611,410 | 404,593; 493,120; 609,995 | pass |
| Corangamite long | 44,416; 52,716; 62,344 | 44,714; 52,320; 62,068 | pass |
| Rangelands short | 24,757; 73,200; 156,292 | 24,402; 71,718; 156,170 | pass |
| Rangelands long | 8,914; 26,492; 50,671 | 8,858; 26,807; 50,957 | pass |
| Australia short, long (same draws) | 31.12 to 49.17; 13.31 to 18.77 | 31.36 to 48.86; 13.35 to 18.69 | pass |
| Base of the draws, six zones | release | release | pass |
| Short flips keeping 2025 status | 1 (SA Arid Lands) | 1 (SA Arid Lands) | pass |
| Short clean and robust | 0 | 0 | pass |
| Short not robust | 7 (names) | 7, same names | pass |
| Long flips keeping status | 1 (South West Qld) | 1 (South West Qld) | pass |
| Long clean and robust | 1 | 1 | pass |
| North Tasmania p5 against 156,393 | 148,681, below | 150,506, below | pass |
| Mackay Whitsunday p5 against 153,841 | 135,581, below | 132,836, below | pass |
| South West Qld long against 7,109 | 17,239 to 24,761, min 15,477 | 17,152 to 24,818, min 15,790 | pass |
| Draws over capacity, North Tasmania; Mackay Whitsunday | 13.5%; 29.4% | 12.0%; 28.8% (500 draws) | pass |
| Average year: central, p95, p5, inside | 16, 15, 23, 8 | 16, 15, 23, 8 | pass |
| 1 in 10 | 21, 19, 26, 7 | 21, 19, 26, 7 | pass |
| 1 in 20 | 24, 22, 26, 4 | 24, 22, 26, 4 | pass |
| Single-draw counts | 17, 18, 21; 21, 23, 24; 24, 24, 25 | same | pass |
| Tipping regions: central, p95, p5 | 5, 4, 3 (names) | 5, 4, 3, same names | pass |
| `regional_flips-3_wide.csv` labels | as in the report | re-derived, same; only the two label columns differ from `-3.csv`; 44 and 44 rows hold | pass |
| Zone 45 shock factor departure | 0.39% | 0.24% (1 in 10), 0.39% (1 in 20) | pass |

**Note on the Northern and Yorke short-term p5.** This is 1 of 42 percentile cells outside 2 combined errors. About two misses are expected by chance at that bar.

* A second seed (47133, zone 45 only, 500 draws) gives 272,478, and the pooled 1,000 draws give 271,583. That is 2.3 combined errors below the builder's 274,751 (the builder's bootstrap error is 938).
* The draw-by-draw test settles that it is not a model difference. On the builder's own parameter rows my copy gives zone 45 short to within 6 people. Also, the zone 45 land handling cannot affect the short term.

I read it as sampling, a difference of 1.2% in a p5 that sits far from the population (92,250), so no status or count moves. It does not change a number in the builder's files.

## Claim rows

| id | Builder's proposed value | My verdict |
|---|---|---|
| A036 | 0 clean and robust short-term flips (was 2); 1 keeps status (SA Arid Lands, artefact) | holds |
| A038 | 7 short-term flips not robust (names) | holds |
| A184 | 21 at 1 in 10 central; 19 to 26 across ranges; 21 to 24 single draw | holds |
| A188 | 24 at 1 in 20; 22 at p95, 26 at p5; 24 to 25 single draw | holds |
| A199 | 5 at central unchanged; 4 at p95, 3 at p5 | holds |
| A402 | 21; 19; 26; seven inside (names); 24; 22; 26; four inside | holds |
| A419 | statement withdrawn or replaced (widened regional draws exist) | holds |
| A056 | values unchanged; 19-choice p5 148,681 below 156,393 | holds (mine 150,506 ± 1,272; below either way) |
| A343 | "clean flip" no longer holds; one of seven inside its 1-in-10 range | holds (my 1-in-10 range 125,490 to 218,296 contains 156,393) |

The builder also lists A039, A041, A042, A043 and A339. My counts agree with them: South West Qld stands; Desert Channels and SA Arid Lands are not robust long term; artefacts and not robust are 3 and 7 short, 2 and 2 long; clean flips are 0 and 1.

## The proposed paper sentences, read for overclaim

* **Section 3.** Supported. Two changes in wording:
  * "The long-term flip of South West Queensland holds in every draw" should read "its 2025 status holds in every draw". The 2011 side is a single figure, 6,848 against a 2011 population of 8,444. The sentence elsewhere says 2011 carries no range, but this clause reads as if the whole flip were drawn.
  * The 29.4% and 13.5% shares rest on the equal-chance land-source judgement. On holdings land alone North Tasmania is over in about a quarter of draws, on the raster land in none. One clause saying so would keep the shares from reading as probabilities.
* **Section 8.1.** Supported. "Taking each region at the 95th and 5th percentile of its own range gives 19 and 26" is stated with its rule, which is right, because no single draw reaches 19 or 26.
* **Section 10.** Supported. "At balance in a 1-in-10 year (capacity 156,413)" is accurate: capacity exceeds the population by 20 people.
* **Conclusion 4: overclaims in its first clause.** "The regional flips that held on 13 settings do not hold on 19" is not true of all of them. South West Queensland held on 13 settings and holds on 19, and SA Arid Lands short term kept its status on both. Suggested: "The two short-term flips that were clean and robust on 13 settings (Mackay Whitsunday and North Tasmania) are not robust on 19; South West Queensland's long-term flip remains so."
* **Conclusion 4: "19 to 26 across the ranges".** This gives each region at its own end at once, which no draw shows. The single-draw spread is 21 to 24. Either quote 21 to 24, or add "each region at its own 95th or 5th percentile".
* **Response-letter words.** Supported.

## What I would do differently

* Report the zone percentiles with their bootstrap errors in `results/ranges_2025-fixed_wide_zones.csv` or the md. North Tasmania's and Rangelands' medians sit between two land-source clusters and are unstable (my standard errors of 5,700 and 43,000).
* Give the flip tests conditional on the land source (holdings only, raster only). The two clean flips fail mainly through that equal-chance judgement, and the paper should say which way each source pushes.
* Guard the factor step against zero-capacity zones (my own slip above). The builder's use of the table factors avoids it.

## Register rows touched

None.

## Rerun

From the repository root, with `S` the scratch folder and `W=$S/../b41/work`:

    MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 V47_SEED=47132 V47_ZONES=1,16,34,37,45,52,57 node $S/mc_v47.mjs $W $S/draws500_pad.csv 500
    MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 V47_SEED=47132 V47_ZONES=45 V47_Z45=relax node $S/mc_v47.mjs $W $S/z45_relax.csv 500
    cd $S && node factors.mjs && python3 summ.py && python3 step23.py && python3 cmp_zones.py

Files read: the two briefs and the shared rules; `qa/reports/B115_monte_carlo_widened.md`; `qa/reports/V44_check_B123.md` (method only); `analysis/sensitivity_2025/README.md` (B115 to B130 sections); `analysis/sensitivity_2025/evaluate.mjs`; the pre-B132 `monte_carlo.mjs` copy; `results/2025-fixed.csv`; `web/public/data/2025-fixed/regions.json`; `analysis/paper_a/regional_flips-3.csv`. Opened last: `qa/reports/B132_regional_widened_draws.md`, `results/ranges_2025-fixed_wide_zones.csv`, `monte_carlo_draws_2025-fixed_wide_all.csv`, `monte_carlo_draws_2025-fixed_wide.csv` (block A), `monte_carlo_draws_2025-fixed_wide_states.csv`, `regional_flips-3_wide.csv`, `shocks_ranges_wide_zones.csv`, `shocks_counts_wide_zones.csv`, `analysis/resilience_2025/tables.csv` (header only), and the X140 block of `monte_carlo.mjs`.
