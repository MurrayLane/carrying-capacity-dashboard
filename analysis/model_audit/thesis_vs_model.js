// Thesis Table 16 (population carrying capacities) against the shipped model, both as large-scale zones and as the sum of regions,
// run from (A) the workbook's own default blocks and (B) the default CSV files the website served.
// Usage: node thesis_vs_model.js MODEL.xlsx ../../data/2011/
const { load, parseCsv } = require('./engine'); const XLSX = require('xlsx');
const m = load(process.argv[2]); const dir = process.argv[3];
const st = XLSX.readFile(process.argv[2]).Sheets['Settings']; const at = (r1, c) => { const x = st[XLSX.utils.encode_cell({ r: r1 - 1, c })]; return x ? x.v : undefined; };
const rg = XLSX.utils.decode_range(st['!ref']);
const groups = { 2: [3,4,5,6,7,8,9,10,11,12,13,14], 15: [16,17,18,19,20,21,22,23,24,25], 26: [27,28,29,30,31,32,33,34,35,36,37,38,39], 40: [41,42,43,44,45,46,47,48], 49: [50,51,52,53,54,55], 56: [57,58,59], 60: [] };
const names = { 1: 'Australia', 2: 'NSW-ACT', 15: 'VIC', 26: 'QLD', 40: 'SA', 49: 'WA', 56: 'TAS', 60: 'NT' };
const T = { short: { large: { 1: 40439187, 2: 10033151, 15: 5975944, 26: 6178020, 40: 2069865, 49: 3696938, 56: 222986, 60: 33274 }, agg: { 2: 8513897, 15: 3426773, 26: 4712882, 40: 1842100, 49: 4168458, 56: 248409, 60: 33274, 1: 22945793 } },
            long:  { large: { 1: 9431487, 2: 1609575, 15: 539589, 26: 516284, 40: 830042, 49: 2105909, 56: 24414, 60: 3722 }, agg: { 2: 1030841, 15: 271527, 26: 569450, 40: 352488, 49: 1523837, 56: 41554, 60: 3722, 1: 3793418 } } };
const runBlock = first => { const out = {}; for (let c = 1; c <= rg.e.c; c++) { const id = at(first, c); if (typeof id !== 'number' || id < 1) continue; const d = {}; require('./engine').ORDER.forEach((k, i) => d[k] = at(first + i, c)); m.set(d); out[id] = m.capacity(); } return out; };
const runCsv = file => { const out = {}; for (const d of parseCsv(dir + file)) { m.set(d); out[d.regionId] = m.capacity(); } return out; };
for (const [lab, first, file] of [['short', 110, 'default-inputs-short-term.csv'], ['long', 138, 'default-inputs-long-term.csv']]) {
  const A = runBlock(first), B = runCsv(file); console.log(`\n${lab}-term   zone      thesis  (A) workbook block  diff%   (B) site CSV  diff%`);
  let sa = 0, sb = 0;
  for (const s of [2, 15, 26, 40, 49, 56, 60]) { const t = T[lab].large[s];
    console.log(`  large  ${names[s].padEnd(8)} ${String(t).padStart(9)} ${A[s].toFixed(0).padStart(12)} ${((A[s] - t) / t * 100).toFixed(2).padStart(8)} ${B[s].toFixed(0).padStart(12)} ${((B[s] - t) / t * 100).toFixed(2).padStart(8)}`);
    const ra = s === 60 ? A[s] : groups[s].reduce((x, i) => x + A[i], 0), rb = s === 60 ? B[s] : groups[s].reduce((x, i) => x + B[i], 0); sa += ra; sb += rb; const ta = T[lab].agg[s];
    console.log(`  regions ${names[s].padEnd(7)} ${String(ta).padStart(9)} ${ra.toFixed(0).padStart(12)} ${((ra - ta) / ta * 100).toFixed(2).padStart(8)} ${rb.toFixed(0).padStart(12)} ${((rb - ta) / ta * 100).toFixed(2).padStart(8)}`); }
  const t = T[lab].agg[1]; console.log(`  regions AUST    ${String(t).padStart(9)} ${sa.toFixed(0).padStart(12)} ${((sa - t) / t * 100).toFixed(2).padStart(8)} ${sb.toFixed(0).padStart(12)} ${((sb - t) / t * 100).toFixed(2).padStart(8)}`); }
