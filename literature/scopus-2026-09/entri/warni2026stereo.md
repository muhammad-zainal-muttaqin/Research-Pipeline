# Stereo Vision-Based Detection and 3D Localization of Loose Oil Palm Fruits Using YOLOv8 and Hungarian Matching

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `warni2026stereo` |
| Judul asli | Stereo Vision-Based Detection and 3D Localization of Loose Oil Palm Fruits Using YOLOv8 and Hungarian Matching |
| Penulis | Warni, Elly; Indrabayu; Achmad, Andani; Syarif, Syafruddin; Rudi; Sadi, Nadya Petroya |
| Tahun | 2026 |
| Venue | Ingenierie Des Systemes D Information |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [warni2026stereo.pdf](../pdf/warni2026stereo.pdf)
- DOI resmi: https://doi.org/10.18280/isi.310225

## Gambaran Umum

Penelitian ini bertujuan mengembangkan sistem persepsi berbasis *stereo vision* untuk mendeteksi dan melokalisasi buah brondolan kelapa sawit di perkebunan. Pengumpulan buah yang jatuh dari tandan masih dilakukan secara manual di sebagian besar perkebunan. Kondisi ini menimbulkan kehilangan hasil, biaya tenaga kerja yang tinggi, dan kesulitan memperluas skala panen. Penulis menilai robot panen otomatis membutuhkan modul persepsi yang mampu menemukan buah sekaligus menentukan posisinya dalam ruang tiga dimensi.

Data berasal dari perkebunan kelapa sawit dengan buah brondolan di permukaan tanah sebagai objek. Kumpulan data terdiri atas 1.520 citra beranotasi dalam format YOLO. Sebanyak 759 citra direkam langsung dengan kamera stereo ZED 2 pada tinggi kamera 20 hingga 50 cm dan jarak objek 20 hingga 120 cm. Sebanyak 761 citra lainnya diambil dari repositori publik Roboflow. Anotasi *bounding box* dibuat secara manual. Untuk pengujian sistem dalam kondisi nyata, penulis menyiapkan 41 video rekaman ZED 2. Setelah augmentasi, data latih berjumlah 3.998 citra. Jarak antara lensa kamera stereo tetap 120 mm.

Penulis membandingkan tiga varian YOLOv8, yaitu YOLOv8n, YOLOv8s, dan YOLOv8m, yang dilatih dengan pengaturan yang sama. Setiap frame kiri dan kanan diproses secara terpisah, lalu deteksi dipasangkan dengan *Hungarian matching* memakai matriks biaya pada pusat kotak dan ambang penyaring. Jarak dihitung dengan *triangulation* stereo yang dikombinasikan dengan proyeksi *ground-plane*. YOLOv8s memberikan hasil paling baik dengan akurasi 94,79% dan F1-score 0,972. YOLOv8n mencapai akurasi 93,56% dan F1-score 0,966. Pada tinggi kamera 30 cm, YOLOv8s mencapai akurasi 97,63% dengan F1-score 0,99. Jumlah *false positive* dan *false negative* YOLOv8s adalah 1.982 dan 3.787, lebih rendah daripada YOLOv8n yang masing-masing 2.574 dan 4.706. Untuk estimasi jarak, galat terendah dicapai pada tinggi kamera 50 cm dengan MAPE 0,86% dan MAE 0,62 cm. Pada tinggi 20 cm, MAPE mencapai 2,84% dan MAE 1,45 cm. Pada tinggi 40 cm, MAPE 1,44% dengan akurasi 94,42%.

Penulis menyatakan beberapa batasan. Evaluasi dilakukan pada tingkat instance, sehingga *True Negative* bernilai nol. Akibatnya, akurasi berpotensi tergelembung, meskipun penulis menilai dampaknya kecil karena buah muncul pada sebagian besar frame uji. Oleh sebab itu, F1-score dipandang sebagai indikator yang lebih andal. Penulis juga belum melaporkan mAP dan menyebutnya sebagai pekerjaan lanjutan. Kinerja sistem dipengaruhi oleh variasi pencahayaan dan stabilitas mekanis platform kamera. Kinerja YOLOv8n juga kurang stabil pada jarak dekat. Penulis menyarankan penelitian lanjutan tentang ketahanan terhadap pencahayaan ekstrem, algoritma adaptif, pelacakan objek, dan integrasi sistem ke robot panen. Penulis juga menyarankan kamera dengan tinggi ganda atau tinggi yang dapat diatur.
