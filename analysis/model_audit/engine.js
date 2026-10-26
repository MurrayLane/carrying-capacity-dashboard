// Shared helper: evaluate the dashboard workbook in JavaScript.
// The workbook (model.xls, converted to .xlsx first) uses IF, SUM, LOOKUP, AVERAGE and AND.
// HyperFormula has no vector LOOKUP, so it is rewritten as INDEX/MATCH.
const XLSX = require('xlsx'); const { HyperFormula } = require('hyperformula'); const fs = require('fs');
// Order of the 24 inputs written to Settings!B2:B25, as in the 2011 servlet
const ORDER = ['regionId','cropping','pasture','nonAg','infrastr1','nature1','resilience','food','meategg','redmeat','activity',
  'recycling','losses','organic','irrigation','fuel','biofuel','fibre','fibreNat','fibreWool','timber','infrastr2','nature2','population'];
function load(modelXlsx) {
  const wb = XLSX.readFile(modelXlsx, { cellFormula: true });
  const horizontal = r => { const m = r.match(/\$?[A-Z]+\$?(\d+):\$?[A-Z]+\$?(\d+)/); return m && m[1] === m[2]; };
  const rewrite = f => f.replace(/LOOKUP\(([^,()]+),([^,()]+),([^,()]+)\)/g, (m, x, k, v) =>
    horizontal(v) ? `INDEX(${v},1,MATCH(${x},${k},1))` : `INDEX(${v},MATCH(${x},${k},1),1)`);
  const sheets = {};
  for (const name of wb.SheetNames) {
    const ws = wb.Sheets[name]; const rg = XLSX.utils.decode_range(ws['!ref']); const rows = [];
    for (let r = 0; r <= rg.e.r; r++) { const row = [];
      for (let c = 0; c <= rg.e.c; c++) { const cell = ws[XLSX.utils.encode_cell({ r, c })];
        row.push(!cell ? null : cell.f ? '=' + rewrite(cell.f) : (cell.t === 'n' || cell.t === 's' || cell.t === 'b') ? cell.v : null); }
      rows.push(row); }
    sheets[name] = rows; }
  const hf = HyperFormula.buildFromSheets(sheets, { licenseKey: 'gpl-v3' });
  const id = n => hf.getSheetId(n); const sid = id('Settings');
  const val = (sheet, r, c) => { const v = hf.getCellValue({ sheet, row: r, col: c }); return typeof v === 'number' ? v : (v === null ? 0 : NaN); };
  return {
    hf, sheets, sid, bid: id('Base'), yid: id('Yield'), val,
    num: (r, c) => val(sid, r, c),                         // Settings cell, 0-based row and column
    set: d => hf.batch(() => ORDER.forEach((k, i) => hf.setCellContents({ sheet: sid, row: i + 1, col: 1 }, [[d[k]]]))),
    capacity: () => val(sid, 75, 1),                       // Settings!B76
  };
}
function parseCsv(path) {
  const L = fs.readFileSync(path, 'utf8').trim().split(/\r?\n/); const h = L[0].split(',');
  return L.slice(1).map(l => { const c = l.split(','); const o = {}; h.forEach((k, i) => o[k] = isNaN(+c[i]) ? c[i] : +c[i]); return o; });
}
module.exports = { load, parseCsv, ORDER };
