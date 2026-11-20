# Improved kiwifruit detection using VGG16 with RGB and NIR information fusion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2019improved` |
| Judul asli | Improved kiwifruit detection using VGG16 with RGB and NIR information fusion |
| Penulis | Liu, Zhihao; Feng, Yali; Li, Rui; Zhang, Shuang; Zhang, Lihui; Cui, Gongpei; Ahmad, Al-Mallahi; Fu, Longsheng; Cui, Yongjie |
| Tahun | 2019 |
| Venue | 2019 Asabe Annual International Meeting |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | kiwifruit |

## Tautan Akses
- PDF: [liu2019improved.pdf](../pdf/liu2019improved.pdf)
- DOI resmi: https://doi.org/10.13031/aim.201901260

## Gambaran Umum

Liu dkk. (2019) mendeteksi buah kiwi di kebun dengan detektor objek dua tahap, Faster R-CNN berbasis VGG16. Detektor menerima dua sumber citra dari sensor Kinect v2: citra warna (RGB) dan citra inframerah dekat (NIR, *near-infrared*) yang dihasilkan sensor time-of-flight. Penulis membandingkan empat masukan: RGB saja, NIR saja, Feature-Fusion, dan Image-Fusion. Hasil utama: Image-Fusion memberi average precision (AP) tertinggi, yaitu 90,7% pada tabel dan 91,05% pada kesimpulan, dengan total detection rate 91,7%.

Deteksi buah di kebun terhambat oleh daun yang menutupi buah, buah yang saling berdekatan, dan perbedaan pencahayaan. Citra RGB saja kehilangan informasi ketika warna buah dan daun mirip. Penulis menilai bahwa informasi NIR dapat melengkapi RGB pada kondisi tersebut. Penulis tidak menghitung total buah per pohon. Evaluasi yang dilaporkan berupa deteksi per citra dan per kategori tingkat hambatan visual.

Gagasan utamanya adalah menggabungkan RGB dan NIR sebelum atau di dalam jaringan deteksi. Dua cara fusi diuji. Image-Fusion menyusun citra RGB dan NIR yang sudah dijajarkan menjadi satu masukan 6 kanal. Feature-Fusion memakai dua aliran VGG16, satu untuk RGB dan satu untuk NIR, lalu peta fiturnya digabung.

Sensor Kinect v2 menghasilkan citra RGB dan NIR. Kedua citra dijajarkan (*registration*) agar piksel yang sama menunjuk objek yang sama. Dataset berisi 500 citra dengan 19.839 buah yang dianotasi sebagai kotak pembatas (*bounding box*). Data dibagi acak 80/20 menjadi data latih dan uji. Data validasi terdiri atas 50 citra dengan 2.518 buah.

Masukan jaringan berupa 6 kanal (3 kanal RGB dan 3 kanal NIR yang diperlakukan sebagai kanal tambahan). Bobot lapisan konvolusi pertama untuk 6 kanal diambil dari rata-rata bobot RGB pada VGG16 yang dilatih di ImageNet. Dengan cara ini jaringan dapat memakai pengetahuan awal dari RGB tanpa mengubah arsitektur VGG16.

Setiap modalitas diproses oleh aliran VGG16 terpisah. Peta fitur dari dua aliran digabung, lalu diteruskan ke lapisan deteksi Faster R-CNN. Cara ini menambah beban komputasi, dan kecepatan deteksinya paling lambat di antara keempat konfigurasi.

Optimasi memakai SGD dengan momentum 0,9 dan weight decay 0,0005. Learning rate awal 0,001 diturunkan 10% setiap 10.000 iterasi. Pelatihan 100.000 iterasi memakan sekitar 12 jam. Implementasi memakai Caffe.

Pada Tabel 2, AP untuk setiap modalitas adalah RGB 88,4%, NIR 89,2%, Feature-Fusion 90,5%, dan Image-Fusion 90,7%. Kecepatan deteksi per citra adalah 0,134 s untuk RGB, 0,135 s untuk NIR, 0,134 s untuk Image-Fusion, dan 0,188 s untuk Feature-Fusion. Selisih AP antara RGB dan Image-Fusion adalah 2,3 poin persentase.

Pada Tabel 3, total detection rate adalah RGB 88,1%, NIR 89,0%, Image-Fusion 91,7%, dan Feature-Fusion 90,8%. Rincian per kategori untuk Image-Fusion adalah occluded 83,6%, overlapped 87,4%, adjacent 92,8%, dan separated 96,7%. Untuk kategori adjacent, RGB mencapai 88,2% dan NIR 89,5%, sehingga kenaikan terbesar terjadi pada buah yang berdekatan. Kategori occluded tetap paling sulit pada semua modalitas.

Pada Tabel 4, penulis membandingkan hasilnya dengan dua studi Fu dkk. Fu dkk. (2018a) mencapai 89,3% dengan kamera Canon s110 dan resolusi 2352×1568. Fu dkk. (2018b) mencapai 92,3% dengan 0,50×10-2 s per buah. Image-Fusion mencapai 91,7% dengan 0,36×10-2 s per buah pada resolusi 512×424. Angka Fu dkk. dan studi lain di tabel itu adalah kutipan pembanding, bukan hasil studi ini.

Ada dua ketidakcocokan dalam teks. Pertama, AP Image-Fusion tertulis 90,7% di abstrak dan Tabel 2, tetapi 91,05% di kesimpulan. Kedua, kecepatan dilaporkan dalam s per citra di Tabel 2 dan s per buah di Tabel 4, sehingga keduanya tidak dapat langsung dibandingkan.

Kelebihan kajian ini adalah perbandingan langsung empat konfigurasi pada dataset yang sama, dengan pembagian kategori tingkat hambatan visual. Dari sisi rekayasa, kenaikan AP sekitar 2 poin persentase dari RGB ke Image-Fusion dicapai tanpa menambah jumlah parameter jaringan secara signifikan, karena hanya lapisan pertama yang berubah. Feature-Fusion lebih lambat dan tidak lebih akurat daripada Image-Fusion dalam penelitian ini.

Keterbatasannya: dataset hanya 500 citra dari satu jenis buah. Pembagian data acak 80/20 tidak mengendalikan korelasi antarcitra dari pohon yang sama. Kamera yang dipakai adalah Kinect v2, sehingga hasilnya belum tentu berlaku untuk sensor RGB-D lain. Selisih AP antara modalitas (sekitar 0,8 sampai 2,3 poin persentase) tidak dilaporkan dengan interval kepercayaan atau uji signifikansi. Secara konseptual, perbandingan dengan Fu dkk. tidak sebanding karena kamera, resolusi, dan dataset berbeda.
