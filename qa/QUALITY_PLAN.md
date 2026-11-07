# Quality plan: from analysis to publishable

Proposed 2026-11-07 for Murray's decision. Nothing in this plan has been run. It covers both papers, the correction notes and the supporting archive.

**The standard.** Murray cannot be wrong when this is published. Every method, data source, interpretation and calculation is checked and verified before submission. The sessions do the verification first and produce a short verification pack; Murray checks the verification (not the raw work), by sampling and by reading every high-risk item.

## 1. Why a verification programme and not a final read

The sessions' own record in this project, found by self-checks or by Murray's questions, not by an outside check:

| Kind of defect | Examples in this project |
|---|---|
| Stale state | The comparator rerun predated the dairy module, so improved figures read 45.7 instead of 53.6; the ten-diet table the same |
| Wrong cause or label | The drought allowance described as crop-only (it scales every yield); a fidelity target taken as 5.96 hectares (the whole footprint) where the food row is 2.71 |
| Mis-read source | Alexander's Australia 158 against the paper's 112.2 (different denominator) |
| Incomplete search | A source called missing that was on hand (Byron 2011); Figure 57 declared unreproducible after one workbook of 29 |
| Code fault | Monte Carlo draws overwrote release-set rows, so the improved-cell ranges started from 21.2 instead of 53.6 and were wrong |
| Assumed coverage | ABARE assumed to hold fruit, vegetable and egg tonnages (it does not) |
| Arithmetic slip | 87% typed where the computed value was 92% |

Seven kinds in a few weeks, each caught only because someone looked again. The base rate is not zero, so independent checking is needed, and the checks have to be able to fail.

## 2. What already exists to build on

Each release carries a hash of its model and regions (`results/releases.json`); `analysis/SOURCES.md` records input files with checksums; the constants have a source trace (`analysis/constants_audit/source_trace/`); `ERRATA.md` lists the corrections and was checked line by line; the 2011 thesis result is replicated (`baseline/`); the test suite fails if the generated results are stale; the comparison register marks each other-author figure as read or reported; `DISCUSSION.md` holds known limitations. The new analyses (`analysis/method_tests_2025/`, `analysis/paper_a/`) are scripts with outputs, but their README tables were typed by hand, and some constants are typed in the scripts. That is the weakest part and the first target.

## 3. The claim is the unit of verification

A **claims register** (`qa/claims_register.csv`, to be built) lists every number and statement that will appear in a paper: id, paper and section, the statement, the script and release that produce it, the data sources, the method source, the claims it depends on, its tier, its status and the verifier report that last checked it.

**Tiers.** A: headline results and any claim a reader would quote (checked by two independent routes). B: supporting numbers (one independent check). C: context and descriptions (self-check plus a read by the verifier).

**Status:** unverified, self-checked, independently verified, Murray-verified, withdrawn.

A **sources register** (`qa/sources_register.csv`) does the same for every dataset and every cited work: where it came from, date accessed, checksum or page, what was taken from it, and whether the figure was read from the source or reported by a secondary source. Anything marked reported is read at the source or removed before publication.

## 4. The layers of checking

| Layer | What is checked | Who and how | Passes when |
|---|---|---|---|
| 1 Data | Each source: origin, date, licence, transcription | A verifier re-fetches or re-reads the source blind to our extract and compares; a second source for each headline input where one exists (FAO against ABS did this once: 1997-98 production within 1.2%) | Source and extract agree within a stated tolerance; differences explained |
| 2 Method | Each method faithful to its source; each constant traced | A verifier reads the source and the implementation; fidelity check against the author's own figure where one exists; otherwise labelled "from the published description alone" | Reproduces the author's figure, or the gap is explained, or the label is on |
| 3 Calculation | Each headline number | A second implementation written from the brief by a worker that has not seen the first (for example HALF for Australia from raw FAO data; the model evaluator against the original workbook) | The two agree to a stated tolerance |
| 4 Interpretation | What each result means | A reader is given only the table and asked what it supports; the text is compared with that reading; over-claims and wrong causes are flagged (check the cause, not the number) | Every sentence is supported by a table; every cause names the file read |
| 5 Literature | Every cited figure, quote and characterisation of other authors | A literature checker reads the primary source and the sentence | Source page and wording confirm the sentence; the critique of each method is fair to its authors |
| 6 Reproduction | The whole chain | A clean-room worker clones the tagged repository, rebuilds the releases, regenerates every table and figure, and diffs against what the manuscript uses | No difference, or each difference explained |
| 7 Uncertainty | Monte Carlo design and ranges | Independent rerun with another seed; assertion that the base of every draw equals the release; check that each range has a source | Ranges agree within sampling error; the base assertion passes |
| 8 Editorial | Wording against evidence ("corrected", "published", footnotes, limits) | Verifier text-to-register audit: every number in the manuscript maps to a register row | No orphan number; no number without a passing row |

A check that cannot fail does not count. Every brief states what result would make the check go red and how it was confirmed capable of going red.

## 5. Gates

The order is fixed. A paper does not pass a gate while any Tier A claim at that gate is open.

0. **Freeze:** the release, the method modules and the data set for the paper are locked and hashed (the method stays frozen during the data refresh).
1. **Sources verified** (layer 1 and 5 for every source the paper uses).
2. **Methods and calculations verified** (layers 2, 3 and 7).
3. **Interpretation verified** (layer 4).
4. **Manuscript audit** (layer 8: every number maps to the register).
5. **Clean-room reproduction** (layer 6).
6. **Murray's verification** of the pack, then the freeze, the tag and the archive (Zenodo stays on hold until Murray releases it).

## 6. Keeping quality through production, not only at the end

* **No number is typed.** Manuscript and README tables are generated from `results/` and the analysis outputs by script, with the release id and commit beside them (the existing rule, extended to the new analyses; the typed README tables are replaced by generated ones).
* **Numbers lint.** A script lists every number in the outlines, READMEs and manuscripts and flags any that is not in a current generated output, which would have caught the stale improved figures.
* **Change control.** Each register row lists its dependencies. A change to a release, module, source or script marks every dependent claim "unverified" and the orchestrator reports which. A correction is itself verified before it is propagated.
* **Blind verification.** A verifier receives the requirement and the recipe, never the earlier finding, and is a different model from the builder.
* **Stopping rule.** Before another verification round the orchestrator writes "if this comes back the other way I will do X differently"; with no X, the rounds stop.
* **Defect tally.** Every defect a check catches is logged with its layer and kind; the tally calibrates how much checking each kind of claim needs.
* **Known weaknesses recorded at once** in `DISCUSSION.md`, the existing rule.
* **Seat hygiene.** The plan, registers and decisions live in files, so a long session or a restart loses nothing.

## 7. What Murray checks

A **verification pack** per gate: for each Tier A claim one line (statement, value, how it was produced, the two routes that agree, the verifier's verdict, anything left open) and a list of open items. Murray reads every Tier A line and every item marked cannot-determine or interpretation, samples Tier B, and signs off the gate. He is not asked to re-derive.

## 8. Limits, stated plainly

* Independent sessions reduce the chance of an error reaching print; they do not remove it. Checks by AI sessions are not a substitute for expert judgement on what a result means.
* Some items need people: whether the critique of each other method is fair (the authors or an expert in each method could check the reconstructions, in particular Alexander et al. on HALF and Cassidy et al.); whether the choice of methods is defensible to the journal's readers; whether the interpretation of Australian results suits planners. An external reader before submission is recommended for the methods paper.
* Reconstructions are labelled as reconstructions in the text; a method checked only against its description is never described as reproduced.
* If a Tier A claim cannot be verified two ways, it is either downgraded in the text or removed.

## 9. Decisions for Murray

The decisions are in `qa/DECISIONS.md` as numbered rows with a recommendation, confidence, cost and reason. The four listed below are rows 4, 5, 6 and the standing order of the papers.


1. **Tiering and depth:** A, B, C as above, or a different split.
2. **External readers:** who, and whether to contact the authors of HALF and people-per-hectare to check the reconstructions.
3. **Whether the registers are published** as supplementary material (recommended: yes for the reproducibility part, which is part of the quality claim).
4. **The order of the gates for the two papers:** the methods paper first, as planned, with the model material verified once for both.
