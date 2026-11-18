# B133: the change between years tested (decision 135)

Builder report. Brief: `qa/briefs/B133_paired_draws_and_2011_on_2025_table.md`. Releases: `2011-fixed-3` and `2025-fixed`. No register row, paper file, frozen release or existing output was edited; `monte_carlo.mjs` is untouched.

## 1. The three answers

* **Paired draws (short term).** In **none of 2,000 paired draws (0.0%)** is 2025 capacity below 2011's. The difference runs from 2.3 to 16.5 million (5th to 95th percentile, median 8.4), the ratio 1.08 to 1.53 (median 1.28). On holdings land only (1,000 draws): no fall, 1.9 to 9.6 million. On the settings the years share alone: no fall, 6.5 to 8.4 million. The unpaired comparison (2025 draws against the 2011 value at its base settings) gives 13.2% below, which is R05a's 13%; R05a's rough paired reading of 0.2% falling becomes 0.0% on the full computation.
* **Paired draws (long term).** The long-term change is **not established**: 26.1% of the paired draws show a fall (difference -0.9 to +3.4 million, median +1.1); on holdings land only 52.2% do (-1.0 to +0.8, median -0.05). On the shared choices alone none fall (+0.24 to +0.29 million), so the long-term difference is carried by 2025-only choices and the land source.
* **2011 on the 2025 weather table.** National people over capacity (population over capacity) at 1 in 20: **1.119 on the thesis table, 1.057 on the 2025 table, against 1.049 in 2025**; capacity over population 0.894, 0.946 and 0.953. At 1 in 10: 0.904, 0.903 and 0.896 (the tables agree there). So the 1-in-20 improvement since 2011 is the table: 1.119 to 1.049 across tables, 1.057 to 1.049 on one table. R05a's rough reading (1.06 against 1.05) is confirmed. By region the table changes no region's status at any return period; the regional tipping counts (3 to 5 at 1 in 10, 4 to 8 at 1 in 20) are the same on either 2011 table and are data changes.
* **Failure probability as a range.** Yearly probability that capacity falls below the 2025 population, 5th to 95th percentile over the 2,000 widened draws: **2.3% to 19.4% (median 7.6%) linear in the return period; 2.4% to 19.5% (median 8.0%) logarithmic**. Base values reproduce (5.84% at 17.1 years linear, 6.10% at 16.4 years logarithmic). Nine draws (0.45%) fail in an average year (probability set to 1); none needs a factor beyond the 150-year anchor. R05a's rough reading, 2.3% to 19%, is confirmed.

## 2. What was done

**1. Paired draws.** The 2,000 rows are block A of `monte_carlo_draws_2025-fixed_wide.csv` (B115). The 2025 capacity is the file's. The 2011 capacity is evaluated with the shared choices from the same row (common random numbers). I did not copy or edit `monte_carlo.mjs`: the new script builds its own evaluator from the releases (it needs no yield matrices, because 2011's yields are the release's and the 2025 yield-matrix choices are all 2025-only).

Shared (7 of the 19) and the reason:

| Choice | How it is paired |
|---|---|
| energy requirement | the same multiplier on each year's food amount |
| avoidable waste | the same rate (2011's 12% is also the 2025 base) |
| loss factors | the same weight between the US and Australian factors (both releases hold the same US factors, checked) |
| organic yield factor | the same value in the same 119 default cells (checked equal in both releases) |
| meat and egg share | relative move: 0.13 times draw over 0.12 |
| red meat share | relative move: 0.64 times draw over 0.578 |
| resilience table (long term only) | each cell of the 2011 thesis table moved by the ratio that the leave-one-out table makes to the 2025 release table |

2025-only (12 of the 19) and the reason: field-crop and vegetable, fruit and nut group factors (the error of the rule carrying 2016-21 yields to 2022-25; 2011's yields are the thesis's own); meat window and meat calibration (2011 is the archive years and calibration); trend window (a 2025 device); land source (no 2011 raster is held); fuel, biofuel and timber (2011 is the thesis value, the end of the 2025 range); organic share of land (2011's 2% is the thesis's measured share); long-term fuel (2011 keeps 253); feeding benchmark (constant in both releases).

Three bases are in `results/paired_change_2011-2025.csv`: `all_draws`, `holdings_land_only` (the like-for-like land source R05a recommended) and `shared_choices_only` (2025 with the 7 shared choices drawn and everything 2025-only at the release; the 2025 capacity is in the draws file as `cap2025_shared_only_*`).

Results, millions of people (difference = 2025 minus 2011; p5, p50, p95):

| Preset | Basis | n | draws with a fall | difference | ratio | unpaired share (2025 below 2011 base) | shifted pairing |
|---|---|---|---|---|---|---|---|
| short | all draws | 2,000 | 0 (0.0%) | 2.32, 8.43, 16.48 | 1.08, 1.28, 1.53 | 13.2% | 6.1% |
| short | holdings land only | 1,000 | 0 (0.0%) | 1.87, 6.02, 9.64 | 1.06, 1.20, 1.31 | 25.2% | 11.1% |
| short | shared choices only | 2,000 | 0 (0.0%) | 6.55, 7.43, 8.45 | 1.24, 1.25, 1.25 | 7.5% | 3.6% |
| long | all draws | 2,000 | 522 (26.1%) | -0.87, 1.08, 3.40 | 0.94, 1.08, 1.23 | 41.9% | 28.7% |
| long | holdings land only | 1,000 | 522 (52.2%) | -0.98, -0.05, 0.80 | 0.93, 1.00, 1.06 | 77.7% | 53.4% |
| long | shared choices only | 2,000 | 0 (0.0%) | 0.24, 0.26, 0.29 | 1.02, 1.02, 1.02 | 63.2% | 38.8% |

The 2011 distribution on the shared choices is 26.3, 30.3, 34.8 million short term (base 33.3, at the upper end because every shared choice but the diet shares can only lower it).

Checks: at the release settings the script's evaluations equal the releases (2011: 33,307,814 and 15,350,146; 2025: 41,503,537 and 15,623,209); its 2025 evaluation with all seven shared choices moved equals `monte_carlo.mjs ... fixed` on 2025-fixed in both presets (34,582,059 and 14,124,158, run on a copy of the work folder of an earlier job, read only); every row's 19 choices and 2025 capacities equal the widened draws file; the first 40 rows were re-made and are byte-identical.

**2. 2011 on the 2025 table.** `analysis/paper_a/shocks_2011_on_2025_table.mjs` gives `2011-fixed-3` the resilience sheet of `2025-fixed` (override in the script; layout checked equal, 1,350 numeric cells; no release made). Its thesis-table rows reproduce all 648 published rows of `shocks_by_region-3.csv` exactly. National figures:

| Basis | 1 in 10: people over capacity (capacity over population) | 1 in 20 | regions over capacity of 53 at 1 in 10 / 1 in 20 | tipping from under capacity in an average year |
|---|---|---|---|---|
| 2011, thesis table | 0.904 (1.106) | 1.119 (0.894) | 25 / 26 | 3 / 4 |
| 2011, 2025 table | 0.903 (1.107) | 1.057 (0.946) | 25 / 26 | 3 / 4 |
| 2025, 2025 table | 0.896 (1.116) | 1.049 (0.953) | 21 / 24 | 5 / 8 |

Tipping regions at 1 in 10: Burnett Mary, Corangamite, North East Vic (2011, either table); Burnett Mary, Mackay Whitsunday, North East Vic, Rangelands, Wet Tropics (2025). At 1 in 20: Burnett Mary, Corangamite, Murrumbidgee - ACT, North East Vic (2011, either table); those less Corangamite plus Mackay Whitsunday, North Tasmania, Rangelands, Southern Gulf, Wet Tropics (2025, eight). At 1 in 5, 50 and 100 the national figures are in the CSV; at 1 in 100 the factors are identical (0.456).

**3. Failure probability range.** `failure_probability_range.py` inverts the Australia row of the release table for each draw (linear in the return period between tabulated factors; logarithmic between the anchors 1, 3, 5, 10, 20, 30, 50, 150). Return periods at the ends of the linear range: about 1 in 43 and 1 in 5.

## 3. Sentences the paper patch needs (no paper file edited)

* **Abstract, the change sentence.** "The short-term capacity of Australia rose from 33.3 to 41.5 million at fixed settings. Across the settings that 2011 and 2025 share (energy requirement, waste, loss factors, organic factor, diet shares), 2025 capacity was above 2011's in all 2,000 paired draws, by 2.3 to 16.5 million (5th to 95th percentile) when the 2025-only data choices are drawn as well, and by 6.5 to 8.4 million when they are not. The long-term change (15.35 to 15.6 million) is not established: 26% of paired draws show a fall."
* **Section 9.1 (replace "2011 was not sampled ... not a test across the settings" in part).** "2011 was not sampled on the 2025-only choices. On the seven choices both years share, drawn with common random numbers, 2025 short-term capacity is above 2011's in every one of 2,000 draws (difference 2.3 to 16.5 million, 5th to 95th percentile; 1.9 to 9.6 on holdings land only, the same land source in both years). The 13% of 2025 draws that fall below 2011's base value is an unpaired comparison and overstates the doubt. The long-term change is within the paired range: 26% of the draws fall (52% on holdings land only)." This amends decision 115's sentence; a decision row is needed.
* **Section 8.1, margin at 1 in 20 (after "people over capacity was 1.12 in 2011 and 1.05 in 2025").** "On one weather table the two years are the same: with the 2025 table (0.634 at 20 years) in place of the thesis table (0.599), 2011's people over capacity at 1 in 20 is 1.06, against 1.05 in 2025. The improvement from 1.12 to 1.05 is the table, not the data; the change between the years in a 1-in-10 year is 0.90 to 0.90 on either table." Table 6's 2011 rows at 1 in 20 go to the 2025 table (`shocks_2011_on_2025_table_summary.csv`), the thesis rows to the supplement. The regional sentence ("three regions to five", four to eight at 1 in 20) stays and can add "on either table".
* **Section 8.1 and S8, failure probability (where the 5.8% sits).** "At the 2025 population the failure probability is 2.3% to 19% a year across the widened draws (5th to 95th percentile, median 7.6%; 2.4% to 19.5% read in the logarithm of the return period); 5.8%, 1 in 17, is the value at the base settings." The abstract and Conclusions drop the single figure "about 5.8% a year, 1 in 17" for this range (R05a issue 7).
* **Conclusions.** "The change since 2011 is positive in every paired draw in the short term and not established in the long term; the narrower 1-in-20 margin in 2011 against 2025 is a change of weather table, not of data."

## 4. Claim rows that move (register not edited)

Tier A:
* A196; A; "0.89 in 2011, 0.95 in 2025" (thesis table for 2011); 0.95 (0.946) in 2011 on the 2025 table, 0.95 (0.953) in 2025; the thesis-table 0.89 stays as the as-published basis. Source rows: `shocks_2011_on_2025_table_summary.csv`, basis and return period 20.
* A009; A; wording only: "lies inside the widened 2025 uncertainty range" is true of the levels and stays; the paired result is added (short term: no fall in 2,000 paired draws; long term: 26.1% fall).
* A418; A; 5.84 and 6.10 stay as the base-settings values; the conclusion's single "5.8%" is replaced by new rows: linear 2.3 to 19.4 (median 7.6), logarithmic 2.4 to 19.5 (median 8.0) per cent a year.
* A223; A; does not move: 2025's -26% at 1 in 10 is unchanged and 2011 on the 2025 table is -25.8% too. (Listed in the brief; checked, no figure of it changes.)
* A027; A; does not move (the 2025 level range 31.1 to 49.2 is not touched); its "rise holds" reading is carried by the A009 and 9.1 wording above.

Tier B and C:
* A013; B; "the long-term gap widened because the population grew, not because capacity fell (15.4 to 15.6 inside the range)"; add that 26.1% of paired draws show a capacity fall.
* B363; B; "the corrected 2011 national figures lie inside the widened ranges": true as levels; the paired change is the stronger statement.
* A072; B; 8.2 million rise unchanged; the paired 5th to 95th percentile (2.3 to 16.5) is new context.
* New rows needed (not edited here): paired share and differences (six rows of `results/paired_change_2011-2025.csv`), the 2011-on-2025-table national and regional figures (`shocks_2011_on_2025_table_summary.csv`), the failure-probability range (`failure_probability_range.csv`).

**Register rows touched: none.**

## 5. Files changed

New:
* `analysis/sensitivity_2025/monte_carlo_paired.mjs`
* `analysis/sensitivity_2025/monte_carlo_draws_paired_2011-2025.csv` (2,000 rows)
* `results/paired_change_2011-2025.csv` (6 rows)
* `analysis/paper_a/shocks_2011_on_2025_table.mjs`
* `analysis/paper_a/shocks_2011_on_2025_table.csv` (648 rows: 3 bases, Australia and 53 regions, 6 return periods)
* `analysis/paper_a/shocks_2011_on_2025_table_summary.csv`
* `analysis/paper_a/failure_probability_range.py`
* `analysis/paper_a/failure_probability_range.csv`
* `analysis/paper_a/check_b133.py`
* this report

Edited by appending (earlier text byte for byte unchanged, checked with `cmp`): `analysis/paper_a/README.md` (one new section at the end, as brief step 4 asks; the brief's write list says "new files" for that folder, so I appended there only and did not touch `analysis/sensitivity_2025/README.md`, which another job may be editing). The draws file is documented in that section.

Not touched: `monte_carlo.mjs`, `analysis/sensitivity_2025/_mc_part_tmp.mjs` (present in the folder, not mine), papers, claims register, any release or `results/` file other than the one added.

## 6. Limits

* National only. A regional paired run would need the 2025-only machinery per zone (issue 4's run).
* The paired 2025 side reuses the widened draws' capacities; the draws file rounds each choice to five decimals, and the 2011 side uses those rounded values (not tested for its size; five decimals on shares of 0.1 to 1 is a relative change under 0.001%).
* The ratio method for the 2011 resilience table (the 2025 leave-one-out ratios applied to the thesis table) is a judgement; the leave-one-out table of 2011's own record is not held. It affects the long term only.
* The organic share of land is treated as 2025-only (the 2011 value is a measured share). Pairing it as a relative move was not run.
* The failure range uses the release table for every draw (the short-term draws are made at resilience 1, so no draw defines its own table); using the leave-one-out table instead was not run.

## 7. Wrong-value check

`python3 -I analysis/paper_a/check_b133.py [KEY=VALUE ...]` recomputes from the draws and tables and checks quoted figures.
* True figures pass (exit 0): `short:all_draws:fall=0.0 short:all_draws:unpaired=13.2 fail:linear:p5=2.3 fail:linear:p95=19.4 shock:2011_on_2025_table:20:poc=1.06 shock:2011_thesis_table:20:poc=1.12 shock:2025_2025_table:20:poc=1.05`.
* **Example of a deliberate wrong value** (R05a's rough 0.2%, the 13-choice 3.9%, and the thesis-table 1.12 quoted for the 2025 table); it exits 1:

```
$ python3 -I analysis/paper_a/check_b133.py short:all_draws:fall=0.2 fail:linear:p5=3.9 shock:2011_on_2025_table:20:poc=1.12
short:all_draws:fall: quoted 0.2, the draws give 0.0
fail:linear:p5: quoted 3.9, the files give 2.3
shock:2011_on_2025_table:20:poc: quoted 1.12, the files give 1.06
```
