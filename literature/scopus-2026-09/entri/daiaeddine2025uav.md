# UAV imagery, advanced deep learning, and YOLOv7 object detection model in enhancing citrus yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `daiaeddine2025uav` |
| Judul asli | UAV imagery, advanced deep learning, and YOLOv7 object detection model in enhancing citrus yield estimation |
| Penulis | Daiaeddine, Mohamed Jibril; Badrouss, Sara; El Harti, Abderrazak; Bachaoui, El Mostafa; Biniz, Mohamed; Mouncif, Hicham |
| Tahun | 2025 |
| Venue | Foods and Raw Materials |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [daiaeddine2025uav.pdf](../pdf/daiaeddine2025uav.pdf)
- DOI resmi: https://doi.org/10.21603/2308-4057-2025-2-650

## Gambaran Umum

Kajian ini membangun detektor jeruk berbasis YOLOv7 yang dimodifikasi untuk citra UAV (drone) RGB, lalu menghitung buah per pohon. Tujuannya adalah mengganti penghitungan manual di lapangan dengan penghitungan otomatis dari citra udara. Sumber teks menyebut akuisisi memakai Phantom 4 Multispectral, tetapi hanya kanal RGB yang dipakai.

Hasil utama: rata-rata akurasi penghitungan per pohon 87,68% pada 20 pohon, dengan nilai tertinggi 94% dan terendah 74%. Model menghasilkan jumlah yang lebih rendah daripada jumlah sebenarnya pada sebagian pohon. Regresi antara hitungan model (x) dan hitungan manual (y) adalah y = 1,10·x + 3,27. Kajian ini tentang jeruk, bukan kelapa sawit.

Penghitungan buah jeruk di kebun dilakukan manual dan memakan waktu. Teks kajian menyebut penghitungan manual mengumpulkan jumlah buah dari beberapa sudut pandang. Metode itu bergantung pada pengamat, sehingga galatnya sulit dikendalikan. Kajian ini menawarkan pendekatan citra udara untuk mengurangi beban kerja lapangan.

Detektor objek dilatih untuk mengenali buah jeruk pada citra UAV RGB. Jumlah kotak deteksi per pohon dianggap sebagai hitungan buah. Gagasan ini termasuk penghitungan dari satu sudut pandang per pohon, dengan dua sisi pohon difoto dan keduanya dihitung. Teks tidak menjelaskan cara menghubungkan buah yang terlihat dari dua sisi, sehingga buah yang sama bisa terhitung dua kali.

Citra dipotong menjadi sub-citra berukuran 400x433 piksel. Teks menyebut 1.804 sub-citra beranotasi, dibagi 70/20/10 untuk latih, validasi, dan uji. Angka validasi berbeda antara teks (130) dan Tabel 2 (180). Total 1.804 cocok dengan 1.263 + 361 + 180 pada teks, tetapi tabel memuat 1.419 + 361 + 130 = 1.910, sehingga pembagian ini tidak konsisten.

Modifikasi YOLOv7 mencakup blok konvolusi ganda (double CBS, Conv-BN-SELU-Conv-BN-SiLU) dan fungsi aktivasi SELU. Hyperparameter dicari dengan YOLO Evolve, dan model memakai transfer learning. Rincian lengkap arsitektur ada di bagian metode teks.

Pada data uji, model mencapai tingkat deteksi benar (true positive) 96%, menurut teks. Presisi dan recall dihitung per citra, dan rasio presisi penghitungan adalah jumlah terdeteksi dibagi jumlah sebenarnya dikali 100. Hasil per pohon untuk 20 pohon berkisar 74% sampai 94%, dengan rata-rata 87,68%. Hasil ini adalah rasio penghitungan, bukan mAP, sehingga tidak sebanding dengan metrik deteksi di tinjauan lain.

Kelebihan kajian ini adalah protokol penghitungan per pohon yang jelas dan perbandingan langsung dengan hitungan manual. Keterbatasannya: penghitungan manual memakai banyak sudut, sedangkan algoritma memakai dua sisi, sehingga kedua cara tidak setara. Teks tidak menyebut penghubungan buah lintas sisi. Dari sisi rekayasa, pembagian data yang tidak konsisten (130 atau 180) menyulitkan pengulangan.
