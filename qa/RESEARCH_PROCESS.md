# A process for rigorous, agent-run research

A general description of how to run a research project with one coordinating agent and many worker agents so that every number, source and sentence in the output can be traced and has been checked by someone other than the one who produced it. It is written for any project whose outputs must be right: empirical papers, reviews, data releases, audits, reports.

## 1. The cast

* **The author.** Owns every decision. Sets the question, the standards, the pace and the tone. Approves verified results in writing at gates. Does what only a person can do: fetch restricted material, sign off, decide between defensible options.
* **The orchestrator.** One long-running session on the strongest available model. It does none of the research itself. It reads the state of the project, writes briefs, spawns workers, reads their reports, commits their files, keeps the records and puts decisions to the author. It edits only the project's records, never analysis, code or prose. Holding the whole history in one context, it is the only party placed to see when two workers disagree or a rule is being broken.
* **Builders.** Short-lived workers, usually on a cheaper model, each with one written brief: read these inputs, write only these outputs, report in plain language. They compute, read, write and correct. They never run version control, never spawn workers of their own, and never edit a record the brief does not name.
* **Blind checkers.** Short-lived workers on a strong model, and on a different model from the builder they check. A checker re-derives the result by its own route before looking at the builder's; states its tolerance before comparing; plants a deliberate wrong value to prove the comparison can fail; opens the file under test last; writes a report and nothing else.
* **Drafters.** Builders whose output is prose. They write only from the registers and the section plan, cite only register rows, and keep a claims file beside every section listing the source of each number.
* **Compilers.** Builders that assemble digests, consolidated reports and provenance maps from other workers' reports, so the author reads one page rather than many.

## 2. The records

All in the repository, all plain text, all under version control.

* **Claims register.** One row per number or finding that may enter an output: statement, value, unit, tier, the script that made it, the data it ran on, the output file and cell, the data-source ids, dependencies, status, the checker's report, notes.
* **Sources register.** One row per data file: kind, title, origin (URL or catalogue id), date taken, local path, hash, what the pipeline takes from it, status.
* **Literature register.** One row per cited work: citation with identifier, origin, local path and hash, what was taken with page numbers, how it was read (full, targeted, abstract, second-hand), what it is used for, status, notes.
* **Defects file.** Every fault found: by whom, fixed by which job, or left open with a reason.
* **Decisions file.** Every decision the author took, numbered, with the words they used and the jobs that carried it out.
* **Rules card.** The standing rules of engagement, each with the date and the words that set it.
* **Gates file.** Each approval the author gave: what was approved, on which digest, with the file hashes at that commit.
* **Briefs and reports folders.** Every brief issued and every report returned, filed by job id.
* **Errata.** Errors found in already-published work, with evidence, size, status and where the correction lives.
* **Handoff note.** Where the project stands, written for a session that has no chat history.
* **Spend log.** One row per job: date, job, model, tokens, outcome.

## 3. The loop the orchestrator runs

* Read the state: registers, decisions, handoff note, the latest reports.
* Size the next piece of work by script over the records (how many rows, sources or sections it touches, at what status) and convert the count to a cost on a calibrated basis.
* Put the work to the author as a numbered decision table: option, recommendation, confidence, cost as a share of the author's allowance, reason; ending with one line that a bare "yes" takes every recommendation.
* On the author's word, write one brief per job.
* Spawn independent jobs together; sequence jobs that share a file.
* On each report: read it in full, commit that worker's files by explicit path with a message naming the job and its headline, push, and tell the author the finding in two or three plain sentences.
* After a wave: log spend, update the handoff note, regenerate derived records (maps, summaries), and put the next decision table to the author.
* When a checker fails a builder's work: spawn a correction builder with the checker's exact findings. When a correction would change a verified value: hold it as pending until the author approves it at a gate.

## 4. The anatomy of a brief and a report

* A brief has the same skeleton every time: a title naming the decision it serves; the rules that bind (plain language, tone, no vague time words, typographic rules for anything that may enter the output); the exact files the worker may write and nothing else; the inputs by path; the method in numbered steps; the checks the worker must run before finishing; the report's required contents.
* Row lists inside a brief are generated by script from the registers, never typed by hand.
* A brief for a checker adds: state the tolerance first; derive before you look; plant one wrong value; open the file under test last; edit nothing.
* A brief for a drafter adds: cite only register rows; keep a claims file beside the text; flag any value that awaits approval; where a question is open, take the recommended option and flag it; cite pages from the document on disk, never from a register.
* A report always contains: what was done and found, in plain language; every file changed; the records touched (often "none"); anything noticed outside the brief, as flags; and a worked wrong-value example, marked as an example, showing the check can fail.
* The worker is spawned with the brief's path and three sentences: who it is, where it works, what to report back.

## 5. The standard of evidence

* A number is usable only if it has a register row with a script, an output cell and data sources.
* A number is verified only when two independent routes agree: the builder's and a checker's own.
* Every data source is opened against its original: file present, hash matching, origin confirmed, and a sample of the values the pipeline uses checked against the source file itself.
* Every literature figure is cited to the page where the number is printed, from a file on disk, never from memory and never copied from a register. Second-hand figures are labelled as second-hand. Works with no file are cited as reported in the work that reports them, or marked as not seen.
* Every check states its tolerance before comparing, plants one deliberate wrong value, and reports the records it touched.
* A provenance map, generated by script, traces every fact in each output to its claim row, output cell, script, data row and original source, with the status of each link, so the whole chain can be inspected on one page and regenerated at any time.
* A verified value never changes without the author's written approval of a one-page digest of plain statements; the approval is recorded with the files' hashes.

## 6. The check and double-check chain

* **First route.** The builder computes or reads and writes the value into a register row with its script, cell and sources; status "self-checked".
* **Second route.** A blind checker on a different model derives each value by its own route (its own script over the committed data, or the document opened on disk) before reading the stated value. Pass raises the row to "independently verified"; fail names the right value.
* **Correction.** A fail spawns a correction builder with the checker's findings. The builder applies them and reports before and after. A corrected lower-tier row is marked "verified after correction"; a corrected verified value is not changed but marked "pending gate" with the new value in its notes.
* **Re-check where the stakes are high.** A correction that changes a result (an input error, a rebuilt dataset) gets its own blind checker, who reproduces the correction from the sources without reading the builder's script.
* **Gate.** The orchestrator writes a one-page digest of plain statements covering every pending value, with the rows and reports behind each. The author replies "approved" or names a statement. On approval the statuses change and the gates file records the digest's hash and the commit.
* **Logic check.** Numbers being right is not enough. A separate checker per output reads each section's points with their evidence and asks whether the evidence supports the point, whether the output contradicts itself or a sibling output, and whether any figure is quoted on a different basis from the one named.
* **Draft check.** After drafting, a checker reads every sentence against the registers and the documents on disk, opening the drafters' claims files only afterwards to find anything the prose carries that the files do not.
* **Consolidation.** A compiler turns a wave's reports into one document, and a script regenerates the provenance maps.

## 7. The order of work

* Register and verify the project's own results before any reading or writing about them.
* Read every source at page level, raising register rows from "abstract" or "record" to "read" with pages.
* Plan every section of every output before drafting: purpose in plain words, the points in order, the claim rows behind each point, the tables and figures with the file each is built from, the sources with read status and recency, the gaps, the open decisions, a word budget.
* Run a logic check per output.
* Run a provenance audit before the first draft: every source against its original; every one-route claim given a second route; every literature row at page level; the maps regenerated.
* Draft from the plans in parallel parts, each with its claims file. Check every sentence blind. Fix. Cut to the venue's stated limit by moving detail to supplementary material, never by dropping a number the plan requires.
* Gate: digest, approval, statuses updated, hashes recorded. Only then does the next stage rest on the result.

## 8. Steering

### 8.1 Who steers what
* The author sets the destination and the standard: which outputs, which question, which venues, what counts as verified, what tone, what pace. These are recorded as decisions and stand across sessions; the orchestrator reopens one only when new evidence demands it, and then as a decision row.
* The orchestrator steers the route: the order of work, the size of each wave, what runs in parallel, when a check is needed, when to stop and ask. It steers from the records, not from memory of the chat.
* Workers steer nothing. A worker that finds something outside its brief reports it and does not act on it.

### 8.2 The anchors
* The outline of each output is the destination in detail. Every job serves a section of an outline or the machinery under it; a job that serves none is questioned.
* The section plans translate the outline into evidence; their gaps lists are a backlog in themselves.
* The quality plan states the stages and what passes each gate; progress is measured against it, not against time.
* The decisions file is the authoritative record of direction; when the chat and the file disagree, the file wins and the chat is corrected.

### 8.3 Choosing the next job
* Dependency first: nothing rests on an unverified thing, so own results before reading, reading before plans, plans before logic checks, logic checks before the audit, the audit before drafting.
* Then what blocks the next gate: unverified key values, rows with one route, sources never opened, a changed finding awaiting a second route.
* Then what checkers flagged; a flag that touches a headline result jumps the queue.
* Then the gaps lists: plan gaps, literature without a file, figures without a script.
* The author's asks override all of the above, subject to the dependency rule: if an ask cannot be met without an unverified input, the orchestrator says so and proposes the verifying job first.
* The next-steps list the author can request at any time is this ordering written out with a cost per item, regenerated from the records.

### 8.4 Moving between the large scale and the small
* Four levels: strategy (outputs, question, venues); structure (outlines and plans); evidence (claims, sources, literature rows); detail (a page, a cell, a hash).
* Down on failure: a check that fails at one level sends the work one level down until the cause is found; a point unsupported leads to its claim row, the row to its output cell, the cell to its input, the input to its source.
* Up on completion: when a wave at one level passes its checks, the orchestrator writes the summary one level up (a digest, a consolidated report, a refreshed plan) before the next wave starts. The author sees digests and decision tables, not detail, unless they ask.
* The sizing script is the hinge between levels: it decides whether a wave is one job or ten, and what it costs.
* Parallel when independent, serial when shared; a check never runs beside the build it checks.

### 8.5 Holding direction
* A direction the author has set stands until they change it; a failed check against it is a decision row, not a reversal.
* Scope is the deliverable: a job is not widened because something interesting appeared; the interesting thing is a flag for the author.
* Disproportionate work is challenged at planning, in the decision table, with its cost; never abandoned mid-execution.
* Manual shortcuts are never offered as an escape from hard work.
* A question from the author gets an assessment; nothing changes until they ask for a change.
* When two workers disagree, the orchestrator does not pick a side; it spawns a third route or puts both to the author with the evidence.

### 8.6 Stopping and pausing
* A wave stops when its checks pass and its digest is written, or when a check changes a finding, which then goes to the author before anything is built on it.
* The project pauses on the author's word, on an ask that needs their input, or when the next job would cross a standing boundary.
* Every pause leaves a handoff note saying what is in progress, what is pending whom, and what the next decision table will contain.

## 9. Rules of engagement with the author

* Plain language in everything the author reads; numbers in tables, not prose; one idea per sentence.
* Every open item is a decision row; nothing is deferred with a vague time word.
* Standing approval for small reversible actions inside the project. An explicit ask before spending money, sending anything outside, publishing or tagging, deleting data, changing a standing decision, touching another repository, or changing a verified value.
* Every task that sends the author online carries its full URL in the same sentence, every time, including inside a decision row; for library items, the institution's title-search URL with the title filled in.
* Costs as a share of the author's allowance, calibrated once against the author's own meter and then against the spend log; never raw tokens.
* The orchestrator relays each worker's finding faithfully, including its own mistakes when a checker catches them.
* The author's objections become rules on the card the same day, in the same way as technical faults.

## 10. Rules for the outputs

* Tone: state what each method or author does, the access had and the assumptions made; no verdicts on others' shortcomings.
* Recency: reviews lead with recent work; older work appears for lineage.
* Basis: the dataset version, the method variant, the time frame and the unit basis are named at every figure; one ratio convention throughout; a number shared between outputs means the same thing in each.
* Length: the venue's stated limit, checked on the venue's own page; detail goes to supplementary material.
* Integrity: released datasets are frozen and never edited; a correction goes into a new hash-locked release with an errata entry; nothing copyrighted enters a public repository; the author's identity and personal details never enter a prompt, a payload or a sample value.

## 11. Failure modes to design against from the start

Each of these appeared in practice; each is now a rule in the briefs rather than a lesson.

* Register notes go stale when a builder changes an output: every builder lists the records it touches.
* Characterisations of a work written from its abstract are wrong or loose a substantial share of the time: nothing rests on a line until the work is read at page level.
* Readers cite the page of the discussion rather than the page where the number is printed: every reading brief says "the page where the number is printed".
* A plan written before a check carries stale statuses into drafting: plans are refreshed after every check that touches their rows.
* True numbers become wrong sentences through mixed bases (dataset versions, time frames, aggregation levels, unit bases): naming the basis at every figure is a header rule of every plan.
* Input data copied from an adjacent row or column survives every output-level check: the audit includes an input-plausibility pass (duplicates, sums, ranges) on every input table.
* The orchestrator makes slips of its own (a title typed from memory, a file saved under the wrong name): checkers never take the orchestrator's summary as an input; they re-derive from files.
* Cost estimates drift until calibrated: one calibration against the author's meter, then the spend log after every wave.
* Workers editing one file at the same time overwrite each other: shared files are edited in sequence or with a re-read-before-save rule, and the orchestrator commits by explicit path only.

## 12. Adopting it

* The cast, the records, the loop, the standard of evidence and the steering transfer unchanged to any project where numbers and citations must be right.
* The registers' columns are the only project-specific part; keep the ids, the status vocabulary (unverified, self-checked, independently verified, approved, withdrawn) and the two-route rule.
* The minimum viable version is one orchestrator, builders and checkers on different models, the four registers, decision tables, and gates with hashes. Everything else grows from those.
