# Paper A (results): Australia's carrying capacity, 2011 to 2025, by region

Outlined 2026-11-06 from the plan in `PUBLICATIONS.md` (sections agreed 2026-11-03; scale curve in Paper A again 2026-11-06 once each paper had a narrative). This is an outline only: it fixes the structure, what each section answers and the files it would draw on. No results are stated and no tables or prose have been built.

**Working title:** Australia's carrying capacity, 2011 to 2025: what changed, where, and how sure we can be. *(To revisit with Murray.)*

**Narrative (Murray asked for a story to drive each paper, 2026-11-06).** *Claim:* between 2011 and 2025 the national food margin held, the long-term margin shrank, a drought year leaves little room, and the margin sits where the people are not. *Arc:* (1) the comfortable headline, about 1.5 times the population in both years; (2) production grew in step with people but in different places: capacity inland (basin, cropping belts, rangelands), people on the coast, and the scale curve to SA2 shows how much of the national margin dissolves at fine scale; (3) the comfort depends on the weather: the worst of ten years leaves a thin margin, and a 100-year self-sufficient plan has slipped from about 69% to about 57% of the population; (4) which regional results survive the ranges and the land-definition checks; (5) regions in depth. *Takeaway for planners:* the national margin is not safe, it held because production grew where the people are not.
**Headline (corrected releases; to confirm at freeze).** Short-term capacity about 1.5 times population in both years (33.3 against 22.3 million in 2011; 41.5 against 27.6 in 2025); long term 15.35 to 15.6 million, a change inside the uncertainty range, so the plan covers a smaller share of a larger population; worst-of-ten drought about 30.8 million against 27.6 population; sum of SA2 capacities 37% of the national figure (states 75%), barely changed since 2011. Shocks by region, run 2026-11-06 (`analysis/paper_a/README.md`): the national margin is 1.5 times in an average year, 1.12 at a 1-in-10 year and below 1 at 1 in 20 (0.95; 0.89 in 2011); about 80% of the population lives in over-capacity regions even in an average year; five regions tip over capacity at a 1-in-10 year in 2025 against one in 2011; a field-crop shock barely moves the short term (-0.3% at 24% lower yields) while a one-year grain store raises the long term 48%. Regional headline, recounted 2026-11-06 (`analysis/paper_a/README.md`): of nine short-term status flips on the corrected method only three are clean and robust (Mackay Whitsunday, North Tasmania, North East Victoria; three are land-definition artefacts and three are not robust to the 2025 range); of four long-term flips one is (South West Queensland); regions over capacity fall from 23 to 16 short term and 36 to 32 long term.

**Readers.** Land use planners and sustainability analysts, with population and environment researchers (sequel to Lane, Dawes and Grace 2015 and Lane 2017, *Population and Environment*).

**Type.** Quantitative results paper. Same model, same 60 zones, same method (frozen during the data refresh), data brought forward from 2011 to 2025.

**The questions.**
1. Which regions moved between under and over capacity between 2011 and 2025, by how much, and how much of the change is population, land use or yield (the data effect)?
2. What would a 100-year self-sufficiency plan (the long term) ask of each region, and how has that changed?
3. How do regional results hold under shocks (drought, a failed harvest, fuel, waste)?
4. How sure are the regional results: which flips survive the ranges, and which method choices move which regions?
5. How much of the national margin survives as the unit of self-sufficiency shrinks (the whole curve, national to SA2), and has that changed since 2011? Why do some partitions do worse (boundary effect)?

**Contribution beyond the earlier papers.** The 2015 and 2017 papers gave one data vintage and, for the long term, one national and regional picture. This paper brings the whole picture forward to 2025 with the method frozen; decomposes the change; gives the long term and the shock cases region by region; says which regional findings are robust; and takes four or five regions in depth.

## Sections

**1. Introduction.** (Highlight that the model is the author's own, as in Paper B.) The 2015 and 2017 findings, what was left open (change over time, robustness), the questions. Points to Paper B for the method comparison and the choice of method.

**2. Method and data in brief.** The frozen method, the 60 zones, the 2011 and 2025 data sets, the release chain (`methods/README.md`). One page; the full model and constants table belong to the supporting model paper. *Sources: `methods/`, `analysis/constants_audit/`.*

**3. The short-term picture, 2011 to 2025.** National capacity against population; region by region change; the status flips between over and under capacity. *Sources: `results/comparison_cells.csv`, `analysis/comparison_2025/movers.md`.*

**4. What drove the change.** The decomposition of the 2011 to 2025 change into population, land use and yield (the data effect), nationally and by region. *Sources: D4 decomposition, `results/comparison_cells.csv`.*

**5. The scale curve: where the margin goes.** Sum of capacities at state, NRM region, SA4, SA3 and SA2 level for both vintages; the boundary effect (landscape regions against NRM zones on identical data); why NRM regions do badly (rangeland pasture stranded from cropland); where the curve bends; the ideal contiguous split. Reads for shape, not for individual SA2s: SA2 units are administrative, the 2011 SA cells use 2020-21 land, and the state-yield basis is the conservative bound (a local-yield basis gives 54% against 37% at SA2). *Sources: `results/scale_curve.csv`, `analysis/scale_curve_2025/`, `analysis/regionalise_2025/`.*

**6. The mechanism.** Capacity is set by pairing pasture-fed food with crops; what a meat limit does to rangeland; dairy pasture quality. One short section. *Sources: `analysis/sensitivity_2025/`.*

**7. The long term: a 100-year plan.** (Run 2026-11-06: capacity 15.4 and 15.6 million against populations of 22.3 and 27.6, so the plan covers 69% then 57%; 36 then 32 regions over capacity and 94% of the population in them in both years; the weather allowance and liquid fuel are the largest settings. `analysis/paper_a/README.md`.) The long-term settings (100 years of weather, low-meat diet, no avoidable waste, full recycling, organic, almost no fossil liquid fuel, 30% reserve); what each setting is worth (the weather allowance is the largest single lever); long-term capacity by region in both vintages; which regions are over capacity in the long term. *Sources: `analysis/long_term_2025/`, `analysis/resilience_2025/`, the long-term preset of `results/<release>.csv`.*

**8. Shocks and food security by region.** Drought by return period (the worst year of 5, 10, 20, 50, 100), a failed harvest (field-crop yields down), a grain store of one or two years, liquid fuel, waste at the national target or none; which regions are exposed. *Sources: `results/scenarios.csv`, `analysis/reliability_2025/`, `analysis/resilience_2025/`.*

**9. How sure are the regional results.** (Run 2026-11-06, `analysis/paper_a/README.md`: the beef carcase correction lowers the short term 10% to 22% in the beef and cropping regions; dairy on good land moves regions both ways, -27% to +22%; the short-term count of over-capacity regions is the same under the published, corrected and improved tiers (15, 16, 15) but the long-term count is not (36, 32, 36): six southern and western regions change status. Figure 7 is the heat map, `analysis/paper_a/method_effects_heatmap.png`.) (a) Which status flips of section 3 hold across the 5th to 95th percentile ranges for each zone (the Monte Carlo method is described and tested in Paper B, section 6, and only used here). (b) The effect of each method choice region by region: each correction and improvement alone and in sequence, with the interaction; which regions are sensitive to which choice (the national reading of the same choices is in Paper B, section 6). *Sources: `results/ranges_*.csv`, `results/likely_range_*.csv`, `results/method_effects.csv`.*

**10. Regions in depth.** Four or five from the largest movers: a capital with hinterland, a Murray-Darling Basin region, south-west WA, Tasmania, an arid region. Each read through short term, long term, shocks and robustness. The 2015 migration map redrawn on current data. (Run 2026-11-07, `analysis/paper_a/regions_in_depth.md` and `regions_in_depth.csv`, `analysis/paper_a/migration_map.png`: the regions chosen on 2026-11-07 are Hawkesbury-Nepean-Sydney, the Murray region with Murrumbidgee-ACT, Avon, North Tasmania, and SA Arid Lands paired with the Eyre Peninsula; one table per region and a comparison table; North Tasmania is the clean flip, balanced at a 1-in-10 drought (capacity 1.000 times population) and over capacity at 1 in 100 (0.798); Murrumbidgee-ACT is under capacity in the average year (2.076) but over capacity in the long term (0.411) and at 1 in 100 (0.623); the SA Arid Lands change is a land-definition artefact (land layer alone 6.5 times), set beside the Eyre Peninsula, which has no flag; Hawkesbury-Nepean-Sydney carries the land-definition flag too (land layer alone 0.49). The migration map is proportional circles on region centroids because the repository holds no region polygons; the centroids are derived from SA2 centroids. Every figure is in the csv.) *Sources: `analysis/comparison_2025/movers.md`.*

**11. Discussion: what would widen the margin.** The ameliorative measures, tested one at a time on the model and read against what binds: livestock productivity and diet composition for the short term (livestock output +10% gives +9.6%; the meat and egg share to 5%, +85%; red to white meat, +56%; waste at the national target, +16%), the weather allowance for the long term (drought-proofing the worst year +57%; a one-year grain store +48%, two years +64%, equal to planning for a 16-year or 10-year drought instead of 100), and almost nothing from field-crop yields, irrigation or more cropland (0 to 2%); the regions as a pool (the national capacity is 1.6 to 1.8 times the sum of regional capacities, so trade in products between regions recovers 10 to 15 million people-equivalents); measures the model cannot carry (export diversion in a bad year, imports, aquaculture, insurance and finance, household and community stocks, population distribution, water) are discussed, not measured. *Sources: `analysis/paper_a/README.md`, `analysis/paper_a/measures.csv`, `papers/A_results/DISCUSSION_MEASURES.md`.*

**12. Limitations and conclusions.** What the model cannot carry (`DISCUSSION.md`); forced local self-sufficiency (gardens, fruit and vegetables, diet) as a limitation of the closed-region reading; the data and code availability statement. *Sources: `analysis/regionalise_2025/`.*

## Figures (to be scripts over `results/` when drafting begins)

1. National capacity against population, 2011 and 2025.
2. Region-by-region change and the status flips (map), with the flips that survive the ranges marked.
3. The decomposition of the change by region.
4. The scale curve, 2011 and 2025, to SA2.
5. The long term: what each setting is worth, and long-term capacity by region.
6. Exposure to shocks by region.
7. The effect of each method choice by region (heat map).
8. The 2015 migration map redrawn.

## Decided 2026-11-06

* **No reconciliation table.** Earlier published figures are not tabulated against the new ones; the correction notes carry that. The 2011 results appear as corrected only, with one footnote saying the original published values were updated.
* **2011 results: corrected only** (footnote as above).
* **The scale curve is in Paper A** (the Australian result, sequel to the 2015 scale paper); Paper B shows scale as a design choice with three points.
* **Two papers only.** The data paper is the archive with a DOI, not a journal paper.

## Division of labour with Paper B (proposed 2026-11-06, to confirm)

Paper B reads the model's design choices **nationally**, set against the other methods (what moves the number, which method for which purpose). Paper A reads the same choices **regionally** and over time (which regions move, which results are robust). The module-by-module regional effects, the zone-by-zone ranges (the Monte Carlo method itself is in B), the long term and the shock cases are here; B carries only the national effect of each choice as a design choice.

## Decisions still open

1. **Is this the right weight for Paper A?** Sections 7 to 9 are added to thicken it; they could instead form a short model paper.
2. **Journal.** *Population and Environment* is the plan.
3. **Authors and order,** and whether the correction notes go out first (later).
