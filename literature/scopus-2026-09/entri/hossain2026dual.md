# Dual-Detector Vision and Depth-Aware Back-Projection for Accurate Apple Detection and 3D Localisation for Robotic Harvesting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hossain2026dual` |
| Judul asli | Dual-Detector Vision and Depth-Aware Back-Projection for Accurate Apple Detection and 3D Localisation for Robotic Harvesting |
| Penulis | Hossain, Tagor; Shi, Peng; Kovacs, Levente |
| Tahun | 2026 |
| Venue | Robotics |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [hossain2026dual.pdf](../pdf/hossain2026dual.pdf)
- DOI resmi: https://doi.org/10.3390/robotics15020047

## Gambaran Umum

Penelitian ini mengatasi deteksi apel dan pelokalan tiga dimensi untuk pemanen robot di kebun, tempat oklusi daun, tumpang tindih buah, perubahan pencahayaan, derau kedalaman, dan kesamaan warna antara buah serta daun menurunkan keandalan penglihatan RGB. Penulis menilai bahwa metode dengan satu detektor rentan terhadap deteksi palsu, kelewatan, dan pemisahan instance yang buruk pada adegan rapat, sementara kesalahan deteksi 2D langsung merambat ke tahap pelokalan 3D. Usulan yang diajukan adalah kerangka penglihatan RGB-D dengan dua detektor, YOLOv8 dan Mask R-CNN, yang digabungkan dengan back-projeksi sadar kedalaman untuk menghasilkan representasi 2D yang stabil dan posisi 3D metrik secara real time.

Penulis memakai dua himpunan data publik untuk mengembangkan komponen segmentasi, yaitu MinneApple yang berisi 1.000 citra kebun beranotasi dan Amodal Apple yang berisi 3.019 citra dengan ragam penampilan apel yang lebih luas. Data dibagi menjadi 2.290 citra latih dan 801 citra validasi, dengan semua masukan diubah ke resolusi tetap 896 × 896 piksel. Pengujian lapangan dilakukan di kebun apel Lenswood, Australia Selatan, dengan kamera RGB-D yang digenggam dan dijalankan pada sistem tertanam NVIDIA Jetson AGX dengan 32 GB VRAM; pengambilan dilakukan pada pagi dan siang hari dalam kondisi cerah berawan serta angin ringan. Augmentasi pasangan RGB-depth diterapkan secara terkoordinasi berupa pembalikan horizontal, rotasi dalam bidang, penskalaan anisotropik, dan penyesuaian kecerahan, sehingga kedua modalitas tetap selaras secara geometris dan fotometrik.

Fusi dua detektor memanfaatkan kecepatan YOLOv8 dalam melokalisasi kandidat dan kemampuan Mask R-CNN dalam menghasilkan batas instance yang presisi. Skor kepercayaan kedua detektor dinormalisasi ke skala yang sama, lalu kotak ikat digabungkan secara berbobot terhadap kepercayaan, topeng segmentasi disatukan secara pixel-wise, dan skor akhir diambil sebagai nilai maksimum dari kedua detektor. Representasi 2D hasil fusi dipetakan ke ruang 3D dengan model kamera pinhole, menghasilkan himpunan titik per buah dari piksel yang ditandai sebagai buah pada topeng. Pusat buah diperkirakan dengan median geometrik, lalu diperhalus dengan pembobotan konsistensi kedalaman berbentuk Gaussian yang memberikan pengaruh lebih besar pada piksel dengan kedalaman dekat nilai rata-rata topeng, sehingga menekan pengaruh daun, ranting, dan pengukuran kedalaman yang bergeser. Normalisasi intensitas lokal dengan jendela 9 × 9 mengurangi bayangan dan sorotan. Ukuran buah diperkirakan dari luas topeng dengan asumsi siluet hampir melingkar, dikonversi ke metrik memakai kedalaman rata-rata dan panjang fokus, sedangkan rentang kedalaman diperkirakan melalui regresi kuadratik dari rentang lateral yang dikalibrasi pada apel dengan ukuran terukur.

Pada tabel perbandingan, metode yang diusulkan mencapai akurasi 98,9%, mAP 94,2%, F1-score 93,3%, recall 92,8%, dan kecepatan 86,42 FPS. Sebagai pembanding, Improved YOLOv8 mencatat 95,2% akurasi, 93,3% mAP, 91,0% F1, 87,4% recall, dan 72,5 FPS; Mask R-CNN mencatat 96,0%, 89,0%, 85,2%, 92,7%, dan 78,6 FPS; MobileNetV3 mencatat 93,8%, 87,1%, 86,1%, 79,7%, dan 90,5 FPS. Presisi, recall, dan F1 dihitung dari TP, FP, dan FN dengan rumus P = TP/(TP + FP), R = TP/(TP + FN), serta F1 = 2PR/(P + R). Penulis menyatakan kecepatan 86,42 FPS diukur pada Jetson AGX untuk tahap deteksi 2D saja, bukan untuk keseluruhan alur deteksi dan pelokalan 3D.

Batasan yang dinyatakan penulis mencakup munculnya kasus gagal ketika oklusi parah, pencahayaan ekstrem, dan kesamaan warna buah dengan latar terjadi bersamaan; dalam kondisi tersebut segmen menjadi tidak lengkap atau buah tidak terdeteksi. Asumsi siluet hampir melingkar merupakan penyederhanaan karena apel nyata dapat memanjang dan topeng dapat terpotong saat oklusi, meski penulis menyatakan pengaruhnya diredam oleh rata-rata kedalaman dan analisis rentang lateral serta kedalaman. Parameter toleransi pembobotan kedalaman dan ukuran jendela normalisasi dipilih secara empiris pada data validasi, bukan dioptimalkan secara luas. Data yang digunakan tidak dipublikasikan dan hanya dapat diperoleh atas permintaan penulis korespondensi. Penulis juga menempatkan persepsi multi-pandang, informasi temporal dari video, pembelajaran fitur invarian pencahayaan, serta perencanaan gerak dengan RRT atau RRT* sebagai pekerjaan mendatang, sehingga kemampuan tersebut belum dinilai dalam studi ini.
