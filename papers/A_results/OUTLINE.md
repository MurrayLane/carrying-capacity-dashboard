# Paper A (results): Australia's carrying capacity, 2011 to 2025, by region

Outlined 2026-11-06 from the plan in `PUBLICATIONS.md` (sections agreed 2026-11-03; scale curve decided 2026-11-02). This is an outline only: it fixes the structure, what each section answers and the files it would draw on. No results are stated and no tables or prose have been built.

**Working title:** Australia's carrying capacity, 2011 to 2025: what changed and where. *(To revisit with Murray.)*

**Readers.** Land use planners and sustainability analysts, with population and environment researchers (sequel to Lane, Dawes and Grace 2015 and Lane 2017, *Population and Environment*).

**Type.** Quantitative results paper. Same model, same 60 zones, same method (frozen during the data refresh), data brought forward from 2011 to 2025.

**The questions.**
1. Which regions moved between under and over capacity between 2011 and 2025, by how much, and how much of the change is population, land use or yield (the data effect)?
2. Has the penalty for a smaller unit of self-sufficiency (national, state, region; the three points of 2015) changed since 2011? The full curve and the boundary effect are in Paper B.

**Contribution beyond the earlier papers.** The 2015 paper gave three points (national, states, regions) on 2011 data. This paper repeats the three-point comparison on 2025 data and gives the change in the penalty since 2011 (the full scale curve is in Paper B); decomposes the 2011 to 2025 change into population, land use and yield; and takes four or five regions in depth.

## Sections

**1. Introduction.** (Highlight that the model is the author's own, as in Paper B.) The 2015 and 2017 findings, what was left open (scale, change over time), the question. Points to Paper B for the method comparison and the choice of method.

**2. Method and data in brief.** The frozen method, the 60 zones, the 2011 and 2025 data sets, the release chain (`methods/README.md`). One page; the full model and constants table belong to the supporting model paper. *Sources: `methods/`, `analysis/constants_audit/`.*

**3. The national and regional picture, 2011 to 2025.** Short-term national capacity against population; region by region change; the status flips between over and under capacity; ranges around each. *Sources: `results/comparison_cells.csv`, `results/ranges_*.csv`, `results/likely_range_*.csv`, `analysis/comparison_2025/movers.md`.*

**4. What drove the change.** The decomposition of the 2011 to 2025 change into population, land use and yield (the data effect), nationally and by region. *Sources: D4 decomposition, `results/comparison_cells.csv`.*

**5. Scale, briefly.** The 2015 three-point comparison (national, states, regions) on 2025 data and the change in the penalty since 2011; the full curve, the boundary effect and why NRM regions do badly are cited to Paper B. *Sources: `results/scale_curve.csv` (state, NRM and national rows).*

**6. The mechanism.** Capacity is set by pairing pasture-fed food with crops; what a meat limit does to rangeland; dairy pasture quality. One short section. *Sources: `analysis/sensitivity_2025/`.*

**7. What-if cases.** Forced local self-sufficiency (gardens, fruit and vegetables, diet); the long term. (The ideal contiguous split goes with the scale curve to Paper B.) *Sources: `analysis/regionalise_2025/`, long-term releases.*

**8. Regions in depth.** Four or five from the largest movers: a capital with hinterland, a Murray-Darling Basin region, south-west WA, Tasmania, an arid region. The 2015 migration map redrawn on current data. *Sources: `analysis/comparison_2025/movers.md`.*

**9. Limitations and conclusions.** What the model cannot carry (`DISCUSSION.md`); the data and code availability statement.

## Figures (to be scripts over `results/` when drafting begins)

1. National capacity against population, 2011 and 2025, with ranges.
2. Region-by-region change and the status flips (map).
3. The decomposition of the change by region.
4. The three-point scale comparison, 2011 and 2025.
5. The 2015 migration map redrawn.

## Decided 2026-11-06

* **No reconciliation table.** Earlier published figures are not tabulated against the new ones; the correction notes carry that. The 2011 results appear as corrected only, with one footnote saying the original published values were updated.
* **2011 results: corrected only** (footnote as above).

## Decisions still open

1. **Where the model material goes.** The improvements one at a time and the Monte Carlo method: in this paper, in Paper B (as what the method comparison suggests the model should change), or in the supporting model paper. *Proposal:* ranges stay here (they qualify every number); see the discussion of Paper B for the improvements.
2. **Journal.** *Population and Environment* is the plan.
3. **Authors and order,** and whether the correction notes go out first (later).
