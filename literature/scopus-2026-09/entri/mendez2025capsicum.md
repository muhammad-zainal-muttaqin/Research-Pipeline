# Capsicum Counting Algorithm Using Infrared Imaging and YOLO11

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mendez2025capsicum` |
| Judul asli | Capsicum Counting Algorithm Using Infrared Imaging and YOLO11 |
| Penulis | Mendez, Enrico; Escobedo Cabello, Jes\'us Arturo; G\'omez-Espinosa, Alfonso; Cantoral-Ceballos, Jose Antonio; Ochoa, Oscar |
| Tahun | 2025 |
| Venue | Agriculture Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | sweet pepper |

## Tautan Akses
- PDF: [mendez2025capsicum.pdf](../pdf/mendez2025capsicum.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture15242574

## Gambaran Umum

Makalah ini menyajikan pipeline pencacahan *capsicum* (paprika manis) di rumah kaca yang memakai citra inframerah (*infrared*, IR) dan detektor YOLO11 yang digabung dengan pelacak multi-objek BoT-SORT. Penulis berargumen bahwa penetrasi cahaya pada panjang gelombang IR membuat buah hijau lebih mudah dibedakan dari daun hijau dibandingkan citra RGB, terutama pada cahaya rendah, latar yang mirip warna buah, dan oklusi oleh dedaunan. Jumlah buah dihitung sebagai jumlah lintasan (*track*) yang masuk ke suatu wilayah hitung pada bingkai, bukan jumlah instans per bingkai.

Data berasal dari kamera OAK-D Pro pada robot bergerak Jackal di rumah kaca CAETEC (Tecnologico de Monterrey, Querétaro, Meksiko). Dataset IR terdiri atas 1.000 citra dengan 11.916 *capsicum* beranotasi; dataset RGB pembanding berisi 17.448 instans beranotasi.

Hasil utama: pada set uji IR, YOLO11m memperoleh F1 0,82; pada satu segmen baris rumah kaca dengan 70 buah, pelacak mencapai MOTA 0,85 dan menghitung 67 dari 70 buah. Model RGB pada segmen yang sama menghitung 25 dari 70 buah dengan MOTA 0,34.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi dan pencacahan buah di rumah kaca dipakai untuk manajemen sumber daya dan estimasi hasil. Pada *capsicum*, penulis menyebut tiga tantangan: cahaya rendah akibat bayangan, kebingungan latar karena buah dan daun berwarna serupa, dan oklusi oleh dedaunan. Penelitian sebelumnya memakai Mask R-CNN (yang menurut penulis lambat untuk aplikasi waktu-nyata), YOLOv5 dengan DeepSORT (F1 0,77), dan YOLO dengan algoritma lain (akurasi rata-rata 0,92). Modalitas lain seperti multispektral, hiperspektral, dan termal pernah dicoba, tetapi penulis menyatakan bahwa pencitraan IR belum pernah dipakai untuk mendeteksi atau menghitung *capsicum*.

Pertanyaan penelitian yang dinyatakan: apakah citra IR dapat dipakai untuk mendeteksi dan menghitung *capsicum*, dan apa keuntungannya.

## Ide Utama

Kamera stereo OAK-D Pro memiliki dua sensor monokrom tanpa filter IR, sehingga selain citra RGB juga menghasilkan citra IR tanpa perangkat keras tambahan. Citra IR (disimpan dan diproses sebagai citra tiga kanal) dipakai melatih YOLO11, dan BoT-SORT menjaga identitas buah sepanjang aliran video. Buah yang tertutup sebagian dan tidak terdeteksi pada beberapa bingkai tetap dihubungkan ke lintasan yang sama saat terlihat kembali, sehingga dihitung sekali.

Mekanisme identitas adalah pelacakan dalam satu urutan video dengan wilayah hitung berbentuk persegi panjang, bukan pencocokan antarsisi atau antarsudut pandang.

## Cara Kerja Langkah demi Langkah

```
 Video IR/RGB -> YOLO11 -> kotak -> BoT-SORT (Kalman, ReID, 2 tahap)
                                        -> lintasan masuk wilayah hitung
                                        -> jumlah lintasan = jumlah buah
```

### 1. Akuisisi data

Kamera OAK-D Pro (sensor warna IMX378 12 MP dan dua sensor monokrom OV9282 1 MP) dipasang pada penstabil Scorp Mini 2 di atas robot Jackal. Sepuluh baris rumah kaca direkam dengan robot di tengah baris, kamera menghadap satu sisi tanaman, kecepatan konstan 0,2 m/s dan dikendalikan manual. Rekaman IR beresolusi 1280 × 720 dan RGB 1920 × 1080 pada 30 bingkai per detik. Kultivar tidak dilaporkan.

### 2. Dataset dan pelatihan

Citra diambil dari video pada 5 citra per detik dan dianotasi di Roboflow. Untuk anotasi IR (skala abu-abu), kontras tiap citra disesuaikan sementara dengan transformasi intensitas linear $I_{adj} = \text{clip}(\alpha I + \beta, 0, 255)$; citra asli tetap dipakai untuk pelatihan. Dataset IR berisi 1.000 citra 1280 × 720 dengan 11.916 instans. Dataset RGB berasal dari makalah penulis sebelumnya ditambah 1.000 citra beranotasi 1920 × 1080, total 17.448 instans. Pembagian data 80% latih, 10% validasi, 10% uji. Augmentasi (Ultralytics): pergeseran HSV (hue 0,015, saturasi 0,70, kecerahan 0,40), translasi 0,10, skala 0,50, pembalikan horizontal 0,50, *mosaic* 1,0. Pelatihan 500 *epoch* dengan bobot praterlatih, penghentian dini 100, ukuran *batch* 64, `imgsz` 800, *optimizer* Adam, pada GPU RTX A6000 48 GB. Varian n, s, dan m dilatih untuk IR dan RGB.

### 3. Pelacakan BoT-SORT

BoT-SORT memakai filter Kalman dengan vektor keadaan delapan dimensi (pusat, lebar, tinggi, dan kecepatannya), estimasi gerak kamera, pencocokan Hungaria, dan pengodean tampilan ResNeSt50 yang digabung dengan jarak IoU. Asosiasi berlangsung dua tahap: tahap pertama untuk deteksi berskor tinggi (IoU dan ReID), tahap kedua untuk deteksi sisa berdasarkan IoU. Parameter: `track_high_thresh` 0,5, `track_low_thresh` 0,3, `new_track_thresh` 0,29, `track_buffer` 35, `match_thresh` 0,8.

### 4. Wilayah hitung

Satu buah dihitung ketika suatu lintasan muncul atau melewati wilayah hitung, yaitu persegi panjang setinggi bingkai penuh dan membentang dari 0,33 sampai 0,75 lebar bingkai. Wilayah dipilih setelah beberapa lokasi dicoba, agar buah yang terhalang sementara tetap dapat terhitung.

## Eksperimen dan Hasil

Metrik: akurasi, presisi, *recall*, F1, dan MOTA ($1 - (FN + FP + IDS)/GT$). Acuan GT pencacahan diperoleh dengan analisis video secara manual dan menghitung semua *capsicum* yang terlihat.

Detektor pada set uji (Tabel 5):

| Model | Recall (terbaik) | Presisi (terbaik) | F1 (terbaik) | Data |
|---|---|---|---|---|
| YOLO11n | 0,88 | 1 | 0,81 | IR |
| YOLO11s | 0,96 | 1 | 0,81 | IR |
| YOLO11m | 0,92 | 1 | 0,82 | IR |
| YOLO11n | 0,92 | 1 | 0,82 | RGB |
| YOLO11s | 0,95 | 1 | 0,81 | RGB |
| YOLO11m | 0,93 | 1 | 0,82 | RGB |

Pelacakan dan pencacahan pada segmen satu baris rumah kaca dengan jumlah buah diketahui (Tabel 6):

| Sensor | GT | Terhitung | FP | FN | IDS | MOTA |
|---|---|---|---|---|---|---|
| IR | 70 | 67 | 5 | 4 | 1 | 0,85 |
| RGB | 70 | 25 | 3 | 43 | 0 | 0,34 |

Penulis menyatakan bahwa RGB menghasilkan FN sepuluh kali lebih banyak daripada IR, dan sebagian besar galat berasal dari detektor, bukan pelacak. Terdapat satu pertukaran ID pada aliran IR, yaitu buah yang tertutup beberapa bingkai lalu dikaitkan dengan lintasan baru. Pada kurva validasi YOLO11m, F1 0,82 dicapai pada ambang keyakinan 0,483.

## Kelebihan dan Keterbatasan

Kelebihan: pendekatan IR memanfaatkan sensor yang sudah ada pada kamera stereo tanpa perangkat keras tambahan; perbandingan IR dan RGB dilakukan pada segmen video yang sama; dataset IR dinyatakan tersedia untuk umum; parameter pelatihan dan pelacak dilaporkan rinci.

Keterbatasan yang dinyatakan penulis: buah yang tertutup sebagian dan buah yang hanya tampak pada beberapa bingkai menyebabkan deteksi terlewat (FN) dan tidak sempat masuk wilayah hitung; algoritma hanya dapat menghitung buah yang terlihat pada suatu saat oleh kamera dan dirancang untuk rumah kaca; penulis mengusulkan informasi kedalaman dari kamera stereo, modalitas spektral lain, ekstensi ke buah lain, dan arsitektur YOLO untuk satu kanal sebagai pekerjaan lanjutan.

Menurut pembacaan ringkasan ini, evaluasi pencacahan hanya memakai satu segmen baris dengan 70 buah, sehingga kesimpulan tentang pencacahan bertumpu pada sampel yang sangat kecil dan tanpa ulangan. Acuan hitungan berasal dari hitungan manual pada video, bukan hasil panen. Hasil tidak dipisahkan per kelas kematangan. Selisih F1 IR dan RGB pada detektor sangat kecil (0,82 dan 0,82 untuk varian m), sehingga keunggulan IR tampak terutama pada pelacakan satu segmen. Presisi terbaik bernilai 1 untuk semua model pada Tabel 5, yang tidak lazim bila dikaitkan dengan F1 sekitar 0,81 sampai 0,82. Wilayah hitung dipilih setelah beberapa lokasi dicoba pada data yang kemungkinan sama dengan data evaluasi, tetapi makalah tidak merinci hal itu.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat pada banyak bingkai video dengan mekanisme pelacakan (BoT-SORT), dan hitungan dibentuk dari lintasan yang masuk wilayah hitung tertentu pada bingkai. Hitungan tidak dilaporkan per kelas, dan acuannya adalah hitungan manual buah yang terlihat pada video segmen uji, bukan panen.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan wilayah hitung sebagai aturan penghitungan lintasan, serta temuan bahwa kegagalan hitungan didominasi galat deteksi, bukan galat identitas pelacak (satu pertukaran ID dari 70 buah pada IR). Makalah tidak membahas penyatuan identitas antarsisi pohon dan tidak mengevaluasi hitungan per kelas.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `mendez2025capsicum`.

Mendez dkk. mengusulkan pencacahan *capsicum* di rumah kaca dengan citra inframerah dari kamera OAK-D Pro, detektor YOLO11, dan pelacak BoT-SORT dengan wilayah hitung. Pada set uji IR (1.000 citra, 11.916 instans), YOLO11m memperoleh F1 0,82, dan pada satu segmen baris dengan 70 buah pelacak menghitung 67 buah dengan MOTA 0,85, dibandingkan 25 buah dan MOTA 0,34 untuk model RGB.

Catatan verifikasi data: F1 0,82, 1.000 citra, dan 11.916 instans berasal dari abstrak, Tabel 5, dan seksi 4.2; angka pencacahan dan MOTA dari Tabel 6 (nilai MOTA 0,85 dan 0,34 konsisten dengan rumus Persamaan 10 menurut hitungan ringkasan ini). Seksi 4.4 menyebut YOLO11n sebagai model terbaik dengan presisi 1 pada keyakinan 0,96 dan *recall* 0,92, sedangkan seksi 4.3 dan kesimpulan menyatakan YOLO11m dipilih karena F1 tertinggi; ketidakselarasan ini tidak terselesaikan dari teks. Ukuran set uji tidak dinyatakan secara eksplisit (hanya rasio 80/10/10). Teks ekstraksi memuat kurva pada Gambar 8 dan 9 tanpa angka yang dapat diverifikasi. Jumlah baris tanaman atau pohon di rumah kaca dan kultivar tidak dilaporkan.
