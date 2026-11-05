# Paper B (methods): outline for approval

Drafted 2026-11-05 from `PUBLICATIONS.md` (Paper B). This is an outline only: it fixes the structure, what each section covers and the files it would draw on. No results are stated and no tables or prose have been built. Venue in the plan: Ecological Modelling.

**Working title.** Why estimates of Australia's carrying capacity differ, and how sure we can be: assumptions tested one at a time.

**The question.** Which of the 2014 paper's assumptions carried and which did not, and how much of the spread of published estimates (9 to 100 million) is the definition, the diet or the method?

## Sections

**1. Introduction.** The spread of published estimates; why it matters; what a resource-accounting estimate can and cannot say. Sequel to the 2010 methodology review (its material is this section). Framing: affordability, supply chains and climate as the energy constraint, not the 2007 to 2013 peak-oil literature; every energy parameter kept.

**2. Options for assessing carrying capacity.** The typology of the thesis, section 6: global and local, resource-based, footprint, energy-balance, nutrition-limited. Where this model sits and what each option answers. *Sources: thesis section 6; `analysis/comparators_2025/`.*

**3. The model and the frozen baseline.** Per-region land accounting; diet and food chain (edible portion, cooking, processing, loss) with each constant traced to a source; the six-cell grid of data vintage (2011, 2025) by method tier (published, corrected, improved); releases, modules and the rule that the method is frozen during a data refresh; reproducibility. *Sources: `methods/README.md`, `analysis/constants_audit/source_trace/README.md` (every Base-sheet constant traced; seven declared assumptions), `HANDOFF.md`.*

**4. Corrections.** Two errors against the model's own sources, found on rebuilding: the beef carcase-to-retail yield and the biodiesel yield (agreed wording in `ERRATA.md`), and a data correction (2011 state populations). Size on both vintages; why they are errors and not method choices; what they do to the earlier published conclusions. *Sources: `ERRATA.md`, `CORRECTION_NOTES.md`.*

**5. Improvements, one at a time.** Each judgement-based change tested alone and in sequence, with its reason and evidence: reserve land shared pro rata, recycling by stage, Australian loss factors, regional beef output, organic yield of grazing ruminants, dairy charged at observed dairy-farm yield. Effect on national and regional capacity and what each cannot fix. *Sources: `methods/README.md`, `analysis/waste_2025/`, `analysis/loss_factors_2025/`, `analysis/pasture_2025/`, `analysis/organic_2025/`.* Not in this paper: spatial pasture productivity, a water ceiling, an energy-to-yield link (not built); stated as limitations.

**6. What changed between 2011 and 2025.** The data effect on each tier and its decomposition (land, crop yields, livestock, consumption, organic, resilience table, fuel). *Sources: `results/comparison_cells.csv`, `analysis/comparison_2025/`.*

**7. How sure we can be.** The Monte Carlo (1,000 draws, 13 choices, all 60 zones) and the quick range; which choices drive the spread; which conclusions survive the range. Scenario choices (law, grain store, time frame) are not sampled. *Sources: `analysis/sensitivity_2025/README.md`, `results/ranges_*.csv`.*

**8. Scale.** How the capacity of smaller units (states, regions) sums against the national capacity, why national and regional self-sufficiency differ, and what that does to the 2015 argument. *Sources: `analysis/scale_curve_2025/README.md`.*

**9. Comparison with other estimates (Part 2).** The verified register of other estimates and the model re-run under each definition: energy-balance (Gifford 1975, Henry and Godden 1995, CSIRO and UQ 2025), the Jones inquiry's 30 to 35 and 50 plus million, integrated resource models (Foran and Poldy), footprint studies (Lenzen and Murray, Simpson), land-and-diet models elsewhere (Peters, Alexander, Cassidy). The answer to the opening question: how much of the spread is definition, diet and method. *Sources: `analysis/comparators_2025/README.md`, `rerun.csv`, `harmonisation.csv`.* **If the paper grows too long, this section moves to the results paper's discussion** (decision below).

**10. The nutrition-constrained option.** The diet that feeds the most people from Australia's land, as one more way of asking the question, and what its result must not be read as. *Sources: `analysis/nutrition_lp_2025/README.md`.*

**11. Limitations.** What the model cannot carry (`DISCUSSION.md`): disease and biosecurity, nutrient return, trade, Indigenous food systems, water and energy links, regional pasture productivity, labour and soil; the constants with no source (declared as assumptions); the 2011 cells having no range.

**12. Conclusions, data and code availability.** Releases, scripts and tables in the public repository with a DOI (Zenodo, held).

## Figures (to be scripts over `results/` when drafting begins)

1. The grid: six cells, short and long term, with ranges.
2. Waterfall from published 2011 to improved 2025, one step per correction, improvement and data layer.
3. Spread of published estimates against the model re-run under each definition (section 9).
4. Capacity against the size of the unit of self-sufficiency (section 8).

## Decisions needed before drafting prose

1. **Part 2 (section 9): in this paper or moved to the results paper?** Together with section 10 it is likely to make the paper long. My recommendation: keep section 9's register as a short table here, move the re-runs and discussion to the results paper.
2. **Headline tier.** The plan says the papers lead with the corrected comparison. Section 5 then reports the improved tier as a second set of results. Confirm the order.
3. **The nutrition model (section 10):** one section here (current plan), a separate paper, or an appendix.
4. **Authors and order**, and whether the correction notes go out before submission (the plan says yes).
5. **Climate scenarios:** the plan lists them; they are built (`results/scenarios.csv`). In this paper as a short section, or left for the results paper.
