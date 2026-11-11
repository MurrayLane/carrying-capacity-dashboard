# B66f readings: Paper B sections 4 and 8 (targeted reads)

Nine rows read at TARGETED depth. Each file was opened first and matched to its register row on title, authors and year; all nine matched, and every file's SHA-256 matches the register. Eight characterisations hold and one holds in part (L215). Full figures with page numbers are in `qa/reports/B66f_readings.csv`. Page numbers are the journals' own, except where stated.

**L204 Chaudhary 2019 (holds).** The paper finds a diet for each of 152 countries that meets 29 nutrient limits and five per-capita limits for greenhouse gas, water, cropland, nitrogen and phosphorus, while staying as close as possible to what people eat. Intake data are for 2011. With the observed diets, 85 countries are inside the carbon limit; with the optimised diets all 152 are inside all five limits (p.7698). The changes needed are large: the median country departs 177% from its observed diet (p.7699). Carbon and nitrogen limits are the hardest to meet (p.7700). The per-country tables, including any Australian row, are in a spreadsheet that is not on disk, so no Australian value is taken.

**L205 Gazan 2018 (holds).** This is a review of 67 studies that use mathematical optimisation to design diets. It explains the objective functions (for example minimum cost or least departure from the observed diet) and the constraints (nutrient, cost, cultural, environmental). It states what a constraint that cannot be met signals: clashing nutrient recommendations, monotonous eating patterns, too few nutrient-rich foods, or a clash with another dimension. It reads the studies as showing that nutrition, cost and environment seem compatible up to a 30 to 40% cut in diet environmental impact. The text rendering has no page numbers, so sections are cited.

**L206 Ridoutt 2021 (holds).** The paper scores 9,341 Australian adult daily diets from the 2011-12 Australian Health Survey on three footprints (climate, water scarcity, cropland scarcity), combined into one impact score weighted by distance to planetary-boundary targets, and on diet quality against the Australian Dietary Guidelines. The average adult diet scores 41 of 100 on quality. A guideline diet built from lower-impact eating patterns cuts the impact score 15.9% and the climate footprint 34.9% but raises the water-scarcity footprint 11.6%; none of the three footprints reaches its target (p.806). The authors conclude that the larger share of the reduction may need to come from the food production system (p.808).

**L208 Gao 2017 (holds).** The paper runs the LUTO land-use model, a linear-programming model of Australia's agricultural zone, on 648 pathways to 2050 and checks seven land-sector targets (economic returns, food, water, bioenergy, biofuels, emissions, biodiversity) at three ambition levels, with targets set from 2012. Meeting several targets together is rare: five Moderate 2030 targets together occur in 0.9% of pathways (p.219). The Moderate 2030 water target, 5,783 GL a year in water-stressed catchments, is met in 41.7% of pathways, only where strong emissions incentives and large reforestation are absent (p.219).

**L209 Navarro Garcia 2022 (holds).** The paper uses the FABLE Calculator, an Excel model of the Australian food and land system that does not optimise, and samples it 200,000 times across three Shared Socioeconomic Pathway ranges. Six targets are tested: diet energy, net afforestation, irrigation water at or below the 2010 level, net-zero emissions, 50% of land for biodiversity, and exports at 1.5 times 2010. With exports required, 13% of SSP1 scenarios meet all targets and none of SSP2 or SSP3 do (Results); the abstract says about 10%. Livestock productivity and density, afforestation and diet matter most. No page numbers in the rendering.

**L210 Herrington 2020 (holds).** The paper compares four World3-03 scenarios (business as usual, doubled resources, comprehensive technology, stabilised world) with observed world data for ten variables, with data ending between 2015 and 2020. It repeats Turner's comparisons using the 2004 model version and adds one scenario and two variables. Closest-fit counts are comprehensive technology 7, doubled resources 6, business as usual 4, stabilised world 3, none 2 (Table 3, p.622). BAU2 and CT do not separate up to 2020, and the author notes the tally could change as data points are added (p.622).

**L215 Yi 2018 (partly).** This six-page review compares five methods for water resources carrying capacity: conventional trend, system dynamics, multi-objective model analysis, comprehensive evaluation, and dynamic simulation recursive. The register row lists the first four; the fifth is described as closest to the physical meaning of carrying capacity and needing long, high-quality data (p.458). The paper says index choice and weights are set by the researchers in the multi-objective and comprehensive-evaluation methods, and that the basic calculation methods have not changed in over ten years (p.457-458). It gives no capacity values and nothing on Australia. The byline is LI Yi, so the first author's surname is Li.

**L216 Cottrell 2019 (holds).** The paper finds shocks (sharp production drops) in national FAO series for crops, livestock, fisheries and aquaculture, 1961 to 2013: 226 shocks across 134 nations from 741 series (p.130). Decade averages of shock frequency rise in all four sectors (p.130). Extreme weather caused over half of crop shocks and geopolitical events 41% of livestock shocks (p.131). The authors say the reason for the rise is unclear because reporting quality has also changed (p.132), and that national totals smooth out shocks in large countries such as Australia (p.135).

**L221 Bentham 2020 (holds).** The paper analyses FAO food balance sheet energy for 18 food groups in 171 countries, 1961 to 2013, using principal component analysis. Four scores explain 89.2% of the variation: animal source and sugar; vegetable; starchy root and fruit; seafood and oilcrops (file p.4, 14). It describes how national food supply composition changed, comparing 1961-65 with 2009-13. Australia is among the high-income English-speaking countries whose animal source and sugar score fell most (file p.7). It does not model or project change. The file is the author's accepted manuscript, so page numbers are file pages.

## Flags

- B Section 4 (families of methods), L208 and L209: the register places both under integrated resource-flow or stocks-and-flows models (B4.8). The Gao paper describes LUTO as an integrated, constrained, partial-equilibrium linear programming model (p.217), so it is an optimisation model; the Navarro Garcia paper states the FABLE Calculator uses no optimisation (Methods). The family label for LUTO needs a decision; nutrition optimisation (B4.7) is a separate family in the register.
- B Section 4 (water-bounded capacity, B4.9) and the register title, L215: the paper's own citation line reads LI Yi et al. 2018 (p.455), so the key 'Yi 2018' uses the given name. A Paper B line citing it should read Li et al. 2018.
- No flag touches papers/A_results/OUTLINE.md. No other flag touches papers/B_methods/OUTLINE.md.

Other observations (not outline flags):

- L206 and L204 set different per-person water limits: Ridoutt uses 216 L a day for Australia (global boundary 1,100 km3 a year, 70% to food, 9.7 billion people, p.804); Chaudhary uses 786 L a day (global boundary 1,980 km3 a year over the 2011 population, p.7696-7697). Any Paper B sentence quoting a per-person water limit needs to name the basis.
- L209: the abstract's 'around 10%' and the Results' 13% (with exports) and 41% (five environmental targets, no export requirement) differ; a quoted share needs the Results figure and its target set.
- L210: for B Section 2, where Turner's finding that world data follow business as usual is cited, Herrington p.622-623 reports a different closest fit.
- L216: for B Section 8 (variability between years), the national-total caveat for Australia is on p.135.
- L221: the file is the accepted manuscript; numbers should be checked against the typeset Nature Food article (70-75) if quoted in print. L205 and L209 are text renderings without page numbers. Supplementary files for L204, L206, L210, L216 and L221 are not on disk and were not read.

## Register rows touched

| id | file | characterisation holds |
|---|---|---|
| L204 | Chaudhary2019.pdf | yes |
| L205 | Gazan2018 PMC text (.md) | yes |
| L206 | Ridoutt2021.pdf | yes |
| L208 | Gao2017.pdf | yes |
| L209 | NavarroGarcia2022 PMC text (.md) | yes |
| L210 | Herrington2020.pdf | yes |
| L215 | Yi2018.pdf | partly |
| L216 | Cottrell2019.pdf | yes |
| L221 | Bentham2020 accepted manuscript PDF | yes |

Wrong-value check: EXAMPLE ONLY, not a finding. Suppose the L216 line read 'shock frequency fell across 1961 to 2013'. Checked against Cottrell p.130 ('shock frequency has increased through time on land and sea') the answer would be holds = no, and the row would need rewriting. Suppose the L204 line read '152 countries meeting 12 nutrient targets'. Table 1 on p.7696 lists 29 nutrient rows, so holds = no. Both lines are invented to show the test can fail; the real rows passed.
