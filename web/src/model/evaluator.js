// Evaluates the carrying-capacity workbook for one region and one set of inputs.
// Runs unchanged in the browser (inside a worker) and in Node (the acceptance test).
import { HyperFormula } from 'hyperformula';

// Settings!B2:B25, in order. Land areas are km2; the rest are the 17 parameters; population is people.
export const INPUT_ORDER = ['regionId', 'cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1', 'resilience', 'food', 'meategg', 'redmeat',
  'activity', 'recycling', 'losses', 'organic', 'irrigation', 'fuel', 'biofuel', 'fibre', 'fibreNat', 'fibreWool', 'timber', 'infrastr2', 'nature2', 'population'];

function denseSheets(model) {
  const out = {};
  for (const [name, s] of Object.entries(model.sheets)) {
    const rows = Array.from({ length: s.rows }, () => new Array(s.cols).fill(null));
    for (const [k, v] of Object.entries(s.cells)) { const [r, c] = k.split(':'); rows[+r][+c] = v; }
    out[name] = rows;
  }
  return out;
}

export class Evaluator {
  constructor(model) {
    this.model = model;
    this.hf = HyperFormula.buildFromSheets(denseSheets(model), { licenseKey: 'gpl-v3' });
    this.sid = this.hf.getSheetId('Settings'); this.yid = this.hf.getSheetId('Yield'); this.bid = this.hf.getSheetId('Base');
    this.lastRegion = null;
  }
  num(sheet, row, col) { const v = this.hf.getCellValue({ sheet, row, col }); return typeof v === 'number' ? v : (v === null ? 0 : NaN); }
  s(row, col) { return this.num(this.sid, row, col); }

  /**
   * @param region  a record from regions.json (supplies the yield vector and climate zone)
   * @param inputs  { cropping, pasture, nonAg, infrastr1, nature1, resilience ... nature2, population }
   */
  evaluate(region, inputs) {
    const { hf, sid, yid } = this;
    hf.batch(() => {
      if (this.lastRegion !== region) {
        this.model.meta.yieldRows.forEach((row, i) => hf.setCellContents({ sheet: yid, row: row - 1, col: 5 }, [[region.yield[i]]]));
        this.lastRegion = region;
      }
      INPUT_ORDER.forEach((k, i) => hf.setCellContents({ sheet: sid, row: i + 1, col: 1 }, [[k === 'regionId' ? region.climateZone : inputs[k]]]));
    });
    const s = (r, c) => this.s(r, c);
    const excess = [], requirements = [];
    for (let r = 83; r < 89; r++) excess.push([s(r, 2), s(r, 3) * 100]);
    for (let r = 90; r < 107; r++) requirements.push([s(r, 1), s(r, 2), s(r, 3) * 100, s(r, 4) * 100]);
    // five land types: cropping, pasture, non-agricultural, infrastructure, nature reserve
    const landTypes = col => [2, 3, 4, 5, 6].map(c => s(col, c));
    const diet = { energy: 0, protein: 0, fat: 0, carbs: 0, sugar: 0, fibre: 0 };
    const dc = { energy: 31, protein: 32, fat: 33, carbs: 34, sugar: 35, fibre: 36 };
    for (const r of this.model.meta.dietRows) for (const k of Object.keys(dc)) { const v = this.num(this.bid, r, dc[k]); if (Number.isFinite(v)) diet[k] += v / 7; }
    return {
      capacity: s(75, 1), totalLand: s(53, 1), excess, requirements,
      existing: landTypes(53), used: [s(62, 2), s(62, 3), s(62, 4), s(62, 5), s(62, 6)],
      diet,                                        // per person per day: kJ and grams
    };
  }
}
