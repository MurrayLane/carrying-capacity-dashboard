// Worker of decompose_corrected.mjs --order / --average (brief B111): evaluates one model variant on a list of (zone, inputs) jobs and returns the capacities.
// It holds no logic of its own beyond the evaluator call that decompose_corrected.mjs's compose() makes; the main script builds every model and input.
import { parentPort } from 'node:worker_threads';
import { Evaluator } from '../../web/src/model/evaluator.js';

parentPort.on('message', ({ model, jobs, yields }) => {
  const ev = new Evaluator(model), regionOf = new Map(), out = new Float64Array(jobs.length);
  // the evaluator writes a region's yield vector only when the region object changes, so jobs arrive sorted by yield vector and share one object per vector
  jobs.forEach((j, i) => {
    const k = `${j.climateZone}|${j.yieldId}`;
    if (!regionOf.has(k)) regionOf.set(k, { climateZone: j.climateZone, yield: yields[j.yieldId] });
    out[i] = ev.evaluate(regionOf.get(k), j.inputs).capacity;
  });
  parentPort.postMessage(out, [out.buffer]);
});
