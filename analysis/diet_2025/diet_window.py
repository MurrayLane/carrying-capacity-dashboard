#!/usr/bin/env python3
"""The diet layer over the cattle price cycle (B138 item 5; R05a issue 14; R04b 8; R04a minors 10 and 11).

The 2025 diet inputs are three: the meat-and-egg share of food (13% in 2011), the red-meat share of meat (64%) and the split of red meat among beef, lamb, veal and pork (Base!V175:V178).
Each is the 2011 value times the change of an FAO food-balance series for Australia between a base window (2010-12) and a latest window (2021-23): analysis/consumption_2025/consumption_proxies.py
and make_red_meat_mix.py. This script recomputes the three inputs with every available three-year latest window (2010-12 to 2021-23 in the FAO file), and with the 10-year window 2014-2023 and the
whole series 2010-2023 (spanning the cattle price cycle), keeping the base window 2010-12, and evaluates the national short-term capacity of release 2025-fixed with each.
The rounding of the release is kept (meat-and-egg share to the nearest 0.5 point, red-meat share to three decimals, mix shares to six) and the unrounded figures are shown too.

The layer's effect = capacity with the window's three inputs minus capacity with the 2011 values of the three (0.13, 0.64, 1995 mix), everything else at 2025-fixed. This is the diet layer measured last
(an order of its own); the 2021-23 row reproduces the released 2025-fixed (41,503,537). It differs from the decomposition's consumption and red-meat-mix layers (A376, A380), which are measured in a chain
that also moves fuel, biofuel, timber and the organic share, and from the all-orderings averages.

Usage: python3 -I analysis/diet_2025/diet_window.py [FBS_CSV]   (run from the repository root; needs node with web/node_modules and the built data)
FBS_CSV defaults to /tmp/claude-0/fao/x/FoodBalanceSheets_E_All_Data_(Normalized).csv, the FAOSTAT bulk file whose sha256 is in qa/fao_bulk_hashes.csv (checked here). Writes diet_window.csv.
Deterministic: no random numbers.
"""
import csv, hashlib, json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
FBS = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/fao/x/FoodBalanceSheets_E_All_Data_(Normalized).csv'
want = next(r['sha256_csv'] for r in csv.DictReader(open(os.path.join(REPO, 'qa/fao_bulk_hashes.csv'))) if r['file'].startswith('FoodBalanceSheets'))
h = hashlib.sha256()
with open(FBS, 'rb') as f:
    for chunk in iter(lambda: f.read(1 << 24), b''): h.update(chunk)
if h.hexdigest() != want: sys.exit(f'FBS file hash {h.hexdigest()} is not the registered {want}')
with open(FBS, encoding='latin1') as f:
    head = f.readline(); lines = [l for l in f if l.startswith('"10",')]            # area code 10 is Australia; the Area column is checked below
rows = [r for r in csv.DictReader([head] + lines) if r['Area'] == 'Australia' and r['Element'] == 'Food supply quantity (kg/capita/yr)']
val = {}
for r in rows:
    try: val[(r['Item'], int(r['Year']))] = float(r['Value'])
    except ValueError: pass
FOOD = ['Cereals - Excluding Beer', 'Starchy Roots', 'Sugar & Sweeteners', 'Pulses', 'Treenuts', 'Oilcrops', 'Vegetable Oils', 'Vegetables', 'Fruits - Excluding Wine', 'Meat', 'Offals', 'Animal fats', 'Eggs', 'Milk - Excluding Butter', 'Fish, Seafood']
mean = lambda item, P: sum(val.get((item, y), 0.0) for y in P) / len(P)


def diet(P):
    tot = sum(mean(i, P) for i in FOOD); red = sum(mean(i, P) for i in ('Bovine Meat', 'Mutton & Goat Meat', 'Pigmeat', 'Meat, Other')); pou = mean('Poultry Meat', P)
    return dict(meat_eggs_share=(mean('Meat', P) + mean('Eggs', P)) / tot, red_share=red / (red + pou), beef=mean('Bovine Meat', P), mutton=mean('Mutton & Goat Meat', P), pork=mean('Pigmeat', P), poultry=pou)


BASE = (2010, 2011, 2012); b = diet(BASE)
M0 = {175: 0.6922456950886146, 176: 0.17890898284622808, 177: 0.01993170633841729, 178: 0.10891361572674008}    # Base!V175:V178 of the workbook (beef, lamb, veal, pork), as make_red_meat_mix.py
snap = lambda v, s: round(round(v / s) * s, 6)


def inputs(P):
    d = diet(P); me_r = d['meat_eggs_share'] / b['meat_eggs_share']; rd_r = d['red_share'] / b['red_share']
    br, mr, pr = d['beef'] / b['beef'], d['mutton'] / b['mutton'], d['pork'] / b['pork']
    raw = {175: M0[175] * br, 176: M0[176] * mr, 177: M0[177] * br, 178: M0[178] * pr}; s = sum(raw.values())
    mix = {r: raw[r] / s for r in raw}
    return dict(me_ratio=me_r, red_ratio=rd_r, beef_ratio=br, mutton_ratio=mr, pork_ratio=pr, meategg_raw=0.13 * me_r, redmeat_raw=0.64 * rd_r, meategg=snap(0.13 * me_r, 0.005), redmeat=round(0.64 * rd_r, 3),
                mix_raw=mix, mix={r: round(mix[r], 6) for r in mix}, beef_kg=d['beef'], poultry_kg=d['poultry'], me_share=d['meat_eggs_share'], red_share=d['red_share'])


windows = [(f'{y}-{str(y + 2)[2:]}', tuple(range(y, y + 3)), 'three-year') for y in range(2010, 2022)]
windows += [('2014-23', tuple(range(2014, 2024)), 'ten-year (cattle price cycle)'), ('2010-23', tuple(range(2010, 2024)), 'whole FAO series')]
payload = {'off': {'meategg': 0.13, 'redmeat': 0.64, 'mix': M0}, 'windows': []}
for name, P, kind in windows:
    payload['windows'].append({'name': name, 'kind': kind, 'years': [P[0], P[-1]], 'inputs': inputs(P)})
with tempfile.TemporaryDirectory() as td:
    pj = os.path.join(td, 'w.json'); json.dump(payload, open(pj, 'w'))
    subprocess.run(['node', os.path.join(HERE, 'diet_window_eval.mjs'), pj, os.path.join(HERE, 'diet_window.csv')], check=True, cwd=os.path.join(REPO, 'web'))
print('wrote diet_window.csv')
