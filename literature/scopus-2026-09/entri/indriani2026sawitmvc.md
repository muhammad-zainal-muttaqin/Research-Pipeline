# SawitMVC: A multi-view oil palm fruit bunch dataset for detection and counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `indriani2026sawitmvc` |
| Judul asli | SawitMVC: A multi-view oil palm fruit bunch dataset for detection and counting |
| Penulis | Indriani, Fatma; Saputro, Setyo Wahyu; Muttaqin, Muhammad Zainal; Rahmi, Alia; Saragih, Triando Hamonangan; Budianoor, Rahmat; Hartoni; Kartini, Dwi; Said, Naufal |
| Tahun | 2026 |
| Venue | Data in Brief |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [indriani2026sawitmvc.pdf](../pdf/indriani2026sawitmvc.pdf)
- DOI resmi: https://doi.org/10.1016/j.dib.2026.112990

## Gambaran Umum

Makalah ini merupakan artikel data (*Data Article*) pada jurnal *Data in Brief* yang memperkenalkan SawitMVC, kumpulan data citra multi-sisi tandan buah segar kelapa sawit (*Elaeis guineensis*) untuk deteksi dan pencacahan. Kumpulan data memuat 3.992 citra ponsel pintar dari 953 pohon pada dua perkebunan komersial di Kabupaten Tanah Laut, Kalimantan Selatan (perkebunan DAMIMAS 854 pohon dan LONSUM 99 pohon). Setiap pohon difoto dari empat sisi dengan selang 90 derajat atau delapan sisi dengan selang 45 derajat. Tandan dianotasi dalam empat kelas kematangan *Black Bunch Census* (BBC), yaitu B1 (≤1 bulan menuju panen), B2 (~2 bulan), B3 (~3 bulan), dan B4 (~4 bulan).

Kumpulan data memiliki dua lapis anotasi: kotak pembatas format YOLO per citra (18.540 kotak pada 3.926 citra beranotasi) dan berkas JSON kebenaran dasar per pohon yang mencatat 9.823 tandan unik beserta tautan identitas lintas sisi. Lapis kedua memungkinkan evaluasi algoritma pencacahan terpisah dari kinerja detektor.

Makalah juga melaporkan dua acuan dasar (*baseline*) yang sengaja tidak di-tuning. Detektor YOLO26m mencapai AP50 keseluruhan 0,531 pada data uji. Pada pencacahan, akurasi Class ±1 turun dari 96,81% (anotasi sebagai masukan, penghitung SVR) menjadi 75,35% (deteksi YOLO26m, penghitung SVR). Penulis menyimpulkan bahwa deteksi, bukan tahap pencacahan, merupakan sumber galat dominan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi hasil kebun sawit dilakukan secara berkala melalui BBC, yaitu praktik lapangan nondestruktif ketika petugas terlatih menghitung dan mengklasifikasikan tandan yang terlihat pada sampel pohon untuk memproyeksikan produksi bulan-bulan berikutnya. Setiap kelas BBC dipetakan ke fraksi pematangan bulanan pada model peramalan Ulu Bernam, sehingga hitungan per kelas menjadi keluaran operasional utama, bukan hitungan total saja.

Tandan muncul pada ketinggian dan sisi yang beragam di sekeliling tajuk, sehingga tidak ada satu sudut pandang yang menangkap seluruh inventaris tandan pada pohon. Pemotretan dari beberapa posisi tetap di sekeliling batang menjawab geometri ini, tetapi tandan yang sama muncul pada beberapa citra. Penjumlahan langsung hasil deteksi melebihi jumlah tandan unik yang sebenarnya, sehingga diperlukan deduplikasi lintas pandang.

Menurut penulis, kumpulan data sawit publik yang ada menangani deteksi dan penilaian kematangan, tetapi tidak menyediakan hitungan tandan unik per pohon yang independen dari keluaran deteksi. Kumpulan data multi-pandang untuk buah lain (apel) menyediakan hitungan, tetapi identitas buah dipulihkan dari rekonstruksi *structure-from-motion* (SfM) atau stereo, bukan dari anotasi pakar. Tabel 1 makalah membandingkan kumpulan data tersebut berdasarkan tanaman, kondisi, jumlah citra, kelas, anotasi, ketersediaan hitungan, dan cara pengambilan multi-pandang.

## Ide Utama

Kontribusi makalah adalah desain kumpulan data dengan dua target evaluasi yang dapat dipakai terpisah atau bersama. Target pertama adalah deteksi dan klasifikasi kematangan dari kotak pembatas. Target kedua adalah pencacahan tandan unik per pohon dan per kelas dari kebenaran dasar JSON yang dibuat secara manual oleh anotator, lengkap dengan tautan penampakan lintas sisi.

Identitas tandan lintas sisi tidak diturunkan dari rekonstruksi geometris, melainkan dari tautan berpasangan yang dikonfirmasi anotator pada dua sisi bersebelahan. Himpunan tautan itu membentuk graf atas seluruh kotak pada satu pohon, dan setiap komponen terhubung dianggap sebagai satu tandan fisik. Pendekatan ini memungkinkan pengukuran akurasi pencacahan tanpa bercampur dengan galat detektor, dan memakai citra ponsel pintar biasa tanpa sensor kedalaman.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Citra diambil pada Februari 2026 dari dua perkebunan komersial di Kabupaten Tanah Laut, Kalimantan Selatan: DAMIMAS (varietas DxP Dami Mas, 854 pohon) dan LONSUM (PT PP London Sumatra Indonesia, 99 pohon), total 953 pohon pada beberapa blok. Beberapa tim lapangan bekerja bersamaan. Seluruh pohon yang dikumpulkan dimasukkan tanpa penyaringan, termasuk pohon yang tidak memiliki tandan beranotasi.

Setiap pohon dipotret dari empat atau delapan posisi dengan selang sudut kira-kira sama di sekeliling batang. Sebanyak 908 pohon (95,3%) memiliki empat sisi dan 45 pohon (4,7%) memiliki delapan sisi. Operator diinstruksikan memotret dari jarak kira-kira 2–3 m dari batang; kepatuhan terhadap jarak ini tidak diverifikasi. Citra diambil dengan sepuluh model ponsel pintar konsumen (Xiaomi Redmi Note 12 Pro 5G, Redmi Note 11 Pro 5G, Poco F6, Samsung Galaxy A55 5G, A52 5G, A56 5G, iPhone 11, iPhone 14 Pro, Realme C33, dan Infinix Hot 10s) dengan eksposur otomatis. Citra disimpan 960 × 1280 piksel berorientasi potret dalam format JPEG. Aplikasi seluler PohonKu dipakai operator untuk registrasi pohon, urutan sisi, dan metadata; nama berkas mengikuti pola `{VARIETY}_{BLOCK}_{TREEID}_{VIEW}.jpg`.

### 2. Anotasi kotak pembatas

Tujuh anotator terlatih menggambar kotak pada setiap tandan yang terlihat dan menetapkan kelas B1–B4 menggunakan alat anotasi berbasis web. Definisi kelas mengikuti kriteria agronomi yang diverifikasi seorang pakar agronomi yang mengawasi proses. Satu peninjau memeriksa seluruh anotasi dan menerapkan koreksi sebelum ekspor ke format YOLO (`class_id cx cy w h` ternormalisasi).

Isyarat visual kelas menurut makalah adalah sebagai berikut. B1 adalah tandan terbesar dan paling khas dengan warna merah-jingga pada titik panen optimal. B2 telah mencapai kepadatan struktural penuh dan masih berwarna ungu tua hingga hitam. B3 masih membesar secara volumetrik dengan buah hitam yang rapat dan memanjang. B4 adalah tandan terkecil yang baru keluar dari tahap tersembunyi.

### 3. Anotasi identitas lintas sisi

Alat anotasi yang sama menampilkan dua sisi bersebelahan pada pohon yang sama. Anotator menunjuk kotak yang merupakan tandan fisik yang sama dan mencatat tautan terkonfirmasi (`_confirmedLinks`: `sideA`, `bboxIdA`, `sideB`, `bboxIdB`). Identitas tandan unik dihitung sebagai komponen terhubung (penutup transitif) dari graf tautan. Setiap rekaman tandan memuat kelas kematangan, `appearance_count` (jumlah sisi tempat tandan terlihat), dan rujukan silang ke kotak pada tiap sisi. Penanda `class_mismatch` ditetapkan otomatis bila kelas anotasi berbeda antarsisi dalam satu komponen. Anotasi, penautan, dan peninjauan berlangsung Maret hingga Mei 2026.

### 4. Pembagian data dan pengemasan

Pohon dibagi menjadi latih 716, validasi 96, dan uji 141 (kira-kira 75/10/15 berdasarkan jumlah pohon), terstratifikasi menurut varietas dan kelas kematangan dominan. Seluruh citra satu pohon masuk ke pembagian yang sama. Repositori berisi direktori `images/`, `labels/`, `json/` (953 berkas), dan `data/` (satu berkas Parquet `ground_truth.parquet`, satu baris per tandan unik), serta `data.yaml`, daftar pembagian, metadata ML Croissant, dan skrip unduh. Data dirilis di Zenodo dengan lisensi CC BY-NC 4.0.

### 5. Acuan dasar deteksi dan pencacahan

Detektor YOLO26m di-*fine-tune* pada 716 pohon latih dengan `epochs = 60`, `batch = 32`, `imgsz = 640`, `patience = 60`, dan `seed = 42`. Untuk pencacahan, dua strategi dikenakan pada deteksi per sisi setiap pohon uji. Strategi pertama adalah faktor koreksi global yang membagi jumlah naif per kelas dengan k = 1,8905, lalu membulatkan ke bilangan bulat terdekat. Nilai k adalah rasio kotak terhadap tandan unik pada data latih (14.041 / 7.427) sehingga tidak memuat informasi dari data uji.

Strategi kedua adalah *support vector regression* (SVR) dengan kernel RBF dan pengaturan bawaan scikit-learn (C = 1,0, epsilon = 0,1, gamma = "scale"). Empat model dilatih, satu per kelas B1–B4, dari vektor fitur lintas sisi 13 dimensi yang meliputi jumlah naif per kelas, nilai maksimum dan rerata per kelas antarsisi, dan jumlah sisi. Tidak ada pencarian hiperparameter, fitur tidak distandardisasi, dan prediksi dipotong pada nol serta dibulatkan. Setiap strategi dievaluasi pada dua kondisi: anotasi kebenaran dasar sebagai masukan (batas atas yang memisahkan mutu pencacahan dari galat detektor) dan prediksi YOLO26m (kinerja ujung ke ujung).

## Eksperimen dan Hasil

### Statistik kumpulan data

Tabel 2 makalah merangkum pembagian data.

| Pembagian | Pohon | Citra | Kotak YOLO | Tandan unik | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|---|---|
| Latih | 716 | 3.000 | 14.041 | 7.427 | 739 | 1.337 | 3.818 | 1.533 |
| Validasi | 96 | 404 | 1.887 | 992 | 95 | 198 | 504 | 195 |
| Uji | 141 | 588 | 2.612 | 1.404 | 120 | 256 | 745 | 283 |
| Total | 953 | 3.992 | 18.540 | 9.823 | 954 | 1.791 | 5.067 | 2.011 |

Distribusi kelas pada 9.823 tandan unik adalah B3 51,6% (5.067), B4 20,5% (2.011), B2 18,2% (1.791), dan B1 9,7% (954). Jumlah kotak per citra berkisar 0 hingga 10 dengan rerata 4,64 dan median 5; 66 citra tidak memiliki anotasi karena tidak ada tandan yang terlihat. Jumlah tandan unik per pohon berkisar 0 hingga 22 dengan rerata 10,31 dan median 10. Setiap tandan unik muncul pada 1 hingga 6 sisi; 74,6% muncul pada dua sisi atau lebih, dengan rerata jumlah penampakan 1,89.

### Hasil deteksi YOLO26m (data uji)

| Kelas | AP50 | Presisi | *Recall* |
|---|---|---|---|
| Keseluruhan | 0,531 | 0,508 | 0,571 |
| B1 | 0,739 | 0,602 | 0,776 |
| B2 | 0,433 | 0,482 | 0,441 |
| B3 | 0,599 | 0,515 | 0,674 |
| B4 | 0,354 | 0,432 | 0,393 |

### Hasil pencacahan (141 pohon uji)

| Deteksi | Penghitung | Class ±1 Acc | Tree ±1 Acc | Macro MAE | Mean Bias |
|---|---|---|---|---|---|
| Kebenaran dasar | Jumlah naif | 50,00% | 6,38% | 2,142 | +2,142 |
| Kebenaran dasar | Koreksi global (k = 1,89) | 95,57% | 86,52% | 0,356 | +0,009 |
| Kebenaran dasar | SVR | 96,81% | 88,65% | 0,303 | −0,048 |
| YOLO26m | Koreksi global (k = 1,89) | 72,34% | 30,50% | 1,119 | 0,381 |
| YOLO26m | SVR | 75,35% | 33,33% | 1,027 | 0,158 |

Class ±1 Acc adalah proporsi pohon dengan hitungan prediksi dalam rentang ±1 dari kebenaran dasar, dirata-ratakan makro atas B1–B4. Tree ±1 Acc adalah proporsi pohon yang keempat kelasnya serentak berada dalam ±1. Macro MAE dan Mean Bias adalah galat absolut rerata dan galat bertanda (prediksi − benar) per kelas, dirata-ratakan makro. Penulis menyatakan SVR lebih baik daripada koreksi global pada kedua kondisi, paling jelas pada Tree ±1 dan MAE. Kesenjangan antarkondisi besar (Class ±1 turun dari 96,81% menjadi 75,35%), sehingga deteksi merupakan sumber galat dominan.

## Kelebihan dan Keterbatasan

Kelebihan menurut penulis adalah kumpulan data sawit publik pertama yang memasangkan kotak pembatas per citra dengan kebenaran dasar tandan unik per pohon, memakai citra ponsel biasa yang kompatibel dengan alur kerja lapangan, dilengkapi pembagian latih/validasi/uji yang telah ditentukan, tabel Parquet, dan metadata Croissant.

Keterbatasan yang dinyatakan penulis:

- Seluruh citra berasal dari dua perkebunan komersial di Kalimantan pada satu periode pengumpulan (Februari 2026), sehingga perubahan musiman distribusi kematangan dan perbedaan pengelolaan kebun tidak tertangkap.
- Hanya dua varietas yang terwakili dan DAMIMAS mencakup 854 dari 953 pohon (89,6%), sehingga generalisasi ke varietas lain belum tentu berlaku.
- Citra diambil dengan beragam ponsel pada cahaya sekitar dan eksposur otomatis; tidak ada pencahayaan terkendali maupun informasi kedalaman, dan mutu citra bervariasi.
- Label kematangan memiliki ambiguitas yang tidak dapat dihilangkan pada batas B2/B3, dan kesepakatan antaranotator tidak diukur secara formal.
- Metadata per pohon seperti umur pohon atau tinggi tajuk tidak dicatat.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan tambahan. Pertama, acuan dasar dilatih dan diuji pada satu pembagian dengan satu *seed* sehingga tidak ada ukuran ragam. Kedua, jarak pemotretan 2–3 m tidak diverifikasi, sehingga ukuran tandan pada citra dapat bervariasi. Ketiga, identitas lintas sisi hanya ditautkan antara sisi yang bersebelahan menurut alat anotasi, sedangkan konsistensi tautan antara anotator tidak dilaporkan. Keempat, acuan hitung adalah anotasi citra, bukan hitung panen atau hitung manual di lapangan.

## Kaitan dengan Tinjauan main6

Makalah ini menangani tandan yang terlihat lebih dari sekali, tetapi sebagai penyedia data, bukan pengusul algoritma pencocokan. Mekanismenya adalah tautan berpasangan buatan manusia antarsisi bersebelahan dengan penutup transitif untuk membentuk identitas unik. Untuk pencacahan, hanya dua penghitung dasar yang diuji: pembagian dengan faktor koreksi global k = 1,8905 dan SVR per kelas dari fitur ringkasan lintas sisi. Tidak ada pencocokan penampakan atau rekonstruksi 3D yang dievaluasi. Hitungan dilaporkan per kelas (B1–B4), dan acuan hitung adalah anotasi citra per pohon oleh anotator di bawah pengawasan pakar agronomi, bukan hasil panen atau hitung lapangan.

Bagi pencacahan tandan sawit multi-sisi, makalah ini menyediakan data, definisi kelas, protokol pemotretan empat atau delapan sisi, dan metrik pencacahan (Class ±1, Tree ±1, Macro MAE, Mean Bias) yang dapat langsung dipakai sebagai acuan. Temuan bahwa jumlah naif melebihi hitungan unik (Class ±1 hanya 50,00% pada anotasi) dan bahwa deteksi mendominasi galat ujung ke ujung dapat dipakai untuk memotivasi metode identitas lintas sisi yang lebih kuat.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `indriani2026sawitmvc`.

Indriani dkk. merilis SawitMVC, kumpulan data 3.992 citra ponsel pintar dari 953 pohon kelapa sawit di dua perkebunan komersial di Kalimantan Selatan, difoto dari empat atau delapan sisi, dengan 18.540 kotak pembatas pada empat kelas kematangan BBC dan kebenaran dasar 9.823 tandan unik beserta tautan identitas lintas sisi yang dianotasi manual. Pada data uji 141 pohon, detektor YOLO26m mencapai AP50 0,531, dan penghitung SVR mencapai akurasi Class ±1 sebesar 96,81% dengan masukan anotasi tetapi 75,35% dengan deteksi YOLO26m, yang menunjukkan bahwa deteksi merupakan sumber galat dominan.

Catatan verifikasi data: Statistik kumpulan data bersumber dari Tabel 2 dan seksi 3.2, 3.3, serta 3.5. Hasil deteksi bersumber dari Tabel 3 dan hasil pencacahan dari Tabel 4 (seksi 4.7). Nilai k = 1,8905 dan rasio 14.041 / 7.427 tertulis di seksi 4.7. Teks ekstraksi menyajikan tabel secara terpecah per sel, tetapi nilainya dapat dibaca dan dicocokkan dengan total pada teks. Gambar 1–8 tidak terbaca dari teks. Makalah tidak melaporkan hasil per kelas untuk pencacahan, tidak melaporkan ragam antar-*seed*, dan tidak mengukur kesepakatan antaranotator. Lisensi artikel tertulis CC BY, sedangkan lisensi data tertulis CC BY-NC 4.0. Tanggal pada metadata JSON contoh (2026-05-16) adalah tanggal penyelesaian anotasi, bukan tanggal pemotretan. Berkas ini ditulis dari teks ekstraksi PDF berbahasa Inggris.
