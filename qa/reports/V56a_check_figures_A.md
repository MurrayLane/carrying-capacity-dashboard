# V56a: blind check of the Paper A figures (B144a)

Checker brief: `qa/briefs/V56a_check_figures_A.md`. Builder brief: `qa/briefs/B144a_figures_paper_A.md`. Outputs under test: `analysis/figures_2025/paper_A/` (nine scripts, nine PNG and SVG pairs, `figures.csv`). The builder's report was opened last, after every check below was run.

No git; no subagents; no network. No builder script was edited: all instrumented runs used scratch copies (`_common.py` copied with `ROOT` set to the repository and outputs written to the scratch folder). One side effect to declare: the first `--check` run on the original scripts (plain `python3 -I`) wrote `analysis/figures_2025/paper_A/__pycache__/_common.cpython-313.pyc`; the folder did not exist before and I deleted it at once. Every later run used `-B`. No other repository file was written except this report.

## Tolerance and the wrong-value example

* Data cells: exact. A plotted value must equal its csv cell (or the cell divided by a stated constant such as 1e6, or a stated ratio of two cells) to floating-point identity (|difference| at or under 1e-12 for ratios; exact for clipped colour values). Counts and names exact.
* Wrong-value example: `python3 -I -B analysis/figures_2025/paper_A/fig1_national.py --check --expect 41.6` prints `recomputed 41.5034, plotted 41.5035, expected 41.6 -> FAIL` and exits 1. Also planted: Figure 2 `--expect 465` (FAIL, exit 1) and Figure 6 `--expect 22` (FAIL, exit 1). All nine scripts pass `--check` with their default expected value (exit 0).
* My own comparison code was also given a wrong value: setting the Figure 6 whisker floor to 1e-2 instead of 1e-3 in my comparison makes 12 of the 159 whiskers report a mismatch (Alinytjara Wilurara, Swan, Hawkesbury-Nepean-Sydney and others with p5 under 0.01), so the sweep can fail.

## Reproducibility

The scratch copies regenerate eight of the nine PNGs pixel for pixel. Figure S6 does not: `fig6s_scenarios.py` iterates a Python set of zones when drawing, so the drawing order of overlapping dots depends on the hash seed (`PYTHONHASHSEED=1` and `=2` differ in 4,339 pixels). The data drawn are the same; the fix is `for z in sorted(zones)`.

## Step 1: data behind the marks

Ten values (twelve, with S6 and a second Figure 1 value) were named before any plot data were read: 2011 national capacity and the 2025 19-choice p95 (Figure 1); the Wet Tropics arrow and the Corangamite population change (Figure 2); Wet Tropics land and livestock, short term (Figure 3); 2025 short-term SA2 share (Figure 4); the largest lever (Figure 5a); NT long-term ratio 2025 (Figure 5b); Wet Tropics 1-in-20 whisker (Figure 6); Wet Tropics beef carcase, short term (Figure 7); Wet Tropics excess (Figure 8); Wet Tropics under fuel-csiro-340, long term (S6). Values were read from the drawn matplotlib artists (offsets, sizes, line data, colour arrays, texts) captured from the scratch runs.

| # | Figure | Value drawn | csv cell | Result |
|---|---|---|---|---|
| 1 | 1 | 2011 dot y = 33.307814 | `2011-fixed-3.csv` zone 1 short capacity 33,307,814 | equal |
| 2 | 1 | 19-choice whisker top 49.169829 | `ranges_2025-fixed_wide.csv` wide, short, p95 49,169,829 | equal |
| 3 | 2 | Wet Tropics arrow 0.76771 to 1.10508; label +126 | `movers-3.csv` 189,537/246,885 and 315,100/285,138; dcap 125,563 | equal |
| 4 | 2 | Corangamite population change +125 | `movers-3.csv` dpop 125,254 | equal |
| 5 | 3 | Wet Tropics land and livestock, short, 46.784% (label +47) | `capacity_by_cause_corrected_orders.csv` eight-layer `shapley_mean` 88,673 / cap2011 189,537 (the forward walk, 74,350, would give 39.2%) | equal |
| 6 | 4 | 2025 short SA2 point 37.4% | `scale_curve.csv` 2025-fixed short SA2 state 0.374 | equal |
| 7 | 5a | weather allowance +119% | `long_term_levers-3.csv` 34,274,878 / 15,623,209 - 1 = 119.38% | equal |
| 8 | 5b | NT dots 0.024 and 0.049 | `long_term_regions-3.csv` zone 60 ratio 0.024 and 0.049 | equal |
| 9 | 6 | Wet Tropics 1 in 20 whisker 0.430 to 0.677 | `shocks_ranges_wide_zones.csv` 0.430, 0.677 | equal |
| 10 | 7 | Wet Tropics beef carcase, short, -21.5 (label -22) | `method_effects_by_region-3.csv` -21.5 | equal |
| 11 | 8 | Wet Tropics circle area 4.195 pt2 = 29,962 x 1.4e-4 | `movers-3.csv` 285,138 - 315,100 = -29,962 | proportional, equal |
| 12 | S6 | Wet Tropics, fuel-csiro-340 long, dot at 0.23721 | `scenarios_2025-fixed.csv` 67,638 / 285,138 | equal |

Full sweeps (beyond the ten):

* **Figure 1.** Ranges 36.3 to 45.8 (13 choices; p5 36,332,875, p95 45,763,902) and 31.1 to 49.2 (19 choices; 31,115,433 and 49,169,829); bases 33.3 (2011) and 41.5 (2025). All hold.
* **Figure 2.** All 53 arrows equal the movers ratios (one end, Alinytjara Wilurara 2025, floored at 0.001). Eight flips, bold. Verdicts against `regional_flips-3_wide.csv` (term short): SA Arid Lands holds (blue, diamond, open because land-definition flag); Wet Tropics, Desert Channels (open; land definition and older boundary), Mackay Whitsunday, Rangelands, North Tasmania, Southern Gulf (open; land definition) and Corangamite do not hold (orange). All eight match the csv.
* **Figure 3.** All 954 cells (53 regions x 9 columns x 2 terms) equal 100 x `shapley_mean` / region cap2011 of the same preset (clipped at +-50 for colour). They are the all-orderings average: 306 cells would differ by more than half a point on the forward walk. The eight layers sum to the total within 2 people everywhere.
* **Figure 4.** Both lines and both diamonds equal `scale_curve.csv`; the four partition bars equal `scale_partition_summary.csv` grouping `uniform` p5 and p95 (2025 short 51.94 to 122.49; 2011 short 55.08 to 118.57; 2025 long 35.60 to 61.24; 2011 long 31.47 to 53.63).
* **Figure 5b.** All 106 dots equal the `ratio` column (nine at the 0.01 floor).
* **Figure 6.** All 159 whiskers equal `capacity_over_population_p5` and `_p95` of `shocks_ranges_wide_zones.csv` (short, 2025-fixed); three (Alinytjara Wilurara) sit at the floor. Panel counts 16, 21, 24 recomputed.
* **Figure 7.** All 1,060 cells equal `method_effects_by_region-3.csv` (vintage 2025), clipped at +-40 for colour; 20 cells are blank (Alinytjara Wilurara, short and long: the builder's report says 10).
* **Figure 8.** Circle area divided by |population less capacity| is 1.4e-4 for 43 of 53 circles: proportional. The other 10 (|excess| under 28,571 people: Kangaroo Island, North West Tasmania, SA Arid Lands, Cape York, Southern Gulf, East Gippsland, North East Vic, Rangelands, Corangamite, Alinytjara Wilurara) are drawn at a fixed minimum of 4 pt2 and are not proportional. Colour sign right for all 53 (16 red, 37 blue).
* **Figure S6.** Tip counts recomputed for all ten scenarios in both terms equal `scenarios_by_region.csv` (2025-fixed); none in the short term, as the caption says.

## Step 2: design rules (PNGs opened)

Print sizes: Figure 1 is 90 x 80 mm; the rest 190 mm wide; all 300 dpi. Every text object is 7 pt or larger (smallest found 7.0 in each figure). No em dash, en dash or minus sign character in any label or caption (the SVGs store text as paths, so I checked the text of every drawn object and the script sources instead of grepping the SVGs, which would pass trivially). One axis per chart in all; Figure 5 is two panels, one axis each. Categorical colours are slots 1 and 2 only (blue, orange) plus greys. Region labels in Figures 2, 3, 6, 7: no collisions or overflow (the overlaps my box test found in Figures 3 and 7 are the boxes of the 50-degree column labels, not the glyphs; the images are clean).

Greyscale (Pillow `convert('L')`): blue 107, orange 137, muted grey 135; diverging map: red pole 119, blue pole 71, neutral 239; at +-20 the map gives 179 (red side) and 154 (blue side).

* Year pairs (Figures 1, 4, 5b, 6) differ by 30 grey levels with the same marker: distinguishable side by side, weak where dots overlap.
* Figure 2: colour carries the verdict and the marker shape repeats it (diamond holds, circle does not); the year is position (small dot 2011, large marker 2025, arrow direction). It reads for the three long arrows; for the five flips near 1 (Mackay Whitsunday, North Tasmania, Wet Tropics, Rangelands, Corangamite) the arrow and 2011 dot are mostly hidden under the 2025 marker, so direction is hard to see. In greyscale the orange flips (137) match the grey non-flips (135); bold names and marker size still separate them.
* Diverging Figures 3, 7, 8: in greyscale both arms darken away from the midpoint, so sign is lost for unlabelled cells and circles (-40 reads near +25). The arms are also unbalanced (red pole slot 8, light; blue pole sequential step 600, dark), which the palette's "equal steps per arm" rule does not allow.
* S6: orange tippers (137) match the grey dots (135); the larger size, ring and name list carry them.

## Step 3: captions and claims rows

`figures.csv` caption checks: see the table. Claims: `finalize_figures_csv.py` lists a row when its `output_file` equals a source csv. That misses rows whose `output_file` names the pre-"-3" file and lists rows whose numbers are not drawn. Figure 1 still carries `CLAIMS_PLACEHOLDER` in `figures.csv` (it appears the Figure 1 script was rerun after the finaliser).

## Per-figure verdicts

| Figure | Data | Design | Caption | Claims rows |
|---|---|---|---|---|
| 1 | pass | pass | **fail**: says the 2025 bars are "over 2,000 draws", but the 13-choice band is 1,000 draws (`variant=existing`, `draws=1000`; Supplementary S4 says the same); "(13-choice basis)" for the 2011 value is not true of anything: 2011 was not sampled. Suggested: "The 2011 value is the base case of the corrected 2011 release with ABS populations; 2011 inputs were not sampled, so it has no range. The thin line is the 19-choice range (2,000 draws), the thick band the earlier 13-choice range (1,000 draws)." | **fail**: `CLAIMS_PLACEHOLDER`. Rows that hold: A001 (33.3), A003 (41.5), A163 (1.49), A027 (31.1 to 49.2). 36.3 to 45.8 has no live Paper A row (Supplementary S4 table only). |
| 2 | pass | pass, with notes: blue and orange mean verdict here but year in Figures 1, 4, 5, 6 (the builder says so; I would use other encodings or say it in the caption); five short flip arrows hidden under their markers | **fail** (small): no floor sentence, but Alinytjara Wilurara 2025 is drawn at the 0.001 edge (the builder's report says each caption states its floor) | Hold: A420, A042, A043 (6 net, derivable), A057 in part (SA Arid Lands +26 drawn). Do not hold: A041, A421 (long term, not drawn), A339 (description), A422 and A067 (not drawn). Missing: A061 (+464, +456, +441 are in the column; `output_file` is `comparison_2025/movers.csv`). |
| 3 | pass (954 cells; all-orderings average, not forward walk) | **fail**: clipped labels "+1.2k", "+1.5k", "+1.9k" mean 1,200% to 1,900% but read as thousand people (write "+1,200" or "+1200%"); greyscale loses sign; arms unbalanced | pass. The paper must change both the placeholder and the sentence "Figure 3 gives ... on the forward walk" to "the average over all orderings" | Hold: A450 (recounted from the averages: short 42, 7, 4; long 31, 20, 1, 1). A372 to A388 are national people values or forward/reverse gaps not drawn (the figure has regions only, in %): do not hold. A057, A067 do not hold. |
| 4 | pass | pass (minor: the legend swatch for the bars is grey while the bars are drawn in year colours) | **fail**: the caption and legend say the bars are "random groupings of the SA2s into 7 groups"; `scale_partition.mjs` and A459 say they are 200 random groupings of the 53 regions into 7 groups. The caption must also say a mixed group takes the yields of the state with most of its cropland, which can lift the sum above 100% (A459: the median depends on that rule and "is not quoted in the paper"; the bars draw that same 51.9 to 122.5) | Hold: A015, A016, A017, A018, A074, A075, A120. A458 (national yield vector) not drawn. A459 conflicts with drawing the band (see caption). A076 to A109 not checked one by one. |
| 5 | pass | **fail** (small items): panel a bars use the 2011 blue next to panel b where blue means 2011 (use one ink grey); wrapping splits ranges ("0.12 to / 0.9", "0 / to 1") and doubles brackets ("(years) (1 to 100)"); "capacity equals population" sits at the left edge of panel b, not at the line at 1; at the floor the 2011 dot hides under the 2025 dot | pass | Hold: A417 (18 under, 35 over in 2011). Missing: A152 to A162 (lever values; `output_file` is `long_term_levers.csv`; A152's 34.3 equals the -3 file's 34,274,878). |
| 6 | pass | pass (greyscale weak: same marker for both years) | **fail** (small): does not say short term; does not point to Figure S6 for the scenarios | Hold: A370 (4, recomputed), A402 for 21 and 24 (panel titles). |
| 7 | pass (1,060 cells) | pass, with the greyscale and arm-balance note of Figure 3 (labels at 10% or more carry the sign) | **fail**: says nothing of the blank Alinytjara Wilurara row | **fail**: "none matched", but A294 to A303 exist (`output_file` is `method_effects_by_region.csv`); A294 (Wet Tropics -21.5, drawn -22) and A298 (Swan +22.6, Southern Gulf +17.8, Mackay Whitsunday +15; drawn +23, +18, +15) hold. |
| 8 | pass for 43 circles; 10 drawn at a minimum size | **fail**: east-coast leader lines cross (Hawkesbury-Nepean-Sydney's crosses Central West NSW's and Lachlan's; the two Border Rivers leaders cross), the Border Rvs Maranoa-Balonne label crowds the 5 million legend circle; greyscale loses sign for unlabelled circles | **fail**: does not say circles under about 29,000 people are drawn at a minimum size | **fail**: A057, A067 do not hold (SA Arid Lands is neither labelled nor drawn to scale). No register row found for the labelled excesses (+5.4, +5.4, +3.8, +2.3, +1.4; -1.6, -1.6, -1.4, -1.3, -1.3 million). |
| S6 | pass (all tip counts) | pass, with notes: rows are file codes ("fuel csiro 340", "waste target 6") not names; draw order depends on the hash seed | **fail** (small): the scenario codes are not defined; the reference counts (16 short, 32 long over capacity) would help | A201 to A227 and A264 are national changes, not drawn: do not hold as figure claims. A202's 16 and 32 can be counted from the reference row. |

Weakness of the `--check` design (not a fail): the "plotted" value is the script's own variable, not the drawn artist, and three of the "second routes" are restatements (Figure 7 reads the same cell by splitting the line text; Figures 3 and 5 re-derive by algebra on the same rows). They do fail on a planted expected value, as the brief asks.

## Step 4: the builder's departures

1. **S6 split out.** Right. Figure 6 already holds 53 rows by three return periods with whiskers; eleven scenario rows would overload it, and the per-region scenario values are in `results/scenarios_2025-fixed.csv`, not `scenarios_by_region.csv` (national figures and counts only, as the builder says). The Figure 6 caption must say "The named scenarios by region are in Supplementary Figure S6", and the paper placeholder ("with the named scenarios by region on 2025 data") must drop that clause. S6's caption must name the scenarios in words.
2. **Figure 6 at three return periods.** Right: `shocks_ranges_wide_zones.csv` has ranges only at 1, 10 and 20 years, so the other three could have no whiskers. The caption already says the 1-in-5, 50 and 100 results are in the csv; add "short term" and "ranges exist at these three return periods only".
3. **Figure 4's partition bar at the State level only.** Right as to placement: the summary holds only groupings into 7 (the state count), so a bar at the State level is all the data supports. Wrong as to label: the bars are random groupings of the 53 regions, not of the SA2s. And A459 records that this range depends on the mixed-group yield rule and is not quoted in the paper; drawing it puts that number in the paper. Either draw the `uniform_national_yield_reference` range beside it, or keep it with a caption that says: "200 random groupings of the 53 regions into 7 groups, a group taking the yields of the state with most of its cropland; this rule can lift the sum above 100% and the range depends on it."
4. **Figure 7's blank Alinytjara Wilurara cells.** Right to leave blank: the 2025 published capacity is 0 (thousand), so a percentage of it is not defined (the older plot drew it as 0, which states a value that does not exist). It is 20 cells, both terms, not 10. The caption must say: "Alinytjara Wilurara is blank: its 2025 published-method capacity is about zero, so no percentage is defined."

## Register rows touched

None. No file in `qa/claims_register.csv`, `results/`, `releases/` or the paper was changed.

## Rerun

Scratch harness: `/tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v56a/harness.py` runs a scratch copy of a figure script and pickles every axis's artists (`python3 -B harness.py <scratch figs dir> <script>.py <out.pkl>`); the comparisons were inline Python reading those pickles and the named csv files. Checks: `python3 -I -B analysis/figures_2025/paper_A/<script>.py --check [--expect X]` from the repository root.
