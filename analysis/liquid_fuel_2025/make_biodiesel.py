#!/usr/bin/env python3
"""Writes methods/biodiesel-yield/method.json (SCOPE.md E17). It is a correction, listed in CORRECTIONS of analysis/comparison_2025/make_cells.py, which writes the releases that apply it (2011-fixed, 2025-fixed, and the improved cells that build on them).
Usage: python3 analysis/liquid_fuel_2025/make_biodiesel.py          (repository root)

The model's biodiesel yield from oilseeds (Base!K336:K344, grams of biodiesel per gram of feedstock) is oil content x 0.352, where 0.352 is the thesis workbook's '400 litres per tonne of input' times 0.00088 tonnes per
litre (archive: prelim models/non-food resource data.xls, sheet biofuel, columns 'lt fuel / tonne input', 'tonne fuel / tonne input', 'Initial processing yield').
THE SOURCE OF THE 400 (found 2026-10-28 in the archive's 'references re production yields/Non-food'): ABARE, Australian Energy Resource Assessment 2009, chapter 12, Table 12.12 (p. 331, from O'Connell et al. 2009b):
'Oilseeds, biodiesel 400 L/t' and the text 'Current technologies can produce 280 to 560 litres of ethanol per tonne of biomass and 400 litres of biodiesel per tonne of oilseeds'; the same table is Table 10-3 of the CSIRO
Rural Land Use greenhouse gas analysis and the conversion factor of CSIRO's 'Biofuels in Australia', which multiplies it directly by the tonnes of oilseed crops produced (2,533 kt x 400 L/t = 1,013 ML).
So 400 litres is per tonne of SEED; the workbook multiplies it by the oil content again (canola 0.42), counting the oil twice. The module keeps the source's 400 litres a tonne for canola (0.352 t/t) and scales the other oilseeds by
their oil content relative to canola's, K = 0.352 x oil content / 0.42, so canola gives 0.352 instead of 0.148."""
import json, os
ROOT = os.getcwd()
OIL = {336: ('canola seed', 0.42), 337: ('olive', 0.18), 338: ('macadamia (unshelled)', 0.17), 339: ('grape', 0.28497109704641355), 340: ('linseed', 0.35021097046413496),
       341: ('sesame', 0.47), 342: ('sunflower', 0.405), 343: ('soy bean (whole)', 0.185), 344: ('peanut', 0.31)}
cells = {f'K{r}': f'=0.352*{oil}/0.42' for r, (_, oil) in OIL.items()}
mod = {'id': 'biodiesel-yield', 'label': 'Biodiesel yield from oilseeds: oil content counted once', 'line': 'improved',
       'description': "A correction to the method, not to data. The workbook's biodiesel yield from each oilseed (Base!K336:K344) is the oil content times 0.352, the thesis's 400 litres of biodiesel per tonne of input times 0.00088 tonnes a litre. The source of the 400 is ABARE's Australian Energy Resource Assessment 2009 (chapter 12, Table 12.12, from O'Connell et al. 2009b; also CSIRO's Rural Land Use greenhouse gas analysis, Table 10-3, and Biofuels in Australia), where it is 400 litres of biodiesel per tonne of OILSEEDS, applied to the tonnes of seed produced. The workbook multiplies it by the oil content again (canola 0.42), so the oil is counted twice and canola yields 14.8% of its mass as biodiesel in the model against 35.2% in the source. The module keeps the source's 400 litres a tonne for canola and scales the other oilseeds by their oil content relative to canola's (K = 0.352 x oil content / 0.42). Ethanol is unchanged (its workings are per tonne of sugar and of grain, with the cane-to-sugar step separate, as in the same table). Biodiesel is 45% of the fuel and most of the land the model charges for fuel.",
       'cellOverrides': {'Base': cells},
       'errata': ["The source gives one figure for all oilseed crops (400 litres a tonne, an average weighted to canola); scaling the other oilseeds by oil content relative to canola's is the thesis's own approach to differences between crops and is kept, so olive, macadamia and soy are lower than 400.",
                  "The module does not change the mix of feedstocks (canola 20%, then olive, macadamia, grape, linseed, sesame, sunflower, soy and peanut at 10% each, which are mostly low-yielding or high-value food oils); a mix of canola and sunflower would use far less land (analysis/liquid_fuel_2025/README.md). The same sources list tallow (894 litres a tonne) and waste cooking oil (870), which need no land."]}
os.makedirs(os.path.join(ROOT, 'methods/biodiesel-yield'), exist_ok=True); json.dump(mod, open(os.path.join(ROOT, 'methods/biodiesel-yield/method.json'), 'w'), indent=2)
print('wrote methods/biodiesel-yield/method.json')
