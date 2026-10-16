# Automatic pear and apple detection by videos using deep learning and a Kalman filter

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `itakura2021automatic` |
| Judul asli | Automatic pear and apple detection by videos using deep learning and a Kalman filter |
| Penulis | Itakura, Kenta; Narita, Yuma; Noaki, Shuhei; Hosoi, Fumiki |
| Tahun | 2021 |
| Venue | OSA Continuum |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple, pear |

## Tautan Akses
- PDF: [itakura2021automatic.pdf](../pdf/itakura2021automatic.pdf)
- DOI resmi: https://doi.org/10.1364/osac.424583

## Gambaran Umum
Makalah ini (OSA Continuum 4(5), 2021) menghitung buah pir dan apel secara otomatis dari video yang direkam sambil berjalan di bawah kanopi. Buah dideteksi pada setiap bingkai dengan jaringan YOLO v2, kemudian buah yang sama pada bingkai berurutan diidentifikasi dengan filter Kalman (*Kalman filter*, penaksir keadaan linear waktu diskret yang memprediksi posisi objek pada bingkai berikutnya) sehingga tidak dihitung ganda. Video diambil dengan iPhone X pada resolusi 1920×1080 piksel dan 30 fps.

Pada video uji pir yang memuat 234 buah, metode ini mendeteksi 231 buah dan 226 di antaranya terhitung benar (*precision* 0,978, *recall* 0,966, F1 0,972). Presisi rerata (*average precision*, AP) deteksi pir 0,97 dan apel 0,97. Pada apel, 157 dari 170 buah terhitung benar (F1 0,929). Penulis menyatakan galat mutlak penghitungan berada di bawah 10%.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi jumlah buah yang tepat berguna untuk perkiraan hasil dan kematangan, perencanaan wisata petik, evaluasi kerusakan akibat bencana, dan sistem pengenalan untuk robot pertanian. Penghitungan dari video memerlukan dua langkah, yaitu deteksi dan pelacakan buah pada urutan bingkai. Pelacakan sulit karena posisi dan tampilan buah berubah akibat faktor lingkungan seperti pencahayaan.

Penulis menyatakan bahwa hanya sedikit metode deteksi dan pelacakan buah untuk penghitungan yang dilaporkan untuk buah kehijauan dan cahaya tidak stabil di bawah kanopi. Bila deteksi gagal karena buah tertutup daun atau ranting dan buah tidak dilacak, buah itu akan terhitung dua kali ketika terdeteksi lagi pada bingkai berikutnya.

## Ide Utama
Deteksi per bingkai dengan detektor YOLO berukuran masukan besar dan augmentasi warna dipadukan dengan filter Kalman yang memprediksi posisi buah. Dengan prediksi itu, jalur buah tetap dipertahankan walaupun deteksi gagal pada beberapa bingkai akibat oklusi atau perubahan cahaya, sehingga buah yang sama tidak dihitung dua kali dan buah yang sempat hilang tidak kehilangan identitasnya.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Video pir direkam di Hatsuseien, Kota Matsudo, Prefektur Chiba, Jepang, pada 20 Agustus dengan kultivar Kosui, Hosui, Kaori, dan Niitaka; tinggi pohon sekitar 1,5 m dan buah berada di bawah kanopi. Video apel direkam di Nagano Fruits Production, Kota Nagano, pada 23 September dengan kultivar Fuji, Shinano Sweet, dan Akibae. Perekaman dilakukan sambil berjalan dengan iPhone X, 1920×1080 piksel, 30 fps. Jumlah pohon tidak dilaporkan.

### 2. Anotasi dan pembagian data
Buah dilabeli manual dengan kotak pembatas memakai aplikasi Video Labeler di MATLAB 2020b: 6.341 pir pada 1.077 citra dan 7.494 apel pada 526 citra (angka itu mencakup buah yang sama pada bingkai berbeda). Bingkai dibagi acak menjadi latih, validasi, dan uji dengan rasio 8:1:1 pada tiap kumpulan data. Penghitungan dievaluasi pada video yang tidak dipakai sebagai data latih maupun uji detektor.

### 3. Deteksi dengan YOLO v2
YOLO v2 praterlatih dengan ukuran masukan 608×608 piksel dipakai. Pembanding adalah YOLO v2 berbackbone ResNet-18 dengan masukan 224×224, YOLO v3, dan *single-shot detector* (SSD). Augmentasi mencakup pembalikan horizontal (peluang 50%), perubahan rona, saturasi, dan nilai pada HSV acak sebesar −20% sampai +20%, dan rotasi 30° dengan koreksi kotak. Hiperparameter: laju belajar awal 1×10⁻², momentum 0,9, regularisasi L2 1×10⁻⁴, ukuran *minibatch* 4, optimiser SGD dan ADAM dibandingkan, serta epoch ditentukan manual pada 120. Perangkat: Intel Core i7-9700F, RAM 16 GB, GeForce RTX 2070; pelatihan memakan sekitar 9 jam.

### 4. Pelacakan dengan filter Kalman
Filter Kalman linear waktu diskret melacak posisi dan kecepatan objek terdeteksi. Ambang penghapusan jalur diatur [5,5]: jalur yang terkonfirmasi dihapus bila tidak ditetapkan pada deteksi mana pun sebanyak 5 kali dalam 5 pembaruan pelacak terakhir, yaitu buah yang hilang lima bingkai berturut-turut dilepas. Sebagai pembanding, pelacak fitur Kanade-Lucas-Tomasi (KLT) dipakai.

### 5. Evaluasi penghitungan
Hasil penghitungan otomatis dibandingkan dengan hitungan manual pada video uji. Deteksi salah, penghitungan ganda, dan kelalaian (*omission*) dipertimbangkan dalam menghitung buah yang terhitung benar.

## Eksperimen dan Hasil
Tabel 1 membandingkan AP deteksi pir untuk berbagai konfigurasi, dan Tabel 2 serta Tabel 3 melaporkan hasil penghitungan.

| Konfigurasi deteksi pir | AP |
|---|---|
| YOLO v2 backbone ResNet-18 (masukan 224×224) | 0,95 |
| YOLO v2, optimiser ADAM | 0,96 |
| YOLO v2 tanpa augmentasi | 0,88 |
| YOLO v2, optimiser SGD | 0,97 |
| YOLO v3, optimiser SGD | 0,97 |

| Penghitungan pir (234 buah acuan manual) | Terdeteksi | Omisi | Ganda | Salah | Benar | Presisi | Recall | F1 |
|---|---|---|---|---|---|---|---|---|
| Metode yang diusulkan | 231 | 8 | 4 | 1 | 226 | 0,978 | 0,966 | 0,972 |
| Tanpa augmentasi | 206 | 38 | 8 | 2 | 196 | 0,951 | 0,838 | 0,891 |
| Masukan lebih kecil | 234 | 23 | 2 | 21 | 211 | 0,902 | 0,902 | 0,902 |

Pada apel (170 buah acuan manual), metode diusulkan mendeteksi 168 buah dengan 13 omisi, 3 penghitungan ganda, 8 deteksi salah, 157 benar, presisi 0,935, *recall* 0,924, dan F1 0,929. Dengan pelacak KLT sebagai pengganti filter Kalman, jumlah pir yang dihitung 310 dari 234, yaitu menghitung berlebih. Hitungan dilaporkan satu kelas per buah (pir atau apel), tidak per tingkat kematangan.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: deteksi akurat pada buah kehijauan dan tumpang tindih; pelacakan Kalman mempertahankan jalur ketika deteksi gagal sesaat; metode juga mendeteksi apel hijau.

Keterbatasan yang dinyatakan penulis: bila buah keluar dari bingkai lalu direkam kembali, identifikasi sulit dan terjadi penghitungan ganda; citra buram, misalnya dari robot di tanah bergelombang, menyulitkan penghitungan; area penghitungan dipilih pengguna secara manual, sehingga diperlukan pemotongan video otomatis; pengujian pada detektor lain (EfficientDet, YOLO v4) dan bidang lain belum dilakukan; data tidak tersedia untuk publik.

Menurut pembacaan ringkasan ini, hasil penghitungan hanya berasal dari satu video uji pir (234 buah) dan satu video apel (170 buah), sehingga generalisasi terbatas. Pelacakan hanya memakai gerak (Kalman) tanpa ciri tampilan, sehingga buah yang keluar dan masuk kembali bingkai, seperti pada sisi pohon yang berbeda, tidak ditangani, sebagaimana diakui penulis.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dengan pelacakan: deteksi YOLO per bingkai dan filter Kalman untuk menghubungkan buah yang sama, dengan jalur dipertahankan bila deteksi gagal sampai lima bingkai berturut-turut. Hitungan tidak dilaporkan per kelas kematangan. Acuan hitungnya adalah hitungan manual buah pada video uji (234 pir dan 170 apel); detail apakah hitungan manual dari video atau dari pohon fisik tidak dijelaskan, dan panen tidak dipakai.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pola pelacakan prediktif yang menahan identitas ketika deteksi terputus, serta cara pelaporan kesalahan yang memisahkan omisi, penghitungan ganda, dan deteksi salah. Mekanisme ini tidak menangani buah yang muncul kembali dari sisi pohon berbeda; penulis sendiri menyebut hal itu sebagai penyebab penghitungan ganda.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `itakura2021automatic`.

Itakura dkk. menghitung pir dan apel dari video yang direkam sambil berjalan dengan mendeteksi buah memakai YOLO v2 (masukan 608×608) dan menghubungkan buah yang sama antarbingkai dengan filter Kalman. Pada video uji pir, 226 dari 234 buah terhitung benar (F1 0,972), sedangkan pelacak KLT menghasilkan 310 hitungan (menghitung berlebih); pada apel, 157 dari 170 buah terhitung benar (F1 0,929). Penulis menyatakan galat mutlak di bawah 10%.

Catatan verifikasi data: Angka AP (0,97 pir dan apel; 0,88 tanpa augmentasi) ada pada Bagian 3 dan Tabel 1. Hitungan pir (231, 226, 234, presisi 0,978, recall 0,966, F1 0,972) ada pada Tabel 2 dan Bagian 3; hitungan apel (168, 157, 170, 0,935, 0,924, 0,929) ada pada Tabel 3. Angka 310 untuk KLT ada pada Bagian 3. Tabel terekstraksi sebagai daftar sel; kolom dipetakan mengikuti judul kolom tabel asli. Jumlah pohon dan durasi video tidak dilaporkan.
