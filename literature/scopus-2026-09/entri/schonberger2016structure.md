# Structure-from-Motion Revisited

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `schonberger2016structure` |
| Judul asli | Structure-from-Motion Revisited |
| Penulis | Schonberger, Johannes L.; Frahm, Jan-Michael |
| Tahun | 2016 |
| Venue | Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [schonberger2016structure.pdf](../pdf/schonberger2016structure.pdf)
- DOI resmi: https://doi.org/10.1109/cvpr.2016.445

## Gambaran Umum

Kajian ini membahas rekonstruksi tiga dimensi dari kumpulan citra yang diambil dari berbagai sudut pandang tanpa urutan tertentu. Masalah utama pada *Structure-from-Motion* (SfM) inkremental adalah ketahanan (*robustness*), akurasi, kelengkapan, dan skalabilitas. Penulis menyatakan bahwa sistem yang ada belum dapat dipakai sebagai metode umum. Karena itu, penulis mengusulkan algoritma SfM baru yang bertujuan memperbaiki keempat aspek tersebut. Implementasinya dirilis sebagai perangkat lunak sumber terbuka bernama COLMAP.

Data yang digunakan adalah 17 kumpulan data yang seluruhnya berisi 144.953 foto dari internet yang tidak berurutan. Foto tersebut tersebar pada area yang luas dengan kepadatan kamera yang sangat bervariasi. Kumpulan data Quad memiliki lokasi kamera kebenaran dasar (*ground truth*), sehingga dapat dipakai untuk mengukur galat rekonstruksi. Contoh hasil pada Roma menunjukkan 21 ribu citra terdaftar dari 75 ribu citra. Seluruh eksperimen memakai fitur RootSIFT. Setiap citra dicocokkan dengan 100 tetangga terdekatnya menggunakan *vocabulary tree* yang dilatih pada kumpulan data lain. Waktu komputasi diukur pada mesin 2,7 GHz dengan memori 256 GB, dan waktu pencocokan citra tidak dihitung.

Metode terdiri atas beberapa komponen yang memperbaiki tahap SfM inkremental. Komponen pertama adalah augmentasi graf adegan (*scene graph augmentation*), yang menambah keterkaitan antarcitra untuk membantu registrasi. Komponen kedua adalah pemilihan tampilan terbaik berikutnya (*next best view selection*), yang mengurutkan citra berdasarkan jumlah dan distribusi titik terlihat sehingga citra dengan konfigurasi lebih baik didaftarkan lebih dahulu. Komponen ketiga adalah triangulasi yang tahan terhadap pencilan, yang memakai RANSAC dan mampu memisahkan titik-titik independen yang sebelumnya tergabung dalam satu lintasan fitur. Komponen keempat adalah penyesuaian berkas (*bundle adjustment*) yang dipercepat untuk kumpulan citra padat. Komponen kelima adalah penambangan tampilan berlebih (*redundant view mining*), yang melanjutkan lintasan titik yang sebelumnya gagal didaftarkan. Penulis menyatakan bahwa sistem ini mengungguli sistem inkremental Bundler dan VisualSFM serta sistem global DISCO dan Theia pada hal kelengkapan, ketahanan, akurasi, dan efisiensi. Angka perbandingan yang dinyatakan secara eksplisit dalam teks hanya berupa jumlah citra terdaftar pada contoh Roma tersebut.

Batasan yang dinyatakan penulis terutama berkaitan dengan tujuan jangka panjang. Penulis menyebut bahwa SfM belum sepenuhnya bersifat umum, dan algoritma ini hanya langkah menuju tujuan itu. Teks tidak memuat bagian batasan tersendiri, sehingga keterbatasan lain tidak dapat dirinci dari naskah ini. Untuk keperluan tinjauan pencacahan buah, makalah ini relevan sebagai rujukan metode rekonstruksi multi-citra yang dapat dipindahkan. Makalah ini tidak memuat deteksi buah maupun evaluasi pencacahan buah.
