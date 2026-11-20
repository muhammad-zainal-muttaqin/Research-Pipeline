# Smartphone-based 3D imaging for canopy and berry cluster volume estimation in wine grapes

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `upadhyaya2025smartphone` |
| Judul asli | Smartphone-based 3D imaging for canopy and berry cluster volume estimation in wine grapes |
| Penulis | Upadhyaya, Priyanka; Paudel, Achyut; Karkee, Manoj |
| Tahun | 2025 |
| Venue | Smart Agricultural Technology |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | grape |

## Tautan Akses
- PDF: [upadhyaya2025smartphone.pdf](../pdf/upadhyaya2025smartphone.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2025.101592

## Gambaran Umum

Kajian ini bertujuan mengestimasi volume kanopi dan volume tandan buah anggur menggunakan pencitraan tiga dimensi pada *smartphone*. Estimasi volume penting untuk manajemen kebun, prediksi hasil, dan alokasi sumber daya dalam viticultur presisi. Pengukuran manual bersifat padat karya dan memakan waktu, sedangkan sensor seperti LiDAR berbiaya tinggi dan sulit dijangkau petani skala kecil dan menengah. Menurut penulis, sebagian besar studi berbasis *smartphone* sebelumnya hanya menghasilkan indeks dua dimensi atau ukuran buah. Studi tersebut juga sering bergantung pada objek kalibrasi atau pengambilan citra dari satu sudut. Kajian ini menggabungkan segmentasi YOLO11, *Structure from Motion* (SfM), dan *Gradient Boosting Classifier* dalam satu alur kerja, tanpa objek kalibrasi.

Penelitian dilakukan di kebun percobaan Washington State University di Prosser, Washington, Amerika Serikat, pada musim panen anggur Chardonnay yang telah mencapai tahap E-L 38. Perangkat yang digunakan adalah iPhone 14 Pro Max dengan sensor LiDAR dan kamera 48 MP. Data kanopi terdiri atas 30 tanaman anggur yang dipindai dengan aplikasi Scaniverse. Sepuluh tanaman dipilih secara acak untuk validasi. Data tandan dikumpulkan dengan aplikasi 3D Scanner, dengan minimal 30 citra untuk setiap tandan dari berbagai sudut. Untuk segmentasi tandan, 250 citra RGB dianotasi dan dibagi menjadi 80 persen data latih, 10 persen validasi, dan 10 persen uji. Untuk segmentasi kanopi, lima tanaman dipilih dan 1000 titik diberi label, dengan 800 titik untuk latih dan 200 titik untuk uji.

Pada kanopi, *Gradient Boosting Classifier* memisahkan titik kanopi dari latar belakang dengan akurasi segmentasi 98 persen. Permukaan kanopi kemudian direkonstruksi dengan *alpha shape* menjadi mesh kedap air. Hasil estimasi dibandingkan dengan volume acuan hasil pengukuran manual. RMSE volume kanopi adalah 0,135 m³, setara galat relatif 21,68 persen, dengan korelasi 0,7 dan bias −0,027 m³. Pada tandan, YOLO11 mencapai mAP@50 sebesar 0,90 pada data uji. Titik awan dibangun dengan SfM, dibersihkan dari *outlier* menggunakan DBSCAN, lalu dibentuk menjadi mesh. Volume acuan diukur dengan metode perpindahan air dan dirata-rata dari tiga kali pengulangan. Untuk seluruh data tandan, RMSE adalah 46,47 cm³ (44,72 persen) dengan r = 0,272. Untuk tandan dengan titik awan lengkap, RMSE turun menjadi 24,50 cm³ (22,28 persen) dengan r = 0,653 dan bias −6,16 cm³. Bias seluruh data tandan adalah −11,7 cm³. Pemrosesan kanopi membutuhkan 20 sampai 40 detik per tanaman, sedangkan tandan dengan 25 sampai 30 citra membutuhkan sekitar 2 menit.

Penulis menyebutkan beberapa batasan. Oklusi oleh daun atau tandan lain membuat titik awan tidak lengkap dan menyebabkan estimasi volume tandan cenderung rendah. Kehilangan data pada tahap pencocokan fitur SfM juga menurunkan akurasi rekonstruksi. Kedua model segmentasi hanya dilatih satu kali, sehingga stabilitas hasil antarpelatihan belum dinilai. Tandan longgar dengan celah besar lebih sulit direkonstruksi daripada tandan yang padat. Variasi cahaya, bayangan, dan latar belakang juga dapat memengaruhi pencocokan fitur dan segmentasi. Volume acuan kanopi dihitung dengan pendekatan balok persegi panjang, sehingga bentuk kanopi yang tidak beraturan tidak tergambarkan sepenuhnya. Penulis menyatakan bahwa dataset yang lebih besar dan pengulangan pelatihan di berbagai kondisi kebun diperlukan untuk menilai ketahanan pendekatan ini.
