# B153 report: Supplementary Figure S1 at 300 dpi

Result: done. Figure S1 is redrawn at 300 dpi with SVG and PDF beside it.

## Download
- URL: https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs/edition-3-july-2021-june-2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip (link on the ASGS Edition 3 digital boundary files page; no browser needed)
- Size: 50,678,443 bytes. sha256: c4dc5bac209f01177eaa0715d27f32cdb09ab5784fb82979741556d2f8e6d148. The zip tests clean.
- Taken: the GDA2020 shapefile (the GDA94 one was not). Saved in data/asgs_sa2_2021/, unzipped to data/asgs_sa2_2021/extracted/. Sources register id D59.

## Regions
- 53 regions drawn (map_regions.py prints "written 53 regions"; the regions csv holds 53 distinct region numbers).

## Same regions and colours as the 170 dpi image
- Re-running the changed script at the default 170 dpi gave a PNG of 1,100 by 1,021 pixels with a maximum pixel difference of 0 against analysis/regionalise_2025/ideal_K53_cap650k.png: the same drawing.
- The 300 dpi PNG is 1,941 by 1,802 pixels; downscaled to 1,100 by 1,021 its mean absolute difference from the existing image is 1.3 of 255 (resampling only).
- Legend: one colourbar, 0.0 to 0.5, label "Cropping share of cropping plus pasture land", identical. Both images have 48 distinct fill colours covering more than 200 pixels. Title unchanged. No em or en dash in labels. Text is 10 to 10.5 pt at 216 mm wide, about 9 pt when scaled to 190 mm.

## Files written
- data/asgs_sa2_2021/SA2_2021_AUST_SHP_GDA2020.zip, README.md, extracted/ (5 files)
- analysis/regionalise_2025/map_regions.py: `--dpi N` option, default 170. Also, as step 1 asked, a .png output now also saves .svg and .pdf from the same figure (same style as `_common.save`). This is a second change to the script beyond the one the scope line names; revert the three added lines if unwanted.
- analysis/figures_2025/paper_A/figS1_regions.png (300 dpi), figS1_regions.svg, figS1_regions.pdf
- analysis/figures_2025/paper_A/register_S1.py (rewritten; adds a `--check` for the region count) and the S1 row of figures.csv
- qa/sources_register.csv: new row D59
- qa/reports/B153_figure_S1_300dpi.md

## For the coordinator
- papers/A_results/draft/supplementary.md (not mine to edit) still says the image is 1,100 by 1,021 pixels at 170 dpi and that Section S11 names the old file. register_S1.py drops that sentence from the figures.csv caption; the draft text and Section S11 need the same update. analysis/regionalise_2025/README.md still names the old 170 dpi image as the shape file.
- The old analysis/regionalise_2025/ideal_K53_cap650k.png is left in place.

Wrong-value check: `python3 -I analysis/figures_2025/paper_A/register_S1.py --check --expect 52` prints "check Figure S1 region count: recomputed 53, plotted 53, expected 52 -> FAIL" and exits 1; with 53 it prints OK and exits 0.
