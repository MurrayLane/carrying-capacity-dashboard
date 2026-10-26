"""Stage 2: the five-year average (thesis step 12), as the workbook computes it: IF(SUM(years)=0, 0, AVERAGE(years)).
A year with no figure is left out of the mean; a year whose result is 0 (a product with too little land) counts as a 0."""


def five_year_average(per_year):
    """per_year: list of arrays (one per year) of per-zone values or None; returns the per-zone mean of the years that have a value."""
    n = len(per_year[0]); out = []
    for c in range(n):
        vals = [y[c] for y in per_year if y is not None and y[c] is not None]
        out.append(sum(vals) / len(vals) if vals and sum(vals) != 0 else None)
    return out
