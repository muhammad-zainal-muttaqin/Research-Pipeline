# Deep Learning Method with Domain-Task Adaptation and Client-Specific Fine-Tuning YOLO11 Model for Counting Greenhouse Tomatoes

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `glukhikh2025deep` |
| Judul asli | Deep Learning Method with Domain-Task Adaptation and Client-Specific Fine-Tuning YOLO11 Model for Counting Greenhouse Tomatoes |
| Penulis | Glukhikh, Igor; Glukhikh, Dmitry; Gubina, Anna; Chernysheva, Tatiana |
| Tahun | 2025 |
| Venue | Applied System Innovation |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [glukhikh2025deep.pdf](../pdf/glukhikh2025deep.pdf)
- DOI resmi: https://doi.org/10.3390/asi8030071

## Gambaran Umum

Kajian ini mengatasi penilaian operasional volume tomat di rumah kaca. Penerapan sistem visi komputer berskala besar memerlukan cara yang mengurangi biaya, waktu, dan kerumitan, terutama dalam menyiapkan data latih dan model. Model YOLO yang tersedia umumnya belum mencapai akurasi yang dibutuhkan untuk tugas spesifik. Tujuannya adalah membangun metode pelatihan berurutan yang terdiri atas Domain-Task Adaptation dan Client-Specific Fine-Tuning, disertai algoritme penghitungan tomat yang tampak pada baris depan dari citra video.

Tanaman yang dikaji adalah tomat. Penelitian memakai YOLO11n dari Ultralytics, varian terkecil dengan 2,6 juta parameter dan 6,5 miliar FLOPs pada masukan 640 × 640. Tiga himpunan data dipakai berurutan. Himpunan adaptasi berasal dari 895 citra beranotasi di Kaggle yang ditambah foto tanaman tomat pada kompleks agrobio-teknologi Universitas Tyumen, sehingga total 1.300 citra dengan oklusi minimal dan pencahayaan seragam. Himpunan latih kustom berisi 500 citra beranotasi dari sebuah rumah kaca di Siberia Barat, dengan oklusi, derau, vegetasi lebat, dan banyak objek berukuran kecil. Himpunan uji kustom berisi 50 citra dari lokasi yang sama dengan karakteristik serupa. Citra tidak diproses sebelum dianotasi.

Kerangka kerja terdiri atas enam tahap, yaitu model pralatih, adaptasi pada himpunan khusus, analisis kondisi dan kebutuhan pengguna, fine-tuning pada data kustom, evaluasi pada data uji kustom, dan penerapan. Arsitektur YOLO11n tidak diubah. Untuk menghitung buah, model mendeteksi semua tomat, lalu k-means membagi lebar kotak pembatas menjadi dua klaster, yaitu latar depan baris yang sedang diamati dan latar belakang, berdasarkan asumsi bahwa buah baris depan memiliki kotak rata-rata lebih besar. Aturan heuristik ditambahkan dengan memasukkan objek di tepi citra berukuran terbesar ke himpunan awal deteksi depan sebelum pengklasteran. Metrik deteksi memakai mAP@50, mAP@75, mAP@50:95, presisi, dan recall; metrik penghitungan memakai MAE, MAPE, RMSE, dan R².

Pada himpunan uji kustom 50 citra, model pralatih YOLO11n.pt menghasilkan mAP@50 0,0219, presisi 0,0435, dan recall 0,0009. Setelah adaptasi, Task-Adaptation.pt mencapai mAP@50 0,5781, presisi 0,6857, dan recall 0,4889. Setelah fine-tuning, Client-Specific.pt mencapai mAP@50 0,8384, mAP@75 0,6383, mAP@50:95 0,5542, presisi 0,7974, dan recall 0,7530. Relatif terhadap model hasil adaptasi, fine-tuning menaikkan mAP@50 sebesar 45,0%, mAP@75 127,6%, mAP@50:95 85,8%, presisi 16,3%, dan recall 54,0%. Validasi silang lima lipat pada 500 citra kustom menghasilkan mAP@50 0,8, presisi 0,8, dan recall 0,71. Untuk penghitungan, k-means saja memberi MAE 0,74, MAPE 12,28%, RMSE 0,73, dan R² 0,89; penambahan aturan heuristik menurunkan MAE menjadi 0,36 dan MAPE menjadi 5,60%, RMSE 0,72, serta R² 0,98. Kecepatan inferensi pada GPU GTX 1650 adalah 22–30 ms per citra atau 33–45 FPS, sedangkan pada CPU i5-11400H 100–150 ms per citra atau 6,5–10 FPS.

Penulis tidak memuat bagian batasan tersendiri. Dalam pembahasan dinyatakan bahwa kajian memakai model siap pakai tanpa mengubah arsitektur YOLO11, sehingga perbaikan lebih lanjut masih memungkinkan melalui perubahan arsitektur, dan bahwa varian YOLO11 yang lebih besar umumnya meningkatkan mutu deteksi. Penulis juga menyatakan hasil penghitungan berlaku pada kondisi rumah kaca yang diamati dan berencana mengembangkan algoritme untuk mendeteksi buah tidak layak, mengklasifikasikan tingkat kematangan, serta mengidentifikasi penyakit buah.

