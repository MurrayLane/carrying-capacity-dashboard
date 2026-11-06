# Paper B (methods): a critical review of carrying capacity methods, tested on common Australian data

Redrafted 2026-11-06 after Murray's decisions (below). This is an outline only: it fixes the structure, what each section covers and the files it would draw on. No results are stated and no tables or prose have been built.

**Working title** (Murray: a good title; to revisit now the paper is a review): Why estimates of Australia's carrying capacity differ, and how sure we can be. *Possible subtitle:* a critical review and a common-data comparison of methods.

**Readers.** Land use planners and sustainability analysts.

**Type.** A critical narrative review (decided 2026-11-06): organised around an argument and a stated, purposeful selection of literature, not a systematic search protocol.

**The question.** Which method suits which purpose? How much of the spread of published estimates of Australia's capacity (9 to 100 million) is the definition, the diet or the method, and which design choices decide the answer?

**The paper's contribution beyond Murray's earlier work.** The thesis (chapter 6) and *Land Use Policy* 2010 ("The carrying capacity imperative") already review the planning-oriented methods: Limits to Growth, the ecological footprint, South East Queensland, Noosa and Douglas Shire, Peters (New York State), Fairlie (Britain) and Fearnside. This paper does not repeat that review. It adds:
1. Method families not in the earlier work: energy and protein balance (Gifford 1975; Henry and Godden 1995), integrated resource flow (Foran and Poldy 2002), people per hectare (Cassidy 2013), the HALF land index (Alexander 2016), Simpson et al. 2000, the critiques of the footprint, and the literature since 2011.
2. **Testing the methods through the model, on Murray's own data:** the same current Australian production, land, population and diet data (2025) put through each method, with each method checked against its authors' published figure where possible.
3. What each design choice does to the answer, measured, not asserted.
4. A guide to which method fits which purpose.

## Sections

**1. Introduction.** The spread of published estimates, why it matters to planners and analysts, and the question. Sequel to the 2010 methodology review.

**2. The concept and its critics.** Hardin, Seidl and Tisdell, Sayre, Meyer and Ausubel, Price, Cohen and the thesis typology (inputs and outputs, scale). Brief: points back to the thesis chapter 6 and the 2010 paper. *Sources: `Literature review/` library.*

**3. How the review was done.** What was selected and why: the well-known methods across the main approaches, plus papers published since 2011 from Murray's citation exports; what the earlier work already covered. Stated briefly and transparently.

**4. A catalogue of methods.** Families, each by the question it answers, its inputs and outputs, and its scale: resource-based land and diet; energy and protein balance; commodity balance; ecological footprint; land per diet indices; integrated resource-flow models; failure-probability simulation (Fearnside); nutrition optimisation; export-inclusive counts. The planning-oriented studies get one line each and a pointer to the earlier work; the families new to Murray's work are treated in full.

**5. Testing the methods on common Australian data (the core).**
* The common data set: production, land, population and diet for 2025, from the model's releases (decided 2026-11-06: 2025 only; the 2011 data and the change since 2011 belong to the results paper; at most one 2011 column in one table as a check that method differences are not an artefact of the data).
* Each method: how it was implemented, what it needs, and and how closely the implementation follows the authors' description. Where the authors' own figure is published and the inputs are obtainable, the implementation is checked against it (a fidelity check, not the test); the test itself is the method applied to the Australian data.
* Murray's own method is one of them (the model's baseline), run and reported in the same way.
* The result: the same data through each method, side by side.

**6. What moves the number.** The design choices measured with the model on the same data: whether exports count, the diet and waste assumed, a drought allowance (the failure-probability view), the unit of self-sufficiency (scale; the full curve is in the results paper), the yield basis and the time frame. Uncertainty as a design dimension, not a stand-alone section.

**7. Which method for which purpose.** A matrix of intended outcomes against method features, with a fit-for-purpose recommendation and a minimum reporting checklist. Outcomes, in order of how strongly the paper's evidence supports them:
1. food security and drought risk;
2. why national estimates range from 9 to 100 million (exports, energy balance, definitions);
3. regional and local land-use planning;
4. diet change and land use.

**8. Limitations and what no method yet does.** What the model cannot carry (`DISCUSSION.md`); where an implementation could not be checked against its authors' figure and rests on their description alone; the constants declared as assumptions.

**9. Conclusions, data and code availability.**

## Figures (to be scripts over `results/` when drafting begins)

1. The methods mapped by the question each answers.
2. The same data through each method: Australia's capacity on 2025 data by method.
3. The effect of each design choice on the answer.
4. The purpose-to-method matrix.

## Method tests scoped (nothing built yet)

| Method | Fidelity check (author's own figure, where one can be reached) | Data status |
|---|---|---|
| Energy and protein balance (Gifford 1975; Henry and Godden 1995) | Henry and Godden Table 5 (1990-91): contemporary excluding wool and cotton **109 million (energy), 96 (protein)**; no wool and cotton expansion 172 and 156; total 206 and 188; Gifford et al. 82 and 60. Recipe (read from the scanned paper): food energy and protein of domestic production (404 x 10^15 J and 306 x 10^10 g, excluding wool and cotton) scaled up by Nix's 70 Mha of intensive land over the 45.7 Mha in use (crop 17.4, sown pasture 28.3), then divided by consumption factors inferred from Gifford (0.1760 million people per 10^15 J; 0.2041 per 10^10 g); no exports, no future yield gains (Gifford doubled sugar, fruit, vegetable and nut yields). 404 x 70/45.7 x 0.1760 = 109 | Henry and Godden's sources were ABS and ABARE 1993. The recipe is arithmetic once the production totals are built, so it is easy to run on 2025 data. For the 1990-91 fidelity check: ABARE (2010 edition, in the archive) covers broadacre, meat and dairy but not fruit, vegetables or eggs; ABS 7503.0 1990-91 (`Comparators/`, 31 pages) gives their gross values and average unit values (eggs $322.5m at $1.54 a dozen, apples, oranges, potatoes), so tonnage is value divided by unit value; the check would still be approximate because energy and protein conversion factors are not published in the paper |
| Commodity balance (Foran and Poldy 2002) | Their 1997-98 production and 2050 requirements (Table 2.5) | Requirements derived in `analysis/comparators_2025/` |
| Land per diet (Alexander 2016, HALF index) | Australia 112.20 on the paper's basis (percentage of the world's total land, 13,009 Mha), confirmed in the supplement's Table S5 (`Literature review/Alexander2016_SI.pdf`); 158 on the habitable-land basis in the comparators register (same data, ratio 1.41). World 35.13, United States 97.73, India 15.76 | Paper and supplement read. The SI gives the full allocation recipe (worked soybean, poultry and beef examples: area by use pro rata to mass, 1,556/1,378 cropland-to-harvested adjustment, 50:50 value split for oil and meal, feed conversion ratios, ruminants take remaining feed and all pasture). Table S3 lists the 90 commodities but gives no values, so the world-average land per tonne must be rebuilt from FAOSTAT 2011 (commodity balances, areas, population); the Australian side needs per-person consumption by commodity. A reconstruction, checked against the published 112.20 by running the same recipe on the global and Australian FAO data |
| People per hectare (Cassidy 2013) | US 16.1 people fed per hectare on produced calories, 5.4 on delivered calories (world 10.1 and 6.0); circa 2000, cropland only | Paper read. Counts cropland only: no grazing and no sheep or goats, so it cannot stand for Australia's pastoral capacity. Needs crop use split (food, feed, other) and feed conversion (paper Table 1); 2,700 kcal a day. Reproducing the US figure needs EarthStat gridded data, so the test would be a reconstruction for Australia |
| Ecological footprint, food-only (Simpson 2000) | Whole footprint 5.96 hectares a person, 1991-92; the **food row alone is 2.71** (energy 0.43, garden 0.03, crop 0.41, pasture 1.76, forest 0.08). The paper does not publish the consumption or world-yield inputs, so a reproduction is not possible from the paper; food-only is a reconstruction | ABS 4306.0 1991-92 issue online (not yet read); Lenzen and Murray 1994-95 cannot be reproduced (input-output tables) |
| Failure probability (Fearnside-style) | Applied to Australia as a method; no check against his figure is possible or needed (his data are Brazilian; the 1990 paper is a five-page overview and gives only the concept and one result, at most 0.24 persons a hectare for a 23,600 ha Trans-Amazon study area against 0.5 to 1 in the FAO/UNFPA/IIASA study); its result is context only. Failure is the share of settlers below minimum consumption standards, chosen by society, with capacity read from a density-by-failure curve built from repeated simulations | Model's drought allowances by return period and the reliability runs. Method detail now in hand from Fearnside 1985 (Spanish translation, `Literature review/`): failure tested separately on calories (2,500 kcal a person a day in the text, 2,550 in a figure caption), total protein 38 g, animal protein 25 g and money per person; weather and yields drawn from distributions fitted to observations; runs of 25 years with population held at fixed densities; failure rate = share of settler-years in the last ten years below the standard; capacity = density at which failure reaches a maximum acceptable probability chosen by the planner |
| The Australian model (Murray's method) | The model's own releases | In the repository |

Test rule (Murray, 2026-11-06): the focus is the method, not where its author applied it. Every method in the table is run on the Australian data, whatever the original study area (Fearnside's Brazil, Cassidy's United States). Checking an implementation against its author's published figure is a fidelity check where one exists; each method is reported as a fidelity-checked implementation or as an implementation from the published description alone.

## Moved out of this paper

The corrections, the improvements one at a time, the 2011 to 2025 decomposition and the Monte Carlo ranges are not in this paper. Their home (the results paper, Paper A, or a short model paper) is a decision for Murray. The scale curve is already planned for Paper A.

## Decided 2026-11-06

* **No reproduction gate.** The thing tested is the method applied to Australian data, wherever its author first used it. Matching an author's figure is only a fidelity check.

* Critical narrative review; readers are land use planners and sustainability analysts; the methods tested are the well-known ones across a range of approaches, run through the model on Murray's data.
* **Paper B uses 2025 data only.** 2011 is essential in Paper A (the change since 2011, on corrected 2011 numbers) and is not needed for a method comparison.
* **The correction notes stay** (they correct the published record and give Paper A its baseline); whether to send them is still Murray's decision.
* Whether the dashboard keeps a 2011 option is left for later.

## Decisions still open

1. **Journal and exact readership,** now that the type is settled (Land Use Policy, Ecological Indicators and Environmental Science and Policy were suggested).
2. **Where the model material goes** (improvements, decomposition, ranges): Paper A or a short model paper.
3. ~~The gate~~ Settled 2026-11-06: no reproduction gate; every method is applied to Australia, and the fidelity check is reported where available.
4. **Authors and order,** and whether the correction notes go out first.
