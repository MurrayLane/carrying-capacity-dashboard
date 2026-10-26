// Separates the difference between the online model (release 2011) and the thesis-results model (release 2011-thesis) into its causes.
// The two differ in (a) default inputs and (b) the model itself: the timber yield row of the Yield sheet and Base!K348 (the timber usable fraction).
// Every cause is applied alone to the final model, then all together, and the effect on capacity is reported.
// Usage: from web/ after `npm run build:data`:  node ../analysis/model_archive/decompose_versions.mjs
import fs from 'fs'; import path from 'path';
const web = new URL('../../web/', import.meta.url).pathname;
const { Evaluator } = await import(path.join(web, 'src/model/evaluator.js'));
const load = id => { const d = path.join(web, 'public/data', id); return { model: JSON.parse(fs.readFileSync(d + '/model.json')), regions: JSON.parse(fs.readFileSync(d + '/regions.json')) }; };
const A = load('2011'), T = load('2011-thesis');
const K348 = '347:10', timberIdx = A.regions.yieldRows.indexOf(138);
const evalWith = (changes, preset) => {
  const model = JSON.parse(JSON.stringify(A.model)); const regions = JSON.parse(JSON.stringify(A.regions.regions));
  for (const [id, r] of Object.entries(regions)) {
    const t = T.regions.regions[id];
    for (const f of changes.fields ?? []) r.presets[preset][f] = t.presets[preset][f];
    if (changes.timberYield) r.yield[timberIdx] = t.yield[timberIdx];
  }
  if (changes.k348) model.sheets.Base.cells[K348] = T.model.sheets.Base.cells[K348];
  const ev = new Evaluator(model); const out = {};
  for (const [id, r] of Object.entries(regions)) out[id] = ev.evaluate(r, { ...r.land, ...r.presets[preset], population: r.population }).capacity;
  return out;
};
const names = { 1: 'Australia', 2: 'NSW-ACT', 15: 'VIC', 26: 'QLD', 40: 'SA', 49: 'WA', 56: 'TAS', 60: 'NT' };
const diffFields = preset => Object.keys(A.regions.regions[1].presets[preset]).filter(f => Object.values(A.regions.regions).some(r => Math.abs(r.presets[preset][f] - T.regions.regions[r.id].presets[preset][f]) > 1e-9));
for (const preset of ['short', 'long']) {
  const base = evalWith({}, preset), fields = diffFields(preset);
  const steps = [...fields.map(f => [`input ${f}`, { fields: [f] }]), ['model: timber yield per region', { timberYield: true }], ['model: Base!K348 (timber usable fraction)', { k348: true }],
    ['ALL inputs, same final model', { fields }], ['ALL model changes, final inputs', { timberYield: true, k348: true }], ['EVERYTHING (= release 2011-thesis)', { fields, timberYield: true, k348: true }]];
  console.log(`\n=== ${preset}-term: change from release 2011 caused by each difference (percent change in capacity; Australia, then the largest change among the 52 NRM regions)`);
  console.log('cause'.padEnd(44), 'Australia'.padStart(10), 'worst NRM'.padStart(11), ' region');
  for (const [label, ch] of steps) {
    const got = evalWith(ch, preset); let worst = 0, wid = null;
    for (const [id, v] of Object.entries(got)) if (A.regions.regions[id].kind === 'region') { const d = (v / base[id] - 1); if (Math.abs(d) > Math.abs(worst)) { worst = d; wid = id; } }
    console.log(label.padEnd(44), ((got[1] / base[1] - 1) * 100).toFixed(2).padStart(9) + '%', (worst * 100).toFixed(1).padStart(10) + '%', ' ', wid ? A.regions.regions[wid].name : '');
  }
}
