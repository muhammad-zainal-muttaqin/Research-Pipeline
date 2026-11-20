# OIL PALM LEVEL OF RIPENESS CLASSIFICATION USING EFFICIENTDET-LITE CNN ARCHITECTURE

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `soetrisno2024oil` |
| Judul asli | OIL PALM LEVEL OF RIPENESS CLASSIFICATION USING EFFICIENTDET-LITE CNN ARCHITECTURE |
| Penulis | Adi Soetrisno, Yosua Alvin |
| Tahun | 2024 |
| Venue | Journal of Oil Palm Research |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [soetrisno2024oil.pdf](../pdf/soetrisno2024oil.pdf)
- DOI resmi: https://doi.org/10.21894/jopr.2023.0059

## Gambaran Umum

Penentuan tingkat kematangan tandan buah segar (TBS) diperlukan untuk memilih buah yang layak diolah, karena tandan yang terlalu matang menurunkan mutu minyak akibat naiknya asam lemak bebas. Petani selama ini menilai kematangan berdasarkan pengalaman dan terkadang salah karena pengamatan tidak terpusat. Penelitian ini bertujuan mencari model CNN yang sesuai untuk klasifikasi kematangan TBS dengan EfficientDet yang memakai penskalaan fitur tidak seragam, sekaligus membangun alat pengamat yang dapat memvalidasi model langsung di kebun untuk pohon setinggi sekitar 2–20 meter tanpa menara pengamat.

Sampel adalah kelapa sawit varietas Dumpy (DyP Sungai Pancur I) dari Pusat Penelitian Kelapa Sawit di Langkat, Sumatra Utara, dan beberapa kebun swasta di Kalimantan. Dataset latih berjumlah 240 citra dengan empat kelas, yaitu Unripe, underripe, ripe, dan overripe, masing-masing 60 citra; validasi memakai 15 citra per kelas atau 60 citra di luar data latih. Penulis memakai 170 citra TBS unik yang diperbanyak dengan rotasi dan zoom menjadi sekitar dua sampai lima citra per citra asli, serta flip horizontal bawaan dengan probabilitas 50%. Citra diambil dengan Samsung Galaxy J7 13 MP f/1.9 28 mm dan webcam X85 HD 720P 5 MP pada jarak 3–5 meter, dengan sudut dan latar berbeda: 27 citra tandan menggantung, 183 citra di tanah, 11 citra adegan dengan TBS menggantung, dan 19 citra kelompok dengan rumput sebagai latar. Anotasi kotak pembatas dan label kelas disimpan dalam berkas XML, dan citra asli sekitar 1080×1920 diubah ukurannya menjadi 768×768 sesuai masukan EfficientDet D2. Pelatihan dilakukan di Google Collaboratory dengan variasi batch 8 dan 16 serta epoch 20, 50, 100, 200, 300, 400, dan 500; ambang kepercayaan deteksi ditetapkan 50%.

Mekanisme yang diuji adalah deteksi dan klasifikasi objek dengan EfficientDet-Lite2 yang diimplementasikan pada perangkat Android melalui TensorFlow Lite. Model ini memakai backbone yang hampir sama dengan EfficientDet D2, lima lapis Bi-FPN, dan tiga lapis ClassNet dan BoxNet per lapis. Bi-FPN menggabungkan fitur secara dwiarah, atas-bawah dan bawah-atas, dengan bobot untuk setiap masukan dan sambungan lewati dari peta fitur awal. Aplikasi memiliki dua mode kamera, langsung dari ponsel atau melalui webcam USB, menampilkan kelas dan kotak pembatas hasil klasifikasi, menyimpan hasil penghitungan yang disetujui ke basis data SQLite Android, dan mengekspor berkas CSV.

Penulis membandingkan varian EfficientDet-Lite berdasarkan ukuran, latensi, dan mAP pada data validasi COCO 2017. EfficientDet-Lite2 memiliki ukuran 7,2 MB, latensi 69 ms pada Google Pixel 4 dengan empat utas CPU, dan mAP 33,97%, lebih tinggi daripada Lite0 (4,4 MB; 37 ms; 25,69%) dan Lite1 (5,8 MB; 49 ms; 30,55%), sedangkan Lite3 dan Lite4 mencapai 37,70% dan 41,96% dengan latensi 116 ms dan 260 ms. Pada data TBS, mAP latih tertinggi diraih batch 16 pada 300 epoch sebesar 59,81%; untuk batch 8 nilai tertinggi 58,00% pada 20 epoch, dan penulis menyatakan mAP menurun setelah 300 epoch serta batch 16 sedikit lebih tinggi daripada batch 8. Pengujian pada 100 citra di luar data latih, terdiri atas citra kebun dan sekitar 50 citra yang diunduh dari Google, menghasilkan akurasi 84,00%, presisi 82,00%, recall 85,00%, dan F1-score 84,00%; matriks confusion menunjukkan 21 dari 25 citra overripe, 22 dari 25 ripe, 17 dari 25 underripe, dan 24 dari 25 unripe diklasifikasikan benar.

Penulis menyatakan beberapa batasan. Akurasi 84% lebih rendah daripada beberapa hasil sebelumnya yang sekitar 90%, meskipun model dinyatakan layak digunakan di kebun. Perkebunan badan usaha milik negara menerapkan baku kematangan yang lebih ketat daripada kebun swasta, sehingga tandan setengah matang atau underripe terkadang dianggap ripe. Pada pengujian aplikasi Android, kelas dan kotak pembatas dapat berubah saat kondisi kilat karena ada area campuran antara bagian hitam dan merah-jingga. Citra dari internet memiliki keterbatasan karena variasi pencahayaan, sehingga fitur warnanya kurang dapat diandalkan daripada citra yang diambil langsung di kebun. Data dari Kalimantan relatif terbatas ruang lingkupnya dibandingkan data dari Sumatra. Penulis tidak memakai segmentasi regional karena kompleksitasnya dapat menurunkan kinerja model di perangkat Android; MobileNetV2 juga gagal memberi klasifikasi stabil karena terkadang objek tidak terdeteksi.
