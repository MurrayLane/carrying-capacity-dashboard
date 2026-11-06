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
Outline (draft 2026-11-03, Murray agreed the order of sections):
1. The corrected short-term picture: 33 million, not 40, and how it changed from 2011 to 2025 region by region (the data effect, the status flips: eight regions move from over to under capacity and one, Corangamite, the other way, short term on the corrected method), with the ranges.
2. Real boundaries: the scale curve on states, NRM regions and SA4, SA3, SA2 (the state-yield basis, monotone), and why the NRM regions do badly: rangeland pasture is stranded from cropland (SA Arid Lands 41 thousand against the SA4 that pairs it with the Eyre Peninsula, 1.7 million).
3. The mechanism in one paragraph: capacity is set by pairing pasture-fed food with crops; the best diet uses up both (the nation 118 million at 3% meat and eggs, all red); a meat limit strands rangeland; dairy pasture quality (improved against other pasture, with dairy on land that can support it).
4. One "what if" section: the ideal contiguous split (53 regions keep 76% of national capacity against 33% for the NRM zones, ignoring population), forced local self-sufficiency (gardens add little; fruit and vegetables are 7% of cropland; diet recovers most of the fine-scale loss), and the long term.
5. Reconciliation with the earlier papers (the table of what each published figure becomes, `ERRATA.md`) and limitations (`DISCUSSION.md`).

Corrections: the corrected releases lead, and the paper states the 2011 results as published and as
corrected (`ERRATA.md`), so it carries the reconciliation with the earlier papers. Whether the original
papers also get correction notes is Murray's decision (below).
Uses: A1 baseline (old data, old zones); B0, B0a, B0b, B0c; D2 zones; D3 result sets; D4 decomposition.
Submitted second, after the methods paper (see Order).
Venue: Population and Environment (sequel).

## Paper B (methods). A critical review of carrying capacity methods, tested on common Australian data

(Old papers 3 and 5; refocused by Murray 2026-11-06. Full outline: `papers/B_methods/OUTLINE.md`.)

Question: which carrying capacity method suits which purpose, and how much of the spread of published
estimates of Australia's capacity (9 to 100 million) is the definition, the diet or the method?
Type: a critical narrative review (not a systematic search protocol). Readers: land use planners and
sustainability analysts. It does not repeat the thesis (chapter 6) or *Land Use Policy* 2010, which already
review the planning-oriented methods; it adds the method families those did not cover (energy and protein
balance, commodity balance, people per hectare, the HALF index, Simpson et al. 2000, footprint critiques),
the literature since 2011, and **tests of the methods through the model on Murray's own 2011 and 2025
data** (each checked against its authors' figure where possible), the measured effect of each design
choice, and a guide to which method fits which purpose.
Moved out: the corrections, the improvements one at a time, the 2011 to 2025 decomposition and the
Monte Carlo ranges; their home (Paper A or a short model paper) is open.
Method tests scoped in the outline (nothing built): energy and protein balance (Gifford; Henry and
Godden), commodity balance (Foran and Poldy), land per diet (Alexander), people per hectare (Cassidy),
food-only footprint (Simpson), a failure-probability measure (Fearnside-style), and the Australian model.
Uses: `analysis/comparators_2025/`, `analysis/reliability_2025/`, the `Literature review/` library.
Submitted first of the two (see Order).
Venue: to be decided (Land Use Policy, Ecological Indicators, Environmental Science and Policy suggested).

## Supporting paper. The model and data as a citable resource

The open workbook, the SA2 data layer, grouping files and browser evaluator, archived
with a DOI. Holds the reproducibility material so the two papers stay short.
Uses: Workstream F, all rows.
Constants table (decided 2026-11-04): every Base-sheet constant lists its source from the source trace
(`analysis/constants_audit/source_trace/`); the few without one are declared as assumptions with their
sensitivity (seven edible portions: guava, kale, bok choy, crab, lobster, scallop, squid; under 0.15% nationally
for a 10% change), not searched for after the fact and not reported as errors.
Venue: Environmental Modelling and Software or Scientific Data.

## Not written separately

A sequel to the 2010 methodology review; its material is the methods paper's introduction.

## Order (decided by Murray 2026-11-02: methods first, then results)

1. **Supporting paper: archive the model and releases with a DOI** (SCOPE F3). Short; makes the releases citable by both papers.
2. **Correction notes** to the journals of the three most affected papers (Ecological Modelling 2014, Population and Environment 2015 and 2017) and the thesis repository, so the record is corrected before either new paper cites the old numbers. The facts are in `ERRATA.md` (checked line by line 2026-11-02); the wording is not drafted and whether to send is Murray's decision.
3. **Methods paper** (paper B): a critical review of carrying capacity methods tested on common Australian data (see Paper B above and `papers/B_methods/OUTLINE.md`); drafted from an outline, no prose until the outline is approved.
4. **Results paper** (paper A): 2011 to 2026 by region and scale, on the corrected releases, citing the methods paper for the tiers and the corrections. Drafted while the methods paper is under review; the writing is not serial, the submission is.

## How the platform feeds the papers and the dashboard (decided 2026-10-28)

* **Six cells.** Every comparison is read from the grid of data vintage (2011, 2025) by method tier (published, corrected, improved): releases `2011-corrected`, `2011-fixed`, `2011-improved`, `2025-mirror`, `2025-fixed`, `2025-improved` (`methods/README.md`). `results/comparison_cells.csv` has the correction effect, the improvement effect and the data effect separately; the two papers report these three, not one combined change, and lead with the corrected comparison.
* **One source of numbers.** `results/` (generated by `cd web && npm run results`) is read by the dashboard's change pages and by the papers. A table or figure in a paper is a script over `results/` with the release ids and the commit written beside it; no number is typed.
* **Freeze at submission.** When a paper is submitted, the releases it uses are frozen (`web/scripts/lock-release.mjs`), tagged and archived with a DOI (SCOPE F3). Later improvements are new releases, so the published numbers never change.
* **Per paper, when it is written:** a folder `papers/paperN/` with a manifest (releases, commit), the table and figure scripts, and the generated tables. Not created yet.
* **Discussion and limitations** come from `DISCUSSION.md`, the register of things the model cannot or should not carry (sketchy or missing figures included); a limitation found while working is added there at once, so the papers draw it from one place.
* **Biodiesel yield (SCOPE E17; the double count is confirmed from the thesis's own source, the decision to adopt is pending):** it changes the thesis's long-term figure (9.4 to 15.7 million on the 2011 data) and the data effect in the results paper (+4.6 to +1.9 million). Adopted as the first correction (2026-10-28): the results paper reports the 2011 long-term result as published and corrected, and both papers lead with the corrected releases `2011-fixed` and `2025-fixed`.
* **Second correction (2026-10-28, beef carcase yield):** lowers the short-term headline by about 18% (2011: 40.45 to 33.31 million), so the results paper's short-term level and the 2015 scale paper's national figure of about 40 million need a correction note; the 2011 to 2025 short-term increase is robust (+7.6 published, +6.2 corrected) while the long-term increase is not (+4.6 published, +0.6 corrected). Confirmed by Murray 2026-10-28 (kept); the wording of the correction note is still to be agreed. The errors, their evidence and size, and the publications they touch are registered in `ERRATA.md` (nothing drafted or sent; Murray will send them to publishers in time).
* **Ranges (full Monte Carlo rerun 2026-11-04, supersedes 2026-10-28):** on the corrected method the short-term increase since 2011 is outside the uncertainty (2011 corrected 33.3 million against a 2025 range of 35.9 to 45.1); the long-term increase is not (15.35 against 14.3 to 17.8), so the results paper reports the long-term change as not distinguishable from zero on the corrected method. On the improved method both increases are outside the range (2011 41.7 and 13.1 against 46.8 to 61.3 and 16.4 to 20.4); on the thesis method likewise (40.45 and 9.43 against 42.8 to 53.1 and 11.7 to 15.8). The earlier improved-cell ranges had a fault (see `analysis/sensitivity_2025/README.md`) and are not to be quoted.
