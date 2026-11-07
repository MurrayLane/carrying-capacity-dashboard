# Builder brief

You are a builder helper. The coordinator (the main session) wrote this brief and will review your work, so do not try to decide what anything means.

Rules, no exceptions:
* Write only the file(s) named under "Write". Read anything else, change nothing else. Do not run git; the coordinator commits.
* Do not change any result, script or data file. Do not spawn subagents.
* Never invent. If you cannot establish a field, write `unknown` and list it in your report. Copy citations and titles exactly as you find them and record where you found them.
* Every row must rest on something you opened (a file, a page). A path in a row means the file exists: check it.
* Plain, specific notes. No time words (tonight, later, for now, not urgent).
* Repository root: /home/user/carrying-capacity-dashboard (public). The private archive is /home/user/carrying-capacity-models; refer to its files as `carrying-capacity-models/<path>`. Both exist on this machine.

Standing decisions you must not reopen: two papers only; the methods paper tests each method on Australian 2025 data and gives no reproduction gate; corrected values are assumed; the results paper gives 2011 as corrected only. Read `qa/CARD.md` and `qa/README.md` (the schemas) first.
Report format (your final message): (1) what you wrote; (2) what you could not establish; (3) anything surprising or that looks wrong in the project's own documents; (4) items a human should check first.

## Task B07: the numbers lint

Write: `qa/tools/numbers_lint.py` and `qa/reports/numbers_lint_2026-11-07.csv` (its first run). Nothing else.

Purpose: find every number typed into a document that is not present in a current generated output file, so stale or hand-typed figures are caught mechanically. The pre-dairy-module figures that survived in several READMEs until today are the case this exists for.

Specification:
* Inputs, by default (take paths as arguments so they can be changed): documents to scan `papers/B_methods/OUTLINE.md`, `papers/B_methods/SECTION7_DRAFT.md`, `papers/A_results/OUTLINE.md`, `papers/A_results/DISCUSSION_MEASURES.md`, `analysis/method_tests_2025/README.md`, `analysis/paper_a/README.md`, `analysis/comparators_2025/README.md`, `HANDOFF.md`; output files to trust: every `.csv` under `results/`, `analysis/method_tests_2025/`, `analysis/paper_a/`, `analysis/comparators_2025/`, `analysis/sensitivity_2025/` and `analysis/scale_curve_2025/`.
* Build the set of trusted values: every numeric cell in the trusted csvs, plus each such value rounded to 0, 1 and 2 decimal places, plus the value divided by 1e3 and 1e6 (so 41503537 is found as 41.5 and 41.504), plus percentages where a csv holds a share (0.754 is found as 75 and 75.4).
* Scan the documents for numbers: decimals, integers of two or more digits, numbers with thousands separators, percentages. Skip: years 1860 to 2030, dates, ids such as `2025-fixed`, section numbers at a line start, citation numbers (volume, issue, page ranges), DOIs, commit hashes, token counts, file sizes, and numbers inside code spans or paths. Keep a list of the skip rules in the script header.
* For each number found, look for a trusted value equal to it or within a rounding tolerance of half a unit in the number's last written digit. Numbers between 0 and 1 and small integers under 10 are too ambiguous to lint: report them in a separate `ambiguous` category, not as failures.
* Output csv columns: `document`, `line`, `number`, `context` (the line, trimmed to 160 characters), `status` (`found` / `not found` / `ambiguous` / `skipped`), `matched_file`, `matched_value`. Print a summary per document: counts of found, not found, ambiguous.
* Run with `python3 -I qa/tools/numbers_lint.py` from the repository root; it must run with no arguments and finish in under a minute.

In your report, list the `not found` numbers for `analysis/method_tests_2025/README.md` and `papers/B_methods/OUTLINE.md` with their context, so the coordinator can see which are typed figures (from other authors' papers, or arithmetic in prose) and which are stale. Do not change any document.
