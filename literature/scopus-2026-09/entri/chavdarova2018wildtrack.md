# WILDTRACK: A Multi-camera HD Dataset for Dense Unscripted Pedestrian Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chavdarova2018wildtrack` |
| Judul asli | WILDTRACK: A Multi-camera HD Dataset for Dense Unscripted Pedestrian Detection |
| Penulis | Chavdarova, Tatjana; Baque, Pierre; Bouquet, Stephane; Maksai, Andrii; Jose, Cijo; Bagautdinov, Timur; Lettry, Louis; Fua, Pascal; Van Gool, Luc; Fleuret, Francois |
| Tahun | 2018 |
| Venue | Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [chavdarova2018wildtrack.pdf](../pdf/chavdarova2018wildtrack.pdf)
- DOI resmi: https://doi.org/10.1109/cvpr.2018.00528

## Gambaran Umum

Kajian ini memperkenalkan WILDTRACK, kumpulan data dan metode untuk mendeteksi serta melacak pejalan kaki di ruang terbuka yang diamati oleh tujuh kamera yang saling tumpang tindih. Tujuannya adalah menentukan posisi setiap orang di bidang tanah (*ground plane*) dengan menggabungkan informasi dari semua kamera, sehingga satu orang yang terlihat di beberapa kamera hanya dihitung sekali. Objek yang dikaji adalah manusia, bukan buah.

Deteksi objek pada satu citra kesulitan ketika objek saling menutupi (*oklusi*). Penulis membandingkan kumpulan data yang ada dan mencatat bahwa sebagian besar belum menyediakan beberapa kamera dengan wilayah pandang yang benar-benar tumpang tindih serta anotasi posisi di bidang tanah. Tanpa data seperti itu, metode lintas kamera sulit diuji. Kajian ini mengisi kekosongan tersebut dengan data yang direkam di luar ruangan dan dianotasi secara terukur.

Gagasan utamanya adalah memakai semua pandangan secara bersamaan. Setiap kamera diproyeksikan ke bidang tanah melalui kalibrasi, lalu hasil deteksi dari kamera-kamera itu digabung. Penalaran oklusi kemudian memperkirakan siapa yang tertutup oleh siapa di bidang tanah, sehingga hasil akhir berupa satu titik per orang, bukan satu kotak per citra.

Perekaman memakai empat kamera GoPro Hero 3 dan tiga GoPro Hero 4 dengan resolusi 1920×1080 dan 60 fps. Sinkronisasi antarkamera berada sekitar 50 ms. Kalibrasi dilakukan dengan 1398 titik 3D yang dianotasi, lalu diperhalus dengan *bundle adjustment* yang meminimalkan galat reproyeksi (Persamaan 1 dalam naskah). Dataset berisi 400 bingkai beranotasi per rangkaian, lebih dari 40.000 kotak, dan lebih dari 300 individu.

Metode deteksi yang dibandingkan meliputi DeepMCD (*Deep Multi-camera Detection*), yang memetakan peluang hunian ke bidang tanah dari fitur CNN setiap kamera, dan Deep-Occlusion Reasoning, yang menambahkan CRF (*conditional random field*) dengan inferensi *mean-field* untuk memodelkan oklusi. Untuk pelacakan, digunakan K-Shortest Paths (KSP) pada peta hunian, lalu lintasan dihaluskan dengan ptrack.

Evaluasi deteksi memakai MODA, MODP, presisi, dan recall pada ambang jarak 0,5 m di bidang tanah. Deep-Occlusion+KSP mencapai MODA 0,752. Deep-Occlusion tanpa KSP mencapai MODA 0,741 dengan presisi 0,95 dan recall 0,80. Varian ResNet-DeepMCD mencapai MODA 0,678, DenseNet-DeepMCD 0,635, dan Top-DeepMCD 0,601. Peta hunian dengan CNN (POM-CNN) hanya mencapai MODA 0,232. Model satu pandang (ResNet-View 1 sampai 7) berkisar dari MODA −1,841 sampai 0,466, sehingga pandang tunggal jauh lebih lemah daripada pandang gabungan.

Untuk pelacakan, DeepOcclusion+KSP mencapai IDF1 73,2 dan MOTA 69,6. Dengan ptrack, IDF1 naik menjadi 78,4 dan MOTA menjadi 72,2. Penulis menyimpulkan bahwa penggunaan semua pandang secara bersama meningkatkan kinerja deteksi secara nyata, dan penalaran oklusi eksplisit menaikkan MODA lebih lanjut.

Kelebihan utama kajian ini adalah kumpulan data yang terkalibrasi dan beranotasi di bidang tanah, sehingga perbandingan antarmetode dapat diulang. Dari sisi rekayasa, kelebihan lain adalah bukti kuantitatif bahwa pandang gabungan jauh mengungguli pandang tunggal pada data yang sama. Keterbatasan dari sisi analisis penulis bab ini: dataset hanya berisi pejalan kaki pada satu lokasi luar ruang, sehingga penerapannya pada objek yang kecil dan tertutup daun belum diuji.
