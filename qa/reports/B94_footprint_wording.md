# B94: footprint low-end wording (decision 85)

Statements reworded; no value field changed. Arithmetic: 343 / 41.5 = 8.3; 146 / 41.5 = 3.5; 103 / 41.5 = 2.5. On current yields the low end is 146 (B268: 146.2), so the multiple is about three to eight; 103 is the figure at 1990 world yields.

## Search
Grep for "103 to 343" and "two to eight" in the register found only B046, B156 and B247 in statements. The same text remains in the value fields of B046, B156 and B247 ("103 to 343", "103 to 343; 12 to 41", "3 to 8; 103 to 343"), left unchanged as instructed. No other row repeats either phrase.

## Register rows touched: B046, B156, B247
Each row's notes had "; B94 (2026-11-13): statement reworded per decision 85; value unchanged" appended.

B046 before: Read as a capacity, the food-row footprint method gives 103 to 343 million for Australia on current data.
B046 after: Read as a capacity, the food-row footprint method gives 146 to 343 million for Australia on current yields (103 million at 1990 world yields).

B156 before: ...people per hectare) read 103 to 343 million, about two to eight times the model; the commodity balance and Fearnside's view read 12 to 41 million, the model's range.
B156 after: ...people per hectare) read 146 to 343 million on current yields (103 million at 1990 world yields), about three to eight times the model; the commodity balance and Fearnside's view read 12 to 41 million, the model's range.

B247 before: ...give about two to eight times the land-and-diet balance because ...; HALF and footprint read Australia as 103 to 343 million.
B247 after: ...give about three to eight times the land-and-diet balance because ...; HALF and footprint read Australia as 146 to 343 million on current yields (103 million at 1990 world yields).

B268 was read only; it holds 146.2 and was not edited.

## Draft lines changed (papers/B_methods/SECTION7_DRAFT.md)
V32b says four places; I found three places that carry the wording, and changed all three.
- Line 24: "(they read 103 to 343 million)" became "(they read 146 to 343 million on current yields, 103 million at 1990 world yields)".
- Line 34: "103 to 343 million on the footprint builds" became "146 to 343 million on the footprint builds at current yields (103 million at 1990 world yields)".
- Line 43: "about two to eight times" became "about three to eight times".
The fourth place V32b counts was not found by grep for 103, 343 or eight; Murray may want to say which it meant.

## Checks
Register parses: 698 lines including header = 697 rows, 18 columns on every row. Line endings unchanged (CRLF throughout, 698 each). No em dashes in the register or the draft. Draft keeps LF endings.

Wrong-value check: example of a deliberately wrong ratio, not to be used: 146 / 41.5 = 2.5 would be wrong (it is 3.5; 2.5 belongs to 103).
