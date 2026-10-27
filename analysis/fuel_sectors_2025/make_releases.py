#!/usr/bin/env python3
"""Writes releases/2025-fuel/release.json (long-term liquid fuel re-derived from current sector use, thesis method: 210 L) and releases/2025-fuel-ev/release.json (alternate: light vehicles electrified, 156 L),
from analysis/fuel_sectors_2025/scenarios.csv.   Usage: python3 analysis/fuel_sectors_2025/make_releases.py          (repository root; run sector_derivation.py first)"""
import csv, json, os
ROOT = os.getcwd(); sc = {r['scenario']: r for r in csv.DictReader(open(os.path.join(ROOT, 'analysis/fuel_sectors_2025/scenarios.csv')))}
l_thesis = round(float(sc['thesis method; 2023-24']['litres_a_person_long_term'])); l_ev = round(float(sc['road: petrol electrified; diesel kept at 10%']['litres_a_person_long_term']))
cap = {r['scenario']: float(r['capacity']) / 1e6 for r in csv.DictReader(open(os.path.join(ROOT, 'analysis/fuel_sectors_2025/capacity.csv')))}
reason = lambda l, how: f"Long-term liquid fuel, litres a person, re-derived from the Australian Energy Statistics Table F (2023-24): {how} The thesis set 253 L by keeping a share of each sector's 2008 use (analysis/fuel_sectors_2025/README.md). All of it is biofuel (the Biofuel setting stays at 100%)."
rels = {
 '2025-fuel': {'id': '2025-fuel', 'label': '2025 data and the long-term liquid fuel re-derived', 'status': 'current', 'extends': '2025-resilience',
   'description': f"Layer 8, a data update of the long-term liquid fuel default. The thesis's own derivation (sector use of 2008, each sector cut: road, rail, water and other industry to 10%, mining 5%, air 0.1%, agriculture 80%, lubricants 5%) is repeated on the 2023-24 sector use of Table F1 of the Australian Energy Statistics and the total fuel sold per person in the year to June 2024. The result is {l_thesis} L a person instead of 253. Only the long-term result moves (Australia {cap['thesis method; 2023-24']:.1f} million against {cap['current default (253 L)']:.1f}); the short-term settings are unchanged.",
   'vintage': 'Table F to 2023-24', 'patches': [{'preset': 'long', 'field': 'fuel', 'value': float(l_thesis), 'reason': reason(l_thesis, 'the thesis cuts on current sector use, and total liquid fuel per person 2,265 L (Australian Petroleum Statistics, year to June 2024) against 2,580 L for 2008.')}],
   'errata': ['The cuts and the 100% biofuel setting are the thesis choices; mining use has nearly tripled since 2008 but is cut 95%, and air travel is cut to almost nothing.', 'Water transport and lubricants are partly estimated (analysis/fuel_sectors_2025/README.md).']},
 '2025-fuel-ev': {'id': '2025-fuel-ev', 'label': 'Alternate: long-term liquid fuel with the light road fleet electrified', 'status': 'current', 'extends': '2025-fuel',
   'description': f"An alternate to 2025-fuel, not a later layer. Petrol used on the road is taken as electrified (CSIRO projects 82% of cars electric by 2050); road diesel, which has nearly doubled since 2008, is cut to the thesis's 10%. The long-term liquid fuel falls to {l_ev} L a person; long-term capacity of Australia {cap['road: petrol electrified; diesel kept at 10%']:.1f} million against {cap['thesis method; 2023-24']:.1f} in 2025-fuel. Capacity is very sensitive to this figure: with no biofuel at all it would be 18.3 million.",
   'vintage': 'Table F to 2023-24, CSIRO electric vehicle projections 2025', 'patches': [{'preset': 'long', 'field': 'fuel', 'value': float(l_ev), 'reason': reason(l_ev, 'petrol on the road electrified and road diesel kept at 10% (so heavy vehicles keep their diesel, which is the weakest assumption: CSIRO has trucks electrifying more slowly than cars).')}],
   'errata': ['The share of road diesel that is light vehicles (utes and SUVs) is not separated in the table; treating all road diesel as heavy is conservative for the electric case.']}}
idx = json.load(open(os.path.join(ROOT, 'releases/index.json')))
for rid, rel in rels.items():
    os.makedirs(os.path.join(ROOT, f'releases/{rid}'), exist_ok=True); json.dump(rel, open(os.path.join(ROOT, f'releases/{rid}/release.json'), 'w'), indent=2); print('wrote releases/%s/release.json (%s L)' % (rid, rel['patches'][0]['value']))
    if rid not in idx['order']: idx['order'].insert(idx['order'].index('2025-resilience'), rid)
# order: newest layer first, its alternate just after it
idx['order'].remove('2025-fuel-ev'); idx['order'].insert(idx['order'].index('2025-fuel') + 1, '2025-fuel-ev')
json.dump(idx, open(os.path.join(ROOT, 'releases/index.json'), 'w'), indent=2); print(idx['order'][:8])
