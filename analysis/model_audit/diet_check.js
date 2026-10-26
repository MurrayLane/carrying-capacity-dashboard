// Diet chain checks at Australia's short-term defaults.
//  1. Preference weights: within every sub-category the adjusted weights (column U) must sum to 1.
//  2. Diet energy and nutrients against thesis Table 12 (7,362 kJ, protein 34 kg, fat 16 kg, carbohydrate 82 kg, sugar 39 kg, fibre 8 kg per person per year, sedentary).
// Usage: node diet_check.js MODEL.xlsx ../../src/main/webapp/
const { load, parseCsv } = require('./engine');
const m = load(process.argv[2]); const au = parseCsv(process.argv[3] + 'default-inputs-short-term.csv')[0]; m.set(au);
const F = m.sheets['Base']; let V = m.hf.getSheetValues(m.bid); const bad = []; let n = 0;
for (let r = 5; r < 321; r++) { const f = F[r][20]; if (typeof f === 'string' && /^=SUM\(U\d+:U\d+\)$/.test(f)) { n++; const v = V[r][20]; if (!(Math.abs(v - 1) < 1e-6 || v === 0)) bad.push([r + 1, +v.toFixed(4)]); } }
console.log(`preference weights: ${n} sub-categories, ${bad.length} not summing to 1`, bad);
const rows = []; for (let r = 5; r < 349; r++) if (typeof F[r][29] === 'string' && F[r][29].startsWith('=')) rows.push(r);
for (const act of [1, 2, 3]) { m.set({ ...au, activity: act }); V = m.hf.getSheetValues(m.bid);
  const sum = c => rows.reduce((a, r) => a + (typeof V[r][c] === 'number' ? V[r][c] : 0), 0) / 7;
  console.log(`activity ${act}: energy ${sum(31).toFixed(0)} kJ/day, protein ${sum(32).toFixed(0)} g, fat ${sum(33).toFixed(0)} g, carbohydrate ${sum(34).toFixed(0)} g, sugar ${sum(35).toFixed(0)} g, fibre ${sum(36).toFixed(0)} g`); }
console.log('thesis Table 12, activity 1: 7,362 kJ/day, protein 93 g, fat 43 g, carbohydrate 224 g, sugar 107 g, fibre 21 g (from kg per year)');
