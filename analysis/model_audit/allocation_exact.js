// Is the workbook's step-by-step land allocation correct? Solve the same problem exactly and compare, for all 120 default cases.
// Land is treated as nested qualities, as in thesis 8.6.4: cropping can serve every use, pasture all but crops, the rest only forestry,
// infrastructure and reserve. Capacity is the largest population for which three conditions hold:
//   cropping demand <= cropping land;  crop plus pasture demand <= cropping plus pasture land;  all demand plus the fixed reserve <= all land.
// Usage: node allocation_exact.js MODEL.xlsx ../../data/2011/
const { load, parseCsv } = require('./engine');
const m = load(process.argv[2]); const dir = process.argv[3]; const res = [];
for (const [file, label] of [['default-inputs-short-term.csv', 'short'], ['default-inputs-long-term.csv', 'long']]) for (const d of parseCsv(dir + file)) {
  m.set(d);
  const c = m.num(52, 2), p = m.num(52, 3), n = m.num(52, 4), f = m.num(52, 5);             // km2 per person per year by land class
  const C = m.num(53, 2), Pa = m.num(53, 3), T = m.num(53, 1), R = m.num(23, 1) * T;         // existing areas, fixed reserve area
  const cand = { cropping: c > 0 ? C / c : Infinity, croppasture: c + p > 0 ? (C + Pa) / (c + p) : Infinity, allland: c + p + n + f > 0 ? (T - R) / (c + p + n + f) : Infinity };
  const exact = Math.min(...Object.values(cand)); const bind = Object.entries(cand).sort((a, b) => a[1] - b[1])[0][0];
  res.push({ tag: `${label}:${d.regionId}:${d.regionName}`, wb: m.capacity(), exact, bind });
}
const rel = r => (r.wb - r.exact) / r.exact;
console.log('cases:', res.length, '| within 0.01%:', res.filter(r => Math.abs(rel(r)) < 1e-4).length, '| workbook below exact by >0.5%:', res.filter(r => rel(r) < -0.005).length, '| workbook above exact:', res.filter(r => rel(r) > 1e-4).length);
console.log('binding constraint:', res.reduce((a, r) => (a[r.bind] = (a[r.bind] || 0) + 1, a), {}));
