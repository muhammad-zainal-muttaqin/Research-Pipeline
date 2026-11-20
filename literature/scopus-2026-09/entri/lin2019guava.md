# Guava detection and pose estimation using a low-cost RGB-D sensor in the field

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lin2019guava` |
| Judul asli | Guava detection and pose estimation using a low-cost RGB-D sensor in the field |
| Penulis | Lin, Guichao; Tang, Yunchao; Zou, Xiangjun; Xiong, Juntao; Li, Jinhui |
| Tahun | 2019 |
| Venue | Sensors Switzerland |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | persimmon/guava |

## Tautan Akses
- PDF: [lin2019guava.pdf](../pdf/lin2019guava.pdf)
- DOI resmi: https://doi.org/10.3390/s19020428

## Gambaran Umum

Lin dkk. (2019) menguji sistem penglihatan RGB-D untuk mendeteksi, mensegmentasi, dan menentukan pose (arah tangkai) buah guava di kebun komersial di Guangzhou, Tiongkok. Sistem memakai kamera Kinect V2 yang menghasilkan citra warna dan peta kedalaman yang sudah diselaraskan. Citra warna dianalisis dengan jaringan konvolusi penuh (*fully convolutional network*, FCN) yang memberi label setiap piksel sebagai latar, buah, atau cabang. Piksel buah kemudian diubah menjadi titik 3D dan dikelompokkan dengan *Euclidean clustering* agar tiap buah terpisah. Arah buah dihitung dari pusat buah ke titik cabang induk terdekat, dan titik cabang induk dicari dengan RANSAC.

Data terdiri atas 437 citra RGB-D yang diambil pada 8 Juli, 15 September, dan 13 Oktober 2018, tanpa lampu buatan sehingga kondisi cahaya bervariasi. Sekitar 80% citra dipakai untuk latihan dan sisanya untuk uji. Himpunan uji terdiri atas 91 citra dan 237 buah. Anotasi piksel dikerjakan secara manual dengan Image Labeler MATLAB dan memakan waktu lima hari. Pose buah hanya diukur untuk 63,55% buah uji, karena cabang induk pada sisanya tidak terlihat. Angka ini berarti evaluasi pose tidak mencakup buah yang tertutup, dan penulis tidak menyebut apakah buah tertutup berbeda dalam galatnya.

Hasil segmentasi menunjukkan FCN unggul. Mean IoU untuk buah sebesar 0,806 dan untuk cabang 0,473, dibanding SegNet (0,665 dan 0,389) dan CART (0,235 dan 0,067). Penulis menjelaskan keunggulan FCN atas SegNet dengan overfitting pada SegNet saat latihan, dan menyatakan FCN lebih cocok untuk himpunan data kecil. Pada deteksi buah, presisi 0,983 dan recall 0,949 melampaui metode Kusumam dkk. (presisi 0,941, recall 0,671), yang memakai depth filtering, Euclidean clustering, dan SVM berbasis fitur sudut. Abstrak melaporkan recall 0,948, sedangkan bagian 4.2 melaporkan 0,949. Selisih ini kecil, tetapi pembaca yang mengutip angka perlu memilih satu sumber. Galat pose 3D dilaporkan 23,43° ± 14,18° dengan waktu 0,565 detik per buah.

Keterbatasan yang disebut penulis ada dua. Pertama, sinar matahari kuat siang hari menaikkan simpangan baku data kedalaman Kinect V2 hingga 32 mm pada jarak 1 m (dikutip dari Fankhauser dkk.), sehingga titik tidak valid bertambah dan deteksi gagal. Kedua, pada empat kejadian Euclidean clustering menggabungkan dua buah bertetangga menjadi satu. Penulis mengusulkan penutup cahaya atau menghindari pengambilan citra pada tengah hari, serta menambahkan isyarat kelengkungan pada pengelompokan. Dari sisi cakupan, data berasal dari satu kebun, satu varietas (carmine), dan tiga tanggal panen, sehingga generalisasi ke kondisi lain belum diuji. Teks tidak memuat hasil pada kebun atau varietas lain.
