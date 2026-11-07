// Paper A sections 7 and 8 and the discussion: the long term by region and what each long-term setting is worth (corrected method, both vintages),
// and ameliorative measures tested one at a time on Australia, 2025 corrected method, short and long term.
//   node analysis/paper_a/long_term_and_measures.mjs OUT_DIR      (repository root; needs the built data)
// Writes OUT_DIR/long_term_levers.csv, long_term_regions.csv, measures.csv, store_equivalence.csv, transfers.csv.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const out = process.argv[2], base = new URL('../../web/public/data/', import.meta.url).pathname;
const load = (id, edit = null) => { const m = JSON.parse(fs.readFileSync(`${base}${id}/model.json`)); if (edit) edit(m); const r = JSON.parse(fs.readFileSync(`${base}${id}/regions.json`)); return { ev: new Evaluator(m), R: r.regions, rows: r.yieldRows }; };
const KEYS = ['resilience', 'food', 'meategg', 'redmeat', 'activity', 'recycling', 'losses', 'organic', 'irrigation', 'fuel', 'biofuel', 'fibre', 'fibreNat', 'fibreWool', 'timber', 'infrastr2', 'nature2'];
// ---- what each long-term setting is worth, Australia and states, both vintages
const lv = ['release,zone,name,lever,alone,without'];
for (const id of ['2011-fixed', '2025-fixed']) {
  const { ev, R } = load(id);
  for (const z of [1, 2, 15, 26, 40, 49, 56, 60]) {
    const r = R[z], S = r.presets.short, L = r.presets.long, run = pre => Math.round(ev.evaluate(r, { ...r.land, ...pre, population: r.population }).capacity);
    lv.push([id, z, JSON.stringify(r.name), 'short settings', run(S), run(S)].join(',')); lv.push([id, z, JSON.stringify(r.name), 'long settings', run(L), run(L)].join(','));
    for (const k of KEYS) { if (S[k] === L[k]) continue; lv.push([id, z, JSON.stringify(r.name), `${k} (${S[k]} to ${L[k]})`, run({ ...S, [k]: L[k] }), run({ ...L, [k]: S[k] })].join(',')); }
  }
}
fs.writeFileSync(`${out}/long_term_levers.csv`, lv.join('\n') + '\n');
// ---- the long term by region, both vintages
const lr = ['release,zone,name,kind,capacity_long,population,ratio'];
for (const id of ['2011-fixed', '2025-fixed']) { const { ev, R } = load(id); for (const [z, r] of Object.entries(R)) { if (!(r.kind === 'region' || z === '60' || z === '1')) continue; const c = ev.evaluate(r, { ...r.land, ...r.presets.long, population: r.population }).capacity; lr.push([id, z, JSON.stringify(r.name), r.kind, Math.round(c), r.population, (c / r.population).toFixed(3)].join(',')); } }
fs.writeFileSync(`${out}/long_term_regions.csv`, lr.join('\n') + '\n');
// ---- ameliorative measures, Australia, 2025 corrected
const { ev, R, rows } = load('2025-fixed'); const N = R[1];
const idx = lo => rows.map((r, i) => (r >= lo[0] && r <= lo[1]) ? i : -1).filter(i => i >= 0);
const FIELD = [...idx([4, 20]), ...idx([94, 94])], HORT = idx([21, 93]), LIVE = [...idx([95, 103]), ...idx([135, 136])], ALL = idx([4, 137]);
const cap = (preset, o = {}, scale = null, land = {}) => { const r = scale ? { ...N, yield: N.yield.map((v, i) => v * (scale[i] ?? 1)) } : N; return ev.evaluate(r, { ...N.land, ...land, ...N.presets[preset], ...o, population: N.population }).capacity / 1e6; };
const sc = (groups, f) => { const a = {}; for (const g of groups) for (const i of g) a[i] = f; return a; };
const rowsM = [['measure', 'what it does in the model', 'short term (million)', 'change', 'long term (million)', 'change']];
const b = { s: cap('short'), l: cap('long') };
const add = (name, what, fs_, fl) => rowsM.push([name, what, fs_.toFixed(1), ((fs_ / b.s - 1) * 100).toFixed(1) + '%', fl.toFixed(1), ((fl / b.l - 1) * 100).toFixed(1) + '%']);
rowsM.push(['reference (2025, corrected)', '', b.s.toFixed(1), '', b.l.toFixed(1), '']);
add('Field-crop yields +10%', 'wheat, barley, other field crops and cotton', cap('short', {}, sc([FIELD], 1.1)), cap('long', {}, sc([FIELD], 1.1)));
add('Field-crop yields +20%', 'as above', cap('short', {}, sc([FIELD], 1.2)), cap('long', {}, sc([FIELD], 1.2)));
add('Horticulture yields +10%', 'vegetables, fruit, nuts', cap('short', {}, sc([HORT], 1.1)), cap('long', {}, sc([HORT], 1.1)));
add('Livestock output +10%', 'meat, wool and milk per hectare (herd productivity, pasture improvement)', cap('short', {}, sc([LIVE], 1.1)), cap('long', {}, sc([LIVE], 1.1)));
add('Livestock output +20%', 'as above', cap('short', {}, sc([LIVE], 1.2)), cap('long', {}, sc([LIVE], 1.2)));
add('All yields +10%', 'every food yield', cap('short', {}, sc([ALL], 1.1)), cap('long', {}, sc([ALL], 1.1)));
// drought-proofing by the factor route: the 100-year allowance factor of every state and of Australia (resilience!2:101 to 9:101) goes from f to 1 - (1 - f) / 2
const DP = load('2025-fixed', m => { for (let r = 2; r <= 9; r++) { const f = m.sheets.resilience.cells[`${r}:101`]; m.sheets.resilience.cells[`${r}:101`] = 1 - (1 - f) / 2; } });
add('Drought-proofing: worst year loses half as much', 'long term at 100 years: the allowance factor f becomes 1 - (1 - f) / 2 (Australia 0.4558 to 0.7279)', b.s, DP.ev.evaluate(DP.R[1], { ...DP.R[1].land, ...DP.R[1].presets.long, population: DP.R[1].population }).capacity / 1e6);
for (const v of [0.02, 0.05]) add(`Irrigated share of cropland ${v} (now ${N.presets.short.irrigation})`, 'more irrigation (water not constrained in the model)', cap('short', { irrigation: v }), cap('long', { irrigation: v }));
add('Waste at the national target (6%)', 'avoidable waste 0.06', cap('short', { losses: 0.06 }), cap('long', { losses: 0.06 }));
add('No avoidable waste', 'avoidable waste 0', cap('short', { losses: 0 }), cap('long', { losses: 0 }));
add('Full recycling of food waste', 'recycling setting 1 (short term) ', cap('short', { recycling: 1 }), cap('long', { recycling: 1 }));
add('Cropland +25% from pasture', 'a quarter more cropping land, the pasture area reduced by the same amount', cap('short', {}, null, { cropping: N.land.cropping * 1.25, pasture: N.land.pasture - N.land.cropping * 0.25 }), cap('long', {}, null, { cropping: N.land.cropping * 1.25, pasture: N.land.pasture - N.land.cropping * 0.25 }));
add('Cropland doubled from non-agricultural land', 'the 1975 CSIRO case', cap('short', {}, null, { cropping: N.land.cropping * 2, nonAg: Math.max(N.land.nonAg - N.land.cropping, 0) }), cap('long', {}, null, { cropping: N.land.cropping * 2, nonAg: Math.max(N.land.nonAg - N.land.cropping, 0) }));
add('Diet: meat and eggs 7.5%', 'meat and egg share of the diet 0.075', cap('short', { meategg: 0.075 }), cap('long', { meategg: 0.075 }));
add('Diet: meat and eggs 5%', 'meat and egg share 0.05', cap('short', { meategg: 0.05 }), cap('long', { meategg: 0.05 }));
add('Diet: red meat 30% of meat', 'red-meat share of meat 0.3 (more poultry and pork)', cap('short', { redmeat: 0.3 }), cap('long', { redmeat: 0.3 }));
add('Liquid fuel 156 litres a person', 'electrified transport', cap('short', { fuel: 156 }), cap('long', { fuel: 156 }));
fs.writeFileSync(`${out}/measures.csv`, rowsM.map(r => r.map(x => /[,]/.test(x) ? JSON.stringify(x) : x).join(',')).join('\n') + '\n');
// ---- how many years of weather a store is worth (improved release, long term)
const I = load('2025-improved'), NI = I.R[1];
const capI = o => I.ev.evaluate(NI, { ...NI.land, ...NI.presets.long, ...o, population: NI.population }).capacity / 1e6;
const eq = ['resilience_years,capacity_long_improved'];
for (const t of [1, 2, 3, 5, 7, 10, 15, 20, 30, 50, 75, 100, 150]) eq.push([t, capI({ resilience: t }).toFixed(2)].join(','));
fs.writeFileSync(`${out}/store_equivalence.csv`, eq.join('\n') + '\n');
// ---- the food that would have to move between regions: excess population in over-capacity regions against spare capacity elsewhere (2025 corrected, average year and 1 in 10)
const tr = ['release,return_period,excess_population_million,spare_capacity_million,national_capacity_minus_population,regions_over,regions_under'];
for (const T of [1, 5, 10, 20]) {
  let ex = 0, sp = 0, no = 0, nu = 0;
  for (const [z, r] of Object.entries(R)) { if (!(r.kind === 'region' || z === '60')) continue; const c = ev.evaluate(r, { ...r.land, ...r.presets.short, resilience: T, population: r.population }).capacity; if (c < r.population) { ex += r.population - c; no++; } else { sp += c - r.population; nu++; } }
  const nat = ev.evaluate(N, { ...N.land, ...N.presets.short, resilience: T, population: N.population }).capacity;
  tr.push(['2025-fixed', T, (ex / 1e6).toFixed(1), (sp / 1e6).toFixed(1), ((nat - N.population) / 1e6).toFixed(1), no, nu].join(','));
}
fs.writeFileSync(`${out}/transfers.csv`, tr.join('\n') + '\n');
console.log(rowsM.map(r => r.join(' | ')).join('\n')); console.log(tr.join('\n')); console.log(eq.join('\n'));
