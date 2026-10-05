# A comparative study of fruit detection and counting methods for yield mapping in apple orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hani2020comparative` |
| Judul asli | A comparative study of fruit detection and counting methods for yield mapping in apple orchards |
| Penulis | H\"ani, Nicolai; Roy, Pravakar; Isler, Volkan |
| Tahun | 2020 |
| Venue | Journal of Field Robotics |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [hani2020comparative.pdf](../pdf/hani2020comparative.pdf)
- DOI resmi: https://doi.org/10.1002/rob.21902

## Gambaran Umum

Makalah ini membandingkan metode deteksi dan pencacahan buah untuk pemetaan hasil panen (*yield mapping*) di kebun apel. Penulis membangun sistem modular dari ujung ke ujung, yaitu deteksi dan pencacahan per bingkai, pelacakan buah antarbingkai, lalu penggabungan hitungan dari sisi depan dan sisi belakang barisan pohon melalui rekonstruksi 3D bersama. Penulis mengajukan pendekatan baru berbasis segmentasi semantik (U-Net) untuk deteksi, dan memperbarui metode pencacahan klaster buah dengan jaringan klasifikasi ResNet50. Kedua metode itu dibandingkan dengan Faster R-CNN dan dengan pengelompokan warna berbasis *Gaussian Mixture Model* (GMM) pada data yang sama.

Data berasal dari kebun penelitian University of Minnesota Horticultural Research Center (Eden Prairie, Minnesota), Juni 2015 sampai September 2016, direkam sebagai video dengan telepon seluler Samsung Galaxy S4 yang menghadap sisi barisan pohon secara horizontal. Pengujian hasil panen memakai tiga set data (masing-masing 6, 10, dan 6 pohon) yang divideo dari kedua sisi barisan dan dibandingkan dengan jumlah buah hasil panen.

Hasil utama: pada deteksi, metode GMM semi-terawasi (diawasi pengguna) unggul pada sebagian besar set data, sedangkan pada pencacahan, ResNet50 lebih baik daripada GMM pada seluruh set uji. Kombinasi deteksi GMM dan pencacahan ResNet50 dengan penggabungan dua sisi menghasilkan akurasi estimasi hasil 95,56% sampai 97,83% terhadap hitungan panen. Penjumlahan hitungan dua sisi tanpa penggabungan menghasilkan hitungan 101,93% sampai 150% dari hasil panen (GMM) dan 103,86% sampai 147,81% (ResNet50).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pemetaan hasil panen otomatis dibutuhkan karena penaksiran manual mengambil sampel acak sejumlah pohon lalu mengekstrapolasi, yang dapat menghasilkan estimasi keliru. Sistem yang ada pada umumnya mengambil citra dari satu sisi atau kedua sisi barisan, mendeteksi dan menghitung buah, melacaknya antarbingkai, lalu menggabungkan hitungan. Menurut penulis, sebelum karya mereka (Roy dkk., 2018a) tidak ada sistem yang menggabungkan hitungan dari dua sisi barisan tanpa sensor navigasi eksternal. Sistem yang hanya mengaitkan hitungan satu sisi dengan hasil nyata cenderung menaksir terlalu tinggi atau terlalu rendah, terutama bila pohon tidak dipangkas dengan baik.

Masalah kedua adalah perbandingan antarmetode. Setiap metode deteksi dan pencacahan di pustaka diuji pada set data khusus masing-masing, sehingga perbandingan langsung tidak dimungkinkan. Penulis menyebut karya ini sebagai yang pertama membandingkan beberapa metode deteksi dan pencacahan buah pada data yang sama. Masalah ketiga adalah biaya pelabelan: menganotasi satu citra 1920 × 1080 dapat memakan waktu hingga 15 menit, sehingga perlu diukur seberapa besar peningkatan yang diberikan model pembelajaran mendalam dibanding metode klasik yang sederhana.

## Ide Utama

Gagasan pertama adalah memperlakukan deteksi buah sebagai klasifikasi tingkat piksel (apel atau latar) dengan U-Net, yang dapat memakai sedikit data latih dan menangani objek kecil (apel menempati 5 sampai 50 piksel pada citra 1920 × 1080 dari jarak 2 sampai 3 meter). Gagasan kedua adalah memperlakukan pencacahan klaster apel sebagai klasifikasi multikelas atas jumlah buah per wilayah minat (*Region of Interest*, RoI), dengan tujuh kelas (0 sampai 6 apel).

Gagasan ketiga, yang dipakai dari karya sebelumnya penulis, adalah menghilangkan penghitungan ganda lewat geometri. Setiap sisi barisan direkonstruksi secara terpisah dengan *Structure from Motion* (SfM), kedua rekonstruksi digabung berdasarkan informasi semantik menjadi satu model 3D, dan klaster buah yang terlihat dari kedua sisi dihitung satu kali. Hitungan klaster dari beberapa bingkai dirangkum dengan median tiga bingkai yang memuat piksel apel terbanyak.

## Cara Kerja Langkah demi Langkah

```
  Video sisi depan ──┐                          ┌─> deteksi + hitungan per bingkai
                     ├─> SfM per sisi ─> masker ┤
  Video sisi belakang┘    3D buah             └─> klaster 3D ─> RoI per klaster
                                   │
                  gabung dua sisi (semantik) ─> irisan klaster
                                   │
            prinsip inklusi-eksklusi ─> hitungan total tanpa ganda
```

### 1. Akuisisi data

Video direkam dengan Samsung Galaxy S4 di kebun penelitian yang memuat banyak varietas apel (nama kultivar tidak dirinci). Set latih deteksi terdiri atas 10 set data dari 6 barisan pohon (2015), dengan 103 citra beranotasi berukuran 1920 × 1080 piksel. Set uji deteksi dan hasil panen berasal dari empat bagian kebun (2016) dengan tujuh video. Untuk acuan, penulis mengumpulkan hasil per pohon dan mengukur diameter buah setelah panen.

| Set uji hasil panen | Jumlah pohon | Apel yang dipanen | Karakteristik |
|---|---|---|---|
| 1 | 6 | 270 | Apel merah, geometri planar, akuisisi akhir musim (daun menguning) |
| 2 | 10 | 274 | Apel merah, geometri non-planar |
| 3 | 6 | 414 | Campuran merah dan hijau, non-planar |
| 4 | 4 | 568 | Campuran merah dan hijau, non-planar, hanya video sisi yang terkena matahari |

Set data 4 tidak dipakai untuk uji hasil panen karena tidak memiliki video dari kedua sisi.

### 2. Deteksi buah

Tiga metode dibandingkan. U-Net memakai tulang punggung VGG-16 berbobot ImageNet, citra potongan 224 × 224 piksel (sekitar 59.000 potongan beranotasi), *weighted categorical cross-entropy* untuk ketidakseimbangan kelas (rasio buah terhadap latar sekitar 1:20), optimizer Ada-Delta, dan hingga 50 epoch. Faster R-CNN mengikuti Bargoti dan Underwood (2017a) dengan ResNet50, *Feature Pyramid Network*, dan *focal loss*, dilatih pada potongan 500 × 500 piksel (sekitar 9.000 potongan beranotasi). GMM mengelompokkan superpiksel SLIC ruang warna LAB menjadi sekitar 25 kelas warna dan mengklasifikasikannya berdasarkan divergensi KL terhadap kelas yang dilabeli pengguna; versi terawasi pengguna memakai klik pada lima bingkai pertama tiap video, dan versi semi-terawasi memakai model dari satu set data lain.

### 3. Pencacahan klaster per bingkai

Jaringan ResNet50 mengklasifikasikan potongan citra klaster menjadi tujuh kelas hitungan (0 sampai 6). Batas enam apel per klaster ditetapkan secara empiris dari karya sebelumnya. Data latih terdiri atas 13.000 potongan beranotasi dari dua set data (apel hijau dan merah) ditambah 4.500 potongan acak tanpa apel, ditingkatkan menjadi sekitar 65.000 potongan dengan augmentasi. Label diberikan oleh sedikitnya dua pelabel dengan penengah ketiga untuk ketidaksesuaian. Pembanding adalah model GMM dua dimensi yang mencari jumlah komponen paling mungkin lewat algoritma EM. Inception-ResNet v2 juga diuji tetapi hanya lebih baik 0,4% secara rerata, sehingga tidak dipakai.

### 4. Pelacakan dan penggabungan dua sisi

Setelah masker buah diperoleh, rekonstruksi SfM semi-padat tiap sisi diproyeksikan kembali ke seluruh bingkai. Titik 3D yang beririsan dengan masker dikelompokkan menjadi komponen terhubung 3D, dan tiap komponen diproyeksikan ulang menjadi deret RoI satu klaster. Apel di tanah dan pohon di latar belakang dibuang dengan bidang tanah 3D dan masker kedalaman. Rekonstruksi dua sisi digabung dengan algoritma Roy dkk. (2018a) dan Dong dkk. (2018), lalu irisan komponen dihitung dengan prinsip inklusi-eksklusi agar buah yang terlihat dari kedua sisi tidak terhitung dua kali. Detail algoritma pelacakan hanya diulas singkat dan dirujuk ke karya lain.

## Eksperimen dan Hasil

Deteksi dievaluasi dengan presisi, *recall*, dan F1 pada rentang ambang IoU 0,01 sampai 0,99 pada tujuh set uji (kombinasi set 1 sampai 4, sisi depan dan belakang). Hasilnya disajikan hanya sebagai kurva pada Gambar 11 sampai 13, sehingga nilai numerik per set tidak tersedia pada teks. Temuan kualitatif dari teks: GMM terawasi pengguna unggul pada enam dari tujuh set dan satu-satunya yang memperoleh presisi di atas 90% di semua set; GMM semi-terawasi turun pada set 1 (depan) dan 4 (depan) karena ruang warna uji berbeda dari model latih; U-Net memiliki *recall* konsisten tinggi, presisinya tidak mencapai 80% pada empat dari tujuh set (daun menguning terdeteksi sebagai apel), dan unggul atas GMM pada set 4 (depan); Faster R-CNN memiliki presisi terendah di semua set. Kecepatan: GMM 5 bingkai per detik, U-Net kurang dari 4,5 detik per bingkai 1920 × 1080, Faster R-CNN dengan tiling hingga 46 detik per bingkai (laptop dengan GPU Quadro M1000).

Akurasi pencacahan potongan citra (Tabel 3, empat set uji, total 2.874 potongan):

| Metode | Set 1 (956) | Set 2 (628) | Set 3 (587) | Set 4 (703) |
|---|---|---|---|---|
| GMM | 88,0% | 81,8% | 77,2% | 76,1% |
| ResNet50 | 88,8% | 92,68% | 95,1% | 88,5% |

ResNet50 menolak deteksi positif palsu pada 87% kasus, sedangkan GMM pada 43%. Teks menyebut akurasi keseluruhan jaringan sekitar 90,5%. Distribusi hitungan sangat condong ke satu apel, dan penulis menyimpulkan bahwa asumsi tujuh kelas terlalu lebar.

Estimasi hasil panen (Tabel 4), memakai deteksi GMM saja karena U-Net dan Faster R-CNN dinilai belum memuaskan:

| Set | Panen | Gabungan dua sisi, GMM | Gabungan dua sisi, ResNet50 | Penjumlahan sisi tunggal, GMM | Penjumlahan sisi tunggal, ResNet50 |
|---|---|---|---|---|---|
| 1 | 270 | 256 (94,81%) | 258 (95,56%) | 348 (128,89%) | 347 (128,52%) |
| 2 | 274 | 252 (91,98%) | 268 (97,81%) | 411 (150%) | 405 (147,81%) |
| 3 | 414 | 392 (94,68%) | 405 (97,83%) | 422 (101,93%) | 430 (103,86%) |

Dengan penggabungan dua sisi, ResNet50 memiliki galat 2,17% sampai 4,44% terhadap hitungan panen. Penulis menekankan bahwa sistem hanya menghitung apel yang terlihat, tidak apel di dalam tajuk.

## Kelebihan dan Keterbatasan

Kelebihan menurut makalah: perbandingan ketiga metode deteksi dan dua metode pencacahan pada data yang sama; penggabungan dua sisi barisan menghilangkan penghitungan ganda tanpa sensor navigasi atau perangkat khusus (cukup kamera telepon); hitungan dibandingkan dengan hasil panen per pohon.

Keterbatasan yang dinyatakan penulis: data latih U-Net dan Faster R-CNN terbatas (103 citra beranotasi) sehingga generalisasinya belum dapat disimpulkan, dan U-Net salah mendeteksi daun menguning karena data latih 2015 tidak memuatnya. Pelabelan hitungan klaster tidak konsisten antarpelabel, terutama pada klaster tumpang tindih. Kesalahan pencacahan sering terjadi pada buah yang terlihat sebagian. Metode GMM tidak bekerja bila buah tidak dapat dibedakan dari warna dan tidak dapat menolak positif palsu. Hanya apel yang terlihat yang dihitung. Penulis berencana menambah data latih dan menjajaki data sintetis.

Menurut pembacaan ringkasan ini: (a) sistem hasil panen terbaik memakai GMM yang disetel dengan klik pengguna per video, sehingga akurasi 95,56% sampai 97,83% bergantung pada pengawasan manual per set uji; (b) pengujian hasil panen hanya mencakup tiga set (22 pohon, dihitung dari 6 + 10 + 6 pada Tabel 1), dengan satu set video per sisi, dan tidak ada ulangan atau selang kepercayaan; (c) hitungan dinilai hanya sebagai total per set sehingga kesalahan positif palsu dan negatif palsu pada tingkat klaster dapat saling meniadakan; (d) set uji pencacahan dibuat dari keluaran deteksi GMM sehingga tidak independen dari metode deteksi; (e) tidak ada hitungan per kelas atau atribut buah.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali, dan merupakan contoh langsung metode koreksi dua sisi barisan. Buah terlihat berulang pada bingkai video berurutan dan terlihat dari dua sisi barisan. Mekanismenya meliputi pelacakan lewat rekonstruksi SfM tiap sisi (klaster 3D diproyeksikan ke bingkai), penggabungan rekonstruksi dua sisi memakai informasi semantik, dan penghilangan hitungan ganda dengan prinsip inklusi-eksklusi atas irisan klaster 3D. Makalah ini juga menunjukkan akibat tanpa penggabungan: penjumlahan hitungan dua sisi menghasilkan 101,93% sampai 150% dari hasil panen.

Hitungan tidak dilaporkan per kelas; hanya hitungan total buah (tanpa atribut kematangan) yang dibandingkan. Acuan hitungnya adalah jumlah buah hasil panen per pohon (Tabel 1 dan 4), bukan anotasi citra, sedangkan pencacahan potongan citra memakai anotasi manual. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: prinsip menggabungkan model 3D dari sisi-sisi yang berbeda lalu mengurangi irisan, penggunaan hitungan panen sebagai acuan, dan pelaporan hasil penjumlahan sisi tunggal sebagai pembanding bahwa tanpa penggabungan identitas hitungan terlalu tinggi. Kendalanya, penggabungan ini bergantung pada SfM dari video kontinu serta geometri barisan pohon yang berjajar, sehingga perlu penyesuaian untuk pengambilan citra diskret per sisi pohon sawit. Hal itu merupakan kesimpulan ringkasan ini.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `hani2020comparative`.

Häni, Roy, dan Isler membandingkan tiga metode deteksi apel (U-Net, Faster R-CNN, dan GMM) serta dua metode pencacahan klaster (ResNet50 dan GMM) pada data video kebun yang sama. Dengan sistem pemetaan hasil panen yang menggabungkan hitungan dari kedua sisi barisan pohon melalui rekonstruksi 3D bersama, kombinasi deteksi GMM dan pencacahan ResNet50 mencapai akurasi estimasi 95,56% sampai 97,83% terhadap jumlah apel hasil panen pada tiga set data, sedangkan penjumlahan hitungan sisi tunggal menghasilkan hitungan 101,93% sampai 150% dari hasil panen.

Catatan verifikasi data: Angka 95,56% sampai 97,83% dan 91,98% sampai 94,81% ada di abstrak, Tabel 4, dan Bagian 6.5. Akurasi pencacahan ada di Tabel 3. Jumlah pohon dan buah panen ada di Tabel 1, dan jumlah potongan citra pada Tabel 2 serta Bagian 5.2. Hasil deteksi (presisi, *recall*, F1) hanya berupa kurva pada Gambar 11 sampai 13 dan tidak dapat diverifikasi sebagai angka dari teks ekstraksi. Teks menyebut ResNet50 mengungguli GMM sebesar "18% dan 12%" pada set 2 dan 4 dan "hampir 11%" pada set 3, tetapi selisih Tabel 3 adalah 10,88 poin pada set 2, 17,9 poin pada set 3, dan 12,4 poin pada set 4, sehingga uraian teks tampak menukar set; ringkasan ini memakai angka tabel. Jumlah 22 pohon pada uji hasil panen dihitung dari Tabel 1 (set 1 sampai 3), bukan dinyatakan di teks. Nama kultivar, jumlah citra uji deteksi, dan venue jurnal tidak dilaporkan dalam teks (teks berasal dari arXiv 1810.09499v2).
