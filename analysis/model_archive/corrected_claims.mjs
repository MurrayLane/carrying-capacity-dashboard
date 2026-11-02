// What each published paper's numbers become with the two corrections (biodiesel yield, beef carcase yield), against the release that produced them (ERRATA.md).
//   node analysis/model_archive/corrected_claims.mjs      (repository root; needs the built data: cd web && npm run build:data)
// Releases: `2011-thesis` produced thesis Table 16 and the 2015 and 2017 Table 2; `2011` is the final online model (2014 paper, 2013 UES text). "corrected" applies the cell overrides of
// methods/biodiesel-yield and methods/beef-carcase-yield to that release's workbook, exactly as build-data.mjs does for `2011-fixed`.
import fs from 'node:fs'; import path from 'node:path';
const web = new URL('../../web/', import.meta.url).pathname, root = new URL('../../', import.meta.url).pathname;
const { Evaluator } = await import(path.join(web, 'src/model/evaluator.js'));
const XLSX = (await import(path.join(web, 'node_modules/xlsx/xlsx.mjs'))).default ?? (await import(path.join(web, 'node_modules/xlsx/xlsx.mjs')));
const base = path.join(web, 'public/data') + '/', MODS = ['biodiesel-yield', 'beef-carcase-yield'];
const load = (id, fix) => {
  const model = JSON.parse(fs.readFileSync(base + id + '/model.json')), { regions } = JSON.parse(fs.readFileSync(base + id + '/regions.json'));
  if (fix) for (const m of MODS) for (const [sheet, cells] of Object.entries(JSON.parse(fs.readFileSync(path.join(root, 'methods', m, 'method.json'))).cellOverrides)) for (const [addr, v] of Object.entries(cells)) { const { r, c } = XLSX.utils.decode_cell(addr); model.sheets[sheet].cells[`${r}:${c}`] = v; }
  return { ev: new Evaluator(model), regions };
};
const R = { 'thesis': load('2011-thesis', false), 'thesis+fix': load('2011-thesis', true), 'final': load('2011', false), 'final+fix': load('2011', true) };
const run = (k, zone, preset, over = {}) => { const r = R[k].regions[zone]; return R[k].ev.evaluate(r, { ...r.land, ...r.presets[preset], population: r.population, ...over }); };
const M = x => Math.round(x / 1e5) / 10, P = x => Math.round(x).toLocaleString();
const names = { 1: 'Australia', 2: 'NSW-ACT', 15: 'Victoria', 26: 'Queensland', 40: 'SA', 49: 'WA', 56: 'Tasmania', 60: 'NT' };
const regionIds = k => Object.values(R[k].regions).filter(r => r.kind === 'region' && r.id !== 60).map(r => r.id).concat([60]);
console.log('=== Thesis Table 16, Lane, Dawes and Grace 2015 Table 2, Lane 2017 Table 2 (release 2011-thesis): national and state capacity, as published and corrected');
for (const preset of ['short', 'long']) { console.log(preset); for (const z of Object.keys(names)) { const a = run('thesis', +z, preset).capacity, b = run('thesis+fix', +z, preset).capacity; console.log('  ', names[z].padEnd(10), P(a).padStart(11), P(b).padStart(11), ((b / a - 1) * 100).toFixed(1).padStart(7) + '%'); } }
console.log('\n=== Sums (million): states, regions; scale ratio national / regions (short term); regions under capacity (count of', regionIds('thesis').length, 'regions)');
for (const k of ['thesis', 'thesis+fix']) for (const preset of ['short', 'long']) {
  const cap = z => run(k, z, preset).capacity, states = [2, 15, 26, 40, 49, 56, 60].reduce((a, z) => a + cap(z), 0), regs = regionIds(k).reduce((a, z) => a + cap(z), 0), under = regionIds(k).filter(z => R[k].regions[z].population <= cap(z)).length;
  const exNat = run(k, 1, preset).excess[5][0], exReg = regionIds(k).reduce((a, z) => a + run(k, z, preset).excess[5][0], 0);
  console.log(k.padEnd(11), preset.padEnd(6), 'national', M(cap(1)), 'states', M(states), 'regions', M(regs), 'ratio', (cap(1) / regs).toFixed(2), '| under capacity:', under, '| excess land national', M(exNat), 'regional', M(exReg), 'million km2');
}
console.log('\n=== Lane 2017 Figure 4 text: long term, Australia, cropping share raised by taking pasture (4,5,6,7,8,10%); with meat-eggs 3.5% at 10% (paper: "23 million")');
for (const k of ['thesis', 'thesis+fix']) { const r = R[k].regions[1], tot = Object.values(r.land).reduce((a, b) => a + b, 0);
  const at = (pct, meat) => { const crop = pct / 100 * tot, pasture = Math.max(0, r.land.pasture - (crop - r.land.cropping)), nonAg = r.land.nonAg - Math.min(0, r.land.pasture - (crop - r.land.cropping)); return M(run(k, 1, 'long', { cropping: crop, pasture, nonAg, ...(meat != null ? { meategg: meat } : {}) }).capacity); };
  console.log(k.padEnd(11), [4, 5, 6, 7, 8, 10].map(p => at(p)).join(', '), '| meat 3.5% at 10% =', at(10, 0.035)); }
console.log('\n=== Lane, Dawes and Grace 2014 (release 2011): Australia short term, land shares (percent of all land); paper: food 48.9, biofuel 0.2, textiles 2.2, timber 1, infrastructure 0.4');
for (const k of ['final', 'final+fix']) { const o = run(k, 1, 'short'), pct = i => o.requirements[i][2].toFixed(2); console.log(k.padEnd(10), 'capacity', P(o.capacity), '| food', pct(10), 'biofuel', pct(11), 'textiles', pct(12), 'timber', pct(13), 'infrastructure', pct(14)); }
console.log('\n=== Lane and Dawes 2013 UES (release 2011): short term default; meat-eggs 15% (paper "just over 39 million"); vegan (0%) ("80 million"); red-meat sweep peak ("40%"); regions sum ("about 23 million"); long term national ("more than nine million") and regional sum ("less than four million")');
for (const k of ['final', 'final+fix']) { const c = o => M(run(k, 1, 'short', o).capacity); let best = 0, bv = 0; for (let p = 0; p <= 100; p += 5) { const v = run(k, 1, 'short', { redmeat: p / 100 }).capacity; if (v > bv) { bv = v; best = p; } }
  const regs = preset => regionIds(k).reduce((a, z) => a + run(k, z, preset).capacity, 0);
  console.log(k.padEnd(10), 'default', c({}), '| meat 15%', c({ meategg: 0.15 }), '| vegan', c({ meategg: 0 }), '| red-meat peak at', best + '% (' + M(bv) + ')', '| regions short', M(regs('short')), '| long national', M(run(k, 1, 'long').capacity), 'regions', M(regs('long'))); }

console.log('\n=== Lane 2017 Table 2 (release 2011-thesis): existing population as a proportion of capacity, published and corrected (paper: short 55, 74, 91, 63, 63, 51, 213, 690%; long 237, 463, 1004, 757, 158, 90, 1942, 6172%)');
for (const preset of ['short', 'long']) for (const k of ['thesis', 'thesis+fix']) console.log(preset.padEnd(6), k.padEnd(11), Object.keys(names).map(z => Math.round(R[k].regions[z].population / run(k, +z, preset).capacity * 100) + '%').join(', '));
console.log('\n=== UES 2013 (release 2011): other quantities; paper: eliminating food waste adds "about ten million"; long term with biofuel set to zero "about 18 million"; fuel 253 L (long-term default)');
for (const k of ['final', 'final+fix']) { const c = (preset, o) => M(run(k, 1, preset, o).capacity), r0 = R[k].regions[1].presets;
  console.log(k.padEnd(10), 'short default', c('short', {}), '| no waste', c('short', { losses: 0 }), '(+' + (c('short', { losses: 0 }) - c('short', {})).toFixed(1) + ')', '| long default', c('long', {}), '| long biofuel 0', c('long', { biofuel: 0 }), '| long fuel setting', r0.long.fuel); }
