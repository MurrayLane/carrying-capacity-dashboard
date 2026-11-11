# V28: blind re-derivation of the Paper B section 7 matrix (decision 61)

Checker: independent, blind. Brief: `qa/briefs/V28_section7_matrix_rederivation.md`; rules: `qa/briefs/_checker_rules_results_wave.md`. Decision 33 applies: the reasons below describe what each method counts and what the tests found, not shortcomings of its authors. No repository file other than this report was changed. Working files (my ratings, a transcription of the draft matrix, the comparison script) are in the scratch folder `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v28/`.

## 1. The rule, stated before rating

A method is **well suited** to a purpose when the tests show it sees what the purpose turns on; **partly** when it does so with a stated limit or only beside another method; **not suited** when it cannot see it.

What each purpose turns on, as I applied it:
1. **Food security and drought risk:** whether a diet that has to balance can be supplied from domestic land, and how often it cannot (a bad year).
2. **Why national estimates range from 9 to 100 million:** the definitions that move the number (exports, energy count against diet balance, drought allowance, diet, time frame, land base), and whether a method reproduces or explains a part of the published spread.
3. **Regional and local land-use planning:** a unit of land below the nation, at that land's own productivity, with what it can feed.
4. **Diet change and land use:** the land a diet needs, with the diet as an input that can be changed.

Tie rule for well suited against partly: every method has stated limits; I rate partly only when the stated limit touches the core of what the purpose turns on.

## 2. A deliberate wrong rating, to show the check can fail

Before comparing, I fed my comparison script (`compare.py`) a copy of my ratings with one cell deliberately wrong: HALF for purpose 1 set to "well suited" (the tests say HALF is not predictive and has no weather, B071, so by my rule it is "not suited"). The script reported 24 of 28 and listed `half P1` as a difference with the draft, beside the three real differences. With my true ratings it reports 25 of 28. So a wrong cell does show up as a mismatch.

## 3. My 28 ratings, derived before opening the draft

Sources: `analysis/method_tests_2025/README.md` (MT), `analysis/comparators_2025/README.md` (CMP), `analysis/sensitivity_2025/README.md` (SENS), `papers/B_methods/OUTLINE.md` sections 4 to 6 (OUT), `qa/claims_register.csv` (ids). I did not read the register rows of section 7 until after the comparison.

**Energy and protein balance (Gifford; Henry and Godden)**
* P1 not suited: counts calories and protein of production with exports as food, no diet, no pairing, no weather (B029; MT "What it shows").
* P2 partly: reproduces the 1975 and 1995 figures that sit in the published range (B015) and exposes the hidden land base (31%, B022) and consumption factor (B023); it cannot see drought, diet or time frame, so it explains one family only.
* P3 not suited: national production totals scaled to a national potential area (Nix's 70 Mha, B013); no unit below the nation.
* P4 not suited: has no diet; each nutrient counted alone (B029; MT harmonised "kept").

**Ecological footprint, food row (Simpson)**
* P1 not suited: an accounting of land demand, not of a limit; no weather, no pairing (MT application bullets; B049).
* P2 partly: shows why land-at-world-productivity readings run high (103 to 343, B046) and come down to 64.8 to 84.6 at local productivity (B270); the footprint-ratio estimates of 27 to 39 million sit in the published range (B223).
* P3 partly: the method's own local-productivity adjustment (Wackernagel and Rees 1996 p. 78; B270, B271) lets it set demand against a given area's land, and it has been used at regional scale beside a capacity figure (Gutteridge, South East Queensland, CMP Lane 2014 row); as run it is national, at world-average productivity and without pairing.
* P4 partly: diet is the input (per-person consumption times land per tonne, B049) and the fall of 45% follows beef and sheep consumption (B041); world-average productivity, energy land mixed in, and the plant-crop component not reproduced (B035).

**HALF index (Alexander)**
* P1 not suited: the authors say it is not predictive; no weather, no limit (B071).
* P2 partly: read as a capacity it gives 276 million (B068) and 76.0 at local productivity (B272), which shows why land-per-diet counts read high; it is not itself one of the published Australian estimates.
* P3 not suited: a percentage of world land at world-average production (B071); no regional unit.
* P4 well suited: built for diet land, reproduced for Australia within 0.8% and the world within 2.1%, independent rebuild within 2% (B056, B058); diet change drives its 28% fall (B067). Limit (world-average, not Australian productivity, B069) noted but does not touch comparison of diets.

**People per hectare (Cassidy)**
* P1 not suited: a calorie count, no protein, no balanced diet, no grazing, no weather (MT application; B086).
* P2 partly: its delivered-calorie reading (145 to 190, B083, B084) is the same kind as the energy counts that make up the high end of the spread (B164, B165); cropland only.
* P3 not suited: cropland only, so it cannot stand for pastoral land (OUT method-test table; B086).
* P4 partly: sees the diet lever of feed against food on cropland (B087) but not pasture, which is most of Australia's diet land (B069).

**Commodity balance (Foran and Poldy)**
* P1 partly: names the binding item (meat 40 to 41, fish 12 to 17; B153, B154), which is what security turns on; no weather and no land (B155).
* P2 partly: shows why grain-based counts are three to twelve times higher (grain is not what binds, MT) and gives the 30 to 32 million meat reading in the register (B222); only beside the model.
* P3 not suited: no land, national totals (B155).
* P4 not suited: no view of what could replace the binding item and no land (MT "A balance is a statement..."; B155).

**Failure probability (Fearnside)**
* P1 well suited: capacity against failure probability: 41.5 to 30.8 (1 in 10) to 18.9 (1 in 100), about 6% a year at today's population (B130, B134, B137).
* P2 partly: explains the drought-allowance part of the spread (factor 2.2, B167) and the Jones committee's 30 to 35 (B138); not exports or diet.
* P3 partly: a planner's method for a settlement area in its original form (23,600 ha, B121; B122), here carried only nationally with one weather factor from the national grain record (B139).
* P4 not suited: one criterion, the default diet, held fixed (B139).

**The author's land and diet balance (thesis method, corrected and improved)**
* P1 well suited: diet balance with pasture and crop pairing, drought allowance as a quantity at each return period (B095 to B103), reproduces the Jones figures (B198), Monte Carlo range (B112).
* P2 well suited: the ladder spans the published 9.4 to 100 by definition (B189 to B193; B190: factor 4 without exports).
* P3 well suited: the only method with sub-national units (states 75%, NRM 44%, SA4 58%, SA3 44%, SA2 37% of the national figure; B171 to B177). Stated limit: zone figures are sensitive to the reserve definition and small zones are fragile (SENS "What it shows"); I judged this does not remove the method's sight of the purpose. A judgement call (partly is defensible).
* P4 well suited: diet as input, guideline and optimised diets with their land (B178 to B182, B205 to B215, B216).

## 4. Comparison with the draft (`papers/B_methods/SECTION7_DRAFT.md`, opened after the ratings above were filed)

● well suited, ◐ partly, ○ not suited. Draft abbreviations: EP, FP, HALF, PPH, CB, FAIL, LDB.

| Cell | Draft | Mine | Agree or differ | Why |
|---|---|---|---|---|
| P1 EP | ○ | ○ | agree | |
| P1 FP | ○ | ○ | agree | |
| P1 HALF | ○ | ○ | agree | |
| P1 PPH | ○ | ○ | agree | |
| P1 CB | ◐ | ◐ | agree | |
| P1 FAIL | ● | ● | agree | |
| P1 LDB | ● | ● | agree | |
| P2 EP | ◐ | ◐ | agree | |
| P2 FP | ◐ | ◐ | agree | |
| P2 HALF | ○ | ◐ | **differ** | Draft: not a capacity method, produces no estimate in the disputed range. Mine: read as a capacity (276, 76.0 at local productivity; B068, B272) it shows why land-per-diet readings are high, which is part of explaining the range. |
| P2 PPH | ○ | ◐ | **differ** | Draft: cropland only, not a capacity method. Mine: its delivered-calorie reading (145 to 190) is the calorie-count kind that makes up the high end (B083, B164, B165). |
| P2 CB | ◐ | ◐ | agree | |
| P2 FAIL | ◐ | ◐ | agree | |
| P2 LDB | ● | ● | agree | |
| P3 EP | ○ | ○ | agree | |
| P3 FP | ○ | ◐ | **differ** | Draft: world-average productivity, so it cannot say what a region's own land feeds. Mine: the method's own p. 78 local-productivity adjustment (B270, B271) and its regional use beside a capacity figure (Gutteridge) give a partial, stated-limit use. |
| P3 HALF | ○ | ○ | agree | |
| P3 PPH | ○ | ○ | agree | |
| P3 CB | ○ | ○ | agree | |
| P3 FAIL | ◐ | ◐ | agree | |
| P3 LDB | ● | ● | agree | (my rating is itself a judgement call, see section 3) |
| P4 EP | ○ | ○ | agree | |
| P4 FP | ◐ | ◐ | agree | |
| P4 HALF | ● | ● | agree | |
| P4 PPH | ◐ | ◐ | agree | |
| P4 CB | ○ | ○ | agree | |
| P4 FAIL | ○ | ○ | agree | |
| P4 LDB | ● | ● | agree | |

**Agreement: 25 of 28.** Purposes 1 and 4: 7 of 7 each; purpose 2: 5 of 7; purpose 3: 6 of 7.

## 5. Judgement call or factual difference

* **All three differences are judgement calls**, not factual ones. In each, the draft and I cite the same test facts; we differ on whether a method that is not itself a capacity method, or that needs its own adjustment, counts as "partly" for explaining the range or for regional use. The draft's reasons for those cells are factually correct as stated (HALF's authors say it is not predictive, B071; PPH is cropland only, B086; FP and HALF use world-average productivity).
* Of the two P2 cells, the draft's test ("do they produce estimates in the disputed range") is a defensible reading of the purpose; mine ("do they help explain why readings in the range differ") is broader. Murray's choice.
* **One factual point in the draft's reasons (not a rating):** under purpose 1 the draft says EP, FP, HALF and PPH "read 134 to 343 million". The tests give 103 to 343 for this group (B046, B156; MT cross-method table: footprint build 3 cropland-bound is 103). 134 is the low end of the energy and protein balance alone. Suggested wording: "103 to 343 million".
* Two statements in the draft's reasons rest on sources outside the inputs named in my brief and so are not checked here: Fearnside's statement that KPROG2 needs so much data it is impractical for large areas (P3 FAIL), and "rangeland is stranded unless a unit also holds cropland" (P3 LDB).
* All other figures in the draft's reasons match the register: 41.5, 30.8, 18.9 and about 6% (7% in 2011) (B130, B131, B137); 30.8 for the Jones 1-in-10 (B138); fish 12 to 17, meat 40 to 41 (B153); 15.6 to 62.9, factor 4, 100 with exports, the 9 as the pre-correction long-term figure (B160, B190, B193); 30 to 32 meat count (B222); states 75%, NRM 44%, SA3 44%, SA2 37% (B171, B172, B174, B175); 23,600 ha (B121); 103 to 343 and 276 under P3 (B046, B068); HALF within 0.8% and 2.1%, rebuild within 2%, fell 28%, 2.4 times (B056, B058, B067); 6.2 and 0.27 ha, 103.6, dip at 2.5%, cliff after 5.5%, 118.0 against 112.4 (B216, B228); "two to eight times" (B156).
* The draft's rating legend matches the brief's rule word for word in substance.

## 6. Register rows touched

None. No row of `qa/claims_register.csv` was changed.

## 7. Ids cited

B013, B015, B022, B023, B029, B035, B041, B046, B049, B056, B058, B067, B068, B069, B071, B083, B084, B086, B087, B095 to B103, B112, B121, B122, B130, B131, B134, B137, B138, B139, B153, B154, B155, B156, B160, B164, B165, B167, B171 to B182, B189 to B193, B198, B205 to B216, B222, B223, B228, B270, B271, B272. Decisions 33, 35 and 61.

## 8. Rerun

```
D=/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v28
python3 -I $D/compare.py $D/mine.csv $D/draft.csv        # 25 of 28
python3 -I $D/compare.py $D/mine_wrong.csv $D/draft.csv  # deliberate wrong cell: 24 of 28
```

Files read: the brief; `qa/briefs/_checker_rules_results_wave.md`; `qa/DECISIONS.md` (rows 33 to 36, 61 to 64); `analysis/method_tests_2025/README.md`; `analysis/comparators_2025/README.md` (sections 1 to 3); `analysis/sensitivity_2025/README.md` (opening sections); `papers/B_methods/OUTLINE.md`; `qa/claims_register.csv` (Paper B rows); and, last, `papers/B_methods/SECTION7_DRAFT.md`.
