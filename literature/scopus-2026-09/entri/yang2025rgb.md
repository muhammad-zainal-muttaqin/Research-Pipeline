# An RGB-D Multi-modal Apple Recognition and Instance Segmentation Method for Orchard Harvesting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2025rgb` |
| Judul asli | An RGB-D Multi-modal Apple Recognition and Instance Segmentation Method for Orchard Harvesting |
| Penulis | Yang, Mingji; Teng, Da |
| Tahun | 2025 |
| Venue | Proceedings of 2025 2nd International Symposium on AI and Cybersecurity Isaics 2025 |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [yang2025rgb.pdf](../pdf/yang2025rgb.pdf)
- DOI resmi: https://doi.org/10.1109/isaics66888.2025.11350135

## Gambaran Umum

Penelitian ini bertujuan melokalisasi apel untuk pemetikan otomatis di kebun. Penulis menyebut oklusi dan cahaya latar sebagai kendala model berbasis RGB saja, yang tidak memberi posisi sasaran cukup tepat untuk pencengkeraman. Mereka mengusulkan model segmentasi instans RGB-D dua cabang berbasis YOLOv11n-seg.

Data berasal dari set data publik PApple-RGB-D-Size: 3.925 citra RGB PNG 1200×1200 piksel dari enam pohon apel Fuji pada tahap pertumbuhan berbeda, masing-masing dengan peta kedalaman (*depth*) berformat NPY. Terdapat 15.335 apel berlabel. Tiga pohon berada pada tahap matang akhir dan tiga pohon dicitrakan saat apel sekitar 70% ukuran akhir. Data dibagi latih, validasi, dan uji dengan rasio 8:1:1. Pemberi label tidak disebut.

Modelnya memakai dua cabang ekstraksi fitur: tulang punggung (*backbone*) YOLOv11 untuk RGB dan MobileNetV4 untuk kedalaman. Modul perhatian silang (*cross-attention*) dua arah, disebut PSFM, menggabungkan fitur kedua modalitas. Modul DySample membangkitkan kernel *upsampling* secara dinamis untuk memperhalus tepi mask. Operasi *star* ditambahkan ke modul C3K2.

Pada ablasi, model dasar YOLOv11n-seg mencapai Box mAP50 0,886 dan Mask mAP50 0,882. Model akhir mencapai 0,915 dan 0,909, naik 2,9% dan 2,7%. Penambahan kedalaman saja menaikkan keduanya sebesar 0,007 dan 0,009. Pada perbandingan, YOLOv12n-seg terbaik di antara pembanding (0,897 dan 0,894). Semua angka dari satu set data.

Keterbatasan dapat diperiksa dari teks. Pembagian 8:1:1 dilakukan pada citra, dan teks tidak menyebut pembagian per pohon, padahal hanya ada enam pohon. Tidak ada ulangan dengan *seed* lain atau interval kepercayaan. Tidak ada lengan kontrol kanal kedalaman berisi derau. Tidak ada pencacahan buah atau penautan antarpandang. Hanya satu set data apel yang dipakai.
