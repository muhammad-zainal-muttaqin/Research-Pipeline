# Mask-GK: An efficient method based on mask Gaussian kernel for segmentation and counting of grape berries in field

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2025mask` |
| Judul asli | Mask-GK: An efficient method based on mask Gaussian kernel for segmentation and counting of grape berries in field |
| Penulis | Yang, Canchen; Geng, Tianyu; Peng, Jian; Xu, Chun; Song, Zichen |
| Tahun | 2025 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [yang2025mask.pdf](../pdf/yang2025mask.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2025.110286

## Gambaran Umum

Kajian ini membahas segmentasi dan pencacahan buah anggur di kebun terbuka. Buah anggur kecil, jumlahnya banyak, dan letaknya rapat. Warnanya sering mirip dengan latar belakang daun dan batang. Kondisi ini menyulitkan metode segmentasi instans yang umum, seperti Mask R-CNN. Metode itu perlu mendeteksi setiap objek satu per satu sebelum menyegmentasinya, sehingga akurasinya turun dan beban komputasinya besar pada kerapatan tinggi. Selain itu, belum ada tolok ukur publik untuk segmentasi buah anggur di lapangan. Penulis berangkat dari dua hal ini. Tujuan mereka adalah mengusulkan metode yang mampu menyegmentasi dan mencacah seluruh buah secara paralel dari satu citra.

Data yang digunakan adalah tanaman anggur di kebun wilayah Longquanyi dan Shuangliu, Chengdu, Sichuan, Tiongkok, yang difoto pada Juli 2023. Penulis mengambil citra menggunakan ponsel iPhone 12, iPhone 13, dan HUAWEI Mate 40 Pro. Mereka membuat kumpulan data bernama *Sichuan Grape Berry Instance Segmentation and Counting Dataset* (GBISC). Kumpulan ini berisi 150 citra RGB beresolusi tinggi dari tiga varietas, yaitu Kyoho, Shine Muscat, dan Summer Black. Seluruh citra diambil dari arah depan dengan jarak yang kurang lebih sama terhadap tanaman. Total 50.718 buah diberi anotasi segmentasi instans dalam format COCO. Citra berukuran 4032 × 3024 dan 4096 × 3072 piksel diubah menjadi 2048 × 1536 piksel saat pelatihan dan pengujian. Pembagiannya adalah 100 citra untuk latih, 25 citra untuk validasi, dan 25 citra untuk uji.

Metode yang diusulkan bernama Mask-GK. Metode ini membangkitkan peta probabilitas dengan *mask Gaussian kernel* dari anotasi mask setiap buah. Jaringan saraf dilatih menggunakan peta tersebut, lalu algoritma *watershed* diterapkan pada peta prediksi untuk memisahkan setiap buah. Pada data uji, Mask-GK mencatat MAE 9,40 dan RMSE 12,28 untuk pencacahan. Hasil ini lebih baik daripada metode segmentasi instans lain yang dibandingkan. Metode pembanding terbaik, CondInst, berada di bawah Mask-GK. Untuk segmentasi, pada data uji seluruh ukuran buah Mask-GK mencatat AP (0,5:0,95) sebesar 0,664, AP (0,5) sebesar 0,907, AR (0,5:0,95) sebesar 0,684, dan F1-Score sebesar 0,674. Penulis juga menyatakan bahwa penambahan informasi bentuk buah pada kernel Gaussian meningkatkan akurasi pencacahan. Nilai AP pada abstrak, yaitu 0,665, sedikit berbeda dengan 0,664 pada bagian hasil. Perbedaan ini ditemukan di dalam teks sumber.

Penulis menyebutkan beberapa batasan. Pertama, metode ini bekerja baik untuk objek kecil yang maskernya utuh. Pada objek yang lebih besar dan maskernya tidak kontinu atau tidak lengkap, metode ini kurang efektif. Kedua, kumpulan data hanya berisi citra yang diambil saat cahaya cukup. Citra saat senja atau malam tidak tercakup. Ketiga, pelatihan memerlukan anotasi segmentasi instans yang mahal dan memakan banyak tenaga kerja. Penulis menilai hal ini menjadi tantangan untuk penelitian lanjutan dan perluasan metode.
