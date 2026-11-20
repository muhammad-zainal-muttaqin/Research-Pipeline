# Image-based analysis of yield parameters in viticulture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zabawa2022image` |
| Judul asli | Image-based analysis of yield parameters in viticulture |
| Penulis | Zabawa, Laura; Kicherer, Anna; Klingbeil, Lasse; T\"opfer, Reinhard; Roscher, Ribana; Kuhlmann, Heiner |
| Tahun | 2022 |
| Venue | Biosystems Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [zabawa2022image.pdf](../pdf/zabawa2022image.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2022.04.009

## Gambaran Umum

Estimasi hasil panen anggur penting bagi keputusan pengelolaan kebun dan pemuliaan. Praktik yang umum saat ini adalah pengambilan sampel destruktif di lapangan, lalu analisis rinci di laboratorium. Hasilnya kemudian diekstrapolasi ke kebun, sehingga hanya mendekati kondisi sebenarnya. Penelitian ini mengusulkan alur kerja berbasis citra untuk mendeteksi, mencacah, dan mengestimasi hasil buah anggur (*berry*) dari citra yang saling tumpang tindih. Penulis melangkah dari pengolahan satu citra tanaman menuju hitungan pada tingkat tanaman, lalu pada tingkat baris.

Data dikumpulkan pada tahun 2018 sampai 2020 menggunakan platform fenotipe lapangan Phenoliner, yang dibangun dari pemanen anggur yang dimodifikasi. Sistem kamera terdiri atas lima kamera yang menghasilkan citra kanopi yang saling tumpang tindih, dengan jarak 35 cm antarkamera vertikal. Penelitian mencakup tiga varietas, yaitu Riesling, Felicia, dan Regent, serta dua sistem pembinaan, yaitu VSP (*vertical shoot positioned*) dan SMPH. Untuk melatih CNN, 59 citra dianotasi per piksel, terdiri atas 38 citra tanaman SMPH dan 21 citra tanaman VSP, dengan 30 citra Riesling, 18 citra Felicia, dan 11 citra Regent. Pada akhir musim, 10 tanaman (satu meter kanopi) per baris dipanen manual sebagai referensi hasil. Tandan contoh juga dikumpulkan pada tiga tahap BBCH, yaitu 75, 79, dan 89, dengan 10 tandan per baris pada tiap tahap.

Model deteksi berupa CNN untuk segmentasi semantik, dengan encoder MobilenetV2 dan decoder DeepLabV3+. Kelas yang dipisahkan adalah *berry*, *edge*, dan *background*. Jumlah buah per citra dihitung dengan algoritma komponen terhubung setelah kelas *edge* dibuang. Untuk menghindari hitungan ganda pada area yang tumpang tindih, penulis mencocokkan *patch* tandan antarcitra dengan koefisien korelasi ternormalisasi, dengan ambang 0,3. Hitungan dari beberapa citra kemudian digabungkan menjadi hitungan tingkat tanaman dan tingkat baris. Bobot rata-rata buah pada akhir musim, dirata-ratakan selama tiga tahun untuk tiap varietas dan sistem pembinaan, dipakai sebagai faktor bobot dalam estimasi hasil. Hasil utama adalah galat prediksi hasil absolut rata-rata sebesar 26% untuk tanaman VSP.

Penulis menegaskan bahwa variabilitas oklusi daun menjadi faktor pembatas utama. Untuk memperhitungkan proporsi buah yang tertutup, penulis melakukan dua percobaan oklusi pada tahun 2019 dan 2020 dengan tanaman Riesling pada kedua sistem pembinaan. Penulis mengamati 35 tanaman pada VSP (5 pada 2019 dan 30 pada SMPH) dan 28 tanaman pada SMPH (10 pada 2019 dan 18 pada 2020). Angka galat 26% hanya dilaporkan untuk VSP. Penulis juga menyatakan bahwa potensi dan batasan pipeline ini dieksplorasi dalam studi tersebut.
