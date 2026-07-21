# 120 - Deep Learning for Real-Time Fruit Detection and Orchard Fruit Load Estimation: Benchmarking of 'MangoYOLO'

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `koirala2019deepfruit` |
| Judul asli | Deep Learning for Real-Time Fruit Detection and Orchard Fruit Load Estimation: Benchmarking of 'MangoYOLO' |
| Penulis | Koirala, Anand; Walsh, Kerry B.; Wang, Zhenglin; McCarthy, Cheryl |
| Tahun | 2019 |
| Venue / Jurnal | Precision Agriculture |
| Tema klaster | Pertanian |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Deep%20Learning%20for%20Real-Time%20Fruit%20Detection%20and%20Orchard%20Fruit%20Load%20Estimation%3A%20Benchmarking%20of%20%27MangoYOLO%27
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Deep%20Learning%20for%20Real-Time%20Fruit%20Detection%20and%20Orchard%20Fruit%20Load%20Estimation%3A%20Benchmarking%20of%20%27MangoYOLO%27&sort=relevance

## Gambaran Umum
Makalah ini memperkenalkan MangoYOLO, model deteksi objek satu tahap (*single-stage detector*) berbasis pembelajaran mendalam (*deep learning*) untuk mendeteksi buah mangga secara seketika (*real-time*) di perkebunan. Masalah utamanya adalah ketidakseimbangan akurasi deteksi dan kecepatan komputasi pada perangkat keras komputasi tepi (*edge computing*) kendaraan pertanian. Model ini melakukan estimasi beban panen (*fruit load estimation*) secara cepat guna mendukung logistik perkebunan komersial sebelum pemanenan.

Hasil utamanya adalah arsitektur kustom 33 layer yang memadukan deteksi multi-skala YOLOv3 dan efisiensi YOLOv2 (*tiny*). Pada dataset uji malam hari dengan pencahayaan LED buatan, varian MangoYOLO(*pretrained*) mencapai skor F1 sebesar 0,968 dan Average Precision (AP) sebesar 0,983. Model memproses citra resolusi tinggi 2048×2048 piksel melalui ubinan (*tiling*) berkecepatan 14 FPS menggunakan GPU NVIDIA GTX 1070 Ti, sehingga layak untuk kendaraan perkebunan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi beban buah secara akurat krusial dalam perencanaan panen dan pengelolaan rantai pasok hortikultura komersial. Metode konvensional mengandalkan penghitungan manual terhadap sampel pohon secara acak oleh pekerja lapangan. Pendekatan ini memiliki kelemahan bawaan berupa biaya operasional tinggi, waktu pelaksanaan yang lama, serta kerentanan terhadap kesalahan estimasi akibat bias subjektif manusia dan ukuran sampel yang terbatas.

Otomatisasi berbasis pengolahan citra konvensional (segmentasi warna dan bentuk geometris) sering kali gagal menghadapi kondisi luar ruangan yang dinamis. Variasi pencahayaan alami siang hari, bayangan tajam dedaunan, dan pantulan cahaya (*lens flare*) menurunkan keandalan deteksi secara drastis. Ditambah lagi, kerapatan kanopi pohon yang tinggi memicu oklusi daun (buah terhalang daun atau cabang) dan oklusi buah (buah berhimpitan), sehingga algoritma konvensional gagal melokalisasi buah secara akurat.

Meskipun model deteksi berbasis pembelajaran mendalam dua tahap (*two-stage detector*) seperti Faster R-CNN mampu meningkatkan akurasi, arsitekturnya menuntut sumber daya komputasi yang besar. Kebutuhan memori GPU yang tinggi dan waktu inferensi yang lambat (ratusan milidetik per citra) menghambat penerapan *real-time* pada kendaraan perkebunan. Industri membutuhkan arsitektur satu tahap (*single-stage detector*) yang efisien namun tetap sensitif terhadap objek kecil dan oklusi parsial.

## Ide Utama
Gagasan inti dari MangoYOLO adalah memangkas kedalaman jaringan YOLOv3 untuk menekan biaya komputasi tanpa mengorbankan performa deteksi objek multiskala melalui integrasi lateral. YOLOv3 standar memiliki 106 layer dengan tulang punggung (*backbone*) Darknet-53 yang terlalu berat untuk komputasi tepi lapangan. MangoYOLO membatasi jumlah lapisan hanya pada 33 layer, menggunakan 26 lapisan konvolusional (*convolutional layers*) sebagai pengekstraksi fitur utama yang terinspirasi dari arsitektur YOLOv2 (*tiny*).

Untuk mengompensasi hilangnya kapasitas representasi spasial akibat penyusutan kedalaman jaringan, MangoYOLO mengadopsi mekanisme deteksi multi-skala dari YOLOv3. Hal ini dicapai dengan menyertakan 2 *route layer* dan 2 *up-sample layer* untuk menggabungkan peta fitur (*feature maps*) dari lapisan dangkal (yang kaya akan informasi spasial objek kecil) dengan peta fitur lapisan dalam (yang kaya akan fitur semantik objek besar). Deteksi diprediksi secara paralel pada 3 lapisan deteksi (*detection layers*) dengan resolusi spasial berbeda, sehingga model tetap sensitif terhadap buah mangga berukuran kecil yang berada di kejauhan maupun buah berukuran besar yang dekat dengan kamera.

## Cara Kerja Langkah demi Langkah
Operasional deteksi buah dan estimasi beban panen menggunakan MangoYOLO mengikuti alur pemrosesan data terstruktur dari akuisisi citra hingga penentuan hasil akhir:

1. **Akuisisi Citra Malam Hari**: Citra diambil pada malam hari menggunakan kamera RGB 5 megapiksel yang dipasang pada kendaraan darat. Sistem dilengkapi dengan lampu sorot LED (*LED floodlights*) untuk menstandardisasi kondisi pencahayaan. Langkah ini meminimalkan variasi bayangan siang hari dan menghasilkan kontras warna kuning-hijau buah mangga yang konsisten terhadap dedaunan gelap di latar belakang.
2. **Pemotongan Citra (Tiling)**: Citra beresolusi penuh 2048×2048 piksel dipotong menjadi beberapa ubin (*tiles*) berukuran 512×512 piksel sebelum dimasukkan ke dalam jaringan. Metode ini mencegah hilangnya fitur spasial buah berukuran kecil yang dapat terjadi jika citra langsung direskala secara drastis ke ukuran input jaringan yang lebih kecil.
3. **Ekstraksi Fitur Konvolusional**: Setiap ubin citra 512×512 piksel diproses melalui blok konvolusi. Blok ini tersusun atas lapisan konvolusional dengan ukuran filter konvolusi 3×3 dan 1×1, normalisasi tumpukan (*batch normalization*), serta fungsi aktivasi *Leaky Rectified Linear Unit* (Leaky ReLU).
4. **Penskalaan Naik dan Perutean Lateral**: Peta fitur dari lapisan yang lebih dalam diperbesar resolusinya spasialnya menggunakan *up-sample layer* dengan faktor perbesaran 2. Fitur yang telah diperbesar tersebut kemudian digabungkan secara lateral dengan peta fitur resolusi spasial tinggi dari lapisan awal menggunakan *route layer* untuk mempertahankan detail tepi buah.
5. **Prediksi Kotak Pembatas Multi-Skala**: MangoYOLO melakukan prediksi koordinat kotak pembatas (*bounding box*), skor keyakinan (*confidence score*), dan klasifikasi pada 3 skala grid yang berbeda. Setiap sel grid menggunakan 3 kotak jangkar (*anchor boxes*) yang telah dikelompokkan sebelumnya menggunakan metode klasterisasi *k-means* agar sesuai dengan distribusi dimensi buah mangga pada dataset latih.
6. **Non-Maximum Suppression (NMS)**: Redundansi kotak pembatas yang mendeteksi buah yang sama dieliminasi menggunakan algoritma NMS berdasarkan ambang batas indeks tumpang-tindih (*Intersection over Union* / IoU). Kotak pembatas dengan skor keyakinan tertinggi dipertahaman sebagai hasil deteksi final.
7. **Estimasi Beban Buah Kebun**: Jumlah buah terdeteksi dikalikan dengan faktor koreksi (*correction factor*) empiris. Faktor ini diperoleh melalui regresi linear yang membandingkan jumlah deteksi visual dengan jumlah panen manual nyata. Faktor ini mengoreksi persentase buah yang tersembunyi sepenuhnya di balik kanopi daun tebal yang tidak terjangkau sensor kamera RGB.

Diagram berikut mengilustrasikan aliran data multi-skala pada arsitektur 33 layer MangoYOLO:

```
                  [ Input Image Tile: 512 x 512 x 3 ]
                                  │
                       [ Blok Konvolusi Awal ] ──────┐
                                  │                  │
                                  ▼                  │
                       [ Blok Konvolusi Tengah ] ────┼──────────────┐
                                  │                  │              │
                                  ▼                  │              │
                        [ Blok Konvolusi Dalam ]     │              │
                                  │                  │              │
                      ┌───────────┴───────────┐      │              │
                      ▼                       ▼      ▼              │
            [ Detection Layer 1 ]        [ Route Layer 1 ]          │
                (Skala Kasar)                 │                     │
                                         [ Upsample 1 ]             │
                                              │                     │
                                         [ Route Layer 2 ] ◄────────┘
                                              │
                                     [ Blok Konvolusi D ]
                                              │
                                  ┌───────────┴───────────┐
                                  ▼                       ▼
                        [ Detection Layer 2 ]        [ Route Layer 3 ]
                           (Skala Sedang)                 │
                                                     [ Upsample 2 ]
                                                          │
                                                     [ Route Layer 4 ] ◄────┘
                                                          │
                                                [ Detection Layer 3 ]
                                                    (Skala Halus)
```

## Eksperimen dan Hasil
Evaluasi model MangoYOLO dilakukan menggunakan dataset citra pohon mangga yang dikumpulkan dari lima perkebunan komersial di Queensland, Australia, yang mencakup kultivar Kensington Pride, Calypso, dan Keitt. Dataset ini terdiri dari 1.515 citra pohon utuh beresolusi tinggi (2048×2048 piksel) yang diambil pada malam hari. Citra dibagi menjadi ubin berukuran 512×512 piksel untuk kebutuhan pelatihan dan pengujian.

Model MangoYOLO dievaluasi dalam tiga varian konfigurasi latih: MangoYOLO(s) yang dilatih dari awal (*scratch*), MangoYOLO(pt) yang menggunakan bobot pra-latih (*pretrained*) dari dataset COCO, dan MangoYOLO(bu) yang dilatih pada dataset siang hari milik Bargoti dan Underwood (2017) untuk pembandingan. Hasil eksperimen kuantitatif menunjukkan:

*   **Akurasi Deteksi**: Varian MangoYOLO(pt) mencapai skor F1 tertinggi sebesar **0,968** dengan presisi 0,961, sensitivitas (*recall*) 0,974, dan presisi rata-rata (AP) sebesar **0,983** pada dataset uji independen malam hari.
*   **Perbandingan dengan Baseline**: Model ini mengungguli arsitektur Faster R-CNN (VGG16) yang mencapai skor F1 sebesar 0,945 pada dataset yang sama. Pada dataset siang hari Bargoti, MangoYOLO(bu) mencapai skor F1 sebesar 0,890, hampir menyamai performa Faster R-CNN (VGG16) asli milik Bargoti dan Underwood yang mencapai skor F1 sebesar 0,900. Ini membuktikan pengurangan kedalaman jaringan pada MangoYOLO tidak mendegradasi akurasi secara signifikan.
*   **Kecepatan dan Penggunaan Memori**: Pada GPU NVIDIA GeForce GTX 1070 Ti, MangoYOLO memproses satu ubin 512×512 piksel hanya dalam waktu **8 milidetik** (*ms*) dan mengonsumsi memori GPU sebesar **833 Megabita** (*MB*). Untuk citra penuh 2048×2048 piksel, total waktu pemrosesan adalah **70 ms** (~14 FPS) dengan konsumsi memori GPU sebesar **4.417 MB**. Sebagai perbandingan, Faster R-CNN memerlukan memori GPU di atas 8 Gigabita untuk citra beresolusi setara.
*   **Estimasi Hasil Panen**: Pengujian estimasi beban buah pada tingkat blok kebun menunjukkan selisih deviasi antara prediksi model dan hasil hitung nyata di rumah pengemasan (*packhouse*) berkisar antara **4,6% hingga 15,2%**, yang memadai untuk kebutuhan logistik industri.

## Kelebihan dan Keterbatasan
Kelebihan utama dari MangoYOLO terletak pada rancangan arsitekturnya yang berhasil menyeimbangkan aspek akurasi tinggi dan kecepatan komputasi seketika pada perangkat keras kelas menengah. Pengurangan parameter jaringan menjadi 33 layer menurunkan beban memori GPU secara drastis (hanya 833 MB per ubin), sehingga model ini layak diterapkan pada komputer papan tunggal (*single-board computer*) yang dipasang langsung pada traktor atau robot pertanian di lapangan. Selain itu, metodologi pengambilan citra malam hari menggunakan lampu sorot LED terbukti efektif memotong variabilitas pencahayaan alami dan bayangan matahari siang hari yang kerap menurunkan keandalan deteksi citra pertanian.

Namun, model ini memiliki beberapa keterbatasan. Dari sisi sensor, MangoYOLO beroperasi murni pada domain citra RGB dua dimensi (2D). Model ini tidak memiliki pemahaman kedalaman spasial (*depth information*) sehingga mengalami kesulitan dalam memisahkan buah-buah yang saling menempel rapat (*fruit-to-fruit occlusion*) dan tidak dapat menyediakan koordinat 3D yang presisi untuk kebutuhan lengan robot manipulator pemanen. Secara konseptual, akurasi estimasi beban buah akhir masih sangat bergantung pada faktor koreksi empiris kustom. Faktor koreksi ini bersifat sensitif terhadap kerapatan kanopi daun dan bentuk tajuk pohon, sehingga memerlukan kalibrasi ulang apabila diterapkan pada kebun dengan varietas mangga yang berbeda atau pola pemangkasan cabang yang baru. Selain itu, keharusan operasional malam hari menambah kompleksitas logistik perkebunan.

## Kaitan dengan Bab Lain
MangoYOLO merupakan pionir adaptasi detektor satu tahap untuk hortikultura pada klaster Pertanian, mewarisi prinsip efisiensi YOLOv2 (*tiny*) dan deteksi multi-skala YOLOv3 yang dibahas pada [003 - YOLOv3: An Incremental Improvement](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md). Pendekatan deteksi buah satu tahap ini dikembangkan lebih lanjut dalam [121 - 2019 - Apple Detection (Improved YOLOv3) - Pertanian](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md) dengan menyematkan DenseNet untuk mendeteksi apel multi-tahap tumbuh, serta pemangkasan model pada YOLOv4 untuk deteksi bunga apel dalam [122 - 2020 - Apple Flower Detection (Pruned YOLOv4) - Pertanian](./122%20-%202020%20-%20Apple%20Flower%20Detection%20%28Pruned%20YOLOv4%29%20-%20Pertanian.md).

Keterbatasan deteksi 2D RGB pada MangoYOLO dipecahkan oleh penelitian berbasis RGB-D (RGB + Depth) seperti Faster R-CNN dalam [123 - 2020 - Apple Detection RGB+Depth (Faster R-CNN) - Pertanian](./123%20-%202020%20-%20Apple%20Detection%20RGB%2BDepth%20%28Faster%20R-CNN%29%20-%20Pertanian.md) dan lokalisasi spasial 3D buah apel oleh Gene-Mola dkk. pada [124 - 2020 - Fruit Detection & 3D Location (Gene-Mola dkk.) - Pertanian](./124%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Location%20%28Gene-Mola%20dkk.%29%20-%20Pertanian.md). Sistem visualisasi 3D buah real-time untuk pemanenan dibahas pada [127 - 2020 - Fruit Detection & 3D Visualisation (Kang & Chen) - Pertanian](./127%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Visualisation%20%28Kang%20%26%20Chen%29%20-%20Pertanian.md), yang melandasi robotika panen otomatis seperti pemanen selada dalam [125 - 2020 - Iceberg Lettuce Harvesting Robot - Pertanian](./125%20-%202020%20-%20Iceberg%20Lettuce%20Harvesting%20Robot%20-%20Pertanian.md) dan robot pemanen buah serbaguna pada [126 - 2019 - Automated Fruit Harvesting Robot (Onishi dkk.) - Pertanian](./126%20-%202019%20-%20Automated%20Fruit%20Harvesting%20Robot%20%28Onishi%20dkk.%29%20-%20Pertanian.md).

## Poin untuk Sitasi
*   **Kunci BibTeX**: `koirala2019deepfruit`
*   **Ringkasan Sitasi**: Koirala dkk. (2019) merancang MangoYOLO, detektor objek satu tahap kustom 33 layer yang memadukan backbone ringan YOLOv2 (tiny) dengan tiga lapisan deteksi skala paralel dari YOLOv3. Diuji pada citra pohon mangga malam hari dengan pencahayaan LED buatan, model ini mencapai skor F1 sebesar 0,968 dan Average Precision (AP) sebesar 0,983, serta mampu memproses citra resolusi tinggi dengan kecepatan 14 FPS pada GPU NVIDIA GTX 1070 Ti untuk keperluan estimasi hasil panen kebun.
*   **Catatan Verifikasi**: Nilai F1-score 0,968 dan AP 0,983 diperoleh pada dataset citra malam hari dengan pemrosesan ubin (*tiling*) citra ukuran 512×512 piksel. Estimasi beban panen akhir memerlukan faktor koreksi empiris tambahan guna mengompensasi buah yang terhalang sepenuhnya di dalam struktur kanopi daun pohon mangga.
