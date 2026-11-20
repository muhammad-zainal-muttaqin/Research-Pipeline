# Oil Palm Bunch Ripeness Classification and Plantation Verification Platform: Leveraging Deep Learning and Geospatial Analysis and Visualization

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `puttinaovarat2024oil` |
| Judul asli | Oil Palm Bunch Ripeness Classification and Plantation Verification Platform: Leveraging Deep Learning and Geospatial Analysis and Visualization |
| Penulis | Puttinaovarat, Supattra; Chai-Arayalert, Supaporn; Saetang, Wanida |
| Tahun | 2024 |
| Venue | ISPRS International Journal of Geo Information |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [puttinaovarat2024oil.pdf](../pdf/puttinaovarat2024oil.pdf)
- DOI resmi: https://doi.org/10.3390/ijgi13050158

## Gambaran Umum

Penilaian kematangan tandan kelapa sawit dipakai untuk menentukan harga pembelian, pemeriksaan sebelum panen, dan penilaian dampak bencana atau harga rendah. Penilaian oleh manusia akurat tetapi lambat dan memerlukan petugas atau pakar, sedangkan pembelajaran mesin pada kajian sebelumnya hanya mengklasifikasikan tandan yang sudah dipanen dan tidak menyediakan platform untuk tandan di pohon. Penelitian ini bertujuan membangun platform klasifikasi yang menggabungkan pembelajaran mendalam dengan analisis dan visualisasi geospasial untuk menilai kematangan tandan yang masih menempel di pohon, guna mendukung pengelolaan data pemerintah dan keputusan petani.

Wilayah kajian adalah Distrik Lamae, Provinsi Chumphon, Thailand Selatan (9,7593° LU, 99,0350° BT), yang memiliki lebih dari 48.000 rai perkebunan sawit dan mengalami banjir tahunan. Data terdiri atas data spasial, atribut, dan citra digital dari Google Earth Engine Data Catalog, Google, serta pengumpulan oleh warga (crowdsourcing/Volunteered Geographic Information), lalu disimpan dalam basis data geospasial. Citra tandan di pohon berjumlah 8779, terdiri atas 4004 tandan unripe dan 4775 tandan ripe, dengan dua kelas target, yaitu Ripe dan Unripe. Penulis memakai validasi silang 10 lipat dan menyisihkan 1160 citra (580 per kelas) untuk validasi yang tidak dipakai saat membangun model. Lima algoritma diuji, yaitu CNN dengan arsitektur MobileNetV1, Random Forest, Decision Tree, KNN, dan SVM; empat algoritma klasik diberi penyematan citra (image embedding) memakai InceptionV3, lalu dibandingkan dengan SqueezeNet. Parameter latih mencakup 100 epoch dan batch 32 untuk CNN, 10 pohon untuk RF, maksimal 100 pohon untuk DT, lima tetangga dengan jarak Euclidean untuk KNN, serta 100 iterasi dan kernel RBF untuk SVM. Platform dibangun dengan PHP, Python, Leaflet JavaScript, TensorFlow, dan MySQL.

Mekanisme yang diuji adalah klasifikasi citra keseluruhan, bukan deteksi atau penghitungan kotak per tandan. MobileNetV1 dipilih karena kecepatannya pada perangkat berdaya rendah seperti ponsel. Platform mengekstrak koordinat lintang-bujur dari GPS perangkat dan dari geotag foto, menampilkan peta lokasi kebun dari crowdsourcing, memakai geofencing dengan radius 50 meter, lapisan overlay, dan peta kerapatan (heatmap), serta membandingkan koordinat foto dengan klasifikasi lahan perkebunan sawit dari citra satelit GEE. Model dapat diperbarui ketika jumlah data bertambah.

Metrik yang dipakai adalah akurasi, F-measure, presisi, dan recall dari matriks confusion, bukan mAP atau ambang IoU. CNN mencapai akurasi 99,89%, F-measure 99,88%, presisi 99,90%, dan recall 99,85%; pada data latih, tingkat benar kelas Ripe 99,92% (4771 dari 4775 citra) dan Unripe 99,85% (3998 dari 4004 citra). RF, DT, KNN, dan SVM berturut-turut mencapai akurasi 99,24%, 96,84%, 92,44%, dan 72,07%. Pada 1160 citra validasi, CNN mencapai akurasi 96,12%, F-measure 96,11%, presisi 95,86%, dan recall 96,35%, dengan tingkat benar Ripe 95,86% (556 dari 580) dan Unripe 96,38% (559 dari 580). Penggantian InceptionV3 dengan SqueezeNet menghasilkan akurasi RF 99,16%, DT 97,80%, KNN 91,14%, dan SVM 81,00%; DT naik sekitar 1% dan SVM naik 8–9%.

Penulis menyatakan beberapa batasan. Kecerahan berlebih saat pemotretan menghasilkan citra yang gagal memperlihatkan kematangan, dan getaran tangan pengguna menghasilkan citra kabur. Perbedaan praktik pemeliharaan dan kondisi lingkungan tiap kebun menimbulkan variasi citra. Tandan yang tertutup gulma atau parasit masih dapat diklasifikasikan bila tertutup sebagian, tetapi klasifikasi menjadi tidak tepat bila buah tertutup seluruhnya. Pemotretan dengan cahaya dari belakang dan kendali guncangan kamera juga perlu perbaikan; penulis menyarankan bahan petunjuk bagi pengguna. Model hanya membedakan dua kelas, dan penelitian lanjutan disarankan menambah beberapa tingkat kematangan serta deteksi wilayah terdampak banjir.
