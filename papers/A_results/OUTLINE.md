# Paper A (results): Australia's carrying capacity, 2011 to 2025, by region

Outlined 2026-11-06 from the plan in `PUBLICATIONS.md` (sections agreed 2026-11-03; scale curve in Paper A again 2026-11-06 once each paper had a narrative). This is an outline only: it fixes the structure, what each section answers and the files it would draw on. No results are stated and no tables or prose have been built.

**Working title:** Australia's carrying capacity, 2011 to 2025: what changed, where, and how sure we can be. *(To revisit with Murray.)*

**Narrative (Murray asked for a story to drive each paper, 2026-11-06).** *Claim:* between 2011 and 2025 the national food margin held, the long-term margin shrank, a drought year leaves little room, and the margin sits where the people are not. *Arc:* (1) the comfortable headline, about 1.5 times the population in both years; (2) production grew in step with people but in different places: capacity inland (basin, cropping belts, rangelands), people on the coast, and the scale curve to SA2 shows how much of the national margin dissolves at fine scale; (3) the comfort depends on the weather: the worst of ten years leaves a thin margin, and a 100-year self-sufficient plan has slipped from about 69% to about 57% of the population; (4) which regional results survive the ranges and the land-definition checks; (5) regions in depth. *Takeaway for planners:* the national margin is not safe, it held because production grew where the people are not.
**Headline (corrected releases, 2011 on `2011-fixed-3`; revised under B117).** Short-term capacity about 1.5 times population in both years (33.3 against 22.3 million in 2011; 41.5 against 27.6 in 2025). On the average of every ordering of the data layers the consumption and red-meat-mix layers (the diet with less beef) add 5.6 million of the 8.2 million rise and land with livestock 2.4 million (the two layers share one grazing area); forward and reverse walks are the two ends of the chain, and in the long term the average can lie outside both. Long term 15.35 to 15.6 million, so the plan covers a smaller share of a larger population (69% then 57%); the 2011 figures lie inside the 2025 ranges (31.1 to 49.2 million short term, factor 1.58; 13.3 to 18.8 long term), so the comparison is at fixed settings, not a test across them. At the base settings the worst of ten years leaves 30.8 million against 27.6 million (1.12 times) and a 1-in-20 year leaves 26.3 (0.95 times), on a weather allowance that is a cereal factor, but the widened Monte Carlo ranges (23.1 to 36.5 and 19.7 to 31.2 million) contain the population (37% and 78% of draws below it); the failure probability at the 2025 population is 2.3% to 19.4% a year across the widened draws (median 7.6%). Sum of SA2 capacities 37% of the national figure on state yields (states 75%), barely changed since 2011, because the model's cropland can carry pasture-fed food but pasture cannot carry crops. About 82% of the 53 regions' population lives in over-capacity regions even in an average year; five regions tip over capacity at a 1-in-10 year in 2025 against three in 2011. Of eight short-term status flips on the corrected method none is robust and free of an artefact flag on the 19-choice regional ranges (seven are not robust; three are land-definition artefacts); of three long-term flips one is (South West Queensland); regions over capacity fall from 22 to 16 short term and 35 to 32 long term. A field-crop shock barely moves the short term (-0.2% at 24% lower yields) while a one-year grain store raises the long term 48%.

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

* **A1.1 Australian population debate and planning.** The paper starts from the debate about how many people Australia can plan for, 2011 to 2025. (added 2026-11-11, decision 52)
* **A1.4 Food security in Australian planning and policy.** Regional food self-sufficiency and food security appear in Australian planning and policy, which is why a regional capacity result matters. (added 2026-11-11, decision 52)
* **A1.5 Observed drought and climate effects on Australian farming.** Drought and climate variability have affected Australian farming since 2011, which is the weather dependence the margin is tested against. (added 2026-11-11, decision 52)

**2. Method and data in brief.** The frozen method, the 60 zones, the 2011 and 2025 data sets (the regional populations are the ABS estimated resident population in both years), the cereal weather allowance, the release chain (`methods/README.md`). One page; the model summary, the data sources by year and Table S1 are in the supplement. *Sources: `methods/`, `analysis/constants_audit/`.*

**3. The short-term picture, 2011 to 2025.** National capacity against population; region by region change; the status flips between over and under capacity. *Sources: `results/comparison_cells.csv`, `analysis/comparison_2025/movers.md`.*

**4. What drove the change.** The decomposition of the 2011 to 2025 change into land, crop yields, livestock, consumption and the red meat mix (population changes status, not capacity), nationally and by region: the average over all 362,880 orderings as the main figures, the forward and reverse walks as the two ends of the chain, land and livestock read together because the 2025 livestock yields divide output by the land layer's grazing area. *Sources: `analysis/comparison_2025/capacity_by_cause_corrected_orders.csv`, `results/comparison_cells.csv`.*

**5. The scale curve: where the margin goes.** Sum of capacities at state, NRM region, SA4, SA3 and SA2 level for both vintages on the state-yield basis (the one basis in the main text; the own-yield bound, 54% against 37% at SA2, is one sentence and a supplementary table); the substitution rule behind the loss; the boundary effect (landscape regions against NRM zones on identical data); why NRM regions do badly (rangeland pasture stranded from cropland); where the curve bends; the ideal contiguous split. Reads for shape, not for individual SA2s: SA2 units are administrative and the 2011 SA cells use 2020-21 land. *Sources: `results/scale_curve.csv`, `analysis/scale_curve_2025/`, `analysis/regionalise_2025/`.*

**6. The mechanism.** Capacity is set by pairing pasture-fed food with crops; what a meat limit does to rangeland; dairy pasture quality. One short section. *Sources: `analysis/sensitivity_2025/`.*

**7. The long term: a 100-year plan.** (Run 2026-11-06: capacity 15.4 and 15.6 million against populations of 22.3 and 27.6, so the plan covers 69% then 57%; 36 then 32 regions over capacity and 94% of the population in them in both years; the weather allowance and liquid fuel are the largest settings. `analysis/paper_a/README.md`.) The long-term settings (100 years of weather, low-meat diet, no avoidable waste, full recycling, organic, almost no fossil liquid fuel, 30% reserve); what each setting is worth (the weather allowance is the largest single lever); long-term capacity by region in both vintages; which regions are over capacity in the long term. *Sources: `analysis/long_term_2025/`, `analysis/resilience_2025/`, the long-term preset of `results/<release>.csv`.*

**8. Shocks and food security by region.** Drought by return period (the worst year of 5, 10, 20, 50, 100), a failed harvest (field-crop yields down), a grain store of one or two years, liquid fuel, waste at the national target or none; which regions are exposed. *Sources: `results/scenarios.csv`, `analysis/reliability_2025/`, `analysis/resilience_2025/`.*

**9. How sure are the regional results.** (Revised under B117: the national range is the widened 19-choice range, 31.1 to 49.2 million, with the herd-cycle range 39.4 to 43.8; the flip tests keep the 13-choice zone ranges; the "rise holds" sentence follows decision 115.) (Run 2026-11-06, `analysis/paper_a/README.md`: the beef carcase correction lowers the short term 10% to 22% in the beef and cropping regions; dairy on good land moves regions both ways, -27% to +22%; the short-term count of over-capacity regions is the same under the published, corrected and improved tiers (15, 16, 15) but the long-term count is not (36, 32, 36): six southern and western regions change status. Figure 7 is the heat map, `analysis/paper_a/method_effects_heatmap.png`.) (a) Which status flips of section 3 hold across the 5th to 95th percentile ranges for each zone (the Monte Carlo method is described and tested in Paper B, section 6, and only used here). (b) The effect of each method choice region by region: each correction and improvement alone and in sequence, with the interaction; which regions are sensitive to which choice (the national reading of the same choices is in Paper B, section 6). The paper will label five range ends as the author's judgement (the meat-window three-way choice, the meat-and-egg low end 0.115, the red-meat low end 0.528, the 50/50 weight on the leave-one-out resilience table, the long-term benchmark low end 0.30). *Sources: `results/ranges_*.csv`, `results/likely_range_*.csv`, `results/method_effects.csv`.*

**10. Regions in depth.** Four or five from the largest movers: a capital with hinterland, a Murray-Darling Basin region, south-west WA, Tasmania, an arid region. Each read through short term, long term, shocks and robustness. The 2015 migration map redrawn on current data. (Run 2026-11-07, `analysis/paper_a/regions_in_depth.md` and `regions_in_depth.csv`, `analysis/paper_a/migration_map.png`: the regions chosen on 2026-11-07 are Hawkesbury-Nepean-Sydney, the Murray region with Murrumbidgee-ACT, Avon, North Tasmania, and SA Arid Lands paired with the Eyre Peninsula; one table per region and a comparison table; North Tasmania is the clean flip, balanced at a 1-in-10 drought (capacity 1.000 times population) and over capacity at 1 in 100 (0.798); Murrumbidgee-ACT is under capacity in the average year (2.076) but over capacity in the long term (0.411) and at 1 in 100 (0.623); the SA Arid Lands change is a land-definition artefact (land layer alone 6.5 times), set beside the Eyre Peninsula, which has no flag; Hawkesbury-Nepean-Sydney carries the land-definition flag too (land layer alone 0.49). The migration map is proportional circles on region centroids because the repository holds no region polygons; the centroids are derived from SA2 centroids. Every figure is in the csv.) *Sources: `analysis/comparison_2025/movers.md`.*

**11. Discussion: what would widen the margin.** The ameliorative measures, tested one at a time on the model and read against what binds: **A11.1 Livestock productivity.** livestock productivity and diet composition for the short term (livestock output +10% gives +9.7%; the meat and egg share to 5%, +85%; red to white meat, +56%; **A11.3 Food waste.** waste at the national target, +16%), the weather allowance for the long term (**A11.5 Drought resilience.** drought-proofing the worst year +60%; **A11.4 Grain reserves.** a one-year grain store +48%, two years +64%, equal to planning for a 16-year or 10-year drought instead of 100), and almost nothing from field-crop yields, irrigation or more cropland (0 to 2%); **A11.6 Interregional freight and food supply chains.** the regions as a pool (the national capacity is 1.6 to 1.8 times the sum of regional capacities, so trade in products between regions recovers 10 to 15 million people-equivalents); **A11.7 Import dependence.** measures the model cannot carry (export diversion in a bad year, imports, aquaculture, insurance and finance, household and community stocks, population distribution, water) are discussed, not measured. *Sources: `analysis/paper_a/README.md`, `analysis/paper_a/measures.csv`, `papers/A_results/DISCUSSION_MEASURES.md`.*

**12. Limitations and conclusions.** What the model cannot carry (`DISCUSSION.md`); **A12.1 Self-sufficiency as a policy concept.** forced local self-sufficiency (**A12.2 Urban agriculture.** gardens, fruit and vegetables, diet) as a limitation of the closed-region reading; the data and code availability statement. *Sources: `analysis/regionalise_2025/`.*

* **A12.3 Water for food.** The model does not carry water as a limit on food production; the limitations say so. (added 2026-11-11, decision 52)
* **A12.4 Fuel and energy in food production.** The model does not carry fuel and energy for growing and moving food beyond its liquid fuel setting; the limitations say so. (added 2026-11-11, decision 52)

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

## Revised under B117 (2026-11-18)

Decisions 100 to 104, 111 and 115 to 117 were applied to the section files: 2011 on `2011-fixed-3`; the decomposition as an all-orderings average; the shocked ranges and the cereal basis named; the widened range; one yield basis; the projections compared with capacity; Table S1, the data sources, a model summary and the failure probability in the supplement; uncited references removed from the claims files. `SECTION_SCOPE.md` records the changes by section and the claims csvs name the report and checker for every figure.

## Decisions still open

1. **Is this the right weight for Paper A?** Sections 7 to 9 are added to thicken it; they could instead form a short model paper.
2. **Journal.** *Population and Environment* is the plan.
3. **Authors and order,** and whether the correction notes go out first (later).

## Revised under B141a (2026-11-18)

Decisions 134 to 140, 149 and 150 were applied to the section files, supplement, abstract and highlights: regional ranges on all 19 choices (no short-term flip robust); paired 2011 and 2025 draws (short-term rise in every paired draw, long-term change not established); 2011 on the 2025 weather table; the 5.8% replaced by its range; land and livestock as one layer (eight layers); the meat balance as a consistency check; drought-factor variants; reference-period table, projections, partition effect, diet window and 2011 subsets; national 2011 row as the regional sum; one ratio, capacity over population; the long-term preset renamed and defined; section 11 shortened with its detail in Supplementary Section S6.
