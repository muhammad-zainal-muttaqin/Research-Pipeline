# AGENTS.md — Panduan Kerja Agen

Berlaku untuk semua agen (Claude Code, Codex, dan lainnya). `CLAUDE.md` hanya
mengimpor berkas ini. Nomor bagian dirujuk berkas lain (terutama §3 dan §7);
jangan diubah.

## 1. Bahasa

Isi repo dan percakapan memakai **Bahasa Indonesia baku** (EYD V). Istilah teknis
asing ditulis miring dan dijelaskan singkat saat pertama muncul. Nama pustaka,
perintah, dan berkas tetap dalam bahasa aslinya. Naskah LaTeX untuk jurnal
ditulis dalam bahasa Inggris.

**Penyampaian kepada manusia.** Jawaban di percakapan dan dokumen yang dibaca
peninjau ditulis agar dipahami sekali baca, tanpa mengorbankan ketepatan untuk
agen.

- Pokok lebih dahulu, kalimat pendek, satu gagasan per kalimat. Istilah awam
  ditulis dahulu dan kode internal menyusul dalam kurung, misalnya "artikel yang
  menggabungkan beberapa foto (C1)". Kode verifikasi dijelaskan di
  `literature/scopus-2026-09/verifikasi/ISTILAH.md`.
- Setiap folder kerja punya satu pintu masuk manusia (`README.md`) yang menjawab
  tiga hal: apa isi folder, posisi sekarang, dan langkah berikutnya. Rincian
  teknis untuk agen (aturan data, perintah, asal-usul isian model) ditaruh di
  berkas terpisah, misalnya `SERAH-TERIMA.md`, dan ditautkan dari bagian
  "Untuk agen".
- Satu fakta, satu tempat. Keputusan yang menunggu peninjau hanya dicatat di
  satu daftar (untuk verifikasi: `verifikasi/TUGAS.md`); status tidak
  digandakan di beberapa berkas.
- Butir tugas memakai pola tetap: pertanyaan yang dapat dijawab, tautan relatif
  ke lembar yang dibuka, nomor baris atau saringan kolom, dan dampaknya
  (misalnya "angka naskah berubah").
- Angka di dokumen manusia dihitung ulang dari data saat dokumen diperbarui,
  bukan disalin dari catatan lama.

## 2. Isi Repo

Dua jalur riset tentang tandan buah segar (TBS) kelapa sawit:

1. **Tinjauan pustaka** untuk jurnal terindeks Scopus. Naskah aktif `main6`:
   tinjauan sistematis tentang identitas lintas pandang (*cross-view identity*)
   dalam pencacahan buah berbasis citra, dari korpus Scopus September 2026.
2. **Eksperimen deteksi** yang menguji keputusan teknis dari tinjauan itu.

## 3. Kondisi Terkini

| Jalur | Status |
|---|---|
| Naskah | Hanya **`main6`** yang aktif (Muttaqin & Indriani; kelas Elsevier `cas-dc`, sitasi penulis-tahun; 34 halaman, 12 seksi, 2 lampiran, 10 gambar, 6 tabel). `main`–`main5v3` adalah arsip: jangan disunting atau dirujuk. |
| Korpus `main6` | Scopus Search API, 28 September 2026: 6.491 rekaman → 5.889 unik → 5.723 disaring judul → 1.144 dinilai kelayakannya → **1.001 masuk peta** (2012–2026). Kode: C1 195 · C2 238 · C3 176 · C4 49 · C5 135 · R 120 · T 88. Angka terkini selalu di `literature/scopus-2026-09/ANGKA-NASKAH.md`. **Verifikasi: peninjau mulai dari `literature/scopus-2026-09/verifikasi/README.md` (tugas di `TUGAS.md`); agen membaca `SERAH-TERIMA.md` dahulu.** |
| Hasil deteksi final | **RF-DETR-L E-021**: test mAP50 **0,6038**, mAP50-95 **0,2770** (SawitMVC). Kutip hanya dari `experiments/METRICS.md`. |
| Replikasi E-021 | F-004 (3 seed): rerata test mAP50 0,5949, SD seed 0,0049. |
| Depth sensor (E-022…E-033b) | Pipeline reproyeksi tervalidasi, tetapi **tidak ada klaim peningkatan deteksi yang sah**. |
| Seri F | Ditutup 6 Agustus 2026. Rincian: `experiments/SERI-F.md`. |
| Sasaran terbuka | mAP50-95 0,30 (kurang ±0,023). |

Titik masuk: `manuscript/source/main6-body.tex` (naskah),
`literature/scopus-2026-09/README.md` (korpus), `experiments/STATUS.md`
(eksperimen), `README.md` (peta repo).

## 4. Peta Berkas

| Lokasi | Isi |
|---|---|
| `literature/scopus-2026-09/` | Korpus `main6`: `PROTOKOL.md`, `QUERY.md`, `topik/` (kueri, rekaman, penyaringan, `bukti/`), `pdf/` dan `teks/` |
| `literature/scopus-2026-09/verifikasi/` | `cek-1-…` sampai `cek-6-…` mengikuti rencana Bu Fatma dan hanya memuat bahan peninjau. Pintu masuk manusia `README.md`; keputusan yang menunggu peninjau `TUGAS.md`; arti kode `ISTILAH.md`; catatan teknis `SERAH-TERIMA.md`. Keluaran model ada di `hasil-kerja-ai/`: `menunggu-acc/` (draf), `putaran-kedua/` (sudah diterapkan). Cadangan lama di `arsip/` |
| `literature/entries/` | 182 ringkasan makalah korpus lama (dasar Ruang Baca dan naskah arsip) |
| `literature/withheld/` | 20 entri ditahan; jangan masuk naskah |
| `manuscript/source/` | `main6.tex`, `main6-body.tex`, `references6.bib`; berkas `main`–`main5v3` adalah arsip |
| `manuscript/figures/main6/` | Gambar F01–F10 (keluaran skrip) |
| `manuscript/guides/` | Panduan penulisan dan `POLA-TINJAUAN-PUSTAKA.md`; artikel contoh yang dirujuk panduan ada di `literature/example/` |
| `manuscript/output/papers/` | PDF hasil kompilasi |
| `experiments/` | `STATUS.md`, `EKSPERIMEN.md` (log), `METRICS.md`, `SERI-F.md`, `SR/`, `code/` (peta: `PETA-SKRIP.md`) |
| `pipeline/` | Deliverable produksi: YOLO 4 kanal untuk kamera Orbbec Gemini |
| `tools/scopus/` | Pipeline korpus `main6` |
| `site/build.js` → `index.html` | Ruang Baca Riset; `index.html` hasil build, **jangan disunting tangan** |
| `datasets/`, `literature/pdf/` | Bahan lokal besar, tidak masuk Git |
| `legacy/`, `temp/`, `tmp/` | Abaikan kecuali diminta |

**Invarian 182:** bila jumlah entri korpus lama berubah, perbarui juga
`literature/synthesis.md`, `README.md`, `manuscript/source/evidence-body.tex`,
dan `audit/claim-audit-182.md`. Invarian ini tidak berlaku untuk `main6`.

## 5. Perintah

```bash
node site/build.js --dry        # laporan saja
node site/build.js              # rakit ulang index.html

cd manuscript/source
tectonic main6.tex              # latexmk/pdflatex tidak tersedia

python3 tools/scopus/kode_bukti.py       # matriks bukti
python3 tools/scopus/gambar_tinjauan.py  # gambar F01–F10
python3 tools/scopus/tabel_lampiran.py   # Lampiran A
python3 tools/scopus/lampiran_kueri.py   # Lampiran B
```

- Perintah lengkap ada di `literature/scopus-2026-09/README.md`. Kunci API
  Elsevier dibaca dari `ELSEVIER_API_KEY` / `ELSEVIER_API_KEY_FILE` dan tidak
  pernah disimpan di repo.
- Jalankan `build.js` setiap kali `literature/entries/*.md`,
  `literature/synthesis.md`, atau laporan eksperimen berubah; commit `index.html`
  bersamaan.
- Pindahkan PDF hasil `tectonic` ke `manuscript/output/papers/`.

## 6. Kontrak Berkas Entri (melanggar = build web rusak)

- Nama berkas `NNN - YYYY - Judul singkat - Tema.md` dan baris pertama
  `# NNN - Judul` tidak boleh diubah.
- Tabel metadata wajib memuat `| Kunci BibTeX | \`kunci\` |`.
- Heading hanya `##` dan `###`. Tidak ada gambar; diagram ASCII ≤78 kolom.
- Tautan antar-entri relatif, spasi di-encode `%20`.
- **Jangan mengarang angka.** Setiap klaim numerik terlacak ke sumber primer.
- Kunci BibTeX `sapkota2024yoloagri` (penulis sebenarnya Alif & Hussain) dan
  `alif2024yoloevolution` (penulis sebenarnya Jegham dkk.) sengaja tidak diganti;
  di teks naskah, sebut nama penulis sebenarnya.

## 7. Kontrak Naskah `main6`

- Setiap angka korpus di naskah harus dapat dihitung ulang dari
  `literature/scopus-2026-09/` dengan skrip `tools/scopus/`. Bila data atau kode
  manual berubah, jalankan ulang skrip lalu perbarui teks naskah, `PROTOKOL.md`,
  dan §3 berkas ini.
- `main6-appendix-c1.tex`, `main6-appendix-queries.tex`, `references6.bib`, dan
  `manuscript/figures/main6/F0*` adalah keluaran skrip; **jangan disunting tangan**.
- Kode mekanisme C1 dan kode C3 disunting di `topik/bukti/mekanisme_C1.txt` dan
  `kode_C3.txt`; berkas itu menimpa kode otomatis `kode_bukti.py`.
- Naskah tidak memuat jalur folder atau kode internal repo.
- Penyaringan dilakukan satu peninjau dengan bantuan model bahasa besar;
  nyatakan apa adanya, jangan diklaim sebagai dua peninjau independen.
- Hasil eksperimen SawitMVC (E-/F-) bukan bagian korpus `main6`; bila dikutip,
  angkanya dari `experiments/METRICS.md`.

## 8. Log Eksperimen — Wajib

Setiap temuan eksperimen dicatat ke `experiments/EKSPERIMEN.md` dalam giliran
yang sama dengan selesainya eksperimen, lalu di-commit.

- **Append-only.** Koreksi ditulis sebagai entri baru yang merujuk entri lama.
- Satu entri = satu hipotesis yang dapat dipalsukan; kriteria pemalsuan ditulis
  sebelum hasil dilihat.
- Hasil negatif dan tidak konklusif dicatat apa adanya.
- Cantumkan nama skrip di `experiments/code/` yang menghasilkan angka.
- Setiap angka mAP menyebut **split** dan dihitung dengan **pycocotools protokol
  tunggal**; `hasil.json` ultralytics tidak dipakai membandingkan antar lengan.
- Penomoran: seri E sampai E-033b, seri F sampai F-009. Seri baru memakai
  prefiks baru.

## 9. Keputusan yang Mengikat — Jangan Ditawar Ulang

1. **Tuning sudah habis dijalankan.** Jangan menyarankan tuning hyperparameter
   dan jangan meminta bukti angka plafonnya.
2. Teknik siap pakai dari literatur (termasuk SAHI) sudah dicoba dan tidak
   menaikkan mAP. Yang diminta: dekomposisi *first-principles* dan perubahan
   formulasi atau arsitektur.
3. Perangkat keras sudah diputuskan: **depth sensor Orbbec Gemini**, masukan 4
   kanal (`pipeline/README.md`).

Diagnosis yang disepakati:

- Bottleneck ada di **detektor**, bukan counter.
- Kegagalan terbelah dua: **(A) geometris** — B4 kecil, tertanam, atau tertutup
  pelepah, tempat depth relevan; **(B) fotometrik** — ambiguitas kematangan
  antarkelas, yang tidak ditolong depth. Kelas paling ambigu adalah **B2**; AP
  rendah B4 adalah kegagalan deteksi.
- `class_mismatch` nol dari 7.328 tandan (E-001) adalah pemeriksa integritas
  data, bukan bukti tentang ambiguitas; jangan diulang atau dikutip untuk itu.

Jalur yang sudah dipalsukan atau dihentikan (jangan diusulkan ulang tanpa
perubahan mendasar): pseudo-depth sebagai pemisah tandan (SR-005), detektor dua
tahap (SR-012), fusi awal E-022 sebagai bukti peningkatan, klaim plafon
kematangan E-016, K3 lintas-sisi (F-003), gate init-nol F-007.

## 10. Fakta Dataset

**Arah kelas:** **B1 = MATANG** (jingga-merah) → **B4 = MENTAH** (gelap
kehijauan). Jangan dibalik.

| Dataset | Isi |
|---|---|
| **SawitMVC** (HF `ULM-DS-Lab/SawitMVC`) | 953 pohon, 4–8 sisi, 3.992 citra 960×1280, 18.540 bbox, 9.823 tandan unik, split pohon 716/96/141 |
| **Sawit** (master mentah) | 3.992 JPG 3024×4032 + 45 video. Nama berkas **tidak unik** antar folder `Kelompok N`; pemetaan ke anotasi harus berbasis isi |
| **SawitMVC-Depth** (HF, private) | 352 pohon, 1.408 citra RGB 1280×800, 2.299 kotak, depth Orbbec Y16 848×480 mm. Distribusi kelas berbeda; **mAP di sini tidak sebanding dengan E-021** |

Jebakan SawitMVC-Depth:

1. Sidecar `"alignedTo": "color"` menyesatkan; buffer masih di grid depth. Pakai
   `experiments/code/build/reproject_depth.py`, bukan `cv2.resize`.
2. Ada dua unit kamera; baca kalibrasi **per berkas**.
3. Rentang depth **0,8–15,0 m**.

Baseline publikasi: Indriani dkk., *Data in Brief* 67 (2026) 112990. YOLO26m
test AP50 0,531. Baseline itu sengaja tidak di-tuning; ia titik acuan, bukan
plafon.

## 11. Cara Kerja

- Laporkan hasil apa adanya, termasuk kegagalan, dengan bukti.
- "GPU/CPU jangan menganggur" berarti mempercepat todo yang sudah ada, **bukan**
  menambah eksperimen baru tanpa diminta.
- Paralelisme dibatasi VRAM (RTX A4500 20,4 GB; RF-DETR-L @1280 ~10,3 GB,
  paralelisme 1). Periksa `nvidia-smi --query-gpu=memory.free` sebelum
  menyalakan run berikutnya.
- Subagen: jangan menjalankan puluhan agen Opus; untuk pekerjaan massal per
  makalah pakai Haiku. Penilaian buta berarti konteks baru tanpa kode model,
  hasil sebelumnya, atau petunjuk lain.
- **Keluaran model untuk verifikasi ditulis ke
  `literature/scopus-2026-09/verifikasi/hasil-kerja-ai/menunggu-acc/<cek>/`
  dahulu**, bukan ke folder `cek-N`. Setiap draf baru dicatat di
  `verifikasi/TUGAS.md` sebagai butir berbahasa awam (pertanyaan, berkas yang
  dibuka, dampak); asal-usul teknisnya dicatat di `SERAH-TERIMA.md`.
  Berkas baru dipindah atau diisikan ke folder `cek-N` setelah pengguna
  menyetujuinya secara eksplisit; butirnya lalu dihapus dari `TUGAS.md`.
- Isian lembar verifikasi yang berasal dari model harus ditandai demikian di
  kolom `catatan`; jangan disajikan sebagai bacaan peninjau.
- Klaim tentang depth berstatus hipotesis yang dapat dipalsukan.
- Temuan yang mengubah cara kerja jangka panjang dicatat di berkas ini, bukan di
  log eksperimen.
