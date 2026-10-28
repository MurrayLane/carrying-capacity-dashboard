# Recycling split by stage, origin and dry matter (SCOPE.md E4 and E15)

**Line 2 of the two lines of enquiry (an improved method).** Line 1, the thesis method on current data, is release `2025-fuel` and the rest of `README.md`; nothing in line 1 changed. This page is the
method that I think the thesis's own workbook would have used had it split recycling the way it already splits the losses. It is published as the alternate release `2025-recycling-stage` (extends `2025-fuel`), so both numbers can be shown side by side.

## What the thesis method does

`Base!P` credits the recycling setting times every recyclable loss of every food, `1 - E*H*J*M` of its primary production (inedible part, consumer waste, retail waste, primary-to-retail loss; processing losses for foods whose processing yield is below one),
in wet grams. The `Recycle` sheet then shares that total among pork, eggs, chicken, duck, turkey, farmed fish and farmed seafood in proportion to what is eaten, divides by each animal's feed conversion ratio (a mass of dry feed per mass of product) and subtracts the resulting displaced production from the land those animals need.
Four things follow that the thesis does not say:

1. **It treats every gram alike.** A gram of apple core (15% dry matter) counts as a gram of grain (88%), and the conversion ratios are measured on dry feed.
2. **It feeds animal-origin waste to animals.** Meat, fish, dairy and egg waste are 48% of the short-term pool and 32% of the long-term pool; feeding food waste containing meat or dairy to pigs or ruminants is banned in every state and territory (and to poultry in Queensland).
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

Each part is multiplied by (a) the share of it that can be fed, plant and animal origin separately (`Settings!BL4:BM8`), (b) for processing by-products, the feed-grade share of the by-product class (whey and skim milk, bran and offal, oilseed meal, potato and corn residues: fed; shells, hulls, bagasse, pomace, grounds and animal by-products: not fed), and
(c) its dry matter, relative to the 88% dry matter of feed. Dry matters are medians of the raw foods of the diet category in the AUSNUT 2007 table (archive, `prelim models/ausnut07full.xls`) for fruit (15%), green (9%), other (8%), orange (15%) and starchy (22%) vegetables and nuts (97%); dried legumes 90%, grain 88%, cow's milk 13% and whey 7% (judgement from the same table and standard feed tables).
The recycling setting keeps its meaning as the uptake of what can be fed. With every share set to one and dry matters to one the formulas reproduce the thesis result to the person (checked for Australia, NSW and ACT, Queensland, short and long term).

Capacity of Australia, millions of people, as each correction is added (`stages_ladder.csv`; avoidable waste 12% short term, 0% long term):

Short term (recycling 0% gives 48.00 in every row):

| Step | recycling 25% | 50% | 100% |
|---|---|---|---|
| thesis (as published) | 48.47 | 48.93 | 49.17 |
| dry matter of the waste counted | 48.15 | 48.29 | 48.58 |
| animal-origin waste not fed | 48.11 | 48.22 | 48.44 |
| only feed-grade by-products (the improved method) | 48.09 | 48.18 | 48.36 |

Long term (recycling 0% gives 12.53 in every row):

| Step | recycling 25% | 50% | 100% |
|---|---|---|---|
| thesis (as published) | 13.09 | 13.70 | 14.05 |
| dry matter of the waste counted | 12.69 | 12.85 | 13.18 |
| animal-origin waste not fed | 12.67 | 12.81 | 13.10 |
| only feed-grade by-products (the improved method) | 12.63 | 12.73 | 12.94 |

* **The thesis's long-term credit of 14.05 million falls to 12.94 million** (-1.1 million, -8%) once dry matter, the law and feed-grade by-products are counted; the dry-matter correction is the largest single step (-0.9 million) and the law and by-products take 0.24 million between them.
* In the short term the full credit is small either way (49.17 against 48.36 million at 100%).
* Because the thesis's credit was capped at the whole industry, the thesis result hides how little of it is real. With the corrections the recycled feed replaces 29 to 31% of the feed land of pigs, poultry, eggs and farmed fish at 100% recycling.

## What can be fed, and what is fed today

The pool that survives the corrections (dry-matter feed grams a person a week at 100% uptake; `pool.csv`), and how much of each stage's pool was fed in 2018-19 (FIAL 2021 Table 3: retail 68 of 629 thousand tonnes to feed, manufacturing 6,253 of 11,131, households, food service and procurement none; primary production not measured):

Short term:

| Stage | Fed pool (g a week) | Share | Fed in 2018-19 |
|---|---|---|---|
| primary to retail (culls, transport, packing) | 68 | 3% | 0% |
| retail | 499 | 22% | 11% |
| consumer avoidable waste (households, food service) | 979 | 44% | 0% |
| inedible parts (peel, core, bones, shells) | 140 | 6% | 0% |
| processing by-products | 543 | 24% | 56% |
| all stages | 2,228 | 100% | 16% |

Long term:

| Stage | Fed pool (g a week) | Share | Fed in 2018-19 |
|---|---|---|---|
| primary to retail (culls, transport, packing) | 20 | 2% | 0% |
| retail | 41 | 3% | 11% |
| consumer avoidable waste (households, food service) | 81 | 6% | 0% |
| inedible parts (peel, core, bones, shells) | 331 | 26% | 0% |
| processing by-products | 795 | 63% | 56% |
| all stages | 1,269 | 100% | 36% |

* **Consumer-level waste is the biggest part of the short-term pool (44%) and none of it is fed today**; the barrier is collection and the law, not the model.
* **By-products are the biggest part of the long-term pool (63%)** and are the part that is already fed. Weighted by the pools, 16% of the short-term pool and 36% of the long-term pool is fed on 2018-19 practice.
* The release therefore sets the short-term recycling to **16%** (the practice of 2018-19, instead of the thesis's 0%) and keeps the long term at 100% of the feasible pool, the counterpart of the thesis's 100%.

## Results

Release `2025-recycling-stage`, millions of people, at each release's own settings:

| Zone | Short term: 2025-fuel | 2025-recycling-stage | Long term: 2025-fuel | 2025-recycling-stage |
|---|---|---|---|---|
| Australia | 48.00 | 48.06 | 14.05 | 12.94 |
| NSW and ACT | 11.99 | 12.01 | 2.44 | 2.27 |
| Victoria | 6.96 | 6.99 | 0.95 | 0.87 |
| Queensland | 8.84 | 9.05 | 0.86 | 0.81 |
| Western Australia | 3.56 | 3.56 | 1.80 | 1.79 |

The short term rises by 0.06 million for Australia (0.2 in Queensland). The long term falls by 1.1 million, which is the change to the recycling credit alone.

## Not in this method (candidates)

* **Compost.** 19% of consumer-level waste is composted. It returns nutrients, not feed; the model has no nutrient constraint, so compost has no effect on capacity here.
* **Ruminants.** The sheet displaces only monogastric production. Fruit, vegetable and bakery waste and whey are lawfully fed to cattle, sheep and goats; the model's ruminants are mainly on pasture, so the gain is probably small, but it is not zero.
* **Rendered animal by-products** (meat and bone meal, fish meal, poultry meal) are lawful feed for pigs, poultry and farmed fish, but not for the same species; the model treats animal waste as not fed.
* **Insects and other conversions** (black soldier fly) are outside the model.
* **Item-level dry matter and feed-grade shares.** Dry matters are by diet category and the feed-grade classes are judgements (`Settings!BL12:BL17` in the release can be edited); the whey (cheese) and sugar (bagasse) items carry most of the processing pool and are worth checking item by item.
* **Uptake of plant waste at the consumer level.** The legal ceiling is counted; what a collection scheme would achieve is not measured in Australia, and is left to the recycling setting.

## Decisions

1. Publish `2025-recycling-stage` as the line-2 alternate; keep `2025-fuel` as line 1 (the like-for-like comparison with 2011).
2. For the comparison paper, report the long-term result both ways (14.1 and 12.9 million) and say that the difference is the correction to the recycling credit.
3. Decide whether the dashboard's named long-term scenarios use 100% of the feasible pool (as here) or a lower uptake; the ladder gives 25% and 50%.
