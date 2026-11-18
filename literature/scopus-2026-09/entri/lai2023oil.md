# Oil Palm Fresh Fruit Bunch Ripeness Detection Methods: A Systematic Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lai2023oil` |
| Judul asli | Oil Palm Fresh Fruit Bunch Ripeness Detection Methods: A Systematic Review |
| Penulis | Lai, Jin Wern; Ramli, Hafiz Rashidi; Ismail, Luthffi Idzhar; Wan Hasan, Wan Zuha |
| Tahun | 2023 |
| Venue | Agriculture Switzerland |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [lai2023oil.pdf](../pdf/lai2023oil.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture13010156

## Gambaran Umum

Tinjauan sistematis ini menjawab kebutuhan deteksi kematangan tandan buah segar (TBS) kelapa sawit sebagai langkah pertama sistem pemanen otomatis. Latar belakangnya adalah kelangkaan tenaga kerja di industri minyak sawit Malaysia, yang mendorong penggunaan robot otonom. Akurasi panen ditentukan oleh pemilihan TBS yang tepat, karena tingkat ekstraksi minyak (OER) paling tinggi dicapai bila buah dipanen pada kematangan yang benar. Cara petani memeriksa buah secara visual di lapang diakui rawan salah klasifikasi, sehingga penulis mengkaji metode penentuan kematangan yang objektif.

Sumber data adalah makalah yang diterbitkan antara 2012 dan 2022, berbahasa Inggris, ditemukan lewat Google Scholar dengan kombinasi kata kunci terkait minyak sawit, TBS, kematangan, dan klasifikasi, lalu disaring hanya yang mengusulkan metode deteksi kematangan TBS kelapa sawit. Abstrak menyebut 51 makalah dengan 11 pendekatan unik, sedangkan bagian diskusi menyebut 48 artikel yang dikaji; kedua angka ini dinyatakan penulis sendiri. Sampel berupa TBS utuh atau buah lepas (fruitlet), diambil dari perkebunan lalu umumnya dibawa ke laboratorium. Metode dibagi menjadi nondestruktif (visi warna, LiDAR, citra spektral, NIR, Raman, fluoresensi, gelombang mikro, induktif, hamburan balik laser, termal) dan destruktif (baterai buah). Visi warna adalah yang paling banyak dipakai, yaitu 22 artikel. Pengklasifikasi yang paling sering dipakai adalah ANN (13 artikel), diikuti CNN (7) dan SVM (6).

Mekanisme deteksi berbeda tiap modalitas. Visi warna menganalisis nilai RGB, dengan segmentasi Otsu atau Canny, lalu classifier ANN, SVM, atau CNN. LiDAR memancarkan laser 905 nm dan memakai jarak serta intensitas pantulan sebagai penanda kematangan. NIR memakai panjang gelombang 750–2500 nm untuk membaca komposisi kimia; Raman memakai puncak karoten; fluoresensi memakai rasio biru-merah (BRR_FRF); gelombang mikro memakai kandungan air lewat permitivitas relatif; sensor induktif memakai frekuensi resonansi; termal memakai suhu permukaan Buah. CNN bekerja lewat lapisan konvolusi dan pooling dan menghasilkan kotak pembatas, sehingga YOLOv3 dinilai mampu mendeteksi dan membedakan tingkat kematangan secara langsung. Angka hasil yang dikutip penulis bersumber dari kajian yang ditinjau, bukan percobaan baru: kombinasi hamburan balik laser dan visi komputer mencapai akurasi di atas 85% untuk klasifikasi kematangan TBS; desain kumparan ganda pada sensor induktif meningkatkan sensitivitas hingga 167%; frekuensi resonansi buah mentah dan matang masing-masing sekitar 8,5 MHz dan 9,8 MHz; kandungan air dan lipid buah mentah 80,1% dan 5,9%, berubah menjadi 24,7% dan 58,3% pada buah matang. Semua angka tersebut dilaporkan penulis sebagai hasil kajian pustaka, tanpa perhitungan ulang atau metrik statistik tambahan dalam tinjauan ini.

Batasan yang dinyatakan penulis mencakup kelemahan visi warna yang tidak dapat mengenali kematangan sebagian, karena satu sisi TBS bisa tampak matang sementara bagian lain masih mentah, sehingga citra dari sisi yang matang memicu salah klasifikasi. Sebagian besar eksperimen dilakukan di laboratorium dengan lingkungan terkendali yang bebas oklusi dan latar bising; hasil dari kondisi ideal tersebut diperkirakan tidak otomatis berlaku di kebun, apalagi dengan cuaca dan topografi yang menyulitkan akuisisi data. Dari 12 metode yang ditinjau, hanya tiga yang diuji langsung di lapang, yaitu visi komputer, LiDAR, dan sensor induktif. Penulis menyimpulkan kombinasi visi warna dan CNN sebagai sistem paling layak diterapkan, karena biaya rendah, nirkontak, mampu beroperasi secara langsung, dan dapat ditingkatkan dengan memperbesar data serta optimasi hyperparameter; arah lanjutan yang diusulkan adalah penggabungan sistem AI dengan IoT untuk penandaan lokasi pohon berbuah matang.

