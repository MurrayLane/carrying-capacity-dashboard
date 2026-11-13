# Builder brief B94: footprint low-end wording on three Tier A rows (decision 85, approved by Murray 2026-11-13)

Rules: plain language; no time words; no em dashes. No git; no subagents; no network. Write only `qa/claims_register.csv` (rows B046, B156, B247 and any row whose statement repeats "103 to 343" or "two to eight times" for the footprint; grep for both and list what you find), `papers/B_methods/SECTION7_DRAFT.md` (the four places V32b names) and `qa/reports/B94_footprint_wording.md`.

Read `qa/reports/V32b_logic_B.md` problem 2 and rows B046, B156, B247, B268 first. Change statements only, never a value field: "103 to 343 million" becomes "146 to 343 million on current yields (103 million at 1990 world yields)" where the sentence is about current data; "two to eight times" becomes "about three to eight times" (state the arithmetic: 343 / 41.5 = 8.3; 146 / 41.5 = 3.5; 103 / 41.5 = 2.5). Append to each row's notes "; B94 (2026-11-13): statement reworded per decision 85; value unchanged". Checks: the register parses, 697 rows, 18 columns, line endings unchanged, no em dashes.

Report: each row (before and after statement), the draft lines changed, the register rows touched, and "Wrong-value check:" with one deliberate wrong ratio, marked as an example.
