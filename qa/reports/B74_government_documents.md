# B74 government documents for Paper A's introduction

Taken on 2026-11-11 with a plain client string ("research-fetch/1.0"), one request at a time, no retries after a refusal. The literature register was not edited. Rows for merging: `qa/reports/B74_grey_rows.csv` (9 rows: 4 reached, 5 not reached).

## Documents

**1. Intergenerational Reports (Treasury).** Both reached from the Treasury site. The 2023 report gives a population of 26.5 million in 2022-23 rising to 40.5 million in 2062-63, growth of 1.1% a year against 1.4% over the past 40 years (printed pp. 37, 39), net overseas migration fixed at 235,000 a year (p. 38), a note that the projections do not account for climate change (p. 227), and a higher case 3.1 million above baseline (p. 254). The 2021 report projects 38.8 million in 2060-61, the first downward revision in an intergenerational report (pp. viii, 14), and 35.3 million in June 2050 against 37.8 million in the 2015 report (Table A2.1.1, p. 158).

**2. Population Statement (Centre for Population).** The latest listed is the 2025 Statement, reached as a PDF. Population 27.5 million in March 2025, 28 million by the end of 2025-26 and 41 million by 2065-66 (Table 1, p. 1); long-run net overseas migration 235,000 and fertility 1.42 in 2025-26 recovering to 1.62 (p. 1); a case study holding population at 30 million needs net overseas migration of 32,000 a year by 2035-36 (Box 1, p. 4). Useful for A1.1 and as a government statement of a 30 million case.

**3. Australian Food Story (House Standing Committee on Agriculture).** Not reached. The Parliament site returned a block page (HTTP 403) for the report address. Not retried.

**4. National Food Waste Strategy, Baseline and Feasibility Study.** None reached. The Department's host (dcceew.gov.au) closed the connection without a reply (an HTTP/2 error, then an empty reply over HTTP/1.1), for the topic page, a direct PDF address and the home page. Not retried. A11.3 stays on L161 Mirosa 2020 for the Baseline's 7.3 Mt.

**5. Productivity Commission review of the Future Drought Fund.** Reached: Inquiry report no. 102, "Review of Part 3 of the Future Drought Fund Act", 8 September 2023, from the Commission's report page. The Fund makes $100 million a year available (p. v); it is "establishing a solid foundation" but needs a stronger focus on lasting public benefits (p. 2); drought is now treated as a business risk with a policy shift to self-reliance (p. 3); $400 million was allocated under the first Funding Plan (read from PDF page 16; printed page not checked). Covers A11.5.

**6. ABARES Snapshot of Australian Agriculture and crop report or farm performance series.** Not reached. The agriculture.gov.au host failed in the same way as dcceew.gov.au (HTTP/2 error, empty reply over HTTP/1.1). Not retried. The observed 2011 to 2025 national output or wheat series for A1.5 is still missing.

## Files saved (in `/home/user/carrying-capacity-models/Literature review/grey/`)

| File | Bytes | sha256 |
|---|---|---|
| Treasury2023_Intergenerational_Report.pdf | 9244488 | a8036065cd2dbb7530fb5fd9f7c2cbdabff603e45ed6eab6b025c03b2b84eb69 |
| Treasury2021_Intergenerational_Report.pdf | 6474391 | 98df6c7bb8304f9a41bc67de5a70bb3448364161f3743156aa41360274702569 |
| CentreForPopulation2025_Population_Statement.pdf | 1788897 | fe95cbf7c7d6c8e4d3f93960bc0e64fb8c742bdccf23c7289a0c088f459070a3 |
| ProductivityCommission2023_Future_Drought_Fund_Inquiry_Report.pdf | 1948148 | ca3077dc9283cddb718a5b8110cd75a00c4ca7f18c8bac0b63b69df7ab8d9977 |

## Paper A points covered

- A1.1: closed by documents 1 and 2.
- A11.5: closed by document 5 (the Fund's review now has a source).
- A1.4: still open (document 3 not reached).
- A11.3: still open for the primary documents (document 4 not reached).
- A1.5: still open (document 6 not reached).

Register rows to be added: 9 (4 read, 5 "not reached": the House report, the Strategy, the Baseline, the Feasibility Study, the ABARES pages).

Wrong-value check: EXAMPLE ONLY, not a finding. A drafter should reject this line if it appeared: "Treasury projects 38.8 million people in 2062-63 (2023 Intergenerational Report, p. 39)." The 38.8 million is the 2021 report's figure for 2060-61 (p. 14); the 2023 report gives 40.5 million for 2062-63.
