# Publication strategy

Status: saved 2026-10-25; consolidated 2026-11-02 (Murray: the data was being stretched too thin across
five papers). **Two papers and a data paper:** one for results, one for methods, and the supporting
resource. Papers come out of the results files the scope produces; none needs work outside SCOPE.md
once Workstreams E and F are in it. The results paper uses the data refresh with the method frozen
(SCOPE D1); the methods paper uses the method changes compared one at a time against that frozen
baseline. Earlier numbering, for tracing: old papers 1, 2, 4 are the results paper; old papers 3 and
5 are the methods paper; the nutrition and diet work (E11, E16) is held back, to become a third
paper or a section of the methods paper once these two are written. (2026-11-02: it is now one of the options in the methods paper.)

Prior work this builds on, all with 2005 to 2011 data and the fixed 60-zone geography:
Lane 2010 Land Use Policy (methodology review); Lane 2011 Urban Design (planning
argument); Lane and Dawes 2013 Urban Environment (regional case studies); Lane, Dawes
and Grace 2014 Ecological Modelling (essential parameters); Lane 2014 thesis (full
method, the reference for everything here); Lane, Dawes and Grace 2015 Population and
Environment (scale); the time-frames paper (ePrints 99790); Lane 2015 IAFOR (policy).

## Paper A (results). Australia's carrying capacity, 2011 to 2026, by region and scale

(Old papers 1, 2 and 4.)

Question: same model, same 60 zones, data brought forward 15 years. Which regions moved between under
and over capacity, by how much, and how much of the change is population, land use or yield (the data
effect, read from the corrected releases `2011-fixed` and `2025-fixed`)? How does capacity fall as the
unit of self-sufficiency shrinks: the 2015 paper had three points (national 40 million, states 28 million,
regions 23 million; on the corrected method 33.3, and 21.0 summed over regions); give the whole curve,
national to SA3, on current data, and separate the boundary effect (landscape regions versus 2011 NRM
zones on identical data) from the scale effect. Where does the curve bend: excess pasture, or cities
without hinterland? Four or five regions in depth chosen from the largest movers (a capital with
hinterland, a Murray-Darling Basin region, south-west WA, Tasmania, an arid region); the 2015 migration
map redrawn.
Scale curve and ideal split (decided 2026-11-02, Murray; `analysis/regionalise_2025/`: a contiguous split of 53 regions can keep 76% of the national capacity against 33% for the NRM zones):
Scale curve (decided 2026-11-02, Murray): the sum of capacities at state, NRM region, SA4, SA3 and SA2 level for both vintages, from `results/scale_curve.csv`, with the boundary effect noted (`analysis/scale_curve_2025/`).
Corrections: the corrected releases lead, and the paper states the 2011 results as published and as
corrected (`ERRATA.md`), so it carries the reconciliation with the earlier papers. Whether the original
papers also get correction notes is Murray's decision (below).
Uses: A1 baseline (old data, old zones); B0, B0a, B0b, B0c; D2 zones; D3 result sets; D4 decomposition.
Submitted second, after the methods paper (see Order).
Venue: Population and Environment (sequel).

## Paper B (methods). Why estimates of carrying capacity differ, and how sure we can be

(Old papers 3 and 5.)

Question: which of the 2014 paper's assumptions carried and which did not, and how far is the spread of
published estimates of Australia's capacity (9 to 100 million) the definition, the diet or the method?
Part 1, the model: each change tested alone against the frozen baseline and reported as its effect on
national and regional capacity: the corrections (biodiesel yield, beef carcase yield) and the improvements
(reserve land shared pro rata, recycling by stage, Australian loss factors `loss-factors-australia`,
regional beef output, organic yield of grazing ruminants), spatial pasture productivity, a water ceiling on
irrigation, a non-stationary climate series (absorbs the time-frames sequel), an energy-to-yield link; the
Monte Carlo ranges (full run at freeze). Framing: lead with affordability, supply chains and climate as
the energy constraint, not the 2007 to 2013 peak-oil literature; keep every energy parameter.
Part 2, the comparison: the verified register of other estimates and the model re-run under each
definition (`analysis/comparators_2025/README.md`; sections 2, 2b and 3b): energy-balance estimates
(Gifford 1975, Henry and Godden 1995, CSIRO and UQ 2025, Bellotti 2017, industry), the Jones inquiry's
50-plus and 30 to 35 million (the model's average year and 10-year drought allowance), integrated resource
models (Foran and Poldy 2002), ecological footprint studies (Lenzen and Murray 2001, Simpson et al. 2000, the
National Footprint Accounts), and land-and-diet models elsewhere (Peters 2016, Alexander 2016, Cassidy 2013).
If the paper grows too long, Part 2 moves to the results paper's discussion.
Included as one of the options (decided 2026-11-02): the nutrition-constrained model (E11; `analysis/nutrition_lp_2025/`), the diet that feeds the most
people from Australia's land; regional diets (E16) only as a limitation, the work being parked.
Uses: Workstream E, all rows; E11, E12, E16, E18; `analysis/comparators_2025/`.
Submitted first of the two (see Order).
Venue: Ecological Modelling.

## Supporting paper. The model and data as a citable resource

The open workbook, the SA2 data layer, grouping files and browser evaluator, archived
with a DOI. Holds the reproducibility material so the two papers stay short.
Uses: Workstream F, all rows.
Venue: Environmental Modelling and Software or Scientific Data.

## Not written separately

A sequel to the 2010 methodology review; its material is the methods paper's introduction.

## Order (decided by Murray 2026-11-02: methods first, then results)

1. **Supporting paper: archive the model and releases with a DOI** (SCOPE F3). Short; makes the releases citable by both papers.
2. **Correction notes** to the journals of the three most affected papers (Ecological Modelling 2014, Population and Environment 2015 and 2017) and the thesis repository, so the record is corrected before either new paper cites the old numbers. The facts are in `ERRATA.md` (checked line by line 2026-11-02); the wording is not drafted and whether to send is Murray's decision.
3. **Methods paper** (paper B): the options for assessing carrying capacity (the typology of the thesis, section 6: global and local, resource-based, footprint, energy-balance, nutrition-limited), the corrections and improvements each tested alone, the ranges, and the comparison with other published estimates. Scope: only what is finished (the two corrections; the five improvements; the climate scenarios; the Monte Carlo ranges at freeze; the comparison with published estimates; the nutrition-limited model as one of the options). Unfinished items (a water ceiling on irrigation, the energy-to-yield link) go in its limitations. Post a preprint when submitted, so the results paper can cite it.
4. **Results paper** (paper A): 2011 to 2026 by region and scale, on the corrected releases, citing the methods paper for the tiers and the corrections. Drafted while the methods paper is under review; the writing is not serial, the submission is.

## How the platform feeds the papers and the dashboard (decided 2026-10-28)

* **Six cells.** Every comparison is read from the grid of data vintage (2011, 2025) by method tier (published, corrected, improved): releases `2011-corrected`, `2011-fixed`, `2011-improved`, `2025-mirror`, `2025-fixed`, `2025-improved` (`methods/README.md`). `results/comparison_cells.csv` has the correction effect, the improvement effect and the data effect separately; the two papers report these three, not one combined change, and lead with the corrected comparison.
* **One source of numbers.** `results/` (generated by `cd web && npm run results`) is read by the dashboard's change pages and by the papers. A table or figure in a paper is a script over `results/` with the release ids and the commit written beside it; no number is typed.
* **Freeze at submission.** When a paper is submitted, the releases it uses are frozen (`web/scripts/lock-release.mjs`), tagged and archived with a DOI (SCOPE F3). Later improvements are new releases, so the published numbers never change.
* **Per paper, when it is written:** a folder `papers/paperN/` with a manifest (releases, commit), the table and figure scripts, and the generated tables. Not created yet.
* **Discussion and limitations** come from `DISCUSSION.md`, the register of things the model cannot or should not carry (sketchy or missing figures included); a limitation found while working is added there at once, so the papers draw it from one place.
* **Biodiesel yield (SCOPE E17; the double count is confirmed from the thesis's own source, the decision to adopt is pending):** it changes the thesis's long-term figure (9.4 to 15.7 million on the 2011 data) and the data effect in the results paper (+4.6 to +1.9 million). Adopted as the first correction (2026-10-28): the results paper reports the 2011 long-term result as published and corrected, and both papers lead with the corrected releases `2011-fixed` and `2025-fixed`.
* **Second correction (2026-10-28, beef carcase yield):** lowers the short-term headline by about 18% (2011: 40.45 to 33.31 million), so the results paper's short-term level and the 2015 scale paper's national figure of about 40 million need a correction note; the 2011 to 2025 short-term increase is robust (+7.6 published, +6.2 corrected) while the long-term increase is not (+4.6 published, +0.6 corrected). Confirmed by Murray 2026-10-28 (kept); the wording of the correction note is still to be agreed. The errors, their evidence and size, and the publications they touch are registered in `ERRATA.md` (nothing drafted or sent; Murray will send them to publishers in time).
* **Ranges on the corrected method (2026-10-28):** the short-term increase since 2011 is outside the uncertainty (2011 corrected 33.3 million against a 2025 range of 34.7 to 43.5); the long-term increase is not (15.35 against 13.6 to 16.8), so the results paper should report the long-term change as not distinguishable from zero on the corrected method (`analysis/sensitivity_2025/README.md`).
