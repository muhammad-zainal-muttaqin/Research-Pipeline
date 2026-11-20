# Investigation of oil palm fruit bunch ripeness classification using machine learning classifiers

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zulkhoiri2024investigation` |
| Judul asli | Investigation of oil palm fruit bunch ripeness classification using machine learning classifiers |
| Penulis | Zulkhoiri, Muhammad Arif; Ali, Hasimah; Ahmad Zaidi, Ahmad Firdaus; Mohd Kanafiah, Siti Nurul Aqmariah; Jusman, Yessi; Elshaikh, Mohamed; Tuan Noor, Tuan Muhammad Taufiq Aiman |
| Tahun | 2024 |
| Venue | E3s Web of Conferences |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [zulkhoiri2024investigation.pdf](../pdf/zulkhoiri2024investigation.pdf)
- DOI resmi: https://doi.org/10.1051/e3sconf/202459502010

## Gambaran Umum

Industri minyak sawit, khususnya di Asia Tenggara, bergantung pada ketepatan klasifikasi kematangan tandan buah segar (TBS) kelapa sawit untuk menjaga mutu minyak yang dihasilkan. Penilaian kematangan selama ini dilakukan secara manual oleh pekerja terlatih dengan melihat warna, tekstur, dan jumlah brondolan di tanah. Cara tersebut memakan waktu dan hasilnya bergantung pada penilaian subjektif. Penulis mengusulkan pengklasifikasi cerdas yang hanya memakai fitur warna untuk membedakan tiga kelas, yaitu matang (*ripe*), setengah matang (*half-ripe*), dan mentah (*unripe*). Tujuan kajian ini adalah menyelidiki klasifikasi kematangan memakai fitur warna, mempelajari karakteristik fitur warna pada ruang warna HSV, YCbCr, dan RGB, serta mengevaluasi kinerja pengklasifikasi *k-nearest neighbour* (kNN) dan *support vector machine* (SVM).

Citra tandan dikumpulkan di perkebunan Felda Chuping 2, Perlis, Malaysia, memakai kamera komersial Infinix GT 10 Pro beresolusi 108 MP. Jumlah citra seluruhnya 257, terdiri atas 100 citra matang, 101 citra setengah matang, dan 57 citra mentah. Setiap citra dipangkas (*cropping*) untuk memperoleh area tandan, lalu diubah ukurannya dari 9000×12000 piksel menjadi 300×400 piksel. Fitur dihitung sebagai nilai rerata dan simpangan baku setiap kanal pada ruang warna HSV, YCbCr, dan RGB. Evaluasi memakai dua strategi. Strategi pertama adalah *hold-out* dengan pembagian 70% data latih dan 30% data uji. Strategi kedua adalah *10-fold cross-validation*, yang membagi data menjadi sepuluh subset dan setiap subset bergantian menjadi data uji.

Hasil pada strategi *hold-out* menunjukkan fitur YCbCr dengan kNN mencapai 97,40%, sedangkan fitur HSV dengan kNN dan dengan SVM masing-masing mencapai 93,4%. Fitur RGB dengan kNN mencapai 92,2%. Pada *10-fold cross-validation*, fitur YCbCr dengan SVM mencapai 100%, fitur YCbCr dengan kNN mencapai 96,12%, dan fitur HSV dengan SVM sekitar 99%. Fitur RGB dengan SVM disebut mencapai akurasi sempurna pada kedua strategi. Penulis menyimpulkan bahwa fitur warna efektif membedakan tingkat kematangan, dan HSV serta YCbCr menghasilkan hasil yang sangat baik. Penulis juga menilai pendekatan ini menjanjikan untuk diterapkan pada aplikasi waktu nyata.
