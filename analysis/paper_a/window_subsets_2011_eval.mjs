// Evaluates release 2011-fixed-3 with the yield vectors of each 2011 three-year subset (B138 item 6). Called by window_subsets_2011.py:
//   cd web && node ../analysis/paper_a/window_subsets_2011_eval.mjs YIELDS.json OUT.csv
// Rows: the five-year window (as released, label "all five years"), then each subset; Australia, the seven states and the 53 regions (52 NRM regions and the Northern Territory), both presets.
// Columns carry the capacity, its ratio to the five-year capacity, the population over capacity, and for Australia the 2025-fixed capacity and its ratio to the subset's 2011 capacity.
import fs from 'node:fs'; import path from 'node:path';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir, PRESETS } from '../../web/scripts/results-lib.mjs';
const [yieldsFile, outFile] = process.argv.slice(2);
const P = JSON.parse(fs.readFileSync(yieldsFile)), id = P.release;
const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions, ev = new Evaluator(model);
const m25 = JSON.parse(fs.readFileSync(path.join(dataDir('2025-fixed'), 'model.json'))), r25 = JSON.parse(fs.readFileSync(path.join(dataDir('2025-fixed'), 'regions.json'))).regions, ev25 = new Evaluator(m25);
const cap = (e, z, p, yv) => { const zz = yv ? { ...z, yield: yv } : z; return e.evaluate(zz, { ...z.land, ...z.presets[p], population: z.population }).capacity; };
const cap25 = {}; for (const p of PRESETS) cap25[p] = cap(ev25, r25[1], p);
const sets = [{ name: 'all five years (2005-06 to 2009-10, as released)', consecutive: '', yields: null }, ...P.subsets];
const zones = Object.values(regions).sort((a, b) => a.id - b.id).filter(z => z.kind === 'nation' || z.kind === 'state' || z.kind === 'region' || z.id === 60);
const base = {};
const rows = [['subset', 'consecutive', 'preset', 'zone', 'name', 'kind', 'population', 'capacity', 'ratio_to_five_year_capacity', 'population_over_capacity', 'over_capacity', 'capacity_2025_fixed_australia', 'ratio_2025_over_2011_australia']];
for (const s of sets) for (const p of PRESETS) for (const z of zones) {
  const c = cap(ev, z, p, s.yields ? s.yields[z.id] : null), key = p + '|' + z.id; if (!s.yields) base[key] = c;
  const nat = z.id === 1;
  rows.push([s.name, s.consecutive === '' ? '' : (s.consecutive ? 1 : 0), p, z.id, z.name, z.kind, z.population, Math.round(c), base[key] ? (c / base[key]).toFixed(4) : '', z.population ? (z.population / c).toFixed(4) : '', z.population > c ? 1 : 0,
    nat ? Math.round(cap25[p]) : '', nat ? (cap25[p] / c).toFixed(4) : '']);
}
const q = v => /[",]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : v;
fs.writeFileSync(outFile, rows.map(r => r.map(q).join(',')).join('\n') + '\n');
console.log('wrote', outFile, rows.length - 1, 'rows');
