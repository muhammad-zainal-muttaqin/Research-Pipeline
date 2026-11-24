# Oil Palm Fresh Fruit Branch Ripeness Detection Using YOLOV6 Algorithm

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chowdhury2024oil` |
| Judul asli | Oil Palm Fresh Fruit Branch Ripeness Detection Using YOLOV6 Algorithm |
| Penulis | Chowdhury, Alvi Khan; Said, Wan Zailah Binti Wan; Saruchi, Sarah `Atifah |
| Tahun | 2024 |
| Venue | Lecture Notes in Mechanical Engineering |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [chowdhury2024oil.pdf](../pdf/chowdhury2024oil.pdf)
- DOI resmi: https://doi.org/10.1007/978-981-97-0169-8_14

## Gambaran Umum

Makalah konferensi ini menguji YOLOv6s dan YOLOv6m untuk mendeteksi tandan buah segar (TBS) kelapa sawit sekaligus memberi kelas kematangannya. *YOLO* adalah detektor satu tahap yang memprediksi kotak pembatas (*bounding box*) dan kelas dalam satu lintasan jaringan. Masalah yang disebut adalah penilaian kematangan oleh petugas panen yang keliru karena tandan tertutup pelepah, pohon tinggi, cuaca, pencahayaan, dan salah hitung brondolan di tanah.

Data berupa 80 citra dari satu kebun di Selangor, Malaysia, dibagi 80% latih dan 20% uji. Ada empat kelas: mentah (*unripe*), kurang matang (*underripe*), matang (*ripe*), dan lewat matang (*overripe*). Pelabelan memakai situs makesense.ai. Teks hanya menyebut kebun sebagai tempat pemotretan. Contoh citra menunjukkan satu tandan lewat matang di tanah dan tiga tandan di pohon, masing-masing difoto dari dekat. Kamera, jumlah pohon, dan jumlah tandan per citra tidak disebut.

Kedua model dilatih 100 *epoch* pada GPU Tesla K80 di Google Colab, dengan ukuran citra 416×416 dan *batch* 16. YOLOv6m lebih baik: presisi 0,369, *recall* 0,30, F1 0,331, mAP50 0,369, dan mAP50-95 0,165. YOLOv6s mencapai mAP50 0,30 dan mAP50-95 0,093, tetapi lebih cepat (103,6 FPS dibanding 54 FPS). Penulis menyatakan presisi dapat dinaikkan dengan menambah data latih. Kalimat simpulan di seksi hasil menyebut "YOLOV5m" sebagai model terpilih, padahal YOLOv5 tidak diuji; tabel dan simpulan akhir menunjuk YOLOv6m.

Keterbatasan yang dapat diperiksa dari teks adalah sebagai berikut. Set uji sekitar 16 citra, tanpa set validasi terpisah, tanpa pembagian per pohon, dan tanpa ulangan. Tandan tidak dicacah dan tidak ditautkan antarcitra. Kelompok penulis yang sama kemudian melaporkan perbandingan YOLOv5, YOLOv6, dan YOLOv7 pada 2.000 citra dari kebun di Selangor ([Chowdhury dkk. 2025](chowdhury2025comparative.md)). Ke-14 nilai YOLOv6 di laporan itu (presisi, *recall*, F1, FPS, dan nilai per kelas, untuk YOLOv6s dan YOLOv6m) sama dengan Tabel 1 makalah ini. Akurasi per kelas pada citra uji di makalah ini disebut AP di laporan 2025, dan laporan 2025 tidak mengutip makalah ini, walaupun ukuran datanya berbeda menurut teks (80 citra di sini, 2.000 citra di sana).
