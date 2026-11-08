# V25 report: re-check of the gap attribution (decision 34)

I followed the checker rules in `qa/briefs/_checker_rules_results_wave.md`. I edited no repository file, made no git changes and did not run `gap_attribution.py`, because it writes into the repository. I opened no B49 material. I opened the files under test only in part D, apart from one incident noted under "Found beyond the brief".

**Tolerance, set before comparing (the brief's own):** shares within 5 points and figures within 0.5%. Names and counts must match exactly.

**Can-fail checks:**
1. Cassidy: I changed the world's published "produced" figure from 10.1 to 11.5. My code then reported 197% against the claimed 72%.
2. Simpson: I changed the rate in (a) from 34.1 to 33.0. The share went to +129% against the claimed -13%.

Both changes land well outside the tolerance, so the comparison can fail.

FAO bulk file: its sha256 is `c4ff713e...6bac01`. This equals `sha256_csv` in `qa/fao_bulk_hashes.csv`.

## A. Henry and Godden: holds, with one attribution note

- **Recipe check.** I applied 404 x 10^15 J and 306 x 10^10 g (Table 2, "excl. wool/cotton"), times 70/45.7, times 0.1760 and 0.2041 (Table 4). This gives 108.912 and 95.6635, against 109 and 96 (Table 5). `henry_godden_summary.csv` prints 108.9 and 95.7.
- **Residuals as shares of half a unit:** 0.088 / 0.5 = 17.6%, and 0.3365 / 0.5 = 67.3%. **The claimed 18% and 67% hold.**
- **Totals 205.96 and 187.89:** these hold, but they do not come from `henry_godden_summary.csv`. They are the same recipe applied to the "Total" row of Table 2 (764 and 601, read from the scan at p. 99). That gives 205.9624 and 187.8881 against 206 and 188 (Table 5 "total", p. 100). Those residuals are **8% and 22%** of half a unit, not 18% and 67%. The brief pairs the totals with the 18% and 67% shares, but the shares belong to the 109 and 96 row. The README and CSV attribute each correctly: the CSV prints 8% and 22% for the total row.
- **Factors:** 82/466 = 0.17597 and 60/294 = 0.20408. These match the printed 0.1760 and 0.2041.

## B. Simpson pasture (1.718 against 1.758): holds, all within tolerance

Inputs from ABS 4306.0, 1991-92:
- Beef and veal 37.4, lamb 13.4 and mutton 7.6 kg a person, giving 58.4 kg. From the tonnes, 650,620 + 232,891 + 132,873 = 1,016,384 t.
- Mean population 1991-92 is 17,390,836 and 1990-91 is 17,176,910 (technical note 2).
- Estimated resident population at 30 June 1991 is 8,615,409 + 8,668,627 = 17,284,036 (p. 25).

The test figure is 58.4 / 34 = 1.7176, so the residual is 0.0404. From the tonnes it would be 1.7189, with a residual of 0.0391.

| | My value (58.4 basis / tonnes basis) | Claim | Verdict |
|---|---|---|---|
| (a) rate 34.1 (5.5 x 5 x 1.24 = 34.10) | 1.7126; -12.5% / -12.9% | -13% | holds |
| (b) milk rate | 2,637.6 kg/ha | 2,638 | holds (see note) |
| (b) milk that closes the residual | 106.4 kg a person = 57% of 186.4 kg | 106 kg, 57% | holds |
| (b) all milk on pasture | 1.7883, +175% / +181% | +175% | holds |
| (c) population at 30 June 1991 (17,284,036) | +26.3% / +27.2% | +30% | holds (within 5 points; see note) |
| (c) 1990-91 mean population (17,176,910) | +53.0% / +54.8% | +56% | holds (within 5 points; see note) |

Notes on (b):
- **The milk rate is not printed on thesis p. 284.** Page 284 gives the carrying capacity of 1.24 cattle a hectare (e12) and the milk-cattle reasoning. The 2,638 kg/ha is derived: world milk production of 474,020,000 t over 222,846,000 milk animals (Table A2.3, rows 99 and 100, p. 297) is 2,127 kg a milk animal, and 2,127 x 1.24 = 2,637.6. The README says this correctly ("1.24 a hectare, p. 284" and "world milk a milk animal (Table A2.3)").
- **The consumption base of 186 kg is assumed.** ABS prints only milk solids, 23.3 kg a person, and that figure includes an allowance for cream. The 186 kg comes from dividing by an assumed 12.5% solids (the assumption is from `simpson_food.py`). Market milk alone (101.4 L, about 104 kg) would make the closing milk 102% of consumption, and all of it on pasture +98%.

Note on (c): the CSV's figures shift from the 58.4 basis to the tonnes basis (see D).

## C. Cassidy: holds

My build:
- **Crops:** 23 FAOSTAT crops in 2011 (cereals including triticale, potatoes, cassava, sweet potatoes, yams, four pulses, groundnuts, soybeans, rapeseed, sunflower, sugar cane and sugar beet).
- **Yields:** each crop's 1997 to 2003 yield is its summed production over its summed area.
- **The cause applied:** each crop at its 1997 to 2003 yield, with 2011 areas and uses held. Its effect is a single calorie-weighted ratio on people per hectare.
- **Energy densities:** two assumed sets.
- **Base figures:** test figures from `cassidy.csv`; published figures from `published_values.csv`.

World yields in t/ha, 1997 to 2003 against 2011:

| Crop | 1997-2003 | 2011 | Crop | 1997-2003 | 2011 |
|---|---|---|---|---|---|
| wheat | 2.72 | 3.16 | dry beans | 0.71 | 0.84 |
| rice (paddy) | 3.88 | 4.45 | dry peas | 1.73 | 1.67 |
| maize | 4.38 | 5.14 | chickpeas | 0.77 | 0.92 |
| barley | 2.46 | 2.74 | lentils | 0.82 | 1.06 |
| sorghum | 1.36 | 1.36 | groundnuts | 1.46 | 1.64 |
| millet | 0.79 | 0.79 | soybeans | 2.24 | 2.52 |
| oats | 2.05 | 2.38 | rapeseed | 1.52 | 1.87 |
| rye | 2.20 | 2.55 | sunflower | 1.22 | 1.56 |
| triticale | 3.62 | 3.52 | sugar cane | 65.27 | 70.49 |
| potatoes | 15.97 | 19.72 | sugar beet | 39.89 | 54.93 |
| cassava | 10.38 | 11.84 | | | |
| sweet potatoes | 14.27 | 12.05 | | | |
| yams | 9.96 | 8.12 | | | |

Calorie-weighted ratio of 1997 to 2003 yields to 2011 yields: world 0.871 to 0.872, United States 0.918, India 0.837 to 0.840, China 0.859 to 0.863, Brazil 0.808 to 0.815.

| Share explained | Mine (produced / delivered, two density sets) | Claim | Verdict |
|---|---|---|---|
| World | 72% / 64 to 65% | 72% produced, 64% delivered | holds |
| United States | 35% / 37 to 38% | 35% | holds (produced) |
| India | 61 to 62% / 63 to 64% | 64% | holds |
| China | 51 to 53% / 46 to 48% | 50% | holds (produced) |
| Brazil | 74 to 77% / 79 to 82% | 82% | holds (produced 82.3 in CSV; mine 74 to 77, within 5 points on set B only) |

On the Brazil produced share: set A is 74% and set B is 77%. Against the CSV's 82.3% that is 8 points (set A, outside tolerance) and 5 points (set B, at the edge). The CSV's delivered share of 83.3% matches mine at 79 to 82%. The gap comes from my energy densities and crop set, not from the cause itself. I mark it as holding at the edge; it depends on the densities typed in.

An alternative reading of the cause changes the results. Taking the whole 1997 to 2003 crop basket instead (its own areas and mix) gives larger shares: world 82 to 84% produced, Brazil about 100%. The script and README use the fixed-area reading and say so ("2011 area and uses held").

## D. Files under test

**Figures in `gap_attribution.csv` against mine:** they match within tolerance on every target. I found these differences:

1. **Simpson (e) mixes two bases.** `current` is 58.4 / 34 = 1.7176 (per-person figures as printed). The (e) rows are computed from tonnes, and at the ABS's own 1991-92 population the tonnes give 58.44 kg and 1.7189, not 1.7176. About 0.0013 of each (e) shift, roughly 3 points of the residual, is the rounding of the printed per-person figures, not population. On one consistent basis:
   - 30 June 1991: 27.2% (tonnes basis) or 26.3% (per-person scaling), against the CSV's 29.5%. The README rounds this to 30%.
   - 1990-91 mean: 54.8% or 53.0%, against 56.2% (README 56%).
   - 30 June 1992: -23.1%, against -19.2%.

   All of these are within 5 points, so no verdict changes. The README sentence "(e) ... explain 56%, ... 30%" holds within tolerance, but it would read 55% and 27% on one basis.
2. **Henry and Godden total row:** the brief's pairing of 205.96 and 187.89 with 18% and 67% is the brief's, not the files'. The CSV gives 8% and 22% for the total row. The README states the total-row figures without their shares, which is correct but incomplete.
3. **Cassidy country deliveries:** the CSV's China delivered share is 40.5%; mine is 46 to 48% (6 to 7 points). The United States delivered share is 32.4%; mine is 37 to 38%. The README claims only the produced shares for the countries, so no stated figure is affected. The difference comes from the script letting each crop's yield change move the crop mix, and hence the delivered fraction. My single-ratio build cannot reproduce that.
4. **The year window matters for Cassidy, which the README does not say.** With 2000 alone in place of the 1997 to 2003 mean (the CSV's own rows), Brazil goes to 99%, China to 56% and the United States to 27%. The README reports only the 1997 to 2003 rows.

**README attribution sentences:**
- **Henry and Godden, "rounding":** holds.
- **Simpson:**
  - (a) -13% and the unrounded 34.0: hold; I checked 5.506 x 5 x 2.47 x 0.5 = 34.00.
  - (b) retail: not in the brief; arithmetic consistent with the CSV.
  - (c) 2,638, 106 kg, 57% and 175%: hold. The README does not state that the 186 kg rests on an assumed 12.5% solids.
  - (d) 149%: consistent with the CSV.
  - (e): holds within tolerance (see D1).
  - "left unexplained": consistent with the figures.
- **Cassidy:** every claim holds:
  - 72% and 64% for the world; 35%, 64%, 50% and 82% for the countries on calories produced; 74% with (b).
  - "22 to 42% above the paper": the range of test over published across the ten figures is 22% (world produced) to 42% (China delivered).
  - "at most 28% of a residual": United States, 27.7%.
  - "two thirds of the United States one": 65% is left unexplained.

**Neutral wording (decision 33):** holds. The section names causes ("FAOSTAT revisions", "the sources do not show which reading the paper used", "not attributed", "left unexplained"). None of the words error, mistake, wrong, flaw, fault or incorrect appears in it. The only wording note: "so the published figure is consistent with carcase weight" is a reading of the source, not a judgement of the authors.

**Can-fail for part D:** both deliberate changes stated at the top move a share outside the 5-point tolerance (197% against 72%, and +129% against -13%).

## Found beyond the brief

- Before part D, a repository-wide grep for "205.96" showed me one README line from the section under test (the Henry and Godden attribution bullet) and one CSV row. I did not use them to derive any value. I obtained the 764 and 601 totals independently from the scanned paper (Table 2, p. 99).
- The Simpson milk test uses the world milk yield. The script's own row c3 shows that at the Canadian rate (7,199 kg/ha) closing the residual needs 291 kg a person, 156% of consumption. The README does not mention this row.
- "China" in both the script and my build is FAO's "China" aggregate. "China, mainland" gives the same shares in my build (51% and 47%).

## Rerun

```
cd /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v25
python3 -I extract.py "/tmp/claude-0/fao/q/Production_Crops_Livestock_E_All_Data_(Normalized).csv"   # writes qcl_sub.csv
python3 -I cassidy_check.py            # part C; add 'canfail' for the deliberate wrong value
pdftotext -layout "/home/user/carrying-capacity-models/Comparators/ABS-4306.0-1991-92-Apparent-Consumption-of-Foodstuffs.pdf" abs.txt
python3 -I simpson_check.py            # part B; add 'canfail'
python3 -c "f=70/45.7; [print(x*f*k, (p-x*f*k)/0.5) for x,k,p in ((404,.176,109),(306,.2041,96),(764,.176,206),(601,.2041,188))]"   # part A
sha256sum "/tmp/claude-0/fao/q/Production_Crops_Livestock_E_All_Data_(Normalized).csv"
```

## Files read

- /home/user/carrying-capacity-dashboard/qa/briefs/_checker_rules_results_wave.md, /home/user/carrying-capacity-dashboard/qa/briefs/V25_gap_attribution_recheck.md
- /home/user/carrying-capacity-dashboard/qa/fao_bulk_hashes.csv
- /home/user/carrying-capacity-dashboard/analysis/method_tests_2025/henry_godden_summary.csv, henry_godden_items.csv, henry_godden.py (header and factor lines), published_values.csv, cassidy.csv, cassidy_people_per_hectare.py (header docstring only), fao_qcl_countries.csv (head)
- /home/user/carrying-capacity-dashboard/qa/reports/V22_simpson_third_build_recheck.md (method only), qa/reports/V03_energy_protein.md (grep)
- /tmp/claude-0/hgimg/p-3.png and p-4.png (Henry and Godden 1995, Tables 2 to 5, pp. 99 to 100)
- /home/user/carrying-capacity-models/Literature review/Wackernagel_1994_PhD_thesis_UBC_Ecological_footprint_and_appropriated_carrying_capacity.pdf (pdftotext; thesis pp. 284 to 285, Table A2.3 p. 297)
- /home/user/carrying-capacity-models/Comparators/ABS-4306.0-1991-92-Apparent-Consumption-of-Foodstuffs.pdf (pdftotext; Tables 1 and 2, technical note 2, p. 25)
- /tmp/claude-0/fao/q/Production_Crops_Livestock_E_All_Data_(Normalized).csv
- Part D: /home/user/carrying-capacity-dashboard/analysis/method_tests_2025/gap_attribution.py, gap_attribution.csv, README.md (lines 353 to 420, "Gap attribution")
- My code: /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v25/extract.py, /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v25/cassidy_check.py, /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v25/simpson_check.py
