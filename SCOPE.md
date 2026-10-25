# Scope of work: static rebuild and data refresh

Status: scoped 2026-10-25, not started. Sizes are quick, small or session-size.
Rows marked DECIDE need a call from Murray before that row starts.

## Goal

Run the Carrying Capacity Dashboard with no server, at no monthly cost, from a
repository Murray controls, and bring its data forward from 2005 to 2011 vintages
to current sources while keeping the thesis methodology (Lane 2014, chapter 8).

## Workstream A: static rebuild

The model workbook uses five Excel functions (IF, SUM, LOOKUP, AVERAGE, AND) in
7,444 formulas. A feasibility test on 2026-10-25 evaluated it in HyperFormula
with zero mismatches against the original servlet across 18 recorded cases, about
30 ms per recalculation. The workbook stays the editable model; the browser does
the arithmetic.

| # | Item | Size | Notes |
|---|------|------|-------|
| A1 | Extend the regression baseline to all 60 regions x 2 presets (120 cases) from the Java servlet while it still exists | quick | Run before anything else; it is the acceptance test for A2 to A5 |
| A2 | Build step: workbook to `model.json` (cells, formulas, LOOKUP rewritten to INDEX/MATCH, blank-as-zero) | small | Node script, runs in the Action; reads the .xls directly, no LibreOffice |
| A3 | Browser evaluator: load `model.json` into HyperFormula, write the 24 inputs, read B76, C84:D89, B91:E107 | small | Same contract as `CarryingCapacityModel.java` |
| A4 | Front end: `dashboard.jsp` becomes `index.html`; the form posts to the evaluator instead of `/ProcessExcel` | small | Sliders, CSV presets and help text unchanged |
| A5 | JS regression test against the 120-case baseline, run in the Action | quick | Tolerance 0.015 absolute |
| A6 | Fix the pie charts, which draw one slice in the original too | small | Replace the 2011 Flot pie with a plain SVG donut, or pin a compatible Flot |
| A7 | Hosting: publish the built site from the Action to GitHub Pages; custom domain and HTTPS | quick | DECIDE: domain (carryingcapacity.com.au ownership, or a new name) |
| A8 | Retire the Java and Docker path once A5 passes on the static build | quick | DECIDE: delete, or keep under a tag as reference |

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
| B0 | DECIDE geography: NRM regions (2016 edition), SA4 throughout, or hybrid (Greater Capital Cities as single regions, SA4 elsewhere) | decision | ABS ASGS; ABS crop and water data were published on both SA4 and NRM from 2015-16 | All regional layers exist on either unit. SA4 nests exactly from the ABS's SA2 estimates and is maintained; NRM is an area approximation but follows catchments as the thesis argued. Recommend the hybrid: about 58 regions, fits the 60 slots, each city one consuming unit |
| B1 | Land areas by region: cropping, pasture, non-agricultural, infrastructure, reserve | session-size | ABARES Catchment Scale Land Use, Dec 2023 (50 m raster, CC BY); CAPAD 2024 | One GIS pass. Needs the ALUM v8 class to five-class mapping written down to match thesis 8.2 |
| B2 | Population by region | quick | 2021 Census by NRM region, or 2024-25 ERP aggregated from SA2 | Replaces 2011 figures that were partly from a 2007 journal article |
| B3 | Crop yields, about 140 commodities by region, five-year average | session-size, the largest row | ABS Agricultural Commodities 2016-17 to 2020-21 by NRM region | Commodity names changed; missing cells use the thesis equation (national yield x regional cereal ratio); re-apply the dryland adjustment recorded in the workbook log |
| B4 | National scalars: liquid fuel per person, biofuel share, timber per person and per hectare, textiles per person and fibre shares, organic share, climate variability series | small in total | Australian Petroleum Statistics; ABARES Forest and Wood Products Statistics; FAO/ICAC fibre data; Australian Organic Market Report; ABARES crop reports | Each is a single figure or short series |
| B5 | Infrastructure m2 per person and nature reserve share per region | quick | Derived from B1 and B2 | |
| B6 | Diet, phase 1: rescale food groups | small | ABS National Nutrition and Physical Activity Survey 2023, published tables | |
| B7 | Diet, phase 2: item-level refresh of 746 foods | session-size | NNPAS 2023 microdata (due Q2 2026), current FSANZ food composition | DECIDE whether phase 2 is wanted |
| B8 | Waste and loss factors | small | USDA loss-adjusted food availability, current | DECIDE: methodological change, not a refresh |
| B9 | Short-term and long-term default sets re-derived per thesis 8.4; sources recorded in a new Sources sheet; log sheet updated; baseline regenerated | small | | Closes each data row |

Deliverable per row: the workbook, CSV presets and baseline updated together in
one commit, with the source and vintage written in the Sources sheet.

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
3. B0 before any B row. B1 and B2 together. B3 after B0. B4 any time.
4. C rows ride along with A4.

## Decisions outstanding

B0 geography; A7 domain; A8 retire or keep Java; B7 diet depth; B8 waste
factors; C1 name and attribution; C2 contact route; C3 licences; C4 analytics.
