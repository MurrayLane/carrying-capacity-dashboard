# B73 page-level reads (seven rows)

Each file was opened from `/home/user/carrying-capacity-models/Literature review/` and checked against the row's title before reading. All seven are the paper the row names. Pages are the paper's own printed pages unless stated.

## L144 Davies 2024 (book chapter, ANU Press, doi 10.22459/AUP.2024.08)
* Identity: confirmed; the copy carries the printed chapter pages 149 to 164 and the ANU Press citation page.
* Confirmed: population grew by 5 million over two decades, described as unexpected, unprecedented and unplanned (p. 149). Centre for Population 2020 Population Statement: cited in the text on p. 152 and listed in the references on p. 162. Growth into regional cities and towns: section from p. 153.
* Added: the chapter says on p. 150 that growth is in fact highly managed, so the "unplanned" wording is the characterisation it reports.
* Corrections: none to the figures.

## L146 Bolleter 2018 (Australian Planner 55(2): 103-125)
* Identity: confirmed; the published journal copy with Taylor and Francis cover sheet, printed pages 103 to 125.
* Confirmed: 5,000,000 by 2060 (p. 103 abstract); the white paper's own wording is four to five million (p. 104); three scenarios (p. 105); Lane 2017 used on p. 123 (reference on p. 124).
* Correction: the row said the north's population already exceeds its regional capacity. The paper states it for the Northern Territory and the north of Western Australia, and names the Northern Gulf as the one area that has not exceeded it (p. 123). The row now says so.

## L164 Laio 2016 (Environmental Research Letters 11: 035010)
* Identity: confirmed. The file name says Laio2026 but the paper is the 2016 article.
* Confirmed: 92 products and 50 years in kcal (p. 1 abstract); 92 products and 253 countries (p. 2); per-capita stocks stationary (p. 1); Oceania larger per-capita stocks and higher halving probability (p. 1 and p. 7).
* Added: Oceania 2.4 x 10^6 kcal per person in 2011 against 2.5 x 10^5 in Africa (p. 4). The export link is stated on p. 4 (major exporting region) and p. 6 (net exports to West Europe); the paper does not give exports as the cause of the larger stocks, and the row wording is kept as a link.
* Corrections: none to the figures.

## L165 Marchand 2016 (Environmental Research Letters 11: 095009)
* Identity: confirmed.
* Confirmed: cereals, 17 year period (p. 1 abstract); Australia's R/S ratio in 2009 is 0.435 (p. 4).
* Added: the paper gives 0.435 as the worked example for scaling 1996 reserves, with supply S as production plus imports minus exports.
* Corrections: none.

## L182 Beltran-Pena 2020 (Environmental Research Letters 15: 095004)
* Identity: confirmed.
* Confirmed: 165 countries (p. 1 abstract); decline under the middle-of-the-road and business-as-usual paths (p. 1); years 2030 to 2100 (p. 3).
* Correction: Australia is named as a surplus producer under the sustainability and middle-of-the-road scenarios (p. 4). It is not named in the business-as-usual text, and the paper has no other mention of Australia in its text. The row now says so.

## L185 Langemeyer 2021 (Landscape and Urban Planning 210: 104055)
* Identity: confirmed.
* Pagination: the copy prints the article number 104055 and no page numbers, so pages are file pages 1 to 8.
* Confirmed: perspective essay (file p. 2, p. 6); loss of urban and peri-urban farmland to higher-value uses (file p. 1); three blind spots (file p. 1 abstract, file p. 2).
* Added: the word self-sufficiency appears once, in the abstract (file p. 1); the body uses food sovereignty (file p. 2 and p. 6).
* Corrections: none to the figures.

## L191 D'Odorico 2018 (Reviews of Geophysics 56(3): 456-531)
* Identity: confirmed; footers carry the printed pages 456 to 531.
* Confirmed: US food-related energy use at 16% of the national energy budget (p. 486, section 7, citing Canning et al. 2010); biofuel competition (p. 486, and section 8.1 on pp. 486 to 487); trade in water used for food (section 9.1.2, p. 491).
* Added: ammonia synthesis uses more than 1% of world energy (p. 486); 24% of water used for food production is traded (p. 491). The paper's term is virtual water trade, not embodied water.
* Corrections: none to the figures.

## Register rows touched
L144, L146, L164, L165, L182, L185, L191 in `qa/literature_register.csv`: `what_taken` rewritten with page citations, `read_or_reported` set to "read (B73 page level)", `status` to "self-checked (B73)", and a B73 clause appended to `notes`. Checks after saving: 225 data rows plus header (226 lines), 12 columns on every row, parses with Python's csv module, no em dashes, CRLF line endings unchanged (every line still ends in CRLF, and the other 218 rows are byte-identical to the file as found).

Wrong-value check: example only, not a finding. Citing Bolleter's Lane 2017 statement to p. 124 (where the Lane 2017 reference entry is printed) would be a wrong page; the sentence is printed on p. 123. Citing D'Odorico's 16% to p. 491 (where virtual water trade is discussed) would also be a wrong page; it is printed on p. 486.
