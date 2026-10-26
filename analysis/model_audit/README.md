# Model audit

Independent checks of the dashboard workbook, made on 2026-10-26. The scripts here evaluate the
workbook in JavaScript, separately from the Excel engine and the Java servlet, and compare the
results with the original servlet's output, with exact solutions of the same problem, and with the
thesis. `engine_vs_servlet.js` is also the acceptance test for the static rebuild.

## Setup

```bash
soffice --headless --convert-to xlsx ../../model/model.xls   # gives model.xlsx
npm install
```

## Scripts and what they found

| Script | Check | Result |
|---|---|---|
| `engine_vs_servlet.js` | Replay the 120-case baseline through the JavaScript engine | All 120 agree with the original servlet to its two-decimal rounding |
| `allocation_exact.js` | Workbook's sequential land allocation against an exact solution, 120 cases | Equal in all 120. Cropping limits capacity in 76 cases, cropping plus pasture in 38, all land in 6 |
| `diet_check.js` | Preference weights, and diet energy and nutrients against thesis Table 12 | All 21 sub-categories sum to one. Energy 7,350 kJ a day against 7,362 in the thesis; protein, fat, carbohydrate, sugar and fibre identical |
| `stress_test.js` | Every slider at both limits for ten zones; demand and supply responses | 340 cases, none negative, missing or unbalanced. Red meat peaks near half then falls, as thesis 9.1.4 describes |
| `thesis_vs_model.js` | Thesis Table 16 against the shipped model | Short term within 1.3% per zone. Long term differs by up to 3.3% per zone and 5.6% for the national sum of regions: the workbook was edited after the thesis tables |
| `audit_workbook.py` | Static audit of formulas, constants, subtotals, defaults and regional sums | See below |
| `../yield_conversion/` | Irrigation conversion and sensitivity | Separate write-up |

### Findings from `audit_workbook.py`

- No error cells; the only off-pattern formulas are subtotal rows. All 178 food subtotals feed exactly one category total.
- Two named ranges point at deleted cells and four more are built on them; nothing uses any of them.
- Numbers typed into formulas: the 155% irrigation uplift appears in 135 formulas, and some feed conversion constants such as 74.3% sit inside cells.
- Long-term defaults disagree between the workbook and the website's CSV: textiles 11.5 against 12.5 (the thesis text says 12), and irrigation uses the national 0.7% for every region in the workbook but regional shares in the CSV for 57 regions.
- Regional rows do not add up to their state rows. State populations sum to 20.7 million against 22.3 million nationally, while regional populations sum exactly to the national figure. Queensland regions hold 4.3% more total area and 5.0% less cropping than the Queensland row; South Australian regions hold 46% more non-agricultural land. This affects the scale comparison at state level, not capacity at default settings.

### Other observations

- Thesis Table 14, the worked example, gives 42.8 million for Australia; Table 16 and the shipped model give about 40.4 million. Table 14 reflects an earlier workbook.
- Two sentences in thesis 8.6.6 describe a percentage division upside down; the numbers are right.
- The front end would print "&infin;%" literally if capacity were ever zero. No default case triggers it.
- Irrigation is not limited by water, so setting it to 100 percent lifts national capacity from 40 to 62 million.
