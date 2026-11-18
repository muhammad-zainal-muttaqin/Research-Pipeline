# FF3D: A Rapid and Accurate 3D Fruit Detector for Robotic Harvesting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2024ff3d` |
| Judul asli | FF3D: A Rapid and Accurate 3D Fruit Detector for Robotic Harvesting |
| Penulis | Liu, Tianhao; Wang, Xing; Hu, Kewei; Zhou, Hugh; Kang, Hanwen; Chen, Chao |
| Tahun | 2024 |
| Venue | Sensors |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [liu2024ff3d.pdf](../pdf/liu2024ff3d.pdf)
- DOI resmi: https://doi.org/10.3390/s24123858

## Gambaran Umum

Penelitian ini mengatasi keterbatasan deteksi buah berbasis citra dua dimensi untuk pemanenan robotik, terutama ketika tingkat oklusi tinggi. Metode berbasis gambar tidak dapat memberikan informasi posisi tiga dimensi yang presisi, sehingga lokasi buah yang tertutup sering keliru dan dapat menggagalkan cengkeraman. Penulis juga mencatat bahwa metode tiga dimensi di bidang kendaraan otonom mengompres informasi ketinggian, sedangkan pendekatan banyak pandangan dengan estimasi next-best view umumnya memakai voxel yang kehilangan detail oklusi. Tujuan penelitian ini adalah membangun detektor buah tiga dimensi ujung-ke-ujung yang tangguh terhadap oklusi, dilengkapi penentu sudut pandang terbaik berikutnya.

Data dikumpulkan dengan lidar dan kamera pada Monash Apple Retrieve System (MARS) dari 141 pohon apel dengan beragam tingkat oklusi, kondisi pencahayaan, dan struktur pohon. Titik lidar hanya memuat nilai x, y, z, dan intensitas, sehingga diwarnai dengan memproyeksikannya ke citra kamera memakai matriks intrinsik dan matriks transformasi lidar–kamera hasil kalibrasi. Dataset memuat apel, jeruk, dan leci; untuk apel terdapat 141 pemindaian berlabel dengan 2.283 buah, dibagi menjadi 70% latih, 20% validasi, dan 10% uji, ditambah 1.455 apel dari dataset Fuji-SfM yang dicampurkan hanya untuk latih. Anotasi kotak tiga dimensi memakai CloudCompare dengan delapan titik sudut dan satu titik pusat, lalu dikonversi ke format SUN-RGBD; augmentasi berupa rotasi, translasi, dan penskalaan. Evaluasi banyak pandangan memakai lingkungan simulasi NVIDIA Omniverse Isaac Sim dengan model pohon dari neural radiance fields, lengan robot UR5, dan kamera RealSense; enam uji masing-masing memakai sembilan apel dengan batas tiga pandangan.

Arsitektur FF3D dibangun di atas FCAF3D, jaringan deteksi tiga dimensi sepenuhnya konvolusional dan bebas anchor yang menerima awan titik berwarna. Encoder memakai MinkResNet dengan 64, 128, 256, dan 512 kanal per lapis; decoder merupakan penyederhanaan GSDN dengan pemangkasan voxel, sedangkan kepala deteksi menghasilkan probabilitas klasifikasi, centerness, dan regresi kotak. Penulis menambahkan rugi oklusi ke dalam total fungsi rugi di samping focal loss, DIoU loss, dan binary cross-entropy; rasio oklusi dihitung sebagai proporsi luas buah yang tertutup oleh titik latar depan pada proyeksi citra. Untuk banyak pandangan, rintangan direpresentasikan sebagai ellipsoid Gaussian anisotropik yang dicocokkan pada ruang voxel, menghasilkan fungsi indeks tabrakan yang kontinu. Tingkat oklusi suatu pandangan adalah integral indeks tersebut sepanjang sinar dari kamera ke pusat buah. Information gain didefinisikan dari kebalikan tingkat oklusi buah yang terlihat, lalu sudut pandang terbaik ditentukan dengan gradient descent; hasil setiap pandangan digabungkan memakai 3D non-maximum suppression.

Pada deteksi satu pandangan atas 14 pohon apel uji dengan rata-rata 15 percobaan, FF3D memperoleh AP@25 sebesar 0,763, AP@50 0,602, AR@25 0,923, dan AR@50 0,789, mengungguli FCAF3D, TR3D, GroupFree3D, ImVoteNet, maupun metode dasar dua dimensi. Waktu inferensi tercantum 14,871 ms pada Tabel 1 dan 140 ms tanpa NBV ketika model dijalankan di Jetson AGX Orin. Pada uji banyak pandangan, galat posisi rata-rata berkisar antara 5,19 dan 6,17 mm, sedangkan galat diameter rata-rata antara 1,62 dan 1,93 mm; abstrak menyebut galat jarsak Euclidean rata-rata kurang dari 6,2 mm. Penulis menyatakan optimasi NBV memakan waktu kurang dari 100 ms untuk sekitar 1.500 Gaussian. AP dan AR dihitung pada beberapa ambang 3D IoU, sedangkan galat posisi merupakan jarak Euclidean antara posisi buah hasil deteksi dan posisi kebenaran dasar.

Penulis mengakui tiga keterbatasan. Jaringan deteksi tiga dimensi memerlukan daya komputasi jauh lebih besar sehingga mungkin memerlukan unit pemroses grafis khusus untuk inferensi luring. Pengumpulan dan anotasi dataset tiga dimensi juga menuntut tenaga kerja manusia yang banyak. Selain itu, penulis menemukan galat yang konsisten pada estimasi posisi dan ukuran yang diduga berasal dari kesalahan anotasi manual. Penelitian lanjutan diarahkan pada perbaikan estimasi NBV, estimasi pose cengkeraman, serta pembangkitan dan anotasi otomatis data latih di lingkungan simulasi.

