# Classification of Tomato Harvest Timing Using an AI Camera and Analysis Based on Experimental Results

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `okabe2025classification` |
| Judul asli | Classification of Tomato Harvest Timing Using an AI Camera and Analysis Based on Experimental Results |
| Penulis | Okabe, Yasuhiro; Hiraguri, Takefumi; Endo, Keita; Kimura, Tomotaka; Hayashi, Daisuke |
| Tahun | 2025 |
| Venue | Agriengineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [okabe2025classification.pdf](../pdf/okabe2025classification.pdf)
- DOI resmi: https://doi.org/10.3390/agriengineering7020048

## Gambaran Umum

Penelitian ini bertujuan memprediksi hasil panen tomat hingga satu minggu ke
depan agar petani dapat merencanakan pengiriman dan biaya. Permasalahan yang
diangkat adalah kekurangan tenaga kerja dan perlunya penentuan ukuran panen
serta kematangan yang tidak dipengaruhi pencahayaan rumah kaca. Penulis
menetapkan tiga syarat: prediksi hingga satu minggu, identifikasi ukuran yang
tepat untuk dipanen, dan diskriminasi warna kematangan yang bergantung pada
lingkungan tetapi tidak bergantung pada intensitas cahaya.

Sistem yang dikembangkan adalah kamera pengenal berbasis YOLO untuk mendeteksi
tomat per buah, dilengkapi kamera kedalaman dan LiDAR untuk mengukur ukuran
dari data awan titik, serta analisis hue untuk menilai kematangan. Percobaan
lapang dilakukan di Ama-gun, Prefektur Aichi, Jepang, pada tomat varietas
“Karen” di rumah kaca. Kamera dipasang pada kereta panen dan mengirim data
melalui Wi-Fi ke cloud untuk dianalisis. Untuk deteksi, penulis mengumpulkan
1166 citra lapang dan memberi anotasi dengan labelImg; 315 citra dijadikan
data uji (sekitar 30%) dan sisanya data latih, dengan 100 epoch dan ukuran
batch 32. Pengukuran ukuran memakai vektor normal awan titik untuk menemukan
tepi buah dan jarak Euclidean antartitik tepi; volume dihitung dengan
mengintegralkan luas penampang awan titik setengah permukaan lalu menggandakannya.

Mekanisme penghitungan dan asosiasi ditangani dengan pelacakan agar buah yang
sama tidak terhitung dua kali, dan ambang pada kotak pembatas kecil dipakai
untuk mengecualikan tomat dari barisan belakang. Kematangan diklasifikasikan
dari nilai hue dalam ruang warna HSV karena hue relatif kebal terhadap
perubahan intensitas cahaya dibanding RGB. Penulis menetapkan sepuluh rentang
ambang warna, dari merah (0–6) hingga hijau (46–60). Pengujian lapang
mencakup empat barisan panjang masing-masing sekitar 90 m dengan sekitar 100
tanaman, direkam dengan kecepatan tetap sekitar 0,5 m/s. Acuan akurasi adalah
jumlah tomat yang benar-benar dipanen di lapang.

Hasil utama meliputi tingkat kebenaran deteksi 99% dan tingkat deteksi 88%
dari jumlah tomat dalam video; mAP50 meningkat selama pelatihan. Pengukuran
dengan pencocokan template memberi galat 8,00% untuk tinggi dan 8,57% untuk
lebar, sedangkan pengukuran volume awan titik memberi galat 4,96%, 9,24%, dan
25,98% untuk tiga buah contoh. Diskriminasi hue stabil pada dua kondisi
pencahayaan: merah bernilai 3 (gelap) dan 0 (terang), jingga 11 pada keduanya,
serta hijau 31 (gelap) dan 30 (terang). Perbandingan hasil analisis dengan
panen aktual memberi galat rata-rata 6,85% (per baris 0%, 7,14%, 7,41%, dan
11,40%). Untuk prediksi satu minggu, penjumlahan kategori “kuning hijau hingga
jingga” dan “kuning hijau” memberi galat 8,43–22,02%; setelah sekitar 4%
kategori “hijau muda hingga kuning hijau” ditambahkan, galat turun menjadi
0,60–1,27%.

Batasan yang dinyatakan penulis mencakup percobaan yang hanya dilakukan pada
satu peternakan dan pada musim dingin, sehingga kriteria panen untuk musim
panas perlu disesuaikan karena pematangan berlangsung lebih cepat. Prediksi
juga belum memasukkan pengaruh suhu dan cahaya satu minggu ke depan. Penulis
menyatakan ukuran dan volume belum berhasil diterapkan dalam prosedur pemanenan
dan pengiriman petani, serta masih diperlukan peningkatan akurasi.

