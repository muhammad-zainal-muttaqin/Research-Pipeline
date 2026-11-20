# Oil palm fresh fruit bunch ripeness classification on mobile devices using deep learning approaches

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `suharjito2021oil` |
| Judul asli | Oil palm fresh fruit bunch ripeness classification on mobile devices using deep learning approaches |
| Penulis | Suharjito; Elwirehardja, Gregorius Natanael; Prayoga, Jonathan Sebastian |
| Tahun | 2021 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [suharjito2021oil.pdf](../pdf/suharjito2021oil.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2021.106359

## Gambaran Umum

Kajian ini membahas klasifikasi tingkat kematangan tandan buah segar (TBS) kelapa sawit pada perangkat seluler. Penulis menyatakan bahwa sebagian besar metode pembelajaran mendalam untuk kematangan sawit membutuhkan sumber daya komputasi besar sehingga tidak dapat dijalankan pada aplikasi seluler. Pemilahan kematangan secara manual di lapangan dinilai memakan waktu dan kurang efisien. Karena itu penulis mengembangkan aplikasi Android yang memakai *Convolutional Neural Network* (CNN) ringan untuk mengklasifikasikan TBS dari citra kamera secara langsung.

Data berasal dari satu pabrik kelapa sawit di Kalimantan Tengah yang diambil saat proses grading. Citra diambil dengan kamera digital ponsel pintar di berbagai lokasi luar ruangan pada hari cerah. Dataset terdiri atas 653 citra dan dibagi ke dalam enam kategori: *unripe*, *under-ripe*, *ripe*, *over-ripe*, *abnormal*, dan *empty fruit bunch* (EFB). Setiap kategori berisi 110 citra, kecuali kategori *abnormal* yang berisi 103 citra. Pelabelan dilakukan secara manual oleh pihak pabrik. Citra dibagi dengan rasio 5:2:3 untuk data latih, validasi, dan uji. Format citra adalah JPG dengan resolusi 3120 × 4160 piksel.

Metode utama terdiri atas tiga unsur. Pertama, *transfer learning* dengan bobot ImageNet, dengan tiga blok konvolusi yang tidak dibekukan. Kedua, augmentasi data baru yang disebut "9-angle crop", yang menghasilkan sepuluh citra dari setiap citra asal. Ketiga, *post-training quantization* untuk memperkecil model. Empat arsitektur ringan dibandingkan, yaitu MobileNetV1, MobileNetV2, NASNet Mobile, dan EfficientNetB0. Pada MobileNetV1, *transfer learning* dengan tiga blok terbuka menghasilkan akurasi validasi 0,777 dan akurasi uji 0,806. Penambahan 9-angle crop menaikkan akurasi validasi menjadi 0,915 dan akurasi uji menjadi 0,811. Penulis juga menyatakan bahwa 9-angle crop menurunkan selisih akurasi latih dan validasi sebesar 0,074 pada MobileNetV1, sehingga membantu mencegah *overfitting*. EfficientNetB0 menghasilkan akurasi uji tertinggi pada Keras, yaitu 0,898. Setelah dikonversi ke TensorFlow Lite dengan kuantisasi float16, akurasi uji EfficientNetB0 menjadi 0,893 dengan waktu klasifikasi 96 ms per citra. Kuantisasi float16 memangkas ukuran model menjadi separuh, dengan penurunan akurasi hanya 0,005. MobileNetV1 memerlukan waktu klasifikasi paling singkat, yaitu 39 ms per citra, dengan akurasi uji 0,811. Penulis melaporkan bahwa aplikasi Android menghasilkan hasil yang serupa ketika menerima citra dari kamera langsung.

Penulis menyebut beberapa batasan dan arah lanjutan. Pembelajaran mendalam memerlukan data latih yang besar agar tidak mengalami *overfitting*, dan kajian ini hanya memakai 653 citra. Data diambil dari satu pabrik dan pada kondisi luar ruangan yang cerah, sehingga cakupan kondisi pencahayaan dan lokasi tidak luas. Penulis menyatakan bahwa hasil penelitian ini dapat dikaji dan diperbaiki lebih lanjut untuk mencapai akurasi yang lebih tinggi dan waktu proses yang lebih cepat. Penulis juga menegaskan bahwa aplikasi ini ditujukan bagi perangkat dengan sumber daya komputasi rendah, seperti ponsel pintar yang biasa digunakan petani.
