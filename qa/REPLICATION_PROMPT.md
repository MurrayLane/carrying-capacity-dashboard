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

## 9. How the pieces interact, step by step

### 9.1 A single job, from need to record
* **Trigger.** A need surfaces from one of four places: the author asks; a checker's report flags something; the orchestrator's sizing script finds rows without a route; or a decision in the decisions file names a job.
* **Sizing.** The orchestrator runs a short script over the registers to count what the job touches (rows, sources, papers) and converts that to a cost on the calibrated basis. It never estimates from feel.
* **Decision.** The job goes to the author as one row of a decision table unless it is small, reversible and inside the project, in which case standing approval covers it and the author hears of it in the report.
* **Brief.** One file per job in the briefs folder, written by the orchestrator, with the same skeleton every time: title with the decision number it serves; the rules that bind (plain language, no time words, no em dashes, tone rule); the exact files it may write and nothing else; the inputs by path; the method in numbered steps; the checks it must run before finishing; the report's required contents (findings, every file changed, the register rows touched, a wrong-value example marked as an example). Row lists are generated by script into the brief so no id is typed by hand.
* **Spawn.** The worker gets the brief's path and three sentences: who it is, where it works, what to report. Independent jobs are spawned in one go; jobs sharing a file run in sequence or are told to re-read the file from disk before saving and to change only their rows.
* **Work.** The worker reads the brief, does the work, runs its own checks, writes its outputs and its report.
* **Report.** The worker's hand-back is read in full. The orchestrator commits the named files by explicit path with a message naming the job and its headline, pushes, and tells the author the finding in two or three plain sentences.
* **Record.** The report file sits in the reports folder under the job id; the spend log gets a row; the handoff note is updated at the end of the wave; the decisions file links the job to the decision it served.

### 9.2 The check and double-check chain
* **First route.** The builder computes or reads and writes the value into a register row with its script, cell and sources, status "self-checked".
* **Second route.** A blind checker, on a different model, is given the row ids and told to derive each value by its own route (its own script over the committed data, or the paper opened on disk) before reading the row's stated value. It states its tolerance first and plants a wrong value to show the comparison can fail. Pass raises the row to "independently verified"; fail names the right value.
* **Correction.** A fail spawns a correction builder with the checker's exact findings. The builder applies them and reports before and after. A corrected Tier B or C row becomes "independently verified after correction (job)"; a corrected Tier A value is not changed in the register but marked "pending gate" with the new value in its notes.
* **Re-check where the stakes are high.** A correction that changes a result (an input error, a release rebuilt) gets its own blind checker, who reproduces the correction from the sources without reading the builder's script, cell by cell.
* **Gate.** The orchestrator writes a one-page digest of plain statements covering every pending value, with the rows and reports behind each. The author replies "approved" or names a statement. On approval the register statuses change to "approved (gate n)" and the gates file records the digest's hash and the commit.
* **Logic check.** Numbers being right is not enough: a separate checker per paper reads each section's points with their evidence and asks whether the evidence supports the point, whether the paper contradicts itself or the other paper, and whether any figure is quoted on a different basis from the one named.
* **Draft check.** After drafting, a checker reads every sentence against the registers and the papers on disk, with the drafters' claims files opened only afterwards to find anything the prose carries that the files do not.
* **Consolidation.** A compiler turns the wave's reports into one document per audit, and a script regenerates the provenance maps, so the author can see the whole chain without opening fourteen files.

### 9.3 Iteration: how the work improves between waves
* Each wave ends with a decision table that lists what the checks found, what was corrected without asking (small, in-project), and what needs the author's word (a changed finding, a Tier A value, a new direction).
* The author's reply is recorded verbatim in the decisions file, one numbered row per decision, with the jobs that carry it out named beside it.
* A rule that would have prevented a fault is added to the rules card the same day, with the fault that prompted it. Later briefs cite the rule by its wording; the rules card is read by the orchestrator at the start of every wave.
* Scopes, registers and maps are refreshed after any job that changes what they describe, before the next job reads them; a job that reads a stale scope inherits its errors.
* Estimates are compared with the spend log after each wave and the basis adjusted; the author is told when an estimate was wrong and by how much.
* The author's own objections ("that is a lot of numbers", "what does it mean", "give me the URL") become rules in the same way as technical faults.

### 9.4 Record keeping, moment to moment
* Every file a worker writes is committed by explicit path immediately after its report, never earlier and never with other workers' unfinished files. The commit message names the job and its headline finding.
* Every brief and report is a file under the job id, so a finding can be traced to the brief that asked for it and the worker that found it.
* Every register edit is attributed in the row's notes with the job id and date ("B89 (2026-11-13): corrected after V31c").
* Every decision carries the author's words and the date; every rule carries the author's words and the fault behind it.
* Every verified value carries the report that verified it and, after a gate, the gate number.
* The handoff note is updated at the end of every wave and says what is in progress, what is pending the author, and the cost basis, so a fresh session can continue without the chat history.
* The spend log carries one row per job (date, job, model, tokens, outcome); the orchestrator's own tokens are not logged, which is stated wherever the log is summarised.
* Nothing is deleted: a withdrawn claim keeps its row with status "withdrawn" and the reason; a superseded decision is marked as replaced by the later one; a correction to a frozen release is a new release and an errata entry, not an edit.

### 9.5 A worked example from this project
* A logic checker (V32a) noticed that one region's 2011 population equalled its neighbour's to the person.
* The orchestrator confirmed the duplicate in the data file by a one-line command and put it to the author as the first row of a decision table, with the recommendation to trace, correct, rerun and check, and the cost.
* On "yes", a brief (B90) sent an Opus builder to find the true figure from the registered ABS source, correct it in a new release (the frozen one untouched), log an errata entry, rerun the dependent analyses and list every claim row that moved, Tier A separated and left unchanged.
* The builder found the figure, found that the copy came from the author's original workbook, found a second copy of the same kind (logged, not corrected, because the decision covered one region), and listed seven Tier A counts that move by one.
* A blind checker (V33) rebuilt the figure from the ABS SA2 populations by its own allocation and re-evaluated both new releases cell by cell: zero mismatches.
* A register builder (B95) applied the Tier B and C changes, marked the seven Tier A rows "pending gate 4" with their new values, and updated the defects file.
* The drafters used the new values flagged "[gate 4]" in their claims files; the draft checkers verified them against the pending notes.
* The gate 4 digest put the change to the author in two plain statements with a decision row for the second copy. The register values change only on the author's "approved".
* Every step above is a file: the two reports, the brief, the errata entry, the defect rows, the register notes, the digest, the decision rows, and the commits that carry them.

## 10. Steering: how direction is set and how the next job is chosen

### 10.1 Who steers what
* The author sets the destination and the standard: which papers, which question, which journals, what counts as verified, what tone, what pace. These are recorded as decisions and stand across sessions; the orchestrator never reopens them unless new evidence demands it, and then only as a decision row.
* The orchestrator steers the route: the order of work, the size of each wave, which jobs run in parallel, when a check is needed, when to stop and ask. It does this from the records, not from memory of the chat.
* Workers steer nothing. A worker that finds something outside its brief reports it; it does not act on it.

### 10.2 The anchor documents
* **The outline of each paper** (sections, argument, figures) is the destination in detail. Every job serves a section of an outline or the machinery under it; a job that serves none is questioned.
* **The section scopes** translate the outline into evidence: each point names the rows it needs. A scope's gaps list is a backlog in itself.
* **The readiness or quality plan** states the stages and what passes each gate. Progress is measured against it, not against time.
* **The decisions file** is the authoritative record of direction; when the chat and the file disagree, the file wins and the chat is corrected.

### 10.3 How "what next" is decided
* **Dependency first.** Nothing rests on an unverified thing. The order is fixed by what each stage needs: own results before reading, reading before scopes, scopes before logic checks, logic checks before the audit, the audit before drafting, drafting before cutting. A job out of order creates rework.
* **Then what blocks a gate.** Within a stage, the jobs that stand between the project and the next approval come first: unverified Tier A rows, rows with one route, sources never opened, a changed finding awaiting a second route.
* **Then what checkers flagged.** Every check report ends with flags beyond its brief; the orchestrator collects them into the defects file and the next decision table. A flag that touches a headline result jumps the queue.
* **Then the gaps lists.** Scope gaps, literature rows without a file, figures without a script.
* **Then the author's asks**, which override all of the above when they arrive, subject to the dependency rule: if the ask cannot be met without an unverified input, the orchestrator says so and proposes the verifying job first.
* The "next steps" list the author can ask for at any time is this ordering written out with a cost per item; it is regenerated from the records, not carried in the orchestrator's head.

### 10.4 Moving between the large scale and the small
* **Four levels.** Strategy (the papers, the question, the journals); structure (outlines and scopes); evidence (claims, sources, literature rows); detail (a page number, a cell, a hash).
* **Down on failure.** A check that fails at one level sends the work one level down until the cause is found: a logic check that finds a point unsupported leads to the claim row; the claim row leads to the output cell; the cell leads to the input data; the input leads to the source. The North East Victoria population went all four levels down in one day.
* **Up on completion.** When a wave at one level completes with its checks passed, the orchestrator writes the summary one level up (a digest, a consolidated report, a refreshed scope) before starting the next wave. The author is never shown the detail level unless they ask; they see digests and decision tables.
* **The sizing script is the hinge.** Before each wave the orchestrator counts, by script, how many rows, sources or sections the wave touches and at what status. That count decides whether the wave is one job or ten, and what it costs.
* **Parallel when independent, serial when shared.** Jobs that touch different files run together; jobs that touch the same register run in sequence or with the re-read-before-save rule; a check never runs in parallel with the build it checks.

### 10.5 Keeping direction without drifting
* A direction the author has set stands until the author changes it; a failed check against that direction is a decision row, not a reversal.
* Scope is the deliverable. The orchestrator does not widen a job because something interesting appeared; it reports the interesting thing as a flag and lets the author decide.
* Disproportionate work is challenged at planning, in the decision table, with the cost; never abandoned mid-execution.
* "Do it manually instead" is never offered as an escape from hard work; difficulty is the point.
* When the author asks a question rather than for a change, the answer is an assessment, and nothing is changed until they ask.
* When two workers' findings disagree, the orchestrator does not pick one; it spawns a third route or puts both to the author with the evidence.

### 10.6 Stopping and pausing
* A wave stops when its checks have passed and its digest is written, or when a check fails in a way that changes a finding, in which case the finding goes to the author before anything else is built on it.
* The project pauses on the author's word, on an ask that needs their input, or when the next job would cross a standing boundary (money, publication, deletion, a Tier A value, another repository).
* On every pause the handoff note says exactly what is in progress, what is pending whom, and what the next decision table will contain, so a fresh session can pick up without the chat.

### 10.7 What this looked like here, in order
* Stage 1 (own results): the model rebuilt, its releases frozen and hash-locked, its headline figures given two routes, gate 1 and gate 2.
* Stage 2 (reading): the archive filled, every cited work read at page level, the author sent one consolidated list of links for what only a person could fetch.
* Stage 3 (structure): both papers scoped section by section, with word budgets and gaps.
* Stage 4 (logic): both scopes checked for support and consistency; the three findings that changed a result came from this stage and the next.
* Stage 5 (audit): every source against its original; every one-route claim given a second route; the provenance maps; the register brought true.
* Stage 6 (drafting): six drafters in parallel from the refreshed scopes; two blind checks; fixes; cut to the journals' limits; gate 4 digest written.
* Each stage ended with a decision table; each decision is a numbered row; 92 so far.

## 11. Adopting it elsewhere

* The cast, the records, the loop and the standard of evidence transfer unchanged to any project where numbers and citations must be right: empirical papers, systematic reviews, data releases, audits.
* The registers' columns are the only project-specific part; keep the ids, the status vocabulary (unverified, self-checked, independently verified, approved, withdrawn) and the two-route rule.
* The minimum viable version is: one orchestrator, builders and checkers on different models, the four registers, decision tables, and gates with hashes. Everything else here grew from those.
