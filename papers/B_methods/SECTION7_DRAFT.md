# Paper B, section 7 (draft for Murray): which method for which purpose

Drafted 2026-11-06 from the method tests (`analysis/method_tests_2025/README.md`), the design-choice measurements and `analysis/comparators_2025/`. It is a matrix, a recommendation per purpose and a reporting checklist, not prose. The ratings are judgements from what each test showed and are for Murray to change.

**Rating.** ● well suited (the method sees what the purpose turns on) · ◐ partly (useful with a stated limit or beside another method) · ○ not suited (it cannot see what the purpose turns on).

The methods: **EP** energy and protein balance (Gifford; Henry and Godden) · **FP** ecological footprint, food row (Simpson) · **HALF** land per diet (Alexander) · **PPH** people per hectare (Cassidy) · **CB** commodity balance (Foran and Poldy) · **FAIL** failure probability (Fearnside) · **LDB** resource-based land and diet balance (the thesis method and its corrected and improved forms; Peters and Fairlie are the same family at other scales).

## The matrix

| Purpose (in order of how strongly the evidence supports it) | EP | FP | HALF | PPH | CB | FAIL | LDB |
|---|---|---|---|---|---|---|---|
| **1. Food security and drought risk** | ○ | ○ | ○ | ○ | ◐ | ● | ● |
| **2. Explaining why national estimates range from 9 to 100 million** | ◐ | ◐ | ○ | ○ | ◐ | ◐ | ● |
| **3. Regional and local land-use planning** | ○ | ○ | ○ | ○ | ○ | ◐ | ● |
| **4. Diet change and land use** | ○ | ◐ | ● | ◐ | ○ | ○ | ● |

## Why each rating (evidence from the tests)

**1. Food security and drought risk.**
* FAIL ●: the only method built on the question "how often does supply fall short". On the model's data the average-year capacity of 41.5 million falls to 30.8 at a 1-in-10 failure level and 18.9 at 1 in 100; the failure risk at today's population is about 6% a year (7% in 2011). Fearnside's own caution: it needs one criterion per standard and heavy data, and the model carries the weather as one factor on every yield and the default diet.
* LDB ●: supplies the level the failure curve is read from, with the diet and the pasture and crop pairing. It reproduces the Jones committee's 30 to 35 million at a 1-in-10 allowance (30.8 corrected).
* CB ◐: finds which item runs out first (fish, 12 to 17 million; then meat, 40 to 41), which the aggregate methods cannot; it has no weather and no land.
* EP, FP, HALF, PPH ○: they count calories or land in an average year at a single productivity; none has a way to see a bad year or a diet that has to balance (they read 134 to 343 million).

**2. Explaining the 9 to 100 million range.**
* LDB ●: one model, one data set, run under each definition, spans 15.6 to 62.9 million (a factor of 4) without counting exports; counting exports takes it to 100. The 9 million is the author's own pre-correction long-term figure.
* EP, FP, CB, FAIL ◐: each reproduces a family of published estimates (EP the 1975 and 1995 figures; FP the footprint ratios; CB the 30 to 32 million meat count; FAIL the Jones figures) and shows what that family counts and leaves out.
* HALF, PPH ○: not capacity methods (the authors say HALF is not predictive; PPH is cropland only); they do not produce estimates in the disputed range.

**3. Regional and local land-use planning.**
* LDB ●: the only method with a unit of land, a diet and a pairing of pasture and crops at the regional level; the unit of self-sufficiency decides the answer (states 75%, NRM regions 44%, SA3 44%, SA2 37% of the national figure on the state yield basis) and rangeland is stranded unless a unit also holds cropland.
* FAIL ◐: the right idea for a site (Fearnside's own application was 23,600 ha), but he states that KPROG2 needs so much data it is impractical for large areas.
* EP, FP, HALF, PPH, CB ○: national or global in construction; FP and HALF use world-average productivity, so they cannot say what a region's own land feeds (they read Australia as 265 to 343 million); PPH is cropland only; EP and CB take national totals.

**4. Diet change and land use.**
* HALF ●: built for it, and reproduced well on 2011 data (world, United States and India within 2%): Australia's HALF fell 30% between 2011 and 2021-23 as beef and mutton consumption fell, and is 2.5 times the world average. It measures the land a diet needs at world-average production, not at Australian productivity.
* LDB ●: gives the diet's land at Australian productivity (about 6.2 ha a person on the default diet, 0.27 with no meat), the shape of capacity against meat share (a peak at an intermediate share because a little pasture-fed meat uses land crops cannot), and, with the nutrition model, diets that meet the nutrient constraints.
* FP ◐: compares diets by land, with the same world-average basis as HALF plus energy land; PPH ◐: the effect of crop use (feed, biofuel) on cropland only, with no pasture.

## What the matrix says in short
* **No single method serves all four purposes.** Only the land-and-diet balance is well suited to all four, and for purpose 1 it needs the failure-probability view beside it.
* **The aggregate methods answer a different question.** Energy balance, footprint, HALF and people per hectare ask what land or calories a diet needs at a given productivity; read as a capacity they give three to eight times the land-and-diet balance because none carries the pairing of pasture-fed food with crops that binds Australia.
* **Use two methods for a security claim.** A level from a land-and-diet balance with a stated diet, and a failure probability from the weather record, reported together; add a commodity balance to name the item that fails first.
* **For comparison across countries use HALF; for what Australia's land can feed use the balance.**

## Minimum reporting checklist (each item is a design choice that moved the answer by more than 1.2 times)
1. The question the number answers, in a sentence ("how many could be fed", "how often would supply fail", "how much land does this diet need").
2. Exports: in or out, and how counted (a proportion, an energy count, or none).
3. The diet: composition and energy, who eats it, and whether it is today's or a stated alternative.
4. Waste and losses: the rate and its source (Australian or imported).
5. Weather: an average year, or an allowance with its return period or failure probability.
6. The land base: which land counts, at what productivity (world-average or local), and any reserve.
7. The unit of self-sufficiency and its boundary (nation, state, catchment, SA2).
8. The time frame and settings (today's, or a stated long-term plan).
9. The data year and source for production, land and population.
10. The uncertainty: a range, and which inputs drive it.
11. Whether the implementation reproduces the method's authors' own figure, and where it does not.
12. Code and data availability.

## Cautions for the paper
* A figure of people "fed" is not a forecast or a target; none of these methods says what population should be.
* The tests are on Australian data; the ratings may differ where grazing is a small share of food land (the United States, much of Europe).
* The ratings and the matrix are the author's judgement on seven methods; the three planning-oriented studies of the earlier work (Peters, Fairlie, Noosa and Douglas, Gutteridge's South East Queensland) are treated as the same family as the balance at other scales.
