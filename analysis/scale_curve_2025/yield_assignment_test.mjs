// Why does the sum of capacities rise from the states to the SA4s? Test: evaluate the SA levels with three yield assignments (the unit's dominant NRM zone, its parent state's zone, the national vector)
// and compare with the state level. Usage: cd web && node ../analysis/scale_curve_2025/yield_assignment_test.mjs RELEASE   (needs built data)
import fs from 'node:fs'; import path from 'node:path';
import { root } from '../../web/scripts/releases.mjs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const id = process.argv[2] ?? '2025-fixed', year = id.startsWith('2011') ? '2011' : '2025';
const csv = f => { const [h, ...rows] = fs.readFileSync(path.join(root, f), 'utf8').trim().split('\n').map(l => l.replace(/\r$/, '').split(',')); return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]]))); };
const meth = csv('data/sa2/land_2011_method_by_sa2.csv'), hier = Object.fromEntries(csv('data/sa2/land_types_by_sa2.csv').map(r => [r.sa2_code, r])), erp = Object.fromEntries(csv('data/sa2/population_erp.csv').map(r => [r.sa2_code, r]));
const KEYS = ['cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1'];
const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions, ev = new Evaluator(model), R = regions[1];
const STATE_ZONE = { 1: 2, 2: 15, 3: 26, 4: 40, 5: 49, 6: 56, 7: 60, 8: 2, 9: 1 };
const classes = Object.fromEntries(csv('data/sa2/clum_classes.csv').map(r => [r.Value, r.TERTV8.split(' ')[0].replace(/\.$/, '')])), CROPLAND = ['3.3', '3.4', '3.5', '3.6', '4.3', '4.4', '4.5', '4.6'], isCrop = c => CROPLAND.some(p => c === p || c.startsWith(p + '.'));
const ZONE_OF = {}; for (const [z, codes] of Object.entries(JSON.parse(fs.readFileSync(path.join(root, 'pipeline/land/zone_to_nrm2011.json'))).zones)) for (const c of codes) ZONE_OF[c] = +z;
const piece = new Map(); for (const r of csv('data/nrm2011/land_use_by_sa2_nrm2011_piece.csv')) { const n = +r.nrmr_code_2011; if (!(n in ZONE_OF)) continue; const k = r.zone_name + '|' + ZONE_OF[n], p = piece.get(k) ?? { sa2: r.zone_name, zone: ZONE_OF[n], total: 0, cropland: 0 }; p.total += +r.km2; if (isCrop(classes[r.class_code] ?? '')) p.cropland += +r.km2; piece.set(k, p); }
const share = {}; { const by = {}; for (const p of piece.values()) (by[p.sa2] ??= []).push(p); for (const [s, ps] of Object.entries(by)) { const key = ps.some(p => p.cropland > 0) ? 'cropland' : 'total', tot = ps.reduce((a, p) => a + p[key], 0); share[s] = {}; for (const p of ps) share[s][p.zone] = (share[s][p.zone] ?? 0) + p[key] / tot; } }
const dom = sh => Object.entries(sh).filter(([z]) => regions[z]).sort((x, y) => y[1] - x[1])[0]?.[0] ?? '1';
const sa = meth.map(r => ({ sa3: hier[r.sa2_code]?.sa3_code, sa4: hier[r.sa2_code]?.sa4_code, state: +hier[r.sa2_code]?.state, cropping: +r.cropping_km2, pasture: +r.pasture_km2, nonAg: +r.nonAgricultural_km2, infrastr1: +r.infrastructure_km2, nature1: +r.reserve_km2, pop: +erp[r.sa2_code]?.[year] || 0, sh: share[r.sa2_code] ?? { 1: 1 } }));
const zoneOf = (mode, us) => { if (mode === 'national') return '1'; if (mode === 'state') return String(STATE_ZONE[us[0].state] ?? 1); const zs = {}; for (const u of us) for (const [z, v] of Object.entries(u.sh)) zs[z] = (zs[z] ?? 0) + v * (u.cropping > 0 ? u.cropping : 1e-6); return dom(zs); };
const cap = (u, zone, preset) => { const z = regions[zone]; const o = ev.evaluate({ ...R, yield: z.yield }, { ...R.presets[preset], irrigation: z.presets[preset].irrigation, nature2: z.presets[preset].nature2, ...Object.fromEntries(KEYS.map(k => [k, u[k]])), population: Math.max(u.pop, 1) }).capacity; return Number.isFinite(o) ? o : 0; };
const grp = key => { const m = new Map(); for (const u of sa) (m.get(u[key]) ?? m.set(u[key], []).get(u[key])).push(u); return [...m.values()]; };
const agg = us => Object.fromEntries(KEYS.concat('pop').map(k => [k, us.reduce((a, u) => a + u[k], 0)]));
const rows = [];
for (const preset of ['short', 'long']) {
  const nat = cap(agg(sa), '1', preset); const out = { preset, national: nat, stateZones: [2, 15, 26, 40, 49, 56, 60].reduce((a, z) => a + cap({ ...Object.fromEntries(KEYS.map(k => [k, regions[z].land[k]])), pop: regions[z].population }, String(z), preset), 0) };
  for (const mode of ['dominant', 'state', 'national']) for (const lvl of ['state', 'sa4', 'sa3', 'sa2']) { const groups = lvl === 'sa2' ? sa.map(u => [u]) : grp(lvl); out[`${lvl}_${mode}`] = groups.reduce((a, us) => a + cap(agg(us), zoneOf(mode, us), preset), 0); }
  rows.push(out); }
for (const o of rows) { console.log(`\n${id} ${o.preset}: national ${(o.national / 1e6).toFixed(1)} M; states (release zones) ${(o.stateZones / 1e6).toFixed(1)} M`);
  for (const mode of ['dominant', 'state', 'national']) console.log(' yields by', mode.padEnd(9), ['state', 'sa4', 'sa3', 'sa2'].map(l => `${l} ${(o[`${l}_${mode}`] / 1e6).toFixed(1)} (${(o[`${l}_${mode}`] / o.national * 100).toFixed(0)}%)`).join(' | ')); }
