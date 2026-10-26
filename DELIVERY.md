# Online delivery design

Status: decided 2026-10-25 for the static rebuild (SCOPE.md workstream A). The thesis
specifies the model; this document specifies how a visitor meets it. Where the 2011
interface got something right it is kept; where it was shaped by its technology it is not.

## Principles

1. **No server.** Everything runs in the visitor's browser from static files. No account,
   no cookie, no analytics unless C4 decides otherwise. A shared scenario is a URL.
2. **Three questions, in order: where, what if, so what.** The 2011 page already had this
   shape (region, sliders, results). It stays, because it is the thesis's own flowchart.
3. **Show the scale effect.** The thesis's most striking result (9.4: a region as one unit
   versus the sum of its parts) was never on screen. It is now a first-class output.
4. **Show the change since 2011.** Objective 2 is visible to the visitor, not only in a report.
5. **Honest numbers.** Every figure carries its vintage; every parameter keeps its help text;
   yields never appear for areas too small to be reliable.
6. **Works on a phone.** Half of visitors will arrive from one.

## Architecture

| Layer | Choice | Why |
|---|---|---|
| Model | `model.json` built from `model.xls` at build time; evaluated with HyperFormula in a Web Worker | Keeps Excel as the editable method; 30 ms per recalculation; worker keeps sliders smooth |
| Regional data | `regions/*.json`: per-SA2 additive layers plus grouping files (`regions.json` current, `zones_2011.json` thesis, SA3, states) | Any grouping is a sum; yields recomputed from summed production and area at display level |
| Map | D3-geo with TopoJSON per level, no basemap tiles | Matches the thesis's own map style, needs no tile provider or key, small files |
| Charts | Inline SVG | Replaces the 2011 Flot pie plugin, which draws one slice; themeable and accessible |
| App | Small single-page app (Preact or plain modules) built with Vite; hash routing | GitHub Pages serves static files only |
| Hosting | GitHub Pages from the Action, custom domain, HTTPS | Free, rebuilt on every push |
| Build check | Regression test against the 120-case baseline runs in the Action before deploy | The thesis numbers are the acceptance test |

## Pages

- **Dashboard** `/` : the three-part page below.
- **Methods** `/methods` : generated from the workbook's Sources sheet and the thesis
  chapter 8 structure; one row per parameter: definition, source, vintage, how it enters the model.
- **What changed since 2011** `/changes` : the comparison report (SCOPE D4), per zone,
  with the split into population, land and yield effects.
- **About** `/about` : attribution, thesis citation and link, licences (C3), contact (C2).

## Dashboard layout

Desktop: three columns, Where / What if / So what. Phone: stacked, with the headline
result pinned at the top while sliders scroll.

### Where

- Map of Australia with the current display regions. Click selects. A search box
  matches region names and towns. The selected region is highlighted and its
  land areas and population fill the inputs, as the 2011 dropdown did.
- Layer switch: **Current regions** (default), **2011 zones**, **States**, **Australia**.
  States appear only if B0d keeps them.
- Drill-down: a selected region offers "show its SA3s"; the map zooms and the SA3s
  become selectable. No level below SA3 (B0b).
- Choropleth: the map colours regions by the current scenario's result (over or under
  capacity, and by how much). Changing a slider recolours the whole map, which turns
  the thesis's static Figures 64 and 65 into a live view. Recoloured lazily, after the
  selected region's result, so sliders stay responsive.

### What if

- The 17 parameters, grouped as in 2011: Food, Climate, Agriculture, Textiles, Fuel,
  Timber, Infrastructure, Nature reserve. Each is a native range input paired with a
  number field, so it works with keyboard, touch and screen readers.
- Reference ticks on each slider keep the 2011 markers ("2011 level", "healthy level")
  and add the current-year marker from the refreshed data, so the visitor sees both.
- Presets: Short-term defaults, Long-term defaults, as now; plus "Reset to this region's
  current values".
- Land areas and population remain editable by typing, as the thesis intended (8.2),
  with a one-click return to the region's defaults.

### So what

- Headline: carrying-capacity population and the current population, with the over or
  under capacity percentage. Same hierarchy as 2011, because it is the answer.
- **Scale panel**: two figures side by side: this region as one self-sufficient unit, and
  the sum of its sub-regions each self-sufficient. The difference is the 9.4 effect.
- **Land reallocation chart**: existing area by land type against area used at carrying
  capacity, as a paired bar per land type. This is thesis Table 14 rows 20 and 28, which
  the 2011 page never showed, and it explains where the capacity comes from.
- The land-use breakdown is a stacked bar with a legend and a table view, and existing versus used land is a paired horizontal bar chart. Donuts were dropped: with more than six segments they do not read.
- **Since 2011**: the same region's 2011 result on 2011 data beside today's, with the
  three-way split, from the D4 results file. Shown whenever the selected region maps to
  a 2011 zone, which every current region does through its SA2s.
- Diet components panel (energy, protein, fat, fibre per person) from the Base sheet,
  which the model already computes and the 2011 page did not display. Collapsed by default.

## Scenario state

The URL hash holds the layer, region, preset and the 17 parameters. "Copy link" shares a
scenario; the browser back button undoes. "Download CSV" exports the scenario's inputs
and all outputs with their vintages. Nothing is stored server side because there is no server.

## Data vintages on screen

Every number that comes from a dataset shows its year on hover and in the CSV. The
headline carries one line: "Land use 2023, population 2024, yields 2016-17 to 2020-21".
This is the honest version of the 2011 page's "prototype dashboard only" notice, which
stays too.

## Accessibility and performance

Colour palette safe for the common colour-vision deficiencies, with the over or under
state also given in words. All controls keyboard-operable. First result on screen within
two seconds on a mid-range phone: model and regional data are about 1 MB compressed
and load in parallel; the map TopoJSON for the default level is under 300 KB.

## What is deliberately not built

- A basemap or satellite layer: adds a third-party dependency for no modelling value.
- Accounts or saved scenarios: the URL is the saved scenario.
- A forum: replaced by the contact route C2 decides.
- Sub-SA3 regions: yields are not reliable there (B0b).
