#!/usr/bin/env bash
# B151: build the submission files for both papers. Run from the repository root:
#   bash qa/tools/build_submission.sh
# Reads the section files, registers and figure scripts' outputs as they stand; edits none of them.
# Writes papers/SUBMISSION/build/{A,B}/ (manuscript .docx and .md, supplement .docx and .md, figure PDFs and PNGs,
# highlights.txt for Paper B, keywords.txt for Paper A) and papers/SUBMISSION/build/_work/ (intermediate files).
# assemble_draft.py --submission also (re)writes papers/<paper>/draft/paper_<P>_submission.md, as that tool always does.
# Nothing is uploaded, tagged, sent or published. Needs python3 and pandoc; no network.
set -euo pipefail
cd "$(dirname "$0")/../.."
BUILD=papers/SUBMISSION/build
WORK=$BUILD/_work
FIG=analysis/figures_2025
mkdir -p "$BUILD/A" "$BUILD/B" "$WORK"

# (a) the submission markdown: title only, no working headings, drafter notes or comments
python3 qa/tools/assemble_draft.py A --submission
python3 qa/tools/assemble_draft.py B --submission

# (b) reference lists without id comments, written to the work folder (the lists in draft/ are left alone)
python3 qa/tools/make_references.py A --style springer --no-ids --out "$WORK/references_A.md" > "$WORK/make_references_A.log"
python3 qa/tools/make_references.py B --no-ids --out "$WORK/references_B.md" > "$WORK/make_references_B.log"

# (c) compose each manuscript: title, abstract, keywords, main text, statements, references
python3 -I - <<'PY'
import re
def rd(p): return open(p, encoding="utf-8").read()
def clean(t):
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    return re.sub(r"\n{3,}", "\n\n", t).strip() + "\n"
def keywords(p):
    m = re.search(r"#\s*Keywords\s*\n+(.+)", rd(p))
    return m.group(1).strip()
paths = {"A": ("papers/A_results/draft", "Declarations", "## Declarations"),
         "B": ("papers/B_methods/draft", "Declaration of generative AI", "## Declaration of generative AI")}
for P, (d, _, cut) in paths.items():
    t = rd(f"{d}/paper_{P}_submission.md")
    # the section files end with a declarations block; the statements file replaces it so each statement appears once
    i = t.index("\n" + cut)
    t = re.sub(r"\n---\s*$", "", t[:i].rstrip()) + "\n"
    kw = keywords(f"{d}/highlights.md")
    t = re.sub(r"(\n## Abstract\n.*?)(\n## 1\.)", lambda m: m.group(1).rstrip() + f"\n\n**Keywords:** {kw}\n" + m.group(2), t, count=1, flags=re.S)
    stm = clean(rd(f"{d}/acknowledgements_and_statements.md"))
    ref = clean(rd(f"papers/SUBMISSION/build/_work/references_{P}.md"))
    ref = re.sub(r"^# References", "## References", ref)
    out = clean(t) + "\n" + stm + "\n" + ref
    open(f"papers/SUBMISSION/build/{P}/paper_{P}.md", "w", encoding="utf-8").write(out)
    sup = clean(rd(f"{d}/supplementary.md"))
    open(f"papers/SUBMISSION/build/{P}/Supplement_{P}.md", "w", encoding="utf-8").write(sup)
    if P == "A":
        open(f"papers/SUBMISSION/build/A/keywords.txt", "w", encoding="utf-8").write(kw + "\n")
# (f) Ecological Economics highlights: the bullets only, one per line, no keywords
h = rd("papers/B_methods/draft/highlights.md").split("# Keywords")[0]
bul = [l[2:].strip() for l in h.splitlines() if l.startswith("- ")]
open("papers/SUBMISSION/build/B/highlights.txt", "w", encoding="utf-8").write("\n".join(bul) + "\n")
PY

# (d) .docx with pandoc, default styles; zip timestamps and core properties fixed so a rerun is identical
fixdocx() {
python3 -I - "$1" <<'PY'
import sys, zipfile, re, shutil
p = sys.argv[1]; tmp = p + ".tmp"
with zipfile.ZipFile(p) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
    for n in zi.namelist():
        b = zi.read(n)
        if n == "docProps/core.xml":
            b = re.sub(rb"(<dcterms:(created|modified)[^>]*>)[^<]*", rb"\g<1>2026-01-01T00:00:00Z", b)
        zi_ = zipfile.ZipInfo(n, (2026, 1, 1, 0, 0, 0)); zi_.compress_type = zipfile.ZIP_DEFLATED
        zi_.external_attr = 0o644 << 16
        zo.writestr(zi_, b)
shutil.move(tmp, p)
PY
}
for P in A B; do
  for stem in paper_$P Supplement_$P; do
    pandoc -f markdown -t docx --metadata date=2026-01-01 "$BUILD/$P/$stem.md" -o "$BUILD/$P/$stem.docx"
    fixdocx "$BUILD/$P/$stem.docx"
  done
done

# (e) figures with journal-style names: Paper A Figs 1 to 8 (and S6), Paper B Figs 1 to 3 (full-page 190 mm set)
copyfig() { cp "$1.pdf" "$2.pdf"; cp "$1.png" "$2.png"; }
n=1
for s in fig1_national_capacity_population fig2_regional_change_flips fig3_layer_effects fig4_scale_curve fig5_long_term fig6_shocks fig7_method_effects fig8_migration_map; do
  copyfig "$FIG/paper_A/$s" "$BUILD/A/Fig$n"; n=$((n+1))
done
copyfig "$FIG/paper_A/fig6s_scenarios" "$BUILD/A/FigS6"
n=1
for s in fig1_method_map_190mm fig2_method_readings_190mm fig3_design_choices_190mm; do
  copyfig "$FIG/paper_B/$s" "$BUILD/B/Fig$n"; n=$((n+1))
done

# (g) counts and placeholders
echo "== Main text words (qa/tools/wordcount.py, prose only)"
for P in A B; do echo "Paper $P: $(python3 qa/tools/wordcount.py $P | grep TOTAL)"; done
python3 -I - <<'PY'
import re
for P in "AB":
    t = open(f"papers/SUBMISSION/build/{P}/paper_{P}.md", encoding="utf-8").read()
    m = re.search(r"## Abstract\n(.*?)\n\*\*Keywords", t, re.S)
    a = m.group(1).strip()
    print(f"Abstract Paper {P}: {len(a.split())} words, {len(a)} characters")
b = [l.rstrip("\n") for l in open("papers/SUBMISSION/build/B/highlights.txt", encoding="utf-8")]
print("Highlights (Paper B, limit 85):", ", ".join(str(len(x)) for x in b), "characters;", len(b), "bullets")
print("Keywords Paper A:", len(open("papers/SUBMISSION/build/A/keywords.txt").read().split(";")), "items")
print("== Placeholders ('[') left in the built files (file: count of lines, then each distinct bracket text)")
import glob, collections
for f in sorted(glob.glob("papers/SUBMISSION/build/[AB]/*.md") + glob.glob("papers/SUBMISSION/build/[AB]/*.txt")):
    c = collections.Counter(); lines = 0
    for l in open(f, encoding="utf-8"):
        if "[" in l:
            lines += 1
            for x in re.findall(r"\[[^\]]*\]?", l): c[x[:90]] += 1
    print(f"{f}: {lines} lines with '['")
    for k, v in sorted(c.items()): print(f"    {v} x {k}")
PY
echo "== Files"
ls -l "$BUILD/A" "$BUILD/B" | sed 's/^/  /'
