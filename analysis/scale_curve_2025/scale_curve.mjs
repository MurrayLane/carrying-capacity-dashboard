// Prototype of the scale curve (candidate for the results paper): capacity summed over units of shrinking size, with every unit evaluated on the SAME yields and settings (the national vector),
// so that only the land mix and the population of the unit differ. Units: Australia, states, SA4, SA3, SA2 (land by the 2011 method on 2020-21 data and 2025 population from data/sa2/land_2011_method_by_sa2.csv).
//   node analysis/scale_curve_2025/scale_curve.mjs RELEASE OUT.csv        (from web/ ; needs the built data)
import fs from 'node:fs'; import path from 'node:path';
const web = new URL('../../web/', import.meta.url).pathname, root = new URL('../../', import.meta.url).pathname;
const { Evaluator } = await import(path.join(web, 'src/model/evaluator.js'));
const [rel, out] = process.argv.slice(2);
const base = path.join(web, 'public/data', rel) + '/', model = JSON.parse(fs.readFileSync(base + 'model.json')), R = JSON.parse(fs.readFileSync(base + 'regions.json')).regions[1], ev = new Evaluator(model);
const csv = f => { const [h, ...rows] = fs.readFileSync(path.join(root, f), 'utf8').trim().split('\n').map(l => l.replace(/\r$/, '').split(',')); return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]]))); };
const meth = csv('data/sa2/land_2011_method_by_sa2.csv'), hier = Object.fromEntries(csv('data/sa2/land_types_by_sa2.csv').map(r => [r.sa2_code, r]));    // the 2011 land method (as the 2025 zones use) with its population; the SA3, SA4 and state codes
const units = meth.map(r => ({ sa2: r.sa2_code, sa3: hier[r.sa2_code]?.sa3_code, sa4: hier[r.sa2_code]?.sa4_code, state: hier[r.sa2_code]?.state, cropping: +r.cropping_km2, pasture: +r.pasture_km2, nonAg: +r.nonAgricultural_km2, infrastr1: +r.infrastructure_km2, nature1: +r.reserve_km2, pop: +r.population || 0 }));
const sum = (arr, k) => arr.reduce((a, u) => a + u[k], 0);
console.log('SA2s', units.length, '| land totals km2 (SA2 sum vs national):', ['cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1'].map(k => k + ' ' + Math.round(sum(units, k)) + ' / ' + Math.round(R.land[k])).join(', '), '| population', Math.round(sum(units, 'pop')), '/', Math.round(R.population));
const cap = (u, preset) => { const o = ev.evaluate(R, { ...R.presets[preset], cropping: u.cropping, pasture: u.pasture, nonAg: u.nonAg, infrastr1: u.infrastr1, nature1: u.nature1, population: Math.max(u.pop, 1) }).capacity; return Number.isFinite(o) ? o : 0; };
const group = (key) => { const m = new Map(); for (const u of units) { const g = key ? u[key] : 'all'; if (!m.has(g)) m.set(g, { cropping: 0, pasture: 0, nonAg: 0, infrastr1: 0, nature1: 0, pop: 0 }); const a = m.get(g); for (const k of Object.keys(a)) a[k] += u[k]; } return [...m.values()]; };
const rows = [['release', 'preset', 'level', 'units', 'sum_capacity', 'population', 'sum_capacity_over_national', 'units_over_capacity']];
for (const preset of ['short', 'long']) { let nat; for (const [level, key] of [['Australia', null], ['State', 'state'], ['SA4', 'sa4'], ['SA3', 'sa3'], ['SA2', 'sa2']]) {
  const g = key === 'sa2' ? units : group(key); const caps = g.map(u => cap(u, preset)), total = caps.reduce((a, b) => a + b, 0); if (level === 'Australia') nat = total;
  const over = g.filter((u, i) => u.pop > caps[i]).length;
  rows.push([rel, preset, level, g.length, Math.round(total), Math.round(sum(g, 'pop')), (total / nat).toFixed(3), over]); console.log(preset, level.padEnd(9), String(g.length).padStart(5), 'units | sum of capacities', (total / 1e6).toFixed(2), 'million |', (total / nat).toFixed(3), 'of national | over capacity:', over); } }
fs.writeFileSync(out, rows.map(r => r.join(',')).join('\n') + '\n');
