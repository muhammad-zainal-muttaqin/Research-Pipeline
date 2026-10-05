# Robust Counting of Soft Fruit Through Occlusions with Re-identification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kirk2021robust` |
| Judul asli | Robust Counting of Soft Fruit Through Occlusions with Re-identification |
| Penulis | Kirk, Raymond; Mangan, Michael; Cielniak, Grzegorz |
| Tahun | 2021 |
| Venue | Lecture Notes in Computer Science Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [kirk2021robust.pdf](../pdf/kirk2021robust.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-030-87156-7_17

## Gambaran Umum
Makalah ini mengusulkan sistem pelacakan multi-objek dan multi-kelas (*multi-object tracking*, MOT) untuk mencacah buah stroberi dari urutan citra yang diambil robot bergerak. Sistem memperluas kerangka DeepSORT dengan jaringan identifikasi ulang (*re-identification*, re-ID) yang memiliki dua kepala: satu untuk identitas objek dan satu untuk klasifikasi tingkat kematangan (bunga, mentah, matang). Keluaran kedua kepala dipakai untuk menjaga konsistensi lintasan dan menekan positif palsu antartingkat kematangan.

Data berupa empat urutan citra stroberi (varietas Driscoll's Amesti dan Katrina) dari terowongan plastik di kebun penelitian Riseholme, University of Lincoln, Inggris, yang direkam kamera RGBD Intel RealSense D435i pada robot Thorvald. Evaluasi dilakukan pada satu urutan yang tidak dipakai untuk pelatihan (Amesti-1, 500 bingkai).

Hasil utama: galat deviasi absolut terkecil (*L1 loss*) untuk semua kelas turun dari 41 pada baseline menjadi 7 pada sistem gabungan. Abstrak menyebut *mean average percentage error* (MAPE) 3% dibandingkan 21% pada baseline.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pencacahan buah penting bagi keputusan panen, tenaga kerja, dan estimasi hasil; penulis menyebut tenaga kerja mencakup 65% dari total biaya panen. Pelacak berbasis deteksi (*detect-to-track*) harus membedakan buah yang hampir identik, menghadapi perubahan penampilan, iluminasi, dan sudut pandang, serta mengidentifikasi ulang buah setelah hilang akibat oklusi.

Pendekatan terdahulu umumnya memperlakukan buah sebagai satu kelas. Penulis menelaah apakah informasi tingkat kematangan dan odometri robot dapat memperkuat pelacakan.

## Ide Utama
Ide utamanya adalah memperkaya biaya asosiasi pelacak dengan tiga sumber informasi: gerak (jarak Mahalanobis dari filter Kalman), penampilan (vektor re-ID), dan deskripsi kelas (probabilitas label kematangan dari kepala klasifikasi). Posisi robot di sepanjang baris tanaman dari odometri dimasukkan ke ruang keadaan filter Kalman. Augmentasi masukan (menjaga rasio aspek dan menambah konteks sekitar kotak) mempertajam pembedaan identitas.

Hitungan total diperoleh dari jumlah identitas lintasan unik. Kepala klasifikasi menjadikan vektor fitur lebih terpisah menurut kelas, dan ini divisualisasikan dengan analisis komponen utama (*principal component analysis*, PCA).

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data
Urutan citra dikumpulkan dari dua terowongan plastik berukuran 8x24 m, masing-masing berisi 5 baris di atas meja dengan jarak 1,5 m. Baris tengah dipakai untuk data Amesti dan Katrina, diambil berselang satu hari pada akhir musim (September). Kamera diatur setinggi kantong tanah stroberi, direkam pada 7 Hz dengan kecepatan robot 0,1 m/s (Amesti-1, Katrina-1, Katrina-2) dan 0,2 m/s (Amesti-2), pada resolusi 1920x1080. Teks menulis satuan "0.1ms", yang diinterpretasikan di sini sebagai kecepatan robot sesuai konteks. Anotasi manual oleh ahli memakai tiga kelas: matang (>85% tertutup warna merah), bunga (kelopak putih tanpa kaliks), dan mentah (kaliks hijau tampak). Setiap urutan dihentikan pada 500 bingkai. Sisi kiri dan kanan baris disebut sisi 1 dan 2.

Jumlah anotasi kotak untuk Amesti-1, Amesti-2, Katrina-1, dan Katrina-2 berturut-turut 12.219, 4.895, 15.850, dan 14.507, dengan 233, 172, 299, dan 326 lintasan (hitungan). Pembagian data: pelatihan memakai Katrina-1, Katrina-2, dan Amesti-2; pengujian memakai Amesti-1; set pelatihan dibagi lagi 75% dan 25% untuk pelatihan dan validasi jaringan re-ID.

### 2. Pelacakan dan asosiasi
Formulasi mengikuti SORT dengan filter Kalman kecepatan tetap. Keadaan berdimensi 10: (u, v, γ, h, r) dan kecepatannya, dengan r posisi robot sepanjang baris. Tidak ada informasi gerak ego dan kamera tidak dikalibrasi. Asosiasi diselesaikan dengan algoritma Hungarian. Jarak Mahalanobis kuadrat dibatasi pada ambang chi-kuadrat 95% sebesar 11,07 (10 derajat kebebasan). Jarak penampilan berupa jarak kosinus terkecil terhadap galeri 100 pengamatan terakhir tiap lintasan. Jarak kelas dihitung dari probabilitas label terhadap galeri pengamatan kelas sebelumnya. Matriks biaya menggabungkan ketiganya dengan bobot λ, dan ambang gerbang dipakai tiap metrik. Kaskade pencocokan DeepSORT dipakai dengan matriks biaya baru.

### 3. Jaringan re-ID dan deskripsi kelas
Jaringan berbasis blok ResNet menerima potongan 64x64 dari kotak deteksi dan menghasilkan vektor 128 dimensi pada hipersfer satuan. Total parameter terlatih 825.152. Kepala re-ID memakai *Cosine Softmax*, kepala klasifikasi memakai *cross entropy* untuk tiga tingkat kematangan. Pelatihan memakai batch 128, 6.400 iterasi, laju belajar awal 0,1 yang dikurangi sepuluh kali pada 80% dan 90% iterasi. Satu proses maju (batch 128) memerlukan 412 µs per kotak pada GPU (ditulis "Nvidia GeForce GTX 3090"), dengan kapasitas lebih dari 2.400 kotak per detik.

### 4. Augmentasi
Dua transformasi: *square* (kotak dijadikan persegi untuk menjaga rasio aspek) dan *pad* (kotak diperluas p piksel untuk memasukkan konteks sekitar).

## Eksperimen dan Hasil
Metrik adalah deviasi absolut terkecil (L1 loss) antara hitungan sebenarnya dan hitungan taksiran per bingkai selama 500 bingkai pada Amesti-1; kelas tertentu dievaluasi dengan hanya menghitung buah kelas itu. Baseline ialah pelacak DeepSORT yang bersifat agnostik kelas. Akurasi re-ID saat pelatihan 97% untuk baseline dan Sub-Net, serta lebih dari 99% untuk eksperimen lain.

Tabel 1 makalah (L1 loss, dengan hitungan taksiran/hitungan sebenarnya di dalam kurung):

| Eksperimen | Agnostik | Bunga | Matang | Mentah |
|---|---|---|---|---|
| Baseline | 41 (192/233) | 1 (23/24) | 19 (69/50) | 59 (100/159) |
| Square | 57 (176/233) | 2 (26/24) | 3 (53/50) | 62 (97/159) |
| Sub-Net (kepala klasifikasi) | 31 (202/233) | 1 (25/24) | 3 (53/50) | 35 (124/159) |
| Pad-8 | 33 (266/233) | 14 (38/24) | 29 (79/50) | 10 (149/159) |
| Pad-16 | 86 (319/233) | 13 (37/24) | 36 (86/50) | 37 (196/159) |
| Pad-32 | 25 (258/233) | 3 (27/24) | 12 (62/50) | 10 (169/159) |
| Pad-64 | 8 (241/233) | 3 (27/24) | 4 (54/50) | 1 (160/159) |
| Gabungan | 7 (240/233) | 2 (26/24) | 2 (52/50) | 3 (162/159) |

Pada sistem gabungan, hitungan total taksiran 240 terhadap 233 sebenarnya, dan hitungan per kelas berselisih 2, 2, dan 3. Baseline menghitung terlalu rendah pada total (192 dari 233). Beberapa varian padding menghitung berlebih (misalnya Pad-16 menghasilkan 319).

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: sistem mempertahankan konsistensi lintasan lewat oklusi dan pada kluster padat, memakai kamera murah, serta cukup cepat untuk pelacakan daring. Penulis juga membagikan empat urutan stroberi berlabel tangan sebagai tolok ukur.

Keterbatasan yang dinyatakan penulis: kerja lanjutan mencakup evaluasi lebih lanjut, studi ablasi dengan isyarat tambahan, jaringan ekstraksi fitur lain, dan perluasan ke ruang 3D dengan data kedalaman atau SfM.

Menurut pembacaan ringkasan ini, evaluasi akhir hanya memakai satu urutan uji (Amesti-1) dengan satu varietas pada sisi yang sama dengan latar kebun terowongan, sehingga ketahanan umum belum teruji. Kenaikan akurasi juga bergantung pada pemilihan konfigurasi (hasil Pad-8 hingga Pad-64 sangat bervariasi), yang dipilih berdasarkan hasil pada urutan yang sama sebagai evaluasi, sehingga risiko penyetelan pada set uji tidak dapat disingkirkan dari teks. Buah dihitung dari satu sisi baris pada tiap urutan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai berurutan dengan pelacakan berbasis deteksi, fitur re-ID, probabilitas kelas, dan filter Kalman, ditambah odometri robot. Penulis menyebut sistem mampu menghitung "dari banyak sudut pandang", tetapi dalam percobaan tiap sisi baris direkam sebagai urutan terpisah, dan penggabungan hitungan antar-sisi tidak dievaluasi. Hitungan dilaporkan per kelas (bunga, matang, mentah) maupun agnostik kelas. Acuan hitungnya berupa lintasan yang dilabel manual pada urutan citra (anotasi citra), bukan hitungan lapangan atau panen.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: penggunaan probabilitas kelas sebagai bagian biaya asosiasi, pelatihan kepala klasifikasi bersama re-ID agar vektor lebih terpisah menurut kelas, dan evaluasi per kelas. Perlu dicatat bahwa pelacak mengandalkan keterurutan bingkai dan odometri satu arah, sedangkan pencocokan sisi pohon sawit tidak berurutan sehingga asosiasi gerak tidak langsung berlaku.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `kirk2021robust`.

Kirk dkk. (2021) mengusulkan pencacahan stroberi melalui pelacakan dengan re-ID dan probabilitas kelas kematangan di atas kerangka DeepSORT, ditambah odometri robot pada filter Kalman. Pada urutan uji Amesti-1 (500 bingkai), L1 loss untuk semua kelas turun dari 41 pada baseline menjadi 7, dengan hitungan taksiran 240 terhadap 233 sebenarnya.

Catatan verifikasi data: angka L1 loss dan hitungan per kelas tertulis pada Tabel 1; MAPE 3% dan 21% hanya tertulis pada Abstrak, tanpa tabel pendukung dalam teks. Jumlah anotasi dan lintasan tertulis pada Bagian 3.3. Kecepatan robot tertulis "0.1ms" dan "0.2ms" dalam teks (kemungkinan m/s); GPU tertulis "GTX 3090". Ekstraksi teks Tabel 1 terbaca baik. Pembagian "75% ke 25%" pada Bagian 3.3 tidak sepenuhnya sesuai dengan jumlah urutan (tiga urutan untuk pelatihan, satu untuk uji) dan tidak dapat dikonfirmasi lebih lanjut dari teks.
