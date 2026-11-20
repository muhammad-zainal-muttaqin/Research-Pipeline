# A smartphone-based apple yield estimation application using imaging features and the ANN method in mature period

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `qian2018smartphone` |
| Judul asli | A smartphone-based apple yield estimation application using imaging features and the ANN method in mature period |
| Penulis | Qian, Jianping; Xing, Bin; Wu, Xiaoming; Chen, Meixiang; Wang, Yan'an |
| Tahun | 2018 |
| Venue | Scientia Agricola |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [qian2018smartphone.pdf](../pdf/qian2018smartphone.pdf)
- DOI resmi: https://doi.org/10.1590/1678-992x-2016-0152

## Gambaran Umum

Produksi apel sangat berfluktuasi dari tahun ke tahun dan antarkebun. Kondisi ini merugikan petani dan memengaruhi keseimbangan antara pasokan dan permintaan. Estimasi hasil yang memperhatikan variasi antarpohon menjadi langkah penting dalam manajemen kebun presisi. Di Tiongkok, sebagian besar kebun dikelola petani dengan lahan kecil. Karena itu dibutuhkan cara yang sederhana dan murah untuk estimasi hasil secara *real-time* di lapangan. Penulis mengajukan kerangka kerja yang memakai *smartphone* untuk mengambil citra tajuk pohon, menghitung estimasi hasil, dan menampilkan peta hasil kebun.

Penelitian dilakukan di kebun percobaan apel *Fuji* (*Malus domestica* Borkh. cv. Red Fuji). Dari 80 pohon, sebanyak 26 pohon dipilih untuk membangun model, dengan jumlah yang dipilih sesuai kelipatan tiga. Data dibagi menjadi 21 kelompok data latih dan 5 kelompok data validasi. Setiap pohon difoto dari dua sisi, yaitu arah tenggara dan barat laut, sehingga diperoleh 160 citra. Citra berformat JPG dengan resolusi 1600 × 1200. Sensor yang digunakan adalah kamera ponsel berbasis Android. Ponsel pintar Huawei G716 dengan CPU 1,2 GHz dan memori 1 GB dipakai untuk menguji waktu proses. Pohon diidentifikasi dengan kartu label berkode QR. Data hasil aktual dicatat pada 13 sampai 25 Oktober 2013, dan hasil per pohon dihitung secara otomatis pada akhir panen.

Metode ini memisahkan objek buah dari latar dengan nilai R/B yang dikombinasikan dengan nilai V. Rata-rata nilai R/B pada 174 titik tepi apel adalah 1,375, dan rata-rata nilai V adalah 0,456. Untuk memisahkan apel yang tumpang tindih, penulis memakai *circle-fitting* berbasis analisis kelengkungan. Dari 10 citra apel, rata-rata jari-jari adalah 45, jari-jari maksimum 65, dan jari-jari minimum 30. Empat parameter diperoleh dari citra: total area piksel teridentifikasi (TP), jumlah lingkaran yang dicocokkan (FC), rata-rata jari-jari lingkaran (RC), dan area poligon kecil (SP). Keempat parameter ini menjadi masukan *Artificial Neural Network* (ANN) tiga lapisan dengan 14 neuron tersembunyi dan satu keluaran berupa hasil per pohon.

Pada data latih, nilai R2 adalah 0,996 dan RRMSE adalah 0,063. Galat absolut terbesar pada data latih adalah 3,15 kg, yaitu pada pohon N° 63. Pada data validasi, RRMSE adalah 0,284. Selisih terkecil antara hasil prediksi dan aktual adalah 0,1 kg pada pohon N° 66, dan selisih terbesar adalah 4,54 kg pada pohon N° 45. Rata-rata hasil prediksi validasi adalah 41,84 kg dengan simpang baku 9,22 kg. Peta hasil untuk 80 pohon menunjukkan hasil estimasi dari 13,60 sampai 71,92 kg. Peta ini menunjukkan pola sebaran hasil di kebun dan dapat mendukung pengambilan keputusan pengelolaan spesifik lokasi. Waktu proses sekitar 4 detik per pohon ketika pengambilan citra dan tampilan hasil dilakukan di ponsel serta perhitungan model di server.

Penulis menyatakan bahwa efektivitas pengenalan citra dan kinerja ANN memengaruhi ketepatan estimasi. Identifikasi buah masih perlu diperbaiki pada kondisi pencahayaan yang berbeda. Model dalam penelitian ini belum diuji pada kondisi pencahayaan tersebut. Model juga perlu dikalibrasi ulang sesuai kondisi aktual kebun. RRMSE data validasi lebih tinggi daripada data latih, yang juga diakui penulis.
