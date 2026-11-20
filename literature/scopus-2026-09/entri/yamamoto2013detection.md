# Detection and counting of intact tomato fruits on tree using image analysis and machine learning methods

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yamamoto2013detection` |
| Judul asli | Detection and counting of intact tomato fruits on tree using image analysis and machine learning methods |
| Penulis | Yamamoto, K.; others |
| Tahun | 2013 |
| Venue | Conference Proceeding 5th International Conference Tae 2013 Trends in Agricultural Engineering 2013 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [yamamoto2013detection.pdf](../pdf/yamamoto2013detection.pdf)

## Gambaran Umum

Penelitian ini bertujuan mendeteksi buah tomat utuh secara otomatis pada tanaman sebelum panen. Estimasi hasil panen yang otomatis memberi manfaat bagi petani, misalnya untuk pemetaan hasil, pengelolaan lahan secara spesifik lokasi, dan perkiraan kapasitas penyimpanan. Banyak metode pengolahan citra sebelumnya bergantung pada ambang batas warna, bentuk, dan ukuran. Kinerjanya berubah antarcitra karena ambang batas yang optimal berbeda-beda. Selain itu, sebagian besar metode hanya mendeteksi buah matang dan mentah, padahal jumlah buah muda penting untuk memprediksi fluktuasi hasil jangka panjang. Penulis mengusulkan metode yang memakai kamera RGB digital biasa dan pembelajaran mesin. Metode ini tidak memerlukan penyesuaian ambang batas untuk setiap citra.

Data diambil di fasilitas tanaman (*plant factory*) Institut Ilmu Sayuran dan Teh di Tsukuba, Jepang. Kamera *digital single-lens reflex* Canon EOS Kiss X3 dipasang di fasilitas tersebut. Citra diambil setiap dua jam pada malam hari dari 5 Februari sampai 7 Maret 2013, dengan total 154 citra. Lampu kilat bawaan kamera dipakai sebagai sumber cahaya. Sebanyak 54 citra dipilih secara acak dari 154 citra. Dari citra terpilih, 13 citra dipakai untuk pelatihan dan sisanya untuk pengujian. Data latih piksel terdiri atas 140.000 piksel buah serta masing-masing 100.000 piksel daun, batang, dan latar belakang. Data latih *blob* terdiri atas 30 blob multi-buah, 200 blob buah tunggal, dan 2.000 blob bukan buah. Buah dibagi menjadi tiga tahap pertumbuhan. Buah muda memiliki diameter terpanjang 30 sampai 40 mm. Buah mentah dan buah matang sama-sama berdiameter 41 sampai 80 mm, dan keduanya dibedakan dari warnanya.

Metode terdiri atas tiga tahap. Pertama, segmentasi berbasis piksel memakai *decision tree* CART dengan 15 fitur warna dari lima ruang warna. Kedua, segmentasi berbasis blob memakai *random forest* untuk membuang blob yang tidak berisi buah. Klasifikasi ini memakai rata-rata warna, tekstur *gray level co-occurrence matrix*, ukuran, dan rasio lebar terhadap tinggi. Ketiga, untuk blob multi-buah, penulis mengalikan saturasi terbalik dengan kanal nilai pada ruang HSV. Area terlalu terang akibat lampu kilat kemudian diekstraksi dengan *X-means clustering*. Pusat massa setiap area dipakai sebagai posisi satu buah. Pada citra contoh, segmentasi piksel menghasilkan 8.715 blob, padahal citra itu hanya berisi tujuh buah. Setelah segmentasi berbasis blob, jumlah kandidat berkurang menjadi tujuh dan tujuh buah terdeteksi. Kinerja diukur dengan recall dan precision. Pada citra uji, recall keseluruhan adalah 0,80 dan precision 0,88. Recall per tahap pertumbuhan adalah 1,00 untuk buah matang, 0,80 untuk buah mentah, dan 0,78 untuk buah muda.

Penulis menyatakan beberapa batasan. Segmentasi berbasis piksel juga mengenai batang dan daun, dan kesalahan paling sering terjadi ketika batang atau sorotan pada buah memiliki warna yang mirip dengan buah muda. Ukuran blob berubah sesuai jarak antara kamera dan tanaman. Penelitian ini memakai citra dari jarak yang selalu sama, dengan kesalahan ukuran kurang dari kira-kira 20 persen antara sisi dekat dan jauh tanaman. Penulis menilai bahwa untuk citra dari jarak berbeda diperlukan penanda skala di sebelah tanaman atau informasi 3D, misalnya dari kamera kedalaman. Penulis juga menyebut bahwa informasi daun, batang, dan percabangan yang ikut terdeteksi belum diukur dan dapat diteliti pada studi lanjutan.
