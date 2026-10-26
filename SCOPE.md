# Scope of work: static rebuild and data refresh

Status: scoped 2026-10-25, not started. Sizes are quick, small or session-size.
Rows marked DECIDE need a call from Murray before that row starts.

## Objectives

1. Make the dashboard current and relevant: data brought forward from 2005 to
   2011 vintages to current sources, run with no server at no monthly cost, from a
   repository Murray controls, keeping the thesis method (Lane 2014, chapter 8).
2. Compare the new output with the old. This needs the thesis's 60 zones (52
   NRM regions as drawn in 2011, 7 state groups, Australia) reconstructed from
   SA2s so that new data can be run on old boundaries, and it needs the method
   held constant while the data changes.

Objective 2 sets the order: data refresh first with the workbook formulas frozen,
comparison recorded, then any method changes (B7, B8) as a separate, separately
compared step. One thing changes at a time.

## Workstream A: static rebuild

The model workbook uses five Excel functions (IF, SUM, LOOKUP, AVERAGE, AND) in
7,444 formulas. A feasibility test on 2026-10-25 evaluated it in HyperFormula
with zero mismatches against the original servlet across 18 recorded cases, about
30 ms per recalculation. The workbook stays the editable model; the browser does
the arithmetic.

| # | Item | Size | Notes |
|---|------|------|-------|
| A1 | Extend the regression baseline to all 60 regions x 2 presets (120 cases) from the Java servlet while it still exists | quick | Run before anything else. It is the acceptance test for A2 to A5 and, kept permanently as `baseline_2011.json`, it is the complete output of the old version for objective 2 **Done: `baseline/`** |
| A2 | Build step: workbook to `model.json` (cells, formulas, LOOKUP rewritten to INDEX/MATCH, blank-as-zero) | small | Node script, runs in the Action; reads the .xls directly, no LibreOffice **Done: `web/scripts/build-data.mjs`** |
| A2a | Move regional data out of the workbook: the Yield sheet's one-column-per-region block and the Settings default rows become `regions.json`; the evaluator injects the selected region's yield vector and land areas at evaluation time | small | Removes the 60-region cap and the .xls 256-column limit; the workbook keeps only the method. Prerequisite for B0's drill-down **Done: `regions.json`, yield vector injected per region** |
| A3 | Browser evaluator: load `model.json` into HyperFormula, write the 24 inputs, read B76, C84:D89, B91:E107 | small | Same contract as `CarryingCapacityModel.java` **Done: `web/src/model/`, runs in a Web Worker** |
| A4 | Front end rebuilt per `DELIVERY.md`: Where / What if / So what layout, native sliders with 2011 and current markers, presets, editable land areas | small | Help text carried over from the 2011 page **Done: `web/src/`** |
| A4a | **Deferred.** Map: D3-geo TopoJSON per level, click to select, search, layer switch (current regions, 2011 zones, states, Australia), drill-down to SA3, live choropleth of the scenario result | session-size | Needs B0a and D2 grouping files; can start with the 2011 zones |
| A4b | Scale panel (region alone versus sum of sub-regions), land reallocation chart, diet components panel | small | Outputs the model already computes **Done: scale panel, land use, diet panels** |
| A4c | Scenario URL state, copy link, CSV download with vintages | quick **Done: hash state, copy link, CSV** |
| A4d | Methods, Changes since 2011 and About pages generated from the Sources sheet and the D4 results | small | Changes page depends on D4 **Done: Methods, Since 2011 (placeholder until D4) and About** |
| A5 | JS regression test against the 120-case baseline, run in the Action | quick | Tolerance 0.015 absolute **Done: `web/test/baseline.test.js`, 120/120 within 0.015** |
| A6 | Charts in inline SVG, replacing the 2011 Flot pie plugin that draws one slice | small | Donuts kept for continuity; see DELIVERY.md **Done: stacked and horizontal bars rather than donuts (a donut with more than six segments does not read)** |
| A7 | Hosting: publish the built site from the Action to GitHub Pages; custom domain and HTTPS | quick | DECIDE: domain (carryingcapacity.com.au ownership, or a new name) **Done: workflow in `.github/workflows/pages.yml`; needs Pages enabled (Settings, Pages, Source: GitHub Actions) and the domain decision** |
| A8 | Retire the Java and Docker path once A5 passes on the static build | quick | DECIDE: delete, or keep under a tag as reference **Done: Java path removed from main; kept on branch `legacy-java`** |

Deliverable: the dashboard live at the chosen domain, served as static files,
rebuilt automatically on every push.

## Workstream B: data refresh

Two constraints shape the order. First, the 52 sub-state regions use 2000s NRM
boundaries that no longer exist; regional data cannot be refreshed one for one
until the geography is remapped. Second, the ABS ceased the agricultural census
and the Agricultural Commodities series after 2021-22, so 2020-21 is the last
year with crop data by region.

| # | Item | Size | Source | Notes |
|---|------|------|--------|-------|
| B0 | DECIDED 2026-10-25: SA2 is the base unit. Every regional layer (land use, protected area, population, crop production and area, irrigated area) is stored per SA2 and aggregated on demand. Regions shown to users are groupings of SA2s. NRM regions drop out as a data unit; a later NRM-approximation layer is possible but not planned | decided | ABS ASGS Edition 3 SA2 (2021); ABS crop estimates are built at SA2 and sum exactly upward | Yields are always recomputed from summed production and summed area at the display level, never averaged from SA2s, because SA2 crop cells are modelled and partly suppressed |
| B0a | Define the display regions: group SA2s into roughly 60 to 90 regions, each a population centre with its productive hinterland, edges following catchment divides where the SA2 mosaic allows (thesis 7.10). Capitals include their hinterland. Deliver as `regions.json` mapping region to SA2 list, plus a map for review | session-size | SA2 boundaries; BoM river basins or NRM boundaries as the catchment guide | Murray reviews the map before B1 to B3 are summed onto it. This replaces the 52 thesis regions |
| B0b | Drill-down below display regions stops at SA3 (exact sums of SA2s) | quick | | Below SA3 crop yields are not reliable |
| B0c | Scale toggle on the page: "this region alone" versus "its regions summed", so the thesis 9.4 scale effect is visible | small | | National figure remains as the backdrop |
| B0d | DECIDE: drop the state scale as thesis 10.1.10 suggested, or keep it as a comparison layer | decision | | |
| B1 | Land areas by region: cropping, pasture, non-agricultural, infrastructure, reserve | session-size | ABARES Catchment Scale Land Use, Dec 2023 (50 m raster, CC BY); CAPAD 2024 | One GIS pass. Needs the ALUM v8 class to five-class mapping written down to match thesis 8.2 |
| B2 | Population by region | quick | 2021 Census by NRM region, or 2024-25 ERP aggregated from SA2 | Replaces 2011 figures that were partly from a 2007 journal article |
| B2a | Yield conversion test: rebuild 2006 to 2010 regional average yields from the archived ABS cubes, apply the thesis's seed adjustments, and fit the zero-irrigation conversion against the workbook's stored yields | small | ABS 7121.0 2007-08 to 2009-10 and 7125.0 2005-06 and 2006-07 data cubes | Replaces the lost "Fix irrigation figures" files; result goes in `analysis/yield_conversion/`. Gate for B3. DONE 2026-10-26: consistent with the thesis rule (seed deducted in t/ha, divide by 1 + 0.55 x irrigation share) but cannot exclude zero; sensitivity national -0.4%, worst region -13%; see `analysis/yield_conversion/README.md` |
| B3 | Crop yields, about 140 commodities by region, five-year average | session-size, the largest row | ABS Agricultural Commodities 2016-17 to 2020-21 by NRM region | Commodity names changed; missing cells use the thesis equation (national yield x regional cereal ratio); re-apply the dryland adjustment recorded in the workbook log Apply the B2a-inferred conversion like for like; sensitivity feeds F4 |
| B4 | National scalars: liquid fuel per person, biofuel share, timber per person and per hectare, textiles per person and fibre shares, organic share, climate variability series | small in total | Australian Petroleum Statistics; ABARES Forest and Wood Products Statistics; FAO/ICAC fibre data; Australian Organic Market Report; ABARES crop reports | Each is a single figure or short series |
| B5 | Infrastructure m2 per person and nature reserve share per region | quick | Derived from B1 and B2 | |
| B6 | Diet, phase 1: rescale food groups | small | ABS National Nutrition and Physical Activity Survey 2023, published tables | |
| B7 | Moved to E7 | | | Method change; waits for the comparison |
| B8 | Moved to E4 | | | Method change; waits for the comparison |
| B9 | Short-term and long-term default sets re-derived per thesis 8.4; sources recorded in a new Sources sheet; log sheet updated; baseline regenerated | small | | Closes each data row |

Deliverable per row: the workbook, CSV presets and baseline updated together in
one commit, with the source and vintage written in the Sources sheet.

## Workstream D: comparison with the old version

| # | Item | Size | Notes |
|---|------|------|-------|
| D1 | Freeze the method: no formula changes in the workbook during the data refresh. Changes to waste factors (B8) and item-level diet (B7) wait until D4 is recorded | rule | Otherwise data and method effects cannot be separated |
| D2 | Reconstruct the thesis's 60 zones as SA2 groupings: the 2011 NRM boundaries (ABS ASGS 2011 non-ABS structures), with the thesis merges applied (ACT into Murrumbidgee, Torres Strait into Cape York, Sydney Metro into Hawkesbury-Nepean), plus 7 state groups and Australia. Assign straddling SA2s by farmland share. Deliver `zones_2011.json` and a map showing the SA2 approximation against the original lines | small | States and Australia are exact; NRM 2011 is approximate at boundary SA2s, which the map shows |
| D3 | Run the refreshed data on the 2011 zones and on the new display regions. Three result sets: old data on old zones (A1 baseline), new data on old zones (data effect), new data on new regions (boundary effect) | quick once B rows land | Both presets, all zones |
| D4 | Comparison report: per zone, old and new carrying capacity, current population then and now, over or under capacity then and now, and a split of the change into population change, land-area change and yield change (hold two of the three at old values, vary one) | small | Published as a page in the site and a CSV; this is the record objective 2 asks for |
| D5 | DECIDED 2026-10-25: expose a "2011 zones" layer in the dashboard's region chooser, so a visitor can see the thesis regions with new data and switch to the current regions | quick | Follows D4 |

## Workstream E: method updates (after D4 is recorded; each compared alone against the frozen baseline)

Feeds PUBLICATIONS.md paper 3. No row starts until D1 is lifted by D4 being recorded.

| # | Item | Size | Source | Notes |
|---|------|------|--------|-------|
| E1 | Spatial pasture productivity: replace the regional stock-count average with stocking-rate or pasture-growth rasters summed per SA2 | session-size | ABARES and CSIRO pasture and livestock density products | The largest lever: red meat is 83 percent of food land in the national default |
| E2 | Water ceiling on irrigation: cap irrigable share by regional water availability and entitlements | small | ABS Water Account; Basin Plan entitlements | Closes the unconstrained 55 percent uplift |
| E3 | Non-stationary climate: extend the detrended grain series to 2024 and add a trend or projection adjustment to yields | small | ABS and ABARES historical yields; climate projections | Absorbs the time-frames sequel |
| E4 | Australian loss and waste factors replacing the US figures (B8 moves here) | small | National Food Waste Baseline | DECIDE: adopt |
| E5 | Organic yield penalty from the 2012 and 2015 meta-analyses | quick | Seufert et al.; Ponisio et al. | |
| E6 | Energy-to-yield link: yields respond to fuel and fertiliser availability, so the fuel and organic sliders test a constrained-energy future | small | Literature on input intensity and yield | DECIDE: include; the thesis notes the effect but does not model it |
| E7 | Item-level diet refresh (B7 moves here) | session-size | NNPAS 2023 microdata; FSANZ composition | DECIDE |

## Workstream F: publication support

Feeds the supporting paper and the reviewers of papers 1 to 4.

| # | Item | Size | Notes |
|---|------|------|-------|
| F1 | Scripted data pipeline from source files to SA2 layers and grouping files, with each source release pinned by URL, date and checksum | small | Lives in the repository; runs in the Action |
| F2 | Sources sheet in the workbook and `SOURCES.md` generated from it: dataset, release, vintage, licence, how it enters the model | quick | Also feeds the Methods page (A4d) |
| F3 | Archived release with a DOI for each paper's result set | quick | Zenodo from a GitHub release |
| F4 | Uncertainty: sensitivity of results to yield relative standard errors and to the SA2 approximation of 2011 zone boundaries | small | Reported in D4 and in the supporting paper |
| F5 | Licences settled (C3) so the resource paper can state them | decision | |

## Workstream C: ownership and presentation

| # | Item | Size | Notes |
|---|------|------|-------|
| C1 | Branding: replace QUT logos, header links and the QUT blog link | quick | DECIDE: what name and attribution appear; the thesis citation stays |
| C2 | Remove `forum.jsp` and the Facebook comments embed | quick | DECIDE: replacement contact route, or none |
| C3 | Licence files: code and model | quick | DECIDE: for example MIT for code, CC BY 4.0 for the model and data |
| C4 | Analytics | quick | DECIDE: none, or a cookie-free counter |

## Order and dependencies

1. A1 first; it is cheap and needs the Java app that A8 removes.
2. A2 to A8 are independent of B and produce a live site with the current data.
3. B0 is decided. B0a (region map) before B1 to B3 are summed onto regions; B1 and B2 can be computed at SA2 in parallel with B0a. B4 any time.
4. C rows ride along with A4.
5. E rows only after D4 is recorded. F1 and F2 run with the first B rows; F3 at each paper; F4 with D4.
6. D1 applies from the first B commit. D2 can be built with B0a in the same GIS pass. D3 and D4 follow the last data row; D5 after D4.

## Related documents

DELIVERY.md (online delivery design), PUBLICATIONS.md (publication strategy).

## Decisions

Accepted 2026-10-26: all recommendations in the decision review, as follows.

| Row | Decision |
|-----|----------|
| A7 domain | carryingcapacity.com.au if the registration is held by Murray, otherwise a new domain. Ownership of the registration still to be confirmed |
| B0d state scale | Keep states as a comparison layer and in the scale panel, not as the default view |
| A8 Java path | Delete from main once the static build passes the baseline; keep the QUT snapshot in git history |
| E4 loss factors | Adopt Australian figures from the National Food Waste Baseline, as a separately compared method change |
| E6 energy-to-yield link | Include with a documented elasticity, off by default so the baseline comparison is unaffected |
| E7 diet depth | Food groups first; item-level refresh only if the food-group rescale moves national capacity by more than a few percent |
| C1 name and attribution | Keep the name Carrying Capacity Dashboard; attribute to Murray Lane with the thesis citation; acknowledge QUT and co-authors on the About page; remove QUT logos |
| C2 contact route | An email address on the About page; no forum, no third-party embeds |
| C3 licences | MIT for code; CC BY 4.0 for the workbook, data layers and results |
| C4 analytics | None at launch |

No decisions are outstanding. Open confirmation: domain registration ownership (A7).
