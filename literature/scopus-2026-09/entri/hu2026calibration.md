# Calibration-enhanced multi-view RGB-D vision for robust recognition and 3D localization of strawberries under occlusions

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hu2026calibration` |
| Judul asli | Calibration-enhanced multi-view RGB-D vision for robust recognition and 3D localization of strawberries under occlusions |
| Penulis | Hu, Shimin; Sun, Meili; Zhao, Chunjiang; Xiong, Ya |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [hu2026calibration.pdf](../pdf/hu2026calibration.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2025.111221

## Gambaran Umum
Makalah ini (*Computers and Electronics in Agriculture* 241, 2026) menyajikan sistem persepsi RGB-D multi-pandang untuk robot pemanen stroberi tipe meja tanam (*table-top*) pada platform HarvestFlex. Sistem memakai dua kamera Intel RealSense D455F yang dipasang simetris di kedua sisi basis bergerak. Kontribusi pertama adalah metode kalibrasi dua tahap, TCC-RM (*two-sided checkerboard calibration with residual modeling*), yang menggabungkan inisialisasi rigid dengan kompensasi residual berbasis bola. Kontribusi kedua adalah jalur fusi multi-RGB-D yang mencocokkan deteksi stroberi antarkamera dengan metrik IoU 3D yang dimodifikasi, lalu menggabungkan posisinya dengan bobot berbasis luas proyeksi dan kedalaman.

Hasil utama menurut abstrak dan teks: RMSE kalibrasi 7,23 mm (dua kamera) dan 6,74 mm (kamera ke lengan, *hand-eye*), yaitu perbaikan 49,23% dan 69,25% (abstrak menulis 69,3%) terhadap metode checkerboard tradisional. Fusi mengurangi galat lokalisasi Euklides sebesar 2,84% sampai 39,21% dibanding konfigurasi satu kamera, dan menambah jangkauan persepsi sebesar 42,86% pada oklusi ringan. RMSE lokalisasi 6,31 mm (oklusi ringan) dan 12,62 mm (oklusi sedang). Ini bukan makalah pencacahan, melainkan lokalisasi 3D untuk pemanenan; tetapi bagian pencocokan lintas kamera dan jumlah deteksi tergabung relevan bagi identitas lintas pandang.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Lokalisasi 3D stroberi sulit karena buah bergerombol, tertutup daun dan buah lain, serta bentuknya tidak beraturan. Sistem multi-kamera memberi sudut pandang saling melengkapi, tetapi akurasinya bergantung pada parameter ekstrinsik antarkamera dan kalibrasi *hand-eye*. Penulis menyatakan bahwa kalibrasi klasik tidak mengoreksi galat nonlinear yang bergantung pada kedalaman pada kamera RGB-D, bahwa metode kalibrasi baru sering kompleks atau lambat, dan bahwa urutan transformasi koordinat pada sistem multi-RGB-D dengan lengan robot belum banyak dikaji.

## Ide Utama
Kalibrasi dilakukan dalam dua tahap: (1) transformasi rigid dari papan catur dua sisi dan metode Tsai-Lenz; (2) kompensasi residual dengan regresi polinomial orde dua yang dilatih pada pusat bola 3D berjari-jari 5 cm. Untuk persepsi, tiap stroberi menghasilkan kotak batas 3D dari deteksi 2D dan kedalaman. Kotak dari dua kamera dipasangkan bila jarak pusatnya di bawah ambang dan IoU yang dimodifikasi cukup besar, lalu pusatnya digabungkan secara terbobot. Dua urutan fusi dibandingkan: fusi pada kerangka kamera (*Camera-Frame*, CF) dan fusi pada kerangka basis robot (*Base-Frame*, BF).

## Cara Kerja Langkah demi Langkah

### 1. Perangkat keras dan akuisisi data
Dua kamera D455F dipasang pada basis bergerak dengan sudut horizontal keluar sekitar 110 derajat dan kemiringan ke atas sekitar 55 derajat, dengan rel gerak lengan di antara kamera. Jangkauan kerja berkisar 1,2 sampai 3 m. Citra RGB dan kedalaman 640 × 480 piksel. Percobaan dilakukan di lingkungan pertanian nyata dengan pencahayaan bervariasi, sedangkan kalibrasi residual dilakukan sekali di dalam ruangan terkendali. Kultivar stroberi, jumlah citra latih detektor, dan jenis detektor tidak dilaporkan pada teks yang dibaca.

### 2. Kalibrasi TCC-RM
Tahap 1: kalibrasi dua kamera memakai papan catur dua sisi dengan metode Zhang; pose dengan galat reproyeksi rata-rata terkecil dipilih. Kalibrasi *hand-eye* memakai konfigurasi *eye-to-hand* dan metode Tsai-Lenz. Tahap 2: pusat bola diekstraksi dengan segmentasi HSV, lingkaran terkecil, dan koreksi perspektif memakai jari-jari diketahui. Residual $\Delta P_i$ antara pusat bola dari dua kerangka dimodelkan dengan regresi polinomial orde dua pada $(x, y, z)$ per komponen, dan titik baru dikoreksi sebagai $\hat{X} = T X + \Delta P$.

### 3. Urutan transformasi
CF mentransformasikan titik kamera 2 ke kerangka kamera 1 dengan kompensasi, memfusikan di kamera 1, lalu mentransformasikan ke basis dengan kompensasi akhir. BF mentransformasikan titik tiap kamera langsung ke basis dengan kompensasi masing-masing, lalu memfusikan di basis.

### 4. Pencocokan lintas kamera
Pasangan kandidat disaring dengan ambang jarak pusat. IoU termodifikasi didefinisikan $\text{IoU}_{new} = V_{inter} / \min(V_1, V_2)$, sehingga lebih toleran terhadap oklusi parsial dan perbedaan ukuran dibandingkan IoU tradisional.

### 5. Fusi terbobot dan strategi hibrida
Bobot $w_i = A_i / (d_i^2 + \epsilon)$ dengan $A_i$ luas proyeksi dan $d_i$ kedalaman, dan pusat gabungan adalah rerata terbobot; bila kedua bobot mendekati nol dipakai rerata sederhana. Daerah pandang yang tidak tumpang tindih dihitung di muka, sehingga deteksi di daerah itu dilokalisasi langsung dari satu kamera tanpa pencocokan; pencocokan IoU hanya dilakukan di daerah tumpang tindih.

## Eksperimen dan Hasil
Acuan posisi stroberi diperoleh dari kinematika lengan: pena logam pada fiksur cetak 3D di ujung efektor menunjuk stroberi. Pada oklusi sedang, ujung pena diletakkan tepat di bawah pusat stroberi. Jumlah stroberi atau sampel untuk Tabel 2 sampai 6 tidak dinyatakan pada teks yang dibaca.

Kalibrasi (RMSE Euklides):

| Kalibrasi | TCC | TCC-RM | Reduksi |
|---|---|---|---|
| Dua kamera (Tabel 2) | 14,24 mm | 7,23 mm | 49,23% |
| *Hand-eye* (Tabel 3) | 21,92 mm | 6,74 mm | 69,25% |

Pencocokan lintas pandang pada 21 sampel oklusi ringan, ambang IoU 0,4 (Tabel 4):

| Metrik IoU | Presisi (%) | Recall (%) | F1 (%) |
|---|---|---|---|
| Tradisional | 100,00 | 19,75 | 32,99 |
| Termodifikasi | 93,65 | 72,84 | 81,94 |

Lokalisasi 3D (RMSE Euklides, mm; Tabel 5 dan 6):

| Metode | Tanpa oklusi | Oklusi ringan | Oklusi sedang |
|---|---|---|---|
| C1-B (kamera 1 ke basis) | 6,49 | 7,05 | 14,32 |
| C2-B (kamera 2 ke basis) | 8,52 | 9,19 | 14,72 |
| C2-C1-B | 9,60 | 10,38 | 25,37 |
| CF | 6,11 | 6,85 | 13,65 |
| BF | 5,94 | 6,31 | 12,62 |

Perluasan jangkauan persepsi (Tabel 7, 21 sampel): total deteksi kamera 1 sebanyak 140, kamera 2 sebanyak 159, pasangan cocok 49 (ambang IoU termodifikasi 0,5), deteksi tergabung $A + B - C$ sebanyak 250, dan deteksi maksimum satu pandang 175 (jumlah per sampel). Selisih sederhana 250 dikurangi 175 adalah 75, atau peningkatan 42,86%. Teks menyebut rerata 2,33 pasangan cocok per sampel dan 80,4% deteksi berasal dari daerah tidak tumpang tindih. Tidak ada deteksi positif palsu pada eksperimen ini, tetapi penulis menyatakan deteksi terlewat (stroberi kecil, cahaya sangat kuat, oklusi berat) terjadi dan tidak diperhitungkan. Seluruh alur berjalan rata-rata 250 ms per bingkai (4 Hz). Pada oklusi berat, model persepsi gagal mendeteksi stroberi sehingga tidak ada analisis kuantitatif.

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: kalibrasi lebih akurat dibanding TCC dan, pada *hand-eye*, galat 2,07 mm (X) dan 4,95 mm (Y) lebih kecil daripada nilai yang dilaporkan untuk Kalib (4,8 mm dan 3,0 mm); fusi mengurangi galat dan kasus ekstrem; penghitungan pasangan cocok menambah jangkauan persepsi.

Keterbatasan yang dinyatakan penulis: evaluasi hanya sampai oklusi sedang; oklusi berat belum tertangani; evaluasi dilakukan pada kondisi statis dengan sistem terbuka (*open-loop*), dan panen dinamis memerlukan kecepatan persepsi lebih tinggi serta kontrol dan perencanaan gerak; residual pada sumbu Y kadang lebih besar daripada TCC pada beberapa sampel karena rentang data kompensasi Y terbatas; galat meningkat pada oklusi sedang akibat sedikitnya titik kedalaman valid dan perlekatan awan titik pada kamera cahaya terstruktur.

Menurut pembacaan ringkasan ini, terdapat keterbatasan lain. Jumlah sampel dan jumlah stroberi evaluasi lokalisasi tidak tercantum pada teks yang dibaca, dan evaluasi pencocokan hanya memakai 21 sampel oklusi ringan. Stroberi yang dipasang pada pena bukan kondisi tanaman nyata. Deteksi yang terlewat tidak dihitung pada metrik jangkauan, sehingga peningkatan 42,86% bersifat relatif terhadap deteksi yang berhasil. Dua nilai ambang IoU yang berbeda (0,4 dan 0,5) dipakai pada dua evaluasi tanpa penjelasan. Hanya dua kamera dengan geometri tetap yang diuji.

## Kaitan dengan Tinjauan main6
Makalah ini menangani objek yang terlihat dari dua kamera sekaligus. Mekanismenya adalah pencocokan 3D lintas kamera: kotak batas 3D dari tiap kamera ditransformasikan ke kerangka bersama (kamera atau basis) menggunakan kalibrasi, disaring dengan jarak pusat, dicocokkan dengan IoU termodifikasi (volume irisan dibagi volume terkecil), lalu digabung terbobot. Identitas ditetapkan secara geometris, tidak dengan tampilan. Tidak ada hitungan per kelas (hanya satu kelas stroberi). Jumlah deteksi tergabung dilaporkan sebagai ukuran perluasan jangkauan (Tabel 7), tetapi acuan jumlahnya adalah deteksi model itu sendiri, bukan hitungan manual atau panen; untuk lokalisasi, acuannya adalah posisi dari kinematika lengan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: gagasan menormalkan irisan dengan volume terkecil agar tahan terhadap oklusi parsial, penggabungan terbobot menurut kualitas pengamatan (luas proyeksi dan kedalaman), serta penetapan di muka daerah tidak tumpang tindih agar pencocokan hanya dilakukan di daerah tumpang tindih. Syaratnya, pose kamera dan kalibrasi antarsisi harus akurat, dan mekanisme ini diuji hanya pada dua kamera tetap dengan jarak 1,2 sampai 3 m, bukan pohon tinggi berbagai sisi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `hu2026calibration`.

Hu dkk. (2026) mengusulkan kalibrasi dua tahap TCC-RM dan jalur fusi multi-RGB-D untuk lokalisasi 3D stroberi pada robot pemanen HarvestFlex dengan dua kamera RealSense D455F. Pencocokan lintas kamera memakai IoU 3D termodifikasi yang menaikkan recall dari 19,75% menjadi 72,84% (F1 dari 32,99% menjadi 81,94%) pada 21 sampel oklusi ringan, dan fusi menurunkan RMSE lokalisasi hingga 5,94 mm (tanpa oklusi) dan 6,31 mm (oklusi ringan) pada konfigurasi BF.

Catatan verifikasi data: Angka kalibrasi dari Tabel 2 dan 3; pencocokan dari Tabel 4; lokalisasi dari Tabel 5 dan 6; cakupan dari Tabel 7 dan Persamaan 14; waktu 250 ms dari Seksi 3.3 dan 3.5. Persentase pengurangan 69,25% (Tabel 3) tampak sebagai 69,3% pada abstrak. Pernyataan "2,84% sampai 39,21%" berasal dari abstrak dan Seksi 3.3. Angka "2,33 pasangan per sampel" cocok dengan 49 dibagi 21 (dihitung). Tabel pada ekstraksi terpecah satu sel per baris; urutan kolom disimpulkan dari kepala tabel dan konsistensi (misalnya 140 + 159 - 49 = 250). Jumlah sampel lokalisasi, jenis detektor, dan kultivar tidak ditemukan pada teks. Teks terpotong pada bagian daftar pustaka (baris 1.579 dari 1.716), yang tidak memengaruhi isi.
