# Deposit package: Zenodo deposit of the public repository at the submission commit

Prepared 2026-11-18. **Nothing here has been run, uploaded, tagged or published.** This file and `metadata.json` prepare the deposit for Murray (decisions 96, 120 and 131: the Zenodo hold is lifted and the public repository and the data the papers rest on are deposited and cited as [dataset] with the DOI). The creators, ORCID and related identifiers in `metadata.json` are placeholders.

## What the deposit holds

One archive of the public repository `https://github.com/MurrayLane/carrying-capacity-dashboard` as it stands at the commit tagged `submission-1`. It holds every file the repository tracks at that commit:

| In the archive | What it is |
|---|---|
| `model/`, `baseline/` | the workbook and the 2011 baseline results it must reproduce |
| `releases/`, `methods/`, `scenarios/` | the frozen release chain (2011 and 2025 data; published, corrected and improved methods), the method modules and the named scenarios |
| `data/` | the data layers (2011, 2025, regions, SA2 and NRM tables, ABS cubes) |
| `pipeline/`, `web/` (source, not `node_modules` or `dist`) | the code that builds the yields and land, and the browser evaluator |
| `results/` | the generated numbers, one file per release, from which every table and figure is built |
| `analysis/` | one folder per question, each with a README, including `analysis/figures_2025/paper_A/` and `paper_B/` (figure scripts, PNG and SVG files, `figures.csv`) |
| `papers/` | both drafts, their supplementary information, highlights, declarations, references and these submission files |
| `qa/` | the claims, literature and sources registers, the decisions file, and the briefs and reports that record how each number was checked (the AI declaration says these are kept in the repository) |
| `ERRATA.md`, `CORRECTION_NOTES.md`, `README.md`, `LICENSE`, `LICENSE-DATA.md`, `CITATION.cff` | the errata, the licences and the citation file |

## What is excluded, and why

| Excluded | Why |
|---|---|
| The private archive repository `MurrayLane/carrying-capacity-models` and the PDFs, scans and workbooks in it (the thesis, journal articles, ABARES, MLA, CSIRO and AUSNUT reports, the comparators' scans) | copyrighted by their publishers; the papers cite them, and the sources register (`qa/sources_register.csv`) gives each one's origin, date and sha256 so a reader can fetch the same file |
| FAOSTAT bulk downloads | not stored in the repository; `qa/fao_bulk_hashes.csv` holds the file hashes |
| Land-use raster and ABS boundary files, where the sources register says they are not stored | large public files owned by their publishers; the register names the origin |
| `web/node_modules`, `web/dist`, build output, `__pycache__` | not tracked by git; rebuilt by `npm ci` |
| The `legacy-java` branch and history before the tag | a tag archive holds one commit's files only |
| Source data's own licences | source data from the ABS and other agencies keep their publishers' licences (`LICENSE-DATA.md`); the archive does not relicense them |

`git archive` holds only tracked files, so it follows these exclusions without a list. A search of the working tree on 2026-11-18 found no PDF file outside `web/node_modules`; repeat `find . -name '*.pdf' -not -path './web/node_modules/*'` on the submission commit.

## Licence

As the repository states it: code MIT (`LICENSE`); model workbook, default inputs, 2011 baseline and analysis outputs CC BY 4.0 (`LICENSE-DATA.md`); source data keep their publishers' licences. Zenodo's licence field takes one value, so `metadata.json` carries `mit` (the file named `LICENSE`) and the description states the CC BY 4.0 part; if the form lets Murray add a second licence, add `cc-by-4.0`. `CITATION.cff` gives version 1.0.0 and the date 2026-11-03; the deposit version is `submission-1`; Murray may wish the two to agree.

## Steps and commands (written here, not run)

The coordinator commits first, so the tag has a commit to point at. Then, from the repository root, Murray or the coordinator runs:

```bash
# 1. check the commit to be tagged: clean tree, final drafts in
git status
git log -1 --stat

# 2. tag that commit (replace the placeholder with the hash from step 1)
git tag -a submission-1 -m "Submission 1: Paper A (Population and Environment) and Paper B (Ecological Economics)" [submission commit hash]

# 3. check the tag, then publish it to the public repository
git show --stat submission-1
git push origin submission-1

# 4. build the archive from the tag, outside the working tree
git archive --format=zip --prefix=carrying-capacity-dashboard-submission-1/ -o ../carrying-capacity-dashboard-submission-1.zip submission-1
sha256sum ../carrying-capacity-dashboard-submission-1.zip
```

Then in Zenodo: start a new upload, add the zip, fill the form from `metadata.json` (title, creators, description, keywords, licence, version), add the related identifiers once the papers have DOIs or leave the two paper rows out, and publish. Zenodo's GitHub integration is an alternative to steps 3 and 4 but needs a GitHub release, not only a tag. The DOI shown is a version DOI; the record also has a concept DOI that always points to the latest version. Murray chooses which goes in the papers (the version DOI reproduces exactly what was submitted).

The tagged commit holds both drafts with the placeholder `[DOI]` in their data statements. The DOI goes into the two submitted manuscripts, and the repository's drafts take it in one small patch committed after the tag; the tag is not moved. (If Murray prefers the DOI inside the archived drafts, Zenodo can reserve the DOI before publishing; patch, commit, then tag.)

## The sentences each paper carries once the DOI exists

**Paper A** (`papers/A_results/draft/A_s09-12.md`, the closing "Data and code availability"). Replace "The claims and sources registers are published with the archive (DOI: [to be added at release])." with:

> The repository at the commit tagged submission-1, with the claims and sources registers, is archived at https://doi.org/[DOI] [dataset].

**Paper B** (`papers/B_methods/draft/B_s06-09.md`, section 9.4). Replace the last sentence ("On 18 November 2026 the archive has no DOI and the author has not deposited it on Zenodo.") with:

> The repository at the commit tagged submission-1 is archived at https://doi.org/[DOI] [dataset].

**Reference-list entry for each paper** (placeholders for the author's name and the DOI):

* Paper B, Elsevier form: `[Author surname, initials], 2026. Carrying Capacity Dashboard: model, data and results, version submission-1 [dataset]. Zenodo. https://doi.org/[DOI]`
* Paper A, Springer author-date form: `[Author surname, initials] (2026) Carrying Capacity Dashboard: model, data and results, version submission-1 [dataset]. Zenodo. https://doi.org/[DOI]`

The portal fields for research data (Ecological Economics, Option C) and the data statement of Paper A take the same DOI.

## Before the tag

* The final blind reads (V57a, V57b), the gate 6 apply and any last patches are in the commit.
* `papers/CORRESPONDENCE/` holds draft emails to the HALF and people-per-hectare authors and `papers/*/response_letter_round2.md` answer simulated referee reports. All sit in the public repository once tagged. Murray decides whether they stay.
