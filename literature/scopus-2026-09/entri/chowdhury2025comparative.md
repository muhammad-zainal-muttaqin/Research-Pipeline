# Comparative Study of Different YOLO Variants for Ripeness Detection of Palm Oil Fresh Fruit Bunches

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chowdhury2025comparative` |
| Judul asli | Comparative Study of Different YOLO Variants for Ripeness Detection of Palm Oil Fresh Fruit Bunches |
| Penulis | Chowdhury, Alvi Khan; Saruchi, Sarah 'Atifah; Said, Wan Zailah Wan; Ul Rehman, Ateeq; Lie, Louis Gautama; Izni, Nor Aziyatul; Jahan, Mohammad Saukat |
| Tahun | 2025 |
| Venue | 2025 IEEE 6th International Conference in Robotics and Manufacturing Automation Roma 2025 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [chowdhury2025comparative.pdf](../pdf/chowdhury2025comparative.pdf)
- DOI resmi: https://doi.org/10.1109/roma66616.2025.11155279

## Gambaran Umum

Penulis membandingkan tiga versi *YOLO* (YOLOv5, YOLOv6, YOLOv7) untuk mendeteksi kematangan tandan buah segar (TBS) kelapa sawit secara waktu nyata. Masalah yang disebut adalah penilaian manual oleh manusia yang keliru karena posisi tandan, tinggi pohon, cuaca, dan pencahayaan. Penulis juga menyatakan bahwa kebanyakan studi terdahulu tidak memakai data yang dikumpulkan langsung dari kebun.

Data berupa 2.000 citra dari satu kebun sawit di Selangor, Malaysia. Citra dibagi rata untuk empat kelas: terlalu matang (*overripe*), matang (*ripe*), kurang matang (*underripe*), dan mentah (*unripe*). Pembagian latih dan uji 80,0% dan 20,0%. Pelabelan memakai situs makesense.ai. Jumlah tandan per citra, jumlah pohon, sensor atau kamera, dan pemberi label tidak disebut.

Lima model dilatih: YOLOv5s, YOLOv5m, YOLOv6s, YOLOv6m, dan YOLOv7. *YOLO* adalah detektor satu tahap yang memprediksi kotak pembatas (*bounding box*) dan kelas dalam satu lintasan jaringan. Semua model memakai ukuran citra 416, ukuran *batch* 16, dan 100 *epoch*. Arsitektur tidak diubah.

YOLOv5s terbaik menurut penulis: presisi 97,0%, *recall* 100%, F1 98,5%, 35,76 FPS. AP per kelas YOLOv5s: mentah 93,0%, kurang matang 95,0%, matang 92,0%, terlalu matang 86,0%. YOLOv5m memiliki presisi 98,0% dan AP mentah 95,0%, tetapi 29,5 FPS. YOLOv6s mencapai 103,6 FPS dengan F1 27,0%. YOLOv6m F1 33,1% dan YOLOv7 F1 94,6%. Tabel II membandingkan F1 98,5% dengan F1 lima studi lain (69,3% sampai 97,0%).

Keterbatasan yang dapat diperiksa: tidak ada pembagian per pohon dan tidak ada set validasi terpisah. Tidak ada mAP50-95 dan tidak ada ukuran sebaran seperti ulangan atau interval kepercayaan. Perbandingan dengan studi lain memakai data berbeda. Tidak ada pencacahan, pelacakan, atau penggabungan beberapa citra tandan yang sama. Nilai YOLOv6s dan YOLOv6m di Tabel I sama persis dengan Tabel 1 [Chowdhury dkk. 2024](chowdhury2024oil.md), yang memakai 80 citra dari kebun di Selangor; laporan ini tidak mengutip makalah 2024 itu.
