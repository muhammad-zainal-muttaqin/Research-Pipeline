# Detection and Counting of Small Target Apples under Complicated Environments by Using Improved YOLOv7-tiny

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ma2023detection` |
| Judul asli | Detection and Counting of Small Target Apples under Complicated Environments by Using Improved YOLOv7-tiny |
| Penulis | Ma, Li; Zhao, Liya; Wang, Zixuan; Zhang, Jian; Chen, Guifen |
| Tahun | 2023 |
| Venue | Agronomy |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [ma2023detection.pdf](../pdf/ma2023detection.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy13051419

## Gambaran Umum

Kajian ini bertujuan mendeteksi dan menghitung apel berukuran kecil pada kebun dengan latar kompleks dan cuaca berubah, untuk mendukung estimasi produksi dan pemanenan otomatis. Gangguan yang diangkat meliputi pencahayaan yang berubah, bayangan buah dan daun, serta buah kecil di kejauhan yang mirip latar belakang. Penulis mengusulkan model ringan berbasis YOLOv7-tiny yang dapat dipasang pada perangkat seluler.

Data berasal dari himpunan publik MinneApple, yang dikumpulkan di Horticultural Research Center Universitas Minnesota antara Juni 2015 dan September 2016 menggunakan ponsel Samsung Galaxy S4. Penulis memotong dan memberi label pada citra menjadi tiga kelas, yaitu GreenApple, Red1Apple, dan Red2Apple, dengan jumlah masing-masing 302, 252, dan 287 citra hasil potongan beresolusi 320 × 320 atau 410 × 410 dari citra awal 1280 × 720. Anotasi dibuat dengan makesense.ai dalam format VOC lalu diubah ke format YOLO. Untuk mensimulasikan cuaca kabut dan hujan, setiap kelas diberi augmentation pada 80 citra memakai fungsi iaa.Fog() dan iaa.Rain(speed = (0,1, 0,3)). Himpunan akhir memuat 829 citra, terdiri atas 232 citra kabut dan 236 citra hujan. Pembagian acak 7:2:1 menghasilkan 586 citra latih, 164 citra uji, dan 66 citra validasi.

Mekanisme model mencakup tiga perubahan pada YOLOv7-tiny. Pertama, sambungan lintas (skip connection) ditambahkan pada bagian P3 dari backbone dengan mengadaptasi gagasan DenseNet untuk menyatukan fitur dangkal dan mengurangi hilangnya ciri sasaran kecil, dengan dua lapisan sambungan agar kecepatan tidak turun. Kedua, PANet pada leher diganti P2BiFPN: lapisan deteksi sasaran kecil P2 ditambahkan, kepala deteksi P5 dihapus, fitur P5 digabungkan dengan P4, lalu kepala deteksi P4 menjadi keluaran, sehingga fusi dwiarah mempertahankan informasi sasaran kecil. Ketiga, mekanisme perhatian ringan ULSAM dimasukkan pada leher untuk membuang fitur berlebih tanpa menambah ukuran model. Pelatihan memakai citra 416 × 416, 300 epoch, laju belajar 0,01, momentum 0,937, weight decay 0,0005, dan optimizer Adam pada Ubuntu 18.04.6, PyTorch, Intel Core i7-11700k, serta GPU GTX 1080Ti dengan CUDA 10.2. Penghitungan buah dinilai dengan MAE dan RMSE; deteksi dinilai dengan presisi, recall, mF1, dan mAP@0,5.

Hasil utama adalah mAP 80,4%, presisi 80,1%, recall 74,1%, mF1 76,8%, ukuran model 5,06 MB, dan kecepatan 101,01 fps pada himpunan uji. Nilai mAP ini 5,5% lebih tinggi daripada YOLOv7-tiny awal yang mencapai 74,9%; abstrak menyebut ukuran model turun 15,81%. Untuk penghitungan, model menghasilkan MAE 2,737 dan RMSE 4,220, masing-masing 5,69% dan 8,97% lebih rendah daripada model awal yang mencatat 2,902 dan 4,636. Studi ablasi menunjukkan sambungan lintas, P2BiFPN, dan ULSAM masing-masing menaikkan mAP sebesar 3,6%, 3,8%, dan 2,9% terhadap jaringan dasar. Dalam perbandingan model, YOLOv7-tiny-Apple memiliki mAP tertinggi, 2% di atas YOLOv5s, dengan jumlah parameter paling kecil.

Batasan yang dinyatakan penulis adalah sebagian apel hijau kecil di kejauhan masih terlewat pada citra hujan dan kabut karena kesamaan dengan latar, penutupan daun, dan resolusi rendah. Kecepatan model juga lebih rendah daripada YOLOv7-tiny awal dan YOLOv5s. Penulis mengarahkan pekerjaan berikutnya pada optimasi ringan, peningkatan akurasi, dan penerapan pada perangkat seluler.
