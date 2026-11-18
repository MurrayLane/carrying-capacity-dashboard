#!/usr/bin/env python3
"""Every 2011 zone population on the ABS footing (decision 100, brief B110; ERRATA.md errors 9 and 10).
Usage (repository root): python3 -I analysis/population_2011/zone_populations_2011.py
Reads: analysis/population_2011/zone_population_2011.csv (column erp_2011_sa2_route: the ABS estimated resident population at 30 June 2011 by SA2,
sources register D31, allocated to the 2011 NRM zones as the 2025 population is; written by ne_vic_population.py), data/2011/default-inputs-short-term.csv
(the thesis's land and population per zone) and results/2011-fixed-2.csv (the corrected release the comparison is made against).
Writes: analysis/population_2011/zone_population_2011_comparison.csv (zone; the 2011-fixed-2 figure; the ABS figure; difference; percent of the ABS figure)
and methods/zone-population-2011/method.json (zoneInputs for all 53 regions, the 52 NRM regions and the Northern Territory: population set to the ABS figure,
infrastructure at the 2011 land method's 730 m2 a person, rounded to the km2 as in the default inputs, non-agricultural land the remainder, total area unchanged).
The national row (22,326,388) is not touched; state rows are the sum of their regions through state-population-sum, which the releases already apply.
Deterministic: no randomness, no network, sorted output."""
import csv, json, os

RATE = 730   # m2 of infrastructure a person: the 2011 land method (analysis/land_2011/README.md) and the model's infrastr2 default
STATE_OF = {**{z: 2 for z in range(3, 15)}, **{z: 15 for z in range(16, 26)}, **{z: 26 for z in range(27, 40)}, **{z: 40 for z in range(41, 49)},
            **{z: 49 for z in range(50, 56)}, **{z: 56 for z in range(57, 60)}, 60: 60}
rd = lambda p: list(csv.DictReader(open(p)))
erp = {int(r['zone']): int(r['erp_2011_sa2_route']) for r in rd('analysis/population_2011/zone_population_2011.csv')}
names = {int(r['zone']): r['name'] for r in rd('analysis/population_2011/zone_population_2011.csv')}
old = {int(r['regionId']): r for r in rd('data/2011/default-inputs-short-term.csv')}
rel = {int(r['zone']): int(r['population']) for r in rd('results/2011-fixed-2.csv') if r['preset'] == 'short'}
assert sorted(erp) == sorted(STATE_OF), 'the 53 regions'
for z, o in old.items():   # the rule the module relies on holds in every one of the 60 zones of the default inputs
    assert int(o['infrastr1']) == round(int(o['population']) * RATE / 1e6), f'zone {z}: infrastructure is not population x {RATE} m2'

rows = [['zone', 'name', 'state', 'population_2011_fixed_2', 'abs_erp_2011_sa2_route', 'difference', 'percent_of_abs', 'note']]
for z in sorted(erp):
    d = rel[z] - erp[z]
    note = 'error 8: corrected in 2011-fixed-2 (was 204,651, a copy of zone 19)' if z == 22 else (
           'error 9: shares 230,982 with zone ' + ('39' if z == 33 else '33') if z in (33, 39) else '')
    rows.append([z, names[z], STATE_OF[z], rel[z], erp[z], d, '%.1f' % (100 * d / erp[z]), note])
csv.writer(open('analysis/population_2011/zone_population_2011_comparison.csv', 'w', newline='')).writerows(rows)

zi = {}
for z in sorted(erp):
    o = old[z]; pop = erp[z]; inf = round(pop * RATE / 1e6); non = int(o['nonAg']) + int(o['infrastr1']) - inf
    assert non >= 0, f'zone {z}: non-agricultural land would be negative'
    zi[str(z)] = {'population': pop, 'infrastr1': inf, 'nonAg': non}
tot_rel, tot_erp = sum(rel[z] for z in erp), sum(erp.values())
mod = {
  'id': 'zone-population-2011',
  'label': "Every 2011 regional population set to the ABS estimate (30 June 2011, SA2 route)",
  'line': 'improved',
  'description': ("A correction to the data, not to the method (error 10 of ERRATA.md; it also settles error 9). The thesis's 2011 regional populations "
                  "(thesis Table 25, p. 382; section 8.5, p. 221: 'sourced predominantly from journal articles', footnote 912 citing Robins and Dovers 2007) have no recorded "
                  "source, reference date or allocation, and two pairs of zones carry one figure to the person (errors 8 and 9). The module sets each of the 53 regions "
                  "(the 52 NRM regions and the Northern Territory) to the ABS estimated resident population at 30 June 2011 by SA2 (sources register D31), allocated to the "
                  "2011 NRM zones exactly as the 2025 population is (analysis/population_2011/ne_vic_population.py, zone_population_2011.csv), so 2011 and 2025 are like for like. "
                  f"Infrastructure follows at the 2011 land method's {RATE} m2 a person (rounded to the km2, as in the default inputs) and non-agricultural land takes the "
                  "difference, so each zone's total area is unchanged. It is applied before state-population-sum, so each state's population is the sum of its regions. "
                  f"The national row (22,326,388) is not changed, as error 6 and error 8 left it; the 53 regions now sum to {tot_erp:,}."),
  'zoneInputs': zi,
  'errata': [
    "Error 10 of the error register (ERRATA.md); also closes error 9 (Fitzroy and Wet Tropics) without deciding which zone carried the copy. Zone 22 is set to the same 98,604 as north-east-vic-population.",
    "Capacity does not depend on the population input; the infrastructure area moves capacity only where a module shares the reserve and infrastructure shortfall (reserve-pro-rata, improved tier).",
    f"The national population (22,326,388) is left as it is: a published input, kept as errors 6 and 8 kept it (B90 decision 2; qa/reports/R03a_response_plan_A.md issue 1); the 53 regions sum to {tot_erp:,}, {tot_erp - 22326388:+,} against it."
  ]
}
os.makedirs('methods/zone-population-2011', exist_ok=True)
open('methods/zone-population-2011/method.json', 'w').write(json.dumps(mod, indent=2, ensure_ascii=False) + '\n')
print(f'53 regions: 2011-fixed-2 {tot_rel:,}; ABS {tot_erp:,}; difference {tot_rel - tot_erp:+,}')
big = [r for r in rows[1:] if abs(float(r[6])) > 10]
print(f'regions more than 10% from the ABS figure: {len(big)}; ratio outside 0.8 to 1.25: {sum(1 for r in rows[1:] if not 0.8 <= r[3] / r[4] <= 1.25)}')
print('wrote analysis/population_2011/zone_population_2011_comparison.csv and methods/zone-population-2011/method.json')
