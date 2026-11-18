# Oil palm fresh fruit bunch ripeness classification using back propagation and learning vector quantization

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fahmi2018oil` |
| Judul asli | Oil palm fresh fruit bunch ripeness classification using back propagation and learning vector quantization |
| Penulis | Fahmi, F; Palti M, H; Emerson P, S; Suherman, S |
| Tahun | 2018 |
| Venue | Iop Conference Series Materials Science and Engineering |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [fahmi2018oil.pdf](../pdf/fahmi2018oil.pdf)
- DOI resmi: https://doi.org/10.1088/1757-899x/434/1/012066

## Gambaran Umum

Penelitian ini mengklasifikasikan tingkat kematangan tandan buah segar (TBS) kelapa sawit menjadi dua kelas, yaitu tandan matang (*ripe fruit bunch*, RFB) dan tandan mentah (*unripe fruit bunch*, UFB). Penulis menyatakan bahwa teknik-teknik kompleks yang telah diusulkan sebelumnya menyulitkan penerapan di lapangan. Karena itu, penelitian ini memakai metode sederhana yang dapat ditanam pada sistem tertanam (*embedded system*) dan kelak dipakai pada aplikasi mobile, misalnya sistem pemanen berbasis drone. Deteksi kematangan memang dapat dilakukan saat buah masih di pohon melalui pengamatan manual, kamera jarak jauh, atau drone; penulis menambahkan bahwa interpolasi beberapa citra dari sudut berbeda dapat memberi hasil lebih baik daripada satu citra tunggal.

Datanya berupa 40 citra TBS, terdiri dari 20 RFB dan 20 UFB, yang dianalisis dengan MATLAB. Tahap praproses mencakup pengubahan ukuran citra melalui pemotongan (*cropping*) dan peningkatan mutu. Segmentasi dilakukan dengan menghilangkan latar belakang dan menyesuaikan ambang saturasi dalam rentang 0,2 sampai 0,7. Ekstraksi ciri didasarkan pada warna citra, khususnya kode warna RGB, dengan setiap tandan direpresentasikan sebagai vektor [C1 C2 C3]. Dari 20 citra hasil praproses diekstraksi ciri RGB sebagai data latih, lalu bobot ditentukan untuk kedua metode, dan 20 tandan sisanya dipakai sebagai data uji.

Mekanisme klasifikasi memakai dua metode. *Back propagation* melakukan propagasi mundur berdasarkan nilai galat, sedangkan *learning vector quantization* (LVQ) memakai kompetisi dan nilai linear. Kedua metode dianggap sederhana sehingga mudah diterapkan pada sistem tertanam. Kinerja keduanya dievaluasi dengan analisis ROC pada rentang ambang saturasi 0,2 sampai 0,7, yang menghasilkan nilai *false positive rate* (FPR) dan *true positive rate* (TPR), serta metrik presisi, akurasi, sensitivitas, dan spesifisitas. Sejumlah metode pembanding yang disebut penulis mencatat akurasi 86,67% untuk logika fuzzy, 73,33% untuk kombinasi Algoritma Hebb dan logika fuzzy pada 45 citra, dan 86,67% untuk jaringan saraf *multilayer perceptron*.

Hasil terbaik untuk kedua metode terjadi pada ambang saturasi 0,4. *Back propagation* mencapai presisi 100%, akurasi 100%, sensitivitas 1, dan spesifisitas 1. LVQ mencapai presisi 95%, akurasi 98%, sensitivitas 1, dan spesifisitas 0,95. Ringkasnya, penulis melaporkan akurasi 100% untuk *back propagation* dan 95% untuk LVQ. Penulis menyatakan bahwa meskipun kedua metode cukup sederhana, tahap praproses yang memerlukan pemotongan dan penghilangan latar belakang tidak efisien untuk klasifikasi langsung dengan drone.

