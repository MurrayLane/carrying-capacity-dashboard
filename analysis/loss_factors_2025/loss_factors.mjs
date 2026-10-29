// Australian loss factors (SCOPE.md E4): the thesis's consumer (Base!G), retail (Base!I) and primary-to-retail (Base!L) losses are US figures (Muth 2011, Buzby 2010).
//   node analysis/loss_factors_2025/loss_factors.mjs compare OUT.csv   per diet category: the model's losses against FIAL 2021 (Australia, 2018-19) and FAO Region 2 (Gustavsson 2011), with the stage totals
//   node analysis/loss_factors_2025/loss_factors.mjs module            writes methods/loss-factors-australia/method.json (retail loss rescaled by category to FIAL's retail waste; consumer loss rescaled in total to FIAL's consumption stages)
//   node analysis/loss_factors_2025/loss_factors.mjs effect OUT.csv    capacity of Australia, short and long term, for the variants below   (repository root; needs: cd web && node scripts/build-data.mjs)
// Data: fial_table5_2018_19.csv (FIAL Table 5, tonnes of waste by stage), fbs_au_food_2018_19.csv (FAO food balance, "Food", thousand tonnes, mean 2018 and 2019), fao_region2_loss.csv (Gustavsson et al. 2011, Annex 4).
// Weights: the diet of Australia at the short-term defaults of release 2025-fixed. The diet does not depend on the data vintage, so the module is data-free.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const ROOT = new URL('../../', import.meta.url).pathname, HERE = ROOT + 'analysis/loss_factors_2025/', [mode, outFile] = process.argv.slice(2);
const csv = f => fs.readFileSync(HERE + f, 'utf8').trim().split('\n').slice(1).map(l => l.match(/("[^"]*"|[^,]*)(,|$)/g).map(x => x.replace(/,$/, '').replace(/^"|"$/g, '')));
const FIAL = Object.fromEntries(csv('fial_table5_2018_19.csv').map(r => [r[0], { primary: +r[1], processing: +r[2], distribution: +r[3], retail: +r[4], consumer: +r[5] + +r[6] + +r[7], consumerHH: +r[5] }]));
const FBS = Object.fromEntries(csv('fbs_au_food_2018_19.csv').map(r => [r[0], +r[3] * 1000]));       // tonnes
const FAO = Object.fromEntries(csv('fao_region2_loss.csv').map(r => [r[0], { post: +r[2], retail: +r[4], consumer: +r[5] }]));
const VEG = ['Vegetables - fresh, root', 'Vegetables - fresh, other non-root', 'Vegetables - fresh, brassicas', 'Vegetables - processed'], VEGB = ['Vegetables', 'Starchy Roots'];
// diet category -> FIAL groups, FBS items (the supply they are measured against), FAO Region 2 group. Categories with no FIAL group (legumes, fats and oils, other, lacto-ovo) are left as they are.
const MAP = {
  'Cereal whole': [['Bread', 'Cereal products'], ['Cereals - Excluding Beer'], 'Cereals'], 'Cereal ref': [['Bread', 'Cereal products'], ['Cereals - Excluding Beer'], 'Cereals'],
  'Dairy High': [['Cheese', 'Milk'], ['Milk - Excluding Butter'], 'Milk'], 'Dairy Med': [['Cheese', 'Milk'], ['Milk - Excluding Butter'], 'Milk'], 'Dairy Low': [['Cheese', 'Milk'], ['Milk - Excluding Butter'], 'Milk'],
  'Fruit': [['Fruit'], ['Fruits - Excluding Wine'], 'Fruits and vegetables'], 'Meat red': [['Red meat'], ['Bovine Meat', 'Mutton & Goat Meat', 'Pigmeat', 'Offals'], 'Meat'],
  'Meat white': [['Poultry', 'Eggs', 'Seafood'], ['Poultry Meat', 'Eggs', 'Fish, Seafood'], 'Meat'], 'Nut & seed': [['Nuts'], ['Treenuts'], 'Oilseeds and pulses'], 'Legume': [[], ['Pulses'], 'Oilseeds and pulses'],
  'Vege green': [VEG, VEGB, 'Fruits and vegetables'], 'Vege orange': [VEG, VEGB, 'Fruits and vegetables'], 'Vege other': [VEG, VEGB, 'Fruits and vegetables'], 'Vege starch': [VEG, VEGB, 'Roots and tubers'],
};
const sum = (g, k) => g.reduce((s, x) => s + FIAL[x][k], 0), supply = items => items.reduce((s, x) => s + FBS[x], 0);

const rel = '2025-fixed', dir = ROOT + `web/public/data/${rel}/`;
const model = JSON.parse(fs.readFileSync(dir + 'model.json')), R = JSON.parse(fs.readFileSync(dir + 'regions.json')).regions[1];
const inputs = { ...R.land, ...R.presets.short, population: R.population };
const cap = (m, preset = 'short') => { const ev = new Evaluator(m); const p = R.presets[preset]; return ev.evaluate(R, { ...R.land, ...p, population: R.population }).capacity; };
// the diet at the short-term defaults: per Base row the purchased mass B = eaten / (E F H), and the loss factors
const ev0 = new Evaluator(model); ev0.evaluate(R, inputs);
const B0 = model.sheets.Base.cells, nv = (r, c) => ev0.num(ev0.bid, r - 1, c);
const rows = [];
for (let r = 6; r <= 346; r++) {
  const cat = B0[`${r - 1}:0`]; if (typeof cat !== 'string' || cat === 'TOTAL' || B0[`${r - 1}:3`] === undefined) continue;
  const Y = nv(r, 24), N = nv(r, 13); if (!(Y > 0) || !(N > 0)) continue;
  rows.push({ r, cat, G: B0[`${r - 1}:6`], I: B0[`${r - 1}:8`], L: B0[`${r - 1}:11`], buy: Y / N / (nv(r, 4) * nv(r, 5) * nv(r, 7)) });
}
const wmean = (cat, k) => { const xs = rows.filter(x => x.cat === cat && typeof x[k] === 'number'); const w = xs.reduce((s, x) => s + x.buy, 0); return w ? xs.reduce((s, x) => s + x.buy * (1 - x[k]), 0) / w : NaN; };   // mean loss, 0..1
const pct = x => (100 * x).toFixed(1);

function retailTargets(source) {                       // share of the purchased mass lost at retail, by category
  const t = {};
  for (const [cat, [fg, fb, fao]] of Object.entries(MAP)) {
    if (source === 'fial' && fg.length) t[cat] = sum(fg, 'retail') / supply(fb);
    if (source === 'fao') t[cat] = FAO[fao].retail / 100;
  }
  return t;
}
// cells of Base!I rescaled so that each category's mean retail loss (weighted by purchased mass) equals the target; each food keeps its share of the category's loss
function retailCells(targets) {
  const cells = {};
  for (const [cat, tg] of Object.entries(targets)) {
    const mean = wmean(cat, 'I'), s = tg / mean;
    for (const x of rows.filter(y => y.cat === cat && typeof y.I === 'number' && y.I < 1)) cells[`I${x.r}`] = +(1 - (1 - x.I) * s).toFixed(5);
  }
  return cells;
}
// FIAL baseline (2018-19, disposal statistics): waste at households 2,463 + hospitality 1,218 + procurement 251 = 3,932 kt, over the food that reaches the consumption stages (16.8 Mt to market less retail 526 and distribution 258 kt)
const FOODROWS = () => rows.filter(x => !['Fibre', 'Biofuel'].includes(x.cat) && typeof x.G === 'number');
const consumerMean = () => { const a = FOODROWS(), w = a.reduce((s, x) => s + x.buy, 0); return a.reduce((s, x) => s + x.buy * (1 - x.G), 0) / w; };
const CONSUMER_TARGET = 3932 / (16800 - 526 - 258);
function consumerCells() { const s = CONSUMER_TARGET / consumerMean(), cells = {}; for (const x of FOODROWS()) if (x.G < 1) cells[`G${x.r}`] = +(1 - (1 - x.G) * s).toFixed(5); return cells; }
// sensitivity only: consumer loss by group = FIAL household waste (Table 5, scaled by 2,463 / 3,172 to the baseline) over the ABS apparent consumption (retail sales, tonnes, 2018-19; abs_apparent_consumption_2018_24.csv),
// then one factor so that the total equals the FIAL baseline target as in the module. Household only: the ABS sales exclude food service, so the denominators are not those of the model's consumer stage.
const ABS = Object.fromEntries(csv('abs_apparent_consumption_2018_24.csv').map(r => [+r[1], +r[3] * 1000]));
const HH = 2463 / 3172, hhw = gs => gs.reduce((s, x) => s + FIAL[x].consumerHH, 0) * HH;
function consumerByGroupCells() {
  const G = { 'Meat red': [['Red meat'], [181, 182, 184, 185, 186, 187, 188]], 'Meat white': [['Poultry'], [183, 189]], 'Dairy High': [['Milk', 'Cheese'], [191, 192, 193, 194, 195, 196, 197, 198]], 'Fruit': [['Fruit'], [16]],
    'Cereal whole': [['Bread', 'Cereal products'], [12]], 'Cereal ref': [['Bread', 'Cereal products'], [12]], 'Nut & seed': [['Nuts'], [222]],
    'Vege green': [VEG, [241, 242, 243, 244, 245, 246, 247, 248]], 'Vege orange': [VEG, [241, 242, 243, 244, 245, 246, 247, 248]], 'Vege other': [VEG, [241, 242, 243, 244, 245, 246, 247, 248]], 'Vege starch': [VEG, [241, 242, 243, 244, 245, 246, 247, 248]] };
  G['Dairy Med'] = G['Dairy Low'] = G['Dairy High'];
  const target = {}; for (const [c, [gs, codes]] of Object.entries(G)) target[c] = hhw(gs) / codes.reduce((s, k) => s + ABS[k], 0);
  const per = {}; for (const x of FOODROWS()) if (x.G < 1) per[x.r] = (1 - x.G) * (target[x.cat] ? target[x.cat] / wmean(x.cat, 'G') : 1);
  const tot = FOODROWS().reduce((a, x) => a + x.buy, 0), mean = FOODROWS().reduce((a, x) => a + x.buy * (per[x.r] ?? 0), 0) / tot, k = CONSUMER_TARGET / mean, cells = {};
  for (const x of FOODROWS()) if (x.G < 1) cells[`G${x.r}`] = +(1 - per[x.r] * k).toFixed(5);
  return cells;
}
const withCells = cells => { const m = JSON.parse(JSON.stringify(model)); for (const [a, v] of Object.entries(cells)) m.sheets.Base.cells[`${+a.slice(1) - 1}:${a[0] === 'G' ? 6 : 8}`] = v; return m; };

if (mode === 'compare') {
  const out = ['category,model_consumer_G,model_retail_I,model_primary_to_retail_L,FIAL_consumer_over_supply,FAO_R2_consumption,FIAL_retail_over_supply,FIAL_distribution_over_supply,FAO_R2_distribution_retail,FIAL_primary_plus_processing_over_supply,FAO_R2_postharvest'.replace(/\n/g, '')];
  for (const [cat, [fg, fb, fao]] of Object.entries(MAP)) {
    const S = supply(fb), f = k => fg.length ? pct(sum(fg, k) / S) : '';
    out.push([`"${cat}"`, pct(wmean(cat, 'G')), pct(wmean(cat, 'I')), pct(wmean(cat, 'L')), f('consumer'), FAO[fao].consumer, f('retail'), f('distribution'), FAO[fao].retail, fg.length ? pct((sum(fg, 'primary') + sum(fg, 'processing')) / S) : '', FAO[fao].post].join(','));
  }
  // stage totals: the model against FIAL's whole chain, as a share of the food reaching that stage
  const tot = (k, sel) => rows.filter(x => !['Fibre', 'Biofuel'].includes(x.cat)).reduce((s, x) => s + x.buy * (sel ? 1 - x[k] : 0), 0);
  const all = rows.filter(x => !['Fibre', 'Biofuel'].includes(x.cat) && typeof x.G === 'number'), W = all.reduce((s, x) => s + x.buy, 0);
  const m = k => all.filter(x => typeof x[k] === 'number').reduce((s, x) => s + x.buy * (1 - x[k]), 0) / W;
  const market = 16.8e6, fc = Object.values(FIAL).reduce((s, g) => s + g.consumer, 0), fr = Object.values(FIAL).reduce((s, g) => s + g.retail, 0), fd = Object.values(FIAL).reduce((s, g) => s + g.distribution, 0);
  out.push('', 'stage,model_mean_loss_pct,FIAL_pct_of_16.8Mt_to_market,note');
  out.push(`consumer (households, hospitality, institutional),${pct(m('G'))},${pct(fc / market)},"Table 5 total; the FIAL baseline (disposal statistics) is 3,932 kt, 23.4%. FIAL waste includes inedible parts; the model applies the loss to the gross purchased mass"`);
  out.push(`retail,${pct(m('I'))},${pct(fr / market)},"Table 5 total 527 kt; the baseline is 526 kt"`); out.push(`distribution / primary to retail,${pct(m('L'))},${pct(fd / market)},"FIAL distribution only; its primary and processing stages are not comparable with the model's L"`);
  fs.writeFileSync(outFile, out.join('\n') + '\n'); console.log(out.join('\n'));
} else if (mode === 'module') {
  const t = retailTargets('fial'), cells = { ...consumerCells(), ...retailCells(t) }, tt = Object.entries(t).map(([c, v]) => `${c} ${pct(v)}%`).join(', ');
  const mod = { id: 'loss-factors-australia', label: 'Retail and consumer losses aligned to Australian measurement (FIAL 2021)', line: 'improved',
    description: `The thesis's retail loss (Base!I, Buzby 2010) and consumer loss (Base!G, Muth 2011) are US figures. Retail: replaced, category by category, by the Australian figure: the retail waste measured by the National Food Waste Strategy Feasibility Study (FIAL 2021, 2018-19, Table 5) as a share of the Australian supply of that food group (FAO food balance, mean 2018 and 2019). Each food keeps its share of its category's loss, so the thesis's differences between foods are preserved and only the level changes. Targets for the share of purchased mass lost at retail: ${tt}. Categories with no FIAL group (legumes, fats and oils, other, lacto-ovo) are unchanged. Consumer: FIAL's group tonnages cannot be set against the model's categories with any confidence (the supply bases differ and FIAL's complex products are unassigned), so only the total is aligned: every food's consumer loss is scaled by one factor so that the mean (weighted by purchased mass) equals FIAL's consumption-stage waste, ${pct(CONSUMER_TARGET)}% of the food reaching those stages (3,932 thousand tonnes: households 2,463, hospitality 1,218, procurement 251), against ${pct(consumerMean())}% in the thesis. The primary-to-retail loss (Base!L) is unchanged: FIAL's primary and processing stages are not comparable with it. The avoidable waste setting (Settings!B14) still scales the three losses together, so its default of 12% now means Australian measured waste.`,
    cellOverrides: { Base: cells },
    errata: ['FIAL measures waste that leaves the retail stage (to landfill, compost, feed or rescue). Product marked down and sold, or returned to suppliers, is not waste; the US retail loss the module replaces may include shrink of that kind, which is one reason it is larger.',
      'The FIAL tonnages are product weight and the supply is the FAO food balance (carcase weight for meat, milk equivalent for dairy, grain equivalent for cereals), so the shares are approximate by group; the retail total (526 thousand tonnes of waste in the baseline, 527 in Table 5; 3.1% of the 16.8 million tonnes to market) is the firmer figure.',
      'FIAL\'s hotspot table (Table 5) puts consumption-stage waste at 4,640 thousand tonnes against 3,932 in its baseline (a fraction-of-throughput method against disposal statistics); the module takes the baseline, which the Australian waste target is tracked against. With the Table 5 total the consumer loss would be 29% rather than 24.6%.',
      'The shares of the diet used to rescale each category are those of the short-term default diet of Australia; other zones and settings use the same factors.',
      'FAO Region 2 (Gustavsson 2011) gives larger distribution and retail percentages (fruit and vegetables 12%); it combines distribution with retail and is mostly US and Canadian. It is run as a sensitivity in analysis/loss_factors_2025.'] };
  fs.mkdirSync(ROOT + 'methods/loss-factors-australia', { recursive: true }); fs.writeFileSync(ROOT + 'methods/loss-factors-australia/method.json', JSON.stringify(mod, null, 2) + '\n');
  console.log('wrote methods/loss-factors-australia/method.json;', Object.keys(cells).length, 'cells;', tt);
} else if (mode === 'effect') {
  const variants = [['current (US factors)', {}], ['retail to FIAL only', retailCells(retailTargets('fial'))], ['consumer to FIAL baseline only', consumerCells()], ['retail and consumer to FIAL (the module)', { ...consumerCells(), ...retailCells(retailTargets('fial')) }],
    ['retail to FIAL and consumer by group (household waste over ABS sales, total as the module; sensitivity)', { ...consumerByGroupCells(), ...retailCells(retailTargets('fial')) }],
    ['retail to FAO Region 2 only (sensitivity)', retailCells(retailTargets('fao'))], ['retail to FAO Region 2 and consumer to FIAL (sensitivity)', { ...consumerCells(), ...retailCells(retailTargets('fao')) }]];
  const out = ['variant,short_million,short_change_pct,long_million,long_change_pct'], b = [cap(model, 'short'), cap(model, 'long')];
  for (const [name, cells] of variants) { const m = withCells(cells), c = [cap(m, 'short'), cap(m, 'long')]; out.push([`"${name}"`, (c[0] / 1e6).toFixed(2), ((c[0] / b[0] - 1) * 100).toFixed(1), (c[1] / 1e6).toFixed(2), ((c[1] / b[1] - 1) * 100).toFixed(1)].join(',')); }
  fs.writeFileSync(outFile, out.join('\n') + '\n'); console.log(out.join('\n'));
}
