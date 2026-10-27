# Organic yields: how the 2011 factors were made, and the update (SCOPE.md E5)

`organic_factors.py` writes `data/2025/organic_factors.json`; release `2025-organic` applies it as cell overrides on the 2011 workbook.

## How the 2011 factors were made (recovered from the archive)

* `Organic/Organic comparisons for paper.xls`, sheet `yield-final`: 40 studies, rows of organic yield as a percentage of conventional, by crop. Yield!G of the model is the **mean over the studies** for the 14 crops with three or more
  (wheat 19 studies, maize 12, potatoes 10, barley 8, soybeans 8, oats 7, tomatoes 7, dairy milk 6, field beans 5, field peas 4, carrots 4, cabbages 3, apples 3, rye 3).
  Every other row gets **0.808**, the mean of all 52 crop means (0.8083).
* The 2% default organic share is also a constant inside the workbook: `Yield!E2 = Settings!B15 - 2%`. The ABS yields already contain the 2% of organic land, so a yield is multiplied by
  1 - (organic share - 2%) x (1 - factor): 1 at the default, and for the long-term settings (100% organic) a penalty of 98% of (1 - factor).
* The paper (draft, February 2016) states the 2% as "just over 12 million hectares".

## What the newer evidence says

| Source | What | Result |
|---|---|---|
| Ponisio et al. 2015, Proc R Soc B 282: 20141396 (115 studies, 1,071 comparisons) | Bayesian meta-analysis | Organic yields 19.2% lower: ratio **0.808** (95% interval 0.771 to 0.845). Conventional higher for every crop type; no significant difference between legumes and non-legumes, perennials and annuals, developed and developing countries. Cereals show the biggest gap and are 53% of the comparisons. With diversification (multi-cropping, rotations) the gap falls to 9% and 8% |
| Kniss et al. 2016, PLoS ONE 11: e0161673 | Commercial yields of more than 10,000 US organic farms, 2014 (USDA Organic Survey) | Averaged over all crops **0.80**; wheat 0.66, soybean 0.68, maize 0.65, barley 0.76, oats 0.80; organic hay as good as or better than conventional; large differences between states within a crop |
| Seufert et al. 2012, Nature 485: 229 (66 studies, 316 comparisons) | Meta-analysis | Overall about 0.75; 5% lower for rain-fed legumes and perennials, 13% lower with best organic practice, 34% lower where the systems are most comparable; cereals the largest gap. **Crop-type ratios not retrieved** (the full text was not reachable) |
| de Ponti et al. 2012, Agricultural Systems 108: 1 | Meta-analysis | Overall 0.80; smallest gap in maize, largest in barley (secondary report). **Crop ratios not retrieved** |

The default 0.808 is the figure Ponisio et al. arrived at independently, and Kniss et al.'s commercial average is 0.80: the 2011 default stands.

## What the release changes

1. **Five crops** that have a commercial ratio in Kniss et al. move to the mean of the 2011 literature mean and that ratio (half weight each: the literature is mostly trials and paired farms, Kniss is what organic farmers harvested):
   wheat 0.694 to 0.677, oats 0.712 to 0.756, barley 0.578 to 0.669, maize 0.824 to 0.737, soybeans 0.884 to 0.782.
2. **The baseline constant** `Yield!E2` becomes `=Settings!B15-0.07`: the 2011 constant moves with the default organic share (7%, `analysis/consumption_2025/`), because the 2022-25 yields already include that organic land. Without
   this the new 7% default would have cost 1.0% of short-term capacity for no reason.
3. Nothing else: rows without three studies keep 0.808, and the crops with three or more but no new evidence keep their 2011 means.

## Effect

Australia, on the 2011 data: short-term, none (organic is at its baseline); long-term (100% organic), 9.43 to 9.47 million people. In the full 2025 data the long-term result is 12.31 million
(`analysis/comparison_2025/`). The factors matter far more when the organic share moves than at either default.

## Open

* Seufert et al. 2012 and de Ponti et al. 2012: the crop-type and crop-specific ratios would let the 40 older studies be replaced by meta-analytic estimates for every crop. Murray can supply the figures from the papers.
* Ponisio et al. 2015 report crop-type ratios in a figure only (cereals, fruits and nuts, oilseeds, roots and tubers, vegetables); their supplement gives the order but not the values.
* The Australian evidence is two studies (Ryan, Kitchen). Organic land in Australia is mostly extensive grazing; cropping is a small share.
