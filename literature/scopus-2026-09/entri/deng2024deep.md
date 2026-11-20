# Deep learning in crowd counting: A survey

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `deng2024deep` |
| Judul asli | Deep learning in crowd counting: A survey |
| Penulis | Deng, Lijia; Zhou, Qinghua; Wang, Shuihua; G\'orriz, Juan Manuel; Zhang, Yudong |
| Tahun | 2024 |
| Venue | Caai Transactions on Intelligence Technology |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [deng2024deep.pdf](../pdf/deng2024deep.pdf)
- DOI resmi: https://doi.org/10.1049/cit2.12241

## Gambaran Umum

Artikel tinjauan ini mengkaji penghitungan keramaian (*crowd counting*), yaitu tugas menghitung jumlah orang dari citra atau video. Masalah utamanya adalah kesulitan mengekstraksi ciri kepala akibat tumpang tindih yang rapat, gangguan antara ciri lingkungan dan ciri keramaian, perubahan ukuran kepala akibat distorsi perspektif, dan mutu citra yang beragam. Penulis menilai tinjauan sebelumnya kurang merinci dataset dan belum mencakup banyak dataset baru, sehingga pengujian algoritme hanya bergantung pada sedikit benchmark. Kebaruan yang diajukan terdiri atas taksonomi dataset standar tiga tingkat (TSDT), indeks kejernihan dataset berupa rata-rata piksel yang ditempati tiap objek (APO), klasifikasi 36 dataset, pengelompokan algoritme menjadi enam kelas, serta evaluasi lebih dari 110 metode.

Tanaman dan data pertanian tidak dinyatakan; objek yang dihitung adalah manusia. Mekanisme yang dibahas adalah penghitungan berbasis peta kepadatan, bukan asosiasi identitas lintas pandang, sehingga asosiasi identitas tidak dinyatakan. Pendekatan awal memakai deteksi berbasis jendela geser dan regresi ciri lokal, lalu Lempitsky dan Zisseman memperkenalkan peta kepadatan pada 2010 yang menyimpan jumlah sekaligus posisi objek. Sejak 2015, jaringan saraf konvolusional (CNN) mempelajari pemetaan nonlinear dari citra ke peta kepadatan. Enam kelas metode menurut sudut pandang data meliputi jaringan multi-skala, jaringan satu kolom seperti CSRnet dengan CNN terdilasi, jaringan banyak kolom seperti MCNN, jaringan multi-tugas seperti DecideNet yang menggabungkan deteksi dan regresi lewat mekanisme perhatian, jaringan perhatian seperti SAAN, serta jaringan tersupervisi lemah. Pembentukan peta kepadatan memakai kernel Gaussian, dengan rumus pada persamaan (1)–(7).

Taksonomi TSDT membagi dataset menurut jumlah anotasi per citra: skala kecil jika Nmax kurang dari 100 atau Navg kurang dari 40, skala besar jika Nmax antara 100 dan 1000 atau Navg antara 40 dan 200, dan skala sangat besar jika Nmax minimal 1000 atau Navg minimal 200. Indeks APO dihitung sebagai akar dari hasil kali tinggi dan lebar citra dibagi jumlah anotasi, sehingga mengukur kejernihan kepala, bukan resolusi citra secara keseluruhan.

Beberapa angka hasil dapat dijadikan acuan. Pada eksperimen APO di dataset Mall (Tabel 2), kenaikan APO dari 24,8 menjadi 99,2 menurunkan MAE ResNet50 dari 2,35 menjadi 2,07 dan RMSE dari 2,93 menjadi 2,62; VGG16De mencatat MAE 7,44 menjadi 7,00 dan RMSE 8,60 menjadi 8,10. Pada Tabel 4, yang membandingkan kinerja dengan metrik MAE dan RMSE—semakin rendah semakin baik—MCNN mencatat MAE 1,07 dan RMSE 1,35 pada UCSD, 26,4 dan 41,3 pada ShanghaiTech B, 110,2 dan 173,2 pada ShanghaiTech A, serta 377,6 dan 509,1 pada UCF_CC_50; Cross-scene mencatat 1,60 dan 3,31 pada UCSD serta 181,8 dan 277,7 pada ShanghaiTech A; DecideNet mencatat 1,52 dan 1,90 pada Mall serta 21,53 dan 31,98 pada ShanghaiTech B. Penulis mengingatkan bahwa MAE dan RMSE sangat dipengaruhi jumlah orang dalam citra.

Batasan yang dikemukakan penulis meliputi penanganan skenario dunia nyata seperti distorsi kamera, latar belakang berantakan, dan oklusi, serta kebutuhan algoritme yang tangguh terhadap pencahayaan dan cuaca berbeda dan mampu memproses keramaian besar secara waktu nyata. Penulis juga mencatat perlambatan riset pada dataset skala kecil, kejenuhan pada dataset skala besar dan sangat besar, keterbatasan daya komputasi, serta perlunya dataset baru yang menargetkan penghitungan keramaian. Transfer learning diusulkan untuk mengatasi keterbatasan data kecil. Penulis mengakui tidak dapat mencakup seluruh pekerjaan yang ada.
