# Recycling split by stage, origin, dry matter and the law in force (SCOPE.md E4 and E15)

**Line 2 of the two lines of enquiry (an improved method).** Line 1, the thesis method on current data, is release `2025-fuel` and the rest of `README.md`; nothing in line 1 changed. This page is the
method that I think the thesis's own workbook would have used had it split recycling the way it already splits the losses, and had it let the law differ between the short term (the law as it is) and the long term (a law adapted to new circumstances).
It is published as the alternate release `2025-recycling-stage` (extends `2025-fuel`), so both numbers can be shown side by side.

## What the thesis method does

`Base!P` credits the recycling setting times every recyclable loss of every food, `1 - E*H*J*M` of its primary production (inedible part, consumer waste, retail waste, primary-to-retail loss; processing losses for foods whose processing yield is below one),
in wet grams. The `Recycle` sheet then shares that total among pork, eggs, chicken, duck, turkey, farmed fish and farmed seafood in proportion to what is eaten, divides by each animal's feed conversion ratio (a mass of dry feed per mass of product) and subtracts the resulting displaced production from the land those animals need.
Four things follow that the thesis does not say:

1. **It treats every gram alike.** A gram of apple core (15% dry matter) counts as a gram of grain (88%), and the conversion ratios are measured on dry feed.
2. **It feeds animal-origin waste to animals.** Meat, fish, dairy and egg waste are 48% of the short-term pool; feeding food waste containing meat or dairy to pigs or ruminants is banned in every state and territory (and to poultry in Queensland).
3. **It counts shells, bagasse, pomace and grounds as feed**, and cheese whey, bran and oilseed meal, which are real feed, alongside them.
4. **At 100% it feeds the whole industry on waste.** The potential production the recycled waste could replace is 3,926 g a week in the short term and 2,342 in the long term, against a production of pork, eggs, poultry and farmed fish of 2,439 and 1,486 (`Recycle!G9`, `B9`). The sheet caps the displacement at all of it, so at 100% recycling the thesis has pigs, poultry, eggs and farmed fish needing no feed land at all, in both the short and the long term.

## Where the recyclable waste arises

The workbook's own chain gives the split exactly: primary to retail `Y(1-M)`, retail `Y*M(1-J)`, consumer avoidable `Y*M*J(1-H)`, inedible parts `Y*M*J*H(1-E)`, and the processing part (what is left of `Base!O` after those). Grams a person a week of primary production, Australia, release `2025-fuel`, recycling 100% (`stages.csv`):

Short term (12% avoidable waste):

| Stage | Plant origin | Animal origin | Share of the pool |
|---|---|---|---|
| primary to retail (culls, transport, packing) | 423 | 3 | 4% |
| retail | 1,130 | 846 | 17% |
| consumer avoidable waste (households, food service) | 2,289 | 2,127 | 38% |
| inedible parts (peel, core, bones, shells) | 893 | 827 | 15% |
| processing by-products | 1,350 | 1,781 | 27% |
| **All stages** | **6,085** | **5,584** | **11,669** (animal origin 48%) |

Long term (the thesis setting, no avoidable waste; the first three stages are the fixed losses of some fruit):

| Stage | Plant origin | Animal origin | Share of the pool |
|---|---|---|---|
| primary to retail (culls, transport, packing) | 120 | 0 | 2% |
| retail | 240 | 0 | 3% |
| consumer avoidable waste (households, food service) | 478 | 0 | 7% |
| inedible parts (peel, core, bones, shells) | 2,138 | 741 | 42% |
| processing by-products | 1,687 | 1,484 | 46% |
| **All stages** | **4,663** | **2,225** | **6,888** (animal origin 32%) |

Animal origin means the primary product is milk, egg, meat, fish or seafood. In the short term cheese whey alone is 1,561 g of the pool (13%) and cane sugar's bagasse 534 g (5%).

## The improved method

Each part is multiplied by (a) the share of it that may be fed, plant and animal origin separately, with the law in force choosing between two animal-origin columns (`Settings!BL4:BO8`), (b) for processing by-products, the feed-grade share of the by-product class (whey and skim milk, bran and offal, oilseed meal, potato and corn residues: fed; shells, hulls, bagasse, pomace, grounds and animal by-products: not fed), and
(c) its dry matter, relative to the 88% dry matter of feed. Dry matters are medians of the raw foods of the diet category in the AUSNUT 2007 table (archive, `prelim models/ausnut07full.xls`) for fruit (15%), green (9%), other (8%), orange (15%) and starchy (22%) vegetables and nuts (97%); dried legumes 90%, grain 88%, cow's milk 13% and whey 7% (judgement from the same table and standard feed tables).
The recycling setting keeps its meaning as the uptake of what may be fed. With every share set to one and dry matters to one the formulas reproduce the thesis result to the person (checked for Australia, NSW and ACT, Queensland, short and long term).

**The law in force follows the time frame** (`Settings!B8`, the years the result must hold: 1 in the short term, 100 in the long term). Under 20 years (`Settings!BL9`, editable) the current law applies; from 20 years on the adapted law applies.

* **Current law (short term):** animal-origin food waste is not fed; plant waste and feed-grade by-products (including whey) are.
* **Adapted law (long term, the Japan and South Korea model):** heat-treated animal-origin food waste may be fed to pigs, poultry and farmed fish, never to ruminants. The waste of a species is kept from its own kind (`Settings!BL10`; Japan and South Korea allow it, the EU does not, and it changes the result by 0.01 to 0.03 million).

Capacity of Australia, millions of people, as each correction is added (`stages_ladder.csv`; avoidable waste 12% short term, 0% long term). The last row is the long-term law and applies only to the long term; with no uptake the capacity is 48.00 (short) and 12.53 (long).

Short term (current law):

| Step | uptake 25% | uptake 40% | uptake 50% | uptake 75% | uptake 100% |
|---|---|---|---|---|---|
| thesis (as published) | 48.47 | 48.75 | 48.93 | 49.17 | 49.17 |
| dry matter of the waste counted | 48.15 | 48.23 | 48.29 | 48.44 | 48.58 |
| animal-origin waste not fed | 48.11 | 48.18 | 48.22 | 48.33 | 48.44 |
| only feed-grade by-products (the improved method) | 48.09 | 48.14 | 48.18 | 48.27 | 48.36 |

Long term:

| Step | uptake 25% | uptake 40% | uptake 50% | uptake 75% | uptake 100% |
|---|---|---|---|---|---|
| thesis (as published) | 13.09 | 13.45 | 13.70 | 14.05 | 14.05 |
| dry matter of the waste counted | 12.69 | 12.78 | 12.85 | 13.01 | 13.18 |
| animal-origin waste not fed | 12.67 | 12.75 | 12.81 | 12.96 | 13.10 |
| only feed-grade by-products (the improved method) | 12.63 | 12.69 | 12.73 | 12.83 | 12.94 |
| law adapted in the long term (the Japan and South Korea model) | 12.64 | 12.71 | 12.75 | 12.87 | 12.98 |

* **The thesis's long-term credit of 14.05 million falls to 12.98 million at 100% uptake and to 12.71 million at the 40% uptake the release uses** (below). Dry matter is the largest single step (-0.9 million at 100%); the law of today and the feed-grade filter take 0.24 million between them.
* **Adapting the law is worth little: +0.04 million at 100% uptake and +0.02 million at 40%.** The reason is mass, not principle: in the long term the animal-origin waste that the law would newly allow is the inedible parts of meat and fish (741 g a week wet, at 25 to 30% dry matter, and with the waste of a species kept from its own kind), because whey is fed under both laws and the long-term diet is low in meat.
* In the short term the full credit is small either way (49.17 against 48.36 million at 100%).

## Is 100% ever feasible?

No. Nothing in the evidence comes near it, and the thesis's 100% is not a defensible default for a long-term scenario. The best-documented systems that feed food waste to animals deliberately, with the law changed to allow it, reach about 40%:

| System | Share of food waste fed to animals | Notes |
|---|---|---|
| Japan, 2006-07 | 35.9% of all food waste (52.5% of manufacturing, retail and catering waste) | Heat-treated "ecofeed"; households are not fed |
| South Korea, 2006 | 42.5% of all food waste | Landfill of food waste banned since 2005; separate collection compulsory since 2013; later reports of 98% recycled by all routes, about half to feed |
| EU, a modelling assumption | 39.2% | The mean of Japan and South Korea, used by zu Ermgassen and colleagues (2016) to estimate that regulated swill could replace 20% of EU pig feed on a dry basis |

Japan's food industry by sector (reported, by all routes of recycling, not feed alone): manufacturing 94%, retail 37% and restaurants 17% in 2010, food service 35% in 2022, with households outside the system. Reasons the share stays well below 100% even where the law allows it and the state pays: waste arises where animals are not (cities), collection and sorting are costly and contaminated streams are unusable, some of it (packaging, bones, shells, spoiled and mixed waste) is not feed, there is a limit to how much a pig or a chicken eats, and competing uses (compost, biogas) are favoured by policy.

**So the release sets the long-term uptake at 40%**, the national rates achieved by the two countries that have done it, applied to the part of the waste that may be fed. This is conservative in one respect (their rates are shares of all food waste, including parts that cannot be fed) and generous in another (Australian waste is more dispersed than theirs). Long-term capacity of Australia at other uptakes, adapted law:

| Step | uptake 25% | uptake 40% | uptake 50% | uptake 75% | uptake 100% |
|---|---|---|---|---|---|
| law adapted in the long term (the Japan and South Korea model) | 12.64 | 12.71 | 12.75 | 12.87 | 12.98 |

With no uptake: 12.53. Japan without households (52.5%) would give 12.76 million.

## The law, and the disease argument

The short term follows the law as it is, and the long term may assume the law is adapted. The reason the law exists is disease: the 2001 foot-and-mouth outbreak in the United Kingdom, which cost the economy about £8 billion, is thought to have started from uncooked food waste fed to pigs, and the EU banned feeding catering waste in 2002; Australia's rules rest on the same risk, with African swine fever added. Heat treatment inactivates the viruses (Japan: 70 degrees for 30 minutes or 80 degrees for 3 minutes; South Korea: at least 80 degrees core temperature for 30 minutes), and no outbreak in Japan or South Korea has been traced to ecofeed; their 2010 foot-and-mouth outbreaks were not linked to it. Feeding meat waste to ruminants remains illegal in both (BSE).

The argument that localising food systems lowers the global disease risk is reasonable and fits this scenario: the pathway in the 2001 outbreak was imported meat entering the food waste stream, and a system in which animals are fed only the waste of food produced and heat-treated at home, with traceability, closes that pathway. It does not remove the risk (domestic outbreaks, illegal feeding by smallholders, failures of treatment), and the model does not test it: it has no disease or trade component. I have recorded it as a reason to accept the adapted law as the long-term assumption, not as a result. I have not checked the current Australian regulations beyond the FIAL summary used in `README.md`.

## What can be fed, and what is fed today

The pool that survives the corrections (dry-matter feed grams a person a week at 100% uptake; `pool.csv`) under the law of each term, and how much of each stage's pool was fed in 2018-19 (FIAL 2021 Table 3: retail 68 of 629 thousand tonnes to feed, manufacturing 6,253 of 11,131, households, food service and procurement none; primary production not measured):

Short term (current law):

| Stage | Fed pool (g a week) | Share | Fed in 2018-19 |
|---|---|---|---|
| primary to retail (culls, transport, packing) | 68 | 3% | 0% |
| retail | 499 | 22% | 11% |
| consumer avoidable waste (households, food service) | 979 | 44% | 0% |
| inedible parts (peel, core, bones, shells) | 140 | 6% | 0% |
| processing by-products | 543 | 24% | 56% |
| all stages | 2,228 | 100% | 16% |

Long term (adapted law; the last column is the Australian practice of 2018-19, not the long-term uptake):

| Stage | Fed pool (g a week) | Share | Fed in 2018-19 |
|---|---|---|---|
| primary to retail (culls, transport, packing) | 20 | 1% | 0% |
| retail | 41 | 3% | 11% |
| consumer avoidable waste (households, food service) | 81 | 6% | 0% |
| inedible parts (peel, core, bones, shells) | 546 | 37% | 0% |
| processing by-products | 795 | 54% | 56% |
| all stages | 1,484 | 100% | 30% |

* **Consumer-level waste is the biggest part of the short-term pool (44%) and none of it is fed today**; the barrier is collection and the law, not the model.
* **By-products are the biggest part of the long-term pool (54%)** and are the part that is already fed. Weighted by the pools, 16% of the short-term pool was fed on 2018-19 practice; the release sets the short-term recycling to **16%** instead of the thesis's 0%.

## Results

Release `2025-recycling-stage`, millions of people, at each release's own settings (short term: current law, 16% uptake; long term: adapted law, 40% uptake):

| Zone | Short term: 2025-fuel | 2025-recycling-stage | Long term: 2025-fuel | 2025-recycling-stage |
|---|---|---|---|---|
| Australia | 48.00 | 48.06 | 14.05 | 12.71 |
| NSW and ACT | 11.99 | 12.01 | 2.44 | 2.23 |
| Victoria | 6.96 | 6.99 | 0.95 | 0.85 |
| Queensland | 8.84 | 9.05 | 0.86 | 0.80 |
| Western Australia | 3.56 | 3.56 | 1.80 | 1.79 |

The short term rises by 0.06 million for Australia (0.2 in Queensland). The long term falls by 1.3 million; of this, 0.9 is the dry-matter correction, 0.2 the feed-grade filter and the law of today net of the adapted law, and 0.3 the lower uptake (40% instead of 100%). At these settings the recycled feed replaces 5% (short term) and 13% (long term) of the feed land of pigs, poultry, eggs and farmed fish, against all of it in the thesis.

## Not in this method (candidates)

* **Compost.** 19% of consumer-level waste is composted. It returns nutrients, not feed; the model has no nutrient constraint, so compost has no effect on capacity here.
* **Ruminants.** The sheet displaces only monogastric production. Fruit, vegetable and bakery waste and whey are lawfully fed to cattle, sheep and goats; the model's ruminants are mainly on pasture, so the gain is probably small, but it is not zero.
* **Rendered animal by-products** (meat and bone meal, fish meal, poultry meal) are feed for pigs, poultry and farmed fish where the law allows (not for the same species); the model leaves them out in both terms.
* **Insects and other conversions** (black soldier fly) are outside the model.
* **Item-level dry matter and feed-grade shares.** Dry matters are by diet category and the feed-grade classes are judgements (`Settings!BL12:BL17` in the release can be edited); the whey (cheese) and sugar (bagasse) items carry most of the processing pool and are worth checking item by item.
* **Stage-specific uptake in the long term.** One uptake is applied to all stages; Japan's sector rates suggest manufacturing far above households.

## Decisions

1. Publish `2025-recycling-stage` as the line-2 alternate; keep `2025-fuel` as line 1 (the like-for-like comparison with 2011).
2. For the comparison paper, report the long term both ways (14.1 and 12.7 million) and say that the difference is the correction to the recycling credit: dry matter, uptake and the law.
3. Dashboard named scenarios: today's law and 2018-19 practice (short), Japan and South Korea practice with adapted law (long, 40%), and a high case at Japan without households (52%) as the evidence-based upper end.

Sources for the evidence table: zu Ermgassen et al. (2016), Food Policy, open access at https://pmc.ncbi.nlm.nih.gov/articles/PMC4750877 (Japan, South Korea, heat treatment, 39.2%, outbreaks); press reports of South Korea's 98% (Washington Post via Environmental Health News; the share to feed varies by source); Japan's sector rates from MAFF figures as reported in secondary sources (2010: manufacturing 94%, retail 37%, restaurants 17%; a Miyagi University report: food service 35% in 2022), not checked against the ministry's tables.
