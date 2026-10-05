## Gambaran Umum

Makalah ini mengusulkan metode penghitungan tandan pisang dan estimasi hasil kebun pisang dengan pelacak DeepSORT dan citra RGB-D. Detektor YOLO-Banana, yang dikembangkan pada karya terdahulu penulis, mendeteksi tandan dan tangkai pisang. Berat tiap tandan dihitung dengan model dari kedalaman dan volume dari karya terdahulu yang sama. DeepSORT (filter Kalman, algoritma Hungarian, jarak Mahalanobis dan jarak kosinus tampilan) memberi identitas lintas bingkai, lalu tiga batasan (jumlah pelacakan berturut-turut, rentang jarak, dan rentang berat) mengendalikan kapan tandan dihitung.

Sistem dipasang pada kendaraan berantai kendali jarak jauh dengan kamera kedalaman Intel RealSense D435i dan diuji di kebun pisang Guangdong Academy of Agricultural Sciences serta lokasi demonstrasi di Kota Jiangmen, Provinsi Guangdong. Kultivar yang dipelajari adalah pisang Cavendish AAA dan turunan budidayanya.

Hasil utama: tingkat keberhasilan penghitungan tandan 96,82% (rerata per baris) dan akurasi estimasi hasil seluruh kebun 97,25% pada enam baris dengan 61 tandan menurut Tabel 1.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi hasil kebun umumnya memakai pengambilan sampel acak sederhana: pohon sampel dinilai, jumlah buah dikalikan berat rerata, lalu diekstrapolasi. Cara itu memakan tenaga dan waktu serta bergantung pada pengalaman pelaksana. Penulis menyatakan bahwa pada penelitian penghitungan berbasis citra, masalah penghitungan ganda antarcitra sering tidak diperhatikan, dan bahwa untuk kebun pisang belum ada studi estimasi hasil berbasis penghitungan dari video; pelacakan tandan pisang lintas bingkai belum diteliti. Di video, oklusi acak dan pencahayaan tidak merata menyebabkan pelacakan gagal dan penghitungan berlebih.

## Ide Utama

Estimasi hasil dibentuk sebagai model hibrida penghitungan dan berat: pelacakan DeepSORT memberi identitas tiap tandan, model berat per tandan memberi nilai berat, dan hasil akhir adalah jumlah dan berat kumulatif. Tiga batasan pada proses penghitungan mengurangi kesalahan akibat pergantian ID, tandan baris lain, dan tandan yang baru sebagian terlihat.

Berat tandan dihitung dengan Persamaan 1 yang diambil dari karya terdahulu (model $h + V_p$, R² 0,8143 menurut makalah): berat bergantung pada tinggi tandan $h$ dan volume terestimasi $V_p$, dengan $V_p = 0{,}5 \times w \times h^2 \times p$ ($w$ lebar tandan, $p$ rasio piksel efektif terhadap luas kotak deteksi). Koefisien persamaan pada teks ekstraksi tidak terbaca utuh dan tidak disalin di sini.

## Cara Kerja Langkah demi Langkah

```
 RGB + depth --> registrasi --> YOLO-Banana (tandan, tangkai)
                                     |
                      berat tandan (Persamaan 1)   DeepSORT (Kalman + Hungarian)
                                     |                      |
                                     +--------> tiga batasan penghitungan
                                                            |
                                                  jumlah dan berat kumulatif
```

### 1. Akuisisi data

Sistem visi terdiri atas kamera RealSense D435i pada sisi kiri depan kendaraan, dengan lensa tegak lurus terhadap arah maju, serta laptop Intel Core i7-9750H, RAM 16 GB, dan NVIDIA GeForce RTX 2070. Citra RGB berukuran 1280 × 720 piksel dan citra kedalaman 848 × 480 piksel; jangkauan operasi kamera 0,28 sampai 3 m. Data latih diambil pada kondisi mendung, cerah dengan cahaya belakang, dan cerah dengan cahaya depan, sedangkan percobaan panen dilakukan pada kondisi mendung. Jumlah citra latih dan jumlah video tidak dilaporkan pada makalah ini; rujukan diberikan ke karya terdahulu.

### 2. Deteksi dan estimasi berat per tandan

YOLO-Banana mendeteksi tandan dan tangkai pada citra RGB-D hasil registrasi. Berat tandan dihitung dengan Persamaan 1 tanpa pelatihan ulang.

### 3. Pelacakan dengan DeepSORT

Keadaan filter Kalman memuat delapan unsur: titik pusat kotak $(u, v)$, rasio aspek $\gamma$, tinggi $h$, dan keempat kecepatannya. Biaya asosiasi adalah gabungan berbobot jarak Mahalanobis dan jarak kosinus minimum fitur tampilan (Persamaan 3, bobot $\lambda$). Algoritma Hungarian melakukan asosiasi bertingkat, lalu pasangan yang belum cocok dicocokkan ulang dengan IoU. Lintasan dibedakan menjadi terkonfirmasi dan belum terkonfirmasi. Tangkai pisang dilacak tetapi tidak dihitung karena tertutup daun dan cabang.

### 4. Tiga batasan penghitungan

1. Hanya tandan yang terlacak berhasil setelah $t$ perubahan posisi berturut-turut yang dihitung (pada percobaan $t = 6$), agar pergantian ID sesaat tidak dihitung.
2. Jarak tandan dari titik asal koordinat kamera dibatasi agar tandan baris jauh tidak dihitung ganda.
3. Berat terestimasi harus berada dalam rentang 15 sampai 35 kg sehingga tandan dihitung dan ditimbang hanya setelah tampak utuh.

Parameter lain: umur maksimum lintasan (Max_age) 60 dan jumlah bingkai pencocokan berturut-turut $n = 3$. Teks tidak konsisten soal rentang jarak: Bagian 3 menyebut 1,5 sampai 3,5 m, sedangkan Bagian 3.2 menyebut 1,5 sampai 2,5 m. Rentang jarak dan berat dirujuk dari buku budidaya pisang.

## Eksperimen dan Hasil

### Penghitungan tandan (Gambar 8)

Empat kondisi dibandingkan terhadap jumlah sebenarnya pada enam baris: tanpa batasan, batasan (1), batasan (1)(2), dan batasan (1)(2)(3). Menurut teks, hitungan semakin mendekati nilai sebenarnya seiring penambahan batasan, dan rerata akurasi per baris meningkat hingga 96,82%. Batasan jarak paling banyak mengurangi hitungan ganda. Hasil per baris hanya tersaji sebagai grafik, sehingga angkanya tidak dapat diverifikasi dari teks ekstraksi.

### Estimasi hasil (Tabel 1)

Pembanding adalah prediksi empiris tiga petani berpengalaman (dirata-ratakan).

| Baris | Jumlah tandan | Berat sebenarnya (kg) | Prediksi empiris (kg) | Akurasi empiris (%) | Prediksi model (kg) | Akurasi model (%) |
|---|---|---|---|---|---|---|
| 1 | 8 | 176,72 | 195 | 89,66 | 167,5 | 94,78 |
| 2 | 10 | 192,85 | 211 | 90,59 | 206,13 | 93,11 |
| 3 | 9 | 176,34 | 163 | 92,44 | 189,36 | 92,62 |
| 4 | 13 | 249,91 | 277 | 89,16 | 263,51 | 94,59 |
| 5 | 11 | 169,2 | 178 | 94,8 | 154,25 | 91,16 |
| 6 | 10 | 198,67 | 182 | 91,61 | 214,94 | 91,81 |
| Total | 61 | 1163,69 | 1206 | 96,36 | 1195,69 | 97,25 |

Rerata akurasi per baris adalah 91,37% (empiris) dan 93,01% (model). RMSE adalah 17,91 kg (empiris) dan 12,81 kg (model). Selang kepercayaan 95% untuk selisih nilai sebenarnya dan prediksi adalah [−18,80; 4,02] kg (empiris) dan [−10,19; 6,15] kg (model). Hitungan tandan pada Tabel 1 tampak sebagai jumlah sebenarnya; makalah tidak menyajikan hitungan sistem per baris dalam tabel.

### Perbandingan dengan studi lain (Tabel 2)

Makalah menempatkan hasilnya pada tingkat menengah-ke-atas dibandingkan studi estimasi hasil lain, misalnya jeruk, markisa, stroberi, bunga kapas, dan tomat tandan, tetapi metrik dan satuan berbeda antar studi sehingga perbandingan bersifat indikatif.

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: estimasi hasil menggabungkan penghitungan dan berat sehingga cocok untuk buah berukuran besar; sistem bersifat modular; dan hasilnya lebih dekat ke berat sebenarnya daripada prediksi empiris petani.

Keterbatasan yang dinyatakan penulis: parameter berat dan jarak tanam hanya sesuai dengan Cavendish AAA sehingga varietas lain memerlukan pembaruan; kedua kebun diuji pada kondisi mendung; kondisi cuaca kompleks (hujan, angin kencang, kabut, kelembapan tinggi) belum dieksplorasi; oklusi penuh dapat memutus pelacakan sementara; dan medan tidak rata memengaruhi akurasi pelacakan.

Menurut pembacaan ringkasan ini: (a) uji akhir hanya mencakup enam baris dan 61 tandan, sehingga selang kepercayaan didasarkan pada sampel kecil; (b) tiga batasan dikalibrasi untuk satu varietas dan jarak tanam, sehingga kinerja pada pengaturan lain tidak terukur; (c) akurasi total 97,25% dihitung pada berat, sehingga kesalahan penghitungan dan kesalahan berat per tandan dapat saling meniadakan; (d) tidak ada hitungan per kelas; (e) tidak ada ukuran pergantian ID seperti IDSW atau IDF1.

## Kaitan dengan Tinjauan main6

Makalah ini menangani tandan yang tampak pada banyak bingkai video dengan pelacakan multi-objek DeepSORT (filter Kalman, algoritma Hungarian, fitur tampilan), ditambah tiga batasan penghitungan: jumlah pelacakan berturut-turut, rentang jarak berdasarkan kedalaman, dan rentang berat berdasarkan volume dari kedalaman. Identitas dipertahankan hanya sepanjang urutan waktu satu pergerakan kendaraan di sepanjang baris; tidak ada pencocokan antar-sisi pohon. Hitungan tidak dilaporkan per kelas. Acuan hitungnya adalah jumlah sebenarnya per baris (dan berat sebenarnya), sedangkan metode penentuan acuan jumlah tidak dirinci di teks.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pemakaian kedalaman untuk membatasi hitungan pada jarak tertentu agar tandan baris lain tidak dihitung, serta penerimaan hitungan hanya setelah tandan tampak utuh melalui ukuran fisik. Kedua gagasan bergantung pada kalibrasi spesifik jenis tandan dan jarak tanam. Gagasan itu searah dengan perhatian pada sensor kedalaman, tetapi tidak menyelesaikan pencocokan identitas lintas sisi yang terpisah dalam ruang.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `zhou2025yield`.

Zhou dkk. (2025) mengusulkan estimasi hasil kebun pisang yang menggabungkan detektor YOLO-Banana, estimasi berat tandan dari citra RGB-D, pelacak DeepSORT, dan tiga batasan penghitungan (jumlah pelacakan berturut-turut, rentang jarak, rentang berat). Pada enam baris dengan 61 tandan, tingkat keberhasilan penghitungan mencapai 96,82% dan akurasi estimasi hasil total 97,25%, dengan RMSE 12,81 kg dibandingkan 17,91 kg untuk prediksi empiris petani.

Catatan verifikasi data: angka estimasi hasil ada pada Tabel 1 (Bagian 3.4); 96,82% dan parameter pelacakan pada Bagian 3 dan 3.3; hitungan per baris hanya ada pada Gambar 8 sehingga tidak terbaca dari teks. Rumus berat tandan (Persamaan 1) rusak pada ekstraksi sehingga koefisiennya tidak dikutip. Rentang jarak tidak konsisten antar bagian (1,5–3,5 m dan 1,5–2,5 m). Jumlah citra latih, jumlah dan durasi video, serta cara penentuan hitungan sebenarnya tidak dilaporkan; data dinyatakan tersedia atas permintaan penulis korespondensi.
