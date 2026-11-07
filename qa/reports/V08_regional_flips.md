# V08 checker report: regional status flips, 2011-fixed against 2025-fixed

## Tolerance and the failing test
- Tolerance: counts and names must match exactly; capacities within 0.5%; shares and ratios within one unit of the last printed digit.
- Deliberate wrong value: I set Corangamite (zone 16) 2025 short-term capacity to 1,000,000,000 (`INJECT=16,short,capacity,1000000000`). My code then reported 15 regions over in 2025 short term, against 16 in the `over_capacity` column, so it does report a mismatch.
- Spot check of the inputs: I evaluated all 11 flip zones in both presets and both releases with `web/src/model/evaluator.js` (44 evaluations). Every one matched the capacity and population in `results/<release>.csv` exactly (worst difference 0.0000%).
- The 53 regions are the 104 `kind = region` rows plus NT (`kind = state`, zone 60). That is 53 per preset in each release.

## A. Counts: holds
Over capacity means population > capacity, computed by me. It agrees with the `over_capacity` column every time.

| | 2011 | 2025 |
|---|---|---|
| Short term | 23 | 16 |
| Long term | 36 | 32 |

## B. Flips: holds
- **Short term: 9 flips, 8 over to under, 1 under to over.**
  - Over to under: North East Vic, Desert Channels, Mackay Whitsunday, Southern Gulf, Wet Tropics, SA Arid Lands, Rangelands (WA), North Tasmania.
  - Under to over: Corangamite.
- **Long term: 4 flips, all over to under:** Desert Channels, South West Qld, Northern and Yorke, SA Arid Lands.

## C. Tests on each flip: holds (one footnote, and the Rangelands verdict is weakened by part D)
- Artefact: the land-definition flag or the older-boundary flag in movers.csv. I recomputed the land rule from `land_only_ratio` (>2 or <0.5) and it agrees with the flag on all 106 rows.
- Not robust: p5 < 2025 population < p95.

| Term | Region | Direction | Land flag (ratio) | Older boundary | pop / p5 / base / p95 | Status |
|---|---|---|---|---|---|---|
| short | Corangamite | under to over | no (0.86) | no | 496,373 / 482,261 / 492,833 / 536,556 | not robust |
| short | North East Vic | over to under | no (0.97) | no | 114,355 / 120,508 / 129,164 / 133,609 | clean and robust |
| short | Desert Channels | over to under | yes (5.7) | **yes** | 10,875 / 86,660 / 92,671 / 95,757 | artefact |
| short | Mackay Whitsunday | over to under | no (1.02) | no | 153,841 / 176,644 / 199,114 / 214,810 | clean and robust |
| short | Southern Gulf | over to under | yes (2.58) | no | 27,303 / 43,823 / 46,690 / 49,798 | artefact |
| short | Wet Tropics | over to under | no (0.68) | no | 285,138 / 273,648 / 315,100 / 342,114 | not robust |
| short | SA Arid Lands | over to under | yes (6.5) | no | 8,049 / 27,016 / 28,609 / 30,939 | artefact |
| short | Rangelands (WA) | over to under | no (1.52) | no | 157,948 / 122,256 / 167,279 / 161,244 | not robust (base lies above its own p95, see D) |
| short | North Tasmania | over to under | no (1.07) | no | 156,393 / 175,328 / 187,593 / 197,215 | clean and robust |
| long | Desert Channels | over to under | yes (5.7) | **yes** | 10,875 / 23,407 / 26,847 / 28,090 | artefact |
| long | South West Qld | over to under | no (1.82) | no | 7,109 / 20,451 / 23,533 / 25,079 | clean and robust |
| long | Northern and Yorke | over to under | no (1.0) | yes | 92,250 / 89,785 / 94,288 / 103,264 | artefact and not robust |
| long | SA Arid Lands | over to under | yes (6.5) | no | 8,049 / 7,194 / 8,217 / 9,031 | artefact and not robust |

- Every target name and grouping holds.
- Footnote: Desert Channels carries both flags, land definition and older 2011 boundary, in both presets. The brief and the README label it as land definition only. Its verdict does not change.

## D. Range anomaly (X046): there is a fault, not a legitimate one-sided edge
**Count.** I checked base against p5 to p95 for every zone in `results/ranges_2025-fixed.csv`. In every row, base equals the 2025-fixed capacity.
- **Short term: 2 zones**, Western NSW (402,411 against 337,096 to 401,203) and Rangelands (167,279 against 122,256 to 161,244).
- **Long term: 1 zone**, Rangelands (49,387 against its p95 of 46,119, which is below base).
- In the 1,000 draws (`monte_carlo_draws_2025-fixed_all.csv`), the share of draws above base is 3.9% for Western NSW short, 1.2% for Rangelands short and 0.0% for Rangelands long.

**What is ruled out.**
- *Overwritten zone-specific input:* the draws set meategg, redmeat, fuel, biofuel, timber and organic for every zone in the short term (`Object.assign(pre, ...)`). In 2025-fixed, all 60 zones carry the same short-term values (0.12, 0.578, 2360, 0.0023, 0.8, 0.07), and those equal `BASEP`. Nothing zone-specific is overwritten.
- *Wrong base:* base equals the release capacity, and the OAT base row of `oat_2025-fixed_all.csv` gives the same values (402,411, 167,279 and 49,387).
- *Draw set missing the base settings:* the base settings are inside every drawn range, the meat windows are equally likely (333/334/333), and the resilience table is drawn 500/500.

**What the evidence shows: a sign-independent shift in the group-factor shortcut.**
- `monte_carlo.mjs` adds `Math.abs(s) * (variant matrix - base matrix)` for the field-crop (sf) and vegetable/fruit/nut (sh) factors. The lo and hi variant matrices come from the work folder of `build_variants.py`; the base matrix is `data/2025/yield_matrix_livestock.csv` with the release's yield factors.
- A yield factor at -1 and at +1 should move capacity in opposite directions. In `oat_2025-fixed_all.csv` they move capacity the **same way, by nearly the same amount**. I split each factor's effect into its even part (half of the sum of the two effects) and its odd part (half the difference):

| Zone, term | sf: even / odd | sh: even / odd |
|---|---|---|
| Rangelands, short | -8.2% / ±0.2% | -8.4% / ±1.3% |
| Rangelands, long | -9.4% / ±0.6% | -9.8% / ±2.3% |
| Western NSW, short | -1.8% / ±0.0% | -1.8% / ±0.0% |
| Australia, long | about +4.6% | about +4.6% |

- In the draws, Rangelands capacity correlates with |sf| and |sh| at -0.45, and with sf and sh themselves at only -0.04 and +0.13. The response is V-shaped.
- So for most zones the "group factor" choice is mainly a constant offset between the work-folder matrices and the release matrix. That offset is applied in proportion to |s|. For these zones it is negative and large, so almost every draw lands below base.
- This is not a one-sided choice. Raising and lowering a crop yield factor cannot both cut capacity by 8%.
- The offset is widespread: |even part| > 1% in 57 of the 120 zone-presets for sf and 70 of 120 for sh. It is not only the three anomalous cells, so every 2025-fixed range is shifted to some degree, including the national long-term range.
- The meat-window differences come from the same work folder. They may carry the same offset; for Rangelands both alternative windows lower capacity (-10.7% and -7.2%).
- **Cannot determine:** the exact source of the offset. It needs the `build_variants.py` work folder, which is not in the repository; I did not read anything outside it. The likely cause is matrices built on another base, for example 2025-organic before the biodiesel and beef corrections. The README check at line 111 ("reproduced two full re-runs at the corners") would not catch this, because the corner re-runs use the same work matrices.

**Effect on the "not robust" test of part C.**

| Term | Flip | Population vs base | Effect of the offset |
|---|---|---|---|
| short | Rangelands (WA) | 5.6% below | **Affected.** Its range is pulled down by an offset of about -8% for each group factor, and the population sits inside that range near its top. Without the offset the range would sit near base. The genuine two-sided choices (meategg -3.3 to +7.2%, redmeat -2.4 to +3.1%) would likely not reach the population, and the meat-window effect is possibly contaminated. Its "not robust" verdict cannot be relied on. |
| short | Corangamite | 0.7% above | Not material: real diet choices move it ±3%, so it stays not robust. |
| short | Wet Tropics | 9.5% below | Not material: offset -0.3%; meat window 1 gives -9.4% and redmeat -7.1%, so it stays not robust (narrowly). |
| long | Northern and Yorke | 2.2% below | Not material: resilience table -6.6%, so it stays not robust. |
| long | SA Arid Lands | 2.0% below | Not material: resilience table -6.6% and fuel -11.3%, so it stays not robust. |
| short and long | Clean flips (Mackay Whitsunday, North Tasmania, North East Vic, South West Qld) | 11.5% to 70% below | Offsets are under 1.2%, so the verdicts stand. |

## E. Comparison with the files under test
**Code and CSV.**
- I ran a copy of `regional_flips.py` that writes to my scratch folder. Its output is byte-identical to the committed `regional_flips.csv`.
- All counts, flip lists, directions, artefact flags and robustness verdicts in the CSV match mine.
- Differences:
  1. The CSV's `artefact flag` column holds one label, and land definition takes precedence over older boundary. So Desert Channels (both presets) shows only "land definition", although it also carries the older-boundary flag. Swan and Alinytjara Wilurara (not flips) are the same.
  2. The robustness column uses the 2025-fixed ranges as they stand, so the Rangelands short-term "no" inherits the part D fault.
- The docstring's "five older 2011 zones" holds: Alinytjara Wilurara, Desert Channels, Northern and Yorke, SA Murray Darling Basin, Swan.

**README, section "Section 3 and 9", sentence by sentence.**
- "53 regions (52 NRM regions and the Northern Territory)": holds.
- Table: short 23 / 16 / 9 (8 over to under, 1 under to over) / 3 / 3 / 3; long 36 / 32 / 4 (all over to under) / 3 / 2 / 1. Holds.
- "Clean and robust: Mackay Whitsunday, North Tasmania, North East Victoria (all over to under)": holds.
- "Land-definition artefacts: Desert Channels, Southern Gulf, SA Arid Lands": holds. Desert Channels is also an older-boundary artefact.
- "Not robust: Wet Tropics, Rangelands (WA), Corangamite (the one region that moves from under to over)": holds on the ranges as published. Rangelands is weakened by X046.
- Long-term "Clean and robust: South West Queensland": holds.
- "Artefacts: Desert Channels and SA Arid Lands (land definition), Northern and Yorke (older 2011 boundary)": holds, with the same Desert Channels footnote.
- "SA Arid Lands and Northern and Yorke are also not robust": holds.
- "headline of the plan (eight over to under, one under to over) is three genuine flips in the short term and one in the long term": holds.
- "net fall (23 to 16 short term, 36 to 32 long term) is more than the clean flips alone explain": holds (net falls of 7 and 4, against 3 and 1 clean flips).
- **"Capital cities and the coast stay over capacity in both years": does not hold as stated.**
  - Murrumbidgee - ACT (Canberra) is *under* capacity in the short term in both years (capacity 1,185,593 and 1,533,929 against population 529,508 and 738,895).
  - Several coastal regions flip: Wet Tropics, Mackay Whitsunday, North Tasmania, Corangamite.
  - Others are under capacity in both years in the short term: South Coast WA, Eyre Peninsula, Glenelg Hopkins.
  - The other capital-city regions are over in both years and both presets: Hawkesbury - Nepean - Sydney, Port Phillip and Westernport, South East Qld, Adelaide - Mount Lofty Ranges, Swan, South Tasmania, NT.
- "The land-definition flag is the rule of movers.csv (>2 or <0.5)": holds (0 mismatches over 106 rows).
- Limits sentences (2011 has no range; the test is on capacity): consistent with the method; no numbers to check.

## Other findings
- The part D offset affects every 2025-fixed Monte Carlo range, not only the three cells flagged by X046. It does so in proportion to each zone's even part (about 1 to 10%). Any use of `results/ranges_2025-fixed.csv` (Paper A ranges, the national 90% range in `monte_carlo_2025-fixed_all.md`) inherits it. The same script built the mirror and improved ranges, and they likely carry it too; I did not check them.
- Non-flip rows marked not robust in the CSV (Fitzroy, South West WA, SA Murray Darling Basin, Mallee and Kangaroo Island, long term) were not examined.

## Commands to rerun (from /home/user/carrying-capacity-dashboard)
```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v08
python3 -I $S/check.py .                                          # parts A to D (counts, flips, tests, base outside range)
INJECT=16,short,capacity,1000000000 python3 -I $S/check.py .      # deliberate wrong value
node $S/spot.mjs > $S/spot_out.txt                                # evaluator spot check of the 11 flip zones
python3 -I $S/their_copy.py && cmp $S/their_rerun.csv analysis/paper_a/regional_flips.csv
```
The OAT even/odd split, the draw correlations and the README capital checks were inline `python3 -I -` snippets over `analysis/sensitivity_2025/oat_2025-fixed_all.csv`, `monte_carlo_draws_2025-fixed_all.csv` and movers.csv. Their logic is described above.

## Files read
- qa/briefs/_checker_rules_results_wave.md, qa/briefs/V08_regional_flips.md, and the X046 line of qa/defects.csv (found by grep)
- results/2011-fixed.csv, results/2025-fixed.csv, results/ranges_2025-fixed.csv, analysis/comparison_2025/movers.csv
- web/public/data/2011-fixed and 2025-fixed regions.json and model.json (through the evaluator)
- analysis/sensitivity_2025/evaluate.mjs, monte_carlo.mjs, monte_carlo_2025-fixed_all.md (head), monte_carlo_draws_2025-fixed_all.csv, oat_2025-fixed_all.csv, build_variants.py (head), and README.md (grep, line 111)
- Part E: analysis/paper_a/regional_flips.py, regional_flips.csv, README.md lines 5 to 24
