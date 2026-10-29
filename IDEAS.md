# Ideas register for the rebuild

Murray, 2026-10-28: all of these are to be kept in mind when the dashboard is rebuilt, and **the rebuild is to be re-conceptualised, not a port of the original code or screens**. This file is the memory of them; SCOPE.md holds the work rows. Nothing here is built unless a row says so.

Things the model cannot or should not carry, kept for the papers: `DISCUSSION.md`.

## Standing frame

* Two lines of enquiry, always (HANDOFF.md): line 1 mirrors the previous method on updated data, line 2 explores improved methods; both are published.
* Two outputs: the dashboard (updated data and method) and journal articles comparing inputs, outputs and methods with the original. Both read `results/` (PUBLICATIONS.md).
* Short-term defaults follow current legislation and practice; long-term defaults may assume laws are adapted (Murray, 2026-10-28).
* Evidence-based defaults: a figure is a benchmark that something has achieved, never 100% of anything because it is theoretically possible.

## Dashboard concepts

1. **Data by method selectors** instead of a list of releases: data 2011 or 2025, method as published, corrected or improved (the six cells, `methods/README.md`), with the change page reading `results/comparison_cells.csv`; the dashboard default is the corrected tier (Murray, 2026-10-28, on the recommendation to separate errors from improvements).
2. **Likely range, not a Monte Carlo** (DELIVERY.md, last section; SCOPE F6): a thin range bar and a plain second value, from a quick range of about 28 runs that agrees with the Monte Carlo within about 5%; the Monte Carlo stays in the papers.
3. **Map classes**: robustly over capacity, robustly under, uncertain (hatched), precomputed for all zones at the defaults, live for the selected zone.
4. **What could change this number**: the two or three inputs that matter most for the selected zone, each with its own slider.
5. **Named scenarios** on top of the two presets (built as data 2026-10-29: `scenarios/scenarios.json`, `results/scenarios.csv`; not yet in the dashboard): today's law and practice; the Japan and South Korea feeding benchmark with an adapted law; a high feeding case (52%); fuel scenarios (210 L thesis method, 156 L electrified light vehicles, the CSIRO biofuel ceiling); avoidable waste at the national target (6%); grain store of one or two years (built as scenario releases `2025-store-1` and `2025-store-2`; the store is free in the model, so a costed store is the next step; as a switch among resilience tables shipped in the release); the reserve shared pro rata.
6. **Honest labels**: the recycling setting now scales a stage pattern (the old caption, "% of food wastage fed to farm animals", is wrong for the improved method); every figure carries its vintage; no yields or ranges for zones too small to be reliable; the 2011 results have no range.
7. **Shared scenario as a URL** (no server), as designed in DELIVERY.md; the saved link names the release, and later the method and data selectors.
8. **Re-conceptualise, do not port**: possible directions to weigh when the rebuild starts are a question-led layout (where, what if, so what) kept from the thesis flowchart, scenarios and diets as first-class objects (not 17 sliders), a map that answers over or under first, the comparison with 2011 as a page of its own, and a methods page generated from the method modules.

## Diets by region (Murray, 2026-10-28)

The model has one diet for every zone: the recommended-serves diet by food group, scaled by the meat and egg share and the red meat share. A diet that fits the local climate would change the result most where land and climate differ from the national average. Examples to test:

* **The Northern Territory eating as the tropical north does** (Papua New Guinea, Torres Strait, northern Queensland): root crops, banana, sweet potato, cassava, fish, coconut, less dairy and wheat. The model has cassava, sweet potato and banana; it has no taro, yam, sago, coconut or breadfruit, and no yields for them, so a tropical diet needs a short list of added crops with yields from FAO and GAEZ (SCOPE E12) rather than ABS.
* **The south eating more meat** where pasture is the comparative advantage (Victoria, Tasmania, south-west WA, the tablelands), which is the red meat share by zone.
* **How:** diet templates as data (a food-group mix and a meat share per template: the national recommended diet, the actual diet of NNPAS (E7), a Mediterranean, a tropical-staples template built from FAO food balance sheets of Papua New Guinea, a low-meat template), chosen per zone on the dashboard or as a scenario in the papers. The nutrition-constrained optimisation (E11) answers the same question without choosing a template: which diet feeds the most people from this zone's land, subject to energy, protein and key micronutrients. A regional diet raises a fairness question to settle first (a template imposed on a population by climate is a scenario about land, not a prediction about what people will eat).
* **First result (2026-10-28, `analysis/diet_templates/README.md`):** trying the model's own diets in every zone, the Northern Territory and Tasmania are best on meat-heavy, mostly red diets (pasture feeds people through cattle and sheep), every other mainland state on little or no meat; the real PNG diet is not nutritionally adequate by Australian standards and cannot be a template as it is.
* **Work row:** SCOPE E16.

## Uncertainty and method ideas not yet built

* Sample the long-term choices in the ranges (resilience table, long-term fuel, feeding benchmark); keep scenario choices (law, grain store, time frame) as switches rather than sampled inputs. SCOPE F6.
* Stage-specific uptake from sector data (Japan's sector rates are not rates of feeding; check the ministry tables).
* Biofuel feedstock mix (canola and sunflower, residues, tallow, used cooking oil) once the biodiesel yield is settled (SCOPE E17).
* Ruminants and rendered by-products in the feed credit; compost and nutrient return (needs a nutrient constraint the model lacks).
* A resilience table for the 2011 vintage so that the leave-one-out table can join the improved method.
* Pasture productivity by region (E1); item-level diet (E7); GAEZ as an upper bound and a fill for unreported crops (E12).
