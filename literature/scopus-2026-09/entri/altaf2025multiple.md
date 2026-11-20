# Multiple object detection and tracking in autonomous vehicles: A survey on enhanced affinity computation and its multimodal applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `altaf2025multiple` |
| Judul asli | Multiple object detection and tracking in autonomous vehicles: A survey on enhanced affinity computation and its multimodal applications |
| Penulis | Altaf, Muhammad Adeel; Kim, Min Young |
| Tahun | 2025 |
| Venue | ICT Express |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [altaf2025multiple.pdf](../pdf/altaf2025multiple.pdf)
- DOI resmi: https://doi.org/10.1016/j.icte.2025.06.005

## Gambaran Umum

Kajian ini membahas pelacakan banyak objek tiga dimensi (*multi-object tracking*, MOT) untuk kendaraan otonom. Kamera kurang andal pada cahaya terik atau gelap, sedangkan LiDAR menghasilkan titik awan yang dapat terganggu partikel di udara dan kabut. Penulis mengusulkan ACMODT, kerangka deteksi dan pelacakan yang menggabungkan data kamera (2D) dan LiDAR (3D). Fokus utamanya adalah perhitungan afinitas, yaitu tingkat kemiripan antara objek pada satu *frame* dan objek pada *frame* berikutnya.

Evaluasi kuantitatif dilakukan pada benchmark pelacakan mobil KITTI. Dataset RADIATE dipakai hanya untuk visualisasi. Pengujian kecepatan dilakukan pada komputer dengan CPU Intel Core i7-8700K, RAM 32 GB, dan GPU NVIDIA TITAN RTX berkapasitas 24 GB. Implementasi memakai Python dan PyTorch. Deteksi memakai model EPNet terlatih sebagai *backbone* dengan fusi fitur 2D-3D untuk menghasilkan proposal. Jaringan korelasi dilatih selama 40 epoch dengan ukuran batch 4. Optimasi memakai AdamW dengan jadwal laju pembelajaran *cosine annealing* yang dimulai dari 0,0002. Asosiasi data memakai pendekatan berbasis *Gaussian mixture model* (GMM), yang parameternya disetel lalu dibandingkan dengan pendekatan berbasis MIP.

Metode utama terdiri atas dua modul afinitas. Pertama, RBCF (*Refined Boost Correlation Features*) menilai jarak spasial dan kesamaan arah antarframe untuk memperkuat identifikasi ulang objek. Kedua, 3D-XGIoU memperluas IoU standar dengan orientasi kotak pembatas, kesesuaian rasio aspek, dan penalti volume. *Kalman filter* dipakai untuk memperhalus prediksi gerak. Pada KITTI, ACMODT mencapai MOTA 88,56%, MOTP 89,61%, MODA 88,73%, dan MODP 90,18%, dengan 589 false positive. Sebagai pembanding, BcMODT mencapai MOTA 86,53%, MODA 86,66%, dan 1.248 false positive. JMODT mencapai MOTA 86,27%, JRMOT 85,70%, mmMOT 84,77%, dan AB3DMOT 83,92%. Jumlah false positive ACMODT adalah yang terendah di antara metode dalam tabel, yaitu lebih rendah dari mmMOT (711), JRMOT (772), JMODT (772), dan AB3DMOT (978). Penulis juga menyatakan pengurangan ID-SW dan peningkatan presisi serta akurasi dibanding metode terdahulu.

Penulis menyatakan beberapa batasan. Pertama, nilai pembanding pada tabel diambil dari hasil yang dilaporkan pada studi terdahulu dan dari papan peringkat publik KITTI, bukan dari eksperimen ulang pada kondisi yang sama. Akibatnya, perbandingan bergantung pada protokol masing-masing sumber. Kedua, evaluasi kuantitatif hanya mencakup kelas mobil pada KITTI. RADIATE hanya dipakai untuk visualisasi hasil, sehingga kinerja pada data tersebut tidak diukur secara kuantitatif. Ketiga, sistem ini bergantung pada pasangan kamera dan LiDAR yang terkalibrasi dan tersinkronisasi, serta pada detektor EPNet terlatih.
