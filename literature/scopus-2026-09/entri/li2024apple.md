# Apple Detection and Yield Estimation Based on YOLOv5

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2024apple` |
| Judul asli | Apple Detection and Yield Estimation Based on YOLOv5 |
| Penulis | Li, Zhaoyang; Bai, Xue; He, Chao; Jiang, Pengfei |
| Tahun | 2024 |
| Venue | 2024 7th International Conference on Advanced Algorithms and Control Engineering Icaace 2024 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [li2024apple.pdf](../pdf/li2024apple.pdf)
- DOI resmi: https://doi.org/10.1109/icaace61206.2024.10549754

## Gambaran Umum

Penulis ingin mendeteksi apel dan memperkirakan jumlah serta hasilnya dari citra kebun dengan model YOLOv5. Masalah yang disebut adalah metode manual yang lambat, padat karya, dan bersifat subjektif, serta pengolah citra tradisional yang sulit menghadapi cahaya, bayangan, dan tertutupnya buah. Selain pencacahan, makalah ini juga membahas sebaran posisi apel, kematangan, dan perkiraan massa dari luas kotak deteksi.

Data tidak dijelaskan secara rinci. Teks hanya menyebut citra apel yang sudah ada dianotasi secara manual dengan alat labelImg lalu dibagi menjadi set latih dan uji. Jumlah citra, jumlah apel, lokasi kebun, sensor, varietas, pemberi label, dan rasio pembagian tidak disebut. Label kematangan terdiri atas empat tingkat (matang, semimatang, belum matang, sangat belum matang), tetapi asal label itu tidak disebut.

Metode memakai YOLOv5s, detektor objek satu tahap yang memprediksi kotak pembatas (*bounding box*), label kelas, dan skor keyakinan dalam sekali lintasan jaringan. Jumlah apel dihitung sebagai C = T x lambda, dengan T jumlah kotak terdeteksi dan lambda faktor skala yang nilainya tidak disebut. Kotak yang tumpang tindih dihapus dengan pascapengolahan. Posisi apel diambil dari titik tengah kotak. Massa diperkirakan dari W = k x Area, dengan Area jumlah luas kotak dalam satu citra dan k = 0,00695 yang disebut diperoleh lewat banyak percobaan. Kematangan dimodelkan dengan regresi polinomial atas fitur warna, ukuran, bentuk, dan tekstur, yang dikombinasikan dengan model pembelajaran mendalam.

Hasil dilaporkan hanya secara deskriptif lewat gambar. Jumlah apel per citra berkisar dari 1 sampai 10 pada sebagian citra dan lebih dari 50 pada citra lain. Apel tersebar lebih padat di tengah citra. Apel matang berjumlah 86,6% dan belum matang 13,4% dari seluruh apel pada kumpulan citra itu. Massa apel umumnya di kisaran 80 sampai 150 gram, dengan sebagian nilai menyimpang ke arah kecil. Tidak ada nilai presisi, *recall*, mAP, MAE, atau metrik galat lain di teks, walaupun ringkasan menyebut kinerja akurasi dan *recall* yang unggul.

Keterbatasan yang dapat diperiksa dari teks: tidak ada angka evaluasi kuantitatif terhadap acuan, tidak ada hitung tangan, hasil panen, atau massa timbangan sebagai pembanding, dan ukuran data tidak disebut. Hitungan berasal dari satu citra tanpa penautan antarcitra. Penulis sendiri menyebut kelemahan pada objek kecil, apel yang tertutup, dan banyak varietas. Faktor skala lambda dan koefisien massa tidak diuji pada data terpisah.
