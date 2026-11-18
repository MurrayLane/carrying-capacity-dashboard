# B126a: Paper A patched to the blind read V45a

Brief: `qa/briefs/B126a_patch_paper_A.md`. Input: `qa/reports/V45a_read_paper_A.md`. No subagents, no network. I ran one `git status` by slip before I saw the rule against git commands; it is read-only and changed nothing. Written: the section files, claims csvs, `supplementary.md` and a new declarations file under `papers/A_results/draft/`, `OUTLINE.md`, `SECTION_SCOPE.md`, and this report. Not touched: `paper_A_draft1.md` (it is now behind the section files until the coordinator reassembles), `references.md`, every register, everything under `analysis/`. No em dash in anything I wrote.

## Counts

* `python3 qa/tools/assemble_draft.py A` on a scratch copy (`.../scratchpad/asm/`): assembled with four section files; declarations land after the data and code statement and before the notes appendix; 0 em dashes in the assembled file.
* `python3 qa/tools/wordcount.py A` (run on the real files and on the scratch copy, same result): TOTAL 7,937 (limit 7,950). By section: 1: 642; 2: 727; 3: 596; 4: 729; 5: 662; 6: 422; 7: 566; 8: 924; 9: 828; 10: 471; 11: 788; 12: 582.
* Abstract: 244 words (150 to 250). V45a counted 246 before the patch; the abstract edits net out at -2.
* The declarations (about 250 words) are in a new section file `A_s13_declarations.md` with unnumbered headings, so the tool's rule leaves them out of the main-text count, as it does the abstract and the notes. Whether Population and Environment counts them is Murray's to check.

## Note for the record: V44

`qa/reports/V44_check_B123.md` exists and passes every B123 item. The widened shocked ranges in 8.1 and Table S9 stand (23.1 to 36.5 and 19.7 to 31.2 million; 37% and 78% of draws; 0.45%), and the "checker pending V44" labels in the claims csvs now read "V44 pass". Register rows A014, A183 and A187 are being moved to the widened figures by B125's job; I changed no figure for them except 0.72 below.

## Every V45a fail, in the read's order

### Number trace

| V45a fail | Fix or stand |
|---|---|
| 0.72 (8.1 sentence 7; Table S9 row 2) | Fixed to 0.71 in both places and in the two stale drafter notes and `SECTION_SCOPE.md`. The claims rows say 0.71 is computed from the two printed figures, 19,735,337 / 27,608,200 = 0.7148, and not read from the csv's rounded 0.715 (V44 prints 0.715 too). |
| Highlight numbers, no row | New `highlights_claims.csv`: five rows, one per highlight (A001 and A003; A357, A358, A362 and B111 for the overlap; A196, B123 and V44; A011; A088 and A015). Highlight text unchanged. |
| 153 (8.1) | New row in `A_s05-08_claims.csv`: source B112 section 3, V38 "Drought factors" (n = 153). |
| 1.3, 1.0, 1.0 million; 141 thousand; 65% to 86%; 12 points; Table 5 change column; 153,025 | These stand as derived values: each is arithmetic on printed csv cells that V45a recomputed and found correct. The claims rows already carried the arithmetic; I set their flag column to "derived" with the sum shown (Table 5: without / 15,623,209 - 1; 12 points: 0.349 - 0.233 = 11.6, printed 35% less 23%). No prose changed. |

### Checker-wording fails (6)

1. No checker for B123: V44 now exists and passes (above). Labels updated.
2. "The diet" (V37). Abstract and conclusions now say "the consumption and red-meat-mix layers".
   * Abstract before: "consumption and the red meat mix, a diet with less beef, add 5.6 million". After: "the consumption and red-meat-mix layers add 5.6 million".
   * Conclusions before: "the consumption and red-meat-mix layers, the diet with less beef, added 5.6 million". After: "the consumption and red-meat-mix layers added 5.6 million".
   * Section 4 keeps its gloss and its caveat (the consumption layer also carries fuel, biofuel and timber).
3. "23 zones" (V36). Before: "differed from these by more than 10% in 23 zones". After: "differed from them by more than 10% of the ABS figure in 23 of the 52 zones other than North East Victoria, and in 24 with it (section 3)". I rechecked the 23 against `analysis/population_2011/zone_population_2011_comparison.csv` (23 rows above 10% on the -2 populations, where North East Victoria is already corrected; its thesis 204,651 against ABS 98,604 is the 24th).
4. Grain-fed animals (V38). 8.1 before: "Applied to crops alone". After: "Applied to crops and grain-fed animals alone". Table S10's caption already says this.
5. Each draw's own resilience table (V38). Supplementary Table S9 text, new sentence: "Each draw takes the release's weather factor; with each draw's own resilience table the ranges are 22.5 to 35.9 and 19.1 to 30.5 million (`analysis/paper_a/shocks_ranges_wide_own_table.csv`)." Values from V44 item 1.
6. Energy range (V41). 9.1 before: "a moderately active population at the top of the energy range". After: "an activity level of 1.8 at the top of the energy range, a chosen part of the source's range of 1.2 to 2.2". S4 adds "the release's own diet has not been checked against a level of 1.4". No number moves.

### Tier A rows

* A038: the condition is in the one sentence that carries it, section 3. Before: "Three are not robust to the 2025 range". After: "Three are not robust to the 2025 zone ranges (two, on the herd-cycle ranges)". 9.1 repeats the claim with "on the 13-choice draws".
* A223: stands as printed. Draft and `analysis/paper_a/scenarios_by_region.csv` line 27 (row `2025-fixed,2025-fixed,climate-crops-24,short`, column `change on reference`) print -0.2%. Listed for the register job.
* A014, A183, A187, A196: B125's job; see the V44 note above.

### Logic

1. Forward and reverse "bound" (Table 2 note, section 4): rewritten. I recomputed all nine-layer rows of zone 1 in `capacity_by_cause_corrected_orders.csv`: the average lies between the two walks in every row except three long-term rows, crop yields (257,755 against 219,940 and 253,434), liquid fuel (124,764 against 90,858 and 114,983) and land with livestock (-619,428 against -608,748 and -591,253).
   * Section 4 before: "the forward and reverse walks bound it". After: "the forward and reverse walks are the two ends of the chain, and the average can lie outside both where the order matters, as it does in the long term for crop yields, liquid fuel and land with livestock (Table 2)".
   * Table 2 caption before: "...and the reverse walk as bounds". After: "...and the reverse walk, the two ends of the chain. The average can lie outside both: long-term crop yields, long-term liquid fuel and long-term land with livestock." The caption also says `2011-fixed-3` gives the same capacities (consistency 8).
   * Section 4 sentence "bound livestock at 4.7 and 6.4 million..." now reads "give livestock 4.7 and 6.4 million and the red meat mix 1.8 and 1.1 million".
   * `OUTLINE.md` and `SECTION_SCOPE.md` said "as bounds"; changed to match.
2. "Every single year" (9.1): **dropped**, not restated. The file behind it, `analysis/reliability_2025/years.csv`, is on the 2025-organic release, has no 2021-22, and is unverified (A317, X118: `build_years.py` fails at 2016-17), so it is not a checked output. 9.1 now says "The short-term rise holds at the base settings, but it is a comparison of two years at fixed settings, not a test across the settings." The single-year figures stay in Supplementary S4, already labelled unverified; the claims row for the dropped clause is removed and a new row records the drop.
3. 9.2 "lowest in both years": restated per `analysis/paper_a/method_status-3.csv` (checked B123, V44 item 4). After: "The corrected tier has the fewest long-term regions over capacity in both years. On the ABS populations of 2011 the counts are 37, 35 and 36 under the published, corrected and improved methods (21, 22 and 20 in the short term), and the published method on its own thesis populations gives 22 short term and 39 long term. On the corrected tier the long-term count falls by 3 between 2011 and 2025, on the published tier by 1 (37 to 36), and on the improved tier it does not fall (36 in both years)." The Table S4 note says the same, and the drafter note that the published tier was not rerun is corrected.
4. Abstract cause clause. Before: "because in the model cropland can carry pasture-fed food but pasture cannot carry crops". After: "a loss the model's substitution rule accounts for: cropland can carry pasture-fed food but pasture cannot carry crops" (V45a's wording).
5. 8.4 Anderson sentence. After: "Bad wheat years share climate drivers: ENSO and the Indian Ocean Dipole together explain 30 to 41% of wheat variability in Australia and East Africa (Anderson et al. 2019), so a widespread drought can hit several states at once." 11.6 matched ("share climate drivers", section 8.4).
6. 7.2. After: "Organic farming, the natural-fibre and wool-fibre shares, the activity level and the biofuel share lower it." (Table 5: +4% and +3% without them.)
7. Table S8 caption: added "Differences of 1 to 2 points between the two orders are estimator noise."
8. Abstract against body: no fail.

### Consistency

1. S4 40.5 million against 33.3 million. 40.5 million is `results/2011-corrected.csv` (40,450,144): the published method, thesis inputs. 33.3 million is `results/2011-fixed-3.csv` (33,307,814): the corrected method. The 2025-organic release has no method modules (`results/releases.json`), so the single-year comparison is published against published. S4 now says: "the 2011 value on the same published method, 40.5 million (release 2011-corrected; the corrected method, 2011-fixed-3, gives 33.3 million)".
2. SA Arid Lands. 5.2 now says "41 thousand people on the state-yield basis (28,609 on its own yields, Table 7)"; S2 labels 41 thousand and 132 thousand as state-yield with 28,609 and 384,476 on own yields; S5 says "on its own yields" before 28,609.
3. Two ratios: fixed by the section 2 sentence (reader's test 1) and 8.1 now reads "the population exceeded capacity, so people over capacity was 1.12 in 2011 and 1.05 in 2025".
4. Table 6 now prints 1.50 (41,503,537 / 27,608,200 = 1.5033; the csv prints 1.5).
5. Figure 2 placeholder now names `analysis/paper_a/movers-3.csv`, which exists.
6. Supplementary tables out of order of first citation: stands. Every table cited exists and is the one meant (V45a), and renumbering touches all four claims csvs and the prose for no gain a journal asks for.
7. Store gain 48.45% (8.3, Table S2), 48% (11.4), 48.4% (Table S5): stands. Each is the figure its own file prints (`scenarios_by_region.csv` 48.45%; `measures.csv` 48.4%); I did not change a printed file value. If Murray wants one form, the fix is in `measures.csv`'s formatting.
8. Table 2 release: caption now says `2011-fixed-3` gives the same capacities.
9. Citations against `references.md`:
   * "USDA undated" became "USDA 1992" in section 2 and S4 (L062 is Agricultural Handbook 697, June 1992; B119).
   * "CSIRO and University of Queensland 2025" became "CSIRO 2025" (entry L010).
   * "Roos et al. 2017" became "Röös et al. 2017".
   * "DCCEEW 2017, 2019, n.d." is for the register job: the three entries are filed under the full department name while ABARES, ABS and CSIRO are filed under their abbreviations. Making the entries' author "DCCEEW" fixes it without touching the prose.
   * Higgins et al. 2018a (L172) is uncited: drop it from the list. Then "Higgins et al. 2018b, p. 341" in S6 becomes "Higgins et al. 2018" (I left the prose as is so it matches the entry until the job runs).
10. "as reported in": removed from section 11 prose. It now reads "(Gifford et al. 1975)"; the reference entry already says "cited in Henry and Godden, 1995" and the claims row carries "second-hand, read in L003 p. 98".
11. Reference form (decision 98 against the journal): for Murray, not mine to decide.
12. No fail.

### Journal checks

* Em dash: the only one is in `references.md` (Hendrie et al. 2014 title); `qa/references.csv` L097 is the source. Register job: replace the dash with a colon (this file I may not write).
* Time word: S4 "The recent droughts" became "The droughts of 2002-03, 2006-07 and 2019-20", tied to the seasons ending 2003, 2007 and 2020.
* Draft furniture ("First draft ... Not for circulation", the notes appendix): assembly's job; the coordinator strips it.

### Reader's test (three sentences)

All three added, and the words cut elsewhere to pay for them (below).
1. Section 2: "Two ratios appear: capacity over population, the margin (above 1 the region can feed itself), and its inverse, people over capacity, the status (above 1 the region is over capacity)." It replaces the old status sentence.
2. Section 2, at the first use of release names: "A release is a frozen set of inputs: "fixed" is the corrected method, "improved" the improved method, "mirror" the published method on 2025 data, "-3" the 2011 inputs with the ABS regional populations, and "organic" and "store" name variants." (V45a's key, shortened and checked against `results/releases.json`.)
3. Section 9.1: the 19 choices named once and Supplementary S4 pointed to. V45a's suggested list did not match the file, so I took the names from `analysis/sensitivity_2025/sobol_2025-fixed.csv`: "The 13 are crop yield factors, the herd and meat window, the meat-and-egg and red-meat shares, fuel, the organic factors, the resilience table and the long-term feeding benchmark; the six added are avoidable waste, the loss factors, the land source, the meat calibration, the energy requirement and the crop-trend window." In S8 "Paper B" is gone: "Reading the capacities at 10 and 20 years ... linearly in the logarithm of the return period gives 16.4 years and 6.1%; ... linearly in the return period gives 17.1 years and 5.8%, the figure used here."

## B119 labels

"Not seen" is off every Paper A row B119 section 9 lists: `A_s01-04_claims.csv` (the L013/L014, L062/L063 and footnote rows), `A_s05-08_claims.csv` (4 rows), `A_s09-12_claims.csv` (3 rows, plus the L002/L003 row now reads "second-hand, read in L003 p. 98"), `supplementary_claims.csv` (3 rows). The line numbers in B119 had drifted by one or two after B124, so I matched by content. Kept: the Kastner row (L080). Pages added from B119 section 3 (L062 printed p. 17, L063 p. 1, L013 p. 14 manuscript, L073 and L074 abstract p. 1, L115 p. 990, L117 and L116 abstract p. 1, L014 pp. 1 to 3).

## The declaration

New `A_s13_declarations.md` (after the conclusions and the data and code statement): the short generative-AI text verbatim from `papers/DECLARATIONS.md` (it keeps the phrase "After using these tools", which is the journal-form wording), competing interests (the Paper A variant), funding, CRediT. Placeholders in brackets: model names and versions; the thesis wording; no grant, employer support or funder payment; the author name. A claims csv for the file records the sources.

**For Murray:** Springer's placement and headings for these statements may differ from the Elsevier form used here; check them against https://link.springer.com/journal/11111/submission-guidelines before submission.

## Words cut to stay at or under 7,950

The patch added about 245 words of prose (two ratios, release key, 19 choices, 23 of 52, the 9.2 restatement, the bound sentence, 5.2 basis, 7.2, 8.4, A038, energy). Cut to pay for it: the 26.2 to 58.1 range in 9.1 (still in Table S7); the Basin 40% sentence in 10 and the Prosser streamflow sentence in 12.3 (both cited still in Supplementary S5); Avon's 1-in-100 sentence in 10 (in Table 7 and S5); North Tasmania's two long-term capacities (Table 7 keeps 58,798); the 11.5 Mt store sentence (in S6); the 93% farmer sentence in 11.7 (Lawrence still cited in 11.7 and S9); the food-group swaps sentence in 12.2 (S7); the interaction detail in 9.2; the halving clause in 8.3 (11.3 has it); the shares sentence in 5.1 (Table 3); "These counts are read with the flip classification" in 8.2; the post-farm-gate sentence in 12.4; compression of the North East Victoria sentences, 8.1's Table S9 pointer and 9.1's judgement list. No cited work became uncited.

## Register rows for the register job

* **0.71**: A187 and A195 (and the 1-in-20 `capacity over population` low end wherever printed): 0.715 in `shocks_ranges_wide.csv` is rounded twice; computed from the two printed figures, 19,735,337 / 27,608,200 = 0.7148, it prints 0.71. Claims rows A183, A187 and A195 widened range text: "0.72 to 1.13" becomes "0.71 to 1.13".
* **A223**: register gate 5 note says "new value -0.3". The draft and the data file print -0.2: `analysis/paper_a/scenarios_by_region.csv`, line 27, row `2025-fixed,2025-fixed,climate-crops-24,short`, column `change on reference` (-0.2%). Correct the note (A205 shares the same cell).
* **Citations**: DCCEEW entries (L230, the 2019 baseline row, L242) filed under the abbreviation; drop L172 (Higgins 2018a) and relabel L173 as 2018 (then S6 prose "2018b" becomes "2018"); USDA, CSIRO and Röös are already fixed in the prose. L062 is "undated" in `SECTION_SCOPE.md` year-band tables (lines 158 and 572); it is 1992.
* **Hendrie 2014 title**: `qa/references.csv` row L097 holds an em dash between "Diet" and "Comparing"; replace with a colon. Regenerate `references.md` after.
* **A317 and X118** stay unverified; the "every single year" sentence no longer rests on them in the main text.
* **Reference form**: decision 98 (Elsevier Harvard form) against Population and Environment's Springer author-date form, and the 17 "[CHECK ...]" markers: for Murray.

## Wrong-value check

My check script (`.../scratchpad/check_b126a.py`) recomputes the capacity-over-population range at 1 in 10 and 1 in 20 from `analysis/paper_a/shocks_ranges_wide.csv`, finds which zone-1 rows of the decomposition fall outside their two walks, and reads the 2011 tier counts from `method_status-3.csv`.

On the patched text it prints `1 in 20 ratio range recomputed 0.71 to 1.13 in text: True`, the three long-term rows (crop yields, liquid fuel, land and livestock) match the three named in the text, the 2011 counts read 21, 22, 20 and 37, 35, 36 with 22 and 39 for the published method on its own population, and `FAILS 0`.

**Example (deliberate, not in the files):** I put the read's 0.72 back into a scratch copy of section 8 only. The same script then prints `1 in 20 ratio range recomputed 0.71 to 1.13 in text: False` and `FAILS 1`, so the check can fail and the 0.72 is the value it catches. The real files carry 0.71.

## Changed files

Under `/home/user/carrying-capacity-dashboard/papers/A_results/`:
* `draft/A_s01-04.md`, `draft/A_s05-08.md`, `draft/A_s09-12.md`, `draft/supplementary.md`
* `draft/A_s13_declarations.md` (new), `draft/A_s13_declarations_claims.csv` (new), `draft/highlights_claims.csv` (new)
* `draft/A_s01-04_claims.csv`, `draft/A_s05-08_claims.csv`, `draft/A_s09-12_claims.csv`, `draft/supplementary_claims.csv`
* `OUTLINE.md`, `SECTION_SCOPE.md`

And this report: `/home/user/carrying-capacity-dashboard/qa/reports/B126a_patch_paper_A.md`. Not changed: `highlights.md`, `references.md`, `paper_A_draft1.md`.
