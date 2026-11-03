// Dairy only on land that can support it at its known yield (Murray 2026-11-03). In the workbook dairy's land is a pasture use (Settings!D34). Here dairy is moved to the cropping column (Settings!C34): it competes
// with crops for "good land" = cropland plus the arable share of the improved pasture, and cannot use rangeland; beef and sheep keep the pasture pool and, as in the workbook, borrow cropland when pasture is short.
// The milk yield on good land is the observed output per m2 of improved pasture in the zones holding 90% of the milk (analysis/pasture_2025/pasture_quality.py: 73 g/m2; the workbook's average-pasture figure is about 26).
// Arable share a of the improved pasture: 0 (lower bound: improved pasture cannot be cropped), the GAEZ share of each SA2 (data/sa2/arable_share_gaez_by_sa2.csv), 1 (upper bound). Non-arable improved pasture stays
// in the pasture pool and is NOT open to dairy (conservative: dairy could use it). Short term, state yields, results as a share of the national capacity of the unchanged model on today's diet.
//   cd web && node ../analysis/pasture_2025/two_pool_test.mjs [RELEASE] [DAIRY_YIELD_G_M2]
import fs from 'node:fs'; import path from 'node:path';
import { root } from '../../web/scripts/releases.mjs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const id = process.argv[2] ?? '2025-fixed', YG = +(process.argv[3] ?? 73), preset = 'short';
const csv = f => { const [h, ...rows] = fs.readFileSync(path.join(root, f), 'utf8').trim().split('\n').map(l => l.replace(/\r$/, '').split(',')); return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]]))); };
const meth = csv('data/sa2/land_2011_method_by_sa2.csv'), hier = Object.fromEntries(csv('data/sa2/land_types_by_sa2.csv').map(r => [r.sa2_code, r]));
const imp = Object.fromEntries(csv('data/sa2/improved_pasture_by_sa2.csv').map(r => [r.sa2_code, +r.improved_km2])), ar = Object.fromEntries(csv('data/sa2/arable_share_gaez_by_sa2.csv').map(r => [r.sa2_code, +r.arable_share_gaez || 0]));
const KEYS = ['cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1'];
const baseModel = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), RJ = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))), regions = RJ.regions, N = regions[1];
const evBase = new Evaluator(baseModel);
const two = JSON.parse(JSON.stringify(baseModel)); const S = two.sheets.Settings.cells;
if (!/AC90:Base!AC143/.test(S['33:3'])) throw new Error('Settings!D34 is not the dairy pasture formula: ' + S['33:3']);
S['33:2'] = S['33:3']; S['33:3'] = 0; const evTwo = new Evaluator(two);        // dairy's land moves from the pasture column (D) to the cropping column (C)
const DAIRY = RJ.yieldRows.indexOf(97), STATE_ZONE = { 1: 2, 2: 15, 3: 26, 4: 40, 5: 49, 6: 56, 7: 60, 8: 2, 9: 1 };
const sa = meth.map(r => ({ code: r.sa2_code, sa3: hier[r.sa2_code]?.sa3_code, sa4: hier[r.sa2_code]?.sa4_code, state: +hier[r.sa2_code]?.state, cropping: +r.cropping_km2, pasture: +r.pasture_km2, nonAg: +r.nonAgricultural_km2, infrastr1: +r.infrastructure_km2, nature1: +r.reserve_km2, imp: imp[r.sa2_code] ?? 0, arImp: (imp[r.sa2_code] ?? 0) * (ar[r.sa2_code] ?? 0) }));
const agg = us => ({ ...Object.fromEntries(KEYS.concat('imp', 'arImp').map(k => [k, us.reduce((a, u) => a + u[k], 0)])), state: us[0].state });
const capBase = (u, over) => { const z = regions[STATE_ZONE[u.state] ?? 1]; const o = evBase.evaluate({ ...N, yield: z.yield }, { ...N.presets[preset], irrigation: z.presets[preset].irrigation, nature2: z.presets[preset].nature2, ...over, ...Object.fromEntries(KEYS.map(k => [k, u[k]])), population: 1 }).capacity; return Number.isFinite(o) ? o : 0; };
const capTwo = (u, over, mode) => { const z = regions[STATE_ZONE[u.state] ?? 1], y = z.yield.slice(); y[DAIRY] = YG; const a = mode === 'upper' ? u.imp : mode === 'lower' ? 0 : u.arImp;
  const o = evTwo.evaluate({ ...N, yield: y }, { ...N.presets[preset], irrigation: z.presets[preset].irrigation, nature2: z.presets[preset].nature2, ...over, ...Object.fromEntries(KEYS.map(k => [k, u[k]])), cropping: u.cropping + a, pasture: u.pasture - a, population: 1 }).capacity; return Number.isFinite(o) ? o : 0; };
const natU = { ...agg(sa), state: 9 }; const natToday = capBase(natU, {});
const m4 = key => { const m = new Map(); for (const u of sa) (m.get(u[key]) ?? m.set(u[key], []).get(u[key])).push(u); return [...m.values()].map(agg); };
const levels = [['Australia', [natU]], ['State', (() => { const m = new Map(); for (const u of sa) { const k = u.state === 8 ? 1 : u.state; (m.get(k) ?? m.set(k, []).get(k)).push(u); } return [...m.values()].map(agg); })()], ['SA4', m4('sa4')], ['SA3', m4('sa3')], ['SA2', sa]];
console.log(`${id}: dairy milk yield on good land ${YG} g/m2 (workbook national ${N.yield[DAIRY].toFixed(1)}); improved pasture ${sa.reduce((a, u) => a + u.imp, 0).toFixed(0)} km2, of which arable by GAEZ ${(sa.reduce((a, u) => a + u.arImp, 0) / sa.reduce((a, u) => a + u.imp, 0) * 100).toFixed(0)}%; national capacity ${(natToday / 1e6).toFixed(1)} M`);
const rows = [['diet', 'level', 'units', 'unchanged_model', 'two_pool_a0', 'two_pool_gaez', 'two_pool_a1']];
for (const [dl, over] of [["today's diet", {}], ['2.5% meat and eggs', { meategg: 0.025 }]]) { console.log(`\n${dl}: share of the national capacity of the unchanged model on today's diet (${(natToday / 1e6).toFixed(1)} M)`); console.log('level      units  unchanged | two pools: a=0 (improved not arable) | GAEZ arable share | a=1 (all improved arable)');
  for (const [name, units] of levels) { const v = [units.reduce((s, u) => s + capBase(u, over), 0), ...['lower', 'gaez', 'upper'].map(m => units.reduce((s, u) => s + capTwo(u, over, m), 0))].map(x => x / natToday * 100);
    console.log(name.padEnd(10), String(units.length).padStart(5), v.map(x => (x.toFixed(0) + '%').padStart(9)).join('  ')); rows.push([dl, name, units.length, ...v.map(x => x.toFixed(1))]); } }
fs.writeFileSync(path.join(root, 'analysis/pasture_2025/two_pool.csv'), rows.map(r => r.join(',')).join('\n') + '\n');
