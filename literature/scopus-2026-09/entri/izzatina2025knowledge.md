# Knowledge Distillation for Efficient Ordinal Classification of Oil Palm Ripeness Level

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `izzatina2025knowledge` |
| Judul asli | Knowledge Distillation for Efficient Ordinal Classification of Oil Palm Ripeness Level |
| Penulis | Izzatina, Almira Raisa; Kamal, Imam Mustafa; Navastara, Dini Adni; Revanda, Aldinata Rizky |
| Tahun | 2025 |
| Venue | 2025 15th International Conference on Information and Communication Technology and System AI for the Now and Next Delivering Solutions and Driving Vision Icts 2025 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [izzatina2025knowledge.pdf](../pdf/izzatina2025knowledge.pdf)
- DOI resmi: https://doi.org/10.1109/icts67612.2025.11369518

## Gambaran Umum

Kajian ini bertujuan mengklasifikasikan kematangan tandan buah segar (TBS) kelapa sawit secara ordinal dengan model ringan. Penulis menyebut penilaian manual memakan tenaga dan tidak konsisten, sedangkan model dalam yang berat sulit dijalankan pada perangkat terbatas. Penulis memakai distilasi pengetahuan (*knowledge distillation*), yaitu pelatihan model kecil (siswa) agar meniru distribusi probabilitas model besar (guru), bukan hanya label keras.

Data berupa 4.728 citra TBS berukuran 256×256 piksel yang disebut diambil pada kondisi lapangan perkebunan Indonesia. Lima kelas: belum matang 758 (16%), setengah matang 1.405 (30%), matang penuh 1.489 (31%), terlalu matang 665 (14%), dan membusuk 411 (9%). Pemberi label, sensor, tempat, dan jumlah pohon tidak disebut. Pembagian acak berstrata: latih 3.306 (70%), validasi 704 (15%), uji 718 (15%). Pembagian per pohon tidak disebut.

Guru adalah ResNet18, ResNet34, ResNet50, atau ResNet101 (jaringan residual). Siswa adalah MobileNetV2, jaringan ringan dengan konvolusi terpisah per kedalaman. Masukan 112×112 piksel. Fungsi kerugian gabungan memakai softmax bersuhu (suhu T diatur umumnya 3 sampai 5) dan bobot α = 0,7 antara kerugian distilasi dan entropi silang. Pembanding adalah VGG16, AlexNet, ResNet101, ConvNeXt-Tiny, EfficientNetV2, MobileViT-S, dan MobileNetV2 mandiri.

Hasil terbaik: MobileNetV2 siswa dengan guru ResNet50 mencapai akurasi 95,64% ± 0,63%, dibanding 94,48% ± 0,57% untuk MobileNetV2 mandiri. Selisih perbaikan antar guru berkisar 0,27% sampai 1,16%. Parameter MobileNetV2 2,23 juta, 91% lebih sedikit dibanding ResNet101 (42,51 juta). Lari terbaik mencapai 96,38%. Data ujinya: 718 citra uji dari set yang sama.

Keterbatasan: penulis menyatakan keragaman data terbatas (geografi, musim, kultivar) dan hanya memakai modalitas visual. Dari teks: tidak ada pembagian per pohon, citra tunggal per tandan tanpa deteksi, tidak ada uji pada set data luar, dan perbaikan 1,16 poin dari siswa mandiri berada di dekat simpangan baku. Nilai MSE di teks (0,0860 untuk hasil distilasi, 0,0175 untuk mandiri) bertentangan dengan klaim perbaikan, sehingga tidak dapat diperiksa dari teks.
