# B147a: Figures 1 to 8 and S6 placed in Paper A

No git, no subagents, no network. Written under `papers/A_results/draft/` and this report only.

## What was done

* The eight main-text placeholders in `A_s01-04.md`, `A_s05-08.md` and `A_s09-12.md` are replaced by "Figure N. caption" lines, text taken from `analysis/figures_2025/paper_A/figures.csv` (as fixed after V56a). The "Sources:" sentence of each caption is left out and no caption names a file, because the second-round response (3.10) keeps file paths out of captions; the files are named in the claims csv rows and in Supplementary Section S11. Three other file-name mentions were reworded to "source table" (Figure 6 and Figure 8 captions; Figure S6 drops the `scenarios.json` path).
* Figure S6 is placed at the end of Supplementary Section S3 (`supplementary.md`) with the ten scenarios defined in its caption and a one-line lead-in.
* Figure 3: placeholder and sentence changed to the all-orderings average. Figure 6: placeholder no longer says "with the named scenarios"; its caption points to Figure S6. Figure 4: caption states that the partition effect depends on the yield rule and draws the national-yield reference bar.
* Supplementary S11 figure list now names the nine files (Figures 1 to 8 and S6, png and svg pairs, in `analysis/figures_2025/paper_A/`) with their source csvs. Supplementary S1 said Figure 3 was "on the forward walk"; changed to the all-orderings average (supplement, not counted).
* Claims rows added for every caption (each cites `figures.csv`, the source csv and the register rows) in `A_s01-04_claims.csv`, `A_s05-08_claims.csv`, `A_s09-12_claims.csv`, `supplementary_claims.csv`. Figure 8 and Figure S6 rows are marked derived (no register row holds the regional values). Old claims rows for the removed placeholders (for example "[Figure 4: ..." in `A_s05-08_claims.csv`) were left in place; the coordinator may drop them.

## Sentences changed (before; after)

1. `A_s01-04.md`, section 4 (counted):
   * Before: "Figure 3 gives each layer's effect in each of the 53 regions on the forward walk; Supplementary Section S1 gives the detail."
   * After: "Figure 3 gives each layer's effect in each of the 53 regions as the average over all orderings; Supplementary Section S1 gives the detail."
2. `supplementary.md`, S1 (not counted):
   * Before: "...is on the corrected releases (`2011-fixed` to `2025-fixed`) and on the forward walk."
   * After: "...is on the corrected releases (`2011-fixed` to `2025-fixed`), and the figure shows the average over all orderings; the forward and reverse walks are quoted where named."
3. Placeholders (not counted, replaced by captions): the Figure 3 placeholder lost "forward walk"; the Figure 6 placeholder lost "with the named scenarios on 2025 data".

## Word counts

`python3 qa/tools/wordcount.py A` on the unedited files gave TOTAL 7937; after the edits, on a scratch copy after `assemble_draft.py A`, TOTAL 7939 (limit 7,950). The change is the two extra words in sentence 1. Abstract unchanged. The real `paper_A_draft1.md` was not touched.

## Wrong-value check (example)

Example: the pre-fix Figure 1 caption in `figures.csv` said the 2025 bars were "over 2,000 draws" for both ranges (V56a). The fixed `figures.csv` says the thin line is the 19-choice range over 2,000 draws and the thick band the earlier 13-choice range over 1,000 draws. Checked against `results/ranges_2025-fixed_wide.csv` (variant `existing`, `draws=1000`) and Supplementary S4, which agree with the fixed text; the placed caption carries the fixed value, so the pre-fix number is caught. A second example: the pre-fix Figure 4 caption said the bars were "random groupings of the SA2s into 7 groups"; the fixed text, placed, says the 53 regions, as in A459.

## Not checked

The figures were not redrawn or re-run (no scripts executed); the caption text rests on `figures.csv` as fixed and V56a. In particular the Figure 8 caption ("3 of the 53 circles under 0.5 mm, no minimum size") was not recomputed.

## Captions as placed

Figure 1. National short-term capacity against population, Australia, 2011 and 2025, corrected method. Each dot is one year; a dot above the line has capacity above population. The 2011 value is the base case on the corrected 2011 release; 2011 has no sampled range. The 2025 bars are the 5th to 95th percentile of capacity: the thin line is the widened range over 19 choices and 2,000 draws, the thick band the earlier range over 13 choices and 1,000 draws.

Figure 2. Change in short-term capacity and population by region, 2011 to 2025, corrected method, 53 regions ordered by 2025 capacity over population. Each line joins the 2011 to the 2025 capacity over population on a log scale; the line at 1 is the status line, so a line that crosses it is a status flip (bold names). Flips are coloured by the verdict on the 19-choice 2025 ranges (green diamond: the 2025 status holds in the range; violet square: it does not); each region has a small dot for 2011 and a larger marker for 2025, and open markers carry a land-definition or older 2011 boundary flag. The two columns give the change in capacity and in population in thousand people. Alinytjara Wilurara has a 2025 capacity near zero and is drawn at the 0.001 floor of the axis.

Figure 3. Effect of each layer on short-term and long-term capacity in each of the 53 regions, 2011 to 2025, corrected method: the average over all 40,320 orderings of the eight layers, as a percentage of the region's 2011 capacity. Blue raises capacity and red lowers it; colour is clipped at 50% and a cell is labelled when the effect is 25% or more, with its true value if clipped. Regions are grouped by state. Hatched cells are negative, so the sign reads in greyscale.

Figure 4. The scale curve: the sum of the units' capacities as a share of the national capacity at each level from the nation to SA2, 2011 and 2025, short and long term, state-yield basis, corrected method. Each unit takes the yields, climate zone and settings of its state and the national diet and waste settings; the number of units is under each level. Circles join the administrative levels; diamonds are the 53 NRM regions. At the State level the solid bar is the 5th to 95th percentile of the same sum over 200 random groupings of the 53 regions into 7 groups on the state-yield basis, and the hatched bar the same groupings on the national-yield reference, which isolates the land mix from the yield assignment. The size of the partition effect depends on that rule, because on the state basis a group that mixes states takes one state's yields and the sum can exceed the national capacity. The SA levels use 2020-21 land with each year's population.

Figure 5. Long-term results, corrected method, own yields. (a) What each long-term setting is worth for Australia in 2025 (grey bars): the change in the long-term capacity when that one setting is put back to its short-term value, as a percentage of the long-term capacity (the settings are listed with their short-term and long-term values; timber, infrastructure area and the reserve share have no effect). (b) Long-term capacity over population in each of the 53 regions, 2011 (blue) and 2025 (orange), ordered by the 2025 value, on a log scale; the line at 1 is the status line and values below 0.01 are drawn at the axis edge.

Figure 6. Exposure to shocks by region: capacity over population in each of the 53 regions in an average year, at 1 in 10 years and at 1 in 20 years, 2011 (blue) and 2025 (orange), own yields, corrected method, regions ordered by the 2025 average-year value, log scale. The orange line is the 5th to 95th percentile of the region's 2025 capacity over population on the widened 19-choice range; 2011 has no range. These are short-term results (the drought allowance applied at each return period). A region is over capacity where its marker is left of the line at 1 (2011 squares, 2025 circles). Values below 0.001 are drawn at the axis edge. Only the three return periods that have ranges are drawn; the 1-in-5, 1-in-50 and 1-in-100 results are in the source table. The named scenarios by region are in Figure S6.

Figure 7. The effect of each method choice on capacity in each of the 53 regions, 2025 data, short and long term, as a percentage of the published-method capacity (Lane 2014). Each choice is applied alone to the published method. Blue raises capacity and red lowers it; colour is clipped at 40% and cells of 10% or more are labelled with their value. The two corrections, marked (C), are the beef carcase yield and the biodiesel yield; the other six are improvements. The last two columns apply the two corrections together (corrected method) and all eight choices together (improved method). Hatched cells are negative. The Alinytjara Wilurara row is blank because its 2025 published-method capacity is 0 (20 cells). Regions are grouped by state.

Figure 8. The migration map redrawn: population less short-term capacity in each of the 53 regions, 2025, corrected method, average year. Each region is a circle at the area-weighted mean of its SA2 centroids (the repository holds no region polygons; grey dots are SA2 centroids). Circle area is proportional to the size of the excess, in people; red is over capacity and blue is room to spare, with a neutral grey at zero and the colour step following the square root of the excess. Regions with room to spare are hatched, so the sign reads in greyscale. There is no minimum circle size: 3 of the 53 circles are under 0.5 mm across at print size and are not visible (their values are in the source table).

Figure S6. The named scenarios by region, 2025 data, corrected release (each grain store with its own resilience table): capacity over population in each of the 53 regions under each scenario, short and long term, on a log scale; the line at 1 is the status line. Orange dots are regions that are under capacity in the reference and over capacity in the scenario; their names are listed for the long term, and no region tips in the short term. Scenario definitions (run on the corrected release; the reference is the corrected 2025 release at its defaults): climate-crops-12: Field-crop yields 12% lower (the climate effect already observed); climate-crops-24: Field-crop yields 24% lower (upper end of the projected wheat decline); fuel-csiro-340: Long term: biofuel at CSIRO's maximum feedstock, 340 litres a person; fuel-ev-156: Long term: light vehicles electrified, 156 litres of liquid fuel a person; grain-store-1: Long term: one year of grain held in store (the store is free in the model); grain-store-2: Long term: two years of grain held in store (the store is free in the model); recycling-half: Half of the stage uptake pattern achieved; recycling-none: No recycling of food waste into animal feed; waste-none: No avoidable food waste; waste-target-6: Avoidable food waste at the national target (halved to 6%).


## Changed files

* papers/A_results/draft/A_s01-04.md
* papers/A_results/draft/A_s05-08.md
* papers/A_results/draft/A_s09-12.md
* papers/A_results/draft/A_s01-04_claims.csv
* papers/A_results/draft/A_s05-08_claims.csv
* papers/A_results/draft/A_s09-12_claims.csv
* papers/A_results/draft/supplementary.md
* papers/A_results/draft/supplementary_claims.csv
* qa/reports/B147a_figures_into_paper_A.md
