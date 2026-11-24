# YOLO-RD-Apple orchard heterogenous image obscured fruit detection model

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hao2023yolo` |
| Judul asli | YOLO-RD-Apple orchard heterogenous image obscured fruit detection model |
| Penulis | Hao, Peng-fei; Liu, Li-qun; Gu, Ren-yuan |
| Tahun | 2023 |
| Venue | Journal of Graphics |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [hao2023yolo.pdf](../pdf/hao2023yolo.pdf)
- DOI resmi: https://doi.org/10.11996/jg.j.2095-302x.2023030456

## Gambaran Umum

Artikel berbahasa Mandarin ini, dengan abstrak berbahasa Inggris, mengusulkan YOLO-RD-Apple, detektor apel untuk robot panen yang menerima dua masukan: citra warna (RGB) dan citra kedalaman (*depth*). Sasarannya buah yang tertutup daun, cabang, atau buah lain di kebun.

Data diambil dari dataset terbuka PApple_RGB-D-Size yang dikumpulkan Universitat de Lleida dengan kereta kamera yang meniru robot panen. Dataset ini berisi 4.017 pasang citra warna dan kedalaman apel Fuji beresolusi 1024×1024, dengan 16.332 buah. Kotak buah dianotasi di citra warna dan dipakai juga untuk citra kedalaman karena keduanya sudah selaras per piksel. Pasangan citra dibagi acak 8:1:1 menjadi 3.216 latih, 401 validasi, dan 400 uji.

Arsitekturnya dibangun dari YOLOv4. Citra warna diproses MobileNetV2 dan citra kedalaman diproses MobileNetV2-Lite, versi yang lebih ringan. Bagian penggabung fitur diberi modul SE-DWCSP3, gabungan CSPNet, konvolusi terpisah per kanal, dan perhatian per kanal. NMS biasa diganti Soft NMS supaya buah yang berdempetan tidak ikut terhapus.

Pada data uji, AP mencapai 93,1%, naik 1,4 poin dari YOLOv4, dengan parameter 70% lebih sedikit dan kecepatan 40,5 FPS pada GPU V100. Kajian ini hanya mendeteksi buah per pasang citra. Tidak ada pencacahan dan tidak ada penautan buah antarcitra.
