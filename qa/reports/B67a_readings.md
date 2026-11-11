# B67a readings: drought and climate on farming, livestock, self-sufficiency (full reads)

Five rows, all read in full from the PDFs under `carrying-capacity-models/Literature review/`. Each file is the paper the row names. Page numbers are the journal's own (Hughes 2022 uses "Page n of 22" of article 12). Figures, methods and base years for every number are in `qa/reports/B67a_readings.csv`.

**L152, Hughes et al. 2022 (holds: partly).** ABARES links a machine-learning model of about 2,250 broadacre farms (sampled 2015-16 to 2018-19, prices and technology held at those years) to daily climate data, then reruns the farms under four climates. The 2001 to 2020 climate gives average profit 22.6% below the 1950 to 2000 climate (Table 5, p. 11); the abstract says 22.3% and the results text 23%. 2050 runs over six climate models give -2.0 to -31.9% under RCP4.5 and -10.7 to -49.9% under RCP8.5 (p. 11). These are simulated profits, not observed ones, and exclude long-run adaptation and CO2 fertilisation (p. 3). Wheat yields fall 2.8 to 24.1% by 2050 under RCP4.5 (p. 16).

**L153, Hochman et al. 2017 (holds: yes).** The paper runs the APSIM crop model at 50 sites with observed weather and 2015 management. Water-limited wheat yield potential fell 27% (1.23 t/ha) from 1990 to 2015 (p. 2075). Lower rainfall explains 83% of the fall and higher temperatures 17%; rising CO2 offset a further 4% (p. 2077). National actual yields stayed flat because farmers closed the gap to potential, relative yield rising from 39% to 55% (p. 2076). The 27% is a fall in potential, not in harvested yield.

**L155, Wittwer and Waschik 2021 (holds: yes).** A dynamic regional general equilibrium model (VU-TERM) runs the 2017 to 2019 drought and 2019-20 bushfires as deviations from a no-drought baseline starting 2015-16. National real GDP sits 0.7% or more below base in 2018-19 and 2019-20 (pp. 918, 928); NSW GDP falls 1.1% ($6.9 billion) and 1.6% ($10.2 billion) (p. 926), and New England-North West more than 10% (p. 928). The present value of the national welfare loss is $63 billion, $53 billion of it from drought, with capital losses over $28 billion (p. 932). The paper does not state the discount rate.

**L159, Ridoutt 2024 (holds: partly).** The paper builds Australian red meat emissions from the national inventory for 1990 to 2020 and reports them as a radiative-forcing footprint: 5.71 mW/m2 in 2005, a 7.13 peak in 2018 and 7.07 in 2020 (p. 400). Industry forecasts of 18% more sheep and 13% more pasture cattle from 2020 to 2030 (Table 1, pp. 398-399) are inputs, not findings. Under business as usual the footprint rises 2.8% by 2030; with the listed interventions it falls 3.6% (p. 401). The paper does not measure livestock productivity.

**L180, Kinnunen et al. 2020 (holds: yes).** A global optimisation on a grid of about 50 km cells, with a 2006 to 2010 baseline, finds the shortest distance from production to consumption for six crop types, eating local output first. Between 11 and 28% of people could meet their demand for a given crop within 100 km (p. 229): 22 to 28% for temperate cereals, rice, tropical cereals and pulses, and 11 to 16% for maize and tropical roots (pp. 229-230). For 26 to 64% the distance exceeds 1,000 km (p. 229). Animal products are left out (p. 233), and the main text gives no Australian figure.

## Flags

1. **A1.5 (results paper, section 1), L152:** the 22.3% is a simulated effect of the 2001 to 2020 climate on 2015-19 farms, not a measured fall in profit, and its window starts in 2001, not 2011. Cite 22.6% (Table 5, p. 11) or "about 23%" and say "simulated". State the 2050 range by pathway (-2 to -32% RCP4.5; -11 to -50% RCP8.5), not as one -2 to -50% span.
2. **A1.5, L152 beside L135:** Hughes gives a national wheat yield fall of 2.8 to 24.1% under RCP4.5 by 2050 (p. 16), against the under-10% from L135 Grundy already at A1.5. Set the two side by side and do not merge them.
3. **A1.5 and B8.1 (methods paper, section 8), L153:** the 27% is water-limited yield potential, not actual yield, which did not fall. Any line reading "wheat yields fell 27%" should read "yield potential". The series ends in 2015, so it gives context for the post-2011 window but does not measure it.
4. **A1.5, L155:** the $53 billion is the present value of a modelled welfare loss, with no discount rate stated. Cite it as the authors' model estimate.
5. **A11.1 (results paper, section 11), L159:** the 13% and 18% are industry forecasts of animal numbers taken as inputs (p. 398), from a 2020 flock low. The paper measures forcing, not productivity, so it cannot support a productivity claim, and the "nothing Australian" gap at A11.1 stays open.
6. **A12.1 (results paper, section 12) and B8.2 (methods paper, section 8), L180:** no change to a claim. The 11 to 28% is a range across single crops, not an uncertainty range and not the whole diet. It gives no Australian number.

## Register rows touched

L152, L153, L155, L159, L180.

## Wrong-value check:

EXAMPLE ONLY, NOT A FINDING. Suppose a row had read "Hochman 2017: Australian actual wheat yields fell 27% from 1990 to 2015." That would NOT hold. The paper says actual national yields showed no significant trend from 1990 to 2015 (Fig. 1b, p. 2072). The 27% fall is in simulated water-limited yield potential (p. 2075). The test would return holds = no.
