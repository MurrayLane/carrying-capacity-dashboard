# Paper A (results): Australia's carrying capacity, 2011 to 2025, by region

Outlined 2026-11-06 from the plan in `PUBLICATIONS.md` (sections agreed 2026-11-03; scale curve moved to Paper B 2026-11-06; thickened 2026-11-06). This is an outline only: it fixes the structure, what each section answers and the files it would draw on. No results are stated and no tables or prose have been built.

**Working title:** Australia's carrying capacity, 2011 to 2025: what changed, where, and how sure we can be. *(To revisit with Murray.)*

**Readers.** Land use planners and sustainability analysts, with population and environment researchers (sequel to Lane, Dawes and Grace 2015 and Lane 2017, *Population and Environment*).

**Type.** Quantitative results paper. Same model, same 60 zones, same method (frozen during the data refresh), data brought forward from 2011 to 2025.

**The questions.**
1. Which regions moved between under and over capacity between 2011 and 2025, by how much, and how much of the change is population, land use or yield (the data effect)?
2. What would a 100-year self-sufficiency plan (the long term) ask of each region, and how has that changed?
3. How do regional results hold under shocks (drought, a failed harvest, fuel, waste)?
4. How sure are the regional results: which flips survive the ranges, and which method choices move which regions?
5. Has the penalty for a smaller unit of self-sufficiency (national, state, region; the three points of 2015) changed since 2011? The full curve and the boundary effect are in Paper B.

**Contribution beyond the earlier papers.** The 2015 and 2017 papers gave one data vintage and, for the long term, one national and regional picture. This paper brings the whole picture forward to 2025 with the method frozen; decomposes the change; gives the long term and the shock cases region by region; says which regional findings are robust; and takes four or five regions in depth.

## Sections

**1. Introduction.** (Highlight that the model is the author's own, as in Paper B.) The 2015 and 2017 findings, what was left open (change over time, robustness), the questions. Points to Paper B for the method comparison and the choice of method.

**2. Method and data in brief.** The frozen method, the 60 zones, the 2011 and 2025 data sets, the release chain (`methods/README.md`). One page; the full model and constants table belong to the supporting model paper. *Sources: `methods/`, `analysis/constants_audit/`.*

**3. The short-term picture, 2011 to 2025.** National capacity against population; region by region change; the status flips between over and under capacity. *Sources: `results/comparison_cells.csv`, `analysis/comparison_2025/movers.md`.*

**4. What drove the change.** The decomposition of the 2011 to 2025 change into population, land use and yield (the data effect), nationally and by region. *Sources: D4 decomposition, `results/comparison_cells.csv`.*

**5. Scale, briefly.** The 2015 three-point comparison (national, states, regions) on 2025 data and the change in the penalty since 2011; the full curve, the boundary effect and why NRM regions do badly are cited to Paper B. *Sources: `results/scale_curve.csv` (state, NRM and national rows).*

**6. The mechanism.** Capacity is set by pairing pasture-fed food with crops; what a meat limit does to rangeland; dairy pasture quality. One short section. *Sources: `analysis/sensitivity_2025/`.*

**7. The long term: a 100-year plan.** The long-term settings (100 years of weather, low-meat diet, no avoidable waste, full recycling, organic, almost no fossil liquid fuel, 30% reserve); what each setting is worth (the weather allowance is the largest single lever); long-term capacity by region in both vintages; which regions are over capacity in the long term. *Sources: `analysis/long_term_2025/`, `analysis/resilience_2025/`, the long-term preset of `results/<release>.csv`.*

**8. Shocks and food security by region.** Drought by return period (the worst year of 5, 10, 20, 50, 100), a failed harvest (field-crop yields down), a grain store of one or two years, liquid fuel, waste at the national target or none; which regions are exposed. *Sources: `results/scenarios.csv`, `analysis/reliability_2025/`, `analysis/resilience_2025/`.*

**9. How sure are the regional results.** (a) Which status flips of section 3 hold across the 5th to 95th percentile ranges for each zone (the Monte Carlo method is described and tested in Paper B, section 6, and only used here). (b) The effect of each method choice region by region: each correction and improvement alone and in sequence, with the interaction; which regions are sensitive to which choice (the national reading of the same choices is in Paper B, section 6). *Sources: `results/ranges_*.csv`, `results/likely_range_*.csv`, `results/method_effects.csv`.*

**10. Regions in depth.** Four or five from the largest movers: a capital with hinterland, a Murray-Darling Basin region, south-west WA, Tasmania, an arid region. Each read through short term, long term, shocks and robustness. The 2015 migration map redrawn on current data. *Sources: `analysis/comparison_2025/movers.md`.*

**11. Limitations and conclusions.** What the model cannot carry (`DISCUSSION.md`); forced local self-sufficiency (gardens, fruit and vegetables, diet) as a limitation of the closed-region reading; the data and code availability statement. *Sources: `analysis/regionalise_2025/`.*

## Figures (to be scripts over `results/` when drafting begins)

1. National capacity against population, 2011 and 2025.
2. Region-by-region change and the status flips (map), with the flips that survive the ranges marked.
3. The decomposition of the change by region.
4. The three-point scale comparison, 2011 and 2025.
5. The long term: what each setting is worth, and long-term capacity by region.
6. Exposure to shocks by region.
7. The effect of each method choice by region (heat map).
8. The 2015 migration map redrawn.

## Decided 2026-11-06

* **No reconciliation table.** Earlier published figures are not tabulated against the new ones; the correction notes carry that. The 2011 results appear as corrected only, with one footnote saying the original published values were updated.
* **2011 results: corrected only** (footnote as above).
* **The scale curve is in Paper B** (design choice and method finding); this paper keeps the three-point comparison.

## Division of labour with Paper B (proposed 2026-11-06, to confirm)

Paper B reads the model's design choices **nationally**, set against the other methods (what moves the number, which method for which purpose). Paper A reads the same choices **regionally** and over time (which regions move, which results are robust). The module-by-module regional effects, the zone-by-zone ranges (the Monte Carlo method itself is in B), the long term and the shock cases are here; B carries only the national effect of each choice as a design choice.

## Decisions still open

1. **Is this the right weight for Paper A?** Sections 7 to 9 are added to thicken it; they could instead form a short model paper.
2. **Journal.** *Population and Environment* is the plan.
3. **Authors and order,** and whether the correction notes go out first (later).
