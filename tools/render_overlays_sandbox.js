// Rasteriza un HTML de rótulos a PNG con alpha usando el Chromium de Playwright del sandbox.
// Uso: NODE_PATH=$(npm root -g) node render_overlays_sandbox.js ov.html N salida.png
const { chromium } = require('playwright');
(async () => {
  const [html, n, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 * Number(n) } });
  await p.goto('file://' + require('path').resolve(html));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(1500);
  const fams = await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family));
  console.log('fuentes cargadas:', [...new Set(fams)].join(','));
  await p.screenshot({ path: out, omitBackground: true, fullPage: true });
  await b.close();
})();
