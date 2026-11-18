# AGENTS.md — Panduan Kerja Agen

Berlaku untuk semua agen (Claude Code, Codex, dan lainnya). `CLAUDE.md` hanya
mengimpor berkas ini. Nomor bagian dirujuk berkas lain (terutama §3, §7, dan
§11); jangan diubah.

Berkas ini adalah satu-satunya pusat aturan repo. Aturan yang terlalu rinci
untuk ditaruh di sini ditulis di berkas khusus berikut, dan hanya di sana.
Aturan baru ditulis di berkas ini. Berkas aturan baru hanya dibuat bila
pengguna memintanya, lalu didaftarkan di tabel ini.

| Bidang | Berkas aturan rinci |
|---|---|
| Gaya tulis naskah `main6` (nama kategori, paragraf bukti, gambar, abstrak, simpulan, daftar periksa sebelum dikirim) | `manuscript/guides/GAYA-NASKAH-MAIN6.md` |
| Pola tinjauan pustaka yang baik (dasar metodologis gaya `main6`) | `manuscript/guides/POLA-TINJAUAN-PUSTAKA.md` |
| Protokol tinjauan `main6`: kriteria, kode kelompok, tahap penyaringan | `literature/scopus-2026-09/PROTOKOL.md` |
| Penulisan entri korpus lama 182 | `manuscript/guides/PANDUAN-PENULISAN.md` (kontrak bentuk di §6) |
| Kontrak kanal ke-4 (depth) untuk model produksi | `pipeline/README.md` |
| Reproduksi E-021: data, split, lingkungan | `experiments/code/REPRODUCE.md` |
| Keputusan verifikasi yang menunggu peninjau | `literature/scopus-2026-09/verifikasi/TUGAS.md` |

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

**Kebersihan repo.**

- **Jangan membuat berkas yang kelak harus dibersihkan.** Yang tidak boleh
  masuk repo: paket bacaan, JSON atau CSV mentah keluaran model, draf usul,
  cadangan (`arsip/`, `*_lama`, `cadangan_*`), salinan format lain dari isi yang
  sama (CSV dan XLSX kembar), dan berkas yang hanya menerangkan berkas lain
  (`ISTILAH`, `PANDUAN`, `SERAH-TERIMA`, `RINGKASAN`, `KEMAJUAN`, dan sejenisnya).
  Bahan kerja itu ditulis ke scratchpad sesi. Yang masuk repo hanya hasil akhir
  yang dibaca manusia dan data minimum yang dibaca skrip (di `literature/scopus-2026-09/verifikasi/.teknis/`).
  Pengecualian: hasil ekstraksi teks lengkap per kajian oleh agen disimpan di
  `literature/scopus-2026-09/ekstraksi/` agar tidak dibaca ulang tiap sesi
  (diminta pengguna, 18 November 2026); folder itu tidak diisi bahan lain. Pada
  19 Oktober 2026 folder `verifikasi` harus dibersihkan dari 667 menjadi 24
  berkas karena aturan ini dilanggar.
- Berkas usang dihapus, bukan dipindah ke folder arsip. Pada 18 November 2026
  naskah `main2`–`main5v3`, folder `audit/` dan `legacy/`, bahan pencarian
  OpenAlex Agustus, laporan *deep research*, serta brief gambar dihapus.
  Keadaan sebelumnya tersimpan di tag Git `arsip-pra-rapi-2026-11-18`
  (`git show arsip-pra-rapi-2026-11-18:<jalur>`). Jangan memulihkannya ke
  pohon kerja kecuali diminta.

**Larangan tulisan agen.** Berlaku untuk dokumen, komentar kode, docstring,
pesan commit, dan naskah.

- **Dilarang membuat berkas Markdown yang tidak diminta.** Agen tidak membuat
  `.md` untuk menjelaskan, membela, atau merangkum pekerjaannya sendiri. Contoh
  yang dilarang: laporan sesi, catatan keputusan, rencana, ringkasan
  perubahan, dan berkas aturan baru. Penjelasan ditulis di jawaban percakapan
  atau pesan commit. Berkas `.md` baru hanya boleh dibuat bila pengguna
  memintanya, atau bila berkas itu menggantikan berkas yang ada sehingga jumlah
  berkas tidak bertambah. Larangan ini ditegakkan `.githooks/pre-commit`: commit
  yang menambah `.md` di luar entri korpus, teks terekstrak, laporan
  `experiments/SR/SR-NNN-*`, dan `README.md` ditolak. `IZINKAN_MD=1` hanya
  dipakai bila pengguna memintanya, dan `--no-verify` tidak dipakai.
- **Dilarang menimbun aturan.** Agen tidak menambah aturan atas inisiatif
  sendiri. Aturan baru hanya ditulis bila pengguna memintanya atau bila ada
  kesalahan nyata yang perlu dicegah, dalam satu butir pendek di bagian yang
  sesuai. Butir yang sudah ada diperbarui, bukan ditambah butir baru yang
  menggandakannya.
  Pelajaran yang berulang dikodekan menjadi pemeriksaan (skrip, *assert*, *hook*
  Git), bukan teks tambahan. Teks hanya untuk hal yang butuh pertimbangan.
- **Dilarang komentar sampah.** Komentar kode dihapus kecuali termasuk salah
  satu dari lima pengecualian:
  1. kepala lisensi;
  2. perilaku tak terduga yang dipaksakan pihak luar yang tidak dapat kita
     ubah, misalnya sidecar Orbbec `"alignedTo": "color"` yang menyesatkan;
  3. penanda pemformat, atau penekan *lint* yang aturannya keliru atau hanya
     soal gaya;
  4. docstring yang menetapkan kontrak skrip: masukan, keluaran, dan cara
     menjalankan;
  5. tautan ke sumber luar (makalah, isu, dokumentasi) yang menjelaskan batasan
     yang tidak dapat dinyatakan kode.

  Bila ragu apakah suatu komentar termasuk pengecualian, komentarnya dihapus.
  Perilaku mengejutkan di kode kita sendiri tidak dijelaskan dengan komentar.
  Kodenya diubah (nama, fungsi terpisah, pemeriksaan) sampai jelas tanpa
  prosa. Komentar penambal (*workaround*) diganti perbaikan akar masalah.
  Komentar bertanda "PENTING" atau "jangan dihapus" dan pembelaan panjang
  diperiksa dulu ke kode yang dirujuknya, karena belum tentu benar. Selalu
  dilarang: komentar yang mengulang kode, riwayat perubahan ("diperbaiki",
  "versi baru"), nama model atau sesi, TODO tanpa pemilik, dan kode mati yang
  dijadikan komentar. Riwayat perubahan cukup di Git.
- **Dilarang slogan.** Tidak ada slogan, kata pemasaran, atau penekanan
  kosong, misalnya "kokoh", "canggih", "siap produksi", "solusi menyeluruh",
  "game changer", atau emoji. Huruf tebal hanya untuk peringatan yang
  berakibat salah bila terlewat. Setiap kalimat harus memuat fakta yang dapat
  diperiksa.
- **Dilarang mengarang.** Setiap klaim di dokumen, komentar, atau commit
  menyebut sumbernya: data, skrip, berkas, atau keluaran perintah. Klaim yang
  belum diperiksa ditulis "belum diperiksa", bukan disajikan sebagai fakta.

**Lembar, log, dan tugas.**

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
  satu daftar (untuk verifikasi: `literature/scopus-2026-09/verifikasi/TUGAS.md`); status tidak
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
| Naskah | Hanya **`main6`** yang aktif (Muttaqin & Indriani; kelas Elsevier `cas-dc`, sitasi penulis-tahun; 34 halaman, 11 seksi, 2 lampiran, 7 gambar, 6 tabel; bahan tambahan `main6-supplementary.tex` 5 halaman). Naskah 182 sumber (`main.tex`, `main-elsarticle.tex`) hanya dipertahankan untuk Ruang Baca; iterasi `main2`–`main5v3` sudah dihapus. Badan naskah ditulis ulang pada 18 November 2026 agar setiap seksi bukti dibuka dengan klaim isi; rincian metode pindah ke bahan tambahan. |
| Korpus `main6` | Scopus Search API, 28 September 2026: 6.491 rekaman → 5.889 unik → 5.723 disaring judul → 1.145 dinilai kelayakannya → 1.013 lolos tahap abstrak (+5 dari luar pencarian) → 479 dengan PDF dinilai dari teks lengkap (539 tidak diperoleh) → **467 masuk peta** (2012–2026). Kode: C1 214 · C2 43 · C3 53 · C4 13 · C5 35 · R 62 · T 47. Korpus dibatasi pada kajian yang PDF-nya ada di `literature/scopus-2026-09/pdf/`; keputusan teks lengkap di `literature/scopus-2026-09/topik/penyaringan/teks_lengkap.txt`. Angka terkini selalu di `literature/scopus-2026-09/ANGKA-NASKAH.md`. **Verifikasi: Cek 1–6 selesai dan disetujui peninjau pada 19 Oktober 2026; tahap teks lengkap disetujui peninjau pada 18 November 2026; F.4, 5.7, A.1, dan A.3 menunggu di `literature/scopus-2026-09/verifikasi/TUGAS.md`.** Belum dikerjakan: pemeriksaan ulang eksklusi tahap judul untuk kueri Q2 dan Q4–Q9 (sekitar 3.300 rekaman; Q1 dan Q3 sudah); ekstraksi teks empat PDF CSAM (`guo2023real`, `tu2026passion`, `wang2024camellia`, `zhu2022identification`) yang fonnya tanpa pemetaan Unicode. |
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
| `literature/scopus-2026-09/ekstraksi/` | Hasil agen membaca teks lengkap: `perbandingan/` (perbandingan pada data yang sama, dasar `tab:assoc`), `tanaman-platform/`, `bacaan/` (lembar kajian inti); masing-masing dengan `prompt.txt`. Pintu masuk `README.md`. Bahan kerja, bukan sumber naskah |
| `literature/entries/`, `synthesis.md`, `extracted/` | Korpus lama: 182 ringkasan makalah, sintesis, dan teks terekstrak (dasar Ruang Baca dan naskah 182 sumber) |
| `literature/withheld/` | 20 entri ditahan; jangan masuk naskah |
| `literature/references/` | PDF baseline SawitMVC; `revisi-dosen-2026-07-23/` berisi delapan permintaan revisi dosen (`Chat.txt`, catatan primer, jangan dihapus) |
| `manuscript/source/` | `main6.tex`, `main6-body.tex`, `main6-supplementary.tex` (bahan tambahan), `main6-angka.tex` (keluaran `angka_naskah.py`), lampiran, `references6.bib`; naskah 182 sumber (`main.tex`, `main-elsarticle.tex`, `evidence-body.tex`, `references.bib`) dan `experiment-ledgers.tex` untuk laporan eksperimen |
| `manuscript/figures/main6/` | Gambar F01–F10 (keluaran skrip) |
| `manuscript/guides/` | `GAYA-NASKAH-MAIN6.md`, `POLA-TINJAUAN-PUSTAKA.md`, `PANDUAN-PENULISAN.md`; artikel contoh yang dirujuk panduan ada di `literature/example/` |
| `manuscript/reports/` | Laporan hasil eksperimen (`reports.tex` dan versi ringkas); figur rasternya di `manuscript/figures/` |
| `manuscript/output/papers/` | PDF hasil kompilasi |
| `experiments/` | `STATUS.md`, `EKSPERIMEN.md` (log), `METRICS.md`, `SERI-F.md`, `SR/`, `code/` (peta: `PETA-SKRIP.md`) |
| `pipeline/` | Deliverable produksi: YOLO 4 kanal untuk kamera Orbbec Gemini |
| `tools/scopus/` | Pipeline korpus `main6` |
| `tools/presentation/` | Pembuat dek PPTX |
| `site/build.js` → `index.html` | Ruang Baca Riset; `index.html` hasil build, **jangan disunting tangan** |
| `datasets/`, `literature/pdf/` | Bahan lokal besar, tidak masuk Git |
| `temp/`, `tmp/` | Abaikan kecuali diminta |

**Invarian 182:** bila jumlah entri korpus lama berubah, perbarui juga
`literature/synthesis.md`, `README.md`, dan `manuscript/source/evidence-body.tex`.
Invarian ini tidak berlaku untuk `main6`.

## 5. Perintah

```bash
git config core.hooksPath .githooks   # sekali per klon; mengaktifkan hook repo

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
  manual berubah, jalankan ulang skrip lalu perbarui teks naskah, `literature/scopus-2026-09/PROTOKOL.md`,
  dan §3 berkas ini.
- `main6-angka.tex`, `main6-appendix-c1.tex`, `main6-appendix-queries.tex`,
  `references6.bib`, dan `manuscript/figures/main6/F*` adalah keluaran skrip;
  **jangan disunting tangan**. Angka korpus di teks naskah ditulis sebagai
  makro dari `main6-angka.tex`, bukan diketik.
- Kode mekanisme C1 dan kode C3 disunting di `literature/scopus-2026-09/topik/bukti/mekanisme_C1.txt` dan
  `literature/scopus-2026-09/topik/bukti/kode_C3.txt`; berkas itu menimpa kode otomatis `kode_bukti.py`.
- Naskah tidak memuat jalur folder atau kode internal repo.
- **Isi lebih dahulu, cara pengumpulan sesudahnya.** Ini berlaku untuk naskah
  tinjauan dan untuk prioritas kerja agen. Pokok tinjauan adalah cara bidang
  ini menyelesaikan masalahnya:
  - asumsi setiap pendekatan;
  - kapan pendekatan berhasil dan kapan gagal;
  - perbandingan pada data yang sama;
  - pertentangan antarkajian dan sebabnya.

  Pencarian, penyaringan, pengodean, dan hitungan korpus hanya pendukung.
  - **Metode dan statistik korpus.** Keduanya ditulis sekali, di metode dan
    lanskap kuantitatif. Bersama-sama, panjangnya paling banyak seperlima badan
    naskah. Naskah hanya memuat metode yang diperlukan pembaca jurnal untuk
    menilai dan mengulang peta. Riwayat verifikasi internal (putaran model,
    ajudikasi, uji sanggah, pendelegasian keputusan, isi log perubahan) dan
    rincian prosedur ditaruh di bahan tambahan dan repo.
  - **Seksi bukti.** Seksi bukti dibuka dengan klaim tentang isi, bukan dengan
    "N dari M kajian".
  - **Paragraf bukti.** Setiap paragraf bukti ditutup dengan sintesis lintas
    kajian (pola, pertentangan, atau sebab), bukan daftar hasil per kajian.
  - **Prioritas agen.** Saat memperbaiki naskah, agen lebih dahulu membaca isi
    kajian dari teks lengkap, baru kemudian memperbaiki *pipeline* korpus.
    Laporan kemajuan kepada pengguna juga dimulai dari temuan isi.
- Penyaringan dilakukan satu peninjau dengan bantuan model bahasa besar.
  Nyatakan sekali secara ringkas di metode, keterbatasan, dan deklarasi AI
  jurnal; jangan diklaim sebagai dua peninjau independen.
- Hasil eksperimen SawitMVC (E-/F-) bukan bagian korpus `main6`; bila dikutip,
  angkanya dari `experiments/METRICS.md`.
- Klaim kebaruan dibatasi pada pencarian yang dilaporkan ("not found in the
  search reported in Section 2"), bukan "belum ada tinjauan yang membahas".
- Gaya tulis mengikuti `manuscript/guides/GAYA-NASKAH-MAIN6.md`. Daftar
  periksanya dijalankan sebelum naskah dikirim.
- Arah naskah ditetapkan delapan permintaan revisi dosen pembimbing
  (`literature/references/revisi-dosen-2026-07-23/Chat.txt`, 23 Juli 2026);
  jangan diubah tanpa persetujuan penulis:
  1. Metode pencarian dapat diulang: basis data (minimal Scopus), string
     kueri, filter tahun, kriteria inklusi dan eksklusi, deduplikasi.
  2. Kerangka naskah adalah ruang desain untuk satu tugas: mengubah banyak
     pengamatan pohon menjadi inventaris buah unik per kelas. Bukan sejarah
     YOLO/RGB-D dan bukan usulan arsitektur tunggal.
  3. Kontribusi utama: deduplikasi lintas pandang (setiap buah dihitung
     sekali), dengan pemosisian eksplisit terhadap tinjauan terdahulu.
  4. Cakupan pertanian dengan sawit sebagai kasus utama; mekanisme dari luar
     pertanian (pelacakan, re-ID, SfM) boleh dipakai sebagai bukti yang dapat
     ditransfer.
  5. Judul tanpa "YOLO", "RGB-D", dan "kelapa sawit".
  6. Klasifikasi tidak terbatas pada kematangan, tetapi tetap bergantung pada
     *instance*; kematangan hanya satu kasus.
  7. Literatur sawit dan tanaman pohon yang terlewat (Suharjito, Goh,
     penghitungan apel, jeruk, anggur) dimasukkan.
  8. Matriks bukti masuk naskah sebagai tabel sintesis (satu baris per kajian),
     bukan hanya CSV terpisah.

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
- Klaim bahwa depth menolong deteksi wajib diuji terhadap lengan kontrol
  negatif tanpa informasi (kanal ke-4 berisi derau) dengan protokol identik
  dan CI 95% bootstrap berpasangan. Bila kontrol memberi kenaikan sebanding,
  klaimnya gugur (`experiments/SR/SR-015-depth-sensor-4kanal.md` §2).
- Split SawitMVC per pohon 716/96/141 dengan irisan nol bersifat tetap; jangan
  diacak ulang. Berkas split memakai jalur absolut `/workspace/SawitMVC/...`
  (`experiments/code/REPRODUCE.md`).

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

Kanal ke-4 model produksi berisi *inverse depth* 1–255 pada rentang tetap
0,3–8 m (0 = tidak ada data). Rentang ini dibekukan bersama bobot
(`fourch.Z_NEAR/Z_FAR`); jangan menormalkan depth per citra
(`pipeline/README.md`).

Jebakan SawitMVC-Depth:

1. Sidecar `"alignedTo": "color"` menyesatkan; buffer masih di grid depth. Pakai
   `experiments/code/build/reproject_depth.py`, bukan `cv2.resize`.
2. Ada dua unit kamera; baca kalibrasi **per berkas**.
3. Rentang depth **0,8–15,0 m**.

Baseline publikasi: Indriani dkk., *Data in Brief* 67 (2026) 112990. YOLO26m
test AP50 0,531. Baseline itu sengaja tidak di-tuning; ia titik acuan, bukan
plafon.

## 11. Cara Kerja

- Verifikasi adalah langkah terpenting. Pekerjaan baru dinyatakan selesai
  setelah diperiksa dengan cara yang dapat diulang: skrip dijalankan, naskah
  dikompilasi, angka dihitung ulang, atau berkas dibaca ulang. Laporkan hasil
  apa adanya, termasuk kegagalan, dengan keluaran pemeriksaannya. Yang belum
  diperiksa disebut belum diperiksa.
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
  `literature/scopus-2026-09/verifikasi/TUGAS.md` sebagai butir berbahasa awam (pertanyaan, berkas yang
  dibuka, dampak). Usul diisikan setelah pengguna menyetujuinya secara
  eksplisit; butirnya lalu dihapus dari `TUGAS.md`.
- Isian lembar verifikasi yang berasal dari model ditandai di kolom
  `diisi_oleh` atau `oleh` ("AI, disetujui peninjau …"); jangan disajikan
  sebagai bacaan peninjau.
- Data verifikasi diubah di sumbernya: keputusan penyaringan di
  `literature/scopus-2026-09/topik/penyaringan/abstrak_*.txt` (setiap idx tepat satu baris; rekaman yang
  dimasukkan peninjau di `literature/scopus-2026-09/topik/penyaringan/abstrak_F00.txt`), label C1 di
  `literature/scopus-2026-09/topik/bukti/mekanisme_C1.txt`, label C3 di `literature/scopus-2026-09/topik/bukti/kode_C3.txt`. Setiap
  perubahan dicatat sebagai baris di `literature/scopus-2026-09/verifikasi/.teknis/log_perubahan.csv`,
  lalu `python3 tools/scopus/verifikasi_log_manusia.py` dijalankan untuk
  membuat ulang `literature/scopus-2026-09/verifikasi/log_perubahan.csv`. Log manusia tidak disunting
  tangan.
- Pekerjaan verifikasi `main6` di-commit setiap kali satu cek selesai, dengan
  pesan yang diawali nama ceknya, misalnya `Cek 4: PDF Yok-In dkk. 2026
  diperoleh`. Commit yang menyentuh beberapa cek menyebut semuanya
  (`Cek 4, Cek 5: …`). Aturan ini berasal dari rencana verifikasi Bu Fatma.
- Klaim tentang depth berstatus hipotesis yang dapat dipalsukan.
- Temuan yang mengubah cara kerja jangka panjang dicatat di berkas ini, bukan di
  log eksperimen.
