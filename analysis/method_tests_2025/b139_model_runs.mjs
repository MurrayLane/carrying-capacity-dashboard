// B139 helper: runs the corrected 2025 model (release 2025-fixed, Australia, short term) through the evaluator, unchanged, and prints JSON on stdout.
// Usage (repository root):
//   node analysis/method_tests_2025/b139_model_runs.mjs cap FOOD:LOSSES [FOOD:LOSSES ...]    capacity (people) at a food amount (Settings!B9; 1 = base) and an avoidable-waste setting (Settings!B14; 0.12 = base)
//   node analysis/method_tests_2025/b139_model_runs.mjs groups LOSSES [LOSSES ...]            the diet by food group at each waste setting: cropland and pasture m2 a person, energy kJ and protein g a day, the non-food needs, the land
//   node analysis/method_tests_2025/b139_model_runs.mjs yields JSON [JSON ...]                capacity with the yield layers scaled: JSON maps "crop" (every plant row and every feed-based animal row, sheet rows 4 to 94, 99 to 133) and single sheet rows
//                                                                                              (95 sheep meat, 96 wool, 97 milk, 98 cattle meat, 135 and 136 goat and sheep milk) to a factor; rows 134, 137 and 138 are never scaled
// Nothing is written to disk. The food-group split is that of analysis/pasture_2025/pairing_relaxed_inputs.mjs (B114), checked here the same way (the groups add up to the diet).
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const id = '2025-fixed', d = new URL(`../../web/public/data/${id}/`, import.meta.url).pathname;
const model = JSON.parse(fs.readFileSync(d + 'model.json')), R = JSON.parse(fs.readFileSync(d + 'regions.json')).regions[1], ev = new Evaluator(model), S = model.sheets.Settings.cells;
const P = R.presets.short, run = (food, losses) => ev.evaluate(R, { ...R.land, ...P, food, losses, population: R.population });
const [mode, ...args] = process.argv.slice(2);
if (mode === 'cap') {
  console.log(JSON.stringify(args.map(a => { const [f, l] = a.split(':').map(Number); return { food: f, losses: l, capacity: run(f, l).capacity }; })));
} else if (mode === 'groups') {
  const expect = { '32:2': 'AC6:Base!AC89', '33:3': 'AC90:Base!AC143', '36:2': 'AC178', '36:3': 'AC175:Base!AC177', '75:1': '=B62' };
  for (const [k, v] of Object.entries(expect)) if (!String(S[k]).includes(v)) throw new Error(`Settings ${k} changed: ${S[k]}`);
  const GROUPS = [['cereals', 33, 'C', [[6, 89]]], ['dairy', 34, 'D', [[90, 143]]], ['fruit', 35, 'C', [[144, 165]]], ['legumes', 36, 'C', [[166, 173], [187, 194], [301, 305]]],
    ['red_meat_pasture_fed', 37, 'D', [[175, 177]]], ['red_meat_crop_fed', 37, 'C', [[178, 178]]], ['white_meat_eggs', 38, 'C', [[180, 186], [320, 320]]],
    ['nuts_seeds', 39, 'C', [[196, 210], [306, 319]]], ['vegetables', 40, 'C', [[211, 264]]], ['oils', 45, 'C', [[266, 282]]], ['sweeteners', 46, 'C', [[283, 296]]]];
  const COL = { C: 2, D: 3 }, s = (r1, c) => ev.s(r1 - 1, c), groupOf = r1 => GROUPS.find(g => g[3].some(([a, b]) => r1 >= a && r1 <= b));
  const out = args.map(Number).map(losses => {
    const base = run(1, losses), E = {}, Q = {};
    for (const r of model.meta.dietRows) { const g = groupOf(r + 1); if (!g) continue; const e = ev.num(ev.bid, r, 31), q = ev.num(ev.bid, r, 32);
      E[g[0]] = (E[g[0]] ?? 0) + (Number.isFinite(e) ? e / 7 : 0); Q[g[0]] = (Q[g[0]] ?? 0) + (Number.isFinite(q) ? q / 7 : 0); }
    const sumE = Object.values(E).reduce((a, b) => a + b, 0), sumQ = Object.values(Q).reduce((a, b) => a + b, 0);
    if (Math.abs(sumE - base.diet.energy) > 1e-6 * base.diet.energy || Math.abs(sumQ - base.diet.protein) > 1e-6 * base.diet.protein) throw new Error('group nutrients do not add to the diet');
    const groups = GROUPS.map(([name, row, c]) => { const land = s(row, COL[c]); return { name, cropland_m2: c === 'C' ? land : 0, pasture_m2: c === 'D' ? land : 0, energy_kj: E[name], protein_g: Q[name] }; });
    const nonfood = { cropland_m2: s(47, 2) + s(48, 2), pasture_m2: s(48, 3), other_m2: s(49, 4) + s(50, 5) };
    const Lnd = R.land, total = Lnd.cropping + Lnd.pasture + Lnd.nonAg + Lnd.infrastr1 + Lnd.nature1;
    return { losses, capacity: base.capacity, diet_energy_kj: base.diet.energy, diet_protein_g: base.diet.protein, groups, nonfood,
             land_km2: { cropland: Lnd.cropping, pasture: Lnd.pasture, other: total * (1 - P.nature2) - Lnd.cropping - Lnd.pasture } };
  });
  console.log(JSON.stringify(out));
} else if (mode === 'yields') {
  const rows = JSON.parse(fs.readFileSync(d + 'regions.json')).yieldRows, PASTURE = new Set([95, 96, 97, 98, 135, 136]), NEVER = new Set([134, 137, 138]);
  console.log(JSON.stringify(args.map(a => { const f = JSON.parse(a);
    const y = R.yield.map((v, i) => { const r = rows[i]; if (NEVER.has(r)) return v; if (PASTURE.has(r)) return v * (f[String(r)] ?? 1); return v * (f.crop ?? 1); });
    return { factors: f, capacity: ev.evaluate({ ...R, yield: y }, { ...R.land, ...P, population: R.population }).capacity }; })));
} else { console.error('usage: cap FOOD:LOSSES ... | groups LOSSES ... | yields JSON ...'); process.exit(2); }
