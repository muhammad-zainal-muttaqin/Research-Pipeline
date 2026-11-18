# Integration of Hybrid GA-PSO-SA with Self-adaptive Dynamic Attention for Multi-objective CNN-based Oil Palm Fruit Ripeness Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `usman2026integration` |
| Judul asli | Integration of Hybrid GA-PSO-SA with Self-adaptive Dynamic Attention for Multi-objective CNN-based Oil Palm Fruit Ripeness Classification |
| Penulis | Usman, Usman; Arifin, Fatchul; Asnawi, Rustam |
| Tahun | 2026 |
| Venue | International Journal of Intelligent Engineering and Systems |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [usman2026integration.pdf](../pdf/usman2026integration.pdf)
- DOI resmi: https://doi.org/10.22266/ijies2026.0228.02

## Gambaran Umum

Kajian ini mengatasi penentuan waktu panen buah kelapa sawit. Cara pemeriksaan visual yang dipakai pemanen dilaporkan hanya mencapai akurasi 65-75% dan menyebabkan kehilangan hasil 15-20% setiap tahun. Tujuan kajian adalah membangun kerangka optimasi yang menggabungkan algoritma genetika (Genetic Algorithm, GA), optimasi kawanan partikel (Particle Swarm Optimization, PSO), dan annealing simulasi (Simulated Annealing, SA), serta mekanisme perhatian dinamis yang menyesuaikan diri (self-adaptive dynamic attention), untuk klasifikasi kematangan buah dengan jaringan saraf konvolusional (CNN) dan beberapa sasaran optimasi.

Data berupa citra buah kelapa sawit dalam empat kelas kematangan, yaitu Unripe, Underripe, Ripe, dan Overripe. Abstrak dan kartu data menyebut sekitar 10.000 citra dari lima lokasi perkebunan di Indonesia, dengan 7.000 citra hasil pengambilan di lapangan dan 3.000 citra dari repositori Roboflow. Citra diambil dengan kamera iPhone 15, Samsung Galaxy A56, dan Canon EOS 80D pada resolusi 1920 × 1080 sampai 4000 × 3000 piksel, dalam kondisi cahaya alami, mendung, dan buatan. Label divalidasi oleh tiga pakar pertanian dengan konsensus. Pembagian data memakai 8.000 citra latihan, 1.000 validasi, dan 1.000 uji dengan pemisahan lokasi: Situs 1-2 untuk latihan, Situs 3 untuk validasi, dan Situs 4-5 untuk uji. Citra diubah menjadi 224 × 224 piksel, dinormalisasi dengan statistik ImageNet, dan diperbanyak dengan RandomResizedCrop.

Model yang diusulkan memakai tulang punggung ResNet (ResNet18/34/50) yang dipadukan dengan modul perhatian dinamis berupa perhatian kanal dengan rasio reduksi 8, 16, atau 32, perhatian spasial kunci-nilai-kueri, fusi adaptif dengan bobot yang dipelajari, gerbang self-modulating, dan penyaringan ambang adaptif. Ruang pencarian mencakup sembilan sampai 16 hyperparameter. Proses optimasi mengejar tiga sasaran secara bersamaan, yaitu akurasi maksimum, latensi minimum, dan ukuran model minimum, dengan kurva Pareto dari NSGA-II. Pengaturan yang disebut antara lain ukuran populasi 20, delapan sampai sepuluh generasi, bobot inersia 0,7, faktor kognitif dan sosial 1,4, suhu awal 0,1, laju pendinginan 0,9, dan arsip Pareto berukuran 50.

Hasil utama pada abstrak serta Tabel 10-11 adalah akurasi 95,73% dan skor F1 95,84% untuk konfigurasi CNN+GA+PSO, dengan selisih presisi-recall 0,16%. Pengulangan sepuluh kali memberi akurasi uji rata-rata 96,12% ± 0,39%, selang kepercayaan 95% [95,85%, 96,39%], dan nilai tertinggi 96,86%. Model pembanding yang disebut adalah MobileNetV2 (95,53%), ResNet50 (95,27%), dan ViT-tiny (96,06%). Latensi model akhir 2,61 ms dengan ukuran 43,64 MB. Validasi silang Leave-Site-Out lima lipat memberi akurasi 94,66% ± 0,54%. Sumber yang sama memuat angka yang tidak konsisten: Tabel 8 mencatat akurasi solusi Pareto 86,86%-90,26%, dan Tabel 2 serta Tabel 3 menyebut 9.000 citra, bukan 10.000 seperti pada abstrak.

Penulis menyatakan bahwa penambahan komponen SA, CBAM, dan SADA menurunkan kinerja akibat kutukan dimensionalitas pada ruang pencarian sembilan hingga lebih dari 25 dimensi. Kelas Unripe paling sulit dibedakan, dengan presisi 66,49%-82,96% pada analisis Pareto, dan penulis menyinggung korelasi negatif antara Overripe dan Unripe karena kemiripan bentuk. Penulis mengusulkan penyelidikan lanjutan berupa fusi multi-modal dengan spektroskopi inframerah-dekat dan pencitraan termal, pembelajaran terfederasi, penalaran yang dapat dijelaskan, pemodelan video, dan pengujian aplikasi panen di lapangan.

