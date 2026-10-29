// Constants audit stage 3 (SCOPE.md E18): the organic yield factor of the ruminant rows (Yield!G95, G96, G98: sheep meat, sheep wool, cattle meat), 0.808 in the workbook, raised to 0.9 and 1.0; long-term capacity of Australia on 2025-improved.
//   node analysis/constants_audit/organic_livestock.mjs      (repository root; needs the built data)
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const d=new URL('../../web/public/data/2025-improved/', import.meta.url).pathname, model=JSON.parse(fs.readFileSync(d+'model.json')), R=JSON.parse(fs.readFileSync(d+'regions.json')).regions[1];
const Y=model.sheets.Yield.cells; const live=[];
for(let r=90;r<=110;r++){const name=Y[`${r}:0`];if(typeof name==='string'&&name.includes('g/m')) live.push([r,name,Y[`${r}:6`]])}
console.log(live.map(x=>`${x[0]+1} ${x[1]} ${x[2]}`).join('\n'));
const cap=m=>{const ev=new Evaluator(m);return ['short','long'].map(k=>ev.evaluate(R,{...R.land,...R.presets[k],population:R.population}).capacity/1e6)};
const base=cap(model);console.log('base',base.map(x=>x.toFixed(2)));
const set=(rows,v)=>{const m=JSON.parse(JSON.stringify(model));for(const r of rows)m.sheets.Yield.cells[`${r}:6`]=v;return cap(m)};
const rum=live.filter(x=>/Sheep|Cattle|Goat/i.test(x[1])).map(x=>x[0]);console.log('ruminant rows',rum.map(r=>r+1));
for(const v of [0.9,1.0]){const c=set(rum,v);console.log('ruminant organic factor',v,c.map(x=>x.toFixed(2)),((c[1]/base[1]-1)*100).toFixed(1)+'% long')}
