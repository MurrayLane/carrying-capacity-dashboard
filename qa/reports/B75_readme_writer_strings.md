# B75: sensitivity README writers keep B69's wording (X092 remainder)

## Literals changed

* `analysis/sensitivity_2025/write_readme.py` line 45: before `costs 13.8%;`, after `costs {-(d[('gt_none', 1, 'long')] / B['long'] - 1) * 100:.1f}%;`. The value now comes from `results.csv`, the same file and the same row (gt_none, Australia, long term, against base) that the ranking table prints as -13.9%. It reads 13.9 (10,660,326 against 12,376,463 = 13.87%).
* `analysis/sensitivity_2025/write_readme.py` line 62: before `ten uncertain choices are drawn together, 2,000 times (`monte_carlo.mjs`;`, after `ten uncertain choices are drawn together, 2,000 times in this three-window run (the all-zones runs behind `results/ranges_<release>.csv` draw thirteen) (`monte_carlo.mjs`;`. This is B69's README line 72 wording. The all-zones runs sample thirteen, of which twelve vary in the 2025 releases; that detail is already in README lines 154 and 173.
* `analysis/sensitivity_2025/summarise_mc.py` line 13 (a comment; no written text): before `(ten, or thirteen with the long-term choices)`, after `(ten in the three-window run; thirteen in the all-zones runs, of which twelve vary in the 2025 releases)`. The "10 uncertain choices" in the summaries comes from `len(INPUTS)`, so it reads 10 for the three-window run and 13 for the all-zones runs; no calculation or output string changed.

## Diff result

`write_readme.py` was run from the repository root into a copy under `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/b75/`. The regenerated README was byte-identical to the committed README (no differences, not even the fixed strings, because B69 had already written the new wording by hand). It was then run in place, and `cmp` against the pre-run copy again showed no difference. So the README was regenerated in place and its content did not change.

## Defect register

`qa/defects.csv` X092: `fixed_in` set to "B69; B75"; a B75 sentence appended to the notes. No other row changed (diff shows line 92 only).

Wrong-value check: example only, not made. Changing the 13.9 source to `d[('gt_none', 1, 'short')] / B['short']` would print about 0.2 instead of 13.9, because that is the short-term change; the long-term row is the one the table quotes.
