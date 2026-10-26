# Yield conversion test (scope row B2a)

**Question.** The workbook's stored yields are described as ABS averages converted to zero
irrigation (thesis 8.3.9, workbook log 2012-06-08), and the model then applies
`1 + 0.55 x irrigation share`. The files that documented the conversion are lost. Can the
conversion be reconstructed from the raw ABS data the thesis used?

**Answer.** Partly. The data are consistent with the thesis rule and with the seed deduction
in Table 19, but they cannot separate the irrigation term from zero at conventional
confidence. The uncertainty matters little nationally and up to 13 percent in a few
irrigation-heavy regions. Use the thesis rule as the like-for-like conversion and carry the
uncertainty forward.

## Data

ABS archive cubes by NRM region for 2006-07, 2007-08, 2008-09 and 2009-10, downloaded with
`fetch_abs_archive.py`. The thesis used five years, 2005-06 to 2009-10. The 2005-06 small area
release is not in the ABS archive and the 2005-06 cubes that are there are state-level only, so
this test has four of the five years. That is the main source of noise.

For nine crops (wheat, oats, barley, sorghum, maize, rice, sugar cane, canola, potatoes) and
the thesis's 52 NRM regions with its merges (ACT into Murrumbidgee, Sydney Metro into
Hawkesbury-Nepean, Torres Strait into Cape York), `compare.py` rebuilds the mean of yearly
yields using the thesis's thresholds, and pairs it with the workbook's stored yield and the
region's default irrigation share. 224 pairs from 43 regions are usable. Evidence table:
`pairs.csv`.

## Method

If stored yield F equals `(raw - seed) / (1 + k x s)`, with seed in tonnes per hectare as in
Table 19 and s the irrigation share, then `(raw - seed) / F - 1` equals `k x s`. `fit.py` fits
that line, with intervals from a bootstrap that resamples whole regions, because crops within a
region share weather and irrigation share and are not independent.

## Results

| Test | Result |
|---|---|
| Slope k, all 224 pairs | 0.80, 95% interval -0.22 to 1.59 |
| Slope k, 63 low-noise pairs (all four years present, yearly spread under 60%) | 0.55, 95% interval -0.60 to 1.24 |
| Share of bootstrap samples with k at or below zero | 6% for all pairs, 17% for the low-noise pairs |
| Intercept with the seed deducted, low-noise pairs | -0.009, interval -0.053 to +0.051 |
| Intercept with no seed deducted, low-noise pairs | +0.043, interval +0.002 to +0.104 |

Mean offset by irrigation share, all pairs: about -5% where the share is under 3%, about 0%
where it is over 6%. The thesis rule predicts a rise of about 6 percentage points; the data
show about 5.5.

Readings:

1. **Seed.** An intercept near zero with the seed deducted, and positive without it, supports
   deducting seed in tonnes per hectare as Table 19 lists. Weak evidence, roughly two standard errors.
2. **Irrigation.** The slope is consistent with 0.55 and with the thesis rule, but the intervals are
   wide and include zero. Yearly yields vary by about 70 percent of their mean, the conversion
   moves yields by at most a few percent in most regions, and only 12 of 43 regions have an
   irrigation share of 5 percent or more. The data cannot settle the exact form.
3. **Offset.** Stored yields average about 6 percent above the four-year raw mean. That fits the
   missing 2005-06 season rather than a conversion, but cannot be confirmed without that year.

## How much it matters

`sensitivity.js` runs every default case with the irrigation parameter at its default and at
zero. Zero removes the uplift. If the stored yields already included irrigation, the uplift would
overstate capacity by the same amounts. Results in `sensitivity.csv`.

| Measure | Change in capacity |
|---|---|
| Australia | -0.4% |
| Median region | -1.0% |
| 90th percentile region | -6.7% |
| Worst region, Mackay Whitsunday, irrigation share 28% | -13.3% |

## Conclusion and use

- **2011 baseline.** Unaffected. It uses the stored yields exactly as shipped.
- **Yield refresh (B3).** Apply the thesis rule like for like: remove the seed deduction in
  tonnes per hectare, divide by `1 + 0.55 x s` with s defined as in the 2011 defaults, then let
  the model apply the user's irrigation choice. This keeps the comparison with the old version
  clean.
- **Uncertainty (F4).** Report the sensitivity above for every zone, so a reader can see where
  the irrigation assumption could move a result by more than a few percent.
- **Method update (Workstream E).** Redefine irrigation by crop group and by share of cropped
  land, as set out in the irrigation review. That change is compared on its own afterwards.

## Reproduce

```bash
python3 -I fetch_abs_archive.py /path/to/xls
ABS_XLS_DIR=/path/to/xls MODEL_XLS=../../model/model.xls python3 -I compare.py
python3 -I fit.py
# sensitivity: convert model.xls to xlsx, npm install hyperformula xlsx, then
node sensitivity.js model.xlsx ../../data/2011/ sensitivity.csv
```

Needs Python with `xlrd`. `fit_output.txt` is the recorded output of `fit.py`.
