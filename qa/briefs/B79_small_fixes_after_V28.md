# Builder brief B79: small fixes after V28 and B77 (decisions 70, 71)

Rules: plain language; no time words; no em dashes. No git; no subagents; no network. Write only `papers/B_methods/SECTION7_DRAFT.md`, `analysis/scale_curve_2025/README.md`, `analysis/comparison_2025/decompose.mjs` (one comment only), `qa/defects.csv` and `qa/reports/B79_small_fixes.md`.

1. In `SECTION7_DRAFT.md`, the reasons under purpose 1 say the energy balance, footprint, HALF and people per hectare "read 134 to 343 million"; the tests give 103 to 343 (claims B046, B156; confirm in `qa/claims_register.csv`). Correct it. Also apply decision 69: set the three cells (HALF and people per hectare on purpose 2; footprint on purpose 3) to "partly" with the one-line reasons in `qa/reports/V28_section7_matrix.md`, keeping the draft's original reason as the stated limit.
2. `analysis/scale_curve_2025/README.md` line about 47 says the SA2 boundaries are not in the repository and the contiguous value is not known; the repository holds `data/sa2/adjacency.csv` and `analysis/regionalise_2025/summary.csv` (claims A124, A347 to A353). Reword to what is now known, with the figures from A124.
3. `analysis/comparison_2025/decompose.mjs` has a comment saying the land and population layers give identical capacities; B76 found this false for Northern and Yorke (infrastructure land that follows population). Change the comment only; no code.
4. Append two defect rows to `qa/defects.csv` (next ids after the last; layer and kind as the register uses): the scale-curve README line (found_by S02/B77, fixed_in B79) and the decompose.mjs comment (found_by B76, fixed_in B79). Keep the file parsing and its line endings.

Report: what changed (file:line, before, after), the register rows touched (none), and "Wrong-value check:" with one deliberate example of a wrong fix, marked as an example.
