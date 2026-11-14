# A process for rigorous, agent-run research projects

Written 2026-11-14 at Murray's request, revised the same day to describe the whole arrangement, including the orchestrator and the workers, in general terms so it can be adopted for most research projects. It is a description, not a prompt.

## 1. The cast

* **The author.** Owns every decision. Sets the question, the standards, the pace and the tone. Approves verified results in writing at gates. Fetches what only a person can fetch (library items, paywalled documents, sites that refuse automated access).
* **The orchestrator.** One long-running session on the strongest available model. It never does the research itself: it reads the state of the project, writes briefs, spawns workers, reads their reports, commits their files, keeps the records, and puts decisions to the author. It edits only the project's own records (decisions, rules, briefs, reports, registers' housekeeping), never analysis, code or prose. Because it holds the whole history in one context, it is the only party that can see when two workers' findings disagree or when a rule is being broken.
* **Builders.** Short-lived worker sessions, usually on a cheaper model, each with one written brief: read these inputs, write only these outputs, report in plain language. They compute, read, write, correct. They never run git, never spawn their own workers, and never edit a register row the brief does not name.
* **Blind checkers.** Short-lived worker sessions on a strong model, and a different model from the builder they check. A checker re-derives the result by its own route before looking at the builder's; states its tolerance before comparing; plants a deliberate wrong value to prove the check can fail; opens the file under test last; writes a report and nothing else.
* **Drafters.** Builders whose output is prose. They write only from the registers and the section scope, cite only register rows, and keep a claims file beside every section listing each number's source.
* **Compilers.** Builders that assemble digests, consolidated reports and provenance maps from the other workers' reports, so the author reads one page rather than fourteen.

## 2. The records (the project's memory, all in the repository)

* **Claims register.** One row per number or finding that may enter a paper: statement, value, unit, tier, the script that made it, the data it ran on, the output file and cell, the data-source ids, dependencies, status, the checker's report, notes.
* **Sources register.** One row per data file: kind, title, origin (URL or catalogue id), date taken, local path, hash, what the pipeline takes from it, status.
* **Literature register.** One row per cited work: citation with DOI, origin, local path and hash, what was taken with page numbers, how it was read (full, targeted, abstract, second-hand), what it is used for, status, notes.
* **Defects file.** Every fault found, by whom, fixed by which job, or left open with a reason.
* **Decisions file.** Every decision the author took, numbered, with the words they used and the jobs that carried it out.
* **Rules card.** The standing rules of engagement, each with the date and the author's words.
* **Gates file.** Each approval the author gave: what was approved, on which digest, with the file hashes at that commit.
* **Briefs and reports folders.** Every brief issued and every report returned, by job id, so any finding can be traced to who found it and how.
* **Errata.** Errors found in the published work, with evidence, size, status and the correction's location.
* **Handoff note.** Where the project stands, for the next session.
* **Spend log.** Every job's model and tokens, so cost estimates are calibrated against actuals.

## 3. The loop the orchestrator runs

* Read the state: registers, decisions, handoff note, the last reports.
* Size the next piece of work and put it to the author as a numbered decision table: option, recommendation, confidence, cost as a share of the author's allowance, reason; ending with one line that a bare "yes" takes every recommendation.
* On the author's word, write one brief per job. A brief names the inputs, the allowed outputs (file by file), the rules that bind (plain language, tone, no time words, no em dashes), the method, the checks the worker must run before finishing, and the report's required contents (including the register rows touched and a worked wrong-value example).
* Spawn independent jobs in parallel; sequence jobs that share a file.
* On each report: read it, commit the worker's files by explicit path with a message naming the job, and relay the finding to the author in two or three plain sentences. Never commit everything at once while another worker is still writing.
* After a wave: log spend, update the handoff note, regenerate the provenance maps, and put the next decision table to the author.
* When a checker fails a builder's work, spawn a correction builder with the checker's exact findings; when a correction changes a verified value, hold it as "pending" until the author approves it at a gate.

## 4. The standard of evidence

* A number is usable only if it has a register row with a script, an output cell and data sources.
* A number is verified (Tier A) only when two independent routes agree: the builder's and a checker's own.
* Every data source is opened against its original: file present, hash matching, origin confirmed, and a sample of the values the pipeline uses checked against the source file itself.
* Every literature figure is cited to the page where the number is printed, from a file on disk, never from memory and never copied from a register. Second-hand figures are labelled as second-hand. Works with no file are cited "as reported in" the work that reports them, or marked as not seen.
* Every check states its tolerance before comparing, plants one deliberate wrong value to show the check can fail, and reports the register rows it touched (usually none).
* A provenance map, generated by a script, traces every fact in each paper to its claim row, output cell, script, data row and original source, with the status of each link, so the whole chain can be inspected on one page and regenerated at any time.
* A verified value never changes without the author's written approval of a one-page digest of plain statements; the approval is recorded with the files' hashes.

## 5. The order of work

* Register and verify the project's own results first, before any reading or writing about them.
* Read every source at page level, raising register rows from "abstract" or "record" to "read" with pages.
* Scope every section of every paper before drafting: purpose in plain words, the points in order, the claim rows behind each point, the tables and figures with the file each is built from, the sources with read status and year band, the gaps, the open decisions, a word budget.
* Run a logic check per paper: does each point's evidence support it; any contradiction within the paper or between papers; any figure quoted on a different basis from the one named.
* Run a provenance audit before the first draft: every source against its original; every one-route claim given a second route; every literature row at page level; the maps regenerated.
* Draft from the scopes, in parallel parts, each with its claims file. Blind-check every sentence of the draft against the registers. Fix. Cut to the journal's stated limit by moving detail to supplementary information, never by dropping a number the scope requires.
* Gate: digest, author's approval, register statuses updated, hashes recorded. Only then does the next stage rest on the result.

## 6. Rules of engagement with the author

* Plain language in everything the author reads; numbers in tables, not prose; one idea per sentence.
* Every open item is a decision row; nothing is deferred with a time word.
* Standing approval for small reversible actions inside the project. An explicit ask before spending money, sending anything outside, publishing or tagging, deleting data, changing a standing decision, touching another repository, or changing a verified value.
* Every task that sends the author online carries its full URL in the same sentence, every time, including inside a decision row; for library items, the institution's title-search URL with the title filled in.
* Costs as a share of the author's allowance, calibrated once against the author's own meter and then against the spend log; raw tokens never.
* The orchestrator relays each worker's finding faithfully, including its own mistakes when a checker catches them.

## 7. Rules for the papers themselves

* Tone: state what each method or author does, the access had and the assumptions made; no verdicts on other authors' shortcomings.
* Recency: reviews lead with work from the last ten years; classics for lineage only.
* Basis: the release, the method tier, the time frame and the yield or land basis are named at every figure; one ratio convention throughout; shared numbers mean the same thing in both papers.
* Length: the journal's stated limit, checked on the journal's own page; detail goes to supplementary information.
* Integrity: frozen releases are never edited; a correction goes into a new hash-locked release with an errata entry; nothing copyrighted enters a public repository; the author's identity and personal details never enter a prompt, a payload or a sample value.

## 8. What went wrong here, and the rule that fixed it

* Register notes went stale when a builder changed an output: every builder now lists the register rows it touches.
* Abstract-based characterisations of papers were loose about a third of the time: nothing rests on a line until the paper is read at page level.
* Full readers cited the discussion page rather than the page the number is printed on: every reading brief now says "the page where the number is printed".
* Scopes written before a check carried stale statuses into drafting: scopes are refreshed after every check that touches their rows.
* True numbers became wrong sentences through mixed bases (published versus corrected release, short versus long term, national versus regional sum, two yield bases): naming the basis at every figure is a header rule of every scope.
* An input copied from an adjacent row survived a decade because every check looked at outputs: the audit now includes an input-plausibility pass (duplicates, sums, ranges) on every input table.
* The orchestrator made slips of its own (a title typed from memory, a file saved under the wrong name): the blind checks caught them because they re-derived from files, not from the orchestrator's words, which is the reason checkers never take the orchestrator's summary as an input.
* Estimates of cost were too high until calibrated: one calibration against the author's meter, then the spend log.

## 9. Adopting it elsewhere

* The cast, the records, the loop and the standard of evidence transfer unchanged to any project where numbers and citations must be right: empirical papers, systematic reviews, data releases, audits.
* The registers' columns are the only project-specific part; keep the ids, the status vocabulary (unverified, self-checked, independently verified, approved, withdrawn) and the two-route rule.
* The minimum viable version is: one orchestrator, builders and checkers on different models, the four registers, decision tables, and gates with hashes. Everything else here grew from those.
