#!/usr/bin/env node
'use strict';

/*
 * build.js: Perakit "Ruang Baca Riset" (index.html mandiri)
 * -----------------------------------------------------------
 * Memindai entri/*.md + TEMUAN.md, menyerap metadata, lalu menyuntikkan
 * seluruh konten + parser Markdown (vendor/marked.min.js) + runtime aplikasi
 * ke dalam satu berkas index.html tanpa dependensi eksternal.
 *
 * Pemakaian:
 *   node build.js         → tulis index.html
 *   node build.js --dry   → hanya laporan (tidak menulis berkas)
 *
 * Tanpa `npm install`; hanya modul bawaan `fs` & `path`.
 */

const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const ENTRI_DIR = path.join(ROOT, 'entri');
const TEMUAN_PATH = path.join(ROOT, 'TEMUAN.md');
const MARKED_PATH = path.join(ROOT, 'vendor', 'marked.min.js');
const OUT_PATH = path.join(ROOT, 'index.html');
const DRY = process.argv.includes('--dry');

const MARKED_VERSION = '12.0.0';

/* ------------------------------------------------------------------ *
 * Validasi awal
 * ------------------------------------------------------------------ */
function fail(msg) {
  console.error('\n[build.js] GAGAL: ' + msg + '\n');
  process.exit(1);
}
if (!fs.existsSync(ENTRI_DIR) || !fs.statSync(ENTRI_DIR).isDirectory()) {
  fail('Direktori "entri/" tidak ditemukan di ' + ROOT);
}
if (!fs.existsSync(TEMUAN_PATH)) fail('Berkas "TEMUAN.md" tidak ditemukan.');
if (!fs.existsSync(MARKED_PATH)) {
  fail('Berkas "vendor/marked.min.js" tidak ditemukan.\n' +
       '        Unduh dahulu:\n' +
       '        curl -L -o vendor/marked.min.js https://unpkg.com/marked@' + MARKED_VERSION + '/marked.min.js');
}

/* ------------------------------------------------------------------ *
 * Helper parsing konten
 * ------------------------------------------------------------------ */

// Pisah nama berkas jadi {num, year, title, theme}.
// Catatan: memakai pemisahan pada " - " (spasi-hubung-spasi), BUKAN regex
// [^-]+ untuk tema, sebab 61 entri memiliki tema bertanda hubung
// (RGB-D SOD, Segmentasi RGB-D, YOLO plus RGB-D, Pedestrian RGB-T, RGB-D SLAM).
// Segmen terakhir = tema; segmen 1 = nomor; segmen 2 = tahun; sisanya = judul.
function parseName(base) {
  const stem = base.replace(/\.md$/i, '');
  const parts = stem.split(' - ');
  if (parts.length < 4) return null;
  const num = parts[0];
  const year = parts[1];
  const theme = parts[parts.length - 1];
  const title = parts.slice(2, parts.length - 1).join(' - ');
  if (!/^\d{3}$/.test(num) || !/^\d{4}$/.test(year) || !title || !theme) return null;
  return { num: parseInt(num, 10), id: num, year: parseInt(year, 10), title: title.trim(), theme: theme.trim() };
}

// Ambil kunci BibTeX dari baris tabel "| Kunci BibTeX | `key` |".
function extractBib(md) {
  const m = md.match(/^\|\s*Kunci BibTeX\s*\|\s*`?([^|`]+?)`?\s*\|/mi);
  if (!m) return null;
  const key = m[1].trim();
  return key && key !== '-' ? key : null;
}

// Ambil tautan Scholar / Semantic Scholar dari bagian "Tautan Akses".
function firstMatch(md, re) {
  const m = md.match(re);
  if (!m) return null;
  return m[0].replace(/[).,;]+$/, '');
}
function extractLinks(md) {
  return {
    scholar: firstMatch(md, /https?:\/\/scholar\.google\.[^\s)\]]+/i),
    semantic: firstMatch(md, /https?:\/\/(www\.)?semanticscholar\.org\/[^\s)\]]+/i)
  };
}

// Bersihkan Markdown entri: buang H1 pertama (judul dirender aplikasi) dan
// bagian "## Daftar Isi" (digantikan rail TOC + scroll-spy aplikasi).
function cleanMarkdown(md, dropH1) {
  let text = md.replace(/\r\n/g, '\n');
  if (dropH1) {
    const lines = text.split('\n');
    let i = 0;
    while (i < lines.length && lines[i].trim() === '') i++;
    if (i < lines.length && /^#\s+/.test(lines[i])) lines.splice(i, 1);
    text = lines.join('\n');
  }
  // Hapus blok "## Daftar Isi" hingga tepat sebelum H2 berikutnya.
  text = text.replace(/^##[ \t]+Daftar Isi[\s\S]*?(?=^##[ \t])/m, '');
  return text.trim() + '\n';
}

function countWords(md) {
  const m = md.match(/[^\s]+/g);
  return m ? m.length : 0;
}

/* ------------------------------------------------------------------ *
 * Pindai dan rakit data entri
 * ------------------------------------------------------------------ */
const files = fs.readdirSync(ENTRI_DIR).filter(function (f) { return /\.md$/i.test(f); });
const entries = [];
const warnings = [];
const seenIds = Object.create(null);

files.forEach(function (file) {
  if (file.toUpperCase() === 'INDEX.MD') return; // sengaja dilewati
  const meta = parseName(file);
  if (!meta) { warnings.push('Nama berkas tidak cocok pola: ' + file); return; }
  if (seenIds[meta.id]) warnings.push('Nomor entri ganda: ' + meta.id + ' (' + file + ')');
  seenIds[meta.id] = true;

  const raw = fs.readFileSync(path.join(ENTRI_DIR, file), 'utf8');
  if (!raw.trim()) { warnings.push('Konten kosong: ' + file); return; }
  const links = extractLinks(raw);
  // Normalisasi jumlah entri usang (artefak batch: 150 / 154 / 191) menjadi 202.
  let md = cleanMarkdown(raw, true);
  md = md
    .replace(/\bdari (150|154|191)\b/g, 'dari 202')
    .replace(/(Lembar \d{3})\/(154|191)\b/g, '$1/202')
    .replace(/\b(154|191) entri\b/g, '202 entri');

  entries.push({
    num: meta.num,
    id: meta.id,
    year: meta.year,
    title: meta.title,
    theme: meta.theme,
    bib: extractBib(raw),
    special: false,
    words: countWords(md),
    scholar: links.scholar,
    semantic: links.semantic,
    md: md
  });
});

// Pemberhentian keras bila ada nama berkas tak dikenal; entri tidak boleh
// hilang diam-diam (lihat PLAN §11).
if (warnings.some(function (w) { return /tidak cocok pola/.test(w); })) {
  console.error('\n[build.js] Berkas bermasalah:');
  warnings.forEach(function (w) { console.error('   - ' + w); });
  fail('Ada nama berkas yang tidak cocok pola penamaan. Perbaiki lalu jalankan ulang.');
}

entries.sort(function (a, b) { return a.num - b.num; });

// TEMUAN sebagai entri spesial (pin di atas).
const temuanRaw = fs.readFileSync(TEMUAN_PATH, 'utf8');
const temuanMd = cleanMarkdown(temuanRaw, true);
const temuan = {
  num: 0,
  id: 'temuan',
  year: null,
  title: 'Temuan Riset: Sintesis Lintas Makalah',
  theme: 'Sintesis',
  bib: null,
  special: true,
  words: countWords(temuanMd),
  scholar: null,
  semantic: null,
  md: temuanMd
};

const DATA = [temuan].concat(entries);

/* ------------------------------------------------------------------ *
 * Statistik dan META
 * ------------------------------------------------------------------ */
const themeCounts = {};
const yearCounts = {};
let totalWords = 0;
entries.forEach(function (e) {
  themeCounts[e.theme] = (themeCounts[e.theme] || 0) + 1;
  yearCounts[e.year] = (yearCounts[e.year] || 0) + 1;
  totalWords += e.words;
});
const years = Object.keys(yearCounts).map(Number).sort(function (a, b) { return a - b; });
const themes = Object.keys(themeCounts).sort();
const minYear = years[0];
const maxYear = years[years.length - 1];
const totalMin = Math.round(totalWords / 200);
const totalHours = Math.max(1, Math.round(totalMin / 60));

const META = {
  total: entries.length,
  themeCount: themes.length,
  minYear: minYear,
  maxYear: maxYear,
  yearCounts: yearCounts,
  themeCounts: themeCounts,
  totalWords: totalWords,
  totalMin: totalMin,
  totalHours: totalHours,
  built: new Date().toISOString().slice(0, 10),
  markedVersion: MARKED_VERSION
};

/* ------------------------------------------------------------------ *
 * Laporan
 * ------------------------------------------------------------------ */
console.log('\n=== build.js: Ruang Baca Riset ===');
console.log('Entri reguler   : ' + entries.length);
console.log('Entri spesial   : TEMUAN (1)');
console.log('Tema            : ' + themes.length);
console.log('Rentang tahun   : ' + minYear + '-' + maxYear + ' (' + years.length + ' tahun berisi)');
console.log('Total kata      : ~' + totalWords.toLocaleString('en-US') + '  (kira-kira ' + totalHours + ' jam baca)');
console.log('\nDistribusi tema :');
themes.sort(function (a, b) { return themeCounts[b] - themeCounts[a]; }).forEach(function (t) {
  console.log('   ' + String(themeCounts[t]).padStart(3) + '  ' + t);
});
console.log('\nDistribusi tahun:');
years.forEach(function (y) { console.log('   ' + y + '  ' + String(yearCounts[y]).padStart(3) + '  ' + '#'.repeat(yearCounts[y])); });
if (warnings.length) {
  console.log('\nPeringatan:');
  warnings.forEach(function (w) { console.log('   ! ' + w); });
} else {
  console.log('\nPeringatan: tidak ada.');
}

if (DRY) {
  console.log('\n[--dry] Mode laporan; index.html TIDAK ditulis.\n');
  process.exit(0);
}

/* ------------------------------------------------------------------ *
 * Serialisasi data aman-script
 * ------------------------------------------------------------------ */
function safeJson(obj) {
  var out = JSON.stringify(obj).replace(/</g, '\\u003c'); // cegah </script> breakout
  out = out.split(String.fromCharCode(0x2028)).join('\\u2028'); // pemisah baris JS
  out = out.split(String.fromCharCode(0x2029)).join('\\u2029');
  return out;
}
const dataScript = 'window.DATA=' + safeJson(DATA) + ';\nwindow.META=' + safeJson(META) + ';';
const markedSrc = fs.readFileSync(MARKED_PATH, 'utf8');

/* ================================================================== *
 * STYLE: design system "Editorial Luxury"
 * ================================================================== */
const CSS = `
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0}
:root{
  --bg:#FAF9F6; --surface:#FFFFFF; --surface-2:#F4F2EC; --surface-3:#ECE9E1;
  --ink:#1A1D21; --ink-2:#5E6267; --ink-3:#8B8778;
  --line:#E6E3DA; --line-strong:#D4D0C4;
  --accent:#A03028; --accent-bg:#F8E9E5; --accent-ink:#A03028;
  --mark:#FCEEC5; --mark-ink:#5A4300;
  --serif:'Newsreader',Georgia,'Times New Roman',serif;
  --sans:'Plus Jakarta Sans','Helvetica Neue',system-ui,-apple-system,sans-serif;
  --mono:'JetBrains Mono','SF Mono',Consolas,monospace;
  --r-card:10px; --r-btn:6px; --r-pill:999px;
  --topbar-h:52px; --sidebar-w:300px; --toc-w:220px; --read-w:740px; --home-w:1080px;
  --ease:cubic-bezier(.32,.72,0,1); --dur:180ms;
  --shadow-hover:0 1px 10px rgba(26,29,33,.07);
}
html[data-theme="dark"]{
  --bg:#171613; --surface:#1F1E19; --surface-2:#1B1A16; --surface-3:#272520;
  --ink:#E9E6DD; --ink-2:#A7A296; --ink-3:#7E796C;
  --line:#2C2A24; --line-strong:#3E3B32;
  --accent:#E2988E; --accent-bg:rgba(226,152,142,.12); --accent-ink:#EBADA3;
  --mark:rgba(252,228,160,.18); --mark-ink:#F2DFAF;
  --shadow-hover:0 1px 10px rgba(0,0,0,.5);
}
body{
  background:var(--bg); color:var(--ink);
  font-family:var(--sans); font-size:15px; line-height:1.55;
  -webkit-font-smoothing:antialiased; text-rendering:optimizeLegibility;
  transition:background var(--dur) var(--ease), color var(--dur) var(--ease);
  -webkit-tap-highlight-color:transparent;
}
::selection{background:var(--accent-bg); color:var(--accent-ink)}
a{color:inherit; text-decoration:none}
button{font:inherit; color:inherit; background:none; border:none; cursor:pointer}
input,select{font:inherit; color:inherit}
h1,h2,h3,h4{font-weight:600; margin:0}
img{max-width:100%}
kbd{font-family:var(--mono); font-size:10.5px; line-height:1; padding:3px 5px;
  border:1px solid var(--line); border-bottom-width:2px; border-radius:4px;
  background:var(--surface-2); color:var(--ink-2)}
a:focus-visible,button:focus-visible,select:focus-visible,[tabindex]:focus-visible,[role="button"]:focus-visible{
  outline:2px solid color-mix(in srgb,var(--accent) 60%,transparent); outline-offset:2px}

/* ---------- topbar ---------- */
.topbar{position:sticky; top:0; z-index:60; height:var(--topbar-h);
  display:flex; align-items:center; gap:12px; padding:0 18px;
  background:color-mix(in srgb, var(--bg) 86%, transparent);
  backdrop-filter:saturate(1.3) blur(10px); -webkit-backdrop-filter:saturate(1.3) blur(10px);
  border-bottom:1px solid var(--line)}
.topbar .brand{display:flex; align-items:center; gap:9px; font-family:var(--serif);
  font-size:17px; letter-spacing:-.01em; white-space:nowrap}
.topbar .brand b{font-weight:600}
.topbar .brand .dot{width:8px; height:8px; border-radius:50%; background:var(--accent); transition:transform var(--dur) var(--ease)}
.topbar .brand:hover .dot{transform:scale(1.3)}
.topbar .spacer{flex:1}
.search-trigger{display:flex; align-items:center; gap:8px; height:34px; padding:0 9px 0 10px;
  min-width:210px; color:var(--ink-3); background:transparent;
  border:1px solid var(--line); border-radius:var(--r-btn); transition:border-color var(--dur), color var(--dur)}
.search-trigger:hover{border-color:var(--line-strong); color:var(--ink-2)}
.search-trigger svg{width:15px; height:15px; flex-shrink:0}
.search-trigger .st-label{flex:1; text-align:left; font-family:var(--mono); font-size:11.5px; letter-spacing:.02em;
  overflow:hidden; text-overflow:ellipsis; white-space:nowrap}
.search-trigger kbd{margin-left:auto}
.icon-btn{display:inline-flex; align-items:center; justify-content:center; width:34px; height:34px;
  border-radius:var(--r-btn); color:var(--ink-2); border:1px solid transparent; transition:all var(--dur) var(--ease)}
.icon-btn:hover{color:var(--ink); background:var(--surface-2); border-color:var(--line)}
.icon-btn svg{width:18px; height:18px}
.icon-btn:active{transform:scale(.94)}
.menu-btn{display:none}
.progress{position:absolute; left:0; right:0; bottom:-1px; height:2px; background:transparent}
.progress > span{display:block; height:100%; width:100%; transform:scaleX(0); transform-origin:left; background:var(--accent);
  transition:transform .1s linear}

/* ---------- layout & mode rute ---------- */
.layout{display:grid; grid-template-columns:var(--sidebar-w) minmax(0,1fr); align-items:start}
body.on-entry .layout{display:block}
.main{min-width:0; padding:36px clamp(20px,4.5vw,56px) 96px}
.main:focus{outline:none}
.wrap{max-width:var(--read-w); margin:0 auto}
body.on-home .wrap{max-width:var(--home-w)}
#katalog{scroll-margin-top:calc(var(--topbar-h) + 14px)}

/* ---------- sidebar (khusus penyaring) ---------- */
.sidebar{position:sticky; top:var(--topbar-h); height:calc(100dvh - var(--topbar-h));
  display:flex; flex-direction:column; border-right:1px solid var(--line);
  background:var(--surface-2)}
@media(min-width:981px){ body.on-entry .sidebar{display:none} }
.sb-top{padding:18px 16px 14px; display:flex; flex-direction:column; gap:13px}
.search-box{position:relative; display:flex; align-items:center}
.search-box svg.ic{position:absolute; left:10px; width:15px; height:15px; color:var(--ink-3); pointer-events:none}
.search-box input{width:100%; height:36px; padding:0 32px 0 32px; color:var(--ink); font-size:13.5px;
  background:var(--surface); border:1px solid var(--line); border-radius:var(--r-btn);
  transition:border-color var(--dur), box-shadow var(--dur)}
.search-box input:focus{outline:none; border-color:var(--accent); box-shadow:0 0 0 3px var(--accent-bg)}
.search-box .clr{position:absolute; right:5px; width:24px; height:24px; display:none;
  align-items:center; justify-content:center; border-radius:5px; color:var(--ink-3)}
.search-box .clr:hover{background:var(--surface-2); color:var(--ink)}
.search-box.has-val .clr{display:flex}
.sb-label{font-family:var(--mono); font-size:9.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--ink-3)}
.chips-wrap{display:flex; flex-direction:column; gap:7px}
.chips{display:flex; flex-wrap:wrap; gap:5px; max-height:112px; overflow:hidden}
.chips.expanded{max-height:40vh; overflow-y:auto}
.chips-toggle{align-self:flex-start; font-family:var(--mono); font-size:10.5px; letter-spacing:.02em;
  color:var(--accent-ink); padding:2px 3px; border-radius:4px}
.chips-toggle:hover{background:var(--accent-bg)}
.chip{display:inline-flex; align-items:center; gap:6px; height:24px; padding:0 8px;
  font-size:11.5px; font-weight:500; color:var(--ink-2); background:var(--surface);
  border:1px solid var(--line); border-radius:var(--r-pill); white-space:nowrap;
  transition:all .16s var(--ease)}
.chip .cd{width:6px; height:6px; border-radius:50%; background:var(--tc,var(--ink-3))}
.chip:hover{border-color:var(--line-strong); color:var(--ink)}
.chip[aria-pressed="true"]{color:var(--tc,var(--accent-ink)); border-color:color-mix(in srgb,var(--tc,var(--accent)) 45%,var(--line));
  background:color-mix(in srgb,var(--tc,var(--accent)) 10%,var(--surface))}
.chip:active{transform:scale(.95)}
.sb-controls{display:flex; align-items:center; gap:7px}
.year-sel{flex:1; height:30px; padding:0 7px; font-size:12px; color:var(--ink);
  background:var(--surface); border:1px solid var(--line); border-radius:var(--r-btn);
  transition:border-color var(--dur)}
.year-sel:hover{border-color:var(--line-strong)}
.reset-btn{height:30px; padding:0 10px; font-size:11.5px; font-weight:500; color:var(--ink-2);
  border:1px solid var(--line); border-radius:var(--r-btn); background:var(--surface);
  transition:color var(--dur), border-color var(--dur)}
.reset-btn:hover{color:var(--accent-ink); border-color:color-mix(in srgb,var(--accent) 40%,var(--line))}
.reset-btn:active{transform:scale(.95)}
.sb-count{font-size:11px; color:var(--ink-3); font-family:var(--mono); letter-spacing:.02em}
.sb-note{margin-top:auto; padding:14px 16px; border-top:1px solid var(--line);
  font-size:11.5px; line-height:1.55; color:var(--ink-3)}
.sb-note a{color:var(--accent-ink)}
.sb-note a:hover{text-decoration:underline}
.sb-note kbd{font-size:9.5px}

/* ---------- header entri ---------- */
.back-link{display:inline-flex; align-items:center; gap:7px; font-family:var(--mono); font-size:10.5px;
  letter-spacing:.1em; text-transform:uppercase; color:var(--ink-3); margin-bottom:24px; transition:color var(--dur)}
.back-link:hover{color:var(--accent-ink)}
.back-link svg{width:12px; height:12px}
.eh{margin-bottom:30px}
.eyebrow{display:flex; flex-wrap:wrap; align-items:center; gap:9px; font-family:var(--mono);
  font-size:11px; letter-spacing:.07em; text-transform:uppercase; color:var(--ink-3); margin-bottom:16px}
.eyebrow .t-chip{display:inline-flex; align-items:center; gap:6px; padding:3px 9px; border-radius:var(--r-pill);
  font-weight:500; letter-spacing:.02em; text-transform:none; color:var(--tc,var(--accent-ink));
  background:color-mix(in srgb,var(--tc,var(--accent)) 10%,var(--surface));
  border:1px solid color-mix(in srgb,var(--tc,var(--accent)) 25%,transparent)}
.eyebrow .t-chip .cd{width:6px; height:6px; border-radius:50%; background:var(--tc,var(--accent))}
.eyebrow .sep{color:var(--line-strong)}
.eh h1{font-family:var(--serif); font-weight:600; letter-spacing:-.022em; line-height:1.1;
  font-size:clamp(30px,4.6vw,44px); margin:0 0 16px; text-wrap:balance}
.eh-meta{display:flex; flex-wrap:wrap; align-items:center; gap:8px 12px; font-size:12.5px; color:var(--ink-2)}
.meta-btn{display:inline-flex; align-items:center; gap:6px; font-family:var(--mono); font-size:11px;
  color:var(--ink-2); padding:4px 9px; border:1px solid var(--line); border-radius:var(--r-btn);
  background:transparent; transition:all var(--dur)}
.meta-btn:hover{color:var(--ink); border-color:var(--line-strong); background:var(--surface-2)}
.meta-btn:active{transform:scale(.95)}
.meta-btn svg{width:12px; height:12px}
.meta-btn.ok{color:#2f7d43; border-color:#8fce9f}
html[data-theme="dark"] .meta-btn.ok{color:#8fd9a3; border-color:#3c6b48}
.meta-link{display:inline-flex; align-items:center; gap:5px; color:var(--accent-ink); font-size:12px; font-weight:500}
.meta-link:hover{text-decoration:underline}
.meta-link svg{width:12px; height:12px}
.readtime{display:inline-flex; align-items:center; gap:5px; font-family:var(--mono); font-size:11px; color:var(--ink-3)}
.readtime svg{width:12px; height:12px}

/* ---------- tipografi artikel (serif) ---------- */
.article{font-family:var(--serif); font-size:17.5px; line-height:1.78; color:var(--ink); overflow-wrap:break-word}
.article > *:first-child{margin-top:0}
.article p{margin:0 0 1.1em; text-wrap:pretty}
.article h2{font-family:var(--serif); font-weight:600; letter-spacing:-.014em; font-size:27px;
  line-height:1.2; margin:2.1em 0 .75em; scroll-margin-top:calc(var(--topbar-h) + 18px); position:relative; text-wrap:balance}
.article h3{font-family:var(--serif); font-weight:600; font-size:20.5px; margin:1.8em 0 .6em; letter-spacing:-.008em;
  line-height:1.3; scroll-margin-top:calc(var(--topbar-h) + 18px); position:relative}
.article h4{font-family:var(--sans); font-size:12px; letter-spacing:.1em; text-transform:uppercase; margin:1.6em 0 .55em; color:var(--ink-2)}
.article h2 .anchor,.article h3 .anchor{position:absolute; left:-1.1em; top:.1em; width:.9em;
  opacity:0; color:var(--ink-3); font-weight:400; transition:opacity .15s; font-family:var(--sans); border:none}
.article h2:hover .anchor,.article h3:hover .anchor{opacity:1}
.article h2 .anchor:hover,.article h3 .anchor:hover{color:var(--accent)}
.article a{color:var(--accent-ink); text-decoration:none; border-bottom:1px solid color-mix(in srgb,var(--accent) 30%,transparent);
  transition:border-color var(--dur)}
.article a:hover{border-bottom-color:var(--accent)}
.article a.entry-link{color:var(--ink); background:var(--surface-2);
  border:1px solid var(--line); border-radius:5px; padding:1px 6px; font-family:var(--sans); font-size:.84em}
.article a.entry-link:hover{border-color:color-mix(in srgb,var(--accent) 40%,var(--line)); color:var(--accent-ink)}
.article ul,.article ol{margin:0 0 1.1em; padding-left:1.35em}
.article li{margin:.32em 0}
.article li::marker{color:var(--ink-3)}
.article ul.contains-task-list{list-style:none; padding-left:.2em}
.article li.task-list-item{display:flex; gap:.6em; align-items:flex-start; list-style:none}
.article li.task-list-item input{margin-top:.45em; accent-color:var(--accent)}
.article blockquote{margin:1.7em 0; padding:.1em 0 .1em 1.2em; border-left:2px solid var(--accent);
  font-style:italic; font-size:1.05em; color:var(--ink-2)}
.article blockquote p{margin:.35em 0}
.article blockquote strong{color:var(--ink)}
.article hr{border:none; margin:2.6em 0; text-align:center; background:none; height:auto}
.article hr::after{content:"···"; font-family:var(--mono); font-size:13px; letter-spacing:.55em; color:var(--ink-3)}
.article code{font-family:var(--mono); font-size:.8em; padding:.14em .4em; border-radius:4px;
  background:var(--surface-3); color:var(--ink); border:1px solid var(--line)}
.article pre{margin:1.4em 0; padding:15px 17px; overflow-x:auto; background:var(--surface-2);
  border:1px solid var(--line); border-radius:8px; line-height:1.65}
.article pre code{background:none; border:none; padding:0; font-size:13px}
.article strong{font-weight:600; color:var(--ink)}
.article del{color:var(--ink-3)}
.table-wrap{margin:1.5em 0; overflow-x:auto; border:1px solid var(--line); border-radius:8px}
.table-wrap::-webkit-scrollbar{height:8px}
.table-wrap::-webkit-scrollbar-thumb{background:var(--line-strong); border-radius:6px}
.article table{width:100%; border-collapse:collapse; font-family:var(--sans); font-size:13.5px; min-width:min(560px,100%)}
.article thead th{background:var(--surface-2); text-align:left; font-weight:600; color:var(--ink-2);
  font-size:11.5px; letter-spacing:.03em; padding:9px 13px; border-bottom:1px solid var(--line-strong); white-space:nowrap}
.article tbody td{padding:9px 13px; border-bottom:1px solid var(--line); vertical-align:top}
.article tbody tr:last-child td{border-bottom:none}

/* prev/next */
.pn{display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:60px; padding-top:26px; border-top:1px solid var(--line)}
.pn a{display:flex; flex-direction:column; gap:6px; padding:14px 16px; border:1px solid var(--line);
  border-radius:var(--r-card); background:transparent; transition:all var(--dur) var(--ease)}
.pn a:hover{border-color:var(--line-strong); background:var(--surface); box-shadow:var(--shadow-hover)}
.pn a:active{transform:scale(.99)}
.pn .pn-dir{font-family:var(--mono); font-size:10px; letter-spacing:.1em; text-transform:uppercase; color:var(--ink-3);
  display:flex; align-items:center; gap:6px}
.pn .pn-dir svg{width:12px; height:12px}
.pn .pn-next{text-align:right; align-items:flex-end}
.pn .pn-title{font-family:var(--serif); font-size:16.5px; line-height:1.28; color:var(--ink)}
.pn a:hover .pn-title{color:var(--accent-ink)}
.pn .empty{visibility:hidden}

/* ---------- TOC melayang (mode entri) ---------- */
.toc{display:none}
@media(min-width:1260px){
  body.on-entry .toc{display:block; position:fixed; z-index:40;
    top:calc(var(--topbar-h) + 44px);
    right:max(16px, calc((100vw - var(--read-w))/2 - var(--toc-w) - 44px));
    width:var(--toc-w); max-height:calc(100dvh - var(--topbar-h) - 72px);
    overflow-y:auto; padding:4px 0 24px}
}
.toc-inner{border-left:1px solid var(--line); padding-left:14px}
.toc-h{font-family:var(--mono); font-size:9.5px; letter-spacing:.16em; text-transform:uppercase;
  color:var(--ink-3); margin-bottom:11px}
.toc a{display:block; font-size:12px; line-height:1.4; color:var(--ink-3); padding:4.5px 0 4.5px 11px;
  margin-left:-15px; border-left:2px solid transparent; transition:color .15s, border-color .15s; border-bottom:none}
.toc a.lvl-3{padding-left:22px; font-size:11.5px}
.toc a:hover{color:var(--ink)}
.toc a.active{color:var(--accent-ink); border-left-color:var(--accent); font-weight:500}

/* ---------- HOME ---------- */
.home{padding-bottom:20px}
.hero{padding:34px 0 44px}
.hero .eb{display:inline-flex; align-items:center; gap:8px; font-family:var(--mono); font-size:10.5px;
  letter-spacing:.12em; text-transform:uppercase; color:var(--ink-2); padding:5px 11px; border:1px solid var(--line);
  border-radius:var(--r-pill); background:transparent; margin-bottom:24px}
.hero .eb .dot{width:6px; height:6px; border-radius:50%; background:var(--accent)}
.hero h1{font-family:var(--serif); font-weight:600; letter-spacing:-.028em; line-height:1.03;
  font-size:clamp(44px,7vw,74px); margin:0 0 22px; text-wrap:balance}
.hero h1 .muted{color:var(--ink-3); font-style:italic; font-weight:500; letter-spacing:-.01em}
.hero .lede{font-size:clamp(15.5px,1.9vw,18px); line-height:1.62; color:var(--ink-2); max-width:620px; margin:0 0 30px; text-wrap:pretty}
.cta-row{display:flex; flex-wrap:wrap; gap:11px}
.btn{display:inline-flex; align-items:center; gap:9px; height:44px; padding:0 20px; font-size:14px;
  font-weight:500; border-radius:var(--r-btn); border:1px solid transparent; transition:all var(--dur) var(--ease)}
.btn svg{width:15px; height:15px}
.btn-solid{background:var(--ink); color:var(--bg)}
.btn-solid:hover{transform:translateY(-1px); box-shadow:0 6px 18px color-mix(in srgb,var(--ink) 20%,transparent)}
.btn-ghost{border-color:var(--line-strong); color:var(--ink); background:transparent}
.btn-ghost:hover{border-color:var(--ink-3); background:var(--surface-2)}
.btn:active{transform:translateY(0) scale(.98)}
.resume{margin-top:26px}
.resume a{display:inline-flex; align-items:baseline; gap:9px; font-size:13px; color:var(--ink-2)}
.resume a:hover .k{border-bottom-color:var(--accent)}
.resume .k{font-family:var(--mono); font-size:10.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--accent-ink);
  border-bottom:1px solid transparent; transition:border-color var(--dur)}
.resume .num{font-family:var(--mono); font-size:11.5px; color:var(--ink-3)}
.resume .t{font-family:var(--serif); font-style:italic; font-size:14.5px}
.resume svg{width:12px; height:12px; align-self:center}

.section-h{display:flex; align-items:baseline; gap:12px; margin:56px 0 22px}
.section-h h2{font-family:var(--serif); font-weight:600; font-size:26px; letter-spacing:-.014em; text-wrap:balance}
.section-h .sub{font-family:var(--mono); font-size:10.5px; letter-spacing:.08em; text-transform:uppercase; color:var(--ink-3)}
.section-h .line{flex:1; height:1px; background:var(--line)}

/* strip statistik */
.stats{display:grid; grid-template-columns:repeat(4,1fr); border-top:1px solid var(--line-strong); border-bottom:1px solid var(--line-strong)}
.stat{padding:22px 18px; border-left:1px solid var(--line)}
.stat:first-child{border-left:none}
.stat .n{font-family:var(--serif); font-size:clamp(30px,3.8vw,42px); font-weight:600; letter-spacing:-.02em; line-height:1}
.stat .l{font-family:var(--mono); font-size:10px; letter-spacing:.12em; text-transform:uppercase; color:var(--ink-3); margin-top:10px}
@media(max-width:640px){
  .stats{grid-template-columns:repeat(2,1fr)}
  .stat{padding:16px 14px}
  .stat:nth-child(odd){border-left:none}
  .stat:nth-child(n+3){border-top:1px solid var(--line)}
}

/* timeline */
.timeline{padding:8px 2px 4px}
.tl-bars{display:flex; align-items:flex-end; gap:2.2%; height:140px}
.tl-col{flex:1; display:flex; flex-direction:column; align-items:center; gap:9px; height:100%; justify-content:flex-end; cursor:pointer}
.tl-bar{width:100%; max-width:26px; border-radius:3px 3px 1px 1px; background:var(--surface-3);
  transition:background var(--dur); position:relative; min-height:3px}
.tl-col:hover .tl-bar{background:var(--accent)}
.tl-bar .tip{position:absolute; bottom:calc(100% + 7px); left:50%; transform:translateX(-50%) scale(.9);
  opacity:0; pointer-events:none; font-family:var(--mono); font-size:10.5px; white-space:nowrap; padding:4px 8px;
  background:var(--ink); color:var(--bg); border-radius:5px; transition:all .15s var(--ease)}
.tl-col:hover .tip{opacity:1; transform:translateX(-50%) scale(1)}
.tl-yr{font-family:var(--mono); font-size:10px; color:var(--ink-3); writing-mode:vertical-rl; transform:rotate(180deg)}
@media(min-width:560px){ .tl-yr{writing-mode:horizontal-tb; transform:none} }

/* indeks tema (daftar datar) */
.tlist{border-top:1px solid var(--line-strong)}
.trow{display:flex; align-items:center; gap:14px; width:100%; padding:13px 4px; text-align:left;
  border-bottom:1px solid var(--line); transition:background .15s}
.trow:hover{background:var(--surface-2)}
.trow .cd{width:8px; height:8px; border-radius:50%; background:var(--tc); flex-shrink:0}
.trow-name{font-weight:600; font-size:14px; width:190px; flex-shrink:0; white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
.trow-samples{flex:1; min-width:0; font-size:12.5px; color:var(--ink-3); white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
.trow-bar{width:110px; height:3px; border-radius:2px; background:var(--surface-3); flex-shrink:0; overflow:hidden}
.trow-bar span{display:block; height:100%; background:var(--tc); border-radius:2px}
.trow-count{font-family:var(--mono); font-size:12px; color:var(--ink-2); width:34px; text-align:right; flex-shrink:0}
@media(max-width:760px){ .trow-samples,.trow-bar{display:none} .trow-name{width:auto; flex:1; min-width:0} }

/* katalog (tabel indeks) */
.cat{overflow-x:auto}
.cat-table{width:100%; border-collapse:collapse}
.cat-table thead th{font-family:var(--mono); font-size:10px; letter-spacing:.12em; text-transform:uppercase;
  color:var(--ink-3); text-align:left; padding:0 12px 10px 4px; border-bottom:1px solid var(--line-strong);
  cursor:pointer; user-select:none; white-space:nowrap; transition:color var(--dur)}
.cat-table thead th:hover{color:var(--ink)}
.cat-table thead th.sorted{color:var(--accent-ink)}
.cat-table thead th .arr{display:inline-block; width:12px; margin-left:2px; font-size:9px}
.cat-table tbody tr{border-bottom:1px solid var(--line); cursor:pointer; transition:background .12s}
.cat-table tbody tr:hover{background:var(--surface-2)}
.cat-table tbody tr:active{background:var(--surface-3)}
.cat-table td{padding:11px 12px 11px 4px; vertical-align:baseline}
.c-num{font-family:var(--mono); font-size:11px; color:var(--ink-3); width:44px; white-space:nowrap}
tr.special .c-num{color:var(--accent)}
.c-title{font-family:var(--serif); font-size:15.5px; line-height:1.32; color:var(--ink)}
.cat-table tbody tr:hover .c-title{color:var(--accent-ink)}
.c-title mark{background:var(--mark); color:var(--mark-ink); border-radius:2px; padding:0 1px}
.c-theme{font-size:11.5px; color:var(--ink-2); white-space:nowrap}
.c-theme .cd{display:inline-block; width:7px; height:7px; border-radius:50%; background:var(--tc); margin-right:7px}
.c-year{font-family:var(--mono); font-size:11.5px; color:var(--ink-3); width:56px; white-space:nowrap}
.c-min{font-family:var(--mono); font-size:11px; color:var(--ink-3); width:64px; text-align:right; white-space:nowrap}
tr.special .c-title{font-style:italic}
.cat-empty{padding:30px 8px; text-align:center; color:var(--ink-3); font-size:13px; border-bottom:1px solid var(--line)}
@media(max-width:760px){
  .c-theme,.c-min,.cat-table thead th[data-sort="theme"],.cat-table thead th[data-sort="min"]{display:none}
  .cat-table td{padding:10px 8px 10px 4px}
}

/* jalur baca bernomor */
.plist{border-top:1px solid var(--line-strong)}
.path{display:grid; grid-template-columns:52px 1fr; gap:4px 18px; padding:20px 4px; border-bottom:1px solid var(--line)}
.path-num{font-family:var(--mono); font-size:10px; letter-spacing:.06em; color:var(--ink-3); padding-top:4px; display:flex; flex-direction:column; line-height:1.25}
.path-num b{font-size:17px; font-weight:500; color:var(--ink); letter-spacing:-.02em}
.path-num i{font-style:normal; margin-top:3px}
.path h3{font-family:var(--serif); font-size:21px; font-weight:600; letter-spacing:-.012em}
.path .ptag{font-family:var(--mono); font-size:10px; letter-spacing:.08em; text-transform:uppercase; color:var(--ink-3); margin-left:10px; white-space:nowrap}
.path p{font-size:13.5px; color:var(--ink-2); line-height:1.55; margin:6px 0 13px; max-width:640px; text-wrap:pretty}
.pchips{display:flex; flex-wrap:wrap; gap:6px}
.pchip{display:inline-flex; align-items:center; gap:6px; height:26px; padding:0 9px; font-size:12px; color:var(--ink-2);
  background:transparent; border:1px solid var(--line); border-radius:var(--r-btn); transition:all var(--dur)}
.pchip .pn2{font-family:var(--mono); font-size:10px; color:var(--ink-3)}
.pchip:hover{border-color:color-mix(in srgb,var(--accent) 40%,var(--line)); color:var(--accent-ink)}
.pchip:active{transform:scale(.95)}

/* footer */
.foot{margin-top:64px; padding-top:22px; border-top:1px solid var(--line-strong); display:flex; flex-wrap:wrap;
  align-items:center; gap:14px 24px; font-family:var(--mono); font-size:11px; letter-spacing:.03em; color:var(--ink-3)}
.foot code{font-family:var(--mono); font-size:10.5px; padding:2px 6px; background:var(--surface-2);
  border:1px solid var(--line); border-radius:4px; color:var(--ink-2)}
.foot a{color:var(--ink-2); border-bottom:1px solid var(--line)}
.foot a:hover{color:var(--accent-ink); border-color:var(--accent)}
.foot .fspacer{flex:1}

/* 404 */
.nf{max-width:var(--read-w); margin:70px auto; text-align:center}
.nf .code{font-family:var(--mono); font-size:11px; letter-spacing:.14em; color:var(--accent)}
.nf h1{font-family:var(--serif); font-size:36px; letter-spacing:-.02em; margin:14px 0 10px; text-wrap:balance}
.nf p{color:var(--ink-2); margin-bottom:26px}

/* ---------- reveal / motion ---------- */
.rv{opacity:0; transform:translateY(12px); transition:opacity .45s var(--ease), transform .45s var(--ease);
  transition-delay:calc(var(--i,0) * 45ms)}
.rv.in{opacity:1; transform:none}
@media(prefers-reduced-motion:reduce){ .rv{opacity:1; transform:none; transition:none} *{scroll-behavior:auto!important} }

/* ---------- drawer / scrim (mobile) ---------- */
.scrim{position:fixed; inset:0; z-index:70; background:rgba(23,22,19,.44); opacity:0; visibility:hidden;
  transition:opacity var(--dur) var(--ease), visibility var(--dur)}
body.drawer-open .scrim{opacity:1; visibility:visible}
.hb{display:block; position:relative; width:17px; height:12px}
.hb span{position:absolute; left:0; width:100%; height:1.5px; background:currentColor; border-radius:2px;
  transition:transform var(--dur) var(--ease), opacity var(--dur) var(--ease)}
.hb span:nth-child(1){top:0} .hb span:nth-child(2){top:5.2px} .hb span:nth-child(3){top:10.4px}
body.drawer-open .hb span:nth-child(1){transform:translateY(5.2px) rotate(45deg)}
body.drawer-open .hb span:nth-child(2){opacity:0}
body.drawer-open .hb span:nth-child(3){transform:translateY(-5.2px) rotate(-45deg)}

@media(max-width:980px){
  .menu-btn{display:inline-flex}
  .layout,body.on-entry .layout{display:block}
  .sidebar{position:fixed; top:0; left:0; z-index:80; display:flex; width:min(330px,86vw); height:100dvh;
    transform:translateX(-100%); transition:transform var(--dur) var(--ease); box-shadow:0 0 40px rgba(0,0,0,.16)}
  body.drawer-open .sidebar{transform:none}
  .toc{display:none!important}
  .main{padding:26px 18px 80px}
}
@media(max-width:560px){
  .pn{grid-template-columns:1fr}
  .search-trigger{min-width:0; padding:0; width:34px; justify-content:center}
  .search-trigger .st-label,.search-trigger kbd{display:none}
}

/* ---------- help modal ---------- */
.modal{position:fixed; inset:0; z-index:120; display:none; align-items:center; justify-content:center; padding:20px}
.modal.open{display:flex}
.modal-bg{position:absolute; inset:0; background:rgba(23,22,19,.5); backdrop-filter:blur(3px)}
.modal-card{position:relative; width:min(460px,100%); background:var(--surface); border:1px solid var(--line);
  border-radius:12px; padding:24px; box-shadow:0 20px 50px rgba(0,0,0,.25)}
.modal-card h3{font-family:var(--serif); font-size:21px; margin-bottom:16px; letter-spacing:-.01em}
.sc-row{display:flex; align-items:center; justify-content:space-between; padding:9px 0; border-bottom:1px solid var(--line); font-size:13px}
.sc-row:last-child{border-bottom:none}
.sc-row .keys{display:flex; gap:5px}
.modal-close{position:absolute; top:14px; right:14px}
.modal.open .modal-card{animation:mpop .22s var(--ease)}
@keyframes mpop{from{opacity:0; transform:scale(.97) translateY(5px)}}
@media(prefers-reduced-motion:reduce){ .modal.open .modal-card{animation:none} }

.skip-link{position:fixed; top:10px; left:10px; z-index:210; padding:9px 14px; font-size:13px; font-weight:500;
  background:var(--ink); color:var(--bg); border-radius:var(--r-btn);
  transform:translateY(-240%); opacity:0; transition:transform var(--dur) var(--ease), opacity var(--dur)}
.skip-link:focus-visible{transform:none; opacity:1}
@media print{
  .topbar,.sidebar,.toc,.scrim,.skip-link,.modal,.pn,.back-link{display:none!important}
  .layout,body.on-entry .layout{display:block}
  .main{padding:0}
  .wrap,body.on-home .wrap{max-width:none}
  body{background:#fff; color:#1a1a1a; transition:none}
  .eh h1{font-size:24pt}
  .article{font-size:12pt; line-height:1.6}
}
`;

/* ================================================================== *
 * SHELL: kerangka markup (bagian dinamis diisi runtime)
 * ================================================================== */
const SHELL = `
<a class="skip-link" href="#main">Langsung ke konten</a>
<header class="topbar">
  <button class="icon-btn menu-btn" id="menuBtn" aria-label="Buka navigasi" aria-expanded="false">
    <span class="hb" aria-hidden="true"><span></span><span></span><span></span></span>
  </button>
  <a class="brand" href="#/" aria-label="Beranda"><span class="dot" aria-hidden="true"></span><b>Ruang Baca Riset</b></a>
  <div class="spacer"></div>
  <button class="search-trigger" id="searchTrigger" aria-label="Cari">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.2-3.2"/></svg>
    <span class="st-label">Cari judul, tema, isi&hellip;</span>
    <kbd>Ctrl K</kbd>
  </button>
  <button class="icon-btn" id="themeBtn" aria-label="Ganti tema"></button>
  <button class="icon-btn" id="helpBtn" aria-label="Pintasan papan tik">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M9.2 9.3a2.8 2.8 0 0 1 5.4 1c0 1.9-2.6 2-2.6 3.4"/><circle cx="12" cy="17.4" r=".9" fill="currentColor" stroke="none"/></svg>
  </button>
  <div class="progress" aria-hidden="true"><span id="progressBar"></span></div>
</header>

<div class="layout">
  <aside class="sidebar" id="sidebar" aria-label="Penyaring katalog">
    <div class="sb-top">
      <div class="search-box" id="searchBox">
        <svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.2-3.2"/></svg>
        <input id="searchInput" type="search" placeholder="Cari judul, tema, isi&hellip;" autocomplete="off" spellcheck="false" aria-label="Kotak pencarian">
        <button class="clr" id="searchClear" aria-label="Bersihkan pencarian">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M6 6l12 12M18 6L6 18"/></svg>
        </button>
      </div>
      <div class="chips-wrap">
        <div class="sb-label">Tema</div>
        <div class="chips" id="chips"></div>
        <button class="chips-toggle" id="chipsToggle" type="button" aria-expanded="false"></button>
      </div>
      <div class="sb-controls">
        <select class="year-sel" id="yearSel" aria-label="Saring tahun"></select>
        <button class="reset-btn" id="resetBtn">Reset</button>
      </div>
      <div class="sb-count" id="sbCount"></div>
    </div>
    <div class="sb-note">Penyaring diterapkan ke <a href="#/">katalog di beranda</a>.<br>Pintasan: <kbd>/</kbd> cari &middot; <kbd>&larr;</kbd><kbd>&rarr;</kbd> pindah entri &middot; <kbd>t</kbd> tema.</div>
  </aside>

  <div class="scrim" id="scrim" aria-hidden="true"></div>

  <main class="main" id="main" tabindex="-1"></main>

  <nav class="toc" id="toc" aria-label="Daftar isi"></nav>
</div>

<div class="modal" id="helpModal" role="dialog" aria-modal="true" aria-label="Pintasan papan tik">
  <div class="modal-bg" data-close></div>
  <div class="modal-card">
    <button class="icon-btn modal-close" data-close aria-label="Tutup">
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
    <h3>Pintasan papan tik</h3>
    <div class="sc-row"><span>Fokus pencarian</span><span class="keys"><kbd>/</kbd><kbd>Ctrl K</kbd></span></div>
    <div class="sc-row"><span>Entri sebelumnya / berikutnya</span><span class="keys"><kbd>&larr;</kbd><kbd>&rarr;</kbd></span></div>
    <div class="sc-row"><span>Ganti tema terang / gelap</span><span class="keys"><kbd>t</kbd></span></div>
    <div class="sc-row"><span>Tutup / bersihkan</span><span class="keys"><kbd>Esc</kbd></span></div>
    <div class="sc-row"><span>Bantuan ini</span><span class="keys"><kbd>?</kbd></span></div>
  </div>
</div>`;

/* ================================================================== *
 * RUNTIME: aplikasi klien (di-serialisasi via .toString())
 *    Hanya mereferensi global browser + window.DATA / window.META.
 * ================================================================== */
function RUNTIME() {
  'use strict';
  var DATA = window.DATA, META = window.META;
  var doc = document;

  /* ---- data index ---- */
  var byId = {};
  DATA.forEach(function (e) { byId[e.id] = e; });
  var ENTRIES = DATA.filter(function (e) { return !e.special; });

  var THEME_COLORS = {
    'Fondasi RGB': '#2B6CB0', 'Survei YOLO': '#2F7D5B', 'YOLO plus RGB-D': '#0E7490',
    'RGB-D SOD': '#3F7A44', 'Segmentasi RGB-D': '#617A1F', 'Estimasi Kedalaman': '#A6740E',
    'Pose 6D': '#7A5AA0', 'Deteksi 3D': '#4F46A5', 'Grasp Robotik': '#B0433F',
    'RGB-D SLAM': '#A04763', 'Pedestrian RGB-T': '#A9611A', 'Pertanian': '#6C8018',
    'Medis': '#128577', 'Industri': '#5C6875', 'Remote Sensing': '#2E86AB',
    'Fusi Multimodal': '#8B5CB4', 'Dataset': '#7C755E', 'Sintesis': '#A03028'
  };
  function tColor(t) { return THEME_COLORS[t] || 'var(--ink-2)'; }

  var PATHS = [
    { name: 'Evolusi YOLO', tag: 'v1 - v11', desc: 'Lintasan inti YOLO: dari deteksi-sebagai-regresi tunggal menuju desain bebas-NMS dan bermodul atensi.', ids: ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'] },
    { name: 'Fondasi Deteksi & Transformer', tag: 'R-CNN - DETR', desc: 'Tulang punggung deteksi modern: dua-tahap, satu-tahap, anchor-free, hingga transformer (DETR, ViT, Swin, RT-DETR).', ids: ['012', '014', '015', '016', '019', '022', '024', '025', '155'] },
    { name: 'Fusi RGB-D Inti', tag: 'SOD / Segmentasi / Integrasi', desc: 'Jantung tinjauan: saliency, segmentasi semantik, dan integrasi YOLO+Depth dengan atensi lintas-modal.', ids: ['035', '036', '042', '055', '058', '112', '113', '118'] },
    { name: 'Robotik & Geometri 3D', tag: 'Pose / Grasp / SLAM / 3D', desc: 'Dari estimasi pose 6D dan penggenggaman ke SLAM dinamis dan deteksi 3D untuk aksi robotik.', ids: ['074', '082', '088', '107', '108', '114'] }
  ];

  var ICON = {
    arrowR: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M5 12h13M13 6l6 6-6 6"/></svg>',
    arrowL: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M19 12H6M11 6l-6 6 6 6"/></svg>',
    book: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 5.5A2 2 0 0 1 6 4h6v15H6a2 2 0 0 0-2 2z"/><path d="M20 5.5A2 2 0 0 0 18 4h-6v15h6a2 2 0 0 1 2 2z"/></svg>',
    copy: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V6a2 2 0 0 1 2-2h9"/></svg>',
    check: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9"><path d="M5 12.5l4.2 4.3L19 7"/></svg>',
    ext: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M14 5h5v5M19 5l-8 8"/><path d="M18 13v5a1.5 1.5 0 0 1-1.5 1.5h-10A1.5 1.5 0 0 1 5 18V8a1.5 1.5 0 0 1 1.5-1.5H11"/></svg>',
    clock: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg>',
    sun: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.4M12 19.1v2.4M4.4 4.4l1.7 1.7M17.9 17.9l1.7 1.7M2.5 12h2.4M19.1 12h2.4M4.4 19.6l1.7-1.7M17.9 6.1l1.7-1.7"/></svg>',
    moon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M20 14.2A8 8 0 1 1 9.8 4 6.4 6.4 0 0 0 20 14.2z"/></svg>',
    spark: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3l1.7 5.1L19 10l-5.3 1.9L12 17l-1.7-5.1L5 10l5.3-1.9z"/></svg>'
  };

  /* ---- helpers ---- */
  function qs(s, r) { return (r || doc).querySelector(s); }
  function norm(s) { return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function readMin(w) { return Math.max(1, Math.round(w / 200)); }
  function pad3(n) { var s = String(n); while (s.length < 3) s = '0' + s; return s; }
  function slugify(s) {
    var out = s.toLowerCase();
    try { out = out.replace(/[^\p{L}\p{N}\s-]/gu, ''); }
    catch (e) { out = out.replace(/[^a-z0-9\s-]/g, ''); }
    return out.trim().replace(/\s+/g, '-').replace(/-+/g, '-') || 'bagian';
  }

  /* ---- element refs ---- */
  var main = qs('#main'), tocEl = qs('#toc'),
      searchInput = qs('#searchInput'), searchBox = qs('#searchBox'),
      chipsEl = qs('#chips'), yearSel = qs('#yearSel'), sbCount = qs('#sbCount'),
      progressBar = qs('#progressBar');

  /* ---- state ---- */
  var state = { path: null, heading: '', q: '', tema: {}, thn: '', ordered: [] };
  var _spy = null, _reveal = null, _rafScroll = false;

  /* ================= SEARCH ================= */
  function ensureHay() {
    DATA.forEach(function (e) {
      if (e._h) return;
      e._h = { nTitle: norm(e.title), nTheme: norm(e.theme), nMd: norm(e.md) };
    });
  }
  function scoreEntry(e, terms) {
    var s = 0;
    for (var i = 0; i < terms.length; i++) {
      var t = terms[i], hit = 0;
      if (e._h.nTitle.indexOf(t) !== -1) { s += 5; hit = 1; }
      if (e._h.nTheme.indexOf(t) !== -1) { s += 3; hit = 1; }
      if (e._h.nMd.indexOf(t) !== -1) { s += 1; hit = 1; }
      if (!hit) return -1; // semua term wajib ada (AND)
    }
    return s;
  }

  /* ================= FILTER + LIST ================= */
  function computeList() {
    ensureHay();
    var terms = norm(state.q).split(/\s+/).filter(Boolean);
    var temaKeys = Object.keys(state.tema);
    var scored = [];
    DATA.forEach(function (e) {
      if (temaKeys.length && !state.tema[e.theme]) return;
      if (state.thn && String(e.year) !== state.thn) return;
      var sc = 0;
      if (terms.length) { sc = scoreEntry(e, terms); if (sc < 0) return; }
      scored.push({ e: e, sc: sc });
    });
    if (terms.length) {
      scored.sort(function (a, b) {
        if (b.sc !== a.sc) return b.sc - a.sc;
        return a.e.num - b.e.num;
      });
    } else {
      scored.sort(function (a, b) { return a.e.num - b.e.num; });
    }
    state.ordered = scored.map(function (x) { return x.e; });
    return state.q.toLowerCase().split(/\s+/).filter(Boolean);
  }

  function markInto(node, text, terms) {
    if (!terms.length) { node.appendChild(doc.createTextNode(text)); return; }
    var low = text.toLowerCase(), ranges = [];
    terms.forEach(function (t) { if (!t) return; var i = 0; while ((i = low.indexOf(t, i)) !== -1) { ranges.push([i, i + t.length]); i += t.length; } });
    if (!ranges.length) { node.appendChild(doc.createTextNode(text)); return; }
    ranges.sort(function (a, b) { return a[0] - b[0]; });
    var merged = [];
    ranges.forEach(function (r) { var l = merged[merged.length - 1]; if (l && r[0] <= l[1]) l[1] = Math.max(l[1], r[1]); else merged.push([r[0], r[1]]); });
    var pos = 0;
    merged.forEach(function (r) {
      if (r[0] > pos) node.appendChild(doc.createTextNode(text.slice(pos, r[0])));
      var m = doc.createElement('mark'); m.textContent = text.slice(r[0], r[1]); node.appendChild(m); pos = r[1];
    });
    if (pos < text.length) node.appendChild(doc.createTextNode(text.slice(pos)));
  }

  function renderList() {
    var terms = computeList();
    syncFilterUI();
    renderCatalogue(terms);
  }

  /* ================= KATALOG (tabel indeks di beranda) ================= */
  var catSort = { key: 'num', dir: 1 };
  function renderCatalogue(terms) {
    var body = qs('#catBody');
    if (!body) return;
    var special = [], rest = [];
    state.ordered.forEach(function (e) { (e.special ? special : rest).push(e); });
    var k = catSort.key, d = catSort.dir;
    rest.sort(function (a, b) {
      var r;
      if (k === 'title') r = a.title.localeCompare(b.title, 'id');
      else if (k === 'theme') r = a.theme.localeCompare(b.theme, 'id') || (a.num - b.num);
      else if (k === 'year') r = (a.year - b.year) || (a.num - b.num);
      else if (k === 'min') r = (a.words - b.words) || (a.num - b.num);
      else r = a.num - b.num;
      return r * d;
    });
    var items = special.concat(rest);
    syncCatHead();
    body.innerHTML = '';
    var empty = qs('#catEmpty');
    if (empty) empty.hidden = items.length > 0;
    if (!items.length) return;
    var frag = doc.createDocumentFragment();
    items.forEach(function (e) { frag.appendChild(catRowEl(e, terms)); });
    body.appendChild(frag);
  }
  function catRowEl(e, terms) {
    var tr = doc.createElement('tr');
    tr.dataset.id = e.id;
    tr.tabIndex = 0;
    if (e.special) tr.className = 'special';
    var num = doc.createElement('td'); num.className = 'c-num'; num.textContent = e.special ? '§' : e.id;
    var title = doc.createElement('td'); title.className = 'c-title';
    markInto(title, e.title, terms);
    var theme = doc.createElement('td'); theme.className = 'c-theme';
    theme.style.setProperty('--tc', tColor(e.theme));
    var dot = doc.createElement('span'); dot.className = 'cd';
    theme.appendChild(dot);
    theme.appendChild(doc.createTextNode(e.theme));
    var yr = doc.createElement('td'); yr.className = 'c-year'; yr.textContent = e.special ? '—' : e.year;
    var min = doc.createElement('td'); min.className = 'c-min'; min.textContent = readMin(e.words) + ' mnt';
    tr.appendChild(num); tr.appendChild(title); tr.appendChild(theme); tr.appendChild(yr); tr.appendChild(min);
    return tr;
  }
  function syncCatHead() {
    var ths = doc.querySelectorAll('.cat-table th[data-sort]');
    for (var i = 0; i < ths.length; i++) {
      var on = ths[i].dataset.sort === catSort.key;
      ths[i].classList.toggle('sorted', on);
      var arr = ths[i].querySelector('.arr');
      if (arr) arr.textContent = on ? (catSort.dir === 1 ? '↑' : '↓') : '';
    }
  }

  /* ================= CHIPS + YEAR ================= */
  function buildChips() {
    var themes = Object.keys(META.themeCounts).sort(function (a, b) { return META.themeCounts[b] - META.themeCounts[a]; });
    chipsEl.innerHTML = '';
    themes.forEach(function (t) {
      var c = doc.createElement('button');
      c.className = 'chip'; c.type = 'button'; c.dataset.tema = t;
      c.setAttribute('aria-pressed', 'false');
      c.style.setProperty('--tc', tColor(t));
      c.innerHTML = '<span class="cd"></span>' + esc(t) + ' <span style="color:var(--ink-3);font-family:var(--mono);font-size:10px">' + META.themeCounts[t] + '</span>';
      c.addEventListener('click', function () {
        if (state.tema[t]) delete state.tema[t]; else state.tema[t] = 1;
        pushFilter(); renderList();
      });
      chipsEl.appendChild(c);
    });
    var toggle = qs('#chipsToggle');
    var collapsedLabel = '+ Semua ' + themes.length + ' tema';
    toggle.textContent = collapsedLabel;
    toggle.addEventListener('click', function () {
      var ex = chipsEl.classList.toggle('expanded');
      toggle.setAttribute('aria-expanded', ex ? 'true' : 'false');
      toggle.textContent = ex ? '− Ringkas' : collapsedLabel;
    });
  }
  function buildYears() {
    var ys = Object.keys(META.yearCounts).map(Number).sort(function (a, b) { return a - b; });
    var opts = '<option value="">Semua tahun</option>';
    ys.forEach(function (y) { opts += '<option value="' + y + '">' + y + ' (' + META.yearCounts[y] + ')</option>'; });
    yearSel.innerHTML = opts;
    yearSel.addEventListener('change', function () { state.thn = yearSel.value; pushFilter(); renderList(); });
  }
  function syncFilterUI() {
    var chips = chipsEl.querySelectorAll('.chip[data-tema]');
    for (var i = 0; i < chips.length; i++) {
      chips[i].setAttribute('aria-pressed', state.tema[chips[i].dataset.tema] ? 'true' : 'false');
    }
    if (yearSel.value !== (state.thn || '')) yearSel.value = state.thn || '';
    if (searchInput.value !== state.q && doc.activeElement !== searchInput) searchInput.value = state.q;
    searchBox.classList.toggle('has-val', !!state.q);
    var active = state.q || state.thn || Object.keys(state.tema).length;
    sbCount.textContent = active
      ? (state.ordered.length + ' dari ' + META.total + ' entri')
      : (META.total + ' entri · ' + META.themeCount + ' tema');
  }

  /* ================= HASH / ROUTER ================= */
  function hashQuery() {
    var p = [];
    if (state.q) p.push('q=' + encodeURIComponent(state.q));
    var tk = Object.keys(state.tema);
    if (tk.length) p.push('tema=' + encodeURIComponent(tk.join('|')));
    if (state.thn) p.push('thn=' + encodeURIComponent(state.thn));
    return p.length ? '?' + p.join('&') : '';
  }
  function pushFilter() {
    var base = '#/' + (state.path && state.path !== '/' ? state.path : '');
    var url = base + hashQuery();
    if (location.hash !== url) history.replaceState(null, '', url);
    syncFilterUI();
  }
  function parseHash() {
    var raw = location.hash.replace(/^#/, '');
    if (raw.indexOf('/') === 0) raw = raw.slice(1);
    var hParts = raw.split('#'); // deep-link heading setelah '#'
    var heading = hParts[1] || '';
    var pq = hParts[0].split('?');
    var pth; try { pth = decodeURIComponent(pq[0] || ''); } catch (e) { pth = pq[0] || ''; }
    var query = new URLSearchParams(pq[1] || '');
    return { path: pth, query: query, heading: heading };
  }
  function applyQueryToState(query) {
    state.q = query.get('q') || '';
    state.thn = query.get('thn') || '';
    state.tema = {};
    var tm = query.get('tema');
    if (tm) tm.split('|').forEach(function (t) { if (t) state.tema[t] = 1; });
  }

  function route() {
    var r = parseHash();
    var prevPath = state.path;
    var samePage = (prevPath === r.path) && r.path !== '' && r.path != null;
    applyQueryToState(r.query);
    state.path = r.path;
    state.heading = r.heading;

    if (samePage) {
      renderList();
      if (r.heading) scrollToHeading(r.heading);
      return;
    }

    var isHome = (r.path === '' || r.path === '/');
    doc.body.classList.toggle('on-home', isHome);
    doc.body.classList.toggle('on-entry', !isHome);
    renderList();
    teardownObservers();
    if (isHome) viewHome();
    else if (byId[r.path]) viewEntry(byId[r.path]);
    else view404(r.path);

    window.scrollTo(0, 0);
    updateProgress();
    if (r.heading) setTimeout(function () { scrollToHeading(r.heading); }, 50);
    closeDrawer();
    try { main.focus({ preventScroll: true }); } catch (e) {}
  }

  function scrollToHeading(slug) {
    var t = doc.getElementById(slug);
    if (t) window.scrollTo({ top: t.getBoundingClientRect().top + window.pageYOffset - 74, behavior: 'smooth' });
  }

  /* ================= CONTENT ENHANCE ================= */
  function enhance(container, e) {
    container.querySelectorAll('table').forEach(function (tbl) {
      if (tbl.parentElement && tbl.parentElement.classList.contains('table-wrap')) return;
      var w = doc.createElement('div'); w.className = 'table-wrap';
      tbl.parentNode.insertBefore(w, tbl); w.appendChild(tbl);
    });
    container.querySelectorAll('a[href]').forEach(function (a) {
      var href = a.getAttribute('href') || '';
      if (href.indexOf('#') === 0) return;
      var dec; try { dec = decodeURIComponent(href); } catch (x) { dec = href; }
      var m = dec.match(/(?:^|\/)(\d{3})\s-\s.*\.md$/i);
      if (m && !/^https?:/i.test(href)) {
        a.setAttribute('href', '#/' + m[1]);
        a.classList.add('entry-link');
      } else {
        a.setAttribute('target', '_blank');
        a.setAttribute('rel', 'noopener noreferrer');
      }
    });
    var used = {}, heads = [];
    container.querySelectorAll('h2, h3').forEach(function (h) {
      var base = slugify(h.textContent);
      var slug = base, n = 2;
      while (used[slug]) slug = base + '-' + (n++);
      used[slug] = 1; h.id = slug;
      var an = doc.createElement('a');
      an.className = 'anchor'; an.href = '#/' + e.id + '#' + slug; an.textContent = '#';
      an.setAttribute('aria-label', 'Tautan ke bagian ini');
      h.insertBefore(an, h.firstChild);
      heads.push({ level: h.tagName === 'H2' ? 2 : 3, text: h.textContent.replace(/^#/, '').trim(), id: slug, el: h });
    });
    return heads;
  }

  /* ================= TOC + SCROLL SPY ================= */
  function buildTOC(heads, e) {
    if (heads.length < 2) { tocEl.innerHTML = ''; return; }
    var html = '<div class="toc-inner"><div class="toc-h">Isi</div>';
    heads.forEach(function (h) {
      html += '<a href="#/' + e.id + '#' + h.id + '" class="lvl-' + h.level + '" data-tid="' + h.id + '">' + esc(h.text) + '</a>';
    });
    html += '</div>';
    tocEl.innerHTML = html;
  }
  function spy(heads) {
    if (heads.length < 2 || !('IntersectionObserver' in window)) return;
    var links = {};
    tocEl.querySelectorAll('a[data-tid]').forEach(function (a) { links[a.dataset.tid] = a; });
    var visible = {};
    _spy = new IntersectionObserver(function (ents) {
      ents.forEach(function (en) { visible[en.target.id] = en.isIntersecting; });
      var current = null;
      for (var i = 0; i < heads.length; i++) { if (visible[heads[i].id]) { current = heads[i].id; break; } }
      if (!current) {
        for (var j = heads.length - 1; j >= 0; j--) {
          if (heads[j].el.getBoundingClientRect().top < 120) { current = heads[j].id; break; }
        }
      }
      Object.keys(links).forEach(function (k) { links[k].classList.toggle('active', k === current); });
    }, { rootMargin: '-15% 0px -72% 0px', threshold: 0 });
    heads.forEach(function (h) { _spy.observe(h.el); });
  }

  /* ================= VIEWS ================= */
  function entryHeader(e) {
    var chip = '<span class="t-chip" style="--tc:' + tColor(e.theme) + '"><span class="cd"></span>' + esc(e.theme) + '</span>';
    var eyebrow = e.special
      ? '<span>SINTESIS</span><span class="sep">·</span>' + chip
      : '<span>ENTRI ' + e.id + ' / ' + META.total + '</span><span class="sep">·</span><span>' + e.year + '</span><span class="sep">·</span>' + chip;
    var meta = '<span class="readtime">' + ICON.clock + readMin(e.words) + ' menit baca</span>';
    if (e.bib) meta += '<button class="meta-btn" data-copy="' + esc(e.bib) + '">' + ICON.copy + '<span>' + esc(e.bib) + '</span></button>';
    meta += '<button class="meta-btn" data-copy-link="' + e.id + '">' + ICON.copy + 'Salin tautan</button>';
    if (e.scholar) meta += '<a class="meta-link" href="' + esc(e.scholar) + '" target="_blank" rel="noopener noreferrer">' + ICON.ext + 'Scholar</a>';
    if (e.semantic) meta += '<a class="meta-link" href="' + esc(e.semantic) + '" target="_blank" rel="noopener noreferrer">' + ICON.ext + 'Semantic Scholar</a>';
    return '<a class="back-link" href="#/' + hashQuery() + '">' + ICON.arrowL + 'Katalog</a>' +
      '<header class="eh rv in"><div class="eyebrow">' + eyebrow + '</div><h1>' + esc(e.title) + '</h1><div class="eh-meta">' + meta + '</div></header>';
  }

  function prevNext(e) {
    if (e.special) {
      var first = ENTRIES[0];
      return '<nav class="pn"><span class="empty"></span>' + (first ? pnCard('next', first) : '<span class="empty"></span>') + '</nav>';
    }
    var list = state.ordered.filter(function (x) { return !x.special; });
    var idx = list.findIndex(function (x) { return x.id === e.id; });
    if (idx === -1) { list = ENTRIES; idx = list.findIndex(function (x) { return x.id === e.id; }); }
    var prev = list[idx - 1], next = list[idx + 1];
    return '<nav class="pn">' +
      (prev ? pnCard('prev', prev) : '<span class="empty"></span>') +
      (next ? pnCard('next', next) : '<span class="empty"></span>') + '</nav>';
  }
  function pnCard(dir, e) {
    var label = dir === 'prev' ? (ICON.arrowL + 'Sebelumnya') : ('Berikutnya' + ICON.arrowR);
    return '<a class="pn-' + dir + '" href="#/' + e.id + hashQuery() + '">' +
      '<span class="pn-dir">' + label + '</span>' +
      '<span class="pn-title">' + esc(e.title) + '</span></a>';
  }

  function viewEntry(e) {
    var art = doc.createElement('div'); art.className = 'article';
    art.innerHTML = window.marked.parse(e.md);
    var heads = enhance(art, e);
    main.innerHTML = '<div class="wrap"></div>';
    var wrap = main.querySelector('.wrap');
    wrap.insertAdjacentHTML('beforeend', entryHeader(e));
    wrap.appendChild(art);
    wrap.insertAdjacentHTML('beforeend', prevNext(e));
    buildTOC(heads, e); spy(heads);
    try { localStorage.setItem('rp-last', e.id); } catch (x) {}
    doc.title = e.title + ' · Ruang Baca Riset';
  }

  function view404(id) {
    tocEl.innerHTML = '';
    main.innerHTML = '<div class="wrap"><div class="nf rv in"><div class="code">404 · ENTRI TIDAK DITEMUKAN</div>' +
      '<h1>Entri "' + esc(id) + '" tidak ada</h1>' +
      '<p>Nomor entri berkisar 001–' + pad3(META.total) + '. Periksa kembali tautannya, atau telusuri lewat daftar di samping.</p>' +
      '<a class="btn btn-solid" href="#/">' + ICON.arrowL + 'Kembali ke Beranda</a></div></div>';
    doc.title = 'Tidak ditemukan · Ruang Baca Riset';
  }

  function viewHome() {
    tocEl.innerHTML = '';
    doc.title = 'Ruang Baca Riset · YOLO / RGB / RGB-D';
    var h = '<div class="wrap home">';
    h += '<section class="hero">' +
      '<div class="eb rv"><span class="dot"></span>Tinjauan Pustaka · ' + META.minYear + '–' + META.maxYear + '</div>' +
      '<h1 class="rv" style="--i:1">Ruang Baca Riset<br><span class="muted">YOLO · RGB · RGB-D</span></h1>' +
      '<p class="lede rv" style="--i:2">Ruang baca digital untuk ' + META.total + ' telaah makalah deteksi objek dan fusi RGB+Depth (' + META.minYear + '–' + META.maxYear + '), plus satu dokumen sintesis lintas makalah.</p>' +
      '<div class="cta-row rv" style="--i:3">' +
      '<a class="btn btn-solid" href="#/temuan">' + ICON.spark + 'Mulai dari Temuan' + ICON.arrowR + '</a>' +
      '<button class="btn btn-ghost" id="exploreBtn" type="button">' + ICON.book + 'Jelajahi katalog ' + META.total + ' entri</button>' +
      '</div>' + resumeHtml() + '</section>';

    h += sectionH('Sekilas angka', 'ringkasan korpus');
    h += '<div class="stats rv">' +
      statCell(META.total, 'Entri telaah') +
      statCell(META.themeCount, 'Tema klaster') +
      statCell(Object.keys(META.yearCounts).length, 'Tahun ' + META.minYear + '–' + META.maxYear) +
      statCell('±' + META.totalHours, 'Jam total baca') + '</div>';

    h += sectionH('Sebaran per tahun', 'klik batang untuk menyaring');
    h += timelineHtml();

    h += sectionH('Peta tema', META.themeCount + ' klaster · klik untuk menyaring');
    h += '<div class="tlist rv">' + themeRowsHtml() + '</div>';

    h += '<span id="katalog"></span>' + sectionH('Katalog', 'klik kolom untuk mengurutkan');
    h += catalogueHtml();

    h += sectionH('Mulai di sini', 'jalur baca terkurasi');
    h += '<div class="plist">' + pathsHtml() + '</div>';

    h += footHtml();
    h += '</div>';
    main.innerHTML = h;

    renderList();

    main.querySelectorAll('[data-year]').forEach(function (el) {
      el.addEventListener('click', function () { goFilter({ thn: el.dataset.year }); });
    });
    main.querySelectorAll('[data-theme-card]').forEach(function (el) {
      el.addEventListener('click', function () { goFilter({ tema: el.dataset.themeCard }); });
    });
    main.querySelectorAll('[data-year]').forEach(function (el) {
      el.addEventListener('keydown', function (ev) {
        if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); el.click(); }
      });
    });
    var exp = qs('#exploreBtn');
    if (exp) exp.addEventListener('click', function () {
      var t = qs('#katalog'); if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
    var cat = qs('.cat');
    if (cat) {
      cat.addEventListener('click', function (ev) {
        var th = ev.target.closest ? ev.target.closest('th[data-sort]') : null;
        if (th) {
          var k = th.dataset.sort;
          if (catSort.key === k) catSort.dir *= -1; else { catSort.key = k; catSort.dir = 1; }
          renderList();
          return;
        }
        var tr = ev.target.closest ? ev.target.closest('tr[data-id]') : null;
        if (tr) location.hash = '#/' + tr.dataset.id + hashQuery();
      });
      cat.addEventListener('keydown', function (ev) {
        if (ev.key !== 'Enter' && ev.key !== ' ') return;
        var tr = ev.target.closest ? ev.target.closest('tr[data-id]') : null;
        if (tr) { ev.preventDefault(); location.hash = '#/' + tr.dataset.id + hashQuery(); }
      });
    }

    setupReveal();
  }

  function catalogueHtml() {
    return '<div class="cat rv"><table class="cat-table"><thead><tr>' +
      '<th data-sort="num">No<span class="arr"></span></th>' +
      '<th data-sort="title">Judul<span class="arr"></span></th>' +
      '<th data-sort="theme">Tema<span class="arr"></span></th>' +
      '<th data-sort="year">Tahun<span class="arr"></span></th>' +
      '<th data-sort="min" style="text-align:right">Baca<span class="arr"></span></th>' +
      '</tr></thead><tbody id="catBody"></tbody></table>' +
      '<div class="cat-empty" id="catEmpty" hidden>Tak ada entri yang cocok. Coba ubah kata kunci atau tekan Reset.</div></div>';
  }

  function goFilter(f) {
    state.q = ''; state.tema = {}; state.thn = '';
    if (f.tema) state.tema[f.tema] = 1;
    if (f.thn) state.thn = f.thn;
    if (location.hash !== '#/' + hashQuery()) history.replaceState(null, '', '#/' + hashQuery());
    closeDrawer();
    renderList();
    var k = qs('#katalog');
    if (k) k.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function resumeHtml() {
    var last; try { last = localStorage.getItem('rp-last'); } catch (x) { last = null; }
    if (!last || !byId[last]) return '';
    var e = byId[last];
    return '<div class="resume rv" style="--i:4"><a href="#/' + e.id + '">' +
      '<span class="k">Lanjutkan membaca</span>' +
      '<span class="num">' + (e.special ? '§' : e.id) + '</span>' +
      '<span class="t">' + esc(e.title) + '</span>' + ICON.arrowR + '</a></div>';
  }
  function sectionH(t, sub) {
    return '<div class="section-h rv"><h2>' + esc(t) + '</h2><span class="sub">' + esc(sub) + '</span><span class="line"></span></div>';
  }
  function statCell(n, l) {
    return '<div class="stat"><div class="n">' + esc(String(n)) + '</div><div class="l">' + esc(l) + '</div></div>';
  }
  function timelineHtml() {
    var ys = [];
    for (var y = META.minYear; y <= META.maxYear; y++) ys.push(y);
    var max = 0; ys.forEach(function (y) { max = Math.max(max, META.yearCounts[y] || 0); });
    var cols = ys.map(function (y) {
      var c = META.yearCounts[y] || 0;
      var hpct = c ? Math.max(4, Math.round(c / max * 100)) : 0;
      // Tahun kosong tetap digambar supaya jeda terlihat, tapi tidak bisa diklik:
      // menyaringnya selalu berujung katalog kosong.
      var attrs = c
        ? ' data-year="' + y + '" role="button" tabindex="0" aria-label="Saring tahun ' + y + ': ' + c + ' entri"'
        : '';
      return '<div class="tl-col' + (c ? '' : ' empty') + '"' + attrs + ' title="' + y + ': ' + c + ' entri">' +
        '<div class="tl-bar" style="height:' + hpct + '%"><span class="tip">' + c + ' entri</span></div>' +
        '<span class="tl-yr">' + y + '</span></div>';
    }).join('');
    return '<div class="timeline rv"><div class="tl-bars">' + cols + '</div></div>';
  }
  function themeRowsHtml() {
    var themes = Object.keys(META.themeCounts).sort(function (a, b) { return META.themeCounts[b] - META.themeCounts[a]; });
    var max = META.themeCounts[themes[0]] || 1;
    return themes.map(function (t) {
      var samples = ENTRIES.filter(function (e) { return e.theme === t; }).slice(0, 2);
      var txt = samples.map(function (e) { return e.title; }).join(' · ');
      var w = Math.max(3, Math.round(META.themeCounts[t] / max * 100));
      return '<button class="trow" data-theme-card="' + esc(t) + '" style="--tc:' + tColor(t) + '" aria-label="Saring tema ' + esc(t) + '">' +
        '<span class="cd"></span><span class="trow-name">' + esc(t) + '</span>' +
        '<span class="trow-samples">' + esc(txt) + '</span>' +
        '<span class="trow-bar"><span style="width:' + w + '%"></span></span>' +
        '<span class="trow-count">' + META.themeCounts[t] + '</span></button>';
    }).join('');
  }
  function pathsHtml() {
    return PATHS.map(function (p, i) {
      var chips = p.ids.map(function (id) {
        var e = byId[id]; if (!e) return '';
        return '<a class="pchip" href="#/' + id + '"><span class="pn2">' + id + '</span>' + esc(e.title) + '</a>';
      }).join('');
      var mins = p.ids.reduce(function (s, id) { return s + (byId[id] ? readMin(byId[id].words) : 0); }, 0);
      return '<section class="path rv" style="--i:' + (i % 2) + '">' +
        '<span class="path-num"><b>' + p.ids.length + '</b>entri<i>±' + mins + ' mnt</i></span>' +
        '<div class="path-body"><h3>' + esc(p.name) + '<span class="ptag">' + esc(p.tag) + '</span></h3>' +
        '<p>' + esc(p.desc) + '</p><div class="pchips">' + chips + '</div></div></section>';
    }).join('');
  }
  function footHtml() {
    return '<footer class="foot rv"><span>' + META.total + ' entri · ' + META.themeCount + ' tema · dibangun ' + esc(META.built) + '</span>' +
      '<span class="fspacer"></span>' +
      '<span>Regenerasi: <code>node build.js</code></span>' +
      '<a href="tinjauan-pustaka.tex" target="_blank" rel="noopener">tinjauan-pustaka.tex</a>' +
      '<a href="references.bib" target="_blank" rel="noopener">references.bib</a></footer>';
  }

  /* ================= COPY ================= */
  function flashCopy(btn, txt) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(txt).catch(function () { fallbackCopy(txt); });
    } else { fallbackCopy(txt); }
    var orig = btn.innerHTML;
    btn.classList.add('ok');
    btn.innerHTML = ICON.check + '<span>Tersalin</span>';
    setTimeout(function () { btn.classList.remove('ok'); btn.innerHTML = orig; }, 1200);
  }
  function fallbackCopy(txt) {
    var ta = doc.createElement('textarea'); ta.value = txt; ta.style.position = 'fixed'; ta.style.opacity = '0';
    doc.body.appendChild(ta); ta.focus(); ta.select(); try { doc.execCommand('copy'); } catch (x) {} doc.body.removeChild(ta);
  }
  main.addEventListener('click', function (ev) {
    var b = ev.target.closest ? ev.target.closest('[data-copy], [data-copy-link]') : null;
    if (!b) return;
    if (b.getAttribute('data-copy') != null) flashCopy(b, b.getAttribute('data-copy'));
    else if (b.getAttribute('data-copy-link') != null) {
      var url = location.origin + location.pathname + location.search + '#/' + b.getAttribute('data-copy-link');
      flashCopy(b, url);
    }
  });

  /* ================= PROGRESS ================= */
  function updateProgress() {
    var el = doc.documentElement;
    var hgt = el.scrollHeight - el.clientHeight;
    var p = hgt > 0 ? Math.min(1, window.pageYOffset / hgt) : 0;
    progressBar.style.transform = 'scaleX(' + p.toFixed(4) + ')';
  }
  window.addEventListener('scroll', function () {
    if (_rafScroll) return; _rafScroll = true;
    requestAnimationFrame(function () { updateProgress(); _rafScroll = false; });
  }, { passive: true });

  /* ================= REVEAL ================= */
  function setupReveal() {
    if (!('IntersectionObserver' in window)) { main.querySelectorAll('.rv').forEach(function (el) { el.classList.add('in'); }); return; }
    if (_reveal) _reveal.disconnect();
    _reveal = new IntersectionObserver(function (ents, obs) {
      ents.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); obs.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: .05 });
    main.querySelectorAll('.rv:not(.in)').forEach(function (el) { _reveal.observe(el); });
  }
  function teardownObservers() {
    if (_spy) { _spy.disconnect(); _spy = null; }
    if (_reveal) { _reveal.disconnect(); _reveal = null; }
  }

  /* ================= THEME ================= */
  function currentTheme() { return doc.documentElement.getAttribute('data-theme') || 'light'; }
  function setTheme(t) {
    doc.documentElement.setAttribute('data-theme', t);
    try { localStorage.setItem('rp-theme', t); } catch (x) {}
    qs('#themeBtn').innerHTML = t === 'dark' ? ICON.sun : ICON.moon;
  }
  function toggleTheme() { setTheme(currentTheme() === 'dark' ? 'light' : 'dark'); }

  /* ================= DRAWER ================= */
  function isMobile() { return window.matchMedia('(max-width:980px)').matches; }
  function openDrawer() { if (isMobile()) { doc.body.classList.add('drawer-open'); qs('#menuBtn').setAttribute('aria-expanded', 'true'); } }
  function closeDrawer() { doc.body.classList.remove('drawer-open'); qs('#menuBtn').setAttribute('aria-expanded', 'false'); }
  function toggleDrawer() { if (doc.body.classList.contains('drawer-open')) closeDrawer(); else openDrawer(); }
  function focusSearch() {
    openDrawer();
    var delay = 60;
    if (!isMobile() && doc.body.classList.contains('on-entry')) {
      // Sidebar tersembunyi di mode entri: pulang dulu ke katalog, baru fokus.
      location.hash = '#/' + hashQuery();
      delay = 150;
    }
    setTimeout(function () { searchInput.focus(); searchInput.select(); }, delay);
  }

  /* ================= HELP MODAL ================= */
  function openHelp() { qs('#helpModal').classList.add('open'); }
  function closeHelp() { qs('#helpModal').classList.remove('open'); }

  /* ================= EVENTS ================= */
  var _searchTimer = null;
  searchInput.addEventListener('input', function () {
    searchBox.classList.toggle('has-val', !!searchInput.value);
    clearTimeout(_searchTimer);
    _searchTimer = setTimeout(function () {
      state.q = searchInput.value.trim();
      pushFilter(); renderList();
    }, 120);
  });
  qs('#searchClear').addEventListener('click', function () {
    searchInput.value = ''; state.q = ''; searchBox.classList.remove('has-val');
    pushFilter(); renderList(); searchInput.focus();
  });
  qs('#resetBtn').addEventListener('click', function () {
    state.q = ''; state.tema = {}; state.thn = '';
    searchInput.value = ''; chipsEl.classList.remove('expanded');
    pushFilter(); renderList();
  });
  qs('#themeBtn').addEventListener('click', toggleTheme);
  qs('#menuBtn').addEventListener('click', toggleDrawer);
  qs('#scrim').addEventListener('click', closeDrawer);
  qs('#helpBtn').addEventListener('click', openHelp);
  qs('#searchTrigger').addEventListener('click', focusSearch);
  qs('.skip-link').addEventListener('click', function (ev) {
    ev.preventDefault(); window.scrollTo(0, 0);
    try { main.focus({ preventScroll: true }); } catch (e) {}
  });
  qs('#helpModal').addEventListener('click', function (ev) { if (ev.target.hasAttribute('data-close')) closeHelp(); });

  doc.addEventListener('keydown', function (ev) {
    var tag = (ev.target.tagName || '').toLowerCase();
    var typing = tag === 'input' || tag === 'select' || tag === 'textarea';
    if ((ev.key === '/' && !typing) || ((ev.ctrlKey || ev.metaKey) && (ev.key === 'k' || ev.key === 'K'))) {
      ev.preventDefault(); focusSearch(); return;
    }
    if (ev.key === 'Escape') {
      if (qs('#helpModal').classList.contains('open')) { closeHelp(); return; }
      if (doc.body.classList.contains('drawer-open')) { closeDrawer(); return; }
      if (typing && ev.target === searchInput) { searchInput.value = ''; state.q = ''; searchBox.classList.remove('has-val'); pushFilter(); renderList(); searchInput.blur(); }
      return;
    }
    if (typing) return;
    if (ev.key === 't' || ev.key === 'T') { toggleTheme(); return; }
    if (ev.key === '?') { openHelp(); return; }
    if (ev.key === 'ArrowLeft' || ev.key === 'ArrowRight') {
      var e = byId[state.path]; if (!e || e.special) return;
      var list = state.ordered.filter(function (x) { return !x.special; });
      var idx = list.findIndex(function (x) { return x.id === e.id; });
      if (idx === -1) { list = ENTRIES; idx = list.findIndex(function (x) { return x.id === e.id; }); }
      var target = ev.key === 'ArrowLeft' ? list[idx - 1] : list[idx + 1];
      if (target) location.hash = '#/' + target.id + hashQuery();
    }
  });

  window.addEventListener('hashchange', route);

  /* ================= INIT ================= */
  (function init() {
    var saved; try { saved = localStorage.getItem('rp-theme'); } catch (x) { saved = null; }
    if (!saved) saved = (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) ? 'dark' : 'light';
    setTheme(saved);
    buildChips(); buildYears();
    if (!location.hash) { try { location.replace('#/'); } catch (e) { location.hash = '#/'; } }
    route();
  })();
}

/* ================================================================== *
 * Rakit halaman
 * ================================================================== */
const runtimeScript = ';(' + RUNTIME.toString() + ')();';

const PAGE = `<!doctype html>
<html lang="id" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<meta name="description" content="Ruang baca digital untuk ${META.total} telaah makalah deteksi objek YOLO dan fusi RGB+Depth (${META.minYear}-${META.maxYear}), plus sintesis lintas makalah.">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#FAF9F6">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#171613">
<meta property="og:title" content="Ruang Baca Riset &middot; YOLO / RGB / RGB-D">
<meta property="og:description" content="Ruang baca digital untuk telaah makalah deteksi objek dan fusi RGB+Depth, plus sintesis lintas makalah.">
<meta property="og:type" content="website">
<meta property="og:locale" content="id_ID">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='15' fill='%23FAF9F6'/%3E%3Crect x='2' y='2' width='60' height='60' rx='13' fill='none' stroke='%23D4D0C4' stroke-width='3'/%3E%3Ccircle cx='32' cy='32' r='11' fill='%23A03028'/%3E%3C/svg%3E">
<title>Ruang Baca Riset &middot; YOLO / RGB / RGB-D</title>
<script>(function(){try{var t=localStorage.getItem('rp-theme');if(!t)t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';document.documentElement.setAttribute('data-theme',t);}catch(e){}})();</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">
<style>${CSS}</style>
</head>
<body>
${SHELL}
<script>${markedSrc}
</script>
<script>${dataScript}
</script>
<script>${runtimeScript}
</script>
</body>
</html>`;

fs.writeFileSync(OUT_PATH, PAGE, 'utf8');
const bytes = Buffer.byteLength(PAGE, 'utf8');
console.log('\nBerkas ditulis : index.html');
console.log('Ukuran         : ' + (bytes / 1048576).toFixed(2) + ' MB (' + bytes.toLocaleString('en-US') + ' bytes)');
console.log('Selesai. Buka index.html di browser atau jalankan `npx serve .`\n');
