#!/usr/bin/env python3
"""Writes analysis/long_term_2025/README.md from levers.csv, fuel_grid.csv and resilience_curve.csv.   Usage: python3 analysis/long_term_2025/write_readme.py (repository root)"""
import csv
L = [r for r in csv.DictReader(open('analysis/long_term_2025/levers.csv'))]
au = [r for r in L if r['zone'] == '1']; S = float(au[0]['alone']); LT = float(au[1]['alone'])
lever_rows = '\n'.join(f"| {r['lever']} | {float(r['alone']) / 1e6:.1f} ({float(r['alone']) / S * 100 - 100:+.0f}%) | {float(r['without']) / 1e6:.1f} ({float(r['without']) / LT * 100 - 100:+.0f}%) |" for r in au[2:-2])
res = {z: [r for r in L if r['zone'] == z] for z in ('1', '2', '15', '26', '40', '49', '56', '60')}
NAME = {'1': 'Australia', '2': 'NSW and ACT', '15': 'Victoria', '26': 'Queensland', '40': 'South Australia', '49': 'Western Australia', '56': 'Tasmania', '60': 'Northern Territory'}
def resv(z):
    rows = res[z]; base = float(rows[1]['alone']); d = float(rows[-2]['alone']); alt = float(rows[-1]['alone'])
    return f"| {NAME[z]} | {d / 1000:,.0f} | {base / 1e6:.2f} | {alt / 1e6:.2f} | {alt / base * 100 - 100:+.1f}% |"
reserve = '\n'.join(resv(z) for z in res)
grid = list(csv.DictReader(open('analysis/long_term_2025/fuel_grid.csv'))); fuels = sorted({int(r['fuel_litres']) for r in grid}); bios = [1.0, 0.5, 0.3, 0.1]
g = {(int(r['fuel_litres']), float(r['biofuel_share'])): float(r['capacity']) / 1e6 for r in grid}
fuel_tab = '| Liquid fuel per person (L) | ' + ' | '.join(f'{int(b * 100)}% biofuel' for b in bios) + ' |\n|---|' + '---|' * len(bios) + '\n' + '\n'.join(f'| {f} | ' + ' | '.join(f'{g[(f, b)]:.1f}' for b in bios) + ' |' for f in fuels)
rc = list(csv.DictReader(open('analysis/long_term_2025/resilience_curve.csv'))); r1 = float(rc[0]['capacity'])
res_tab = '| Years of recurrence | ' + ' | '.join(r['resilience_years'] for r in rc) + ' |\n|---|' + '---|' * len(rc) + '\n| Capacity (million) | ' + ' | '.join(f"{float(r['capacity']) / 1e6:.1f}" for r in rc) + ' |\n| Share of the 1-year figure | ' + ' | '.join(f"{float(r['capacity']) / r1 * 100:.0f}%" for r in rc) + ' |'
RES = {int(r['zone']): r for r in csv.DictReader(open('analysis/long_term_2025/reserve_release.csv'))}
rel_tab = '| Zone | Short term: 2025-resilience | 2025-reserve | Long term: 2025-resilience | 2025-reserve | Change |\n|---|---|---|---|---|---|\n' + '\n'.join(
    f"| {NAME[str(z)]} | {int(r['short_resilience']) / 1e6:.2f} | {int(r['short_reserve']) / 1e6:.2f} | {int(r['long_resilience']) / 1e6:.2f} | {int(r['long_reserve']) / 1e6:.2f} | {(int(r['long_reserve']) / int(r['long_resilience']) - 1) * 100:+.1f}% |" for z, r in RES.items())
s = f'''# The long-term settings: what each is worth, and what could be improved

Release `2025-organic`, Australia, long-term settings: **{LT / 1e6:.1f} million** (today's settings: {S / 1e6:.1f}). The long-term settings are not a forecast. They ask what the land could support if the country planned to be self-sufficient for 100 years of weather,
with a low-meat diet, no avoidable food waste, full nutrient recycling, organic farming, almost no fossil liquid fuel and 30% of the land in reserve. Reproduce: `node analysis/long_term_2025/long_term_levers.mjs analysis/long_term_2025/levers.csv`, then `python3 analysis/long_term_2025/write_readme.py`.

## What each setting is worth (Australia)

"Alone": the short-term settings with only this long-term setting switched on. "Without": the long-term settings with only this one put back to its short-term value. Millions of people (change against the {S / 1e6:.1f} and {LT / 1e6:.1f} baselines).

| Setting (short to long value) | Alone | Without |
|---|---|---|
{lever_rows}

Timber, infrastructure area and the 30% reserve target change nothing for Australia as a whole (non-agricultural land absorbs them, see below), and the dietary meat share matters less than the headline settings.
**The largest are** the 100-year resilience setting (without it the long term would be {float(au[2]['without']) / 1e6:.1f} million), the pair of liquid fuel and biofuel (they act together: see section 2), organic farming, activity level 3, no avoidable waste and full recycling.
The settings are a mix: demanding on resilience, biofuel, activity and organic farming (each lowers capacity), generous on fuel, waste and recycling (each raises it). The long-term figure answers one specific scenario, and the mix has not been checked for coherence.

## 1. The resilience setting is a statistical estimate, and it is the largest lever

{res_tab}

The setting scales the whole harvest by a factor read from a table (the `resilience` sheet of the workbook). The thesis (chapter 8, Figure 34) built it from the ABS yields of wheat, oats and barley for Australia and each state from 1861 (about 150 years): each year's average grain yield divided by its ten-year moving average,
the years ranked from worst to best, and the rank read as a return period (the worst year in 150 is a one-in-150-year event). For Australia the worst year, 1915, gave 36% of the moving average; the factor at 100 years is 0.46.
This is the most statistical part of the model and the least examined. What could be done:

* **Update the series** with the 15 years since the thesis, which include the 2018-19 drought and the record 2022-23 harvest. The ABS series (7124.0) ended with the 2010-11 edition; later years would have to be stitched from the ABS and ABARES crop data.
* **Use a fitted distribution, not a rank.** A one-in-100 event estimated as about the second-worst of 150 values has a wide uncertainty that the table hides. Fit an extreme-value distribution and report an interval (the capacity at 100 years could be given as a range).
* **Detrend properly.** A ten-year moving average is itself pulled down by droughts and up by booms; a smooth trend would give cleaner deviations. Early years (1915: 0.3 against 0.8 t/ha) reflect the farming practices and the marginal land of the time, which may not recur. Test whether variability has changed.
* **Cover more than three grains**, and pasture and livestock, which the factor also scales.
* **Droughts last several years.** Self-reliance means surviving a run of bad years (the 2001-09 drought, the 1895-1903 drought), not one. A factor for a single year ignores storage and carry-over.
* **Regional zones use their state's curve**, so a small region's variability is understated.
Consistency check with the year-by-year runs (`analysis/reliability_2025/`): the worst of eight recent years gives a long-term capacity about 85% of their mean, about a one-in-eight year; the table gives 0.87 at five years and 0.74 at ten. Recent years do not contradict the table.

## 2. Liquid fuel and biofuel

The long-term settings assume 253 L of liquid fuel a person (a tenth of today's 2,520 L) and that all of it is biofuel grown on the land. Millions of people, Australia:

{fuel_tab}

Capacity is very sensitive to this pair, and since the model charges land only for biofuel it depends on litres of biofuel a person (fuel times share). The 253 L is the thesis's designed scenario of a fossil-fuel-free, low-consumption society: each sector of 2008 use is cut (road and most industry by 90%, mining by 95%, air travel to almost nothing, agriculture by 20%), see `analysis/liquid_fuel_2025/README.md`, which also sets it against measured use since 2011 and published projections (residual liquid fuel in 2050 of 840 to 1,700 L a person for the present economy, with electric vehicles removing petrol but not diesel and jet fuel).

## 3. Where the extra reserve comes from

The 30% reserve target is {float(res['1'][-2]['alone']) / 1000:,.0f} thousand km2 more than the existing reserve in Australia. The model takes reserve and infrastructure land from non-agricultural land first (the arid rangelands), so for Australia this costs nothing.
If instead it came from pasture and cropping in proportion (an "ecologically representative" reserve, in the sense of the Kunming-Montreal framework's Target 3, which asks for protected areas that are ecologically representative; this is from search results, not read in full):

| Zone | Reserve deficit (thousand km2) | Long term, model's rule (million) | Taken from pasture and cropping (million) | Change |
|---|---|---|---|---|
{reserve}

**Published as the alternate release `2025-reserve`** (an alternate of `2025-resilience`, three formulas changed in Settings!C55:E55, `make_release_reserve.py`): any shortfall of reserve and infrastructure land is shared by cropping, pasture and non-agricultural land in proportion to their areas. This is gentler than the table above, which put the whole shortfall on pasture and cropping.

{rel_tab}

The short term moves by about 1% in Australia only because the short-term reserve setting is the raster share rounded to a whole percent (0.26 against 0.256), which makes a small shortfall. The long-term fall (Australia {(int(RES[1]['long_reserve']) / int(RES[1]['long_resilience']) - 1) * 100:.0f}%, New South Wales and Queensland about 22%) comes from the 30% target exceeding the existing reserve. Arid land counted as equal to farmland makes the alternate generous; a reserve weighted toward the productive east and south-west would cost more.

Where the reserve comes from is a large, silent assumption. In the regional zones the reserve and infrastructure settings already change capacity (23 of 60 zones in the short term, 18 in the long term).

## 4. The other long-term settings

* **Avoidable waste 0%** (today 12%, a US figure, SCOPE.md E4) and **recycling 100%**: both extreme. I believe Australia's strategy aims to halve food waste by 2030 (the global target is to halve it; I did not find the Australian document); a ladder of 0%, 50% and the baseline would show what is realistic.
* **Organic 100%** costs {(1 - LT / float([r for r in au if r['lever'].startswith('organic')][0]['without'])) * 100:.0f}% of the long-term figure, by the update's factors (Ponisio et al. 2015, Kniss et al. 2016); the nitrogen supply an all-organic system needs (legume rotations, recycling) is not modelled (SCOPE.md E6).
* **Activity level 3** (the most active) adds 12% to the energy needed; it is a population-health assumption, not a physical one, and should be stated as such.
* **Diet**: 7.5% meat and eggs with half of it red meat is a moderate change from today (12%, 58%), not a vegetarian diet. A named reference diet (Australian Dietary Guidelines, or the EAT-Lancet reference diet) with item-level foods would let the long-term diet be checked against nutrition (SCOPE.md E7).
* **Yields are today's.** For a 100-year horizon the yields do not respond to climate change, water limits or soil and nutrient decline (SCOPE.md E2, E3).
'''
open('analysis/long_term_2025/README.md', 'w').write(s)
