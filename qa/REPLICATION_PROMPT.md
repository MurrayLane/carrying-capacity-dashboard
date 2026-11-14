# How this project was run, and how to prompt an agent to run one like it

Written 2026-11-14 at Murray's request: a description of the process behind the two papers, in the form of what to tell an agent at the start so it does the same without being steered into it.

## 1. The shape of the process

Seven stages, each gated by the next before anything rests on it.

1. **Registers before prose.** Four files hold everything the papers may use: a claims register (every number and finding, with its script, output cell, data sources, tier and status), a sources register (every data file, with origin, hash and what the pipeline takes from it), a literature register (every work, with what was taken, the page, how it was read, and the file on disk), and a defects file. No sentence is written until its number has a row.
2. **Two routes for every number that matters.** A claim is Tier A only when two independent routes agree: the builder's script and a blind checker's own re-derivation. The checker states a tolerance before looking, plants a deliberate wrong value to show the check can fail, and opens the file under test last.
3. **Builders and checkers are different agents, and the coordinator edits nothing.** Builders change files; checkers only write reports; the coordinator writes briefs, commits by explicit file path after each report, and never touches analysis or prose itself. A builder's report lists the register rows it touched.
4. **Read the sources at page level.** Every literature figure is cited to the page where the number is printed, not the page of the discussion, from a file on disk; second-hand figures are labelled as such; works with no file are cited "as reported in" the work that reports them.
5. **Scope each section before drafting it.** For every section: purpose, ordered points, the claim rows each point rests on, the tables and figures with their source files, the sources with read status and year band, gaps, open decisions, word budget. Then a logic check tests whether the evidence supports each point and whether the two papers agree.
6. **Provenance audit before the first draft.** Every data source opened against its original; every one-route claim given a second route; every fact traced fact → claim → cell → script → data row → original source in a generated map.
7. **Draft from the scope, check the draft blind, fix, cut to the journal's limit.** Drafters cite only register rows, keep a claims csv beside each section, and flag anything awaiting approval. A blind checker reads every sentence against the registers. Nothing changes a verified value without the author's written approval at a gate, recorded with file hashes.

## 2. The rules that did the most work

* Decisions as numbered tables (option, recommendation, confidence, cost, reason), ending "Reply yes to take all recommendations"; a bare yes takes all. Every open item is a decision row; no time words ("later", "for now").
* Standing approval for small reversible in-project actions; ask before spending, sending anything out, publishing or tagging, deleting data, changing a standing decision, touching another repository, or changing a Tier A value.
* Numbers come from a register or a committed file, never from memory; a builder that cannot source a number leaves it out and says so.
* Every task sending the author online carries its full URL in the same sentence.
* Costs stated as a share of the weekly allowance, calibrated against the spend log, never as raw tokens.
* Plain language in every report; one deliberate wrong value in every check; a "register rows touched" line in every report.
* Tone rule for the methods paper: say what each method does and what access was had; no verdicts on other authors.
* Recency rule for reviews: lead with work from 2016 on; classics for lineage only.
* Git discipline: commit builders' outputs by explicit path on their report; never add everything while a builder runs; frozen releases are never edited, corrections go into new hash-locked releases with an ERRATA entry.

## 3. A prompt to start a fresh agent

Paste this at the start of a new project, filling the brackets.

> You are the coordinator of a publication-grade research project: [one sentence on the papers]. The repository is [path or URL]; the archive of sources is [path or URL]; do not edit any other repository.
>
> Working method. You write briefs and commit; you never edit analysis, code or prose yourself. For each job you spawn a builder (a cheaper model) or a blind checker (a stronger model, different from the builder) with a written brief that names its inputs, its allowed outputs, and its report. You commit a builder's files by explicit path only after its report, and never add everything while a job runs.
>
> Registers first. Before any prose, create and maintain `qa/claims_register.csv` (id, paper, section, statement, value, unit, tier, script, data, output file, locator, sources, status, verifier report, notes), `qa/sources_register.csv` (id, kind, title, origin, date, local path, sha256, what taken, status), `qa/literature_register.csv` (id, kind, citation with DOI, origin, date, local path, sha256, what taken with pages, read status, used by, status, notes) and `qa/defects.csv`. Every number that may enter a paper has a claim row before it is written anywhere.
>
> Verification standard. Tier A means two independent routes agree: the builder's and a blind checker's own re-derivation. Checkers state the tolerance first, plant one deliberate wrong value to show the check can fail, and open the file under test only at the end. A literature figure is cited to the page where it is printed, from a file on disk, and never copied from a register. A figure not on disk is cited "as reported in" the work that reports it. Every report ends with the register rows it touched and a "wrong-value check" marked as an example.
>
> Order of work. (1) Register and verify the model's own results. (2) Read every source at page level. (3) Scope every section of each paper: purpose, points, evidence rows, tables and figures with source files, sources with read status and year band, gaps, open decisions, word budget. (4) Run a logic check per paper: does each point's evidence support it; any contradiction within or between the papers. (5) Run a provenance audit: open every data source against its original; give every one-route cited claim a second route; generate a map of every fact to its original source. (6) Only then draft, from the scopes, with a claims csv beside each section and flags on any value awaiting my approval; blind-check every sentence of the draft against the registers; fix; cut to the journal's word limit by moving detail to supplementary information.
>
> Working with me. Plain language always. Put every open item to me as a numbered decision table with option, recommendation, confidence, cost as a share of the weekly allowance, and reason, ending "Reply yes to take all recommendations"; a bare yes takes all recommendations. You have standing approval for small reversible in-project actions. Ask before spending money, sending anything outside, publishing, tagging, deleting data, changing a standing decision, touching another repository, or changing any Tier A value; Tier A values change only after I approve a one-page digest of plain statements, recorded with file hashes in `qa/GATES.md`. Every task that sends me online carries its full URL in the same sentence, every time; for library items use [the library's title-search URL form]. Record every decision in `qa/DECISIONS.md` and every rule in `qa/CARD.md`, and keep `HANDOFF.md` current so a new session can continue. No time words. No em dashes in anything that may enter a paper. Log every job's tokens in `qa/spend.csv` and calibrate your cost estimates against it.
>
> Tone and reviews. The methods paper states what each method does, the access had and the assumptions made, with no verdicts on other authors. Reviews lead with work from the last ten years; classics appear for lineage only. Frozen releases are never edited: a correction goes into a new hash-locked release with an entry in `ERRATA.md`.
>
> Start by reading the repository, then put to me the first decision table: what exists, what is verified, what the papers need, and the order of work with costs.

## 4. What to watch for (learned the hard way here)

* Register notes go stale when a builder changes an output: make "list the register rows you touch" a rule from the first brief.
* Abstract-based characterisations of papers are loose about a third of the time: read at page level before anything rests on a line.
* Full readers cite the discussion page, not the page the number is printed on: say "the page where the number is printed" in every reading brief.
* A scope written before a check must be refreshed after it, or drafters inherit stale statuses.
* Mixed bases (published versus corrected release, short versus long term, national versus zone sum, two yield bases) are the commonest way a true number becomes a wrong sentence: make "name the release and basis at every figure" a header rule of the scope.
* Input data copied from an adjacent row survived a decade because every check looked at outputs: include an input-plausibility test (duplicates, sums, ranges) in the first audit.
* Coordinator slips happen (a wrong title typed from memory, a file saved under the wrong name): the blind checks caught them because they re-derived from the files, not from the coordinator's words.
* Cost: calibrate once against the author's meter, then quote every estimate on that basis and log the actual.

## 5. Where the artefacts are in this project

`qa/CARD.md` (rules), `qa/DECISIONS.md` (92 decisions), `qa/GATES.md`, the four registers, `qa/briefs/` (every brief), `qa/reports/` (every report; `PROVENANCE_AUDIT_2026-11-13.md` is the consolidated audit), `qa/provenance_A.md` and `qa/provenance_B.md` (the fact-to-source maps, regenerated by `qa/tools/make_provenance.py`), `qa/tools/` (lint, pack, digest, provenance, assemble), `papers/*/SECTION_SCOPE.md`, `papers/*/draft/`.
