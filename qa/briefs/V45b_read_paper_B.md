# Checker brief V45b: blind read of the revised Paper B draft

You are a blind reader of the whole revised Paper B (`papers/B_methods/draft/paper_B_draft1.md`, `supplementary.md`, `highlights.md`, `references.md`). Plain language; no em dashes; no time words. No git; no subagents; no network. Write only `qa/reports/V45b_read_paper_B.md`.

Read the draft before any report. Then, for every number in the main text, the abstract, the highlights and the supplement:
1. Find its row in the section claims csvs (`B_s01-03_claims.csv`, `B_s04-05_claims.csv`, `B_s06-09_claims.csv`, `supplementary_claims.csv`) and the file or report the row names; open that file and confirm the number is printed there (cite the line or cell). A number with no row, or whose file does not carry it, is a fail.
2. Where the row names a builder report B110 to B123, open the matching checker report (V36 to V44 as they exist) and confirm the draft uses the checker's amended wording and value, not the builder's unamended one. List every place it does not.
3. Check `qa/claims_register.csv`: where the register row is Tier A with "pending gate 5" in its status, the draft must carry the pending value (the one the checker passed), and your report lists every such sentence so the gate digest can show it.

Then the text as a whole:
4. Logic: does any sentence claim more than its figures support (cause from a correlation; "every ordering" when only three were run; "the same" when it is +0.5%)? Does the abstract say anything the body does not? Do highlights (3 to 5, at most 85 characters each, checked by counting) match the body?
5. Consistency: the same quantity given two values anywhere (main text against supplement, table against prose, Table 1 against section 5); table numbers cited in prose exist and are the tables meant (B118 renumbered the main-text tables 6 to 9); figure placeholders match the figure list; every citation in the prose is in `references.md` and every entry there is cited (author-date form, Elsevier Harvard); "not seen" or "reported in" appears nowhere in prose.
6. Journal: `python3 qa/tools/wordcount.py B` at most 7,950 (run it, print the total); abstract at most 250 words (count); keywords 1 to 7; no em dash anywhere (grep the four files for the character); no time words ("recently", "currently", "now", "to date" and the like, unless tied to a dated figure); decision 33 tone: no sentence passes a verdict on another author's competence or honesty (a result can be "not reproduced"; an author cannot be "wrong").
7. The reader's test: three places where a referee who has not seen Paper A or the repository would be lost, and the one sentence that would fix each.

Report: the tolerance (exact for every printed number); the wrong-value example (one number you deliberately misread and caught by the file); the trace table (number; section; claims row; file; printed where; pass or fail), fails listed first; the checker-wording fails; the Tier A pending sentences; the logic and consistency fails with the sentence and a suggested rewrite; the journal checks with the counts; the three lost-reader places; register rows touched (none).
