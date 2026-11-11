# Reading brief B66c: Paper A section 11: drought resilience, freight, import dependence (targeted reads)

Write only `qa/reports/B66c_readings.csv` and `qa/reports/B66c_readings.md`.

Rules. Plain language; no time words; no em dashes. Decision 33 applies: say what a paper does and what it finds; no verdicts on other authors' shortcomings. Do not edit `qa/literature_register.csv` or any file other than your two outputs. No git; no subagents; no network. The papers are on disk under `/home/user/carrying-capacity-models/Literature review/` at the `local_path` in each register row (drop the leading `carrying-capacity-models/`); use `pdftotext` (and `pdftotext -layout` for tables); a `.md` file is a full text rendered from PubMed Central and is read as is. Open each file and confirm first that it is the paper the row names (title, authors, year); if it is not, say so and stop on that row.

Each row carries a current characterisation: its `what_taken` text and the "why" line in its `notes` (from the B61 or B63 sweeps, written from the abstract or the record). Your job is to test that characterisation against the paper and record what the paper actually supports, with page numbers.

Depth. TARGETED: read the abstract, introduction, results summary, conclusions and any table or figure the characterisation rests on; enough to confirm or correct the line and take the one or two facts the paper is wanted for. FULL: read the whole paper; take every figure the paper is wanted for and the method and base year behind each. The list below says which.

Output 1: `qa/reports/B66c_readings.csv` with columns `id, file_ok, depth, holds, what_taken, figures, flags, notes`. `holds` is yes / partly / no (does the current characterisation hold?). `what_taken` is the new register text, at most 70 words, concrete, with page numbers. `figures` lists each number taken as "value; unit; base year; page". `flags` names anything that changes a claim in the papers or a line in `papers/A_results/OUTLINE.md` or `papers/B_methods/OUTLINE.md` (name the section), or "none". Quote page numbers from the PDF's own pagination.

Output 2: `qa/reports/B66c_readings.md`: one paragraph per paper (plain language, at most 120 words), then a closing list of flags, then the register rows you touched (all the ids below), then the words "Wrong-value check:" with one deliberate example of a characterisation that would NOT hold, so a checker can see the test can fail (mark it clearly as an example, not a finding).

Depth for every row in this brief: TARGETED.

Rows:
- L168: Botterill 2021, "From National Drought Policy to National Drought Agreement: the evolution of Australia’s drought response", The Rangeland Journal 43(3): 77-86.
  file: Literature review/Botterill2021.pdf
  current: National Drought Policy from 1992 to the 2018 National Drought Agreement: self-reliance stays the stated aim while spending is still announced during severe drought.
  why: priority 1; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.5 Drought resilience and the Future Drought Fund)
- L169: Hughes 2022, "Defining drought from the perspective of Australian farmers", Climate Risk Management 35: 100420. doi:10.1016/j.crm.2022.100420
  file: Literature review/Hughes2022b.pdf
  current: ABARES outcome-based drought indicator for farms; farmers have shifted their idea of drought with the long-term change in climate.
  why: priority 1; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.5 Drought resilience and the Future Drought Fund)
- L170: Hughes 2017, "Climate adjusted productivity on Australian cropping farms", New Directions in Productivity Measurement and Efficiency Analysis. doi:10.4337/97817
  file: Literature review/Hughes2017.pdf
  current: Climate-adjusted productivity of Australian cropping farms 1977-78 to 2014-15: a marked deterioration in cropping climate over the last 15 to 20 years of the series, mainly in the south.
  why: priority 2; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.5 Drought resilience and the Future Drought Fund)
- L171: Sysak 2017, "Social Impacts of a National Drought Policy in Australia", Handbook of Drought and Water Scarcity: 405-422. doi:10.1201/9781315226774-20
  file: Literature review/Sysak2017.pdf
  current: Local social effects of national drought policy in an irrigated region of northern Victoria; drought policy has to be read with water policy.
  why: priority 3; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.5 Drought resilience and the Future Drought Fund)
- L172: Higgins 2018, "Informing transport infrastructure investments using TraNSIT: A case study for Australian agriculture and forestry", Computers and Electronics in
  file: Literature review/Higgins2018.pdf
  current: TraNSIT, the CSIRO model of Australian agricultural and forestry freight, used to weigh transport investments; title only.
  why: priority 1; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.6 Interregional freight and food supply chains)
- L173: Higgins 2018, "Informing major government programs for rural transport infrastructure in northern Australia", The Rangeland Journal 40(4): 341-351. doi:10.1071/
  file: Literature review/Higgins2018b.pdf
  current: TraNSIT applied to the 2016 Beef Roads Program: farm-to-market distances over 1000 km on largely unsealed roads cut by seasonal flooding.
  why: priority 2; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.6 Interregional freight and food supply chains)
- L174: Davis 2020, "Towards food supply chain resilience to environmental shocks", Nature Food 2(1): 54-65. doi:10.1038/s43016-020-00196-3
  file: Literature review/Davis2020.pdf
  current: Scoping review of how environmental shocks pass along or are damped by food supply chains.
  why: priority 2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.6 Interregional freight and food supply chains)
- L175: Kummu 2020, "Interplay of trade and food system resilience: Gains on supply diversity over time at the cost of trade independency", Global Food Security 24: 100
  file: Literature review/Kumma2020.pdf
  current: 1987 to 2013: food supply diversity rose for most people at the cost of greater import dependence and fewer import partners. As A11.7: diversity gained through trade at the cost of import dependence.
  why: priority 1 at A11.7; 2 at B8.2; open access yes; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.7 Import dependence); methods paper (section 8, B8.2 What no method does: trade)
- L176: Soliman Hunter 2021, "Long-term and short-term liquid fuel security in Australia – What role for the Great Australian Bight?", Energy Policy 157: 112472. doi:10
  file: Literature review/Hunter2021.pdf
  current: Australia's long-term and short-term liquid fuel security; the import dependence that farm and freight fuel rests on; title only. As A11.7: Australian liquid fuel security; title only.
  why: priority 1 at A11.7; 1 at A12.4; 2 at B8.3; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.7 Import dependence); results paper (section 12, A12.4 Fuel and energy in food production
- L177: Wood 2018, "Trade and the equitability of global food nutrient distribution", Nature Sustainability 1(1): 34-37. doi:10.1038/s41893-017-0008-6
  file: Literature review/Wood2018.pdf
  current: Trade and the distribution of food nutrients between countries; title only.
  why: priority 2; open access no; filed 2026-11-10: PDF uploaded by Murray
  used by: results paper (section 11, A11.7 Import dependence)
- L178: Ritzel 2024, "Vulnerability assessment of food imports: Conceptual framework and empirical application to the case of Switzerland", Heliyon 10(5): e27058. doi:1
  file: Literature review/Ritzel2024_Heliyon_Vulnerability_assessment_of_food_importsConceptual_framework_and_empirical_application_fulltext_PMC.md
  current: An import vulnerability index (exporter and product factors) applied to Switzerland; a template for measuring import exposure.
  why: priority 3; open access yes; filed 2026-11-10: open-access full text from PubMed Central (JATS XML and a text rendering; not the publisher PDF) fetched by the coordinator (Europe PMC API)
  used by: results paper (section 11, A11.7 Import dependence)
