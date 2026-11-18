# B132: the 19-choice draws for every region; flip tests and tipping counts redone (decision 134)

Brief: `qa/briefs/B132_regional_widened_draws.md`. No git, no subagents, no network. Written only under `analysis/sensitivity_2025/`, `analysis/paper_a/`, new files under `results/`, `qa/defects.csv` (X140 only) and this report. No register row, paper, frozen release or existing output was edited; every existing output is kept and the new files carry the variant in the name.

## Summary (the flips that survive first)

* **Short term: none of the eight flips is clean and robust on the 19-choice ranges; one keeps its 2025 status across the 5th to 95th percentile, SA Arid Lands, and it carries a land-definition flag.** On the 13-choice ranges five kept it (Desert Channels, Mackay Whitsunday, North Tasmania, Southern Gulf, SA Arid Lands) and two were clean and robust (Mackay Whitsunday, North Tasmania). Seven no longer keep it: Wet Tropics, Desert Channels, Mackay Whitsunday, Rangelands, North Tasmania, Southern Gulf and Corangamite (the under-to-over flip).
* **Long term: one of the three flips keeps its 2025 status, South West Queensland, which is also the one clean and robust flip.** Its 5th to 95th percentile is 17,239 to 24,761 against a population of 7,109 (13-choice: 20,634 to 25,661; base 23,533); the lowest of the 2,000 draws is 15,477. It is under capacity in every draw. Desert Channels and SA Arid Lands (both artefact-flagged) do not keep their status.
* **North Tasmania, short term:** 5th percentile 148,681 against a population of 156,393 (13-choice 174,487); 5th to 95th percentile 148,681 to 262,636. **Mackay Whitsunday:** 5th percentile 135,581 against 153,841 (13-choice 174,231); range 135,581 to 199,304. Both are below their populations, as R05a's rough reading said (about 150,700 and 146,600). Draws over capacity: North Tasmania 13.5%, Mackay Whitsunday 29.4%.
* **Tipping counts (53 regions: 52 regions and the Northern Territory), widened ranges, each region at its own 5th or 95th percentile.** 1 in 10: 21 over capacity at the central figure, 19 at the 95th-percentile capacity, 26 at the 5th; seven regions have their population inside their range. 1 in 20: 24, 22 and 26; four inside. Within single draws (all regions together): 21, 23, 24 (5th, 50th, 95th percentile) at 1 in 10 and 24, 24, 25 at 1 in 20. The 13-choice counts were 21, 21, 22 and 24, 24, 24.
* **X140 fixed** by building the raster-land variant on the release land for zone 45. No national or state draw changes (checked). All 60 zones run.

## 1. The fix (X140)

**Cause, found by comparing the variant with the release.** In zone 45 (Northern and Yorke) the release land (ABS holdings: cropping 13,876, pasture 19,723, non-agricultural 0 km2) totals 33,599 km2 in those three; the `land_raster` variant's (raster cropping 14,587, pasture 14,949, non-agricultural 3,911) totals 33,447. The variant sets non-agricultural land to the area left in the zone (never below 0); the release's holdings exceed the zone's area by 152 km2, so its non-agricultural land is clipped at 0. Infrastructure (67) and reserve (629) agree, and no other zone differs by more than 2 km2. The 152 km2 is the release's excess, not a fault of the raster.

**Choice: the raster land is built on the release land for that zone** (the first route in the defect). The only edit to `monte_carlo.mjs` is in the check block of the `MC_WIDE` setup: zone 45's raster entry keeps the raster cropping and pasture and takes non-agricultural land from the release total (33,599 less 14,587 less 14,949 = 4,063 km2, against 3,911). Its total land is then the release's, as in every other zone, so the raster draw changes the source of cropping and pasture and nothing else. I did not relax the land check, because that leaves zone 45 with 152 km2 less land under a raster draw than under a holdings draw, which would read as a land-source effect when it is a clipping effect. The edit applies only to zone 45 and only to a difference of at most 200 km2, prints one line when it applies, and is recorded in the script's comment and in `analysis/sensitivity_2025/README.md` (section B132).

**Confirmed no national or state draw changes:**
* The Australian short and long columns of the new draws file equal block A of `monte_carlo_draws_2025-fixed_wide.csv` as text in all 2,000 draws (difference 0), and its 19 choice columns agree.
* The 16 columns of Australia and the seven states equal those of `monte_carlo_draws_2025-fixed_wide_states.csv` to the person (difference 0).
* Without `MC_WIDE`, and with `MC_WIDE` on the default eight zones, a `fixed` run of the edited script equals the unedited script byte for byte (`cmp`, two settings).
* The base values of the draws (a `fixed` run with `MC_ZONES=all`) equal the release in all 120 zone-and-term results.

## 2. The draws

`MC_RELEASE=2025-fixed MC_LONG=1 MC_WIDE=1 MC_ZONES=all`, 2,000 Latin hypercube draws, the 19 choices of B115, seed 20261027, both presets, 60 zones: `analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide_all.csv`. Ranges: `results/ranges_2025-fixed_wide_zones.csv` (zone, preset, p5, p50, p95, min, max, base, then name, kind, population, whether p5 is below the population; 120 rows). Summary table: `analysis/sensitivity_2025/monte_carlo_2025-fixed_wide_all.md`.

How the run was made: one process takes about two hours, so I ran four interleaved parts (draws i with i modulo 4 equal to 0 to 3) of a temporary copy of the script that differs only in the start and step of the draw loop, merged in draw order, and deleted the copy. The same copy on 20 draws, merged, equals the script's own 20-draw run byte for byte. The README gives the single-process command, which yields the same file. If the coordinator wants the part option in the script itself, that is an edit outside this brief.

**Zones whose 5th percentile is below their population:** 74 of the 120 zone-and-term rows, of which 57 are over capacity at the base already. The 17 that are under capacity at the base (their status is no longer settled by the draws):
* Short term (10): NSW-ACT, SA, WA; North East Vic, Desert Channels, Mackay Whitsunday, Southern Gulf, Wet Tropics, Rangelands, North Tasmania.
* Long term (7): Desert Channels, Northern Gulf, Kangaroo Island, Northern and Yorke, SA Arid Lands, SA Murray Darling Basin, South West WA.

Figures for each are in the md file (for example NSW-ACT short term 7,956,910 against 9,076,673; Wet Tropics 232,918 against 285,138; Rangelands 24,757 against 157,948; Northern and Yorke long term 83,415 against 92,250). Australia's short-term 5th percentile (31.1 million) is above its population. The land source drives the wide regional ranges: with the raster land, Desert Channels' short-term capacity has a median of 2,972 against 82,215 on holdings land (1,000 draws each), and North Tasmania's is 234,040 against 166,406.

## 3. Flip tests

`python3 -I analysis/paper_a/regional_flips.py analysis/paper_a/movers-3.csv analysis/paper_a/regional_flips-3_wide.csv results/ranges_2025-fixed_wide_zones.csv`. `regional_flips.py` takes an optional third argument (the ranges file); with none, and on `movers-3.csv`, it reproduces `regional_flips.csv` and `regional_flips-3.csv` byte for byte (`cmp`).

**2011 basis.** The 2011 status is the base figure; no region has draws for 2011 on any basis (the 13-choice basis never had 2011 ranges; the B133 paired draws are national only and give no regional 2011 range). Only the 2025 range is widened. Rule unchanged: an over-capacity 2025 status needs the population above the 95th-percentile capacity, an under-capacity one below the 5th.

| | Flips | Keep their 2025 status across p5 to p95 | Clean and robust | Not robust |
|---|---|---|---|---|
| Short, 13 choices | 8 | 5 | 2 | 3 |
| **Short, 19 choices** | 8 | **1** (SA Arid Lands, artefact flag) | **0** | **7** |
| Long, 13 choices | 3 | 2 | 1 | 1 |
| **Long, 19 choices** | 3 | **1** (South West Qld) | **1** | **2** |

Across all 106 region-and-term rows the count whose 2025 status holds across the range falls from 97 to 88 (short 50 to 44, long 47 to 44); the nine that change are Desert Channels, Mackay Whitsunday, North Tasmania, Southern Gulf, North East Vic and North West Tasmania (short) and Glenelg Hopkins, Desert Channels and Northern Gulf (long), all from yes to no.

Why North Tasmania and Mackay Whitsunday fail, from the draws: North Tasmania is over capacity in 26.9% of the draws on holdings land and in none on the raster land, and in 36% of draws with the energy multiplier above 1.2; Mackay Whitsunday in 16.2% on holdings land and 42.6% on the raster land. The land-source choice is equal chances (B115's judgement), so these shares depend on it.

## 4. Tipping counts

`node analysis/paper_a/shocks_ranges.mjs analysis/paper_a/shocks_ranges_wide_zones.csv --wide-zones` writes `shocks_ranges_wide_zones.csv` (180 rows: 60 zones, return periods 1, 10, 20, the columns of `shocks_ranges_wide.csv`; each zone's own release-table drought factor on every draw, as B123) and `shocks_ranges_wide_zones_own_table.csv` (B123's alternative). The national and state rows equal `shocks_ranges_wide.csv` in all 24 rows compared. `python3 -I analysis/paper_a/tipping_counts.py` writes `shocks_counts_wide_zones.csv`; called with the 13-choice files it reproduces B112's counts (21, 21, 22; 24, 24, 24; 16 in an average year).

| Return period | Over at central | At p95 capacity | At p5 capacity | Population inside the range | Regions over in one draw (p5, p50, p95) |
|---|---|---|---|---|---|
| Average year | 16 | 15 | 23 | 8 | 17, 18, 21 |
| 1 in 10 | 21 | 19 | 26 | 7 | 21, 23, 24 |
| 1 in 20 | 24 | 22 | 26 | 4 | 24, 24, 25 |

* Inside the range at 1 in 10: Murrumbidgee - ACT, Burnett Mary, Desert Channels, Southern Gulf, SA Arid Lands, North Tasmania, North West Tasmania. At 1 in 20: Murrumbidgee - ACT, Desert Channels, SA Arid Lands, North Tasmania.
* Over at the central figure but not at p95: Burnett Mary, North West Tasmania (1 in 10); Murrumbidgee - ACT, North Tasmania (1 in 20). Over at p5 but not at the central figure: Murrumbidgee - ACT, Desert Channels, Southern Gulf, SA Arid Lands, North Tasmania (1 in 10); Desert Channels, SA Arid Lands (1 in 20).
* Tipping regions (under capacity in an average year, over at 1 in 10): five at the central figure (North East Vic, Burnett Mary, Mackay Whitsunday, Wet Tropics, Rangelands; A199 holds), four at p95 (Corangamite, North East Vic, Mackay Whitsunday, Wet Tropics), three at p5 (Murrumbidgee - ACT, Burnett Mary, SA Arid Lands).
* The p5 and p95 columns put every region at its own end at once, so they bracket more than any one draw shows; the last column evaluates each draw in all regions together. The counts use the release table; the own-table file is not counted. Desert Channels, Southern Gulf and SA Arid Lands are inside their ranges because the raster land source cuts their capacity to a small fraction of the holdings figure; they are the land-definition artefacts already flagged.

## 5. Sentences for Paper A (to say no more than the figures support)

**Section 3 (flips).** "On the full set of 19 settings, none of the eight short-term flips is both free of an artefact flag and robust to the range. Seven do not keep their 2025 status across the 5th to 95th percentile: Wet Tropics, Desert Channels, Mackay Whitsunday, Rangelands, North Tasmania, Southern Gulf and Corangamite. SA Arid Lands keeps its status but is a land-definition case. The two flips that were clean and robust on 13 settings, Mackay Whitsunday and North Tasmania, have 5th-percentile capacities (135,581 and 148,681) below their populations (153,841 and 156,393), and 29.4% and 13.5% of the 2,000 draws put them over capacity. The 2011 status is the base figure and carries no range. The long-term flip of South West Queensland holds in every draw (lowest capacity 15,477 against a population of 7,109)."

**Section 8.1 (regional counts).** "At a 1-in-10 year 21 of the 53 regions are over capacity at the central figure. Taking each region at the 95th and 5th percentile of its own range gives 19 and 26; in a single draw the number is 21 to 24 (5th to 95th percentile, median 23). Seven regions have their population inside their range (Murrumbidgee - ACT, Burnett Mary, Desert Channels, Southern Gulf, SA Arid Lands, North Tasmania and North West Tasmania). At 1 in 20 the counts are 24, 22 and 26, with four regions inside their range (Murrumbidgee - ACT, Desert Channels, SA Arid Lands and North Tasmania)."

**Section 10 (North Tasmania).** "North Tasmania is under capacity at the central figure in 2025 (population 156,393 against capacity 187,593) and at balance in a 1-in-10 year (capacity 156,413). Its range across the 19 settings reaches below its population (5th percentile 148,681), so the settings drawn do not settle its 2025 status: 13.5% of the draws put it over capacity, none of those on the raster land and 26.9% of those on holdings land. It is not reported as a clean flip."

**Conclusion 4.** "The regional flips that held on 13 settings do not hold on 19: none of the eight short-term flips is clean and robust, and the one that is robust in the long term is South West Queensland. The number of regions over capacity at a 1-in-10 year is 21 at the central figure and 19 to 26 across the ranges."

**Response-letter words (R05a issue 4).** "We have run the full 19-choice draws for every region. On them one short-term flip (SA Arid Lands, a land-definition case) keeps its 2025 status across the 5th to 95th percentile, and none is clean and robust; one long-term flip, South West Queensland, is. Sections 3, 8.1 and 10 and the fourth conclusion say so."

Limits to keep in the text: the widened regional ranges rest on the same judged choices as the national one (land source with equal chances, the top of the energy range); the 2011 side has no range; zone 45's shocked capacity is not exactly the average year times the factor (0.39%).

## 6. Checks

* `python3 -I analysis/sensitivity_2025/check_wide_zones.py` (exit 0): 2,000 draws, 19 choices, 120 zone columns; Australian columns equal block A (difference 0); 16 national and state columns equal the state draws (difference 0); 120 rows x 5 statistics recomputed by `statistics.quantiles`; base equals `results/ranges_2025-fixed.csv`; land-source medians quoted in the README.
* `python3 -I analysis/paper_a/check_shocks_ranges_wide_zones.py` (exit 0): 1,440 percentiles and shares of the two shocked files recomputed with the factors of `analysis/resilience_2025/tables.csv`; all counts recomputed from the draws; 12 quoted counts.
* `python3 -I analysis/paper_a/check_regional_flips_wide.py` (exit 0): robust and clean-and-robust labels re-derived from the ranges and `movers-3.csv`; 8 quoted counts; the draw shares and the lowest South West Queensland draw.
* Default reruns equal the earlier files byte for byte: `regional_flips.csv`, `regional_flips-3.csv`, `shocks_ranges.csv`, `shocks_ranges_wide.csv`, `shocks_ranges_wide_own_table.csv`. A second `--wide-zones` run is byte-identical.

## Files changed

Edited: `analysis/sensitivity_2025/monte_carlo.mjs` (zone 45 block only), `analysis/sensitivity_2025/README.md` (section appended), `analysis/paper_a/regional_flips.py` (optional third argument), `analysis/paper_a/shocks_ranges.mjs` (option `--wide-zones`), `analysis/paper_a/README.md` (section appended), `qa/defects.csv` (X140 row only: fixed in B132, awaiting a checker).

New: `analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide_all.csv`, `summarise_wide_zones.py`, `check_wide_zones.py`, `monte_carlo_2025-fixed_wide_all.md`; `results/ranges_2025-fixed_wide_zones.csv`; `analysis/paper_a/regional_flips-3_wide.csv`, `shocks_ranges_wide_zones.csv`, `shocks_ranges_wide_zones_own_table.csv`, `shocks_counts_wide_zones.csv`, `tipping_counts.py`, `check_regional_flips_wide.py`, `check_shocks_ranges_wide_zones.py`; this report.

## Claim rows that move (the register was not edited)

Tier A:

| id | tier | before | after |
|---|---|---|---|
| A036 | A | Two of the eight short-term flips are clean and robust (Mackay Whitsunday, North Tasmania) | None of the eight is clean and robust on 19 choices; 1 (SA Arid Lands, artefact flag) keeps its 2025 status; value 2 becomes 0 |
| A038 | A | Short-term flips not robust: 2 (herd-cycle), 3 (13-choice) | 7 on the 19-choice ranges (Wet Tropics, Desert Channels, Mackay Whitsunday, Rangelands, North Tasmania, Southern Gulf, Corangamite) |
| A184 | A | 21 (21 to 22 across the range; North Tasmania at balance) | 21 (19 to 26 across the ranges; 21 to 24 in a single draw, 5th to 95th percentile) |
| A199 | A | 5 (2025) at the central figure; 3 (2011) | unchanged at the central figure; new companion: 4 at the 95th percentile and 3 at the 5th (names above) |
| A039 | A | South West Queensland clean and robust | stands (long-term range 17,239 to 24,761 against 7,109); no change, restated on 19 choices |

Tier B and C:

| id | tier | before | after |
|---|---|---|---|
| A188 | B | 24; 24 at every point of the range | 24; 22 at p95, 26 at p5; 24 to 25 in a single draw |
| A402 | B | 21; 21; 22; 24; North Tasmania the one inside at 1 in 10; none at 1 in 20 | 21; 19; 26; seven inside at 1 in 10 (names above); 24; 22; 26; four inside at 1 in 20 |
| A419 | B | regional counts stand on the 13-choice ranges (no regional widened draws) | the widened regional draws exist (all 60 zones); the statement is withdrawn or replaced by the counts above |
| A041 | B | One long-term flip is not robust to the 2025 range (SA Arid Lands) | two on 19 choices: Desert Channels and SA Arid Lands |
| A042 | B | short 3 artefacts and 3 not robust; long 2 and 1 | short 3 and 7; long 2 and 2 (19 choices) |
| A043 | B | clean flips 2 (short) and 1 (long) | 0 and 1 (19 choices) |
| A056 | B | values unchanged (capacity 139 to 187 thousand; population 144 to 156 thousand) | values unchanged; add that the 19-choice 5th percentile is 148,681, below the 2025 population |
| A343 | B | North Tasmania is the clean flip (values 1.000; 1.253) | values unchanged; the label "clean flip" no longer holds (not robust on 19 choices); one of seven regions inside its 1-in-10 range |
| A339 | C | flips tested with ranges_2025-fixed.csv | tested with `results/ranges_2025-fixed_wide_zones.csv` (19 choices) |

Not moved: A027, A028, A009 (national), A034, A035, A037, A040, A045 (2011 has no draws; still true), A180, A183, A187, A402's 13-choice companion values (kept as the 13-choice record). New rows the register job may add: the 19-choice flip counts, the zone ranges (North Tasmania, Mackay Whitsunday, South West Queensland), the counts in section 4, and the 74 and 17 zone counts.

**Register rows touched: none.**

## Wrong-value check

`python3 -I analysis/sensitivity_2025/check_wide_zones.py` recomputes the zone ranges from the draws (exit 0 on the true figures).

*Example, a deliberate wrong value (North Tasmania's 13-choice 5th percentile quoted against the widened draws):* `python3 -I analysis/sensitivity_2025/check_wide_zones.py 57:short:p5=174487` fails with exit status 1: `57:short:p5: quoted 174487, the draws give 148681`.

Two more, both exit 1: `python3 -I analysis/paper_a/check_regional_flips_wide.py short clean_and_robust 2` gives `FAIL quoted short clean_and_robust = 2 but the file gives 0`; `python3 -I analysis/paper_a/check_shocks_ranges_wide_zones.py 10 over_at_p5_capacity 22` gives `FAIL quoted 1-in-10 over_at_p5_capacity = 22 but the draws give 26`.
