# B131: register follow-ups after B130 (checked V46), B129 and B128

Builder report. Brief: `qa/briefs/B131_register_after_B130.md`. No subagents, no network, no paper file edited. Register and defects files keep CRLF line endings; every untouched row is identical (compared cell by cell against a copy taken first). No em dashes in anything written.

## 1. Rows changed (id; before; after)

Tier A (value and statement unchanged in each):

| id | before | after |
|---|---|---|
| B159 | status "independently verified; approved gate 5 (2026-11-18)" (the row's own text kept) | status "independently verified; new value pending approval (B130, V46)"; notes end "; pending approval (2026-11-18): improved range 37.9 to 60.0 short term, 15.7 to 22.1 long term, per B130, checked V46 (decision 125 adopted the rerun; the value change awaits Murray's line)". Value stays "41.5 (31.1 to 49.2); 53.6 (46.2 to 60.1)". |
| B114 | status "independently verified" | same new status and same notes clause. Value stays "46.2 to 60.1". |
| A205 | statement "... on the improved reference." | "... on the corrected reference." Value -0.2% unchanged; edit noted in notes. |
| A206 | statement "... -0.65% on the improved reference and 34 regions ..." | "... on the corrected reference and 34 regions ...". Value unchanged; edit noted. |
| A219 | output_file `analysis/paper_a/scenarios_by_region.csv`; locator "scenario=grain-store-1, term=short, column change on reference = 0%; results/scenarios.csv change_pct" | output_file `results/scenarios_2025-fixed.csv`; locator "scenario=grain-store-1, zone=1, preset=short: change_pct 0 (release label '2025-fixed (resilience table of 2025-store-1)')". Old text kept in notes. |
| A264 | output_file `results/scenarios.csv`; locator "...change_pct 48.27 and 64.21" | output_file `results/scenarios_2025-fixed.csv`; locator "scenario=grain-store-1 and grain-store-2, zone=1, preset=long: change_pct 48.45 and 64.47 (release labels ...)". Old text kept in notes. Both figures read from lines 843 and 963 of that file. |
| A220, A265, A266 | notes only | notes add "traced to the file by V45a; no recompute check" |
| A205, A206, A219, A264 | (also) | the same clause added |

Tier B:

| id | before | after |
|---|---|---|
| B115 | value "15.9 to 19.4"; statement "...15.9 to 19.4 million"; output `results/ranges_2025-improved.csv` (zone=1, long); status "independently verified" | value "15.7 to 22.1"; statement "...15.7 to 22.1 million"; script adds `sobol_wide.py; check_wide.py`; output `results/ranges_2025-improved_wide.csv`, locator "variant=wide, zone=1, setting=long, columns p5 and p95"; status "independently verified (B130, V46, 2026-11-18)"; verifier report adds `V46_check_B130.md`; notes give before and after |
| B157 | "...and the improved range contains none of his points; the improved long term (18.5, 15.9 to 19.4) is near his 1-in-100 point (18.9) ..." | B129's text: "...and the improved widened range (37.9 to 60.0) contains the 41.5 average-year point and the meat readings of 40 to 41, and excludes the 1-in-10 point (30.8); the long-term 18.9 lies inside 15.7 to 22.1; the improved long term (18.5) is near his 1-in-100 point (18.9) ..."; same status as B115; value stays "30.8; 18.9" |

## 2. Rows added (Tier B; status "independently verified (B130, V46, 2026-11-18)"; verifier report V46)

* B386: short-term 25th to 75th percentile 43.5 to 52.9; the release's 53.6 lies above the 75th percentile.
* B387: long-term 25th to 75th percentile 17.0 to 20.1.
* B388: medians 48.1 short term (below 53.6) and 18.5 long term (equal to base).
* B389: minimum to maximum 32.0 to 69.5 short term, 15.1 to 23.0 long term (notes: the land raster raises the figure; the bottom falls mainly from the energy requirement).
* B390: factors 1.58 and 1.41 (5th to 95th), 2.17 and 1.53 (max over min).
* B391: 18 choices drawn, not 19; the loss-factor weight has no meaning on this release; all 18 vary, lbench with a small effect (up to about 71,000 people long term).
* B392: top five Sobol indices, short term (first and total order, V46's four-decimal values in notes).
* B393: top five Sobol indices, long term.
* B394: interactions about 5.5% of the short-term variance (corrected release about 2.6%).

The 5th to 95th figures themselves are B114 and B115, so they got no new row. B391 depends on B253 as well.

## 3. Cells changed (analysis)

* `analysis/method_tests_2025/harmonised_lines.py`: the branch at the old line 152 (`elif m.startswith('The model')`, which only the improved row reaches) now reads `results/ranges_2025-improved_wide.csv` (skipping its `#` first line; row variant=wide, setting=short, zone=1; p5 and p95 in millions, one decimal) instead of `cross_method.csv`; nothing hard-coded. Docstring "Reads" line names the file.
* `cross_method_local.csv`, row "The model, improved" (only line that differs; `harmonised_comparison_lines.csv` is byte-identical after the rerun):

| column | before | after |
|---|---|---|
| reading | 53.6 (46.2 to 60.1) | 53.6 (37.9 to 60.0) |
| low | 46.2 | 37.9 |
| high | 60.1 | 60.0 |
| low over corrected model | 1.11 | 0.91 |
| low over improved model | 0.86 | 0.71 |
| source | cross_method.csv (... 13-choice draws; no widened range exists ...) | results/ranges_2025-improved_wide.csv (5th to 95th percentile of 2,000 draws on 18 choices, decision 125; the loss-factor choice has no meaning on this release) |

High over corrected (1.45) and high over improved (1.12) round to the same values.
* `analysis/method_tests_2025/README.md`: line 298 (the B157 sentence; it lives here, not in the sensitivity README, where nothing says "contains none") takes B129's wording; line 614 (the block that `harmonised_lines.py` drives) now says the improved row prints 53.6 (37.9 to 60.0), 0.91 to 1.45 times the corrected central figure and 0.71 to 1.12 times its own, instead of "stale".
* `analysis/sensitivity_2025/README.md`, B130 section, V46's four points: (1) the added choices do not all lower the figure: the land raster raises it to 62.9 (short) and 21.7 (long) and lifts the maximum from 63.1 to 69.5, and the lower bottom comes mainly from the energy requirement (42.5), then meat calibration and waste; (2) lbench has a small effect on this release, up to about 71,000 people long term, first-order index 0.0001 and total order 0.0 (the file's values; V46's "under 0.0001" is read as rounding to those); (3) "the first 14 columns (the 13 earlier choices and avoidable waste)" replaces "the first 13 columns"; (4) the base 53.6 lies above the 75th percentile 52.9, and interactions carry about 5.5% of short-term variance (about 2.6% on the corrected release).
* `analysis/sensitivity_2025/sobol_2025-improved.csv`: the lbench source text in the long-term row only, "no effect in this release" to "small effect in this release (long term only; first-order index 0.0001; total order 0.0)". The short-term row keeps "no effect" because lbench moves only the long term (V46: short unchanged). The brief said one cell; this is one cell.

## 4. Defects

Added X141 (open): `make_readme_tables.py` hard-codes "13 uncertain choices" (line 343) and "21 crops"; found by the B127 and B130 builders. No row existed. The existing 140 rows are byte-identical.

## 5. Register rows touched

B114, B115, B157, B159, A205, A206, A219, A220, A264, A265, A266 (11 changed); B386 to B394 (9 added). Total rows 804 to 813. Defects 140 to 141.

## 6. Checks (as B122)

* 18 columns on every register row; row count old plus 9; untouched rows identical; CRLF kept in both files; no em dashes in the register, defects, READMEs or script.
* `MC_RELEASE=2025-improved check_wide.py` passes on the stated figures (exit 0: short 37.9 to 60.0, long 15.7 to 22.1); the corrected-release default run also passes.
* `harmonised_lines.py` reran with `python3 -I` from the repository root; the stop-if-not-9.6% check passed.
* `qa/tools/numbers_lint.py` ran and finished (5,505 rows). It rewrote its own dated output `qa/reports/numbers_lint_2026-11-07.csv`, which is outside my write list; I did not keep a copy of the old one, so the coordinator may want to restore it from the repository.

## 7. Things I saw and did not change (outside the brief)

* A205, A206, A220, A265, A266 still have locators or `release_or_data` that describe the improved figures (for example A205 locator "-0.26%; results/scenarios.csv", A220 "48.27%"); A219 and A264 `release_or_data` still say 2025-store-1 and 2025-store-2. Only A264 and A219 locators were asked for.
* Paper-side text and claims csvs that carry 46.2 to 60.1 were not touched (rule).
* The method_tests README design_choices block still lacks the improved Monte Carlo row (see X141).
* I ran one `git status` by reflex while checking whether the tree is a repository; it only read. No other git use.

## Wrong-value check:

Example of what was NOT done: B159 is Tier A, so its value was NOT changed outright. A wrong move would be setting its `value` to "41.5 (31.1 to 49.2); 53.6 (37.9 to 60.0)" and its statement to "...improved entry 53.6 (37.9 to 60.0)" while the status still read "approved gate 5". What stands is value "41.5 (31.1 to 49.2); 53.6 (46.2 to 60.1)" and the statement unchanged, with the new range only in `notes` and `status`. A scripted compare of the changed register against the copy taken first shows B159 differing in `status` and `notes` only (B114 likewise), and A205 and A206 in `statement` (wording) and `notes` only, with `value` equal in every one of the 11 changed rows except B115 (Tier B).

## Changed files

* `qa/claims_register.csv`
* `qa/defects.csv`
* `analysis/method_tests_2025/harmonised_lines.py`
* `analysis/method_tests_2025/cross_method_local.csv`
* `analysis/method_tests_2025/README.md`
* `analysis/sensitivity_2025/README.md`
* `analysis/sensitivity_2025/sobol_2025-improved.csv`
* `qa/reports/B131_register_after_B130.md`
* (side effect, not intended) `qa/reports/numbers_lint_2026-11-07.csv`, rewritten by `numbers_lint.py`
