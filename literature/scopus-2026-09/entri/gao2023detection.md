# Detection and counting of overlapped apples based on convolutional neural networks

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gao2023detection` |
| Judul asli | Detection and counting of overlapped apples based on convolutional neural networks |
| Penulis | Gao, Mengyuan; Ma, Shunagbao; Zhang, Yapeng; Xue, Yong |
| Tahun | 2023 |
| Venue | Journal of Intelligent and Fuzzy Systems |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [gao2023detection.pdf](../pdf/gao2023detection.pdf)
- DOI resmi: https://doi.org/10.3233/jifs-213072

## Gambaran Umum

Kajian ini mengusulkan detektor buah berbasis *Mask R-CNN*, arsitektur segmentasi instans (pemisahan setiap objek dalam citra) yang semula memakai ResNet-101 sebagai *backbone* (jaringan ekstraksi fitur). Penulis mengganti *backbone* dengan GhostNet, jaringan ringan yang membangkitkan sebagian peta fitur melalui operasi murah bernama *ghost module*. Modul *Spatial Pyramid Pooling* (SPP), yang menggabungkan fitur pada beberapa skala, ditambahkan di antara *backbone* dan *Region Proposal Network* (RPN), yaitu bagian yang mengusulkan area kandidat objek. Masalah yang diangkat adalah besarnya model dan lambatnya inferensi (prediksi pada data baru).

Data berasal dari 500 citra berukuran 512 × 512 piksel menurut abstrak. Augmentasi berupa derau Gaussian, pemotongan, rotasi, dan perubahan kecerahan menghasilkan 40.000 frame menurut abstrak. Pembagian data tidak konsisten: Tabel 1 menyebut 400 citra latih dan 100 citra uji, sedangkan Bagian 2.1.2 menyebut 400 latih, 50 uji, dan 50 validasi. Jumlah instans juga tercatat dengan dua pembagian berbeda (2.484, 892, dan 627 pada satu bagian; 580, 186, dan 208 pada bagian lain), sehingga pembagian pasti belum dapat dipastikan.

Pada Tabel 2, GhostNet-SPP mencatat presisi 91,67%, recall 97,82%, dan mAP 91,68%. Modelnya memiliki sekitar 2,2 × 10^7 parameter, ukuran 86,23 MB, dan kecepatan 10 frame per detik. Pembanding ResNet-101 memiliki 6,40 × 10^7 parameter, ukuran 245,5 MB, kecepatan 5 frame per detik, dan mAP 90,45%. Selisih parameter antara keduanya sekitar 65,6%, sedangkan abstrak menulis pengurangan 90,90%. Kesimpulan menulis kecepatan 9 frame per detik, berbeda dengan 10 frame per detik pada Tabel 2. Bagian 3.2 dan Kesimpulan menulis kenaikan mAP sebesar 8,148% (Bagian 3.2) dan 8,147% (Kesimpulan), dengan dua angka lain yang juga berbeda antarbagian (45,587% dan 45,487%). Angka pembanding untuk kenaikan itu tidak dipetakan jelas dalam bagian yang dibaca, sehingga belum dapat diperiksa terhadap Tabel 2.

Untuk video, penulis memakai DeepSORT, algoritma pelacakan multi-objek, agar buah yang sama tidak dihitung ulang antarframe. Mekanisme ini dijelaskan di Bagian 3.4 dan hasilnya ditampilkan secara kualitatif (Fig. 10). Teks tidak melaporkan akurasi hitungan per video, galat hitungan, atau perbandingan dengan jumlah buah sebenarnya. Klaim efisiensi model didukung tabel perbandingan, sedangkan klaim pencegahan hitung ganda hanya didukung ilustrasi.
