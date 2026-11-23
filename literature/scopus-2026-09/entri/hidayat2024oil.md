# Oil Palm Fruit Ripeness Detection Technique: Analysis, Challenges, and Opportunities

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hidayat2024oil` |
| Judul asli | Oil Palm Fruit Ripeness Detection Technique: Analysis, Challenges, and Opportunities |
| Penulis | Hidayat, Teddy; Suhardi; Faizal, Ahmad; Albarda; Ramsari, Nopi |
| Tahun | 2024 |
| Venue | 2024 International Conference on Information Technology Systems and Innovation Icitsi 2024 Proceedings |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [hidayat2024oil.pdf](../pdf/hidayat2024oil.pdf)
- DOI resmi: https://doi.org/10.1109/icitsi65188.2024.10929459

## Gambaran Umum

Tinjauan ini merangkum pendekatan berbasis komputer untuk mendeteksi kematangan buah kelapa sawit. Penulis menyebut penilaian manual oleh pekerja lapangan memakan waktu dan bersifat subjektif, sehingga diperlukan teknologi yang lebih objektif. Tinjauan membahas sensor (kamera RGB, *near-infrared* atau NIR, sensor induktif) dan algoritme pembelajaran mesin (KNN, regresi, SVM, jaringan saraf).

Cakupan: 19 artikel penelitian dari Elsevier, IEEE, dan basis data akademik lain. Periode terbit tidak disebut. Kata kunci pencarian, string kueri, kriteria inklusi dan eksklusi, serta jumlah rekaman sebelum penyaringan tidak disebut. Artikel dianalisis menurut tiga aspek: sensor, algoritme, dan akurasi. Artikel dikelompokkan menurut lokasi deteksi: tandan yang sudah dipanen untuk penyortiran, tandan di pohon, dan laboratorium.

Isi rangkuman: kamera RGB paling sering dipakai, diikuti spektroskopi NIR. CNN mencakup 40% algoritme dan jaringan saraf tiruan 20% (Gambar 1). Metode klasik berbasis warna (K-Means, KNN) umumnya di bawah 90%. EfficientNetB0 mencapai akurasi uji 0,898. Model multi-masukan (RGB, inframerah, sel beban) pada 1.575 citra dari 14 varietas mencapai akurasi 90,26%. Untuk deteksi di pohon, sensor induktif mencapai akurasi 100% pada 55 tandan dan YOLOv4 mencapai mAP50 99%. NIR dengan jaringan saraf tiruan mencapai 95%, dan RGB-CNN 91% (Gambar 2).

Tantangan yang disebut: pencahayaan tidak merata, tandan tertutup cabang atau daun, tandan bertumpuk, kebutuhan set data lebih besar dan beragam, serta sensitivitas NIR terhadap sinar matahari, kelembapan, dan suhu di luar ruangan. Usulan penulis: wahana tanpa awak (UAV) dan sensor multispektral. Berdasarkan wawancara dengan penyelia di Sumatera, pohon tua mencapai tinggi 25 sampai 30 meter.

Keterbatasan yang dapat diperiksa: protokol pencarian tidak dilaporkan sehingga tinjauan tidak dapat diulang. Tidak ada penilaian mutu studi. Angka akurasi dari studi berbeda dengan data, jumlah sampel, dan metrik berbeda ditampilkan berdampingan, dan sebagian dari tinjauan ini adalah studi laboratorium NIR (termasuk buah macaw). Pencacahan buah tidak dibahas.
