# Research on Lightweight Apple Detection and 3D Accurate Yield Estimation for Complex Orchard Environments

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2026research` |
| Judul asli | Research on Lightweight Apple Detection and 3D Accurate Yield Estimation for Complex Orchard Environments |
| Penulis | Chen, Bangbang; Sun, Xuzhe; Liu, Xiangdong; Ma, Baojian; Ding, Feng |
| Tahun | 2026 |
| Venue | Horticulturae |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [chen2026research.pdf](../pdf/chen2026research.pdf)
- DOI resmi: https://doi.org/10.3390/horticulturae12030393

## Gambaran Umum

Penelitian ini mengatasi dua masalah yang saling terkait dalam pemanenan apel otomatis: deteksi visual yang akurat dan estimasi hasil yang tepat di kebun kompleks. Oklusi daun dan ranting yang rapat, pencahayaan yang berubah secara dinamis, serta keragaman ukuran target menyebabkan model yang baik di laboratorium mengalami penurunan akurasi dan stabilitas di kebun nyata. Di sisi estimasi hasil, metode penghitungan citra 2D mengabaikan variasi volume buah dan rentan terhadap perspektif serta oklusi, sementara metode berbasis informasi 3D umumnya memerlukan sensor kedalaman presisi tinggi dan algoritma rekonstruksi yang kompleks. Penulis mengusulkan solusi terpadu berupa model deteksi ringan YOLO-WBL dan algoritma estimasi hasil Collaborative Local Volumetric (CLV) yang memanfaatkan awan titik dari kamera kedalaman.

Data dikumpulkan di kebun apel kerdil dan rapat di Aksu, Xinjiang, dengan kultivar utama Fuji termasuk Changfu 2, Qiufu 1, dan Yanfu 2; tinggi pohon dijaga di bawah 3,5 m. Pengambilan memakai Huawei Nova7 dan kamera kedalaman Intel RealSense D455 secara sinkron, dengan variasi pencahayaan (depan, belakang, samping, naungan kanopi), sudut pandang (atas, horizontal, bawah), dan jarak 0,1–1,0 m. Dataset awal berisi 1.634 citra apel yang diambil pada 20 September 2025; setelah augmentasi berupa rotasi ±30°, penyesuaian kecerahan, saturasi, dan derau Gaussian menjadi 2.014 citra, lalu dibagi menjadi 1.410 latih, 403 validasi, dan 201 uji dengan anotasi format PASCAL VOC. Setiap apel dipanen segera setelah pemotretan dan ditimbang dengan timbangan presisi 0,01 g sebagai acuan kebenaran. YOLO-WBL dibangun di atas YOLOv11n dengan tiga perubahan: modul C3K2_WT yang menggabungkan Wavelet Transform Convolution pada backbone, BiFPN pada neck, dan kepala deteksi ringan Detect-SCGN.

Mekanisme deteksi memanfaatkan dekomposisi frekuensi untuk menangkap tekstur dan kontur tanpa membengkakkan parameter. WTConv menguraikan fitur menjadi komponen frekuensi rendah LL dan frekuensi tinggi HL, LH, HH, melakukan konvolusi depthwise dengan kernel kecil pada tiap pita, lalu menyusunnya kembali dengan inverse wavelet transform; dengan demikian kernel kecil bekerja pada reseptif field efektif yang lebih luas. BiFPN menyederhanakan topologi PANet dengan menghapus simpul yang hanya memiliki satu masukan, menambahkan koneksi lewati pada level yang sama, dan memberi bobot adaptif yang dapat dipelajari untuk fusi lintas skala. Detect-SCGN berbagi bobot konvolusi dangkal dan menormalkan tiap cabang keluaran secara terpisah dengan Group Normalization untuk menekan parameter. CLV kemudian memetakan kotak ikat dan koordinat piksel dari deteksi ke koordinat 3D menggunakan parameter intrinsik kamera, merekonstruksi awan titik permukaan buah yang tampak, mengira volume per buah melalui convex hull yang dikoreksi dengan analisis PCA terhadap sferisitas, lalu menjumlahkannya menjadi estimasi hasil total; pendekatan ini menolak penyederhanaan apel sebagai bola atau elipsoid beraturan serta penggunaan berat rata-rata.

Hasil deteksi pada himpunan uji menunjukkan presisi 93,8%, recall 79,3%, dan mAP@0,5 sebesar 87,2%. Model hanya berisi 1,7 juta parameter dan berukuran 3,72 MB, masing-masing lebih rendah 34,61% dan 28,87% dibanding YOLOv11n, dengan 7,2 GFLOPs; kecepatan inferensi mencapai 8,7 FPS saat diterapkan pada NVIDIA Jetson Xavier NX. Untuk estimasi hasil, CLV menghasilkan galat absolut rata-rata sekitar 3,2% untuk berat per buah, dibandingkan sekitar 17,5% pada metode rekonstruksi awan titik tradisional; abstrak juga melaporkan MAPE estimasi hasil dapat dijaga di bawah 8% pada skenario dengan tingkat oklusi di bawah 40%. Galat dihitung sebagai |m0 − m|/m0 × 100%, dengan m0 berupa massa timbangan manual dan m massa estimasi algoritma, sehingga angka tersebut bertumpu pada 201 citra uji dan pengukuran massa aktual. Penulis menyatakan CLV mengungguli metode berbasis berat rata-rata konvensional.

Batasan yang dinyatakan penulis mencakup sifat analisis robustitas yang terutama kualitatif dan berbasis demonstrasi visual pada empat skenario tertentu, bukan evaluasi kuantitatif terstruktur; penulis menyebut pengukuran penurunan mAP akibat oklusi dan anotasi yang lebih rinci sebagai pekerjaan mendatang. Deteksi masih melewatkan sejumlah target kecil di tepi pada skenario sudut lebar dengan tandan rapat, sehingga ruang perbaikan masih ada pada oklusi ekstrem. Selain itu, data berasal dari satu kultivar, satu lokasi, dan satu hari pengambilan, sehingga generalisasi ke kultivar, kebun, atau tanaman lain tidak dinyatakan dalam teks yang dibaca.
