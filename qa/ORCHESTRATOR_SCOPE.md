# An orchestrator for this project: scope

Proposed 2026-11-07 for Murray's decision. Nothing here has been built. It uses the patterns Murray's other project's orchestrator already follows (one seat, briefs as files, independent verifiers, decisions as numbered rows), changed for publication-grade work (`qa/QUALITY_PLAN.md`).

## 1. Purpose and non-goals

**Purpose.** Hold the plan and the registers, write briefs, spawn and review workers, run the gates of the quality plan, and tell Murray in plain language what is verified, what is open and what needs his decision.

**It does not:** decide what a result means, send the correction notes, choose a journal, publish, release the archive, or approve its own work. Those are Murray's. It proposes; a change of direction waits for his yes.

## 2. What differs from the other project's orchestrator

| | Other project (a product, pre-launch) | This project (publication) |
|---|---|---|
| Failure that matters | Shipping something broken | A published claim that is wrong |
| Output | Code and operations | Numbers, text, citations, a frozen archive |
| Evidence standard | Tests and measurements, then decide | Every claim traced and independently verified before submission |
| Human check | Murray reviews decisions | Murray checks a verification pack, then signs off each gate |
| State | Code repository and session notes | The claims and sources registers, the decisions file, the defect tally |

## 3. Roles and models

| Role | Does | Default model | Tools |
|---|---|---|---|
| Orchestrator | Plan, briefs, review, register, gates, plain-language reports | Fable (judgement; small token use because it reads reports, not data) | Read, search, spawn workers, messaging; no editing of analysis files |
| Builder | Scripts, extraction, tables, figures, drafts from a brief | Sonnet | Edit and run within the brief's fence |
| Verifier | Independent check of one requirement; read-only; blind to the earlier finding | Opus (a different model from the builder) | Read-only, scratch space only |
| Literature checker | Reads primary sources; confirms figures, quotes, characterisations | Opus | Read and web fetch |
| Reproducer | Clean-room rebuild from the tagged repository, diff against the manuscript's tables | Sonnet, verified by a diff script | Run in a scratch checkout |
| Red-team reader | Reads only the tables and states what they support; compared with the text | Opus | Read-only |

The mapping is a hypothesis to be tested by the defect tally (what each model's work needs corrected by the independent check), not a fixed rule. Effort level is set per role in the brief.

## 4. State, held in files

```
qa/claims_register.csv     every number and statement: id, paper, section, statement, script, release, sources, method source, dependencies, tier, status, verifier report, last verified commit
qa/sources_register.csv    every dataset and every cited work: origin, date accessed, checksum or page, what was taken, read or reported, status
qa/decisions.md            numbered decisions awaiting Murray, and the standing decisions (2025-only for the methods paper, corrected values, scale curve in Paper A, two papers only, no reproduction gate)
qa/defects.csv             every defect a check caught: layer, kind, what, who found it, fixed in
qa/briefs/                 worker briefs
qa/reports/                worker reports and verification packs
qa/spend.csv               per job: model, effort, tokens, notional cost, outcome
```

The plan documents already in the repository (`PUBLICATIONS.md`, the two outlines, `ERRATA.md`, `DISCUSSION.md`, `HANDOFF.md`) stay the source for content; `qa/` holds only the verification state.

## 5. Briefs and reports

Every brief has: the **fixed decisions** block (copied from `qa/decisions.md`, so no worker reopens them); the one requirement; the inputs and where they are; what the worker may and may not touch; no subagents; the **check must be able to fail** statement; the report format (holds, does not hold, cannot determine, and the evidence paths); and the budget with a stop line. Verifier briefs contain the requirement and the recipe only.

## 6. The loop for one wave of verification

1. The orchestrator picks the next wave from the dependency order, lists the register rows in it and their tiers.
2. It writes briefs and spawns builders (if work is needed) and verifiers (blind).
3. It reads the reports against its own view (what the results mean, what they constrain, what risk they add, whether the chain should continue), not duplicating the verifier's checks.
4. Defects go to `qa/defects.csv`; fixes go back to a builder; the fix is re-verified by a verifier who did not see the defect.
5. It marks register rows, invalidates dependents of anything changed, and writes the verification pack for Murray.
6. Murray signs off the gate or sends it back.

**Waves, in dependency order.** (1) Data sources. (2) The model baseline and the 2011 replication. (3) The corrections and improvements as modules. (4) The seven method tests. (5) The design choices and the Monte Carlo ranges. (6) Paper A's analyses. (7) The register of other authors' estimates and every literature claim. (8) The manuscripts against the register. (9) Clean-room reproduction.

## 7. Controls the orchestrator runs

Numbers lint and stale-document check on every commit; change control with invalidation notices; blind verification; the stopping rule; the defect tally; spend logged per job from the session records; seat rotation: at a context threshold the orchestrator writes its state to files and a new seat resumes from them.

## 8. Build plan, in sizes (quick, small, session-size)

| Phase | What | Size |
|---|---|---|
| P0 | Create `qa/`, the register schemas and `decisions.md`; seed the registers from existing artefacts (`releases.json`, `SOURCES.md`, `ERRATA.md`, the source trace, the comparison register, the outlines' headline numbers) | session-size, mostly Sonnet builders |
| P1 | The numbers lint, the stale-document check and the clean-room reproduction script; replace the typed README tables with generated ones | small |
| P2 | The brief and report templates; a first verification wave on the cheapest, highest-value target (the headline numbers of the methods paper) to calibrate cost and the defect rate | small |
| P3 | Waves 1 to 9 in order, with Murray's sign-off at each gate | several session-size passes; recalibrated after the first wave |
| P4 | Orchestrator seat set-up: where it runs, tool restrictions, seat rotation | quick, after Murray decides the seat |

The allowance use of each phase is not known and is measured, not guessed: P2 produces the first figure and the later phases are re-estimated from it.

## 9. Cost and context

The orchestrator's cost is dominated by its context, which is re-read every turn. Keep it small: it reads reports and registers, never raw data; state lives in files; the seat rotates at a threshold. Builders and verifiers run short, bounded jobs with short contexts. The weekly allowance is shared with Murray's other projects, so every wave states its expected share before it starts.

## 10. Decisions for Murray

1. **The seat:** a cloud session in this repository, or a session on Murray's machine; and its model (Fable proposed).
2. **Tool restriction for the seat** (editing denied), or rules only.
3. **Verifier model:** Opus proposed; the defect tally decides after the first wave.
4. **Tiering** and **external readers** (the quality plan's decisions 1 and 2).
5. **Go-ahead for P0 and P1,** which change no results.

## 11. Relationship to the other orchestrator

A separate seat with its own rules; the patterns are shared, the rules are not (the other project's rules include product, deployment and spending rules that do not apply here). Observations from reading its rules were prepared for it on 2026-11-07; they are not held in this repository, as they concern the other project's internals.
