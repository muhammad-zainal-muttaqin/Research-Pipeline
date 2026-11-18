# Advances in Object Detection and Localization Techniques for Fruit Harvesting Robots

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `shi2025advances` |
| Judul asli | Advances in Object Detection and Localization Techniques for Fruit Harvesting Robots |
| Penulis | Shi, Xiaojie; Wang, Shaowei; Zhang, Bo; Ding, Xinbing; Qi, Peng; Qu, Huixing; Li, Ning; Wu, Jie; Yang, Huawei |
| Tahun | 2025 |
| Venue | Agronomy |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [shi2025advances.pdf](../pdf/shi2025advances.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy15010145

## Gambaran Umum

Tinjauan ini membahas akurasi deteksi objek dan penentuan posisi tiga dimensi buah pada robot pemanen, karena kedua hal itu menentukan efisiensi, mutu, dan kecepatan pemanenan. Algoritma konvensional berbasis pengolahan citra digital dan pembelajaran mesin dianggap kurang memadai akibat akurasi pengenalan yang rendah, kecepatan yang lambat, dan penentuan posisi yang tidak tepat. Penulis menyusun tinjauan sistematis terhadap sekitar 120 publikasi dalam dekade terakhir yang membahas algoritma deteksi objek dan penentuan posisi 3D untuk robot pemanen buah dan sayur.

Sumber dikumpulkan dari Google Scholar, ScienceDirect, Web of Science, dan basis data lain dengan kombinasi kata kunci pengenalan buah, deteksi buah, penentuan posisi buah, robot pemanen, dan visi komputer. Publikasi disaring lalu dikelompokkan menjadi dua topik, yaitu deteksi objek dan penentuan posisi objek. Berbagai tanaman menjadi contoh, antara lain apel, tomat, kelapa, mangga, sawit, nanas, buah naga, delima, anggur, jeruk, markisa, paprika, pir, stroberi, dan melon. Data citra diperoleh dengan kamera RGB (warna, tekstur, bentuk), kamera RGB-D (warna dan kedalaman, misalnya Intel RealSense), serta LiDAR untuk jarak di luar jangkauan kamera kedalaman yang umumnya hanya sampai 3,5 m. Pra-pemrosesan mencakup augmentasi citra, pelabelan, dan teknik peningkatan citra berbasis GAN.

Untuk deteksi, tinjauan membedakan metode dua tahap (R-CNN, Fast R-CNN, Faster R-CNN, Mask R-CNN) yang lebih akurat tetapi lambat, dan metode satu tahap (SSD, seri YOLO, RT-DETR) yang lebih cepat serta memenuhi kebutuhan waktu nyata. Mekanisme dua tahap menghasilkan usulan wilayah lalu mengklasifikasikannya dengan CNN, termasuk perbaikan berupa penggabungan peta fitur dangkal, modul atensi, dan fusi pengklasifikasi untuk buah kecil atau tertutup daun. Mekanisme satu tahap membagi citra menjadi grid S×S dan memprediksi langsung kelas beserta koordinat kotak. Angka yang dikutip dari kajian sumber meliputi deteksi apel dengan YOLOv3 sebesar 92,2% pada 19 ms per citra, apel dengan Mask R-CNN 97,31%, kelapa dengan Faster R-CNN 89,4%, sawit dengan YOLOv4 95% pada 47,6 ms dan 92,6% pada 12,11 ms, markisa dengan Faster R-CNN berpresisi 93,10%, recall 88,50%, dan F1 94,60%, tomat ceri dengan SSD-Inception V2 mAP 98,85%, serta mangga dengan SSD 92,43%. Metrik yang dipakai adalah detection rate, mAP, presisi, recall, F1, dan kecepatan inferensi (ms per citra); seluruh angka merupakan hasil yang dilaporkan kajian yang dikutip, bukan dihitung ulang oleh tinjauan ini.

Untuk penentuan posisi, tinjauan membandingkan visi stereo (triangulasi dua kamera), kamera RGB-D (cahaya terstruktur dan time-of-flight), serta sensor lain seperti LiDAR dan pemindai laser. Mekanismenya memanfaatkan informasi kedalaman atau awan titik pada wilayah buah yang terdeteksi untuk mengubah koordinat dua dimensi menjadi posisi tiga dimensi, dengan teknik seperti pencocokan stereo, konversi piksel-dunia, pemrosesan awan titik berbasis frustum, dan pencocokan bola RANSAC. Angka yang dikutip mencakup kesalahan absolut penentuan posisi nanas sekitar 25 mm (kesalahan relatif 1,17% pada jarak 1,7–2,7 m), kesalahan rata-rata penentuan posisi jeruk kurang dari 2,75 mm, penurunan kesalahan rata-rata 43% untuk apel tertutup dengan YOLACT++, kesalahan keseluruhan 5,7 mm untuk apel RGB-D, dan kesalahan kedalaman kurang dari 4 mm pada sistem penentuan posisi aktif rentang 0,6–1,2 m. Penulis menyatakan tiga batasan utama: dataset buah berkualitas tinggi berskala besar masih langka, kestabilan dan ketahanan algoritma pada adegan kompleks perlu ditingkatkan, serta kompleksitas dan ketidakpastian lingkungan pertanian masih menyisakan kesalahan penentuan posisi yang besar. Arah pengembangan yang diusulkan adalah pembelajaran tersupervisi lemah, model ringan untuk perangkat tertanam, dan fusi banyak sensor.

