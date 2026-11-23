# Yield Quantification of Morus Serrata Fruit Stages Using YOLOv8-Based Identification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `carandang2025yield` |
| Judul asli | Yield Quantification of Morus Serrata Fruit Stages Using YOLOv8-Based Identification |
| Penulis | Carandang, Mark Jason C.; Yang, Jerome; Manlises, Cyrel O. |
| Tahun | 2025 |
| Venue | Computer Systems and Technologies 26th International Conference Compsystech 2025 Proceedings |
| Kode | C4 (Atribut kelas dan pencacahan) |

## Tautan Akses
- PDF: [carandang2025yield.pdf](../pdf/carandang2025yield.pdf)
- DOI resmi: https://doi.org/10.1109/compsystech65493.2025.11137042

## Gambaran Umum

Kajian ini bertujuan mendeteksi dan menghitung buah murbei *Morus serrata* pada empat tahap: berbunga, belum matang, matang, dan terlalu matang. Penulis menyebut penilaian kematangan secara tradisional memakan tenaga dan waktu, dan belum ada kajian murbei yang memakai penglihatan komputer untuk kuantifikasi hasil. Sistem dipasang pada Jetson Nano.

Data berupa citra sendiri yang diambil di Filipina dengan kamera SONY IMX477 pada jarak maksimum 2,5 m, berlatar tirai hitam buram dan cahaya pagi, hanya sisi depan tajuk pohon. Set data memuat 3.500 citra. Jumlah anotasi disebut berbeda di beberapa tempat (15.711; 16.427 dengan 12.710 untuk latih). Anotasi dibuat peneliti dan sampel dikonfirmasi pakar murbei. Citra 1920 × 1920 diperbesar ke 3200 × 3200 lalu dipotong menjadi 25 petak 640 × 640 (*tiling*). Pembagian latih dan validasi atau uji 70:30, dilatih 300 *epoch* pada RTX 3060.

Metodenya YOLOv8n (detektor objek satu tahap) yang mengklasifikasikan setiap buah ke empat kelas. Jumlah per kelas dijadikan persentase komposisi hasil per pohon. Hasil dibandingkan dengan hitung tangan lewat galat absolut rerata (*mean absolute error*, MAE) dan koefisien korelasi pada 20 uji selama 32 hari.

Skor F1 model 72,2 (berbunga 71,3; belum matang 74,1; matang 68,1; terlalu matang 76,3). Korelasi keseluruhan antara hasil prediksi dan hasil nyata 86,69%. Per tahap, berbunga MAE 6,36 dan korelasi 98,08%; belum matang 11,83 dan 79,44%; matang 9,99 dan 87,58%; terlalu matang 0,39 dan 77,24%. Kesalahan klasifikasi terbanyak terjadi antara tahap matang dan belum matang.

Keterbatasan yang dapat diperiksa: MAE dan korelasi dihitung pada persentase komposisi per tahap, bukan jumlah buah mutlak. Hanya satu citra sisi depan per pohon, tanpa penggabungan pandang. Latar dikendalikan dengan tirai. Pembagian per pohon tidak disebut, jumlah pohon dan jumlah uji pohon unik tidak disebut, dan angka anotasi tidak konsisten. Kajian menyebut batas daya Jetson Nano.
