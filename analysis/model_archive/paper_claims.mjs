// Tests the numerical claims of each published paper against each release, to find which model version produced them.
// Usage: from web/ after `npm run build:data`:  node ../analysis/model_archive/paper_claims.mjs
import fs from 'fs'; import path from 'path';
const web = new URL('../../web/', import.meta.url).pathname;
const { Evaluator } = await import(path.join(web, 'src/model/evaluator.js'));
const base = path.join(web, 'public/data') + '/';
const labels = ['Red meat','White meat','Dairy','Cereals','Vegetables','Fruit','Legumes','Nuts & seeds','Oils','Sweeteners','Biofuel','Textiles','Timber','Infrastructure','Nature reserve','Total']; 
const rels = {};
for (const id of ['2011', '2011-corrected', '2011-thesis']) { const model = JSON.parse(fs.readFileSync(base + id + '/model.json')), { regions } = JSON.parse(fs.readFileSync(base + id + '/regions.json')); rels[id] = { ev: new Evaluator(model), regions }; }
const run = (id, zone, preset, over = {}) => { const { ev, regions } = rels[id]; const r = regions[zone]; return ev.evaluate(r, { ...r.land, ...r.presets[preset], population: r.population, ...over }); };
console.log('--- Australia short-term: capacity and land shares (percent of all land)');
for (const id of Object.keys(rels)) { const r = run(id, 1, 'short'); const tot = Object.values(rels[id].regions[1].land).reduce((a, b) => a + b, 0);
  console.log(id.padEnd(15), Math.round(r.capacity).toLocaleString(), '| requirements[0..4] sample:', JSON.stringify(r.requirements.slice(0, 2)).slice(0, 90)); }
console.log('requirements rows:', run('2011', 1, 'short').requirements.length, 'cols', run('2011', 1, 'short').requirements[0].length);
const pct = (r, i) => r.requirements[i][2].toFixed(2) + '%';
console.log('\n--- EM2014 (65503): AU short-term land shares; paper: food 48.9%, biofuel 0.2%, textiles 2.2%, timber 1%, infrastructure 0.4%');
for (const id of Object.keys(rels)) { const r = run(id, 1, 'short'); console.log(id.padEnd(15), 'food', pct(r, 10), 'biofuel', pct(r, 11), 'textiles', pct(r, 12), 'timber', pct(r, 13), 'infra', pct(r, 14)); }

console.log('\n--- PopEnv2017 (99790): long-term, regions under capacity (paper: "only 13 regions are under-capacity"); short-term NT and TAS only states over');
for (const id of Object.keys(rels)) {
  const { regions } = rels[id]; const out = {};
  for (const preset of ['short', 'long']) { let nrm = 0, all = 0, nrmN = 0; for (const r of Object.values(regions)) { const c = run(id, r.id, preset).capacity; const under = r.population <= c; all += under; if (r.kind === 'region') { nrm += under; nrmN++; } } out[preset] = { allZonesUnder: all, nrmUnder: nrm, of: nrmN }; }
  console.log(id.padEnd(15), JSON.stringify(out));
}
console.log('\n--- PopEnv2017 Figure 4 text: long-term AU, cropping share raised from 4% by taking pasture; plateau at about 7%; with meat-eggs 3.5% at 10% cropping reaches 23 million');
for (const id of Object.keys(rels)) {
  const r = rels[id].regions[1]; const tot = Object.values(r.land).reduce((a, b) => a + b, 0);
  const at = (pct, meat) => { const crop = pct / 100 * tot; const pasture = Math.max(0, r.land.pasture - (crop - r.land.cropping)); const nonAg = r.land.nonAg - Math.min(0, r.land.pasture - (crop - r.land.cropping)); return Math.round(run(id, 1, 'long', { cropping: crop, pasture, nonAg, ...(meat != null ? { meategg: meat } : {}) }).capacity / 1e5) / 10; };
  console.log(id.padEnd(15), 'capacity (million) at cropping 4,5,6,7,8,10%:', [4, 5, 6, 7, 8, 10].map(p => at(p)).join(', '), '| with meat 3.5%: at 10% =', at(10, 0.035));
}

console.log('\n--- UES2013 (54114): AU short-term: meat-eggs 15% -> "just over 39 million", vegan (0%) -> "80 million"; red-meat sweep peaks at 40%');
for (const id of Object.keys(rels)) {
  const c = (o) => Math.round(run(id, 1, 'short', o).capacity / 1e5) / 10;
  let best = 0, bestV = 0; for (let p = 0; p <= 100; p += 5) { const v = run(id, 1, 'short', { redmeat: p / 100 }).capacity; if (v > bestV) { bestV = v; best = p; } }
  console.log(id.padEnd(15), 'meat 15%:', c({ meategg: 0.15 }), ' vegan:', c({ meategg: 0 }), ' red-meat sweep peak at', best + '%', '(', Math.round(bestV / 1e5) / 10, 'million )');
}
console.log('\n--- PopEnv2015 (75171): "aggregation of states 28 million, by region 23 million"; excess land "national 1.8 million km2, regional aggregation 4.5 million km2"');
for (const id of Object.keys(rels)) {
  const { regions } = rels[id]; const cap = z => run(id, z, 'short').capacity;
  const states = [2, 15, 26, 40, 49, 56, 60].reduce((a, z) => a + cap(z), 0);
  const nrms = Object.values(regions).filter(r => r.kind === 'region' && r.id !== 60).map(r => r.id);
  const byRegion = nrms.reduce((a, z) => a + cap(z), 0) + cap(60);
  const ex = z => run(id, z, 'short').excess; const totalEx = r => r[5][0];
  const exNat = totalEx(ex(1)); const exReg = nrms.reduce((a, z) => a + totalEx(ex(z)), 0) + totalEx(ex(60));
  console.log(id.padEnd(15), 'states', Math.round(states / 1e5) / 10, 'regions', Math.round(byRegion / 1e5) / 10, '| excess national', Math.round(exNat / 1e5) / 10, 'regional', Math.round(exReg / 1e5) / 10, '(million km2)');
}

console.log('\n--- which NRM regions change status (under or over capacity) between release 2011 and 2011-thesis, and the state tables');
for (const preset of ['short', 'long']) {
  const flips = []; for (const r of Object.values(rels['2011'].regions)) { const a = run('2011', r.id, preset).capacity, b = run('2011-thesis', r.id, preset).capacity; if ((r.population <= a) !== (r.population <= b)) flips.push(`${r.name} (pop ${r.population.toLocaleString()}; capacity ${Math.round(a).toLocaleString()} online vs ${Math.round(b).toLocaleString()} thesis)`); }
  console.log(preset, 'flips:', flips.length ? flips.join(' | ') : 'none');
}
const names = { 1: 'AUST', 2: 'NSW-ACT', 15: 'VIC', 26: 'QLD', 40: 'SA', 49: 'WA', 56: 'TAS', 60: 'NT' };
for (const preset of ['short', 'long']) { console.log(preset, 'state capacities, online vs thesis (and existing population as % of capacity under each):');
  for (const z of Object.keys(names)) { const a = run('2011', +z, preset).capacity, b = run('2011-thesis', +z, preset).capacity, p = rels['2011'].regions[z].population;
    console.log('  ', names[z].padEnd(8), Math.round(a).toLocaleString().padStart(11), Math.round(b).toLocaleString().padStart(11), ((a / b - 1) * 100).toFixed(1).padStart(6) + '%', '|', Math.round(p / a * 100) + '% vs ' + Math.round(p / b * 100) + '%'); } }
