import { defineConfig } from 'vite';

// Relative base so the same build works under github.io/<repo>/ and on a custom domain.
export default defineConfig({
  base: './',
  worker: { format: 'es' },
  build: {
    outDir: 'dist',
    rollupOptions: { input: { main: 'index.html', methods: 'methods.html', changes: 'changes.html', about: 'about.html' } },
  },
});
