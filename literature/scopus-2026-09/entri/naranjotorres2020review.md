# A review of convolutional neural network applied to fruit image processing

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `naranjotorres2020review` |
| Judul asli | A review of convolutional neural network applied to fruit image processing |
| Penulis | Naranjo-Torres, Jos\'e; Mora, Marco; Hern\'andez-Garc\'\ia, Ruber; Barrientos, Ricardo J.; Fredes, Claudio; Valenzuela, Andres |
| Tahun | 2020 |
| Venue | Applied Sciences Switzerland |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [naranjotorres2020review.pdf](../pdf/naranjotorres2020review.pdf)
- DOI resmi: https://doi.org/10.3390/app10103443

## Gambaran Umum

Tinjauan ini mengkaji penerapan *convolutional neural network* (CNN) pada pemrosesan citra buah. Penulis berangkat dari kebutuhan rantai agro-pangan akan pengenalan buah otomatis, baik untuk klasifikasi jenis di pasar grosir dan ritel, pengendalian mutu berupa kerusakan dalam maupun luar dan tingkat kematangan, maupun deteksi buah di kebun untuk panen otomatis. CNN dipilih karena merupakan arsitektur utama *deep learning* untuk citra yang mampu mempelajari representasi secara otomatis. Penulis menyatakan bahwa tinjauan sebelumnya tidak menganggap CNN sebagai pendekatan yang relevan, sehingga kajian ini disajikan sebagai tinjauan pertama yang mengulas penerapan CNN untuk pemrosesan citra buah secara luas.

Penulis membatasi pencarian pada tahun 2015 hingga 2020 karena keterbaruan topik. Kata kunci utama adalah "Fruits" dan "Convolutional Neural Network", dipadukan dengan kata kunci bantu "deep learning", "classification", "quality", dan "detection". Pencarian dilakukan di *Web of Science*, Scopus, serta situs penerbit MDPI, IEEE Xplore Digital Library, dan arXiv. Artikel dikelompokkan ke dalam tiga bidang, yaitu klasifikasi buah, pengendalian mutu buah, dan deteksi buah untuk panen otomatis; ketiga bidang ini mencakup hampir seluruh rantai penanganan buah mulai dari panen hingga konsumen akhir. Tinjauan ini juga menyajikan dasar teori CNN dan dua contoh penerapan, yaitu klasifikasi buah dan pengendalian mutu.

Mekanisme yang dirangkum mencakup arsitektur buatan sendiri dan arsitektur terlatih, seperti LeNet-5, AlexNet, VGG, GoogLeNet/Inception, dan ResNet. CNN memakai operasi konvolusi pada sedikitnya satu lapisan untuk mengekstraksi ciri; jumlah lapisan dan filter disesuaikan dengan kompleksitas tugas. Transfer *learning* memakai bobot ImageNet dengan basis konvolusi yang dibekukan dan lapisan *fully connected* bagian atas yang diganti. Dari studi yang dikumpulkan, 70% memakai model terlatih dan 29,2% memakai model buatan sendiri. Pada deteksi buah, model buatan sendiri kurang dari 6%, sementara VGG mencapai 52,9% dan ResNet 35,3%; pendekatan yang dipakai antara lain segmentasi semantik, *Faster R-CNN*, dan *fully convolutional network* dengan masukan RGB, RGB-D, multi-kamera, maupun gabungan NIR dan LiDAR.

Berbagai angka dilaporkan dengan metrik dan acuan hitung yang beragam. Untuk klasifikasi, CNN dengan kurang dari 13 lapisan mencapai akurasi sekitar 99%. Pada contoh himpunan data Fruit-360, model yang diusulkan mencapai akurasi uji 95,45% dan skor-F1 0,96 atas 1.034 citra uji dengan validasi silang 10 lipat; AlexNet mencapai 100%, VGG16 91,32%, MobileNet 70,02%, InceptionV3 54,49%, dan ResNet50 57,74%. Pada contoh pengendalian mutu Apple-NDDA, model mencapai akurasi 81,25% dan skor-F1 0,87 atas 222 citra uji dengan akurasi kelas cacat 90%, sedangkan transfer VGG16 mencapai 89,58%. Pada deteksi, jambu menghasilkan presisi 0,983 dan *recall* 0,948 dengan waktu 0,565 detik per buah; markisa mencapai akurasi deteksi 92,71% dan klasifikasi kematangan 91,52%; strawberi mencapai *average precision* 88,03% untuk kelas matang dan 77,21% untuk kelas mentah; tomat mencapai akurasi uji 91% pada citra nyata dan 93% pada citra sintetis; apel dan mangga mencapai skor-F1 tingkat piksel 0,791 dan koefisien determinasi r² = 0,826; paprika mencapai skor-F1 0,807–0,838; dan pendekatan multi-pandang pada mangga menghasilkan tingkat galat 1,36% per pohon. Angka-angka ini dihitung pada himpunan uji masing-masing studi dengan label buatan manusia sebagai acuan.

Penulis mencatat beberapa batasan. Tidak ada satu arsitektur CNN yang dapat ditetapkan lebih unggul dari yang lain, dan kompleksitas model perlu disesuaikan dengan kompleksitas tugas serta jumlah data yang tersedia. Model yang terlalu dalam mengalami overfitting pada himpunan data kecil meskipun sudah memakai augmentasi dan *dropout*. Kinerja pengendalian mutu pada contoh Apple-NDDA masih dianggap kurang memadai untuk sistem nyata karena mutu dan ukuran basis data. Tinjauan sebelumnya sebagian besar mengumpulkan informasi sebelum 2019, dan studi penerapan CNN pada buah baru meluas pada akhir 2018. Beberapa studi juga dibatasi pada sedikit kelas dan himpunan data kecil. Penulis melihat hasil hingga 100% pada beberapa kasus, tetapi pertumbuhan penerapan terbesar justru berada pada sektor panen robotik.
