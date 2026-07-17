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

Vibe: **Katalog** — "indeks perpustakaan modern" untuk dokumen akademik:
tipografi serif sebagai suara utama, hairline 1px sebagai pemisah, nomor indeks
mono, satu aksen merah bata. Tanpa kartu berlapis/bento; kedalaman visual
dibangun dari ritme baris dan ruang, bukan bayangan atau tekstur.

### 6.1 Palet (CSS custom properties, mode terang)

| Token | Nilai | Pakai untuk |
|---|---|---|
| `--bg` | `#FAF9F6` | kanvas aplikasi (kertas terang) |
| `--surface` | `#FFFFFF` | area baca / latar baris |
| `--surface-2` | `#F4F2EC` | sidebar / panel sekunder |
| `--ink` | `#1A1D21` | teks utama (bukan hitam murni) |
| `--ink-2` | `#5E6267` | teks sekunder / meta |
| `--line` | `#E6E3DA` | hairline 1px di mana-mana |
| `--accent` | `#A03028` | merah bata — tautan, state aktif |
| `--accent-bg` | `#F8E9E5` | latar aksen sangat lembut |

**Aksen tema (17 tema + Sintesis)** — satu hue jewel-tone per tema dengan
saturasi/lightness seragam, dipakai sebagai `--tc` (dot, chip, bar porsi peta
tema, kolom Tema di katalog). Daftar lengkap di `THEME_COLORS` dalam runtime
(lihat §13).

**Mode gelap:** warm charcoal — `--bg:#171613`, `--surface:#1F1E19`,
`--ink:#E9E6DD`, `--ink-2:#A7A296`, `--line:#2C2A24`; aksen `#E2988E`. Diset
via `html[data-theme="dark"]`; default mengikuti `prefers-color-scheme`.

### 6.2 Tipografi

| Peran | Font stack | Skala |
|---|---|---|
| Serif editorial (judul, hero, **isi artikel**) | `'Newsreader', 'Georgia', serif` — Google Fonts, `opsz` | hero 44–74px; H1 entri 30–44px; body bacaan 17.5px / 1.78 |
| Sans UI (label, sidebar, tabel, tombol) | `'Plus Jakarta Sans', 'Helvetica Neue', system-ui, sans-serif` — Google Fonts | 11.5–15px, weight 400/500/600 |
| Mono (meta, nomor indeks, kunci BibTeX, kbd) | `'JetBrains Mono', 'SF Mono', monospace` — Google Fonts | 10–12px, letterspacing lebar untuk label |

Font dimuat via `<link>` Google Fonts dengan `display=swap`; **tanpa internet
situs tetap utuh** (fallback Georgia + system-ui tetap editorial). Lebar kolom
baca `max-width: 740px`.

### 6.3 Kaidah visual

- **Tanpa** gradasi mencolok, tanpa shadow berat, tanpa emoji, tanpa kartu
  berlapis (pola double-bezel dihapus). Pemisah utama = hairline
  `1px solid var(--line)` dan ruang putih; radius 10px (kartu) / 6px (tombol).
- **Bahasa indeks:** daftar datar berpemisah hairline (peta tema, jalur baca,
  katalog) menggantikan grid kartu; mono untuk semua angka & meta.
- **Shadow** hanya ultra-tipis: `0 1px 10px rgba(26,29,33,.07)` saat hover.
- **Motion:** semua transisi `cubic-bezier(.32,.72,0,1)` 180ms; scroll-reveal
  via `IntersectionObserver` (`translateY(12px) + opacity 0 → 1`, stagger
  `calc(var(--i)*45ms)`); hanya `transform` & `opacity` yang dianimasi.
- **Ikon:** SVG inline custom garis tipis 1.5–1.7px (search, sun/moon, arrow,
  copy, check, book, spark) — tanpa library ikon.
- **Tanpa grain/tekstur** — kanvas bersih.
- `kbd` untuk shortcut: `border:1px solid var(--line); border-bottom-width:2px; border-radius:4px; background:var(--surface-2); font mono 10.5px`.

---

## 7. Tata Letak & Halaman

Aplikasi punya 3 "layar" (semua dalam satu file, di-switch via hash router):

### 7.1 Kerangka umum

Dua mode tata letak, di-switch router lewat kelas `body.on-home` / `body.on-entry`:

```
BERANDA (#/)                            ENTRI (#/042)
┌───────────────────────────────────────┐   ┌───────────────────────────────────────┐
│ TOPBAR (sticky, h=52px, blur)         │   │ TOPBAR + progress baca 2px            │
│  ☰ │ ⌘K Cari…       Tema ◐  Bantuan ? │   │                                       │
├─────────┬─────────────────────────────┤   ├──────────────────────────────┬────────┤
│ SIDEBAR │  KONTEN (max-w 1080px)      │   │  ARTIKEL terpusat            │ TOC    │
│ 300px   │  hero · stats · timeline ·  │   │  max-w 740px                 │ layang │
│ saring  │  peta tema · KATALOG · jalur│   │  (sidebar tersembunyi ≥981px)│ ≥1260px│
└─────────┴─────────────────────────────┘   └──────────────────────────────┴────────┘
 < 980px: sidebar jadi drawer overlay (hamburger morph → X) di kedua mode
```

Sidebar **khusus penyaring** — daftar entri pindah ke tabel Katalog di kolom
utama Beranda; mode entri memakai kolom tunggal terpusat.

### 7.2 Layar Beranda (`#/`)

1. **Hero editorial:** eyebrow mono `TINJAUAN PUSTAKA · 2012–2026`, judul serif
   besar "Ruang Baca Riset\nYOLO · RGB · RGB-D", lede 1 kalimat, dua CTA:
   [Mulai dari Temuan →] (solid ink) dan [Jelajahi katalog 202 entri] (ghost,
   scroll ke katalog). Baris "Lanjutkan membaca" (mono + judul italic serif).
2. **Strip statistik:** satu baris ber-hairline atas-bawah, 4 sel (202 entri ·
   17 tema · rentang tahun · ±X jam baca); angka besar serif, label mono uppercase.
3. **Timeline per tahun:** bar chart murni CSS (batang tipis, label tahun mono;
   hover → tooltip angka; klik → filter tahun itu dan scroll ke katalog).
4. **Peta tema:** daftar datar 17 baris (dot warna, nama, 2 judul contoh, bar
   porsi, jumlah mono); klik baris → filter tema dan scroll ke katalog.
5. **Katalog:** tabel indeks seluruh entri — kolom No / Judul / Tema / Tahun /
   Baca (menit); header kolom bisa diklik untuk mengurutkan (asc/desc; TEMUAN
   selalu ter-pin di atas); klik baris (atau Enter/Space) membuka entri;
   mengikuti penyaring sidebar + pencarian, istilah cocok tersorot `<mark>`.
6. **"Mulai di sini":** 4 jalur baca terkurasi dengan chip entri cepat. Tiap
   jalur diberi bobotnya sendiri (jumlah entri + estimasi menit), bukan nomor
   urut — keempatnya sejajar, bukan langkah berurutan.
7. Footer: hairline, info mono (jumlah entri, tanggal build, cara regenerasi
   `node build.js`, tautan `tinjauan-pustaka.tex` & `references.bib`).

### 7.3 Layar Entri (`#/042`)

- **Tautan balik:** `← Katalog` (mono) kembali ke Beranda dengan filter aktif.
- **Header entri:** eyebrow `ENTRI 042 / 202 · 2021 · chip tema berwarna` →
  judul serif → baris meta mono (kunci BibTeX dengan tombol salin, estimasi
  waktu baca, tautan Scholar/Semantic Scholar yang diekstrak dari isi).
- **TOC melayang:** `position:fixed` di margin kanan (hanya ≥1260px); item
  aktif di-highlight via scroll-spy `IntersectionObserver`.
- **Isi:** hasil render `marked` dengan styling bacaan — **body serif
  Newsreader 17.5px / 1.78**:
  - tabel → dibungkus `.table-wrap` (scroll horizontal di mobile), sans 13.5px,
    header `surface-2`, border hairline;
  - blockquote → pull-quote italic, border-left 2px aksen (tanpa latar);
  - tautan eksternal → aksen, underline saat hover, `target=_blank rel=noopener`;
  - HR → penanda `···` mono terpusat;
  - heading H2/H3 diberi anchor `#` yang muncul saat hover (deep-link).
- **Navigasi bawah:** kartu hairline « Entri sebelumnya / berikutnya » (nomor +
  judul), menghormati urutan filter aktif (jika datang dari hasil filter,
  prev/next mengikuti daftar terfilter).
- **Progress baca:** bar 2px aksen di bawah topbar mengikuti scroll artikel.

### 7.4 Layar Sintesis (`#/temuan`)

Sama seperti layar entri, tetapi: TEMUAN di-pin sebagai baris pertama katalog
(nomor `§`, judul italic), eyebrow berlabel "SINTESIS", dan jadi tujuan CTA
utama Beranda.

### 7.5 Sidebar (khusus penyaring)

- **Search box** dengan ikon, `placeholder: Cari judul, tema, isi…`, tombol
  clear; hasil live (debounce 120ms) diterapkan ke katalog di Beranda.
- **Chip tema** (toggle multi-select; dot warna tema + jumlah) dengan tombol
  "+ Semua N tema" / "− Ringkas"; chip aktif memakai warna temanya.
- **Select tahun** + tombol Reset.
- **Hitungan** hasil penyaringan ("17 dari 202 entri") atau ringkasan korpus.
- **Catatan kaki** kecil: penjelasan bahwa penyaring diterapkan ke katalog +
  ringkasan pintasan.
- Di mode entri (≥981px) sidebar tersembunyi (kolom baca tunggal terpusat);
  di layar sempit (<980px) ia jadi drawer overlay di kedua mode.

---

## 8. Spesifikasi Fitur (runtime `app.js` inline)

| # | Fitur | Detail implementasi |
|---|---|---|
| F1 | Router hash | `hashchange` → parse `#/`, `#/042`, `#/temuan`, query `?q=&tema=&thn=`; render layar; scroll ke atas; simpan riwayat filter |
| F2 | Render Markdown | `marked.parse(md)` + renderer custom: tabel dibungkus div, tautan eksternal `target=_blank`, heading diberi `id` slug + anchor; **sanitasi**: konten milik sendiri (tepercaya), tetap set `marked` `headerIds` manual & hindari injeksi lewat pencarian (input user hanya dipakai untuk `<mark>` via `textContent`) |
| F3 | Pencarian full-text | Normalisasi (lowercase, strip diakritik via `normalize('NFD')`); skor: judul ×5, tema ×3, isi ×1; hasil diurut skor lalu nomor; `<mark>` pada judul di baris katalog (lewat `textContent`, bukan HTML); render seluruh hasil — tabel katalog ringan, tak perlu batas |
| F4 | Filter tema & tahun | Multi-select tema (Set), single-select tahun; kombinasi AND dengan query; URL ikut berubah (replaceState) |
| F5 | Mode gelap/terang | Toggle topbar; `localStorage.rp-theme`; default `prefers-color-scheme`; transisi warna 250ms |
| F6 | TOC + scroll-spy | Heading dipungut dari DOM (`h2, h3`) sesudah render, bukan dari data build; TOC melayang hanya ≥1260px & disembunyikan bila heading < 2; `IntersectionObserver` + klik → smooth scroll |
| F7 | Progress baca | `scroll` listener (passive, rAF-throttle) pada kontainer konten → lebar bar |
| F8 | Prev/Next | Berdasar daftar terfilter terakhir (atau urutan nomor bila tanpa filter) |
| F9 | Shortcut keyboard | `/` atau `Ctrl/⌘+K` fokus search · `Esc` clear/tutup drawer · `←/→` prev/next entri · `t` toggle tema · `?` buka modal bantuan shortcut (grid kbd) |
| F10 | Salin tautan & BibTeX | Tombol copy di header entri → `navigator.clipboard` + feedback ikon check 1,2s |
| F11 | Waktu baca | `words/200` menit, dibulatkan; tampil di meta entri & total di Beranda |
| F12 | Scroll-reveal | `IntersectionObserver` pada `.rv` (hero, judul seksi, strip stat, timeline, katalog, header entri), stagger lewat `--i` |
| F13 | Drawer mobile | Sidebar jadi overlay; hamburger 2 garis morph → X (rotate ±45°); kunci scroll body saat terbuka |
| F14 | State baca terakhir | `localStorage.rp-last` = id entri; Beranda menampilkan chip "Lanjutkan: 042 …" bila ada |
| F15 | Deep-link heading | `#/042#metodologi--arsitektur` → scroll ke heading setelah render |
| F16 | Katalog terurut | Klik `th[data-sort]` (No/Judul/Tema/Tahun/Menit) → toggle naik-turun, panah ↑↓ di header; entri sintesis dipin di atas apa pun urutannya; baris bisa dibuka via klik atau Enter/Spasi |

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
- [ ] Tulis CSS lengkap (token terang/gelap, dua mode tata letak, tipografi
      bacaan serif, tabel, blockquote, chip, strip stat, indeks tema, katalog,
      drawer, kbd, motion) di dalam template `build.js`
- [ ] Tulis markup kerangka (topbar, sidebar penyaring, main, toc melayang,
      modal bantuan)
- [ ] **Cek:** buka `index.html` dummy (data 3 entri) di browser → layout
      responsif 360px / 768px / 1440px benar

### Fase 3 — Runtime app
- [ ] Router hash + render Beranda / Entri / Temuan + kelas mode `body`
- [ ] Integrasi `marked` + renderer custom + anchor heading
- [ ] Sidebar penyaring: chip tema, filter tahun, pencarian + `<mark>`;
      katalog sortable di Beranda (render baris, klik/Enter → entri)
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
8. Tampilan 360px-4K rapi: drawer mobile, TOC melayang hanya ≥1260px, kolom
   baca 740px di layar lebar, kolom katalog menyusut anggun di layar sempit.
9. Tidak ada emoji, gradasi mencolok, shadow berat, atau font terlarang —
   kesan akhir: *editorial, mahal, tenang*.

> **Langkah berikutnya:** Fase 1 — unduh `vendor/marked.min.js` dan tulis
> `build.js` bagian pemindaian & serialisasi data.

---

## 13. Lampiran A — Skema Lengkap CSS Custom Properties

```css
:root{
  /* warna */
  --bg:#FAF9F6; --surface:#FFFFFF; --surface-2:#F4F2EC; --surface-3:#ECE9E1;
  --ink:#1A1D21; --ink-2:#5E6267; --ink-3:#8B8778;
  --line:#E6E3DA; --line-strong:#D4D0C4;
  --accent:#A03028; --accent-bg:#F8E9E5; --accent-ink:#A03028;
  --mark:#FCEEC5; --mark-ink:#5A4300;
  /* tipografi */
  --serif:'Newsreader',Georgia,'Times New Roman',serif;
  --sans:'Plus Jakarta Sans','Helvetica Neue',system-ui,sans-serif;
  --mono:'JetBrains Mono','SF Mono',Consolas,monospace;
  /* geometri */
  --r-card:10px; --r-btn:6px; --r-pill:999px;
  --topbar-h:52px; --sidebar-w:300px; --toc-w:220px; --read-w:740px; --home-w:1080px;
  /* motion */
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
```

**Palet 17 tema + Sintesis** (satu hue jewel-tone per tema, dipakai sebagai
`--tc` untuk dot, chip, bar porsi, dan kolom Tema katalog):

| Tema | hue | Tema | hue |
|---|---|---|---|
| Fondasi RGB | `#2B6CB0` | Grasp Robotik | `#B0433F` |
| Survei YOLO | `#2F7D5B` | RGB-D SLAM | `#A04763` |
| YOLO plus RGB-D | `#0E7490` | Pedestrian RGB-T | `#A9611A` |
| RGB-D SOD | `#3F7A44` | Pertanian | `#6C8018` |
| Segmentasi RGB-D | `#617A1F` | Medis | `#128577` |
| Estimasi Kedalaman | `#A6740E` | Industri | `#5C6875` |
| Pose 6D | `#7A5AA0` | Remote Sensing | `#2E86AB` |
| Deteksi 3D | `#4F46A5` | Fusi Multimodal | `#8B5CB4` |
| Dataset | `#7C755E` | Sintesis (TEMUAN) | `#A03028` (aksen utama) |

---

## 14. Lampiran B — Pseudokode Runtime `app.js`

```
init()
  setTheme(localStorage['rp-theme'] ?? prefers-color-scheme)
  buildChips(); buildYears()          // sidebar penyaring: chip tema + select tahun
  if (!location.hash) location.replace('#/')
  route()                             // layar awal
  // listener terpasang di scope modul: hashchange -> route, keydown global,
  // input pencarian (debounce 120ms), tombol tema/menu/bantuan/reset

route()
  {path, query, heading} = parseHash()  // "#/", "#/042?q=..&tema=A|B&thn=2021", "#/042#slug"
  applyQueryToState(query)              // state.q, state.tema{}, state.thn
  if (path tidak berubah)               // filter berubah saja -> jangan render ulang layar
    renderList(); scrollToHeading?; return
  body.classList.toggle('on-home' / 'on-entry')   // dua mode tata letak
  renderList()                          // hitung state.ordered + gambar katalog/daftar
  teardownObservers()
  path == '' | '/'  -> viewHome()       // hero, stat, timeline, peta tema, katalog, jalur baca
  byId[path]        -> viewEntry(e)     // termasuk 'temuan' (special)
  selain itu        -> view404(path)
  scrollTo(0,0); updateProgress(); closeDrawer(); main.focus()

viewEntry(e)
  main.innerHTML = entryHeader(e) + marked.parse(e.md) + prevNext(e)
  enhance(main, e)     // bungkus tabel, link eksternal -> target=_blank, id+anchor pada h2/h3
  buildTOC(heads, e); spy(heads)         // TOC melayang, scroll-spy IntersectionObserver
  localStorage['rp-last'] = e.id
  // prevNext mengikuti state.ordered (urutan filter aktif), fallback ke ENTRIES penuh

computeList()                            // dipanggil renderList()
  terms = norm(state.q).split()          // lowercase + strip diakritik
  for e in DATA:
    lolos filter tema/tahun?  -> tidak: lewati
    terms kosong              -> skor 0
    selain itu                -> skor = 5*hit(judul) + 3*hit(tema) + 1*hit(isi)
  state.ordered = terurut (skor desc, lalu num) bila ada query; selain itu num asc
  // haystack ter-normalisasi di-cache per entri (ensureHay)
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
- [ ] Baris katalog bisa dibuka lewat klik maupun Enter/Spasi (keyboard)
- [ ] Klik batang timeline & baris tema menyaring katalog, lalu URL ikut berubah
- [ ] Klik header kolom katalog mengurutkan naik/turun (No, Judul, Tema, Tahun)

**Pencarian & filter**
- [ ] `q=fusion` -> hasil < 150 ms, istilah tersorot `<mark>`
- [ ] Kombinasi tema "RGB-D SOD" + tahun 2021 + query "transformer"
- [ ] Reset filter mengembalikan 202 entri; URL ikut bersih
- [ ] `/` atau Ctrl/Cmd+K dari layar entri: pulang ke katalog lalu fokus ke kotak cari

**Tampilan**
- [ ] 360px: drawer buka/tutup, konten tak terpotong, tabel katalog bisa di-scroll
- [ ] 768px: sidebar jadi drawer, katalog tetap terbaca
- [ ] 1260px+: TOC melayang muncul di layar entri; di bawah itu tersembunyi
- [ ] Mode entri: sidebar penyaring tersembunyi, kolom baca terkunci 740px
- [ ] Gelap/terang: semua warna ikut berubah, tersimpan setelah reload
- [ ] Tidak ada layout shift besar saat font ter-loading (display=swap)

**Kualitas**
- [ ] Konsol bersih; Lighthouse A11y >= 95; kontras teks AA
- [ ] Ukuran `index.html` <= 5 MB; gzip transfer Pages < 1 MB
