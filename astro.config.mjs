import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://parlakbeton.com',
  build: {
    inlineStylesheets: 'auto',
  },
  compressHTML: true,
});
