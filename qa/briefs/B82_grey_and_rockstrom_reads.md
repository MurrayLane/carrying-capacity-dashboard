# Reading brief B82: six items uploaded by Murray (decisions 50, 56)

Rules: plain language; no time words; no em dashes; decision 33. No git; no subagents; no network. Write only `qa/literature_register.csv` (rows L229, L230, L234, L240, L241, L242 only) and `qa/reports/B82_grey_and_rockstrom_reads.md`. Files are at `/home/user/carrying-capacity-models/` plus each row's `local_path` without its first path segment (`pdftotext`, `-layout` for tables; for the two `.html` files strip the tags and read the text, and list every PDF link the page carries with its URL).

Targeted reads, each for what its `used_by` point needs (see `qa/reports/B70_paperA_thin_points.md` for A1.4, A1.5, A11.3 and `papers/B_methods/SECTION_SCOPE.md` section 2 for the planetary-limits paragraph):
- L229 House of Representatives inquiry "Australian Food Story" (227 pp): the committee's findings on national food security, self-sufficiency and the recommendation list; the figures it quotes on production versus consumption and exports; the pages. Read the executive summary, the recommendations and the chapter on domestic supply.
- L230 DCCEEW National Food Waste Strategy web page: the Strategy's stated goal and date, the baseline tonnage it cites with its year, and the PDF links (Strategy 2017, Baseline 2019, Feasibility Study 2021) with URLs so Murray can fetch the documents.
- L242 DCCEEW "Reducing Australia's food waste" page: the current headline figures (tonnes a year, cost, share by stage) with the year they refer to, and the PDF links.
- L234 ABARES Snapshot of Australian Agriculture 2026: the gross value of production, the share exported, the number of farms, the land area farmed, and any 2011 to 2025 series on production volume or value; pages.
- L241 ABARES Financial performance of broadacre and dairy farms 2023-24 to 2024-25: the farm cash income and production series it carries back to 2011 or earlier (tables, pages), the drought years named, and the yield or output index if any. Say plainly whether it gives the observed national output series A1.5 lacks, or only financial series.
- L240 Rockström et al. 2009: the nine boundaries, the three transgressed in 2009, the framing of a safe operating space, and whether the paper uses the words "carrying capacity" (p. 472 onward).

For each row: `what_taken` (at most 90 words, page-cited; for web pages say "web page, saved 2026-11-11"), `read_or_reported` "read (B82 targeted)", `status` "self-checked (B82)", `notes` with the "why" line, flags for the scopes, and for L230 and L242 the PDF URLs found. Checks: 242 rows, 12 columns, parses, no em dashes, line endings unchanged.

Report: one block per item; the URLs found for the food waste PDFs; whether A1.5's observed series gap is closed; the register rows touched; and "Wrong-value check:" with one deliberate wrong figure, marked as an example.
