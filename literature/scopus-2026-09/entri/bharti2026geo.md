# Geo-Referenced Factor-Graph SLAM for Orchard-Scale 3D Apple Reconstruction and Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bharti2026geo` |
| Judul asli | Geo-Referenced Factor-Graph SLAM for Orchard-Scale 3D Apple Reconstruction and Yield Estimation |
| Penulis | Bharti, Dheeraj; Faria, Lilian Nogueira de; Koenigkan, Luciano Vieira; Gebler, Luciano; de Rossi, Andrea; Santos, Thiago Teixeira |
| Tahun | 2026 |
| Venue | Agriculture Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [bharti2026geo.pdf](../pdf/bharti2026geo.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture16070764

## Gambaran Umum
Makalah ini mengusulkan alur kerja estimasi hasil apel skala kebun yang konsisten secara geometris. Alur itu menggabungkan fusi GNSS dan *visual-inertial odometry* (VIO) dari kamera stereo ZED X, deteksi apel dengan YOLOv9, pelacakan titik antarbingkai dengan CoTracker3, triangulasi multi-pandang untuk mendapatkan satu pusat 3D per apel (*landmark*), dan optimasi graf faktor inkremental iSAM2 yang menyempurnakan pose kamera dan posisi apel secara bersamaan. Apel hasil rekonstruksi diagregasi menjadi peta kepadatan berreferensi geografis (ENU) dan taksiran massa yang diturunkan dari jari-jari apel dengan asumsi bola dan kerapatan curah.

Data dikumpulkan di kebun apel kultivar Fuji (blok pohon *palmette*) di Stasiun Eksperimen Buah Iklim Sedang Embrapa Uva e Vinho, Vacaria, Brasil, pada Maret 2025, dalam satu lintasan kontinu sekitar 500 m yang melewati empat baris Fuji pada kedua sisi baris. Hasil utama: galat proyeksi ulang (*reprojection error*) rerata turun dari 40,31 piksel menjadi 8,74 piksel setelah iSAM2; jumlah apel hasil rekonstruksi 9.739 terhadap 9.985 apel hasil panen dan hitung manual (kurang hitung 2,46%); dan taksiran massa nominal 1.485,108 kg dengan rentang 1.293,927 sampai 1.692,059 kg untuk kerapatan 650 sampai 850 kg/m3.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penaksiran hasil buah secara konvensional bertumpu pada pengambilan sampel manual dan inspeksi visual yang padat karya, subjektif, dan sulit diperluas. Detektor per bingkai menghasilkan hitungan ganda ketika buah yang sama terlihat berulang dan kurang hitung ketika buah terlewat pada bingkai tertentu. Pelacakan objek tunggal antarbingkai mengurangi masalah itu, tetapi menurut penulis tidak menyelesaikan ambiguitas geometris ketika gerak kamera rumit atau penampakan buah berubah karena sudut pandang dan pencahayaan.

Di sisi lokalisasi, estimasi pose VIO dapat menyimpang (*drift*), dan GNSS di kebun dapat terganggu oleh *multipath* dan peredaman kanopi. Penulis menilai bahwa fusi kendala gerak relatif, petunjuk posisi global, dan pengukuran citra dalam satu estimasi yang konsisten diperlukan agar rekonstruksi apel stabil sepanjang lintasan yang panjang.

## Ide Utama
Setiap apel diperlakukan sebagai *landmark* 3D yang persisten, bukan sebagai deteksi per bingkai. Identitas diberikan oleh pelacakan titik CoTracker3 yang diinisialisasi dari deteksi YOLOv9, lalu pusat 3D tiap lintasan (*track*) diperoleh dari triangulasi pada pose kamera hasil fusi GNSS-VIO. Graf faktor iSAM2 kemudian menyempurnakan pose dan *landmark* secara bersama dengan faktor proyeksi ulang, faktor gerak relatif yang kuat antarpose berurutan, *prior* translasi ENU yang lunak, *prior* posisi *landmark*, dan *prior* kuat pada pose pertama untuk menetapkan kerangka acuan. Hitungan apel adalah jumlah *landmark* valid.

## Cara Kerja Langkah demi Langkah

```
 ZED X (stereo, RGB kiri) + RTK-GNSS
        |-> ZED Fusion (VIO + GNSS) -> pose geo-referensi per bingkai
 YOLOv9 (conf >= 0,55) -> CoTracker3 online (kueri tiap 10 bingkai) -> track
 Triangulasi DLT + RANSAC + gerbang geometris -> landmark 3D awal
 iSAM2: pose + landmark (proyeksi ulang, gerak relatif, ENU, prior)
 -> hitungan, peta kepadatan ENU, taksiran massa
```

### 1. Akuisisi data
Platform bergerak SEEmear dipasang pada traktor dengan tiang yang memungkinkan pencitraan kedua sisi baris. Sensornya adalah kamera stereo ZED X (hanya aliran kiri yang dipakai sebagai masukan monokular) dan penerima GNSS berkemampuan RTK (dengan pascapemrosesan PPK). Laju gerak sekitar 5 km/jam, video sekitar 30 fps pada 1920 × 1200 piksel, dan GNSS 5 Hz. Teks menyebut sekitar 29.000 bingkai berstempel waktu. Lintasan mencakup sekitar 500 m, empat baris Fuji (baris bernomor genap; baris bernomor ganjil adalah Gala pemolinasi yang sudah dipanen), dan belokan di ujung baris. Baris terakhir dilatih dengan konfigurasi berbeda yang lebih rapat.

### 2. Estimasi pose dan geo-referensi
ZED Fusion menyelaraskan stempel waktu kamera dengan GNSS terdekat dan memperkirakan transformasi rigid dari kerangka VIO ke kerangka dunia yang berreferensi GNSS. Pose terfusi $T^t_{WC}$ dipakai sebagai inisialisasi. Penulis menyatakan iSAM2 tidak mengestimasi ulang lengan tuas antena GNSS ke kamera; hal itu diwarisi dari kalibrasi ZED Fusion.

### 3. Deteksi dan pelacakan
YOLOv9 dipakai langsung tanpa pelatihan tambahan (ambang keyakinan 0,55; NMS IoU 0,45; ukuran masukan 640 × 640). CoTracker3 berjalan dalam mode daring dengan kueri diperbarui setiap 10 bingkai. Lintasan yang lebih pendek dari 5 bingkai dibuang. Penulis menyatakan lintasan berakhir ketika apel keluar dari citra; tidak ada reidentifikasi jangka panjang. Pembandingan pelacak dilakukan dengan TrackEval pada satu segmen kebun representatif (konfigurasi kotak MOTChallenge 2D, IoU 0,5).

### 4. Triangulasi multi-pandang
Pusat 3D tiap lintasan diperoleh dengan DLT (*direct linear transform*) dari pengamatan 2D dan pose, dengan RANSAC (84 iterasi), batas galat proyeksi ulang 10 piksel, kendala *cheirality* (titik di depan kamera), paralaks minimum 1,2 derajat, dan jarak kamera-buah maksimum 5 m. Penulis menekankan bahwa rekonstruksi bukan nilai kedalaman stereo per bingkai, melainkan triangulasi berbasis pose.

### 5. Optimasi graf faktor iSAM2
Keadaan terdiri atas pose kamera dan *landmark* apel. Faktor proyeksi ulang memakai fungsi rugi Huber (k = 1,345; sigma 10 piksel). Sigma translasi antarpose 0,01 m dan rotasi 0,3 derajat; sigma translasi ENU 0,50 m dengan sigma rotasi 180 derajat sehingga *prior* efektif hanya membatasi translasi; sigma *prior landmark* 0,05 m; pose pertama diberi *prior* sangat kuat (10^-4 untuk translasi dan 10^-3 untuk rotasi). Tabel A2 lampiran menyebut skrip pada implementasi saat ini melakukan satu pembaruan graf lalu menghitung estimasi.

### 6. Keluaran: hitungan, kepadatan, dan taksiran massa
Hitungan adalah jumlah *landmark* valid. Jari-jari apel dihitung dari lebar dan tinggi kotak, kedalaman *landmark* pada kamera, dan panjang fokus; nilai akhir adalah median dari 15 pandangan dengan kotak terbesar. Volume dihitung sebagai bola, dan massa sebagai kerapatan dikali volume. Kerapatan nominal dikalibrasi dari satu apel acuan berdiameter 8,0 cm dan massa 200 g, menghasilkan sekitar 746 kg/m3, dengan rentang sensitivitas 650 sampai 850 kg/m3. Peta kepadatan adalah histogram posisi *landmark* pada bidang ENU.

## Eksperimen dan Hasil
Optimasi dijalankan pada 11.307 pose kamera dan 9.739 *landmark* yang diinisialisasi dari 11.793 lintasan kandidat, dengan 411.739 faktor proyeksi ulang. Acuan hitung adalah hasil panen fisik blok yang dipindai dan hitung manual seluruh buah (9.985 apel).

Perbandingan pelacak (Tabel 1; persentase kecuali dua kolom terakhir):

| Pelacak | HOTA | DetA | AssA | MOTA | IDF1 | #ID | #GT ID |
|---|---|---|---|---|---|---|---|
| Hungarian | 28,13 | 40,55 | 20,42 | 25,44 | 26,63 | 2.146 | 253 |
| SORT | 11,98 | 6,05 | 24,41 | 3,93 | 8,91 | 402 | 253 |
| ByteTrack | 12,34 | 3,94 | 38,74 | 3,78 | 6,56 | 90 | 253 |
| CoTracker | 42,63 | 33,56 | 55,97 | 3,04 | 50,75 | 320 | 253 |

Galat proyeksi ulang (piksel):

| Kondisi | Rerata | Median | p90 | p95 | Residu > 10 px |
|---|---|---|---|---|---|
| Sebelum iSAM2 | 40,31 | 22,70 | 104,41 | 135,57 | 65,40% |
| Sesudah iSAM2 | 8,74 | 5,46 | 17,12 | 23,41 | 25,38% |

Residu di atas 5 piksel turun dari 76,63% menjadi 53,57%. Koreksi pose oleh iSAM2: translasi rerata 0,229 m (maksimum 1,265 m) dan rotasi rerata 5,17 derajat (maksimum 24,24 derajat); residu gerak relatif tetap kecil (translasi rerata 0,0055 m, rotasi 0,108 derajat).

Hitungan terhadap acuan, per baris (Tabel A1):

| Baris | GT | Prediksi | Galat absolut | Galat |
|---|---|---|---|---|
| 2 | 2.721 | 2.634 | 87 | 3,20% |
| 4 | 2.535 | 2.899 | 364 | 14,36% |
| 6 | 2.564 | 2.707 | 143 | 5,58% |
| 8 | 2.165 | 1.499 | 666 | 30,77% |
| Total | 9.985 | 9.739 | 246 | 2,46% |

Baris 4 dan 6 menunjukkan kelebihan hitung, sedangkan baris 2 dan 8 kurang hitung; galat total kecil sebagian karena galat antarbaris saling meniadakan (pengamatan ringkasan ini dari Tabel A1). Penulis mengaitkan kurang hitung kuat pada baris 8 dengan sistem latihan yang lebih rapat, yang meningkatkan oklusi dan mengurangi dukungan paralaks. Setelah penyaringan jarak 5 m, 9.738 *landmark* dipertahankan; massa nominal 1.485,108 kg, dengan M(650) = 1.293,927 kg dan M(850) = 1.692,059 kg. Makalah tidak membandingkan taksiran massa dengan bobot panen terukur.

## Kelebihan dan Keterbatasan
Kelebihan: hasil pelacakan dan triangulasi menyatu dalam kerangka geografis sehingga keluaran langsung dapat dipetakan di SIG; hitungan dibandingkan dengan hasil panen fisik seluruh blok; diagnostik yang dilaporkan lengkap (statistik proyeksi ulang, besar koreksi pose, residu gerak relatif); pelacak dibandingkan dengan beberapa pembanding memakai metrik yang memisahkan deteksi dan asosiasi; dan data dinyatakan tersedia di Zenodo.

Keterbatasan yang dinyatakan penulis: kinerja menurun pada visibilitas buah rendah, kanopi rapat, dan belokan; metode kurang efektif bila *landmark* buah jarang; degradasi GNSS dapat mengurangi manfaat *prior* ENU; buah jauh atau terokluasi berat cenderung kurang terwakili; front-end tidak menyelesaikan reidentifikasi setelah buah menghilang lalu muncul kembali dari arah sebaliknya (misalnya pada belokan ujung baris), sehingga buah yang sama dapat memperoleh identitas baru; asumsi adegan statis dilanggar oleh ayunan cabang karena angin; penghitungan ganda buah yang terlihat dari dua sisi berlawanan pada lintasan baris yang bersebelahan belum dievaluasi secara sistematis (penulis hanya menyatakan pemeriksaan visual awal menunjukkan sebagian besar buah pada sistem *palmette* tidak terlihat dari kedua sisi); dan pemodelan bola serta kerapatan curah untuk massa hanya pendekatan orde pertama. Penulis juga menyatakan YOLOv9 dipilih tanpa pembandingan arsitektur detektor lain.

Menurut pembacaan ringkasan ini, evaluasi hanya mencakup satu blok, satu kultivar, dan satu lintasan, sehingga generalisasi belum teruji. Menurut pembacaan ringkasan ini, kualitas deteksi YOLOv9 (presisi, *recall*, mAP) tidak dilaporkan, dan pembandingan pelacak (Tabel 1) memakai satu segmen kebun; MOTA CoTracker (3,04%) paling rendah di antara pembanding kecuali SORT dan ByteTrack, sehingga keunggulannya hanya terlihat pada HOTA, AssA, dan IDF1. Menurut pembacaan ringkasan ini, kurang hitung total 2,46% tidak menunjukkan akurasi per baris (galat baris 3,20% sampai 30,77%), dan pelaporan hitungan 9.739 pada bagian hasil serta 9.738 untuk massa berbeda satu karena penyaringan jarak. Menurut pembacaan ringkasan ini, teks menyebut sekitar 29.000 bingkai, sedangkan optimasi memakai 11.307 pose, dan teks tidak menjelaskan selisih itu secara eksplisit (Tabel A2 menyebut rentang bingkai 1000:28.425 tanpa penjelasan lanjut).

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dengan mekanisme pelacakan titik (CoTracker3) yang diinisialisasi dari deteksi, lalu triangulasi multi-pandang dan penyempurnaan bersama pose-*landmark* dalam graf faktor, sehingga identitas buah ditentukan oleh posisi 3D pada kerangka dunia berreferensi GNSS. Kedua sisi baris dipindai dalam satu lintasan, tetapi identitas lintas sisi tidak ditangani secara eksplisit: penulis menyebut penghitungan ganda buah yang terlihat dari sisi berlawanan sebagai masalah terbuka dan menyatakan reidentifikasi lintas pandang berlawanan sebagai arah penelitian lanjutan. Hitungan tidak dilaporkan per kelas; hanya hitungan total dan per baris yang tersedia, dan tidak ada atribut kematangan.

Acuan hitung berupa panen fisik seluruh blok dan penghitungan manual semua buah. Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah rancangan pembanding pelacak berbasis metrik asosiasi (HOTA, AssA, IDF1) dan bukan MOTA saja, penggunaan triangulasi berbasis pose untuk memberikan identitas 3D, penapisan geometris (paralaks, jarak maksimum, galat proyeksi ulang), serta evaluasi galat per baris di samping galat total. Syaratnya adalah tersedianya pose kamera yang andal; makalah ini mengandalkan GNSS-VIO dan tidak menguji kondisi tanpa GNSS.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `bharti2026geo`.

Bharti dkk. (2026) mengusulkan alur estimasi hasil apel skala kebun yang menggabungkan deteksi YOLOv9, pelacakan titik CoTracker3, triangulasi multi-pandang pada pose GNSS-VIO, dan optimasi graf faktor iSAM2. Pada satu lintasan di blok apel Fuji, optimasi menurunkan galat proyeksi ulang rerata dari 40,31 menjadi 8,74 piksel, dan 9.739 apel hasil rekonstruksi dibandingkan dengan 9.985 apel hasil panen (kurang hitung 2,46%), dengan galat per baris berkisar 3,20% sampai 30,77%. Penulis menyatakan penghitungan ganda lintas sisi baris belum dievaluasi secara sistematis.

Catatan verifikasi data: angka pelacak tercantum pada Tabel 1; statistik proyeksi ulang di Bagian 4.2 dan keterangan Gambar 5; koreksi pose di Bagian 4.3; hitungan 9.739 terhadap 9.985 di Bagian 4.4; galat per baris di Tabel A1; massa di Bagian 4.5.2 dan Tabel 3; hiperparameter di Tabel 2 dan Tabel A2. Teks ekstraksi terbaca baik, termasuk isi tabel. Hal yang tidak dapat diverifikasi dari teks adalah jumlah bingkai yang dipakai pada pembandingan pelacak, presisi dan *recall* detektor, serta selisih antara sekitar 29.000 bingkai dan 11.307 pose. Selisih 246 apel dan persentase galat per baris tertulis di makalah, tidak dihitung ulang di sini.
