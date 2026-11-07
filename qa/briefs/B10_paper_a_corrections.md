# Builder brief

You are a builder helper. The coordinator (the main session) wrote this brief and will review your work, so do not try to decide what anything means.

Rules, no exceptions:
* Change only the files named under "Edit", and only the passages listed. Read anything else, change nothing else. Do not run git; the coordinator commits.
* Do not change any result, script or data file. Do not spawn subagents.
* Never invent. If you cannot establish a field, write `unknown` and list it in your report. Copy citations and titles exactly as you find them and record where you found them.
* Every row must rest on something you opened (a file, a page). A path in a row means the file exists: check it.
* Plain, specific notes. No time words (tonight, later, for now, not urgent).
* Repository root: /home/user/carrying-capacity-dashboard (public). The private archive is /home/user/carrying-capacity-models; refer to its files as `carrying-capacity-models/<path>`. Both exist on this machine.

Standing decisions you must not reopen: two papers only; the methods paper tests each method on Australian 2025 data and gives no reproduction gate; corrected values are assumed; the results paper gives 2011 as corrected only. Read `qa/CARD.md` and `qa/README.md` (the schemas) first.
Report format (your final message): (1) each edit applied, with file and new wording; (2) any edit you could not apply as written and why (leave the passage unchanged); (3) anything else that looks wrong that you did not touch.

## Task B10: corrections to the results-paper documents found by the claims-register builder

Each is a correction of wording or a figure against the output file that holds the true value. Verify each replacement value against the named csv before writing it; if the csv disagrees with the value given here, write the csv's value and say so. No frozen release, script or result value changes. Find passages by their wording.

### `analysis/paper_a/README.md`
1. Measures table, row "Waste at the national target (6%)": replace "n/a (the long term already assumes none)" with "14.3 (-8.2%; the long-term settings assume no avoidable waste, so a 6% target is a step back)" (check `measures.csv`).
2. Replace the bullet "**Nothing but diet and waste moves the short term by more than 10%.**" with "**Nothing but diet, waste and livestock productivity moves the short term by more than 10%** (livestock output +20% gives +19%)."
3. In the bullet beginning "**The two corrections act in different places.**": replace "lowers the short term by 16% nationally and 10% to 22% in the beef and cropping regions" with "lowers the short term by 16% nationally, by 10% to 22% in 17 beef and cropping regions and by 3% to 9% in eight more"; replace "the Murray-Darling basin regions -14% to -15%" with "the Murray-Darling basin regions -14% to -16%" (check `method_effects_by_region.csv`); replace "almost nothing in the south-west and the wheat belt" with "almost nothing there in the short term (in the long term Avon +19% and South Coast WA +16%)".
4. Replace "**Australian loss factors raise nearly every region 9% to 23% in the short term**" with "**Australian loss factors raise every region in the short term, by 1% to 23% (median 9%)**".
5. In the Limits line of section 9(b): replace "(the interaction is small, see `results/method_effects.csv`)" with "(the interaction is not small nationally: in 2025 the modules together give +4.25 million short term where the sum of their effects alone would give 7.1, an interaction of -2.9; the long-term correction effect applied in sequence is +10% on the published figure, not the +21% of the biodiesel module alone; see `results/method_effects.csv`)". Check the figures against that csv's zone 1 rows (`effect_total`, `interaction`, `capacity_published`, `capacity_corrected`) and write what it gives.
6. Section 7 "What each long-term setting is worth" table: add three rows from `long_term_levers.csv` (2025-fixed, zone 1): fibre, fibreNat and fibreWool, each with its "without" value and percentage as the other rows are written. Read the csv for the values.

### `papers/A_results/DISCUSSION_MEASURES.md`
7. In the cropland +25% row: replace "there is unused pasture (1.8 million km2 excess nationally)" with "the model holds pasture in excess at the national level (1.96 million km2 unused, `analysis/scale_curve_2025/README.md`)".
8. In the export-diversion bullet: replace "4.65 million tonnes of meat" with "4.66 million tonnes of meat" (check `analysis/method_tests_2025/foran_poldy_balance.csv`).
9. In the fuel bullet (item 7 of part D): replace "(the biofuel share alone cuts the figure to 9.7)" with "(switching the biofuel share to 1 with today's other settings cuts the short-term figure to 9.7; `analysis/paper_a/long_term_levers.csv`)".
10. In part A's table, the waste row: replace "already assumed" in the long-term column for the national-target line with "-8.2% (14.3)" if that row distinguishes target from none; otherwise report the row's wording and leave it.

### `analysis/scale_curve_2025/README.md`
11. Replace "2,140 to 2,270 of 2,450 SA2s" with "2,143 to 2,277 of 2,450 SA2s" (check `results/scale_curve.csv`, `units_over_capacity` for the SA2 rows).
12. Garden percentages: find the sentence giving 27%, 68% and 136% for garden cover of 73, 183 and 365 m2 against 246 m2; recompute (73/246, 183/246, 365/246) and write 30%, 74% and 148%, unless the sentence defines the base differently, in which case report it and leave it.

### `analysis/comparison_2025/movers.md`
13. Replace "(x7.9)" with "(x7.7)", "(x4.5)" with "(x4.3)", "(x2.5)" with "(x2.4)" and "the median region is 0.91" with "the median region is 0.90" (check `movers.csv`, `land_only_ratio`).
14. Swan: replace "193,162" with "170,101" if that figure appears as Swan's 2011 capacity (check `movers.csv` cap2011 for Swan); replace "9 to 356 times" with "10 to 349 times" (check ratio2011 and ratio2025).
15. Replace "**Hawkesbury-Nepean-Sydney 66 to 46 stays a usable case**: the land layer alone gives 0.49" with "**Hawkesbury-Nepean-Sydney 66 to 46 is usable with its flag stated**: the land layer alone gives 0.49, just inside the land-definition flag (below 0.5)".
