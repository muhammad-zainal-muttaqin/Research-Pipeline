# PLAN — `index.html` Reading Room untuk Research-Pipeline

> Dokumen rencana teknis & desain untuk membangun **satu file `index.html` mandiri**
> yang memuat seluruh bahan bacaan (202 entri makalah + TEMUAN.md) agar bisa
> dibaca nyaman dan di-deploy ke **GitHub Pages / Cloudflare Pages** tanpa
> dependensi eksternal apa pun.

---

## 1. Tujuan & Hasil Akhir

| Aspek | Target |
|---|---|
| Output | Satu file `index.html` mandiri (single-file app) di root repo |
| Isi | 202 entri `entri/*.md` + `TEMUAN.md` sebagai dokumen sintesis khusus |
| Dependensi runtime | **Nol** — semua CSS, JS, dan parser Markdown di-inline ke dalam file |
| Ukuran akhir | ± 3–4 MB (konten mentah 2,6 MB + parser + runtime) — masih aman untuk GitHub Pages (limit 100 MB/file, soft limit 1 GB/repo) |
| Deploy | Cukup push repo → aktifkan Pages; tanpa build step di CI |
| Regenerasi | `node build.js` menghasilkan ulang `index.html` kapan pun konten `entri/` berubah |

**Non-goal:** tidak membangun backend, tidak memakai framework JS (React/Vue),
tidak memakai CDN untuk fungsionalitas inti (font Google Fonts boleh dipakai
dengan fallback sistem yang anggun; situs tetap utuh tanpa internet).

---

## 2. Inventaris Konten (Hasil Eksplorasi)

| Sumber | Jumlah | Catatan |
|---|---|---|
| `entri/NNN - YYYY - Judul - Tema.md` | 202 berkas (± 2,6 MB) | Satu makalah = satu berkas |
| `TEMUAN.md` | 1 berkas (24 KB) | Sintesis lintas makalah — diperlakukan sebagai entri spesial "pin di atas" |
| `README.md` | 1 berkas | Referensi copy pengantar; **tidak disertakan mentah** — Beranda adalah dashboard yang ditulis khusus (§5.1 butir 4) |
| `entri/INDEX.md` | 1 berkas | **Dilewati** — fungsinya digantikan navigasi aplikasi |
| `references.bib`, `tinjauan-pustaka.tex` | — | Tidak disertakan di web (tetap di repo) |

**Fakta konten yang sudah diverifikasi:**
- Tidak ada fenced code block (` ``` `) dan tidak ada gambar di semua entri → parser cukup menangani: heading ATX, tabel GFM, blockquote, list (berurut/tidak, bersarang), bold/italic/strikethrough, inline code, tautan, HR.
- Pola nama berkas konsisten: `^(\d{3}) - (\d{4}) - (.+) - ([^-]+)\.md$` (tema = segmen terakhir; judul boleh mengandung " - " di tengah).
- Setiap entri punya struktur heading konsisten: Metadata Ringkas (tabel), Tautan Akses, Identitas Publikasi, Ringkasan Eksekutif, Abstrak (Parafrase), …, hingga Cara Memverifikasi & Sitasi — cocok untuk TOC otomatis.
- Bahasa konten: Indonesia → seluruh label UI juga Bahasa Indonesia.

**17 tema** (untuk filter & warna aksen): Dataset · Deteksi 3D · Estimasi
Kedalaman · Fondasi RGB · Fusi Multimodal · Grasp Robotik · Industri · Medis ·
Pedestrian RGB-T · Pertanian · Pose 6D · RGB-D SLAM · RGB-D SOD · Remote
Sensing · Segmentasi RGB-D · Survei YOLO · YOLO plus RGB-D.

**Rentang tahun:** 2012–2026 (dipakai untuk filter & grafik timeline).

**Catatan rekonsiliasi sumber (terverifikasi saat audit):**
- Aplikasi memakai **17 label tema dari nama berkas**. Dokumen `TEMUAN.md`
  menyebut "14 klaster" — itu taksonomi naskah LaTeX; keduanya tidak
  bertentangan, aplikasi mengikuti label nama berkas.
- Tahun dengan entri berjumlah **14** (2013 kosong); "rentang 2012–2026"
  adalah span 15 tahun kalender.
- Sebagian isi entri menulis "Nomor entri … dari 154" (artefak penulisan
  batch); aplikasi mengabaikannya dan memakai penomoran nama berkas 001–202.
- `vendor/marked.min.js` v12.0.0 terverifikasi **35.159 B (~35 KB)** dan
  semua 202 nama berkas cocok pola regex (hanya `INDEX.md` yang gagal —
  memang dikecualikan).

---

## 3. Arsitektur Sistem

```
┌────────────── build time (lokal, oleh developer) ──────────────┐
│  build.js (Node.js, tanpa dependency npm)                       │
│   1. Scan entri/*.md → parse metadata dari nama berkas          │
│   2. Baca isi Markdown mentah setiap entri + TEMUAN.md          │
│   3. Susun array data → serialisasi JSON aman-script            │
│   4. Suntikkan data + marked.min.js + template ke satu berkas   │
│   5. Tulis index.html                                           │
└──────────────────────────────┬──────────────────────────────────┘
                               ▼
┌────────────── runtime (browser pengguna, statis) ──────────────┐
│  index.html mandiri                                             │
│   • DATA: array entri (markdown mentah) tertanam di <script>    │
│   • marked.min.js (inline) → render Markdown → HTML di klien    │
│   • app.js (inline) → router hash, pencarian, filter, tema      │
│   • style (inline) → design system editorial                    │
└─────────────────────────────────────────────────────────────────┘
```

**Keputusan arsitektur & alasannya:**

1. **Markdown dirender di klien (bukan pre-render ke HTML saat build).**
   - Ukuran total hampir sama, tetapi teks mentah sekaligus menjadi sumber
     pencarian full-text tanpa perlu strip tag HTML.
   - Parser `marked.min.js` (~35 KB, terverifikasi) di-inline → nol dependensi eksternal,
     GFM lengkap (tabel, strikethrough) terdukung dan teruji.
   - Hanya entri yang sedang dibuka yang dirender → DOM ringan meski total
     konten 2,6 MB.
2. **Data disuntik sebagai `const DATA = [...]` di dalam `<script>` biasa**
   (bukan `type="application/json"`): langsung jadi objek JS tanpa
   `JSON.parse` 3 MB; escaping aman dilakukan build script
   (`</` → `<\/`, `<!--` → `<\!--`, U+2028/2029).
3. **Routing memakai hash (`#/042`)** — satu-satunya pola yang bekerja di
   static hosting tanpa rewrite rule; tautan antar-entri bisa disalin.
4. **State filter/pencarian ikut di hash** (`#/?q=fusion&tema=RGB-D+SOD`)
   supaya hasil pencarian bisa di-bookmark.
5. **Preferensi tema gelap/terang & posisi baca terakhir** disimpan di
   `localStorage` (tanpa cookie, tanpa server).

---

## 4. Struktur File Proyek (setelah selesai)

```
Research-Pipeline/
├── PLAN.md            ← dokumen ini
├── build.js           ← build script (satu-satunya alat yang dibutuhkan)
├── index.html         ← HASIL BUILD (jangan diedit manual)
├── vendor/
│   └── marked.min.js  ← parser Markdown yang akan di-inline saat build
├── entri/             ← sumber konten (202 .md + INDEX.md, tidak disentuh)
├── TEMUAN.md          ← sumber konten
├── README.md          ← sumber konten beranda
├── references.bib     ← tidak disentuh
└── tinjauan-pustaka.tex
```

`index.html` boleh di-commit (itulah yang dilayani Pages). `vendor/` dan
`build.js` di-commit agar siapa pun bisa regenerasi.

---

## 5. Spesifikasi Build Script (`build.js`)

Node.js ≥ 18, **tanpa `npm install`** (hanya `fs`, `path`).

### 5.1 Alur kerja

1. **Validasi awal:** pastikan `entri/`, `TEMUAN.md`, `vendor/marked.min.js`
   ada; gagal → pesan error jelas.
2. **Parse entri:** untuk setiap berkas `entri/*.md` (kecuali `INDEX.md`):
   - Regex nama: `/^(\d{3}) - (\d{4}) - (.+) - ([^-]+)\.md$/`
   - Hasil: `{ num, year, title, theme, file }`
   - Baca isi UTF-8; buang baris pertama (`# NNN - ...`) karena judul sudah
     dirender oleh aplikasi (menghindari duplikasi H1).
   - Ekstrak **kunci BibTeX** dari tabel metadata (baris `| Kunci BibTeX |`)
     bila ada → ditampilkan di header entri.
3. **Susun TEMUAN** sebagai objek spesial:
   `{ num: 0, year: null, title: "Temuan Riset — Sintesis Lintas Makalah", theme: "Sintesis", special: true }`.
4. **Susun Beranda** dari `README.md` (dipotong sebelum tabel navigasi besar
   bila terlalu panjang; cukup bagian pengantar) — atau tulis konten beranda
   khusus di template (lihat §7.2, diputuskan saat implementasi; default:
   beranda = dashboard statistik + pengantar singkat, README tidak disertakan
   mentah).
5. **Serialisasi:** `JSON.stringify(entries)` lalu sanitasi:
   `.replace(/</g, '\\u003c')` (mencegah `</script>` breakout) — aman karena
   `\u003c` valid di JSON string.
6. **Rakit HTML:** baca `vendor/marked.min.js`, gabungkan dengan template
   (CSS + markup + app runtime yang tertulis langsung di `build.js` sebagai
   template literal) dan data → tulis `index.html`.
7. **Laporan:** cetak jumlah entri, distribusi tema/tahun, ukuran file akhir,
   dan peringatan (nama berkas tak cocok pola, konten kosong, dsb.).

### 5.2 Kontrak data per entri

```js
{
  num: 42,                    // Number, dari nama berkas
  id: "042",                  // String 3 digit — untuk URL #/042
  year: 2021,                 // Number | null
  title: "Visual Saliency Transformer (VST)",
  theme: "RGB-D SOD",
  bib: "liu2021visual",       // String | null — kunci BibTeX
  special: false,             // true hanya untuk TEMUAN
  words: 1350,                // estimasi kata — untuk "waktu baca"
  headings: [ {depth:2, text:"Metadata Ringkas"}, … ], // untuk TOC (diekstrak saat build)
  md: "…isi markdown mentah…"
}
```

`headings` diekstrak saat build (regex `^(#{2,3})\s+(.+)$` per baris, abaikan
isi blockquote) supaya TOC tidak perlu dihitung ulang di klien.

### 5.3 Memperoleh `vendor/marked.min.js`

```bash
curl -L -o vendor/marked.min.js https://unpkg.com/marked@12.0.0/marked.min.js
```

Disimpan di repo → build berikutnya tidak butuh internet. Versi dipin (12.0.0).

---

## 6. Design System

Menggabungkan dua skill: **minimalist-ui** (palet warm monochrome, tipografi
editorial, flat bento) + **high-end-visual-design** (micro-motion, double-bezel,
ritme spasial). Vibe yang dipilih: **Editorial Luxury** — "ruang baca digital"
untuk dokumen akademik; tenang, kertas hangat, aksen pastel muted.

### 6.1 Palet (CSS custom properties, mode terang)

| Token | Nilai | Pakai untuk |
|---|---|---|
| `--bg` | `#F7F6F3` | kanvas aplikasi (warm bone) |
| `--surface` | `#FFFFFF` | kartu & area baca |
| `--surface-2` | `#FBFAF8` | sidebar / panel sekunder |
| `--ink` | `#1F2328` | teks utama (bukan hitam murni) |
| `--ink-2` | `#6B6F76` | teks sekunder / meta |
| `--line` | `#E8E6E1` | hairline 1px di mana-mana |
| `--accent` | `#9F2F2D` | merah bata pudar — tautan, state aktif |
| `--accent-bg` | `#FDEBEC` | latar aksen sangat lembut |

**Aksen tema (17 tema)** — masing-masing pasangan bg+ink muted pastel,
contoh: Fondasi RGB `#E1F3FE/#1F6C9F`, RGB-D SOD `#EDF3EC/#346538`,
Estimasi Kedalaman `#FBF3DB/#956400`, Pose 6D `#F3EDF7/#6B4E8E`, dst.
(Palet lengkap ditetapkan di `THEMES` dalam app runtime; semua desaturated.)

**Mode gelap:** inversi hangat — `--bg:#16161​4`, `--surface:#1D1C1A`,
`--ink:#E8E6E1`, `--ink-2:#9A978F`, `--line:#2C2B28`; aksen pastel diganti
versi translucent (`rgba` rendah) dengan teks terang. Diset via
`html[data-theme="dark"]`; default mengikuti `prefers-color-scheme`.

### 6.2 Tipografi

| Peran | Font stack | Skala |
|---|---|---|
| Serif editorial (judul entri, hero) | `'Newsreader', 'Georgia', serif` — Google Fonts, `opsz` | H1 34–40px, tracking −0.02em, line-height 1.15 |
| Sans UI (label, sidebar, tombol) | `'Plus Jakarta Sans', 'Helvetica Neue', system-ui, sans-serif` — Google Fonts | 13–15px, weight 400/500/600 |
| Mono (meta, kunci BibTeX, kbd) | `'JetBrains Mono', 'SF Mono', monospace` — Google Fonts | 12–13px |

Font dimuat via `<link>` Google Fonts dengan `display=swap`; **tanpa internet
situs tetap utuh** (fallback Georgia + system-ui tetap editorial). Body teks
bacaan: 16–17px, `line-height: 1.7`, lebar kolom baca `max-width: 720px`.

### 6.3 Kaidah visual (dari kedua skill, diringkas)

- **Tanpa** gradasi mencolok, tanpa shadow berat, tanpa emoji, tanpa pill raksasa untuk kartu. Border selalu `1px solid var(--line)`, radius 8–12px (kartu) / 4–6px (tombol).
- **Double-bezel** untuk kartu penting di Beranda: shell luar `padding:6px; background:color-mix(in srgb, var(--ink) 3%, transparent); border:1px solid var(--line); border-radius:14px` → inti dalam `background:var(--surface); border-radius:10px`.
- **Shadow** hanya ultra-diffuse: `0 2px 12px rgba(31,35,40,.05)` saat hover kartu.
- **Motion:** semua transisi `cubic-bezier(.32,.72,0,1)` 200–500ms; scroll-reveal via `IntersectionObserver` (`translateY(14px) + opacity 0 → 1`, stagger `calc(var(--i)*50ms)`); hanya `transform` & `opacity` yang dianimasi.
- **Ikon:** SVG inline custom garis tipis 1.5px (search, sun/moon, chevron, arrow-left/right, list, x, copy, check, book, filter) — tanpa library ikon.
- **Grain halus:** overlay noise SVG `feTurbulence` pada pseudo-element fixed `opacity:.025`, `pointer-events:none` — kesan kertas.
- `kbd` untuk shortcut: `border:1px solid var(--line); border-bottom-width:2px; border-radius:4px; background:var(--surface-2); font mono 11px`.

---

## 7. Tata Letak & Halaman

Aplikasi punya 3 "layar" (semua dalam satu file, di-switch via hash router):

### 7.1 Kerangka umum

```
┌──────────────────────────────────────────────────────────────────┐
│ TOPBAR (sticky, h=56px, blur saat scroll)                        │
│  ☰ │ ⌘K Cari…            Tema ◐  │ progress baca (hairline 2px)  │
├──────────────┬─────────────────────────────────┬───────────────┤
│ SIDEBAR      │  KONTEN (scroll independen)     │  PANEL TOC    │
│ 300px        │  max-w 720px, padding 48–64px   │  240px        │
│ • search     │                                 │  (≥1200px)    │
│ • chip tema  │                                 │               │
│ • filter thn │                                 │               │
│ • daftar     │                                 │               │
│   entri      │                                 │               │
└──────────────┴─────────────────────────────────┴───────────────┘
 < 900px: sidebar jadi drawer overlay (hamburger morph → X)       
 900–1200px: TOC disembunyikan, TOC inline di atas artikel         
```

### 7.2 Layar Beranda (`#/`)

1. **Hero editorial:** eyebrow pill `TINJAUAN PUSTAKA · 2012–2026`, judul serif
   besar "Ruang Baca Riset\nYOLO · RGB · RGB-D", subjudul 1 kalimat, dua CTA:
   [Mulai dari Temuan →] (solid ink) dan [Jelajahi 202 entri] (ghost).
2. **Strip statistik (bento 4 sel):** 202 entri · 17 tema · rentang 2012–2026 ·
   ±X jam total waktu baca. Angka besar serif, label mono uppercase kecil.
3. **Timeline per tahun:** bar chart murni CSS (flex kolom tinggi = jumlah
   entri; hover → tooltip angka; klik → filter tahun itu). Ini "grafik" tanpa
   library apa pun.
4. **Grid tema (17 kartu):** tiap kartu = nama tema, jumlah entri, 3 judul
   contoh kecil, chip warna pastelnya; klik → daftar terfilter. Kartu memakai
   pola double-bezel + hover lift halus.
5. **"Mulai di sini":** 4 kurasi jalur baca (mis. *Alur YOLO*: 001→010;
   *Alur Fusi RGB-D*; *Survei*; *Fondasi*) — daftar tautan cepat berbasis
   nomor entri yang sudah diketahui dari README.
6. Footer kecil: jumlah entri, petunjuk regenerasi (`node build.js`), tautan
   repo berkas (`tinjauan-pustaka.tex`, `references.bib`).

### 7.3 Layar Entri (`#/042`)

- **Header entri:** eyebrow `ENTRI 042 / 202 · 2021 · chip tema berwarna` →
  judul serif → baris meta mono (kunci BibTeX dengan tombol salin, estimasi
  waktu baca, tautan Scholar/Semantic Scholar yang diekstrak dari isi).
- **TOC:** rail kanan sticky (heading H2/H3 dari data build; item aktif
  di-highlight via `IntersectionObserver` saat scroll — scroll-spy).
- **Isi:** hasil render `marked` dengan styling bacaan:
  - tabel → dibungkus `.table-wrap` (scroll horizontal di mobile), header
    `surface-2`, zebra rows `#000` 2%, border hairline;
  - blockquote → border-left 2px aksen + latar aksen-bg 40%;
  - tautan eksternal → aksen, underline saat hover, `target=_blank rel=noopener`;
  - HR → hairline lebar pendek terpusat;
  - heading H2 diberi anchor `#` yang muncul saat hover (deep-link).
- **Navigasi bawah:** kartu « Entri sebelumnya / berikutnya » (nomor + judul),
  menghormati urutan filter aktif (jika datang dari hasil filter, prev/next
  mengikuti daftar terfilter).
- **Progress baca:** bar 2px di bawah topbar mengikuti scroll artikel.

### 7.4 Layar Sintesis (`#/temuan`)

Sama seperti layar entri, tetapi: di-pin di atas sidebar (label khusus
"SINTESIS"), ikon berbeda, dan jadi tujuan CTA utama Beranda.

### 7.5 Sidebar (komponen inti navigasi)

- **Search box** dengan ikon, `placeholder: Cari judul, tema, isi…`, tombol
  `Esc`/`x` clear; hasil live (debounce 120ms).
- **Chip tema** horizontal-scroll (maks 2 baris, "+N lagi" expand) — toggle
  multi-select; chip aktif memakai warna pastel temanya.
- **Select tahun** (dropdown custom sederhana) + tombol reset filter.
- **Daftar entri virtual-scroll ringan:** 202 item cukup dirender semua
  (DOM ± 202 baris × 2 span — masih ringan), tiap baris: nomor mono 3 digit,
  judul (ellipsis), tahun kecil + dot warna tema. Item aktif: latar aksen-bg,
  bar aksen 2px di kiri. TEMUAN di-pin paling atas dengan divider.
- Saat pencarian aktif: tampilkan jumlah hasil ("17 dari 202") + sorot
  istilah cocok pada judul (`<mark>` aksen-bg).

---

## 8. Spesifikasi Fitur (runtime `app.js` inline)

| # | Fitur | Detail implementasi |
|---|---|---|
| F1 | Router hash | `hashchange` → parse `#/`, `#/042`, `#/temuan`, query `?q=&tema=&thn=`; render layar; scroll ke atas; simpan riwayat filter |
| F2 | Render Markdown | `marked.parse(md)` + renderer custom: tabel dibungkus div, tautan eksternal `target=_blank`, heading diberi `id` slug + anchor; **sanitasi**: konten milik sendiri (tepercaya), tetap set `marked` `headerIds` manual & hindari injeksi lewat pencarian (input user hanya dipakai untuk `<mark>` via `textContent`) |
| F3 | Pencarian full-text | Normalisasi (lowercase, strip diakritik via `normalize('NFD')`); skor: judul ×5, tema ×3, isi ×1; hasil diurut skor; `<mark>` pada judul; batasi render 60 hasil pertama + "tampilkan semua" |
| F4 | Filter tema & tahun | Multi-select tema (Set), single-select tahun; kombinasi AND dengan query; URL ikut berubah (replaceState) |
| F5 | Mode gelap/terang | Toggle topbar; `localStorage.rp-theme`; default `prefers-color-scheme`; transisi warna 250ms |
| F6 | TOC + scroll-spy | Dari `headings` data build; `IntersectionObserver` rootMargin `-20% 0px -70%`; klik → smooth scroll |
| F7 | Progress baca | `scroll` listener (passive, rAF-throttle) pada kontainer konten → lebar bar |
| F8 | Prev/Next | Berdasar daftar terfilter terakhir (atau urutan nomor bila tanpa filter) |
| F9 | Shortcut keyboard | `/` atau `Ctrl/⌘+K` fokus search · `Esc` clear/tutup drawer · `←/→` prev/next entri · `t` toggle tema · `?` buka modal bantuan shortcut (grid kbd) |
| F10 | Salin tautan & BibTeX | Tombol copy di header entri → `navigator.clipboard` + feedback ikon check 1,2s |
| F11 | Waktu baca | `words/200` menit, dibulatkan; tampil di meta entri & total di Beranda |
| F12 | Scroll-reveal | `IntersectionObserver` untuk kartu Beranda & header entri, stagger `--i` |
| F13 | Drawer mobile | Sidebar jadi overlay; hamburger 2 garis morph → X (rotate ±45°); kunci scroll body saat terbuka |
| F14 | State baca terakhir | `localStorage.rp-last` = id entri; Beranda menampilkan chip "Lanjutkan: 042 …" bila ada |
| F15 | Deep-link heading | `#/042#metodologi--arsitektur` → scroll ke heading setelah render |

**Batasan sadar:** tanpa service worker/PWA (single-file tetap bisa offline penuh
karena tak ada request lain setelah font); tanpa sinkronisasi antar-perangkat.

---

## 9. Rencana Implementasi (fase & checklist)

> Setiap fase menghasilkan artefak yang bisa dicek sebelum lanjut.

### Fase 0 — Persiapan ✔ (sudah selesai saat PLAN ini ditulis)
- [x] Inventaris konten, verifikasi pola nama & sintaks Markdown
- [x] Tulis PLAN.md

### Fase 1 — Fondasi build
- [ ] `mkdir vendor && curl -L -o vendor/marked.min.js https://unpkg.com/marked@12.0.0/marked.min.js`
- [ ] Tulis `build.js` bagian 1: scan + parse nama berkas + baca konten +
      ekstrak `bib`, `words`, `headings`; cetak laporan → **cek:** 202 entri,
      0 peringatan pola nama
- [ ] Jalankan: `node build.js --dry` (mode laporan saja, belum menulis HTML)

### Fase 2 — Template & design system
- [ ] Tulis CSS lengkap (token terang/gelap, layout 3 kolom, tipografi bacaan,
      tabel, blockquote, chip, kartu bento, drawer, kbd, grain, motion) di
      dalam template `build.js`
- [ ] Tulis markup kerangka (topbar, sidebar, main, toc-rail, modal bantuan)
- [ ] **Cek:** buka `index.html` dummy (data 3 entri) di browser → layout
      responsif 360px / 768px / 1440px benar

### Fase 3 — Runtime app
- [ ] Router hash + render Beranda / Entri / Temuan
- [ ] Integrasi `marked` + renderer custom + anchor heading
- [ ] Sidebar: daftar, chip tema, filter tahun, pencarian + `<mark>`
- [ ] Tema gelap/terang + persist; TOC scroll-spy; progress bar; prev/next;
      shortcut; copy; drawer mobile; scroll-reveal; state baca terakhir
- [ ] **Cek manual:** semua F1–F15 di browser

### Fase 4 — Build penuh & uji isi
- [ ] `node build.js` → `index.html` final; verifikasi ukuran & laporan
- [ ] Uji sampling 10 entri acak lintas tema: tabel rapi, tautan jalan, TOC
      benar, tak ada artefak Markdown mentah
- [ ] Uji `file://` (klik dua kali) **dan** server statis (`npx serve .`)
- [ ] Lighthouse cepat: tak ada error konsol; warna kontras AA

### Fase 5 — Deploy & dokumentasi
- [ ] Tambah bagian "Baca versi web" di `README.md` (tautan Pages + cara
      regenerasi) — opsional, konfirmasi dulu ke pengguna
- [ ] Panduan deploy (lihat §10) disampaikan ke pengguna

---

## 10. Panduan Deploy

**GitHub Pages**
1. `git add index.html build.js vendor/marked.min.js PLAN.md && git commit -m "Web reading room" && git push`
2. Repo → **Settings → Pages → Source: `Deploy from a branch`** → branch `main`, folder `/ (root)` → Save.
3. Situs tayang di `https://<user>.github.io/Research-Pipeline/` dalam ±1 menit.

**Cloudflare Pages**
1. Dash → **Workers & Pages → Create → Pages → Connect to Git** → pilih repo.
2. **Build command: (kosongkan)** · **Build output directory: `/`** → Deploy.
3. Setiap push otomatis redeploy; URL `https://research-pipeline.pages.dev`.

> Karena `index.html` sudah final di repo, **tidak perlu build step CI**.
> Setelah mengubah isi `entri/`, jalankan `node build.js` lalu commit hasilnya.

---

## 11. Risiko & Mitigasi

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Ukuran file ±3–4 MB | Lambat di koneksi buruk | HTML polos terkompresi gzip Pages ±700–900 KB; render hanya entri aktif; font `display=swap`; tanpa request lain |
| `marked` versi CDN berubah | Build tak reproducible | Versi dipin `12.0.0` + disimpan di `vendor/` (repo) |
| Breakout `</script>` dari konten | HTML rusak | Sanitasi `<` → `\u003c` saat serialisasi JSON (§5.1) |
| Nama berkas baru tak cocok pola | Entri hilang diam-diam | Build gagal keras + daftar berkas bermasalah |
| DOM daftar 202 item berat di HP | Scroll tersendat | Baris entri super ringan (2 span); bila perlu naik ke windowing sederhana (render 50 di sekitar scroll) |

---

## 12. Kriteria Keberhasilan Akhir

1. Satu `index.html` dibuka langsung (file://) **dan** via Pages menampilkan
   Beranda tanpa error konsol, tanpa request wajib selain font.
2. Seluruh 202 entri + TEMUAN dapat dibuka, tabel & tautan ter-render benar.
3. Pencarian "cross-modal fusion" menampilkan entri relevan < 150 ms.
4. Filter tema + tahun + query bekerja bersamaan dan ter-refleksi di URL.
5. Mode gelap/terang konsisten di semua komponen; preferensi tersimpan.
6. `#/042` disalin ke tab baru langsung membuka entri 042.
7. `node build.js` meregenerasi file identik-fungsional kapan pun.
8. Tampilan 360px-4K rapi: drawer mobile, TOC hilang di layar sempit, kolom
   baca tetap 720px di layar lebar.
9. Tidak ada emoji, gradasi mencolok, shadow berat, atau font terlarang —
   kesan akhir: *editorial, mahal, tenang*.

> **Langkah berikutnya:** Fase 1 — unduh `vendor/marked.min.js` dan tulis
> `build.js` bagian pemindaian & serialisasi data.

---

## 13. Lampiran A — Skema Lengkap CSS Custom Properties

```css
:root{
  /* warna */
  --bg:#F7F6F3; --surface:#FFFFFF; --surface-2:#FBFAF8;
  --ink:#1F2328; --ink-2:#6B6F76; --ink-3:#9A978F;
  --line:#E8E6E1; --line-strong:#D9D6CF;
  --accent:#9F2F2D; --accent-bg:#FDEBEC; --accent-ink:#9F2F2D;
  --mark:#FBF3DB;
  /* tipografi */
  --serif:'Newsreader',Georgia,'Times New Roman',serif;
  --sans:'Plus Jakarta Sans','Helvetica Neue',system-ui,sans-serif;
  --mono:'JetBrains Mono','SF Mono',Consolas,monospace;
  /* geometri */
  --r-card:12px; --r-btn:6px; --r-pill:999px;
  --topbar-h:56px; --sidebar-w:300px; --toc-w:240px; --read-w:720px;
  /* motion */
  --ease:cubic-bezier(.32,.72,0,1); --dur:240ms;
  --shadow-hover:0 2px 12px rgba(31,35,40,.05);
}
html[data-theme="dark"]{
  --bg:#141311; --surface:#1C1B18; --surface-2:#181715;
  --ink:#E8E6E1; --ink-2:#A39F96; --ink-3:#6E6A62;
  --line:#2B2A26; --line-strong:#3A3833;
  --accent:#D98A86; --accent-bg:rgba(217,138,134,.12); --accent-ink:#E5A9A4;
  --mark:rgba(251,243,219,.14);
  --shadow-hover:0 2px 12px rgba(0,0,0,.35);
}
```

**Palet 17 tema** (bg / ink — terang; gelap memakai bg `rgba` 12%):

| Tema | bg | ink |
|---|---|---|
| Fondasi RGB | `#E1F3FE` | `#1F6C9F` |
| Survei YOLO | `#E1F3FE` | `#1F6C9F` |
| YOLO plus RGB-D | `#DAEFFB` | `#175E8C` |
| RGB-D SOD | `#EDF3EC` | `#346538` |
| Segmentasi RGB-D | `#E6F0E4` | `#2F5C33` |
| Estimasi Kedalaman | `#FBF3DB` | `#956400` |
| Pose 6D | `#F3EDF7` | `#6B4E8E` |
| Deteksi 3D | `#EFEAF6` | `#5D4A86` |
| Grasp Robotik | `#FDEBEC` | `#9F2F2D` |
| RGB-D SLAM | `#FDEFF0` | `#8E3A52` |
| Pedestrian RGB-T | `#FDF0E4` | `#97550F` |
| Pertanian | `#F0F4DF` | `#5E7016` |
| Medis | `#E4F4F1` | `#0F6E63` |
| Industri | `#EEF0F2` | `#4E5A66` |
| Remote Sensing | `#E8F0FA` | `#3A5C94` |
| Fusi Multimodal | `#F5EEFB` | `#7A4FA0` |
| Dataset | `#F2F0EB` | `#6B6552` |
| Sintesis (TEMUAN) | `#1F2328` | `#FFFFFF` (solid ink, beda sendiri) |

---

## 14. Lampiran B — Pseudokode Runtime `app.js`

```
init()
  theme.init()            // baca localStorage / prefers-color-scheme
  buildIndex()            // normalisasi teks utk pencarian (lazy per entri)
  router.mount()          // hashchange -> route()
  sidebar.mount()         // render chip tema, select tahun, daftar
  shortcuts.mount()       // /, Esc, panah, t, ?
  reveal.mount()          // IntersectionObserver .rv
  route(location.hash)    // layar awal

route(hash)
  {path, query} = parse(hash)          // "#/", "#/042", "#/temuan", "?q=..&tema=..&thn=.."
  state.filter = query
  sidebar.applyFilter(state.filter)    // -> filtered[]  (disimpan utk prev/next)
  switch path:
    ""        -> viewHome()            // statistik, timeline, grid tema, jalur baca
    "temuan"  -> viewEntry(SPECIAL)
    /^\d{3}$/ -> viewEntry(byId[path]) // 404 inline bila tak ada
  window.scrollTo(0,0); toc.build(); progress.reset()

viewEntry(e)
  html = marked.parse(e.md, {renderer: custom})   // tabel dibungkus, link eksternal, heading id
  header = entryHeader(e)                          // eyebrow, judul, meta, copy bib, tautan
  nav    = prevNext(e, sidebar.filtered)
  main.innerHTML = header + html + nav
  spy.observe(main.querySelectorAll('h2,h3'))      // scroll-spy TOC
  localStorage.rp-last = e.id

search(q)
  nq = norm(q)                                       // lowercase + strip diakritik
  for e in DATA: score = 5*has(e.title)+3*has(e.theme)+1*has(e.md)
  return top results (cache norm per entri di Map)
```

---

## 15. Lampiran C — Checklist Uji Manual (Fase 4)

**Konten**
- [ ] 10 entri acak lintas tema: semua tabel rapi & bisa di-scroll horizontal di HP
- [ ] Tautan Google Scholar / Semantic Scholar di setiap entri terbuka di tab baru
- [ ] Tidak ada sisa sintaks Markdown mentah (`|`, `##`, `**`) yang terlihat
- [ ] TEMUAN tampil sebagai entri pin paling atas dengan label SINTESIS

**Navigasi**
- [ ] `#/001` -> `#/202` semua bisa dibuka; id tak dikenal -> pesan 404 anggun
- [ ] Prev/next mengikuti urutan filter aktif
- [ ] Tombol anchor `#` pada H2 menghasilkan URL yang bisa dibuka ulang ke posisi sama

**Pencarian & filter**
- [ ] `q=fusion` -> hasil < 150 ms, istilah tersorot `<mark>`
- [ ] Kombinasi tema "RGB-D SOD" + tahun 2021 + query "transformer"
- [ ] Reset filter mengembalikan 202 entri; URL ikut bersih

**Tampilan**
- [ ] 360px: drawer buka/tutup, hamburger morph X, konten tak terpotong
- [ ] 768px: TOC hilang, sidebar drawer; 1440px: 3 kolom penuh
- [ ] Gelap/terang: semua warna ikut berubah, tersimpan setelah reload
- [ ] Tidak ada layout shift besar saat font ter-loading (display=swap)

**Kualitas**
- [ ] Konsol bersih; Lighthouse A11y >= 95; kontras teks AA
- [ ] Ukuran `index.html` <= 5 MB; gzip transfer Pages < 1 MB
