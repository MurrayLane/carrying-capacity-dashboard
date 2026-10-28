// Writes results/ at the repository root: one CSV per release (every zone, both presets), results/releases.json (what each release is and the hashes of the built data it was evaluated from)
// and results/comparison_cells.csv (the two-by-two with the data and method effects).   Usage: cd web && npm run build:data && node scripts/make-results.mjs [releaseId ...]
// With ids, only those releases are rewritten (the comparison is rewritten when its four cells are all present).
import fs from 'node:fs';
import path from 'node:path';
import { root } from './releases.mjs';
import { index, evaluateRelease, toCsv, releaseInfo, comparison, comparisonCsv, CELLS } from './results-lib.mjs';

const out = path.join(root, 'results'); fs.mkdirSync(out, { recursive: true });
const ids = process.argv.slice(2).length ? process.argv.slice(2) : index().order;
const read = id => fs.readFileSync(path.join(out, `${id}.csv`), 'utf8').trim().split(/\r?\n/).slice(1).map(l => l.split(','));
const byRelease = {};
for (const id of index().order) {
  if (ids.includes(id)) { const rows = evaluateRelease(id); fs.writeFileSync(path.join(out, `${id}.csv`), toCsv(rows)); byRelease[id] = rows; console.log(id, rows.length, 'rows'); }
}
// comparison: needs the four cells; take any that were not just evaluated from their csv
const need = Object.values(CELLS);
if (need.every(id => byRelease[id] || fs.existsSync(path.join(out, `${id}.csv`)))) {
  const cols = ['release', 'zone', 'name', 'kind', 'parent', 'preset', 'population', 'capacity'];
  for (const id of need) if (!byRelease[id]) byRelease[id] = read(id).map(c => ({ release: c[0], zone: +c[1], name: c[2], kind: c[3], parent: c[4], preset: c[5], population: +c[6], capacity: +c[7] }));
  fs.writeFileSync(path.join(out, 'comparison_cells.csv'), comparisonCsv(comparison(byRelease))); console.log('comparison_cells.csv');
}
fs.writeFileSync(path.join(out, 'releases.json'), JSON.stringify({ default: index().default, releases: index().order.map(releaseInfo) }, null, 1) + '\n');
