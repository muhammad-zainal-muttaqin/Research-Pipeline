# Simple online and realtime tracking with a deep association metric

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wojke2017simple` |
| Judul asli | Simple online and realtime tracking with a deep association metric |
| Penulis | Wojke, Nicolai; Bewley, Alex; Paulus, Dietrich |
| Tahun | 2017 |
| Venue | Proceedings International Conference on Image Processing Icip |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [wojke2017simple.pdf](../pdf/wojke2017simple.pdf)
- DOI resmi: https://doi.org/10.1109/icip.2017.8296962

## Gambaran Umum

Kajian ini memperkenalkan perluasan *Simple Online and Realtime Tracking* (SORT), sebuah metode pelacakan banyak objek secara daring dan waktu nyata. SORT dikenal sederhana dan cepat, tetapi sering menghasilkan banyak pergantian identitas. Penyebabnya, metrik asosiasi yang dipakai SORT hanya akurat saat ketidakpastian estimasi keadaan rendah. Hal ini membuat pelacakan melewati oklusi menjadi lemah. Penulis menambahkan informasi tampilan (*appearance*) ke dalam asosiasi, dengan tujuan mempertahankan identitas objek saat terhalang atau tidak terdeteksi, tanpa mengorbankan kemudahan implementasi dan kecepatan.

Evaluasi memakai benchmark MOT16, yang terdiri atas tujuh urutan video uji. Urutan tersebut mencakup adegan tampak depan dengan kamera bergerak serta pengawasan dari atas. Masukan deteksi berasal dari Faster RCNN yang dilatih oleh Yu dkk. pada kumpulan data publik dan privat, dengan ambang nilai kepercayaan 0,3. Kamera tidak dikalibrasi dan tidak tersedia informasi gerak kamera. Ekstraktor fitur tampilan dilatih secara *offline* pada kumpulan data re-identifikasi pejalan kaki yang berisi lebih dari 1.100.000 citra dari 1.261 pejalan kaki. Parameter lain ditentukan pada urutan latih yang disediakan benchmark. Waktu komputasi diukur pada GPU Nvidia GeForce GTX 1050 mobile.

Metode ini mempertahankan filter Kalman dengan model gerak kecepatan konstan pada ruang keadaan delapan dimensi. Asosiasi dilakukan frame demi frame dengan algoritma Hungarian. Metrik gerak Mahalanobis digabung dengan metrik tampilan, dan ambang Mahalanobis ditetapkan 9,4877. Lintasan dihapus setelah 30 frame tanpa asosiasi (Amax = 30). Jaringan tampilan memiliki 2.800.864 parameter dan menghasilkan fitur berdimensi 128. Satu kali proses terhadap 32 kotak pembatas memerlukan sekitar 30 ms. Hasilnya, jumlah pergantian identitas turun dari 1.423 pada SORT menjadi 781, penurunan sekitar 45 persen. Fragmentasi lintasan naik sedikit, sedangkan jumlah objek yang sebagian besar terlacak naik dan jumlah objek yang sebagian besar hilang turun. Metode ini menghasilkan pergantian identitas paling sedikit di antara metode daring yang dibandingkan, dengan nilai MOTA yang tetap kompetitif. Kecepatan implementasi sekitar 20 Hz, dan sekitar separuh waktunya dipakai untuk pembentukan fitur.

Penulis mencatat beberapa batasan. Nilai MOTA terutama terdampak oleh jumlah *false positive* yang besar. Penulis menduga sebagian besar *false positive* berasal dari respons detektor pada geometri statis di adegan. Karena batas usia lintasan maksimum cukup besar, respons tersebut sering tergabung ke lintasan objek. Penulis menilai ambang kepercayaan yang lebih tinggi berpotensi meningkatkan kinerja secara signifikan, tetapi hal itu tidak diuji. Fragmentasi lintasan juga sedikit meningkat akibat upaya mempertahankan identitas melewati oklusi dan deteksi yang hilang. Detail prosedur pelatihan jaringan tampilan berada di luar cakupan makalah. Kinerja waktu nyata bergantung pada ketersediaan GPU modern.
