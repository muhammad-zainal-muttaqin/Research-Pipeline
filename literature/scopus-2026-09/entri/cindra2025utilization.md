# Utilization of Machine Learning in Identifying Oil Palm Fruit Ripeness to Enhance the Efficiency of Oil Palm Plantations

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cindra2025utilization` |
| Judul asli | Utilization of Machine Learning in Identifying Oil Palm Fruit Ripeness to Enhance the Efficiency of Oil Palm Plantations |
| Penulis | Cindra, Jason Ananda; Miranda, Eka; Natawijaya, Yoga Khantisena; Rahman, Fajrul |
| Tahun | 2025 |
| Venue | 2025 4th International Conference on Digital Transformation and Applications Icdxa 2025 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [cindra2025utilization.pdf](../pdf/cindra2025utilization.pdf)
- DOI resmi: https://doi.org/10.1109/icdxa69105.2025.11329640

## Gambaran Umum

Penulis membangun sistem deteksi kematangan TBS kelapa sawit dari citra RGB dengan pembelajaran mesin. Masalah yang disebut adalah penilaian kematangan manual yang subjektif dan dipengaruhi pencahayaan serta sudut pandang. Penulis juga menyatakan bahwa studi terdahulu kebanyakan dilakukan di lingkungan terkendali.

Data adalah set data terbuka berlisensi CC BY 4.0 dari kebun di Johor, Negeri Sembilan, dan Perak, Malaysia. Jumlahnya 450 citra unik dengan anotasi poligon dalam lima kelas: rusak (*damaged*), kosong (*empty*), terlalu matang, matang, dan mentah. Pembagiannya 300 citra latih, 80 validasi, dan 70 uji. Citra latih diaugmentasi menjadi 900. Pemberi label dan sensor tidak disebut.

Metode membandingkan 15 varian *YOLO* (v8, v9, v10, v11, v12; ukuran nano, tiny, small, medium) dari pustaka Ultralytics. Model dilatih paling banyak 300 *epoch* pada ukuran 640x640 dengan optimizer AdamW dan penghentian dini (*early stopping*) berkesabaran 20 *epoch*. Model dari *epoch* terbaik pada validasi dievaluasi pada set uji. mAP50 adalah rerata presisi pada ambang *IoU* (irisan atas gabungan) 0,5.

YOLOv10n terbaik pada set uji: mAP50 0,9007, mAP50-95 0,7410, F1 0,8953, presisi 0,9453, *recall* 0,8504, kecepatan inferensi 7,34 ms/citra. YOLOv8s memperoleh mAP50 0,8911 dan mAP50-95 0,6661. YOLO11s memperoleh mAP50-95 0,6679 dan F1 0,8777. Pada matriks konfusi, kelas kosong terdeteksi 100% dan kelas rusak 67% pada ketiga model.

Keterbatasan yang dapat diperiksa: set uji hanya 70 citra, tidak ada pembagian per pohon yang disebut, dan kelas rusak dan kosong sangat sedikit. Penulis sendiri menyebut kecenderungan *overfitting* pada YOLOv10n (mAP50 di atas 0,9) dan kemungkinan *underfitting* pada YOLOv8s dan YOLOv12s yang berhenti pada *epoch* 14 dan 13. Tidak ada pencacahan tandan dan tidak ada penggabungan beberapa citra tandan yang sama.
