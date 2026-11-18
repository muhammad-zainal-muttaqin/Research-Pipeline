# Lightweight Deep Learning with Intra-Class Half-Mixing and Geometric Augmentation for Imbalanced Oil Palm Fresh Fruit Bunch Ripeness Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `madadum2026lightweight` |
| Judul asli | Lightweight Deep Learning with Intra-Class Half-Mixing and Geometric Augmentation for Imbalanced Oil Palm Fresh Fruit Bunch Ripeness Classification |
| Penulis | Madadum, Hadee; Nasir, Fazal E.; Haruehansapong, Kanjana |
| Tahun | 2026 |
| Venue | Agriengineering |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [madadum2026lightweight.pdf](../pdf/madadum2026lightweight.pdf)
- DOI resmi: https://doi.org/10.3390/agriengineering8070296

## Gambaran Umum

Kajian ini mengatasi klasifikasi kematangan tandan buah segar (TBS) kelapa sawit di ramp penerimaan pabrik. Pemeriksaan manual oleh inspektor berdasarkan warna, tekstur permukaan, dan jumlah buah lepas bersifat subjektif, memakan waktu, dan berbeda antarinspektor. Kajian juga menyoroti keterbatasan komputasi di ramp yang dikelola koperasi petani, yang sering berada di lokasi terpencil tanpa akses layanan cloud yang andal. Tujuan kajian adalah membangun kerangka klasifikasi ringan yang tetap akurat pada data lapang tidak seimbang dan dapat dijalankan pada perangkat tepi. Hipotesisnya, penggabungan pencampuran intra-kelas dengan transformasi geometri meningkatkan pengenalan kelas minoritas tanpa mengorbankan efisiensi komputasi.

Tanaman yang dikaji adalah kelapa sawit. Dataset berisi 857 citra yang dikumpulkan di satu ramp sawit di Distrik Khlong Thom, Provinsi Krabi, Thailand, pada koordinat 7,892781° LU, 99,115334° BT. Tiga kolektor memotret dengan iPhone 13 Pro pada jarak tetap 1–1,5 m, satu tandan utama per citra, pada pukul 10.00–12.00 dan 16.00–18.00 selama satu minggu. Tiga pakar penilai dari ramp memberi label melalui konsensus; rekaman penilaian independen tidak disimpan, sehingga statistik kesepakatan antarpenilai tidak dapat dihitung. Empat kelas kematangan adalah *Over-ripe* (112), *Ripe* (231), *Under-ripe* (334), dan *Unripe* (180). Pembagian berlapis 70/20/10 menghasilkan 598 citra latih, 170 validasi, dan 89 uji. Ketimpangan diukur dengan *imbalance ratio* (IR) terhadap kelas minoritas *Over-ripe*; rasio kelas mayoritas *Under-ripe* terhadap minoritas adalah 3:1.

Mekanisme utama berupa strategi augmentasi E5 yang menggabungkan dua tahap. Tahap pertama, *intra-class half-mixing* berbasis YOCO, membagi citra menjadi dua bagian sejajar dan mengganti salah satu bagian dengan potongan dari citra lain dalam kelas yang sama. Dengan parameter pencampuran q = 0,25, probabilitas pertukaran kiri dan kanan masing-masing 25 persen, sementara 50 persen sisanya memakai YOCO standar pada satu citra. Karena kedua bagian berasal dari kelas yang sama, label tetap terjaga tanpa peluruhan label. Tahap kedua menerapkan transformasi geometri berupa rotasi θ ∼ U(−20°, +20°) dan skala s ∼ U(0,9; 1,3) untuk menghilangkan garis sambungan buatan dan mencegah jaringan mempelajari artefak tersebut. Penulis membandingkan enam konfigurasi (E0 tanpa augmentasi, E1 standar, E2 CutMix, E3 YOCO, E4 pencampuran intra-kelas, E5 usulan). E5 menaikkan sampel minoritas secara spesifik per kelas dan menurunkan IR maksimum dari 3,0× menjadi 1,4×. Enam backbone ringan diuji: MobileNetV2, EfficientNetV2B0/B1, YOLOv8n-cls, YOLO11n-cls, dan YOLO26n-cls. Pelatihan memakai AdamW, laju pembelajaran awal 0,001, batch 16, 100 epoch, masukan 224 × 224 × 3, serta *class-weighted cross-entropy*.

Evaluasi memakai akurasi keseluruhan, presisi, *recall*, dan F1 per kelas serta F1 makro pada cawat uji 89 citra. YOLOv8n-cls dengan E5 mencatat akurasi tertinggi 95,6 persen dan F1 makro 0,955, naik 12,4 poin persentase dari baseline tanpa augmentasi (83,2 persen). EfficientNetV2B0 dan EfficientNetV2B1 masing-masing mencapai 94,8 persen di bawah E5. Kelima dari enam model mencapai akurasi dan F1 makro tertinggi pada E5; pengecualian MobileNetV2 lebih baik pada E2 (92,0 persen). Seluruh model keluarga YOLO mencapai *recall* 1,00 untuk kelas minoritas *Over-ripe* dengan presisi sekurangnya 0,923, sehingga F1 kelas tersebut 0,960. YOLOv8n-cls memiliki *recall* per kelas 1,00; 0,96; 0,97; dan 0,91 berturut-turut untuk *Over-ripe*, *Ripe*, *Under-ripe*, dan *Unripe*, dengan seluruh laju kesalahan antarkelas tidak melebihi 0,03. Ukuran model keluarga YOLO berkisar 2,83–3,05 MB dengan latensi 3,59 ± 0,82 hingga 4,64 ± 0,94 ms per citra pada GPU NVIDIA RTX 3080 12 GB.

Penulis menyatakan sejumlah batasan. Dataset hanya 857 citra dari satu ramp di Thailand yang dikumpulkan dalam satu minggu, sehingga jumlah sampel per kelas pada cawat validasi dan uji kecil, terutama untuk *Over-ripe*. Model mungkin tidak langsung berpindah ke lokasi lain karena penampilan tandan dipengaruhi wilayah, praktik budidaya, musim panen, kultivar, tanah, dan iklim. Anotasi hanya melibatkan tiga penilai dari satu lokasi, dan kesepakatan antarpenilai tidak divalidasi secara kuantitatif. Tidak ada uji signifikansi statistik, sehingga perbedaan kinerja dibaca sebagai tren empiris, bukan bukti keunggulan yang terkonfirmasi. Latensi diukur hanya pada GPU desktop, sehingga tidak mewakili kinerja perangkat tertanam. Kesalahan masih terkonsentrasi pada pasangan kelas berdekatan, yaitu *Ripe*–*Over-ripe* akibat pencahayaan dan sudut pandang, serta *Under-ripe*–*Unripe* akibat ukuran tandan kecil dan kepadatan buah pada masukan 224 × 224.

