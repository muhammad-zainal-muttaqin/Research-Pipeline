# Object-Detection from Multi-View remote sensing Images: A case study of fruit and flower detection and counting on a central Florida strawberry farm

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zheng2023object` |
| Judul asli | Object-Detection from Multi-View remote sensing Images: A case study of fruit and flower detection and counting on a central Florida strawberry farm |
| Penulis | Zheng, Caiwang; Liu, Tao; Abd-Elrahman, Amr; Whitaker, Vance M.; Wilkinson, Benjamin |
| Tahun | 2023 |
| Venue | International Journal of Applied Earth Observation and Geoinformation |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [zheng2023object.pdf](../pdf/zheng2023object.pdf)
- DOI resmi: https://doi.org/10.1016/j.jag.2023.103457

## Gambaran Umum
Makalah ini mengusulkan metode deteksi dan pencacahan objek kecil langsung dari citra mentah multi-pandang (*multi-view raw images*), bukan dari citra ortomosaik hasil *Structure-from-Motion* (SfM). Kasus yang dipelajari adalah bunga, buah stroberi mentah (*unripe*), dan buah stroberi matang (*ripe*) di satu kebun stroberi di Wimauma, Florida, pada musim tanam 2017–2018. Pendeteksi Faster R-CNN diterapkan pada setiap citra mentah. Satu stroberi yang sama terdeteksi berulang kali karena citra saling tumpang tindih, sehingga model FaceNet yang dimodifikasi menghitung jarak fitur antardeteksi dan algoritma pengklasteran mengelompokkan deteksi menjadi stroberi unik.

Perbaikan FaceNet yang diusulkan adalah menambahkan koordinat geografis (X, Y, Z) objek ke citra potongan sebagai masukan penyematan (*embedding*). Pada himpunan uji, penambahan posisi menaikkan *validate rate* (VAL) bunga dari 84,63% menjadi 98,36% dan menurunkan *false accept rate* (FAR) bunga dari 10,31% menjadi 1,11%.

Hasil utama adalah peningkatan akurasi keseluruhan (*overall accuracy*) dibandingkan penghitungan pada ortomosaik saja: bunga dari 76,28% menjadi 96,98%, buah mentah dari 71,64% menjadi 99,09%, dan buah matang dari 69,81% menjadi 97,17%. Tingkat oklusi pada ortomosaik dilaporkan 19,53% untuk bunga, 24,18% untuk buah mentah, 26,42% untuk buah matang, dan rata-rata 22,56%.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pencacahan buah dan bunga dari citra penginderaan jauh lazimnya dilakukan dengan menjalankan jaringan deteksi pada ortomosaik yang dirakit dari citra mentah bertumpang tindih melalui SfM. Ortomosaik didominasi piksel dari satu sudut (umumnya mendekati vertikal) atau campuran citra dari sudut berbeda. Akibatnya, stroberi yang tertutup daun pada pandangan vertikal dapat hilang atau kabur pada ortomosaik, padahal tampak jelas pada citra mentah dari sudut miring.

Penulis menunjukkan bahwa masalah utamanya bukan model deteksi. Pada ortomosaik, Faster R-CNN mencapai laju deteksi sekitar 90,1%, tetapi akurasi terhadap jumlah stroberi sebenarnya hanya sekitar 73,3% (angka yang dinyatakan penulis pada Bab 4). Penulis menyatakan bahwa belum ada studi terdahulu yang memakai informasi multi-pandang untuk deteksi dan pencacahan objek kecil.

## Ide Utama
Gagasannya adalah mendeteksi pada semua citra mentah lalu menyelesaikan masalah identitas: menentukan deteksi mana yang merupakan stroberi fisik yang sama. Masalah itu diperlakukan seperti verifikasi dan pengelompokan wajah. FaceNet memetakan setiap objek ke ruang Euclidean berdimensi 128 sehingga jarak antarvektor mencerminkan kesamaan identitas, dengan fungsi kerugian *triplet*.

Kebaruan yang diklaim ada pada dua hal. Pertama, vektor identitas memadukan penampilan citra dan posisi tanah (X, Y, Z) objek yang diperoleh dari proyeksi sinar kamera ke model 3D. Kedua, pengklasteran menerapkan aturan tambahan bahwa dua objek dengan *Photo_ID* yang sama tidak boleh masuk klaster yang sama, berdasarkan asumsi bahwa semua objek dalam satu citra adalah unik.

## Cara Kerja Langkah demi Langkah

```
  Citra mentah ──> Faster R-CNN ──> kotak + potongan citra
        │                                   │
        └─> SfM (Metashape) ─> posisi X,Y,Z ┤
                                            ▼
                         FaceNet ResNet-34 (citra + posisi)
                                            ▼
                      Klaster ambang / DBSCAN ──> stroberi unik
```

### 1. Akuisisi data
Citra RGB diambil dengan kamera Nikon D-300 yang dipasang pada Vegetation Mobile Mapping System yang ditarik traktor, pada ketinggian sekitar 3,5 m di atas tanah. Lokasi berupa enam bedengan sejajar sepanjang 100 m di Gulf Coast Research and Education Center, University of Florida. Citra memiliki tumpang tindih depan lebih dari 70% dan tumpang tindih samping 60%. Posisi tiap pemotretan ditentukan dari lintasan GNSS (penerima Topcon HiperLite Plus berfrekuensi ganda), dan titik kontrol tanah (GCP) berakurasi sentimeter (sekitar 2 cm) dipasang di lapangan. Sebanyak 236 citra mentah berukuran 2848 × 4288 piksel diproses menjadi satu ortomosaik beresolusi spasial 1 mm. Kultivar stroberi tidak dilaporkan.

### 2. Ortomosaik dan proyeksi ke tanah
SfM dengan Agisoft Metashape menghasilkan parameter orientasi eksterior tiap citra dan model 3D padat. Posisi (X, Y, Z) tiap objek yang terdeteksi pada citra mentah diperoleh dengan memotongkan sinar dari pusat proyeksi kamera melalui titik tengah objek dengan permukaan model 3D, memakai API Python Metashape.

### 3. Deteksi dengan Faster R-CNN
Pendeteksi memakai *backbone* ResNet-50 dengan empat kelas: bunga, buah mentah, buah matang, dan latar. Ambang IoU adalah 0,5. Data pelatihan terdiri atas 2.058 citra dan data uji 357 citra (Tabel 1).

### 4. FaceNet yang ditingkatkan
Model-1 hanya memakai potongan citra objek, sedangkan Model-2 menambahkan posisi (X, Y, Z). Tulang punggung adalah ResNet-34 dan panjang vektor keluaran 128. Faster R-CNN dijalankan pada 456 citra mentah dan menghasilkan 4.363 objek yang dikoreksi dan diinterpretasi secara manual menjadi 1.086 identitas stroberi unik. Untuk pelatihan FaceNet dipilih 995 sampel dari 250 identitas pada area kecil, dan 500 sampel disisihkan untuk uji. Evaluasi pasangan memakai VAL, FAR, dan akurasi.

### 5. Pengklasteran
Dua algoritma dibandingkan pada penyematan hasil FaceNet. Pengklasteran ambang (*threshold clustering*) menambahkan objek ke klaster bila jarak ke tetangga terdekat di klaster itu lebih kecil dari ambang, yang dipilih dari akurasi validasi tertinggi. DBSCAN adalah algoritma berbasis kerapatan yang tidak memerlukan jumlah klaster di muka. Kualitas klaster diukur dengan *pairwise F-measure*, dan akurasi hitungan memakai $1-|N_R-N_P|/N_R$ dengan $N_R$ jumlah acuan stroberi unik yang dihitung manual dari citra mentah.

## Eksperimen dan Hasil
Perangkat lunak yang dipakai adalah PyTorch 1.11 dengan GPU Nvidia TITAN X (Pascal). Acuan hitung adalah interpretasi visual manusia pada citra mentah multi-pandang, bukan panen.

Pada ortomosaik, Faster R-CNN mencapai presisi 95,2% dan *recall* 90,1% untuk semua objek (bunga 95,4% dan 90,5%; buah mentah 94,9% dan 89,7%; buah matang 95,9% dan 91,0%). Pada pelatihan 100 epoch, akurasi pelatihan dan validasi FaceNet mencapai sekitar 85,8% dan 86,1% (Model-1) serta 99,62% dan 99,1% (Model-2).

| Kategori | VAL Model-1 | VAL Model-2 | FAR Model-1 | FAR Model-2 |
|---|---|---|---|---|
| Bunga | 84,63% | 98,36% | 10,31% | 1,11% |
| Buah mentah | 83,75% | 95,29% | 9,53% | 1,08% |
| Buah matang | 86,8% | 99,68% | 8,42% | 0,25% |

Hasil pengklasteran (Tabel 4):

| Target | Metode | Klaster terprediksi | Klaster acuan | Presisi | *Recall* | F-measure |
|---|---|---|---|---|---|---|
| Bunga | Ambang | 417 | 430 | 0,872 | 0,837 | 0,853 |
| Bunga | DBSCAN | 414 | 430 | 0,791 | 0,943 | 0,860 |
| Buah mentah | Ambang | 585 | 550 | 0,839 | 0,905 | 0,870 |
| Buah mentah | DBSCAN | 555 | 550 | 0,860 | 0,879 | 0,869 |
| Buah matang | Ambang | 109 | 106 | 0,821 | 0,973 | 0,891 |
| Buah matang | DBSCAN | 109 | 106 | 0,850 | 0,965 | 0,904 |

Perbandingan hitungan (Tabel 5):

| Kategori | Manual (ortomosaik) | Manual (citra mentah) | Oklusi | Deteksi ortomosaik | DBSCAN | Ambang |
|---|---|---|---|---|---|---|
| Bunga | 346 | 430 | 19,53% | 328 | 414 | 417 |
| Buah mentah | 417 | 550 | 24,18% | 394 | 555 | 585 |
| Buah matang | 78 | 106 | 26,42% | 74 | 109 | 109 |
| Semua | 841 | 1.086 | 22,56% | 796 | 1.078 | 1.111 |

Penulis menyimpulkan bahwa citra mentah menemukan 19,53%, 24,18%, dan 26,42% lebih banyak bunga, buah mentah, dan buah matang dibandingkan ortomosaik, dan bahwa DBSCAN tampak sedikit lebih efektif dan kokoh daripada pengklasteran ambang.

## Kelebihan dan Keterbatasan
Kelebihan: pendekatan ini memakai informasi dari sudut miring untuk memulihkan objek yang tertutup, menghasilkan hitungan per kelas (bunga, buah mentah, buah matang), dan menunjukkan bahwa penambahan posisi geografis memperbaiki pemisahan identitas secara besar.

Keterbatasan yang dinyatakan penulis: metode belum diuji pada fase ketika hampir semua stroberi matang dan kebun sangat padat, sehingga hasil yang andal sulit dijamin. Penulis mengusulkan detektor lain (YOLO, SSD), model terpadu yang menggabungkan pemetaan FaceNet dan pengklasteran, sudut miring optimal, serta kajian pengaruh tumpang tindih depan dan samping. Kualitas keluaran klaster juga bergantung pada pilihan algoritma, kualitas penyematan, dan akurasi deteksi.

Menurut pembacaan ringkasan ini, pelatihan FaceNet memakai sampel dari area kecil (995 sampel, 250 identitas) dan koreksi manual atas deteksi, sedangkan klaster dievaluasi pada seluruh 4.363 sampel yang sebagian termasuk data yang dipakai melatih, sehingga independensi evaluasi tidak sepenuhnya jelas dari teks. Acuan hitung berasal dari anotasi manual pada citra yang sama, bukan hitungan lapangan atau panen. Pembagian pelatihan dan uji tidak dirinci per pohon atau bedengan, dan hanya satu lokasi dan satu musim yang diuji.

## Kaitan dengan Tinjauan main6
Makalah ini menangani objek yang terlihat lebih dari sekali secara eksplisit. Mekanismenya adalah penyematan identitas berbasis citra dan posisi tanah 3D, yang dikelompokkan dengan ambang jarak atau DBSCAN, ditambah kendala bahwa dua deteksi dari citra yang sama tidak boleh menyatu. Ini termasuk pencocokan multi-pandang dengan rekonstruksi 3D. Hitungan dilaporkan per kelas (bunga, buah mentah, buah matang), dan acuan hitungnya adalah interpretasi visual pada citra mentah, bukan panen maupun hitungan lapangan.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan menyematkan penampilan dan posisi dalam satu ruang jarak, serta kendala bahwa deteksi dari satu citra bersifat unik. Pemindahan itu memerlukan posisi 3D yang andal. Pada sawit, pose kamera antarsisi pohon berbeda jauh dan tumpang tindih antarsisi kecil, sehingga proyeksi sinar ke permukaan model seperti pada makalah ini tidak dapat diasumsikan tersedia. Makalah ini tidak membahas pohon atau antarsisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `zheng2023object`.

Zheng dkk. mengusulkan pendeteksian dan pencacahan bunga serta buah stroberi langsung dari citra mentah multi-pandang. Faster R-CNN dijalankan pada tiap citra, lalu model FaceNet yang ditambah informasi posisi (X, Y, Z) dan pengklasteran ambang atau DBSCAN menggabungkan deteksi berulang menjadi objek unik. Dibandingkan penghitungan pada ortomosaik saja, akurasi keseluruhan naik dari 76,28% menjadi 96,98% (bunga), dari 71,64% menjadi 99,09% (buah mentah), dan dari 69,81% menjadi 97,17% (buah matang), dengan tingkat oklusi rata-rata pada ortomosaik 22,56%.

Catatan verifikasi data: Angka VAL dan FAR ada pada Tabel 3, F-measure dan jumlah klaster pada Tabel 4, hitungan dan tingkat oklusi pada Tabel 5, serta kinerja Faster R-CNN pada ortomosaik pada Tabel 2 (teks Bab 3.1 menyebutnya Tabel 1, yang merupakan salah rujuk di makalah). Angka akurasi keseluruhan 96,98%, 99,09%, dan 97,17% muncul pada abstrak, Bab 3.2.2, dan kesimpulan, tetapi makalah tidak menyatakan metode pengklasteran mana yang menghasilkannya. Menurut perhitungan sederhana dari Tabel 5, 96,98% sesuai dengan hitungan ambang untuk bunga (417 terhadap 430), sedangkan 99,09% sesuai dengan hitungan DBSCAN untuk buah mentah (555 terhadap 550) dan 97,17% sesuai dengan 109 terhadap 106. Akurasi keseluruhan mengukur kedekatan jumlah, bukan kebenaran pencocokan tiap objek. Teks ekstraksi memuat angka tabel dengan baik, tetapi gambar tidak terbaca. Kultivar, jumlah bedengan yang dicitrakan pada ortomosaik, dan rincian pembagian data FaceNet tidak dilaporkan. Berkas teks yang dibaca mencakup isi makalah sampai kesimpulan; sisa berkas berupa ucapan terima kasih dan daftar pustaka.
