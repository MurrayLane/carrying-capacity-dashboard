# Verifier brief V02: an independent rebuild of the HALF index for Australia

You are an independent checker doing a second implementation. You receive the method's published description and the data, and nothing else. Do NOT open `analysis/method_tests_2025/half_index.py`, `analysis/method_tests_2025/README.md`, `qa/claims_register.csv`, `papers/`, or `HANDOFF.md`: they contain an earlier implementation and its results, and your value must be reached without them. If you open one by accident, say so in the report.

Hard limits: read only inside /home/user/carrying-capacity-dashboard and /home/user/carrying-capacity-models; write only under /tmp/claude-0/-home-user/31136410-cd0a-5a0c-99b8-c10608414678/scratchpad/v02/ (create it). No git changes, no subagents, no network. Plain language; no time words.

## Requirement
From the method described in Alexander, Brown, Arneth, Finnigan and Rounsevell (2016), "Human appropriation of land for food: the role of diet", Global Environmental Change 41: 88-98, and its supplementary information, compute the HALF index (the land the world would need if everyone ate a country's diet, as a percentage of the world's land area) for (a) the world average diet and (b) Australia, on 2011 data; and then (c) Australia on the mean of 2021 to 2023. Report your values and your reading of the paper's own 2011 values for the world and Australia (from the paper's text or its Table S5), and the difference.

## Materials
* The paper: `/home/user/carrying-capacity-models/Literature review/Alexander2016.pdf`; the supplementary information: `/home/user/carrying-capacity-models/Literature review/Alexander2016_SI.pdf` (use `pdftotext -layout`). Read the Method section (2.1 to 2.3), Table 1 (feed conversion ratios) and the SI worked examples (soybean area allocation, poultry feed, bovine feed and pasture) and Table S4 (allocation ratios for processed commodities). Follow them as written; where the paper leaves a choice open, make it and state it.
* Data, FAOSTAT extracts already cut to what is needed (header `Area,Item,Element,Year,Unit,Value`): `analysis/method_tests_2025/half_fbs_countries.csv` (food balance sheet, World and seven countries, 2011 and 2021 to 2023: production, imports, exports, stock variation, feed, seed, losses, processing, other uses, food, residuals, population); `analysis/method_tests_2025/half_qcl_world.csv` (world area harvested and production by crop, same years); `analysis/method_tests_2025/half_landuse.csv` (world and Australian land areas: cropland, permanent meadows and pastures, land area, and others). Dry-matter contents of feeds are not in the data; take standard values and state them.
* Do not use any other data file in the repository.

## Report format
Your HALF values (world 2011, Australia 2011, Australia 2021-23) with the per-person hectares behind them and the split between animal products and crops; the paper's values as you read them and the page or table; the differences in percent; every choice you made where the paper was open (list them); what in your implementation could be wrong and how you would detect it; anything surprising in the paper or the data.
