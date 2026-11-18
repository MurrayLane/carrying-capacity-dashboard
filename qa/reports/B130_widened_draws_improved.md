# B130: the widened Monte Carlo on the improved release (decision 125)

Builder report. Brief: `qa/briefs/B130_widened_draws_improved.md`. Release `2025-improved`, Australia, both presets, 2,000 Latin hypercube draws, seed 20261027, `MC_LONG=1 MC_WIDE=1 MC_ZONES=national`. No git, no subagents, no network. No register row, frozen release, corrected-release file or existing output was edited.

## 1. The figures (Australia, millions of people)

| | Short term | Long term |
|---|---|---|
| **Improved, widened (18 choices, 2,000 draws): 5th to 95th percentile** | **37.9 to 60.0, factor 1.58** | **15.7 to 22.1, factor 1.41** |
| Improved, widened: min to max | 32.0 to 69.5, factor 2.17 | 15.1 to 23.0, factor 1.53 |
| Improved, widened: median (base) | 48.1 (53.6) | 18.5 (18.5) |
| Improved, 13 choices, 1,000 draws (5th to 95th) | 46.2 to 60.1, factor 1.30 | 15.9 to 19.4, factor 1.22 |
| Improved, 13 choices: min to max | 43.6 to 63.1, factor 1.45 | 14.7 to 19.6, factor 1.33 |
| Corrected, widened (19 choices, 2,000 draws): 5th to 95th | 31.1 to 49.2, factor 1.58 | 13.3 to 18.8, factor 1.41 |
| Corrected, widened: min to max | 26.2 to 58.1, factor 2.22 | 12.4 to 19.9, factor 1.60 |
| Corrected, 13 choices (5th to 95th) | 36.3 to 45.8, factor 1.26 | 13.4 to 16.5, factor 1.23 |

The top of the short-term range does not move (60.1 to 60.0); the bottom falls by 8.3 million. The improved base sits near the top of the meat-window and meat-calibration choices, so each added choice can only pull the figures down. The short-term median (48.1) is below the base (53.6); the long-term median equals the base. The 5th to 95th factors (1.58 and 1.41) equal the corrected release's.

## 2. The six added choices: one has no meaning on this release

**The retail and consumer loss-factor weight (lossaus) has no meaning on the improved release.** The release already applies `methods/loss-factors-australia`; the choice is a weight between the thesis's US factors and that module's Australian factors, so with the module applied there is nothing to weight (the script stopped on it, by design). It is left out: 18 choices are drawn, all 18 vary (the long-term feeding benchmark, `lbench`, has an effect on this release, unlike on the corrected one). The other five (avoidable waste, land source, meat calibration, energy requirement, trend window) are defined the same way here. Checks of their inputs in the script pass on this release (the land raster variant matches the release's infrastructure, reserve and total area in every zone; `meat_nocal` changes only rows 95 and 98; `gt_field_2016` changes only field-crop rows). The dairy-good-land module sets only the milk yield (locked row 97), not land, so the raster land choice is a plain source swap.

Said in: the header comment line of `results/ranges_2025-improved_wide.csv`, the `monte_carlo.mjs` stderr and comment, and `analysis/sensitivity_2025/README.md` (new section "The widened draws on the improved release (B130, decision 125)").

Base-value check: with every added choice at its base value the run gives the release, 53,643,731 short term and 18,496,334 long term (`results/2025-improved.csv`), to the person. One at a time (short, long): land raster 62.9 and 21.7; meat calibration off 49.2 and 17.7; energy 1.286 42.5 (long unchanged); waste 14% 52.1 (unchanged); trend window 53.6 and 18.5.

## 3. Sobol indices (top five by total order; full table of 18 in `sobol_2025-improved.csv`)

Design as for the corrected release: A, B and AB_j of 2,000 rows, 40,000 runs, the Saltelli (2010) first order with f(B) centred and the Jansen (1999) total order, 1,000 bootstrap resamples (seed 20261118).

| Setting | Choice | First order | Total order |
|---|---|---|---|
| Short | land source | 32.8% (30.0 to 35.9) | 35.0% (33.0 to 37.1) |
| Short | meat window | 29.9% (27.0 to 32.8) | 30.2% (28.3 to 32.2) |
| Short | energy requirement | 21.8% (18.8 to 24.4) | 25.5% (23.9 to 27.3) |
| Short | red meat share | 5.7% (4.3 to 7.1) | 6.3% (5.9 to 6.7) |
| Short | meat calibration | 2.1% (0.9 to 3.3) | 3.5% (3.3 to 3.8) |
| Long | land source | 62.9% (58.7 to 66.8) | 66.4% (62.5 to 70.2) |
| Long | resilience table | 19.5% (17.0 to 22.0) | 19.5% (18.5 to 20.6) |
| Long | meat window | 14.2% (12.0 to 16.5) | 15.4% (14.5 to 16.5) |
| Long | meat calibration | 1.5% (0.8 to 2.2) | 1.5% (1.4 to 1.6) |
| Long | long-term liquid fuel | 0.9% (0.2 to 1.7) | 1.2% (1.0 to 1.5) |

First-order sums are 94% short term and 100% long term; total-order sums 102% and 105%. Interactions are a little larger than on the corrected release (land source, short term: 33% first order, 35% total).

## 4. Files written

* `analysis/sensitivity_2025/monte_carlo.mjs`: under `MC_WIDE=1`, a release that already applies `loss-factors-australia` no longer stops; it leaves `lossaus` out (`NOLOSS`). Byte check against the unedited script: 20 draws on `2025-fixed` with `MC_LONG=1 MC_WIDE=1 MC_ZONES=national`, `cmp` identical.
* `analysis/sensitivity_2025/sobol_wide.py`, `check_wide.py`: take `MC_RELEASE` (default `2025-fixed`), skip a leading `#` line. With the variable unset, `sobol_wide.py` run in a scratch copy on the corrected draws reproduces `ranges_2025-fixed_wide.csv`, `sobol_2025-fixed.csv`, `monte_carlo_2025-fixed_wide.md` and the draws file byte for byte.
* New: `analysis/sensitivity_2025/monte_carlo_draws_2025-improved_wide.csv` (40,000 runs), `sobol_2025-improved.csv`, `monte_carlo_2025-improved_wide.md`, `results/ranges_2025-improved_wide.csv` (same columns as the corrected file; `influence_lossaus` empty; first line a `#` comment).
* `analysis/sensitivity_2025/README.md`: one section appended; the earlier text is unchanged byte for byte.
* `analysis/method_tests_2025/cross_method.py`, `design_choices.py` (improved range from the new file; `design_choices.py` also adds an improved Monte Carlo row); regenerated `cross_method.csv`, `model_entry.csv`, `design_choices.csv` (`ladder.csv` is rewritten by `design_choices.py` with the same inputs); `README.md` (three blocks by `make_readme_tables.py --write --only model_entry|cross_method|design_choices`, plus the hand edits below).

## 5. Cells changed

| File; row; column | Before | After |
|---|---|---|
| `model_entry.csv`; 2025-improved; short term, 5th to 95th | 46.2 to 60.1 | 37.9 to 60.0 |
| `model_entry.csv`; 2025-improved; long term, 5th to 95th | 15.9 to 19.4 | 15.7 to 22.1 |
| `cross_method.csv`; The model, improved; reading, low, high | 53.6 (46.2 to 60.1); 46.2; 60.1 | 53.6 (37.9 to 60.0); 37.9; 60.0 |
| `cross_method.csv`; The model, improved; fidelity text | built on; range from the 13-choice draws (no widened draws exist for this release) | built on; range from the widened draws (18 choices, 2,000 draws, decision 125; the loss-factor choice has no meaning on this release) |
| `design_choices.csv`; new last row | none | Uncertainty (Monte Carlo); 5th to 95th percentile over 18 uncertain choices (the loss-factor choice has no meaning on this release; all 18 vary); 37.9; 60.0; 1.58; improved; results/ranges_2025-improved_wide.csv |
| `README.md` (method tests), model_entry block, improved row | 53.6 (46.2 to 60.1); 18.5 (15.9 to 19.4) | 53.6 (37.9 to 60.0); 18.5 (15.7 to 22.1) |
| same, cross_method block, "The model, improved" | 53.6 (46.2 to 60.1) | 53.6 (37.9 to 60.0) |
| same, three source-commit stamps | 6cec3a5 | 5b6d971 |
| same, hand text, heading of the model's entry | the other two rows on 1,000 draws and 13 choices | improved row on 2,000 draws and 18 choices; mirror alone on 13 |
| same, hand text, "What the comparison shows" | the improved range (46.2 to 60.1) contains none of them; long term range 15.9 to 19.4 | the improved range (37.9 to 60.0) contains Fearnside's 41.5 and the meat readings 40 to 41, not the 1-in-10 point (30.8); long term range 15.7 to 22.1 |
| same, hand text, reference-rows bullet | the improved model keeps its 13-choice range | says `cross_method_local.csv` is stale for the improved row and that the other two files print the new range |

The regeneration reverted one hand-patched cell (design_choices block, Uncertainty row, "13 uncertain choices", which the generator hard-codes at `make_readme_tables.py` line 343); I put B127's text back: "19 uncertain choices (18 drawn on this release)". A later regeneration reverts it again until that tool line changes (outside this brief).

## 6. Stale cells I did not regenerate (outside my write list)

* `analysis/method_tests_2025/cross_method_local.csv`, row "The model, improved": 53.6 (46.2 to 60.1), 46.2, 60.1, the ratios to the corrected and improved models, and the source text "13-choice". Written by `harmonised_lines.py`, which reads `cross_method.csv` and hard-codes the "13-choice" text (line 152). Rerunning it would move these cells.
* Paper B tables (`papers/B_methods/draft/B_s04-05.md` lines 132 and 140, `paper_B_draft1.md`), and the paper claims csv rows `B_s04-05_claims.csv` lines 94, 95 and 225 ("53.6 (46.2 to 60.1)", "18.5 (15.9 to 19.4)"): not touched. `supplementary.md` line 321 (Table S3 row 7, "2025-improved, 13 settings") stays true as a statement about the 13-choice run.
* `analysis/sensitivity_2025/README.md` lines 185 and 191, `HANDOFF.md` line 27, `PUBLICATIONS.md`: the 13-choice improved range, historical, unchanged.

## 7. Claim rows that move (register not edited)

Tier A (separated):

| Id | Tier | Before | After |
|---|---|---|---|
| B159 | A | "41.5 (31.1 to 49.2); 53.6 (46.2 to 60.1)" | "41.5 (31.1 to 49.2); 53.6 (37.9 to 60.0)" (improved entry; `cross_method.csv` row, source `results/ranges_2025-improved_wide.csv`) |
| B114 | A | improved short-term Monte Carlo range 46.2 to 60.1 (1,000 draws, 13 choices) | 37.9 to 60.0 if the widened range replaces the 13-choice range (as B112 did for the corrected one); else it stays, labelled 13 choices |

Tier B and C:

| Id | Tier | Before | After |
|---|---|---|---|
| B115 | B | improved long term 15.9 to 19.4 | 15.7 to 22.1 (same condition as B114) |
| B157 | B | "the improved range contains none of his points" | the improved widened range (37.9 to 60.0) contains the 41.5 average-year point; the 1-in-10 point (30.8) is below it; the long-term 18.9 lies inside 15.7 to 22.1 |

No other register row carries 46.2 to 60.1 or 15.9 to 19.4. Not moved: rows on the 13-choice improved run's own provenance (the file `results/ranges_2025-improved.csv` is unchanged).

**Register rows touched: none.**

## 8. Limits

* National only. The six added choices are drawn independently. Equal chances and uniform weights between two point estimates remain the author's judgement (README, B115 section).
* The meat-calibration shortcut was checked against full rebuilds on the corrected release only (B115). On the improved release only the base, the one-at-a-time values above and the input checks were run; no full rebuild through `zone_yields.py` and `livestock_zone.py`.
* One column fewer (lossaus) means the Latin hypercube columns after it (land, meatcal, energy, trendwin) are different draws from the corrected run's; the first 13 columns, drawn in the same order from the same seed, are the same as the corrected run's.

## 9. Corrected-release files untouched (`cmp` against copies taken before the run)

* `results/ranges_2025-fixed_wide.csv`: identical
* `analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv`: identical
* `analysis/sensitivity_2025/sobol_2025-fixed.csv`: identical

## Wrong-value check:

`MC_RELEASE=2025-improved python3 analysis/sensitivity_2025/check_wide.py` recomputes the range from the improved draws and compares the ranges file.

* The true figures pass (exit 0): `ok: 2000 draws; short 37.9 to 60.0 (1.58), min to max 32.0 to 69.5 (2.17); long 15.7 to 22.1 (1.41), min to max 15.1 to 23.0 (1.53)`.
* **Example of a deliberate wrong value** (the 13-choice figures quoted against the widened draws; exit 1):

```
$ MC_RELEASE=2025-improved python3 analysis/sensitivity_2025/check_wide.py short:p5=46.2 short:r595=1.30
short:p5: quoted 46.2, the draws give 37.9
short:r595: quoted 1.30, the draws give 1.58
```
