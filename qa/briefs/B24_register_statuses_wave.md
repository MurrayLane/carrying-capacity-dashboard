# Builder brief B24: register statuses after the results-paper checking wave

Edit only `qa/claims_register.csv` (keep its line endings and every column; change only the `status` and `verifier report` columns, and `last verified commit` where given). No git; no subagents; plain language. The reports are `qa/reports/V08_regional_flips.md`, `V09_shocks_by_region.md`, `V10_long_term_and_measures.md`, `V11_method_effects_by_region.md`, `V12_scale_curve.md`; the defects are X050 to X064 in `qa/defects.csv`.

Rule: a claim is `independently verified` when a report says its number holds by the checker's own route (mark the report id and the commit e532199); `unverified: fault Xnnn` when the report finds the value wrong or the fault touches it; leave untouched any claim no report covers. Apply:
1. V08 holds: A029 to A039 (except that A038's Rangelands verdict depends on X054: mark A038 `independently verified; Rangelands verdict pending X054`).
2. V09 holds: A014, A163 to A165, A167, A171, A179 to A181, A183, A184, A187, A196, A199, A205, A206, A219, A220, A223 and every other section 8 row whose number appears in the V09 report's tables.
3. V10 holds: A007, A008, A010, A011, A234, A235, A246, A247, A258 to A261, A264 to A266 and the other section 7 and 11 rows the report covers; A240, A241, A322 become `unverified: fault X057`.
4. V11 holds: A312 and every section 9 method-effects row the report covers.
5. V12: A015 to A018, A074 to A078, A084 to A088 hold; A079 to A083 and A089 to A093 become `unverified: fault X062`.
6. A027, A028, A009 and every row that quotes a Monte Carlo range or a "not robust" verdict become `unverified: fault X054`.
Report: a count per status before and after, and the list of rows you changed with their new status.
