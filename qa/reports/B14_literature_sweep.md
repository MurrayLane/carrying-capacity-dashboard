# B14: web sweep for carrying-capacity and food-capacity studies, 2011 to 2026

Companion file: `qa/reports/B14_literature_sweep.csv` (60 rows, every row marked `not read`). I read `qa/literature_register.csv` first (72 rows) and did not repeat its rows, except four control rows marked "yes" in `in_register`.

## What "opened" means here
Most DOIs were checked by opening the Crossref record for that DOI (api.crossref.org), which confirms title, authors, year and venue and sometimes gives abstract-level text. The publisher pages were not opened (most publisher hosts were not tried; the tool returned records through Crossref). Where the abstract was not on the record, `what_it_does` says so and gives only what the title supports. No PDF was downloaded. Rows with csiro.au or pc.gov.au addresses rest on those pages.

## What I searched, and what came back
1. Australian studies: Hatfield-Dodds 2015 (found, DOI checked); CSIRO Australian National Outlook 2015 and 2019 (news pages opened, reports not); Bryan 2016 (found) and Bryan 2014; Ridoutt and Hendrie diet and cropland footprints (3 papers); Hadjikakou 2017; Millar and Roots 2012; Lee 2013; Melbourne Foodprint (Candy et al. 2019); Graymore et al. 2010 (South East Queensland, one year outside the window but a planning-oriented carrying capacity tool); Productivity Commission 2011 roundtable. Crossref search on "Lane Dawes Grace" returned only Lane's own four papers.
2. Land-based capacity elsewhere: Peters foodshed papers (2008, 2009, 2022 chapter), Horst and Gaolach 2014, Zumkehr and Campbell 2015, Kurtz 2020, Fader 2013, Tilman 2011, Smith 2013, Hunter 2017, and three China-tradition or recent "how many can our land feed" items.
3. Land per diet: EAT-Lancet, Springmann, Gerten, Poore and Nemecek, Roos, Kastner, van Zanten, Erb, Muller, Clark and Tilman, plus Tilman and Clark 2014, Bajzelj, Mottet, Schader, Shepon.
4. Footprints: Borucke 2013, Giampietro and Saltelli 2014, Blomqvist 2013, van den Bergh and Grazi, Galli 2012, Moore 2012, Wackernagel 2019, Niccolucci 2012, Wiedmann and Lenzen 2018. Lin 2018 is already in the register.
5. Concept reviews: Chapman and Byron 2018, Cohen 2017 and 2013, Tucker 2020.

Candidates per theme: theme 1: 17 (3 of them the author's own papers as control rows); theme 2: 14; theme 3: 15; theme 4: 10 (1 control row); theme 5: 4. Total 60.

## Searches that returned nothing usable, and leads I could not open
* Sobels, Richardson, Turner et al. 2010 for the immigration department: a search found the report (title: Long-term physical implications of net overseas migration: Australia in 2050; this is not the title in the brief) but the library host is outside the session's allowed network and the copy on macrobusiness.com.au returned 503. Not in the CSV. Worth adding once opened.
* ABARES food security 2023: the search found only an ABARES Insights piece on food security and COVID-19 (coverage dated September 2023); the ABARES pages returned 503. No row.
* State of the Environment 2021, land chapter: pages found by search, the land use page returned 503. No row. (A search snippet says SoE links population growth to competition for farmland; unverified.)
* Australian Academy of Science: the academy page returned 404. A search snippet says its 1994 submission to the Jones inquiry; its figure (23 or 26 million) is in secondary sources only. The register already holds this as L018.
* Sustainable Population Australia: no carrying capacity paper from 2015 to 2024 found.
* Papers citing Lane 2014, 2015 or 2017: none found through Crossref's title search. A citation index (Google Scholar, Scopus) was not available, so this is a gap in the method, not a finding that none exist.
* Fairlie-type national studies (the Britain family): a Crossref title search found nothing new after 2011; Fairlie 2007 is already L041.
* Foodprint Melbourne's own 2015 report ("Melbourne's foodbowl: Now and at seven million", Sheridan, Larsen, Carey): the unimelb page returned 403. Only the 2019 paper is in the CSV.
* The brief names "Sobels 2010", "Roos 2017", "Muller 2017": Roos is spelt Röös in the record.

## Points for the coordinator
* Lane's time-frame paper: Crossref gives 2016, the register (L014) says 2017. Check which the project cites.
* Crossref gives the van den Bergh and Grazi paper as 2013 (online); the journal volume may be 2014.
* The Peters 2008 and 2009 papers are both Renewable Agriculture and Food Systems vol. 24 (2009); Crossref carries 2008 for one.

## The ten I judge most important for the paper
1. Hatfield-Dodds et al. 2015, Nature (and the CSIRO Australian National Outlook behind it): the main official Australian scenario study that includes food, land and water together; the paper's Australian case needs to say how a scenario outlook differs from a capacity estimate.
2. Bryan et al. 2016, Global Environmental Change: the only gridded, whole-of-Australia land-use model to 2050; the nearest published Australian comparator for a land-based capacity method.
3. Peters, Bills, Lembo et al. 2009 and Peters 2022 chapter "Foodshed analysis and carrying capacity estimation": the Peters line (Peters 2016, L015, is in the register) is the clearest land-and-diet capacity method, and the 2022 chapter is a methods review in its own right.
4. Ridoutt et al. 2017, Food Security: Australian food balance by food group against 2050 population; a direct Australian test of how many people the supply covers.
5. Kastner et al. 2012, PNAS: separates population, yield and diet effects on land need; a model for how a method review can show which input moves the answer.
6. Willett et al. 2019, The Lancet (EAT-Lancet) with Springmann et al. 2018, Nature: the reference diet and limits that any diet-based capacity figure is now measured against.
7. Gerten et al. 2020, Nature Sustainability: a capacity estimate ("ten billion within four boundaries") that names its limits; a comparator for the national range.
8. Erb et al. 2016, Nature Communications: shows the spread of feasible answers from diet, yield and grazing assumptions; supports reporting a range rather than one figure.
9. Giampietro and Saltelli 2014 with Blomqvist et al. 2013 (and Borucke 2013 or Wackernagel 2019 for the other side): the footprint critique and reply; a review of methods needs both sides.
10. Chapman and Byron 2018, Global Ecology and Conservation: the recent ecology review of the carrying capacity concept itself, for the opening argument of the review.

Close behind: Graymore et al. 2010 (a South East Queensland planning tool that tested footprint and found it poor at regional scale; this is the planners' angle), Poore and Nemecek 2018, Fader 2013, Candy et al. 2019 (Melbourne city-scale).

Nothing in this report is read beyond abstract level; every row stays `not read` until someone opens the paper.
