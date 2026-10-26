"""Stage 3: from five-year averages to the model's Yield sheet (thesis steps 13 and 8.3.9).

1. Where a commodity-zone pair is marked for filling (the author's judgement of climatic suitability, recorded in archive_fill_mask.json;
   for new data the rule is yet to be written) and the zone has no average, it gets the national average times its "major crops yield %": the mean over wheat, oats, barley,
   sorghum, maize, canola and potatoes of (zone average / national average), skipping any the zone does not report. (Base model 021012,
   Yield row 3. The thesis words this as a cereal ratio; the workbook uses these seven crops.)
2. Every figure is divided by (1 + 0.55 x the zone's irrigation share), the zero-irrigation conversion; the model multiplies it back by
   (1 + 0.55 x the irrigation setting), so the default setting returns the observed average exactly.
3. t/ha become g/m2 (x 100), the unit of the Yield sheet.
"""
MAJOR_ROWS = [1, 2, 3, 4, 5, 9, 49]        # rows of the averaged table: Wheat, Oats, Barley, Sorghum, Maize, Canola, Potatoes
UPLIFT = 0.55


def major_factor(avg, zone):
    rs = [avg[r][zone] / avg[r][1] for r in MAJOR_ROWS if avg[r][zone] and avg[r][1]]
    return sum(rs) / len(rs) if rs else None


def model_yield(avg, irrigation, fill_mask):
    """avg: {row: [value for zone 0..60]} (zone 0 unused); irrigation: {zone: share}; fill_mask: {(row, zone)}. Returns {row: [g/m2 for zone 0..60]} with None where no value."""
    factors = {z: major_factor(avg, z) for z in range(1, 61)}; out = {}
    for r, vals in avg.items():
        row = [None] * 61
        for z in range(1, 61):
            v = vals[z]
            if v is None and (r, z) in fill_mask and vals[1] and factors[z] is not None: v = vals[1] * factors[z]
            row[z] = None if v is None else v / (1 + UPLIFT * irrigation[z]) * 100
        out[r] = row
    return out
