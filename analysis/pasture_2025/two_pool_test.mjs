// Dairy on cropland at the milk yield of dairy farms (rebuilt 2026-11-03; the first version moved arable improved pasture to cropping at 73 g/m2, withdrawn: analysis/pasture_2025/README.md). In the workbook dairy's land is a
// pasture use (Settings!D34) at the average milk per m2 of all improved pasture. Here dairy is moved to the cropping column (Settings!C34): it competes with crops for cropland and cannot use rangeland, and its milk yield is its
// state's observed milk per usable hectare of dairy farm (data/2025/dairy_farm_yield_by_state.csv; the national value for the Northern Territory); beef and sheep keep the pasture pool and, as in the workbook, borrow cropland when
// pasture is short. Short term, state yields, results as a share of the national capacity of the unchanged model on today's diet. Columns: unchanged model | dairy on cropland at the observed yield | the same with the yield halved.
//   cd web && node ../analysis/pasture_2025/two_pool_test.mjs [RELEASE]
import fs from 'node:fs'; import path from 'node:path';
import { root } from '../../web/scripts/releases.mjs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const id = process.argv[2] ?? '2025-fixed', preset = 'short';
const csv = f => { const [h, ...rows] = fs.readFileSync(path.join(root, f), 'utf8').trim().split('\n').map(l => l.replace(/\r$/, '').split(',')); return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]]))); };
const meth = csv('data/sa2/land_2011_method_by_sa2.csv'), hier = Object.fromEntries(csv('data/sa2/land_types_by_sa2.csv').map(r => [r.sa2_code, r]));
const YS = Object.fromEntries(csv('data/2025/dairy_farm_yield_by_state.csv').map(r => [r.state, +r.milk_g_per_m2])), YSTATE = { 1: YS.NSW, 2: YS.VIC, 3: YS.QLD, 4: YS.SA, 5: YS.WA, 6: YS.TAS, 7: YS.AUS, 8: YS.NSW, 9: YS.AUS };
const KEYS = ['cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1'];
const baseModel = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), RJ = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))), regions = RJ.regions, N = regions[1];
const evBase = new Evaluator(baseModel);
const two = JSON.parse(JSON.stringify(baseModel)); const S = two.sheets.Settings.cells;
if (!/AC90:Base!AC143/.test(S['33:3'])) throw new Error('Settings!D34 is not the dairy pasture formula: ' + S['33:3']);
S['33:2'] = S['33:3']; S['33:3'] = 0; const evTwo = new Evaluator(two);        // dairy's land moves from the pasture column (D) to the cropping column (C)
const DAIRY = RJ.yieldRows.indexOf(97), STATE_ZONE = { 1: 2, 2: 15, 3: 26, 4: 40, 5: 49, 6: 56, 7: 60, 8: 2, 9: 1 };
const sa = meth.map(r => ({ code: r.sa2_code, sa3: hier[r.sa2_code]?.sa3_code, sa4: hier[r.sa2_code]?.sa4_code, state: +hier[r.sa2_code]?.state, cropping: +r.cropping_km2, pasture: +r.pasture_km2, nonAg: +r.nonAgricultural_km2, infrastr1: +r.infrastructure_km2, nature1: +r.reserve_km2}));
const agg = us => ({ ...Object.fromEntries(KEYS.map(k => [k, us.reduce((a, u) => a + u[k], 0)])), state: us[0].state });
const capBase = (u, over) => { const z = regions[STATE_ZONE[u.state] ?? 1]; const o = evBase.evaluate({ ...N, yield: z.yield }, { ...N.presets[preset], irrigation: z.presets[preset].irrigation, nature2: z.presets[preset].nature2, ...over, ...Object.fromEntries(KEYS.map(k => [k, u[k]])), population: 1 }).capacity; return Number.isFinite(o) ? o : 0; };
const capTwo = (u, over, f) => { const z = regions[STATE_ZONE[u.state] ?? 1], y = z.yield.slice(); y[DAIRY] = YSTATE[u.state] * f;
  const o = evTwo.evaluate({ ...N, yield: y }, { ...N.presets[preset], irrigation: z.presets[preset].irrigation, nature2: z.presets[preset].nature2, ...over, ...Object.fromEntries(KEYS.map(k => [k, u[k]])), population: 1 }).capacity; return Number.isFinite(o) ? o : 0; };
const natU = { ...agg(sa), state: 9 }; const natToday = capBase(natU, {});
const m4 = key => { const m = new Map(); for (const u of sa) (m.get(u[key]) ?? m.set(u[key], []).get(u[key])).push(u); return [...m.values()].map(agg); };
const levels = [['Australia', [natU]], ['State', (() => { const m = new Map(); for (const u of sa) { const k = u.state === 8 ? 1 : u.state; (m.get(k) ?? m.set(k, []).get(k)).push(u); } return [...m.values()].map(agg); })()], ['SA4', m4('sa4')], ['SA3', m4('sa3')], ['SA2', sa]];
console.log(`${id}: dairy on cropland at the observed milk yield of dairy farms by state (${Object.entries(YS).map(([k, v]) => k + ' ' + v).join(', ')} g/m2; workbook national ${N.yield[DAIRY].toFixed(1)}); national capacity ${(natToday / 1e6).toFixed(1)} M`);
const rows = [['diet', 'level', 'units', 'unchanged_model', 'dairy_on_cropland', 'dairy_on_cropland_yield_halved']];
for (const [dl, over] of [["today's diet", {}], ['2.5% meat and eggs', { meategg: 0.025 }]]) { console.log(`\n${dl}: share of the national capacity of the unchanged model on today's diet (${(natToday / 1e6).toFixed(1)} M)`); console.log('level      units  unchanged | dairy on cropland | yield halved');
  for (const [name, units] of levels) { const v = [units.reduce((s, u) => s + capBase(u, over), 0), ...[1, 0.5].map(f => units.reduce((s, u) => s + capTwo(u, over, f), 0))].map(x => x / natToday * 100);
    console.log(name.padEnd(10), String(units.length).padStart(5), v.map(x => (x.toFixed(0) + '%').padStart(9)).join('  ')); rows.push([dl, name, units.length, ...v.map(x => x.toFixed(1))]); } }
fs.writeFileSync(path.join(root, 'analysis/pasture_2025/two_pool.csv'), rows.map(r => r.join(',')).join('\n') + '\n');
