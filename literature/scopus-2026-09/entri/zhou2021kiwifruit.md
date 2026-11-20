# Kiwifruit yield estimation using deep learning and binocular stereo vision on Android smartphones

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhou2021kiwifruit` |
| Judul asli | Kiwifruit yield estimation using deep learning and binocular stereo vision on Android smartphones |
| Penulis | Zhou, Zhongxian; Fu, Longsheng |
| Tahun | 2021 |
| Venue | American Society of Agricultural and Biological Engineers Annual International Meeting Asabe 2021 |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | kiwifruit |

## Tautan Akses
- PDF: [zhou2021kiwifruit.pdf](../pdf/zhou2021kiwifruit.pdf)
- DOI resmi: https://doi.org/10.13031/aim.202100289

## Gambaran Umum

Kajian ini membahas perkiraan hasil panen buah kiwi secara otomatis. Selama ini perkiraan hasil panen mengandalkan penghitungan dan pengukuran manual yang memakan waktu dan kurang akurat. Padahal jumlah dan ukuran buah menentukan kebutuhan tenaga kerja, tempat penyimpanan, dan distribusi pemasaran. Penulis mengusulkan aplikasi Android yang memadukan pembelajaran mendalam dan *binocular stereo vision* untuk mencacah buah kiwi pada video *real-time* sekaligus menghitung ukurannya. Latar belakangnya, sebagian besar studi pengukuran ukuran sebelumnya memakai dua lensa yang sama, sedangkan lensa ponsel umumnya berbeda, yaitu lensa standar dan lensa sudut lebar.

Data dikumpulkan di kebun kiwi Stasiun Eksperimen Kiwi Meixian, Universitas Northwest A&F, Shaanxi, Tiongkok, pada akhir Oktober 2020 saat musim panen. Varietas yang dipakai adalah 'Hayward'. Sensornya adalah ponsel Huawei P30 yang memiliki lensa standar dan lensa sudut lebar. Ponsel dipasang pada tripod sekitar 1 m di bawah tajuk kiwi dengan kamera menghadap ke atas. Sebanyak 800 pasang citra beresolusi 1.920 × 1.080 piksel diambil, masing-masing 400 pasang pada pagi dan sore hari dengan kondisi cahaya yang berbeda. Seluruh target kiwi pada 800 citra dari lensa standar dianotasi manual dengan kotak persegi panjang (*bounding box*) dan disimpan dalam berkas xml.

Model deteksi memakai *single shot multibox detector* (SSD) dengan MobileNetV2 sebagai jaringan ekstraksi fitur. Model dilatih dengan kerangka TensorFlow melalui *transfer learning* dari bobot COCO agar waktu pelatihan lebih singkat. Penghitungan memakai garis deteksi, yaitu buah dihitung ketika titik tengah kotak deteksi melewati garis tersebut. Untuk ukuran, kedua lensa dikalibrasi dengan metode Zhang menggunakan papan catur 9 × 7 kotak berukuran 33 mm dan 20 pasang citra. Setelah rektifikasi distorsi, peta disparitas dibuat dengan SGBM. Kedalaman dihitung dengan triangulasi, dan diameter dihitung sebagai norma Euclidean antara dua titik tepi buah dalam koordinat 3D. Hasilnya, tingkat kesalahan pencacahan rata-rata (CER) sebesar 15,2 persen dengan kecepatan 30 ms per citra. Kesalahan kedalaman rata-rata (DepER) sebesar 6,92 persen dan kesalahan diameter rata-rata (DiaER) sebesar 6,58 persen dibandingkan pengukuran manual. Penulis menyimpulkan bahwa aplikasi ini menjanjikan untuk perkiraan hasil panen kiwi.
