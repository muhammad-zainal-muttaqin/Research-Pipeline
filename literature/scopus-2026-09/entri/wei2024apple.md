# Apple image recognition model based on optimized sYOLOv5 network with small object detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wei2024apple` |
| Judul asli | Apple image recognition model based on optimized sYOLOv5 network with small object detection |
| Penulis | Wei, Cunli; Tan, Hao; Zhang, Jie; Feng, Mengdan; Liu, Zirou; Wang, Jianwei; Zhang, Pan |
| Tahun | 2024 |
| Venue | ACM International Conference Proceeding Series |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [wei2024apple.pdf](../pdf/wei2024apple.pdf)
- DOI resmi: https://doi.org/10.1145/3673277.3673371

## Gambaran Umum

Kajian ini membahas pengenalan citra apel berbasis *YOLOv5* yang dioptimalkan untuk objek kecil. Latar belakangnya adalah pemetikan apel di Tiongkok yang masih dilakukan dengan tangan. Pada waktu panen, petani membutuhkan banyak pekerja dalam beberapa hari, sementara tenaga kerja pertanian semakin menua. Robot pemetik apel yang ada juga sering tidak mampu mengenali rintangan, sehingga buah dapat rusak. Penulis karena itu mengusulkan model *sYOLOv5* untuk mencacah dan melokalisasi apel secara tepat. Selain itu, model ini dipakai untuk menilai tingkat kematangan dan memperkirakan luas serta massa apel.

Data yang dipakai berupa kumpulan citra apel yang sudah dikumpulkan dari kebun dengan kondisi alami. Cahaya alami, oklusi, dan bayangan memengaruhi citra tersebut. Citra awal berukuran 270 × 180 piksel diubah menjadi 640 × 640 piksel sebelum masuk jaringan. Untuk segmentasi instans, penulis memakai 200 citra. Dataset buah panen yang terpisah juga dipakai untuk melatih model pengenalan buah. Citra dengan latar kebun dan hasil panen ini menjadi dasar seluruh tahapan penelitian.

Metode diawali dengan konversi citra dari RGB ke HSV, karena warna apel matang lebih kontras terhadap latar. Pada model awal, 44 citra tidak terdeteksi sama sekali. Penulis menduga YOLOv5 kurang peka terhadap objek kecil yang padat. Karena itu ditambahkan lapisan deteksi pada peta fitur yang lebih dangkal, serta satu anchor untuk target 4 × 4. Modul CBAM juga ditambahkan, lalu jaringan diringankan hingga menjadi sYOLOv5. Untuk kematangan, keluaran keyakinan model dipetakan ke rentang [0,200]. Apel kemudian dibagi menjadi empat kelas: matang, semi-matang, tidak matang, dan sangat tidak matang, dengan bantuan kanal RGB, terutama kanal hijau. Untuk luas, kontur dari deteksi tepi Canny digabung dengan kontur segmentasi instans menurut bobot β = 0,8. Luas apel kemudian dihitung dari jumlah piksel yang termasuk apel. Penulis menyatakan bahwa mereka menyelesaikan tugas deteksi apel dalam kondisi kompleks tanpa anotasi tambahan pada dataset.

Penulis sendiri menyebut beberapa batasan. Penambahan CBAM dan lapisan deteksi objek kecil membuat struktur jaringan menjadi lebih rumit dan memperlambat kecepatan pengenalan. Citra juga memiliki derau karena resolusinya rendah, sehingga tahap prapemrosesan diperlukan. Penilaian kualitas bersifat tidak terawasi dan hanya memberikan kualitas relatif, bukan kualitas absolut. Penulis mengusulkan agar ke depan dilakukan penelitian metode tak terawasi yang lebih sesuai atau penambahan label pada dataset agar algoritma terawasi dapat menghitung kualitas dan informasi lain secara lebih akurat.
