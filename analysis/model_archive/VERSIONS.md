# Timeline of the model versions

From the author's own log of updates (`Log of updates.xlsx`, in the private archive) and the save date and cached results of each
dated workbook. The capacity column is the Australian short-term carrying capacity stored in that workbook.

| Date | Change (from the log unless marked) | Online | Australian capacity | Workbook |
|---|---|---|---|---|
| 2012-03-23 | Dashboard publicly released: fuel 2,600 lt, biofuel 1%, timber 0.5 m3 | yes | 40,256,807 | `superceded/Carrying capacity dashboard model 120412.xls` and its neighbours (Nov 2011 to 11 Jun 2012 all give this figure) |
| 2012-04-03, 04-05 | Fixed a division by zero at 100% nature reserve; adjusted land figures for regions 32, 42, 45, 47 and 55 that gave negative non-agricultural land; reduced nature reserve in region 42 from 103% (ACLUMP reserve areas against ABS for the rest) | yes | unchanged | |
| 2012-06-08 | **Yields reduced to non-irrigation yields**, conversion changed to follow the user's irrigation choice (formulas in Yield D2, B4:B138, D4:D138, "as per Fix irrigation figures.xls", a file not in the archive); irrigation given a decimal place | yes | unchanged | `...model 080612.xls` |
| 2012-06-21 | Fuel 2,600 to 2,520 lt; biofuel 1% to 0.5% in the default file | yes | **40,439,187** | `...model 170612.xls`, `Results/1a.xls`; the state behind thesis Table 16 |
| 2012-07-16, 08-09 | Short-term and long-term buttons; new-look interface | yes | | `...model 210612.xls` (long-term defaults: timber 5, infrastructure 365) |
| 2012-08-28 | (workbook only) biofuel 0.5% in Settings | probably | 40,450,144 | `...model 260612.xls`; still a timber yield per region, timber default 0.5 |
| 2012-10-02 | **Timber modelling updated** (Settings B22 and B130, Base K348, Yield H138:BO138); default files: timber 1, long-term infrastructure 500 | **no** (as logged) | 40,450,144 (timber does not bind nationally) | `...model 021012.xls`, `Lane_Dashboard_model.xls(x)`; the model in the QUT repository snapshot |
| 2012-11-13 | `Totals.xls` saved: still the June 2012 results, not regenerated after 2 October | | 40,439,187 | `Totals.xls` (Nov 2012), same capacities as `Results/Totals.xls` (Jan 2014) |
| 2013-02-19 | (workbook only) development version: Base sheet restructured, recycling and waste inputs 10% | | 42,834,167 | `superceded/temp model.xls`; the submitted *Environmental Modelling & Software* manuscript (Sep 2013) quotes 42,834,167 |
| 2013-08-19 | Final standalone workbook | | 40,450,144 | `Lane_Dashboard_model.xlsx` |
| 2014-01-28 | (workbook only) "examination" copy: Recycle sheet redesigned, one Base link set to 0 | | 42,825,987 | `Lane_Dashboard_model_examination_280114.xlsx` |

## The live dashboard

Checked on 2026-10-27 (`check_live_dashboard.py`): `https://dashboard.carryingcapacity.com.au/` answers all 120 default cases of the baseline
identically to release `2011`, in the capacity and in every land-requirement figure, and its two default files are identical to `data/2011/`.
**The live dashboard runs release `2011`, the October 2012 timber update**, including the 12.5 kg long-term textiles default that the thesis
(Table 7) gives as 11.5. It cannot reproduce the 2015 and 2017 *Population and Environment* tables or thesis Table 16, which come from the
June 2012 model (release `2011-thesis`).

## What this changes

- The **October 2012 timber update was logged as not online**. Release `2011` is that model, taken from the QUT repository snapshot, and it
  matches the Ecological Modelling paper and the thesis text and Tables 7 and 14. The live dashboard runs it (checked 2026-10-27). When the public site received
  it is not recorded in the archive, so the release is described as the final model.
- The version the public site ran from 21 June 2012 until the update (if it was ever applied) is the June 2012 model: a timber yield per
  region, `K348` 0.3624, timber default 0.5. Release `2011-thesis` has that model with the inputs used for the thesis runs.
- Two development versions (Feb 2013 and Jan 2014) give about 42.8 million. They are not published results, except that the Feb 2013 one
  produced the worked example in the submitted manuscript. They are described here and are not releases.
- The log confirms the irrigation conversion date (8 June 2012) and that the original "Fix irrigation figures" file is not in the archive;
  the rule itself is reproduced exactly in `pipeline/yields/`.
