# GDYEY: Grape detection and yield estimation framework based on YOLO architecture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ma2026gdyey` |
| Judul asli | GDYEY: Grape detection and yield estimation framework based on YOLO architecture |
| Penulis | Ma, Jinlin; Xu, Silong; Ma, Ziping; Cao, Haojie; Lin, Baobao |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [ma2026gdyey.pdf](../pdf/ma2026gdyey.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2026.111755

## Gambaran Umum

Penelitian ini membahas pendugaan hasil panen anggur yang akurat. Ketepatan pendugaan bergantung pada deteksi buah. Namun, ukuran buah yang bervariasi dan oklusi sering menurunkan ketepatan deteksi. Penulis menilai bahwa pencacahan saja tidak cukup untuk pendugaan yang akurat. Ukuran dan kedalaman buah juga perlu diperhitungkan. Untuk itu penulis mengusulkan kerangka GDYEY, yang menggabungkan jaringan deteksi anggur berbasis arsitektur YOLO dengan jaringan *depth estimation*. Kontribusi utamanya mencakup kumpulan data deteksi baru, arsitektur deteksi KD-ECNN yang memakai *knowledge distillation*, dan strategi pendugaan hasil berbasis estimasi kedalaman yang disebut YEDE.

Penulis membangun kumpulan data GD yang berisi 1.900 citra anggur. Seluruh citra bersumber dari platform Roboflow. Penulis juga menambahkan citra dari kumpulan data grape_detection_californianight. Data ini mencakup kondisi malam hari, cahaya dari belakang, dan kebun dengan kepadatan tinggi. Kondisi tersebut kurang terwakili dalam WGISD. Data dibagi secara acak menjadi data latih dan data validasi dengan rasio 9:1. Format label dikonversi ke VOC dan COCO. Untuk pendugaan hasil, penulis memakai 50 citra anggur yang dikumpulkan di Yinchuan, Tiongkok. Citra diambil pada tahap buah awal, sekitar satu bulan sebelum matang. Sensor yang digunakan adalah kamera RGB. Penulis tidak dapat memperoleh informasi kedalaman langsung dari kamera karena keterbatasan peralatan. Kedalaman karena itu diperkirakan dari citra dengan jaringan LapDepth.

KD-ECNN memasukkan modul ECA ke dalam ELAN, DCN ke dalam C2f, modul SPF untuk fusi fitur multiskala, dan modul AMMP untuk meningkatkan lokalisasi fitur. Model dilatih dengan ukuran batch 8 selama 300 epoch, dengan *early stopping* bila kinerja pada data validasi tidak membaik. Pada kumpulan data GD, KD-ECNN mencapai mAP 81,6 persen dan mengungguli 15 model pembanding, termasuk Faster RCNN, CenterNet, YOLOv5, YOLOv7, dan YOLOv9. Nilai *precision* KD-ECNN sedikit lebih rendah daripada YOLOv5, dan nilai *recall*-nya sedikit lebih rendah daripada CenterNet. Meski demikian, skor F1-nya lebih tinggi daripada keduanya. Pada pencacahan, persamaan regresi KD-ECNN, y = 0,8678x, paling dekat dengan garis ideal y = x. Persamaan YOLOv5 adalah y = 0,8213x dan YOLOv7 adalah y = 0,7928x. Pada pendugaan hasil, YEDE meningkatkan akurasi sekitar 25 persen dibandingkan metode yang hanya menghitung. Peningkatannya sekitar 10 persen dibandingkan metode berbasis luas area.

Penulis menyatakan bahwa estimasi kedalaman masih terbatas pada kondisi sulit. Contohnya adalah pencahayaan malam hari yang kurang memadai dan kelompok buah yang kecil. Penulis juga tidak memiliki kumpulan data produksi. Akibatnya, hasil pendugaan belum dapat dibandingkan dan diverifikasi dengan produksi aktual. Penelitian lanjutan direncanakan untuk memperbaiki modul estimasi kedalaman dengan menambahkan fitur adegan dan informasi multimodal. Penulis juga berencana membangun kumpulan data produksi.
