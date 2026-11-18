#!/usr/bin/env python3
"""Reference-period table for Paper A section 2 (B138 item 1; R05a issue 1; R04a 3.1 question 1 and minors 4 to 6; decisions 138 and 140).

For each input layer: the data years it uses in 2011 and in 2025, the population date (30 June ERP) and the gap in years, the ERP vintage (sources register D31), and the midpoint-population check:
the national short-term capacity over the population at the midpoint of the layer's data window, from the ERP of D31 (data/sa2/population_erp.csv, 2,450 SA2 of the model, scaled to the release's own
population at the end year so that the allocation loss of D47 is carried the same way). The 2011 midpoints (about 2008) lie before the first ERP year held (30 June 2011): that column is left empty and the
fetch is listed in the report (qa/reports/B138_paper_A_smaller_computations.md); nothing is estimated.

Also writes reference_periods_national_row.csv: the national figures that depend on the Australia population row, on the thesis row 22,326,388 and on the regional sum 22,336,514 (decision 140). Capacity does
not move; only the ratio of capacity and population does. The seven state rows of 2011-fixed-3 sum the ABS regions, so no state figure moves on that release.

Usage (repository root): python3 -I analysis/population_2011/reference_periods.py     Writes reference_periods.csv and reference_periods_national_row.csv beside this file. Deterministic.
Window conventions: an ABS financial year Y runs 1 July Y-1 to 30 June Y, midpoint 1 January Y; a window of years a to b (financial years) has midpoint (a+b)/2 as a decimal year (2008.0 is 1 January 2008);
a calendar-year window y0 to y1 has midpoint (y0+y1)/2 + 0.5. ERP dates: 30 June of year Y is the decimal year Y + 0.5. The gap is the population date minus the window midpoint (and minus the window end).
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
rd = lambda p: list(csv.DictReader(open(os.path.join(REPO, p))))
model_sa2 = {r['sa2_code'] for r in rd('data/sa2/land_2011_method_by_sa2.csv')}
erp = {y: 0.0 for y in range(2011, 2026)}
for r in rd('data/sa2/population_erp.csv'):
    if r['sa2_code'] in model_sa2:
        for y in erp: erp[y] += float(r[str(y)] or 0)
res = {(r['release'], r['zone'], r['preset']): r for r in rd('results/2011-fixed-3.csv') + rd('results/2025-fixed.csv')}
cap = {(y, p): float(res[(rel, '1', p)]['capacity']) for y, rel in ((2011, '2011-fixed-3'), (2025, '2025-fixed')) for p in ('short', 'long')}
pop_release = {2011: 22336514.0, 2025: float(res[('2025-fixed', '1', 'short')]['population'])}      # 2011: the regional sum (decision 140); 2025: the allocated SA2 sum
scale = {2011: pop_release[2011] / erp[2011], 2025: pop_release[2025] / erp[2025]}


def pop_at(t, end_year):
    """population at decimal year t from the ERP of D31, scaled so that the end year equals the release population; None before 30 June 2011"""
    if t < 2011.5 - 1e-9: return None
    lo = int(t - 0.5); f = (t - 0.5) - lo; hi = min(lo + 1, 2025)
    v = erp[lo] * (1 - f) + erp[hi] * f if lo < 2025 else erp[2025]
    return v * scale.get(end_year, 1.0)


fy = lambda a, b: ((a + b) / 2, b + 0.5)                         # financial years a..b: midpoint, end (30 June b)
cy = lambda y0, y1: ((y0 + y1) / 2 + 0.5, y1 + 1.0)              # calendar years y0..y1: midpoint, end (31 December y1)
# (layer, input, 2011 text, 2011 midpoint, 2011 end, 2025 text, 2025 midpoint, 2025 end, source rows, note)
fy11, fy25 = fy(2006, 2010), fy(2021, 2025)
L = [
 ('population', 'Regional population (ERP)', '30 June 2011', 2011.5, 2011.5, '30 June 2025', 2025.5, 2025.5, 'D31; D47; R05a issue 1',
  'The same ABS flow for both years (ABS_ANNUAL_ERP_ASGS2021, 2021 SA2 boundaries). The 2011 regions sum to 22,336,514 (the ABS route, 2011-fixed-3); 2025 is the allocated SA2 sum 27,608,200, 304 below the ABS total of the same SA2.'),
 ('land', 'Cropland area (land mainly used for crops)', 'five years, 2005-06 to 2009-10 (mean)', *fy11, 'one year, 2020-21', *fy(2021, 2021), 'D52; analysis/land_2011/README.md', 'Sheet labels 2006 to 2010 are the financial years 2005-06 to 2009-10.'),
 ('land', 'Pasture area (total grazing)', 'four years, 2005-06, 2007-08, 2008-09, 2009-10 (mean; 2006-07 missing)', 2008.25, 2010.5, 'one year, 2020-21', *fy(2021, 2021), 'D52; analysis/land_2011/README.md', 'ABS changed its land-use categories in 2016, so part of the national pasture fall is a change of definition.'),
 ('land', 'Reserve and total area', 'ABARES CLUM raster, update December 2023 (mapping dates vary by state)', None, None, 'the same raster', None, None, 'D32; D33', 'One raster for both years: not dated to either window. Midpoints not defined.'),
 ('crop yields', 'Field-crop yields (12 crops)', 'five years, 2005-06 to 2009-10 (mean)', *fy11, 'three years, 2022-23 to 2024-25 (mean)', *fy(2023, 2025), 'D01 to D13; data/2025/yield_provenance.csv (455 observed cells)',
  'Supplementary Table S11 says 2006-07 to 2009-10 for 2011 (four years, the years the ABS archive still holds); the pipeline and the thesis average five, the 2005-06 cube being in the author archive (pipeline/yields/README.md, analysis/yield_conversion/README.md).'),
 ('crop yields', 'Vegetable, fruit and nut yields', 'five years, 2005-06 to 2009-10 (mean)', *fy11, 'the 2005-06 to 2009-10 regional pattern times a group factor from 2016-17 to 2020-21 (carried forward; no area published after 2020-21)', *fy(2017, 2021), 'data/2025/yield_provenance.csv; pipeline/yields/recent/README.md', 'Group-trend rule (SCOPE.md B10): about 5,000 of the 2025 yield cells.'),
 ('livestock', 'Meat, wool and milk output per hectare of grazing', 'five years, 2005-06 to 2009-10 (archive years 2006 to 2010; mean of yearly yields)', *fy11, 'five years, 2020-21 to 2024-25 (mean output) over the 2020-21 grazing area', *fy25, 'D49 to D51; pipeline/yields/archive_livestock_inputs.json; data/2025/livestock_national_series.csv',
  'This layer and the land layer are the ones that bind the short term (R05a issues 2 and 3).'),
 ('diet', 'Meat-and-egg share, red-meat share and red-meat split', 'thesis defaults; the FAO 2010-12 means sit close to them (14.5% and 61.3% against 13% and 64%)', *cy(2010, 2012), 'the 2011 defaults times the FAO change, 2010-12 to 2021-23', *cy(2021, 2023), 'D17; D23; analysis/consumption_2025/README.md', 'Food supply (availability), not intake. The 2025 value is a ratio on a base window, so the layer carries both windows.'),
 ('fuel', 'Liquid fuel per person', 'thesis default 2,520 L (year not recorded); proxy base year to June 2011', *fy(2011, 2011), 'year to June 2025 (sales per person, ratio to 2011)', *fy(2025, 2025), 'D35', 'A one-year ratio.'),
 ('weather', 'Weather allowance (resilience table)', 'thesis table, 138 observations (period not recorded here)', None, None, '153 seasons: ABS Historic Agricultural Commodities 1860 to 2022 and the 2022-23 to 2024-25 cubes', None, None, 'analysis/resilience_2025/README.md', 'A long record; midpoints not defined.'),
 ('organic', 'Organic share of farmland', 'draft paper of February 2016: about 12 million hectares certified (2%)', None, None, 'Australian Organic Market Report 2026 snapshot: 44.4 million hectares (7%)', None, None, 'analysis/consumption_2025/README.md', 'Reference years of the two organic areas are not stated in the project.'),
 ('scale curve', 'SA2, SA3, SA4 land and population for the scale curve', 'not used', None, None, 'SA2 land of the 2011 method on 2020-21 data; ERP of the release vintage year', *fy(2021, 2021), 'D52', 'Population is the ERP at the vintage year, as for the regions.'),
]
VINT = ('ABS ERP at 30 June, flow ABS_ANNUAL_ERP_ASGS2021 (2021 SA2 boundaries), file data/sa2/population_erp.csv dated 2026-10-27; the 2025 values agree with the ABS Regional population 2024-25 release of 31 March 2026 '
        '(V30a, 8 SA2 values and the 2024-25 growth); the release label of the file and its retrieval date are not recorded (D31)')
f2 = lambda v: '' if v is None else f'{v:.2f}'
rows = [['layer', 'input', 'data_years_2011', 'data_years_2025', 'window_midpoint_2011', 'window_midpoint_2025', 'window_end_2011', 'window_end_2025', 'population_date_2011', 'population_date_2025',
         'gap_midpoint_to_population_date_2011_years', 'gap_midpoint_to_population_date_2025_years', 'gap_end_to_population_date_2011_years', 'gap_end_to_population_date_2025_years', 'erp_vintage',
         'population_at_midpoint_2011', 'population_at_midpoint_2025', 'capacity_over_population_at_population_date_2011_short', 'capacity_over_population_at_midpoint_2011_short', 'capacity_over_population_at_population_date_2025_short',
         'capacity_over_population_at_midpoint_2025_short', 'capacity_over_population_at_midpoint_2025_long', 'capacity_over_population_at_population_date_2025_long', 'source_rows', 'note']]
for layer, inp, t11, m11, e11, t25, m25, e25, src, note in L:
    p11 = pop_at(m11, 2011) if m11 else None; p25 = pop_at(m25, 2025) if m25 else None
    rows.append([layer, inp, t11, t25, f2(m11), f2(m25), f2(e11), f2(e25), '30 June 2011 (2011.50)', '30 June 2025 (2025.50)',
                 f2(2011.5 - m11) if m11 else '', f2(2025.5 - m25) if m25 else '', f2(2011.5 - e11) if e11 else '', f2(2025.5 - e25) if e25 else '', VINT,
                 '' if p11 is None else round(p11), '' if p25 is None else round(p25), round(cap[(2011, 'short')] / pop_release[2011], 4), '' if p11 is None else round(cap[(2011, 'short')] / p11, 4),
                 round(cap[(2025, 'short')] / pop_release[2025], 4), '' if p25 is None else round(cap[(2025, 'short')] / p25, 4), '' if p25 is None else round(cap[(2025, 'long')] / p25, 4), round(cap[(2025, 'long')] / pop_release[2025], 4), src, note])
with open(os.path.join(HERE, 'reference_periods.csv'), 'w', newline='') as f: csv.writer(f).writerows(rows)

# ---- the national 2011 row: thesis 22,326,388 against the regional sum 22,336,514 ----
OLD, NEW = 22326388.0, 22336514.0
shocks = {(r['release'], r['return_period']): r for r in rd('analysis/paper_a/shocks_by_region-3.csv') if r['zone'] == '1'}
nat = [['figure', 'claim_rows', 'tier', 'capacity', 'population_before', 'population_after', 'value_before', 'value_after', 'rounded_before', 'rounded_after', 'moves_at_printed_precision']]


def add(label, claims, tier, c, digits, kind='ratio', num=None):
    b, a = (c / OLD, c / NEW) if kind == 'ratio' else (None, None)
    if kind == 'growth': b, a = pop_release[2025] / OLD - 1, pop_release[2025] / NEW - 1
    if kind == 'over': b, a = OLD / c, NEW / c
    rb, ra = round(b, digits), round(a, digits)
    nat.append([label, claims, tier, round(c) if c else '', int(OLD), int(NEW), f'{b:.6f}', f'{a:.6f}', rb, ra, 'yes' if rb != ra else 'no'])


c11s, c11l = cap[(2011, 'short')], cap[(2011, 'long')]
add('short-term capacity over population, 2011, average year', 'A005; A163', 'A', c11s, 2)
add('short-term capacity over population, 2011, average year, three decimals', 'A005 (note)', 'A', c11s, 3)
for T, claim, tier in ((5, 'shocks_summary-3 (1 in 5)', 'B'), (10, 'A167', 'A'), (20, 'A171; A196', 'A'), (50, 'shocks_summary-3 (1 in 50)', 'B'), (100, 'A175', 'B')):
    add(f'national capacity over population, 2011, 1 in {T} year', claim, tier, float(shocks[('2011-fixed-3', str(T))]['capacity']), 2)
add('people over capacity, 2011, short term (A363)', 'A363', 'A', c11s, 3, 'over')
add('people over capacity, 2011, long term (A363)', 'A363', 'A', c11l, 3, 'over')
add('long-term capacity as a share of the 2011 population (A010, shown as a ratio; 0.69 is the 69%)', 'A010', 'A', c11l, 2)
add('people over capacity, 2011, 1 in 20 year (text of section 8.1)', 'text only (derived)', '-', float(shocks[('2011-fixed-3', '20')]['capacity']), 2, 'over')
add('population growth 2011 to 2025 (A328 note; A012)', 'A328; A012', 'B', 0, 3, 'growth')
add('population growth 2011 to 2025, percent, one decimal', 'A328', 'B', 0, 3, 'growth')
for r in nat:
    if r[0].endswith('percent, one decimal'):
        r[8], r[9] = round(float(r[6]) * 100, 1), round(float(r[7]) * 100, 1); r[10] = 'yes' if r[8] != r[9] else 'no'
with open(os.path.join(HERE, 'reference_periods_national_row.csv'), 'w', newline='') as f: csv.writer(f).writerows(nat)
for r in rows[1:]: print(r[1][:48].ljust(48), r[4], r[5], r[10], r[11], r[16], r[20])
for r in nat[1:]: print(r[0][:70].ljust(70), r[8], r[9], r[10])
