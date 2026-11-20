# Fruit Detection and Recognition Based on Deep Learning for Automatic Harvesting: An Overview and Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xiao2023fruit` |
| Judul asli | Fruit Detection and Recognition Based on Deep Learning for Automatic Harvesting: An Overview and Review |
| Penulis | Xiao, Feng; Wang, Haibin; Xu, Yueqin; Zhang, Ruiqing |
| Tahun | 2023 |
| Venue | Agronomy |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [xiao2023fruit.pdf](../pdf/xiao2023fruit.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy13061625

## Gambaran Umum

Tinjauan ini mengkaji deteksi dan pengenalan buah berbasis pembelajaran mendalam untuk panen otomatis. Buah tumbuh di lingkungan kompleks dengan banyak ketidakpastian, sehingga sistem penglihatan buah diperlukan untuk pertanian cerdas dan pemanenan otomatis. Sistem tersebut umumnya menjalani lima tahap: akuisisi citra, praproses, ekstraksi fitur, segmentasi, dan pengenalan. Penulis meninjau literatur dari 2018 sampai sekarang dan berfokus pada tantangan yang menurunkan kinerja deteksi, yakni kelangkaan dataset buah berkualitas tinggi, deteksi sasaran kecil, deteksi pada kondisi tertutup dan rapat, deteksi pada banyak skala dan spesies, serta model deteksi ringan.

Penulis memakai Google Scholar sebagai sumber pencarian karena cakupannya lebih luas daripada Web of Science dan Scopus. Kata kunci awal meliputi deteksi buah, pengenalan buah, pembelajaran mendalam, penglihatan komputer, dan pemanenan buah; makalah sebelum 2018 dikeluarkan, sehingga terkumpul 53 artikel penelitian. Sensor pencitraan yang dibahas mencakup kamera hitam putih, RGB, spektral, termal, dan RGB-D, masing-masing dengan kelebihan dan keterbatasan tersendiri. Metode dikelompokkan menjadi dua golongan: metode satu tahap berbasis regresi (YOLO dan SSD) serta metode dua tahap berbasis calon wilayah (AlexNet, VGGNet, ResNet, Faster R-CNN, FCN, SegNet, dan Mask R-CNN).

Mekanisme deteksi pada metode satu tahap memperlakukan deteksi sebagai regresi kelas dan koordinat kotak pada setiap sel citra, sedangkan metode dua tahap membangkitkan calon wilayah melalui region proposal network lalu melakukan klasifikasi dan regresi kotak setelah roI pooling. Tinjauan melaporkan rentang akurasi per keluarga model, yaitu YOLO 84–98%, SSD 75–92%, AlexNet 86–96%, VGGNet 92–99%, ResNet 90–95%, Faster R-CNN 90–99%, FCN 89–98%, SegNet 83–95%, dan Mask R-CNN 80–94%. Angka-angka ini merupakan ringkasan dari kajian primer yang dirujuk, bukan hasil pengukuran tinjauan sendiri. Contoh hasil kajian primer yang dikutip mencakup akurasi 91,91% untuk zaitun (12,64 ms pada CPU dan 4,10 ms pada GPU), 100% untuk lemon asam, 90,70% menjadi 95,75% setelah augmentasi untuk stroberi dengan E-AlexNet, 99,01%/97,25%/98,59% untuk jenis, kematangan, dan keputusan panen kurma dengan waktu 20,6/20,7/35,9 ms, mAP 98,46% dengan waktu 84 ms untuk tomat muda, serta presisi 95,78% dan recall 95,41% untuk stroberi dengan Mask R-CNN. Faster R-CNN menjadi topik paling banyak diteliti (21%), diikuti YOLO (17%); ResNet sebagai backbone paling populer (11%). Apel mendominasi kasus (32,14%), diikuti tomat (8,93%) dan sitrus (7,14%).

Penulis mengemukakan lima batasan utama. Dataset buah berkualitas tinggi masih langka; Fruits-360 misalnya memuat 131 kelas dan 90.380 citra, tetapi latar citranya tunggal, keragamannya kurang, dan katanya tidak seimbang. Sasaran kecil didefinisikan sebagai buah di bawah 32 × 32 piksel dan sulit dideteksi karena fitur terbatas, hilang saat konvolusi, sensitif terhadap pergeseran kotak, serta mengalami ketimpangan sampel. Situasi tertutup dan rapat menurunkan recall karena buah saling menyerupai dan NMS membuang deteksi dengan skor lebih rendah; penambahan mekanisme atensi membantu, tetapi menaikkan kompleksitas dan waktu konvergensi. Deteksi lintas skala dan spesies serta penerapan model ringan pada perangkat seluler juga menjadi tantangan; pemampatan model, kuantisasi, dan distilasi pengetahuan ditawarkan sebagai arah penanganan. Secara umum, metode dua tahap lebih akurat tetapi lebih lambat, sedangkan metode satu tahap lebih cepat tetapi kurang tepat pada sasaran kecil.
