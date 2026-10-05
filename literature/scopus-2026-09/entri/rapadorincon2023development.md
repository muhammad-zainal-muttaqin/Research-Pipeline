# Development and evaluation of automated localisation and reconstruction of all fruits on tomato plants in a greenhouse based on multi-view perception and 3D multi-object tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `rapadorincon2023development` |
| Judul asli | Development and evaluation of automated localisation and reconstruction of all fruits on tomato plants in a greenhouse based on multi-view perception and 3D multi-object tracking |
| Penulis | Rapado-Rinc\'on, David; van Henten, Eldert J.; Kootstra, Gert |
| Tahun | 2023 |
| Venue | Biosystems Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [rapadorincon2023development.pdf](../pdf/rapadorincon2023development.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2023.06.003

## Gambaran Umum

Makalah ini memperkenalkan metode untuk membangun representasi tiga dimensi berpusat objek (*world model*) dari semua buah tomat pada satu tanaman di rumah kaca. Metode ini memakai persepsi multi-pandang dari kamera yang dipasang pada lengan robot dan pelacakan multi-objek tiga dimensi (*3D multi-object tracking*, 3D MOT). Setiap citra diproses oleh Mask R-CNN untuk menghasilkan masker buah, masker dipakai untuk menyaring awan titik dan menghasilkan awan titik parsial per buah, lalu pusat buah diestimasi dengan pencocokan bola (*sphere fitting*). Posisi buah dalam koordinat robot dihubungkan antarpandang oleh pelacak berbasis filter Kalman dan algoritma Hungaria.

Data evaluasi berupa 700 citra dari 100 sudut pandang pada tujuh tanaman tomat varietas Santiana di rumah kaca Wageningen University & Research, Belanda. Detektor dilatih pada 1.180 citra RGB.

Hasil utama: galat hitungan total terendah (MAPE) 5,06% dan akurasi pelacakan HOTA tertinggi 71,47%. Abstrak menyebut galat hitungan maksimum 5,08%, tetapi tabel dan kesimpulan memuat 5,06% (lihat catatan verifikasi). Penulis menekankan bahwa metrik pelacakan seperti HOTA mengungkap galat asosiasi yang tidak terlihat pada galat hitungan total.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Robot agro-pangan sulit dioperasikan karena oklusi berat serta variasi kondisi lingkungan, sistem budi daya, dan bentuk objek. Pendekatan konvensional pada robot pemanen memotret, bertindak, lalu membuang informasi, sehingga lemah saat oklusi. Persepsi multi-pandang berpotensi mengatasi oklusi, tetapi memerlukan model dunia yang menggabungkan informasi dari banyak sudut pandang. Representasi berbasis SLAM hanya geometris, sedangkan pelacakan multi-objek memungkinkan atribut semantik per objek.

Penelitian pencacahan berbasis pelacakan sebelumnya (pada paprika dan stroberi) memakai pelacakan 2D berbasis IoU dengan sistem satu derajat kebebasan yang bergerak sejajar baris tanaman, dan hanya dievaluasi dengan galat hitungan total. Penulis menilai evaluasi itu tidak cukup karena hitungan yang tepat dapat menyembunyikan pertukaran ID atau positif palsu dan negatif palsu yang saling meniadakan.

## Ide Utama

Gagasan intinya adalah merepresentasikan setiap buah sebagai objek dengan posisi 3D berdistribusi Gauss (rerata dan kovarians) yang diperbarui terus oleh filter Kalman setiap kali buah itu terdeteksi dari sudut pandang baru. Karena asosiasi dilakukan di ruang 3D koordinat robot, bukan pada piksel 2D, buah yang berada di depan buah lain tidak tertukar hanya karena koordinat citranya mirip.

Mekanisme identitas adalah asosiasi data 3D antarpandang dengan jarak Mahalanobis; hitungan adalah jumlah objek pada model dunia. Penulis juga mengusulkan evaluasi dengan HOTA yang dapat diuraikan menjadi galat lokalisasi, deteksi, dan asosiasi.

## Cara Kerja Langkah demi Langkah

```
 RGB + awan titik -> Mask R-CNN -> masker -> titik 3D per buah
   -> pencocokan bola -> posisi di koordinat robot -> filter wilayah
   -> asosiasi Hungaria (Mahalanobis) -> pembaruan Kalman -> model dunia
```

### 1. Akuisisi data

Lengan robot ABB IRB1200 dengan kamera LiDAR Intel RealSense L515 pada ujung efektor dipasang pada kereta yang bergerak di rel antarbaris rumah kaca tomat Belanda. Dataset pertama (deteksi) berisi 1.180 citra RGB beranotasi masker piksel dan kotak pembatas, berbasis 123 citra dari Afonso dkk. (2019) ditambah 1.057 citra baru dari rumah kaca Wageningen (varietas Merlice dan Campari). Dataset kedua (evaluasi model dunia) berisi 700 citra dari 100 sudut pandang pada tujuh tanaman varietas Santiana, yang tidak ada pada data latih detektor. Lintasan kamera berbentuk setengah silinder dengan sepuluh tingkat ketinggian, masing-masing setengah lingkaran dengan sepuluh sudut pandang yang tersebar merata. Batang dianggap berada sekitar 60 cm di depan titik asal robot dan jari-jari setengah silinder adalah 30 cm. Pada setiap sudut pandang direkam citra warna 960 × 540, awan titik terstruktur, dan pose kamera terhadap dasar robot. Buah pada setiap bingkai dianotasi dengan kotak pembatas dan ID pelacakan.

### 2. Deteksi dan lokalisasi 3D

Mask R-CNN dijalankan dengan dua ambang keyakinan, 0,5 dan 0,7. Titik 3D tiap deteksi disaring dari awan titik dengan masker; deteksi tanpa titik valid dibuang. Pusat buah diestimasi dengan pencocokan bola, dan buah yang pusat atau jari-jarinya di luar batas wajar disaring. Jari-jari wajar dibatasi $r_{min}=1$ cm hingga $r_{max}=5$ cm; bila di luar batas, pusat tetap diestimasi sebagai rerata titik 3D. Posisi ditransformasi ke koordinat dasar robot lalu disaring dengan ambang sumbu sesuai jarak antartanaman agar hanya tomat pada tanaman sasaran yang dipertahankan.

### 3. Model dunia dan asosiasi data

Model dunia berisi himpunan objek dengan posisi (rerata dan kovarians), kelas, dan kotak pembatas terakhir. Asosiasi memakai algoritma Hungaria dengan biaya berupa kuadrat jarak Mahalanobis; pasangan dengan biaya di atas 7,82 (kuantil 0,95 distribusi khi-kuadrat dengan 3 derajat kebebasan) dibuang. Posisi diperbarui dengan langkah pembaruan filter Kalman, dan diproyeksikan ke bingkai berikutnya dengan langkah prediksi Kalman. Objek baru dibuat bila deteksi tidak terkait objek mana pun; objek dapat berstatus tentatif selama $n_{init}$ bingkai (yang diuji bernilai 0 dan 1), dan objek terkonfirmasi tidak pernah dihapus.

### 4. Metrik evaluasi

Hitungan dinilai dengan MPE (galat persentase rerata, menunjukkan kecenderungan kurang atau lebih hitung) dan MAPE (galat persentase absolut rerata). Pelacakan dinilai dengan HOTA, yang diuraikan menjadi DetA (deteksi) dan AssA (asosiasi). Karena HOTA memerlukan lintasan citra 2D, lintasan buah didefinisikan sebagai posisi kotak pembatas pada bidang citra. Kinerja dihitung per tingkat ketinggian secara kumulatif dan dirata-ratakan atas tujuh tanaman.

## Eksperimen dan Hasil

Detektor pada IoU 0,5 (Tabel 1): teks menyatakan *recall* 0,86 dan presisi 0,71 pada ambang 0,5, serta *recall* 0,66 dan presisi 0,88 pada ambang 0,7, sedangkan Tabel 1 mencantumkan pasangan nilai dengan urutan kolom berlawanan (0,86 dan 0,71 pada ambang 0,5; 0,88 dan 0,66 pada ambang 0,7). *Recall* turun stabil pada bagian atas tanaman.

Persentase deteksi yang ditolak karena tidak ada titik (RD) pada Tabel 2 berkisar 1,22% sampai 4,83%, dan deteksi dengan pencocokan bola tidak valid (NSF) berkisar 44,54% sampai 55,08% antartingkat ketinggian dan ambang keyakinan. Pembaruan model dunia dapat mencapai 10 Hz, dengan lebih dari 95% waktu dipakai pada prapemrosesan dan deteksi.

Hasil hitungan dan pelacakan (Tabel 3, tingkat ketinggian kumulatif; nilai terpilih):

| Tingkat | Ambang | $n_{init}$ | MAPE | MPE | HOTA | DetA | AssA |
|---|---|---|---|---|---|---|---|
| 1 | 0,5 | 0 | 17,48 | 13,86 | 71,47 | 68,82 | 74,78 |
| 1 | 0,7 | 1 | 8,95 | 4,94 | 63,05 | 61,04 | 65,59 |
| 2 | 0,7 | 1 | 5,06 | 3,52 | 62,44 | 63,68 | 61,50 |
| 10 (seluruh urutan) | 0,5 | 0 | 27,50 | 23,86 | 54,32 | 55,98 | 52,96 |
| 10 (seluruh urutan) | 0,5 | 1 | 14,72 | 3,20 | 52,51 | 53,57 | 51,70 |
| 10 (seluruh urutan) | 0,7 | 0 | 18,01 | 13,88 | 53,53 | 54,39 | 52,90 |
| 10 (seluruh urutan) | 0,7 | 1 | 12,21 | 4,50 | 51,25 | 51,53 | 51,16 |

Baris tingkat 2 dengan ambang 0,7 dan $n_{init}=1$ menunjukkan DetA 63,68 dan AssA 61,50 menurut urutan sel pada teks ekstraksi; kolom MAPE tabel dibaca berdasarkan urutan sel yang sama. Penulis menyimpulkan bahwa ambang 0,7 dan $n_{init}=1$ memberi MAPE dan MPE terbaik, sedangkan ambang 0,5 dan $n_{init}=0$ memberi HOTA, DetA, dan AssA terbaik, karena positif palsu tidak dapat dihapus dari model dunia sehingga memperbesar galat hitungan tetapi tidak menurunkan metrik pelacakan. Metrik HOTA menurun seiring tingkat ketinggian, yaitu bagian atas tanaman yang lebih rimbun, berdaun lebat, dan berbuah lebih kecil dan kurang matang.

## Kelebihan dan Keterbatasan

Kelebihan: persepsi multi-pandang dengan asosiasi 3D, evaluasi di rumah kaca nyata dengan oklusi tinggi, dan analisis pelacakan memakai HOTA yang diuraikan menjadi galat deteksi dan asosiasi, bukan hanya galat hitungan total. Penulis juga memperlihatkan bahwa MAPE yang mirip (11,35 dan 11,36) dapat disertai HOTA yang sangat berbeda (66,68 dan 56,09).

Keterbatasan yang dinyatakan penulis: performa detektor turun di bagian atas tanaman; kualitas awan titik terpengaruh cahaya sehingga hingga 4,58% deteksi ditolak dan hingga 55,08% pencocokan bola tidak valid; pengaruh kondisi cahaya tidak dinilai; model dunia tidak dapat menghapus positif palsu karena objek yang tidak terdeteksi dapat saja tertutup daun; asosiasi memakai pusat Kartesius saja sehingga galat asosiasi masih banyak pada sudut pandang atas; lintasan setengah silinder tidak dioptimalkan untuk perolehan informasi. Penulis merencanakan fitur tampilan atau pendekatan *end-to-end*, serta pemilihan sudut pandang berikutnya (*next-best-view*).

Menurut pembacaan ringkasan ini, evaluasi hanya mencakup tujuh tanaman dari satu varietas dan satu rumah kaca, dan jumlah total tomat acuan tidak dilaporkan pada teks. Sistem memerlukan lengan robot enam derajat kebebasan dan kamera LiDAR jarak dekat, sehingga pemindahan langsung ke kebun terbuka tidak terjamin. Keunggulan pelacakan 3D atas 2D hanya diargumenkan, tanpa perbandingan eksperimen langsung pada data yang sama.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat dari banyak sudut pandang dan melakukan penyatuan identitas dengan mekanisme asosiasi 3D (posisi Gauss pada koordinat robot, jarak Mahalanobis, algoritma Hungaria, dan filter Kalman) pada pandangan dari lintasan setengah silinder mengelilingi tanaman. Ini adalah contoh langsung pencocokan multi-pandang yang bergantung pada pose kamera yang diketahui dan kedalaman. Hitungan tidak dilaporkan per kelas (kelas selalu tomat), dan acuan hitungan adalah anotasi kotak dan ID pada citra (bukan panen atau hitung manual di lapangan).

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: penyatuan identitas di ruang 3D bersama dengan model ketidakpastian posisi, serta penggunaan metrik asosiasi (HOTA, AssA) di samping galat hitungan untuk mengungkap pertukaran identitas dan galat yang saling meniadakan. Syaratnya adalah pose kamera dan kedalaman yang andal, yang pada tandan sawit berukuran besar dan pada jarak yang lebih jauh belum dibahas di makalah ini.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `rapadorincon2023development`.

Rapado-Rincon dkk. mengusulkan model dunia berpusat objek untuk buah tomat di rumah kaca, yang menggabungkan Mask R-CNN, pencocokan bola pada awan titik parsial, dan pelacakan 3D berbasis filter Kalman dan algoritma Hungaria dari banyak sudut pandang lengan robot. Pada tujuh tanaman varietas Santiana, MAPE terendah 5,06% dan HOTA tertinggi 71,47%, dan penulis menunjukkan bahwa galat hitungan total saja tidak cukup untuk menilai kualitas asosiasi.

Catatan verifikasi data: angka hitungan dan pelacakan dibaca dari Tabel 3, kutipan galat 5,06% dan HOTA 71,47% dari seksi 4 dan 5; abstrak menulis "5,08%", yang tidak sama dengan 5,06% pada Tabel 3 dan kesimpulan. Teks Tabel 1 dan paragraf seksi 3.1 menukar urutan nilai presisi dan *recall* (paragraf: *recall* 0,86 dan presisi 0,71; tabel menurut judul kolom: presisi 0,86 dan *recall* 0,71), sehingga urutan yang benar tidak dapat dipastikan dari teks. Tabel 3 diekstraksi satu sel per baris; pemetaan sel ke kolom dilakukan menurut urutan kolom judul dan hanya baris yang dikutip di sini yang dipakai. Jumlah total tomat acuan, jumlah tomat per tanaman, dan ukuran awan titik tidak dilaporkan. Definisi MAPE menyebut n sebagai jumlah bingkai, sedangkan evaluasi dirata-ratakan atas tujuh tanaman; kejelasan unit n tidak dapat diverifikasi dari teks. Gambar 7 dan 8 tidak memberi angka yang dapat diverifikasi.
