## Gambaran Umum
Makalah ini mengusulkan metodologi deteksi buah dan lokalisasi 3D apel yang terdiri atas empat tahap: (1) deteksi dan segmentasi instans 2D dengan Mask R-CNN; (2) pembangkitan awan titik 3D apel dengan fotogrametri *structure-from-motion* (SfM) dari citra bertopeng; (3) proyeksi deteksi 2D ke ruang 3D; dan (4) penyaringan positif palsu dengan *support vector machine* (SVM) linear yang dilatih. Metode diuji pada 11 pohon apel Fuji dengan total 1.455 apel di kebun komersial di Agramunt, Catalonia, Spanyol. Citra diperoleh dengan kamera DSLR Canon EOS 60D sebanyak 582 foto (291 per sisi baris), dan dataset dipublikasikan sebagai Fuji-SfM.

Hasil utama pada 8 pohon uji (1.021 apel): tingkat deteksi (*detection rate*, DR) 0,991, *recall* 0,906, presisi 0,857, dan F1 0,881 terhadap seluruh apel pada pohon. Pembanding 2D (Mask R-CNN, dievaluasi terhadap apel yang terlihat pada citra) memperoleh *recall* 0,878, presisi 0,762, dan F1 0,816 pada ambang keyakinan 0,5. Kelemahan utama adalah waktu pemrosesan SfM yang tinggi sehingga metode belum cocok untuk kerja waktu nyata.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pengetahuan tentang sebaran spasial 3D buah pada tingkat pohon dan petak berguna untuk perkiraan hasil, perencanaan panen, pemetaan hasil terhadap faktor pengelolaan, dan sebagai titik awal pemanenan robotik. Sebagian besar sistem deteksi buah berbasis analisis citra 2D, sedangkan lokalisasi 3D yang presisi masih menjadi masalah terbuka. Sensor RGB murah tetapi peka terhadap pencahayaan; LiDAR mahal dan kurang praktis; kamera RGB-D murah tetapi kehilangan kinerja pada kondisi luminansi tinggi di lapangan.

Oklusi buah oleh organ tanaman lain dan perubahan pencahayaan adalah masalah utama. Citra multi-pandang dapat meningkatkan keterlihatan buah, tetapi menimbulkan penghitungan ganda bila registrasi antar-citra tidak dilakukan. Penulis menyebut pendekatan lain: epipolar dengan algoritma Hungarian (Stein dkk., 2016), Hungarian yang diperhalus dengan SfM untuk pelacakan video (Liu dkk., 2018), dan proyeksi deteksi 2D ke model 3D dari sensor RGB-D (Gongal dkk., 2016).

## Ide Utama
Segmentasi instans 2D menghasilkan masker piksel apel, dan masker itu dipakai sebelum SfM sehingga hanya apel (bukan seluruh pohon) yang direkonstruksi. Setelah pose kamera diketahui dari penjajaran SfM, masker 2D diproyeksikan kembali ke awan titik 3D memakai model kamera lubang jarum (*pinhole*). Apel yang sama pada citra berbeda disatukan melalui tumpang tindih di ruang 3D, dan klaster yang tidak khas apel dibuang oleh SVM. Dengan demikian registrasi antar-citra dilakukan otomatis lewat geometri 3D, bukan lewat pelacakan.

Penulis menyebut dua keuntungan tambahan SfM: objek harus terlihat pada sekurang-kurangnya dua citra agar masuk ke model 3D, sehingga positif palsu yang hanya muncul pada satu citra gugur otomatis; dan pendekatan multi-pandang mengurangi oklusi.

## Cara Kerja Langkah demi Langkah
```
 Citra 5184x3456 -> potong 24 sub-citra 1024x1024 -> Mask R-CNN -> masker
        |                                                    |
        +--- citra bertopeng -> SfM (Photoscan) -> awan titik apel
                                       |                     |
                          matriks kamera C_i = K[R_i T_i]    |
                                       v                     v
                          proyeksi masker 2D -> klaster 3D (DBSCAN, 3 cm)
                          IoU > 0,5 antar-citra -> disatukan
                                       |
                          SVM linear (P, V, delta, Psi) -> deteksi 3D valid
```

### 1. Akuisisi data
Lokasi: kebun apel Fuji (*Malus domestica* Borkh. cv. Fuji) komersial di Agramunt, Catalonia, Spanyol, sistem tajuk *tall spindle* dengan jarak tanam 4 x 0,9 m, tinggi kanopi maksimum sekitar 3,5 m dan lebar sekitar 1,5 m. Bagian yang dipelajari adalah 11 pohon berurutan dalam satu baris dengan 1.455 apel. Citra diambil pada akhir September 2017 pada fase BBCH 85 (pematangan lanjut). Kamera Canon EOS 60D (18 MP, 5184 x 3456 piksel) dengan lensa EF-S 24 mm f/2.8 STM, tanpa cahaya buatan, pemotretan dengan tangan (sekitar 8 foto per menit). Sisi timur difoto pagi (11:53 sampai 12:26) dan sisi barat sore (15:27 sampai 16:05). Terdapat 53 posisi foto per sisi dengan sapuan vertikal 5 sampai 6 foto per posisi; jarak antarposisi 22 cm, jarak kamera ke bidang tengah baris sekitar 3 m, tinggi kamera 1,7 m, tumpang tindih vertikal lebih dari 30% dan horizontal lebih dari 90%.

### 2. Segmentasi instans 2D
Mask R-CNN (implementasi Abdulla, 2017) dengan *backbone* ResNet-101-FPN, dimulai dari bobot COCO dan disesuaikan untuk satu kelas. Pelatihan memakai 12 citra dengan 1.749 apel yang dianotasi dengan VIA, tidak mencakup pohon uji 3D. Karena banyak apel per citra, setiap citra dipecah menjadi 24 sub-citra 1024 x 1024 (6 horizontal dan 4 vertikal) dengan tumpang tindih 213 piksel vertikal dan 192 piksel horizontal, menghasilkan 288 sub-citra (231 latih, 57 validasi). Augmentasi hanya pembalikan horizontal; laju belajar 0,001, momentum 0,9, peluruhan bobot 0,0001, 18 epoch. Semua deteksi dengan keyakinan > 0,5 dipakai untuk model 3D, karena penurunan presisi dianggap kurang kritis daripada penurunan *recall*.

### 3. Pembangkitan awan titik 3D
SfM berbasis *bundle adjustment* dijalankan per sisi baris memakai Agisoft Photoscan Professional v1.4 (akurasi tinggi, batas titik kunci 100.000, batas titik pengikat 10.000, awan padat kualitas sedang dengan gambar diperkecil faktor 16). Skala dunia nyata ditetapkan dengan penanda berjarak 85 cm. Awan titik dari citra asli dianotasi manual dengan kotak persegi panjang 3D di sekitar tiap apel sebagai acuan: 1.455 apel, dibandingkan 1.444 apel yang dihitung manual di kebun (selisih dikaitkan dengan galat penghitungan manusia).

### 4. Proyeksi 2D ke 3D dan penyatuan
Setiap masker diproyeksikan ke awan titik 3D. Karena apel yang terhalang dapat ikut terkelompok pada satu proyeksi, DBSCAN dengan jarak minimum 3 cm memisahkan komponen terhubung, dan hanya yang terdekat kamera dipertahankan. Deteksi pada citra berikutnya dengan IoU > 0,5 terhadap deteksi sebelumnya disatukan; deteksi tanpa tumpang tindih atau IoU < 0,5 diproyeksikan sebagai deteksi baru. Proses diulang untuk semua citra.

### 5. Penapis SVM
SVM linear dilatih dengan empat fitur per deteksi: jumlah titik $P$, volume $V$, kepadatan $\delta$ (ditulis $\delta = V/P$ pada teks makalah), dan fitur geometris $\Psi = 27 \cdot \lambda_{1n}\lambda_{2n}\lambda_{3n}$ dari nilai eigen ternormalisasi hasil SVD (nilai 1 untuk deteksi berbentuk bola). Pelatihan memakai 3 dari 11 pohon (434 apel); 8 pohon (1.021 apel) menjadi data uji.

## Eksperimen dan Hasil
Metrik 2D: *recall*, presisi, F1, dan AP dengan IoU > 0,5 antara masker dan acuan. Metrik 3D: DR = LD/T, R = TP/T, P = TP/D, FDR = FP/D, MDR = MD/D, dan F1, dengan T jumlah apel, D jumlah deteksi, LD jumlah label terdeteksi, dan MD jumlah multi-deteksi (satu apel terdeteksi beberapa kali).

Hasil segmentasi 2D (Tabel 2) setelah 18 epoch: AP 0,8599; F1 terbaik 0,8583 pada keyakinan 0,9 (R 0,8597; P 0,8569). Pada keyakinan 0,5 yang dipakai untuk model 3D: R 0,8779, P 0,7622, F1 0,8160.

| Pendekatan | DR | R | P | FDR | MDR | F1 |
|---|---|---|---|---|---|---|
| 3D, data latih (3 pohon, 434 apel) | 0,984 | 0,905 | 0,881 | 0,038 | 0,081 | 0,893 |
| 3D, data uji (8 pohon, 1.021 apel) | 0,991 | 0,906 | 0,857 | 0,037 | 0,106 | 0,881 |
| 2D, keyakinan 0,5 (Tabel 2) | tidak dilaporkan | 0,8779 | 0,7622 | tidak dilaporkan | tidak dilaporkan | 0,8160 |

Pada seluruh 11 pohon, regresi linear antara jumlah deteksi $D$ dan jumlah apel sebenarnya $T$ per pohon menghasilkan R² = 0,80 dan simpangan akar rerata kuadrat 6,42% buah (Gambar 8). Penurunan *recall* di bawah DR dijelaskan oleh dua faktor: beberapa kelompok apel disatukan menjadi satu deteksi (disebut 8,5% apel berada dalam deteksi lebih dari satu apel pada seksi 5) dan multi-deteksi (MDR 0,106), yang paling sering terjadi pada apel yang terlihat dari kedua sisi baris tanpa tumpang tindih cukup untuk disatukan.

Waktu komputasi untuk seluruh dataset (11 pohon, 582 citra), Tabel 4: segmentasi instans 35 menit (CPU+GPU TITAN X); pembangkitan awan titik SfM 500 menit pada CPU dan 50 menit pada CPU+GPU (GTX 1060); proyeksi 2D ke awan titik 3D 260 menit pada CPU (kode tidak diparalelkan).

Pada pembahasan, penulis menyebut peningkatan *recall* 2,8% (0,878 ke 0,906), presisi 9,5% (0,762 ke 0,857), dan F1 6,5% (0,816 ke 0,881), serta menyatakan bahwa selisih bisa lebih besar karena evaluasi 2D terhadap apel yang terlihat, sedangkan evaluasi 3D terhadap seluruh apel pada pohon. Perbandingan penulis dengan karya lain: galat 21,1% untuk identifikasi apel ganda lewat proyeksi ke model RGB-D (Gongal dkk., 2016), korelasi R² = 0,9 pada pelacakan mangga (Stein dkk., 2016) tanpa metrik presisi dan *recall*, serta F1 0,921 pada 59 apel (Tao dan Zhou, 2017).

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: tingkat deteksi tinggi (99,1%) berkat multi-pandang; presisi 3D lebih tinggi karena objek harus terlihat pada sekurang-kurangnya dua citra dan karena penapis SVM; registrasi antar-citra otomatis tanpa pelacakan; presisi data 3D dinilai lebih tinggi daripada LiDAR atau kamera kedalaman (berdasarkan inspeksi visual); dan dataset publik pertama untuk deteksi dan lokalisasi buah 3D fotogrametrik, menurut klaim penulis.

Keterbatasan yang dinyatakan penulis: waktu pemrosesan SfM yang tinggi sehingga tidak cocok untuk waktu nyata atau robot panen; akuisisi data dilakukan manual dan memakan waktu pada area besar, sehingga diusulkan sistem kamera majemuk pada platform darat; multi-deteksi 10,6% masih terjadi; dan 8,5% apel tergabung dalam satu deteksi.

Menurut pembacaan ringkasan ini, data uji hanya 8 pohon dari satu baris pada satu kebun dan satu kultivar, dengan latih SVM pada 3 pohon dari baris yang sama; tidak ada pengulangan atau interval kepercayaan. Pembanding 2D dan 3D memakai penyebut berbeda (apel terlihat berbanding seluruh apel), sehingga selisih F1 tidak sepenuhnya sebanding. Teks makalah juga memuat inkonsistensi kecil: peningkatan presisi ditulis 9,5% (0,762 ke 0,857) dan 11,9% (0,762 ke 0,881) pada bagian berbeda, dan definisi $\delta$ pada teks adalah $V/P$ meskipun disebut "kepadatan". Hasil dilaporkan untuk satu kelas (apel) tanpa pembagian kelas kematangan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali melalui rekonstruksi 3D (C1): masker 2D tiap citra diproyeksikan ke awan titik SfM, klaster 3D dari citra berbeda disatukan lewat IoU > 0,5 di ruang 3D, dan objek yang hanya muncul pada satu citra tidak membentuk model 3D. Sisi timur dan barat baris direkonstruksi terpisah per sisi baris, dan apel yang terlihat dari kedua sisi dapat terhitung ganda bila deteksi dari dua sisi tidak cukup tumpang tindih; penulis melaporkan hal ini sebagai penyebab utama multi-deteksi (MDR 0,106). Dengan demikian, penyatuan lintas dua sisi baris merupakan titik lemah yang dilaporkan secara eksplisit.

Hitungan tidak dilaporkan per kelas (satu kelas apel). Acuan hitungnya adalah anotasi kotak 3D pada awan titik (1.455 apel) yang dibandingkan dengan hitungan manual di kebun (1.444 apel); tidak ada hasil panen. Yang dapat dipindahkan ke tandan sawit multi-sisi: pola penyatuan lintas citra melalui ruang 3D bersama, syarat dukungan minimal dua citra untuk menyaring positif palsu, DBSCAN untuk memisahkan objek terhalang, dan pelaporan MDR dan DR sebagai metrik terpisah. Biaya SfM dan kebutuhan tumpang tindih citra yang tinggi (horizontal di atas 90%) merupakan kendala untuk pohon sawit yang tinggi dengan beberapa sisi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `genemola2020fruitb`.

Gené-Mola dkk. memadukan segmentasi instans Mask R-CNN dengan fotogrametri SfM dan penapis SVM linear untuk mendeteksi dan melokalisasi apel secara 3D pada 11 pohon Fuji (1.455 apel). Pada 8 pohon uji, F1 mencapai 0,881 (R 0,906; P 0,857) terhadap seluruh apel pada pohon, dibandingkan F1 2D 0,816 pada apel yang terlihat. Penyatuan deteksi antar-citra dilakukan otomatis di ruang 3D, dengan multi-deteksi 10,6%, dan SfM menjadi kendala waktu nyata (500 menit pada CPU untuk 582 citra).

Catatan verifikasi data: angka 3D (DR, R, P, FDR, MDR, F1) ada pada Tabel 3 (seksi 3.2); angka 2D pada Tabel 2 (seksi 3.1); waktu komputasi pada Tabel 4; konfigurasi dataset pada Tabel 1 dan seksi 2.1 sampai 2.2; parameter SfM pada Tabel A1; R² 0,80 dan 6,42% pada Gambar 8 dan teks seksi 3.2. Ekstraksi teks menyisipkan nomor baris dan memecah rumus, tetapi isi tabel terbaca utuh. Makalah ini berkode kunci `genemola2020fruitb` pada daftar tugas, sedangkan contoh gaya mencatat makalah yang sama dengan kunci lain; rincian metodenya di sini mengikuti teks, termasuk SVM linear (bukan RBF). Hasil tidak mencakup pengulangan, interval kepercayaan, maupun evaluasi per kelas.
