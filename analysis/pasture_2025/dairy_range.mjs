// The range for the arable share of the improved pasture in the dairy-good-land module (methods/dairy-good-land): none of it arable (a=0), the GAEZ share (the module's default) and all of it (a=1).
// Starts from the built data of a release that includes the module, takes its GAEZ move of pasture to cropping back, and applies each bound. The effect of the module itself against the improved method
// without it is in results/method_effects.csv. Writes results/dairy_range.csv. Run after `npm run build:data`.
//   cd web && node ../analysis/pasture_2025/dairy_range.mjs
import fs from 'node:fs'; import path from 'node:path';
import { root, methodModule } from '../../web/scripts/releases.mjs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const mod = methodModule('dairy-good-land'), D = mod.dairyGoodLand;
const rows = fs.readFileSync(path.join(root, D.file), 'utf8').trim().split(/\r?\n/).map(l => l.split(',')), H = rows[0];
const col = n => H.indexOf(n), shares = Object.fromEntries(rows.slice(1).map(r => [+r[0], { gaez: +r[col('arable_improved_share')], upper: +r[col('improved_share')], lower: 0 }]));
const out = [['release', 'preset', 'zone', 'name', 'population', 'a0_none_arable', 'gaez_default', 'a1_all_arable']];
for (const id of ['2011-improved', '2025-improved']) {
  const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions;
  const k = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).yieldRows.indexOf(D.yieldRow);
  const withMod = new Evaluator(model);
  for (const z of Object.values(regions).sort((a, b) => a.id - b.id)) for (const preset of ['short', 'long']) {
    const g = shares[z.id].gaez, pasture0 = z.land.pasture / (1 - g), crop0 = z.land.cropping - g * pasture0;
    const cap = (ev, a) => { const y = z.yield.slice(); const c = crop0 + a * pasture0, p = pasture0 * (1 - a);
      return ev.evaluate({ ...z, yield: y }, { ...z.land, cropping: c, pasture: p, ...z.presets[preset], population: z.population }).capacity; };
    out.push([id, preset, z.id, z.name, z.population, cap(withMod, shares[z.id].lower), cap(withMod, g), cap(withMod, shares[z.id].upper)]);
  }
}
fs.writeFileSync(path.join(root, 'results', 'dairy_range.csv'), out.map(r => r.map(v => v === null ? '' : typeof v === 'number' ? Math.round(v) : v).join(',')).join('\n') + '\n');
for (const r of out.slice(1).filter(r => r[2] === 1)) console.log(r[0], r[1], 'a=0', (r[5] / 1e6).toFixed(2), ' GAEZ', (r[6] / 1e6).toFixed(2), ' a=1', (r[7] / 1e6).toFixed(2));
