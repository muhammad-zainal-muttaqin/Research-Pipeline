# Catatan Format dari Artikel Contoh dan Penerapannya pada `main6`

Artikel contoh: Xiao dkk., *Research progress of autonomous navigation path
planning methods for agricultural ground machinery: a review*, Computers and
Electronics in Agriculture 253 (2026) 112078 (`literature/example/autonomousnavigation.pdf`,
33 halaman). Catatan ini merekam hal yang diambil dari contoh itu dan cara
penerapannya pada `main6` (1 Oktober 2026).

## 1. Tata letak

| Unsur pada contoh | Penerapan pada `main6` |
|---|---|
| Kelas artikel Elsevier dua kolom, A4 | `cas-dc` (templat CAS Elsevier), dikompilasi dengan `tectonic` |
| Baris "Review Article" di atas judul | Ditulis di dalam `\title` |
| Blok "ARTICLE INFO" (kata kunci) di kiri dan "ABSTRACT" di kanan | Bawaan `cas-dc` |
| Kepala halaman: penulis di kiri, identitas di kanan, miring | Penulis singkat di kiri, judul singkat di kanan (nama jurnal tidak dicantumkan karena naskah belum terbit) |
| Nomor halaman di tengah bawah | Sama |
| Tautan dan sitasi berwarna biru | `hscolor` = `#1A6FB5` |
| Sitasi penulis-tahun, daftar pustaka alfabetis | `natbib` `authoryear`, gaya `cas-model2-names` |
| Judul gambar "Fig. N." tebal, huruf serif, di bawah gambar | Makro judul gambar `cas` ditimpa di `main6.tex` |
| Judul tabel "Table N" tebal, keterangan di baris berikutnya, garis horizontal saja | Makro judul tabel ditimpa; `booktabs` |
| Rujukan dalam teks "Fig. 3", "Table 2", "Section 3.4" | `Fig.~\ref`, `Table~\ref`, `Section~\ref` |
| Lampiran berlabel huruf | Lampiran A (matriks bukti) dan B (string kueri), satu kolom, setelah daftar pustaka agar tidak ada halaman kosong |

## 2. Gambar

| Ciri pada contoh | Penerapan |
|---|---|
| Huruf serif yang sama dengan teks | Times New Roman (cadangan Liberation Serif) di `gambar_tinjauan.py` |
| Sumbu berbingkai penuh, tanda sumbu ke dalam | `rcParams` global |
| Palet biru, jingga, hijau yang konsisten antargambar | Palet Okabe-Ito (aman buta warna) dipertahankan; warna mekanisme sama di F03, F04, F05, F09 |
| Peta panas biru dengan angka di sel dan batang warna | F10 |
| Seluruh gambar vektor | PDF vektor; tidak ada raster |

Padanan gambar:

| Contoh | `main6` |
|---|---|
| Fig. 1 alur PRISMA | F01 |
| Fig. 2 kerangka analitis | F03 |
| Fig. 3–4 peta kookurensi kata kunci (VOSviewer) | **F08 baru**: peta kookurensi istilah dari judul dan abstrak 971 kajian |
| Fig. 5 jumlah kajian per tahun | F02 |
| Fig. 6 dan 8 peta panas skenario × kategori | F05 (tanaman × mekanisme), F06 (sawit: tugas × lokasi) |
| Fig. 9 sensor × skenario | **F10 baru**: modalitas dan platform × tanaman |
| Fig. 11 diagram alur (*Sankey*) empat kolom | **F09 baru**: akuisisi → mekanisme → platform → tanaman |
| Fig. 7 perbandingan KPI antarkajian | Tidak dibuat: metrik antarkajian `main6` tidak sebanding (naskah menyatakan angka hanya dibandingkan dalam satu baris tabel) |
| Fig. 10 foto sistem komersial | Tidak dibuat: tidak ada bahan berlisensi |

## 3. Cara penulisan

- Abstrak satu paragraf dengan urutan: konteks, celah, cakupan dan periode,
  metode dan jumlah rekaman, cara pengodean, temuan, kontribusi. `main6` sudah
  mengikuti urutan ini.
- Pendahuluan ditutup dengan daftar bernomor (contoh: keterbatasan tinjauan
  terdahulu dan kontribusi; `main6`: RQ1–RQ4 dan kontribusi).
- Bagian metode dipecah menjadi subbagian pendek: sumber data, strategi
  pencarian, kriteria, seleksi, ekstraksi, kerangka analisis, sintesis.
- Setiap gambar dan tabel dirujuk di teks lalu ditafsirkan dengan angka; judul
  gambar hanya menyebut apa yang ditampilkan.
- Peta kookurensi dinyatakan sebagai alat orientasi yang tidak memengaruhi
  inklusi. Kalimat yang sama dipakai untuk F08.
- Angka KPI antarkajian dinyatakan sebagai rentang representatif, bukan
  pembanding terkendali.
- Diskusi menutup dengan celah riset dan agenda bernomor (`main6`: G1–G5).

## 4. Yang belum diterapkan dan memerlukan keputusan penulis

Contoh memuat bagian penutup berikut yang isinya hanya dapat diisi penulis:
*CRediT authorship contribution statement*, *Funding*, *Declaration of competing
interest*, dan *Acknowledgment*. `main6` baru memuat *Data availability* dan
*Declaration of generative AI use*.
