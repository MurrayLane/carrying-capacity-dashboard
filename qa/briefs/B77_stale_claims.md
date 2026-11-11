# Builder brief B77: stale claim rows, and claims for the gap attribution (decisions 63, 65)

Rules: plain language; no time words; no em dashes. No git; no subagents; no network. Write only `qa/claims_register.csv` and `qa/reports/B77_stale_claims.md`. Tier A rule: if re-deriving a row changes a Tier A value, do NOT change it; write the finding in the report as a decision row for Murray and leave the register row as it is with a note.

Part 1, re-derive from the analysis file each row cites and correct text, value or notes where they no longer match (the Paper A scope `papers/A_results/SECTION_SCOPE.md` names where each was found):
- A119: NRM zones' unused land 4.80 million km2 against `analysis/scale_curve_2025/README.md` 4.50. Find which is right from the csv behind the README.
- A124: says the ideal contiguous split is not known; `analysis/regionalise_2025/summary.csv` holds it. Update and add Tier B rows for the regionalise results the scope names (section 5 of the scope).
- A140: garden shares against `analysis/` README the scope names.
- A225: reword to "worth more than any other named scenario" (decision 66 route, N-A7).
- A314: the interaction term against `results/method_effects.csv` and its README.
- A333: the figure-script count (figures 4, 7 and 8 have scripts; 1, 2, 3, 5, 6 none; figure 2 needs region polygons).
- B243: reword to the checklist items that moved the answer more than 1.2 times (the land base moved it 1.09; decision 60).
Part 2, add claim rows (Tier B, status "unverified", route "gap_attribution.py") for every figure in `analysis/method_tests_2025/gap_attribution.csv` that the README's "Gap attribution" section quotes, following the register's column conventions exactly (read `qa/README.md` first). Ids continue the B-series.

Checks: the register parses with Python's csv module; row count = old count + rows added; no em dashes; line endings unchanged. Report: a table (row; what was wrong; what it says now; file and cell checked), the Tier A rows you did not change and why, the new rows (ids), and "Wrong-value check:" with one deliberate example of a correction that would itself be wrong, marked as an example.
