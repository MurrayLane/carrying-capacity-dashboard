#!/usr/bin/env python3
"""Writes analysis/liquid_fuel_2025/README.md from fuel_trend.csv and biofuel_litres.csv.   Usage: python3 analysis/liquid_fuel_2025/write_readme.py (repository root)"""
import csv
T = {int(r['year_to_june']): r for r in csv.DictReader(open('analysis/liquid_fuel_2025/fuel_trend.csv'))}
B = {int(r['biofuel_litres_per_person']): int(r['capacity']) / 1e6 for r in csv.DictReader(open('analysis/liquid_fuel_2025/biofuel_litres.csv'))}
g = lambda y, k: int(float(T[y][k]))
rows = '\n'.join(f"| {y} | {g(y,'petrol_L_per_person')} | {g(y,'diesel_L_per_person')} | {g(y,'jet_L_per_person')} | {g(y,'all_products_L_per_person')} | {g(y,'petrol_ML')/1000:.1f} | {g(y,'diesel_ML')/1000:.1f} | {g(y,'jet_ML')/1000:.1f} |" for y in (2011, 2015, 2019, 2021, 2023, 2025))
p = lambda k: (g(2025, k) / g(2011, k) - 1) * 100
btab = '| Biofuel grown on the land, litres a person a year | ' + ' | '.join(str(k) for k in B) + ' |\n|---|' + '---|' * len(B) + '\n| Long-term capacity of Australia (million) | ' + ' | '.join(f'{v:.1f}' for v in B.values()) + ' |'
s = f'''# Liquid fuel: what the electric vehicle boom has changed, and what the long-term setting should say (SCOPE.md E15)

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
{rows}

* **Petrol per person has fallen {abs(p('petrol_L_per_person')):.0f}% since 2011** ({g(2011,'petrol_L_per_person')} to {g(2025,'petrol_L_per_person')} L), and total petrol sold has fallen ({g(2011,'petrol_ML')/1000:.1f} to {g(2025,'petrol_ML')/1000:.1f} billion L) while the population grew by a quarter. That is efficiency, hybrids and, lately, electric vehicles.
* **Diesel per person has risen {p('diesel_L_per_person'):.0f}%** ({g(2011,'diesel_L_per_person')} to {g(2025,'diesel_L_per_person')} L); total diesel has risen by more than half ({g(2011,'diesel_ML')/1000:.1f} to {g(2025,'diesel_ML')/1000:.1f} billion L). Freight, mining and a growing fleet of diesel utes and SUVs.
* **Jet fuel** collapsed in 2021 and is back at {g(2025,'jet_L_per_person')} L a person, close to its 2019 level of {g(2019,'jet_L_per_person')}.
* **All liquid fuel sold per person is only {abs(p('all_products_L_per_person')):.0f}% below 2011** ({g(2011,'all_products_L_per_person')} to {g(2025,'all_products_L_per_person')} L). Year to June 2026: petrol 15.6, diesel 33.8, jet 10.0 billion L (not yet per person).
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

{btab}

* The setting of 253 L of biofuel a person is about 8.9 billion litres at 35 million people, close to the 2050 need that would remain after the thesis's own cuts in a frugal society. The CSIRO estimate of the most that biogenic feedstock could supply, 12.8 billion litres, is about 340 to 365 L a person, which would take the long term to {B[340]:.1f} to {B[365]:.1f} million. So **the long-term fuel setting is reasonable as a statement of the biofuel the land might supply, but it is a design (a fossil-free, low-consumption society), not a statement of total liquid fuel demand, which projections put several times higher for the present economy.**
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
'''
open('analysis/liquid_fuel_2025/README.md', 'w').write(s)
