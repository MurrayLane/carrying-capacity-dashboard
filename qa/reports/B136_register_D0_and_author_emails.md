# B136: decision 133 applied to the register; draft emails to the HALF and Cassidy authors

Brief: `qa/briefs/B136_register_D0_and_author_emails.md`. No git, no subagents, no network. Written: `qa/claims_register.csv`, `papers/CORRESPONDENCE/halff_authors_draft.md`, `papers/CORRESPONDENCE/cassidy_authors_draft.md`, and this report. Nothing is sent. The folder `papers/CORRESPONDENCE/` did not exist and was created.

## One point for Murray first: who the HALF authors are

The brief names the HALF authors as "Peters et al. 2016, Elementa". The repository does not: the HALF index is Alexander, Brown, Arneth, Finnigan and Rounsevell 2016, Global Environmental Change 41: 88-98 (`qa/references.csv` L017; `half_index.py` header; supplement `Alexander2016_SI.pdf`). Peters et al. 2016 in Elementa (L015) is "Carrying capacity of U.S. agricultural land: Ten diet scenarios", a different paper, and the figures in the brief (112.2, 3,364 Mha) are Alexander's. I addressed the HALF draft to the Alexander et al. authors. If Murray did mean the Peters paper, the draft does not apply and needs rewriting.

## 1. Register (decision 133)

Rows changed: B114 and B159 only. Fields changed: `statement`, `value`, `status`, `notes`.

| Row | Field | Before | After |
|---|---|---|---|
| B114 | value | 46.2 to 60.1 | 37.9 to 60.0 |
| B114 | statement | "...short-term capacity, Australia: 46.2 to 60.1 million." | "...short-term capacity, Australia: 37.9 to 60.0 million (18 choices; factor 1.58)." |
| B159 | value | 41.5 (31.1 to 49.2); 53.6 (46.2 to 60.1) | 41.5 (31.1 to 49.2); 53.6 (37.9 to 60.0) |
| B159 | statement | "...the improved entry 53.6 (46.2 to 60.1)." | "...the improved entry 53.6 (37.9 to 60.0)." |
| both | status | independently verified; new value pending approval (B130, V46) | independently verified; approved (decision 133, 2026-11-18) |
| both | notes | ended with the clause "pending approval (2026-11-18): improved range 37.9 to 60.0 ... awaits Murray's line" | that clause removed; added "decision 133 (2026-11-18): improved range 37.9 to 60.0 short term (factor 1.58), 15.7 to 22.1 long term (factor 1.41), 18 choices; was 46.2 to 60.1 (13 choices) until decision 133; B130, checked V46" |

The long-term range (15.7 to 22.1) sits in the notes only: both claims are short-term claims, so their value cells carry the short-term range. Earlier history in the two notes (the 13-choice remarks from B115 and V41) was left as it was; the new clause says it was superseded.

Checks as B122: 18 columns on every row (816 rows including the header before and after; the 817th split element is the closing line end); CRLF on every line (LF count equals CRLF count); the file was edited as bytes and 814 of 816 rows are byte-identical to the copy taken before (the only differing rows are B114 and B159); no em dashes in the file. Not done, outside the four paths: `cross_method.csv`, the README and OUTLINE cells that print 46.2 to 60.1 are not touched here (a register or table job for the coordinator; `cross_method.py` should read the widened rows).

## 2. The two drafts

Word counts (both under 250, whole file including the header lines and sign-off): HALF 235; Cassidy 245. Counted from "Dear" to the sign-off: 204 and 214.

Address lines read "[to: corresponding author, from the paper]"; sign-off "[name, affiliation]". No identity filled in.

Where Murray finds the addresses (no network here): the corresponding-author line in the author notes on the first page of each paper. Alexander et al. 2016: `carrying-capacity-models/Literature review/Alexander2016.pdf` (and the publisher page, doi 10.1016/j.gloenvcha.2016.09.005). Cassidy et al. 2013: the file under `carrying-capacity-models/Literature review/Cassidy2013` (doi 10.1088/1748-9326/8/3/034015); ERL prints the correspondence address in the author footnote.

Figures used (all from `qa/reports/B116_bases_and_fidelity.md` as corrected by `qa/reports/V42_check_B116.md`):
* HALF: Australia 2011 published 112.2; rebuild 113.12 (+0.8%) on current FAOSTAT; 118.88 (+6.0%) with the supplement's world pasture (3,364 Mha against 3,182 Mha); 121.59 (+8.4%) on all printed inputs; world, United States, Argentina, India move toward the published figures on printed inputs; bovine share of pasture 59% (1,982 of 3,364 Mha) in the supplement against 67% here; 70 of 90 commodities; current FAOSTAT in place of the 2015 download.
* Cassidy: world produced 12.3 against 10.1 (+22.0%); delivered +24.9% (world) to +42.3% (China); with 1997-2003 yields +5% to +25%; United States other-use share 32 against 6; feed share 41 against 67; 22 of 41 crops; supplementary information not read (stated in the draft).

Open questions each email asks:
* HALF, 1: is 3,364 Mha the pasture area behind the Australian figure, and which FAOSTAT definition and year gives it? HALF, 2: the supplement gives bovine meat 59% of pasture, we get 67% by feed need; is the share set another way?
* Cassidy, 1: which crop energy values and grain-fed share of beef were used, and are they in the supplementary information? Cassidy, 2: does "other" use cover biofuels and industrial use only, or seed and losses too (our split puts seed and losses outside it)?

Tone (decision 33): each draft describes our access, our assumptions and the residual, and asks which input or step we misread; no verdict on their method, and the HALF draft says the 0.8% "holds on the current revision only" as a statement about our rebuild. The Cassidy "harvest matching" of the brief is covered as the 1997-2003 yield variant; the same-year against previous-year harvested-area matching (`cassidy_matched.csv`) concerns Australia 2021-23 only, so it is not in the email.

## Wrong-value check (an example; constructed by me, not a real slip)

I first wrote the Cassidy sentence with the range taken from the builder's unamended B116 report, where the largest "as run" gap printed in `fidelity.csv` is China produced, +36.5%: "our figures are 22% to 36.5% above yours". Checked against V42's amendment (V42 line for "Cassidy delivered rows for US, India, China, Brazil": +27.9 to +42.3% as run; the top of R03b's "22 to 42%" is China delivered, which the builder's table does not hold), the 36.5 fails. The draft now says 22% to 42%, with world delivered +24.9% and the top +42.3%. The second item V42 caught, the United States other-use share (32 against 6, not tabulated by the builder), is in the draft. The example text is not in either draft.
