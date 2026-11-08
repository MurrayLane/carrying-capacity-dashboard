# B52: PMSEIC 2010 and Grundy et al. 2016, read in full

Both PDFs were read in full with the Read tool: PMSEIC in nine ranges of 10 pages (PDF pp. 1 to 90) and Grundy in two ranges (PDF pp. 1 to 7 and 8 to 14). `pdftotext -layout` was used only to copy quotes exactly and to search the text. No registers were edited.

| File | Pages | sha256 |
|---|---|---|
| `carrying-capacity-models/Literature review/PMSEIC2010_Australia_and_Food_Security_in_a_Changing_World.pdf` | 90 | `abd5b78b361b4efb8614eccd3925b9e73f9d33194d72e1fcb41b6643b800838c` |
| `carrying-capacity-models/Literature review/Grundy2016_AgSystems_Scenarios_for_Australian_agricultural_production_and_land_use_to_2050.pdf` | 14 | `2c345748ea1cbadf0496ca326f091e13b30e318ba41dec695be42897af595f59` |

PMSEIC page numbers are the printed ones. Printed page 1 is PDF page 8, so a printed body page n is PDF page n + 7. The foreword is printed page v (PDF page 6). Grundy page numbers are the journal's (70 to 83, PDF pages 1 to 14).

## Main findings

1. **PMSEIC's 60 million is stated once, in the Executive Summary (p. 1). It comes with no source, no calculation, no year of data and no definition.** The register quotes it as "Australia is food secure and produces enough food today to feed approximately 60 million people". That is Millar and Roots's wording. The report itself says "we produce enough food today to feed 60 million people". It has no "approximately" and no "Australia is food secure".
2. **The report never says that the 60 million counts exports, but its own figures imply it.** On p. 15 it says Australian production feeds "some 40 million people each day outside Australia" (citing DAFF 2009). The 60 million is consistent with the people in Australia plus those 40 million. The report does not add the two figures itself.
3. **PMSEIC cites neither Lane nor any carrying-capacity study.** It has no other people-fed figure for Australia.
4. **Grundy et al. 2016 gives no figure for how many people Australian production could feed.** It reports production in tonnes and head, and value in 2010 dollars, from 2013 to 2050. These come from 72 LUTO scenarios that cover only the intensive land-use zone. It cites Bryan 2016 (as "Bryan et al., 2015a", in review) and both Hatfield-Dodds 2015 works. It does not cite Lane.

## (1) PMSEIC 2010

### The 60 million statement

The full sentence, from the Executive Summary under "Food security is an issue for Australia" (p. 1, PDF p. 8):

> "The likelihood of a food crisis directly affecting the Australian population may appear remote given that we have enjoyed cheap, safe and high quality food for many decades and we produce enough food today to feed 60 million people. However, if our population grows to 35-40 million and climate change constrains food production, we can expect to see years where we will import more food than we export."

- **Where it appears.** Only on p. 1. A text search of the whole report finds "60 million" nowhere else. The Recommendations Preamble (5.1, p. 63) repeats the second sentence without the 60 million: "If our population grows to 35–40 million and climate change reduces food production, we can expect to see years where we will import more food than we export." The page before that adds: "In 2008, following prolonged drought, our wheat exports dropped to nearly match the level of our domestic consumption."
- **What it counts.** The report does not say. "produce enough food ... to feed" is a production count, and the sentence sets it beside a comparison of imports with exports. That suggests production against need, with exports in. The only supporting figure is on p. 15 (section 2.2C, "Food production"):
  > "At present, Australian farmers produce almost 93 per cent of Australia's daily domestic food supply and export 60 per cent (in volume) of total agricultural production. Australian production represents one per cent of all food consumed in the world feeding some 40 million people each day outside Australia. ... (DAFF, 2009)."

  60 less 40 leaves 20 million. Australia's population in 2010 was about 22 million, though the report does not give a population for its base year. The 60 million therefore reads as the people in Australia plus about 40 million abroad, so it is an export-inclusive count. It is not a production-over-consumption ratio: no ratio, energy or tonnage figure is given. The 40 million abroad is itself an unexplained DAFF figure. The "60 per cent (in volume)" exported share is of agricultural production, which includes fibre.
- **Year and data.** None are given. "today" refers to the report's date, October 2010. The nearest data source is *Australian Food Statistics 2008* (DAFF 2009), the source of the 40 million and of the trade figures for 2007-08 (pp. 14, 34 and 35).
- **Own source or calculation.** None. The sentence has no citation, and the report gives no method, table or appendix for it. Appendix D (pp. 79 and 80) holds land use, agencies and curriculum tables only.

### Other capacity or self-sufficiency figures in the report

- p. v (Foreword): "In Australia, we have had an abundance of food. We can produce more food than we need and we have the resources to import food if necessary."
- p. 15: "almost 93 per cent of Australia's daily domestic food supply" comes from Australian farmers. Exports are "60 per cent (in volume) of total agricultural production". Production feeds "some 40 million people each day outside Australia" (DAFF 2009).
- p. 17: "Australia's growing population, estimated to be 35 million in 2050". The population is "projected to increase to between 30.9 and 42.5 million people by 2056 and to between 33.7 and 62.2 million people by 2101" (ABS 2009a).
- pp. 1 and 63: the 35 to 40 million threshold at which, with climate change, there would be "years where we will import more food than we export". It is an assertion, with no calculation given.
- p. 21: "It should be noted that a 15 to 30 per cent decline in food production is predicted for Australia." p. 28 (Key messages): "Climate change is predicted to reduce food production in Australia by over 15 per cent." No source is given for either.
- p. 11: "a drought year can reduce national wheat production by 60 per cent or more when compared with a good year."
- p. 33: imported foods account "for less than 10 per cent of food retail sales". p. 35: "Food exports were worth $23.4 billion to the Australian economy in 2007-08." p. 34: "Over the past five years, export earnings have averaged $18 billion a year in constant dollar terms." p. 38: "It has been suggested that the majority of grain produced in eastern Australia may be domestically consumed and there could be the need to 'import' grain from Western Australia."
- p. 38 asks for exactly the kind of work the methods paper does: "There is a need to develop scenarios for future food production in Australia and compare it with consumption patterns. This would have benefits ... informing broader national decisions about infrastructure development and population policy."

### Lane and carrying-capacity studies

- No citation of Lane. A word search for "Lane" in the text finds nothing, and Appendix C (References, pp. 75 to 78) has no Lane entry.
- No carrying-capacity study is cited: none of Gifford, Henry and Godden, Nix, Foran and Poldy, or Fearnside. A search for "carrying" finds nothing. The global framing rests on FAO and FAOSTAT 2009 and 2010, Godfray et al. 2010, Bruinsma 2009 and the Royal Society 2009.

## (2) Grundy et al. 2016

### Method

- p. 70 (abstract): "We used an integrated systems modelling approach to explore the response of Australian land use and agricultural production to these changes from 2013 to 2050."
- p. 72, 2.3: "The LUTO model is a partial equilibrium model of land use change and its impacts". It works "at a spatial grid cell resolution of ~1.1 km". It "draws on extensive spatial models and data layers for current land use, management practices and inputs, physical characteristics, productivity, price, and costs of production" to "quantify the spatial distribution of economic returns to 23 irrigated and rain-fed agricultural commodities" and "seven new potential land use alternatives (Table 1)". Land changes when a use becomes more profitable, subject to the hurdle rate.
- LUTO is one part of the CSIRO Australian National Outlook chain (Fig. 2, p. 73). The other parts are GIAM.GTEM, GALLM, GIAM.Climate, ESM, MMRF.H2O, NIAM.Flow, MEFISTO and a biodiversity model. Global prices and demand come from GIAM (Fig. 3, p. 75).
- Study area (p. 71, 2.1): "Australia's intensively managed agricultural lands; an area of approximately 85 million ha". It includes "33 Mha of beef cattle, 18 Mha of sheep, 3 Mha of dairy and 25 Mha of grain production". Extensive northern grazing is omitted. Limitation (p. 81): "Most beef cattle production occurs outside of the intensive use zone ... Hence, extrapolating the beef results from this study for Australia as a whole is inappropriate at this stage."
- Climate has little effect on yields (p. 80, 4.3): climate change has "a small aggregate effect (on average influencing production by <10% and in spatially variable ways to 2050)". Shocks and extremes are not simulated.

### Scenarios

- p. 71: "72 unique scenario combinations of four global outlooks, three productivity rates, three adoption hurdle rates, and two capacity constraint settings".
- **Global outlooks** (p. 72; Table 2, p. 74):

  | Outlook | Emissions | Population | Population 2050 | Action on climate |
  |---|---|---|---|---|
  | L1 | RCP 2.6 | low | 8.1 billion | very strong |
  | M3 | RCP 4.5 | high | 10.6 billion | strong |
  | M2 | RCP 4.5 | medium | 9.3 billion | modest |
  | H3 | RCP 8.5 | high | 10.6 billion | none |

  Population in 2010 is 6.9 billion.
- **Productivity** (Table 3, p. 75), as a simple yearly increase in agricultural yield: low 0%, medium 1.5%, high 3.0%. Tree growth is 0%, 0.5% and 1.0%.
- **Adoption hurdle**: 1x, 2x and 5x the profit of the existing use.
- **Capacity constraints** (p. 74), on reforestation, biofuel processing and bioenergy: constrained or unconstrained.
- The central scenario is "medium productivity, 2× hurdle rate" (p. 74).

### Every figure on production change to 2050

None is stated as people fed. All are in tonnes, head, hectares or real value.

- p. 74, 3.1, land leaving food and fibre production by 2050. H3: 5.4 Mha (6.9%). M2 with constraints: 5.4 Mha (6.8%); M2 relaxed: 25.1 Mha (31.8%). M3 unconstrained: 37.0 Mha (47.0%); M3 constrained: 14.2 Mha (18.0%). L1 unconstrained and under central settings: 46.0 Mha (58.3%); L1 least: 23.0 Mha (29.2%); L1 greatest: 62.7 Mha (80.0%).
- p. 75, 3.2: "Australian production of crops, cattle, and sheep output continued to increase, assuming moderate productivity increases and a 2× adoption hurdle rate. Under the L1 scenario with no capacity constraints, growth in production was flat in sheep and cattle, and subdued in crops, especially after 2040." It goes on: "Almost no production increases were achieved by 2050 under assumptions of low productivity rate increases, while production increased substantially under high-productivity assumptions (e.g. M3 central crop production increased 60.8%)." And: "It is notable that crop and sheep production can be doubled with medium or high productivity settings under the M2 and M3 scenarios".
- p. 75, 3.3, output rates: "the marked increase for cattle (265.4% in M3) compared with sheep (118.4%) and crops (73.1%)". "M3 cropping output rates increasing 5.9% under low productivity growth to 143.6% under high productivity growth". "M3 cattle output rates increased 312.0% under 1× hurdle compared to 205.0% under 5× hurdle."
- p. 75, 3.4, value: the "aggregate real value of food and fibre (2010 dollars), increased over time across all scenarios and sensitivity settings". Examples: "sheep production increasing 157.4% under M3"; "crop value increased 249.8% unconstrained versus 276.25% constrained"; sheep in M3 "96.2% under low productivity versus 192.3% under high"; "104.8% under 1× hurdle versus 224.5% under 5×".
- p. 77, Discussion: "In many scenarios, it was possible to maintain the excess of production over demand historically achieved in Australian agriculture (assuming that demand is correlated with domestic population increase)." And: "We found average production increases of over 100% in some scenarios". The sentence goes on to call this consistent with "the level of increase needed to maintain Australia's contribution to global food security and the level needed globally to match current need and future dietary demand". This is the paper's only statement about how far production covers demand, and it gives no number of people.
- Figures 6 to 8 (pp. 78 to 80), read from the plots and not printed as numbers:
  - Crop production starts near 85 Mt a year in 2013 and ends between about 80 and 190 Mt a year in 2050, depending on the setting.
  - Cattle start near 17 million head.
  - Sheep start near 10 million head on the unconstrained panels but near 55 million on the constrained panels. The two panel sets disagree, so the sheep axis is not usable.
- p. 70, Introduction (context, ABARES 2012): "About 65% of Australia's agricultural production is exported". It goes on: "This net excess of production over domestic demand has been built on a sustained increase in productivity".
- p. 75 uses "carrying capacity" once, in the grazing sense: "the more productive and more profitable land has higher per unit carrying capacity". It is not a population figure.

### Base year and food measure

- **Base year:** 2013 for the land use and production paths, which run 2013 to 2050. The global outlooks use 2010 as their base (Table 2). Values are in 2010 dollars.
- **Food measure:** crop tonnes, cattle and sheep head, output rates (t/ha, head/ha), area (Mha), and the real value of "food/fibre". Wool and cotton are inside "food/fibre", and there is no energy, protein or people measure. Fig. 4 excludes grain sold from the wheat food and biofuel uses from the food area.

### Citations

- **Lane:** not cited. The reference list (pp. 81 to 83) runs from Lagi to Lambin to von Lampe, with no Lane.
- **Bryan 2016:** cited, as a manuscript in review. "Bryan, B.A., Nolan, M., McKellar, L., Connor, J.D., Newth, D., Harwood, T., King, D., Navarro, J., Cai, Y., Gao, L., Grundy, M., Graham, P., Ernst, A., Dunstall, S., Stock, F., Brinsmead, T., Harman, I., Grigg, N.J., Battaglia, M., Keating, B., Wonhas, A., Hatfield-Dodds, S., 2015a. Land use and sustainability under intersecting global change and domestic policy scenarios: trajectories for Australia to 2050. Glob. Environ. Chang (in review)." This is the paper published as Bryan et al. 2016, GEC 38: 130-152 (L076). In the text it appears as "Bryan et al., in review" (pp. 77 and 78). Bryan 2014b, 2015 and others are also cited.
- **Hatfield-Dodds 2015:** both works are cited.
  - 2015a: "CSIRO Australian National Outlook 2015 Technical Report: Economic Activity, Resource Use, Environmental Performance and Living Standards, 1970–2050. CSIRO, Canberra, Australia."
  - 2015b: "Australia is 'free to choose' economic growth and falling environmental pressures. Nature 527, 49–53. http://dx.doi.org/10.1038/nature16065."
  - The paper says it was "Undertaken as part of the Australian National Outlook (Hatfield-Dodds et al., 2015a)" (p. 71).

## (3) Method family, use in the methods paper, citation

### PMSEIC 2010

- **Method family:** an export-inclusive count, given as a bare assertion. It is not one of the six methods in the cross-method table. In the four groups of the catalogue (claim B230: domestic average year; drought allowance; energy and protein balance; export-inclusive counts) it falls under export-inclusive counts, beside Bellotti 61, NFF and industry 75, and CSIRO and UQ 100. It is weaker than CSIRO and UQ, which publish their arithmetic (27 x 70/30 + 27). PMSEIC publishes none, and the 40 million abroad behind it is an unexplained DAFF 2009 figure.
- **Use:**
  - A catalogue entry (section 4), labelled "unsourced, export-inclusive, 2010".
  - A comparator only in the ladder's exports band.
  - Context: a government advisory council in 2010 put the threshold for net food imports at 35 to 40 million people, with no calculation (pp. 1 and 63). That is an independent, if unsupported, statement close to the model's drought-allowance range.
  - It should not be used as a ladder step built from the model.
- **Citation as printed** (p. ii): "PMSEIC (2010). *Australia and Food Security in a Changing World*. The Prime Minister's Science, Engineering and Innovation Council, Canberra, Australia." The inside cover adds the subtitle "Can we feed ourselves and help feed the world in the future?" and "Report of the PMSEIC Expert Working Group, October 2010". The publication number is 10/056 (p. ii), and the chair is Professor Peter Langridge. **No DOI** and no ISBN are printed.

### Grundy et al. 2016

- **Method family:** a spatial economic land-use scenario model (LUTO, partial equilibrium), driven by integrated assessment models. It projects production and land use, not people supported. It is the same family and tool as Bryan 2016 (L076), applied to agricultural output.
- **Use:**
  - Context and qualitative comparator in section 5 (food comparator). It shows that national output to 2050 depends mainly on productivity growth (0, 1.5 or 3% a year), less on climate (<10%) and land competition, and that food land can shrink while output rises.
  - It cannot be a catalogue entry or a ladder step, because it gives no people figure and no food energy or protein measure.
  - Its coverage, the 85 Mha intensive zone without the extensive rangelands, and its food-and-fibre value measure must be stated if it is set beside the model.
  - Its 2010 dollar values and output percentages should not be turned into people.
- **Citation as printed** (p. 70): Michael J. Grundy, Brett A. Bryan, Martin Nolan, Michael Battaglia, Steve Hatfield-Dodds, Jeffery D. Connor, Brian A. Keating, "Scenarios for Australian agricultural production and land use to 2050", *Agricultural Systems* 142 (2016) 70–83. DOI printed as http://dx.doi.org/10.1016/j.agsy.2015.11.008 (**10.1016/j.agsy.2015.11.008**). Received 27 May 2015, accepted 17 November 2015, online 26 November 2015.

## (4) Row updates (for the coordinator to merge)

### L136 (PMSEIC 2010)

- `kind`: "report (government advisory council)"
- `title`: "PMSEIC 2010, ""Australia and Food Security in a Changing World"", report of the PMSEIC Expert Working Group, Prime Minister's Science, Engineering and Innovation Council, Canberra, October 2010 (publication 10/056)"
- `origin`: "local copy of the report; first found through Millar and Roots 2012 (L094), p. 26"
- `dated_or_accessed`: "2010 (October); read 2026-11-08 (B52)"
- `local_path`: `carrying-capacity-models/Literature review/PMSEIC2010_Australia_and_Food_Security_in_a_Changing_World.pdf`
- `sha256`: `abd5b78b361b4efb8614eccd3925b9e73f9d33194d72e1fcb41b6643b800838c`
- `what_taken`: "'we produce enough food today to feed 60 million people' (p. 1, Executive Summary; no source, calculation, year or definition given); 'if our population grows to 35-40 million and climate change constrains food production, we can expect to see years where we will import more food than we export' (p. 1; repeated p. 63); production feeds 'some 40 million people each day outside Australia' and supplies 'almost 93 per cent of Australia's daily domestic food supply' (p. 15, DAFF 2009)"
- `read_or_reported`: "read"
- `used_by`: unchanged ("methods paper (section 4 (catalogue of estimates))")
- `notes`: "Full text read (90 pp.). The 60 million is an unsourced assertion that appears only on p. 1. It is export-inclusive by implication: p. 15 says production feeds some 40 million abroad, and 60 less 40 leaves about the 2010 population, but the report does not add the two. Millar and Roots's quotation ('Australia is food secure ... approximately 60 million') is not the report's wording. Does not cite Lane or any carrying-capacity study. No DOI or ISBN printed. Sits with L011 and B163 and the export-inclusive counts (B230)."
- `status`: unchanged (left to the coordinator).

### L135 (Grundy et al. 2016)

- `title`: unchanged, except the en dash in the pages is written as "70-83".
- `origin`: "https://doi.org/10.1016/j.agsy.2015.11.008 (lead from Bryan et al. 2016, L076)"
- `dated_or_accessed`: "2016 (online 26 November 2015); read 2026-11-08 (B52)"
- `local_path`: `carrying-capacity-models/Literature review/Grundy2016_AgSystems_Scenarios_for_Australian_agricultural_production_and_land_use_to_2050.pdf`
- `sha256`: `2c345748ea1cbadf0496ca326f091e13b30e318ba41dec695be42897af595f59`
- `what_taken`: "LUTO partial-equilibrium land-use model (~1.1 km grid, 23 commodities, 7 new land uses) in the CSIRO Australian National Outlook chain; 72 scenarios (4 global outlooks L1, M3, M2, H3 x productivity 0, 1.5, 3% a year x hurdle 1x, 2x, 5x x capacity constraints), 2013 to 2050, intensive zone of about 85 Mha only. Production in tonnes, head and 2010-dollar value, no people figure: almost no increase by 2050 at low productivity; M3 central crop production +60.8% (p. 75); crop and sheep production 'can be doubled' at medium or high productivity under M2 and M3; 'average production increases of over 100% in some scenarios' (p. 77); land leaving food and fibre 5.4 to 62.7 Mha (6.8 to 80.0%) by 2050 (p. 74)"
- `read_or_reported`: "read"
- `used_by`: "methods paper (section 5, context and qualitative food comparator; not a catalogue entry)"
- `notes`: "Full text read (14 pp.). Gives no estimate of people fed; food measure is food-and-fibre output and value, so it cannot sit in the catalogue or on the ladder. Excludes extensive northern grazing (authors: extrapolating beef 'for Australia as a whole is inappropriate'). Climate effect on yields <10% to 2050; no shocks. Cites Bryan 2016 (as 'Bryan et al., 2015a', GEC, in review) and Hatfield-Dodds 2015a (CSIRO National Outlook technical report) and 2015b (Nature 527: 49-53); does not cite Lane."

### Ladder row for PMSEIC's 60 million

PMSEIC's 60 million is a published export-inclusive count, the same kind as the ladder's "exports counted as a proportion (CSIRO and UQ 2025)" row. A row in the form `published_values.csv` uses:

```
ladder,produces enough to feed (PMSEIC 2010; exports in by implication),million people,60.0,"PMSEIC 2010, Australia and Food Security in a Changing World, p. 1: 'we produce enough food today to feed 60 million people'; no source, calculation, data year or definition given; p. 15 (citing DAFF 2009) says production feeds 'some 40 million people each day outside Australia', so the 60 reads as people in Australia plus about 40 million abroad (the report does not add them); read from the local copy, sha256 abd5b78b..."
```

If a step is wanted in `ladder.csv` as well (form `step,million people,definition`):

```
"exports counted, unsourced (PMSEIC 2010)",60.0,"people in Australia plus about 40 million fed abroad (DAFF 2009), 2010; no calculation published"
```

**Caution before adding the ladder step.**
- The ladder is "one model, one data set, different definitions", and its exports rows are 2025 counts. A 2010 count of 60 sits below the model's own no-export step (62.9, improved and no avoidable waste), so as a step it would look like an inversion.
- Recommendation: carry the value in `published_values.csv` as a catalogue and comparator row, and leave it out of `ladder.csv`. If it is added, mark it as a 2010 count with no published arithmetic.
- Related claims that list export-inclusive counts as "61, 75, 100" (B230; B004 notes) could add PMSEIC 60. That is the coordinator's decision, and nothing was edited here.
