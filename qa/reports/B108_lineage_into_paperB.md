# B108 report: Wackernagel et al. 1999 and van den Bergh and Rietveld 2004 into Paper B

Files written: `papers/B_methods/draft/B_s01-03.md`, `B_s04-05.md`, their `_claims.csv` files, `papers/B_methods/SECTION_SCOPE.md` (sections 2 and 4 blocks, the whole-paper table and one note under it), `qa/claims_register.csv` (seven rows appended), this report. `python3 qa/tools/make_references.py B` also rewrote `papers/B_methods/draft/references.md`, as the brief asks.

## Pages confirmed on the files on disk

- van den Bergh and Rietveld (scan, read page by page with the Read tool): 69 studies, p. 195 abstract; 51 method-based studies giving 94 estimates plus 18 of categorical assertion giving 21, p. 196; 115 observations, p. 200; median 7.7 billion, p. 199 text and p. 200 Table 2 (n = 94); method Table 3, p. 201; limiting factor Table 4, p. 202; technology, diet and land availability, p. 201; "assuming it exists", p. 201; conditional estimates, abstract p. 195.
- Wackernagel et al. (text layer; pdf page n is printed page 374 + n): 1993 data, p. 377; division by world-average yields, p. 380; arable 2.8 in Table 3, p. 381; the 2.8 explained as a land-quality ratio, p. 383; Australia 9.0, 14.0, 5.0 and "1993 data", Table 4, p. 386.

One point the brief did not state: the 7.7 billion median is of the 94 method-based estimates (Table 2), not of all 115. The sentence says "for those built on a stated method", and B336 says so.

## Sentences added

- `papers/B_methods/draft/B_s01-03.md` line 49 (end of the critics paragraph, section 2): "At world scale, van den Bergh and Rietveld (2004) pooled 69 studies giving 115 estimates, with a median of 7.7 billion people for those built on a stated method (pp. 195, 199, 200). The estimates move with the method, the limiting factor, the technology and diet assumed and the land available (pp. 201, 202); the authors offer their own figures as conditional estimates, "assuming it exists" (pp. 195, 201)." No Australian figure is drawn from it.
- `papers/B_methods/draft/B_s04-05.md` line 27 (4.5, after the food-row sentence): "Wackernagel et al. 1999 took the method to national accounts on 1993 data, with footprint and bio-capacity both in hectares of world-average productivity, not of the nation's own land (pp. 377, 380, 386). For Australia they print 9.0 ha a person of footprint against 14.0 of bio-capacity, a remainder and not a deficit (p. 386); they give no count of people, so they are no comparator in section 5."
- The 2.8 clause: not added. Neither section 4 nor the gap-attribution prose of sections 4 and 5 mentions 2.8 (the paper's only mentions were in the drafter notes). The statement is carried in the scope (section 4 sources row for L244 and gap 6) and in register row B340.

## Cuts (repeats, no number cut)

- Section 2, first paragraph: "and why planners still use it" (the closing paragraph says it).
- Section 4, 4.5: "and section S2" in "Its critique and defence are in section 2" (section 4's opening names S2).
- Section 4, 4.8: "not how many people the land can feed" (the sentence before says none gives a people count).
- Drafter notes 3 and 5 in `B_s01-03.md` were updated to say section 2 now has claim rows and L245 is cited.

## Claim rows added

Register `qa/claims_register.csv` (Tier B, route "literature, page-cited (B106; B108)", status "self-checked (B106)"): B334 (69 studies, pp. 195, 196), B335 (115 estimates, p. 200), B336 (7.7 billion, pp. 199, 200, 202), B337 (Australia footprint 9.0, p. 386), B338 (bio-capacity 14.0, p. 386), B339 (1993, pp. 377, 386), B340 (2.8, pp. 381, 383; depends on B037; no paper sentence quotes it). The register has 707 data rows, 18 columns on every row, CRLF kept.

Claims csvs: `B_s01-03_claims.csv` gains five rows (section 2, sentences 21 and 22: B334, B335, B336, the method and limiting-factor statement, the "assuming it exists" quotation) and its section 2 sentence numbers from 21 on are shifted by 2. `B_s04-05_claims.csv` gains six rows (section 4, sentences 26 and 27: B339, the units, B337, B338, remainder-not-deficit, no count of people) and its section 4 sentence numbers from old 26 on are shifted by 2. Line endings were left as they were.

## Scope changes (`papers/B_methods/SECTION_SCOPE.md`)

- Section 2: new content point 7 and evidence row 7; evidence note and row 3 updated; L245 added to the sources table; year mix 27 rows (18 / 4 / 5); gap 3 narrowed (rows exist for L245 figures only); new gap 4 closed (world-scale scatter beyond Cohen, which also closes section 1 gap 2); budget line gives about 27 sources and the prose count.
- Section 4: point 5 and evidence row 5 updated; L244 added to the sources table; year mix 64 rows (33 / 20 / 11); gap 6 closed, with B106 flag 6 (the 2.8 withdrawal stands) and flag 8 (the DOI in L244's title field reads (98)90063-5, the printed PII is S0921-8009(98)00063-9; a Crossref check is left to a register job); budget line gives the prose count.
- Whole-paper table: section 1 gaps 4 to 3; section 2 sources 27, mix 18 / 4 / 5; section 4 sources 64, mix 33 / 20 / 11; total 139 distinct rows (222 section citations), distinct mix 66 / 43 / 30 (53% from 2016 on), gaps 26. The earlier 220 and 137 were reproduced from the sources tables before the change, and the new totals from the tables after it.
- Not edited, outside the brief's write list: the section 1 block (it still lists gap 2 as open; the table note says so) and the section 5 block (its L050 rows still carry the withdrawn 2.8).

## Word counts (prose only, the B98b rule; headings, tables, table notes, placeholders, drafter notes and the abstract left out)

| Section | Before | After |
|---|---|---|
| 1 | 854 | 854 |
| 2 | 732 | 795 |
| 3 | 339 | 339 |
| 4 | 1,286 | 1,344 |
| 5 | 1,967 | 1,967 |
| 6 | 1,473 | 1,473 |
| 7 | 585 | 585 |
| 8 | 625 | 625 |
| 9 | 331 | 331 |
| Total | 8,192 | 8,313 |

The brief asks for the paper to stay under 8,000. By this counter it was 8,192 before my edit, so it was over before B108. B98b reported 7,943 with a counter that also left out some notes; the later B101 edits may account for the gap. I cut only true repeats and no number, so the net is plus 121 words. Getting under 8,000 needs about 313 words cut, which is a choice for Murray: the scope names section 4 (details into Table 2) and section 5 as the first cuts.

## Checks

- No em or en dashes in the four files, the register or the scope. No time words added.
- Every new number (69, 115, 7.7 billion, 9.0, 14.0, 1993) is in a claims csv row and in register rows B334 to B339; 2.8 is in B340 and the scope only.
- `python3 qa/tools/make_references.py B`: 130 entries (68 from claims csvs, 62 from prose only), 27 CHECK entries; no id without a register row; L244 and L245 are both in the list.

Wrong-value check: EXAMPLE ONLY, not a finding. "Australia's footprint is 14.0 ha per person" would be wrong: Table 4 (p. 386) prints 14.0 as the bio-capacity and 9.0 as the footprint. Likewise "the median of all 115 estimates is 7.7 billion" is wrong: 7.7 is the median of the 94 method-based estimates (Table 2, p. 200). The check that catches it: B337 and B338 each name their column, and B336 names the 94.
