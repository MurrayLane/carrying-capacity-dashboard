# V11 report: the effect of each method choice region by region (section 9b)

**Tolerance, set before comparing:** counts and names must match exactly. Capacities must be within 0.5%. Shares are in percent and must be within one unit of the last printed digit, so 0.1 for "-16.0" and 1 for "-22%".

**Checks that the code can fail:**
- Part A: I set Wet Tropics' short-term beef effect to -30% of its published capacity. The script then reported a regional min of -30.0 against the stated -21.5.
- Part B: I set Base!K175 to 0.5 instead of 0.705. The nation's effect then came out at -31.4% against -16.0.
- Part C: I flipped Swan's long-term status under the corrected method. The long-term counts then came out as 36, 31, 36 against 36, 32, 36.

**How the regions were counted:** "53 regions" means the rows of `kind = region`, plus NT. In the results CSVs NT is `kind = state`, zone 60. Alinytjara Wilurara has a published 2025 capacity of 0 in both presets, so its share is undefined. I left it out of the shares, which leaves 52 zones. The stated min and max only reproduce when it is left out. Counting it as 0 would make the long-term biodiesel min 0 (stated +3.4), the short-term loss-factor min 0 (stated +0.8) and the long-term recycling max 0 (stated -1.5).

## A. Summary from the file: holds

Values below are the 2025 nation figure, then the regional min to max.

| Module | Short term | Long term |
|---|---|---|
| Beef carcase yield | -16.0 (-21.5 to 0.0) | 0.0 (-7.7 to 0.0) |
| Biodiesel yield | +0.1 (0.0 to +6.9) | +20.7 (+3.4 to +97.9) |
| Loss factors | +11.2 (+0.8 to +22.6) | 0 |
| Dairy on good land | +20.2 (-27.3 to +22.1) | +3.0 (-12.4 to +53.1) |
| Beef output by state | 0.0 (-7.4 to +9.9) | 0.0 (-5.0 to +3.9) |
| Reserve pro rata | -1.1 (-5.4 to 0) | -5.8 (-29.1 to 0) |
| Recycling by stage | +0.1 (0 to +4.3) | -9.7 (-18.2 to -1.5) |
| Organic ruminant factor | 0 | 0 (0 to +7.6) |

All 16 targets hold exactly.

**Beef carcase correction, "17 regions by 10% to 22% and eight more by 3% to 9%": holds only if the shares are truncated, not rounded.** 25 regions fall.
- 17 fall by 10.4% or more: Wet Tropics -21.5, Lower Murray Darling -16.4, Border Rvs Maranoa-Balonne -15.4, Murrumbidgee - ACT -15.0, Murray -15.0, Lachlan -14.8, Condamine -14.4, Central West NSW -14.3, Namoi -14.1, Border Rivers - Gwydir -14.1, Northern and Yorke -11.2, Northern Agricultural -11.1, Eyre Peninsula -11.1, Mallee -11.0, SA Murray Darling Basin -10.9, Wimmera -10.8 and Avon -10.4.
- The eight more are North Central Vic -9.94, South Coast WA -9.78, South West WA -9.65, Corangamite -9.31, Goulburn Broken -9.14, Adelaide - Mount Lofty Ranges -8.82, Mackay Whitsunday -7.63 and Western NSW -3.33.
- Rounded to whole percent, the first three of those eight become -10%, which gives 20 and 5. That is still inside the one-unit tolerance, but the wording is fragile.

**Named values, all holding:**
- Beef carcase: Wet Tropics -21.5 (-22%) and Lower Murray Darling -16.4 (-16%).
- Biodiesel, long term: South East Qld +97.9, Burdekin +95.8 and South Tasmania +83.5. The region is named "South East Qld" in the data.
- Dairy: SA Arid Lands -27.3 and Southern Gulf -15.5 in the short term, and Rangelands +53.1 in the long term.
- Loss factors: median +9.3, Swan +22.6, Southern Gulf +17.8 and Mackay Whitsunday +14.7.
- Reserve pro rata, long term: Condamine -29.1 and Lower Murray Darling -27.8.

## B. Second route for two modules: holds

I applied each module from its `method.json` to `web/public/data/2025-mirror/` with my own code and evaluated short term with `Evaluator`.
- **beef-carcase-yield:** Base!K175 set to 0.705; the published value is 1.
- **dairy-good-land:** Settings!C34 set to the formula, D34 set to 0, and Yield row 97 of each zone set to `milk_g_per_m2` from `data/2025/dairy_farm_yield_by_zone.csv`.

My published baseline equals `capacity_published` exactly for all six zones. Effects are in people.

| Zone | Beef: mine | Beef: CSV | Dairy: mine | Dairy: CSV |
|---|---|---|---|---|
| Australia | -7,925,319 (-16.05%) | -7,925,319 | +9,959,140 (+20.16%) | +9,959,140 |
| Wet Tropics | -86,211 (-21.54%) | -86,212 | +88,590 (+22.13%) | +88,589 |
| Lower Murray Darling | -21,869 (-16.36%) | -21,869 | +29,374 (+21.98%) | +29,374 |
| SA Arid Lands | 0 | 0 | -7,737 (-27.25%) | -7,738 |
| Southern Gulf | 0 | 0 | -7,153 (-15.55%) | -7,152 |
| Rangelands (WA, zone 52) | 0 | 0 | +36,574 (+22.00%) | +36,574 |

Every difference is 1 person or less. Both modules can be applied by hand from their definitions; nothing is missing. One practical trap: the yield file has CRLF line endings, so a naive parser reads the header column as `milk_g_per_m2\r` and gets no values.

## C. Status under each tier: holds

From the `over_capacity` flag in `results/2025-{mirror,fixed,improved}.csv`, over 53 zones:
- **Short term:** 15, 16, 15. Only Corangamite differs (over capacity under the corrected method only).
- **Long term:** 36, 32, 36. Six regions differ between tiers:
  - Kangaroo Island, SA Arid Lands, South East SA and South West WA: over, not over, over.
  - Mallee: over, over, not over.
  - SA Murray Darling Basin: not over, not over, over.

Those six are four SA regions, one Victorian and one WA region, so "six southern and western regions" holds. The flag agrees with capacity < population in every row.

## D. Files under test

I regenerated the three CSVs by running a copy of `method_effects_by_region.py` in my scratch folder against the repository's `results/`. All three are byte-identical to the committed files.

`method_status.csv` uses capacity < population from `results/method_effects.csv`, not the release CSVs. It gives the same counts and the same six names as Part C. Its published-to-corrected long-term change count of 4 also matches.

**README generated tables:** every number matches Parts A and C. The 2011 rows were not asked for and I did not check them independently.

**README prose:**
1. **"10% to 22% in 17 ... 3% to 9% in eight more": holds within tolerance.** It depends on truncation, as described in Part A.
2. **"the Murray-Darling basin regions -14% to -16%": holds for the nine named NSW/QLD basin regions** (-14.1 to -16.4). Other basin regions fall less: Mallee -11, SA Murray Darling Basin -10.9, North Central Vic -9.9, Goulburn Broken -9.1 and Western NSW -3.3. The phrase reads as if it covered the whole basin.
3. **"nothing elsewhere": holds.** 27 zones show exactly 0.
4. **Biodiesel long-term claims: hold.**
   - "+21% nationally" (20.7), "+98%, +96%, +84%" and "Avon +19%, South Coast WA +16%" (19.2 and 16.3) hold.
   - "Almost nothing there in the short term" holds (max +6.9).
   - "+50% to +98% in the coastal and northern regions" holds for 24 regions. Several of them are southern rather than northern (Tasmania, Corangamite, Glenelg Hopkins, South East SA), so the description is loose but not wrong.
5. **Dairy numbers hold; the stated reason does not.** +20% nationally, -27% to +22%, SA Arid Lands -27%, Southern Gulf -16%, Wet Tropics, Rangelands and Lower Murray Darling +22%, and Rangelands +53% long term all match.
   - The README says these regions "had been credited with dairy at the pasture average". That is contradicted for SA Arid Lands and Southern Gulf: their published milk yield (Yield row 97) is 0.
   - Splitting the module in two shows where their fall comes from. The yield change alone gives +0.3% and +0.5%. Moving dairy's land to the cropping column alone gives -97% and -77%.
   - Their fall therefore comes from charging dairy to cropland they barely have, not from losing a pasture-average credit. The NT (-14%) behaves similarly and is not mentioned.
6. **Beef output by state: holds.** 0.0 nationally, -7% to +10%, Lower Murray Darling +9.9, Murrumbidgee +8.9, and Northern Agricultural -7.4, Wet Tropics -7.0 and Avon -6.9.
7. **Loss factors "raise every region ... 1% to 23% (median 9%)": holds for the 52 zones with a defined share.** Alinytjara Wilurara is unchanged at 0.
8. **"Reserve pro rata and recycling by stage act in the long term only": does not hold strictly.**
   - In the short term, reserve pro rata lowers 42 regions (nation -1.1%, down to -5.4% in North West Tasmania).
   - Recycling raises 51 regions (up to +4.3% in NT).
   - Both are small, but neither is zero. "Mainly in the long term" would be accurate.
   - The numbers in that bullet hold: -29% Condamine, -28% Lower Murray Darling, and recycling -18% in Southern Gulf and SA Arid Lands.
9. **"the long-term improvements pull in the opposite direction to the short-term ones": loose.** Dairy is an improvement and is +3.0% in the long term. Organic ruminant raises 16 regions.
10. **Status bullet: (15, 16, 15) and (36, 32, 36) and "six regions in the south and west" hold. "The six are the regions that sit closest to their population" does not hold.**
    - On the corrected long-term capacity, Northern and Yorke (2.2% from its population) and Fitzroy (8.4%) are closer than Mallee (9.4%), yet neither changes status.
    - South East SA, one of the six, is 34% above its population under the corrected method.
    - Mostly close would be fair; "the closest" is not.
11. **Limits paragraph: holds.**
    - The 2025 short-term nation figures are +4,254,317 together against 7,133,291 as the sum of the effects alone, an interaction of -2,878,974 (+4.25, 7.1 and -2.9 million).
    - The long-term corrections in sequence give +10.4% (stated +10%), against +20.7% for biodiesel alone.
    - "Clipped at 40%, darkest blue" is consistent with the code (RdBu, vmax 40).
12. **Heat map: holds, with one caveat.**
    - The figure shows 53 rows, two panels and the eight modules in the stated order, and labels cells with |v| ≥ 10. Rows are ordered by the improved effect in the short term.
    - Caveat: Alinytjara Wilurara is described as "a blank row in the figure". The script actually draws it as 0.0 (`... else 0.0`) and sorts it as 0, so it looks the same as "no change" (near-white) rather than missing data.
    - The figure is also titled "Figure 7" in the README and docstring; I did not check the paper's numbering.

## Anything found outside the brief
- In the 2011 summary rows, Alinytjara Wilurara (published capacity above 0 in 2011) is the extreme in several modules: reserve -28% in the short term, beef carcase -10% in the long term, organic +9% in the long term. The 2025 rows have no such extremes because it is excluded there. This is worth a note if the 2011 columns are quoted.
- `data/2025/dairy_farm_yield_by_zone.csv` has CRLF line endings (see Part B).
- The 53-zone filter in the script uses `zone == '60'` for NT. That is correct for these data but hard-coded.

## Commands to rerun (from /home/user/carrying-capacity-dashboard)
```
S=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v11
python3 $S/partA.py            # summary; add any argument for the injected-error run
python3 $S/partA2.py           # named regions, beef counts
node $S/partB.mjs              # second route; 'node $S/partB.mjs inject' for the injected-error run
python3 $S/partC.py            # status; add any argument for the injected-error run
python3 $S/partD.py            # prose checks: interaction, biodiesel list, closeness to population
mkdir -p $S/run/analysis/paper_a && ln -sfn $PWD/results $S/run/results && (cd $S/run && python3 -I $S/scripts_copy.py) && cmp $S/run/analysis/paper_a/method_status.csv analysis/paper_a/method_status.csv
```

## Files read
- qa/briefs/_checker_rules_results_wave.md, qa/briefs/V11_method_effects_by_region.md
- results/method_effects.csv, results/2025-mirror.csv, results/2025-fixed.csv, results/2025-improved.csv
- methods/README.md, methods/beef-carcase-yield/method.json, methods/dairy-good-land/method.json
- releases/2025-mirror/release.json (head)
- web/src/model/evaluator.js (head), analysis/sensitivity_2025/evaluate.mjs
- web/public/data/2025-mirror/model.json and regions.json (by code)
- data/2025/dairy_farm_yield_by_zone.csv
- Part D: analysis/paper_a/method_effects_by_region.py, plot_method_effects.py, method_effects_summary.csv, method_status.csv, method_effects_by_region.csv (Alinytjara rows), method_effects_heatmap.png, method_effects_heatmap.svg (grep), and README.md section 9(b)
