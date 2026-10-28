#!/usr/bin/env python3
"""Writes analysis/waste_2025/README_stages.md from stages.csv, pool.csv and stages_ladder.csv (run recycling_stages.mjs stages / pool / ladder first).
Usage: python3 analysis/waste_2025/write_readme_stages.py          (repository root)"""
import csv, collections
rd = lambda f: list(csv.DictReader(open('analysis/waste_2025/' + f)))
st, pl, la = rd('stages.csv'), rd('pool.csv'), rd('stages_ladder.csv')
cap = {(r['setting'], int(r['zone']), r['step'], float(r['recycling'])): int(r['capacity']) / 1e6 for r in la}
STEPS = ['thesis (as published)', 'dry matter of the waste counted', 'animal-origin waste not fed', 'only feed-grade by-products (the improved method)', 'law adapted in the long term; one uptake for all stages', 'uptake by stage (the improved method)']
def stage_table(k):
    rows = [r for r in st if r['setting'] == k]; stages = list(dict.fromkeys(r['stage'] for r in rows)); out = ['| Stage | Plant origin | Animal origin | Share of the pool |', '|---|---|---|---|']
    for s in stages:
        p = next(r for r in rows if r['stage'] == s and r['origin'] == 'plant'); a = next(r for r in rows if r['stage'] == s and r['origin'] == 'animal')
        out.append(f"| {s} | {int(p['g_per_week']):,} | {int(a['g_per_week']):,} | {(float(p['share_of_pool']) + float(a['share_of_pool'])) * 100:.0f}% |")
    tp = sum(int(r['g_per_week']) for r in rows if r['origin'] == 'plant'); ta = sum(int(r['g_per_week']) for r in rows if r['origin'] == 'animal')
    out.append(f'| **All stages** | **{tp:,}** | **{ta:,}** | **{tp + ta:,}** (animal origin {ta / (tp + ta) * 100:.0f}%) |'); return '\n'.join(out)
def pool_table(k):
    rows = [r for r in pl if r['setting'] == k]; out = ['| Stage | Fed pool (g a week) | Share | Fed in 2018-19 | Uptake pattern in force |', '|---|---|---|---|---|']
    for r in rows: out.append(f"| {r['stage']} | {int(r['fed_pool_g_per_week']):,} | {float(r['share_of_pool']) * 100:.0f}% | {float(r['uptake_2018_19']) * 100:.0f}% | {float(r['uptake_pattern']) * 100:.0f}% |")
    return '\n'.join(out)
def ladder(k, steps, recs=(0.25, 0.4, 0.5, 0.75, 1.0)):
    out = ['| Step | ' + ' | '.join(f'uptake {int(r * 100)}%' for r in recs) + ' |', '|---|' + '---|' * len(recs)]
    for s_ in steps: out.append(f"| {s_} | " + ' | '.join(f'{cap[(k, 1, s_, r)]:.2f}' for r in recs) + ' |')
    return '\n'.join(out)
zt = ['| Zone | Short term: 2025-fuel | 2025-recycling-stage | Long term: 2025-fuel | 2025-recycling-stage |', '|---|---|---|---|---|']
Z = {1: ('Australia', 48.00, 48.06, 14.05, 12.75), 2: ('NSW and ACT', 11.99, 12.01, 2.44, 2.24), 15: ('Victoria', 6.96, 7.00, 0.95, 0.86), 26: ('Queensland', 8.84, 9.06, 0.86, 0.80), 49: ('Western Australia', 3.56, 3.56, 1.80, 1.79)}
for z, (n, a, b, c, d) in Z.items(): zt.append(f'| {n} | {a:.2f} | {b:.2f} | {c:.2f} | {d:.2f} |')
t0 = lambda k, s_: cap[(k, 1, s_, 0.0)]
txt = f"""# Recycling split by stage, origin, dry matter and the law in force (SCOPE.md E4 and E15)

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

{stage_table('short')}

Long term (the thesis setting, no avoidable waste; the first three stages are the fixed losses of some fruit):

{stage_table('long')}

Animal origin means the primary product is milk, egg, meat, fish or seafood. In the short term cheese whey alone is 1,561 g of the pool (13%) and cane sugar's bagasse 534 g (5%).

## The improved method

Each part is multiplied by (a) the share of it that may be fed, plant and animal origin separately, with the law in force choosing between two animal-origin columns (`Settings!BL4:BO8`), (b) for processing by-products, the feed-grade share of the by-product class (whey and skim milk, bran and offal, oilseed meal, potato and corn residues: fed; shells, hulls, bagasse, pomace, grounds and animal by-products: not fed), and
(c) its dry matter, relative to the 88% dry matter of feed. Dry matters are medians of the raw foods of the diet category in the AUSNUT 2007 table (archive, `prelim models/ausnut07full.xls`) for fruit (15%), green (9%), other (8%), orange (15%) and starchy (22%) vegetables and nuts (97%); dried legumes 90%, grain 88%, cow's milk 13% and whey 7% (judgement from the same table and standard feed tables).
The recycling setting keeps its meaning as the uptake of what may be fed. With every share set to one and dry matters to one the formulas reproduce the thesis result to the person (checked for Australia, NSW and ACT, Queensland, short and long term).

**The law in force follows the time frame** (`Settings!B8`, the years the result must hold: 1 in the short term, 100 in the long term). Under 20 years (`Settings!BL9`, editable) the current law applies; from 20 years on the adapted law applies.

* **Current law (short term):** animal-origin food waste is not fed; plant waste and feed-grade by-products (including whey) are.
* **Adapted law (long term, the Japan and South Korea model):** heat-treated animal-origin food waste may be fed to pigs, poultry and farmed fish, never to ruminants. The waste of a species is kept from its own kind (`Settings!BL10`; Japan and South Korea allow it, the EU does not, and it changes the result by 0.01 to 0.03 million).

**Uptake by stage.** Each stage has its own uptake (`Settings!BP4:BQ8`), and the recycling setting is the share achieved of the pattern of the period (`Settings!BR4:BR8`), so 100% is the pattern, not everything:

* **Time frame under 20 years: the practice of 2018-19** (FIAL 2021 Table 3): retail 11% (68 of 629 thousand tonnes to feed), manufacturing 56% (6,253 of 11,131), households, food service and procurement none; primary production is not measured and counts as none. Weighted by the pools below this is 16% of the short-term pool.
* **20 years and longer: the benchmark** of the countries that have done it, 40% of every stage that may be fed (Japan 35.9%, South Korea 42.5%; section below), except manufacturing, which stays at the 56% it already reaches. Weighted by the long-term pools this is 49%.

The thesis applied one setting to every stage alike, which is wrong at both ends: manufacturing residues are already fed at more than 40%, and households feed nothing.

Capacity of Australia, millions of people, as each correction is added (`stages_ladder.csv`; avoidable waste 12% short term, 0% long term). The last two rows are the long-term law and apply to the long term only; with no uptake the capacity is {t0('short', STEPS[0]):.2f} (short) and {t0('long', STEPS[0]):.2f} (long). Columns are the uptake (every stage alike) except the last row, whose columns are the share achieved of the stage pattern.

Short term (current law):

{ladder('short', STEPS[:4] + [STEPS[5]])}

Long term:

{ladder('long', STEPS)}

* **The thesis's long-term credit of 14.05 million falls to 12.75 million** once the correction of the method is made and the stage pattern is used: 0.9 million is dry matter, 0.2 the feed-grade filter and the law of today net of the adapted law, and 0.2 the stage pattern in place of 100%.
* **Adapting the law is worth little: +0.04 million at 100% uptake.** The reason is mass, not principle: in the long term the animal-origin waste that the law would newly allow is the inedible parts of meat and fish (741 g a week wet, at 25 to 30% dry matter, and with the waste of a species kept from its own kind), because whey is fed under both laws and the long-term diet is low in meat.
* In the short term the full credit is small either way (49.17 against 48.36 million at 100% of everything).

## Is 100% ever feasible?

No. Nothing in the evidence comes near it, and the thesis's 100% is not a defensible default for a long-term scenario. The best-documented systems that feed food waste to animals deliberately, with the law changed to allow it, reach about 40%:

| System | Share of food waste fed to animals | Notes |
|---|---|---|
| Japan, 2006-07 | 35.9% of all food waste (52.5% of manufacturing, retail and catering waste) | Heat-treated "ecofeed"; households are not fed |
| South Korea, 2006 | 42.5% of all food waste | Landfill of food waste banned since 2005; separate collection compulsory since 2013; later reports of 98% recycled by all routes, about half to feed |
| EU, a modelling assumption | 39.2% | The mean of Japan and South Korea, used by zu Ermgassen and colleagues (2016) to estimate that regulated swill could replace 20% of EU pig feed on a dry basis |

Japan's food industry by sector (reported, by all routes of recycling, not feed alone): manufacturing 94%, retail 37% and restaurants 17% in 2010, food service 35% in 2022, with households outside the system. Reasons the share stays well below 100% even where the law allows it and the state pays: waste arises where animals are not (cities), collection and sorting are costly and contaminated streams are unusable, some of it (packaging, bones, shells, spoiled and mixed waste) is not feed, there is a limit to how much a pig or a chicken eats, and competing uses (compost, biogas) are favoured by policy.

**So the release sets the long-term benchmark at 40% of each stage** (manufacturing at its observed 56%), the national rates achieved by the two countries that have done it, applied to the part of the waste that may be fed. This is conservative in one respect (their rates are shares of all food waste, including parts that cannot be fed) and generous in another (Australian waste is more dispersed than theirs, and Japan feeds none of its household waste). Long-term capacity of Australia at other uniform uptakes, adapted law:

{ladder('long', STEPS[4:5], recs=(0.25, 0.4, 0.5, 0.75, 1.0))}

With no uptake: {t0('long', STEPS[0]):.2f}. Japan without households (52.5%) would give 12.76 million at a uniform uptake; the stage pattern at 100% gives {cap[('long', 1, STEPS[5], 1.0)]:.2f}.

## The law, and the disease argument

The short term follows the law as it is, and the long term may assume the law is adapted. The reason the law exists is disease: the 2001 foot-and-mouth outbreak in the United Kingdom, which cost the economy about £8 billion, is thought to have started from uncooked food waste fed to pigs, and the EU banned feeding catering waste in 2002; Australia's rules rest on the same risk, with African swine fever added. Heat treatment inactivates the viruses (Japan: 70 degrees for 30 minutes or 80 degrees for 3 minutes; South Korea: at least 80 degrees core temperature for 30 minutes), and no outbreak in Japan or South Korea has been traced to ecofeed; their 2010 foot-and-mouth outbreaks were not linked to it. Feeding meat waste to ruminants remains illegal in both (BSE).

The argument that localising food systems lowers the global disease risk is reasonable and fits this scenario: the pathway in the 2001 outbreak was imported meat entering the food waste stream, and a system in which animals are fed only the waste of food produced and heat-treated at home, with traceability, closes that pathway. It does not remove the risk (domestic outbreaks, illegal feeding by smallholders, failures of treatment), and the model does not test it: it has no disease or trade component. I have recorded it as a reason to accept the adapted law as the long-term assumption, not as a result. I have not checked the current Australian regulations beyond the FIAL summary used in `README.md`.

## What can be fed, and what is fed today

The pool that survives the corrections (dry-matter feed grams a person a week at 100% uptake; `pool.csv`) under the law of each term, and how much of each stage's pool was fed in 2018-19 (FIAL 2021 Table 3: retail 68 of 629 thousand tonnes to feed, manufacturing 6,253 of 11,131, households, food service and procurement none; primary production not measured):

Short term (current law):

{pool_table('short')}

Long term (adapted law; the 'fed in 2018-19' column is the Australian practice, the last column the long-term benchmark):

{pool_table('long')}

* **Consumer-level waste is the biggest part of the short-term pool (44%) and none of it is fed today**; the barrier is collection and the law, not the model.
* **By-products are the biggest part of the long-term pool (54%)** and are the part that is already fed. Weighted by the pools, 16% of the short-term pool was fed on 2018-19 practice, which the short-term pattern reproduces, instead of the thesis's 0%.

## Results

Release `2025-recycling-stage`, millions of people, at each release's own settings (recycling setting 100% of the pattern in both terms; short term: current law, practice of 2018-19; long term: adapted law, benchmark):

{chr(10).join(zt)}

The short term rises by 0.06 million for Australia (0.2 in Queensland). The long term falls by 1.3 million; of this, 0.9 is the dry-matter correction, 0.2 the feed-grade filter and the law of today net of the adapted law, and 0.2 the stage pattern in place of 100%. At these settings the recycled feed replaces 5% (short term) and 16% (long term) of the feed land of pigs, poultry, eggs and farmed fish, against all of it in the thesis.

## Not in this method (candidates)

* **Compost.** 19% of consumer-level waste is composted. It returns nutrients, not feed; the model has no nutrient constraint, so compost has no effect on capacity here.
* **Ruminants.** The sheet displaces only monogastric production. Fruit, vegetable and bakery waste and whey are lawfully fed to cattle, sheep and goats; the model's ruminants are mainly on pasture, so the gain is probably small, but it is not zero.
* **Rendered animal by-products** (meat and bone meal, fish meal, poultry meal) are feed for pigs, poultry and farmed fish where the law allows (not for the same species); the model leaves them out in both terms.
* **Insects and other conversions** (black soldier fly) are outside the model.
* **Item-level dry matter and feed-grade shares.** Dry matters are by diet category and the feed-grade classes are judgements (`Settings!BL12:BL17` in the release can be edited); the whey (cheese) and sugar (bagasse) items carry most of the processing pool and are worth checking item by item.
* **Sector rates for the long term.** The benchmark is 40% for every stage but manufacturing; Japan's sector rates (manufacturing 94%, retail 37%, restaurants 17% by all routes) suggest manufacturing higher and food service lower, but they are not rates of feeding and are not checked against the ministry's tables.
* **Regional practice.** The practice of 2018-19 is national and is applied to every zone.

## Decisions

1. Publish `2025-recycling-stage` as the line-2 alternate; keep `2025-fuel` as line 1 (the like-for-like comparison with 2011).
2. For the comparison paper, report the long term both ways (14.1 and 12.7 million) and say that the difference is the correction to the recycling credit: dry matter, the law and the stage pattern. The 2011 to 2025 comparison, with the effect of data and of method separated, is read from `results/comparison_cells.csv`.
3. Dashboard named scenarios (not built): today's law and the practice of 2018-19 (short); the Japan and South Korea benchmark with the adapted law (long); and a high case at Japan without households (52% at every stage) as the evidence-based upper end.

Sources for the evidence table: zu Ermgassen et al. (2016), Food Policy, open access at https://pmc.ncbi.nlm.nih.gov/articles/PMC4750877 (Japan, South Korea, heat treatment, 39.2%, outbreaks); press reports of South Korea's 98% (Washington Post via Environmental Health News; the share to feed varies by source); Japan's sector rates from MAFF figures as reported in secondary sources (2010: manufacturing 94%, retail 37%, restaurants 17%; a Miyagi University report: food service 35% in 2022), not checked against the ministry's tables.
"""
open('analysis/waste_2025/README_stages.md', 'w').write(txt); print('wrote README_stages.md', len(txt))
