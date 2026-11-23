# Loose Oil Palm Fruitlet Detection Using YOLOv8 Nano Model By Layer Freezing Training for Better Accuracy with Small Dataset

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hakim2025loose` |
| Judul asli | Loose Oil Palm Fruitlet Detection Using YOLOv8 Nano Model By Layer Freezing Training for Better Accuracy with Small Dataset |
| Penulis | Hakim Nasir, Muhammad Najmi; Zakaria, Wan Nurshazwani Wan; Horio, Ryosuke; Uchiyama, Naoki |
| Tahun | 2025 |
| Venue | Rcar 2025 IEEE International Conference on Real Time Computing and Robotics |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [hakim2025loose.pdf](../pdf/hakim2025loose.pdf)
- DOI resmi: https://doi.org/10.1109/rcar65431.2025.11139587

## Gambaran Umum

Kajian ini menguji deteksi brondolan (buah lepas) kelapa sawit dengan YOLOv8 versi *nano* pada set data kecil. Penulis menyebut pengumpulan brondolan sebagai pekerjaan padat karya dan menyebut kekurangan tenaga kerja di masa depan. Masalah yang dikaji adalah *overfitting* (model hafal data latih) ketika data hanya 280 citra, dan apakah model kecil dengan pembekuan lapisan awal lebih baik daripada model besar.

Data berupa 280 citra brondolan matang dan terlalu matang, difoto dengan ponsel Redmi Note 10 Pro (1080x2400). Sekitar 4,5% data latih adalah citra tanpa objek. Pembagian: 224 latih, 28 uji, 28 validasi. Anotasi memakai Roboflow. Pemberi label, lokasi pengambilan citra, dan pembagian per pohon tidak disebut. Pembanding adalah studi sebelumnya dengan 7.171 citra tandan sawit.

Metode memakai YOLOv8 semua ukuran (n, s, m, l, x), citra diubah menjadi 640x640, dan augmentasi dinamis (*mosaic*, HSV, balik, pemotongan). Pelatihan memakai pengoptimal AdamW, 100 *epoch*, ukuran *batch* 4. Pembekuan lapisan berarti bobot lapisan awal tidak diperbarui (`requires_grad = False`) agar fitur dasar seperti tepi dan tekstur dipertahankan. Jumlah lapisan beku divariasikan pada model nano.

Model nano mencapai mAP50-95 0,75 pada set data kecil. Tabel III melaporkan mAP50-95 set kecil 0,720 (n) sampai 0,665 (l), dan set besar 0,917 (n) sampai 0,927 (m); selisih terbesar 0,251 menurut abstrak. Membekukan lebih dari 7 lapisan menurunkan nilai dari 0,75 menjadi 0,72. Model terbesar tanpa pembekuan mencapai 0,668. Matriks konfusi menunjukkan 10% positif palsu dan tanpa negatif palsu. Jarak latih-validasi sekitar 0,1 (DFL) dan 0,2 (*box loss*).

Keterbatasan: data uji hanya 28 citra dan tidak ada pembagian per pohon yang disebut. Angka 0,75 tidak dikaitkan jelas dengan data uji atau validasi. Tabel IV membandingkan dengan studi lain pada data berbeda. Tidak ada pencacahan atau acuan hitung. Penulis menyatakan metode ini hanya berlaku untuk model nano, data kecil, dan satu kelas, serta tidak membahas ketidakseimbangan citra kosong.
