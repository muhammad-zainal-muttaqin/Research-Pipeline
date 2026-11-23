# DETECTION IN COMPLEX SCENES USING RGB AND DEPTH MULTIMODAL FEATURE FUSION

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yan2024detection` |
| Judul asli | DETECTION IN COMPLEX SCENES USING RGB AND DEPTH MULTIMODAL FEATURE FUSION |
| Penulis | Yan, Shengli; Rao, Yuan; Hou, Wenhui |
| Tahun | 2024 |
| Venue | ICASSP IEEE International Conference on Acoustics Speech and Signal Processing Proceedings |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | pear |

## Tautan Akses
- PDF: [yan2024detection.pdf](../pdf/yan2024detection.pdf)
- DOI resmi: https://doi.org/10.1109/icassp48485.2024.10448205

## Gambaran Umum

Kajian ini mengusulkan metode deteksi buah pada citra RGB dan *depth* (citra jarak tiap piksel ke kamera) untuk kebun yang ditanami rapat. Penulis menyatakan bahwa citra *depth* lebih tahan terhadap adegan kompleks daripada citra RGB. Penggabungan sederhana dengan penjumlahan atau penyambungan dinilai tidak memisahkan fitur yang dimiliki bersama dan fitur khas tiap modalitas.

Data utama adalah set data pir berkantong buatan penulis dari kebun komersial di Kecamatan Xuanmiao, Kabupaten Dangshan, Provinsi Anhui, Tiongkok. Citra diambil dengan kamera Azure Kinect (RGB 1280×720, *depth* 640×576, jangkauan 0,5-3,86 m, galat acak kurang dari 17 mm). Terkumpul 2544 pasang citra warna dan *depth*. Buah diberi label empat kelas oklusi: tanpa oklusi, tertutup daun, tertutup buah, dan tertutup cabang. Pemberi label dan pembagian latih/uji tidak disebut. Set data kedua adalah set data publik RGB-D apel Fuji.

Metode memakai jaringan dua aliran yang mengekstrak fitur RGB dan *depth* secara terpisah pada tiga skala. Modul fusi multimodal (MMFF) menggabungkan fitur tengah kedua aliran. Modul ini terdiri atas modul seleksi diferensial, yang memakai atensi gaya *selective kernel* untuk memberi bobot kanal tiap modalitas, dan modul penguat fitur bersama, yang memakai unit seleksi spasial dan kanal dari SCConv untuk menekan fitur berulang. Pelatihan memakai citra 640×640, ukuran *batch* 32, dan 200 *epoch*.

Pada set data pir, mAP deteksi hanya RGB 84,5% dan hanya *depth* 79,2%. Fusi dengan penjumlahan mencapai 87,2% dan penyambungan 87,7%. MMFF mencapai 89,7% dengan 67,0 juta parameter. AP per kelas MMFF adalah 92,6% (tanpa oklusi), 91,6% (daun), 87,5% (buah), dan 87,0% (cabang). YOLOv7x mencapai 82,1% dengan 71,3 juta parameter. Pada set data apel Fuji, MMFF mencapai mAP 97,5%, dibandingkan YOLOv5l 93,4%.

Keterbatasan yang dapat diperiksa: tidak ada pencacahan, hanya deteksi dengan AP dan mAP. Pembagian data latih, validasi, dan uji tidak disebut, sehingga tidak diketahui apakah ada pemisahan per pohon atau per kebun. Tidak ada rata-rata dari beberapa percobaan atau selang kepercayaan. Hanya satu pandang per citra yang digunakan. Satu citra tidak ditautkan ke citra lain dari buah yang sama.
