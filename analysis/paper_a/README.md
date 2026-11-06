# Analyses for Paper A (results), by section

One script per analysis, each reading `results/` and `analysis/comparison_2025/`; the outputs are the tables and figures of `papers/A_results/OUTLINE.md`. Corrected method (`2011-fixed` against `2025-fixed`) unless stated.

## Section 3 and 9: which regional status flips are real (`regional_flips.py`, `regional_flips.csv`)

Run: `python3 -I analysis/paper_a/regional_flips.py` from the repository root. The 53 regions (52 NRM regions and the Northern Territory), short and long term. A flip is a change in the sign of population minus capacity between 2011 and 2025. Each flip is tested three ways: the land-definition and older-boundary flags of `analysis/comparison_2025/movers.csv` (the capacity change is mostly the land layer, or the 2011 zone was drawn on an older boundary); robustness of the 2025 status to the 5th to 95th percentile of the Monte Carlo draws (the 2011 inputs were not sampled, so 2011 has no range); and both.

| | Regions over capacity 2011 | Over capacity 2025 | Flips | Land-definition or boundary artefacts | Not robust to the 2025 range | **Clean and robust** |
|---|---|---|---|---|---|---|
| Short term | 23 | 16 | 9 (8 over to under, 1 under to over) | 3 | 3 | **3** |
| Long term | 36 | 32 | 4 (all over to under) | 3 | 2 | **1** |

**Short-term flips.** Clean and robust: **Mackay Whitsunday, North Tasmania, North East Victoria** (all over to under). Land-definition artefacts: Desert Channels, Southern Gulf, SA Arid Lands. Not robust to the range: Wet Tropics, Rangelands (WA), and Corangamite (the one region that moves from under to over capacity).

**Long-term flips.** Clean and robust: **South West Queensland**. Artefacts: Desert Channels and SA Arid Lands (land definition), Northern and Yorke (older 2011 boundary). SA Arid Lands and Northern and Yorke are also not robust to the range.

**What this means for the paper.** The status-flip headline of the plan (eight regions over to under, one under to over) is three genuine flips in the short term and one in the long term. The net fall in the number of regions over capacity (23 to 16 short term, 36 to 32 long term) is more than the clean flips alone explain; the rest are the flagged and non-robust cases, so the count of regions over capacity is not itself a finding without the tests. Capital cities and the coast stay over capacity in both years.

**Limits.** Robustness is tested on the 2025 range only; a flip also needs its 2011 status to be robust and the 2011 inputs have no draws. The land-definition flag is the rule of `movers.csv` (the land layer alone moves capacity by more than 2 times or less than 0.5). The test of an artefact is on capacity, not on whether the population change is real.
