# COMPARISON OF PALM OIL FRUIT RIPENESS DETECTION AND CLASSIFICATION METHODS USING DEEP LEARNING

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hutapea2025comparison` |
| Judul asli | COMPARISON OF PALM OIL FRUIT RIPENESS DETECTION AND CLASSIFICATION METHODS USING DEEP LEARNING |
| Penulis | Hutapea, R.R.; others |
| Tahun | 2025 |
| Venue | Icic Express Letters Part B Applications |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [hutapea2025comparison.pdf](../pdf/hutapea2025comparison.pdf)
- DOI resmi: https://doi.org/10.24507/icicelb.16.07.797

## Gambaran Umum

Kajian ini berangkat dari keterbatasan tenaga kerja terampil untuk menilai kematangan buah sawit di Indonesia. Buah pada satu pohon atau satu kebun memiliki tahap kematangan yang berbeda, sehingga hanya buah matang yang seharusnya dipanen dan pemisahannya memerlukan keterampilan. Tujuan kajian adalah membandingkan akurasi deteksi kematangan buah sawit antara YOLOv8s dan YOLOv10s. Pemilihan kedua model didasarkan pada hasil sebelumnya yang menyatakan YOLOv8 lebih baik dalam mengenali objek kecil, sedangkan YOLOv10s dibangun di atas YOLOv8s dengan klaim efisiensi dan 25% lebih sedikit parameter daripada YOLOv9-C.

Data dikumpulkan di kebun sawit PTPN 4 di Medan, Sumatra Utara, dengan kamera iPhone 12. Penulis merekam dua jenis foto, yaitu citra Close-up buah tunggal dan foto kelompok tandan buah matang dari beberapa sudut pandang. Sejumlah 250 citra dikategorikan secara manual ke dalam tiga folder, yaitu ripe, rotten, dan unripe, lalu diunggah ke Roboflow untuk dianotasi sesuai kategori. Dari 250 citra, 80 citra dengan kualitas terbaik dipilih dan diperbanyak dengan pembalikan serta rotasi 15° dan 90°, sehingga menjadi 185 citra. Kedua model dilatih pada data yang sama dengan dua jumlah epoch, yaitu 25 dan 50. Pembagian data latihan, validasi, dan uji tidak dinyatakan, demikian pula jumlah citra per kelas.

Hasil diukur dengan mAP50 dan mAP50-95 pada Tabel 2. YOLOv8s mencapai mAP50 0,995 pada 25 epoch dan 50 epoch, dengan mAP50-95 berturut-turut 0,817 dan 0,829; kedua konfigurasi memakai 28,4 GFLOPS. YOLOv10s mencapai mAP50 0,977 pada 25 epoch dengan mAP50-95 0,646, dan 0,985 pada 50 epoch dengan mAP50-95 0,657; kedua konfigurasi memakai 24,5 GFLOPS. Penulis melaporkan bahwa YOLOv8s memiliki penempatan kotak pembatas dan skor kepercayaan yang lebih baik, serta mencapai nilai presisi 1 dari 1 pada 25 epoch, sedangkan YOLOv10s tidak mencapai nilai itu. YOLOv10s memiliki kebutuhan komputasi lebih rendah, tetapi penulis menyatakan tidak ada peningkatan presisi yang signifikan.

Penulis menyatakan bahwa hasil kedua model masih dapat ditingkatkan dengan menambah jumlah data dan epoch. Penulis juga menyatakan bahwa perbedaan hasil deteksi keduanya kecil dan YOLOv10s lebih efisien dalam GFLOPS serta jumlah parameter. Tinjauan pustaka dalam kajian ini mencatat bahwa YOLO pada umumnya memiliki kesulitan pada objek kecil dan lokalisasi presisi; pernyataan itu merujuk ke literatur lain, bukan hasil percobaan penulis. Selain itu, split uji, interval kepercayaan, dan uji signifikansi tidak dinyatakan, sehingga perbandingan ini hanya berdasarkan nilai metrik yang dilaporkan.

