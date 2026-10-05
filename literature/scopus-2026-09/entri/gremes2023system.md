# System of Counting Green Oranges Directly from Trees Using Artificial Intelligence

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gremes2023system` |
| Judul asli | System of Counting Green Oranges Directly from Trees Using Artificial Intelligence |
| Penulis | Gremes, Matheus Felipe; Fermo, Igor Rossi; Krummenauer, Rafael; Flores, Franklin C\'esar; Andrade, Cid Marcos Gon\ccalves; Lima, Oswaldo Curty da Motta |
| Tahun | 2023 |
| Venue | Agriengineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [gremes2023system.pdf](../pdf/gremes2023system.pdf)
- DOI resmi: https://doi.org/10.3390/agriengineering5040111

## Gambaran Umum
Makalah ini mengusulkan sistem pencacahan jeruk hijau prapanen langsung dari pohon memakai video yang direkam sepanjang baris pohon. Sistem menggabungkan detektor YOLOv4 dengan pelacakan ID berbasis jarak centroid dan pelacak objek (*object tracker*) untuk mengurangi penghitungan ganda. Keunggulan yang diklaim penulis adalah kemampuan membedakan buah hijau dari daun yang berwarna hijau serupa.

Data berupa video telepon pintar (Xiaomi Redmi Note 9PRO) pada jeruk varietas "folha murcha" (tipe Valencia) di perkebunan di Brasil, direkam pada 15 Maret 2021 dan 18 April 2021. Dataset citra berisi 644 citra dengan 43.109 anotasi jeruk. Detektor YOLOv4 mencapai mAP50 80,16%, mAP50:95 53,83%, presisi 0,92, recall 0,93, F1 0,93, dan rerata IoU 82,08% pada 112 citra uji. Pada video uji 10 detik (600 bingkai) dengan hitungan acuan 208 jeruk, sistem dengan YOLOv4 dan pelacak Dlib menghitung 204 jeruk.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi produksi sebelum panen bermanfaat untuk manajemen spesifik lokasi, perkiraan kapasitas penyimpanan, dan pengurangan biaya tenaga kerja. Penulis menyebut tiga tantangan pada pencacahan buah prapanen: oklusi (oleh dedaunan dan antarbuah), ukuran objek yang kecil, dan latar belakang kompleks. Jeruk hijau mudah tertukar dengan dedaunan sehingga lebih sulit daripada jeruk matang.

Menghitung dari jumlah deteksi per citra dinilai keliru pada kondisi oklusi dan pencahayaan yang tidak terkendali. Pada video, jeruk yang sama terdeteksi pada banyak bingkai sehingga perlu pencocokan antarbingkai; bila tidak, jeruk yang tertutup lalu terdeteksi lagi akan dihitung dua kali atau lebih. Penulis menyatakan bahwa kebanyakan studi terdahulu menghitung dari citra atau menghitung jeruk matang, dan hanya sedikit yang memakai deteksi dan pelacakan pada buah kehijauan.

## Ide Utama
Setiap jeruk terdeteksi diberi ID unik, dan ID dijaga antarbingkai dengan dua cara: pencocokan jarak Euclid antarcentroid pada bingkai berurutan, dan pelacak objek yang meneruskan posisi jeruk pada bingkai ketika YOLOv4 tidak mendeteksinya. Jeruk yang sempat tertutup dapat memperoleh ID lamanya kembali bila terdeteksi lagi di dekat posisi yang dilacak, sehingga tidak dihitung ganda.

## Cara Kerja Langkah demi Langkah

### 1. Pembuatan dataset
Data direkam pada 1920 × 1080 piksel dan 60 bingkai per detik, dalam orientasi potret dan lanskap, sambil operator berjalan lurus sejajar baris jeruk. Pengambilan data dilakukan 7 dan 6 bulan sebelum panen. Citra dataset diambil dari bingkai video setiap 3 detik. Anotasi memakai CVAT dengan tiga kelas: jeruk hijau, jeruk matang, dan jeruk busuk. Total 644 citra dengan 43.109 anotasi, terdiri dari 42.710 jeruk hijau, 368 jeruk busuk, dan 31 jeruk matang. Sebanyak 532 citra untuk pelatihan dan 112 citra untuk uji.

### 2. Pelatihan YOLOv4
Pelatihan memakai Darknet di Google Colab dengan GPU Tesla P100 16 GB. Tiga lapisan terakhir disesuaikan untuk tiga kelas. Ukuran masukan jaringan 1056 × 1056 piksel, dipilih agar jeruk tidak mengecil di bawah 11 × 11 piksel. Augmentasi dan hiperparameter dibiarkan pada nilai bawaan, dan jumlah iterasi maksimum 6.000 (jumlah kelas × 2.000). Model kemudian dikonversi ke TensorFlow.

### 3. Pelacakan ID berdasarkan centroid
Empat langkah: (1) menghitung centroid kotak; (2) menghitung jarak Euclid antara centroid bingkai sebelumnya dan bingkai sekarang; (3) mengaitkan pasangan dengan jarak terkecil, kecuali bila jarak lebih dari 70 piksel dari semua objek yang belum berpasangan; (4) memberi ID baru pada objek yang tidak berpasangan bila keyakinan deteksinya 85% atau lebih. Asumsi utamanya adalah objek bergeser sedikit antarbingkai berurutan.

### 4. Pelacak objek
Bila ID bingkai sebelumnya tidak dapat dikaitkan dengan deteksi YOLOv4 pada bingkai sekarang, pelacak objek memperkirakan posisi jeruk dari bingkai sebelumnya. Enam pelacak dibandingkan: Dlib correlation tracker, Boosting, MIL, MedianFlow, KCF, dan CSRT. Pelacakan berlangsung hingga 35 bingkai; bila YOLOv4 tidak mendeteksi jeruk itu lagi dalam rentang itu, ID dihapus dan pelacakan dihentikan.

## Eksperimen dan Hasil
Video uji berdurasi 10 detik (600 bingkai) dan tidak dipakai pada dataset. Penulis menghitung 208 jeruk yang terlihat pada video itu sebagai hitungan benar. Sebagai pembanding, detektor optimal disimulasikan dengan menganotasi manual semua jeruk pada 600 bingkai, sehingga tidak ada deteksi terlewat maupun salah.

Kinerja deteksi YOLOv4 (Tabel 1, 112 citra uji; presisi, recall, dan F1 pada IoU 50%):

| Model | mAP50 | mAP50:95 | Presisi | Recall | F1 | Rerata IoU |
|---|---|---|---|---|---|---|
| YOLOv4 | 80,16% | 53,83% | 0,92 | 0,93 | 0,93 | 82,08% |

Pencacahan dengan detektor optimal simulasi (Tabel 2; hitungan benar 208; deteksi terlewat dan salah 0 pada semua baris):

| Pelacak | Hitungan ganda | ID berulang | Jeruk terhitung |
|---|---|---|---|
| Tanpa pelacak | 10 | 2 | 216 |
| Dlib | 8 | 0 | 216 |
| Boosting | 7 | 0 | 215 |
| CSRT | 8 | 1 | 215 |
| KCF | 10 | 0 | 218 |
| MedianFlow | 8 | 0 | 216 |
| MIL | 9 | 0 | 217 |

Pencacahan dengan YOLOv4 (Tabel 3; hitungan benar 208; deteksi terlewat 15 dan deteksi salah 2 pada semua baris):

| Pelacak | Hitungan ganda | ID berulang | Jeruk terhitung |
|---|---|---|---|
| Tanpa pelacak | 25 | 5 | 215 |
| Dlib | 10 | 1 | 204 |
| Boosting | 10 | 1 | 204 |
| CSRT | 10 | 1 | 204 |
| KCF | 16 | 1 | 210 |
| MedianFlow | 10 | 1 | 204 |
| MIL | 9 | 1 | 203 |

Penulis menjelaskan "deteksi terlewat" sebagai jeruk yang tidak terdeteksi sekali pun pada seluruh bingkai, bukan jumlah bingkai yang gagal. Hitungan dengan YOLOv4 lebih dekat ke nilai benar daripada hitungan dengan detektor optimal, karena galat negatif akibat deteksi terlewat saling mengimbangi galat positif akibat hitungan ganda. Perbedaan antarpelacak tidak signifikan menurut penulis, karena pelacak hanya aktif maksimum 35 bingkai pada video 60 fps yang antarbingkainya hampir tidak berubah. Pelacak tanpa penggunaan pada kedua kondisi menghasilkan hitungan ganda dan ID berulang lebih banyak. Tiga contoh kualitatif (Gambar 10 sampai 12) menunjukkan hitungan ganda terjadi ketika jeruk tertutup dedaunan atau jeruk lain lebih lama daripada 35 bingkai: ID lama dihapus sehingga deteksi ulang memperoleh ID baru (misalnya ID 84 menjadi 124, ID 11 menjadi 102, ID 99 menjadi 133). Contoh keberhasilan (Gambar 9) menunjukkan ID 13 dan 91 dipulihkan setelah oklusi oleh ranting.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: dataset jeruk hijau prapanen yang dapat dipakai kembali (sebagian tersedia di repositori GitHub penulis); penggabungan deteksi dan pelacakan mengurangi hitungan ganda; dan hasilnya mendekati hitungan benar pada video uji.

Penulis tidak memuat bagian keterbatasan yang terpisah, tetapi mengamati bahwa hitungan ganda tetap muncul ketika oklusi berlangsung lebih dari 35 bingkai.

Menurut pembacaan ringkasan ini, evaluasi pencacahan hanya memakai satu video 10 detik dengan 208 jeruk, sehingga tidak ada ukuran variasi atau uji pada banyak baris pohon. Kedekatan 204 terhadap 208 sebagian merupakan hasil saling meniadakan antara galat negatif dan positif (15 jeruk terlewat dan 10 hitungan ganda), sehingga tidak berarti identitas setiap jeruk benar. Hitungan acuan mencakup jeruk yang terlihat pada video, bukan jumlah jeruk sebenarnya pada pohon atau hasil panen, dan tidak ada nilai kesalahan relatif yang dilaporkan penulis. Pelacakan hanya mengandalkan jarak centroid dan bukan ciri tampilan, dengan asumsi gerakan antarbingkai kecil.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dengan pelacakan: ID per jeruk dikaitkan antarbingkai melalui jarak centroid dan pelacak objek, dengan masa pelacakan maksimum 35 bingkai tanpa deteksi. Mekanisme ini tidak menangani buah yang sama dari sisi pohon berbeda; video merekam satu sisi baris. Hitungan tidak dilaporkan per kelas pada pencacahan: dataset memuat tiga kelas (hijau, matang, busuk), tetapi hitungan video tidak dirinci per kelas dan 99,1% anotasi (42.710 dari 43.109, dihitung dari angka dalam makalah) adalah jeruk hijau. Acuan hitungnya adalah hitungan manual jeruk yang terlihat pada video 10 detik (208), bukan panen.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pola pelacak ID dua tingkat (pencocokan centroid dengan ambang jarak dan keyakinan, ditambah pelacak untuk bingkai tanpa deteksi) serta pembedaan jenis galat (hitungan ganda, ID berulang, deteksi terlewat). Keterbatasan yang relevan: ID hilang setelah oklusi panjang sehingga tidak ada pemulihan identitas lintas pandang, dan metrik hitungan tidak per kelas.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `gremes2023system`.

Gremes dkk. (2023) membangun sistem pencacahan jeruk hijau prapanen dari video baris pohon dengan YOLOv4 (mAP50 80,16%) yang digabung dengan pelacakan ID berbasis jarak centroid dan pelacak objek. Pada satu video 10 detik dengan 208 jeruk terlihat, sistem menghitung 204 jeruk dengan Dlib, CSRT, Boosting, atau MedianFlow; tanpa pelacak hitungan ganda meningkat dari 10 menjadi 25. Dataset yang dihasilkan berisi 644 citra dengan 43.109 anotasi jeruk.

Catatan verifikasi data: metrik deteksi dari Tabel 1; hitungan pelacakan dari Tabel 2 dan Tabel 3; jumlah anotasi per kelas dari Bagian 2.1; parameter pelacakan (70 piksel, 85%, 35 bingkai) dari Bagian 2.3 dan 2.4. Persentase 99,1% pada Kaitan dengan Tinjauan adalah hasil bagi sederhana yang dihitung dari 42.710 dan 43.109. Kerapatan pohon, jumlah pohon yang direkam, dan jumlah video total tidak dilaporkan. Teks ekstraksi terbaca dengan baik; label kolom tabel ditulis berurutan satu per baris, dan susunan baris-kolom disimpulkan dari urutan serta konsisten dengan teks (misalnya 204 vs 208 pada ringkasan).
