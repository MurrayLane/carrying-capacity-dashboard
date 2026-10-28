#!/usr/bin/env python3
"""Writes README.md of this folder from capacity_by_cause.csv (run decompose.mjs first).   python3 -I write_readme.py   (from this folder)"""
import csv
r = list(csv.DictReader(open('capacity_by_cause.csv')))
names = {'1': 'Australia', '2': 'NSW-ACT', '15': 'Victoria', '26': 'Queensland', '40': 'South Australia', '49': 'Western Australia', '56': 'Tasmania', '60': 'Northern Territory'}
f = lambda x, k: f"{int(x[k]):,}"
def table(p):
    out = ['| Zone | 2011 | land only | crop yields only | livestock only | consumption only | organic update only | resilience table only | fuel only | all 2025 | people 2011 | people 2025 | people / capacity 2011 | 2025 |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for x in r:
        if x['preset'] == p and x['zone'] in names:
            out.append(f"| {names[x['zone']]} | {f(x,'capacity_2011')} | {f(x,'land_only')} | {f(x,'crop_yields_only')} | {f(x,'livestock_only')} | {f(x,'consumption_only')} | {f(x,'organic_update_only')} | {f(x,'resilience_update_only')} | {f(x,'fuel_update_only')} | {f(x,'all_2025')} | {f(x,'population_2011')} | {f(x,'population_2025')} | {x['population_over_capacity_2011']} | {x['population_over_capacity_2025']} |")
    return '\n'.join(out)
a = {p: next(x for x in r if x['zone'] == '1' and x['preset'] == p) for p in ('short', 'long')}
m = lambda p, k: int(a[p][k]) / 1e6
d = lambda p, k: (int(a[p][k]) - int(a[p]['capacity_2011'])) / 1e6
s = f'''# What changed carrying capacity between the 2011 data and the 2025 data

SCOPE.md D4. `decompose.mjs` applies each cause alone to the 2011 data and then all together (release `2025-fuel`, the tip of the 2025 chain); the full table, both presets and all 60 zones, is `capacity_by_cause.csv`; this file is written from it by `write_readme.py`.
The method and the diet's food-group detail are the 2011 ones throughout, so each column is a data effect. Consumption means five of the six short-term defaults of `analysis/consumption_2025/` (meat and egg share, red meat share, fuel, biofuel,
timber); the long-term settings are scenarios, but two have been updated: the resilience table behind the 100-year setting (`analysis/resilience_2025/`) and the long-term liquid fuel (`analysis/fuel_sectors_2025/`), each a column of its own. The organic update (E5, `analysis/organic_2025/`) is its own column: the organic share and its baseline constant, and new factors for five crops. Population does not enter capacity; it changes whether a zone is over or under its capacity, shown in the last two columns (people divided by
capacity: above 1 is over capacity).

## Short-term settings (today's diet and production)

{table('short')}

## Long-term settings

{table('long')}

## Reading it

* **Short term, Australia: {m('short','capacity_2011'):.1f} to {m('short','all_2025'):.1f} million.** Less pasture on holdings (the ABS grazing area fell 9%, partly a change of its land-use categories) takes {-d('short','land_only'):.1f} million off. Crop yields add {d('short','crop_yields_only'):.1f} million: crops hardly bind the
  short-term result. Livestock adds {d('short','livestock_only'):.1f} million: red meat is more than four fifths of the land in the short-term diet, and the cattle and sheep meat produced per animal and per hectare of grazing rose. Consumption adds
  {d('short','consumption_only'):.1f} million: Australians eat less beef (down a third a head) and slightly less meat overall. The causes do not add up (interaction {int(a['short']['interaction'])/1e6:.1f} million) because they act on the same land.
* **Long term, Australia: {m('long','capacity_2011'):.1f} to {m('long','all_2025'):.1f} million.** Crop yields are the largest cause: {d('long','crop_yields_only'):.1f} million of the {d('long','all_2025'):.1f} million. Wheat, barley and canola yields roughly doubled against the drought years of 2006-2010, and the long-term
  diet is cropping-land limited. Land adds {d('long','land_only'):.1f} million; the organic update changes the long-term result by {d('long','organic_update_only'):+.2f} million (the long-term diet is 100% organic); the resilience table, updated to 2024-25, by {d('long','resilience_update_only'):+.2f} million (on the 2011 data; Australia's 100-year factor is unchanged, the states differ); the re-derived long-term fuel (210 L, the thesis method on current sector use) by {d('long','fuel_update_only'):+.2f} million; livestock and consumption do nothing here (the long-term settings are scenarios).
* **Population {int(a['short']['population_2011'])/1e6:.1f} to {int(a['short']['population_2025'])/1e6:.1f} million.** Today's population is {float(a['short']['population_over_capacity_2011'])*100:.0f}% of the short-term capacity in 2011 and {float(a['short']['population_over_capacity_2025'])*100:.0f}% now; against the long-term capacity it is {a['long']['population_over_capacity_2011']} times in 2011 and {a['long']['population_over_capacity_2025']} times now.
* **Caveats that matter more than the third digit.** Three years of crop data (2022-25), two of them very good winter-crop years; a five-year meat window that ends in two years of heavy slaughter; wool, milk and feedlot
  grain placeholders; vegetables, fruit and nuts carried at their 2016-21 group factor; the five zones of older boundaries (`analysis/land_2011/README.md`); organic share the least certain default. Each has been re-run with
  the alternative choice: `analysis/sensitivity_2025/README.md` ranks the effects.
'''
open('README.md', 'w').write(s)
