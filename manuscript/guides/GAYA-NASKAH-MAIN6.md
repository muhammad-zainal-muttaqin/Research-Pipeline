# Gaya Naskah `main6`

Aturan gaya yang mengikat untuk `manuscript/source/main6.tex` dan
`main6-body.tex`. Naskah ditulis dalam bahasa Inggris. Acuan bentuknya adalah
artikel contoh Xiao dkk., *Computers and Electronics in Agriculture* 253 (2026)
112078 (`literature/example/autonomousnavigation.pdf`). Dasar metodologisnya ada
di `POLA-TINJAUAN-PUSTAKA.md`. Kontrak data dan angka naskah ada di `AGENTS.md`
§7; berkas ini hanya mengatur cara menulis.

## 1. Tata letak

- Kelas `cas-dc` (templat CAS Elsevier), dua kolom, dikompilasi dengan
  `tectonic`. Baris "Review Article" ditulis di dalam `\title`.
- Sitasi penulis-tahun (`natbib` `authoryear`, gaya `cas-model2-names`).
  Tautan berwarna `#1A6FB5`.
- Judul gambar "Fig. N." dan judul tabel "Table N" tebal; tabel memakai
  `booktabs` dengan garis horizontal saja.
- Rujukan dalam teks ditulis `Fig.~\ref`, `Table~\ref`, `Section~\ref`.
- Lampiran A (matriks C1) dan B (string kueri) satu kolom, sesudah daftar
  pustaka, tabel dinomori A1.

## 2. Nama, bukan kode

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

## 3. Arsitektur seksi

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

## 4. Paragraf dan kalimat

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
   atau lampiran menyusul sebagai pendukung (`AGENTS.md` §7, "Isi lebih dahulu").
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

## 5. Metode dan lanskap kuantitatif

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
  Pernyataan "satu peninjau dibantu model bahasa besar" ditulis sekali di
  metode, keterbatasan, dan deklarasi AI.
- Aturan keputusan pengodean ditulis dalam pola "A study was coded as X when
  ...".
- Lanskap kuantitatif ditulis sebagai butir berlabel (i)–(iii), satu gambar per
  butir. Cara hitung (kemunculan, bukan hitungan eksklusif) dinyatakan di
  teks, bukan di judul gambar.
- Peta istilah dinyatakan sebagai alat orientasi yang tidak memengaruhi
  inklusi.

## 6. Gambar, tabel, abstrak, simpulan

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

## 7. Yang tidak ditiru dari contoh

- Peringatan yang diulang. Setiap peringatan ditulis satu kali saat tabel
  diperkenalkan, dan satu kali lagi di keterbatasan.
- Kata penilaian tanpa angka dan besaran kabur.
- Klaim pemeriksaan silang oleh penulis kedua (naskah ini satu peninjau).
- Persona bercampur ("we" dan "this review").
- Simpulan yang tumpang tindih dengan diskusi, dan tinjauan tanpa seksi
  keterbatasan.

## 8. Daftar periksa sebelum naskah dikirim

- [ ] Satu kalimat nilai tambah muncul di abstrak dan pendahuluan.
- [ ] Setiap seksi sintesis menjawab salah satu dari empat pertanyaan.
- [ ] Semua kueri lengkap dengan tanggal dan jumlah hasil (Lampiran B).
- [ ] Diagram alur memuat angka setiap tahap dan alasan eksklusi.
- [ ] Penyaring dan alat bantu AI disebut.
- [ ] Setiap klaim sintesis menyebut kajian, data, metode, dan angka.
- [ ] Tidak ada kode internal, jalur folder, atau `\authorcheck` yang tersisa.
- [ ] Semua angka korpus berupa makro dari `main6-angka.tex`.
- [ ] Ejaan Inggris konsisten memakai -ize.
