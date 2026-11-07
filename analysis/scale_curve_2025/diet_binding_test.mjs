// Which land type binds as the diet changes? For representative units (the nation, a rangeland NRM zone, a cropping NRM zone, a mixed SA4): capacity, and the land used against the land held (cropping, pasture)
// at the capacity, over meat-and-egg shares and red-meat shares.   cd web && node ../analysis/scale_curve_2025/diet_binding_test.mjs [RELEASE]
import fs from 'node:fs'; import path from 'node:path';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const id = process.argv[2] ?? '2025-fixed', preset = 'short';
const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions, ev = new Evaluator(model), N = regions[1];
const KEYS = ['cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1'];
const byName = n => Object.values(regions).find(z => z.name.startsWith(n));
const units = [['Australia', N], ['SA Arid Lands (rangeland)', byName('SA Arid Lands')], ['Eyre Peninsula (cropping)', byName('Eyre Peninsula')], ['Avon (WA wheatbelt)', byName('Avon')], ['WA Rangelands', byName('Rangelands')], ['Murray (NSW)', byName('Murray')]];
const run = (z, over) => { const Y = z.kind === 'region' ? regions[z.parent] : z; /* a region takes its parent state's record; the nation and the NT zone (a state) take their own */ const o = ev.evaluate(Y, { ...N.presets[preset], irrigation: Y.presets[preset].irrigation, nature2: Y.presets[preset].nature2, ...over, ...Object.fromEntries(KEYS.map(k => [k, z.land[k]])), population: 1 }); return o; };
for (const [label, z] of units) { if (!z) { console.log('missing', label); continue; }
  console.log(`\n${label}: land held, km2: cropping ${Math.round(z.land.cropping).toLocaleString()}, pasture ${Math.round(z.land.pasture).toLocaleString()}`);
  console.log('  meat+eggs  red   capacity(thousand)  cropping used/held   pasture used/held   excess land km2');
  for (const [m, r] of [[0.12, 0.578], [0.075, 0.578], [0.025, 0.578], [0, 0.578], [0.05, 1], [0.1, 1], [0.15, 1], [0.025, 0], [0.1, 0]]) { const o = run(z, { meategg: m, redmeat: r }); const u = o.used, e = o.existing;
    console.log('  ' + (m * 100).toFixed(1).padStart(8) + '%' + (r * 100).toFixed(0).padStart(5) + '%' + String(Math.round(o.capacity / 1e3)).padStart(15) + (Math.round(u[0]).toLocaleString() + ' / ' + Math.round(e[0]).toLocaleString()).padStart(28) + (Math.round(u[1]).toLocaleString() + ' / ' + Math.round(e[1]).toLocaleString()).padStart(24) + String(Math.round(o.excess?.[5]?.[0] ?? 0)).padStart(14)); } }
