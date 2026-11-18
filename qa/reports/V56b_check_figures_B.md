# V56b: blind check of the Paper B figures and Table 2 (B144b)

Checker: blind, no git, no subagents, no network. The builder's scripts were not edited; every probe ran on scratch copies (scratchpad `v56b/`), with planted values in a scratch mirror of the repository's csvs. The builder's report was opened last. Written: this file only.

Note on the design rules: `SKILL.md` is absent at the path the brief names (the builder says the same). The `references/` files (`anti-patterns.md`, `color-formula.md`, `marks-and-anatomy.md`, `palette.md`) are present and were used.

## Tolerance

Data cells: exact. The plotted value must equal the csv cell as a float, with no rounding. Text sizes: 7 pt at print size is the minimum. Model bands: one decimal against the brief's 31.1 to 49.2 and 37.9 to 60.0.

## Regeneration

I reran all three scripts from scratch copies. Each of the six PNGs is pixel-identical to the committed file. The sizes are 2244 px and 1062 px wide at 300 dpi, which is 190.0 mm and 89.9 mm. So the committed files are the current output of the scripts.

## 1. Data behind the marks

### Figure 2 (pass)

I fixed the sample before looking at any csv. The ten indices were drawn with `random.Random(5602).sample(range(76),10)`, giving 2, 12, 14, 20, 26, 42, 50, 57, 59, 74. They index the flat list of 76 dots: the 19 readings in the order of the lines csv, each in the order as run, (a), (b), (c). I read each dot's value from the drawn `Line2D` data of the 190 mm figure and matched it on sub-row position and value.

| idx | method | reading | line | csv cell | plotted |
|---|---|---|---|---|---|
| 2 | Energy and protein | energy, production as it is | (b) | 145.2 | 145.2 |
| 12 | Energy and protein | protein, scaled to 70 Mha over 59.95 | as run | 156.2 | 156.2 |
| 14 | Energy and protein | protein, scaled to 70 Mha over 59.95 | (b) | 148.8 | 148.8 |
| 20 | Energy and protein | protein, scaled to 70 Mha over 45.7 | as run | 204.9 | 204.9 |
| 26 | Footprint | build 1, cropland-bound | (b) | 112.5 | 112.5 |
| 42 | Footprint | build 3, pasture | (b) | 77.9 | 77.9 |
| 50 | HALF | agricultural land over the diet's land | (b) | 76.0 | 76.0 |
| 57 | People per hectare | second build (V05) | (a) | 110.9 | 110.9 |
| 59 | People per hectare | second build (V05) | (c) | 167.7 | 167.7 |
| 74 | Commodity balance | grain with embodied feed grain | (b) | 127.0 | 127.0 |

All ten match exactly. As an extra check, the full multiset of 76 drawn dots (sub-row, value) equals the 76 csv cells.

Model bands, from the rows variant=wide, zone=1, setting=short:
- Corrected: p5 31,115,433 and p95 49,169,829, which is **31.1 to 49.2**.
- Improved: 37,903,299 and 59,970,715, which is **37.9 to 60.0**.
- Base lines: 41.5 and 53.6.

All four are confirmed.

Line (c) is cell c1 of `harmonised_line_c.csv`. Its summary rows (distance 1.203, SD 0.477, highest over lowest 4.12) equal Table 6's (c) column, so c1 is the right cell.

### Figure 3 (pass)

All 18 Panel A rows of `design_choices_panels.csv` are drawn. Every bar end equals the csv `factor (high over low)` exactly, and every printed label equals the factor.

The drought rows are correct:
- "Drought allowance, factor on every yield (the model's rule)": 18.9 to 41.5, factor **2.19**, orange.
- "Drought allowance, factor on crops only (bound)": 40.4 to 41.5, factor **1.03**, orange.

The ranked order matches the csv rank column, Table 8 panel A and section 6.11 exactly.

### Figure 1 and Table 2 (data pass; catalogue verdict below)

The marks equal the catalogue's `primary purpose number` and people-count flag. No number is drawn.

## 2. Design rules

| Check | Figure 1 | Figure 2 | Figure 3 |
|---|---|---|---|
| One axis | yes (categorical grid) | yes (log x) | yes (log x) |
| Legend for two or more series | yes | yes | yes |
| Categorical colours in reference order, at most 8 | blue, orange (slots 1, 2) | grey, blue, orange, aqua (slots 1 to 3 plus ink) | blue, orange, plus a lighter blue step for "not ranked" |
| No rainbow | yes | yes | yes |
| Text at least 7 pt at print size | all text 7.0 to 8.0 pt (read from the matplotlib text objects at both widths) | 7.0 to 7.5 | 7.0 to 7.5 |
| Greyscale | readable. Model orange (grey 137) against blue (107) is close, but the label "(the model)" carries it | readable. Shapes carry the lines; the bands are grey and hatched | readable. Drought rows are mid-grey (137) between blue (107) and light blue (174), and the legend swatches stay distinct |
| Em or en dash | none | none | none |
| Collisions or overflow | none | none (no text box overlaps, nothing outside the canvas) | **see the fails below** |

The em dash check had to be done on the text objects, not the files. The SVGs are written with `svg.fonttype = path`, so they contain no `<text>` elements, and a grep of them proves nothing. I checked every rendered text object at both widths instead and found no U+2014 or U+2013. figures.csv, table_2.md and method_catalogue.csv are also clean.

**Figure 3 design fails:**
1. **The bracket spans nine unrelated rows.** At 190 mm the "Same allowance" bracket runs from the 2.19 row down to the 1.03 row and encloses nine other choices, so it reads as a grouping of all of them.
2. **Value labels touch the end markers at 90 mm.** The measured gap from the marker edge to the text is 0.02 mm at 90 mm (0.16 mm at 190 mm), so "3.77", "1.33", "1.09" and the others butt their markers.
3. Minor: the x-axis title differs between widths ("higher over lower" against "higher capacity over lower").
4. Minor: the legend uses a square both as the bundle shape and as the colour swatches.

**Figure 2 minor points (not fails):**
- The base-value vertical lines are not in the legend; the caption covers them.
- Identical harmonised readings overlap, so the six energy readings on line (a) show as two marks. A reader cannot count the 19 readings the caption announces.

## 3. Captions and claims rows

Every claims row named in figures.csv exists in `qa/claims_register.csv`.

**Figure 1 caption: fail.**
- It says "Italic names are not rated in Table 9". Peters and Fearnside are not rated in the paper's Table 9 either, yet both are drawn upright. Peters' ratings are copied from the model because `SECTION7_DRAFT.md` calls it the same family. Table 9's note rates "the same model read through Fearnside's failure frame" and says it "is not counted as a method".
- It says the model "sits where it has no other well-suited method beside it", but Peters is drawn at purpose 2 beside it, carrying a borrowed "well suited".
- Separately, the one-sentence message contradicts Table 9. The message says the methods that give a people count directly are not the ones that serve every purpose, yet the model gives a count directly and is rated well suited to all four.
- Claims rows: none needed (no number drawn). Pass.

**Figure 2 caption: fail (one wording error).**
- "The footprint's printed range in Table 5 leaves those out" is only half true. Table 5 column (e) prints the pasture-alone readings (53.9 to 77.9). Only the as-run and harmonised ranges (103 to 343; 139 to 343) leave out 316.9 and 385.7.
- The rest of the caption matches the drawing.

**Figure 2 claims rows: fail (incomplete, and four rows hold no drawn number).**
- B019, B068, B084, B112, B114, B159, B264, B267, B268, B270, B272, B273 and B274 match the dots drawn.
- B046 gives 146.2 to 343.4, but the drawing reaches 385.7. B044 carries 385.7 and is not named.
- B153 has value "12 to 41", while its own statement and the figure run to 128.
- B341, B342, B402 and B403 are distances and shares; no number of theirs is drawn.
- The 19 line (c) readings (219.6, 225.0, 170.1, 62.0, 139.8 and so on) have no claims row at all.

**Figure 3 caption: pass.** It describes what is drawn.

**Figure 3 claims rows: fail (incomplete).**
- The rows named match their bars.
- Four drawn factors have no named row carrying them:
  - 3.77, where B214 carries 202.1, not the factor;
  - 1.60, where B213 carries 85.5;
  - 1.48, where B425 carries 33.43 and 49.47;
  - 1.76 (improved PAL).
- B412 and B333 carry all four and should be named. B114 (the improved Monte Carlo factor 1.58) is also missing.

**Table 2 claims rows: pass with gaps.**
- B004, B019, B046, B068, B137, B153 and B159 exist and match.
- The 30.8 is in B096, B134 and others, not in B137.
- No row carries Cassidy's "5.8 to 6.0" or "145 to 147"; B084 covers only the 190.

## 4. Catalogue verdict, row by row where it differs from the paper

| Row | Verdict against sections 2 to 4, 7 and the register |
|---|---|
| Commodity balance | Matches 4.3 and Table 9 (partly, partly, not, not). Purpose 1 is a tie-break between 1 and 2, supported by 7.2 and 7.6. Fine. |
| Failure probability (Fearnside) | Description matches 4.10. **Its ratings are not the paper's.** Table 9 rates the model read through the frame and says it is not a method, and 5.8 says "not as an independent method". Placement at 1 still follows from 4.10 and 7.2. It should be italic, like the other unrated rows. |
| Peters / Fairlie | Description matches 4.1. **Not rated in Table 9.** The "well suited x4" comes from SECTION7_DRAFT.md, not the paper. Placement at 2 is the builder's reading. |
| The model | **Drops Table 9's purpose 1 qualifier** ("for crops; not tested on pasture-fed output"). Otherwise matches. |
| Energy and protein balance | Matches 4.2 and Table 9; L003 and L002 hold. |
| Export-inclusive count | Matches 4.4; "directly" holds; 68 to 104 matches Table 8 panel B. Placement at 2 follows 7.3. |
| Footprint | Description and "by a further step" match 4.5. **The Australian reading "103 to 343 as run" repeats the `cross_method.csv` cell that Table 3 corrects**: "146 to 343 on 2021-23 yields; 103 at 1990 world yields". Placement at 3 follows 7.4 (a tie with 4). |
| Integrated resource-flow | Description matches 4.8. **"None for Australia" misreads 4.8**, which says these are national scenario models *of Australia* with no people count; the cell should say "no people count". Placement at 3 does not follow from the text, which calls them national. |
| Water-bounded | Placement at 3 follows 4.9 ("smaller and more local"). The paper does not state "directly" outright, but it is consistent with "cap capacity". |
| Index and planning studies | Placement at 3 follows 4.11. **"No" people count is true of Graymore**, but Gutteridge and the Noosa and Douglas Shire studies set a footprint against a carrying capacity, so "mixed" is more exact. |
| HALF | Matches 4.6 and Table 9 (well suited at 4). |
| People per hectare | Matches. Purpose 4 is a tie-break against 2, supported by the 4.6 family. |
| Optimisation | Matches 4.7 ("a people count is not their output"). Placement at 4 follows. |

Also, the paper's Table 2 placeholder names the columns "family, question answered, inputs, outputs, scale, sources". The catalogue has no scale column. Either the placeholder text or the table must change.

**The six placements the builder made by its own reading:**
1. Export-inclusive count at 2: **follows** (7.3).
2. Optimisation at 4: **follows** (4.7).
3. Integrated resource-flow at 3: **does not clearly follow**. 4.8 calls them national and assigns no purpose.
4. Water-bounded at 3: **follows** (4.9).
5. Index and planning at 3: **follows** (4.11).
6. Peters and Fairlie at 2, by borrowing the model's ratings from SECTION7_DRAFT.md: **not from the paper**. The paper gives no rating. Purpose 2 is defensible only as "same family as the model", and the row should then be italic.

Fearnside is a seventh row whose ratings are not the paper's (see the table above).

## 5. Pass or fail per figure

| Figure | Data | Design | Caption | Claims rows |
|---|---|---|---|---|
| Figure 1 | pass | pass | **fail**: Peters and Fearnside not italic; "no other well-suited method beside it" is false with Peters at 2 | pass (none drawn) |
| Figure 2 | pass (10 of 10 sampled, 76 of 76 overall; bands confirmed) | pass (minor points only) | **fail**: the "Table 5 leaves those out" wording | **fail**: B044 and line (c) rows missing; B341, B342, B402 and B403 hold no drawn number; B046 and B153 do not span what is drawn |
| Figure 3 | pass (18 of 18; 2.19 and 1.03 confirmed) | **fail**: bracket over nine rows; labels touching markers at 90 mm | pass | **fail**: B412 and B333 (3.77, 1.60, 1.48, 1.76) and B114 not named |
| Table 2 | pass against cross_method and the claims rows | n/a | pass | pass with gaps (Cassidy reading has no row) |

## 6. Rerun of `--check` and the wrong-value example

The builder's checks, run as written:

| Check | Result |
|---|---|
| fig1 `--check` | printed 4, recomputed 4, PASS |
| fig1 `--plant 9` | FAIL, exit 1 |
| fig2 `--check` | printed 147.0, recomputed 147.0, PASS |
| fig2 `--plant 150` | FAIL, exit 1 |
| fig3 `--check` | printed 2.19, recomputed 2.1958, PASS |
| fig3 `--plant 2.91` | FAIL, exit 1 |

**Wrong-value example (mine, planted in a scratch csv, not the repository's):**

| Planted value | Result |
|---|---|
| Figure 3: drought factor in `design_choices_panels.csv` set from 2.19 to 2.29 | "printed 2.29 vs recomputed 2.1958 -> FAIL", exit 1 |
| Figure 3: the same factor set to 2.91 | caught earlier, by the rank assertion ("rank differs from factor") |
| Figure 2: energy reading on line (a) set from 145.2 to 154.2 | "printed 148.5 vs recomputed 147.0 -> FAIL", exit 1 |
| Figure 1: export-inclusive question set from 2 to 3, purpose number left at 2 | "printed 4 vs recomputed 3 -> FAIL", exit 1 |

**Weakness:** the tolerances are loose. Figure 3 uses 0.01 and Figure 2 uses 0.05, so a planted 2.20 (Figure 3) and 147.04 (Figure 2) both PASS. Figure 1's "printed" value is a count that is never drawn.

## 7. The builder's decision points, with my reading

1. **Section 5.10 "12 to 41" against the 12 to 128 that Figure 2 plots.**
   - `cross_method.csv` carries low 12 and high 41, and its text cell lists grain at 127 to 128. Table 3 and Table 5 print all three commodities, grain included.
   - Section 4.3 defines the method's capacity as "the smallest population binding". Grain at 127 to 128 never binds, so the capacity reading cannot reach 128. 12 to 41 is the range of the two items that could bind, fish and meat.
   - So the sentence and the csv low and high are right. The figure is also right as a plot of per-commodity readings, and the 19 readings of Table 6 need grain to give 22.69 and 32.14.
   - Fix: keep 12 to 41 in 5.10 and add "(grain with feed grain, which does not bind, 127 to 128)". Add one clause to the Figure 2 caption saying that the commodity balance's grain dot is a non-binding item.
   - Flag to the coordinator, not touched: B153's value field (12 to 41) is narrower than its own statement.
2. **Footprint pasture-only readings included.** They should stay in.
   - They are part of the 19 paired readings of Table 6. Table 6's highest-over-lowest values equal 385.7 / 17.0 = 22.69 as run and 385.7 / 12.0 = 32.14 on line (a), which is only true with them in.
   - The caption must be corrected: Table 5 column (e) does print the pasture-alone line (b) readings (53.9 to 77.9). Only the as-run and harmonised ranges leave out 316.9 and 385.7.
3. **Rank order of Figure 3.** The true rank order is right: it matches Table 8 panel A and section 6.11 row for row. The fault is the bracket, not the order.
   - Drop the long bracket. The orange colour and the legend already pair the rows.
   - Alternatively, put a short note beside the 1.03 row such as "same allowance, crops only; compare 2.19".

## Register rows touched

None. No file other than this report was written in the repository.
