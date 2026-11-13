# Paper A supplementary information

The sections below hold detail moved from the main text to keep it under 8,000 words (decision 92). Each section names the main-text section it supports; the main text keeps the essential finding and a pointer. Release names, yield bases and flags follow the main-text rules.

[Table S1: the settings of both presets (short term and long term) in both data years, from `results/2011-fixed.csv` and `results/2025-fixed.csv` settings columns; named in section 2; not built (N-A2, decision 66)]

## S1. Regional detail for sections 3 and 4

Swan, which holds Perth, is the clearest boundary case of section 3. Its short-term capacity falls from 170 thousand to 6 thousand while its population rises from 1.70 to 2.27 million (`2011-fixed` to `2025-fixed`).

Elsewhere on the coast the picture is mixed: Wet Tropics, Mackay Whitsunday, North Tasmania and Corangamite flip in the short term, while South Coast WA, Eyre Peninsula and Glenelg Hopkins are under capacity in both years in the short term.

The regional decomposition of section 4 (Figure 3) is on the corrected releases (`2011-fixed` to `2025-fixed`). In Central West NSW, Lachlan and Namoi most of the short-term gain is livestock: in Central West NSW livestock added 356,807 people to a capacity that rose from 1,333,553 to 1,798,009. Elsewhere inland the share differs: livestock carried 21% of the short-term gain in Murrumbidgee-ACT, and in the Murray it took 97,458 people off a gain of 153,025. In Swan the land layer took 167,976 off a 2011 capacity of 170,101, the boundary case of section 3. In Fitzroy consumption took 62,789 and the red meat mix 38,290 off short-term capacity, and in the long term crop yields added 34,818 there against 658 from livestock.

## S2. The partition: boundary detail and the best contiguous split (section 5)

All figures in this section are on the 2025 corrected release (`2025-fixed`) and the state-yield basis unless named otherwise.

As shares of national capacity, the regions of New South Wales summed to 17.6% against 25.3% for its SA4s. In South Australia the figures were 1.2% against 4.8%, and in Western Australia 2.0% against 5.1%. The other states were about equal on the two partitions.

SA4 406 joins the arid country of SA Arid Lands with the cropland of the Eyre Peninsula and had a capacity of 1.7 million. The two regions apart had 41 thousand and 132 thousand. In Western Australia the Rangelands region, with 646,000 km2 of pasture and 937 km2 of cropland, had a capacity of 241 thousand. SA4 511 had 1.5 million. Units with more than 1,000 km2 of pasture and cropland under 2% of that pasture held 71% of the nation's pasture among the regions (8 units), 72% among the SA3s (18) and 51% among the SA4s (3). The land the partitions left unused rose from 1.96 million km2 for the nation to 3.67 million for the SA4s and 4.50 million for the regions.

Capacity was exactly proportional to land: 0.5, 0.1 and 0.01 times the national land gave 100.0% of the same fraction of national capacity. A split in which every unit had the national land mix would therefore lose nothing. On the national yield vector, random groupings of the SA2s into 53 groups kept 68 to 81% of national capacity, against 33% for the 53 regions (52 NRM regions and the Northern Territory) as drawn. These are spreads across five draws, not uncertainty ranges. The SA4s, at 54%, were slightly worse than random groupings of their number (56 to 69%), and the SA3s, at 35%, were about equal to random (34 to 44%). The best contiguous split found at 53 regions was searched with each region capped at 650,000 km2 of land (Supplementary Figure S1).

Foodshed reach varies with diet and land type (Kurtz et al. 2020).

[Supplementary Figure S1: the best contiguous split found at 53 regions with each region capped at 650,000 km2 of land, 2025 corrected release (2025-fixed), short term; from `analysis/regionalise_2025/summary.csv` and `analysis/regionalise_2025/ideal_K53_cap650k.png`, drawn by `map_regions.py`]

## S3. Named scenarios (section 8)

Table S2 gives every named scenario on the 2025 corrected release (2025-fixed), against a reference of 41.5 million in the short term and 15.6 million in the long term. Recycling and the two fuel allowances moved either term by less than 2%. The 340-litre fuel allowance took 1.8% off the long term on the corrected release and 18.8% on the improved release (2025-improved), a method effect that has not been explained.

Table S2. Named scenarios, change in national capacity on the reference, 2025 corrected release (2025-fixed; grain stores with the resilience tables of 2025-store-1 and 2025-store-2). Built from `analysis/paper_a/scenarios_by_region.csv` (rows with `reference_release` 2025-fixed, column `change on reference`). The fuel scenarios set the long-term fuel only (`scenarios/scenarios.json`); Table S5 gives the 156-litre measure set in both terms.

| Scenario | Short term | Long term |
|---|---|---|
| Reference (national capacity, million) | 41.5 | 15.6 |
| Field-crop yields 12% lower | -0.09% | -0.28% |
| Field-crop yields 24% lower | -0.2% | -0.65% |
| Waste at 6% | +16.4% | -8.15% |
| No avoidable waste | +33.21% | 0% |
| No recycling | 0% | -1.21% |
| Half recycling | +1.7% | -0.28% |
| Liquid fuel 156 litres a person | 0% | +0.78% |
| Liquid fuel 340 litres a person | 0% | -1.83% |
| Grain store of one year | 0% | +48.45% |
| Grain store of two years | 0% | +64.47% |

## S4. Ranges and method effects by region (section 9)

**The ranges.** Twelve of the 13 sampled choices vary in the corrected and published 2025 releases (2025-fixed and 2025-mirror). The thirteenth, the long-term feeding benchmark, has no effect in those releases; it is drawn in the improved release (2025-improved), with a negligible national effect. On 2025-fixed the meat window alone explains 81% of the variance of the short-term national capacity and 36% of the long-term. The resilience table alone explains 52% of the long-term variance, and its weight is one of the judgement ends. These shares belong to the whole choices: the equal chances of the meat window, the equal weight on the leave-one-out resilience table and the low ends are the parts that rest on judgement.

**The corrections by region.** Each method choice was applied alone to the published-method release on 2025 data (2025-mirror). The beef carcase correction (USDA undated; AUS-MEAT 2005) acts in the beef and cropping regions: Wet Tropics -21.5%, Lower Murray Darling -16.4% and Border Rivers-Maranoa-Balonne -15.4%. The biodiesel correction (Geoscience Australia and ABARE 2010) reaches +95.8% in Burdekin and +83.5% in South Tasmania. In the short term it moves the national figure by +0.1%.

**The improvements by region.** Dairy on land that can carry it has regional effects from -27.3% to +22.1% in the short term. It lowers SA Arid Lands (-27.3%) and Southern Gulf (-15.5%). It raises Wet Tropics (+22.1%), Rangelands (+22.0%) and Lower Murray Darling (+22.0%). In the long term it raises Rangelands by 53%. Australian loss factors raise nearly every region in the short term: +11.2% nationally and +0.8% to +22.6% by region, most in Swan. Reserve pro rata and recycling by stage act mainly in the long term, and they lower it: -5.8% and -9.7% nationally, against -1.1% and +0.1% in the short term. In the long term reserve pro rata takes up to 29.1% off a region (Condamine), and recycling by stage up to 18.2% (Southern Gulf). Beef output by state redistributes without changing the national figure: 0% nationally and -7.4% to +9.9% by region.

**Status under each tier.** The six southern and western regions that change long-term status between the corrected and improved releases are Mallee, Kangaroo Island, SA Arid Lands, SA Murray Darling Basin, South East SA and South West WA (Table S4).

Table S3. The effect of each method module applied alone, 2025 data, as a percentage of the published-method capacity (base release 2025-mirror): nation, with the regional minimum to maximum in brackets. Built from `analysis/paper_a/method_effects_summary.csv`.

| Module | Tier | Short term | Long term |
|---|---|---|---|
| Beef carcase yield | correction | -16.0 (-21.5 to 0.0) | 0.0 (-7.7 to 0.0) |
| Biodiesel yield | correction | +0.1 (0.0 to +6.9) | +20.7 (+3.4 to +97.9) |
| Australian loss factors | improvement | +11.2 (+0.8 to +22.6) | 0.0 (0.0 to 0.0) |
| Dairy on land that can carry it | improvement | +20.2 (-27.3 to +22.1) | +3.0 (-12.4 to +53.1) |
| Beef output by state | improvement | 0.0 (-7.4 to +9.9) | 0.0 (-5.0 to +3.9) |
| Reserve pro rata | improvement | -1.1 (-5.4 to 0.0) | -5.8 (-29.1 to 0.0) |
| Recycling by stage | improvement | +0.1 (0.0 to +4.3) | -9.7 (-18.2 to -1.5) |
| Organic ruminant factor | improvement | 0.0 (0.0 to 0.0) | 0.0 (0.0 to +7.6) |

Table S4. Regions over capacity (of 53) in 2025 under each method tier, and the regions that change status between the corrected and improved tiers. Releases 2025-mirror (published), 2025-fixed (corrected) and 2025-improved (improved). Built from `analysis/paper_a/method_status.csv` (2025 rows).

| 2025 | Published | Corrected | Improved | Regions that change status, corrected to improved |
|---|---|---|---|---|
| Short term | 15 | 16 | 15 | Corangamite |
| Long term | 36 | 32 | 36 | Mallee, Kangaroo Island, SA Arid Lands, SA Murray Darling Basin, South East SA, South West WA |

## S5. Four regions in depth (section 10)

All figures except the method effects are on the corrected releases (2011-fixed and 2025-fixed) and on each region's own yields (Table 7).

**Hawkesbury-Nepean-Sydney.** The region is over capacity in both years and both terms. Its short-term capacity fell from 66,198 to 46,572 people while its population grew from 4,073,137 to 5,401,609. Its long-term capacity is 7,186 in 2011 and 6,106 in 2025. Even the 95th percentile of its 2025 short-term capacity is 48,520 people. The fall in capacity carries the land-definition flag. With only the 2025 land layer swapped in, capacity is 0.491 of the 2011 figure, just below the rule's lower bound of 0.5. Cropping land is 389 km2 on the 2011 layer and 191 km2 on the 2025 layer, on an unchanged boundary. The change is therefore not read as a change in what the land can feed. James and O'Neill (2016, p. 183) found Sydney Basin farm data too uncertain to show a trend, with error margins above 25% in many ABS figures.

**The Murray with Murrumbidgee-ACT.** The Murray region is under capacity in both years and both terms. Its short-term capacity rose from 752,498 to 905,523 against a population of 102,847 to 121,808. Murrumbidgee-ACT, which holds Canberra, is under capacity in an average year: its 2025 population is 0.482 times its capacity. It is over capacity in the long term (2.431 times) and at a 1-in-100 drought (1.604 times). Its short-term capacity rose from 1,185,593 to 1,533,929 while its population grew from 529,508 to 738,895. In both regions the largest short-term method effects are measured on the published base (2025-mirror, section 9): dairy on good land (+17.8% and +17.9%) and the beef carcase correction (-15.0%). The Basin accounts for about 40% of national farm output (Wittwer and Waschik 2021, p. 919). Its median projected streamflow is about 20% lower under 2 °C of global warming (Prosser et al. 2021, p. 4). In northern Victoria, raw milk output fell by 1.3 billion litres between 2001-02 and 2009-10 (Sysak and Beilin 2017, p. 416). The model carries no water limit, so none of this enters the capacities (section 12).

**Avon.** Avon is a cropping region under capacity throughout. Its short-term capacity rose from 971,132 to 1,080,065 against a population of 55,850 to 69,727. In the long term it is among the strongest regions: its 2025 population is 0.14 times its long-term capacity. At a 1-in-100 drought its 2025 short-term capacity is 508,513 people. The model scales its yields by Western Australia's worst-year factor. Hughes and Lawson (2017, p. 189) found a larger climate effect on cropping productivity in Western Australia than nationally: -7.63% against -4.71% for all cropping farms, 2000-01 to 2014-15 (their Table 8.3).

**SA Arid Lands beside the Eyre Peninsula.** SA Arid Lands moved from over to under capacity in the short term. Its capacity rose from 2,164 to 28,609 while its population fell from 31,361 to 8,049. Both changes are matters of definition. The land layer alone raises its capacity 6.5 times. The 2011 population is the model's own figure, while the 2025 population is allocated from estimated resident population by residential land. The change is therefore not read as a change on the ground. In the long term its 2025 status is not robust to the range: 7,194 to 9,031 people against a population of 8,049. Its cropping neighbour, the Eyre Peninsula, carries no flag. There, capacity rose from 217,967 to 384,476 against a population of 41,397 to 59,255, and the region is under capacity in both years and both terms.

## S6. Measures with no read source beyond the model, and other detail (section 11)

Each measure was applied alone to the corrected 2025 release (2025-fixed) unless Table S5 names another release.

**Field crops, irrigation and cropland.** Field-crop yields 10% and 20% higher raise the short term by 0.1% and the long term by 0.2% and 0.3%. Horticulture yields 10% higher leave the short term unchanged and raise the long term by 0.2%. All yields 10% higher raise both terms by 10.0%. An irrigated share of cropland of 0.02 or 0.05, against a base of 0.007, raises both terms by 0.7% or 2.4%. Cropland 25% larger, taken from pasture, changes neither term. In the model, cropland can carry pasture-fed products but pasture cannot carry crops, so capacity is the same for any cropland share from 10% to 99% of the combined area (section 6).

**Diet, waste and fuel.** A meat-and-egg share of 7.5% gives 48.2 million (+16.2%) in the short term. No avoidable waste raises the short term to 55.3 million (+33.2%), and full recycling of food waste adds 2.2%. Liquid fuel of 156 litres a person, set in both terms, moves the short term by +0.1% and the long term by +0.8%.

**The grain store.** A one-year store for domestic use is about 11.5 Mt: 3.1 Mt for direct use at 112 kg a person, and 8.4 Mt for the feed grain embodied in meat at 303 kg a person.

**The regions as a pool.** On each zone's own yields and on 2025-fixed, the national capacity is 1.60 times the sum of the regional capacities in an average year. The factor is 1.82 at a 1-in-10 year. In the long term it is 2.60, and 3.00 on 2011 data (2011-fixed). The regions' pasture and cropland complement each other. In an average year the regions over capacity are short by 20.7 million people-equivalents, and the regions under capacity have 19.1 million to spare. At a 1-in-10 year the shortfall is 21.5 million and the spare 10.8 million. Northern supply chains run over 1000 km on roads cut by seasonal flooding (Higgins et al. 2018b, p. 341). Few studies follow shocks along supply chains (Davis et al. 2020).

**Measures the model cannot carry.** If meat output fell by the national capacity factor, it would be about 3.45 Mt at a 1-in-10 year and 2.95 Mt at a 1-in-20 year; that assumption is untested. Fish imports, 593 thousand tonnes, are about as large as the food use of fish, 641 thousand tonnes. In the commodity balance fish is the item that runs out first, at 12 to 17 million people. Pulses, 4.4 Mt produced and mostly exported, keep for a long time. The herd is also a store: the single-year capacity runs from 43.5 to 55.4 million across 2016 to 2025 with the herd cycle, on the 2025-organic release as built, not on 2025-fixed. The national 100-year worst-year factor, 0.46 of trend, is milder than those of New South Wales (0.30), Victoria (0.22), Queensland (0.35) and South Australia (0.35). It is not milder than those of Western Australia (0.47) or Tasmania (0.67). Spreading production across states therefore lowers national variability. In the long term 94% of the population lives in regions over capacity (2025-fixed; section 7). Settlement policy changes where food must travel, not the national capacity. Aquaculture, seasonal forecasting, household and community stocks, and finance and insurance are further measures the model cannot carry.

**Caution.** The drought, store and livestock results rest on one weather factor applied to every yield.

Table S5. The measures one at a time, Australia, 2025: capacity in millions of people and the change on each release's own reference. Built from `analysis/paper_a/measures.csv` (release named in each row; the grain stores on 2025-fixed use the resilience tables of 2025-store-1 and 2025-store-2). The 156-litre row sets the fuel in both terms, so it moves the short term (+0.1%); the named scenario of Table S2 sets it in the long term only (0%). Both are right for their settings, and in the long term they agree: +0.78% in Table S2 is +0.8% at one decimal.

| Measure | Release | Short term | Long term |
|---|---|---|---|
| Reference | 2025-fixed | 41.5 | 15.6 |
| Field-crop yields +10% | 2025-fixed | 41.5 (+0.1%) | 15.7 (+0.2%) |
| Field-crop yields +20% | 2025-fixed | 41.5 (+0.1%) | 15.7 (+0.3%) |
| Horticulture yields +10% | 2025-fixed | 41.5 (0.0%) | 15.6 (+0.2%) |
| Livestock output +10% | 2025-fixed | 45.5 (+9.7%) | 17.1 (+9.4%) |
| Livestock output +20% | 2025-fixed | 49.6 (+19.4%) | 18.6 (+18.8%) |
| All yields +10% | 2025-fixed | 45.7 (+10.0%) | 17.2 (+10.0%) |
| Drought-proofing: the worst year loses half as much | 2025-fixed | 41.5 (0.0%) | 24.9 (+59.7%) |
| Irrigated share of cropland 0.02 (base 0.007) | 2025-fixed | 41.8 (+0.7%) | 15.7 (+0.7%) |
| Irrigated share of cropland 0.05 (base 0.007) | 2025-fixed | 42.5 (+2.4%) | 16.0 (+2.4%) |
| Avoidable waste 6% | 2025-fixed | 48.3 (+16.4%) | 14.3 (-8.2%) |
| No avoidable waste | 2025-fixed | 55.3 (+33.2%) | 15.6 (0.0%) |
| Full recycling of food waste | 2025-fixed | 42.4 (+2.2%) | 15.6 (0.0%) |
| Cropland +25% from pasture | 2025-fixed | 41.5 (0.0%) | 15.6 (0.0%) |
| Cropland doubled from non-agricultural land | 2025-fixed | 45.1 (+8.7%) | 17.0 (+8.7%) |
| Meat and eggs 7.5% of the diet | 2025-fixed | 48.2 (+16.2%) | 15.6 (0.0%) |
| Meat and eggs 5% of the diet | 2025-fixed | 76.8 (+85.0%) | 19.6 (+25.7%) |
| Red meat 30% of meat | 2025-fixed | 64.6 (+55.6%) | 18.5 (+18.6%) |
| Liquid fuel 156 litres a person | 2025-fixed | 41.5 (+0.1%) | 15.7 (+0.8%) |
| Grain store of one year | 2025-fixed (store table of 2025-store-1) | 41.5 (0.0%) | 23.2 (+48.4%) |
| Grain store of two years | 2025-fixed (store table of 2025-store-2) | 41.5 (0.0%) | 25.7 (+64.5%) |

## S7. Diet and gardens under forced local self-sufficiency (section 12)

On 2025-fixed and the state-yield basis, the sum of SA2 capacities is 37% of the national capacity on the base diet. It is 33% on a 2.5% meat-and-egg diet and 45% with no meat or eggs, each against the national capacity on the same diet. Against the national figure on the base diet, the SA2 sum on the 2.5% diet reaches 95%. Swaps within food groups raise the national capacity by about three fifths (+62%), from 53.6 to 86.9 million, on the improved release (2025-improved). Gardens add little: covering all fruit and vegetable land from gardens would free only about 7% of the cropland a person needs (2025-fixed).
