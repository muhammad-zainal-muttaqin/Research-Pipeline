# Test-Time Adaptation of a Multi-Class Object Localization and Size Estimation Framework for Smart Agriculture Applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2025test` |
| Judul asli | Test-Time Adaptation of a Multi-Class Object Localization and Size Estimation Framework for Smart Agriculture Applications |
| Penulis | Liu, Zixu; Wu, Qinhao; Chai, Yuan; Yu, Huan |
| Tahun | 2025 |
| Venue | Cognitive Computation |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [liu2025test.pdf](../pdf/liu2025test.pdf)
- DOI resmi: https://doi.org/10.1007/s12559-025-10488-0

## Gambaran Umum

Makalah ini mengusulkan cara memperbarui model pendeteksi objek saat uji, tanpa melatih ulang model. Kerangka yang dipakai memprediksi posisi, jumlah, dan ukuran objek dari satu citra dengan metode regresi heatmap. Penulis menargetkan aplikasi pertanian pintar dan kondisi open set recognition (OSR), yaitu kondisi ketika citra uji memuat kelas yang tidak ada saat pelatihan. Menurut abstrak, pendekatan ini memberi prediksi akurat pada setting OSR "within a single epoch of test-time optimization without altering the training process". Menurut pendahuluan, adaptasi ini bersifat tanpa sumber data (source-free) dan merupakan yang pertama untuk tugas regresi heatmap.

Bukti utama berasal dari dataset E-MOCSE13 buatan penulis. Dataset ini berisi 390 citra sintetis berukuran 512×512 piksel dengan 13 kelas. Tiga kelas, yaitu banana, tomato, dan garlic, dipakai sebagai kelas out-of-distribution (OoD) dan tidak muncul saat pelatihan. Menurut Tabel 1 makalah, E-MOCSE13 adalah satu-satunya dataset multi-kelas dalam perbandingan yang dapat diperluas, dapat dipakai untuk OSR, dan memberi anotasi penghitungan serta ukuran sekaligus. Dataset ini juga memuat citra nyata, tetapi evaluasi utama bertumpu pada data sintetis.

Metrik utamanya adalah RMSE untuk jumlah (RMSEcount), jarak posisi (RMSEdistance), dan ukuran (RMSEsize). Pada Tabel 4 makalah, RMSEcount turun dari 5,48 pada backbone asli menjadi 3,29 pada TTA-ft dengan learning rate 1e-2 dan Statistics Calibration nonaktif. RMSEdistance turun dari 10,30 menjadi 6,00 pada learning rate 5e-3 dengan kalibrasi nonaktif. RMSEsize sekitar 0,51 dan tidak berubah berarti. Angka-angka ini dibandingkan dalam satu tabel pada data yang sama.

Penilaian dilakukan pada benchmark buatan penulis dengan metrik RMSE, bukan mAP atau metrik deteksi standar. Karena itu angkanya tidak dapat langsung dibandingkan dengan hasil deteksi pada data kebun. Penulis sendiri menawarkan benchmark ini sebagai bahan uji untuk penelitian lanjutan.
