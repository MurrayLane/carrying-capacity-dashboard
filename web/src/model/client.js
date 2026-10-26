export class ModelClient {
  constructor(base, release) {
    this.pending = new Map(); this.seq = 0;
    this.worker = new Worker(new URL('./worker.js', import.meta.url), { type: 'module' });
    this.ready = new Promise((resolve, reject) => {
      this.worker.onmessage = e => {
        const m = e.data;
        if (m.type === 'ready') resolve();
        else if (m.type === 'result') { this.pending.get(m.id)?.resolve(m.stale ? null : m.results); this.pending.delete(m.id); }
        else if (m.type === 'error') { if (m.id == null) reject(new Error(m.message)); else { this.pending.get(m.id)?.reject(new Error(m.message)); this.pending.delete(m.id); } }
      };
      this.worker.onerror = e => reject(new Error(e.message || 'The model could not start'));
      this.worker.postMessage({ type: 'init', base, release });
    });
  }
  /** jobs: [{ zone, inputs }] -> results in the same order, or null if a newer generation superseded the batch */
  async evaluate(jobs, gen = 0) {
    await this.ready; const id = ++this.seq;
    return new Promise((resolve, reject) => { this.pending.set(id, { resolve, reject }); this.worker.postMessage({ type: 'evaluate', id, jobs, gen }); });
  }
}
