# AGENTS.md — Panduan Kerja Agen

Berlaku untuk semua agen (Claude Code, Codex, dan lainnya). Baca sampai habis
sebelum mengubah apa pun. Kondisi di bawah per **29 September 2026**.

## 1. Bahasa

Seluruh isi repo dan percakapan memakai **Bahasa Indonesia baku** (EYD V).
Istilah teknis asing ditulis miring dan dijelaskan singkat saat pertama muncul
(`manuscript/guides/PANDUAN-PENULISAN.md`). Nama pustaka, perintah, dan berkas
tetap dalam bahasa aslinya. Naskah LaTeX untuk jurnal ditulis dalam bahasa
Inggris.

## 2. Isi Repo

Repo ini menyatukan dua jalur riset tentang tandan buah segar (TBS) kelapa sawit:

1. **Tinjauan pustaka** untuk jurnal terindeks Scopus. Naskah aktif `main6`
   adalah tinjauan sistematis tentang identitas lintas pandang (*cross-view
   identity*) dalam pencacahan buah berbasis citra, dibangun dari korpus Scopus
   September 2026. Korpus lama 182 entri (deteksi YOLO/DETR dan fusi RGB-D)
   tetap ada sebagai bahan latar dan dasar naskah `main`–`main5v3`.
2. **Eksperimen deteksi** yang menguji keputusan teknis dari tinjauan itu.

## 3. Kondisi Terkini

| Jalur | Status |
|---|---|
| Naskah | Kandidat aktif **`main6`** — *Cross-View Identity in Image-Based Fruit Counting: A Systematic Review and Design Space for Class-Wise Inventories* (Muttaqin & Indriani; IEEEtran). 22 halaman, 12 seksi + 2 lampiran (A: matriks bukti 187 kajian C1, B: string kueri Scopus), 7 gambar, 5 tabel isi. Ditulis ulang dari awal pada 28 September 2026 mengikuti `manuscript/guides/POLA-TINJAUAN-PUSTAKA.md`. `main5v3` (*design-space review* berbasis kasus, 27 September 2026) berstatus **usang** (*deprecated*) dan diarsipkan; jangan disunting maupun dirujuk. Hanya `main6` yang aktif. |
| Korpus `main6` | Scopus Search API, 28 September 2026 (UTC), 13 eksekusi kueri (Q1–Q7, Q8a–Q8e, Q9): 6.491 rekaman → 5.889 unik → 5.723 disaring judul → 1.124 dinilai kelayakannya → **971 masuk peta** (2012–2026). Kode: C1 187 · C2 231 · C3 170 · C4 49 · C5 129 · R 119 · T 86. Mekanisme asosiasi M0–M5. PDF akses terbuka 331 dari 971. `references6.bib` 1.031 rekord, 271 dikutip. Protokol: `literature/scopus-2026-09/PROTOKOL.md`. |
| Hasil deteksi final | **RF-DETR-L E-021**: test mAP50 **0,6038**, mAP50-95 **0,2770** (SawitMVC, protokol `pycocotools` tunggal). Kutip hanya dari `experiments/METRICS.md`. |
| Replikasi E-021 | F-004 (3 seed): rerata test mAP50 0,5949, SD seed **0,0049**. |
| Depth sensor (E-022…E-033b) | Pipeline reproyeksi tervalidasi, tetapi **tidak ada klaim peningkatan deteksi yang sah**. YOLO26n: depth merugikan (E-027). Titik fusi (E-032): tidak konklusif, `mid` hanya indikasi. |
| Seri F (formulasi di atas RF-DETR-L) | **Ditutup 6 Agustus 2026.** F-002 dan F-005 lolos gerbang; F-003 gugur (K3 dibatalkan); F-007 dihentikan karena gate γ tidak pernah terbuka; F-006 dan F-009 tidak dijalankan. Rincian: `experiments/SERI-F.md`. |
| Sasaran terbuka | mAP50-95 0,30 (kurang ±0,023). |

Titik masuk: `manuscript/source/main6-body.tex` (naskah), `literature/scopus-2026-09/README.md`
(korpus naskah), `experiments/STATUS.md` (eksperimen), `README.md` (peta repo).

## 4. Peta Berkas

| Lokasi | Isi |
|---|---|
| `literature/scopus-2026-09/` | **Korpus `main6`**: `QUERY.md`, `PROTOKOL.md`, `topik/` (kueri, rekaman, penyaringan, `bukti/matriks_bukti.csv`, kode manual `mekanisme_C1.txt` dan `kode_C3.txt`), `metodologi/` (60 artikel panduan review), `verifikasi/` (Cek 1–6 rencana verifikasi Bu Fatma 29 September 2026; salinan rencana di `verifikasi/rencana/index.html`), `pdf/` + `teks/` (331 PDF akses terbuka), `unduhan/pdf_belum_ada.csv` |
| `literature/entries/` | **182** ringkasan makalah terverifikasi (korpus lama, dasar naskah `main`–`main5v3` dan Ruang Baca) + `INDEX.md`, `INDEX-TAHUN.md` |
| `literature/withheld/` | 20 entri ditahan (PDF tak tersedia); jangan masuk naskah |
| `literature/synthesis.md` | Sintesis lintas makalah (14 klaster tema) |
| `literature/search/` | Pencarian reprodusibel: `PROTOCOL.md`, query Q1–Q7, ekspor mentah, hasil deduplikasi/screening, angka PRISMA |
| `literature/references/` | Bahan luar: PDF baseline SawitMVC (DiB 2026), revisi dosen `revisi-dosen-2026-07-23/` |
| `manuscript/source/main6.tex` + `main6-body.tex` | **Naskah kandidat aktif** (IEEEtran, `references6.bib`); lampiran `main6-appendix-c1.tex` dan `main6-appendix-queries.tex` dibuat skrip |
| `manuscript/figures/main6/` | Gambar F01–F07 `main6` (PDF vektor + PNG) dari `tools/scopus/gambar_tinjauan.py`; `interaktif/simulator-sensus-tandan.html` |
| `manuscript/source/main5v3.tex` + `main5v3-body.tex` | **Usang** (*deprecated*; `references3.bib`); arsip, jangan disunting |
| `manuscript/source/main5v2.tex` + `main5v2-body.tex` | Usang; arsip (ringkasan `RINGKASAN-MAIN5V2.md`), jangan disunting |
| `manuscript/source/main5.tex` + `main5-body.tex` | Usang; arsip baseline revisi sebelumnya, jangan diubah |
| `manuscript/source/main.tex` / `main-elsarticle.tex` + `evidence-body.tex` | Naskah asli 182 sumber; stabil |
| `manuscript/source/main2`–`main4`, `main-elsarticle3.tex` | Iterasi gagal; arsip, jangan disunting |
| `manuscript/source/references.bib` / `references3.bib` / `references6.bib` | 219 / 235 / 1.031 record |
| `manuscript/output/papers/` | PDF hasil kompilasi |
| `manuscript/figures/`, `manuscript/guides/` | Figur final + brief; panduan penulisan, rencana, dan `POLA-TINJAUAN-PUSTAKA.md` (pola review yang dipakai `main6`) |
| `experiments/` | `STATUS.md`, `EKSPERIMEN.md` (log append-only), `METRICS.md`, `SERI-F.md`, `SR/` (laporan per ide), `results/`, `splits/` |
| `experiments/code/` | Skrip eksperimen: `train/`, `eval/`, `build/`, `analysis/`, `shell/`, `config/`. Peta: `PETA-SKRIP.md` |
| `pipeline/` | Deliverable produksi: YOLO 4-kanal untuk kamera Orbbec Gemini |
| `audit/` | Audit pra-submisi, register klaim, `evidence-matrix-v2.csv` (44 studi) |
| `tools/scopus/` | Pipeline korpus `main6`: pencarian Scopus, pengayaan abstrak, unduh/kompres PDF, pengodean bukti, gambar, tabel lampiran, lampiran kueri, BibTeX |
| `tools/` | Skrip pencarian/screening literatur lama dan pembuat matriks bukti 182 |
| `site/build.js` → `index.html` | Ruang Baca Riset; `index.html` hasil build, **jangan disunting tangan** |
| `datasets/`, `literature/pdf/` | Bahan lokal besar, tidak masuk Git |
| `legacy/`, `temp/`, `tmp/` | Usang / sementara; abaikan kecuali diminta |

**14 vs 17 tema bukan kontradiksi:** 14 = klaster taksonomi naskah, 17 = label
tema dari nama berkas yang dipakai `build.js`. Jangan disamakan.

**Invarian 182:** bila jumlah entri berubah, perbarui juga `literature/synthesis.md`,
`README.md`, `manuscript/source/evidence-body.tex`, dan `audit/claim-audit-182.md`.
Invarian ini **tidak** berlaku untuk `main6`; angka `main6` bersumber dari
`literature/scopus-2026-09/` (bagian 7).

## 5. Perintah

```bash
node site/build.js --dry        # laporan saja
node site/build.js              # rakit ulang index.html (tanpa dependensi)

cd manuscript/source
tectonic main6.tex              # kandidat aktif; latexmk/pdflatex tidak tersedia

python3 tools/scopus/kode_bukti.py       # matriks bukti dari keputusan + kode manual
python3 tools/scopus/gambar_tinjauan.py  # gambar F01–F07 main6
python3 tools/scopus/tabel_lampiran.py   # Lampiran A (matriks C1)
python3 tools/scopus/lampiran_kueri.py   # Lampiran B (string kueri)
```

Perintah lengkap (pencarian ulang, pengayaan, BibTeX) ada di
`literature/scopus-2026-09/README.md`. Kunci API Elsevier dibaca dari
`ELSEVIER_API_KEY` / `ELSEVIER_API_KEY_FILE` dan tidak pernah disimpan di repo.

- Jalankan `build.js` setiap kali `literature/entries/*.md`, `literature/synthesis.md`,
  atau laporan eksperimen berubah; commit `index.html` bersamaan.
- Pindahkan PDF hasil `tectonic` ke `manuscript/output/papers/`.
- `tools/build_evidence_matrix.py` butuh `pypdf` dan `literature/pdf/benar/`
  (tidak ada di Git); gagal tanpa folder itu adalah perilaku normal.

## 6. Kontrak Berkas Entri (melanggar = build web rusak)

- Nama berkas `NNN - YYYY - Judul singkat - Tema.md` dan baris pertama
  `# NNN - Judul` **tidak boleh diubah**.
- Tabel metadata wajib memuat `| Kunci BibTeX | \`kunci\` |`.
- Heading hanya `##` dan `###`. Tidak ada gambar; diagram ASCII ≤78 kolom,
  maksimal 1–2 per bab.
- Tautan antar-entri relatif, spasi di-encode `%20`.
- **Jangan mengarang angka.** Setiap klaim numerik terlacak ke sumber primer
  (arXiv/DOI/repo resmi).
- Kunci BibTeX `sapkota2024yoloagri` (penulis sebenarnya Alif & Hussain) dan
  `alif2024yoloevolution` (penulis sebenarnya Jegham dkk.) sengaja tidak diganti
  namanya agar sitasi lama tidak rusak; field penulisnya sudah benar. Di teks
  naskah, sebut nama penulis sebenarnya.

## 7. Kontrak Naskah `main6`

- Setiap angka korpus di naskah (jumlah rekaman, kode C1–C5/R/T, mekanisme M0–M5,
  PDF) harus dapat dihitung ulang dari `literature/scopus-2026-09/` dengan skrip
  `tools/scopus/`. Bila data atau kode manual berubah, jalankan ulang skrip lalu
  perbarui teks naskah, `PROTOKOL.md`, dan bagian 3 berkas ini.
- `main6-appendix-c1.tex`, `main6-appendix-queries.tex`, `references6.bib`, dan
  `manuscript/figures/main6/F0*` adalah keluaran skrip; **jangan disunting tangan**.
- Kode mekanisme C1 dan kode C3 disunting di `topik/bukti/mekanisme_C1.txt` dan
  `kode_C3.txt`; berkas itu menimpa kode otomatis `kode_bukti.py`.
- Naskah tidak memuat jalur folder atau kode internal repo; sebut nama kelompok
  deskriptif.
- Penyaringan dilakukan satu peninjau dengan bantuan model bahasa besar; nyatakan
  apa adanya di naskah, jangan diklaim sebagai dua peninjau independen.
- Hasil eksperimen SawitMVC (E-/F-) bukan bagian korpus `main6`; bila dikutip,
  angka tetap dari `experiments/METRICS.md`.

## 8. Log Eksperimen — Wajib

Setiap temuan eksperimen dicatat ke `experiments/EKSPERIMEN.md` **dalam giliran
yang sama** dengan selesainya eksperimen, lalu di-commit.

- **Append-only.** Koreksi ditulis sebagai entri baru yang merujuk entri lama.
- Satu entri = satu hipotesis falsifiable; kriteria pemalsuan ditulis sebelum
  hasil dilihat.
- Hasil negatif dan tidak konklusif dicatat apa adanya, tidak dinaikkan menjadi
  "menjanjikan".
- Cantumkan nama skrip di `experiments/code/` yang menghasilkan angka.
- Setiap angka mAP wajib menyebut **split** (varians split 0,0488 > varians seed,
  E-031) dan dihitung dengan **pycocotools protokol tunggal**; `hasil.json`
  ultralytics tidak boleh dipakai membandingkan antar lengan (E-025).
- Penomoran: seri E sampai E-033b, seri F sampai F-009. Seri baru memakai prefiks baru.

## 9. Keputusan yang Mengikat — Jangan Ditawar Ulang

Pernyataan pengguna (21 Juli 2026, ditegaskan dua kali):

1. **Tuning sudah habis dijalankan.** Jangan menyarankan tuning hyperparameter,
   dan jangan meminta bukti angka plafonnya.
2. Teknik siap-pakai dari literatur (termasuk SAHI) sudah dicoba dan tidak
   menaikkan mAP; kenaikan 2–5% tidak cukup. Yang diminta: dekomposisi
   *first-principles* dan perubahan formulasi/arsitektur.
3. Arah perangkat keras sudah diputuskan: **depth sensor Orbbec Gemini**, masukan
   4 kanal; aplikasi lapangan sudah ada (`pipeline/README.md`).

Diagnosa yang disepakati:

- Bottleneck ada di **detektor**, bukan counter (GT + SVR 96,81% vs YOLO26m + SVR
  75,35% Class ±1, Tabel 4 DiB).
- Kegagalan terbelah dua: **(A) geometris** — B4 kecil/tertanam/tertutup pelepah,
  tempat depth relevan; **(B) fotometrik** — ambiguitas kematangan antarkelas,
  yang tidak ditolong depth. Kelas paling ambigu adalah **B2** (0,434, E-028);
  AP rendah B4 adalah kegagalan deteksi, bukan kebingungan kelas.
- `class_mismatch` sudah diuji: **nol** dari 7.328 tandan multi-sisi (E-001).
  Itu pemeriksa integritas data, bukan ukuran ambiguitas; jangan diulang dan
  jangan dikutip sebagai bukti apa pun tentang ambiguitas.

Jalur yang sudah dipalsukan/dihentikan (jangan diusulkan ulang tanpa perubahan
mendasar): pseudo-depth sebagai pemisah tandan (SR-005), detektor dua tahap
(SR-012), fusi awal E-022 sebagai bukti peningkatan, klaim plafon kematangan
E-016 (ditarik), K3 lintas-sisi (F-003), gate init-nol F-007 (γ tidak pernah
bergerak; perlu init taknol, warmup, atau LR terpisah bila diulang).

## 10. Fakta Dataset

**Arah kelas:** **B1 = MATANG** (jingga-merah) → **B4 = MENTAH** (gelap
kehijauan). Jangan dibalik.

| Dataset | Isi |
|---|---|
| **SawitMVC** (HF `ULM-DS-Lab/SawitMVC`, CC BY-NC 4.0) | 953 pohon, 4–8 sisi, 3.992 citra 960×1280, 18.540 bbox, 9.823 tandan unik, split pohon 716/96/141, k ≈ 1,89 (dari train saja) |
| **Sawit** (master mentah) | 3.992 JPG 3024×4032 + 45 video; rasio aspek identik sehingga label YOLO ternormalisasi berlaku langsung. Nama berkas **tidak unik** antar folder `Kelompok N` (936 nama kembar); pemetaan ke anotasi harus berbasis isi |
| **SawitMVC-Depth** (HF, private, CC BY-NC 4.0) | 352 pohon, 1.408 citra RGB 1280×800, 2.299 kotak, depth Orbbec Y16 848×480 mm. Distribusi kelas terbalik (B4 hanya 6,4%). **mAP di sini tidak sebanding dengan E-021** |

SawitMVC-Depth — tiga jebakan yang sudah ditangani:

1. Sidecar `"alignedTo": "color"` **menyesatkan**; buffer masih di grid depth.
   Pakai reproyeksi penuh `experiments/code/build/reproject_depth.py`, bukan
   `cv2.resize` (meleset median 29 px). `pipeline/prepare_depth.py` hanya untuk
   keluaran Gemini yang sudah di-align SDK dan tidak membaca `.raw`.
2. Ada dua unit kamera dengan kalibrasi berbeda; baca kalibrasi **per berkas**.
3. Rentang depth **0,8–15,0 m**, bukan 0,3–8,0 m (E-033).

**Baseline publikasi:** Indriani dkk., *Data in Brief* 67 (2026) 112990,
DOI `10.1016/j.dib.2026.112990`, PDF di `literature/references/SawitMVC-DiB-2026.pdf`.
YOLO26m test AP50 0,531 (B4 0,354). Baseline itu **sengaja tidak di-tuning**
(`imgsz=640`, SVR default); ia titik acuan, bukan plafon.

## 11. Cara Kerja

- **Komputasi:** "GPU/CPU jangan menganggur" berarti mempercepat todo yang sudah
  ada, **bukan** menambah eksperimen baru tanpa diminta (insiden 1 Agustus 2026:
  sapuan 12 run tak diminta menunda G4/G6).
- **Paralelisme dibatasi VRAM**, bukan jumlah slot. RTX A4500 20,4 GB:
  yolo26n ~3,0 GB · yolo26m ~5,5 GB · yolo26l ~6,6 GB · rtdetr-l ~7,7 GB ·
  **RF-DETR-L @1280 ~10,3 GB (paralelisme = 1)**. Periksa
  `nvidia-smi --query-gpu=memory.free` sebelum menyalakan run berikutnya.
- Laporkan hasil apa adanya, termasuk kegagalan, dengan bukti.
- Sitasi korpus lokal menyebut nomor entri dan/atau seksi naskah agar dapat
  diverifikasi.
- Klaim tentang depth berstatus **hipotesis yang dapat dipalsukan**: tidak ada
  benchmark RGB-D pada TBS sawit di korpus 182, dan pseudo-depth berbagi galat
  dengan RGB sumbernya.
- Temuan yang mengubah cara kerja jangka panjang dicatat di berkas ini, bukan di
  log eksperimen.
