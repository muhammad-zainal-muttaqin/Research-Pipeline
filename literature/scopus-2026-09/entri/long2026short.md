# A Short-Term Yield Prediction Method for Greenhouse Strawberries Integrating Visual Phenology and Meteorological Sequences

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `long2026short` |
| Judul asli | A Short-Term Yield Prediction Method for Greenhouse Strawberries Integrating Visual Phenology and Meteorological Sequences |
| Penulis | Long, Yuhai; Gao, Quan; Zhang, Xiang; Zhang, Guangchuan; He, Yun |
| Tahun | 2026 |
| Venue | Agronomy |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [long2026short.pdf](../pdf/long2026short.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy16141356

## Gambaran Umum

Kajian ini membahas prediksi hasil panen stroberi jangka pendek di rumah kaca. Produksi stroberi sangat mudah rusak setelah panen, sehingga harga pasar peka terhadap fluktuasi hasil. Prediksi hasil yang akurat membantu pengelolaan produksi, penjadwalan rantai pasok, dan perencanaan panen. Metode konvensional mengandalkan sampling lapangan secara manual. Cara ini padat tenaga kerja, mahal, dan rentan terhadap bias pengamat. Model statistik berbasis data lingkungan juga kurang mampu menangkap hubungan nonlinear iklim mikro. Model tersebut juga tidak memasukkan pengamatan langsung terhadap fenotipe tanaman, seperti jumlah bunga dan buah. Penulis mengusulkan metode yang memadukan fenologi visual dengan deret waktu meteorologi. Tujuannya adalah memprediksi jumlah buah merah per tanaman pada musim panen berikutnya.

Data berasal dari rumah kaca kaca cerdas di Universitas Pertanian Yunnan, Kunming, Tiongkok. Penelitian memakai stroberi kultivar Benihoppe yang berumur empat bulan pada awal pemantauan. Pemantauan berlangsung selama 72 hari, dari 11 Desember 2025 hingga 20 Februari 2026. Dari 595 tanaman di rak budidaya, penulis memilih 150 tanaman sehat sebagai data eksperimen. Setiap tanaman dipantau selama 22 siklus panen. Sensor tanah dipasang di rizosfer, sedangkan sensor iklim dipasang di atap rumah kaca. Citra diambil dengan ponsel Huawei Mate 40 Pro berkamera 50 megapiksel dengan resolusi 3840 × 2160 piksel. Jarak pengambilan gambar sekitar 30 sampai 50 cm dengan sudut 45 sampai 60 derajat. Interval pengambilan gambar tiga hari. Sebanyak 784 citra dianotasi ke dalam lima kelas fenologi, yaitu bunga, hijau, putih, merah muda, dan merah. Anotasi dilakukan dengan perangkat lunak LabelMe. Data dibagi 7:3 menjadi 105 tanaman untuk pelatihan dan 45 tanaman untuk pengujian. Pembagian ini dibuat agar tanaman bertetangga tidak bocor antarset.

Metode terdiri atas tiga bagian. Pertama, YOLO11-SC dipakai untuk mendeteksi lima tahap fenologi buah dengan menambahkan mekanisme atensi *Squeeze-and-Excitation* dan atensi kanal-spasial. Model ini mencapai presisi 87,6%, recall 86,7%, mAP@0,5 sebesar 86,3%, dan mAP@[0,5:0,95] sebesar 59,6%. Kedua, fitur visual dipadukan dengan deret waktu meteorologi seperti suhu, kelembapan, dan intensitas cahaya menjadi matriks fitur *multimodal* spatiotemporal. Ketiga, dua arsitektur prediksi dibandingkan. BiTCN-SA, yaitu Bidirectional Temporal Convolutional Network dengan *self-attention*, ditujukan untuk server. Model ini memperoleh R2 sebesar 0,958 dan RMSE sebesar 3,154 buah per tanaman. Validasi silang lima lipatan menghasilkan R2 rata-rata 0,958 ± 0,005 dan RMSE 3,154 ± 0,047. MAE-nya sebesar 2,049. Stack-LGR, yaitu ensemble pembelajaran mesin ringan untuk perangkat tepi IoT, memperoleh R2 sebesar 0,892, RMSE sebesar 5,058, dan MAE sebesar 3,865. Stack-LGR dirancang untuk perangkat dengan sumber daya terbatas dan dinilai stabil dengan latensi inferensi yang dapat diterima.

Penulis menyatakan beberapa batasan. Pertama, prediksi memakai data meteorologi teramati dari T hingga T + 2, sehingga belum merupakan sistem peramalan operasional. Dalam penerapan nyata, data tersebut harus berasal dari model prakiraan cuaca atau sistem prediksi iklim rumah kaca. Kedua, pengumpulan data hanya dilakukan di satu lokasi selama satu musim tanam. Ukuran data yang terbatas dapat membatasi generalisasi terhadap kondisi lingkungan, praktik budidaya, atau kultivar lain. Ketiga, validasi eksternal di beberapa lokasi geografis belum dilakukan. Penulis menyebut perlunya perluasan data multi-lokasi dan multi-tahun, pengujian pada praktik manajemen yang berbeda, serta evaluasi ketahanan model terhadap oklusi dan cahaya rendah.
