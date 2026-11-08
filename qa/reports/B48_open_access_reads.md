# B48: open-access full texts for twelve abstract-only works

Register rows touched: L075, L076, L088, L103, L104, L109, L114, L116, L117, L119, L124, L129 (`qa/literature_register.csv`; CRLF and all 12 columns kept). No PDF was placed in a repository; copies were read as text in the scratch folder `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/b48`.

## Counts

| Outcome | Works |
|---|---|
| now `read` (full text opened) | 3: L116 Roos, L119 Clark and Tilman, L124 Shepon |
| still abstract only, host refusal named | 9: L109, L114, L129, L103, L117, L104, L088, L076, L075 |

## Read

### L124: Shepon et al. 2016

* **Citation:** Shepon, Eshel, Noor and Milo 2016, Environmental Research Letters 11(10): 105002, "Energy and protein feed-to-food conversion efficiencies in the US and potential food security gains from dietary changes". https://doi.org/10.1088/1748-9326/11/10/105002 (read on the IOP page, open access; supplement not opened).
* **What it argues:** Follows calories and protein from feed through US livestock to human food. About 7% of feed calories and 8% of feed protein end as food; beef is lowest (about 3% of calories, 2.5% of protein), eggs and dairy highest (about 17%). It then asks how many more people the cropland now growing beef feed (pasture excluded) could feed if poultry replaced beef: about 116 million on calories, 142 million on protein, and about 190 million for a legume-led plant swap. These are gains on top of today's US population, not a capacity.
* **Method family:** commodity (energy and protein) balance, with a land per diet step (the "dietary shift potential").
* **Numbers:** US only; the diet needs about 0.5 acre per person per year; no Australian figure.
* **Use in the methods paper:** comparator for the diet assumption (section 6) and for the energy-balance family (section 4): it shows how much the diet term alone moves a land-based count, and that the count is about reallocating feed land.
* **Cites Lane:** No.

### L119: Clark and Tilman 2017

* **Citation:** Clark and Tilman 2017, Environmental Research Letters 12(6): 064016, "Comparative analysis of environmental impacts of agricultural production systems, agricultural input efficiency, and food choice". https://doi.org/10.1088/1748-9326/aa6cd5 (read as the open-access PDF held by Oxford ORA; supplement not opened).
* **What it argues:** A meta-analysis of 164 life cycle assessments (742 systems, over 90 foods, cradle to farm gate, five indicators). Organic needs 25% to 110% more land per unit of food; grass-fed beef needs more land than grain-fed (4 pairs) and emits about 19% more GHG (7 pairs, not significant); ruminant meat has 20 to 100 times the impact of plant foods and 3 to 10 times other animal foods. Diet shifts and input efficiency matter more than switching production system.
* **Method family:** footprint (life cycle meta-analysis).
* **Numbers:** no capacity figure and no Australian figure. 86% of the systems are from Europe, North America, Australia and New Zealand, and the authors say the results describe high-input systems.
* **Use in the methods paper:** context for the diet assumption (section 6). Caution: "land use" is land occupied per unit of food, so grass-fed beef scores worse because pasture counts as land used; it does not test whether that land could grow crops.
* **Cites Lane:** No.

### L116: Roos et al. 2017

* **Citation:** Roos, Bajzelj, Smith, Patel, Little and Garnett 2017, Global Environmental Change 47: 1-12, "Greedy or needy? Land use and climate impacts of food in 2050 under different livestock futures". https://doi.org/10.1016/j.gloenvcha.2017.09.001 (read as the open-access PDF held by Aberdeen AURA; supplement with regional results and model description not opened).
* **What it argues:** Seven livestock futures (including intensification, plant-based eating, artificial meat and "ecological leftovers"), two diets and four yield and waste settings give 56 runs of land need for 2050. At today's yields and waste, cropland suffices only if all animal protein is replaced by artificial variants. With yield gaps and waste both halved, it suffices for every scenario that cuts animal products or moves to poultry and aquaculture, but not for current-pattern livestock fed from cropland. Leftovers-only livestock (30% pasture use) gives 40 to 56 kg red meat per person per year with much less cropland.
* **Method family:** scenario model (an Excel land per diet balance run by region).
* **Numbers:** 12 world regions modelled separately with no trade between them; Oceania is one region and its results are in the supplement, so no Australian number was taken. Global productive cropland is about 2000 Mha (used cropland plus about 450 Mha practically available); 1.4 billion ha of unused land is classed prime or good before constraints.
* **Use in the methods paper:** comparator for the diet assumption and grazing (section 6) and for land per diet (section 4). It is a no-trade regional method of the same kind as the paper's own, and it shows the answer turning on the livestock rule, yield gap and waste.
* **Cites Lane:** No.

## Still abstract only (host refusals)

| Row | Work | What refused or was missing |
|---|---|---|
| L109 | Wang 2022, Land | mdpi.com 403; DOAJ page 403; Unpaywall lists no other copy |
| L114 | Schon and Bohringer 2023 | mdpi.com 403; preprints.org download 403 |
| L129 | Wackernagel 2019 | mdpi.com 403; DOAJ page 403 |
| L103 | Zumkehr and Campbell 2015 | ESA Wiley page returned a challenge page; OpenEdition copy returned a bot check; no other copy listed |
| L117 | van Zanten 2016 | Springer article and PDF links returned a 3 KB script page; WUR repository page had no file link; Europe PMC has no copy |
| L104 | Kurtz 2020 | closed access; no author manuscript at Europe PMC, Unpaywall or Semantic Scholar |
| L088 | Chapman and Byron 2018 | ScienceDirect 403; DOAJ 403; Europe PMC has no copy; CORE returned 429 |
| L076 | Bryan 2016 | UTAS repository link returned an empty 202; figshare file download 403; ScienceDirect PDF host and CSIRO publications repository 403 |
| L075 | Hatfield-Dodds 2015 | both figshare records are embargoed with no file; CSIRO publications repository 403; no other copy listed |

Each refused host was left alone after its refusal. The Oxford ORA and Aberdeen AURA repository files and the IOP page for Shepon were the only open routes that worked.

## What changes the paper's argument

Nothing reverses a position. Three points sharpen existing ones:

* Roos 2017 is a no-trade regional method, close to the paper's own design, and its verdict flips with the livestock rule, yield gap and waste. That supports putting the diet and grazing assumption among the things that move the number (sections 4 and 6). Its Oceania result is in the supplement and is worth fetching if a regional comparator is wanted.
* Shepon 2016 reports a count of extra people fed from a reallocation, not a capacity; the paper should not list it with the capacity estimates.
* Clark and Tilman 2017 counts pasture as land used, so a land-occupied footprint and a land-available capacity point in opposite directions for grazing.

None of the three cites Lane's work or uses the phrase carrying capacity.
