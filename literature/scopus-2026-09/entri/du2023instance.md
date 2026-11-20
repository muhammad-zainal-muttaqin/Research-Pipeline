# Instance Segmentation and Berry Counting of Table Grape before Thinning Based on AS-SwinT

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `du2023instance` |
| Judul asli | Instance Segmentation and Berry Counting of Table Grape before Thinning Based on AS-SwinT |
| Penulis | Du, Wensheng; Liu, Ping |
| Tahun | 2023 |
| Venue | Plant Phenomics |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [du2023instance.pdf](../pdf/du2023instance.pdf)
- DOI resmi: https://doi.org/10.34133/plantphenomics.0085

## Gambaran Umum

Kajian ini mengusulkan AS-SwinT, model deteksi dan segmentasi instance untuk menghitung butir buah anggur meja pada satu tandan sebelum penjarangan (*berry thinning*). Model memakai Swin Transformer-Tiny (*Swin-T*) sebagai *backbone* dan *Feature Pyramid Network* (FPN) sebagai *neck*, lalu menambahkan optimisasi *anchor*, *Soft-NMS*, dan *Adaptively Spatial Feature Fusion* (ASFF). Data berupa 717 citra yang diambil dengan iPhone SE pada resolusi 3.024 × 4.032 piksel, pada 28 Mei 2021. Citra dibagi menjadi 501 untuk latih, 144 untuk validasi, dan 72 untuk uji. Anotasi dibuat dengan Labelme.

Pada data uji, AS-SwinT mencapai APbox 65,7, APbox0,5 95,0, dan APbox untuk objek kecil (APbox_s) 57. Untuk segmentasi, APmask 62,8, APmask0,5 94,3, dan APmask_s 48. Untuk penghitungan jumlah butir, model menghasilkan RMSE 7,13 dan R2 0,95 pada regresi linear antara jumlah prediksi dan jumlah sebenarnya. Angka ini berasal dari teks kajian dan belum diverifikasi ulang dari berkas keluaran.

Tabel 1 memisahkan kontribusi tiap komponen. Optimisasi *anchor* menaikkan APbox sebesar 1,9. Soft-NMS menaikkan APbox0,5 sebesar 3,6, APmask0,5 sebesar 3,7, dan APbox_s sebesar 6,1. ASFF menaikkan APmask dari 60,9 menjadi 62,4. Konfigurasi AS-SwinT secara keseluruhan menaikkan APbox0,5 sebesar 8,6, APbox sebesar 3,1, APmask0,5 sebesar 8,9, APmask sebesar 2,8, APbox_s sebesar 13,6, dan APmask_s sebesar 10,4. Tabel 2 membandingkan *backbone*: SwinT-S sedikit lebih rendah daripada SwinT-T. Dengan demikian, kenaikan terbesar tercatat pada objek kecil, yang sejalan dengan tujuan kajian menghitung butir yang kecil dan rapat.

Teks kajian mencatat beberapa batasan. Data hanya mencakup varietas Shine Muscat, sehingga generalisasi ke varietas lain belum diuji. Butir yang terhalang dan butir kecil sering luput dari deteksi. Pelabelan *instance* dinilai mahal, dan kondisi pencahayaan belum diatasi. Tabel 3 melaporkan AP0,5 box 95,2 dan APbox_s 56,9 pada data buatan, dengan 50,71 juta parameter dan 241,79 GFLOPS. Kode tersedia di https://github.com/AWEN975/AS-SwinT.

Objeknya anggur meja, bukan kelapa sawit, dan kajian ini tidak memakai data kedalaman (depth). Kajian ini dapat menjadi pembanding untuk penghitungan butir pada tanaman lain, tetapi hasilnya tidak diukur pada tandan sawit.
