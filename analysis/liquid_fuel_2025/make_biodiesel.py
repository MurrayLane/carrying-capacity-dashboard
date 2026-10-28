#!/usr/bin/env python3
"""Writes methods/biodiesel-yield/method.json and the releases 2011-biodiesel and 2025-biodiesel that apply it (SCOPE.md E17).
Usage: python3 analysis/liquid_fuel_2025/make_biodiesel.py          (repository root)

The model's biodiesel yield from oilseeds (Base!K336:K344, grams of biodiesel per gram of feedstock) is oil content x 0.352, where 0.352 is the thesis workbook's '400 litres per tonne of input' times 0.00088 tonnes per
litre (archive: prelim models/non-food resource data.xls, sheet biofuel, columns 'lt fuel / tonne input', 'tonne fuel / tonne input', 'Initial processing yield'). 400 litres per tonne is what a tonne of canola SEED gives
(Manitoba costing model: 32% net oil extraction, about 353 litres of biodiesel per tonne of seed), so multiplying again by the oil content counts the oil twice; if 400 was meant per tonne of OIL it is a third of the
yield of the reaction (about 1,100 litres per tonne of oil). Either way canola's 14.8% (thesis appendix table) is about half of the 31% the same model of the seed gives. The module replaces each oilseed's yield by
oil content x 0.737, the product of the net recovery of oil from seed (0.76, canola, Manitoba) and the mass yield of transesterification (0.97), so that canola gives 0.31 tonnes of biodiesel per tonne of seed."""
import json, os
ROOT = os.getcwd()
OIL = {336: ('canola seed', 0.42), 337: ('olive', 0.18), 338: ('macadamia (unshelled)', 0.17), 339: ('grape', 0.28497109704641355), 340: ('linseed', 0.35021097046413496),
       341: ('sesame', 0.47), 342: ('sunflower', 0.405), 343: ('soy bean (whole)', 0.185), 344: ('peanut', 0.31)}
cells = {f'K{r}': f'={oil}*0.76*0.97' for r, (_, oil) in OIL.items()}
mod = {'id': 'biodiesel-yield', 'label': 'Biodiesel yield from oilseeds: oil content counted once', 'line': 'improved',
       'description': "A correction to the method, not to data. The workbook's biodiesel yield from each oilseed (Base!K336:K344) is the oil content times 0.352, the thesis's 400 litres of biodiesel per tonne of input times 0.00088 tonnes a litre. 400 litres is what a tonne of canola seed gives, so the oil content is counted twice: canola yields 14.8% of its mass as biodiesel in the model against about 31% (Manitoba costing model: 32% of seed mass recovered as oil, 97% conversion, about 353 litres a tonne). The module sets each oilseed's yield to its oil content times 0.76 (net recovery of oil from seed) times 0.97 (mass yield of transesterification). Ethanol is unchanged (its workings are per tonne of sugar and of grain, with the cane-to-sugar step separate). Biodiesel is 45% of the fuel and most of the land the model charges for fuel.",
       'cellOverrides': {'Base': cells},
       'errata': ["The recovery of 0.76 is the Manitoba figure for canola, applied to every oilseed; olive and grape are pressed with different recoveries, and the thesis oil contents are kept.",
                  "The module does not change the mix of feedstocks (canola 20%, then olive, macadamia, grape, linseed, sesame, sunflower, soy and peanut at 10% each, which are mostly low-yielding or high-value food oils); a mix of canola and sunflower would use far less land (analysis/liquid_fuel_2025/README.md).",
                  "Not checked against the original source of the 400 litres per tonne; the thesis text gives the biodiesel density (0.88) but not the yield source."]}
os.makedirs(os.path.join(ROOT, 'methods/biodiesel-yield'), exist_ok=True); json.dump(mod, open(os.path.join(ROOT, 'methods/biodiesel-yield/method.json'), 'w'), indent=2)
rels = {'2025-biodiesel': ('2025-fuel', 'Alternate: 2025 data, thesis method, biodiesel yield corrected', "An alternate to 2025-fuel, not a later layer: the data are those of 2025-fuel and the change is the method module biodiesel-yield (methods/biodiesel-yield/method.json; analysis/liquid_fuel_2025/README.md). The long term changes by far the most (the short term only through its 0.23% biofuel share)."),
        '2011-biodiesel': ('2011-corrected', 'Alternate: 2011 data, thesis method, biodiesel yield corrected', "An alternate to 2011-corrected: the 2011 data and zones with the method module biodiesel-yield. It shows what the thesis's long-term result would have been with the oilseed yield counted once. The long term changes by far the most (the short term only through its 0.23% biofuel share).")}
idx = json.load(open(os.path.join(ROOT, 'releases/index.json')))
for rid, (parent, label, desc) in rels.items():
    os.makedirs(os.path.join(ROOT, f'releases/{rid}'), exist_ok=True)
    json.dump({'id': rid, 'label': label, 'status': 'current', 'extends': parent, 'methods': ['biodiesel-yield'], 'description': desc}, open(os.path.join(ROOT, f'releases/{rid}/release.json'), 'w'), indent=2)
    idx['order'] = [i for i in idx['order'] if i != rid]
    anchor = '2025-fuel-ev' if rid.startswith('2025') else '2011-improved'; idx['order'].insert(idx['order'].index(anchor) + 1, rid)
json.dump(idx, open(os.path.join(ROOT, 'releases/index.json'), 'w'), indent=2); print(idx['order'][:10])
