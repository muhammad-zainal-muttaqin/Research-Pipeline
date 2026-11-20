# Deep learning-based multi-object tracking: a comprehensive survey from foundations to state-of-the-art

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `adzemovic2026deep` |
| Judul asli | Deep learning-based multi-object tracking: a comprehensive survey from foundations to state-of-the-art |
| Penulis | Ad\vzemovi\'c, Momir |
| Tahun | 2026 |
| Venue | Visual Computer |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [adzemovic2026deep.pdf](../pdf/adzemovic2026deep.pdf)
- DOI resmi: https://doi.org/10.1007/s00371-026-04607-7

## Gambaran Umum

Artikel ini adalah tinjauan pustaka tentang pelacakan banyak objek (*multi-object tracking*, MOT) berbasis pembelajaran mendalam. Tugas MOT mencakup deteksi objek pada setiap citra video dan pengasosiasiannya lintas waktu dengan pemberi identitas unik, sehingga menghasilkan lintasan tiap objek. Masalah utamanya adalah oklusi yang sering menyebabkan pertukaran identitas atau hilangnya lintasan, kemiripan penampilan antarobjek yang menyulitkan pembedaan, serta gerak dinamis yang tidak dapat diprediksi. Penulis menyusun tinjauan ini karena literatur sebelumnya banyak berhenti pada metode lama atau terbatas pada satu ranah. Meskipun berasal dari luar pertanian, mekanisme asosiasi yang dibahas dapat ditransfer ke permasalahan identitas lintas pandang.

Data yang dibandingkan berupa empat tolok ukur video dengan kotak pembatas dua dimensi dari kamera tunggal. MOT17 memuat 14 adegan, 14.235 citra, dan 292.733 kotak pembatas; MOT20 memuat 8 adegan, 13.410 citra, dan 1.652.040 kotak pembatas dengan kepadatan sekitar lima kali lipat MOT17; DanceTrack memuat 100 video, 105.855 citra, dan 990 lintasan dengan penampilan serupa serta gerak cepat tak linear; SportsMOT memuat 240 rangkaian dan lebih dari 150.000 citra olahraga. Metode dikelompokkan ke dalam dua paradigma. Paradigma *tracking-by-detection* memisahkan deteksi dan asosiasi menjadi dua langkah dan dibagi lagi menjadi deteksi bersama penyematan, berbasis heuristik, berbasis gerak, pembelajaran afinitas, serta metode luring berbasis graf. Paradigma ujung-ke-ujung (*end-to-end*) melakukan keduanya sekaligus melalui *tracking-by-query* berbasis DETR, seperti MOTR, MOTRv3, MeMOT, MeMOTR, dan MOTIP.

Mekanisme asosiasi berawal dari SORT yang memakai detektor Faster R-CNN, Kalman filter dengan model kecepatan tetap, serta algoritme Hungarian dengan biaya berupa negatif IoU; lintasan baru menjalani masa percobaan tiga citra dan dihapus setelah satu citra tanpa asosiasi. Deep SORT menambahkan fitur penampilan hasil pembelajaran mendalam, sedangkan ByteTrack memanfaatkan deteksi berkeyakinan rendah. Metode lanjutan memperbaiki model gerak, misalnya OC SORT dan model gerak berbasis jaringan seperti MoveSORT serta MotionTrack, atau memperbaiki afinitas lewat re-ID, C-TWIX, SMILETrack, QDTrack, dan jaringan saraf graf pada CoNo-Link. Kinerja diukur dengan MOTA yang didefinisikan sebagai 1 dikurangi jumlah deteksi positif palsu, negatif palsu, dan pertukaran identitas dibagi jumlah deteksi sebenarnya; IDF1 yang mencocokkan pada tingkat lintasan; serta HOTA yang merupakan rata-rata geometris dari akurasi deteksi dan akurasi asosiasi pada 19 ambang IoU antara 0,05 dan 0,95.

Angka hasil pada tolok ukur padat MOT17 dan MOT20 menunjukkan perbaikan HOTA dari 63,1% (ByteTrack, 2022) menjadi 67,1% (CoNo-Link, 2024), yaitu 4,0 poin, serta dari 61,3% menjadi 66,4% (BoostTrack++), yaitu 5,1 poin. Pada DanceTrack, HOTA ByteTrack sebesar 53,6% naik menjadi 58,2% dengan MotionTrack dan 63,0% dengan DeepMoveSORT, berturut-turut 4,6 dan 9,4 poin; metode luring terbaik CoNo-Link mencapai 63,8%. Pada SportsMOT, DeepMoveSORT meningkatkan HOTA dari 64,1% menjadi 78,7%, MOTA dari 94,5% menjadi 96,8%, dan IDF1 dari 71,4% menjadi 81,7%. Penulis juga menyusun tolok ukur agregasi dengan rata-rata makro berbobot 0,5 untuk MOT17, 0,5 untuk MOT20, dan 1,0 untuk DanceTrack; pada tolok ini MOTRv2 memimpin dengan HOTA 67,4% dan IDF1 75,8%, sedangkan ByteTrack memimpin MOTA sebesar 85,7%. Dengan bobot tambahan 1,0 untuk SportsMOT, DeepMoveSORT memimpin HOTA sebesar 67,9% dan IDF1 sebesar 74,1%, sementara ByteTrack tetap memimpin MOTA sebesar 89,1%.

Batasan yang dikemukakan penulis mencakup kebutuhan metode ujung-ke-ujung akan banyak kartu grafis dengan memori besar serta lambatnya inferensia yang menghalangi penggunaan waktu nyata; kinerjanya juga rendah pada adegan sangat padat. MOTA lebih dipengaruhi kinerja deteksi daripada asosiasi, sementara IDF1 sebaliknya, sehingga keduanya tidak cukup digunakan sendiri. Penulis mencatat bahwa banyak metode yang disebut daring sebenarnya memakai pascaolahan luring berupa interpolasi linear atau interpolasi Gaussian. Perbandingan antarparadigma tidak sepenuhnya setara karena metode *tracking-by-detection* memakai detektor YOLOX umum, sedangkan metode ujung-ke-ujung melatih detektor sendiri; UCMCTrack juga memerlukan parameter kamera yang diatur manual untuk setiap adegan. Karena banyak kajian hanya mengevaluasi satu atau dua ranah, penulis menyatakan generalisasi belum dapat dinilai secara menyeluruh dan mengusulkan perlunya tolok ukur MOT multiranah berskala besar.
