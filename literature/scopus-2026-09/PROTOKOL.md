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
| Dikeluarkan pada tahap judul | 4.580 |
| Dinilai kelayakannya | 1.143 |
| — dengan abstrak | 889 |
| — hanya judul, sumber, dan ringkasan TLDR | 254 |
| Dikeluarkan pada tahap kelayakan | 143 |
| Masuk peta (Scopus) | 1.000 |
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
| C5 | Deteksi, lokalisasi, atau pengukuran buah dengan depth, 3D, atau modalitas non-RGB | 134 |
| R | Tinjauan terdahulu | 120 |
| T | Metode yang dapat dipindahkan dari luar pertanian | 88 |

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
- Untuk kueri Q3, Q5, dan Q7, judul diurutkan menurut kata kunci sebelum dibaca.
- PDF akses terbuka diperoleh untuk 330 dari 1.000 kajian; sisanya tercantum di
  `unduhan/pdf_belum_ada.csv` beserta alasan kegagalan.
