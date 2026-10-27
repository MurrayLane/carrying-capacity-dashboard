#!/usr/bin/env python3
"""Writes analysis/fuel_sectors_2025/README.md from sectors.csv, scenarios.csv and capacity.csv.   Usage: python3 analysis/fuel_sectors_2025/write_readme.py (repository root)"""
import csv
S = list(csv.DictReader(open('analysis/fuel_sectors_2025/sectors.csv'))); SC = list(csv.DictReader(open('analysis/fuel_sectors_2025/scenarios.csv'))); C = {r['scenario']: r for r in csv.DictReader(open('analysis/fuel_sectors_2025/capacity.csv'))}
sec = '\n'.join(f"| {r['sector']} | {float(r['thesis_2008_PJ']):.1f} | {float(r['table_f_2007_08_PJ']):.1f} | {float(r['table_f_2023_24_PJ']):.1f} | {float(r['table_f_2023_24_PJ']) / float(r['table_f_2007_08_PJ']):.2f} |" for r in S)
def cap(name): return float(C[name]['capacity']) / 1e6
rows = []
for r in SC:
    n = r['scenario']; rows.append(f"| {n} | {r['litres_a_person_long_term']} | {cap(n):.1f} | {r['note']} |")
sc = '\n'.join(rows)
s = f'''# Re-deriving the long-term fuel default from current data (SCOPE.md E15)

The thesis set the long-term liquid fuel at 253 litres a person by keeping a share of each sector's use in 2008 (`analysis/liquid_fuel_2025/README.md`, section 0). This repeats that derivation on the latest Australian Energy Statistics (Table F1, 2025 edition, to 2023-24), which Murray uploaded to `carrying-capacity-models/Energy data/`. Reproduce:
`python3 -I analysis/fuel_sectors_2025/sector_derivation.py ".../Energy data/australian_energy_statistics_2025_table_f.xlsx"`, `node analysis/fuel_sectors_2025/capacity.mjs analysis/fuel_sectors_2025/capacity.csv`, `python3 analysis/fuel_sectors_2025/write_readme.py`.

## 1. The table reproduces the thesis

Liquid fuel (petrol, aviation fuel, kerosene, diesel, fuel oil, lubricants, other petroleum products; LPG left out, as in the thesis) by sector, petajoules:

| Sector | Thesis (2008) | Table F 2007-08 | Table F 2023-24 | Change since 2007-08 |
|---|---|---|---|---|
{sec}

The 2007-08 column matches the thesis within 8% for every sector (water transport is the furthest, the rest within 3%), and "other industry" to 0.1 PJ once petroleum refining's own use is left out, so the mapping is the thesis's. The thesis's arithmetic is reproduced exactly: 55.46 billion litres of liquid fuel over the June 2008 population gives 2,580 L a person, shared by sector energy, less the fuel for exported food, is 2,521 L; the cuts give 253.2 L.
Two sectors are not read from Table F directly: water transport (recent editions report its diesel and fuel oil only inside the whole transport division, so it is the division less road, rail, air and other transport) and lubricants, bitumen and solvents (Table F stopped reporting bitumen and solvents after 2007-08, so the thesis's 63.8 PJ is held).

## 2. What changed since 2008

* **Road transport use is up 23%** (1,012 to 1,246 PJ) and has changed character: petrol is down (638 to 567 PJ) while diesel has nearly doubled (375 to 679 PJ).
* **Mining use has nearly tripled** (111 to 312 PJ, nearly all diesel), rail is up by half and air by 42%.
* **Total liquid fuel per person is lower**: 2,265 L in the year to June 2024 (Australian Petroleum Statistics) against 2,580 L for 2008, so each sector's litres a person fall even where its energy rose.

## 3. The re-derived long-term setting

The thesis cuts (agriculture 80% of its domestic share, road, rail, water and other industry 10%, mining 5%, air 0.1%, lubricants 5%) applied to 2023-24. Long-term capacity of Australia, release `2025-resilience`, with all of the fuel as biofuel:

| Scenario | Litres a person (long term) | Capacity (million) | Note |
|---|---|---|---|
{sc}
| current default (253 L) | 253 | {float(C['current default (253 L)']['capacity']) / 1e6:.1f} | the thesis figure |

* **On current data the thesis method gives 210 L, not 253**, because total fuel per person has fallen. That alone lifts long-term capacity from 12.3 to {cap('thesis method; 2023-24'):.1f} million.
* **Electric vehicles matter only through the road line, and the road line is where the thesis put most of its litres.** If petrol use on the road disappears and only diesel stays at the thesis's 10%, the figure falls to about 156 L; with no liquid fuel on the road at all, about 90 L. Capacity is very sensitive here: the model's long term is {cap('road: petrol electrified; diesel kept at 10%'):.1f} million at 156 L and the ceiling with no biofuel at all is 18.3 million.
* **The cut of road diesel to 10% is the thesis's, and diesel on the road has doubled** (freight, utes and SUVs). Assuming heavy vehicles keep their diesel at the thesis's share is the weakest step of the electric-vehicle scenario; CSIRO has trucks electrifying more slowly than cars.
* **If the thesis text (roads cut 95%) is used instead of its workbook (90%)**, the 2023-24 figure is 150 L.

## 4. Caveats and decisions

* The thesis's cuts are the thesis's judgements about a fossil-free, frugal society (`analysis/liquid_fuel_2025/README.md`); this derivation updates the base they act on, it does not test them. Mining is now much larger, but is cut by 95%; air travel is cut to almost nothing, so the large rise in air fuel does not matter.
* Agriculture is scaled by population over short-term capacity (0.566 here: 27.19 million over 48.0 million), as the thesis scaled by 0.534.
* Table F's mining block includes oil and gas extraction, and its transport figures follow the ABS industry classification; LPG is left out throughout.
* The thesis figure stays as the 2011 replica. Murray decided (2026-10-27) to publish both: release `2025-fuel` (210 L, the thesis method on current data, layer 8 after `2025-resilience`) and `2025-fuel-ev` (156 L, an alternate of `2025-fuel` with the light road fleet electrified); `make_releases.py` writes them. Australia long term: 12.3 million in `2025-resilience`, 14.1 in `2025-fuel`, 17.1 in `2025-fuel-ev`; the short term is unchanged.
'''
open('analysis/fuel_sectors_2025/README.md', 'w').write(s)
