#!/usr/bin/env python3
"""Writes methods/regional-beef-output/method.json (SCOPE.md E1): beef output per dry sheep equivalent differs by state, as the ABARES farm survey measures it.
Usage: python3 -I analysis/pasture_2025/make_regional_beef.py          (repository root; reads analysis/pasture_2025/abares_state_beef_index.csv, made by abares_state_index.py from the ABARES Farm Data Portal)

Evidence (Livestock/ABARES-NT-WA/ of the models archive):
  * ABARES Farm Data Portal, state estimates 1990 to 2025, beef specialist farms, mean 2017 to 2023 (abares_state_index.py): the value of the cattle a farm sends off (sold plus transferred off, at the sale price)
    per animal it keeps: NSW 817, Victoria 836, Tasmania 826, South Australia 772, Queensland 602, Western Australia 533, Northern Territory 553 dollars a head of herd. Index against the temperate south (NSW, Victoria, Tasmania): 0.99,
    1.01, 1.00, 0.93, 0.73, 0.65, 0.67.
  * Cross-checks: ABARES, Australian beef 2012-13 to 2014-15 and 2015-16 to 2017-18 (live weight produced per head of herd, north 156 kg, south 188 kg: ratio 0.83; turn-off 31 to 38% against 41 to 47%); NT Department of
    Agriculture waybills 2019 to 2024 (NT turn-off 22 to 37% of the herd).
The index of each state is applied to the cattle meat yield of every zone of the state (the Australian zone keeps the national yield), times one constant so that the nation's beef, weighted by the states' beef dry
sheep equivalents (2010 class counts, the archive's latest, used by both data vintages), is unchanged."""
import csv, json, os
ROOT = os.getcwd(); P = json.load(open(os.path.join(ROOT, 'pipeline/yields/archive_livestock_parameters.json')))['parameters']
base = json.load(open(os.path.join(ROOT, 'pipeline/yields/archive_livestock_inputs.json')))['years']['2010']['regions']
IDX = {r['state']: float(r['index_vs_temperate_south']) for r in csv.DictReader(open(os.path.join(ROOT, 'analysis/pasture_2025/abares_state_beef_index.csv')))}
dse = lambda z: sum(P[n] * (base[str(z)].get(k) or 0) for n, k in (('dseBeefBulls', 'beefBulls'), ('dseBeefCows', 'beefCows'), ('dseBeefCalves', 'beefCalves'), ('dseBeefBalance', 'beefBalance')))
STATES = {2: 'New South Wales', 15: 'Victoria', 26: 'Queensland', 40: 'South Australia', 49: 'Western Australia', 56: 'Tasmania', 60: 'Northern Territory'}
CHILD = {2: range(3, 15), 15: range(16, 26), 26: range(27, 40), 40: range(41, 49), 49: range(50, 56), 56: range(57, 60), 60: []}
tot = sum(dse(z) for z in STATES); k = tot / sum(dse(z) * IDX[n] for z, n in STATES.items())
zones = {}
for z, n in STATES.items():
    zones[str(z)] = round(k * IDX[n], 4)
    for c in CHILD[z]: zones[str(c)] = round(k * IDX[n], 4)
north = sum(dse(z) for z in (26, 49, 60)) / tot
mod = {'id': 'regional-beef-output', 'label': 'Beef output per animal by state (ABARES farm survey)', 'line': 'improved',
       'description': "The model gives every zone the national meat production in proportion to its dry sheep equivalents, so beef output per animal is the same in the tropical north and the temperate south. The ABARES farm survey measures it: on beef specialist farms, 2017 to 2023, the value of the cattle sent off (sold plus transferred, at the sale price) per animal kept was $817 (NSW), $836 (Victoria), $826 (Tasmania), $772 (South Australia), $602 (Queensland), $533 (Western Australia) and $553 (Northern Territory), an index of 0.99, 1.01, 1.00, 0.93, 0.73, 0.65 and 0.67 against the temperate south. The module multiplies the cattle meat yield of every zone of a state by the state's index and by one constant ("+"%.3f" % k+") so that national beef is unchanged. The Australian figure does not change; the southern state and regional figures rise and the northern ones fall, and fall in capacity only where pasture, not cropland, sets it.",
       'yieldFactors': [{'row': 98, 'label': 'Cattle meat (g/m2)', 'zones': zones}],
       'errata': ["The index is one measure (output value per animal kept, 2017 to 2023, ABARES survey samples) and ignores differences in the price per kilogram; the weight per head produced in ABARES's 2014-15 tables gives a north to south ratio of 0.83, the state indices give 0.65 to 0.73, and the NT waybill turn-off (31%) supports the lower end.",
                  "One factor a state: Western Australia's south-west and rangelands, and the southern and northern parts of Queensland and the NT, share their state's index; the survey has no finer split in this release.",
                  "The ABARES receipts per hectare operated (2021-24) agree with the pattern for Victoria and Tasmania and put the arid South Australian and Western Australian rangelands at about a third of the model's value; not used in the module (area operated includes other land).",
                  "Sheep and wool are unchanged: wool per dry sheep equivalent by state of the farm is within 7% of the nation for the large wool states (analysis/pasture_2025)."]}
os.makedirs(os.path.join(ROOT, 'methods/regional-beef-output'), exist_ok=True)
json.dump(mod, open(os.path.join(ROOT, 'methods/regional-beef-output/method.json'), 'w'), indent=2)
print('k', round(k, 3), {n: zones[str(z)] for z, n in STATES.items()})
