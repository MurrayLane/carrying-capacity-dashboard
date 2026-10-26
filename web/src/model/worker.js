// The model runs in a worker so dragging a slider never stalls the page.
import { Evaluator } from './evaluator.js';
let ev = null, regions = null, latestGen = 0;
const tick = () => new Promise(r => setTimeout(r));
self.onmessage = async e => {
  const m = e.data;
  try {
    if (m.type === 'init') {
      const [model, reg] = await Promise.all(['model.json', 'regions.json'].map(f => fetch(`${m.base}data/${m.release}/${f}`).then(r => { if (!r.ok) throw new Error(`${f}: ${r.status}`); return r.json(); })));
      ev = new Evaluator(model); regions = reg.regions;
      self.postMessage({ type: 'ready' });
    } else if (m.type === 'evaluate') {
      // a batch from an older run is dropped as soon as a newer run arrives; yielding between jobs lets that message in
      latestGen = Math.max(latestGen, m.gen || 0);
      const results = [];
      for (const j of m.jobs) {
        await tick();
        if ((m.gen || 0) < latestGen) { self.postMessage({ type: 'result', id: m.id, stale: true }); return; }
        results.push(ev.evaluate(regions[j.zone], j.inputs));
      }
      self.postMessage({ type: 'result', id: m.id, results });
    }
  } catch (err) { self.postMessage({ type: 'error', id: m.id, message: String(err && err.message || err) }); }
};
