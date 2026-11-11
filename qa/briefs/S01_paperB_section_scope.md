# Scoping brief S01: Paper B (methods), every section scoped, no drafting

Murray's instruction (2026-11-11): no drafting of either paper; scope each section. Rules: plain language; no em dashes; no time words; decision 33. No git; no subagents; no network. Write only `papers/B_methods/SECTION_SCOPE.md`.

Inputs: `papers/B_methods/OUTLINE.md` (as labelled by B72), `papers/B_methods/SECTION7_DRAFT.md`, `qa/DECISIONS.md` (all decisions bind; 40 to 54 are the latest), `qa/reports/B61_lit_review_scope.md`, `qa/reports/B63_recency_sweep.md`, `qa/reports/B68_reader_flags.md`, `qa/reports/B70_paperA_thin_points.md` (for the division of labour with Paper A), `qa/literature_register.csv`, `qa/claims_register.csv`, `analysis/method_tests_2025/README.md`, `analysis/comparators_2025/README.md`, `analysis/sensitivity_2025/README.md`, `analysis/nutrition_lp_2025/README.md`, `results/README.md`, `HANDOFF.md`.

For each of the nine sections of the outline, in order, write a scope block with these headings:
1. **Purpose and argument** (three to six sentences in plain language: what the section says and why it is there).
2. **Content list** (numbered: the points in the order they will be made; each point one or two sentences).
3. **Evidence** (a table: point number; the claim ids from `qa/claims_register.csv` or the csv cell it rests on; the tier and whether two routes agree; or "none needed").
4. **Tables and figures** (each with the csv or results file it is built from, and whether a script exists).
5. **Sources to cite** (a table: register id; Author Year; read status from the register; what it is cited for; year band before 2016 / 2016 to 2019 / 2020 to 2026). Then one line with the section's year mix as counts.
6. **Gaps** (what the section needs that no read source or claim row supplies, each with the kind of source or job that would fill it).
7. **Open decisions** (the decision rows that touch the section, by number, and any new question for Murray, written as a decision row: option, recommendation, confidence, reason).
8. **Word budget** (a number, with the reasoning) and **dependencies** (what must be settled or written first).

Then a closing part: a whole-paper table (section; word budget; sources count; year mix; gaps count; open decisions); the target journal question (outline "Decisions still open" item 1) with a recommendation; the register rows touched (none); and "Wrong-value check:" with one deliberate example of a claim id attached to the wrong point, marked as an example.

Where B74 (government documents, running now) will add rows, say "pending B74" rather than guessing. Do not write any paper prose beyond the purpose sentences.
