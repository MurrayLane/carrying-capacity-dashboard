// Sensitivity of the dairy-good-land module to the source of the improved-pasture share: CLUM (the module's default; Queensland is 0.1% improved, contradicted by the ABS and by the milk produced there)
// against the ABS 2007-08 share of grazing land that is improved pasture, by zone (data/2025/abs_improved_pasture_2007_08_by_zone.csv, abs_improved_check.py), times the pasture-weighted GAEZ arable share of the zone.
// Yield on good land: 73 g/m2 (CLUM basis) or 84.4 (observed milk per m2 of ABS-improved pasture, same 90%-of-milk zones). Takes the built release (GAEZ move undone) and applies each variant. Writes results/dairy_abs_basis.csv.
//   cd web && node ../analysis/pasture_2025/dairy_abs_improved_test.mjs        (after npm run build:data)
import fs from 'node:fs'; import path from 'node:path';
import { root, methodModule } from '../../web/scripts/releases.mjs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const csv = f => { const [h, ...r] = fs.readFileSync(path.join(root, f), 'utf8').trim().split(/\r?\n/).map(l => l.split(',')); return r.map(x => Object.fromEntries(h.map((k, i) => [k, x[i]]))); };
const D = methodModule('dairy-good-land').dairyGoodLand, G = Object.fromEntries(csv(D.file).map(r => [+r.zone, r])), A = Object.fromEntries(csv('data/2025/abs_improved_pasture_2007_08_by_zone.csv').map(r => [+r.zone, +r.abs_improved_share_of_grazing]));
const YABS = +(process.argv[2] ?? 84.4);
const out = [['release', 'preset', 'zone', 'name', 'population', 'clum_gaez_default', 'abs_none_arable', 'abs_gaez', 'abs_gaez_broad', 'abs_all_arable', 'abs_gaez_yield73']];
for (const id of ['2011-improved', '2025-improved']) {
  const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), RJ = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))), regions = RJ.regions, k = RJ.yieldRows.indexOf(D.yieldRow), ev = new Evaluator(model);
  for (const z of Object.values(regions).sort((a, b) => a.id - b.id)) for (const preset of ['short', 'long']) {
    const g = +G[z.id][D.column], pasture0 = z.land.pasture / (1 - g), crop0 = z.land.cropping - g * pasture0, impA = A[z.id];
    const cap = (share, yv) => { const y = z.yield.slice(); y[k] = yv; return ev.evaluate({ ...z, yield: y }, { ...z.land, cropping: crop0 + share * pasture0, pasture: pasture0 * (1 - share), ...z.presets[preset], population: z.population }).capacity; };
    out.push([id, preset, z.id, z.name, z.population, cap(g, 73), cap(0, YABS), cap(impA * +G[z.id].gaez_arable_of_pasture, YABS), cap(impA * +G[z.id].gaez_arable_broad_of_pasture, YABS), cap(impA, YABS), cap(impA * +G[z.id].gaez_arable_of_pasture, 73)]);
  }
}
fs.writeFileSync(path.join(root, 'results', 'dairy_abs_basis.csv'), out.map(r => r.map(v => typeof v === 'number' ? Math.round(v) : v).join(',')).join('\n') + '\n');
for (const r of out.slice(1).filter(r => [1, 2, 15, 26, 40, 49, 56, 60].includes(r[2]) && r[0] === '2025-improved')) console.log(r[1], String(r[3]).padEnd(10), 'pop', (r[4] / 1e6).toFixed(2), '| CLUM', (r[5] / 1e6).toFixed(2), '| ABS a=0', (r[6] / 1e6).toFixed(2), 'GAEZ', (r[7] / 1e6).toFixed(2), 'broad', (r[8] / 1e6).toFixed(2), 'all', (r[9] / 1e6).toFixed(2), '| ABS GAEZ at 73', (r[10] / 1e6).toFixed(2));
