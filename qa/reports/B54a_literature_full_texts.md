# B54a: four archived papers read in full

I read every page of the four papers with the Read tool, from `/home/user/carrying-capacity-models/Literature review/`. All four are PDFs. Ridoutt has 17 pages: 16 of the article and a copyright notice. Chapman and Byron has 12 pages, Kurtz 13 and Zumkehr and Campbell 6: a JSTOR cover page and pages 244 to 248. I searched `qa/literature_register.csv` and `qa/claims_register.csv` by first author, year, DOI, row id and the quoted figures.

**Rows found:**
* L079: Ridoutt 2017.
* L088: Chapman and Byron 2018.
* L103: Zumkehr and Campbell 2015.
* L104: Kurtz 2020.

`qa/claims_register.csv` has no row that cites any of the four, by row id or by name. Three rows sit near Ridoutt's "60 million" and should be read beside it: B163 and L011 (the National Farmers' Federation figure) and L136 (PMSEIC 2010).

**Outlines:** neither `papers/A_results/OUTLINE.md` nor `papers/B_methods/OUTLINE.md` names any of the four papers.

**Earlier reports that describe them:**
* `qa/reports/B14_literature_sweep.md`
* `qa/reports/B17_reading.md` (Ridoutt and Chapman, from abstracts only)
* `qa/reports/B20_reading.md` (Zumkehr and Kurtz, from abstracts only)
* `analysis/literature_review/README.md` (seed list)

Archive hashes (sha256), for `local_path` and `sha256`:

| Row | File | sha256 |
|---|---|---|
| L079 | `Ridoutt2017_FoodSecurity_Australias_nutritional_food_balance.pdf` (17 pages; page 17 is a copyright notice) | a89fc8e4584d38b738680cf2128017bd37123888cf310bb3adcc2936bbce14a3 |
| L088 | `Chapman_Byron2018_GEC_Flexible_application_of_carrying_capacity_in_ecology.pdf` (12 pages) | aa8f5a30a2c1bbcee413bf7d3aa599daf290e4766e8eb3a16b217ba5e6d168dc |
| L104 | `Kurtz2020_EST_Mapping_US_food_system_localization_potential.pdf` (13 pages) | fa14bcf851ddf879741597be54a8af6e6056710fc584aa95d822e40e7f5e35e3 |
| L103 | `Zumkehr_Campbell2015_FrontEcolEnv_Potential_for_local_croplands_to_meet_US_food_demand.pdf` (6 pages: JSTOR cover and pp. 244-248) | 83573b6c9cdf54cf7f08e57761796ff236120eed11bd387282ec0efbbd2e37ec |

None of the four cites Lane. I read all four reference lists in full, and a text search of each file found no "Lane".

---

## 1. Ridoutt et al. 2017 (L079)

**(1) Citation as printed.** Ridoutt, B., Baird, D., Bastiaans, K., Darnell, R., Hendrie, G., Riley, M., Sanguansri, P., Syrette, J., Noakes, M., Keating, B. 2017. "Australia's nutritional food balance: situation, outlook and policy implications". Food Security 9: 211-226. DOI 10.1007/s12571-017-0650-x (printed on p. 211). Original paper. The dates printed are received 10 February 2016, accepted 3 January 2017 and published online 17 February 2017.
* The PDF does not print an issue number. The register's "9(2)" is not contradicted, but it is not confirmed from the file either.
* The paper is based on RIRDC projects PRJ-008806 and PRJ-009653 (Acknowledgements, p. 221). The underlying reports are on the RIRDC website and may hold the tables the article does not print.

**(2) What it argues.**
* The paper compares Australian food intake scenarios to 2050 with linear trend projections of Australian farm production, for each basic food rather than for food energy or macronutrients.
* It builds two intake scenarios:
  * reported intake, from the 1995 and 2011 national nutrition surveys, scaled up for under-reporting;
  * intake following the Australian Guide to Healthy Eating.
* A food system model converts both scenarios to farm-gate demand. It accounts for cooking and processing, supply chain and kitchen losses, and livestock feed. The population is ABS Series B, from about 23 million in 2015 to 37.5 million in 2050 (pp. 213, 215).
* The finding: for most commodities, demand grows faster than local production. The system is therefore heading towards lower net food exports and more dependence on imports, especially for vegetables, fruit, seafood and dairy (pp. 211, 215-216, 220).
* Australia stays a net exporter of food energy. The authors introduce a Nutritional Production Sufficiency Index (NPSI) to show that the nutritional picture differs from the energy picture (pp. 215, 219).

**(3) Method family.** Commodity balance (catalogue section 4), the same family as Foran and Poldy 2002.
* Demand side: a nutrition-based demand built up by food group, age and sex, with losses and feed added.
* Supply side: production as a trend line from FAOSTAT 1995-2013.
* It is not a capacity estimate. It reports tonnes of production against tonnes of demand, plus a 0-to-6 index. Apart from one cited sentence, it never states how many people the production would feed.

**(4) Register figures attributed to the paper (L079 `what_taken`).**

| Register text | Where in the paper | Verdict |
|---|---|---|
| Australian food intake scenarios to 2050 set against linear projections of production, by basic food group | Abstract p. 211; Methods pp. 213-215 | Confirmed as printed |
| population 23 million (2015) to 37.5 million (2050) | Abstract p. 211; p. 213 ("approximately 37.5 million at June 2050"); p. 215 | Confirmed as printed |
| demand rises faster than local production for most commodities | Abstract p. 211 ("in most respects demand is projected to increase at a greater rate than local production"); p. 215 | Confirmed as printed |
| system moving to lower net exports and more import dependence | Abstract p. 211; Conclusions p. 221 | Confirmed as printed |
| Note: "Author list differs between index records; Crossref lists Ridoutt, Baird, Bastiaans, Darnell and others: confirm" | p. 211 | Resolved: ten authors, listed in (1) |

**The national figures the brief asked for (how many people Australian production covers, by food group and year).** The paper has **no table** of people covered, by food group or in total. It has no table at all: its results are Fig. 1 (16 panels of production and demand in million tonnes, pp. 217-218) and Fig. 2 (the NPSI, p. 219). Every national figure it prints in words or numbers is listed here:

| Food group or measure | Year | Figure as printed | Basis | Page |
|---|---|---|---|---|
| All food (food energy) | "currently" (cites Department of Agriculture 2014, *Australian food statistics 2012-13*) | "Australian agriculture currently produces enough food for some 60 million people, which is more than twice the current local population" | food energy requirements; production including exports | p. 212 |
| All food (food energy) | to 2050 "and well beyond" | "current production is sufficient to meet the food energy requirements of some 60 million people"; population "is not expected to reach even two thirds of this number by 2050" | same | p. 219 |
| All food (domestic share) | "currently" (cites PMSEIC 2010) | "more than 90% of food consumed domestically is currently grown in Australia" | share of consumption | p. 212 |
| All food (people fed, global) | not dated | persons directly fed through Australian agriculture are "< 1% of the global population" | none stated | p. 220 |
| All six groups: NPSI (0 to 6) | 1997-1999 peak; 2050 | 5.93 at peak; projected 4.86 in 2050 (maximum possible 6.0) | domestic production / domestic demand per group, capped at 1, summed | p. 219, Fig. 2 |
| Vegetables | 1995; 2050 | farm-gate demand 2.64 Mt (1995) to 5.98 Mt (2050, reported intake); 7.65 Mt (2050, dietary guide) | demand | p. 215 |
| Vegetables | 2050 | production "around 62% of domestic demand" (reported intake); Australia "presently a net importer" | production / demand | p. 216 |
| Grain | 1995; 2050 | demand 5.39 Mt (1995) to 24.9 Mt (2050), "more than 350% increase"; output varies by up to 15 Mt from the long-term average | demand | p. 216 |
| Grain | mid-1990s; 2050 | average annual trade surplus about 26 Mt (mid-1990s) to about 21 Mt (2050) | surplus | p. 216 |
| Seafood | current; 2050 | production about 0.24 Mt, about 0.29 Mt by 2050; demand 1.44 Mt by 2050; local production "less than 20% of local demand" | production / demand | p. 216 |
| Eggs | n/a | local demand appears to exceed local supply consistently, possibly a data artefact (four explanations given) | qualitative | p. 216 |
| Milk (dairy) | 2002; 2020; 2050; 2036; 2017 | production peak 11.3 Mt (2002); trend 9.6 Mt (2020), 9.2 Mt (2050); industry scenarios 6.2 to 15.4 Mt in 2020; net importer from 2036 (reported intake) or 2017 (dietary guide) | production / demand | p. 216 |
| Meat, nuts and seeds, dried beans peas and pulses, vegetable oil, alcoholic beverages, sugar | to 2050 | "production surpluses are projected to continue"; sugar surplus "projected to decline markedly" | qualitative | p. 216; p. 219 (meat exports rise in absolute terms, fall as a share) |
| Honey | to 2050 | "will become substantially import dependent" unless the trend changes | qualitative | p. 216 |
| Tea, coffee, cocoa | all years | "local production is negligible" | qualitative | pp. 212, 216 |
| Edible seaweed | n/a | consumption growing; "production statistics are unknown" | qualitative | p. 216 |

Only the vegetable and seafood ratios can be turned into people. The products below are my arithmetic, not printed: 62% of a 37.5 million population is about 23 million people covered for vegetables in 2050, and below 20% of 37.5 million is under 7.5 million for seafood. The ratios for the other groups and other years exist only as plotted lines in Fig. 1, which the paper does not tabulate.

**(5) Figures that bear on Australia or a capacity range and that the registers lack.**
* **The 60 million on a food-energy basis, with a government source:** "on the basis of food energy requirements" (p. 212, citing Department of Agriculture 2014). The registers hold 60 million from PMSEIC (L136, unsourced) and from industry (L011, B163, grain). Ridoutt is a peer-reviewed CSIRO paper that repeats the figure and names its basis and source. Its "more than twice the current local population" makes the export-inclusive reading explicit. It belongs with the export-inclusive counts (B230), and it is the second published citation of the Department of Agriculture 2014 source.
* **NPSI 5.93 (1997-1999) falling to 4.86 (2050), p. 219.** An Australian nutritional self-sufficiency measure by food group with nothing in the registers, and a ready comparator for "the six groups are not all covered".
* **Food-group ratios:** vegetables 62% of demand in 2050; seafood under 20%; dairy a net importer from 2036, or 2017 on the dietary guide (p. 216). These figures support the point that the energy count (60 million) hides groups already in deficit.
* **Supporting national inputs:** grain demand 5.39 to 24.9 Mt; grain trade surplus 26 to 21 Mt; the milk peak; under-reporting factors of 16% and 1% (1995) and 21% and 17% (2011) for females and males (p. 214).

**(6) Lane.** Not cited.

**(7) Row updates for the coordinator.**
* **L079:**
  * `read_or_reported`: "read".
  * `local_path`: `carrying-capacity-models/Literature review/Ridoutt2017_FoodSecurity_Australias_nutritional_food_balance.pdf`.
  * `sha256`: as in the table at the top.
  * `title`: keep, but drop "(2)" or mark it "issue not printed on the file".
  * `what_taken`: "Australian intake scenarios to 2050 (reported 2011 intake; Australian Guide to Healthy Eating) against FAOSTAT trend projections of production, by basic food; population about 23 million (2015) to 37.5 million (2050); demand outgrows production for most commodities, so net exports fall and import dependence rises. Repeats 'enough food for some 60 million people' on food energy, export-inclusive (p. 212, citing Department of Agriculture 2014; p. 219). Nutritional Production Sufficiency Index 5.93 (1997-1999 peak) to 4.86 (2050) (p. 219); vegetables 62% of demand in 2050, seafood under 20%, dairy net importer from 2036 (p. 216). No table of people covered by food group."
  * `notes`: "Full text read (16 pp. plus a copyright page). Ten authors, confirmed from p. 211. Lane: No. The only people count is the cited 60 million (food energy, export-inclusive); sits with L136, L011, B163 and B230. Underlying RIRDC reports PRJ-008806 and PRJ-009653 not seen."
  * `status`: the coordinator's usual value for self-checked full texts ("self-checked (B54a full text)").
* **Claims register:** no row cites the paper. If the coordinator wants the 60 million to carry a peer-reviewed second source, add L079 to the `sources` of the export-inclusive row that holds the PMSEIC figure (B230) with the qualifier "food energy, citing Department of Agriculture 2014". Do not add it to B010: Gifford's 60 million is a protein figure and is a different number.

---

## 2. Chapman and Byron 2018 (L088)

**(1) Citation as printed.** Chapman, E.J., Byron, C.J. 2018. "The flexible application of carrying capacity in ecology". Global Ecology and Conservation 13: e00365. DOI 10.1016/j.gecco.2017.e00365 (printed p. 1). Review paper. The dates printed are received 8 June 2017, revised 1 December 2017 and accepted 21 December 2017. Open access, CC BY-NC-ND.

**(2) What it argues.**
* The authors reviewed ecosystem-level studies published after Odum (1953) to see how carrying capacity is defined, what governs it and what happens when it is overshot.
* The sample: a Scopus search for "carrying capacity" and "ecosystem" gave 1,170 papers. They dropped 161 that dealt with the global human population, a lineage they trace to Vogt 1948. That left 822 abstracts, and 114 papers both defined and quantified carrying capacity (p. 3).
* They found more than 19 permutations of the concept, most often as the number of individuals in an area (K). Use falls in conservation biology, fisheries, rangeland and wildlife management, and aquaculture, and runs from molecules to landscapes (pp. 3-5).
* Carrying capacity is distally controlled by energy and proximally by habitat and food. Overshoot lowers productivity and biodiversity and can tip an ecosystem into another state (pp. 7-8).
* The authors argue that uncritical adoption leaves the concept without unifying value. Studies should:
  * state whether capacity is static or variable;
  * use "unpackaged" language;
  * frame the work in general ecological principles (pp. 8-9).

**(3) Method family.** Not a method. It is a concept review and fits section 2, "the concept and its critics". It explicitly excludes human carrying capacity, so it speaks to the ecological lineage only. It is useful beside Sayre 2008 (L046), which it quotes at length.

**(4) Register figures attributed to the paper (L088 `what_taken`; no numbers).**

| Register text | Where in the paper | Verdict |
|---|---|---|
| Review of how ecosystem studies since the 1950s apply carrying capacity | Abstract p. 1; Methods p. 3 (papers after 1953 to 2016) | Confirmed as printed |
| a wide range of definitions | Abstract; p. 3 ("over 19 explicit permutations"); Table 1 p. 4 | Confirmed as printed |
| K usually the number of individuals the environment can support | Abstract ("most often use K"); p. 3 | Confirmed as printed |
| unclear whether dynamic | Abstract; section 4.2 p. 6 | Confirmed as printed |
| most use in conservation, rangeland and wildlife management, aquaculture and fisheries | Abstract; p. 3; Fig. 1b | Confirmed as printed |

**(5) Figures the registers lack.** There is nothing on Australia and no human capacity range. The counts are:
* the sample: 1,170 to 822 to 114 papers, with 161 human-population papers excluded;
* fields: conservation 55% (63 papers), fisheries 48% (55), rangeland and wildlife 42% (48), aquaculture 25% (29);
* scales: population 59% (67), ecosystem 35% (40), cellular 2% (3), community 2% (3), landscape under 1% (1);
* governing factors: 83 of 114 studies discussed what governs capacity, and 41 of those 83 named food, space or available energy.

The paper gives one sentence the methods paper could use: "if carrying capacity is conceived as static, it is theoretically elegant but empirically vacuous; but if it is conceived as variable, it is theoretically incoherent or at best question-begging". It quotes this from Sayre 2008 (p. 3), so cite Sayre for it.

**(6) Lane.** Not cited.

**(7) Row updates for the coordinator.**
* **L088:**
  * `read_or_reported`: "read".
  * `local_path`: `carrying-capacity-models/Literature review/Chapman_Byron2018_GEC_Flexible_application_of_carrying_capacity_in_ecology.pdf`.
  * `sha256`: as above.
  * `what_taken`: "Review of 114 ecosystem studies after Odum 1953 (from 1,170 Scopus hits; 161 human-population studies excluded): over 19 definitions of carrying capacity, most often K, the number of individuals in an area; used mostly in conservation biology, fisheries, rangeland and wildlife management and aquaculture; unclear whether static or dynamic; overshoot lowers productivity and biodiversity. Asks studies to state static or variable capacity and use plain ecological terms."
  * `notes`: replace the retrieval history with "Full text read (12 pp., archive copy). Lane: No. Excludes human carrying capacity by design (p. 3), so it supports section 2 for the ecological lineage only."

---

## 3. Kurtz et al. 2020 (L104)

**(1) Citation as printed.** Kurtz, J.E., Woodbury, P.B., Ahmed, Z.U., Peters, C.J. 2020. "Mapping U.S. Food System Localization Potential: The Impact of Diet on Foodsheds". Environmental Science & Technology 54: 12434-12446. DOI 10.1021/acs.est.9b07582 (printed p. 12434). Published 14 September 2020. The PDF does not print an issue number; the register's "54(19)" is not contradicted.

**(2) What it estimates.**
* The paper models how far the food of each of the 378 US metropolitan statistical areas would have to travel in a closed national system that gives priority to local supply, across seven diets from current consumption to vegan.
* For each of 3,106 counties it computes "Human Nutritional Equivalents" (HNEs: people fed for a year) on three land types: cultivated cropland, perennial forage cropland and grazing land. It uses the Peters 2016 Foodprint model, adjusted by a county productivity index. The paper itself calls HNE_produced "the carrying capacity of each county" (eq 2, p. 12437).
* A linear optimisation then sends each county's surplus to the nearest metros, and the result is reported as weighted average source distance (WASD) (pp. 12436-12439).
* National average WASD is 351-481 km on cultivated cropland, 80-492 km on perennial cropland and 117-799 km on grazing land. Within 250 km, 35-53%, 39-94% and 26-88% of metro populations could be fed from the three land types (pp. 12439-12440).
* Every scenario leaves land unused (p. 12439).

**(3) Method family.** Resource-based land and diet with a spatial allocation (the Peters foodshed lineage). B17 used the same label for Peters 2009. B20 filed it as "land per diet", but the catalogue keeps that family for HALF-type indices (see the final list). Its diet and land-type split also makes it a diet-assumption case for section 6.

**(4) Register figures attributed to the paper (L104 `what_taken`).**

| Register text | Where in the paper | Verdict |
|---|---|---|
| US foodsheds across 7 diets | Abstract; Table 1 p. 12437 | Confirmed as printed |
| 35-53% of people within 250 km on cropland | Abstract; p. 12440 text; Fig. 5 p. 12441 | Confirmed with a difference: the share is of the **aggregate metro (MSA) population**, not all people, and is for **cultivated cropland** (perennial forage cropland is a separate 39-94%) |
| every diet leaves some land unused | Abstract ("All seven scenarios leave some land unused"); p. 12439 takeaway 3 | Confirmed as printed |

Figures B20 reported from the abstract:
* "Foodshed distance 351-428 km for cultivated cropland" is in the abstract. Table 2 (p. 12439) and the results text give **351-481 km**, because the US baseline diet is 481 km. The abstract's upper end is the positive-control diet (428 km). Confirmed with a difference.
* 80-492 km on perennial cropland and 117-799 km on grazing land: confirmed (Table 2; p. 12439).

**(5) Figures the registers lack.** None are on Australia. On capacity:
* **Per-person land by diet (Fig. 2, p. 12438), cultivated + perennial + grazing, hectares a person a year:**
  * baseline 0.175 + 0.108 + 0.965 (total 1.248);
  * positive control 0.152 + 0.103 + 0.990;
  * 80% omnivore 0.142 + 0.077 + 0.657;
  * 50% omnivore 0.129 + 0.054 + 0.376;
  * 20% omnivore 0.123 + 0.031 + 0.097;
  * ovolacto vegetarian 0.120 + 0.021;
  * vegan 0.136.

  Grazing is 77% of the baseline footprint. This bears directly on the grazing design choice (outline section 6). Set it beside B202, which holds Peters 2016 at 1.08 ha on national average yields; Kurtz is county-weighted.
* **Diets (Table 1, p. 12437):** baseline 2,844 kcal a day; the other six about 2,150 kcal.
* **County self-sufficiency (p. 12439):** 1,571 of 3,106 counties meet their own cultivated-cropland needs on the baseline diet, and 1,713 on ovolacto. These counties hold only 17.6% and 21.7% of the population. This is a published US parallel for the scale curve, where small units with few people are self-sufficient and the populous ones are not.
* **Within 100 miles (161 km) (p. 12442):** only 26% (baseline) and 41% (ovolacto) of metro populations could be fed.
* **The 20% omnivorous diet** needs a tenth of the baseline's grazing land (p. 12442).
* **Fruit, vegetables and nuts** take 5-18% of cultivated cropland (p. 12443).
* **Peters 2016 (cited p. 12435):** US land could feed 1.3 to 2.6 times the US population, depending on diet. This is consistent with B202 and L015.

**(6) Lane.** Not cited. It cites Peters 2007 and 2016 under "carrying capacity" titles.

**(7) Row updates for the coordinator.**
* **L104:**
  * `read_or_reported`: "read".
  * `local_path`: `carrying-capacity-models/Literature review/Kurtz2020_EST_Mapping_US_food_system_localization_potential.pdf`.
  * `sha256`: as above.
  * `what_taken`: "378 US metros, 3,106 counties, 7 diets, 3 land types (Peters 2016 Foodprint with county productivity); county HNEs called county carrying capacity (eq 2). National average WASD 351-481 km cultivated, 80-492 perennial, 117-799 grazing (Table 2; the abstract's 351-428 omits the baseline diet). Within 250 km, 35-53% of metro population on cultivated cropland, 39-94% perennial, 26-88% grazing (Fig. 5). Land per person 1.248 ha baseline (0.965 grazing) to 0.136 vegan (Fig. 2). Every diet leaves land unused."
  * `notes`: "Full text read (archive copy, 13 pp.). Lane: No. Method family: resource-based land and diet with spatial allocation (foodshed). Its comparison with Zumkehr and Campbell (p. 12442) is consistent with that paper."
* **Claims register:** no row cites the paper. If the paper's grazing paragraph quotes the footprints, add L104 to its `sources`.

---

## 4. Zumkehr and Campbell 2015 (L103)

**(1) Citation as printed.** Zumkehr, A., Campbell, J.E. 2015. "The potential for local croplands to meet US food demand". Frontiers in Ecology and the Environment 13(5): 244-248. DOI 10.1890/140246 (printed p. 244). Research Communications. The file is the JSTOR copy (stable URL 24891187).

**(2) What it estimates.**
* The paper defines "foodshed potential": the share of the population that could be fed if all existing US cropland were given over to local food.
* It simulates foodshed potential for 1850 to 2000 using the Peters 2007/2009 diet model with three diets: vegetarian, standard, and meat-intensive (381 g meat a day).
* Other inputs: a 40% farm-to-table loss, corn silage and hay yields as productivity proxies, and an allocation of grid cells to cities within a maximum radius (pp. 244-246).
* Nearly everyone could be fed locally up to 1900. In 2000 the share was:

  | Radius | Vegetarian | Standard | Meat-intensive |
  |---|---|---|---|
  | 50 miles | 85% | 82% | 80% |
  | 100 miles | 93% | 90% | 88% |

  At 200 miles the share reaches 100% (p. 246).
* Large coastal cities fall far short: New York and Los Angeles reach about 10% at 50 miles. The national figure is insensitive to diet, losses and yield, and very sensitive to radius (pp. 246-247).
* The authors conclude that the barriers are social and economic rather than agronomic (p. 248).

**(3) Method family.** Resource-based land and diet with a spatial allocation (the Peters foodshed lineage). It counts cropland only: pasture is excluded, and the authors expect including it to raise the national figure only modestly (p. 246).

**(4) Register figure attributed to the paper (L103 `what_taken`).**

| Register text | Where in the paper | Verdict |
|---|---|---|
| US cropland could meet up to 90% of national food demand locally (upper potential, range of diets) | Abstract p. 244 ("as much as 90% of the national food demand"); Results p. 246 | Confirmed with a difference. The 90% is one case: the **100-mile** radius, **standard diet**, **year 2000**, expressed as the share of the population fed. The paper's own **baseline is the 50-mile radius, 82%** (pp. 246-247); vegetarian at 100 miles is 93%, and 100% is reached at 200 miles. "Upper potential" is the paper's framing (p. 244). "Range of diets" is three diets. |

**(5) Figures the registers lack.** None are on Australia.
* The national result moves with radius, not diet: 82% rises to only 87% with no food loss, and switching to a vegetarian diet changes it about as little (p. 247).
* New York State: 31% by this method, against 34% in Peters 2009 (L077) (p. 247).
* Seattle: 32% at 50 miles and 100% at 100 miles. San Diego: 30% on the meat-intensive diet and 50% on vegetarian (pp. 246-247).
* Together these give a published scale parallel: the share fed falls as the unit shrinks and rises with radius, with diminishing returns (Fig. 3).

**(6) Lane.** Not cited. It cites Peters et al. 2007 under its "agricultural carrying capacity" title.

**(7) Row updates for the coordinator.**
* **L103:**
  * `read_or_reported`: "read".
  * `local_path`: `carrying-capacity-models/Literature review/Zumkehr_Campbell2015_FrontEcolEnv_Potential_for_local_croplands_to_meet_US_food_demand.pdf`.
  * `sha256`: as above.
  * `what_taken`: "Share of the US population that existing cropland could feed locally, 1850-2000, three diets (Peters diet model), 40% loss, cropland only. Year 2000: 50-mile radius (baseline) 85/82/80% (vegetarian/standard/meat-intensive); 100-mile 93/90/88%; 100% at 200 miles. Insensitive to diet and losses (82% to 87% with no loss); sensitive to radius. The abstract's 'as much as 90%' is the 100-mile standard-diet case."
  * `notes`: replace the retrieval history with "Full text read (JSTOR archive copy, pp. 244-248). Lane: No. Method family: resource-based land and diet with spatial allocation (foodshed)."

---

## Characterisations in our outlines and earlier reports that the texts do not support

1. **`qa/reports/B14_literature_sweep.md` line 37: Ridoutt 2017 as "a direct Australian test of how many people the supply covers".**
   * Not supported. The paper compares tonnes of production with tonnes of demand by food group and reports an index (NPSI). It gives no people count of its own.
   * Its one people figure, "some 60 million", is on food energy, includes exports, and is cited to Department of Agriculture 2014 (pp. 212, 219).
   * The B54 brief's request for "the table" of people covered by food group and year rests on the same expectation. The paper has no such table, and no table at all.

2. **`qa/reports/B20_reading.md` (L103): Zumkehr and Campbell's 90% as "the stated upper potential", whose "size depends on the diet and waste assumed".**
   * Two problems. First, the 90% is the 100-mile radius case; the paper's own baseline is 50 miles and 82%.
   * Second, the paper says the national figure is *not* highly sensitive to diet or waste (82% to 87% with no loss; small change with a vegetarian diet, p. 247). It is the radius that moves it (Fig. 3).
   * The comparator should be described as radius-dependent.

3. **`qa/reports/B20_reading.md` (L104): Kurtz foodshed distance "351-428 km for cultivated cropland".**
   * This is the abstract's figure. The paper's Table 2 and results text give 351-481 km. The baseline diet, the one that matters for a current-diet comparison, is 481 km.

4. **`qa/reports/B20_reading.md`: Zumkehr and Kurtz filed under the method family "land per diet".**
   * In the methods outline's catalogue (section 4), "land per diet indices" means the HALF-type index (Alexander 2016). These two papers are spatial allocations of a complete-diet land requirement: the resource-based land and diet family with a foodshed allocation, as B17 labelled Peters 2009.
   * This is a classification point, not a factual error. The coordinator should pick one label for the Peters foodshed lineage.

5. **`qa/reports/B14_literature_sweep.md` line 43 and `analysis/literature_review/README.md`: Chapman and Byron as "the recent ecology review of the carrying capacity concept itself, for the opening argument".**
   * Supported only in part. The review deliberately excludes the 161 human-population carrying-capacity studies (p. 3), so it cannot be cited on how human carrying capacity is defined or criticised.
   * It can support only the point that the ecological concept is used in many inconsistent ways. Its sharpest line on static against variable capacity is Sayre's (L046).

6. **The L079 register note ("Author list differs between index records ... confirm") and the B17 caution ("weakest basis").** Both are settled by the full text: ten authors, listed in section 1 (1). The abstract-level description in B17 (scenarios, population, demand outpacing production, import dependence) is supported as written.

The outlines (`papers/A_results/OUTLINE.md`, `papers/B_methods/OUTLINE.md`) do not mention these four papers, so the outlines make no claim about them for the texts to contradict.
