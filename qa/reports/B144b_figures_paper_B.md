# B144b: the three figures and Table 2 of Paper B
Built by rerunnable scripts under `analysis/figures_2025/paper_B/`. No paper, claims register or results file was touched. Dataviz skill files read first (`SKILL.md` was absent at the named path; the five reference files were read and followed, and the palette validator was run on the slots used: blue, orange, aqua pass all-pairs; aqua is below 3:1 on the surface, so shape and the legend carry it).
## Table 2 (13 rows, from `analysis/method_tests_2025/method_catalogue.csv`)
| Method | Family | What it measures | Question it answers (purpose) | Data it needs | People count directly | Australian reading | Register ids |
|---|---|---|---|---|---|---|---|
| Commodity balance (Foran and Poldy) | Commodity balance | whether domestic production covers the human requirement for each commodity, in tonnes | 1 Food security and drought risk | production by commodity, a requirement per person | by a further step | 40 to 41 (meat), 12 to 17 (fish), 127 to 128 (grain with feed grain) million people | L007 |
| Failure probability (Fearnside) | Failure probability | the chance that settlers fail in a year, as a relation to population density, not as one number | 1 Food security and drought risk | a yield record, a consumption standard, a rule for when a settler fails | by a further step | 41.5 (average year), 30.8 (1 in 10), 18.9 (1 in 100) million people, the model read through Fearnside's frame | L042 |
| Resource-based land and diet balance (Peters, Wilkins and Fick; Peters et al.; Fairlie) | Resource-based land and diet | the land a population needs for a stated diet, set against the land available | 2 Why national estimates range from 9 to 100 million | land by class, yields, a stated diet | directly | none for Australia | L015;L040;L041 |
| Land and diet balance, the author's model (thesis method, corrected and improved) | Resource-based land and diet | the people the land feeds on a stated diet, pairing pasture-fed food with crops and charging land for waste, fuel, fibre and a reserve | 2 Why national estimates range from 9 to 100 million | land by class, yields, diet, waste, fuel, fibre and reserve settings, a drought allowance | directly | 41.5 (31.1 to 49.2) corrected; 53.6 (37.9 to 60.0) improved (million people) | L020;L012;L013;L014 |
| Energy and protein balance (Gifford; Henry and Godden) | Energy and protein balance | the food energy and protein of domestic production, with exports counted as food, divided by a consumption factor per person | 2 Why national estimates range from 9 to 100 million | production totals, a land base, a consumption factor per person | directly | 134 to 211 million people | L003;L002 |
| Export-inclusive proportional count (CSIRO and University of Queensland) | Export-inclusive count | the people fed at home plus the people fed abroad, taken in proportion to the exported share of production | 2 Why national estimates range from 9 to 100 million | production, the exported share, the home population | directly | 68 to 104 million people, the proportional count rebuilt from the food balance by energy | L010 |
| Ecological footprint, food row (Rees; Wackernagel; Wackernagel and Rees; Simpson; Lenzen and Murray) | Ecological footprint | the productive land a population appropriates, at world-average productivity, wherever that land lies | 3 Regional and local land-use planning | consumption per person, land per tonne of each product, the country's land | by a further step | 103 to 343 million people as run in world-average hectares; 64.8 to 117.0 at Australia's own productivity | L139;L134;L050;L023;L022 |
| Integrated resource-flow models (Foran and Poldy; Hatfield-Dodds et al.; Bryan et al.; Navarro Garcia) | Integrated resource-flow models | stocks and flows of land, water, energy and materials through an economy, with their feedbacks and pressures | 3 Regional and local land-use planning | national accounts of land, water, energy and materials, scenario settings | no | none for Australia | L007;L075;L076;L209 |
| Water-bounded capacity (Khorsandi et al.) | Water-bounded capacity | capacity capped by land suitability, water, realistic yields and a share of net primary production, at several spatial scales | 3 Regional and local land-use planning | land suitability, water supply, yields, net primary production | directly | none for Australia | L073 |
| Index methods and planning studies (Graymore, Sipe and Rickson; Gutteridge; Noosa and Douglas Shire; Lane 2010) | Index methods and planning studies | regional indicators ranked against thresholds, or a footprint set against a carrying capacity for a planning area | 3 Regional and local land-use planning | regional indicators and thresholds, local land and population | no | none for Australia | L091;L034;L038;L039;L055 |
| HALF index, land per diet (Alexander et al.) | Land per diet and people per hectare | the land the world would need if everyone ate a given country's diet, as a share of world land, at world-average production | 4 Diet change and land use | a diet by food, world-average yields, world land | by a further step | 276 million people as run in world-average hectares; 76.0 at Australia's own productivity | L017 |
| People per hectare of cropland (Cassidy et al.) | Land per diet and people per hectare | the people nourished per hectare of cropland, after feed and other uses, on a stated diet energy | 4 Diet change and land use | crop production by item, the uses of each crop, cropland area | by a further step | 5.8 to 6.0 people a hectare delivered; 145 to 147 million (about 190 on all cropland) | L016 |
| Optimisation models, diet and land use (Chaudhary and Krishna; Gazan et al.; van Dooren; Gao and Bryan) | Optimisation models | the diet or land use that meets stated limits at least cost or least departure from what is observed | 4 Diet change and land use | nutrient and cost tables, land and environmental limits, observed diets | no | none for Australia | L204;L205;L207;L208 |

## Figure 1

Caption text for the patch:

> Figure 1. The methods of section 4 mapped by the question each answers, in the four purposes of section 7 (columns). Each method has one mark, placed at the purpose where the author's matrix (Table 9, with the failure-frame column named in its note) rates it highest and fewest other methods share that rating; the author's model is rated well suited to all four and sits where it has no other well-suited method beside it. Italic names are not rated in Table 9 and are placed from their description in section 4. Mark shape shows whether the method gives a people count directly, only by a further step, or not at all; orange is the author's model. Built from `analysis/method_tests_2025/method_catalogue.csv` (Table 2).

Message: Methods answer different questions, and the ones that give a people count directly are not the ones that serve every purpose.

Claims rows whose numbers appear: none (no number is drawn)

Files: analysis/figures_2025/paper_B/fig1_method_map_190mm.png; analysis/figures_2025/paper_B/fig1_method_map_190mm.svg; analysis/figures_2025/paper_B/fig1_method_map_90mm.png; analysis/figures_2025/paper_B/fig1_method_map_90mm.svg

## Figure 2

Caption text for the patch:

> Figure 2. Each method's reading of Australia on the common 2021 to 2023 data, as run and under lines (a), (b) and (c) of section 5.11, beside the model's widened ranges (million people, log scale). Every reading is one dot, 19 readings of five methods on each line, including the footprint's pasture-only readings; the footprint's printed range in Table 5 leaves those out. Line (a) keeps the productivity basis as part of the method, line (b) treats it as an input, and line (c) adds one per-person requirement and waste treatment to line (b) (cell c1 of Table S7). The grey band is the corrected release's 5th to 95th percentile (31.1 to 49.2) and the hatched band the improved release's (37.9 to 60.0); the vertical lines mark each release's base value. Built from `harmonised_comparison_lines.csv`, `harmonised_line_c.csv`, `results/ranges_2025-fixed_wide.csv` and `results/ranges_2025-improved_wide.csv`.

Message: As run, every aggregate method reads well above the model's ranges, and the footprint and HALF come down toward them only when productivity is counted as an input (line b).

Claims rows whose numbers appear: B019; B046; B068; B084; B112; B114; B153; B159; B264; B267; B268; B270; B272; B273; B274; B341; B342; B347; B348; B357; B402; B403

Files: analysis/figures_2025/paper_B/fig2_method_readings_190mm.png; analysis/figures_2025/paper_B/fig2_method_readings_190mm.svg; analysis/figures_2025/paper_B/fig2_method_readings_90mm.png; analysis/figures_2025/paper_B/fig2_method_readings_90mm.svg

## Figure 3

Caption text for the patch:

> Figure 3. The factor by which each single choice moved the answer of the author's model, one at a time (Table 8, panel A; higher capacity over lower, log scale). Single choices are ranked by factor; the drought allowance appears twice, with the weather factor on every yield (2.19) and on crop output alone (1.03), joined by the bracket. Below the line, not ranked: the diet C upper bound (triangle), two bundles of settings (squares) and the spread across the settings drawn together (diamonds). Built from `analysis/method_tests_2025/design_choices_panels.csv`.

Message: The weather allowance moves the model by 2.19 on every yield but only 1.03 on crops alone, and diet, the unit and the allowance outrank waste and land.

Claims rows whose numbers appear: B167; B168; B169; B170; B177; B181; B182; B183; B184; B187; B213; B214; B421; B422; B425; B426

Files: analysis/figures_2025/paper_B/fig3_design_choices_190mm.png; analysis/figures_2025/paper_B/fig3_design_choices_190mm.svg; analysis/figures_2025/paper_B/fig3_design_choices_90mm.png; analysis/figures_2025/paper_B/fig3_design_choices_90mm.svg

## Decisions and issues for the coordinator (not resolved here)

1. Placement in Figure 1 is a rule, not a judgement call: the purpose where the author's matrix (SECTION7_DRAFT.md, the source of Table 9 plus its failure-frame column) rates the method highest and the fewest other methods share that rating, ties to the lowest number. Peters and Fairlie take the model's rating because SECTION7_DRAFT.md names them the same family. Six methods (export-inclusive count, optimisation, integrated flow, water-bounded, index and planning) are not rated in Table 9; their placement is my reading of section 4 and 7.3, marked italic, and recorded in the csv column `placement basis`. Murray should confirm or move them.
2. Section 5.10 says the commodity balance "reads 12 to 41 million", but the same table and Table 5 give grain with feed grain at 127 to 128. Figure 2 plots all 19 readings, so the commodity row runs 12 to 128. The prose range leaves grain out.
3. The footprint's as-run readings in Figure 2 include the pasture-only builds (316.9 and 385.7), part of the 19 readings of Table 6; Table 5's printed "103 to 343" leaves them out. The caption says so.
4. Line (c) is cell c1 of Table S7 (its readings are line (b) times 1.512; recomputed distance 1.203 equals Table 6).
5. Claims rows for Figures 2 and 3 are chosen by reading statements (the register values are mostly text); the register cites `design_choices.csv` and `harmonised_comparison.csv` for several numbers the figures take from the panels and lines csvs.
6. Figure 3 keeps true rank order, so the 1.03 crop-only row sits at the bottom with a bracket to the 2.19 row, not directly beside it.
7. Both widths are drawn (190 and 90 mm), every text at 7 pt or more at print size; greyscale was checked on Figure 2 (shapes and sub-row position carry the lines).

## Files written

- `analysis/figures_2025/paper_B/build_catalogue.py`
- `analysis/figures_2025/paper_B/common.py`
- `analysis/figures_2025/paper_B/fig1_method_map.py`
- `analysis/figures_2025/paper_B/fig1_method_map_190mm.png`
- `analysis/figures_2025/paper_B/fig1_method_map_190mm.svg`
- `analysis/figures_2025/paper_B/fig1_method_map_90mm.png`
- `analysis/figures_2025/paper_B/fig1_method_map_90mm.svg`
- `analysis/figures_2025/paper_B/fig2_method_readings.py`
- `analysis/figures_2025/paper_B/fig2_method_readings_190mm.png`
- `analysis/figures_2025/paper_B/fig2_method_readings_190mm.svg`
- `analysis/figures_2025/paper_B/fig2_method_readings_90mm.png`
- `analysis/figures_2025/paper_B/fig2_method_readings_90mm.svg`
- `analysis/figures_2025/paper_B/fig3_design_choices.py`
- `analysis/figures_2025/paper_B/fig3_design_choices_190mm.png`
- `analysis/figures_2025/paper_B/fig3_design_choices_190mm.svg`
- `analysis/figures_2025/paper_B/fig3_design_choices_90mm.png`
- `analysis/figures_2025/paper_B/fig3_design_choices_90mm.svg`
- `analysis/figures_2025/paper_B/figures.csv`
- `analysis/figures_2025/paper_B/make_figures_csv.py`
- `analysis/figures_2025/paper_B/table_2.md`
- `analysis/method_tests_2025/method_catalogue.csv`
- `qa/reports/B144b_figures_paper_B.md`

Rerun: `python3 build_catalogue.py; python3 fig1_method_map.py; python3 fig2_method_readings.py; python3 fig3_design_choices.py; python3 make_figures_csv.py` from the paper_B folder.

## Wrong-value check

Each script has `--check`; `--plant X` replaces the printed value with a wrong one.

```
fig1_method_map.py --check            Figure 1, methods placed at purpose 2: printed 4 vs recomputed 4 -> PASS
fig1_method_map.py --check --plant 9  printed 9.0 vs recomputed 4 -> FAIL (exit 1)
fig2_method_readings.py --check       energy balance line (a) centre: printed 147.0 vs recomputed 147.0 -> PASS
fig2_method_readings.py --check --plant 150   printed 150.0 vs recomputed 147.0 -> FAIL (exit 1)
fig3_design_choices.py --check        drought allowance, high over low: printed 2.19 vs recomputed 2.1958 -> PASS
fig3_design_choices.py --check --plant 2.91   printed 2.91 vs recomputed 2.1958 -> FAIL (exit 1)
```

Wrong-value check: planted 2.91 for the Figure 3 drought factor (true 2.19) fails with exit 1.


## Appendix: fixes after the blind check (V56b)

Table 2 now has 13 rows and a scale column; the rows below replace the Table 2 above. Placement is rebuilt from Table 9 as the paper prints it (six columns); Fearnside's failure view, Peters, the export-inclusive count, optimisation, integrated flow, water-bounded and index and planning are not rated there, so all seven are placed by reading section 4 and set in italic in Figure 1. Changes: the model carries its purpose 1 qualifier (for crops; not tested on pasture-fed output); the footprint reads 146 to 343 as run on 2021-23 yields with 103 at 1990 yields, and 64.8 to 117.0 at Australia's own productivity; integrated flow is described as national Australian scenario models giving no people count and moved to purpose 4 (diet change and land use; none is a regional planning method); index and planning is marked mixed on the people count, with the reason in the cell.

| Method | Family | What it measures | Question it answers (purpose) | Data it needs | People count directly | Scale | Australian reading | Register ids |
|---|---|---|---|---|---|---|---|---|
| Land and diet balance, the author's model (thesis method, corrected and improved) | Resource-based land and diet | the people the land feeds on a stated diet, pairing pasture-fed food with crops and charging land for waste, fuel, fibre and a reserve | 1 Food security and drought risk (for crops; not tested on pasture-fed output) | land by class, yields, diet, waste, fuel, fibre and reserve settings, a drought allowance | directly | national, with regional and small-area (SA2) units | 41.5 (31.1 to 49.2) corrected; 53.6 (37.9 to 60.0) improved (million people) | L020;L012;L013;L014 |
| Commodity balance (Foran and Poldy) | Commodity balance | whether domestic production covers the human requirement for each commodity, in tonnes | 1 Food security and drought risk | production by commodity, a requirement per person | by a further step | national | 40 to 41 (meat), 12 to 17 (fish), 127 to 128 (grain with feed grain) million people | L007 |
| Failure probability (Fearnside) | Failure probability | the chance that settlers fail in a year, as a relation to population density, not as one number | 1 Food security and drought risk | a yield record, a consumption standard, a rule for when a settler fails | by a further step | a settlement or study area (Fearnside's Brazilian area); here the national model run through the frame | 41.5 (average year), 30.8 (1 in 10), 18.9 (1 in 100) million people, the model read through Fearnside's frame | L042 |
| Energy and protein balance (Gifford; Henry and Godden) | Energy and protein balance | the food energy and protein of domestic production, with exports counted as food, divided by a consumption factor per person | 2 Why national estimates range from 9 to 100 million | production totals, a land base, a consumption factor per person | directly | national | 134 to 211 million people | L003;L002 |
| Export-inclusive proportional count (CSIRO and University of Queensland) | Export-inclusive count | the people fed at home plus the people fed abroad, taken in proportion to the exported share of production | 2 Why national estimates range from 9 to 100 million | production, the exported share, the home population | directly | national | 68 to 104 million people, the proportional count rebuilt from the food balance by energy | L010 |
| Ecological footprint, food row (Rees; Wackernagel; Wackernagel and Rees; Simpson; Lenzen and Murray) | Ecological footprint | the productive land a population appropriates, at world-average productivity, wherever that land lies | 3 Regional and local land-use planning | consumption per person, land per tonne of each product, the country's land | by a further step | any population, from a country to the world; applied to Australia as a nation | 146 to 343 million people as run, in world-average hectares on 2021-23 yields (103 at 1990 world yields); 64.8 to 117.0 at Australia's own productivity | L139;L134;L050;L023;L022 |
| Water-bounded capacity (Khorsandi et al.) | Water-bounded capacity | capacity capped by land suitability, water, realistic yields and a share of net primary production, at several spatial scales | 3 Regional and local land-use planning | land suitability, water supply, yields, net primary production | directly | several spatial scales, from the country to small units (Iran) | none for Australia | L073 |
| Index methods and planning studies (Graymore, Sipe and Rickson; Gutteridge; Noosa and Douglas Shire; Lane 2010) | Index methods and planning studies | regional indicators ranked against thresholds, or a footprint set against a carrying capacity for a planning area | 3 Regional and local land-use planning | regional indicators and thresholds, local land and population | mixed: none for Graymore, Sipe and Rickson; Gutteridge sets a footprint against a capacity; the Noosa and Douglas Shire studies are cited only through Lane (2010) and the thesis | regional and local planning areas | none for Australia | L091;L034;L038;L039;L055 |
| Resource-based land and diet balance (Peters, Wilkins and Fick; Peters et al.; Fairlie) | Resource-based land and diet | the land a population needs for a stated diet, set against the land available | 4 Diet change and land use | land by class, yields, a stated diet | directly | a region or a country (New York State, the United States, Britain) | none for Australia | L015;L040;L041 |
| HALF index, land per diet (Alexander et al.) | Land per diet and people per hectare | the land the world would need if everyone ate a given country's diet, as a share of world land, at world-average production | 4 Diet change and land use | a diet by food, world-average yields, world land | by a further step | country against the world | 276 million people as run in world-average hectares; 76.0 at Australia's own productivity | L017 |
| People per hectare of cropland (Cassidy et al.) | Land per diet and people per hectare | the people nourished per hectare of cropland, after feed and other uses, on a stated diet energy | 4 Diet change and land use | crop production by item, the uses of each crop, cropland area | by a further step | the world and countries | 5.8 to 6.0 people a hectare delivered; 145 to 147 million (about 190 on all cropland) | L016 |
| Optimisation models, diet and land use (Chaudhary and Krishna; Gazan et al.; van Dooren; Gao and Bryan) | Optimisation models | the diet or land use that meets stated limits at least cost or least departure from what is observed | 4 Diet change and land use | nutrient and cost tables, land and environmental limits, observed diets | no | a country (diets) or a fine grid (LUTO's Australian land uses) | none for Australia | L204;L205;L207;L208 |
| Integrated resource-flow models (Foran and Poldy; Hatfield-Dodds et al.; Bryan et al.; Navarro Garcia) | Integrated resource-flow models | stocks and flows of land, water, energy and materials through an economy, with their feedbacks and pressures | 4 Diet change and land use | national accounts of land, water, energy and materials, scenario settings | no | national (Australian scenario models) | none for Australia | L007;L075;L076;L209 |

### Figure 1 (revised)

Caption text for the patch:

> Figure 1. The methods of section 4 mapped by the question each answers, in the four purposes of section 7 (columns). Each method has one mark. A method rated in Table 9 sits at the purpose where Table 9 rates it highest and the fewest other rated methods share that rating; the author's model, rated well suited to all four (for crops at purpose 1, not tested on pasture-fed output), sits at the first. Names in italic are not rated in Table 9 (the Peters land and diet balance, failure probability, the export-inclusive count, optimisation, integrated resource-flow, water-bounded capacity, and index and planning studies); the builder placed them by reading section 4. Mark shape shows whether the method gives a people count directly, only by a further step, not at all, or is mixed (the planning studies); orange is the author's model. Built from `analysis/method_tests_2025/method_catalogue.csv` (Table 2).

Message: The methods answer different questions, so a figure from one method is not an answer to the question another asks.

Claims rows: none

Printed numbers with no register row of their own: none: no number is drawn

### Figure 2 (revised)

Caption text for the patch:

> Figure 2. Each method's reading of Australia on the common 2021 to 2023 data, as run and under lines (a), (b) and (c) of section 5.11, beside the model's widened ranges (million people, log scale). Every reading is one dot: 19 readings of five methods on each line, including the footprint's pasture-only readings (Table 5 column (e) prints those at Australia's own productivity, 53.9 to 77.9; as run they are 316.9 and 385.7). The commodity-balance row runs 12 to 128 because grain with feed grain (127 to 128) is plotted but never binds, so the commodity balance's capacity range is 12 to 41. Line (a) keeps the productivity basis as part of the method, line (b) treats it as an input, and line (c) adds one per-person requirement and waste treatment to line (b) (cell c1 of Table S7). The grey band is the corrected release's 5th to 95th percentile (31.1 to 49.2) and the hatched band the improved release's (37.9 to 60.0); the vertical lines mark each release's base value. Built from `harmonised_comparison_lines.csv`, `harmonised_line_c.csv`, `results/ranges_2025-fixed_wide.csv` and `results/ranges_2025-improved_wide.csv`.

Message: As run, every aggregate method reads well above the model's ranges, and the footprint and HALF come down toward them only when productivity is counted as an input (line b).

Claims rows: B019; B044; B046; B068; B084; B112; B114; B153; B159; B264; B267; B268; B270; B272; B273; B274; B347; B348; B357

Printed numbers with no register row of their own: line (c) readings (8.0 MJ as eaten, the model's loss factors; 19 dots): no register row carries them singly, so they are cells of analysis/method_tests_2025/harmonised_line_c.csv, rows whose classification starts (c1) and reference starts reading, column harmonised; the Table 6 and S7 shares are B402 and B403, not drawn here

### Figure 3 (revised)

Caption text for the patch:

> Figure 3. The factor by which each single choice moved the answer of the author's model, one at a time (Table 8, panel A; higher capacity over lower, log scale). Single choices are ranked by factor; the drought allowance appears twice, with the weather factor on every yield (2.19) and on crop output alone (1.03), a note beside the 1.03 row linking them. Below the line, not ranked: the diet C upper bound (triangle), two bundles of settings (squares) and the spread across the settings drawn together (diamonds). Built from `analysis/method_tests_2025/design_choices_panels.csv`.

Message: The weather allowance moves the model by 2.19 on every yield but only 1.03 on crops alone, and diet, the unit and the allowance outrank waste and land.

Claims rows: B114; B167; B168; B169; B170; B177; B181; B182; B183; B184; B187; B213; B214; B333; B412; B421; B422; B425; B426

Printed numbers with no register row of their own: 3.77, 1.60, 1.48 and 1.76 are in B412 (and B333 orders them); 1.60 also B213, 3.77 also B214 (the diet readings 85.5 and 202.1 over 53.6), 1.48 also B425, 1.76 also B426 and pal_one_at_a_time_2025.csv, improved row; 1.27 is the drawn-window row of design_choices_panels.csv (B333); 1.58 for both releases is B187 and B390

### Other fixes
- Figure 3: the bracket is removed; a note beside the 1.03 row reads "same allowance as the 2.19 row". At 90 mm the value labels sit clear of the end markers.
- Figure 1 adds an open-square class (mixed) to the legend.
- Check tolerances: Figure 3 compares exactly with the csv factor column (a planted 2.20 against the true 2.19 fails) and also with high over low from the csv's rounded low and high (tolerance 0.01); Figure 2 compares the one-decimal centre exactly (a planted 147.04 against 147.0 fails); Figure 1 is an exact count.
- Rebuild: two full runs of all scripts give identical md5 sums for every PNG, SVG, csv and md (SVG date metadata is off and the hash salt is fixed in `common.py`).
- Figure 2 reading of line (c) rows: no register row carries them singly, so they are named as cells of `harmonised_line_c.csv` (classification c1, column harmonised) in `figures.csv`.

```
fig3_design_choices.py --check --plant 2.20   printed 2.2 vs recomputed 2.19 -> FAIL (exit 1)
fig2_method_readings.py --check --plant 147.04   printed 147.04 vs recomputed 147.0 -> FAIL (exit 1)
```

## Appendix 2: B149b flags

- Figure 1's drawn legend note now reads "author's reading" (PNG, SVG and PDF, both widths); `build_catalogue.py` and the catalogue's `placement basis` column say "author's reading" too.
- The caption strings in `make_figures_csv.py` now equal the text in `figures.csv` exactly (Figures 1 to 3 and Table 2), so a rerun leaves `figures.csv` unchanged (checked by diff).
- `table_2.md` no longer has the register-id column; the scale column stays. The register ids remain in `method_catalogue.csv`.
- Figures 2 and 3 (PNG, SVG, PDF at both widths) are byte-identical to the previous run.
