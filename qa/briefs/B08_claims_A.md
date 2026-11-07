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

## Task B08: the claims register for the results paper (Paper A)

Write: append rows to `qa/claims_register.csv` (ids A001, A002, ...; keep every existing B row untouched; header unchanged; status `unverified`). Nothing else.

Build the rows from, in this order, reading each in full: `papers/A_results/OUTLINE.md` (the narrative and headline block, every section with a run note, the figures list), `analysis/paper_a/README.md` (every table and every bullet with a number), its csv outputs (`regional_flips.csv`, `shocks_summary.csv`, `shocks_by_region.csv`, `scenarios_by_region.csv`, `long_term_regions.csv`, `long_term_levers.csv`, `measures.csv`, `store_equivalence.csv`, `transfers.csv`, `method_effects_summary.csv`, `method_status.csv`), `papers/A_results/DISCUSSION_MEASURES.md` (every number), `analysis/scale_curve_2025/README.md` (the table and the reading bullets; the scale curve is Paper A's), `results/scale_curve.csv`, `analysis/comparison_2025/movers.md` and `movers.csv` (the candidate regions), and `HANDOFF.md`'s headline table (the national figures and ranges).

Follow the same rules as the methods-paper rows (see the first B rows for the style): one sentence per claim; tier A for the headline block of the outline, the national figures, the scale curve shares and the regional-flip counts; B for other numbers; C for descriptions. `script` and `output_file` from the script headers in `analysis/paper_a/` (the `.mjs` and `.py` files name their outputs); `output_locator` the csv row or cell; `sources` from `qa/sources_register.csv`; `depends_on` other A or B claim ids. Mark any number typed into a README or script with `typed, no output file` in notes. As you go, compare every README table number with its csv value and report mismatches under (3) with both values. In particular check: the regional-flip counts against `regional_flips.csv`; the long-term "94% of the population" and the regions-over-capacity counts against `long_term_regions.csv`; every measure's percentage against `measures.csv`; the store-equivalence years (16 and 10) against `store_equivalence.csv`; the transfers figures; and the scale-curve shares in the README against `results/scale_curve.csv` (state yield basis, 2025-fixed and 2011-fixed).
