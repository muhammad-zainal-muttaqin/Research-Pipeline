# Object Detection Algorithms for Ripeness Classification of Oil Palm Fresh Fruit Bunch

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mansour2022object` |
| Judul asli | Object Detection Algorithms for Ripeness Classification of Oil Palm Fresh Fruit Bunch |
| Penulis | Mansour, Mohamed Yasser Mohamed Ahmed; D. Dambul, Katrina; Choo, Kan Yeep |
| Tahun | 2022 |
| Venue | International Journal of Technology |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [mansour2022object.pdf](../pdf/mansour2022object.pdf)
- DOI resmi: https://doi.org/10.14716/ijtech.v13i6.5932

## Gambaran Umum

Makalah ini membandingkan tiga keluarga detektor objek untuk mengklasifikasikan tingkat kematangan tandan buah segar (TBS) kelapa sawit dari citra. Tujuannya memilih model yang paling tepat untuk aplikasi pada perangkat bergerak dan sistem panen otonom. Penulis menguji MobileNetV2 SSD, EfficientDet-Lite0, Lite1, dan Lite2, serta YOLOv5n, YOLOv5s, dan YOLOv5m. Hasil utamanya: YOLOv5m memperoleh mAP 0,842 (0,5:0,95) dan diusulkan sebagai model untuk klasifikasi kematangan.

Data terdiri atas 328 citra TBS yang dikumpulkan di tanah setelah panen, bukan pada pohon. Sebanyak 304 citra dipakai setelah seleksi, lalu dibagi dengan rasio 70%, 20%, dan 10% untuk latih, validasi, dan uji. Empat kelas mengikuti standar MPOB: matang, belum matang, setengah matang, dan lewat matang. Pelatihan memakai masukan 640×640 piksel, 300 epoch, dan ukuran batch 16 untuk YOLOv5. Model dilatih awal (pralatih) pada COCO. EfficientDet dan SSD memakai backend TensorFlow. Pelatihan dilakukan pada GPU Tesla K80 di Google Colab.

Tabel perbandingan model melaporkan mAP pada data penelitian, waktu latih, mAP COCO sebagai acuan, dan jumlah parameter. MobileNetV2 SSD memperoleh mAP 0,478 dan mAP COCO 0,222, tanpa waktu latih yang dilaporkan. EfficientDet-Lite0 memperoleh 0,743 (65 menit; 3,2 juta parameter), Lite1 0,803 (100 menit; 4,2 juta), dan Lite2 0,812 (140 menit; 5,3 juta). YOLOv5n memperoleh 0,781 (43 menit; 1,9 juta parameter), YOLOv5s 0,832 (90 menit; 7,2 juta), dan YOLOv5m 0,842 (235 menit; 21,2 juta). Penulis menjelaskan bahwa YOLOv5m lebih lama dilatih karena kedalaman dan lebar modelnya lebih besar. Kecepatan deteksi YOLOv5 disebut 6 sampai 8 ms, tetapi angka itu tidak disertai tabel maupun keterangan perangkat uji. Perbandingan dengan YOLOv3 (Khamis, 2022) hanya naratif: YOLOv5m mencapai 0,84 untuk empat kelas, sedangkan YOLOv3 dipakai untuk tiga kelas. Kedua penelitian itu tidak memakai data yang sama.

Penulis mengakui beberapa keterbatasan. Citra diambil di tanah, sehingga TBS di pohon, yang tertutup pelepah atau tersinari berbeda, belum diuji. Penyetelan hiperparameter belum dilakukan. Ensemble YOLOv5 dengan EfficientDet, aplikasi seluler, dan uji waktu nyata belum dikerjakan. Jumlah citra uji sekitar 30 (10% dari 304), dan jumlah objek per kelas tidak dilaporkan. Selisih 0,01 antarmodel karena itu tidak dapat diuji signifikansinya dengan data yang tersedia.
