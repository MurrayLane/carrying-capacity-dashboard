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
Report format (your final message): (1) what you wrote and the row count; (2) every field or row you could not establish; (3) anything surprising or that looks wrong in the project's own documents; (4) rows a human should check first.

## Task B05: the claims register for the methods paper (Paper B)

Write: `qa/claims_register.csv` (header exactly as in `qa/README.md`; ids B001, B002, ...; status `unverified` on every row).

A claim is a number or a statement that will appear in the paper. Build the rows from these documents, in this order, reading each in full: `papers/B_methods/OUTLINE.md` (the headline block, the method-tests table, section 6's design-choice bullets), `analysis/method_tests_2025/README.md` (every table and every bullet with a number), `analysis/method_tests_2025/cross_method.csv`, `design_choices.csv`, `ladder.csv`, `model_entry.csv`, `papers/B_methods/SECTION7_DRAFT.md` (every number in the "why each rating" lists), and `analysis/comparators_2025/README.md` sections 2, 2b, 3 and 3b (the model re-run under other definitions, the ten diets, the export counts).

For each claim: `statement` in one sentence; `value` and `unit`; `tier` A for anything in the outline's headline block, the cross-method table, the design-choices table or the ladder, B for other numbers in the READMEs, C for descriptions of methods and sources; `script` the script that produces it (read the script headers: each names its inputs and outputs); `release_or_data` the release id or data extract; `output_file` and `output_locator` (the csv and the row or cell, or the README table and row); `sources` the ids from `qa/sources_register.csv`; `method_source` the L-id from `qa/literature_register.csv` of the method's paper; `depends_on` other claim ids whose value feeds this one. Where a README number has no output file (typed into the README), say so in `notes` with the words `typed, no output file`: that is a finding, not a failure.

Check as you go: where a README table number should equal a csv value, compare them and put any mismatch in your report under (3), with both values. Do not change any file except the register.
