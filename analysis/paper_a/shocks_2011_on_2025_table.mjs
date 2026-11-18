// B133 (decision 135): 2011's bad years on the 2025 weather table. Release 2011-fixed-3 (the corrected 2011 release) with the resilience sheet of 2025-fixed (the table of the data to 2024-25)
// in place of its own (the thesis table), so that both years meet the same drought factors. An override in this script; no release is made or changed.
//   node analysis/paper_a/shocks_2011_on_2025_table.mjs analysis/paper_a/shocks_2011_on_2025_table.csv      (repository root; needs the built data)
// writes the table above and <out minus .csv>_summary.csv. Method as shocks_by_region.mjs: short-term settings, drought return periods 1, 5, 10, 20, 50 and 100, Australia, the 52 NRM regions and the
// Northern Territory (53 regions), capacity against the release's own population. Three bases in one file (column basis):
//   2011_thesis_table     2011-fixed-3 as published (its own table); must equal the 2011-fixed-3 rows of shocks_by_region-3.csv (checked below, the script stops if not)
//   2011_on_2025_table    2011-fixed-3 with the resilience sheet of 2025-fixed
//   2025_2025_table       2025-fixed as published; must equal the 2025-fixed rows of shocks_by_region-3.csv (checked)
// The two resilience sheets must have the same layout (same cells, same labels and formulas; only the numbers of the table differ): checked, the script stops if not.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const out = process.argv[2] ?? 'analysis/paper_a/shocks_2011_on_2025_table.csv', root = new URL('../../', import.meta.url).pathname, base = root + 'web/public/data/';
const load = id => ({ model: JSON.parse(fs.readFileSync(`${base}${id}/model.json`)), regions: JSON.parse(fs.readFileSync(`${base}${id}/regions.json`)).regions });
const A = load('2011-fixed-3'), B = load('2025-fixed');
const ta = A.model.sheets.resilience, tb = B.model.sheets.resilience;
{ const ka = Object.keys(ta.cells).sort(), kb = Object.keys(tb.cells).sort(); let numeric = 0;
  if (ka.join() !== kb.join() || ta.rows !== tb.rows || ta.cols !== tb.cols) { console.error('the resilience sheets have different cells'); process.exit(1); }
  for (const k of ka) { const x = ta.cells[k], y = tb.cells[k]; if (typeof x === 'number' && typeof y === 'number') numeric++; else if (x !== y) { console.error(`resilience ${k}: ${x} against ${y}`); process.exit(1); } }
  console.error(`resilience sheets: same layout, ${numeric} numeric cells`); }
const swapped = JSON.parse(JSON.stringify(A.model)); swapped.sheets.resilience = JSON.parse(JSON.stringify(tb));
const RUNS = [['2011_thesis_table', '2011-fixed-3', A.model, A.regions], ['2011_on_2025_table', '2011-fixed-3', swapped, A.regions], ['2025_2025_table', '2025-fixed', B.model, B.regions]];
const rows = ['basis,release,zone,name,kind,return_period,capacity,population,people_over_capacity,capacity_over_population'];
const cap = {};
for (const [basis, rel, model, regions] of RUNS) {
  const ev = new Evaluator(model);
  for (const [z, R] of Object.entries(regions)) {
    if (!(R.kind === 'region' || z === '60' || z === '1')) continue;
    for (const T of [1, 5, 10, 20, 50, 100]) {
      const c = Math.round(ev.evaluate(R, { ...R.land, ...R.presets.short, resilience: T, population: R.population }).capacity);
      cap[`${basis}|${rel}|${z}|${T}`] = c;
      rows.push([basis, rel, z, JSON.stringify(R.name), R.kind, T, c, R.population, (R.population / c).toFixed(3), (c / R.population).toFixed(3)].join(','));
    }
  }
}
// check against the published shocks_by_region-3.csv rows (rounded integers, same method)
const ref = fs.readFileSync(root + 'analysis/paper_a/shocks_by_region-3.csv', 'utf8').trim().split(/\r?\n/).slice(1).map(l => l.split(','));
let n = 0, bad = 0;
for (const c of ref) { const rel = c[0], z = c[1], T = c[c.length - 3], capv = +c[c.length - 2]; const basis = rel === '2025-fixed' ? '2025_2025_table' : '2011_thesis_table'; n++; if (cap[`${basis}|${rel}|${z}|${T}`] !== capv) { bad++; if (bad < 5) console.error(`differs from shocks_by_region-3.csv: ${rel} zone ${z} T ${T}: ${cap[`${basis}|${rel}|${z}|${T}`]} against ${capv}`); } }
console.error(`checked ${n} published rows of shocks_by_region-3.csv: ${bad} differ`);
if (bad) process.exit(1);
fs.writeFileSync(out, rows.join('\n') + '\n');
// summary: national and the count of regions over capacity, for each basis and return period
const sum = ['basis,return_period,national_capacity,national_population,people_over_capacity,capacity_over_population,regions_over_capacity_of_53,regions_tipping_over_capacity_against_the_average_year,share_of_population_in_over_capacity_regions'];
for (const [basis, rel, , regions] of RUNS) for (const T of [1, 5, 10, 20, 50, 100]) {
  const reg = Object.entries(regions).filter(([z, R]) => R.kind === 'region' || z === '60'), over = reg.filter(([z, R]) => cap[`${basis}|${rel}|${z}|${T}`] < R.population);
  const tip = over.filter(([z, R]) => cap[`${basis}|${rel}|${z}|1`] >= R.population).length;
  const pop = reg.reduce((s, [, R]) => s + R.population, 0), popOver = over.reduce((s, [, R]) => s + R.population, 0), N = regions[1];
  const c = cap[`${basis}|${rel}|1|${T}`];
  sum.push([basis, T, c, N.population, (N.population / c).toFixed(3), (c / N.population).toFixed(3), over.length, tip, (popOver / pop).toFixed(4)].join(','));
}
fs.writeFileSync(out.replace(/\.csv$/, '_summary.csv'), sum.join('\n') + '\n');
for (const l of sum) console.log(l);
