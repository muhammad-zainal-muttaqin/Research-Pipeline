# Populating Digital Orchards: Evaluation of a 3D Positioning Algorithm for Semi-Automated Data Collection and Spawning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `simini2024populating` |
| Judul asli | Populating Digital Orchards: Evaluation of a 3D Positioning Algorithm for Semi-Automated Data Collection and Spawning |
| Penulis | Simini, Antonella; Piani, Mirko; Bortolotti, Gianmarco; Sanchez, Alberto Martinez; Mengoli, Dario; Manfrini, Luigi |
| Tahun | 2024 |
| Venue | 2024 IEEE International Workshop on Metrology for Agriculture and Forestry Metroagrifor 2024 Proceedings |
| Kode | C5 (Depth, 3D, dan non-RGB) |

## Tautan Akses
- PDF: [simini2024populating.pdf](../pdf/simini2024populating.pdf)
- DOI resmi: https://doi.org/10.1109/metroagrifor63043.2024.10948798

## Gambaran Umum

Kajian ini mengevaluasi algoritma penentuan posisi 3D buah pada satu tanaman terhadap pangkal batang, memakai citra RGBD. Penulis menyebut kebutuhan representasi tanaman berpresisi tinggi untuk manajemen kebun dan pembuatan kembaran digital (*digital twin*) kebun. Posisi buah juga dipakai untuk memetakan sebaran hasil dan menjadi dasar penjarangan serta pemanenan otonom. Kajian ini tidak bertujuan mencacah buah.

Data dikumpulkan di laboratorium dan kebun dengan kamera Intel RealSense D435i pada tripod setinggi 1,1 m, berjarak 1,5 m dari pohon. Di laboratorium dipakai pohon tiruan dengan apel dan bola tenis, dalam pengaturan 2D dan 3D. Terkumpul 27 pasang citra RGBD berisi 405 objek (2D) dan 12 pasang berisi 300 objek (3D). Di kebun, tiga buah per pohon dipilih dan ditandai dari lima pohon untuk tiap sistem pelatihan tajuk (*Spindle* dan *Planar Cordon*), menghasilkan 5 pasang citra berisi 15 objek per sistem. Kotak pembatas dianotasi manual dengan Supervisely. Koordinat acuan diukur manual dengan pita ukur. Pembagian latih/uji tidak ada karena tidak ada model yang dilatih.

Metode memproyeksikan balik setiap piksel ke koordinat ruang memakai parameter intrinsik kamera dan matriks kedalaman. Hasilnya disimpan dalam tensor enam kanal (x, y, z, R, G, B). Koordinat lalu digeser ke titik asal pada penanda merah muda di pangkal batang lewat matriks translasi. Posisi tiap objek diambil dari piksel pusat anotasinya. Atribut ukuran, bobot, dan warna rerata kemudian ditulis ke berkas dunia Gazebo (*spawning*), simulator robotika. Tiap objek diperlakukan sebagai satu pengamatan pada satu citra.

Hasil di laboratorium: bias rerata (MBE) +0,001 m pada sumbu x, -0,010 m pada y, dan +0,043 m pada z. Galat akar kuadrat rerata (RMSE) jarak Manhattan 0,057 m (2D) dan 0,072 m (3D), jarak Euklides 0,045 m dan 0,056 m. Di kebun, RMSE jarak Manhattan 0,460 m (*Planar Cordon*) dan 0,607 m (*Spindle*), jarak Euklides 0,370 m dan 0,380 m. Galat di kebun hampir sepuluh kali lipat galat laboratorium. Waktu proses 3,5 ms per objek di laboratorium dan 3,4 ms di kebun.

Keterbatasan: sampel di kebun hanya 15 objek per sistem, sehingga korelasi posisi tidak bermakna. Pengaruh latar, jenis objek, dan ukuran tidak diuji di kebun. Anotasi dibuat manual, bukan hasil detektor. Acuan koordinat diukur tangan dengan ketidakpastian ±0,01 m, dan antarpengukur di kebun 0,050 sampai 0,200 m. Penanda batang harus terlihat. Tidak ada penautan buah yang sama antarcitra atau antarposisi kamera, dan tidak ada pencacahan.
