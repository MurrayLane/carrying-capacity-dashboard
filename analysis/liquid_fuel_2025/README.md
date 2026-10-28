# Liquid fuel: what the electric vehicle boom has changed, and what the long-term setting should say (SCOPE.md E15)

## 0. Where the 253 litres came from

It is a designed scenario, not a forecast. The thesis (section 8.4.2, long-term defaults) sets out a fossil-fuel-free future in which a society would not replace its petroleum with an equal amount of biofuel (that would need 96% of the cropping land: the Dashboard gives 293,487 km2 against the 2520 L default with 100% biofuel). So the Biofuel parameter is set to 100% and the liquid fuel parameter is cut from 2,520 to 253 litres a person by cutting each sector of today's use: agriculture is viewed as essential and cut 20% (after removing the fuel used to grow exported food), most other industry, construction, commerce, rail and water transport cut 90%, mining 95%, and air travel is "virtually non-existent".
The workings are in the models archive, `prelim models/non-food resource data.xls`, sheet `biofuel` (sector energy from ABARE *Energy in Australia 2011* p.16 and the ABARES *Australian Energy Resource Assessment*, 2008 data, converted at 28.4 million litres a petajoule):

| Sector | Energy (PJ) | Today, L a person | Share kept | Long term, L a person |
|---|---|---|---|---|
| Agriculture (after removing fuel for exported food) | 86.9 | 126.3 (67.4) | 80% | 53.9 |
| Road transport | 1,003.3 | 1,457.7 | 10% | 145.8 |
| Rail | 34.1 | 49.5 | 10% | 5.0 |
| Air transport | 230.3 | 334.6 | 0.1% | 0.3 |
| Water transport | 60.3 | 87.6 | 10% | 8.8 |
| Mining | 114.3 | 166.1 | 5% | 8.3 |
| Other industry, construction, commercial and residential | 182.7 | 265.4 | 10% | 26.5 |
| Lubricants, bitumen, solvents | 63.8 | 92.7 | 5% | 4.6 |
| **Total** | **1,775.7** | **2,521** | **10.04%** | **253.2** |

Points to know about it:
* **Road transport is 58% of the 253 litres.** That is the component electric vehicles act on directly. The thesis does not say how much of its 10% is for the engines of the future; an electrified road fleet would leave very little.
* **The text and the workbook differ for roads.** The thesis text says mining and roads are cut 95%; the workbook keeps 10% for road transport (a 90% cut) and 5% for mining. At 5% for roads the total would be 180 litres.
* **How the 2,520 L baseline is built:** total liquid fuel from barrels of oil and biofuel (55.46 billion litres in 2008) divided by the June 2008 population (21.5 million) gives 2,580 L a person; the sector shares of energy (the 1,775.7 PJ) share that out; the fuel for exported food is removed from agriculture (-58.8 L) to give 2,521 L. (An earlier version of this note suggested a population divisor of 20.0 million; that was a misreading of the sheet, corrected after reproducing its arithmetic exactly in `analysis/fuel_sectors_2025/`.)
* **It is deliberately frugal.** It assumes no aviation, a fraction of today's mining (which exports most of what it digs) and freight. Comparing it with projected demand (section 2) compares a design for a fossil-free, low-consumption society with forecasts for the present economy. It is not wrong because forecasts are higher; it answers a different question.

The question in this folder is whether electric vehicles and the other changes since 2011 call for a different long-term setting. Sources are listed at the end; figures I read in the primary documents are marked as such.

## 1. What has been measured (Australian Petroleum Statistics, year to June; `fuel_trend.py`)

| Year | Petrol L/person | Diesel L/person | Jet fuel L/person | All products L/person | Petrol (billion L) | Diesel (billion L) | Jet (billion L) |
|---|---|---|---|---|---|---|---|
| 2011 | 847 | 959 | 316 | 2403 | 18.9 | 21.4 | 7.1 |
| 2015 | 764 | 1097 | 342 | 2393 | 18.2 | 26.1 | 8.1 |
| 2019 | 694 | 1155 | 372 | 2386 | 17.6 | 29.3 | 9.4 |
| 2021 | 623 | 1175 | 132 | 2063 | 16.0 | 30.2 | 3.4 |
| 2023 | 605 | 1204 | 281 | 2226 | 16.1 | 32.1 | 7.5 |
| 2025 | 579 | 1206 | 348 | 2250 | 16.0 | 33.3 | 9.6 |

* **Petrol per person has fallen 32% since 2011** (847 to 579 L), and total petrol sold has fallen (18.9 to 16.0 billion L) while the population grew by a quarter. That is efficiency, hybrids and, lately, electric vehicles.
* **Diesel per person has risen 26%** (959 to 1206 L); total diesel has risen by more than half (21.4 to 33.3 billion L). Freight, mining and a growing fleet of diesel utes and SUVs.
* **Jet fuel** collapsed in 2021 and is back at 348 L a person, close to its 2019 level of 372.
* **All liquid fuel sold per person is only 6% below 2011** (2403 to 2250 L). Year to June 2026: petrol 15.6, diesel 33.8, jet 10.0 billion L (not yet per person).
* **Electric vehicles so far:** 13.1% of new cars sold in 2025 (9.6% in 2024; Electric Vehicle Council and FCAI figures, secondary report), 14.6% in March 2026 (NIEIR, VFACTS). They are still about 2% of cars on the road, because the fleet turns over slowly: the average vehicle is about ten years old. Grattan Institute (2026) reports that in August 2026 battery electric vehicles outsold petrol cars for the first time.

## 2. What is projected

| Source | Projection |
|---|---|
| CSIRO for AEMO, Electric vehicle projections 2025 (read: Apx Table A.2) | Share of cars on the road that are electric: 1.8% in 2025; Step Change 10% in 2030, 24% in 2035, 45% in 2040, 82% in 2050 (Slower Growth 68%, Accelerated Transition 96% in 2050). Trucks and buses are slower than cars. |
| CEFC and Deloitte, Refined Ambitions (2025) (read) | Australia uses over 56 billion litres of liquid fossil fuel a year. Electrification could cut liquid fuel demand 29% by 2040 and 57% by 2050, to about 30 billion litres (29.3). Aviation, heavy freight and mining are 42% of demand in 2024, 64% in 2040 and 80% in 2050. If electrification is 20% slower, about 7.7 billion litres more are needed in 2050. |
| Grattan Institute submission 2026 (read) | Over 25 years petrol demand falls 66%, diesel rises 4% and jet fuel doubles. |
| CSIRO Sustainable Aviation Fuel Roadmap 2023 (search summary) | Jet fuel demand rises about 75% between 2023 and 2050. |
| CEFC and CSIRO (read in CEFC) | Biogenic feedstock could be processed into 7.2 billion litres of low carbon liquid fuel in 2030, rising to 12.8 billion litres by 2050. A strongly regulated market would be almost 12 billion litres in 2050. |
| AEMO 2026 Integrated System Plan (press summaries only) | About 80% of vehicles electric by 2050 in the central scenario; road transport electricity from about 1 TWh to 61 TWh. |

**Residual liquid fuel in 2050 is therefore not small.** About 30 billion litres (CEFC with strong electrification) to about 59 billion litres (Grattan's changes applied to 2025 sales: petrol 5.4 + diesel 34.6 + jet 19.2). At a population of 35 million (my assumption; an ANU commentary quoted 32 to 38 million) that is roughly 840 to 1,700 litres a person, three to seven times the model's 253 L.
Electric vehicles cut petrol, which is the largest and easiest part; the diesel and jet fuel that remain are the hard sectors, and they are growing.

## 3. What this means for the model

The model charges land only for the fuel that is biofuel. Fuel that is not biofuel (fossil, hydrogen or electricity-derived e-fuel) costs no land in the model, so **capacity depends on litres of biofuel a person**, not on total liquid fuel (253 L all biofuel and 506 L half biofuel give the same answer). Australia, long-term settings, release `2025-resilience`:

| Biofuel grown on the land, litres a person a year | 0 | 100 | 200 | 253 | 340 | 365 | 500 | 750 | 1000 |
|---|---|---|---|---|---|---|---|---|---|
| Long-term capacity of Australia (million) | 18.3 | 17.7 | 14.5 | 12.3 | 9.8 | 9.3 | 7.2 | 5.0 | 3.9 |

* The setting of 253 L of biofuel a person is about 8.9 billion litres at 35 million people, close to the 2050 need that would remain after the thesis's own cuts in a frugal society. The CSIRO estimate of the most that biogenic feedstock could supply, 12.8 billion litres, is about 340 to 365 L a person, which would take the long term to 9.8 to 9.3 million. So **the long-term fuel setting is reasonable as a statement of the biofuel the land might supply, but it is a design (a fossil-free, low-consumption society), not a statement of total liquid fuel demand, which projections put several times higher for the present economy.**
* Faster electrification does not help the long-term figure by much. It lowers total demand (the 2050 need falls from about 59 to about 30 billion litres) and so lowers the share that has to come from somewhere other than biofuel. The land used is set by how much biofuel is grown, not by how much fuel is used.
* CEFC reports CSIRO's view that the feedstock (wastes, residues, oilseeds in rotation) need not displace food production. If so the land cost of biofuel is lower than the model's cropland-based figure, and the table above is an upper bound on the cost.
* The balance of 2050 demand (about 20 to 50 billion litres) has to come from e-fuels or imports, or stay fossil, which the long-term (sustainable) scenario cannot assume. The model does not represent that, and the README of `analysis/long_term_2025/` should be read with this in mind.

## 4. Proposed changes (decisions for SCOPE.md E15)

1. Keep the default of 253 L of biofuel, and the thesis derivation, as the 2011 replica. State it as "litres of biofuel grown on the land" and show the total liquid fuel need beside it (840 to 1,700 L a person in 2050), with the balance named as e-fuel, imports or fossil.
2. Offer named scenarios: no biofuel on cropland (residues only), 253 L (current), 340 L (CSIRO's maximum).
3. Treat the model's cropland-based biofuel yield as an upper bound on land cost and review it against the CSIRO feedstock mix (not done).
4. The re-derivation of the sector table on current data (Australian Energy Statistics Table F, uploaded by Murray) is in `analysis/fuel_sectors_2025/README.md`: the thesis cuts on 2023-24 use give 210 L; electrifying light vehicles gives about 156 L.

## Sources

* APS: Australian Petroleum Statistics, August 2026 extract, data.gov.au (the workbook used by `analysis/consumption_2025/`).
* CSIRO, *Electric vehicle projections 2025* for AEMO, December 2025: https://www.aemo.com.au/-/media/files/stakeholder_consultation/consultations/nem-consultations/2025/draft-2026-fau/csiro-electric-vehicle-projections.pdf
* CEFC and Deloitte, *Refined Ambitions: exploring Australia's low carbon liquid fuel potential*: https://www.cefc.com.au/media/jh3gvm14/refined-ambitions-exploring-australia-s-low-carbon-liquid-fuel-potential.pdf
* Grattan Institute, *Getting fuel storage right* (submission, 2026): https://grattan.edu.au/wp-content/uploads/2026/09/Grattan-Institute-Submission-2026-Getting-fuel-storage-right.pdf
* NIEIR, long and short-term implications of the 2026 oil price shock for Australia's transport sector emissions: https://nieir.com.au/?p=7201 (its fuel table matches the APS figures above).
* Electric Vehicle Council, *State of Electric Vehicles 2025*: https://electricvehiclecouncil.com.au/wp-content/uploads/2025/10/State-of-EVs_2025_141025-2.pdf (secondary summaries read).
* CSIRO Sustainable Aviation Fuel Roadmap (2023): https://www.csiro.au/-/media/Energy/Sustainable-Aviation-Fuel/Sustainable-Aviation-Fuel-Roadmap.pdf (search summary only).
* Not reached: the AEMO 2026 ISP document itself, DCCEEW *Australia's emissions projections 2025*, Net Zero Australia, and the Australian Energy Statistics Table F (diesel by sector; the energy.gov.au server returned an error).

Reproduce: `python3 -I analysis/liquid_fuel_2025/fuel_trend.py APS_XLSX`, `node analysis/liquid_fuel_2025/scenarios.mjs analysis/liquid_fuel_2025/scenarios.csv`, `python3 analysis/liquid_fuel_2025/write_readme.py`.

## Biodiesel yield from oilseeds: a probable double count in the thesis workings (2026-10-28, SCOPE.md E17)

Looking for what drives the long-term range (the long-term liquid fuel explains about half of its variance) led to how the model turns litres of fuel into land. Biodiesel is 45% of the fuel and nearly all of the land the model charges for fuel, and its yield from each oilseed is low.

**What the workbook does.** `Base!K336:K344` is the grams of biodiesel per gram of feedstock. It comes from the archive workbook (`prelim models/non-food resource data.xls`, sheet `biofuel`, rows 39 to 48): `lt fuel / tonne input` = 400, times 0.00088 tonnes a litre = `tonne fuel / tonne input` 0.352, times `Initial processing yield` (the seed's oil content: canola 0.42, olive 0.18, sunflower 0.405, soy 0.185 and so on) = `Yield`. For canola this is 0.14784, the 14.8% in the thesis appendix table. Ethanol is built the same way with its cane-to-sugar step as the initial processing yield (cane 0.1429, so 560 litres a tonne of sugar gives 80 litres a tonne of cane, which is right).

**Why it looks wrong.** 400 litres is what a tonne of canola seed gives (the Manitoba costing model: 42% oil, 32% recovered as oil by pressing, about 353 litres of biodiesel a tonne of seed; laboratory yields 310 to 342), so multiplying by the oil content again counts the oil twice and cuts the yield to 168 litres a tonne. If 400 was meant per tonne of oil, it is a third of the roughly 1,100 litres the reaction gives (97% mass yield, 0.88 kg a litre). Either reading gives a yield about half of what the same figures give for the seed. I have not found the source of the 400, and the thesis text gives only the density (0.88): **this needs Murray's check against the original source before it is called an error.**

**The method module** `biodiesel-yield` sets each oilseed's yield to its oil content times 0.76 (net recovery of oil from seed, canola) times 0.97 (transesterification), so canola gives 0.31 tonnes a tonne (about 350 litres a tonne). Releases `2011-biodiesel` and `2025-biodiesel` apply it to the thesis method on each vintage. Australia, long term, millions of people (the short term moves by 0.1% through its 0.23% biofuel share):

| | As published | Yield counted once | Change | Land charged for fuel, m2 a person |
|---|---|---|---|---|
| 2011 data, thesis method (`2011-corrected`) | 9.43 | 14.77 | +57% | 41,130 to 20,300 |
| 2011 data, improved method (not a release) | 7.94 | 11.87 | +50% | |
| 2025 data, thesis method (`2025-mirror`) | 14.06 | 17.62 | +25% | 24,698 to 12,035 |
| 2025 data, improved method (not a release) | 12.01 | 16.42 | +37% | |

* **It changes the comparison with 2011.** The long-term change from 2011 to 2025 on the thesis method is +4.6 million as published and +2.9 million with the yield counted once, because the fuel land was binding more on the 2011 data; the thesis's 9.4 million (the figure of the published papers) would be 14.8 million.
* **Other values in the model are unaffected**: ethanol, the diet and all the short-term settings except a 0.1% change through the biofuel share.
* **The feedstock mix is a second lever, not yet a module.** The model takes biodiesel from canola 20% and then olive, macadamia, grape, linseed, sesame, sunflower, soy and peanut at 10% each; most are low-yielding or high-value food oils (sesame 0.12 tonnes a hectare). With the yield fixed, a mix of 60% canola and 40% sunflower gives 17.85 million (Australia, 2025) against 17.62, and in Queensland 2.14 against 1.40 million; all canola 17.92 and 2.41. The model's national figure is bounded by another land type once fuel needs little land, so the national gain is small; the mix matters most where cropland binds. Residues, tallow and used cooking oil (no land) and second-generation ethanol are not in the model (`DISCUSSION.md`, `IDEAS.md`).
* **The ranges** of `analysis/sensitivity_2025/` were computed on the yield as published; with it counted once the long-term fuel would explain less of the spread and they should be rerun if the module is adopted.

**Decision for Murray:** is 400 litres a tonne of seed (so the oil content is counted twice, and the module is a correction) or per tonne of oil (a lower figure still wrong)? If a correction, it is recorded as `2011-biodiesel` and `2025-biodiesel` and should join the improved method (`IMPROVED` in `analysis/comparison_2025/make_cells.py`) and paper 1 should report the 2011 long-term figure both ways.
