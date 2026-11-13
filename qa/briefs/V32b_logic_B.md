# Checker brief V32b: logic and consistency of Paper B (methods) (decision 77)

You are a blind checker of argument, not of arithmetic: the numbers have been checked (V30, V31); your job is whether the facts support what the paper means to say with them. Rules: plain language; no time words; no em dashes; decision 33. No git; no subagents; no network. Write only `qa/reports/V32b_logic_B.md`. Edit nothing else.

Inputs: `papers/B_methods/SECTION_SCOPE.md` (every section block: purpose, content list, evidence table, sources table), papers/B_methods/OUTLINE.md, papers/B_methods/SECTION7_DRAFT.md, `qa/claims_register.csv` (read each cited claim's statement, value, unit, release and status as it now stands), `qa/literature_register.csv` (each cited row's what_taken and notes), `qa/DECISIONS.md`, and `papers/A_results/SECTION_SCOPE.md` for the cross-paper check.

For each section, in order, and for each numbered point in its content list:
1. Support: does each claim or literature row cited for the point actually say what the point needs? Say supported / partly (what is missing) / not supported (why), quoting the claim statement or register line that falls short. Watch for: a figure from one release or method quoted as if from another (published versus corrected versus improved; short term versus long term; national versus zone sum); a second-hand figure used as primary; a simulated or projected figure read as observed; a range that is a spread across cases read as uncertainty; a rounded figure that would round differently; a point that relies on a row whose status is unverified or withdrawn.
2. Consistency: does the point contradict any other point in this paper (list the pair and the two figures or statements), or any decision in DECISIONS.md?
3. Cross-paper: where the same figure, method or finding appears in the other paper's scope, do the two agree (value, release, wording of what it means)? List every disagreement.
4. Logic: does the section's purpose follow from its points (name any gap in the chain, any conclusion stronger than the evidence, any point that is asserted without evidence listed)?

Then: a table (section; points; supported / partly / not; contradictions; cross-paper disagreements); the ten most important problems in order, each with the fix you recommend and whether it is a wording change, a register change or a new computation; the register rows touched (none); and "Wrong-value check:" with one deliberate example of a point you would wrongly pass if you read only the claim id and not its statement, marked as an example.
