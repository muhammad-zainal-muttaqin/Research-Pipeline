# Semantic segmentation model for greenhouse tomato images using RGB and depth bimodal

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2024semantic` |
| Judul asli | Semantic segmentation model for greenhouse tomato images using RGB and depth bimodal |
| Penulis | Zhang, Y.; others |
| Tahun | 2024 |
| Venue | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [zhang2024semantic.pdf](../pdf/zhang2024semantic.pdf)
- DOI resmi: https://doi.org/10.11975/j.issn.1002-6819.202309169

## Gambaran Umum

Penulis menyebut bahwa buah tomat yang belum matang di rumah kaca berwarna mirip dengan batang dan daun. Kemiripan ini menurunkan ketelitian *segmentasi semantik* (pemberian label kelas pada setiap piksel citra). Penelitian ini mengusulkan model DFST (*depth-fusion semantic transformer*) yang menambahkan citra kedalaman sebagai modalitas pendamping citra warna (RGB) agar piksel buah tomat lebih mudah dipisahkan dari daun dan batang.

Data berupa citra tomat di rumah kaca yang diambil dengan kamera Azure Kinect pada tiga rentang waktu (08.00 sampai 10.00, 12.00 sampai 14.00, dan 16.00 sampai 18.00) dari berbagai sudut dan posisi. Terkumpul 1.000 pasang citra RGB dan kedalaman. Setelah penyaringan citra mirip dengan *cosine similarity* (kemiripan sudut antarvektor) dengan ambang 0,88 dan pemeriksaan manual, tersisa 500 pasang. Sebanyak 450 pasang (90%) menjadi data latih dan 50 pasang (10%) data uji. Data latih diperbesar menjadi 2.500 citra dengan augmentasi. Pemberi label piksel tidak disebut.

DFST memakai dua *encoder* Mix Transformer (Mit), satu untuk RGB dan satu untuk kedalaman. Kedalaman lebih dahulu diubah menjadi citra tiga kanal HHA (selisih horizontal, tinggi di atas tanah, dan sudut permukaan terhadap arah gravitasi). Modul koreksi memperbaiki fitur kedua modalitas, modul fusi menggabungkannya, dan *decoder* berupa perceptron berlapis ringan menghasilkan peta segmentasi. Fungsi kerugian *focal loss* dipakai karena piksel latar jauh lebih banyak daripada piksel tomat. *Encoder* diinisialisasi dari bobot yang dilatih pada ImageNet-1K.

Pada data uji, DFST dengan masukan RGB+HHA mencapai rerata *intersection over union* (mIoU, rasio irisan terhadap gabungan area prediksi dan label) 96,99% dan akurasi piksel 95,13%. Masukan RGB saja memberi mIoU 95,62% dan akurasi piksel 92,92%. Masukan RGB+kedalaman mentah memberi mIoU 95,78% dan akurasi piksel 93,18%. Dibandingkan *backbone* ResNet101, Swin-S, dan Swin-B, Mit lebih tinggi 2,42, 1,52, dan 0,79 poin persentase mIoU. Dibandingkan ShapeConv, SA-gate, dan CMX dengan masukan RGB+HHA, DFST lebih tinggi 2,43, 1,97, dan 1,21 poin.

Keterbatasan yang dapat diperiksa: data uji hanya 50 pasang citra dan pembagiannya per citra, tanpa keterangan pembagian per tanaman, sehingga citra dari tanaman yang sama dapat berada di data latih dan uji. Tidak ada pencacahan buah, deteksi per buah, ataupun pelacakan antarcitra. Tidak ada kontrol berupa kanal kedalaman berisi derau, sehingga kenaikan 1,37 poin mIoU belum dibedakan dari efek tambahan kanal masukan. Satu spesies, satu lokasi, satu sensor. Penulis menyebut hasil bergantung pada mutu citra kedalaman.
