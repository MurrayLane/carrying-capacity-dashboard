# Builder brief B72: number the outline subsections (decision 45)

Rules: plain language; no time words; no em dashes. No git; no subagents; no network. Write only `papers/A_results/OUTLINE.md`, `papers/B_methods/OUTLINE.md` and `qa/reports/B72_outline_numbering.md`.

Read the label-to-heading mapping table in `qa/reports/B68_reader_flags.md`. In each outline, inside the numbered section the mapping points to, add a bold subsection label at the start of the bullet or paragraph that the label names (for example `**A11.5 Drought resilience.**` before the drought-proofing bullet of section 11; `**B8.2 Trade.**` before the trade item of section 8), so that every `used_by` label in `qa/literature_register.csv` (grep the distinct labels: A1.1, A1.4, A1.5, A11.1 to A11.7, A12.1 to A12.4, B1-2.a, B1-2.b, B3.1, B4.7 to B4.9, B8.1 to B8.4 and any other) resolves to one labelled place. Where a label has no matching text in the outline (B70 found section 1 of Paper A names none of A1.1, A1.4, A1.5), add a one-line bullet in plain language stating the point, drawn from the B61 scope table's description of it, marked "(added 2026-11-11, decision 52)". Change no other wording.

Report: a table of label, file, line number, added or matched; the register rows touched (none); and "Wrong-value check:" with one deliberate example of a label placed in the wrong section, marked as an example.
