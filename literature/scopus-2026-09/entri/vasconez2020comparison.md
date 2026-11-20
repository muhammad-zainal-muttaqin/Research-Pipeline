# Comparison of convolutional neural networks in fruit detection and counting: A comprehensive evaluation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `vasconez2020comparison` |
| Judul asli | Comparison of convolutional neural networks in fruit detection and counting: A comprehensive evaluation |
| Penulis | Vasconez, J.P.; Delpiano, J.; Vougioukas, S.; Auat Cheein, F. |
| Tahun | 2020 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple, citrus, avocado |

## Tautan Akses
- PDF: [vasconez2020comparison.pdf](../pdf/vasconez2020comparison.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2020.105348

## Gambaran Umum

Kajian ini membahas kebutuhan untuk mengetahui jumlah buah sebelum panen. Perkiraan jumlah buah yang tepat mendukung logistik dan pengambilan keputusan di industri pertanian. Berbagai sensor dan teknik sensing telah diusulkan untuk pencacahan buah, tetapi hasilnya beragam. *Convolutional neural network* (CNN) menjadi pendekatan utama dalam pemrosesan citra, namun kajian yang menguji kegunaannya untuk pencacahan buah di kebun masih jarang. Penulis menyatakan bahwa proses belajar CNN peka terhadap data latih, sensor yang dipengaruhi kondisi lingkungan, dan arsitektur yang dipilih. Karena itu, penelitian ini membandingkan dua arsitektur, yaitu *Faster R-CNN* dengan Inception V2 dan *Single Shot Multibox Detector* (SSD) dengan MobileNet, untuk pencacahan buah berbasis video.

Penelitian ini menggunakan tiga jenis buah. Dua di antaranya berasal dari Valparaíso, Chile, yaitu alpukat Hass dan lemon. Yang ketiga adalah apel dari California, Amerika Serikat. Alpukat Hass menyumbang 66% produksi buah di Valparaíso. Pohon alpukat setinggi 5 sampai 9 meter, dan buahnya berada di dalam tajuk sehingga sulit terdeteksi dari udara. Intensitas cahaya saat akuisisi data berkisar 1890 sampai 43600 lux untuk alpukat, 3500 sampai 38000 lux untuk apel, dan 4800 sampai 52000 lux untuk lemon. Sensor yang digunakan adalah kamera RGB komersial dengan resolusi 360 × 640 piksel. Kamera dipegang tangan dan merekam pada 30 bingkai per detik. Resolusi tersebut dipilih agar sistem dapat diterapkan pada telepon seluler. Data dibagi menjadi himpunan latih, validasi, dan uji.

Kedua detektor dilatih dan dievaluasi dengan *precision-recall* dan *mean average precision* (mAP). Faster R-CNN dengan Inception V2 mencapai performa terbaik pada 70.000 iterasi, dengan mAP 77%. SSD dengan MobileNet mencapai performa terbaik pada 40.000 iterasi, dengan mAP 57%. Faster R-CNN membutuhkan sekitar 220 ms per bingkai, sedangkan SSD sekitar 60 ms. Hasil pada himpunan uji mirip dengan hasil pada himpunan validasi, sehingga penulis menilai kedua model memiliki kemampuan generalisasi yang dapat diterima. Untuk pencacahan, penulis memakai pelacakan multi-objek berbasis estimasi Gaussian guna mencegah *pencacahan ganda* akibat deteksi yang terlewat dan oklusi. Enam uji dilakukan dengan urutan 5, 15, 30, 60, dan 100 citra untuk tiap jenis buah. Kinerja pencacahan mencapai 93% secara keseluruhan dengan Faster R-CNN dan 90% dengan SSD. Pada alpukat, galat rata-rata SSD lebih besar daripada Faster R-CNN di semua kasus. Galat pencacahan meningkat seiring bertambahnya jumlah citra yang dievaluasi.

Penulis mencatat bahwa oklusi oleh daun dan cabang menyebabkan beberapa buah tidak terdeteksi pada ketiga jenis buah. Penulis juga menjelaskan bahwa perbedaan galat alpukat antara kedua model terkait dengan kemampuan ekstraktor fitur Inception V2 yang lebih baik dalam menangkap fitur buah alpukat dibandingkan MobileNet. Kebun yang diteliti hanya tiga, dengan satu kamera dan kondisi lapangan tertentu, sehingga hasil ini belum tentu berlaku untuk kebun dan sensor lain.
