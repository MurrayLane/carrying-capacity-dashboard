# Card: standing decisions, never-do rules and how "yes" is read

Re-read after every compaction and at the start of every session. One page. Changes only by Murray's word.

## How "yes" is read (Murray, 2026-11-07: "I say yes to all recommendations a lot and it costs me time")
1. **A bare "yes" or "go" to a message that ends with a decision table means yes to every row's Recommended option**, the "Recommended combined action". "Yes except 3" or "yes, 4 no, 5 option B" overrides by number. Every table ends with the line: *Reply "yes" to take all recommendations.*
2. **Standing approval.** A recommended action is done without asking, and reported afterwards under "Done, and how to undo it", when ALL of these hold: (a) it is inside the standing decisions below; (b) one command or one revert undoes it; (c) it costs no money beyond the weekly allowance, with the share stated when it is large or known; (d) nothing leaves the project (no email, post or submission); (e) it does not change the value of a headline (Tier A) claim.
3. **Always asked, never standing:** spending money; anything sent outside (emails to authors, correction notes, submissions); publishing or releasing (the archive, Zenodo, tags); deleting or overwriting data; changing a standing decision or the direction of a paper; touching another project's repository; anything that changes a Tier A claim.
4. The decision table keeps only the rows that need Murray. Rows under standing approval are listed under "Done".
5. Murray can narrow or widen these bounds here, in one place.

## Tasks that send Murray online (Murray, 2026-11-08)
Every task that asks Murray to open, search, download or upload something online carries the full URL in the same sentence, and for a library item the QUT sign-in link (https://go.openathens.net/redirector/qut.edu.au?url=<link>). A task without its URL is not finished. The URL goes in the same sentence as the request every time it is made, including inside a decision row, even when the same link appears elsewhere in the message or in an earlier message; a sentence such as "check the journal's page" or "you fetch it" without the link breaks the rule (Murray, 2026-11-14, after a third reminder). Where no exact URL is known, give the search URL with the search terms filled in and say it is a search. For a library item the preferred form is the QUT library search with the title filled in: https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,<title, URL-encoded>&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT (Murray, 2026-11-09).

## Reporting the cost of work (Murray, 2026-11-07)
* State the cost of any job or round as an **anticipated percentage of the weekly allowance**, never as tokens. The session cannot read the allowance, only that it is allowed and when it resets (Saturdays, 09:59 Brisbane), so the percentage rests on a calibration: Murray's reading of the usage figure in the app at a stated time, set against the tokens logged in `spend.csv` since the previous reading. Record each calibration here. Small percentages are fine to state.
* **Calibration 2026-11-07 (rates measured by Murray's other coordinator from eight readings, 18 to 26 October):** "Fable only" is a sub-limit inside "all models"; coordinator turns count on both meters, Opus and Sonnet workers on "all models" only. A long Opus worker (20 to 30 minutes) is about half a point of all models; a short one about a quarter; a wide-reading one, one to two points. A heavy coordinator day is about 18 Fable points and 10 all-models points; a light day about 6 Fable. The week resets Saturday 09:59 Brisbane; the warning line is 90 per cent of all models. Sonnet workers are not separately measured: assume a third to a half of an Opus worker of the same length until a reading says otherwise. State every job's share from these rates and its expected length.

## Standing decisions (do not reopen)
* **Recency in the literature reviews (Murray, 2026-11-09):** journals favour recent citations. Each review point carries recent work (2016 onwards) wherever it exists, and the classics only where the lineage needs them; every sweep and reading brief ranks recent candidates first and reports the year mix of each section.
* **Tone of the methods paper (Murray, 2026-11-08):** no big deal is made of other authors' methodological shortcomings (Simpson among them). Each reconstruction states the access we had (which sources, which pages) and the assumptions we made, and reports reproduced or not reproduced on that basis. Critique is of what the method can and cannot see, not of the authors' work.
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
* Every builder brief that changes a script or an output ends with "list the register rows whose value or status this changes"; the coordinator applies the list before the commit (X074, 2026-11-07: six measures rows went stale for a day because this was not done).
* A Tier A claim is verified only when two routes agree: the evaluator and a second implementation (the original workbook, V15) for capacities; the script and a blind re-derivation for every other figure.
* Before another verification round, write "if this comes back the other way I will do X differently"; with no X, stop.
