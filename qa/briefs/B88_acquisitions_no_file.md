# Builder brief B88: the cited works with no file that carry a number into a paper (decision 82)

Rules: plain language; no time words; no em dashes. No git; no subagents. Network allowed only to api.crossref.org to confirm a title or DOI. Write only `qa/reports/acquisitions_2026-11-13.md`.

From `qa/literature_register.csv`, take every row cited in `papers/A_results/SECTION_SCOPE.md` or `papers/B_methods/SECTION_SCOPE.md` (ids L###) that has an empty `local_path`. For each, decide from the scope's use of it (the sources table row and the evidence table) whether a figure from the work enters a paper (a number, a range, a named finding quoted as fact) or whether it is cited only as a reference for an idea. Produce two lists:
A. Number-bearing, to fetch: one line each with the register id, the full citation, what figure the paper takes from it, and ONE link: the DOI link if the row or Crossref gives a DOI, else the QUT title search in this exact form `https://qut.primo.exlibrisgroup.com/discovery/search?query=any,contains,<title URL-encoded>&tab=Everything&search_scope=MyInst_and_CI&vid=61QUT_INST:61QUT`. Skip rows that are second-hand by design (reported through another work, such as the Migration Committee range via Henry and Godden) and say so in list C.
B. Reference-only: id and short citation, no link needed.
C. Second-hand by design or unobtainable (grey reports with no catalogue entry): id, short citation, and why.
Head the file with the upload link https://github.com/MurrayLane/carrying-capacity-models/upload/main/Literature%20review and the counts. Then "Register rows touched: none" and "Wrong-value check:" with one deliberate example of a work wrongly placed in list A, marked as an example.
