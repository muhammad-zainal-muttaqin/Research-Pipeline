# Tree-level citrus yield prediction utilizing ground and aerial machine vision and machine learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `vijayakumar2023tree` |
| Judul asli | Tree-level citrus yield prediction utilizing ground and aerial machine vision and machine learning |
| Penulis | Vijayakumar, Vinay; Ampatzidis, Yiannis; Costa, Lucas |
| Tahun | 2023 |
| Venue | Smart Agricultural Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [vijayakumar2023tree.pdf](../pdf/vijayakumar2023tree.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2022.100077

## Gambaran Umum

Makalah ini membangun tiga model pembelajaran mesin (*machine learning*, ML) untuk memprediksi hasil panen jeruk (*Citrus sinensis*, kultivar Hamlin) pada tingkat pohon di Florida, Amerika Serikat. Model-1 memakai citra pesawat tanpa awak (*unmanned aerial vehicle*, UAV) saja. Model-2 menambahkan hitungan buah dari citra darat satu sisi pohon. Model-3 menambahkan hitungan buah dari citra darat dua sisi pohon. Hitungan buah dihasilkan detektor YOLOv3, dan acuan evaluasi adalah jumlah buah hasil panen manual per pohon pada 48 pohon.

Hasil utamanya dinyatakan dengan *mean absolute percentage error* (MAPE) terbaik tiap model: Model-1 35,59%, Model-2 23,45%, dan Model-3 25,72%. Uji-t berpasangan menunjukkan Model-2 dan Model-3 berbeda nyata dari Model-1 (p = 0,0013 dan p = 0,0010), tetapi Model-2 dan Model-3 tidak berbeda nyata (p = 0,29). Penulis memilih Model-2 karena galatnya terendah dan pengumpulan datanya lebih sederhana.

Pada tingkat blok (48 pohon), ketiga model dinyatakan memprediksi hasil dengan akurasi lebih dari 99%. Penulis menyatakan bahwa penelitian berskala lebih besar diperlukan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Prediksi hasil jeruk sebelum panen dibutuhkan untuk merencanakan tenaga kerja, penyimpanan, dan transportasi. Penulis menyebut cara umum di Florida: mengambil sejumlah pohon tetap dari satu blok, menghitung seluruh buahnya, lalu mengekstrapolasi ke seluruh blok dengan memperhitungkan buah gugur menurut standar penyesuaian kehilangan buah negara bagian. Cara ini dinilai rawan galat karena ekstrapolasi, pemilihan pohon acak, dan indeks buah gugur yang seragam. Data panen aktual juga bersifat agregat menurut ruang dan waktu.

Penelitian terdahulu yang dirujuk menggunakan citra udara hiperspektral, ukuran pohon dari sensor ultrasonik, atau pengolahan citra untuk menghitung buah, tetapi menurut penulis hanya berfokus pada pengolahan citra dan tidak menghasilkan prediksi hasil per pohon. Penulis menyatakan bahwa sepengetahuan mereka belum ada pekerjaan lain yang menggabungkan citra UAV dan citra darat untuk membangun model prediksi hasil jeruk per pohon dengan ML.

## Ide Utama

Gagasannya adalah menggabungkan dua sumber data yang saling melengkapi. Citra UAV multispektral memberi informasi struktur dan kesehatan pohon (tinggi, luas tajuk, indeks kesehatan, lima pita spektral). Citra darat memberi hitungan buah yang tampak melalui detektor. Hitungan buah dari citra tidak dipakai langsung sebagai hasil panen, tetapi sebagai salah satu peubah masukan model regresi yang dilatih terhadap hitungan panen manual. Dengan cara ini, hitungan yang tidak lengkap karena oklusi daun diperlakukan sebagai indikator yang dikalibrasi terhadap hasil panen. Penulis menyatakan secara eksplisit bahwa tujuan detektor bukan menghitung semua buah pada pohon, melainkan memberi taksiran hitungan untuk model prediksi hasil.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Lokasi penelitian adalah blok kebun jeruk di Southwest Florida Research and Education Center, University of Florida (26°27'47" LU, 81°26'35" BB) dengan lebih dari 100 pohon Hamlin; 48 pohon dipilih. Seluruh data (UAV, citra darat, hitungan panen) dikumpulkan pada minggu ketiga dan keempat Maret 2020, dan panen manual dilakukan sekitar seminggu setelah data spektral dan citra dikumpulkan. Citra UAV diambil dengan DJI Phantom 4 Pro+ pada ketinggian 122 m sekitar tengah hari, memakai kamera RGB (tumpang tindih depan 80%, samping 70%) dan kamera multispektral RedEdge-M (tumpang tindih 80% depan dan samping). Citra darat diambil dengan kamera Canon EOS 5D, dua citra per pohon dari sisi timur dan barat baris, pada pukul 12.00 sampai 14.00 dan 17.00 sampai 18.00 untuk menghindari silau. Citra sisi depan diambil dari tengah blok pada jarak 3,8 m dari pusat pohon, dan sisi belakang dari blok sebelah pada jarak 5,4 m. Jumlah total citra darat adalah dua per pohon untuk 48 pohon (96 citra, dihitung dari uraian tersebut); jumlah citra beranotasi untuk pelatihan detektor tidak dilaporkan, hanya pembagian 80/20 antara pelatihan dan pengujian.

### 2. Pengolahan citra UAV

Citra dijahit dengan Pix4Dmapper menjadi peta untuk pita merah, hijau, biru, tepi merah (*red edge*), dan inframerah dekat. Tinggi pohon, luas tajuk, dan indeks kesehatan diekstraksi dengan Agroview, aplikasi berbasis awan dan kecerdasan buatan; makalah menyebut akurasi Agroview untuk tinggi pohon 95,53% dan luas tajuk 86,12% (dikutip dari acuan lain).

### 3. Deteksi dan hitungan buah

Buah dianotasi dengan LabelMe. YOLOv3 dilatih dengan bobot awal dari model yang sebelumnya dilatih pada buah jeruk muda (*immature citrus*), lalu dipakai untuk mendeteksi dan menghitung buah pada citra tiap sisi pohon. Hitungan satu sisi menjadi masukan Model-2, dan jumlah hitungan kedua sisi menjadi masukan Model-3.

### 4. Model regresi

Empat algoritma dipakai untuk setiap model: *gradient boosting regression* (GBR), *random forest regression* (RFR), *linear regression* (LR), dan *partial least squares regression* (PLSR). Peubah target adalah hitungan panen per pohon. Evaluasi memakai validasi silang lipat-5 (k = 5), dan metriknya MAPE rerata lintas lipatan. Detektor dievaluasi dengan presisi, recall, dan skor F1.

## Eksperimen dan Hasil

Detektor YOLOv3 mencapai presisi 0,96, recall 0,83, dan F1 0,88 secara keseluruhan (baris 1: recall 0,80, F1 0,87; baris 2: recall 0,86, F1 0,90; presisi 0,96 pada keduanya).

Tabel 1. MAPE rerata validasi silang lipat-5 (%) menurut model dan algoritma (Tabel 4, 5, dan 6 makalah).

| Algoritma | Model-1 (UAV) | Model-2 (UAV + 1 sisi) | Model-3 (UAV + 2 sisi) |
|---|---|---|---|
| PLSR | 35,84 | 23,45 | 25,72 |
| RFR | 41,47 | 31,29 | 37,78 |
| LR | 35,59 | 26,25 | 30,31 |
| GBR | 41,12 | 31,72 | 33,37 |

Penulis menyatakan penambahan hitungan buah memperbaiki MAPE terbaik dari 35,59% menjadi 23,45% (peningkatan yang disebut 34,11%). Pada Model-1, galat di atas 100% terjadi pada pohon kecil dengan hasil kurang dari 100 buah (hitungan panen 61, 87, 92, dan 44); penulis menyimpulkan bahwa prediksi dari data spektral saja tidak andal untuk pohon kecil. Pada pohon kecil, RMSE Model-2 adalah 54,64, dibandingkan 102,77 pada Model-1 dan 79,07 pada Model-3. Untuk pohon dengan hasil lebih dari 350 buah, Model-2 lebih baik daripada Model-1 pada 5 dari 7 pohon, dan Model-3 lebih baik daripada Model-1 pada 6 dari 7 pohon serta lebih baik daripada Model-2 pada 3 dari 7 pohon.

Tabel 2. Uji-t berpasangan antarmodel.

| Pasangan | p |
|---|---|
| Model-1 dan Model-2 | 0,0013 |
| Model-1 dan Model-3 | 0,0010 |
| Model-2 dan Model-3 | 0,29 |

Penulis menyatakan bahwa Model-2 dan Model-3 tanpa data UAV menunjukkan varians lebih tinggi, tetapi data itu tidak ditampilkan pada makalah.

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: gabungan data UAV dan data darat menurunkan galat dibanding UAV saja; Model-2 hanya memerlukan citra satu sisi sehingga lebih mudah diskalakan, misalnya dengan kamera pada kendaraan kebun yang merekam video satu sisi baris.

Keterbatasan yang dinyatakan penulis: detektor tidak dapat mendeteksi semua buah karena oklusi daun dan cabang, dan kualitas citra dipengaruhi spesifikasi kamera, waktu pengambilan, dan bayangan. Bobot awal berasal dari buah jeruk muda, dan penulis menyarankan lebih banyak citra buah matang dari beberapa kebun dan waktu. Penulis juga menyatakan perlunya percobaan berskala besar, pengujian di lokasi dan tanggal berbeda sebelum panen, serta analisis biaya terhadap metode manual. Kemungkinan penyebab Model-3 tidak lebih baik adalah penghitungan ganda buah dari dua sisi pohon, terutama saat kerapatan daun rendah, sebagaimana dinyatakan penulis.

Menurut pembacaan ringkasan ini, keterbatasan tambahan meliputi: hanya 48 pohon dari satu blok dan satu musim; hasil validasi silang dilaporkan sebagai rerata MAPE pada sampel kecil, dengan variasi antarlipatan besar (misalnya MAPE RFR Model-1 berkisar 26,48% sampai 86,53% antarlipatan); pemilihan algoritma terbaik dilakukan pada data yang sama dengan pelaporan; dan klaim akurasi blok lebih dari 99% tidak disertai rincian perhitungan pada teks.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat dari dua sisi pohon, tetapi tidak dengan mekanisme pencocokan identitas. Hitungan dua sisi dijumlahkan, dan penulis mengakui penghitungan ganda sebagai penyebab hitungan dua sisi menjadi berlebih dan Model-3 tidak lebih baik daripada Model-2. Koreksi terhadap hal itu dilakukan secara statistik tidak langsung, yaitu regresi terhadap hitungan panen, bukan dengan menghubungkan buah yang sama lintas sisi. Hitungan hanya satu kelas buah, tanpa pemisahan per kelas.

Acuan hitungannya adalah hitungan buah hasil panen manual per pohon, bukan anotasi citra. Bagi pencacahan tandan sawit multi-sisi, temuan yang dapat dipindahkan adalah bukti empiris bahwa penjumlahan mentah dua sisi dapat menggandakan hitungan dan menurunkan akurasi dibanding satu sisi, sehingga identitas lintas sisi perlu ditangani eksplisit. Makalah ini juga memperlihatkan pola kalibrasi hitungan citra terhadap panen sebagai peubah regresi, dengan keterbatasan skala 48 pohon.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `vijayakumar2023tree`.

Vijayakumar, Ampatzidis, dan Costa membandingkan tiga model ML untuk prediksi hasil jeruk Hamlin per pohon pada 48 pohon di Florida: citra UAV saja (MAPE terbaik 35,59%), UAV ditambah hitungan buah YOLOv3 dari citra darat satu sisi (23,45%), dan UAV ditambah hitungan dua sisi (25,72%). Hitungan dua sisi tidak lebih baik daripada satu sisi (p = 0,29), dan penulis mengaitkannya dengan kemungkinan penghitungan ganda buah dari kedua sisi pohon.

Catatan verifikasi data: MAPE per algoritma dan lipatan diambil dari Tabel 4, 5, dan 6; presisi, recall, dan F1 detektor dari Tabel 2 (Bagian 3.1); nilai p dari akhir Bagian 3.2; RMSE pohon kecil dan perbandingan pohon besar dari Bagian 4.2 serta Tabel 7 dan 8. Tabel 3 (data lengkap 48 pohon) terbaca sebagai deretan angka tanpa batas kolom, sehingga hanya dipakai untuk memastikan jumlah pohon. Jumlah citra beranotasi dan jumlah buah beranotasi untuk detektor tidak dilaporkan; hitungan 96 citra darat adalah turunan dari dua citra per 48 pohon. Pernyataan akurasi blok lebih dari 99% tidak disertai tabel pada teks. Tahun jurnal di berkas adalah 2023 (volume 3), sedangkan tersedia daring 9 Juni 2022.
