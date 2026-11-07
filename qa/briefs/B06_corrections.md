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
Report format (your final message): (1) each edit applied, with file and the new wording; (2) any edit you could not apply as written and why (then leave the passage unchanged); (3) the regenerated outputs and whether they match (byte for byte, or the diff); (4) anything else that looks wrong that you did not touch.

## Task B06: apply the corrections found by the claims-register builder

Every change below is a correction of a stale figure, an imprecise or wrong sentence, or a file format. No frozen release, no script logic and no result value changes. Use the exact replacement wording given; where a line is quoted, find it by its wording, not by line number. Repository root: /home/user/carrying-capacity-dashboard.

### Edit 1: `analysis/comparators_2025/README.md`
a. In the Jones committee bullet of section 2, replace "(22 to 25 million at 50 years, 19 to 21 at 100)" with "(22.9 million on the corrected method and 29.9 on the improved at 50 years; 18.9 and 24.7 at 100)".
b. In the CSIRO 1975 bullet of section 2, replace "(`analysis/nutrition_lp_2025`: 268 and 458 million)" with "(`analysis/nutrition_lp_2025`: 254 and 410 million on the current improved release; the earlier 268 and 458 predate the dairy module)".
c. In the export-inclusive bullet of section 2, after "(27 million x 70/30 = 63 million abroad; 90 million, \"around 100\")" add " (the report's own arithmetic; 100 minus 27 would be 73 abroad)".
d. In section 3b (the harmonised table in the README, the rows that quote improved-method values): replace "45.7 improved" with "53.6 improved", "30.8 and 34.0" with "30.8 and 39.9", "49.7 improved" with "58.3 improved", "Australia 7.4 ha (default diet)" with "Australia 6.2 ha (default diet)", and "(41 to 49 and 31 to 34)" with "(41 to 54 and 31 to 40 across the corrected and improved methods)". If any of these strings is absent, say so; do not search for near matches.

### Edit 2: `analysis/comparators_2025/harmonisation.csv`
Update the same stale improved-method values in this file to the ones in Edit 1d (45.7 to 53.6; 34.0 to 39.9; 49.7 to 58.3; 7.4 to 6.2 in the Peters row; "10-year drought 31 to 34" to "10-year drought 30.8 corrected, 39.9 improved"). Keep every other cell as it is. Report each cell changed.

### Edit 3: `analysis/comparators_2025/energy_exports.py` and the csv it writes
In the row label "CSIRO and UQ 2025 (reported): in all 100, of whom Australians 27, so abroad" and its value 73, change the label to "CSIRO and UQ 2025 (reported): 63 abroad as the report states (100 in all less 27 at home would be 73)" and the value to 63. Re-run the script only if its input file (the FAO food balance csv it names in its usage line) is on this machine under /tmp/claude-0/fao/; if it is not, edit the csv by hand to match and say so.

### Edit 4: `analysis/comparators_2025/rerun.mjs` and `rerun.csv`
Quote the variant field in the output so the comma inside "R1 drought allowance (return period, years)" is inside double quotes (change the row-building code to wrap the variant in double quotes). Regenerate `rerun.csv` with `node analysis/comparators_2025/rerun.mjs analysis/comparators_2025/rerun.csv` from the repository root; confirm that every numeric value is identical to the previous file (compare after stripping quotes). Then confirm that `python3 -I analysis/method_tests_2025/fearnside_failure_curve.py`, `python3 -I analysis/method_tests_2025/cross_method.py` and `python3 -I analysis/method_tests_2025/design_choices.py` (run from the repository root) regenerate their csv outputs byte-identically; report any difference and do not try to fix it.

### Edit 5: `analysis/method_tests_2025/README.md`
a. Simpson fidelity table: "within 1.2%" to "1.2% lower"; "within 3%" to "3.6% higher".
b. Simpson energy-land bullet: "a fifth to a third of the food row" to "16% of Simpson's food row and 22% of the crop-and-pasture part rebuilt here".
c. Foran and Poldy fidelity bullet: "(within 1.2%)" to "(grain 1.2% higher, meat 1.2% lower)".
d. HALF fidelity table: the World row's "-2%" to "-2.1%"; and in the sentence "The recipe is therefore reproduced closely for the world, the United States, India and Argentina" leave the wording but add after "Argentina" the words "(within 2.1%, 0.5%, 0.3% and 3.9%)".
e. Cross-method section, "What the comparison shows": in the Three groups bullet replace "read 12 to 41 million, the model's range" with "read 12 to 41 million; the meat count and Fearnside's average-year point sit at the model's own figure, the fish count and the 1-in-100 point below it". Replace the bullet beginning "**The improved tier raises every reading**" so that it begins "**The improved tier raises the model's own readings**" (rest of the sentence unchanged).
f. Design-choices section: replace "the corrected model on its own data spans 18.9 (worst of 100 years) to 55.3 (no avoidable waste) by definition alone" (if present in this file) with "the corrected model on its own data spans 15.6 (long-term settings) or 18.9 (worst of 100 years) to 55.3 (no avoidable waste) by definition alone; 62.9 with the improved settings". Replace the bullet beginning "**The published spread (9 to 100 million, a factor of 10.6) decomposes along the ladder**" with: "**The published spread (9 to 100 million, a factor of 10.6) can be read along the ladder**: 1.7 from the thesis's own long-term figure to its corrected value (9.4 to 15.6: the 9 is the author's biodiesel error), 4.0 from definitions inside the model (long term 15.6 to improved and no-waste 62.9) and 1.6 from counting exports (62.9 to 100). The three factors multiply to 10.6 by construction (100 over 9.4), so this is a reading of where the spread sits, not a decomposition; the order of the steps is a choice and the ladder mixes the corrected and improved tiers." Replace "**Without counting exports one model spans a factor of 4**: from 15.6 (long term) or 18.9 (worst of 100 years) to 62.9." with "**Without counting exports one model spans a factor of 4 from its long-term settings (15.6 to 62.9), or 3.3 from its worst-of-100-years point (18.9)**."

### Edit 6: `analysis/method_tests_2025/cross_method.py`
In the Simpson row's fidelity text replace "pasture and feed crop within 3%" with "pasture 1.2% lower, feed crop 3.6% higher"; in the Foran and Poldy row replace "production within 1.2%" with "production within 1.3%"; in the HALF row replace "world, US, India within 2%" with "world within 2.1%, US and India within 0.5%"; in the Cassidy row replace "calorie shares within a few points" with "world, India, China and Brazil calorie shares within a few points; the US feed share lower (ethanol since 2000)". Then regenerate `cross_method.csv` with `python3 -I analysis/method_tests_2025/cross_method.py` from the repository root and confirm that only those text cells changed.

### Edit 7: `papers/B_methods/OUTLINE.md`
a. In the Headline block replace "One model on one data set spans about 19 million (worst of 100 years) to 55 million (no avoidable waste) by definition alone" with "One model on one data set spans about 16 million (its long-term settings) or 19 million (worst of 100 years) to 55 million (no avoidable waste) by definition alone, 63 million with the improved settings".
b. Replace the heading "## Method tests scoped (nothing built yet)" with "## Method tests (all seven run on 2026-11-06; see `analysis/method_tests_2025/README.md`)".
c. In the Simpson row of that table replace "ABS 4306.0 1991-92 issue online (not yet read)" with "ABS 4306.0 1991-92 (`Comparators/`, read from the scan)". If the string differs, report the row's wording and leave it.
d. In section 6, the unit-of-self-sufficiency bullet: replace "Shown here with three points from the model (national, states, regions)" with "Shown here with the model's levels (national, states, regions, and the SA4, SA3 and SA2 sums as the design-choice table lists them)".
e. In the contribution block (the sentence listing method families new to the earlier work), if Fearnside is named there as new, leave it; in section 2 or section 4, if Fearnside is listed among the methods the thesis chapter 6 already reviewed, add after it "(reviewed there as a planning method; applied here as a test for the first time)". Report what you found.

### Edit 8: `papers/B_methods/SECTION7_DRAFT.md`
a. Replace the heading "## Minimum reporting checklist (each item is a design choice that moved the answer by more than 1.2 times)" with "## Minimum reporting checklist (items 2 to 8 are the design choices measured in section 6; items 1 and 9 to 12 are what a reader needs to use the number)".
b. Replace "the three planning-oriented studies of the earlier work (Peters, Fairlie, Noosa and Douglas, Gutteridge's South East Queensland)" with "the planning-oriented studies of the earlier work (Peters, Fairlie, Noosa and Douglas Shire, Gutteridge's South East Queensland)".
c. In the HALF bullet of purpose 4 replace "(world, United States and India within 2%)" with "(world within 2.1%, United States and India within 0.5%)".
