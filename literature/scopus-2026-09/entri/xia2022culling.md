# Culling Double Counting in Sequence Images for Fruit Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xia2022culling` |
| Judul asli | Culling Double Counting in Sequence Images for Fruit Yield Estimation |
| Penulis | Xia, Xue; Chai, Xiujuan; Zhang, Ning; Zhang, Zhao; Sun, Qixin; Sun, Tan |
| Tahun | 2022 |
| Venue | Agronomy |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple, citrus |

## Tautan Akses
- PDF: [xia2022culling.pdf](../pdf/xia2022culling.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy12020440

## Gambaran Umum

Makalah ini mengusulkan kerangka estimasi hasil buah dari rangkaian citra (*sequence images*) yang diambil dari video kebun. Kerangka tersebut terdiri atas detektor tanpa jangkar (*anchor-free*) CenterNet untuk mendeteksi buah pada tiap citra, model pencocokan potongan citra (*patch matching*) untuk mengenali buah yang sama pada citra berurutan, dan algoritma Kuhn–Munkres untuk menetapkan pasangan secara satu-ke-satu. Tujuannya adalah menghilangkan penghitungan ganda (*double counting*) buah yang tampak pada lebih dari satu citra.

Data berupa video yang direkam dengan kamera utama iPhone 8 pada resolusi 1080 × 1920 piksel di kebun apel (XingCheng, Tiongkok) dan kebun jeruk (NanNing, Tiongkok). Dari video diekstraksi bingkai kunci (*keyframes*) menjadi 120 rangkaian citra apel dan 120 rangkaian citra jeruk, yang dibagi sama besar untuk pelatihan dan pengujian.

Hasil utama: CenterNet mencapai mAP 0,939 pada IoU 0,5 (data milik penulis, apel dan jeruk). Model pencocokan memperoleh F1-score 0,816 untuk apel dan 0,864 untuk jeruk, lebih tinggi daripada pembanding DeepCompare (0,544 dan 0,737). Hitungan akhir pada rangkaian uji sesuai dengan acuan, dengan R² 0,9737 untuk apel dan 0,9562 untuk jeruk.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi hasil buah secara konvensional bergantung pada pengambilan sampel acak sebagian pohon (contoh dalam makalah: 5% atau 10%) yang dihitung manual, lalu diekstrapolasi ke seluruh kebun. Cara ini memakan tenaga dan waktu serta rentan terhadap kelelahan penghitung. Estimasi otomatis berbasis visi dipandang lebih murah dan efisien.

Penulis menyatakan bahwa banyak penelitian terdahulu meningkatkan kinerja estimasi pada citra tunggal, tetapi tidak memperhitungkan hubungan buah antarcitra yang berdekatan dalam suatu rangkaian. Akibatnya, buah yang sama dihitung lebih dari sekali. Penulis juga menyatakan bahwa model pencocokan potongan yang ada, seperti DeepCompare, hanya menyelesaikan masalah penugasan maksimum, bukan penugasan optimal, sehingga satu buah dapat dipasangkan dengan banyak buah lain dan hitungan ganda tidak dikoreksi dengan benar.

## Ide Utama

Gagasan utamanya adalah memisahkan pekerjaan menjadi tiga langkah: mendeteksi buah pada tiap citra, mengenali buah yang sama pada citra berurutan, dan mengoreksi hitungan menurut jumlah buah ganda. Pencocokan diperlakukan sebagai masalah penugasan pada graf bipartit, sehingga setiap buah pada satu citra dipasangkan paling banyak dengan satu buah pada citra berikutnya. Penulis menggunakan algoritma Kuhn–Munkres (*Hungarian method*) pada lapisan keputusan untuk mengubah matriks kemiripan menjadi pencocokan optimal.

Hitungan total rangkaian citra $S$ dinyatakan pada Persamaan 1:

$$count(S) = \sum_{i=1}^{n} count(s_i) - \sum_{i=1}^{n-1} count(s_i \cap s_{i+1})$$

dengan $n$ jumlah citra dalam rangkaian, $s_i$ citra ke-$i$, dan $count(s_i \cap s_{i+1})$ jumlah buah ganda antara dua citra berurutan. Dengan rumus ini, pengurangan hanya dilakukan antara citra yang bersebelahan.

## Cara Kerja Langkah demi Langkah

```
 Rangkaian citra --> CenterNet --> kotak buah per citra
                                        |
                                        v
                       potongan 94 x 94, dua citra berurutan
                                        |
                                        v
                    lapisan pencocokan --> matriks kemiripan
                                        |
                                        v
                    lapisan keputusan (Kuhn-Munkres, satu-ke-satu)
                                        |
                                        v
              jumlah buah ganda --> koreksi hitungan (Persamaan 1)
```

### 1. Akuisisi dan anotasi data

Video direkam dengan iPhone 8 (1080 × 1920 piksel) sambil berjalan menyusuri baris pohon, pada beberapa hari cerah dari pagi hingga senja agar intensitas cahaya bervariasi. Bingkai kunci diekstraksi dari video, menghasilkan 120 rangkaian citra apel dan 120 rangkaian citra jeruk; masing-masing dibagi dua sama besar untuk pelatihan dan pengujian. Kultivar tidak dilaporkan.

Anotasi dilakukan dengan dua alat yang dikembangkan penulis. Alat pertama menandai kotak buah (min-x, min-y, max-x, max-y). Alat kedua (*pair tool*) menandai nomor urut buah yang sama pada citra berdekatan. Dua teknisi data menghitung acuan: yang pertama menghitung acuan dengan mengurangkan buah ganda dari total buah dalam rangkaian, dan yang kedua memeriksa ulang angkanya.

### 2. Deteksi buah dengan CenterNet

CenterNet memperlakukan deteksi sebagai prediksi titik kunci dan regresi kotak pembatas, tanpa jangkar dan tanpa *non-maximum suppression*. Peta fitur akhir memiliki tiga cabang: peta panas titik kunci (tiap objek diwakili kernel Gaussian), *offset* lokal, dan ukuran objek. Parameter awal pelatihan (Tabel 2): ukuran masukan 512 × 512, 1000 epoch, ukuran batch 16, optimizer Adam, momentum 0,9, laju belajar awal 10⁻⁴, *weight decay* 0,0001, deteksi maksimum 100.

### 3. Model pencocokan buah

Model terdiri atas lapisan pencocokan dan lapisan keputusan. Masukan adalah potongan citra dari wilayah buah hasil CenterNet; setiap pasangan potongan diubah ukurannya menjadi 94 × 94 piksel dan digabungkan sebelum masuk ke lapisan pencocokan. Lapisan pencocokan (konvolusi, lapisan terhubung penuh, softmax) menghasilkan skor kemiripan dalam rentang (0, 1) untuk tiap pasangan potongan; pasangan dianggap cocok bila skor lebih besar dari 0 menurut Persamaan 3. Fungsi kerugian adalah *cross-entropy*.

Lapisan pencocokan dilatih dari awal dengan ukuran batch 16, laju belajar tetap 0,0005, 300 epoch, optimizer Adam, dan seluruh pasangan diubah menjadi skala abu-abu. Data latih terdiri atas 3.066 pasang potongan apel dan 6.028 pasang potongan jeruk dari data latih rangkaian citra.

### 4. Keputusan satu-ke-satu dengan Kuhn–Munkres

Skor kemiripan dari matriks dipakai sebagai bobot sisi pada graf bipartit antara buah pada citra $s_i$ dan $s_{i+1}$. Algoritma Kuhn–Munkres mencari pencocokan optimal, dan jumlah pasangan hasilnya menjadi jumlah buah ganda terkoreksi antara kedua citra.

### 5. Perangkat percobaan

Percobaan dijalankan pada GPU NVIDIA TITAN Xp 16 GB, CPU Intel Core i7 7700, RAM 32 GB, Ubuntu 16.04, CUDA 10.0, cuDNN v7.5, PyTorch 1.0.

## Eksperimen dan Hasil

### Deteksi

Untuk deteksi dipilih secara acak 1.199 citra apel (10.177 buah) dan 2.849 citra jeruk (34.470 buah) dari rangkaian citra. Data publik ACFR-Apple (1.120 citra apel, 5.765 buah) dipakai sebagai pembanding. Pembagian: apel milik penulis 1.078 latih dan 121 uji; jeruk 2.563 latih dan 286 uji; ACFR-Apple 1.008 latih dan 112 uji.

| Dataset | Kelas | IoU | AP | mAP |
|---|---|---|---|---|
| Milik penulis | Apel | 0,5 | 0,927 | 0,939 |
| Milik penulis | Jeruk | 0,5 | 0,951 | 0,939 |
| Milik penulis | Apel | 0,6 | 0,862 | 0,898 |
| Milik penulis | Jeruk | 0,6 | 0,933 | 0,898 |
| Milik penulis | Apel | 0,7 | 0,713 | 0,790 |
| Milik penulis | Jeruk | 0,7 | 0,866 | 0,790 |
| ACFR-Apple | Apel | 0,5 | 0,924 | tidak ada |
| ACFR-Apple | Apel | 0,6 | 0,866 | tidak ada |
| ACFR-Apple | Apel | 0,7 | 0,744 | tidak ada |

### Pencocokan

Evaluasi memakai 20 pasang citra berdekatan apel (828 buah) dan 20 pasang citra berdekatan jeruk (793 buah) dari data uji. Pembanding adalah DeepCompare. Metrik adalah rerata akurasi, presisi, *recall*, dan F1 (Tabel 4).

| Kelas | Metode | Akurasi | Presisi | Recall | F1 |
|---|---|---|---|---|---|
| Apel | DeepCompare | 0,937 | 0,503 | 0,592 | 0,544 |
| Apel | Model penulis | 0,975 | 0,793 | 0,840 | 0,816 |
| Jeruk | DeepCompare | 0,966 | 0,701 | 0,776 | 0,737 |
| Jeruk | Model penulis | 0,985 | 0,853 | 0,875 | 0,864 |

### Estimasi hasil

Pipeline diuji pada 20 rangkaian citra apel (910 buah) dan 20 rangkaian citra jeruk (844 buah). R² antara hitungan prediksi dan acuan adalah 0,9737 (apel) dan 0,9562 (jeruk); RMSE adalah 10,0920 (apel) dan 4,2544 (jeruk). Waktu komputasi rerata adalah 5,33 menit per rangkaian citra uji.

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: penugasan satu-ke-satu mencegah satu buah dipasangkan dengan banyak buah sehingga hitungan ganda berkurang; kerangka diuji pada dua komoditas; dan penulis menyatakan bahwa kerangka ini tidak menghalangi perluasan ke tanaman lain.

Keterbatasan yang dinyatakan penulis:
- Pencocokan belum memenuhi kebutuhan waktu-nyata, sebab seluruh potongan dibandingkan satu sama lain secara *brute force*; rerata 5,33 menit per rangkaian uji.
- Model pencocokan memakai potongan skala abu-abu sehingga informasi warna belum dimanfaatkan.
- Kerangka hanya menangani pandangan satu sisi pohon. Buah pada sisi lain atau yang terhalang cabang dan daun dapat tidak terdeteksi; penulis menyebut pengambilan citra dari kedua sisi pohon dan penggabungan kemiripan fitur lokal dan global sebagai pekerjaan lanjutan.
- Data latih tidak mencakup semua kondisi gangguan; kebun dengan jarak tanam tidak teratur dapat memasukkan buah dari baris lain ke dalam citra.

Menurut pembacaan ringkasan ini: (a) pengurangan pada Persamaan 1 hanya mempertimbangkan pasangan citra yang bersebelahan, sehingga buah yang muncul kembali setelah menghilang dari beberapa citra tidak ditangani secara eksplisit; (b) pencocokan dievaluasi pada 20 pasang citra per komoditas, jumlah yang kecil; (c) acuan hitungan adalah anotasi citra, bukan panen; (d) tidak ada hasil per kelas atribut seperti kematangan.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang tampak lebih dari sekali pada citra berurutan dari video yang direkam menyusuri baris pohon. Mekanismenya adalah deteksi per citra, pencocokan pasangan potongan buah antara dua citra yang bersebelahan dengan jaringan konvolusi, dan penugasan satu-ke-satu dengan algoritma Kuhn–Munkres, lalu pengurangan jumlah buah ganda dari total. Mekanisme ini bukan pelacakan multi-objek dengan identitas yang bertahan lintas banyak bingkai, dan juga bukan rekonstruksi 3D.

Hitungan tidak dilaporkan per kelas atribut; apel dan jeruk dievaluasi sebagai dua komoditas terpisah. Acuan hitungnya adalah anotasi citra: dua teknisi menghitung buah dengan alat pasangan, bukan hasil panen atau hitung lapangan. Untuk tandan kelapa sawit multi-sisi, yang dapat dipindahkan adalah pola pencocokan pasangan dengan penugasan optimal satu-ke-satu dan persamaan koreksi hitungan. Penulis sendiri menyatakan bahwa penanganan dua sisi pohon, yang paling mendekati kebutuhan multi-sisi, belum dikerjakan dan menjadi pekerjaan lanjutan. Pencocokan lintas sisi akan menghadapi perbedaan penampakan yang jauh lebih besar daripada citra berurutan pada video.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `xia2022culling`.

Xia dkk. (2022) mengusulkan kerangka estimasi hasil buah dari rangkaian citra video yang menggabungkan detektor CenterNet dengan model pencocokan potongan buah berbasis algoritma Kuhn–Munkres untuk menghilangkan penghitungan ganda antara citra berurutan. Pada data apel dan jeruk, model pencocokan memperoleh F1 0,816 dan 0,864 (pembanding DeepCompare 0,544 dan 0,737), dan hitungan akhir pada rangkaian uji menunjukkan R² 0,9737 (apel) dan 0,9562 (jeruk) terhadap acuan hasil anotasi. Metode ini hanya menangani satu sisi pohon dan belum berjalan dalam waktu-nyata.

Catatan verifikasi data: mAP 0,939/0,898/0,790 dan AP per kelas ada pada Tabel 3 serta bagian Kesimpulan; angka pencocokan pada Tabel 4; R², RMSE, dan waktu 5,33 menit pada Bagian 3.4; jumlah data pada Bagian 2.1, 3.2, dan 3.3. Teks ekstraksi terbaca baik, tetapi gambar (termasuk Gambar 13 dan 14) tidak tersedia sehingga tidak diperiksa. Jumlah total citra pada 240 rangkaian dan panjang tiap rangkaian tidak dilaporkan. Tabel 3 memuat mAP per tingkat IoU untuk data milik penulis saja. Nama kultivar apel dan jeruk tidak dilaporkan.
