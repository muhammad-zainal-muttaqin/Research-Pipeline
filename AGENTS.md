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
  menggabungkan beberapa foto (C1)".
- Setiap folder kerja punya satu pintu masuk manusia (`README.md`) yang menjawab
  tiga hal: apa isi folder, posisi sekarang, dan langkah berikutnya. Rincian
  teknis untuk agen ditulis di docstring skrip dan di berkas ini, bukan di
  berkas catatan terpisah.
- Setiap berkas dapat dipahami sendiri. Arti kode, isi kolom, dan alasan
  ditulis lengkap di berkas itu, bukan dirujuk ke berkas lain atau ditulis
  sebagai nama proses ("putaran kedua (AI-2)"). Di lembar, kode ditulis bersama
  artinya, misalnya "M3 (pelacakan video)"; daftar artinya ada di
  `tools/scopus/verifikasi_istilah.py`. Berkas yang sulit dibaca diperbaiki
  langsung, bukan dijelaskan dengan berkas tambahan.
- **Jangan membuat berkas yang kelak harus dibersihkan.** Yang tidak boleh
  masuk repo: paket bacaan, JSON atau CSV mentah keluaran model, draf usul,
  cadangan (`arsip/`, `*_lama`, `cadangan_*`), salinan format lain dari isi yang
  sama (CSV dan XLSX kembar), dan berkas yang hanya menerangkan berkas lain
  (`ISTILAH`, `PANDUAN`, `SERAH-TERIMA`, `RINGKASAN`, `KEMAJUAN`, dan sejenisnya).
  Bahan kerja itu ditulis ke scratchpad sesi. Yang masuk repo hanya hasil akhir
  yang dibaca manusia dan data minimum yang dibaca skrip (di `.teknis/`). Pada
  19 Oktober 2026 folder `verifikasi` harus dibersihkan dari 667 menjadi 24
  berkas karena aturan ini dilanggar.
- Lembar untuk manusia: kode ditulis bersama artinya; Y/N ditulis ya/tidak;
  asal isian di kolom `diisi_oleh` atau `oleh`; catatan tidak memuat nama
  model, nama proses, tanggal isian, atau jalur berkas. Log perubahan memuat
  satu baris per perubahan: artikel (penulis, tahun, judul), kelompok sekarang,
  yang diubah, sebelum, sesudah, alasan sebenarnya, dan pengubah; baris yang
  mengubah keanggotaan artikel ditaruh paling atas.
- Sebelum pekerjaan diserahkan, periksa `git status`. Setiap berkas baru harus
  dibaca manusia atau dibaca skrip; selain itu dihapus. Sebelum menghapus berkas
  yang dibaca skrip, jalankan ulang `angka_naskah.py` dan pastikan angka naskah
  tidak berubah.
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
| Naskah | Hanya **`main6`** yang aktif (Muttaqin & Indriani; kelas Elsevier `cas-dc`, sitasi penulis-tahun; 34 halaman, 12 seksi, 2 lampiran, 10 gambar, 6 tabel). `main`–`main5v3` adalah arsip: jangan disunting atau dirujuk. Penulisan ulang gaya menurut `manuscript/guides/CATATAN-GAYA-TULIS-CONTOH.md` belum selesai (paragraf panjang, kolom hasil terpisah di tabel perbandingan, ringkasan sawit per subseksi). |
| Korpus `main6` | Scopus Search API, 28 September 2026: 6.491 rekaman → 5.889 unik → 5.723 disaring judul → 1.145 dinilai kelayakannya → **1.013 masuk peta**, ditambah 5 dari luar pencarian = 1.018 (2012–2026). Kode Scopus: C1 199 · C2 243 · C3 171 · C4 52 · C5 138 · R 122 · T 88; luar pencarian: C1 1 · C2 2 · C5 1 · R 1. Angka terkini selalu di `literature/scopus-2026-09/ANGKA-NASKAH.md`. **Verifikasi: Cek 1–6 selesai dan disetujui peninjau pada 19 Oktober 2026; tersisa F.4 dan 5.7 di `verifikasi/TUGAS.md`.** Belum dikerjakan: pemeriksaan ulang eksklusi tahap judul untuk kueri Q2 dan Q4–Q9 (sekitar 3.300 rekaman; Q1 dan Q3 sudah); ekstraksi teks empat PDF CSAM (`guo2023real`, `tu2026passion`, `wang2024camellia`, `zhu2022identification`) yang fonnya tanpa pemetaan Unicode. |
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
| `literature/scopus-2026-09/verifikasi/` | `cek-1-…` sampai `cek-6-…` mengikuti rencana Bu Fatma dan hanya memuat lembar peninjau. Pintu masuk `README.md`; keputusan yang menunggu peninjau `TUGAS.md`; log perubahan `log_perubahan.csv`. `.teknis/` berisi data yang dibaca skrip: log teknis, alasan label C1/C3 dan ajudikasi Cek 1 (sumber alasan log), serta dua CSV dasar angka pemeriksaan ulang tahap judul |
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
- Naskah hanya memuat metode yang diperlukan pembaca jurnal untuk menilai dan
  mengulang peta. Riwayat verifikasi internal (putaran model, ajudikasi, uji
  sanggah, pendelegasian keputusan, isi log perubahan) tidak dijabarkan di
  naskah; rinciannya cukup di repo dan bahan tambahan.
- Penyaringan dilakukan satu peninjau dengan bantuan model bahasa besar.
  Nyatakan sekali secara ringkas di metode, keterbatasan, dan deklarasi AI
  jurnal; jangan diklaim sebagai dua peninjau independen.
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
- **Usul model untuk verifikasi tidak langsung diisikan ke lembar `cek-N`.**
  Bahan kerja model disimpan di scratchpad. Setiap usul dicatat di
  `verifikasi/TUGAS.md` sebagai butir berbahasa awam (pertanyaan, berkas yang
  dibuka, dampak). Usul diisikan setelah pengguna menyetujuinya secara
  eksplisit; butirnya lalu dihapus dari `TUGAS.md`.
- Isian lembar verifikasi yang berasal dari model ditandai di kolom
  `diisi_oleh` atau `oleh` ("AI, disetujui peninjau …"); jangan disajikan
  sebagai bacaan peninjau.
- Data verifikasi diubah di sumbernya: keputusan penyaringan di
  `topik/penyaringan/abstrak_*.txt` (setiap idx tepat satu baris; rekaman yang
  dimasukkan peninjau di `abstrak_F00.txt`), label C1 di
  `topik/bukti/mekanisme_C1.txt`, label C3 di `topik/bukti/kode_C3.txt`. Setiap
  perubahan dicatat sebagai baris di `verifikasi/.teknis/log_perubahan.csv`,
  lalu `python3 tools/scopus/verifikasi_log_manusia.py` dijalankan untuk
  membuat ulang `verifikasi/log_perubahan.csv`. Log manusia tidak disunting
  tangan.
- Klaim tentang depth berstatus hipotesis yang dapat dipalsukan.
- Temuan yang mengubah cara kerja jangka panjang dicatat di berkas ini, bukan di
  log eksperimen.
