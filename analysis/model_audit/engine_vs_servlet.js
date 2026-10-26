// Replay the 2011 baseline (baseline/baseline_2011.json) through the JavaScript engine and compare with the
// original servlet's output. This is the acceptance test for the static rebuild: it must pass before the Java path is retired.
// Usage: node engine_vs_servlet.js MODEL.xlsx ../../baseline/baseline_2011.json
const { load } = require('./engine'); const fs = require('fs');
const m = load(process.argv[2]); const base = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
const PCT = new Set(['inputFoodRatio','inputMeateggRatio','inputRedmeatRatio','inputRecyclingRatio','inputLossesRatio','inputOrganicRatio','inputIrrigationRatio','inputBiofuelRatio','inputFibreNaturalRatio','inputFibreWoolRatio','inputNatureRatio']);
const FIELD = { inputRegionId: 'regionId', inputAreasCropping: 'cropping', inputAreasPasture: 'pasture', inputAreasNonAg: 'nonAg', inputAreasBuilt: 'infrastr1', inputAreasNature: 'nature1',
  inputResilienceYears: 'resilience', inputFoodRatio: 'food', inputMeateggRatio: 'meategg', inputRedmeatRatio: 'redmeat', inputActivityLevel: 'activity', inputRecyclingRatio: 'recycling',
  inputLossesRatio: 'losses', inputOrganicRatio: 'organic', inputIrrigationRatio: 'irrigation', inputFuelTotal: 'fuel', inputBiofuelRatio: 'biofuel', inputFibreTotal: 'fibre',
  inputFibreNaturalRatio: 'fibreNat', inputFibreWoolRatio: 'fibreWool', inputTimber: 'timber', inputInfrastructure: 'infrastr2', inputNatureRatio: 'nature2', inputPopulation: 'population' };
let bad = 0, worstRel = 0, n = 0;
for (const [key, c] of Object.entries(base.cases)) {
  const d = {}; for (const [f, k] of Object.entries(FIELD)) { let v = parseFloat(String(c.params[f]).replace(/[^\d.\-]/g, '')); if (PCT.has(f)) v /= 100; d[k] = v; }
  m.set(d); n++;
  const got = [m.capacity()]; for (let r = 83; r < 89; r++) got.push(m.num(r, 2), m.num(r, 3) * 100);
  for (let r = 90; r < 107; r++) got.push(m.num(r, 1), m.num(r, 2), m.num(r, 3) * 100, m.num(r, 4) * 100);
  const e = c.result, exp = [e.popcc]; e.excess.forEach(x => exp.push(x[0], x[1])); e.requirements.forEach(x => exp.push(...x));
  exp.forEach((v, i) => { const tol = Math.max(0.015, Math.abs(v) * 1e-9); const diff = Math.abs(v - got[i]); worstRel = Math.max(worstRel, diff / Math.max(1, Math.abs(v))); if (!(diff <= tol)) { bad++; if (bad <= 5) console.log('MISMATCH', key, i, v, got[i]); } });
}
console.log(`${n} cases, ${bad} values beyond the servlet's two-decimal rounding, worst relative difference ${worstRel.toExponential(1)}`);
process.exit(bad ? 1 : 0);
