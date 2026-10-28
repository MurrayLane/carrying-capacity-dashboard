#!/usr/bin/env python3
"""Writes methods/beef-carcase-yield/method.json (SCOPE.md E18, flag A1): the carcase-to-retail-cuts yield of beef, 0.705, restored.
Usage: python3 analysis/constants_audit/make_beef.py          (repository root)

Evidence (all in the models archive unless noted):
 * superceded/170611 Base model.xls, row 467 (beef lean): processing yield K = 0.705, note 'USDA weights measures 1992: used figure for entire animal (retail cuts) across all cuts. Yield converted to loss.'
 * superceded/Base model (12).xls, same row: K = 1.0 and the note 'Originally used figure of 70.5% as per USDA weights measures 1992 ... BUT: the ABS yield figures are for carcass weight, not live weight so reverted to 100% processing yield.'
 * The 70.5% is a carcase-to-retail factor, not a live-weight one: USDA ERS (Nelson, Duewer and Crawford 1989) reevaluated the beef carcass-to-retail conversion factor to 0.705 for 1988 (retail cuts as a share of carcase weight), and a
   live-weight yield to retail cuts cannot be 70.5% (a carcase is about 55 to 62% of live weight). The ABS tables being carcase weight is the reason to USE the factor, not to drop it.
 * AUS-MEAT beef carcase yield guide (references re food processing yields/Ausmeat - beef yields.pdf): 68.7% meat, 12.0% fat, 19.3% bone.
 * The other red meats keep their carcase-to-retail yields (lamb 0.894, veal 0.83, pork 0.776); beef was the only red meat without one."""
import json, os
ROOT = os.getcwd()
mod = {'id': 'beef-carcase-yield', 'label': 'Beef carcase-to-retail yield restored (0.705)', 'line': 'improved',
       'description': "A correction to the method, not to data. The workbook's processing yield for beef (dressed), Base!K175, is 1.0 (no loss between the carcase and the retail cut), while lamb, veal and pork have 0.894, 0.83 and 0.776. The archive shows why: earlier versions used 0.705 (the USDA carcase-to-retail factor, retail cuts as a share of carcase weight) and a note in a later version reverts it to 100% because the ABS beef figures are carcase weight rather than live weight. That reverses the logic: the ABS figures being carcase weight is the reason the carcase-to-retail factor is needed (a live-weight yield of 70.5% is impossible). The module restores 0.705, in line with the AUS-MEAT carcase yield guide (68.7% meat yield). The edible portion (0.9155) and the cooking yield are unchanged.",
       'cellOverrides': {'Base': {'K175': 0.705}},
       'errata': ["0.705 is the USDA factor of 1988; Australian beef is trimmed differently (AUS-MEAT 68.7% meat plus 12% fat, of which some is eaten). A value between 0.69 and 0.74 is defensible; the module keeps the thesis's own earlier value.",
                  "Lamb, veal and pork processing yields were not checked against sources in this module.",
                  "Beef is 69% of the red meat eaten and red meat is most of the land in the short-term diet, so this correction is the largest single change in the corrected tier for the short term."]}
os.makedirs(os.path.join(ROOT, 'methods/beef-carcase-yield'), exist_ok=True); json.dump(mod, open(os.path.join(ROOT, 'methods/beef-carcase-yield/method.json'), 'w'), indent=2); print('wrote methods/beef-carcase-yield/method.json')
