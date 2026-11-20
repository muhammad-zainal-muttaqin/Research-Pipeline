# Deep learning image segmentation and extraction of blueberry fruit traits associated with harvestability and yield

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ni2020deep` |
| Judul asli | Deep learning image segmentation and extraction of blueberry fruit traits associated with harvestability and yield |
| Penulis | Ni, Xueping; Li, Changying; Jiang, Huanyu; Takeda, Fumiomi |
| Tahun | 2020 |
| Venue | Horticulture Research |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | blueberry |

## Tautan Akses
- PDF: [ni2020deep.pdf](../pdf/ni2020deep.pdf)
- DOI resmi: https://doi.org/10.1038/s41438-020-0323-3

## Gambaran Umum

Kajian ini mengatasi kebutuhan pengukuran sifat buah blueberry yang berkaitan dengan hasil dan kemudahan pemanenan. Kerapatan rumpun, kematangan, dan jumlah buah per rumpun membantu pemulia memilih genotipe serta membantu produsen menentukan strategi panen. Penilaian kematangan secara visual tidak konsisten, sementara metode kuantitatif kerapatan rumpun yang ada memerlukan banyak pekerjaan manual dan tidak berdaya guna tinggi. Penulis membangun alur pemrosesan citra untuk menghitung buah, mengukur kematangan, dan menilai kerapatan rumpun secara otomatis pada empat kultivar southern highbush, yaitu Emerald, Farthing, Meadowlark, dan Star.

Dua dataset dikumpulkan. Dataset untuk deteksi dan segmentasi memuat 724 citra dalam tiga kondisi, yaitu cahaya luar ruang dengan latar alami, cahaya luar ruang dengan latar karton, dan cahaya buatan dengan latar buatan di laboratorium. Citra diambil di kebun komersial Alma, Georgia, pada 17 April 2019 serta di laboratorium University of Georgia, lalu dibagi menjadi 524 citra latih, 145 validasi, dan 55 uji. Anotasi memakai tiga kelas, yaitu latar, buah matang berwarna biru, dan buah belum matang berwarna hijau atau merah, dengan poligon pada VGG Image Annotator. Strategi anotasi iteratif dipakai untuk menghemat waktu: 137 citra dianotasi manual untuk Model_1, 88 citra berikutnya memperoleh anotasi otomatis yang dikoreksi manual dalam waktu 1 jam, dibandingkan 6 jam untuk anotasi manual penuh, lalu 444 citra sisanya dianotasi dengan Model_3 dan koreksi manual. Dataset kedua dipakai untuk ekstraksi sifat dan terdiri atas 104 sampel, yaitu 26 cabang per kultivar dengan lima sudut pandang mengelilingi rumpun, sehingga total 520 citra. Citra diambil dengan kamera DSLR Fujifilm X-A10 beresolusi 4896 × 2760 piksel pada latar buatan.

Mekanisme deteksi memakai Mask R-CNN dengan backbone ResNet101 dan feature pyramid network serta region proposal network, diikuti pengklasifikasi ROI, regresor kotak pembatas, dan jaringan mask. Citra diubah ke 1024 × 1024 piksel. Pelatihan memakai bobot awal dari MS COCO, learning rate 0,001, momentum 0,9, ukuran batch 2, dan tujuh augmentasi, meliputi rotasi horizontal dan vertikal masing-masing 50%, rotasi 90°, 180°, dan 270°, perkalian dengan nilai acak 0,5–1,5, serta blur Gaussian dengan sigma 5,0, pada GPU Tesla V100 16 GB. Sifat dihitung dari hasil segmentasi: jumlah buah adalah banyaknya buah terdeteksi, kematangan adalah hasil bagi jumlah buah matang dengan jumlah buah terdeteksi, dan kerapatan adalah luas mask buah dibagi luas kotak pembatas minimum yang mencakup seluruh buah. Nilai Hue juga diuji sebagai ukuran kematangan yang objektif, dengan batas mask dikurangi 10 piksel agar tidak terpengaruh latar dan pencahayaan.

Performa diukur dengan mAP dan mean IoU. Model pada epoch 510 mencatat mAP 0,783 pada himpunan validasi dan 0,716 pada himpunan uji pada ambang IoU 0,5; mIOU berturut-turut adalah 0,906 dan 0,904. Pada ambang IoU di atas 0,85, mAP turun di bawah 0,5 dan mendekati nol pada IoU 0,95. Perbandingan metode anotasi menunjukkan AP tertinggi 0,706 untuk anotasi manual pada epoch 553 dan 0,699 untuk anotasi otomatis terkoreksi pada epoch 546, dengan selisih 0,007; mIOU anotasi otomatis lebih tinggi sekitar 0,004. Regresi antara jumlah buah terdeteksi dan hitungan manual menghasilkan R² sebesar 0,886 dan RMSE 1,484. Model per kultivar lebih akurat, misalnya Star mencatat R² 0,934 dan RMSE 0,359, sedangkan Emerald mencatat R² 0,932 dan RMSE 0,715. Nilai rata-rata sifat per kultivar adalah Emerald 13,861 buah, kematangan 0,528, kerapatan 0,595; Farthing 12,897, 0,477, 0,647; Meadowlark 11,394, 0,651, 0,514; dan Star 8,534, 0,574, 0,574.

Batasan yang dinyatakan penulis mencakup empat jenis kesalahan deteksi, yaitu satu buah terdeteksi sebagai dua, buah terlewat, dua buah terdeteksi sebagai satu, dan deteksi sebagian; kesalahan itu terutama disebabkan buah yang saling menutupi dan keterbatasan citra dua dimensi. Daun juga kadang terdeteksi sebagai buah belum matang. Anotasi kematangan tidak konsisten karena buah dengan warna serupa dapat diberi label berbeda, sehingga penulis menguji nilai Hue sebagai pengganti yang lebih objektif. Jumlah buah cenderung lebih rendah dari hitungan manual karena tidak semua buah tampak dalam satu citra, dan kesalahan membesar seiring bertambahnya buah. Metode ini belum dapat menentukan kontribusi panjang tangkai terhadap kerapatan rumpun. Penulis menyarankan pencitraan tiga dimensi pada penelitian lanjutan; penggunaan lima sudut pandang pada tiap sampel sudah mengurangi pengaruh pencilan dari satu sudut.
