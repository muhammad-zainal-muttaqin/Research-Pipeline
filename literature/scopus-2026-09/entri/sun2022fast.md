# Fast Location and Recognition of Green Apple Based on RGB-D Image

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sun2022fast` |
| Judul asli | Fast Location and Recognition of Green Apple Based on RGB-D Image |
| Penulis | Sun, Meili; Xu, Liancheng; Luo, Rong; Lu, Yuqi; Jia, Weikuan |
| Tahun | 2022 |
| Venue | Frontiers in Plant Science |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [sun2022fast.pdf](../pdf/sun2022fast.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2022.864458

## Gambaran Umum

Penelitian ini mengatasi kesulitan mengenali dan menentukan lokasi apel hijau secara cepat dalam proses pemanenan maupun pendugaan hasil. Buah apel hijau memiliki warna yang mirip dengan ranting dan daun di sekitarnya, sehingga batas buah menjadi kabur, apalagi di lingkungan kebun yang tidak teratur dan dipengaruhi perubahan intensitas serta sudut cahaya. Metode yang hanya mengandalkan fitur warna memiliki kinerja buruk pada kondisi tersebut, sedangkan metode pembelajaran mendalam memerlukan perangkat keras berkinerja tinggi dan banyak sampel latih, sehingga sulit dipenuhi dalam operasi lapangan. Penulis mengusulkan metode yang memadukan informasi citra kedalaman dan citra warna, dengan urutan kerja menentukan titik pusat buah terlebih dahulu, baru mengenali daerahnya—kebalikan dari metode konvensional yang melakukan segmentasi lebih dulu.

Data dikumpulkan di basis produksi apel Longwangshan, Distrik Fushan, Kota Yantai, Provinsi Shandong, dengan kultivar Gala yang masih belum matang dan berwarna hijau. Pengambilan citra dilakukan di bawah cahaya alami memakai kamera Kinect V2 (Microsoft); citra warna memiliki resolusi 1920×1080 piksel dan citra kedalaman 512×424 piksel, dengan jarak kamera ke objek 0,5–4,5 m. Kamera dipasang pada tripod dengan sudut tetap dan akuisisi memakai Kinect SDK 2.0. Untuk keperluan fusi, resolusi semua citra warna disesuaikan menjadi 512×424 piksel. Dataset terdiri dari 300 titik sampel atau 300 pasangan citra warna dan kedalaman yang memuat 526 buah, dengan rincian 287 buah tunggal tanpa hambatan, 89 buah tertutup ranting dan daun, serta 150 buah bertumpang tindih.

Mekanisme deteksi terdiri dari dua cabang. Pada cabang kedalaman, peta kontur garis sama-dalam dibangun dari nilai kedalaman piksel, lalu medan gradien tiga dimensi V = ∇D diproyeksikan ke bidang dua dimensi menjadi (∂D/∂x, ∂D/∂y). Vektor gradien diputar 90° searah jarum jam sehingga daerah buah yang berbentuk cembung membentuk pusaran yang teratur, sementara latar belakang bersifat menyebar dan tidak beraturan; pusat pusaran dengan nilai vortisitas maksimum ditetapkan sebagai titik pusat buah. Pada cabang warna, algoritma density peak clustering (DPCA) disempurnakan dengan estimasi kepadatan inti Gaussian agar tidak bergantung pada jarak potong yang ditentukan secara subjektif. Sebelum pengelompokan, segmentasi super-pikel SLIC dalam ruang warna L*a*b mengubah citra dari tingkat piksel menjadi tingkat blok guna mengurangi jumlah titik data; komponen ciri yang dipakai adalah nilai rata-rata R−B dan G−B per blok. Pusat klaster dipilih otomatis dengan algoritma pengurutan ganda, yaitu mengambil 20 blok dengan kepadatan tertinggi lalu 15 blok dengan jarak terbesar; tiga klaster pertama mencakup 91,69% dari total piksel. Hasil kedua cabang digabungkan: daerah tersegmentasi yang memuat titik pusat lingkaran dinyatakan sebagai buah, dan jari-jari diperoleh dengan metode nilai maksimum—jarak terjauh dari pusat ke tepi untuk buah tunggal, sedangkan untuk buah bertumpang tindih dipindai enam panjang vektor maksimum lalu nilai terkecil yang dipakai. Metode ini tidak memerlukan iterasi, ekstraksi ciri, atau pengklasifikasi, serta dapat bekerja pada himpunan data kecil.

Hasil pengujian pada 300 pasangan citra itu menunjukkan tingkat pengenalan keseluruhan sebesar 96,96%, dengan rincian 99,30% untuk buah tanpa hambatan, 95,33% untuk buah tertutup, dan 92,13% untuk buah bertumpang tindih. Metode pembanding dalam literatur menghasilkan tingkat pengenalan keseluruhan 93,92%, 93,35%, dan 93,53%. Dari segi kecepatan, metode penulis memerlukan 897 ms per pengenalan, lebih cepat daripada metode pembanding yang masing-masing memakan 1.269 ms, 1.505 ms, dan 1.627 ms. Pengujian dijalankan pada komputer dengan prosesor Intel Core i5-5257 2,7 GHz dan memori 4 GB, memakai MATLAB R2015a pada sistem operasi Windows 10 64-bit.

Penulis menyatakan batasan utama pada buah yang bertumpang tindih secara berlebihan, terutama bila tertutup ranting dan daun. Pada kondisi itu, penentuan jari-jari dengan metode nilai maksimum justru memindai nilai minimum pada daerah yang tertutup, sehingga jari-jari optimal sulit diperoleh dan akurasi pengenalan menurun. Penelitian lanjutan yang diusulkan mencakup penyempurnaan penentuan pusat buah agar lebih sedikit bergantung pada informasi kedalaman, dengan memanfaatkan sejumlah kecil informasi gradien, serta perbaikan segmentasi citra warna agar batasnya lebih halus. Penulis menyatakan metode ini bersifat ringan dan tidak memerlukan server berkinerja tinggi, sehingga dapat ditanam pada perangkat keras robot pemanen atau sistem pemantauan pertumbuhan buah, serta berpotensi diperluas ke buah berbentuk bola lainnya.
