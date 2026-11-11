# B83 report: National Food Waste Strategy 2017 (L230) and Baseline 2019 executive summary (L231)

Both files are the documents their rows name. The sha256 of each PDF matches the register. The Strategy is "National Food Waste Strategy: Halving Australia's Food Waste by 2030", Commonwealth of Australia, November 2017, 54 pages (cover and PDF 2). The summary is "National Food Waste Baseline, Final assessment report, Executive Summary", 20 March 2019, 4 PDF pages holding printed pages 3 to 8. Page citations give the PDF page first, then the printed page where one exists. In the Strategy, printed page = PDF page minus 6.

## Figures

| Value | Unit | Year | Page |
|---|---|---|---|
| Goal: halve food waste | by 2030 | 2030 | Strategy cover; PDF 9 (printed 3); PDF 24 (printed 18) gives "50 per cent reduction" |
| Food waste defined across "the entire supply and consumption chain" | definition | 2017 | Strategy PDF 14 (printed 8) |
| UN Target 12.3 ("halve per capita food waste at the retail and consumer levels and reduce food losses along production and supply chains") | quoted sidebar | 2015 UN text | Strategy PDF 9 (printed 3); the text aligns with SDG 12, not 12.3 by name |
| Baseline tonnage the Strategy cites | none of its own | n/a | Strategy has no whole-chain tonnage |
| Closest tonnage: over 5.3 Mt wasted from households and commercial and industrial | Mt a year | no year printed; source Blue Environment 2016 | Strategy PDF 12 (printed 6); source note PDF 48 |
| Households 3.1 Mt edible; commercial and industrial 2.2 Mt | Mt a year | no year printed | Strategy PDF 12 |
| 7.6 million tonnes of carbon dioxide equivalent from landfilled food waste | Mt CO2e | 2014-15 | Strategy PDF 12; not a food waste tonnage |
| Cost to the economy about $20 billion | $ a year | no year | Strategy PDF 7, 9, 12 |
| Four priority areas: policy support, business improvements, market development, behaviour change | list | 2017 | Strategy PDF 23 (printed 17) |
| Baseline study committed ($370,000 from the National Environment Science Program) | commitment | 2017 | Strategy PDF 7 (foreword), 10, 24, 37 (printed 31) |
| Total food waste 7.3 Mt (Table 1 total 7,320 kt) | Mt | 2016/17 | Baseline PDF 1 (printed 3); Table 1 PDF 3 (printed 6) |
| Per person 298 kg (297.7 in Table 1); population 24.59 million | kg a person | 2016/17 | Baseline PDF 1 (printed 3) and Table 1 |
| Primary production 2,270 kt (31%) | kt | 2016/17 | Table 1 PDF 3; Figure 1 PDF 1 |
| Manufacturing 1,758 kt (24%) | kt | 2016/17 | same |
| Wholesale 27 kt (0.4%) | kt | 2016/17 | same |
| Retail 232 kt (3%) | kt | 2016/17 | same |
| Hospitality and food services 324 kt (4%) | kt | 2016/17 | same |
| Institutions 209 kt (3%) | kt | 2016/17 | same |
| Households 2,500 kt (34%) | kt | 2016/17 | same |
| Households plus primary production 65% | share | 2016/17 | Baseline PDF 1 |
| Recycled 1.2 Mt, recovered 2.9 Mt, disposed 3.2 Mt | Mt | 2016/17 | Baseline PDF 1 |
| Animal feed 3,934 kt and food rescue 48 kt, counted as food outcomes, outside the 7,320 kt | kt | 2016/17 | Table 1 PDF 3; PDF 2 |
| Excluded: sugarcane bagasse, 11 Mt | Mt | 2016/17 | Baseline PDF 3 (printed 6) |
| Method: consultation of more than 300 organisations (March to June 2018), 91 gave data, modelled to national scale by "best fit" per sector, adapting the FLW Standard, UK, EU methods | method | 2018 | Baseline PDF 4 (printed 8); PDF 2 |
| Uncertainty: "moderate across the board", lower in some sectors; wholesale, retail, hospitality and some manufacturing data limited; transport reported separately; no interval given | stated confidence | 2016/17 | Baseline PDF 2 (printed 5) |

The Baseline summary prints the Figure 1 shares as scattered labels; the order of the labels matches the Table 1 tonnes and the computed shares (31, 24, 0.4, 3, 4, 3, 34).

## Scope finding for decision 44

The Strategy's halving is whole-chain, not retail-and-consumer.

- The goal is to halve "food waste" (cover, PDF 9, PDF 24), and the Strategy defines food waste as generated "across the entire supply and consumption chain" (PDF 14, printed 8).
- The Baseline summary states: "The Strategy sets the objective to halve food waste along the supply and consumption chain by 2030" (PDF 1), and that Australia "has adopted a broad approach, both to the definition of food waste and the scope of the food supply and consumption chain" (PDF 3 to 4), after quoting Target 12.3 as retail and consumer levels (PDF 3).
- The retail-and-consumer wording is the UN target, quoted in a sidebar of the Strategy (PDF 9). The Strategy does not adopt that wording as its own goal; it says it aligns with SDG 12.
- Limit of the finding: the Strategy does not say, stage by stage, that the 50 per cent applies to each stage. It states a national goal on a whole-chain definition. It gives no baseline year or tonnage for the goal.

Relation of 7.3 Mt and 7.6 Mt: 7.3 Mt is the Arcadis Baseline (2016-17), confirmed. The 7.6 Mt on L242 is from the 2021 Feasibility Study update (2018-19 data per the README; L242's page does not state the year). They are different projects' estimates. Neither is in the Strategy. The Strategy's own "7.6" is carbon dioxide equivalent and must not be mixed up with it.

## Flags

- `analysis/waste_2025/README.md`: line 20 ("halve food waste across the whole chain by 2030") is supported by these documents. Line 10 ("the national strategy target is a 50% cut") is supported (PDF 24, 38). Lines 65 to 70 call a halving of the 12% retail-and-consumer setting to 6% "the national target"; that is a model choice mirroring Target 12.3, because the national target is whole-chain. Decision 44's wording carries the same mix-up. The README's stage split for 7.6 Mt (retail 7%) is from the 2021 update; the 2019 split has retail 3%, so the two splits must not be mixed.
- Paper A scope, `papers/A_results/SECTION_SCOPE.md` line 636 (A11.3 item 4): "the national target as halving the retail-and-consumer avoidable share (decision 44)" is not what the Strategy says. Suggest: the national target is to halve food waste across the whole chain; the model's 6% setting applies the same proportional cut to the retail-and-consumer share, which matches the UN Target 12.3 scope. Line 698 still says the Strategy and Baseline are "not registered"; they are L230 and L231 now.
- Decision 44 itself (`qa/DECISIONS.md`, row 44) needs a wording change for Murray; this reader did not edit it.

## Rows touched

L230 and L231 in `qa/literature_register.csv`: what_taken (89 words each), read_or_reported "read (B83 targeted)", status "self-checked (B83)", notes extended. Checks: 242 rows, 12 columns on every row, parses, no em dashes, 243 CRLF line endings as before, only lines 231 and 232 differ from the prior file.

## Wrong-value check

EXAMPLE of a wrong figure, not a finding: "households 3,500 kt in 2016/17". The document prints 2,500 kt (Table 1, PDF 3); a reader who took 3,500 would have households at 48% of the total instead of 34%.
