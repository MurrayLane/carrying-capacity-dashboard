
# B55 merge: B54a and B54b readings into the literature register

Edited only `qa/literature_register.csv` (CRLF and all 12 columns kept; a read-and-rewrite test reproduced the original byte for byte first), `qa/claims_register.csv` (B230 `sources` only) and this file. All eight rows: `read_or_reported` "read"; `status` "self-checked (B54a full text)" for L079, L088, L103, L104 and "self-checked (B54b full text)" for L109, L114, L117, L129. Local paths and sha256 as the reports give them.

## Rows changed (old and new `what_taken`)

**L079**
- Old: Australian food intake scenarios to 2050 set against linear projections of production, by basic food group; population 23 million (2015) to 37.5 million (2050); demand rises faster than local production for most commodities; system moving to lower net exports and more import dependence
- New: Australian intake scenarios to 2050 (reported 2011 intake; Australian Guide to Healthy Eating) against FAOSTAT trend projections of production, by basic food; population about 23 million (2015) to 37.5 million (2050); demand outgrows production for most commodities, so net exports fall and import dependence rises. Repeats 'enough food for some 60 million people' on food energy, export-inclusive (p. 212, citing Department of Agriculture 2014; p. 219). Nutritional Production Sufficiency Index (NPSI) 5.93 (1997-1999 peak) to 4.86 (2050), maximum 6.0 (p. 219); vegetables 62% of demand in 2050, seafood under 20%, dairy net importer from 2036 (reported intake) or 2017 (dietary guide) (p. 216). No table of people covered by food group.

**L088**
- Old: Review of how ecosystem studies since the 1950s apply carrying capacity: a wide range of definitions, K usually the number of individuals the environment can support, unclear whether dynamic; most use in conservation, rangeland and wildlife management, aquaculture and fisheries
- New: Review of 114 ecosystem studies after Odum 1953 (from 1,170 Scopus hits; 161 human-population studies excluded): over 19 definitions of carrying capacity, most often K, the number of individuals in an area; used mostly in conservation biology, fisheries, rangeland and wildlife management and aquaculture; unclear whether static or dynamic; overshoot lowers productivity and biodiversity. Asks studies to state static or variable capacity and use plain ecological terms.

**L103**
- Old: US cropland could meet up to 90% of national food demand locally (upper potential, range of diets)
- New: Share of the US population that existing cropland could feed locally, 1850-2000, three diets (Peters diet model), 40% loss, cropland only. Year 2000: 50-mile radius (the paper's baseline) 85/82/80% (vegetarian/standard/meat-intensive); 100-mile 93/90/88%; 100% at 200 miles. Insensitive to diet and losses (82% to 87% with no loss); sensitive to radius. The abstract's 'as much as 90%' is the 100-mile standard-diet case, not a range over diets.

**L104**
- Old: US foodsheds across 7 diets: 35-53% of people within 250 km on cropland; every diet leaves some land unused
- New: 378 US metros, 3,106 counties, 7 diets, 3 land types (Peters 2016 Foodprint with county productivity); county HNEs called county carrying capacity (eq 2). National average weighted source distance 351-481 km cultivated cropland, 80-492 km perennial, 117-799 km grazing (Table 2; the abstract's 351-428 omits the baseline diet at 481). Within 250 km, 35-53% of the metro population on cultivated cropland, 39-94% perennial, 26-88% grazing (Fig. 5). Land per person a year by diet (Fig. 2): baseline 1.248 ha (0.965 of it grazing), vegan 0.136 ha. Every diet leaves land unused.

**L109**
- Old: Review: region-specific limits on feeding 9 billion; no estimate
- New: Single-author review (not an editorial) of the water, land, soil and energy limits on food production for 9 billion people in 2050. Argues that limits must be set region by region. Proposes an 'agricultural production boundary': an irrigation cap of 1003.82 m3/ha/yr (p. 11) and yield ceilings for rice, wheat, maize and potato (p. 12). No population estimate.

**L114**
- Old: Hesse region: land per person for current and planetary-health diets; region cannot feed its current livestock
- New: Hesse (6.3 million people) and five sub-regions, four scenarios (current; 100% self-sufficiency at current diets; planetary health diet at 2150 kcal; PHD with seven-year rotation and extensive husbandry). Hesse cannot feed its current livestock (p 13). At 100% self-sufficiency on current diets, cropland need exceeds supply by 81% (p 14). On the PHD, 482 m2 of cropland a person is needed against 648 m2 available, 74% (p 15). Pasture need 767 m2 against 467 m2 at current diets, 128 m2 on the PHD (p 14). Fruit, nuts, fish and food waste are excluded. No headcount is stated.

**L117**
- Old: Land use ratio for livestock: hens 2.08, dairy 2.10 sandy and 0.67 peat; below 1 means livestock out-produce crops on that land
- New: Land use ratio (protein): laying hens 2.08, dairy on sandy soil 2.10, dairy on peat 0.67 (p 754). Below 1 means the livestock yield more human-digestible protein than food crops could on the same land. On energy, every case is above 1 (6.39, 1.22, 4.35; Table 8, p 755). Grass-fed beef or milk on land unsuitable for crops gives a LUR of zero (p 756).

**L129**
- Old: Footprint accounts used to predict country prospects; financial and biophysical assessments disagree
- New: 2018 National Footprint and Biocapacity Accounts, 1961-2014. Argues that global-hectare biocapacity accounting is the best available metric of demand against regeneration (section 2.1). Eight countries are in an 'ecological poverty trap' and 23 are candidates. No correlation between biocapacity and GDP per person among low-income countries in 2014 (Fig 6). Australia's footprint is 6.5 global hectares a person (2014 data, p 13), a primary figure. World demand exceeds regeneration by over 70% (p 8).

Other changes: titles of L079 (issue number dropped), L109 ("Wang 2022", single author) and L114 (subtitle "How Many People Can Our Land Feed?"); L129 `used_by` (defence slot is Goldfinger 2014, L086); notes carry the method families (Kurtz and Zumkehr: resource-based land and diet with spatial allocation (foodshed), as Peters 2009; Chapman and Byron: concept review of the ecological lineage only; Ridoutt: commodity balance with no people count of its own) and the new figures (Wackernagel p. 13, 6.5 gha, 2014 data; Ridoutt NPSI 5.93 to 4.86 and group ratios; Kurtz 1.248 ha baseline, 0.965 grazing, vegan 0.136). L103 and L104 corrections applied as briefed (L103: 90% is the 100-mile standard-diet case, baseline 50 miles and 82%, radius-dependent; L104: 351 to 481 km, 35 to 53% of metro population).

## Claims register

B230 `sources` was empty; it now reads `L079 (Ridoutt 2017 p. 212 repeats the 60 million on food energy, export-inclusive, citing Department of Agriculture 2014 (Australian food statistics 2012-13))`. No other cell changed.

## Rows added

L137: Department of Agriculture 2014, "Australian food statistics 2012-13", kind report, status unverified, `read_or_reported` "not read (lead from Ridoutt 2017 and PMSEIC 2010's figure)"; the primary source of the 60 million, to be read before the figure is quoted.

## Notes

- Authors' diacritics (Schön and Böhringer) kept ASCII in the register.
- L079 `used_by` still lists section 5 (comparator); Ridoutt gives no people count of its own, so the coordinator may want to revisit that.

## Final count

137 data rows (136 before, plus L137), 138 lines with the header.
