#!/usr/bin/env python3
"""Projections against capacity (B138 item 2; R05a issue 8; R04a 3.6 and question 8).

The projection series held on disk are the figures printed in three government reports (sources: literature register L226, L227, L228; PDFs in the models archive, hashes in the register):
  IGR 2023  Table A1.1 (PDF p. 240): 26.5 (2022-23), 30.4, 33.9, 37.3, 40.5 million (2062-63); population sensitivity text (PDF p. 274): the higher growth case is 3.1 million higher by 2062-63 (net
            overseas migration 50,000 higher a year from 2031-32 and a fertility rate converging to 1.72); the lower case is 'broadly symmetric' (read here as 3.1 million lower: a reading, not a printed figure).
  PS 2025   Table 1 (PDF p. 9): population at 30 June, 27.2 (2023-24, actual), 27.6, 28.0, 28.3 (2026-27), 31.5 (2035-36), 41.0 (2065-66); Box 7 (PDF p. 34): a higher-fertility or higher-migration case adds
            40,000 people a year from 2031-32 and reaches 'around 43 million' by 2065-66 (the path between is not printed).
  IGR 2021  Table A1.1 (PDF p. 168): 25.7 (2020-21), 28.8, 32.2, 35.6, 38.8 million (2060-61); kept to show the downward revision.
ABS Population Projections (3222.0) are NOT held: no series, no variants (the fetch is in the report). Only the figures quoted above are used, which is all the paper's section 1 quotes plus the printed tables.

Method: a series is the published points joined by straight lines, each point read as the population at 30 June of the financial year printed (2063 means 30 June 2063, the end of 2062-63).
The year a series reaches a threshold is the first point on that line at or above it, as a decimal of that convention (2058.0 is 30 June 2058; 2034.2 is about March 2034).
Where the printed points stop below the threshold the row says so, gives the last printed value over the threshold, and shows the year the last printed segment's slope would reach it (an extrapolation, marked).
The two sensitivity cases are built as the baseline plus an excess that grows in a straight line from the year the case starts (2031-32) to the printed end excess: an assumption, marked 'assumed path'.
Thresholds are the 2025-fixed capacities: national short term (41,503,537) and long term (15,623,209) at their release defaults, the 5th and 95th percentiles of the widened 19-choice draws
(results/ranges_2025-fixed_wide.csv; shocked ranges analysis/paper_a/shocks_ranges_wide.csv), and the herd-cycle range (results/ranges_2025-fixed_herdcycle.csv). Capacity is held at 2025 data by assumption.
Usage (repository root): python3 -I analysis/paper_a/projections_against_capacity.py    Writes projections_against_capacity.csv beside this file. Deterministic.
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
rd = lambda p: list(csv.DictReader(open(os.path.join(REPO, p))))
wide = {(r['zone'], r['setting']): r for r in rd('results/ranges_2025-fixed_wide.csv') if r['variant'] == 'wide'}
herd = {(r['zone'], r['setting']): r for r in rd('results/ranges_2025-fixed_herdcycle.csv')}
shk = {(r['return_period'], r['zone']): r for r in rd('analysis/paper_a/shocks_ranges_wide.csv') if r['preset'] == 'short'}
res = {(r['zone'], r['preset']): r for r in rd('results/2025-fixed.csv')}
POP25 = float(res[('1', 'short')]['population']); CAP_S = float(res[('1', 'short')]['capacity']); CAP_L = float(res[('1', 'long')]['capacity'])
T = [  # id, label, people
 ('S_base', 'short-term capacity, average year (41.5 million)', CAP_S),
 ('S_p5', 'short term, average year, 5th percentile of the widened draws', float(wide[('1', 'short')]['p5'])),
 ('S_p95', 'short term, average year, 95th percentile of the widened draws', float(wide[('1', 'short')]['p95'])),
 ('S_herd_lo', 'short term, herd-cycle range, 5th percentile', float(herd[('1', 'short')]['p5'])),
 ('S_herd_hi', 'short term, herd-cycle range, 95th percentile', float(herd[('1', 'short')]['p95'])),
 ('S10_central', 'short term, 1-in-10 year, central', float(shk[('10', '1')]['central'])),
 ('S10_p5', 'short term, 1-in-10 year, 5th percentile of the widened draws', float(shk[('10', '1')]['p5'])),
 ('S10_p95', 'short term, 1-in-10 year, 95th percentile of the widened draws', float(shk[('10', '1')]['p95'])),
 ('S20_central', 'short term, 1-in-20 year, central', float(shk[('20', '1')]['central'])),
 ('S20_p5', 'short term, 1-in-20 year, 5th percentile of the widened draws', float(shk[('20', '1')]['p5'])),
 ('S20_p95', 'short term, 1-in-20 year, 95th percentile of the widened draws', float(shk[('20', '1')]['p95'])),
 ('L_base', 'long-term capacity (15.6 million)', CAP_L),
 ('L_p5', 'long term, 5th percentile of the widened draws', float(wide[('1', 'long')]['p5'])),
 ('L_p95', 'long term, 95th percentile of the widened draws', float(wide[('1', 'long')]['p95'])),
]
# series: id -> (label, source, [(financial year end, million)], note)
IGR23 = [(2023, 26.5), (2033, 30.4), (2043, 33.9), (2053, 37.3), (2063, 40.5)]
PS25 = [(2024, 27.2), (2025, 27.6), (2026, 28.0), (2027, 28.3), (2036, 31.5), (2066, 41.0)]
IGR21 = [(2021, 25.7), (2031, 28.8), (2041, 32.2), (2051, 35.6), (2061, 38.8)]


def with_excess(base, start_fy, end_excess):
    """baseline plus an excess growing in a straight line from 0 at start_fy to end_excess at the last year; the baseline is linearly interpolated at the start year"""
    pts = []
    for fy, v in base:
        ex = 0.0 if fy <= start_fy else end_excess * (fy - start_fy) / (base[-1][0] - start_fy)
        pts.append((fy, v + ex))
    if start_fy not in [p[0] for p in base]:
        lo = max(p for p in base if p[0] < start_fy); hi = min(p for p in base if p[0] > start_fy); v0 = lo[1] + (hi[1] - lo[1]) * (start_fy - lo[0]) / (hi[0] - lo[0]); pts.append((start_fy, v0)); pts.sort()
    return pts


S = [
 ('IGR2023_base', 'Intergenerational Report 2023, baseline', 'Treasury 2023, Table A1.1 (PDF p. 240); L226', IGR23, 'printed points'),
 ('IGR2023_high', 'Intergenerational Report 2023, higher population growth', 'Treasury 2023, Appendix A4 (PDF pp. 272, 274); L226', with_excess(IGR23, 2032, 3.1), 'assumed path: the printed excess of 3.1 million by 2062-63 grows in a straight line from 2031-32'),
 ('IGR2023_low', 'Intergenerational Report 2023, lower population growth (read as symmetric)', 'Treasury 2023, Appendix A4 (PDF pp. 272, 274); L226', with_excess(IGR23, 2032, -3.1), 'assumed path and assumed size: "broadly symmetric" read as 3.1 million lower by 2062-63'),
 ('PS2025_base', 'Population Statement 2025, baseline', 'Centre for Population 2026, Table 1 (PDF p. 9); L228', PS25, 'printed points'),
 ('PS2025_high', 'Population Statement 2025, higher fertility or higher migration modelling', 'Centre for Population 2026, Box 7 (PDF p. 34); L228', with_excess(PS25, 2032, 2.0), 'assumed path: "around 43 million" by 2065-66 against 41.0 (excess 2.0 million) grows in a straight line from 2031-32'),
 ('IGR2021_base', 'Intergenerational Report 2021, baseline (superseded)', 'Treasury 2021, Table A1.1 (PDF p. 168); L227', IGR21, 'printed points; superseded by the 2023 report'),
]


def reach(pts, target):
    """first financial-year position (fractional) at which the straight-line series reaches target (million); None if the points stop below it; exact point match counts"""
    if pts[0][1] >= target: return pts[0][0], 'at or above at the first printed point'
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if y1 >= target: return x0 + (x1 - x0) * (target - y0) / (y1 - y0), 'interpolated'
    (x0, y0), (x1, y1) = pts[-2], pts[-1]
    return None, (x1 + (target - y1) * (x1 - x0) / (y1 - y0)) if y1 > y0 else None


def at(pts, x):
    if x <= pts[0][0]: return pts[0][1]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x <= x1: return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return pts[-1][1]


rows = [['series_id', 'series', 'source', 'printed_or_assumed', 'points_financial_year_end_and_million', 'threshold_id', 'threshold', 'threshold_people', 'population_30_june_2025', 'population_2025_over_threshold',
         'status', 'year_reached_financial_year', 'last_point_year', 'last_point_million', 'last_point_over_threshold', 'extrapolated_year_if_not_reached', 'note']]
for sid, label, src, pts, how in S:
    ptxt = '; '.join(f'{x}: {y:.1f}' for x, y in pts)
    for tid, tl, people in T:
        tm = people / 1e6; r, extra = reach(pts, tm); last = pts[-1]; ratio25 = POP25 / people
        if r is not None and r <= 2025 + 1e-9: status, yr, ex = 'at or above in 2025', '', ''
        elif r is not None: status, yr, ex = 'reached', f'{r:.1f}', ''
        else: status, yr, ex = 'not reached by the last printed point', '', ('' if extra is None else f'{extra:.0f}')
        rows.append([sid, label, src, how, ptxt, tid, tl, round(people), round(POP25), f'{ratio25:.3f}', status, yr, last[0], f'{last[1]:.1f}', f'{last[1] * 1e6 / people:.3f}', ex,
                     'extrapolated year uses the slope of the last printed segment and is not a projection' if ex else ''])
with open(os.path.join(HERE, 'projections_against_capacity.csv'), 'w', newline='') as f: csv.writer(f).writerows(rows)
for r in rows[1:]:
    if r[5] in ('S_base', 'L_base', 'S_p5', 'S_p95', 'S10_central'): print(r[0].ljust(14), r[5].ljust(12), r[10][:40].ljust(40), r[11], r[14], r[15])
