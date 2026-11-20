# Deep Learning with Data Augmentation for Fruit Counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `pawara2020deep` |
| Judul asli | Deep Learning with Data Augmentation for Fruit Counting |
| Penulis | Pawara, Pornntiwa; Boshchenko, Alina; Schomaker, Lambert R. B.; Wiering, Marco A. |
| Tahun | 2020 |
| Venue | Lecture Notes in Computer Science Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [pawara2020deep.pdf](../pdf/pawara2020deep.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-030-61401-0_20

## Gambaran Umum

Pencacahan buah dalam citra penting untuk pengelolaan kebun, tetapi sulit dilakukan karena buah saling menutupi dan dataset berlabel untuk tugas ini jarang tersedia. Kajian ini mengusulkan teknik *data augmentation* yang disebut *fruit data-augmentation* (FDA). Teknik ini membuat citra baru dengan menambahkan potongan buah yang sudah diisolasi ke citra asli. Dengan cara ini, jumlah citra dan jumlah buah per citra bertambah, sementara label jumlah atau *bounding box* tetap akurat. Penulis juga membandingkan dua pendekatan pencacahan, yaitu regresi holistik dan berbasis deteksi, untuk mengetahui pendekatan mana yang lebih diuntungkan oleh augmentasi.

Data yang digunakan adalah dataset *Five-Tropic-Fruits* (FTF) yang dikumpulkan penulis dari internet. Dataset ini memuat lima kelas buah, yaitu apel, srikaya, lemon, pir, dan kesemek. Setiap kelas terdiri atas 300 citra, sehingga totalnya 1.500 citra. Setiap citra hanya memuat satu jenis buah dengan satu sampai 15 buah, dan citra dapat berupa pemandangan dalam ruangan atau luar ruangan. Dataset dibagi menjadi 80% data latih dan 20% data uji, dan eksperimen memakai validasi silang lima lipatan. Penulis tidak menyebutkan sensor kamera atau platform pengambilan citra. Anotasi dibuat secara manual dengan LabelImg. Pendekatan regresi hanya memerlukan jumlah buah per citra, sedangkan pendekatan deteksi memerlukan koordinat *bounding box* untuk setiap buah.

Metode yang diuji adalah ResNet50 dan Inception-V3 untuk regresi, serta Faster R-CNN dan SSD-MobileNet untuk deteksi. Setiap arsitektur dilatih dari awal (*scratch*) maupun melalui *fine-tuning*, baik pada data asli maupun data augmentasi. Pada pendekatan regresi, semua model augmentasi lebih baik daripada model asli dengan peningkatan 15%–31%. Nilai MAECC terbaik adalah 0,26, dicapai oleh ResNet50 hasil *fine-tuning* yang dilatih dengan data augmentasi, dibandingkan 0,38 pada model asli. Untuk MAECO, ResNet50 dari awal membaik 38%, dari 3,1 menjadi 1,93. Nilai MAECO terbaik adalah 1,07. Untuk MAEMC, versi *fine-tuning* membaik 67%. Pada pendekatan deteksi, augmentasi tidak memberikan perbedaan yang signifikan. Faster R-CNN tetap menjadi pendekatan deteksi terbaik dan mengungguli pendekatan regresi, tetapi SSD-MobileNet kalah dari pendekatan regresi ketika augmentasi dipakai bersama CNN pralatih.

Penulis menyatakan beberapa batasan. Pertama, pendekatan deteksi terbaik memerlukan anotasi *bounding box* manual pada setiap buah, yang jauh lebih lama daripada pelabelan jumlah total per citra. Kedua, augmentasi tidak membantu pendekatan deteksi karena FDA tidak menambahkan jenis tampilan buah yang baru, sehingga variasi lokal tidak bertambah. Ketiga, hasil diuji pada lima jenis buah dengan citra dari internet, bukan citra kebun yang diambil langsung. Penulis merencanakan penelitian lanjutan tentang deteksi penyakit tanaman dan metode augmentasi lain untuk mengatasi terbatasnya citra tanaman sakit.
