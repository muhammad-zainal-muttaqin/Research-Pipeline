# AGENTS.md — Panduan Kerja Agen

Berlaku untuk semua agen (Claude Code, Codex, dan lainnya). `CLAUDE.md` hanya
mengimpor berkas ini. Nomor bagian dirujuk berkas lain (terutama §3, §7, dan
§11); jangan diubah.

Berkas ini adalah satu-satunya berkas aturan agen. Aturan baru ditulis di sini,
dan berkas aturan terpisah tidak dibuat. Empat berkas berikut bukan aturan
agen, tetapi dokumen riset yang menjadi acuan isi:

| Isi | Berkas |
|---|---|
| Protokol tinjauan `main6`: kriteria, kode kelompok, tahap penyaringan | `literature/scopus-2026-09/PROTOKOL.md` |
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
  (diminta pengguna, 18 November 2026); folder itu tidak diisi bahan lain.
- Berkas usang dihapus, bukan dipindah ke folder arsip. Berkas yang sudah
  dihapus dibaca dari Git (`git show <tag-atau-commit>:<jalur>`, misalnya tag
  `arsip-pra-rapi-2026-11-18`) dan tidak dipulihkan ke pohon kerja kecuali
  diminta.

**Larangan tulisan agen.** Berlaku untuk dokumen, komentar kode, docstring,
pesan commit, dan naskah.

- **Dilarang membuat berkas `.md` atau `.py` tentang pekerjaan agen sendiri**,
  di repo maupun di scratchpad. Berkas seperti itu menjelaskan, membela,
  memeriksa, atau merangkum pekerjaan agen, dan tidak dibaca naskah, skrip
  lain, atau peninjau.
  - Contoh `.md` yang dilarang: laporan sesi, catatan keputusan, rencana
    kerja, ringkasan perubahan, daftar kemajuan, berkas aturan baru, dan
    berkas penjelas yang disebut di "Kebersihan repo".
  - Contoh `.py` yang dilarang: pemeriksa hasil kerja agen (misalnya skrip
    yang mencocokkan setiap PDF dengan judulnya), pembuat paket bacaan untuk
    subagen, skrip audit atau pembanding sekali pakai, dan skrip yang dibuat
    hanya untuk membuktikan klaim kepada pengguna.
  - Penggantinya: penjelasan ditulis di percakapan atau pesan commit;
    pemeriksaan sekali pakai dijalankan langsung (`python - <<'EOF' ... EOF`)
    tanpa disimpan.
  - Yang boleh dibuat atau diubah: skrip `tools/scopus/` yang menghasilkan
    berkas yang dibaca naskah, skrip lain, atau lembar peninjau (misalnya
    `kode_bukti.py`, `angka_naskah.py`, `gambar_tinjauan.py`,
    `tabel_lampiran.py`, `verifikasi_log_manusia.py`); skrip
    `experiments/code/` yang menghasilkan angka di `experiments/EKSPERIMEN.md`;
    kode `pipeline/`; entri korpus; teks terekstrak; laporan
    `experiments/SR/SR-NNN-*`; `README.md`; dan `.md` yang menggantikan
    berkas yang ada sehingga jumlah berkas tidak bertambah. Berkas lain dibuat
    hanya bila pengguna memintanya.
  - Penegakan: `.githooks/pre-commit` menolak `.md` baru di luar jalur yang
    boleh dan `.py` baru di luar `tools/`, `experiments/code/`, dan
    `pipeline/`. `IZINKAN_MD=1` atau `IZINKAN_PY=1` hanya dipakai bila
    pengguna memintanya; `--no-verify` tidak dipakai.
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
  catatan tidak memuat nama
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
| Naskah | Hanya **`main6`** yang aktif (Muttaqin & Indriani; kelas Elsevier `cas-dc`, sitasi penulis-tahun; 53 halaman termasuk halaman *highlights*, 11 seksi, 2 lampiran, 9 gambar, 7 tabel; bahan tambahan `main6-supplementary.tex` 7 halaman dengan daftar periksa PRISMA 2020 di S5, ditambah daftar kajian `manuscript/output/papers/main6-supplementary-studies.csv`). Naskah 182 sumber (`main.tex`, `main-elsarticle.tex`) hanya dipertahankan untuk Ruang Baca; iterasi `main2`–`main5v3` sudah dihapus. Badan naskah ditulis ulang pada 18 November 2026 agar setiap seksi bukti dibuka dengan klaim isi; rincian metode pindah ke bahan tambahan. |
| Korpus `main6` | Scopus Search API, 28 September 2026: 6.491 rekaman → 5.889 unik → 5.723 disaring judul → 1.145 dinilai kelayakannya → 1.013 lolos tahap abstrak (+5 dari luar pencarian) → 814 dengan PDF dinilai dari teks lengkap (809 Scopus + 5 dari luar pencarian; 204 tidak diperoleh) → **789 masuk peta** (2012–2026). Kode: C1 236 · C2 132 · C3 110 · C4 33 · C5 91 · R 105 · T 82. Korpus dibatasi pada kajian yang PDF-nya ada di `literature/scopus-2026-09/pdf/`; keputusan teks lengkap di `literature/scopus-2026-09/topik/penyaringan/teks_lengkap.txt`. Angka terkini selalu di `literature/scopus-2026-09/ANGKA-NASKAH.md`. **Verifikasi: Cek 1–6 selesai dan disetujui peninjau pada 19 Oktober 2026; tahap teks lengkap disetujui peninjau pada 18 November 2026, untuk 325 PDF tambahan pada 20 November 2026 (bersama A.1 tanaman dan platform C1 dari teks lengkap, dan A.3 label C1), dan untuk 3 tinjauan tambahan pada 21 November 2026; Ni dkk. 2020 dan 2021 dikeluarkan (pencitraan laboratorium) dengan persetujuan peninjau pada 22 November 2026; 4 PDF sawit tambahan dinilai dan disetujui peninjau pada 23 November 2026 (3 masuk C3, Husin dkk. 2021 dikeluarkan); 5.7 (isian penulis) menunggu di `literature/scopus-2026-09/verifikasi/TUGAS.md`.** Belum dikerjakan: pemeriksaan ulang eksklusi tahap judul untuk kueri Q2 dan Q4–Q9 (sekitar 3.300 rekaman; Q1 dan Q3 sudah). |
| Hasil deteksi final | **RF-DETR-L E-021**: test mAP50 **0,6038**, mAP50-95 **0,2770** (SawitMVC). Kutip hanya dari `experiments/METRICS.md`. |
| Replikasi E-021 | F-004 (3 seed): rerata test mAP50 0,5949, SD seed 0,0049. |
| Depth sensor (E-022…E-033b) | Pipeline reproyeksi tervalidasi, tetapi **tidak ada klaim peningkatan deteksi yang sah**. |
| Seri F | Ditutup 6 Agustus 2026. Rincian: `experiments/SERI-F.md`. |
| Sasaran terbuka | mAP50-95 0,30 (kurang ±0,023). |

Titik masuk: `manuscript/source/main6-body.tex` (naskah),
`literature/scopus-2026-09/README.md` (korpus), `experiments/README.md`
(eksperimen), `README.md` (peta repo).

## 4. Peta Berkas

| Lokasi | Isi |
|---|---|
| `literature/scopus-2026-09/` | Korpus `main6`: `PROTOKOL.md`, `QUERY.md`, `topik/` (kueri, rekaman, penyaringan, `bukti/`), `pdf/` dan `teks/` |
| `literature/scopus-2026-09/entri/` | 789 ringkasan per kajian `main6`, satu berkas per kunci BibTeX; dasar Ruang Baca bersama entri korpus lama |
| `literature/scopus-2026-09/verifikasi/` | `cek-1-…` sampai `cek-6-…` mengikuti rencana Bu Fatma dan hanya memuat lembar peninjau. Pintu masuk `README.md`; keputusan yang menunggu peninjau `TUGAS.md`; log perubahan `log_perubahan.csv`. `.teknis/` berisi data yang dibaca skrip: log teknis, alasan label C1/C3 dan ajudikasi Cek 1 (sumber alasan log), serta dua CSV dasar angka pemeriksaan ulang tahap judul |
| `literature/scopus-2026-09/ekstraksi/` | Hasil agen membaca teks lengkap: `perbandingan/` (perbandingan pada data yang sama, dasar `tab:assoc`), `bacaan/` (lembar kajian inti); masing-masing dengan `prompt.txt`. Pintu masuk `README.md`. Bahan kerja, bukan sumber naskah |
| `literature/entries/`, `synthesis.md`, `extracted/` | Korpus lama: 182 ringkasan makalah, sintesis, dan teks terekstrak (dasar naskah 182 sumber; masuk Ruang Baca bersama entri `main6`) |
| `literature/withheld/` | 20 entri ditahan; jangan masuk naskah |
| `literature/references/` | PDF baseline SawitMVC; `revisi-dosen-2026-07-23/` berisi delapan permintaan revisi dosen (`Chat.txt`, catatan primer, jangan dihapus) |
| `manuscript/source/` | `main6.tex`, `main6-body.tex`, `main6-supplementary.tex` (bahan tambahan), `main6-angka.tex` (keluaran `angka_naskah.py`), lampiran, `references6.bib`; naskah 182 sumber (`main.tex`, `main-elsarticle.tex`, `evidence-body.tex`, `references.bib`) dan `experiment-ledgers.tex` untuk laporan eksperimen |
| `manuscript/figures/main6/` | Gambar F01–F12 (keluaran skrip) |
| `manuscript/templates/els-cas-templates/` | Bundel CAS Elsevier 2.4 (`cas-dc.cls`, `cas-common.sty`, `cas-model2-names.bst`) yang dipakai `main6.tex`; `main6.tex` berhenti bila kelas yang terbaca lebih tua |
| `literature/example/` | Artikel contoh bentuk naskah `main6` (§12) |
| `manuscript/reports/` | Laporan hasil eksperimen (`reports.tex` dan versi ringkas); figur rasternya di `manuscript/figures/` |
| `manuscript/output/papers/` | PDF hasil kompilasi |
| `experiments/` | `README.md` (status dan langkah berikutnya), `EKSPERIMEN.md` (log), `METRICS.md`, `SERI-F.md`, `SR/`, `code/` (peta skrip di `code/README.md`) |
| `pipeline/` | Deliverable produksi: YOLO 4 kanal untuk kamera Orbbec Gemini |
| `tools/scopus/` | Pipeline korpus `main6` |
| `tools/presentation/` | Pembuat dek PPTX |
| `site/build.js` → `index.html` | Ruang Baca Riset, 971 entri (182 korpus lama + 789 entri `main6`); `index.html` hasil build, **jangan disunting tangan** |
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
tectonic -Z search-path=../templates/els-cas-templates main6.tex   # cas-dc 2.4; latexmk/pdflatex tidak tersedia

python3 tools/scopus/kode_bukti.py       # matriks bukti
python3 tools/scopus/gambar_tinjauan.py  # gambar F01–F12
python3 tools/scopus/tabel_lampiran.py   # Lampiran A
python3 tools/scopus/lampiran_kueri.py   # Lampiran B
```

- Perintah lengkap ada di `literature/scopus-2026-09/README.md`. Kunci API
  Elsevier dibaca dari `ELSEVIER_API_KEY` / `ELSEVIER_API_KEY_FILE` dan tidak
  pernah disimpan di repo.
- Jalankan `build.js` setiap kali `literature/entries/*.md`,
  `literature/scopus-2026-09/entri/*.md`, `literature/synthesis.md`,
  `literature/scopus-2026-09/KATALOG-PDF.md`, atau laporan eksperimen berubah;
  commit `index.html` bersamaan. Teks di
  `literature/scopus-2026-09/teks/*.txt` diambil saat entri dibuka dan isi
  `literature/scopus-2026-09/ekstraksi/` tidak dibaca `build.js`, sehingga
  keduanya tidak perlu build ulang.
- Pindahkan PDF hasil `tectonic` ke `manuscript/output/papers/`.

## 6. Kontrak Berkas Entri (melanggar = build web rusak)

- Nama berkas `NNN - YYYY - Judul singkat - Tema.md` dan baris pertama
  `# NNN - Judul` (misalnya `# 003 - YOLOv3: An Incremental Improvement`)
  tidak boleh diubah.
- Tabel metadata wajib memuat `| Kunci BibTeX | \`kunci\` |`; baris ini
  di-*parse* `build.js`.
- Heading hanya `##` dan `###` (dipakai untuk daftar isi web); `#` hanya untuk
  baris judul pertama.
- Gambar dan foto dilarang: repo tidak memuat berkas gambar entri dan aplikasi
  web tidak merendernya.
- Diagram ASCII dianjurkan untuk arsitektur atau mekanisme yang sulit
  dipahami dari teks saja, paling banyak dua per bab, dalam *fenced code block*
  tanpa tag bahasa. Lebar paling banyak ±78 kolom; karakter ASCII dan kotak
  sederhana (─ │ ┌ ┐ └ ┘ ├ ┤ ▼ ▲ ●). Isinya faktual (alur data, ukuran
  tensor, perbandingan *pipeline*), bukan dekorasi; setiap diagram diawali
  satu kalimat pengantar dan dijelaskan di teks sesudahnya.
- Tabel GFM paling banyak satu per bab, bila benar-benar diperlukan.
- Tautan antar-entri relatif dengan spasi di-encode `%20`, misalnya
  `./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md`.
- Penulis entri tidak menyentuh berkas lain selain berkas yang ditugaskan.
- **Jangan mengarang angka.** Setiap klaim numerik terlacak ke sumber primer.
- Struktur dan kaidah isi entri korpus lama ada di §14.
- Kunci BibTeX `sapkota2024yoloagri` (penulis sebenarnya Alif & Hussain) dan
  `alif2024yoloevolution` (penulis sebenarnya Jegham dkk.) sengaja tidak diganti;
  di teks naskah, sebut nama penulis sebenarnya.

## 7. Kontrak Naskah `main6`

- Setiap angka korpus di naskah harus dapat dihitung ulang dari
  `literature/scopus-2026-09/` dengan skrip `tools/scopus/`. Bila data atau kode
  manual berubah, jalankan ulang skrip lalu perbarui teks naskah, `literature/scopus-2026-09/PROTOKOL.md`,
  dan §3 berkas ini.
- `main6-angka.tex`, `main6-appendix-c1.tex`, `main6-appendix-queries.tex`,
  `main6-certainty.tex`, `references6.bib`, `manuscript/figures/main6/F*`, dan
  `manuscript/output/papers/main6-supplementary-studies.csv` adalah keluaran skrip;
  **jangan disunting tangan**. Angka korpus di teks naskah ditulis sebagai
  makro dari `main6-angka.tex`, bukan diketik.
- Kode mekanisme C1 dan kode C3 disunting di `literature/scopus-2026-09/topik/bukti/mekanisme_C1.txt` dan
  `literature/scopus-2026-09/topik/bukti/kode_C3.txt`; berkas itu menimpa kode otomatis `kode_bukti.py`.
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
  - **Prioritas agen.** Saat memperbaiki naskah, agen lebih dahulu membaca isi
    kajian dari teks lengkap, baru kemudian memperbaiki *pipeline* korpus.
    Laporan kemajuan kepada pengguna juga dimulai dari temuan isi.
- Penyaringan dilakukan satu peninjau dengan bantuan model bahasa besar.
  Nyatakan sekali secara ringkas di metode, keterbatasan, dan deklarasi AI
  jurnal; jangan diklaim sebagai dua peninjau independen.
- Hasil eksperimen SawitMVC (E-/F-) bukan bagian korpus `main6`; bila dikutip,
  angkanya dari `experiments/METRICS.md`.
- Gaya tulis mengikuti §12. Daftar periksanya dijalankan sebelum naskah
  dikirim.
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

## 12. Gaya Naskah `main6`

Aturan gaya yang mengikat untuk `manuscript/source/main6.tex`,
`main6-body.tex`, dan `main6-supplementary.tex`. Naskah ditulis dalam bahasa Inggris. Acuan bentuknya adalah
artikel contoh Xiao dkk., *Computers and Electronics in Agriculture* 253 (2026)
112078 (`literature/example/autonomousnavigation.pdf`). Dasar metodologisnya ada
di §13. Kontrak data dan angka naskah ada di §7; bagian ini hanya mengatur
cara menulis.

### 12.1 Tata letak

- Kelas `cas-dc` (templat CAS Elsevier), dua kolom, dikompilasi dengan
  `tectonic`. Baris "Review Article" ditulis di dalam `\title`.
- Sitasi penulis-tahun (`natbib` `authoryear`, gaya `cas-model2-names`).
  Tautan berwarna `#1A6FB5`.
- Judul gambar "Fig. N." dan judul tabel "Table N" tebal; tabel memakai
  `booktabs` dengan garis horizontal saja.
- Rujukan dalam teks ditulis `Fig.~\ref`, `Table~\ref`, `Section~\ref`.
- Lampiran A (matriks C1) dan B (string kueri) satu kolom, sesudah daftar
  pustaka, tabel dinomori A1.

### 12.2 Nama, bukan kode

Kode internal repo tidak pernah tampil di naskah. Setiap kategori punya nama
tetap dalam tiga panjang.

| Kode internal | Nama di definisi dan judul | Bentuk pendek dalam prosa | Label sel tabel atau gambar |
|---|---|---|---|
| M0 | No association | no association | No association |
| M1 | Statistical correction | statistical correction | Statistical |
| M2 | Appearance matching | appearance matching | Appearance |
| M3 | Temporal tracking | tracking (sesudah nama lengkap muncul) | Tracking |
| M4 | Geometric or 3D association | geometric association | Geometric |
| M5 | Learned association | learned association | Learned |
| V, D, S, T, 1 | acquisition design | video along a path; discrete views; 3D scan; revisits over time; a single view | Video; Discrete views; 3D scan; Revisits; Single view |
| C1–C5, R, T | tujuh kelompok | multi-observation studies; single-view counting studies; oil-palm studies; single-image class-wise counting studies; depth and 3D sensing studies; earlier reviews; methods papers from outside agriculture | sama |
| RQ1–RQ4, G1–G5 | (1)–(4) dan (i)–(v) | dirujuk dengan isinya | — |

- Kunci kueri Q1–Q9 hanya dipakai sebagai penghubung tabel kueri dan Lampiran B.
- Satu istilah untuk satu konsep. Keluarga kategori selalu "association
  mechanism".
- Label pada gambar dan lampiran adalah keluaran skrip. Label diubah di
  `tools/scopus/gambar_tinjauan.py`, `tabel_lampiran.py`, atau
  `lampiran_kueri.py`, bukan di berkas data.
- Setiap akronim dijabarkan saat pertama muncul, termasuk yang umum (SfM,
  SLAM, MOT, RGB-D, LiDAR, UAV, MAE, MAPE, MOTA, IDF1, HOTA, PRISMA). Akronim
  yang hanya muncul sekali ditulis dengan kata. Tidak ada daftar singkatan.

### 12.3 Arsitektur seksi

- Kerangka lima tahap diumumkan di pendahuluan, diberi aturan di metode,
  dihitung di lanskap kuantitatif (Seksi 3.4), lalu menata seksi bukti: Seksi 4
  akuisisi, Seksi 5 asosiasi, Seksi 6 atribut kelas, Seksi 7 depth, Seksi 8
  sawit.
- Pendahuluan: satu fungsi per paragraf (masalah terukur, kasus, keterbatasan
  tinjauan terdahulu, tujuan, kontribusi, pertanyaan), ditutup peta isi "The
  remainder of this article is organized as follows."
- Setiap seksi bukti dibuka dengan klaim tentang isinya (asumsi, galat yang
  dikendalikan, atau kondisi gagal), lalu ditutup dengan sintesis, batas, dan
  penunjuk ke seksi berikutnya. Seksi 5 dibuka dengan tabel sintesis
  mekanisme (asumsi, sumber hitung ganda yang dihilangkan, kondisi gagal,
  bukti pada data yang sama, kecocokan untuk pandang diskret).
- Subseksi padat dipecah menjadi aliran atau isu berlabel miring, misalnya
  "*(1) Background removal.*"
- Diskusi (Seksi 9) adalah lapisan tersendiri: lintasan mekanisme, jawaban
  empat pertanyaan sebagai argumen, posisi terhadap tinjauan terdahulu, celah
  (i)–(v), dan set pelaporan minimum. Diskusi tidak mengulang uraian kajian.
- Seksi 8 (sawit) disusun: mengapa sensus menantang setiap mekanisme, cara
  deteksi berkembang, lalu yang belum ada.
- Setiap subseksi bukti merujuk Seksi 3 setidaknya sekali, dan setiap
  keterbatasan di Seksi 4–8 menunjuk ke Seksi 10.

### 12.4 Paragraf dan kalimat

Paragraf bukti mengikuti empat langkah:

1. pembuka tanpa kajian,
2. dua sampai empat kajian dengan nama dan tahun,
3. pernyataan lintas kajian,
4. batasnya.

Aturannya:

1. Kajian yang diuraikan disitasi dengan `\citet`, satu kali, dengan kata kerja
   lampau. Pernyataan tentang beberapa kajian disitasi dengan `\citep` di akhir
   kalimat. Nama penulis tidak diketik tangan.
2. Satu kajian per kalimat. Kontras ditulis dengan "whereas", dan rantai titik
   koma dipecah.
3. Subseksi mekanisme dibuka dengan klaim tentang mekanismenya: asumsi, galat
   yang dikendalikan, dan kondisi gagalnya. Jumlah kajian dan penunjuk ke gambar
   atau lampiran menyusul sebagai pendukung (§7, "Isi lebih dahulu").
4. Rangkaian kajian ditutup dengan pola dan batasnya ("Taken together, ...").
5. Batas ditulis dengan fakta yang dapat diperiksa (kajian yang tidak
   mengukurnya, atau hitungan dari kode teks lengkap), bukan kata penilaian.
6. Setiap angka disertai data, split atau rujukan hitung, dan metriknya. Angka
   antarkajian tidak dirata-ratakan, dan tabel perbandingan dibaca per baris.
7. Kala dan persona: lampau untuk kajian, kini untuk himpunan bukti, "this
   review" tanpa "we".
8. Paragraf yang melewati sekitar 150 kata atau lima kajian bernama dipecah di
   pergantian topik.
9. Klaim kebaruan dibatasi pada pencarian: "not found in the search reported in
   Section 2", bukan "no review has addressed".
10. Hindari slogan dan kata sifat kosong ("revolutionary", "plays a crucial
    role", "promising"), pembuka generik ("In recent years ..."), dan daftar
    tiga kata sifat. Kalimat yang dapat dipindah ke topik lain tanpa kehilangan
    makna dihapus.

### 12.5 Metode dan lanskap kuantitatif

- Seksi metode dibuka dengan jenis tinjauan (systematic mapping review,
  sintesis konfiguratif, tanpa penggabungan efek), PRISMA 2020, dan alur kerja.
  Subseksinya: *Search strategy*, *Inclusion and exclusion criteria*, *Study
  selection*, *Data extraction and coding*, *Appraisal and synthesis*.
  Rincian prosedur (lintasan kedua, pemeriksaan ulang tahap judul, aturan
  pengodean lengkap, peta istilah, gambar tanaman dan sensor) ada di
  `main6-supplementary.tex`.
- Kriteria ditulis bernomor. Alasan eksklusi memakai kata dan urutan yang sama
  dengan kotak diagram alur.
- Penyaringan ditulis tiga tahap: judul, judul dan abstrak, teks lengkap.
- Aturan keputusan pengodean ditulis dalam pola "A study was coded as X when
  ...".
- Lanskap kuantitatif ditulis sebagai butir berlabel (i)–(iii), satu gambar per
  butir. Cara hitung (kemunculan, bukan hitungan eksklusif) dinyatakan di
  teks, bukan di judul gambar.
- Peta istilah dinyatakan sebagai alat orientasi yang tidak memengaruhi
  inklusi.

### 12.6 Gambar, tabel, abstrak, simpulan

- Gambar atau tabel menjadi subjek kalimat. Judulnya hanya menyebut isi,
  pengodean visual, dan n; temuan ditulis di teks.
- Tabel perbandingan diberi catatan bawah: nilai seperti dilaporkan,
  dibandingkan hanya dalam satu baris, dan jabaran akronim. "Not stated"
  dipakai, bukan "NR".
- Abstrak satu paragraf dengan urutan: konteks, celah, cakupan dan periode,
  metode dan alur rekaman, cara pengodean, temuan, kontribusi.
- Simpulan 350–450 kata dalam empat paragraf: yang dikerjakan; yang mapan dan
  yang belum; panduan menurut desain akuisisi; lima prioritas (i)–(v). Kalimat
  abstrak tidak diulang.
- Bagian penutup: CRediT, deklarasi kepentingan, pendanaan, ucapan terima
  kasih, ketersediaan data, dan deklarasi AI.

### 12.7 Yang tidak ditiru dari contoh

- Peringatan yang diulang. Setiap peringatan ditulis satu kali saat tabel
  diperkenalkan, dan satu kali lagi di keterbatasan.
- Kata penilaian tanpa angka dan besaran kabur.
- Klaim pemeriksaan silang oleh penulis kedua (naskah ini satu peninjau).
- Persona bercampur ("we" dan "this review").
- Simpulan yang tumpang tindih dengan diskusi, dan tinjauan tanpa seksi
  keterbatasan.

### 12.8 Daftar periksa sebelum naskah dikirim

- [ ] Satu kalimat nilai tambah muncul di abstrak dan pendahuluan.
- [ ] Setiap seksi sintesis menjawab salah satu dari empat pertanyaan.
- [ ] Semua kueri lengkap dengan tanggal dan jumlah hasil (Lampiran B).
- [ ] Diagram alur memuat angka setiap tahap dan alasan eksklusi.
- [ ] Penyaring dan alat bantu AI disebut.
- [ ] Setiap klaim sintesis menyebut kajian, data, metode, dan angka.
- [ ] Tidak ada kode internal, jalur folder, atau `\authorcheck` yang tersisa.
- [ ] Semua angka korpus berupa makro dari `main6-angka.tex`.
- [ ] Ejaan Inggris konsisten memakai -ize.

## 13. Pola Tinjauan Pustaka

Bagian ini merangkum cara menulis tinjauan pustaka (*literature review*) menurut
panduan metodologi dan contoh review yang terindeks Scopus. Isinya menjadi dasar
metodologis aturan gaya di §12.

### 13.1 Cara bagian ini disusun

Sumber dicari hanya melalui Scopus Search API pada 28 September 2026. Tujuh query
(MA1–MA7) dijalankan; string lengkap, waktu eksekusi, dan jumlah hasilnya ada di
`literature/scopus-2026-09/QUERY.md`.

| Query | Sasaran | Hasil Scopus | Diambil |
|---|---|---:|---:|
| MA1 | Panduan menulis *literature review* (judul) | 2.592 | 150 teratas menurut sitasi |
| MA2 | Panduan *systematic review*, *mapping*, *scoping*, *snowballing* | 859 | 100 teratas |
| MA3 | Standar pelaporan PRISMA | 2.470 | 75 teratas |
| MA4 | Review visi komputer untuk buah dan tanaman | 1.052 | 125 teratas |
| MA5 | Review deteksi objek, RGB-D, *multi-view*, MOT, re-ID, SfM | 373 | 100 teratas |
| MA6 | Review kelapa sawit berbasis citra atau pembelajaran mesin | 50 | 50 |
| MA7 | Artikel metodologi klasik yang dicari berdasarkan judul | 37 | 37 |

Dari hasil itu dipilih 60 artikel (`literature/scopus-2026-09/metodologi/terpilih.csv`):
36 panduan metodologi dan 24 contoh review domain. Pemilihan berdasarkan dua hal:
jumlah sitasi di Scopus dan relevansi langsung dengan pertanyaan "bagaimana menulis
tinjauan yang benar" atau dengan topik naskah. PDF akses terbuka berhasil diperoleh
untuk 25 artikel (`metodologi/pdf/`); teksnya diekstrak ke `metodologi/teks/`
(keduanya di `literature/scopus-2026-09/`).
Artikel lain dibaca dari abstraknya. Tabel di 13.6 menandai mana yang dibaca
penuh dan mana yang hanya abstrak. Klaim di bagian ini yang bersumber dari abstrak
saja ditulis lebih hati-hati.

Sebagai pembanding, dipakai juga laporan dosen pembimbing tentang delapan review di
*Computers and Electronics in Agriculture* (CEA) tahun 2026
(`literature/references/revisi-dosen-2026-07-23/CEA_review_conventions_report.md`).

### 13.2 Apa yang membedakan tinjauan yang baik

Panduan yang dibaca sepakat pada satu hal: tinjauan pustaka adalah penelitian, bukan
daftar ringkasan. Van Wee dan Banister (2016) membedakan makalah *overview*, yang
cukup merangkum, dari makalah *review*, yang harus menambah nilai. Mereka memberi
enam bentuk nilai tambah: sintesis bukti empiris, analisis metode, analisis teori,
peta celah beserta agenda riset, relevansi untuk praktik, dan model konseptual.
Kraus dkk. (2022) menyatakan syarat serupa: metode yang jelas, pemilihan artikel yang
sistematis, dan hasil yang dapat diulang. Snyder (2019, dari abstrak) menyebut review
tradisional sering "ad hoc" dan tidak mengikuti metode tertentu, sehingga mutunya
diragukan.

Artinya, sebelum menulis, penulis harus bisa menjawab satu kalimat: apa yang pembaca
ketahui setelah membaca tinjauan ini yang tidak dapat mereka peroleh dari membaca
studi-studinya satu per satu.

### 13.3 Pola yang ditemukan

#### P1. Jenis dan fokus tinjauan dinyatakan sejak awal

Kraus dkk. (2022) membagi tinjauan mandiri menjadi dua tipe, sistematis dan
non-sistematis, lalu tiga fokus: ranah (*domain*), teori, dan metode. Grant dan
Booth (2009, dari abstrak) memetakan 14 tipe review dengan kerangka SALSA (*search,
appraisal, synthesis, analysis*) dan mencatat bahwa banyak tipe tidak punya metode
baku dan saling tumpang tindih. Arksey dan O'Malley (2005) memberi lima tahap
*scoping study*: pertanyaan, pencarian, seleksi, pencatatan data (*charting*), dan
pelaporan. Petersen dkk. (2015) memberi panduan *systematic mapping* untuk rekayasa
perangkat lunak.

Konsekuensinya: naskah harus menyebut tipe yang dipakai dan alasannya. Jika tinjauan
memetakan bukti dan membangun kerangka, bukan menghitung efek gabungan, sebutkan
itu, lalu jangan menulis kesimpulan seolah-olah hasil meta-analisis.

#### P2. Pertanyaan tinjauan dan kerangka diletakkan di depan

Baumeister dan Leary (1997) mencatat kesalahan yang paling sering pada naskah yang
ditolak: pengantar yang lemah. Penulis menunda gagasan pengikatnya sampai bagian
diskusi, sehingga pembaca harus membaca puluhan halaman tanpa tahu arah. Saran
mereka: sajikan kerangka konseptual lengkap di depan, atau setidaknya pratinjau
singkat "pesan utama" sebelum bukti dibahas. Sauer dan Seuring (2023) menempatkan
tiga keputusan pertama dari 14 keputusan SLR di tahap ini: merumuskan celah dan
pertanyaan, memilih pendekatan (induktif, deduktif, abduktif), dan menetapkan
kerangka serta konstruk yang akan dipakai untuk mengode studi.

#### P3. Metode pencarian ditulis sampai dapat diulang

Tiga sumber memberi daftar isi yang hampir sama:

- Kraus dkk. (2022): basis data, kata kunci, operator Boolean dan tanda kutip,
  periode, bidang pencarian (judul-abstrak-kata kunci), bidang subjek, tahap
  publikasi, tipe dokumen, tipe sumber, bahasa, dan filter mutu. Tiap pilihan harus
  disertai alasan.
- Van Wee dan Banister (2016): sebutkan basis data, kata kunci termasuk *truncation*,
  operator Boolean, bahasa, rentang waktu beserta alasannya, dan apakah *snowballing*
  dipakai. Mereka menyebut bagian metode sebagai salah satu kelemahan terbesar
  makalah review.
- PRISMA 2020 (Page dkk., 2021), butir 6 dan 7: sebutkan semua sumber dan tanggal
  terakhir pencarian, lalu tampilkan strategi pencarian lengkap untuk semua basis
  data, termasuk filter dan batasan.

Wohlin (2014) menjelaskan *snowballing*: mulai dari himpunan awal, lalu telusuri
daftar pustaka (*backward*) dan artikel yang mengutip (*forward*) secara berulang.
Wohlin dkk. (2020) menunjukkan bahwa untuk memperbarui SLR, satu iterasi *forward
snowballing* dari himpunan studi lama adalah cara paling hemat. Garousi dkk. (2019)
menjelaskan kapan literatur abu-abu layak dimasukkan (*multivocal review*).

#### P4. Seleksi dilaporkan dengan angka dan alasan eksklusi

PRISMA 2020 butir 8 meminta penulis menjelaskan cara memutuskan inklusi: berapa
penyaring, apakah bekerja independen, dan alat otomatis apa yang dipakai. Butir 16a
meminta alur angka dari rekaman teridentifikasi sampai studi terinklusi, sebaiknya
dengan diagram alir; butir 16b meminta contoh studi yang tampak memenuhi syarat
tetapi dikeluarkan, beserta alasannya. Dalam sampel CEA, tujuh dari delapan review
memuat diagram alir, dan enam memberi angka lengkap tiap tahap.

#### P5. Sintesis disusun per konsep, bukan per penulis

Baumeister dan Leary (1997) menyebut "kurangnya integrasi" sebagai kesalahan kedua
yang sama merusaknya: penulis menguraikan studi satu per satu tanpa mengaitkannya
dengan pertanyaan. Pembaca, kata mereka, lebih membutuhkan bagaimana studi-studi itu
saling berhubungan daripada daftar lengkapnya. Van Wee dan Banister (2016) memberi
dua cara menyusun hasil: per sumber (baris = studi) atau per isi (baris = metode,
temuan, atau klaster). Untuk tinjauan yang ingin membangun kerangka, susunan per isi
lebih tepat. Torraco (2016, dari abstrak) menyebut tinjauan integratif yang baik
bersifat integratif, definitif, dan provokatif, dan menganjurkan representasi visual.

#### P6. Bukti ditulis pada tingkat operasional

Ini pola yang paling praktis. Baumeister dan Leary (1997) memberi contoh: kalimat
"X menyebabkan Y (Rujukan)" tidak cukup. Tulislah "pada sampel A, metode B memberi
hasil C (Rujukan), sehingga mendukung pandangan bahwa X menyebabkan Y". Dengan begitu
pembaca bisa menilai sendiri apakah kesimpulan sesuai dengan bukti. Van Wee dan
Banister (2016) menambahkan tiga aturan:

1. Jangan merata-ratakan hasil studi dengan ukuran sampel berbeda secara naif;
   tampilkan hasil tiap studi bersama jumlah kasusnya, dan tampilkan rentangnya.
2. Pisahkan dengan jelas kesimpulan penulis asli dari tafsiran penulis review.
3. Jangan mengkritik studi karena tidak melakukan hal di luar ruang lingkupnya.

#### P7. Mutu bukti dinilai, bukan hanya dicatat

Baumeister dan Leary (1997) menyebut "kurangnya penilaian kritis" sebagai kesalahan
berikutnya: kesimpulan tinjauan dibatasi oleh kelemahan studi yang ditinjau, jadi
kelemahan itu harus dinyatakan. Tranfield dkk. (2003), seperti dirangkum Kraus dkk.
(2022), memasukkan penilaian mutu studi sebagai fase tersendiri, di antara seleksi
studi dan ekstraksi data. Untuk topik teknik, penilaian ini bisa berupa pertanyaan tetap
yang diajukan ke tiap studi: apakah ada data acuan yang independen, apakah uji
dilakukan di data yang tidak dipakai melatih, apakah metrik yang dilaporkan sesuai
dengan klaim.

#### P8. Tabel ringkasan dan tabel sintesis

Van Wee dan Banister (2016) menyarankan tabel deskriptif (penulis, tahun, konteks,
ukuran sampel) terpisah dari tabel hasil, dan memindahkan tabel yang sangat panjang
ke lampiran. Dalam sampel CEA, tujuh dari delapan review memuat setidaknya satu
tabel sintesis besar, satu baris per studi. Revisi dosen butir 8 meminta hal yang
sama: matriks bukti masuk ke naskah sebagai tabel, bukan hanya berkas CSV terpisah.

#### P9. Posisi terhadap review terdahulu dinyatakan eksplisit

Van Wee dan Banister (2016) meminta penulis menyebut review yang sudah ada dan
menjelaskan posisi tinjauannya. Contoh review domain melakukannya dengan kalimat
yang spesifik. Zhou dkk. (2021) menulis bahwa review SOD sebelumnya membahas model
berbasis RGB, sedangkan mereka membahas model RGB-D dan dataset-nya. Naranjo-Torres
dkk. (2020) membuat daftar kontribusi "dibandingkan review sebelumnya". Dalam sampel
CEA, enam dari delapan review melakukan pemosisian eksplisit. Revisi dosen butir 3
meminta pemosisian terhadap review kelapa sawit dan penghitungan buah.

#### P10. Kontribusi konseptual berupa taksonomi atau kerangka keputusan

Dalam sampel CEA, enam atau tujuh dari delapan review mengusulkan taksonomi. Luo
dkk. (2021) membuka review MOT dengan formulasi masalah yang menyatukan sebagian besar
metode, lalu dua cara mengelompokkan metode. Post dkk. (2020, dari abstrak) memberi
beberapa jalan kontribusi teoretis dari review: menyingkap perspektif baru, menguji
asumsi, memperjelas konstruk, menetapkan batas berlaku, dan berteori dengan
mekanisme. Breslin dan Gatrell (2023) membedakan review "penambang" yang bekerja di
dalam satu ranah dari review "pencari" yang mengambil gagasan dari ranah lain.
Tinjauan yang mengambil mekanisme pelacakan, re-ID, dan SfM dari luar pertanian untuk
masalah penghitungan buah termasuk jenis kedua, sehingga harus menjelaskan mengapa
bukti dari ranah lain berlaku di kebun dan di mana batasnya.

#### P11. Penutup: tantangan, agenda, dan keterbatasan tinjauan itu sendiri

Semua review dalam sampel CEA ditutup dengan bagian tantangan dan arah riset, lalu
kesimpulan singkat. Agenda yang berguna menyebut apa yang harus diukur, di data apa,
dan dengan metrik apa, bukan sekadar "perlu penelitian lebih lanjut". Tinjauan juga
harus menyebut keterbatasannya sendiri: basis data yang tidak dicari, bahasa,
penyaringan oleh satu orang, dan akses teks lengkap.

#### P12. Kebiasaan pada contoh review domain

Dua belas contoh review domain yang teksnya tersedia dicek dengan penghitungan kata
kunci sederhana (`literature/scopus-2026-09/metodologi/fitur_contoh.csv`). Hasilnya:

- Review naratif yang banyak disitasi sering tidak melaporkan cara pencarian sama
  sekali. Tang dkk. (2020), Zhao dkk. (2019), Zhou dkk. (2021), dan Sharma dkk. (2021)
  tidak menyebut basis data maupun kriteria inklusi.
- Review yang menyebut dirinya sistematis melaporkan metode. Khan dkk. (2021) memakai
  pertanyaan penelitian, PRISMA, dan kriteria inklusi; Abade dkk. (2021) juga;
  Hasan dkk. (2021) memberi string Boolean dan daftar sumber pencarian, termasuk Scopus
  dan Web of Science.
- Review CEA tahun 2026 hampir semuanya melaporkan metode pencarian. Standar jurnal
  bergeser; jumlah sitasi review lama tidak berarti metodenya masih cukup.

Kesimpulannya, contoh review yang terkenal berguna untuk melihat susunan dan cara
membahas bukti, tetapi tidak untuk meniru bagian metodenya.

### 13.4 Kesalahan umum

Dikumpulkan dari Baumeister dan Leary (1997), van Wee dan Banister (2016), dan
Kraus dkk. (2022):

1. Pengantar hanya meyakinkan bahwa topik penting, tanpa kerangka dan tanpa pesan
   utama.
2. Cakupan bukti tidak seimbang: beberapa studi favorit dibahas panjang, sisanya
   sekilas.
3. Mengutip kesimpulan studi tanpa menyebut data, metode, dan hasilnya.
4. Menguraikan studi satu per satu tanpa integrasi.
5. Tidak menilai kelemahan bukti.
6. Bagian metode terlalu pendek atau tidak ada, atau sebaliknya mengulang semua
   tahapan protokol secara bertele-tele (Kraus dkk. menyebut ini pelaporan yang tidak
   hemat).
7. Merata-ratakan angka dari studi yang tidak sebanding.
8. Mencampur kesimpulan penulis asli dengan tafsiran sendiri.
9. Tidak menyebut review terdahulu, sehingga kebaruan tidak dapat dinilai.

### 13.5 Penerapan

Aturan gaya yang diturunkan dari pola di atas, termasuk daftar periksa
sebelum naskah dikirim, ada di §12.

### 13.6 Sumber

Semua sumber ditemukan melalui Scopus. Kolom "Teks" menunjukkan apakah artikel
dibaca dari teks lengkap (penuh) atau hanya abstrak.

| Rujukan | Sumber | DOI | Sitasi Scopus* | Teks |
|---|---|---|---:|---|
| Arksey & O'Malley (2005) | Int. J. Social Research Methodology | 10.1080/1364557032000119616 | 30.332 | penuh |
| Baumeister & Leary (1997) | Review of General Psychology | 10.1037/1089-2680.1.3.311 | 1.091 | penuh |
| Breslin & Gatrell (2023) | Organizational Research Methods | 10.1177/1094428120943288 | 242 | penuh |
| Garousi dkk. (2019) | Information and Software Technology | 10.1016/j.infsof.2018.09.006 | 713 | penuh |
| Grant & Booth (2009) | Health Information and Libraries Journal | 10.1111/j.1471-1842.2009.00848.x | 8.771 | abstrak |
| Kraus dkk. (2022) | Review of Managerial Science | 10.1007/s11846-022-00588-8 | 977 | penuh |
| Kunisch dkk. (2023) | Organizational Research Methods | 10.1177/10944281221127292 | 212 | penuh |
| Marzi dkk. (2025) | Int. J. Management Reviews | 10.1111/ijmr.12381 | 490 | penuh |
| Page dkk. (2021), PRISMA 2020 | BMJ | 10.1136/bmj.n71 | 99.709 | penuh |
| Page dkk. (2021), penjelasan PRISMA | BMJ | 10.1136/bmj.n160 | 11.065 | penuh |
| Petersen dkk. (2015) | Information and Software Technology | 10.1016/j.infsof.2015.03.007 | 2.246 | abstrak |
| Post dkk. (2020) | Journal of Management Studies | 10.1111/joms.12549 | 485 | abstrak |
| Sauer & Seuring (2023) | Review of Managerial Science | 10.1007/s11846-023-00668-3 | 443 | penuh |
| Snyder (2019) | Journal of Business Research | 10.1016/j.jbusres.2019.07.039 | 7.503 | abstrak |
| Torraco (2016) | Human Resource Development Review | 10.1177/1534484316671606 | 1.090 | abstrak |
| Tranfield dkk. (2003) | British Journal of Management | 10.1111/1467-8551.00375 | 12.934 | abstrak |
| Tricco dkk. (2018), PRISMA-ScR | Annals of Internal Medicine | 10.7326/m18-0850 | 35.758 | penuh |
| van Wee & Banister (2016) | Transport Reviews | 10.1080/01441647.2015.1065456 | 486 | penuh |
| Wohlin (2014) | Proc. EASE (ACM) | 10.1145/2601248.2601268 | 1.864 | penuh |
| Wohlin dkk. (2020) | Information and Software Technology | 10.1016/j.infsof.2020.106366 | 121 | penuh |
| Abade dkk. (2021) | Computers and Electronics in Agriculture | 10.1016/j.compag.2021.106125 | 316 | penuh |
| Hasan dkk. (2021) | Computers and Electronics in Agriculture | 10.1016/j.compag.2021.106067 | 481 | penuh |
| Khan dkk. (2021) | Agriculture | 10.3390/agriculture11090832 | 62 | penuh |
| Koirala dkk. (2019) | Computers and Electronics in Agriculture | 10.1016/j.compag.2019.04.017 | 574 | abstrak |
| Lai dkk. (2023) | Agriculture | 10.3390/agriculture13010156 | 47 | penuh |
| Luo dkk. (2021) | Artificial Intelligence | 10.1016/j.artint.2020.103448 | 883 | penuh |
| Naranjo-Torres dkk. (2020) | Applied Sciences | 10.3390/app10103443 | 401 | penuh |
| Patrício & Rieder (2018) | Computers and Electronics in Agriculture | 10.1016/j.compag.2018.08.001 | 923 | penuh |
| Sharma dkk. (2021) | IEEE Access | 10.1109/access.2020.3048415 | 1.045 | penuh |
| Tang dkk. (2020) | Frontiers in Plant Science | 10.3389/fpls.2020.00510 | 605 | penuh |
| Zhao dkk. (2019) | IEEE Trans. Neural Networks and Learning Systems | 10.1109/tnnls.2018.2876865 | 5.085 | penuh |
| Zhou dkk. (2021) | Computational Visual Media | 10.1007/s41095-020-0199-z | 318 | penuh |

\* Jumlah sitasi pada saat pengambilan (28 September 2026).

## 14. Penulisan Entri Korpus Lama

Bagian ini adalah acuan gaya untuk menulis ulang setiap berkas di
`literature/entries/` (korpus lama 182). Setiap penulis, termasuk subagen, membaca
§6 dan bagian ini sampai selesai sebelum menulis. Tujuan penulisan ulang: mengubah lembar telaah yang telegrafik
menjadi **bab bergaya buku teks** — runtut, lengkap, dan dapat dipahami pembaca yang
belum mengenal topiknya.

### 14.1 Peran dan Alur Kerja

Satu penulis menangani **satu berkas entri** (satu makalah). Urutan kerja wajib:

1. Baca §6 dan bagian ini sampai selesai.
2. Baca berkas entri lama yang ditugaskan. Ambil darinya: kunci BibTeX, identitas
   makalah (judul, penulis, tahun, venue), tema klaster, dan tautan akses. **Isi
   pembahasannya jangan dipertahankan** — tulis ulang sepenuhnya.
3. Riset sumber primer:
   - Buka tautan arXiv/DOI pada berkas lama; baca abstrak dan, bila
     tersedia, halaman HTML makalah.
   - Bila klaim/angka penting belum jelas, cari dengan WebSearch (situs resmi,
     repositori kode, halaman proyek, dokumentasi model).
   - Catat hanya fakta yang terverifikasi dari sumber; jangan mengarang angka.
4. Distil: tentukan masalah, gagasan inti, mekanisme kerja, hasil utama, dan
   keterbatasan makalah.
5. Tulis ulang berkas (overwrite penuh) mengikuti struktur dan kaidah di bawah.
6. Laporkan ke pemanggil: jumlah kata, bagian yang tidak dapat diverifikasi dari
   sumber, dan penyimpangan dari panduan (bila ada).

### 14.2 Struktur Bab (wajib, urut)

Sepuluh bagian `##` berikut, dengan judul persis seperti tertulis:

1. `## Metadata Ringkas` — tabel dua kolom: Kunci BibTeX, Judul asli, Penulis,
   Tahun, Venue, Tema.
2. `## Tautan Akses` — bullet tautan (arXiv/DOI/Scholar) dari berkas lama.
3. `## Gambaran Umum` — 1–2 paragraf: apa makalah ini, masalah apa yang dipecahkan,
   apa hasil utamanya. Ditulis sehingga pembaca yang hanya membaca bagian ini tetap
   mendapat inti bab.
4. `## Latar Belakang: Masalah yang Ingin Dipecahkan` — kondisi bidang sebelum
   makalah ini ada; kekurangan pendekatan sebelumnya yang spesifik; mengapa masalah
   itu penting. Rujuk bab terdahulu bila relevan.
5. `## Ide Utama` — gagasan inti makalah dalam bentuk paling sederhana yang benar
   secara teknis. Jelaskan intuisi mekanis (apa masuk, apa keluar, apa yang berubah),
   bukan metafora.
6. `## Cara Kerja Langkah demi Langkah` — bagian terpanjang (±40–50% isi bab).
   Uraikan mekanisme secara berurutan; gunakan `###` per komponen/tahap. Setiap
   istilah teknis dijelaskan saat pertama muncul. Gunakan contoh numerik konkret.
   Bila arsitekturnya sukar dipahami dari teks (mis. aliran data antar-komponen,
   perbandingan dengan pipeline pendahulu), sertakan satu diagram ASCII.
7. `## Eksperimen dan Hasil` — apa yang diuji, pada data apa, dibandingkan dengan
   apa; angka hasil utama beserta interpretasinya.
8. `## Kelebihan dan Keterbatasan` — prosa seimbang; keterbatasan yang merupakan
   analisis penulis bab (bukan pernyataan penulis makalah) ditandai dengan frasa
   seperti "dari sisi rekayasa, ..." atau "secara konseptual, ...".
9. `## Kaitan dengan Bab Lain` — narasi kesinambungan: bab ini mewarisi apa dari
   bab mana, dan memengaruhi bab mana; sertakan tautan relatif. Minimal merujuk
   satu bab sebelumnya dalam silsilahnya bila ada.
10. `## Poin untuk Sitasi` — kunci BibTeX; ringkasan 2–3 kalimat yang aman dikutip
    dalam tinjauan pustaka; catatan angka/klaim yang perlu diverifikasi ke naskah
    asli sebelum sitasi formal (wajib untuk makalah sangat baru).

### 14.3 Kaidah Bahasa (syarat utama)

- **Bahasa Indonesia baku sesuai EYD V.** Perhatikan: penulisan imbuhan
  (`di-` awalan pasif vs `di` kata depan), kata baku (sistem, metode, praktik,
  hingga→sampai), dan tanda baca. Angka desimal memakai koma (`63,4%`).
- **Istilah asing dicetak miring** pada kemunculan pertama dan selanjutnya boleh
  tetap miring: *bounding box*, *confidence*, *backbone*. Istilah yang sudah
  diserap ditulis sesuai kaidah serapan (mis. *citra*, *piksel*, *filter* →
  *tapis* bila konteksnya pemrosesan citra; boleh tetap *filter* bila merujuk
  nama teknis baku).
- **Dilarang metafora, perumpamaan, dan kalimat mewah.** Tidak ada "ibarat",
  "bagaikan", "bak", "laksana". Kejelasan dicapai melalui struktur penjelasan:
  definisi → mekanisme → contoh numerik → interpretasi.
- **Dilarang frasa pengisi dan hiperbola ("AI slop")**, antara lain: "di era
  modern ini", "perkembangan pesat", "revolusioner", "terobosan", "menariknya",
  "perlu dicatat bahwa", "penting untuk dipahami", "dunia deteksi objek",
  "seperti yang kita ketahui", pujian kosong pada makalah. Setiap kalimat wajib
  memuat informasi.
- Nada buku teks: impersonal, langsung, tepat. Tidak memakai "kita"/"Anda"
  kecuali sangat terpaksa; gunakan konstruksi pasif atau nominal ("model ini
  memprediksi...", bukan "kita akan melihat model memprediksi...").
- Kalimat efektif: satu gagasan per kalimat; hindari kalimat majemuk lebih dari
  dua anak kalimat.

### 14.4 Kaidah Isi

- Panjang **1200–1800 kata** (tidak termasuk tabel metadata dan tautan).
- Alur naratif runtut: masalah → gagasan → cara kerja → bukti → penilaian.
  Bullet hanya untuk enumerasi murni (daftar komponen, daftar hasil); penjelasan
  konsep wajib berbentuk paragraf.
- **Setiap istilah teknis dijelaskan saat pertama muncul**, dalam 1–2 kalimat
  definisi langsung. Tidak boleh ada jargon yang dipakai tanpa penjelasan —
  termasuk nama metode lain yang dirujuk (mis. bila menyebut FPN, jelaskan satu
  kalimat apa itu FPN).
- **Contoh numerik konkret** untuk memperjelas mekanisme, misalnya: "pada citra
  448×448 dan grid 7×7, setiap sel mencakup wilayah 64×64 piksel".
- **Setiap angka hasil diberi interpretasi**, misalnya: "63,4% mAP berada di bawah
  Fast R-CNN (70,0%), tetapi kecepatannya 45 FPS dibandingkan ±0,5 FPS".
- **Tidak ada pengulangan**: satu fakta dibahas sekali di satu bagian; bagian lain
  cukup merujuknya secara singkat.
- Bab harus **mandiri** (semua istilah dijelaskan di tempat) **tetapi terhubung**
  (bagian 4 dan 9 merujuk bab lain secara naratif dengan tautan).
- Kejujuran akademik: klaim yang tidak berhasil diverifikasi dari sumber primer
  diberi tanda di bagian *Poin untuk Sitasi*; narasi utama hanya memuat hal yang
  diyakini benar. Jangan mengarang angka, nama dataset, atau hasil.

### 14.5 Checklist Sebelum Melapor

- [ ] Baris pertama dan nama berkas tidak berubah; baris `| Kunci BibTeX |` ada.
- [ ] Sepuluh bagian `##` lengkap dan urut; heading hanya `##`/`###`.
- [ ] 1200–1800 kata.
- [ ] Tidak ada boilerplate administratif lama (checklist verifikasi, glosarium
      generik, catatan integritas, daftar isi panjang).
- [ ] Semua istilah teknis terjelaskan saat pertama muncul; tidak ada jargon telanjang.
- [ ] Tidak ada metafora/perumpamaan; tidak ada frasa pengisi; ejaan EYD V.
- [ ] Setiap angka hasil memiliki interpretasi; tidak ada fakta diulang antar-bagian.
- [ ] Bagian *Kaitan dengan Bab Lain* berisi narasi + tautan relatif yang benar.
- [ ] Bagian arsitektur/mekanisme yang kompleks dibantu diagram ASCII yang faktual.
- [ ] Tanpa gambar/foto; diagram ASCII dalam fenced code block, lebar ≤78 kolom.
- [ ] Laporan akhir menyebut jumlah kata dan klaim yang belum terverifikasi.

### 14.6 Contoh Bab Jadi

Contoh bab yang sudah memenuhi seluruh kaidah: `literature/entries/001 - 2016 - You Only Look
Once (YOLOv1) - Fondasi RGB.md`. Baca berkas tersebut sebagai acuan bentuk akhir —
perhatikan panjang bagian, cara istilah diperkenalkan, dan cara angka diinterpretasi.
Tirukan polanya pada bab yang ditugaskan, dengan isi yang sepenuhnya dari makalah
tugas Anda.
