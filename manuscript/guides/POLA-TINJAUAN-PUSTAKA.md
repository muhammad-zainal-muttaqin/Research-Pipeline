# Pola Penulisan Tinjauan Pustaka

Dokumen ini merangkum cara menulis tinjauan pustaka (*literature review*) menurut
panduan metodologi dan contoh review yang terindeks Scopus. Isinya dipakai sebagai
dasar menulis ulang naskah `main5v3` dari awal menjadi `main6`.

## 1. Cara dokumen ini disusun

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
untuk 25 artikel (`metodologi/pdf/`); teksnya diekstrak ke `metodologi/teks/`.
Artikel lain dibaca dari abstraknya. Tabel di bagian 8 menandai mana yang dibaca
penuh dan mana yang hanya abstrak. Klaim di dokumen ini yang bersumber dari abstrak
saja ditulis lebih hati-hati.

Sebagai pembanding, dipakai juga laporan dosen pembimbing tentang delapan review di
*Computers and Electronics in Agriculture* (CEA) tahun 2026
(`literature/references/revisi-dosen-2026-07-23/CEA_review_conventions_report.md`).

## 2. Apa yang membedakan tinjauan yang baik

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

## 3. Pola yang ditemukan

### P1. Jenis dan fokus tinjauan dinyatakan sejak awal

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

### P2. Pertanyaan tinjauan dan kerangka diletakkan di depan

Baumeister dan Leary (1997) mencatat kesalahan yang paling sering pada naskah yang
ditolak: pengantar yang lemah. Penulis menunda gagasan pengikatnya sampai bagian
diskusi, sehingga pembaca harus membaca puluhan halaman tanpa tahu arah. Saran
mereka: sajikan kerangka konseptual lengkap di depan, atau setidaknya pratinjau
singkat "pesan utama" sebelum bukti dibahas. Sauer dan Seuring (2023) menempatkan
tiga keputusan pertama dari 14 keputusan SLR di tahap ini: merumuskan celah dan
pertanyaan, memilih pendekatan (induktif, deduktif, abduktif), dan menetapkan
kerangka serta konstruk yang akan dipakai untuk mengode studi.

### P3. Metode pencarian ditulis sampai dapat diulang

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

### P4. Seleksi dilaporkan dengan angka dan alasan eksklusi

PRISMA 2020 butir 8 meminta penulis menjelaskan cara memutuskan inklusi: berapa
penyaring, apakah bekerja independen, dan alat otomatis apa yang dipakai. Butir 16a
meminta alur angka dari rekaman teridentifikasi sampai studi terinklusi, sebaiknya
dengan diagram alir; butir 16b meminta contoh studi yang tampak memenuhi syarat
tetapi dikeluarkan, beserta alasannya. Dalam sampel CEA, tujuh dari delapan review
memuat diagram alir, dan enam memberi angka lengkap tiap tahap.

### P5. Sintesis disusun per konsep, bukan per penulis

Baumeister dan Leary (1997) menyebut "kurangnya integrasi" sebagai kesalahan kedua
yang sama merusaknya: penulis menguraikan studi satu per satu tanpa mengaitkannya
dengan pertanyaan. Pembaca, kata mereka, lebih membutuhkan bagaimana studi-studi itu
saling berhubungan daripada daftar lengkapnya. Van Wee dan Banister (2016) memberi
dua cara menyusun hasil: per sumber (baris = studi) atau per isi (baris = metode,
temuan, atau klaster). Untuk tinjauan yang ingin membangun kerangka, susunan per isi
lebih tepat. Torraco (2016, dari abstrak) menyebut tinjauan integratif yang baik
bersifat integratif, definitif, dan provokatif, dan menganjurkan representasi visual.

### P6. Bukti ditulis pada tingkat operasional

Ini pola yang paling praktis. Baumeister dan Leary (1997) memberi contoh: kalimat
"X menyebabkan Y (Rujukan)" tidak cukup. Tulislah "pada sampel A, metode B memberi
hasil C (Rujukan), sehingga mendukung pandangan bahwa X menyebabkan Y". Dengan begitu
pembaca bisa menilai sendiri apakah kesimpulan sesuai dengan bukti. Van Wee dan
Banister (2016) menambahkan tiga aturan:

1. Jangan merata-ratakan hasil studi dengan ukuran sampel berbeda secara naif;
   tampilkan hasil tiap studi bersama jumlah kasusnya, dan tampilkan rentangnya.
2. Pisahkan dengan jelas kesimpulan penulis asli dari tafsiran penulis review.
3. Jangan mengkritik studi karena tidak melakukan hal di luar ruang lingkupnya.

### P7. Mutu bukti dinilai, bukan hanya dicatat

Baumeister dan Leary (1997) menyebut "kurangnya penilaian kritis" sebagai kesalahan
berikutnya: kesimpulan tinjauan dibatasi oleh kelemahan studi yang ditinjau, jadi
kelemahan itu harus dinyatakan. Tranfield dkk. (2003), seperti dirangkum Kraus dkk.
(2022), memasukkan penilaian mutu studi sebagai fase tersendiri, di antara seleksi
studi dan ekstraksi data. Untuk topik teknik, penilaian ini bisa berupa pertanyaan tetap
yang diajukan ke tiap studi: apakah ada data acuan yang independen, apakah uji
dilakukan di data yang tidak dipakai melatih, apakah metrik yang dilaporkan sesuai
dengan klaim.

### P8. Tabel ringkasan dan tabel sintesis

Van Wee dan Banister (2016) menyarankan tabel deskriptif (penulis, tahun, konteks,
ukuran sampel) terpisah dari tabel hasil, dan memindahkan tabel yang sangat panjang
ke lampiran. Dalam sampel CEA, tujuh dari delapan review memuat setidaknya satu
tabel sintesis besar, satu baris per studi. Revisi dosen butir 8 meminta hal yang
sama: matriks bukti masuk ke naskah sebagai tabel, bukan hanya berkas CSV terpisah.

### P9. Posisi terhadap review terdahulu dinyatakan eksplisit

Van Wee dan Banister (2016) meminta penulis menyebut review yang sudah ada dan
menjelaskan posisi tinjauannya. Contoh review domain melakukannya dengan kalimat
yang spesifik. Zhou dkk. (2021) menulis bahwa review SOD sebelumnya membahas model
berbasis RGB, sedangkan mereka membahas model RGB-D dan dataset-nya. Naranjo-Torres
dkk. (2020) membuat daftar kontribusi "dibandingkan review sebelumnya". Dalam sampel
CEA, enam dari delapan review melakukan pemosisian eksplisit. Revisi dosen butir 3
meminta pemosisian terhadap review kelapa sawit dan penghitungan buah.

### P10. Kontribusi konseptual berupa taksonomi atau kerangka keputusan

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

### P11. Penutup: tantangan, agenda, dan keterbatasan tinjauan itu sendiri

Semua review dalam sampel CEA ditutup dengan bagian tantangan dan arah riset, lalu
kesimpulan singkat. Agenda yang berguna menyebut apa yang harus diukur, di data apa,
dan dengan metrik apa, bukan sekadar "perlu penelitian lebih lanjut". Tinjauan juga
harus menyebut keterbatasannya sendiri: basis data yang tidak dicari, bahasa,
penyaringan oleh satu orang, dan akses teks lengkap.

### P12. Kebiasaan pada contoh review domain

Dua belas contoh review domain yang teksnya tersedia dicek dengan penghitungan kata
kunci sederhana (`metodologi/fitur_contoh.csv`). Hasilnya:

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

## 4. Kesalahan umum

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

## 5. Gaya bahasa

Pola P6 menentukan gaya. Setiap paragraf sintesis berisi: klaim, bukti operasional
(studi, data, metode, angka), tafsiran, lalu batasnya. Yang dihindari:

- Slogan dan kata sifat tanpa isi: "revolusioner", "terobosan", "sangat menjanjikan",
  "memainkan peran penting".
- Pembuka generik: "Dalam beberapa tahun terakhir, kecerdasan buatan telah...".
- Jargon tanpa definisi. Istilah teknis ditulis sekali dengan definisi singkat.
- Daftar tiga kata sifat yang berulang dan kalimat yang bisa ditukar ke topik lain
  tanpa kehilangan makna.
- Angka tanpa konteks. Setiap angka disertai data, split, dan metriknya.

## 6. Kerangka yang diterapkan pada naskah `main6`

Naskah `manuscript/source/main6.tex` + `main6-body.tex` menerapkan pola di atas
sebagai berikut.

| Bagian naskah `main6` | Isi | Pola |
|---|---|---|
| 1. Introduction | Masalah terukur (27–58% buah terlihat pada satu atau dua citra; 9,9% hitung ganda), kasus sensus sawit, empat pertanyaan tinjauan, tiga kontribusi | P2, P9, P10 |
| 2. Review method | Tipe tinjauan, sumber dan tanggal, tabel 13 eksekusi kueri, kriteria E1–E7, penyaringan, pengodean, penilaian bukti, alur PRISMA (Gambar 1) | P1, P3, P4, P7 |
| 3. Design space | Lima tahap dari akuisisi ke inventaris, tiga sumber hitung ganda, enam mekanisme M0–M5 beserta asumsinya (Gambar 3–5) | P10 |
| 4. Acquisition | Tabel II: delapan kajian yang membandingkan desain akuisisi pada pohon yang sama | P5, P6, P8 |
| 5. Evidence by mechanism | Tabel III: 13 perbandingan mekanisme pada data yang sama; bukti M1–M5; cara bukti diukur (Gambar 7) | P5, P6, P7, P8 |
| 6. Class attributes | Hitungan per kelas pada buah unik (19 kajian C1, 49 kajian C4) | P5, P6 |
| 7. Depth and other modalities | Peran depth pada deteksi, ukuran, dan asosiasi | P5, P6 |
| 8. Oil palm | 170 kajian menurut tugas dan lokasi (Gambar 6); celah pencacahan lintas pandang | P5, P9 |
| 9. Position | Tabel IV: sepuluh tinjauan terdahulu | P9 |
| 10. Gaps and agenda | G1–G5, masing-masing dengan ukuran yang harus dilaporkan | P11 |
| 11. Limitations | Sumber tunggal, abstrak dari layanan terbuka, satu peninjau dengan bantuan model bahasa | P11 |
| Lampiran A | Matriks bukti 187 kajian C1 | P4, P8 |

## 7. Daftar periksa sebelum naskah dikirim

- [ ] Satu kalimat nilai tambah dapat ditulis dan muncul di abstrak dan pendahuluan.
- [ ] Tipe tinjauan disebut dan sesuai dengan cara kesimpulan ditulis.
- [ ] Pertanyaan tinjauan tertulis dan setiap bagian sintesis menjawab salah satunya.
- [ ] Semua query ditulis lengkap dengan tanggal eksekusi dan jumlah hasil.
- [ ] Kriteria inklusi dan eksklusi bernomor; alasan eksklusi tercatat per rekaman.
- [ ] Diagram alir dengan angka setiap tahap.
- [ ] Jumlah penyaring dan alat bantu disebut, termasuk alat berbasis AI.
- [ ] Setiap klaim sintesis menyebut studi, data, metode, dan angka.
- [ ] Tidak ada rata-rata lintas studi yang tidak sebanding.
- [ ] Tabel pemosisian terhadap review terdahulu.
- [ ] Matriks bukti di naskah atau lampiran.
- [ ] Agenda menyebut apa yang diukur, dengan data dan metrik apa.
- [ ] Bagian keterbatasan tinjauan.
- [ ] Setiap rujukan dapat dilacak ke rekaman Scopus (EID atau DOI).

## 8. Sumber

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
