# Intelligent yield estimation for tomato crop using SegNet with VGG19 architecture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `maheswari2022intelligent` |
| Judul asli | Intelligent yield estimation for tomato crop using SegNet with VGG19 architecture |
| Penulis | Maheswari, Prabhakar; Raja, Purushothamman; Hoang, Vinh Truong |
| Tahun | 2022 |
| Venue | Scientific Reports |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [maheswari2022intelligent.pdf](../pdf/maheswari2022intelligent.pdf)
- DOI resmi: https://doi.org/10.1038/s41598-022-17840-6

## Gambaran Umum

Penelitian ini bertujuan membangun sistem estimasi hasil panen tomat yang mendeteksi, melokalisasi, dan menghitung buah di lapangan. Estimasi hasil secara manual memerlukan tenaga ahli, bersifat subjektif, dan memakan waktu lama untuk lahan luas. Penulis mengusulkan segmentasi semantik SegNet dengan tulang punggung VGG19 dan menyatakan ini sebagai pekerjaan pertama deteksi buah tomat dengan arsitektur tersebut.

Tanaman yang diteliti adalah tomat. Data awal berupa 123 citra RGB dari himpunan data publik Rob2Pheno (Afonso dkk.), yang direkam dengan empat kamera Intel RealScene pada troli di rumah kaca tomat di Belanda. Citra berukuran 720×1280 piksel, diambil dari jarak 5 m pada malam hari untuk menghindari variasi pencahayaan. Anotasi memakai Computer Vision Annotation Tool dengan tiga kelas, yaitu tomat matang (piksel merah), tomat belum matang (piksel hijau), dan latar. Augmentasi berupa translasi ±5 satuan pada arah x dan y serta rotasi ±10° menghasilkan 672 citra untuk latih.

Metode memodifikasi SegNet asli yang memakai 13 lapisan pertama VGG16 dengan menambah tiga lapisan pada setiap sisi pengode dan dekode agar memakai 16 lapisan pertama VGG19; tiga lapisan penuh terakhir dihapus. Pengode mengekstrak ciri oleh tumpukan lapisan konvolusi dengan ReLU dan max-pooling, sedangkan dekode mengganti max-pooling dengan upsampling dan hanya menerima indeks max-pooling, bukan seluruh peta ciri, untuk menghemat memori. Prediksi dilakukan per piksel ke dalam tiga kelas tersebut. Pelatihan memakai SGD, laju pembelajaran awal 0,001, ukuran kumpulan mini 8, 100 epoch, 67 iterasi per epoch, maksimum 6.700 iterasi, regularisasi L2, dan faktor penurunan laju 0,3. Pemrosesan memakai MATLAB 2021a dengan GPU NVIDIA GeForce GTX 1080. Pembagian data adalah 80 persen latih dan 20 persen validasi. Metrik presisi, recall, IoU, dan skor F1 dihitung dari true positive, false positive, false negative, dan true negative pada piksel.

Pada himpunan validasi, SegNet dengan VGG19 mencapai presisi 97,62 persen, recall 75,37 persen, IoU 84,57 persen, dan F1 85,06 persen; SegNet dengan VGG16 berturut-turut 90,30 persen, 72,44 persen, 82,90 persen, dan 80,39 persen; U-Net berturut-turut 85,40 persen, 70,55 persen, 80,10 persen, dan 77,28 persen. Uji lapangan dilakukan di desa Manapparai, Trichy, India, pada lahan sekitar seperempat acre dengan varietas Novo84 dan sampel 33×16 kaki. Enam puluh lima citra diambil satu minggu sebelum panen dengan kamera ponsel 16 MP beresolusi 4608×3456 piksel. Hasil uji adalah presisi 89,7 persen, recall 72,55 persen, IoU 82,57 persen, F1 80,22 persen, dan loss 19,82 persen. Pasca-pemrosesan memakai kontur dan kotak pembatas dengan ambang 0,5, lalu membedakan tomat merah dan hijau dari intensitas piksel. Hitungan model menghasilkan 4.760 buah, sedangkan data manual petani sekitar 5.000 buah, yang dihitung dari seperempat acre ≈ 20 kotak × 20 kg × 12 buah per kg. Tingkat deteksi 91 persen ketika satu buah tertutup buah lain sedikit, dan turun menjadi 84 persen ketika tertutup buah, daun, dan ranting secara besar.

Batasan yang dinyatakan penulis: recall lebih rendah daripada presisi karena sejumlah piksel tomat diprediksi sebagai latar, dan presisi turun pada buah yang tertutup seluruhnya. Penggunaan VGG sebagai tulang punggung membuat waktu eksekusi menjadi hambatan untuk aplikasi waktu nyata. Penulis mengusulkan arsitektur segmentasi lain seperti YOLO atau DeepLabV3+ sebagai pengganti pada pekerjaan berikutnya.
