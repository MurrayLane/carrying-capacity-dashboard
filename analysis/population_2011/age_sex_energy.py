#!/usr/bin/env python3
"""Age-sex energy requirement (B138 item 3; R05a issue 9; R04a 3.7 and question 7).

The national average energy requirement per person, weighted by the estimated resident population by age and sex, against the model's fixed 8.0 MJ a person a day.

Requirement by age and sex: NHMRC Nutrient Reference Values for Australia and New Zealand, dietary energy (sources register A27; file Foundation diets/nutrient-refererence-dietary-intakes.pdf), at the PAL the model's
diet uses, 1.4 (very sedentary; the food amount of the release is the sedentary NHMRC diet): Table 1 for infants (kJ a day by month: age 0 is the mean of months 1 to 11, age 1 the mean of months 12, 15, 18
and 21, age 2 the value at 24 months), Table 2 for 3 to 18 years (MJ a day, PAL 1.4 column), Table 3 for adults (PAL 1.4 column at the reference body weights of the text: men 76 kg, women 61 kg, by linear
interpolation between the table's rows of BMI 22; bands 19-30, 31-50, 51-70 and over 70; the text's own sedentary values for 19-30, 10.8 MJ for men and 8.1 MJ for women, are checked below).
The model's 8.0 MJ: analysis/nutrition_lp_2025/README.md (the food groups of the evaluator give 7.38 MJ; 8.0 counts drinks; qa/reports/V49_check_B134.md).

Population by age and sex: ABS Australian Demographic Statistics, June quarter 2010 (31010DO002_201006), Tables 7 and 8, ERP at 30 June 2009 and 30 June 2010, single years of age to 84 and five-year groups above
(models archive, 'Yield data/ABS - Aust demographics 2010.xls'; not in the sources register). These are the ONLY age-sex counts on disk. ERP by age and sex at 30 June 2011 and at 30 June 2025 is NOT held (D31 is
totals), so the 2011 and 2025 averages, the change between them, and its sign and size are NOT computed here; rows for them are written empty and the fetch is listed in the report. The 2009 and 2010 averages
are shown as the nearest held readings: they show the level against 8.0 MJ and how little the mean moves in a year.

Usage (repository root): python3 -I analysis/population_2011/age_sex_energy.py [ABS_DEMOGRAPHICS_XLS]     (needs xlrd; default path /home/user/carrying-capacity-models/Yield data/ABS - Aust demographics 2010.xls)
Writes age_sex_energy.csv beside this file. Deterministic.
"""
import csv, os, re, sys
import xlrd
HERE = os.path.dirname(os.path.abspath(__file__))
XLS = sys.argv[1] if len(sys.argv) > 1 else '/home/user/carrying-capacity-models/Yield data/ABS - Aust demographics 2010.xls'
MODEL_MJ = 8.0
# Table 1, kJ a day: months 1..12 then 15, 18, 21, 24
INF = {'M': [2000, 2400, 2400, 2400, 2500, 2700, 2800, 3000, 3100, 3300, 3400, 3500, 3800, 4000, 4200, 4400],
       'F': [1800, 2100, 2200, 2200, 2300, 2500, 2500, 2700, 2800, 3000, 3100, 3200, 3500, 3800, 4000, 4200]}
# Table 2, PAL 1.4, MJ a day, ages 3..18
CH = {'M': [4.9, 5.2, 5.5, 5.8, 6.1, 6.4, 6.8, 7.3, 7.7, 8.2, 8.7, 9.3, 9.9, 10.3, 10.7, 10.9],
      'F': [4.5, 4.8, 5.1, 5.4, 5.7, 6.0, 6.4, 6.7, 7.0, 7.4, 7.8, 8.1, 8.2, 8.4, 8.4, 8.5]}
# Table 3, PAL 1.4, MJ a day: (weight kg at BMI 22, value) for each height row, by age band
AD = {'M': {'19-30': [(56.3, 9.0), (63.6, 9.7), (71.3, 10.3), (79.4, 11.1), (88.0, 11.8)], '31-50': [(56.3, 8.9), (63.6, 9.4), (71.3, 9.9), (79.4, 10.4), (88.0, 11.0)],
            '51-70': [(56.3, 8.2), (63.6, 8.6), (71.3, 9.1), (79.4, 9.6), (88.0, 10.2)], '>70': [(56.3, 7.3), (63.6, 7.8), (71.3, 8.3), (79.4, 8.9), (88.0, 9.5)]},
      'F': {'19-30': [(49.5, 7.1), (56.3, 7.7), (63.6, 8.4), (71.3, 9.0), (79.4, 9.7)], '31-50': [(49.5, 7.3), (56.3, 7.6), (63.6, 8.0), (71.3, 8.3), (79.4, 8.7)],
            '51-70': [(49.5, 6.9), (56.3, 7.3), (63.6, 7.6), (71.3, 8.0), (79.4, 8.4)], '>70': [(49.5, 6.5), (56.3, 6.9), (63.6, 7.2), (71.3, 7.7), (79.4, 8.1)]}}
REF_KG = {'M': 76.0, 'F': 61.0}


def interp(pts, x):
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= x <= x1: return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    raise ValueError(x)


adult = {(sx, b): interp(AD[sx][b], REF_KG[sx]) for sx in 'MF' for b in AD[sx]}
# the text of Table 3's rationale: 10.8 MJ (men) and 8.1 MJ (women) at 19-30, sedentary; a check on the interpolation and the transcription
for sx, txt in (('M', 10.8), ('F', 8.1)):
    if abs(adult[(sx, '19-30')] - txt) > 0.06: sys.exit(f'transcription check failed: {sx} 19-30 interpolates to {adult[(sx, "19-30")]:.2f}, the text says {txt}')


def req(sx, age):
    """MJ a day at PAL 1.4"""
    if age == 0: return sum(INF[sx][:11]) / 11 / 1000
    if age == 1: return sum(INF[sx][11:15]) / 4 / 1000                 # months 12, 15, 18, 21
    if age == 2: return INF[sx][15] / 1000                              # 24 months
    if age <= 18: return CH[sx][age - 3]
    return adult[(sx, '19-30' if age <= 30 else '31-50' if age <= 50 else '51-70' if age <= 70 else '>70')]


wb = xlrd.open_workbook(XLS)
ERP = {}                                                                # (year, sex, age) -> persons; age 85 stands for the 85 and over groups
for year, sheet in ((2009, 'Table_7'), (2010, 'Table_8')):
    s = wb.sheet_by_name(sheet)
    assert 'at 30 June %d' % year in s.cell_value(3, 0).replace('–', '-'), s.cell_value(3, 0)
    sex = None; col = 9                                                 # Australia
    for r in range(5, 230):
        lab = str(s.cell_value(r, 0)).strip()
        if lab in ('MALES', 'FEMALES'): sex = 'M' if lab == 'MALES' else 'F'; continue
        if lab == 'PERSONS': break
        m = re.fullmatch(r'(\d+)\.?0?', lab)
        if m and sex and int(m.group(1)) <= 84: ERP[(year, sex, int(m.group(1)))] = float(s.cell_value(r, col))
        elif lab in ('85–89', '90–94', '95–99', '100 and over') and sex: ERP[(year, sex, 85)] = ERP.get((year, sex, 85), 0.0) + float(s.cell_value(r, col))
tot = {y: sum(v for (yy, sx, a), v in ERP.items() if yy == y) for y in (2009, 2010)}
for y, exp in ((2009, 21965287.0), (2010, 22342398.0)):
    if abs(tot[y] - exp) > 1: sys.exit(f'ERP total {y} {tot[y]} is not the workbook All ages total {exp}')
mean = {y: sum(req(sx, a) * v for (yy, sx, a), v in ERP.items() if yy == y) / tot[y] for y in (2009, 2010)}
rows = [['row_type', 'sex', 'age', 'requirement_mj_per_day_pal_1_4', 'erp_30_june_2009', 'erp_30_june_2010', 'share_2009', 'share_2010', 'mean_requirement_mj', 'ratio_to_model_8_0_mj', 'note']]
for sx in 'MF':
    for a in range(0, 86):
        rows.append(['age_sex_group', sx, f'{a}' if a < 85 else '85 and over', f'{req(sx, a):.3f}', round(ERP[(2009, sx, a)]), round(ERP[(2010, sx, a)]), f'{ERP[(2009, sx, a)] / tot[2009]:.6f}', f'{ERP[(2010, sx, a)] / tot[2010]:.6f}', '', '',
                     'age 85 holds all ages 85 and over, at the over-70 adult value' if a == 85 else ''])
for y in (2009, 2010):
    rows.append(['national_mean', 'both', 'all', '', round(tot[y]) if y == 2009 else '', round(tot[y]) if y == 2010 else '', '', '', f'{mean[y]:.4f}', f'{mean[y] / MODEL_MJ:.4f}', f'ERP at 30 June {y} (ABS ADS June quarter 2010, Table {7 if y == 2009 else 8}); NHMRC PAL 1.4; model 8.0 MJ'])
rows.append(['national_mean', 'both', '30 June 2011', '', '', '', '', '', '', '', 'NOT COMPUTED: ERP by age and sex at 30 June 2011 is not on disk (fetch listed in qa/reports/B138_paper_A_smaller_computations.md)'])
rows.append(['national_mean', 'both', '30 June 2025', '', '', '', '', '', '', '', 'NOT COMPUTED: ERP by age and sex at 30 June 2025 is not on disk (fetch listed in the report)'])
rows.append(['change_2011_to_2025', 'both', '', '', '', '', '', '', '', '', 'NOT COMPUTED (needs both of the rows above): sign expected negative for the requirement per person as the population ages; size unknown'])
with open(os.path.join(HERE, 'age_sex_energy.csv'), 'w', newline='') as f: csv.writer(f).writerows(rows)
print({y: round(mean[y], 4) for y in mean}, {y: round(mean[y] / MODEL_MJ, 4) for y in mean}, adult[('M', '19-30')], adult[('F', '19-30')])
