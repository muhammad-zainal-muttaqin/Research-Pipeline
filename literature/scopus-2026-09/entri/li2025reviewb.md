# A Review of Optical-Based Three-Dimensional Reconstruction and Multi-Source Fusion for Plant Phenotyping

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2025reviewb` |
| Judul asli | A Review of Optical-Based Three-Dimensional Reconstruction and Multi-Source Fusion for Plant Phenotyping |
| Penulis | Li, Songhang; Cui, Zepu; Yang, Jiahang; Wang, Bin |
| Tahun | 2025 |
| Venue | Sensors |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [li2025reviewb.pdf](../pdf/li2025reviewb.pdf)
- DOI resmi: https://doi.org/10.3390/s25113401

## Gambaran Umum

Tinjauan ini mengkaji rekonstruksi tiga dimensi (3D) berbasis optik untuk fenotiping tanaman. Masalah utamanya adalah geometri dan tekstur tanaman yang kompleks, sehingga analisis citra dua dimensi (2D) tidak memadai untuk pemodelan yang akurat. Rekonstruksi 3D diperlukan untuk pemantauan pertumbuhan, deteksi hama dan penyakit, serta pengembangan peralatan pertanian cerdas. Penulis menyusun literatur sekitar sepuluh tahun terakhir dan membagi metode menjadi tiga paradigma: visi aktif, visi pasif, dan rekonstruksi berbasis pembelajaran mendalam (*deep learning*).

Metode yang ditinjau mencakup cahaya terstruktur (*structured light*), waktu tempuh (*time-of-flight*/ToF), pemindaian laser, visi stereo, *structure from motion* (SfM), *neural radiance fields* (NeRF), jaringan saraf konvolusional (CNN), dan *3D Gaussian splatting* (3DGS). Mekanisme pengambilan kedalaman berbeda tiap metode: cahaya terstruktur memakai triangulasi optik dari deformasi pola garis, ToF menghitung jarak dari waktu tempuh pulang-pergi cahaya dengan rumus d = ct/2, pemindaian laser mengukur waktu atau pergeseran fase pantulan, visi stereo memakai perbedaan posisi titik (paralaks) antardua kamera, dan SfM merekonstruksi lintasan kamera lewat pencocokan titik fitur serta *bundle adjustment*. NeRF memodelkan warna dan kerapatan volume tiap titik 3D dengan *multilayer perceptron* (MLP) dan rendering volume terdiferensial; CNN mengekstrak fitur bertingkat untuk menutup bagian yang tertutup; 3DGS merepresentasikan adegan dengan distribusi Gauss yang dioptimalkan lewat rasterisasi terdiferensial.

Penulis juga mengulas fusi multi-sumber pada tiga lapis, yaitu data, fitur, dan keputusan, serta penggabungan model fisik tanaman dan pencitraan dinamis. Fusi citra RGB dan kedalaman mengatasi oklusi, pencocokan hasil deteksi beberapa sensor menurunkan positif dan negatif palsu, dan *cross-view clustering* dipakai untuk membuang buah kapas ganda lintas pandang. Sejumlah angka dilaporkan dari kajian yang ditinjau: pengukuran apel memberi R² = 0,97, RMSE = 0,755 mm, dan MAPE = 7,23% untuk indeks deformasi, dengan RMSE volume 6,015 cm³ dan diameter maksimum 1,823 mm; lokalisasi jagung berbasis ToF memberi deviasi rata-rata 3,4 cm dengan simpangan baku ±1,3 cm; inventarisasi pohon dengan LiDAR memberi tingkat penemuan (*recall*) 98,1% dengan RMSE diameter setinggi dada 1,93 cm.

Untuk tanaman lain, visi stereo pada gandum mencapai akurasi segmentasi 99,8% dan RMSE tinggi kanopi 0,016 m dengan RMSE indeks luas daun 0,37; metode SfM-Instant-NGP pada kedelai memangkas waktu rekonstruksi menjadi 2,82 menit (turun 90,7% terhadap MVS dan 99,4% terhadap NeRF) dengan PSNR 24,47 dB dan MSE 0,15; NeRF pada sayur memberi RMSE titik-ke-titik 0,128–0,395 cm serta R² tinggi tanaman 0,971 dan diameter batang 0,907; rekonstruksi kapas dengan 3DGS memberi MAPE jumlah buah 9,23% terhadap acuan LiDAR, dengan YOLOv11x mengungguli SAM sebesar 5,9% dalam skor F1 untuk topeng instansi (*instance mask*).

Batasan yang dinyatakan penulis meliputi biaya sensor khusus yang tinggi, kebutuhan komputasi besar untuk model pembelajaran mendalam, dan minimnya sumber pelatihan bagi praktisi pertanian. Fusi sensor menuntut kalibrasi serta registrasi waktu dan ruang yang tepat, disertai pembobotan data yang andal. NeRF membutuhkan sumber daya komputasi besar dan waktu pemrosesan lama serta sulit diterapkan pada adegan dinamis berskala besar; 3DGS memakai memori dan penyimpanan besar, kurang kompatibel dengan alur *rendering* yang ada, dan hanya mendukung adegan statis; pemindaian laser mahal serta terganggu oleh permukaan transparan atau sangat reflektif; visi stereo peka terhadap kalibrasi, oklusi, dan tekstur berulang. Penulis menyatakan tidak ada konflik kepentingan; pendanaan berasal dari proyek platform *digital twin* proses produksi pertanian.
