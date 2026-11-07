# Card: standing decisions, never-do rules and how "yes" is read

Re-read after every compaction and at the start of every session. One page. Changes only by Murray's word.

## How "yes" is read (Murray, 2026-11-07: "I say yes to all recommendations a lot and it costs me time")
1. **A bare "yes" or "go" to a message that ends with a decision table means yes to every row's Recommended option**, the "Recommended combined action". "Yes except 3" or "yes, 4 no, 5 option B" overrides by number. Every table ends with the line: *Reply "yes" to take all recommendations.*
2. **Standing approval.** A recommended action is done without asking, and reported afterwards under "Done, and how to undo it", when ALL of these hold: (a) it is inside the standing decisions below; (b) one command or one revert undoes it; (c) it costs no money beyond the weekly allowance, with the share stated when it is large or known; (d) nothing leaves the project (no email, post or submission); (e) it does not change the value of a headline (Tier A) claim.
3. **Always asked, never standing:** spending money; anything sent outside (emails to authors, correction notes, submissions); publishing or releasing (the archive, Zenodo, tags); deleting or overwriting data; changing a standing decision or the direction of a paper; touching another project's repository; anything that changes a Tier A claim.
4. The decision table keeps only the rows that need Murray. Rows under standing approval are listed under "Done".
5. Murray can narrow or widen these bounds here, in one place.

## Reporting the cost of work (Murray, 2026-11-07)
* State the cost of any job or round as an **anticipated percentage of the weekly allowance**, never as tokens. The session cannot read the allowance, only that it is allowed and when it resets (Saturdays, 09:00 Brisbane), so the percentage rests on a calibration: Murray's reading of the usage figure in the app at a stated time, set against the tokens logged in `spend.csv` since the previous reading. Record each calibration here. Until the first calibration, give the estimate with its basis stated. Small percentages are fine to state.

## Standing decisions (do not reopen)
* **Two papers only.** The data paper is the archive with a DOI, not a journal paper. Order of submission: methods paper first, then results paper.
* **Methods paper (B):** a critical narrative review for land use planners and sustainability analysts. Each method is tested by applying it to Australian 2025 data, wherever its authors first used it; no reproduction gate; a published author's figure is a fidelity check where one exists, and a method checked only against its description is never called reproduced. 2025 data only. The author's own model is one exemplar, disclosed as the author's, tested and critiqued by the same tests and then built on (baseline and improved). Scale appears as a design choice with three points; the Monte Carlo method and the national range are here.
* **Results paper (A):** 2011 to 2025 by region, on the corrected releases; 2011 results given as corrected only, with one footnote that the original published values were updated; no reconciliation table; the full scale curve to SA2, the zone-by-zone ranges, the long term, shocks, the method effects by region and the discussion of measures are here.
* **Corrected values are assumed** (the correction notes are drafted; whether and when to send them is Murray's). The error search closed on 2026-11-04.
* **The method is frozen during the data refresh;** two lines of enquiry always: the thesis method on new data, and improvements.
* **Zenodo release is on hold** until Murray releases it.
* **Journal, authors and order of authors** are decided later by Murray.
* **Quality:** `QUALITY_PLAN.md` and `DECISIONS.md` (all seven recommendations approved on 2026-11-07).

## Never do
* Commit with `git add -A` while any builder is running: add files by explicit path, and only the files of a job whose report is in (2026-11-07, defect X030).
* Put copyrighted PDFs, or anything from TenderFolio's internals, in the public repository.
* Edit any repository other than `carrying-capacity-dashboard` and the private archive `carrying-capacity-models`.
* Push tags (the proxy refuses; the unmodified snapshot is commit `04a612e`).
* Type a number into a paper, outline or README by hand: tables are generated, or the number is copied from a named output file with the file named.
* Describe a reconstruction as a reproduction, or a secondary-source figure as read.
* Use the words tonight, later, for now, not urgent, fresh session (TenderFolio house rule loaded in this session); quote code work in human hours.
* Report to Murray in jargon: plain language, the outcome first, decisions as a numbered table with recommendation, confidence, cost and reason.

## Verification rules
* A verifier gets the requirement and the recipe, never the earlier finding, and is a different model from the builder.
* A check that cannot fail does not count: say what would make it go red and confirm it can.
* A change to a release, module, source or script marks every dependent claim unverified (`INVALIDATES:` first line of the message).
* Before another verification round, write "if this comes back the other way I will do X differently"; with no X, stop.
