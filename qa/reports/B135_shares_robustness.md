# B135: the robustness table for the shares closed; the footprint's own accounting (decision 142)

Brief: `qa/briefs/B135_shares_robustness.md`. Read: R05b issues 1, 3, 5; B113; V39; `harmonised_lines.py` (not edited); `harmonised_comparison_lines.csv`; `cross_method_local.csv`; the README's harmonised section; register rows B270, B276, B277, B156, B046. No git, no network, no subagents.

## Headline: the ranges across variants

Core set of twelve variants (the base case, each method out, fish dropped, pasture-alone dropped, median centres, three land scale-up variants); shares of the log distance closed.

| | Line (a) | Line (b) |
|---|---|---|
| To the corrected model, 41.5 | -1.1% to 6.8% | 27.7% to 45.9% |
| To the model at 31.1, 41.5, 49.2, 53.6 | -1.2% to 7.8% | 23.2% to 52.8% |
| To the median of the method centres | -32.1% to -0.5% | 4.1% to 35.5% (9.4% to 35.5% without the combined scale-up variant) |
| To the geometric mean of the method centres | -27.4% to 1.4% | 5.9% to 32.0% |
| Energy balance alone | 8.2% | 8.2% |
| Footprint and HALF left out | 10.5% | 10.5% |
| Narrowing of SD of log method centres | widens in every variant but footprint and HALF out (7.7%); base -8.6% | 22.3% to 47.5% with the commodity balance in; -11.5% (widens) without it; base 31.8% |

R05b's scratch is reproduced: line (a) about -1% to 7%; line (b) 28% to 46% to the model, 9% to 36% to the median, 10.5% without the footprint and HALF. The one scratch row not reproduced exactly is the land scale-up: scratch 1.4% and 35.8%; classing the scaled energy readings as method gives 2.1% and 36.5%; dropping them gives 1.4% and 36.8%. Both are in the csv.

The base case reproduces the paper exactly (the script stops otherwise): 4.1% and 38.5% to 41.5; SD of log method centres 0.65 to 0.70 (a) and 0.65 to 0.44 (b), 31.8%; highest over lowest centre 6.22 to 6.95 (a) and 6.22 to 3.70 (b); the shares to the median (-4.9%, 16.0%) and geometric mean (-6.3%, 17.2%) agree with `harmonised_comparison_lines.csv`.

**Which single method "about a third" depends on:** the commodity balance. Left out, the line (b) spread of centres widens by 11.5% (0.236 to 0.263) instead of narrowing by 31.8%, because the footprint and HALF move from above the energy balance and people per hectare to below them. Every other single removal leaves a narrowing of 23% to 48%. The line (b) share to the model depends most on HALF (27.7% without it) and the footprint (31.1% without it); the energy balance pulls it down (45.9% without).

## Footprint accounting (decision 142)

Reading = FAO population (26.20 million) x output in world-average hectares / consumption in world-average hectares, per land type; the pooled reading is the consumption-weighted mean of the land-type ratios. Build 1: cropland 5.19 Mha consumed, 22.28 produced, ratio 4.29, reading 112.5; pasture 22.53 consumed, 46.35 produced, 2.06, 53.9; pooled 27.72 and 68.56, 2.47, 64.8. Build 3: 4.47 (117.0), 2.97 (77.9), 3.23 (84.6). The binding land type (B270): 53.9 to 77.9 million, 1.30 to 1.88 times the corrected model and 1.01 to 1.45 times the improved; the pooled 64.8 to 117.0 is 1.56 to 2.82 and 1.21 to 2.18. The pooled reading is higher because it lets the surplus of cropland output stand in for the smaller pasture surplus, while the binding reading holds each land type as its own constraint.

## Sentences the paper patch needs (not applied; papers/ untouched)

Section 5.11 and Table 6:
1. "Table 6 leads with the measures that need no reference point: the standard deviation of the log method centres and the highest over lowest centre, as run and harmonised; the distances to the corrected model, the median and the geometric mean of the method centres follow."
2. "At Australian productivity the footprint reads the population times the ratio of Australia's output to its consumption, each in world-average hectares, so it counts exports as the export-inclusive counts do; for build 1 the ratios are 4.29 for cropland, 2.06 for pasture and 2.47 pooled."
3. "Line (b) is the footprint's own accounting (a hectare counts at Australia's productivity, Wackernagel and Rees 1996, p. 78); the world-average readings on line (a) are a counterfactual, Australian hectares divided by world-average hectares."
4. "Under line (a) equalising the inputs closes about zero of the distance to the model: -1% to 7% across references at 31.1 to 53.6 million, each method left out, the fish reading dropped and other variants (4.1% as printed), and the spread of method centres does not narrow. Under line (b) it closes 28% to 46% of the distance to the corrected model (38.5% as printed; 23% to 53% across the four references) and 4% to 36% of the distance to the median of the method centres (16.0% as printed); without the footprint and HALF it closes 10.5%, so the line (b) closure is the productivity conversion of those two land indices."
5. "The spread of method centres narrows by about a third on line (b) (standard deviation of logs 0.65 to 0.44; highest over lowest 6.2 to 3.7), by 22% to 48% in every variant that keeps the commodity balance, and widens by 12% without it."
6. "The footprint read at its binding land type, 53.9 to 77.9 million (1.30 to 1.88 times the corrected model), sits beside the pooled 64.8 to 117.0; the pooled reading is higher because surplus cropland output offsets the pasture shortfall."
Abstract (s5): "Equalising the data the methods take closes about none of the distance to the model when the productivity basis is part of the method (-1% to 7%), and 28% to 46% when it is an input, almost all of it the footprint and HALF at Australian productivity."
Highlights (H2), within 85 characters: "Footprint and HALF at Australian productivity close most of their gap to the model" (82 characters).

## Claim rows that move (register not edited)

Tier A:
- B276; A; "4% (line a); 39% (line b)"; after: "about -1% to 7% (line a, to 41.5 across variants; 4.1% as printed); 28% to 46% (line b; 38.5% as printed); to the median of centres -32% to -0.5% (a), 4% to 36% (b)". The 0.59 to 1.42 input factors and the factor split do not move.
- B277; A; "SD of log centres 0.65 to 0.44, highest over lowest 6.2 to 3.7" (value unchanged); the statement gains: depends on the commodity balance (without it the spread widens 11.5%); 22% to 48% with it in.
- B156; A; values unchanged (65 to 211; 134 to 343; 12 to 41); no figure moves; the paper sentence on the footprint may cite the binding reading beside, which is Tier B (B270).
- B046; A; values unchanged (64.8 to 117.0 primary; 146.2 to 343.4 secondary); no figure moves.
Tier B:
- B270; B; values unchanged (53.9; 64.8; 112.5; 77.9; 84.6; 117.0); additions: pasture/cropland output over consumption ratios (4.29, 2.06, 2.47; 4.47, 2.97, 3.23); binding reading 53.9 to 77.9 is 1.30 to 1.88 times corrected and 1.01 to 1.45 times improved. New rows, for a later register job, would be needed for the robustness ranges and the ratios (the script and csv are the locators).
Register rows touched: none.

## Files changed
- Added `analysis/method_tests_2025/harmonised_robustness.py` (rerunnable, deterministic: two runs give identical md5 on both csv files).
- Added `analysis/method_tests_2025/harmonised_robustness.csv` (176 data rows).
- Added `analysis/method_tests_2025/harmonised_robustness_footprint.csv` (7 data rows).
- Appended one section to `analysis/method_tests_2025/README.md` (robustness table, ranges, footprint accounting, binding land type); no other text touched.
- Added this report.
`harmonised_lines.py`, its csv files, papers/ and qa/claims_register.csv untouched.

Wrong-value check: EXAMPLE only, a deliberately wrong value: asserting the line (b) share to 41.5 is 0.405 (40.5%) in place of 38.5% fails in the script's own base-case check (`measure(...)` returns 0.3854; AssertionError, 0.3853587...). The script's own assertions likewise stop on any base-case value other than 0.041 and 0.385.
