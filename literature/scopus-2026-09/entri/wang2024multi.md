# Multi Perspective Point Cloud Reconstruction Method for Sweet Pepper Fruit under Occlusion Conditions

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2024multi` |
| Judul asli | Multi Perspective Point Cloud Reconstruction Method for Sweet Pepper Fruit under Occlusion Conditions |
| Penulis | Wang, Y.; others |
| Tahun | 2024 |
| Venue | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | sweet pepper |

## Tautan Akses
- PDF: [wang2024multi.pdf](../pdf/wang2024multi.pdf)
- DOI resmi: https://doi.org/10.6041/j.issn.1000-1298.2024.05.020

## Gambaran Umum

Kajian ini membahas pengukuran fenotipe buah paprika (*sweet pepper*, varietas Luska) langsung di tanaman (*in situ*) di rumah kaca, yaitu tinggi dan lebar buah. Penulis menyebut buah yang tertutup daun menurunkan keberhasilan deteksi saat pengukuran. Penulis mengusulkan rekonstruksi tiga dimensi (3D) awan titik buah dari beberapa sudut pandang, dengan sudut pandang yang disesuaikan menurut posisi buah dan tingkat tutupannya. Buah tidak dicacah. Tujuan kajian adalah ukuran buah.

Data deteksi diambil di rumah kaca Guangdong Academy of Agricultural Sciences pada 2 April 2023 sebanyak 1.700 citra. Kamera yang dipakai adalah Olympus TG-4 beresolusi 3.200 x 2.400 piksel pada jarak 350 sampai 700 mm. Penulis menambah data dengan daun virtual (100 potongan daun ditempel pada 500 citra buah, 1.500 citra) dan dengan simulasi cuaca (1.500 citra). Total menjadi 3.000 citra, dibagi 8:2 menjadi 2.400 citra latih dan 600 citra validasi. Pemberi label memakai LabelImg, dan jumlah orangnya tidak disebut. Ada tiga kelas: buah tanpa tutupan, tutupan 0 sampai 30%, dan tutupan 30 sampai 60%.

Detektor YOLO v5, yaitu detektor satu tahap berbasis *convolutional network*, dilatih 200 epoch pada citra 640 x 640 piksel dengan *batch* 32. Robot beroda memakai kamera kedalaman Azure Kinect DK untuk menemukan buah. Lengan robot 6 sumbu CR5 lalu membawa kamera cahaya terstruktur RVC X mini ke 6, 10, atau 15 sudut pandang, sesuai tingkat tutupan. Posisi kamera ditentukan lewat kalibrasi tangan-mata. Awan titik dari tiap sudut pandang disatukan dengan ICP (*iterative closest point*, yaitu pencocokan dua awan titik dengan meminimalkan jarak titik terdekat). Buah dipisahkan dari tanaman, dan tinggi serta lebar buah diambil dari kotak pembatas terkecil awan titik buah.

Pada data validasi, detektor mencapai presisi 91,5%, *recall* 92,7%, dan mAP 95,3% untuk seluruh kelas. Per kelas, mAP adalah 98,0% (tanpa tutupan), 94,2% (tutupan 0 sampai 30%), dan 93,8% (tutupan 30 sampai 60%). Pada uji rekonstruksi, 30 awan titik (10 per kelas tutupan) dibandingkan dengan ukuran jangka sorong. Galat relatif rata-rata keseluruhan adalah 1,72% untuk satu dimensi dan 1,60% untuk dimensi lainnya. Abstrak menyebut 1,72% untuk lebar dan 1,60% untuk tinggi, sedangkan simpulan menyebut sebaliknya (tinggi 1,72%, lebar 1,60%). Galat maksimum yang dilaporkan 3,54%.

Keterbatasan yang dapat diperiksa dari teks adalah sebagai berikut. Pembagian latih dan validasi dilakukan setelah augmentasi, sehingga citra turunan dari citra yang sama dapat berada di kedua himpunan. Tidak ada data uji terpisah untuk detektor. Pembagian per tanaman tidak disebut. Uji ukuran hanya memakai 30 buah dari satu varietas di satu rumah kaca. Tutupan hanya diuji sampai 60%. Tidak ada pencacahan buah dan tidak ada penautan buah yang sama antar-sudut pandang selain registrasi awan titik.
