# Irrigation share review

**Question.** The dashboard's irrigation parameter is irrigated area over all farmland, and the
model applies a flat 55 percent yield uplift in proportion to it. Is that the right share to drive
a yield uplift?

**Finding.** No, not as a definition. Farmland is dominated by rangeland grazing, which is almost
never irrigated, while the uplift acts on crops, which are irrigated far more often and unevenly.
The 2011 defaults still reproduce the original ABS yields, so the baseline is not distorted. The
distortion is in what the slider means when a user moves it.

Source: ABS Water Use on Australian Farms 2020-21, the last edition. Figures are 2020-21, not
2006 to 2010, so read them for scale and ranking only. Script `irrigation_shares.py`; results for
all regions in `irrigation_shares_2020-21.csv`.

| Region | Watered share of all farmland | Watered share of cropped land |
|---|---|---|
| Australia | 0.5% | 4.6% |
| Murray | 5.8% | 13.2% |
| South East Queensland | 3.9% | 32.8% |

| Crop group, Australia | Share of area watered |
|---|---|
| Cereals excluding rice | 1.6% |
| Cotton | 72% |
| Sugar cane | 39% |
| Vegetables | 77% |
| Fruit and nuts | 87% |
| Rice | 100% |
| Grapes | 92% |

**Consequences.** At zero irrigation the model removes under half a percent of national yield,
although horticulture and cotton depend on water. At 100 percent it adds 55 percent to every crop,
cereals included, and the 100 percent end means irrigating all farmland.

**Recommended fix** (Workstream E, compared on its own after the baseline comparison is recorded,
never during the data refresh):

1. Define the slider as the share of cropped land irrigated, with defaults by crop group from the ABS data.
2. Apply the uplift by crop group, using ABS irrigated and non-irrigated yields where published.
3. Cap the slider by regional water availability.
4. Treat the 55 percent, which is output per farm, as an assumption with a sensitivity range.

The thesis documents the zero-irrigation adjustment in section 8.3.9. What is missing is the
formula and the shares used for it; see `../yield_conversion/` for the reconstruction.
