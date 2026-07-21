# CLAUDE.md — Memori Proyek

Panduan kerja untuk Claude Code di repositori ini. Baca sebelum mengubah apa pun.

## Bahasa

**Seluruh isi repo dan seluruh percakapan memakai Bahasa Indonesia.** Istilah teknis
asing ditulis miring dan dijelaskan singkat saat pertama muncul (lihat
`docs/PANDUAN-PENULISAN.md`). Jangan beralih ke Inggris kecuali diminta.

## Apa Ini

Repositori **tinjauan pustaka** untuk riset deteksi objek berbasis YOLO dan fusi
RGB-D. Bukan repo kode eksperimen. Isinya: korpus ringkasan makalah, naskah LaTeX,
basis data sitasi, dan aplikasi web statis untuk membaca korpus.

| Angka | Nilai |
|---|---|
| Entri di ledger (`references.bib`) | 202 |
| Entri terverifikasi (ada PDF lokal) = korpus naskah | **182** (`entri/`) |
| Entri ditahan (PDF sumber tak tersedia) | 20 (`entri-withheld/`) |
| Klaster tema | 14 |
| Rentang fokus | 2019–2026 (+ fondasi 2012–2018) |

Angka 182 itu **invarian yang dijaga**: naskah, situs, `TEMUAN.md`, dan
`docs/claim-audit-182.md` semuanya diselaraskan ke angka ini. Jika mengubah jumlah
entri, seluruh berkas tersebut harus ikut diperbarui.

## Peta Berkas

| Berkas / folder | Isi |
|---|---|
| `evidence-body.tex` | **Isi naskah aktif.** Semua penyuntingan naskah masuk ke sini. |
| `main.tex` / `main-elsarticle.tex` | Driver IEEEtran / Elsevier; keduanya `\input` `evidence-body.tex`. |
| `tinjauan-pustaka.tex` | Draf lama mandiri — **tidak dipakai**; jangan disunting tanpa diminta. |
| `entri/` | 182 berkas ringkasan (satu makalah = satu berkas) + `INDEX.md`. |
| `entri-withheld/` | 20 entri ditahan; jangan dimasukkan ke naskah. |
| `references.bib` | 202 record BibTeX. |
| `TEMUAN.md` | Sintesis lintas makalah. |
| `figures/` | Figur final F01–F08 (`-en.jpg`), C01, C02, plus brief `.md`-nya. |
| `docs/` | Rencana, panduan, audit, matriks bukti. `docs/archive/` = draf usang. |
| `build.js` | Perakit `index.html` (Ruang Baca Riset). |
| `index.html` | **Hasil build — jangan disunting tangan.** |
| `tools/build_evidence_matrix.py` | Membangun matriks bukti dari `entri/` + `PDF/`. |

## Perintah

```bash
node build.js --dry      # laporan saja, tidak menulis
node build.js            # rakit ulang index.html
```

`build.js` tanpa dependensi (`fs`/`path` saja, marked di-vendor). Jalankan setiap
kali `entri/*.md` atau `TEMUAN.md` berubah, lalu commit `index.html` bersamaan.

Kompilasi naskah: `latexmk -pdf main.tex` (dan `main-elsarticle.tex`).

`tools/build_evidence_matrix.py` butuh `pypdf` dan folder `PDF/benar/` yang
**tidak ada di git** (di-gitignore, terlalu besar). Skrip akan gagal tanpa itu —
itu perilaku normal, bukan bug.

## Kontrak Teknis Berkas Entri (melanggar = merusak build web)

Diambil dari `docs/PANDUAN-PENULISAN.md` §2 — baca lengkap sebelum menulis entri.

- Nama berkas: `NNN - YYYY - Judul singkat - Tema.md`. **Jangan diubah.**
- Baris pertama = judul `# NNN - Judul`. **Jangan diubah.**
- Tabel metadata **wajib** memuat `| Kunci BibTeX | \`kunci\` |` — diparse `build.js`.
- Heading hanya `##` dan `###`. Tidak ada `#` selain baris pertama.
- **Dilarang gambar.** Diagram ASCII dianjurkan (maks 1–2/bab, fenced code block,
  lebar ≤78 kolom, harus faktual).
- Tautan antar-entri: relatif, spasi di-encode `%20`.
- Satu tugas = satu berkas. Jangan menyentuh berkas lain.

Aturan isi: **jangan mengarang angka**. Setiap klaim numerik harus terlacak ke
sumber primer (arXiv/DOI/repo resmi). Ini repo yang seluruh nilainya bertumpu pada
keterlacakan.

## `_config.yml` (GitHub Pages)

`entri/`, `tools/`, `docs/extracted/`, `docs/archive/`, `PDF/`, `tmp/` di-exclude dari
build Jekyll. Situs yang tayang = `index.html` hasil `build.js`. Menambah folder besar
baru? Pertimbangkan menambahkannya ke exclude.

## Konteks Riset Berjalan (per Juli 2026)

Tinjauan pustaka **sudah selesai ditulis**. Fokus sekarang bergeser ke eksperimen.

**Dataset:** SawitMVC — <https://huggingface.co/datasets/ULM-DS-Lab/SawitMVC>
(CC BY-NC 4.0). 953 pohon, 3.992 gambar 960×1280, 4–8 sisi per pohon, 18.540 bbox,
9.823 *unique bunch*, 4 kelas kematangan B1–B4, split pohon 716/96/141.
Rasio duplikasi lintas-sisi k ≈ 1,89. **Belum ada salinan lokal di workspace ini
(~2,44 GB).**

**Baseline yang sudah dipublikasi** — Indriani, Saputro, Muttaqin dkk., *SawitMVC:
A multi-view oil palm fruit bunch dataset for detection and counting*, Data in Brief
67 (2026) 112990, DOI `10.1016/j.dib.2026.112990`, gold OA. **PDF ada di repo:**
`docs/SawitMVC A multi-view oil palm fruit bunch dataset for detection and counting.pdf`
(teks terekstrak: `/workspace/experiments/refs/dib-text.txt`). Angka di bawah sudah
**diverifikasi langsung dari PDF** (Tabel 3 hal. 12, Tabel 4 hal. 12) — boleh dikutip.

Tabel 3 — deteksi YOLO26m, test split:

| | AP50 | Precision | Recall |
|---|---|---|---|
| Overall | 0,531 | 0,508 | 0,571 |
| B1 | 0,739 | 0,602 | 0,776 |
| B2 | 0,433 | 0,482 | 0,441 |
| B3 | 0,599 | 0,515 | 0,674 |
| **B4** | **0,354** | 0,432 | 0,393 |

Tabel 4 — counting, test 141 pohon (Class ±1 / Tree ±1 / Macro MAE / Mean Bias):

| Deteksi | Counter | Class ±1 | Tree ±1 | MAE | Bias |
|---|---|---|---|---|---|
| GT | Naïve sum | 50,00% | 6,38% | 2,142 | +2,142 |
| GT | Koreksi global k=1,89 | 95,57% | 86,52% | 0,356 | +0,009 |
| GT | SVR | **96,81%** | 88,65% | 0,303 | −0,048 |
| YOLO26m | Koreksi global | 72,34% | 30,50% | 1,119 | 0,381 |
| YOLO26m | SVR | **75,35%** | 33,33% | 1,027 | 0,158 |

**Baseline DiB itu sengaja TIDAK di-tuning** (kutipan: "deliberately simple reference
points rather than tuned systems"). Konfigurasinya: YOLO26m `epochs=60, batch=32,
imgsz=640, patience=60, seed=42` — perhatikan **imgsz=640 pada citra 960×1280**.
SVR: RBF, default scikit-learn (C=1.0, eps=0.1, gamma="scale"), **tanpa pencarian
hyperparameter dan tanpa standardisasi fitur**, 4 model terpisah per kelas, fitur
13-dimensi lintas-sisi. Artinya: angka DiB adalah *titik acuan*, bukan plafon hasil
tuning. Plafon yang pengguna maksud berasal dari eksperimen tuning mereka sendiri
di luar naskah — jangan mencampuradukkan keduanya.

Fakta lain dari PDF yang berguna:

- 908 pohon (95,3%) difoto 4 sisi, 45 pohon (4,7%) 8 sisi. 10 model smartphone,
  eksposur otomatis, potret 960×1280.
- k = 1,8905 dihitung **hanya dari train** (14.041 bbox / 7.427 bunch) → tidak bocor
  ke test. Dataset-wide 18.540/9.823 = 1,887.
- Identitas bunch lintas-sisi diturunkan sebagai **connected component (transitive
  closure)** dari graf `_confirmedLinks`.
- **`class_mismatch`**: flag otomatis saat kelas yang dianotasi berbeda antar-sisi
  dalam satu komponen. Ini aset yang belum dipakai — ia mengukur ambiguitas
  kematangan (B2/B3) langsung dari data, bukan dari asumsi.
- Limitasi yang diakui penulis: dua perkebunan di Kalimantan, satu periode
  pengambilan (Februari 2026) — tidak menangkap variasi musiman.

**Diagnosa yang sudah disepakati dengan pengguna — jangan diulang/ditawar lagi:**

1. Bottleneck ada di **detektor**, bukan di tahap counting. Counter sudah nyaris
   sempurna bila diberi deteksi bersih (bukti: jurang 96,81% → 75,35%).
2. **Tuning sudah habis dijalankan** (batch, imgsz, hyperparameter). Jangan
   menyarankan tuning lagi. Yang dibutuhkan perubahan arsitektur.
3. Kegagalan deteksi terbelah dua, dan pemisahan ini penting:
   - **(A) geometris** — B4 kecil/tertanam/tertutup pelepah, bunch bertumpuk.
     Di sinilah depth relevan.
   - **(B) fotometrik** — ambiguitas kematangan B2↔B3. Depth **tidak** akan
     menolong di sini. Jangan menjanjikan sebaliknya.

**Hipotesis kerja (bersumber dari korpus sendiri):** tambahkan *pseudo-depth* dari
RGB smartphone yang sudah ada, difusikan secara **middle/late — bukan early**
(temuan sapuan 28 titik fusi Ophoff dkk., `evidence-body.tex` §174), dengan
**gating kualitas depth** (*filter-before-fuse* ala SA-Gate entri 055; D3Net entri
037 menunjukkan depth buruk justru merusak prediksi). Rujukan pendukung lain: CMX
(058), CIR-Net (046).

**Model depth yang tersedia di korpus — jangan hanya menyebut V2:**

- **entri 175 — Depth Anything V2** (2024, `yang2024depthanythingv2`). Monokular,
  via `transformers`, Apache-2.0. Baseline paling matang.
- **entri 198 — Depth Anything 3** (2025, `lin2025depthanything3`, arXiv 2511.10647,
  ByteDance Seed; disitasi di `evidence-body.tex` §133). Menerima **sembarang jumlah
  pandangan** dan menghasilkan geometri **konsisten lintas-pandangan** + pose kamera.
  Bukan lewat `transformers` — perlu paket `depth-anything-3` dari GitHub. Bobot
  CC BY-NC 4.0 (sejalan dengan lisensi SawitMVC).
- Pendukung: 067 DPT, 068/071 MiDaS, 177 Metric3D, 178 Marigold, 199–202
  (survei metrik, AsyncMDE, UniDAC, FocusDepth).

**Peluang DA3 yang belum dieksploitasi:** SawitMVC punya 4–8 sisi per pohon, dan
inti masalah counting adalah *duplikasi lintas-sisi* (k ≈ 1,89; 63,8% bunch tampak
dari tepat 2 sisi) yang sekarang ditangani secara statistik (bagi k / SVR). Bila DA3
berhasil merekonstruksi geometri pohon yang konsisten, penautan bunch lintas-sisi
bisa dikerjakan **secara geometris** (bunch sama = titik 3D sama) alih-alih ditaksir.
Risikonya nyata dan harus diuji lebih dulu pada beberapa pohon: sisi berjarak ~90°
= *baseline* lebar dengan tumpang tindih rendah, objek menutupi dirinya sendiri
(pelepah), dan foto diambil berurutan sehingga kanopi dapat bergerak tertiup angin.

**Caveat yang wajib tetap disampaikan, jangan dihaluskan:**

- Pseudo-depth berasal dari RGB yang sama → *error*-nya berkorelasi. Ia prior
  struktural, bukan sensor independen (`evidence-body.tex` §133).
- **Tidak ada satu pun benchmark RGB-D pada FFB sawit di korpus 182.** Jadi "depth
  menaikkan angka" berstatus **hipotesis desain yang falsifiable**, bukan hasil
  terjamin.
- Hasil naik di B4/*crowded* tapi datar di B2/B3 = **konfirmasi teori**, bukan
  kegagalan eksperimen. Laporkan apa adanya.

**Rencana eksperimen** (resep `evidence-body.tex` §271–275): (1) generate
pseudo-depth untuk train/test; (2) latih varian YOLO middle-fusion dua cabang vs
baseline RGB; (3) bandingkan **terstratifikasi menurut oklusi**, khususnya pada B4.

## Cara Kerja yang Diharapkan

- Laporkan hasil apa adanya. Kalau eksperimen gagal atau angka tidak naik, katakan
  langsung dengan bukti — jangan dibungkus.
- Sitasi ke korpus lokal sebutkan nomor entri dan/atau seksi `evidence-body.tex`
  agar pengguna bisa memverifikasi sendiri.
- Sebelum mengubah angka agregat (182, 202, 20), periksa dampaknya ke `TEMUAN.md`,
  `README.md`, `evidence-body.tex`, dan `docs/claim-audit-182.md`.
