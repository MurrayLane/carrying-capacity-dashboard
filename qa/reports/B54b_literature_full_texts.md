# B54b: literature full texts (Schon and Bohringer 2023, Wackernagel et al. 2019, Wang 2022, van Zanten et al. 2016)

Brief: `qa/briefs/B54_literature_full_texts_2.md`, part B54b, with the seven items of `qa/briefs/B50_literature_full_texts.md`. Checked 2026-11-09. Registers were not edited; the row updates are listed for the coordinator. No network, no git, no subagents.

All four PDFs were read in full with the Read tool. A text search of each (pdftotext) for "Lane", "Australia" and "carrying capacity" was run as a second check.

Files (all in `carrying-capacity-models/Literature review/`):

| File | PDF pages read (Read tool ranges) | Journal pages | sha256 |
|---|---|---|---|
| `Schon_Bohringer2023_Sustainability_Land_consumption_for_current_diets.pdf` | 1-35 (1-10, 11-20, 21-30, 31-35) | 1-35 of 35 | 1a2f5b5487fc4c9072f3f949b4b9d2bd6201ef04155207e4c8e618c8ca5b9490 |
| `Wackernagel2019_Sustainability_Defying_the_footprint_oracle.pdf` | 1-22 (1-10, 11-22) | 1-21 of 21, plus a ProQuest licence page | 3dfe176767f1b3686a42af5e8436f8c732c6a759f759a0978f21f59aa4246a68 |
| `Wang2022_Land_Managing_land_carrying_capacity.pdf` | 1-22 (1-10, 11-20, 21-22) | 1-21 of 21, plus a "reproduced with permission" page | 79219ab5a0c6c14b9ff74dfa99a8ea3b05753e65778b975b3388fb13e643d497 |
| `vanZanten2016_IJLCA_Global_food_supply_livestock_land_use_FIRST_PAGE_ONLY.pdf` | 1-13 (1-10, 11-13) | 747-758 (all twelve), plus a "reproduced with permission" page | ce81048aac5edb42f454fd6fae7d1099e71b239fef7396c16c1797b2570d5346 |

**Deviation from the rule:** the second Wackernagel range was 11-22, twelve pages, not at most 10. All twelve pages rendered and were read; nothing was skipped.

**Two premises of the brief do not hold for these files:**

* **van Zanten is not first page only.** The file holds the whole article: twelve journal pages (747-758) plus a permission page, 13 PDF pages. Only the file name says "FIRST_PAGE_ONLY". I report on the full text below. The brief asked me to mark the row as still abstract only; the evidence supports "read", so I recommend that and leave the choice to the coordinator.
* **Wang is not six pages.** It runs to 21 journal pages (22 PDF pages). The `file` utility reports 10, 6 and 1 pages for the Schon, Wang and van Zanten files; pdfinfo and the Read tool both give 35, 22 and 13. The `file` count is probably where "six pages" and "first page only" came from.

**Register rows found:**

* Literature register: L114 (Schon and Bohringer), L129 (Wackernagel et al. 2019), L109 (Wang), L117 (van Zanten).
* Claims register: **no row** cites any of the four. I searched by L id, by author and by the quoted figures (2.08, 2.10, 0.67, Hesse, 9 billion, global hectares).
* Outlines: none of `papers/B_methods/OUTLINE.md`, `papers/B_methods/SECTION7_DRAFT.md`, `papers/A_results/OUTLINE.md` or `papers/A_results/DISCUSSION_MEASURES.md` names any of the four.
* Elsewhere: their characterisations sit in the literature register and in reports B14 (sweep csv and md), B20 and B48, plus a seed-list line for van Zanten in `analysis/literature_review/README.md`.

---

## 1. Schon and Bohringer 2023, L114

**(1) Citation as printed.** Anna-Mara Schön and Marita Böhringer, "Land Consumption for Current Diets Compared with That for the Planetary Health Diet: How Many People Can Our Land Feed?"

* Journal: *Sustainability* 2023, 15, 8675.
* DOI: 10.3390/su15118675.
* Affiliation: Department of Business, Fulda University of Applied Sciences.
* Dates: received 31 March 2023; revised 11 May 2023; accepted 23 May 2023; published 26 May 2023.
* Licence: open access, CC BY.

**The printed subtitle differs from the register.** The title page, the citation box and the PDF metadata all print "How Many People Can Our Land Feed?". The register (L114) has "How Much Land Does a Region Need?" and says that is Crossref's subtitle. B14's sweep csv had the printed form.

**(2) What it argues.**

* The paper builds a framework that works out land use in square metres per person for different diets. It applies the framework to the German state of Hesse (6,295,017 people, Fig 2) and to five sub-regions, with the emphasis on livestock.
* It runs four scenarios (pp 4, 8):
  * *current*: current consumption and current livestock;
  * *SSD 100%*: the livestock needed for 100% self-sufficiency at current consumption;
  * *PHD*: the planetary health diet scaled to 2150 kcal a day;
  * *extensive*: the PHD with a seven-year crop rotation and extensive husbandry.
* Findings:
  * Hesse cannot feed its current livestock, nor the livestock that self-sufficiency at current diets would need, from its own land (p 13).
  * On the PHD, the cropland needed is 74% of the existing cropland: 482 m² a person needed against 648 m² available (p 15).
  * In the extensive scenario, most regions could feed themselves a plant-based diet plus extensively kept livestock (pp 16-19).
* The authors conclude that a local diet within planetary boundaries is possible only if consumption of animal products falls sharply and farming practice changes as well (pp 19, 23).
* Despite its title, the paper never states how many people the land could feed. It reports self-sufficiency percentages, square metres per person, and how many people one animal can supply (Fig 8).

**(3) Method family.** Land per diet. It is a regional self-sufficiency and feed-balance calculation from state statistics: yields, cropland and pasture, herd factors and fodder rations. The fodder rations come from the literature and expert interviews.

The paper excludes:

* fruit, nuts and fish (p 7; discussion p 21);
* food waste (p 8);
* energy crops, which are subtracted (Table A7).

**(4) Register figures (L114 `what_taken`).**

| Figure in L114 | Where in the paper | Verdict |
|---|---|---|
| Hesse region: land per person for current and planetary-health diets | Section 3.7, pp 14-15; Fig 6 p 15; section 3.8 pp 16-17; Fig 7 p 17 | Confirmed. The figures are in m² per capita. Examples: pasture 767 m² needed against 467 available at current diets (p 14); cropland 482 needed against 648 available on the PHD (p 15). |
| region cannot feed its current livestock | p 13 ("the local land cannot feed the currently kept livestock nor the livestock necessary to achieve a 100% SSD"); abstract p 1 | Confirmed as printed |

**(5) Figures bearing on Australia or a capacity range that the registers lack.**

* No Australian figure. No mention of Australia.
* **Region 1 (all of Hesse), stated:**
  * agricultural land is 764,705 ha, of which 61% is cropland and 38% pasture (p 9);
  * the PHD needs 74% of existing cropland (p 15);
  * at SSD 100% on current diets, Hesse "exceeds its cropland resources by 81%" (p 14);
  * the plant-based share of the PHD needs 358 m² of cropland a person (p 16);
  * the diet is set at 2150 kcal a day, 86% of the PHD's 2500 kcal (p 4, Table 1).
* **Derived here, not stated by the authors** (the headcount the title asks for, cropland only, with the exclusions above):
  * 6.30 million × 648/482 ≈ 8.5 million on the PHD;
  * 6.30 million / 1.81 ≈ 3.5 million at current diets with 100% self-sufficiency in animal products.
  * If used at all, these should go in as a derived reading, like B223.
* **A per-person benchmark the authors quote:** "each of us has only 2000 m² of cropland for our total consumption" (p 15, citing the 2000m2.eu Global Field project).
* **Relevance to our design choices:**
  * the diet scaling to a population median energy need (2150 kcal) bears on the diet assumption (section 6);
  * the finding that pasture sits underused under the PHD (14% to 65% of pasture needed, p 11) bears on the grazing assumption.
* The reference list includes Cassidy et al. 2013 (ref 37, our L016), Willett et al. 2019 (ref 13), Clark and Tilman 2017 (ref 30) and Poore and Nemecek 2018 (ref 97).

**(6) Lane.** Not cited (reference list pp 31-35 read; text search found no "Lane").

**(7) Row updates for L114.**

* `title`: correct the subtitle to "How Many People Can Our Land Feed?" and give the authors with diacritics (Schön and Böhringer).
* `local_path`: `carrying-capacity-models/Literature review/Schon_Bohringer2023_Sustainability_Land_consumption_for_current_diets.pdf`
* `sha256`: as above.
* `read_or_reported`: read.
* `what_taken`: "Hesse (6.3 million people) and five sub-regions, four scenarios (current; 100% self-sufficiency at current diets; planetary health diet at 2150 kcal; PHD with seven-year rotation and extensive husbandry). Hesse cannot feed its current livestock (p 13). At 100% self-sufficiency on current diets, cropland need exceeds supply by 81% (p 14). On the PHD, 482 m² of cropland a person is needed against 648 m² available, 74% (p 15). Pasture need 767 m² against 467 m² at current diets, 128 m² on the PHD (p 14). Fruit, nuts, fish and food waste are excluded. No headcount is stated."
* `notes`: "Full text read (B54b). The B14 csv calls it a country study; it is a German state and five sub-regions. Lane: not cited."

---

## 2. Wackernagel et al. 2019, L129

**(1) Citation as printed.** Mathis Wackernagel, David Lin, Mikel Evans, Laurel Hanscom and Peter Raven, "Defying the Footprint Oracle: Implications of Country Resource Trends".

* Journal: *Sustainability* 2019, 11, 2164.
* DOI: 10.3390/su11072164.
* Dates: received 1 February 2019; accepted 4 April 2019; published 11 April 2019.
* Affiliations: Global Footprint Network (the first four authors) and Missouri Botanical Garden (Raven).
* Licence: CC BY.

**(2) What it argues.**

* The paper argues that national competitiveness and development assessments ignore resource security, and that biocapacity is the most limiting physical factor for economies (pp 2-4).
* It compares candidate metrics and argues that global-hectare biocapacity accounting comes closest to comparing demand with regeneration (section 2.1, pp 4-7). The metrics it sets aside are mass flows, CO2, money, energy, net primary production and plain hectares.
* Using the 2018 National Footprint and Biocapacity Accounts (1961-2014), it identifies:
  * eight low-income countries in an "ecological poverty trap" (Fig 4, Table 1);
  * 23 candidates for it (Fig 5).
* It then shows the "paradox": among low-income countries, biocapacity per person is not correlated with GDP per person in 2014, and the correlation is "weak and slightly negative" (Fig 6, p 14). The authors explain this as prices failing to reflect natural capital (pp 15-17).
* It closes on four levers: cities, energy, food and population (pp 17-18).

**(3) Method family.** Footprint: the National Footprint Accounts used as an indicator of national resource security, with time series and a correlation with income. The paper estimates no capacity.

**(4) Register figures (L129 `what_taken`).**

| Figure in L129 | Where in the paper | Verdict |
|---|---|---|
| Footprint accounts used to predict country prospects | Abstract p 1; section 3 p 10 (the "oracle" part); p 13 ("the oracle reads") | Confirmed as printed |
| financial and biophysical assessments disagree | Abstract p 1; section 4, pp 13-14, Fig 6 | Confirmed as printed |

**(5) Figures bearing on Australia or a capacity range that the registers lack.**

* **Australia:** "Australia has one of 6.5 gha per person, significantly higher than what is available, per person, in the identified African and central American countries" (p 13).
  * This is the 2014 footprint per person from the 2018 edition.
  * The registers carry Australia's footprint only as about 7.3 gha for 2022 from secondary pages (L026, used in B223).
  * This primary 6.5 for 2014 is a dated point the comparators could cite. The paper gives no Australian biocapacity, so no ratio count can be derived from it.
* **Other per-person footprints on p 13:** EU-28 4.7 gha; Canada and the US "over 8".
* **World:**
  * "human demand now exceeds what the planet's ecosystems can renew by over 70 percent" (p 8, citing Lin et al. 2018, our L025);
  * "food production uses over half of our planet's biocapacity" (p 17).
* **Points for the methods paper's footprint section:**
  * The accounts "tend to undercount demand", while biocapacity "may be overstated" because erosion, groundwater depletion and similar losses are not factored in (p 8).
  * Footprints in the paper are consumption footprints, that is, production plus net imports (p 7).

**(6) Lane.** Not cited (references pp 18-21 read; text search found no "Lane").

**(7) Row updates for L129.**

* `local_path`: `carrying-capacity-models/Literature review/Wackernagel2019_Sustainability_Defying_the_footprint_oracle.pdf`
* `sha256`: as above.
* `read_or_reported`: read.
* `what_taken`: "2018 National Footprint and Biocapacity Accounts, 1961-2014. Argues that global-hectare biocapacity accounting is the best available metric of demand against regeneration (section 2.1). Eight countries are in an 'ecological poverty trap' and 23 are candidates. There is no correlation between biocapacity and GDP per person among low-income countries in 2014 (Fig 6). Australia's footprint is 6.5 gha a person (2014, p 13). World demand exceeds regeneration by over 70% (p 8)."
* `notes`: "Full text read (B54b). Not a reply to Giampietro and Saltelli or Blomqvist: it cites neither and refers criticisms to Wackernagel et al. 2018, 'Ecological Footprint Accounts: Criticisms and Applications' (ref 43). Lane: not cited."
* `used_by`: the section 4 slot "footprint family, the defence" should rest on Goldfinger et al. 2014 (L086), with this paper as a statement of the accounts' rationale and an example of their use.

---

## 3. Wang 2022, L109

**(1) Citation as printed.** Xiukang Wang, "Managing Land Carrying Capacity: Key to Achieving Sustainable Production Systems for Food Security".

* Journal: *Land* 2022, 11, 484.
* DOI: 10.3390/land11040484.
* Affiliation: College of Life Sciences, Yan'an University.
* Dates: received 27 February 2022; accepted 25 March 2022; published 27 March 2022.
* Academic editors: Bruce A. McCarl, Chengcheng Fei and Jianhong Mu.
* Licence: CC BY.

**There is one author, not "Wang et al."**

**Is it an editorial? No.**

* The article type printed on p 1 is "Review".
* It has a received and accepted history and named academic editors.
* It runs 21 pages with 121 references and a funding statement (National Natural Science Foundation of China 52169014; Shaanxi 2022NY-192).
* It includes a small compilation of yield data of the author's own (Fig 3).

**(2) What it argues.**

* The paper reviews the resources that limit food production: water, arable land, soil quality and energy, together with fertiliser (sections 2-3).
* It argues that the aim should be "input under and reasonable output under the ultimate environmental bearing capacity" rather than maximum output (p 2).
* It claims to "present the agricultural production boundary theory for the first time" (p 3). The boundary amounts to:
  * an irrigation ceiling of 1003.82 m³ per ha per year (p 11);
  * yield ceilings for rice, wheat, maize and potato, drawn from 1516 yield records (p 12, Fig 3).
* It argues that measures must be region-specific and that food trade faces shocks such as pandemic and war (abstract, sections 4-5).
* It gives no population carrying capacity.

**(3) Method family.** Concept review, with a small empirical yield compilation. It belongs to the Chinese "bearing capacity" vocabulary (environmental carrying capacity as a limit on inputs), not to any capacity-estimation family.

**(4) Register figures (L109 `what_taken`).**

| Figure in L109 | Where in the paper | Verdict |
|---|---|---|
| Review: region-specific limits on feeding 9 billion | Abstract p 1; p 4 ("look at regional/local details"); p 10 ("global boundaries must be spatially narrowed"); conclusions p 16 | Confirmed as printed |
| no estimate | Whole text | Confirmed with a difference. There is no population estimate, but the paper does state numerical limits: the irrigation cap of 1003.82 m³/ha/yr (p 11), and yield ceilings of rice 6920.41, wheat 4345.05, maize 5348.43 and potato 38,928.5 kg/ha (p 12). |

**(5) Figures bearing on Australia or a capacity range that the registers lack.**

* No Australian figure. No mention of Australia.
* **A carrying-capacity range quoted second-hand:** "The potential limits of water on the carrying capacity of earth and reported calculations of 4 billion up to 157 billion" (p 4).
  * The paper attributes it to ref 34, Zisopoulou and Panagoulia 2021, *Water* 13: 1693.
  * The range is not checked here and should not be cited from Wang.
  * Wang also lists Cohen 1995, "How Many People Can the Earth Support?" (ref 79, printed as *Sciences* 35: 18-23), but uses it for a water point, not for a population figure.
* **Global land figures:**
  * about 3 billion of the world's 13.4 billion hectares are suitable for crops, about half of them cultivated (1.4 billion ha in 2008) (p 12, citing refs 93 and 96);
  * cropland share of land area rose from 10.32% in 1961 to 11.97% in 2017, with 12.72% projected for 2050 and 13.73% for 2100 (p 13);
  * per-person agricultural land is about 0.7 ha (p 10);
  * food production must rise 70% by 2050 (p 1).
* Some units are printed oddly: "4900 km−3 year−1" on p 11, and "552.1 m3 ha−1 year−1" on p 10 where the input was per capita. Nothing should be taken from these lines without checking the source.

**(6) Lane.** Not cited (references pp 16-21 read; text search found no "Lane").

**(7) Row updates for L109.**

* `title`: "Wang 2022" (single author: Xiukang Wang); article type Review.
* `local_path`: `carrying-capacity-models/Literature review/Wang2022_Land_Managing_land_carrying_capacity.pdf`
* `sha256`: as above.
* `read_or_reported`: read.
* `what_taken`: "Single-author review (not an editorial) of the water, land, soil and energy limits on food production for 9 billion people in 2050. Argues that limits must be set region by region. Proposes an 'agricultural production boundary': an irrigation cap of 1003.82 m³/ha/yr (p 11) and yield ceilings for rice, wheat, maize and potato (p 12). No population estimate."
* `notes`: "Full text read (B54b), 21 pages. The '4 to 157 billion' water-based range on p 4 is second-hand (ref 34) and not to be cited from this paper. Lane: not cited."

---

## 4. van Zanten et al. 2016, L117

**(1) Citation as printed.** Hannah H. E. van Zanten, Herman Mollenhorst, Cindy W. Klootwijk, Corina E. van Middelaar and Imke J. M. de Boer, "Global food supply: land use efficiency of livestock systems".

* Journal: *Int J Life Cycle Assess* (2016) 21: 747-758.
* DOI: 10.1007/s11367-015-0944-1.
* Affiliations: Animal Production Systems group, Wageningen University; Wageningen UR Livestock Research.
* Dates: received 29 January 2015; accepted 21 July 2015; published online 12 August 2015.
* Licence: open access, CC BY.

**(2) What it argues.**

* The paper proposes a land use ratio (LUR), set out on p 749:
  * the numerator is the most human-digestible protein (HDP) that food crops could yield on all the land used to grow the feed for 1 kg of animal-source food;
  * the denominator is the HDP in that 1 kg;
  * crop suitability on each feed-growing area comes from GAEZ (pp 751-752).
* The ratio adds something the existing measures lack: the opportunity cost of land for growing crops. Those measures are feed conversion, protein and energy conversion ratios, and LCA land occupation (pp 748-749).
* Three Dutch case systems (p 754):
  * laying hens: LUR 2.08;
  * dairy cows on sandy soils: 2.10;
  * dairy cows on peat soils: 0.67, because peat cannot grow food crops.
* The authors conclude that livestock with a LUR below 1 add to food supply. Such systems use land with low opportunity cost or by-products. Food supply is better served by aiming for LUR below 1 together with "a more modest consumption of animal-source food in affluent countries" (p 756).

**(3) Method family.** Land per diet, applied to livestock: an LCA-based land-efficiency metric for one product. It does not estimate a capacity, but it bears directly on how pasture that cannot grow crops is counted.

**(4) Register figures (L117 `what_taken`).**

| Figure in L117 | Where in the paper | Verdict |
|---|---|---|
| Land use ratio for livestock: hens 2.08 | Abstract p 747; p 754 (0.27/0.13 = 2.08) | Confirmed as printed |
| dairy 2.10 sandy | Abstract p 747; p 754 | Confirmed as printed |
| 0.67 peat | Abstract p 747; p 754 | Confirmed as printed |
| below 1 means livestock out-produce crops on that land | Abstract p 747 ("animals produce more HDP per square metre than crops"); p 754 | Confirmed as printed. It holds for protein only. On an energy basis, every case is above 1: hens 6.39, dairy on peat 1.22, dairy on sand 4.35 (Table 8, p 755). |
| 2016 (online 2015), IJLCA 21(5): 747-758 | Running head p 747; "Published online: 12 August 2015" | Confirmed. The issue number (5) is not printed on the pages. |

**(5) Figures bearing on Australia or a capacity range that the registers lack.**

* **Australia:** Table 6 (p 752) gives FAOSTAT 2011 country-average yields for Australia: maize 5739, sweet potato 24,546, white potato 35,089, wet rice 9544, soybean 1714 and wheat 2030 kg/ha. These are second-hand FAOSTAT values for one year, so they are of little use beyond a cross-check.
* The paper cites Ridoutt, Page, Opie, Huang and Bellotti 2012 on carbon, water and land-use footprints for beef cattle in southern Australia (LCA Food 2012). That is a lead for the grazing design choice and links to the Ridoutt line in B54a.
* **The LUR on energy** (Table 8): 6.39, 1.22 and 4.35. The registers carry only the protein values.
* **The statement that beef or milk from grass on peat "would even result in a LUR of zero"** (p 756). This is the paper's clearest support for counting non-arable grazing as adding to food supply, not competing with it.
* "The current livestock sector already uses about 70% of global agricultural land (FAO 2009)" (p 747).

**(6) Lane.** Not cited (references pp 757-758 read; text search found no "Lane").

**(7) Row updates for L117.**

* `read_or_reported`: read. The brief asked for "abstract only", but the file is the complete article (13 PDF pages: pp 747-758 plus a permission page). If the coordinator keeps "abstract only" because of the brief, the note should say the full text is on file.
* `local_path`: `carrying-capacity-models/Literature review/vanZanten2016_IJLCA_Global_food_supply_livestock_land_use_FIRST_PAGE_ONLY.pdf`. The file name is misleading and is worth renaming in the models repository.
* `sha256`: as above.
* `what_taken`: "Land use ratio (protein): laying hens 2.08, dairy on sandy soil 2.10, dairy on peat 0.67 (p 754). Below 1 means the livestock yield more human-digestible protein than food crops could on the same land. On energy, every case is above 1 (6.39, 1.22, 4.35; Table 8). Grass-fed beef or milk on land unsuitable for crops gives a LUR of zero (p 756)."
* `notes`: "Full text read (B54b). Three Dutch case systems; crop suitability from GAEZ; Table 6 lists Australian FAOSTAT 2011 yields. Lane: not cited."

---

## Characterisations the texts do not support

1. **L114 title.** The register's subtitle "How Much Land Does a Region Need?" is not the printed one. The article prints "How Many People Can Our Land Feed?" (p 1, citation box, PDF metadata).
2. **B14 sweep csv, Schon and Bohringer:** "Land-based capacity of a country". The study is of a German state (Hesse) and five sub-regions, not a country. The authors suggest the per-capita figures generalise to "a wide range of European regions" (p 3).
3. **L114 and B20 on Schon and Bohringer as "the same shape as the paper's diet side".** This holds for land per person by diet. But unlike our model, the paper never converts to a population count, and it leaves out fruit, nuts, fish and food waste. A comparison should say both.
4. **L109, B14 and B48: "Wang et al. 2022".** The paper has one author, Xiukang Wang.
5. **L109: "no estimate".** No population estimate, correct. But the paper does state numerical caps: on irrigation (p 11) and on yields (p 12).
6. **B14 csv and B14 md item 9: Wackernagel et al. 2019 as "a response to critics" and "the other side" of the Giampietro and Saltelli and Blomqvist critique.** L129 places it under "footprint family, the defence". The paper cites neither critique and answers no criticism. It defends the global-hectare metric against other metrics (section 2.1) and refers criticisms to another work (ref 43). The reply to the critique is Goldfinger et al. 2014 (L086).
7. **L117 and the brief: van Zanten "abstract only" or "first page only".** The file is the full article.
8. **The brief's "six pages" for Wang.** The article runs to 21 pages.
9. **L117: "below 1 means livestock out-produce crops on that land".** True of the protein ratio only. On an energy basis, none of the three systems is below 1 (Table 8).
