#!/usr/bin/env node
'use strict';

/**
 * Rakit index.html dari dua koleksi Markdown, dokumen riset, dan aset site/.
 * Ringkasan serta teks sumber Scopus tetap diambil dari berkas asal saat dibuka.
 * Jalankan `node site/build.js` atau tambahkan `--dry` untuk melihat laporan.
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const ENTRI_DIR = path.join(ROOT, 'literature', 'entries');
const MARKED_PATH = path.join(__dirname, 'vendor', 'marked.min.js');
const OUT_PATH = path.join(ROOT, 'index.html');
const DRY = process.argv.includes('--dry');

const MARKED_VERSION = '12.0.0';
const { methodsInTitle } = require('./discovery.js');

const SPECIAL_DOCS = [
  {
    id: 'temuan',
    kind: 'sintesis',
    label: 'SINTESIS',
    marker: '§',
    title: 'Temuan Riset: Sintesis Lintas Makalah',
    theme: 'Sintesis',
    file: 'literature/synthesis.md',
    sourceDir: 'literature',
    desc: 'Sintesis lintas makalah koleksi deteksi objek dan RGB-D.'
  },
  {
    id: 'laporan-eksperimen',
    kind: 'laporan',
    label: 'LAPORAN EKSPERIMEN',
    marker: '¶',
    title: 'Laporan Eksperimen: Deteksi & Penghitungan Tandan Sawit',
    theme: 'Eksperimen',
    file: 'experiments/LAPORAN-EKSPERIMEN.md',
    sourceDir: 'experiments',
    desc: 'Cuplikan terkurasi eksperimen deteksi dan penghitungan tandan sawit.'
  },
  {
    id: 'katalog-pdf',
    kind: 'katalog',
    label: 'KATALOG PDF',
    marker: '#',
    title: 'Katalog PDF Tinjauan Penghitungan Buah',
    theme: 'Katalog PDF',
    file: 'literature/scopus-2026-09/KATALOG-PDF.md',
    sourceDir: 'literature/scopus-2026-09',
    desc: 'Tautan PDF setiap kajian tinjauan, per kelompok kajian.'
  }
];

/* Folder yang di-exclude dari build Jekyll (`_config.yml`): berkas di
 * dalamnya TIDAK tayang di GitHub Pages, jadi tautan ke sana harus
 * diturunkan menjadi teks biasa alih-alih menjadi tautan mati. PDF akhir
 * di `manuscript/output/papers/` sengaja tetap tayang untuk pratinjau naskah.
 * Pengecualian: `literature/entries/`, sebab tautan ke entri korpus ditangani runtime
 * (`enhance()`) dan diubah menjadi rute internal `#/NNN`. */
const PAGES_EXCLUDED = [
  'experiments/code/', 'experiments/results/', 'experiments/logs/', 'experiments/runs/',
  'experiments/splits/', 'experiments/figures/', 'literature/extracted/',
  'datasets/', 'site/', 'tools/', 'pipeline/'
];
const ENTRY_LINK_RE = /(?:^|\/)\d{3}\s-\s.*\.md$/i;

function fail(msg) {
  console.error('\n[build.js] GAGAL: ' + msg + '\n');
  process.exit(1);
}
if (!fs.existsSync(ENTRI_DIR) || !fs.statSync(ENTRI_DIR).isDirectory()) {
  fail('Direktori "literature/entries/" tidak ditemukan di ' + ROOT);
}
SPECIAL_DOCS.forEach(function (d) {
  if (!fs.existsSync(path.join(ROOT, d.file))) {
    fail('Dokumen spesial "' + d.file + '" (id: ' + d.id + ') tidak ditemukan.');
  }
});
if (!fs.existsSync(MARKED_PATH)) {
  fail('Berkas "vendor/marked.min.js" tidak ditemukan.\n' +
       '        Unduh dahulu:\n' +
       '        curl -L -o vendor/marked.min.js https://unpkg.com/marked@' + MARKED_VERSION + '/marked.min.js');
}
const marked = require(MARKED_PATH);

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

const ACCENTS = {
  "'": '\u0301', '`': '\u0300', '"': '\u0308', '^': '\u0302', '~': '\u0303',
  '=': '\u0304', '.': '\u0307', c: '\u0327', v: '\u030c', H: '\u030b',
  u: '\u0306', k: '\u0328', r: '\u030a', b: '\u0331', d: '\u0323'
};
const LETTERS = { ss: 'ß', ae: 'æ', AE: 'Æ', oe: 'œ', OE: 'Œ', aa: 'å', AA: 'Å', o: 'ø', O: 'Ø', l: 'ł', L: 'Ł', i: 'ı', j: 'ȷ' };

function displayText(text) {
  return text
    .replace(/\\(['"`^~=.cvHukrbd])\s*(?:\{(\\?[A-Za-z])\}|(\\[ij]|[A-Za-z]))/g,
      (_, accent, braced, letter) => (braced || letter).replace('\\', '') + ACCENTS[accent])
    .replace(/\\(ss|ae|AE|oe|OE|aa|AA|o|O|l|L|i|j)(?:\{\}|(?![A-Za-z]))/g, (_, letter) => LETTERS[letter])
    .replace(/\\([ij])/g, (_, letter) => LETTERS[letter])
    .replace(/\\([&%|_$#{}])/g, '$1')
    .normalize('NFC');
}

function metadata(md) {
  const header = md.split(/^##(?!#)/m, 3)[1] || '';
  return new Map(Array.from(header.matchAll(/^\|\s*([^|]+?)\s*\|\s*([^\n]+?)\s*\|\s*$/gm),
    ([, name, value]) => [name.toLowerCase(), displayText(value.trim().replace(/^`|`$/g, ''))]));
}

function authorNames(value, surnameFirst) {
  const text = (value || '').replace(/\([^()]*\)/g, '').trim();
  const parts = text.split(/\s*,\s*/);
  if (surnameFirst || text.includes(';') || (parts.length === 2 && !/\s/.test(parts[1]))) {
    return text.split(/\s*;\s*/).filter(Boolean).map(name => {
      const comma = name.indexOf(',');
      return comma < 0 ? name : `${name.slice(comma + 1).trim()} ${name.slice(0, comma)}`.trim();
    });
  }
  return parts.filter(name => name && !/^(?:dkk\.?|et al\.?)$/i.test(name));
}

function section(md, heading) {
  const lines = md.split(/^##[ \t]+/m);
  const block = lines.find(line => line.slice(0, line.indexOf('\n')).trim() === heading);
  return block ? block.slice(block.indexOf('\n') + 1).trim() : '';
}

const textParser = new marked.Parser();
const ENTITIES = { amp: '&', quot: '"', lt: '<', gt: '>', '#39': "'", apos: "'" };

function plainText(md) {
  return textParser.parseInline(marked.Lexer.lexInline(md), textParser.textRenderer)
    .replace(/<\/?[A-Za-z][^>]*>/g, '')
    .replace(/&(amp|quot|lt|gt|#39|apos);/g, (_, key) => ENTITIES[key])
    .replace(/\s+/g, ' ')
    .trim();
}

function excerpt(overview) {
  const paragraph = plainText(overview.split(/\n\s*\n/, 1)[0]);
  if (paragraph.length <= 330) return paragraph;
  const end = paragraph.lastIndexOf(' ', 330);
  return paragraph.slice(0, end > 0 ? end : 330) + '…';
}

function markdownLinks(md) {
  const urls = [];
  marked.walkTokens(marked.lexer(md), token => {
    if (token.type === 'link') urls.push(token.href);
  });
  return urls;
}

function accessLinks(md, sourceDir) {
  const urls = markdownLinks(section(md, 'Tautan Akses'));
  const web = urls.filter(url => /^https?:\/\//i.test(url));
  const doiUrl = web.find(url => /^https?:\/\/(?:dx\.)?doi\.org\/10\.\d{4,}\//i.test(url));
  const doi = doiUrl ? new URL(doiUrl).pathname.slice(1) : null;
  const localPdf = urls.find(url => /^\.\.\/pdf\/[a-z0-9_%-]+\.pdf$/i.test(url));
  const onlinePdf = web.find(url => /\.pdf(?:[?#]|$)|^https?:\/\/arxiv\.org\/pdf\//i.test(url));
  const arxiv = web.find(url => /^https?:\/\/arxiv\.org\/abs\//i.test(url));
  const pdf = localPdf ? joinRelative(sourceDir, localPdf) : onlinePdf || (arxiv && arxiv.replace('/abs/', '/pdf/')) || null;
  const sourceUrl = doiUrl || arxiv || web.find(url =>
    /^https?:\/\/(?:openaccess\.thecvf\.com\/|ieeexplore\.ieee\.org\/|proceedings\.mlr\.press\/|openreview\.net\/|papers\.nips\.cc\/|aclanthology\.org\/)/i.test(url)) || onlinePdf || null;
  return {
    doi, pdf, sourceUrl,
    scholar: web.find(url => /^https?:\/\/scholar\.google\./i.test(url)) || null,
    semantic: web.find(url => /^https?:\/\/(www\.)?semanticscholar\.org\//i.test(url)) || null
  };
}

function referenceIds(md) {
  const ids = new Set();
  for (const url of markdownLinks(md)) {
    if (url.startsWith('#/')) {
      ids.add(url.slice(2).split(/[?#]/, 1)[0]);
      continue;
    }
    if (isAbsoluteTarget(url)) continue;
    let target;
    try { target = decodeURIComponent(url.split(/[?#]/, 1)[0]); }
    catch { continue; }
    if (target.split('/').includes('withheld')) continue;
    const old = target.match(/(?:^|\/)(\d{3}) - .*\.md$/i);
    const scopus = target.match(/(?:^|\/)([a-z][a-z0-9_-]*\d{4}[a-z0-9_-]*)\.md$/i);
    if (old || scopus) ids.add((old || scopus)[1]);
  }
  return Array.from(ids);
}

function cleanMarkdown(md, dropH1) {
  let text = md.replace(/\r\n/g, '\n');
  if (dropH1) {
    const lines = text.split('\n');
    let i = 0;
    while (i < lines.length && lines[i].trim() === '') i++;
    if (i < lines.length && /^#\s+/.test(lines[i])) lines.splice(i, 1);
    text = lines.join('\n');
  }
  text = text.replace(/^##[ \t]+Daftar Isi[\s\S]*?(?=^##[ \t])/m, '');
  return text.trim() + '\n';
}

function countWords(md) {
  const m = md.match(/[^\s]+/g);
  return m ? m.length : 0;
}

/* ------------------------------------------------------------------ *
 * Penulisan ulang tautan relatif dokumen spesial
 * ------------------------------------------------------------------ *
 * Isi dokumen disematkan ke `index.html` yang berada di akar repo, jadi
 * tautan relatif yang ditulis dari sudut pandang `sourceDir` harus digeser
 * ke akar. Untuk `sourceDir = 'experiments'`: `METRICS.md` menjadi
 * `experiments/METRICS.md`.
 */

function joinRelative(dir, rel) {
  const parts = String(dir || '').split('/').filter(function (p) { return p && p !== '.'; });
  String(rel).split('/').forEach(function (seg) {
    if (!seg || seg === '.') return;
    if (seg === '..') parts.pop();
    else parts.push(seg);
  });
  return parts.join('/');
}

function isAbsoluteTarget(t) {
  return /^[a-z][a-z0-9+.-]*:/i.test(t) || t.indexOf('//') === 0 || t.charAt(0) === '#' || t.charAt(0) === '/';
}

function isPagesExcluded(target) {
  if (ENTRY_LINK_RE.test(target)) return false;
  return PAGES_EXCLUDED.some(function (p) { return target.indexOf(p) === 0; });
}

function mapOutsideFences(md, fn) {
  let fence = null;
  return md.split('\n').map(function (line) {
    const m = line.match(/^\s{0,3}(`{3,}|~{3,})/);
    if (fence) {
      if (m && line.trim().indexOf(fence) === 0) fence = null;
      return line;
    }
    if (m) { fence = m[1]; return line; }
    return fn(line);
  }).join('\n');
}

function rebaseLinks(md, sourceDir, stats) {
  return mapOutsideFences(md, function (line) {
    return line.replace(/(!?)(\[[^\]]*\])\(\s*([^()\s]+)((?:\s+"[^"]*")?)\s*\)/g,
      function (whole, bang, label, target, title) {
        if (isAbsoluteTarget(target)) return whole;
        const rebased = joinRelative(sourceDir, target);
        if (isPagesExcluded(rebased)) {
          stats.dropped.push(rebased);
          return label.slice(1, -1);
        }
        if (rebased !== target) stats.rebased.push(target + ' -> ' + rebased);
        return bang + label + '(' + rebased + title + ')';
      });
  });
}

/* ------------------------------------------------------------------ *
 * Pindai dan rakit data entri
 * ------------------------------------------------------------------ */
const files = fs.readdirSync(ENTRI_DIR).filter(function (f) { return /\.md$/i.test(f); });
const entries = [];
const warnings = [];
const seenIds = Object.create(null);

files.forEach(function (file) {
  if (/^INDEX(-[A-Z]+)?\.MD$/.test(file.toUpperCase())) return;
  const meta = parseName(file);
  if (!meta) { warnings.push('Nama berkas tidak cocok pola: ' + file); return; }
  if (seenIds[meta.id]) warnings.push('Nomor entri ganda: ' + meta.id + ' (' + file + ')');
  seenIds[meta.id] = true;

  const raw = fs.readFileSync(path.join(ENTRI_DIR, file), 'utf8').replace(/\r\n/g, '\n');
  if (!raw.trim()) { warnings.push('Konten kosong: ' + file); return; }
  const srcIdx = raw.indexOf('<!--SRC-->');
  const summaryRaw = srcIdx >= 0 ? raw.slice(0, srcIdx) : raw;
  const srcText = srcIdx >= 0 ? raw.slice(srcIdx + 10).replace(/^\s*\n/, '').replace(/\s+$/, '') : '';
  const fields = metadata(summaryRaw);
  const md = cleanMarkdown(summaryRaw, true);
  const ov = section(md, 'Gambaran Umum');
  const title = fields.get('judul asli') || meta.title;

  entries.push({
    num: meta.num,
    id: meta.id,
    year: meta.year,
    title,
    aliases: [meta.title].filter(alias => alias !== title),
    theme: meta.theme,
    koleksi: 'deteksi',
    bib: fields.get('kunci bibtex') || null,
    special: false,
    words: countWords(md),
    authors: authorNames(fields.get('penulis'), false),
    venue: fields.get('venue') || fields.get('venue / jurnal') || '',
    ...accessLinks(md, 'literature/entries'),
    summary: excerpt(ov),
    crops: [],
    methods: methodsInTitle(`${title} ${meta.title}`),
    references: referenceIds(md),
    md,
    src: srcText
  });
});

if (warnings.some(function (w) { return /tidak cocok pola/.test(w); })) {
  console.error('\n[build.js] Berkas bermasalah:');
  warnings.forEach(function (w) { console.error('   - ' + w); });
  fail('Ada nama berkas yang tidak cocok pola penamaan. Perbaiki lalu jalankan ulang.');
}

entries.sort(function (a, b) { return a.num - b.num; });

const linkStats = { rebased: [], dropped: [] };
const specials = SPECIAL_DOCS.map(function (d, i) {
  const raw = fs.readFileSync(path.join(ROOT, d.file), 'utf8');
  const md = rebaseLinks(cleanMarkdown(raw, true), d.sourceDir, linkStats);
  return {
    num: i - SPECIAL_DOCS.length,
    id: d.id,
    year: null,
    title: d.title,
    theme: d.theme,
    bib: null,
    special: true,
    kind: d.kind,
    label: d.label,
    marker: d.marker,
    desc: d.desc,
    summary: d.desc,
    source: d.file,
    words: countWords(md),
    scholar: null,
    semantic: null,
    md: md
  };
});

/* ------------------------------------------------------------------ *
 * Entri korpus main6
 * ------------------------------------------------------------------ *
 * Satu berkas per kajian di literature/scopus-2026-09/entri/<kunci>.md.
 * Entri ini kini menjadi bagian dari satu korpus bersama entri lama dan
 * isinya TIDAK disematkan: index.html hanya memuat metadata dan paragraf
 * "Gambaran Umum" (untuk pencarian); isi lengkap diambil runtime dari
 * berkas .md saat entri dibuka.
 */
const M6_DIR = path.join(ROOT, 'literature', 'scopus-2026-09', 'entri');
const M6_GROUPS = {
  C1: 'Hitung Multi-Pengamatan',
  C2: 'Hitung Satu Pandang',
  C3: 'Kelapa Sawit',
  C4: 'Hitung per Kelas',
  C5: 'Depth & Sensor 3D',
  R: 'Tinjauan Terdahulu',
  T: 'Metode Luar Pertanian'
};
const COLLECTIONS = [
  { key: 'buah', name: 'Tinjauan Penghitungan Buah',
    desc: 'Kajian Scopus (pencarian 28 September 2026) tentang penghitungan buah berbasis citra: cara setiap buah dihitung sekali dari banyak pengamatan, dikelompokkan menurut jenis kajian.' },
  { key: 'deteksi', name: 'Deteksi Objek & RGB-D',
    desc: 'Telaah makalah deteksi objek, keluarga YOLO, dan fusi warna dengan kedalaman (RGB-D) yang menjadi dasar eksperimen deteksi.' }
];
const M6_URL = 'literature/scopus-2026-09/entri/';
const M6_TEKS_URL = 'literature/scopus-2026-09/teks/';
const m6 = [];
if (fs.existsSync(M6_DIR)) {
  fs.readdirSync(M6_DIR).filter(function (f) { return /\.md$/i.test(f); }).sort().forEach(function (file) {
    const raw = fs.readFileSync(path.join(M6_DIR, file), 'utf8').replace(/\r\n/g, '\n');
    const key = file.replace(/\.md$/i, '');
    const h1 = raw.match(/^#\s+(.+)$/m);
    const fields = metadata(raw);
    const year = fields.get('tahun');
    const group = (fields.get('kode') || '').split(/\s/, 1)[0];
    if (!h1 || !/^\d{4}$/.test(year) || !M6_GROUPS[group] || fields.get('kunci bibtex') !== key) {
      warnings.push('Entri main6 tanpa kepala sah (jalankan tools/scopus/entri_main6.py): ' + file);
      return;
    }
    const ov = section(raw, 'Gambaran Umum');
    const title = fields.get('judul asli') || h1[1].trim();
    m6.push({
      id: key,
      year: Number(year),
      title,
      theme: M6_GROUPS[group],
      koleksi: 'buah',
      bib: key,
      special: false,
      m6: true,
      words: countWords(raw),
      authors: authorNames(fields.get('penulis'), true),
      venue: fields.get('venue') || '',
      ...accessLinks(raw, 'literature/scopus-2026-09/entri'),
      summary: excerpt(ov),
      crops: (fields.get('tanaman') || '').split(/\s*,\s*/).filter(Boolean),
      methods: methodsInTitle(title),
      references: referenceIds(raw),
      md: '',
      ov,
      lazy: M6_URL + file,
      srcLazy: M6_TEKS_URL + key + '.txt'
    });
  });
}

const maxOldNum = entries.reduce(function (m, e) { return Math.max(m, e.num); }, 0);
const korpus = entries.concat(m6.map(function (e, i) {
  return Object.assign({}, e, { num: maxOldNum + i + 1 });
}));

const DATA = specials.concat(korpus);
const entryIds = new Set(korpus.map(entry => entry.id));
korpus.forEach(entry => {
  entry.references = entry.references.filter(id => id !== entry.id && entryIds.has(id));
});

/* ------------------------------------------------------------------ *
 * Statistik dan META
 * ------------------------------------------------------------------ */
const themeCounts = {};
const yearCounts = {};
const yearByCol = {};
let totalWords = 0;
korpus.forEach(function (e) {
  themeCounts[e.theme] = (themeCounts[e.theme] || 0) + 1;
  yearCounts[e.year] = (yearCounts[e.year] || 0) + 1;
  yearByCol[e.year] = yearByCol[e.year] || {};
  yearByCol[e.year][e.koleksi] = (yearByCol[e.year][e.koleksi] || 0) + 1;
  totalWords += e.words;
});
const years = Object.keys(yearCounts).map(Number).sort(function (a, b) { return a - b; });
const themes = Object.keys(themeCounts).sort();
const minYear = years[0];
const maxYear = years[years.length - 1];
const totalMin = Math.round(totalWords / 200);
const totalHours = Math.max(1, Math.round(totalMin / 60));

const META = {
  total: korpus.length,
  themeCount: themes.length,
  minYear: minYear,
  maxYear: maxYear,
  yearCounts: yearCounts,
  themeCounts: themeCounts,
  totalWords: totalWords,
  totalMin: totalMin,
  totalHours: totalHours,
  yearByCol: yearByCol,
  collections: COLLECTIONS.map(function (c) {
    const items = korpus.filter(function (e) { return e.koleksi === c.key; });
    const ys = items.map(function (e) { return e.year; });
    const tc = {};
    items.forEach(function (e) { tc[e.theme] = (tc[e.theme] || 0) + 1; });
    return {
      key: c.key, name: c.name, desc: c.desc, total: items.length,
      minYear: Math.min.apply(null, ys), maxYear: Math.max.apply(null, ys),
      themes: Object.keys(tc).sort(function (a, b) { return tc[b] - tc[a] || a.localeCompare(b); })
    };
  }),
  markedVersion: MARKED_VERSION
};

if (META.collections.reduce(function (n, c) { return n + c.themes.length; }, 0) !== themes.length) {
  fail('Nama tema dipakai di lebih dari satu koleksi; ubah M6_GROUPS agar tidak sama dengan tema entri lama.');
}

/* ------------------------------------------------------------------ *
 * Laporan
 * ------------------------------------------------------------------ */
console.log('\n=== build.js: Ruang Baca Riset ===');
console.log('Entri korpus    : ' + korpus.length + '  (' + COLLECTIONS.map(function (c) { return c.name + ' ' + korpus.filter(function (e) { return e.koleksi === c.key; }).length; }).join(' · ') + ')');
console.log('Dokumen spesial : ' + specials.length + '  ' +
  specials.map(function (s) { return s.id + ' [' + s.kind + ', ' + s.words + ' kata]'; }).join(' · '));
console.log('Tema            : ' + themes.length);
console.log('Rentang tahun   : ' + minYear + '-' + maxYear + ' (' + years.length + ' tahun berisi)');
console.log('Total kata      : ~' + totalWords.toLocaleString('en-US') + '  (kira-kira ' + totalHours + ' jam baca)');
console.log('\nDistribusi tema :');
themes.sort(function (a, b) { return themeCounts[b] - themeCounts[a]; }).forEach(function (t) {
  console.log('   ' + String(themeCounts[t]).padStart(3) + '  ' + t);
});
console.log('\nDistribusi tahun:');
years.forEach(function (y) { console.log('   ' + y + '  ' + String(yearCounts[y]).padStart(3) + '  ' + '#'.repeat(yearCounts[y])); });
console.log('\nTautan dokumen spesial:');
console.log('   ' + linkStats.rebased.length + ' tautan relatif digeser ke akar');
linkStats.rebased.forEach(function (r) { console.log('     ' + r); });
console.log('   ' + linkStats.dropped.length + ' tautan ke folder non-Pages diturunkan jadi teks');
linkStats.dropped.forEach(function (r) { console.log('     ' + r); });

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

const css = fs.readFileSync(path.join(__dirname, 'style.css'), 'utf8');
const discovery = fs.readFileSync(path.join(__dirname, 'discovery.js'), 'utf8');
const app = fs.readFileSync(path.join(__dirname, 'app.js'), 'utf8');
const description = `Katalog ${META.total} kajian penghitungan buah berbasis citra, deteksi objek, dan sensor kedalaman.`;

const PAGE = `<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#262648">
<meta name="description" content="${description}">
<meta property="og:title" content="Ruang Baca Riset">
<meta property="og:description" content="${description}">
<meta property="og:type" content="website">
<meta property="og:locale" content="id_ID">
<title>Ruang Baca Riset</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Crect width='40' height='40' rx='7' fill='%23e3ef9c'/%3E%3Cpath d='M20 13c-4-3-8-3-11-2v17c3-1 7-1 11 2 4-3 8-3 11-2V11c-3-1-7-1-11 2Zm0 0v17' stroke='%23293019' fill='none' stroke-width='2' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400..750&amp;family=Source+Serif+4:ital,wght@0,400..650;1,400..600&amp;display=swap">
<style>${css}</style>
</head>
<body>
<div id="app"></div>
<noscript><p>Aktifkan JavaScript untuk mencari dan membuka kajian.</p></noscript>
<script>${markedSrc}
</script>
<script>${dataScript}</script>
<script>${discovery}
</script>
<script>${app}
</script>
</body>
</html>
`;

fs.writeFileSync(OUT_PATH, PAGE, 'utf8');
console.log('\nBerkas ditulis : index.html');
console.log('Ukuran         : ' + (Buffer.byteLength(PAGE, 'utf8') / 1048576).toFixed(2) + ' MB');
