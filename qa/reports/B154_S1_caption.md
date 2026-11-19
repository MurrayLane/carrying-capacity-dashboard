# B154 report: Supplementary Figure S1 caption and file names

Result: done. The supplement caption now matches the figures.csv caption, Section S11 names the new figure files, the claims row is updated, and the regionalise README names the new image.

## Caption (supplementary.md)
Before: "...The search was heuristic, so the split is a lower bound on the best. The image is 1,100 by 1,021 pixels at 170 dpi, a lower resolution than the other figures (Section S11 names the file)."
After: "...The search was heuristic, so the split is a lower bound on the best."
The wording up to that sentence is identical to the figures.csv caption for Figure S1. The figures.csv caption also ends with a "Sources:" sentence that holds file paths; it is left out of the supplement caption because the brief says no file path in the caption (Section S11 carries those sources). Checked: no em dash, no slash, no "170", no "pixel" in the caption.

## Section S11 (supplementary.md)
Before: "Supplementary Figure S1 is analysis/regionalise_2025/ideal_K53_cap650k.png (1,100 by 1,021 pixels, 170 dpi), drawn by map_regions.py from analysis/regionalise_2025/summary.csv (corrected 2025 release, short term)."
After: "Supplementary Figure S1 is figS1_regions (png, svg and pdf) in the same folder, drawn by map_regions.py. Its inputs are the region csv data/regions/ideal_2025-fixed_short_K53_cap650k.csv, the land csv data/sa2/land_2011_method_by_sa2.csv, analysis/regionalise_2025/summary.csv (corrected 2025 release, short term) and the ABS ASGS Edition 3 (2021) SA2 boundary file data/asgs_sa2_2021/SA2_2021_AUST_SHP_GDA2020.zip (sources register D59)."

## Claims row (supplementary_claims.csv, section S2, B149a, Figure S1 caption)
Before: text "...69% long term, 1,100 by 1,021 pixels at 170 dpi"; source "analysis/regionalise_2025/summary.csv (...); image properties of analysis/regionalise_2025/ideal_K53_cap650k.png (1,100 by 1,021 pixels; 170 dpi)".
After: text "...69% long term"; source "analysis/figures_2025/paper_A/figures.csv row Figure S1 (caption text); qa/reports/B153_figure_S1_300dpi.md; analysis/regionalise_2025/summary.csv (2025-fixed, 53 regions, cap 650,000 km2: short 0.757, long 0.694)".

## README (analysis/regionalise_2025/README.md)
Before: "The shape (`ideal_K53_cap650k.png`, `ideal_K53_cap1300k.png`; ..."
After: "The shape (`analysis/figures_2025/paper_A/figS1_regions.png`, `ideal_K53_cap1300k.png`; ..."

## Left alone
- supplementary_claims.csv row 57 (the bracketed Figure S1 placeholder, section S2) still names ideal_K53_cap650k.png; it was outside the brief.
- The old ideal_K53_cap650k.png file is still in place.
