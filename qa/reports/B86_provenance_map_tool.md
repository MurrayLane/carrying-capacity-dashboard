# B86: the provenance map tool (decision 78)

Files written: `qa/tools/make_provenance.py`, `qa/provenance_A.md`, `qa/provenance_B.md`, and this report. The three registers and both scope files were read and not changed. The script reads local files only, uses no clock and no randomness, and gave byte-identical output on repeated runs. Rerun with `python3 qa/tools/make_provenance.py`.

## How the parser reads the scopes

* A section starts at a line `## Section N. Title` and runs to the next `## ` line. The closing parts ("The whole paper", "Closing part", and so on) are not sections and are skipped.
* Point texts come from the numbered list under "2. Content list" (Paper A uses a `###` heading, Paper B a bold run-in heading; both are matched).
* The evidence table is the first table whose header starts `| Point`. The middle cell is scanned for claim ids (`A123`, `B123`), including ranges written "A354 to A362", which are expanded one by one; for literature ids (`L123`, ranges such as "L148 to L151" expanded); for source ids (`D43`, `A04`); and for backticked file names (a known extension, a trailing slash, or the bare name `LICENSE`). Names with no folder (for example `cross_method.csv`) are looked up by file name anywhere in the repository. A pattern with a wildcard is matched as a glob.
* The sources table is the first table whose header starts `| Register id`. A first cell holding two ids (for example "L230, L231") gives two rows. A first cell with no id (a "pending B74" row) is listed under the Unparsed heading, not dropped.
* Each claim id becomes a row: statement shortened to about 100 characters, tier, status word, output file and locator, script, the data sources the claim names (kind and status), each source's origin field, and the literature ids in the claim's `sources` and `method_source` fields with a read word. A path or literature id the scope names directly gets its own row. A point that says "none needed" with nothing else gets a single row saying so.
* Files are checked against this repository, then the folder above it (the register paths begin `carrying-capacity-models/`), then by bare file name.
* One-word statuses. Claim: two-route (independently verified at tier A), one-route (self-checked, or independently verified at tier B or C), none (unverified or withdrawn). Source: verified or unverified. Literature: page-level, read, weak (reported, record only, not reached).

## Tallies

| | Points | Parsed | Unparsed | Fact rows | Distinct claims | two-route / one-route / none (claim rows) | Distinct sources verified / unverified | Literature page-level / read / weak | Distinct broken links |
|---|---|---|---|---|---|---|---|---|---|
| Paper A, 12 sections | 91 | 91 | 0 | 434 | 336 | 132 / 145 / 122 | 0 / 23 | 7 / 76 / 2 | 18 |
| Paper B, 9 sections | 73 | 72 | 1 | 341 | 251 | 77 / 127 / 96 | 0 / 25 | 12 / 107 / 8 | 36 |

Per-section rows are in the Tallies table at the end of each map. Every source in the sources register has status unverified, so the verified column is zero. Paper A cites 94 tier A, 220 tier B and 22 tier C claims; Paper B cites 57, 169 and 25.

## Broken links found

* Claim ids the scope cites that the register lacks: none, in either paper.
* Source ids a cited claim names that no register holds: none.
* File paths that do not exist (scope paths, and the output file and script of every cited claim): none.
* Literature ids cited that the literature register lacks: none.
* Literature ids with no file: 18 in Paper A and 36 in Paper B. Most have no `local_path` in the register (for example L002, L012, L013, L014, L020, L099 in both papers; the Lane papers and the thesis are among them). L073, L074 (both papers) and L086 (Paper B) carry the register note that the file is not stored. L117 (both papers) has a recorded path, `carrying-capacity-models/Literature review/vanZanten2016_IJLCA_Global_food_supply_livestock_land_use_FIRST_PAGE_ONLY.pdf`, that does not exist in the sibling models repository. The full lists, with each id's state, are under "Broken links" in each map.

Unparsed: Paper A none. Paper B section 3 point 3 (evidence cell "no csv holds the counts (see gap 1)"): it names no id or file, so it is listed, not counted. The "pending B74" and similar sources-table rows (Paper A section 1; Paper B sections 1, 6 and 7) are listed beside it.

## Notes for the reader of the maps

* The scopes' own tier-and-route text sometimes differs from the register status (for example a scope says "not yet checked" where the register has since moved on). The map shows the register's word and quotes the scope's note under each point, so such differences are visible.
* Tier B and C claims with status independently verified are shown as one-route, because one route meets their tier requirement. The raw register status is not repeated in the cell; look the id up in the register for it.
* The literature register was read once and not written.

Wrong-value check: Example (deliberate, not an observed error): a literature row whose `local_path` begins `carrying-capacity-models/Literature review/...` would be marked MISSING by a check that looks only inside this repository, because that folder sits in the sibling repository one level up. The script does not mark it, because it also resolves paths against the parent folder, so, for example, L144's Davies 2024 file shows ok. The same logic is why L117 is marked: its file is absent from both places, which I confirmed by testing both locations.
