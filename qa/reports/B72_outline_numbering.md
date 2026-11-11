# B72 report: numbered subsection labels in the two outlines (decision 45)

Each label below now appears once, in bold, in the outline named. Labels that matched existing text were placed inline in front of the words that name them (the outlines are single paragraphs per section, so the label sits mid-paragraph at the matching phrase, not at a paragraph start). Labels with no matching text got a one-line bullet marked "(added 2026-11-11, decision 52)". No other wording was changed. Line numbers are those of the files after the edit.

| Label | File | Line | Result |
|---|---|---|---|
| A1.1 | papers/A_results/OUTLINE.md | 27 | added |
| A1.4 | papers/A_results/OUTLINE.md | 28 | added |
| A1.5 | papers/A_results/OUTLINE.md | 29 | added |
| A11.1 | papers/A_results/OUTLINE.md | 49 | matched (livestock productivity) |
| A11.3 | papers/A_results/OUTLINE.md | 49 | matched (waste at the national target) |
| A11.4 | papers/A_results/OUTLINE.md | 49 | matched (grain store) |
| A11.5 | papers/A_results/OUTLINE.md | 49 | matched (drought-proofing) |
| A11.6 | papers/A_results/OUTLINE.md | 49 | matched (regions as a pool) |
| A11.7 | papers/A_results/OUTLINE.md | 49 | matched (imports, export diversion) |
| A12.1 | papers/A_results/OUTLINE.md | 51 | matched (forced local self-sufficiency) |
| A12.2 | papers/A_results/OUTLINE.md | 51 | matched (gardens, fruit and vegetables) |
| A12.3 | papers/A_results/OUTLINE.md | 53 | added |
| A12.4 | papers/A_results/OUTLINE.md | 54 | added |
| B1-2.b | papers/B_methods/OUTLINE.md | 26 | matched (section 1, why it matters to planners) |
| B1-2.a | papers/B_methods/OUTLINE.md | 30 | added (planetary limits and overshoot debate not named in section 2) |
| B3.1 | papers/B_methods/OUTLINE.md | 32 | matched (section 3 start) |
| B4.7 | papers/B_methods/OUTLINE.md | 34 | matched (nutrition optimisation) |
| B4.8 | papers/B_methods/OUTLINE.md | 34 | matched (integrated resource-flow models) |
| B4.9 | papers/B_methods/OUTLINE.md | 34 | matched (land-suitability, water and realistic-yield bounds) |
| B8.1 | papers/B_methods/OUTLINE.md | 57 | matched (variability between years) |
| B8.2 | papers/B_methods/OUTLINE.md | 57 | matched (imports and exports) |
| B8.3 | papers/B_methods/OUTLINE.md | 57 | matched (fossil energy land) |
| B8.4 | papers/B_methods/OUTLINE.md | 57 | matched (a single fixed diet) |

Totals: 23 distinct labels in `qa/literature_register.csv` `used_by`; 17 matched, 6 added (A1.1, A1.4, A1.5, A12.3, A12.4, B1-2.a). A11.2 and the B-series labels outside this set do not appear in `used_by`, so none was added.

Notes:
- The register `used_by` field holds descriptive strings (label plus topic); labels were extracted by pattern, and all 23 resolve to one labelled place.
- Added bullets draw on the B61 scope table's topic for each label (A12.3 water, A12.4 fuel and energy; the others from the B68 mapping table).
- Paper B section 2 still does not discuss the planetary boundaries debate; the B1-2.a bullet states the point only, and B68 decision 4 (take on the debate or drop the label) stays open.

Register rows touched: none.

Wrong-value check: EXAMPLE ONLY, not a finding. If the label B8.2 Trade were placed in front of "variability between years" in section 8, or in section 6 of Paper B, a reader following register row `used_by` B8.2 would land on text about years, not trade, so the label and the register topic would disagree.
