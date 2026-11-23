# Analysis Of Ground FFB Detection Via Real Sense Camera

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kadir2022analysis` |
| Judul asli | Analysis Of Ground FFB Detection Via Real Sense Camera |
| Penulis | Kadir, K.; Hasan, W.Z.W.; Zaidi, M.S.A.A; Kassim, M.S.M; Mustafa, M.F. |
| Tahun | 2022 |
| Venue | 8th IEEE International Conference on Smart Instrumentation Measurement and Applications Icsima 2022 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [kadir2022analysis.pdf](../pdf/kadir2022analysis.pdf)
- DOI resmi: https://doi.org/10.1109/icsima55652.2022.9929099

## Gambaran Umum

Makalah konferensi ini menguji detektor YOLOv4 dan YOLOv4-tiny untuk mendeteksi tandan buah segar yang tergeletak di tanah. Detektor itu menjadi bagian mesin pengumpul tandan otomatis yang dikembangkan Universiti Putra Malaysia bersama industri sawit. Kamera RGB-D Intel RealSense D435i memberi citra warna untuk deteksi dan jarak tandan ke kamera untuk menggerakkan lengan pengambil. Pengendali utamanya Nvidia Jetson AGX Xavier, sedangkan Arduino menggerakkan sendi lengan melalui ROS.

Set data dilabeli di Roboflow dan berisi satu kelas (tandan): 1.104 citra latih, 105 citra validasi, dan 47 citra uji. Augmentasi berupa distorsi fotometrik (kecerahan, kontras, rona, saturasi, derau) dan geometrik (skala, potong, balik, putar). Model dilatih di Google Colab. Evaluasi memakai mAP, IoU rata-rata, F1, FPS, dan waktu deteksi.

Penulis melaporkan F1 0,96 untuk YOLOv4 dan YOLOv4-tiny. YOLOv4-tiny lebih cepat: waktu deteksi satu tandan sekitar 1 detik, dibanding 3 detik untuk YOLOv4, dan laju bingkai pada robot sekitar 50 sampai 60 FPS. Nilai mAP dan IoU ada di tabel yang tercetak sebagai gambar, sehingga tidak terbaca dari teks hasil ekstraksi.

Keterbatasan yang dapat diperiksa dari teks adalah sebagai berikut. Tandan tidak dicacah, dan tidak ada penautan tandan antarcitra; setiap citra dinilai sendiri. Depth hanya dipakai untuk menentukan posisi lengan, bukan untuk deteksi. Set uji hanya 47 citra, dan tidak disebutkan apakah citra uji berasal dari lokasi atau hari yang berbeda dengan citra latih.
