// Behaviour checks: every slider at both limits for ten zones (finite, non-negative, land balances), demand and supply responses,
// and the applied versus stored yield at default irrigation (thesis Table 30 gives the stored yields).
// Usage: node stress_test.js MODEL.xlsx ../../src/main/webapp/
const { load, parseCsv } = require('./engine');
const m = load(process.argv[2]); const byId = Object.fromEntries(parseCsv(process.argv[3] + 'default-inputs-short-term.csv').map(d => [d.regionId, d]));
const sl = { resilience: [1, 150], food: [0, 5], meategg: [0, 0.15], redmeat: [0, 1], activity: [1, 3], recycling: [0, 1], losses: [0, 0.2], organic: [0, 1], irrigation: [0, 1], fuel: [0, 3000], biofuel: [0, 1], fibre: [0, 30], fibreNat: [0, 1], fibreWool: [0, 1], timber: [0, 10], infrastr2: [0, 2000], nature2: [0, 1] };
let tests = 0; const fails = [];
for (const id of [1, 2, 15, 26, 40, 49, 56, 60, 36, 9]) for (const [k, ext] of Object.entries(sl)) for (const v of ext) {
  const d = { ...byId[id], [k]: v }; m.set(d); tests++;
  const pop = m.capacity(), ex = [], req = []; for (let r = 83; r < 89; r++) ex.push(m.num(r, 2)); for (let r = 90; r < 107; r++) req.push(m.num(r, 1));
  const total = d.cropping + d.pasture + d.nonAg + d.infrastr1 + d.nature1, bal = ex[5] + m.num(106, 2) - total;
  if (!isFinite(pop) || pop < 0 || ex.some(e => !isFinite(e) || e < -1) || req.some(x => !isFinite(x) || x < 0) || Math.abs(bal) > 1 + 1e-6 * total) fails.push(`${id}:${k}=${v}`);
}
console.log(`extreme-input test: ${tests} cases, ${fails.length} failures`, fails.slice(0, 5));
const resp = (k, vals) => vals.map(v => { m.set({ ...byId[1], [k]: v }); return (m.capacity() / 1e6).toFixed(2) + 'M'; }).join(' ');
for (const [k, vals] of [['food', [0.5, 1, 2, 3]], ['meategg', [0, 0.05, 0.13, 0.15]], ['redmeat', [0, 0.5, 1]], ['activity', [1, 2, 3]], ['losses', [0, 0.12, 0.2]], ['nature2', [0, 0.24, 0.6]], ['biofuel', [0, 0.5, 1]], ['organic', [0, 0.5, 1]], ['irrigation', [0, 0.5, 1]], ['recycling', [0, 0.5, 1]]])
  console.log(`  ${k.padEnd(10)} ${vals.join(',').padEnd(16)} capacity ${resp(k, vals)}`);
console.log('  (red meat peaks near half then falls: thesis 9.1.4 describes this inflection)');
const names = {}; for (let r = 3; r < 24; r++) { const v = m.sheets['Yield'][r][0]; if (typeof v === 'string') names[v.split(' (')[0]] = r; }
for (const id of [36, 1, 9]) { m.set(byId[id]); const yv = (r, c) => m.val(m.yid, r, c);
  console.log(`region ${id} ${byId[id].regionName}: irrigation ${byId[id].irrigation}; applied/stored yield for wheat = ${(yv(names.Wheat, 1) / yv(names.Wheat, 5)).toFixed(3)} (stored ${yv(names.Wheat, 5).toFixed(0)} g/m2)`); }
