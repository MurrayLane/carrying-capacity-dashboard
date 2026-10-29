#!/usr/bin/env python3
"""Writes methods/regional-beef-output/method.json (SCOPE.md E1): beef output per dry sheep equivalent lower in northern Australia than in the south, as the ABARES beef farm survey measures it.
Usage: python3 -I analysis/pasture_2025/make_regional_beef.py          (repository root)

Evidence (Livestock/ABARES-NT-WA/ of the models archive):
  * ABARES, Australian beef: financial performance of beef farms, 2015-16 to 2017-18, Table 7: total live weight of cattle produced per farm in 2014-15, 227 tonnes in northern Australia and 75 in southern
  * ABARES, Australian beef 2012-13 to 2014-15 (austbeef_2015_v100), Table 2: beef cattle at 30 June per farm in 2014-15, 1,453 northern and 400 southern; turn-off 38% and 47%; branding 70% and 86 to 89%
  Live weight produced per head: north 227,000 / 1,453 = 156 kg, south 75,000 / 400 = 188 kg; ratio 0.83. The turn-off rates (31 to 38% north, 41 to 47% south; decade averages 32 to 33% and 44%) give 0.74 to 0.81.
  ABARES's northern region is northern Western Australia, the Northern Territory and Queensland; the southern region is the rest. Here: Queensland and its regions, the Northern Territory and the WA Rangelands region.
The factor f (0.83) is applied to the cattle meat yield of the northern zones, and the southern zones are scaled up by k so that the nation's beef is unchanged (the Australian zone keeps the national yield). The shares
are the beef dry sheep equivalents of the 2010 class counts (the archive's latest), which both data vintages use."""
import json, os
ROOT = os.getcwd(); P = json.load(open(os.path.join(ROOT, 'pipeline/yields/archive_livestock_parameters.json')))['parameters']
base = json.load(open(os.path.join(ROOT, 'pipeline/yields/archive_livestock_inputs.json')))['years']['2010']['regions']
F = 227000 / 1453 / (75000 / 400)
dse = lambda z: sum(P[n] * (base[str(z)].get(k) or 0) for n, k in (('dseBeefBulls', 'beefBulls'), ('dseBeefCows', 'beefCows'), ('dseBeefCalves', 'beefCalves'), ('dseBeefBalance', 'beefBalance')))
STATES = [2, 15, 26, 40, 49, 56, 60]; NORTH_REGIONS = list(range(27, 40)) + [52]
w = {s: 0.0 for s in STATES}; w[26] = w[60] = 1.0; w[49] = dse(52) / dse(49)
n = sum(w[s] * dse(s) for s in STATES) / sum(dse(s) for s in STATES)
f = round(F, 2); k = (1 - f * n) / (1 - n)
zones = {}
for s in STATES: zones[str(s)] = round(w[s] * f + (1 - w[s]) * k, 4)
for z in NORTH_REGIONS: zones[str(z)] = f
for z in range(3, 60):
    if z not in STATES and z not in NORTH_REGIONS: zones[str(z)] = round(k, 4)
mod = {'id': 'regional-beef-output', 'label': 'Beef output per animal lower in northern Australia (ABARES survey)', 'line': 'improved',
       'description': f"The model gives every zone the national meat production in proportion to its dry sheep equivalents, so beef output per animal is the same in the tropical north and the temperate south. The ABARES beef farm survey measures it: live weight of cattle produced per head of herd in 2014-15 was 156 kg on northern farms (227 tonnes a farm, 1,453 head) and 188 kg on southern farms (75 tonnes, 400 head), a ratio of {F:.2f}; turn-off rates (31 to 38% against 41 to 47%) and branding rates (70% against 86 to 89%) point the same way. The module multiplies the cattle meat yield of the northern zones (Queensland and its regions, the Northern Territory, the WA Rangelands and WA in proportion {w[49]:.2f}) by {f} and the southern zones by {k:.3f}, so that national beef is unchanged ({n:.1%} of the national beef dry sheep equivalents are northern). The Australian figure does not change; the southern state and regional figures rise and the northern ones are unchanged where cropland, not pasture, sets their capacity.",
       'yieldFactors': [{'row': 98, 'label': 'Cattle meat (g/m2)', 'zones': zones}],
       'errata': ["The ratio is one year of one survey (2014-15; standard errors 5% on the live weight, 4% on the herd). Turn-off ratios of 0.74 to 0.81 and the factor's own error give a plausible range of 0.74 to 0.90; the sensitivity in analysis/pasture_2025 spans 0.6 to 0.85.",
                  "Live weight produced per head compares the herd of a beef farm; the model's allocation is per beef dry sheep equivalent. Northern cattle are older and lighter at sale and stocking is half the southern rate, so the factor does not capture differences in land productivity per hectare except through the animals.",
                  "ABARES counts all of Queensland as northern; south-east Queensland is temperate and contributes a small share of the beef. Within the WA Rangelands and the Kimberley and Pilbara there is no finer split.",
                  "The Northern Territory's live exports and interstate sales are inside the producing farms' output; the model has no information on where the animals are finished.",
                  "Sheep and wool are unchanged: wool per dry sheep equivalent by state of the farm is within 7% of the nation for the large wool states (analysis/pasture_2025)."]}
os.makedirs(os.path.join(ROOT, 'methods/regional-beef-output'), exist_ok=True)
json.dump(mod, open(os.path.join(ROOT, 'methods/regional-beef-output/method.json'), 'w'), indent=2)
print('f', f, 'k', round(k, 3), 'northern share of beef DSE', round(n, 3), 'WA weight', round(w[49], 3))
