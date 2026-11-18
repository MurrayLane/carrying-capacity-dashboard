# What to check before you press submit

For Murray. Nothing has been sent, tagged, uploaded or published. Counts and line numbers are as read on 2026-11-18; other builders edit the drafts, so run `grep -n "\[" ` on the final files again.

**Order:** tag and deposit (`deposit/README_deposit.md`), get the DOI, patch both data statements, build the Word files, submit Paper B (Ecological Economics), then Paper A (Population and Environment). Corrections letters to the earlier journals go after Paper A is accepted (decision 117).

## 1. Placeholders in the files

| Where | Placeholder | Who |
|---|---|---|
| `papers/A_results/draft/A_s09-12.md` line 85 (Paper A data statement) | `[to be added at release]`, the archive DOI | you, after the deposit |
| `papers/B_methods/draft/B_s06-09.md` section 9.4 | a dated sentence that says the archive has no DOI; replace it with the DOI sentence | you, after the deposit |
| `papers/A_results/draft/A_s13_declarations.md` line 17 and `papers/B_methods/draft/B_s10_declarations.md` line 15 | `[Author name]` in the CRediT statement | you |
| `papers/B_methods/draft/B_s10_declarations.md` line 3 | two model names and versions for the Opus and Sonnet models (Paper A's AI text has none; keep the two papers alike) | you, from the account's usage history |
| `papers/DECLARATIONS.md` lines 15, 29, 35 | `[CONFIRM]`: the coordinating model's name and version; the thesis wording in the competing-interests text; no grant, no employer support, no funder paying for the Claude subscription | you |
| `papers/A_results/draft/supplementary.md` line 44 | `[Supplementary Figure S1: ...]`, a placeholder for the best-split map (file `analysis/regionalise_2025/ideal_K53_cap650k.png`, 170 dpi, no caption in `figures.csv`) | figure job or you |
| `papers/B_methods/draft/references.md` | 30 entries marked `[CHECK]` | see section 2 |
| `papers/A_results/draft/references.md` | 18 entries marked `[CHECK]` | see section 2 |
| both title pages | author name, affiliation with full postal address, corresponding email, ORCID, final title (drafts carry a "Paper A, results:" or "Paper B, methods:" label) | you |
| neither paper | an acknowledgements section (Ecological Economics asks for one, or say none) | you |
| `cover_letter_A.md`, `cover_letter_B.md` | `[Editor name]`, `[date]`, the final title, `[name, affiliation]`, `[author to supply]` reviewers, the companion paper's status, `[DOI]` | you |
| `deposit/metadata.json` | `[Family name, Given name]`, `[affiliation]`, `[ORCID]`, the two paper DOIs | you |
| `deposit/README_deposit.md`, both checklists | `[submission commit hash]`, `[DOI]` | coordinator, you |

The drafts also carry bracketed flags inside their "Drafter notes (not for the paper)" blocks (`[CONFIRM]`, `[open: Qn]`, `[gate 4]`); those blocks and the "First draft, assembled ..." line are left out of the manuscripts.

## 2. Fetches open (reference entries)

* **Not seen, you fetch:** Jansen (1999) and Saltelli et al. (2010) in both papers; NHMRC (2006) in Paper B. Mottet et al. (2017) needs its full author list (https://doi.org/10.1016/j.gfs.2017.01.001).
* **Author or year form:** ABARE (2010) and ABARES (2026a) author forms (Paper A); DCCEEW n.d. year; Chisholm (2000) volume and surname spelling; Fairlie (2008) volume, pages and DOI; Gifford et al. (1975) DOI; the second-hand entries (Buzby 2010, Nix, Migration Committee 1986, National Population Council 1992, National Population Inquiry 1975, Taylor 1922 end page); AUSNUT 2007 URL, date accessed and version.
* **Place of publication or publisher:** 12 entries in Paper A and 17 in Paper B. `grep -n CHECK papers/*/draft/references.md` lists every one.
* After each is settled, change `qa/references.csv` and rerun `qa/tools/make_references.py`; do not edit the lists by hand.
* Add the [dataset] entry for the Zenodo deposit to both lists.
* Also open from the third round: the public footprint release edition checked (R06c M2).

## 3. Emails to send

1. The HALF authors (`papers/CORRESPONDENCE/halff_authors_draft.md`) and the people-per-hectare authors (`cassidy_authors_draft.md`): drafts only, recipients and your name blank. Decision 5: asked after our own checks pass. The papers say "reproduced in part" and "not reproduced" without waiting for a reply; update if one comes.
2. A land-use planning colleague to read Paper B (decision 5); outside raters for the Table 9 matrix are your call and not needed to submit (decision 113).
3. After Paper A is accepted: one corrections letter per journal for Lane, Dawes and Grace 2014 and 2015, Lane 2017 and Lane and Dawes 2013, from `ERRATA.md` and `CORRECTION_NOTES.md` (drafted 2026-11-05, not reviewed by you). Whether the thesis gets a note is your call.

## 4. Reviewers to name

Both portals ask. Both cover letters say `[author to supply]`. None is chosen in any file.

## 5. Checks on the files themselves

* Gate 6 (your yes on the Tier A rows), the apply job (B148), the last patches and the final blind reads (V57a, V57b) are open: rerun `python3 qa/tools/wordcount.py A` and `B` after them. The margins are 61 words (A, limit 8,000) and 66 words (B), and Paper B's abstract is at 250 of 250.
* The cover letters quote the span of published estimates and Paper A's 33.3 to 41.5 million and 22.3 to 27.6 million; confirm each against the final abstracts.
* The two response letters (`response_letter_round2.md`) answer simulated referee reports. They are not for a journal.
* Journal rules to confirm at the sources: Population and Environment's guidelines (https://link.springer.com/journal/11111/submission-guidelines), which no file holds: keyword count, anonymised review, figure widths, where the AI declaration goes, how supplements are cited. Ecological Economics: whether captions, tables and references count toward 8,000 words.
* Vector figures exist only as SVG; both journals prefer EPS or PDF. No converter is installed on the build machine.
* The repository is public from the tag: `papers/CORRESPONDENCE/` and the response letters go with it.
