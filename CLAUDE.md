# CLAUDE.md — Memori Proyek

Panduan kerja untuk Claude Code di repositori ini. Baca sebelum mengubah apa pun.

> **Melanjutkan eksperimen?** Baca **[`docs/experiments/STATUS.md`](docs/experiments/STATUS.md)** dulu —
> titik berhenti, hasil terbaik (**RF-DETR-L test mAP50 0,6038**, E-021 —
> melewati sasaran 0,60; sebelumnya RT-DETR-L 0,5794), dan jalur lanjutan.
> Aktif per 2026-07-25 (YOLO26l @1280 param-adil **selesai**; perbandingan
> 1-protokol tuntas, lihat [SR-014](docs/experiments/SR/SR-014-rfdetr-dinov2.md)).
> Aktif per 2026-07-30: **E-022/SR-015** — depth SENSOR Orbbec diuji pada dataset
> baru `SawitMVC-Depth`; fusi 4-kanal awal **dipalsukan**, arah lanjutan = fusi
> menengah (E-023).
> Peta seluruh dokumen: [`docs/README.md`](docs/README.md).

## Bahasa

**Seluruh isi repo dan seluruh percakapan memakai Bahasa Indonesia.** Istilah teknis
asing ditulis miring dan dijelaskan singkat saat pertama muncul (lihat
`docs/manuscript/guides/PANDUAN-PENULISAN.md`). Jangan beralih ke Inggris kecuali diminta.

## Apa Ini

Repositori **tinjauan pustaka** untuk riset deteksi objek berbasis YOLO dan fusi
RGB-D. Bukan repo kode eksperimen. Isinya: korpus ringkasan makalah, naskah LaTeX,
basis data sitasi, dan aplikasi web statis untuk membaca korpus.

| Angka | Nilai |
|---|---|
| Entri di ledger (`docs/manuscript/source/references.bib`) | 202 |
| Entri terverifikasi (ada PDF lokal) = korpus naskah | **182** (`docs/literature/entries/`) |
| Entri ditahan (PDF sumber tak tersedia) | 20 (`docs/literature/withheld/`) |
| Klaster tema (taksonomi naskah `docs/literature/synthesis.md`) | 14 |
| Label tema (segmen terakhir nama berkas `docs/literature/entries/`) | 17 |
| Rentang fokus | 2019–2026 (+ fondasi 2012–2018) |

**14 dan 17 bukan kontradiksi** dan sudah direkonsiliasi saat audit
(`docs/manuscript/guides/PLAN-SITUS.md` §"Catatan rekonsiliasi sumber", `docs/manuscript/figures/C02-distribusi-tema.md` §2):
14 adalah klaster taksonomi naskah LaTeX, yang menggabungkan beberapa label berkas;
17 adalah label tema yang dipakai `build.js` dan situs, dibaca dari nama berkas.
Jangan "memperbaiki" salah satunya jadi sama.

Angka 182 itu **invarian yang dijaga**: naskah, situs, `docs/literature/synthesis.md`, dan
`docs/audit/claim-audit-182.md` semuanya diselaraskan ke angka ini. Jika mengubah jumlah
entri, seluruh berkas tersebut harus ikut diperbarui.

## Peta Berkas

| Berkas / folder | Isi |
|---|---|
| `docs/manuscript/source/evidence-body.tex` | **Isi naskah aktif.** Semua penyuntingan naskah masuk ke sini. |
| `docs/manuscript/source/main.tex` / `docs/manuscript/source/main-elsarticle.tex` | Driver IEEEtran / Elsevier; keduanya `\input` `docs/manuscript/source/evidence-body.tex`. |
| `artifacts/legacy/tinjauan-pustaka.tex` | Draf lama mandiri — **tidak dipakai**; jangan disunting tanpa diminta. |
| `docs/literature/entries/` | 182 berkas ringkasan (satu makalah = satu berkas) + `INDEX.md` (urut nomor) + `INDEX-TAHUN.md` (per tahun & tema). |
| `docs/literature/withheld/` | 20 entri ditahan; jangan dimasukkan ke naskah. |
| `docs/manuscript/source/references.bib` | 202 record BibTeX. |
| `docs/literature/synthesis.md` | Sintesis lintas makalah. |
| `docs/manuscript/figures/` | Figur final F01–F08 (`-en.jpg`), C01, C02, plus brief `.md`-nya. |
| `docs/` | Seluruh dokumen, dipecah per fungsi — **peta di `docs/README.md`**. |
| `docs/experiments/` | `STATUS.md` (baca pertama), `EKSPERIMEN.md` (log append-only), `METRICS.md` (tabel definitif), `LAPORAN-EKSPERIMEN.md` (tayang di situs), `SR/` (laporan per-ide). |
| `docs/manuscript/guides/` | Panduan penulisan, rencana naskah & situs, keputusan reframe, prompt figur. |
| `docs/audit/` | Audit pra-submisi, claim audit 182, register klaim, matriks bukti. |
| `evidence/literature/references/` | Bahan luar: PDF baseline SawitMVC, deep research report, revisi dosen. |
| `artifacts/legacy/` | Draf & figur usang. |
| `reproduce/pipeline/` | **Deliverable produksi**: pipeline YOLO 4-kanal (RGB+depth) untuk kamera Gemini — latih/konversi/inferensi. Kode kecil tanpa bobot model; bukan kode eksperimen sekali pakai. |
| `reproduce/experiments/` | **Arsip kode + hasil JSON + split** eksperimen E-001…E-022 (snapshot dari `reproduce/experiments/`, di luar repo). Skrip dikelompokkan: `train/`, `eval/`, `build/`, `analysis/`, `shell/`, `config/`; hasil di `results/E-0NN/`. Peta: `reproduce/experiments/PETA-SKRIP.md`. Tanpa bobot/dataset besar — bisa dibuat ulang dari skripnya. Di-exclude dari Jekyll. |
| `build.js` | Perakit `index.html` (Ruang Baca Riset). |
| `index.html` | **Hasil build — jangan disunting tangan.** |
| `reproduce/tools/build_evidence_matrix.py` | Membangun matriks bukti dari `docs/literature/entries/` + `evidence/literature/pdf/`. |

## Perintah

```bash
node site/build.js --dry      # laporan saja, tidak menulis
node site/build.js            # rakit ulang index.html
```

`build.js` tanpa dependensi (`fs`/`path` saja, marked di-vendor). Jalankan setiap
kali `docs/literature/entries/*.md` atau `docs/literature/synthesis.md` berubah, lalu commit `index.html` bersamaan.

Kompilasi naskah: `latexmk -pdf -outdir=artifacts/papers docs/manuscript/source/main.tex` (dan `docs/manuscript/source/main-elsarticle.tex`).

`reproduce/tools/build_evidence_matrix.py` butuh `pypdf` dan folder `evidence/literature/pdf/benar/` yang
**tidak ada di git** (di-gitignore, terlalu besar). Skrip akan gagal tanpa itu —
itu perilaku normal, bukan bug.

## Kontrak Teknis Berkas Entri (melanggar = merusak build web)

Diambil dari `docs/manuscript/guides/PANDUAN-PENULISAN.md` §2 — baca lengkap sebelum menulis entri.

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

`docs/literature/entries/`, `reproduce/tools/`, `evidence/literature/extracted/`, `artifacts/legacy/`, `evidence/literature/pdf/`, `artifacts/scratch/` di-exclude dari
build Jekyll. Situs yang tayang = `index.html` hasil `build.js`. Menambah folder besar
baru? Pertimbangkan menambahkannya ke exclude.

## Konteks Riset Berjalan (per Juli 2026)

Tinjauan pustaka **sudah selesai ditulis**. Fokus sekarang bergeser ke eksperimen.

**Dataset ketiga (per 2026-07-29): `/workspace/SawitMVC-Depth/data`** —
<https://huggingface.co/datasets/ULM-DS-Lab/SawitMVC-Depth>, CC BY-NC 4.0, repo
**private** (butuh token). 352 pohon, 1.408 citra RGB **1280×800 lanskap**, 2.299
kotak B1–B4, plus **depth sensor Orbbec** Y16 848×480 uint16 milimeter per citra.
Inilah dataset yang menutup lubang "depth SENSOR belum pernah diuji" (E-022/SR-015).

**Tiga sifat dataset itu yang wajib diingat** (semuanya terverifikasi di E-022a,
dan **ketiganya sudah ditangani** — ini keputusan yang berlaku, bukan pekerjaan
yang tertunda):

1. Sidecar `"alignedTo": "color"` **MENYESATKAN** — buffer masih di grid kamera
   depth. Berkas yang sama membantah dirinya sendiri: ia mengirim ekstrinsik
   `mTrans ≈ −23,7 mm` yang mestinya nol bila buffer benar sudah di bidang color.
   `cv2.resize` naif karena itu meleset median 29 px / maks 61 px pada 1280×800.
   **Sudah diselesaikan:** depth dataset ini diproses lewat
   `reproduce/experiments/build/reproject_depth.py` (reproyeksi penuh), dan seluruh angka E-022
   memakai jalur itu. `reproduce/pipeline/prepare_depth.py` bukan alternatif yang salah pakai —
   ia melayani kasus lain (keluaran Gemini yang sudah di-align SDK di lapangan)
   dan filter ekstensinya (`.png/.tif/.tiff`) membuatnya tidak bisa membaca `.raw`
   dataset ini sama sekali.
2. Ada **dua unit kamera** dengan kalibrasi berbeda (fx_depth 416,55 vs 414,38);
   kalibrasi wajib dibaca **per berkas** dari sidecar.
3. Rentang `fourch.Z_NEAR/Z_FAR` (0,3–8,0 m) tidak cocok untuk sensor ini —
   0,000% piksel di bawah 0,3 m, 10,07% di atas 8 m. Dipakai **0,8/15,0 m**.

Distribusi kelasnya **terbalik** dari SawitMVC lama (B2 43,5%, B1 36,1%, B3 14,0%,
B4 hanya 6,4% = 148 kotak) dan kepadatannya 1,63 kotak/citra (lama 4,64). **Angka
mAP di dataset ini TIDAK sebanding dengan 0,6038 milik E-021.**

**Dua tingkat dataset SawitMVC, sudah lengkap terunduh di workspace ini:**

| | `/workspace/Sawit/data` (master mentah) | `/workspace/SawitMVC/data` (turunan) |
|---|---|---|
| Resolusi | **3024 × 4032** | 960 × 1280 |
| Rasio aspek | 0,75 | 0,75 — **identik** |
| JPG | 3.992 (16 GB) | 3.992 (2,3 GB) |
| Video | **45 MP4**, 1920×1080, ~21 dtk (~618 frame) | — |
| Anotasi | tidak ada | label YOLO, 953 JSON, split_manifest |

SawitMVC (<https://huggingface.co/datasets/ULM-DS-Lab/SawitMVC>, CC BY-NC 4.0):
953 pohon, 4–8 sisi, 18.540 bbox, 9.823 *unique bunch*, B1–B4, split pohon
716/96/141, k ≈ 1,89. Dipakai untuk iterasi cepat.

**Arah kelas — jangan dibalik:** **B1 = MATANG** (jingga-merah), menurun sampai
**B4 = MENTAH** (gelap kehijauan). Konsekuensinya: B4 yang gelap kehijauan
adalah kelas yang paling menyatu dengan pelepah, dan itulah penjelasan fisik
dari kontras rendah yang didiagnosis di SR-007.

Sawit = master mentah yang sama, belum dibagi/dianotasi. Dipakai bila resolusi
terbukti jadi bagian bottleneck. Karena rasio aspeknya identik, **koordinat YOLO
ternormalisasi dari MVC berlaku persis di raw** — tidak perlu anotasi ulang.

**Penghalang yang sudah terverifikasi (21 Juli 2026): nama berkas raw TIDAK unik
secara global.** Dari 3.992 berkas hanya 1.352 nama unik; **936 nama kembar**
antar folder `Kelompok N` (mis. `LONSUM_A21A_044_3.jpg` ada di Kelompok 2 *dan*
5 = dua pohon berbeda). Ditambah penomoran raw 3 digit vs MVC 4 digit, pemetaan
raw ↔ anotasi **tidak bisa dari nama berkas**. Perlu pencocokan berbasis isi
(perceptual hash / downscale-and-compare) yang hasilnya wajib diperiksa — atau
tabel pemetaan dari tim. Video juga hanya bernama cap waktu
(`VID_20260205_090556.mp4`), semuanya dari Kelompok 6 saja, tanpa ID pohon.

**Nilai strategis video:** risiko terbesar rencana DA3 multi-view adalah baseline
~90° antar sisi. Video menghapus risiko itu — ratusan frame mengelilingi satu
pohon = baseline antar-frame kecil, kondisi ideal untuk geometri multi-view, dan
DA3 menerima masukan video. **Uji DA3 pada video dulu**, baru transfer ke kasus
4-sisi.

**Catatan resolusi (bukan tawaran tuning):** melatih `imgsz=1280` pada sumber
960×1280 tidak sama dengan melatih pada sumber 3024×4032 — yang pertama hanya
memperbesar piksel yang detailnya sudah hilang saat kompresi. Untuk B4 (bunch
kecil, tertanam) perbedaan ini berpotensi material. Raw adalah eksperimen yang
berbeda, bukan sekadar cadangan.

**Baseline yang sudah dipublikasi** — Indriani, Saputro, Muttaqin dkk., *SawitMVC:
A multi-view oil palm fruit bunch dataset for detection and counting*, Data in Brief
67 (2026) 112990, DOI `10.1016/j.dib.2026.112990`, gold OA. **PDF ada di repo:**
`docs/SawitMVC A multi-view oil palm fruit bunch dataset for detection and counting.pdf`
(teks terekstrak: `reproduce/experiments/refs/dib-text.txt`). Angka di bawah sudah
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
  dalam satu komponen. **SUDAH DIUJI — HASILNYA NOL. Jangan diulang.**
  `reproduce/experiments/analysis/class_mismatch_stats.py` (21 Juli 2026): 0 ketidaksepakatan dari
  7.328 bunch multi-sisi, di semua split/varietas/kelas. Parser diverifikasi
  silang dengan angka publikasi (9.823 bunch, 18.540 kemunculan, sebaran
  6.264/834/147/71/12) — cocok persis, jadi nol itu nyata, bukan bug.
  **Tafsirnya:** flag ini pemeriksa integritas data yang bersih, **bukan**
  pengukur ambiguitas kematangan. Ketidaksepakatan sudah diselesaikan sebelum
  rilis ("reviewed in full by a single reviewer, who applied corrections before
  export"). Angka nol ini **tidak** mendukung maupun membantah klaim ambiguitas
  B2/B3 — jangan pernah mengutipnya sebagai bukti salah satunya.
  **Pengganti yang masih layak:** pakai graf `_confirmedLinks` sebagai oracle
  identitas, lalu ukur inkonsistensi *prediksi detektor* pada bunch fisik yang
  sama antar-sisi. Itu mengukur ambiguitas tanpa bergantung label manusia, dan
  ukuran yang sama bisa menguji apakah depth menstabilkannya. Butuh detektor
  terlatih, jadi jalankan bersama eksperimen utama.
- Limitasi yang diakui penulis: dua perkebunan di Kalimantan, satu periode
  pengambilan (Februari 2026) — tidak menangkap variasi musiman.

**Pernyataan pengguna 21 Juli 2026 (tambahan, sama mengikatnya):** dalam
beberapa bulan terakhir mereka sudah mengimplementasikan sendiri teknik-teknik
standar dari literatur/internet — **termasuk SAHI** — dan tidak satu pun
menaikkan mAP. Kenaikan 2–5% pun dianggap tidak cukup. Konsekuensi kerja:
(a) jangan mengusulkan ulang teknik siap-pakai dari literatur sebagai solusi
utama; (b) yang diminta adalah dekomposisi first-principles dan perubahan
formulasi/arsitektur; (c) arah perangkat keras baru sudah diputuskan — kamera
**depth sensor (Orbbec Gemini)**, masukan 4 kanal; `reproduce/pipeline/` adalah
deliverable untuk itu, dan aplikasi lapangan pengguna sudah ada (tinggal ganti
model, lihat `reproduce/pipeline/README.md`).

**Diagnosa yang sudah disepakati dengan pengguna — jangan diulang/ditawar lagi:**

1. Bottleneck ada di **detektor**, bukan di tahap counting. Counter sudah nyaris
   sempurna bila diberi deteksi bersih (bukti: jurang 96,81% → 75,35%).
2. **Tuning sudah habis dijalankan** (batch, hyperparameter, ukuran input, dll.) dan
   angkanya tetap. Ini pernyataan langsung pengguna, dan **sudah ditegaskan dua
   kali** setelah asisten sempat mempertanyakannya. Jangan menyarankan tuning lagi,
   dan **jangan meminta pengguna membuktikan angka plafonnya** — itu sudah
   dijawab. Yang dibutuhkan perubahan arsitektur, bukan pencarian hyperparameter.
   (Catatan `imgsz=640` pada baseline DiB di atas tetap relevan sebagai fakta
   naskah, tetapi bukan alasan untuk menawarkan tuning ulang.)
3. Kegagalan deteksi terbelah dua, dan pemisahan ini penting:
   - **(A) geometris** — B4 kecil/tertanam/tertutup pelepah, bunch bertumpuk.
     Di sinilah depth relevan.
   - **(B) fotometrik** — ambiguitas kematangan B2↔B3. Depth **tidak** akan
     menolong di sini. Jangan menjanjikan sebaliknya.

**Hipotesis kerja (bersumber dari korpus sendiri):** tambahkan *pseudo-depth* dari
RGB smartphone yang sudah ada, difusikan secara **middle/late — bukan early**
(temuan sapuan 28 titik fusi Ophoff dkk., `docs/manuscript/source/evidence-body.tex` §174), dengan
**gating kualitas depth** (*filter-before-fuse* ala SA-Gate entri 055; D3Net entri
037 menunjukkan depth buruk justru merusak prediksi). Rujukan pendukung lain: CMX
(058), CIR-Net (046).

**Model depth yang tersedia di korpus — jangan hanya menyebut V2:**

- **entri 175 — Depth Anything V2** (2024, `yang2024depthanythingv2`). Monokular,
  via `transformers`, Apache-2.0. Baseline paling matang.
- **entri 198 — Depth Anything 3** (2025, `lin2025depthanything3`, arXiv 2511.10647,
  ByteDance Seed; disitasi di `docs/manuscript/source/evidence-body.tex` §133). Menerima **sembarang jumlah
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
  struktural, bukan sensor independen (`docs/manuscript/source/evidence-body.tex` §133).
- **Tidak ada satu pun benchmark RGB-D pada FFB sawit di korpus 182.** Jadi "depth
  menaikkan angka" berstatus **hipotesis desain yang falsifiable**, bukan hasil
  terjamin.
- Hasil naik di B4/*crowded* tapi datar di B2/B3 = **konfirmasi teori**, bukan
  kegagalan eksperimen. Laporkan apa adanya.

**Rencana eksperimen** (resep `docs/manuscript/source/evidence-body.tex` §271–275): (1) generate
pseudo-depth untuk train/test; (2) latih varian YOLO middle-fusion dua cabang vs
baseline RGB; (3) bandingkan **terstratifikasi menurut oklusi**, khususnya pada B4.

## Log Eksperimen — WAJIB

Kode eksperimen tinggal di **`reproduce/experiments/`** (di luar repo ini; repo
ini tidak menampung artefak besar, bobot model, atau keluaran gambar). Tetapi
**setiap hal penting yang dipelajari dari eksperimen wajib dicatat ke repo ini**
di [`docs/experiments/EKSPERIMEN.md`](docs/experiments/EKSPERIMEN.md).

Alasannya: tinjauan pustaka ini berdiri di atas klaim yang dapat dilacak ke
sumber. Eksperimennya harus memenuhi standar yang sama — kalau tidak, ada
asimetri antara 182 sitasi terverifikasi dan keputusan eksperimen berbasis
ingatan. Log bertanggal juga menjawab pertanyaan reviewer "apa saja yang sudah
dicoba".

Aturannya:

- **Append-only.** Jangan mengedit entri lama untuk "memperbaiki" hasil. Kalau
  kesimpulan berubah, tulis entri baru yang merujuk entri lama.
- **Hasil negatif wajib dicatat**, dengan bobot yang sama seperti hasil positif.
  Itu isi paling berharga di log ini — lihat E-001 (`class_mismatch`), sebuah
  hipotesis yang dipalsukan dan karenanya tidak perlu diulang siapa pun.
- **Satu entri = satu hipotesis yang falsifiable.** Tulis sejak awal apa yang
  akan memalsukannya, sebelum melihat hasilnya.
- **Angka apa adanya.** Kalau gagal, tulis gagal. Kalau tidak konklusif, tulis
  tidak konklusif — jangan dinaikkan jadi "menjanjikan".
- Format entri dan daftar status ada di kepala `docs/experiments/EKSPERIMEN.md`.
- Catat juga **nama skrip** di `reproduce/experiments/` yang menghasilkan angka
  itu, supaya dapat dijalankan ulang.
- Temuan yang mengubah cara kerja jangka panjang (bukan hasil satu eksperimen)
  masuk ke CLAUDE.md ini, bukan ke log.

Kapan menulis: **segera setelah eksperimen selesai**, dalam giliran yang sama —
jangan ditunda ke akhir sesi. Commit log bersama perubahan terkait.

## Cara Kerja yang Diharapkan

- Laporkan hasil apa adanya. Kalau eksperimen gagal atau angka tidak naik, katakan
  langsung dengan bukti — jangan dibungkus.
- Sitasi ke korpus lokal sebutkan nomor entri dan/atau seksi `docs/manuscript/source/evidence-body.tex`
  agar pengguna bisa memverifikasi sendiri.
- Sebelum mengubah angka agregat (182, 202, 20), periksa dampaknya ke `docs/literature/synthesis.md`,
  `README.md`, `docs/manuscript/source/evidence-body.tex`, dan `docs/audit/claim-audit-182.md`.
