# Blueberry Yield Estimation Through Multi-View Imagery with YOLOv8 Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2023blueberry` |
| Judul asli | Blueberry Yield Estimation Through Multi-View Imagery with YOLOv8 Object Detection |
| Penulis | Li, Zhengkun; Li, Changying; Munoz, Patricio |
| Tahun | 2023 |
| Venue | 2023 Asabe Annual International Meeting |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | blueberry |

## Tautan Akses
- PDF: [li2023blueberry.pdf](../pdf/li2023blueberry.pdf)
- DOI resmi: https://doi.org/10.13031/aim.202300883

## Gambaran Umum

Makalah ini adalah presentasi pertemuan ASABE 2023 (bukan artikel jurnal yang ditelaah sejawat) yang mengusulkan estimasi hasil blueberry per tanaman dari citra tiga pandang (atas, kiri, kanan) yang diambil oleh platform robot beroda di lapangan pemuliaan University of Florida di Citra, Florida. Buah blueberry dideteksi dengan YOLOv8x pada setiap pandang. Jumlah deteksi dari ketiga pandang kemudian dimasukkan ke regresi linear berganda untuk memperkirakan jumlah buah per tanaman. Kotak prediksi juga dipakai membuat peta kerapatan (*density map*).

Pada 12 tanaman dengan genotipe berbeda, yang dipanen dan dihitung manual, regresi multi-pandang menghasilkan kesalahan persentase absolut rata-rata (*mean absolute percentage error*, MAPE) 24,63% dan $R^2$ sebesar 0,77. Pandang atas saja menghasilkan MAPE 29,86% dan $R^2$ sebesar 0,75, sedangkan pandang kiri saja menghasilkan MAPE 30,5%. Penulis menyatakan keunggulan multi-pandang sebesar 5,2% sampai 15,7% terhadap pendekatan satu pandang. Detektor terbaik (YOLOv8x, masukan 1280) mencapai mAP@0,5 sebesar 77,3% pada 39 citra uji.

Penulis sendiri menyatakan bahwa penggabungan informasi spasial antarpandang tidak dapat dilakukan karena ketiga kamera tidak memiliki tumpang tindih yang cukup. Dengan demikian, makalah ini tidak melakukan pencocokan identitas buah lintas pandang, tetapi hanya menjumlahkan hitungan per pandang dengan bobot hasil regresi.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Blueberry tumbuh bergerombol dan sering tertutup daun atau buah lain, sehingga penghitungan buah satu per satu hampir tidak mungkin. Penulis membedakan dua pendekatan terdahulu: pengambilan sampel sedikit tanaman atau tandan yang diekstrapolasi dengan pengetahuan pakar, dan regresi tidak langsung yang memakai peubah terkait hasil (indeks vegetasi, cuaca, tanah). Metode langsung terbatas ukuran sampel dan tenaga kerja, sedangkan metode tidak langsung bergantung pada data yang banyak dan beragam.

Penulis menyatakan bahwa sebagian besar penelitian sebelumnya berfokus pada blueberry liar atau gerombolan kecil. Pada blueberry liar, buah umumnya terlihat dari atas. Pada blueberry komersial, buah berada pada ketinggian yang berbeda pada semak sehingga satu pandang tidak mencukupi dan sebagian besar buah tersembunyi. Pengambilan sampel juga dapat menimbulkan bias. Tujuan penelitian ada tiga: merancang platform seluler dengan sensor multi-kamera dan membangun dataset blueberry, membandingkan konfigurasi YOLOv8 untuk objek kecil dan padat, dan memvalidasi estimasi hasil melalui regresi multi-pandang.

## Ide Utama

Gagasan utamanya adalah memperlakukan setiap pandang sebagai pengamatan parsial dari tanaman yang sama, lalu menghubungkan hitungan terdeteksi dari ketiga pandang dengan hitungan manual per tanaman melalui regresi linear. Karena tumpang tindih antarkamera tidak cukup untuk pencocokan fitur, penulis tidak menyatukan identitas buah. Bobot regresi mencerminkan seberapa banyak buah yang terlihat pada tiap pandang. Penulis mencatat bahwa hubungan regresi hanya berlaku untuk sistem pencitraan yang sama (posisi dan resolusi kamera) sehingga tidak dapat digeneralisasi.

```
  Atas  ----\
  Kiri  -----+--> pangkas per tanaman --> YOLOv8x --> hitungan tiap pandang
  Kanan ----/       (manual)                              |
                                                          v
                                         regresi linear -> jumlah buah per tanaman
                                         kotak prediksi -> peta kerapatan
```

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Lapangan berada di IFAS Plant Science Research and Education Unit, Citra, Florida (29,408593 LU; 82,164398 BB), dengan berbagai genotipe untuk pemuliaan. Data diambil di barisan kedua dan ketiga dari atas. Jarak antarbaris 3 m dan jarak antartanaman 0,5 m. Tinggi tanaman bervariasi dari 0,4 sampai 2,0 m. Sistem pencitraan dipasang pada robot beroda empat (empat kemudi dan empat penggerak) yang dikendalikan dengan ROS, dan bergerak dengan kecepatan 0,2 sampai 0,4 m/s. Sembilan kamera dari tiga sistem merekam dari atas, kiri, dan kanan: tiga kamera Panasonic Lumix G7 (foto 4592×3448 atau video 1920×1080), tiga kamera Raspberry Pi 3MP (1920×1080, 30 FPS, terekam dengan data RTK-GPS dalam ROSBAG), dan satu RealSense D435i (RGB dan depth 1280×720, 15 FPS). Penulis menyebut tiga jenis sistem dan sembilan kamera, tetapi uraian menyebutkan 3 + 3 + 1 kamera, dan selisihnya tidak dijelaskan. Dataset yang dipakai hanya citra RGB.

### 2. Dataset Field-Blueberry

Dataset terdiri dari tiga bagian (Tabel 1 makalah):

| Subset | Jumlah citra | Citra beranotasi | Keterangan |
|---|---|---|---|
| HANDset | 19.460 | 215 | Kamera digital dan ponsel, 2018 sampai 2023 |
| OPENset | 92 | 92 | Dataset terbuka Roboflow, anotasi diubah; berfokus pada gerombol |
| ROBOset | 4.742 | 50 | Sistem multi-pandang robot; berfokus pada tanaman individu |

Jumlah buah per citra beranotasi berkisar dari 45 hingga lebih dari 3.000, dan sebagian besar citra memuat lebih dari 100 buah. Anotasi dibantu model (Roboflow): YOLOv8 dilatih pada OPENset dan beberapa citra anotasi sendiri, lalu dilatih ulang tiga kali sehingga mampu memberi 40% sampai 70% kotak sebagai pra-anotasi. Kultivar atau genotipe tiap citra tidak dilaporkan, kecuali bahwa 12 tanaman uji memiliki genotipe yang berbeda.

### 3. Detektor YOLOv8

Dataset diperbanyak enam kali dengan penambahan data (kecerahan -15% dan +15%, buram hingga 0,5 piksel, pemotongan 0 sampai 20%, dan mosaic), lalu dibagi 80:20 menjadi data latih dan validasi. Data uji adalah 39 citra tambahan yang diambil dengan platform multi-pandang pada 12 April 2023. Model dilatih dengan kerangka Ultralytics, dan konfigurasi N, S, M, L, X pada ukuran masukan 640 dan 1280 dibandingkan, serta YOLOv5x sebagai pembanding. Kecepatan diukur pada GPU Tesla T4. Karena alur kerja bersifat luring, penulis memilih YOLOv8x.

### 4. Pemangkasan per tanaman

Citra tiga pandang dipangkas per tanaman berdasarkan stempel waktu dan informasi spasial lapangan. Pemangkasan otomatis gagal karena penyelarasan antarpandang dengan ORB menghasilkan banyak pasangan fitur yang salah, misalnya fitur pada bagian robot yang dicocokkan dengan tajuk tanaman, sehingga pemangkasan dilengkapi secara manual. Penulis menyebut alternatif yang belum diuji, yaitu penjahitan panorama dan LoFTR.

### 5. Regresi multi-pandang

Regresi linear berganda: $y = a_0 + a_1 x_{atas} + a_2 x_{kiri} + a_3 x_{kanan}$, dengan $x$ adalah jumlah blueberry terdeteksi pada tiap pandang. Hasilnya $a_0=-6{,}47$, $a_1=1{,}11$, $a_2=0{,}73$, $a_3=0{,}45$ dengan $R^2=0{,}772$. Regresi linear dipilih karena jumlah pasangan data terbatas (12 tanaman).

### 6. Peta kerapatan

Kotak prediksi digambar pada citra putih berukuran sama, lalu dikaburkan dengan filter Gauss berinti tetap. Ukuran inti ditentukan dari analisis rata-rata ukuran buah pada data latih. Hasil abu-abu diubah menjadi citra warna semu dan dicampur dengan citra RGB asli. Evaluasi peta kerapatan hanya berupa ilustrasi pada Gambar 10, tanpa angka.

## Eksperimen dan Hasil

### Kinerja detektor (Tabel 2 makalah, 39 citra uji)

| Model | Ukuran | Presisi | Recall | mAP@0,5 | mAP@0,5-0,95 | Parameter (juta) | Kecepatan T4 (ms) |
|---|---|---|---|---|---|---|---|
| YOLOv5x | 640 | 78,9 | 46,5 | 62,0 | 29,5 | 86,7 | 46,1 |
| YOLOv5x | 1280 | 87,7 | 62,7 | 76,6 | 47,5 | 86,7 | tidak terbaca |
| YOLOv8n | 640 | 69,2 | 45,6 | 58,4 | 30,5 | 3,2 | 10,6 |
| YOLOv8n | 1280 | 86,1 | 61,2 | 75,1 | 46,8 | 3,2 | 16,0 |
| YOLOv8s | 1280 | 86,9 | 63,1 | 76,5 | 48,7 | 11,2 | 34,4 |
| YOLOv8m | 1280 | 87,1 | 63,0 | 76,6 | 48,8 | 25,9 | 82,5 |
| YOLOv8l | 1280 | 87,8 | 62,7 | 76,6 | 48,5 | 43,7 | 125,0 |
| YOLOv8x | 640 | 81,0 | 54,1 | 69,0 | 39,3 | 68,2 | 58,5 |
| YOLOv8x | 1280 | 88,3 | 63,3 | 77,3 | 49,0 | 68,2 | 232,3 |

Tabel pada teks ekstraksi tersusun per sel sehingga pengelompokan kolom di atas disimpulkan dari urutan nilai. Baris YOLOv8s, YOLOv8m, dan YOLOv8l pada ukuran 640 memiliki mAP@0,5 masing-masing 65,7, 68,0, dan 68,9. YOLOv8x 1280 memberi mAP@0,5 tertinggi (77,3%) pada sekitar 4,3 FPS di Tesla T4. YOLOv8n 1280 hanya 2,2 poin lebih rendah dengan kecepatan sekitar empat belas kali lebih cepat menurut penulis. Masukan 1280 memberi mAP lebih tinggi sekitar 10 sampai 17 poin daripada 640, dengan selisih mengecil pada model besar. YOLOv8x lebih baik daripada YOLOv5x, terutama pada masukan 640 (kenaikan mAP@0,5 sebesar 7 poin dengan parameter lebih sedikit).

Regresi antara hitungan prediksi (benar positif ditambah positif palsu) dan hitungan anotasi pada citra uji memberi $R^2$ sebesar 0,87, dan penulis mencatat bahwa model cenderung menaksir terlalu rendah. MAPE sebagian besar deteksi di bawah 25%. Pada satu citra pandang atas (Gambar 8), jumlah anotasi adalah 572, prediksi 526, benar 490, salah 82, dan terlewat 36. Persentase yang dilaporkan penulis untuk citra itu adalah 85,67% benar, 15,58% salah deteksi, dan 6,29% terlewat.

### Multi-pandang terhadap satu pandang (12 tanaman, hitungan panen manual)

| Pendekatan | $R^2$ | MAPE (%) | Visibilitas (anotasi / hitungan manual) |
|---|---|---|---|
| Multi-pandang | 0,77 | 24,63 | tidak berlaku |
| Pandang atas | 0,75 | 29,86 | 52,7% |
| Pandang kiri | tidak dilaporkan | 30,5 | 47,3% |
| Pandang kanan | tidak dilaporkan | tidak dilaporkan pada teks | 38,1% |

Keempat pendekatan dibandingkan pada Gambar 9, tetapi nilai MAPE dan $R^2$ untuk pandang kanan serta $R^2$ pandang kiri tidak tertulis pada teks. Kenaikan 5,2% sampai 15,7% yang dinyatakan penulis konsisten dengan selisih MAPE multi-pandang terhadap pandang atas (29,86 − 24,63 = 5,23, dihitung ringkasan ini), sedangkan basis nilai 15,7% tidak dijelaskan pada teks. Hanya sekitar setengah buah terlihat pada pandang atas, yang merupakan pandang dengan cakupan tertinggi.

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: platform robot multi-kamera dapat menghasilkan estimasi per tanaman, multi-pandang meningkatkan akurasi dan ketahanan terhadap oklusi dibandingkan satu pandang, kotak prediksi dapat dipakai membuat peta kerapatan untuk fenotipe, dan acuan estimasi berupa hitungan panen manual per tanaman.

Keterbatasan yang dinyatakan penulis: tidak ada tumpang tindih yang cukup antara tiga kamera, sehingga penggabungan informasi spasial antarpandang tidak mungkin; penyelarasan otomatis dengan ORB gagal, sehingga pemangkasan per tanaman memerlukan campur tangan manual; hubungan regresi hanya berlaku untuk sistem pencitraan yang sama; buah yang jatuh tetap terdeteksi; gerombol yang tumpang tindih, bayangan, dan baris tetangga menyebabkan kesalahan deteksi; dan hanya regresi linear yang dipakai karena sampel terbatas.

Menurut pembacaan ringkasan ini, ada beberapa keterbatasan tambahan. Pertama, regresi dilatih dan dinilai pada 12 tanaman yang sama tanpa validasi silang yang dilaporkan, dengan tiga koefisien dan satu intersep, sehingga $R^2$ dan MAPE kemungkinan optimistis. Kedua, hitungan manual per tanaman tidak dibandingkan dengan hasil timbangan, dan makalah menghitung semua buah tanpa memandang kematangan. Ketiga, tidak ada hitungan per kelas. Keempat, makalah bukan terbitan yang ditelaah sejawat, sebagaimana dinyatakan pada halaman judulnya. Kelima, gagasan multi-pandang tidak memecahkan buah ganda, karena buah yang tampak pada dua pandang dihitung pada kedua pandang dan hanya dikoreksi secara statistik oleh bobot regresi.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat dari lebih dari satu pandang, tetapi tidak dengan pencocokan identitas. Mekanismenya adalah koreksi statistik: hitungan deteksi dari tiga pandang digabung melalui regresi linear berganda terhadap hitungan panen manual per tanaman. Upaya pencocokan fitur geometris antarpandang (ORB) dilaporkan gagal, dan penulis menyatakan penggabungan spasial tidak dapat dilakukan. Hitungan tidak dilaporkan per kelas. Acuan hitung adalah hitungan manual dari semua buah per tanaman pada saat panen (tanpa memandang kematangan), disertai anotasi kotak citra untuk menilai deteksi dan visibilitas.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: koefisien regresi per pandang sebagai koreksi statistik dua sisi atau multi-sisi bila pencocokan identitas tidak tersedia, pelaporan visibilitas tiap pandang (rasio anotasi pandang tunggal terhadap hitungan manual) sebagai ukuran cakupan, serta peringatan bahwa model regresi hanya berlaku untuk konfigurasi kamera yang sama. Hasil makalah juga memperlihatkan bahwa tanpa tumpang tindih antarpandang yang cukup, identitas buah tidak dapat disatukan.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `li2023blueberry`.

Ringkasan yang aman dikutip: Li dkk. (2023), dalam makalah pertemuan ASABE, memperkirakan jumlah blueberry per tanaman dari citra tiga pandang (atas, kiri, kanan) yang diambil oleh robot lapangan, dengan detektor YOLOv8x dan regresi linear berganda atas hitungan deteksi tiap pandang. Pada 12 tanaman dengan hitungan panen manual, regresi multi-pandang menghasilkan MAPE 24,63% dan $R^2$ sebesar 0,77, dibandingkan MAPE 29,86% dan $R^2$ sebesar 0,75 untuk pandang atas saja. Penulis menyatakan bahwa tumpang tindih antarkamera tidak memadai untuk menyatukan buah yang sama secara spasial.

Catatan verifikasi data: Angka abstrak (MAPE 24,6%, $R^2$ 0,77, kenaikan 5,2% sampai 15,7%, 12 tanaman) cocok dengan Subbab 3.3 dan Kesimpulan. Koefisien regresi dan $R^2$ 0,772 tertulis di Subbab 3.3. Angka detektor ada pada Tabel 2 dan Subbab 3.2, tetapi tabel diekstraksi per sel sehingga pengelompokan kolom disimpulkan dari urutan nilai dan kecepatan YOLOv5x 1280 tidak terbaca. Nilai MAPE dan $R^2$ pandang kanan, serta $R^2$ pandang kiri, hanya ada pada Gambar 9 dan tidak terbaca dari teks. Persentase pada citra Gambar 8 (85,67%; 15,58%; 6,29%) tidak sama persis dengan hitungan pada keterangan gambar, dan basis penghitungannya tidak dijelaskan. Penamaan kamera (sembilan kamera, tetapi 3 + 3 + 1 pada uraian) dan jumlah genotipe tidak konsisten atau tidak dilaporkan. Hitungan panen per tanaman, jumlah buah rata-rata, dan hasil validasi silang tidak dilaporkan.
