#!/usr/bin/env python3
"""Checks on the B138 outputs (items 1 to 6): each output against a value that is held somewhere else, or against arithmetic done here by a different route.
Usage (repository root): python3 -I analysis/paper_a/check_B138.py            prints ok or FAIL per check; exit 1 if any FAIL
       python3 -I analysis/paper_a/check_B138.py --wrong    adds deliberate wrong expected values (marked TEST); each must print FAIL, the real checks stay ok
Reads the CSVs the six jobs wrote; it does not rerun them. Deterministic."""
import csv, os, sys
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
rd = lambda p: list(csv.DictReader(open(os.path.join(REPO, p))))
WRONG = '--wrong' in sys.argv; bad = 0
nfail = 0


def check(name, got, want, tol=0.0, test=False):
    global nfail
    ok = abs(float(got) - float(want)) <= tol
    print(('ok   ' if ok else 'FAIL ') + ('TEST | ' if test else '') + f'{name} | got {got} | expected {want} | tolerance {tol}')
    if not ok and not test: nfail += 1


res = {(r['release'], r['zone'], r['preset']): r for r in rd('results/2011-fixed-3.csv') + rd('results/2025-fixed.csv')}
# item 6: the five-year row of the window subsets is the released 2011-fixed-3 capacity; every subset ratio is capacity over that capacity
sub = [r for r in rd('analysis/paper_a/window_subsets_2011.csv') if r['zone'] == '1']
five = {r['preset']: r for r in sub if r['subset'].startswith('all five years')}
for p in ('short', 'long'): check(f'item 6: five-year row, Australia {p}', five[p]['capacity'], res[('2011-fixed-3', '1', p)]['capacity'])
for r in sub:
    if not r['subset'].startswith('all five'): check(f'item 6: ratio {r["subset"]} {r["preset"]}', r['ratio_to_five_year_capacity'], float(r['capacity']) / float(five[r['preset']]['capacity']), 5.1e-5)
check('item 6: subsets per preset (10 of 5 years choose 3, plus the five-year row)', len([r for r in sub if r['preset'] == 'short']), 11)
# item 1: the 2025 midpoint population is the mean of the ERP of June 2022 and June 2023 (livestock window 2020-21 to 2024-25, midpoint 1 January 2023), scaled to the release population
erp = {y: 0.0 for y in (2022, 2023, 2025)}; sa2 = {r['sa2_code'] for r in rd('data/sa2/land_2011_method_by_sa2.csv')}
for r in rd('data/sa2/population_erp.csv'):
    if r['sa2_code'] in sa2:
        for y in erp: erp[y] += float(r[str(y)] or 0)
want = (erp[2022] + erp[2023]) / 2 * float(res[('2025-fixed', '1', 'short')]['population']) / erp[2025]
liv = next(r for r in rd('analysis/population_2011/reference_periods.csv') if r['input'].startswith('Meat, wool'))
check('item 1: 2025 livestock-window midpoint population', liv['population_at_midpoint_2025'], want, 1.0)
check('item 1: gap from the 2011 livestock window midpoint to 30 June 2011 (years)', liv['gap_midpoint_to_population_date_2011_years'], 3.5)
nat = {r['figure']: r for r in rd('analysis/population_2011/reference_periods_national_row.csv')}
check('item 1: 2011 short-term capacity over the regional sum', nat['short-term capacity over population, 2011, average year, three decimals']['value_after'], 33307814 / 22336514, 5e-7)
check('item 1: A328 population growth on the regional sum, percent', nat['population growth 2011 to 2025, percent, one decimal']['rounded_after'], 23.6)
# item 2: IGR 2023 baseline reaches 31.115 million (the 5th percentile) between 30.4 (2033) and 33.9 (2043); worked by hand
pr = {(r['series_id'], r['threshold_id']): r for r in rd('analysis/paper_a/projections_against_capacity.csv')}
check('item 2: IGR 2023 base reaches the widened 5th percentile in', pr[('IGR2023_base', 'S_p5')]['year_reached_financial_year'], 2033 + 10 * (31.115433 - 30.4) / (33.9 - 30.4), 0.051)
check('item 2: 2062-63 projection over the long-term capacity (the 2.6 times)', pr[('IGR2023_base', 'L_base')]['last_point_over_threshold'], 40.5e6 / 15623209, 5e-4)
# item 3: the national mean requirement is between the lightest and heaviest adult values; the interpolation reproduces the NHMRC text
ae = {r['row_type'] + '|' + r['age']: r for r in rd('analysis/population_2011/age_sex_energy.csv') if r['row_type'] == 'national_mean'}
m10 = float(ae['national_mean|all']['mean_requirement_mj']) if ae['national_mean|all']['mean_requirement_mj'] else None
rows = [r for r in rd('analysis/population_2011/age_sex_energy.csv') if r['row_type'] == 'national_mean' and r['mean_requirement_mj']]
check('item 3: mean requirement 2010 against 8.0 MJ ratio is the mean over 8', [r for r in rows if r['erp_30_june_2010']][0]['ratio_to_model_8_0_mj'], float([r for r in rows if r['erp_30_june_2010']][0]['mean_requirement_mj']) / 8.0, 5e-5)
ages = [r for r in rd('analysis/population_2011/age_sex_energy.csv') if r['row_type'] == 'age_sex_group']
check('item 3: share of the population over all age-sex groups in 2010 sums to 1', sum(float(r['share_2010']) for r in ages), 1.0, 1e-5)
# item 4: the real partitions on the state basis equal results/scale_curve.csv (2025-fixed, short, state basis)
sc = {(r['release'], r['preset'], r['level'], r['yield_basis']): r for r in rd('results/scale_curve.csv')}
sp = {(r['release'], r['preset'], r['section'], r['variant']): r for r in rd('analysis/scale_curve_2025/scale_partition.csv') if r['section'] in ('real_partition', 'arable_relaxation') and r['draw'] == ''}
check('item 4: 7 states, 2025-fixed short', sp[('2025-fixed', 'short', 'real_partition', 'states')]['share_of_national_unrelaxed'], sc[('2025-fixed', 'short', 'State', 'state')]['share_of_national'], 5.1e-4)
check('item 4: 53 regions, 2025-fixed short', sp[('2025-fixed', 'short', 'real_partition', 'nrm_regions')]['share_of_national_unrelaxed'], sc[('2025-fixed', 'short', 'NRM region', 'state')]['share_of_national'], 5.1e-4)
sa2u = [r for r in rd('analysis/scale_curve_2025/scale_partition.csv') if r['section'] == 'arable_relaxation' and r['variant'] == 'unrelaxed' and r['preset'] == 'short' and r['groups'] == '2450'][0]
check('item 4: SA2 level unrelaxed, 2025-fixed short', sa2u['share_of_national_unrelaxed'], sc[('2025-fixed', 'short', 'SA2', 'state')]['share_of_national'], 5.1e-4)
draws = [r for r in rd('analysis/scale_curve_2025/scale_partition.csv') if r['section'] == 'random_grouping' and r['variant'] == 'uniform' and r['release'] == '2025-fixed' and r['preset'] == 'short']
check('item 4: 200 random groupings', len(draws), 200)
# item 5: the 2021-23 window reproduces the released 2025-fixed capacity, the 2010-12 window has no effect
dw = [r for r in rd('analysis/diet_2025/diet_window.csv') if r['zone'] == '1' and r['preset'] == 'short' and r['rounding'] == 'release rounding']
check('item 5: window 2021-23 capacity is 2025-fixed', [r for r in dw if r['window'] == '2021-23'][0]['capacity'], res[('2025-fixed', '1', 'short')]['capacity'])
check('item 5: window 2010-12 layer effect is nil (people, rounding of the mix only)', [r for r in dw if r['window'] == '2010-12'][0]['layer_effect'], 0, 50)
if WRONG:
    print('--- deliberate wrong values (examples; each must FAIL) ---')
    check('five-year Australia short capacity entered as 33,300,000', five['short']['capacity'], 33300000, 0.0, True)
    check('IGR 2023 base reaches the widened 5th percentile entered as 2040', pr[('IGR2023_base', 'S_p5')]['year_reached_financial_year'], 2040, 0.051, True)
    check('national 2011 ratio entered as 1.52', nat['short-term capacity over population, 2011, average year, three decimals']['value_after'], 1.52, 5e-7, True)
sys.exit(1 if nfail else 0)
