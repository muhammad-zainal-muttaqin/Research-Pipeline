# Comparison of the Latest Version of Deep Learning YOLO Model in Automatically Detecting the Ripeness Level of Oil Palm Fruit in PTPN IV, North Sumatra, Indonesia

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `purba2024comparison` |
| Judul asli | Comparison of the Latest Version of Deep Learning YOLO Model in Automatically Detecting the Ripeness Level of Oil Palm Fruit in PTPN IV, North Sumatra, Indonesia |
| Penulis | Purba, Samdo Jumar; Ferdinandz Tandion, William; Irwansyah, Edy |
| Tahun | 2024 |
| Venue | Proceedings 2024 International Conference on Information Technology and Computing Icitcom 2024 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [purba2024comparison.pdf](../pdf/purba2024comparison.pdf)
- DOI resmi: https://doi.org/10.1109/icitcom62788.2024.10762053

## Gambaran Umum

Penelitian ini membandingkan akurasi YOLOv8 dan YOLOv9 dalam mendeteksi tingkat kematangan buah kelapa sawit. Penulis ingin mengetahui apakah YOLOv9 lebih akurat daripada pendahulunya. Penulis menyebut bahwa pada saat penulisan belum ditemukan kajian yang memakai YOLOv9 untuk tujuan ini.

Data dikumpulkan langsung dari area kebun kelapa sawit PTPN IV Medan, Sumatera Utara. Set data terdiri atas 180 citra berukuran 640x640 dengan kamera 12 megapiksel. Sebagian citra memuat beberapa buah dan sebagian hanya satu buah. Citra diberi label di Roboflow dengan tiga kelas: matang (*ripe*), busuk (*rotten*), dan mentah (*unripe*). Pembagiannya 124 citra latih, 37 citra validasi, dan 19 citra uji. Siapa pemberi label tidak disebut.

Pra-pemrosesan mencakup *auto-orient* (menyesuaikan orientasi citra dengan penyimpanannya), pengubahan ukuran ke 640x640, dan *null filter* (membuang citra tanpa objek). Augmentasi memakai empat variasi: *flip*, rotasi 90 derajat, rotasi, dan *shear* (kemiringan). Set data menjadi 428 citra dan set latih menjadi 372 citra. Kedua model dilatih di Google Colab selama 25 *epoch* dengan *batch* 16 dan ukuran citra 640x640. YOLOv8 adalah detektor satu tahap. YOLOv9 memakai GELAN (tulang punggung jaringan) dan PGI (metode pelatihan dengan cabang bantu untuk gradien).

Pada Tabel II dan III, YOLOv8 memperoleh precision 0,987, recall 0,944, mAP50 0,984, dan mAP50-95 0,736 untuk semua kelas. YOLOv9 memperoleh precision 0,945, recall 0,967, mAP50 0,99, dan mAP50-95 0,787. Per kelas, mAP50 YOLOv9 untuk kelas matang 0,982 (YOLOv8 0,963), untuk kelas mentah 0,992 (YOLOv8 0,995), dan untuk kelas busuk keduanya 0,995. Tabel itu berjudul hasil pelatihan, dan teks tidak menyebut jelas apakah angkanya dihitung pada set validasi atau set uji.

Keterbatasan yang dapat diperiksa: set data hanya 180 citra, set uji hanya 19 citra, dan tidak ada pengulangan dengan beberapa *seed* atau uji signifikansi untuk selisih 0,984 dan 0,99. Pembagian tidak dinyatakan per pohon. Tidak disebut apakah citra dari pohon yang sama jatuh di set berbeda. Augmentasi dilakukan sebelum atau bersama pembagian, dan teks tidak menjelaskan apakah citra hasil augmentasi bocor ke set evaluasi. Penulis sendiri menyatakan perlunya validasi pada kondisi lingkungan yang berbeda. Tidak ada pencacahan buah.
