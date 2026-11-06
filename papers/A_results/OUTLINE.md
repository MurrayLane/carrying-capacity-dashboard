# Paper A (results): Australia's carrying capacity, 2011 to 2025, by region and scale

Outlined 2026-11-06 from the plan in `PUBLICATIONS.md` (sections agreed 2026-11-03; scale curve decided 2026-11-02). This is an outline only: it fixes the structure, what each section answers and the files it would draw on. No results are stated and no tables or prose have been built.

**Working title:** Australia's carrying capacity, 2011 to 2025: what changed, where, and how much depends on the scale. *(To revisit with Murray.)*

**Readers.** Land use planners and sustainability analysts, with population and environment researchers (sequel to Lane, Dawes and Grace 2015 and Lane 2017, *Population and Environment*).

**Type.** Quantitative results paper. Same model, same 60 zones, same method (frozen during the data refresh), data brought forward from 2011 to 2025.

**The questions.**
1. Which regions moved between under and over capacity between 2011 and 2025, by how much, and how much of the change is population, land use or yield (the data effect)?
2. How does capacity fall as the unit of self-sufficiency shrinks, from national to SA2 (the whole curve, where the 2015 paper had three points)?
3. Where does the curve bend, and how much of the fall is the boundary rather than the scale?

**Contribution beyond the earlier papers.** The 2015 paper gave three points (national, states, regions) on 2011 data. This paper gives the whole curve on current data; separates the boundary effect (landscape regions against 2011 NRM zones on identical data) from the scale effect; decomposes the 2011 to 2025 change into population, land use and yield; and takes four or five regions in depth.

## Sections

**1. Introduction.** The 2015 and 2017 findings, what was left open (scale, change over time), the question. Points to Paper B for the method comparison and the choice of method.

**2. Method and data in brief.** The frozen method, the 60 zones, the 2011 and 2025 data sets, the release chain (`methods/README.md`). One page; the full model and constants table belong to the supporting model paper. *Sources: `methods/`, `analysis/constants_audit/`.*

**3. The national and regional picture, 2011 to 2025.** Short-term national capacity against population; region by region change; the status flips between over and under capacity; ranges around each. *Sources: `results/comparison_cells.csv`, `results/ranges_*.csv`, `results/likely_range_*.csv`, `analysis/comparison_2025/movers.md`.*

**4. What drove the change.** The decomposition of the 2011 to 2025 change into population, land use and yield (the data effect), nationally and by region. *Sources: D4 decomposition, `results/comparison_cells.csv`.*

**5. Real boundaries: the scale curve.** Sum of capacities at state, NRM region, SA4, SA3 and SA2 level for both vintages; the boundary effect (landscape regions against NRM zones on identical data); why some regions do badly (pasture stranded from cropland). *Sources: `results/scale_curve.csv`, `analysis/scale_curve_2025/`.*

**6. The mechanism.** Capacity is set by pairing pasture-fed food with crops; what a meat limit does to rangeland; dairy pasture quality. One short section. *Sources: `analysis/sensitivity_2025/`.*

**7. What-if cases.** The ideal contiguous split ignoring population; forced local self-sufficiency (gardens, fruit and vegetables, diet); the long term. *Sources: `analysis/regionalise_2025/`, long-term releases.*

**8. Regions in depth.** Four or five from the largest movers: a capital with hinterland, a Murray-Darling Basin region, south-west WA, Tasmania, an arid region. The 2015 migration map redrawn on current data. *Sources: `analysis/comparison_2025/movers.md`.*

**9. Limitations and conclusions.** What the model cannot carry (`DISCUSSION.md`); the data and code availability statement.

## Figures (to be scripts over `results/` when drafting begins)

1. National capacity against population, 2011 and 2025, with ranges.
2. Region-by-region change and the status flips (map).
3. The decomposition of the change by region.
4. The scale curve: capacity against unit of self-sufficiency, both vintages, boundary effect marked.
5. The 2015 migration map redrawn.

## Decided 2026-11-06

* **No reconciliation table.** Earlier published figures are not tabulated against the new ones; the correction notes carry that. The 2011 results appear as corrected only, with one footnote saying the original published values were updated.
* **2011 results: corrected only** (footnote as above).

## Decisions still open

1. **Where the model material goes.** The improvements one at a time and the Monte Carlo method: in this paper, in Paper B (as what the method comparison suggests the model should change), or in the supporting model paper. *Proposal:* ranges stay here (they qualify every number); see the discussion of Paper B for the improvements.
2. **Journal.** *Population and Environment* is the plan.
3. **Authors and order,** and whether the correction notes go out first (later).
