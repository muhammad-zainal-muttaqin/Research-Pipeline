# Simultaneous Localization and Mapping System for Agricultural Yield Estimation Based on Improved VINS-RGBD: A Case Study of a Strawberry Field

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yuan2024simultaneous` |
| Judul asli | Simultaneous Localization and Mapping System for Agricultural Yield Estimation Based on Improved VINS-RGBD: A Case Study of a Strawberry Field |
| Penulis | Yuan, Quanbo; Wang, Penggang; Luo, Wei; Zhou, Yongxu; Chen, Hongce; Meng, Zhaopeng |
| Tahun | 2024 |
| Venue | Agriculture Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [yuan2024simultaneous.pdf](../pdf/yuan2024simultaneous.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture14050784

## Gambaran Umum

Makalah ini mengusulkan sistem pemetaan dan lokalisasi serentak (*simultaneous localization and mapping*, SLAM) berbasis VINS-RGBD yang disempurnakan untuk merekonstruksi peta semantik 3D tanaman stroberi dan memperkirakan jumlah buah. Penyempurnaan mencakup penggantian titik sudut Shi–Tomasi dengan titik fitur L_SuperPoint (versi ringan SuperPoint), penambahan jaringan segmentasi semantik PP-LiteSeg-T, penyaringan pencilan berbasis radius, dan penyimpanan peta dengan Voxblox. Jumlah buah diperoleh dari awan titik semantik kelas buah melalui penyaringan bersyarat dan pencocokan bola dengan RANSAC.

Data diambil pada 16 Maret 2024 di kebun stroberi di Langfang, Provinsi Hebei, Tiongkok, dengan kamera Intel RealSense D435i dan kamera Sony CX450. Hasil utama: galat relatif rerata estimasi jumlah buah 10,87% pada lima sampel, mIoU segmentasi 73,2%, penghematan memori peta rata-rata 96,91% dengan Voxblox, dan penurunan rerata ATE sebesar 1,933 serta RPE sebesar 0,042 pada dua dataset publik dibandingkan titik sudut Shi–Tomasi.

Makalah ini bukan metode pencacahan lintas pandang dalam arti pencocokan identitas buah antarcitra. Satu peta 3D disatukan oleh SLAM, dan buah dihitung sebagai bola yang dicocokkan pada awan titik hasil penggabungan itu.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penulis menyatakan bahwa estimasi hasil panen penting untuk perencanaan produksi dan pengelolaan risiko, dan bahwa rekonstruksi 3D tanaman dengan SLAM visual memungkinkan pemahaman kondisi pertumbuhan secara intuitif. Penulis menilai penelitian SLAM pertanian sebelumnya terutama memperbaiki pemrosesan data dan menghasilkan peta yang hanya memuat informasi geometris tanpa semantik. Sebagian peta semantik yang ada disebut tidak berjalan waktu-nyata, padahal robot pemanen dan penyemprot membutuhkan persepsi waktu-nyata.

Penulis juga menyatakan bahwa sistem SLAM waktu-nyata pertanian yang ada masih kurang akurat dalam lokalisasi, dan bahwa penyimpanan peta awan titik berukuran besar menyulitkan pemetaan skala luas pada sumber daya terbatas. Lingkungan kebun stroberi disebut menimbulkan kehilangan pelacakan titik fitur.

## Ide Utama

Gagasan pokoknya adalah menyatukan lokalisasi visual-inersia berbantuan kedalaman (VINS-RGBD) dengan segmentasi semantik ringan sehingga setiap titik pada peta 3D berlabel kelas (buah, daun, latar), lalu menghitung buah dari titik berlabel buah saja. Dua perubahan lain ditujukan pada ketelitian dan beban penyimpanan: titik fitur belajar yang ringan (L_SuperPoint) untuk mengurangi kehilangan pelacakan dan memperbaiki lokalisasi, serta kompresi peta dengan Voxblox.

## Cara Kerja Langkah demi Langkah

```
RGB + depth + IMU -> VINS-RGBD (L_SuperPoint, VIO, loop DBoW2)
        |                          |
   keyframe -> PP-LiteSeg-T -> label semantik ke awan titik
                                   |
                  radius filter (r = 0,03; k = 10) + Voxblox
                                   |
        penyaringan bersyarat (kelas buah) -> RANSAC bola -> jumlah buah
```

### 1. Akuisisi dan penyiapan data

Kamera D435i merekam citra warna, citra kedalaman terjajar (*aligned depth*), dan data IMU dengan ROS rosbag untuk citra jarak jauh; Sony CX450 dipakai untuk citra jarak dekat buah. Lima rekaman stroberi dicatat pada Tabel 1 (misalnya Dataset 1: 3.030 pesan kedalaman, 3.034 pesan warna, 14.986 pesan IMU). Dataset segmentasi terdiri dari 752 citra jarak jauh (640 × 480) dan 350 citra jarak dekat (1920 × 1080) sehingga total 1.102 citra, seluruhnya diubah ke 640 × 480. Anotasi memakai LabelMe dengan tiga kelas: buah, daun, dan latar. Pembagian data latih, validasi, dan uji 7:2:1. Kultivar stroberi tidak dilaporkan.

### 2. Segmentasi semantik

PP-LiteSeg-T berstruktur pengode–penyandi dengan tiga komponen: *Flexible Lightweight Decoder* (FLD), *Unified Attention Fusion Module* (UAFM) berbasis atensi spasial, dan *Simple Pyramid Pooling Module* (SPPM). Pelatihan pembanding berlangsung 100 epoch dengan laju belajar 0,01 dan dioptimalkan dengan TensorRT. Keyframe dari VINS-RGBD disegmentasi lalu labelnya dimasukkan ke awan titik.

### 3. VINS-RGBD yang disempurnakan

Sistem terdiri dari pemrosesan pengukuran, inisialisasi (*structure from motion* dan pra-integrasi IMU), VIO lokal, segmentasi semantik, serta deteksi loop dan pemetaan. L_SuperPoint menggantikan titik Shi–Tomasi; jaringannya terdiri dari lima lapis, empat lapis terakhir memakai konvolusi terpisah-kedalaman (*depth-wise separable*), dengan ReLU6 pada konvolusi kedalaman dan fungsi linear pada konvolusi titik. Deskriptor dicocokkan dengan KNN dan titik tak cocok disaring dengan RANSAC. Gambar dibagi menjadi beberapa wilayah dan hanya titik dengan laju pelacakan tertinggi dipertahankan. Kedalaman titik fitur diambil dari citra kedalaman, dan titik di luar jangkauan sensor diperkirakan dengan triangulasi. Penutupan loop memakai DBoW2.

### 4. Kompresi dan penyimpanan peta

Filter pencilan radius menghapus titik yang jumlah tetangganya dalam radius $r$ kurang dari $k$; di sini $r = 0{,}03$ dan $k = 10$. Voxblox menyimpan peta sebagai medan jarak bertanda terpotong (TSDF) dengan *voxel hashing*.

### 5. Estimasi jumlah buah

Titik berlabel buah diekstraksi dengan penyaringan bersyarat dari pustaka PCL, lalu bola dicocokkan dengan RANSAC di CloudCompare 2.12.2; setiap bola dianggap satu buah. Galat relatif $\delta = |N_p - N_t| / N_t \times 100\%$.

## Eksperimen dan Hasil

Perangkat keras evaluasi: Intel Core i7-7800X dan NVIDIA GTX 1080 Ti, PyTorch 1.9, Ubuntu 18.04.

### Estimasi jumlah buah (Tabel 5)

| Sampel | Nilai aktual | Nilai prediksi | Galat relatif (%) |
|---|---|---|---|
| 1 | 16 | 14 | 12,5 |
| 2 | 33 | 32 | 3,03 |
| 3 | 43 | 39 | 9,30 |
| 4 | 59 | 51 | 13,56 |
| 5 | 69 | 58 | 15,94 |
| Rerata | - | - | 10,87 |

Seluruh prediksi lebih rendah daripada nilai aktual. Penulis mengaitkan galat dengan penghalangan oleh daun dan derau awan titik yang mengganggu pencocokan bola. Cara memperoleh nilai aktual (misalnya hitung manual di lapangan) tidak dijelaskan pada teks.

### Segmentasi (Tabel 4)

PP-LiteSeg-T (encoder STDC1) mencapai mIoU 73,2% dan 228,3 FPS. Pembanding terdekat: STDC1-Seg 73,2% dan 198,1 FPS; STDC2-Seg 74,1% dan 153,9 FPS; BiSeNetV2 73,7% dan 124,5 FPS. Metrik per kelas tidak dilaporkan pada teks selain kurva presisi–*recall* (Gambar 9, tidak terbaca dari teks).

### Titik fitur

| Metode | Perubahan iluminasi | Perubahan sudut pandang | Galat posisi (PE) | FPS |
|---|---|---|---|---|
| L_SuperPoint | 66,3% | 54,7% | 1,10 | 9,2 |
| SuperPoint | 67,8% | 55,3% | 1,05 | 2,3 |
| FAST | 60,3% | 51,0% | 1,93 | 9,5 |
| Harris | 62,5% | 58,5% | 1,09 | 1,4 |

### Akurasi lokalisasi (Tabel 8, satuan meter)

| Metode | ATE Dataset 1 | RPE Dataset 1 | ATE Dataset 2 | RPE Dataset 2 | ATE rerata | RPE rerata |
|---|---|---|---|---|---|---|
| Shi–Tomasi | 5,164 | 0,267 | 4,456 | 0,204 | 4,810 | 0,236 |
| L_SuperPoint | 3,512 | 0,241 | 2,241 | 0,146 | 2,877 | 0,194 |

Dataset 1 berasal dari Tsukuba Challenge 2022 dan Dataset 2 dari Kampus Ikuta Universitas Meiji; keduanya bukan data stroberi dan diperoleh dengan perangkat genggam.

### Memori dan waktu-nyata

Filter radius menurunkan konsumsi memori rata-rata 5,59% dan Voxblox rata-rata 96,91% (Tabel 6). Contoh: peta semantik tiga baris 354,7 MB menjadi 335,6 MB setelah penyaringan dan 9,8 MB dengan Voxblox (penghematan 97,23%). Setiap baris stroberi sepanjang 8 m. Pemrosesan per bingkai: deteksi dan pelacakan fitur 13,61 ms, segmentasi 8,67 ms (Tabel 7), dibandingkan laju video 30 bingkai per detik.

## Kelebihan dan Keterbatasan

Kelebihan menurut makalah: peta semantik waktu-nyata pada tanaman nyata di lapangan, kompresi peta yang besar, dan lokalisasi yang lebih baik dengan titik fitur belajar.

Keterbatasan yang dinyatakan penulis: akurasi lokalisasi hanya diuji pada dua dataset publik karena tidak tersedia kebenaran dasar presisi di kebun sendiri, dan lintasan estimasi masih mengalami drift; segmentasi keliru akibat penghalangan daun, cahaya, dan galat sensor; terjadi *overfitting* ketika model diterapkan ke dataset stroberi lain karena data latih terbatas; kerja lanjutan mencakup LiDAR, RTK, GPS, dan NeRF.

Menurut pembacaan ringkasan ini: estimasi jumlah buah hanya diuji pada lima sampel tanpa uraian cara penentuan nilai aktual, dan semuanya menghasilkan hitungan kurang, yang menunjukkan bias hitungan rendah akibat oklusi. Keterhubungan identitas buah pada pandangan berbeda tidak dievaluasi terpisah; hitungan bergantung pada kualitas peta gabungan. Hitungan tidak dilaporkan per kelas atau per tingkat kematangan.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali melalui rekonstruksi 3D: pose kamera dari VINS-RGBD dan kedalaman menempatkan setiap pengamatan pada satu kerangka koordinat, sehingga buah yang sama dari pandangan berbeda terakumulasi pada titik ruang yang sama dan dihitung sekali sebagai satu bola hasil pencocokan RANSAC. Tidak ada pelacakan identitas eksplisit atau pencocokan citra-ke-citra untuk buah; identitas ditentukan oleh posisi spasial pada peta.

Hitungan tidak dilaporkan per kelas; hanya jumlah buah total. Acuan hitungnya berupa "nilai aktual" tanpa penjelasan asal-usulnya pada teks, dan bukan hasil panen atau anotasi citra yang dinyatakan. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah gagasan menggabungkan pengamatan lintas pandang pada satu peta metrik sehingga duplikasi dicegah oleh geometri; batasannya, tandan sawit lebih besar, tertanam di antara pelepah, dan memerlukan kedalaman rentang jauh, sedangkan makalah ini hanya menguji tanaman rendah pada jarak dekat. Pemindahan ini merupakan inferensi dari ringkasan ini, bukan klaim makalah.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `yuan2024simultaneous`.

Yuan dkk. mengusulkan sistem VINS-RGBD yang disempurnakan dengan titik fitur L_SuperPoint dan segmentasi semantik PP-LiteSeg-T untuk membangun peta semantik 3D kebun stroberi, dengan jumlah buah diperkirakan lewat penyaringan bersyarat dan pencocokan bola RANSAC pada awan titik berlabel buah. Pada lima sampel, galat relatif rerata jumlah buah adalah 10,87%, mIoU segmentasi 73,2%, dan Voxblox menghemat memori peta rata-rata 96,91%.

Catatan verifikasi data: Galat 10,87% dan nilai per sampel ada pada Tabel 5; mIoU 73,2% dan FPS 228,3 pada Tabel 4 dan Seksi 3.2; ATE dan RPE pada Tabel 8 (selisih rerata 4,810 − 2,877 = 1,933 dan 0,236 − 0,194 = 0,042 cocok dengan teks); memori pada Tabel 6; waktu per bingkai pada Tabel 7. Teks mencantumkan penghematan memori 96,91% pada abstrak dan Seksi 3.3.2 tetapi 96,61% pada Seksi 4 dan Seksi 5; ringkasan ini memakai 96,91% yang sesuai dengan Tabel 6. Jumlah pohon atau tanaman per sampel, kultivar, dan cara penentuan nilai aktual tidak dilaporkan. Kurva presisi–*recall* dan gambar rekonstruksi tidak terbaca dari teks.
