# Protokol Tinjauan `main6`

Protokol ini mencatat cara rekaman Scopus disaring dan dikodekan. Laporan
mengikuti PRISMA 2020 sejauh butirnya berlaku untuk tinjauan pemetaan
(*systematic mapping review*).

## 1. Pertanyaan tinjauan

1. Mekanisme apa yang dipakai untuk memutuskan bahwa pengamatan di citra berbeda
   berasal dari buah yang sama, dan kondisi akuisisi apa yang diasumsikan tiap
   mekanisme?
2. Bukti apa yang menunjukkan seberapa baik tiap mekanisme mengendalikan hitung
   ganda dan buah terlewat, dan bagaimana bukti itu diukur?
3. Bagaimana atribut kelas, terutama kematangan, dilekatkan pada buah unik, bukan
   pada setiap deteksi?
4. Apa yang sudah dicakup literatur pencitraan kelapa sawit, dan apa yang belum
   ada untuk sensus tandan per kelas dari citra?

## 2. Sumber dan pencarian

- Sumber tunggal: Scopus Search API, tampilan STANDARD, 28 September 2026 (UTC).
- Tiga belas eksekusi kueri: Q1–Q7, Q8a–Q8e, Q9. String lengkap ada di
  [`QUERY.md`](QUERY.md).
- Rentang tahun 2012–2026; bidang subjek dibatasi pada bidang yang menerbitkan
  karya teknik atau pertanian.
- Q8a–Q8e dan Q9 (metode di luar pertanian) hanya diambil 25 rekaman yang paling
  banyak disitasi per eksekusi, karena perannya menunjukkan mekanisme yang dapat
  dipindahkan, bukan memetakan bidang tersebut.

## 3. Alur dan angka

| Tahap | Jumlah |
|---|---:|
| Rekaman diambil dari 13 eksekusi | 6.491 |
| Duplikat (EID sama) | 602 |
| Rekaman unik | 5.889 |
| Dikeluarkan menurut tipe dokumen (front matter prosiding, erratum, catatan, editorial, surat, ditarik) | 166 |
| Judul disaring | 5.723 |
| Dikeluarkan pada tahap judul | 4.579 |
| Dinilai kelayakannya | 1.144 |
| — dengan abstrak | 890 |
| — hanya judul, sumber, dan ringkasan TLDR | 254 |
| Dikeluarkan pada tahap kelayakan | 143 |
| Masuk peta (Scopus) | 1.001 |
| Rekaman metode lain (Liu dan Ampatzidis 2026) | 1 |

Alasan eksklusi tahap kelayakan: E1 bukan buah pada tanaman (20), E2 hanya
pascapanen atau laboratorium (18), E3 model hasil tanpa deteksi tingkat buah (27),
E4 hanya pemetikan atau manipulasi (9), E5 deteksi tanpa pencacahan atau evaluasi
lain (65), E6 sensor non-citra (3), E7 bahasa selain Inggris (1).

## 4. Kode inklusi

| Kode | Arti | Jumlah |
|---|---|---:|
| C1 | Metode yang menggabungkan beberapa pengamatan buah yang sama (video, beberapa pandang, pindaian berulang) | 195 |
| C2 | Pencacahan atau estimasi hasil dari satu pandang | 238 |
| C3 | Pencitraan TBS kelapa sawit, termasuk grading di pabrik dan brondolan | 176 |
| C4 | Atribut kelas disertai pencacahan dari citra tunggal | 49 |
| C5 | Deteksi, lokalisasi, atau pengukuran buah dengan depth, 3D, atau modalitas non-RGB | 135 |
| R | Tinjauan terdahulu | 120 |
| T | Metode yang dapat dipindahkan dari luar pertanian | 88 |

Dua aturan berlaku saat menetapkan kode (keputusan Fatma, 5 Oktober 2026):

- **Stereo.** Sepasang citra stereo dihitung sebagai satu pengamatan, sehingga
  kajian yang mendeteksi, melokalisasi, atau mengukur buah dari satu pasang stereo
  berkode C5. Kajian berkode C1 hanya bila buah dihubungkan antar-*frame* atau
  antarposisi kamera.
- **Prioritas.** Bila lebih dari satu kode cocok, C1 didahulukan untuk kajian
  yang menggabungkan beberapa pengamatan buah yang sama.

## 5. Pengodean

- **C1** dikodekan manual dari abstrak dan, bila ada, teks lengkap
  (`topik/bukti/mekanisme_C1.txt`): mekanisme M0–M5, akuisisi (V, D, S, T, 1),
  hitungan per kelas (Y/N), dan hasil ringkas.
  - M0 tanpa asosiasi; M1 koreksi statistik; M2 pencocokan penampilan atau re-ID;
    M3 pelacakan temporal; M4 asosiasi geometris atau 3D; M5 asosiasi yang
    dipelajari; DATA makalah set data.
- **C3** dikodekan manual (`topik/bukti/kode_C3.txt`): tugas, lokasi, modalitas,
  penggunaan beberapa pandang, dan label kelas pada instans.
- Kategori lain dikodekan dengan aturan kata kunci (`tools/scopus/kode_bukti.py`)
  untuk tanaman, modalitas, platform, atribut kelas, dan jenis metrik, lalu diperiksa
  secara acak.
- Jenis metrik hanya dibaca dari abstrak dan hanya dilaporkan untuk kajian yang
  abstraknya tersedia.

## 6. Keterbatasan

- Hanya Scopus; karya yang hanya terindeks di basis data lain tidak tercakup.
- Kunci API hanya memberi tampilan STANDARD, sehingga abstrak diambil dari layanan
  terbuka; 254 rekaman diputuskan dari judul, sumber, dan ringkasan TLDR.
- Penyaringan dan pengodean dilakukan satu peninjau dengan bantuan model bahasa
  besar, tanpa peninjau kedua yang independen. Berkas keputusan dirilis agar dapat
  diaudit.
- Putaran kedua (1–2 Oktober 2026) dikerjakan model bahasa besar yang sama dalam sesi
  terpisah tanpa melihat putaran pertama: 510 rekaman kunci (C1, C3, eksklusi tahap
  kelayakan), sampel buta 300 judul dan 100 abstrak, ajudikasi rekaman yang berbeda,
  uji sanggah untuk setiap perubahan kelompok, dan pembacaan ulang 1.325 eksklusi
  tahap judul dari kueri Q1 dan Q3 (19 dimasukkan kembali). Ini mengukur konsistensi
  prosedur, bukan penilaian independen oleh orang kedua. Rincian: `verifikasi/hasil-kerja-ai/`,
  `verifikasi/log_perubahan.csv`, `verifikasi/SERAH-TERIMA.md`. Eksklusi judul dari
  kueri selain Q1 dan Q3 belum dibaca ulang.
- **Sampel buta peninjau (Cek 1, 4 Oktober 2026).** Peninjau menilai 300 judul dan
  165 rekaman tahap abstrak tanpa melihat keputusan model
  (`verifikasi/cek-1-sampel-buta/kesepakatan.md`). Lima judul yang dieksklusi model
  tetapi ditandai peninjau sebagai C1 atau C3 diputuskan Fatma pada 5 Oktober 2026:
  empat tetap dieksklusi, dan satu (Qiu dkk., 2022, idx 3661) masuk peta sebagai C5
  (`topik/penyaringan/abstrak_F00.txt`).
- Untuk kueri Q3, Q5, dan Q7, judul diurutkan menurut kata kunci sebelum dibaca.
- PDF tersedia untuk 479 dari 1.001 kajian (`KATALOG-PDF.md`); teksnya sudah
  diekstrak untuk 330 kajian. Daftar awal PDF yang belum ada tercantum di
  `unduhan/pdf_belum_ada.csv` beserta alasan kegagalan.
