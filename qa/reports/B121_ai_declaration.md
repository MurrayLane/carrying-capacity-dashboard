# B121 report: generative AI declaration, competing interests, funding and CRediT, drafted from the records

## Files changed
* `/home/user/carrying-capacity-dashboard/papers/DECLARATIONS.md` (new: the texts)
* `/home/user/carrying-capacity-dashboard/qa/reports/B121_ai_declaration.md` (this report)

No other file was written. Records touched: none. No git, no subagents, no network.

## What the texts are
All in `papers/DECLARATIONS.md`: (1) short declaration, 103 words, for the manuscript; (2) fuller declaration, about 320 words, for a cover letter or supplement, in the audit's shape (registers, two routes, blind checks, gates); (3) competing interests; (4) funding; (5) CRediT for one author. Both declarations end with the journal's required sentence in the singular ("I reviewed and edited the content as needed and take full responsibility for the content of the published article"), taken from `papers/B_methods/JOURNAL_REQUIREMENTS.md`.

Paper A: no copy of the Population and Environment guidelines is on disk (searched the repository and the file system for submission-guideline files; none). As the brief says, the Elsevier form is used for both and the file notes it, with the URL for the author to check.

## What each sentence rests on
* Tools named (Claude Opus and Sonnet; Claude Code): `qa/spend.csv`, whose model column holds only "opus" (98 rows) and "sonnet" (86 rows), plus two rows with a stray comma in the job name; the 186 logged jobs run 2026-11-07 to 2026-11-18. The coordinating session is "Fable" in `qa/CARD.md` (calibration note); it is not in the spend log.
* Rebuilding and running the model: B-series builders, V02, V03, V06 independent rebuilds, R01 clean-room reproduction (spend.csv; `qa/reports/R01_clean_room_reproduction.md`).
* Retrieving and reading sources: B14 literature sweep (web search and fetch, brief `qa/briefs/B14*.md`), B66a to B67b page-level readings, `qa/RESEARCH_PROCESS.md` section 5.
* Checking by independent re-derivation, planted wrong value, tolerance stated first, different model from builder: `qa/RESEARCH_PROCESS.md` sections 1 and 6; `qa/CARD.md` verification rules; briefs such as V40; two routes for Tier A, `qa/README.md` claims schema.
* Registers: `qa/sources_register.csv` (86 data rows), `qa/literature_register.csv` (246 rows), `qa/claims_register.csv` (707 rows) (line counts less header; the declaration states no counts, by the house rule against recording observations).
* Drafting from outline and registers, claims file beside each section: `RESEARCH_PROCESS.md` section 1 (Drafters); `papers/*/draft/*_claims.csv`; decision 91.
* Blind checks of drafts, sentence by sentence, drafting notes opened last: `RESEARCH_PROCESS.md` section 6 (Draft check); V35 named in decision 92.
* Simulated referee review: R02a to R02d (four personas, major revision each), R03a and R03b response plans; decision 112.
* Author's role: decisions 1 to 120 in `qa/DECISIONS.md` each carry Murray's words and date; gates in `qa/GATES.md` (gate 2 and the harmonised-comparison extension approved 2026-11-09 on the digest); `qa/CARD.md` ("anything that changes a Tier A claim" is always asked); Murray fetches closed works (decisions 47, 82, 89, 111).
* Competing interests: the decisions file and CARD say the model is the author's own; Paper B draft 9.5 already says it, and the journal requirement says to declare it.
* Funding: the journal's stock sentence, from JOURNAL_REQUIREMENTS.md; the records show no grant.
* CRediT: a single author, the roles that apply.

## The author must confirm or change
1. **Model names and versions.** The spend log gives families only ("opus", "sonnet"). A journal may want the version (for example "Claude Opus 4.x"). Check the account's usage history and enter versions. The coordinating model ("Fable", CARD.md) is named only as "a further Claude model"; give its name or drop the clause.
2. **Dates.** The logged jobs span 2026-11-07 to 2026-11-18, and the work may continue to submission. The declaration gives no dates; add a range if the journal asks, after the last job is logged.
3. **"Retrieved sources."** Retrieval was done by builder jobs with web access (B14, and later sweeps); several works were fetched by the author. The text says both. Confirm this matches what you want to claim about data fetching.
4. **"Every number and citation."** Citations were checked to register rows and page level, but the register holds rows "reported" or "not reached" for works with no file (decisions 82, 111). Either confirm you have personally checked every reference, as Elsevier requires, or soften the sentence. The fuller text says "I checked the reference lists"; that is a claim only you can make.
5. **"Doctoral thesis."** The competing-interests sentence says the model was built for the author's doctoral thesis. The records say "thesis model" and "thesis"; confirm the type of thesis and whether to name it.
6. **Funding.** Confirm no grant, no employer support and no funder paying for the Claude access.
7. **CRediT.** Name and affiliation left blank by design. Confirm that you want "Software" and "Formal analysis" claimed, given the agents did that work under direction.
8. **Paper A form.** Check the Population and Environment guidelines (URL in the file) for placement, heading and whether a separate AI statement is wanted; the Springer policy may differ from the Elsevier wording.
9. **Heading.** The Elsevier heading used is "Declaration of generative AI and AI-assisted technologies in the writing process"; confirm it against the guide for authors at submission.
10. **Simulated referees.** The text says plainly they are not real reviews; keep that if the journal reads "referee" claims closely.

## Worked wrong-value example (an example, not a finding)
If the text said "the Opus and Sonnet models" but spend.csv held a "haiku" row, the model line would fail against the log. Check run: the model column has only the two values (opus 98, sonnet 86) apart from two comma-split rows, so the claim holds.

## Flags outside the brief
* Two rows of `qa/spend.csv` (job names containing a comma: "Chapman and Byron, Kurtz" and "Wackernagel 2019, Wang") are split into the wrong columns; a model-count script will misread them. Not changed.
* Em-dash check on `papers/DECLARATIONS.md`: none found.
