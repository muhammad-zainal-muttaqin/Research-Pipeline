# Segmentation of oil palm crop bunch from tree images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `siddesha2018segmentation` |
| Judul asli | Segmentation of oil palm crop bunch from tree images |
| Penulis | Siddesha, S; Niranjant, S K; Aradhya, V N Manjunath |
| Tahun | 2018 |
| Venue | Proceedings of the 2017 International Conference on Smart Technology for Smart Nation Smarttechcon 2017 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [siddesha2018segmentation.pdf](../pdf/siddesha2018segmentation.pdf)
- DOI resmi: https://doi.org/10.1109/smarttechcon.2017.8358639

## Gambaran Umum

Kajian ini membandingkan enam metode segmentasi untuk memisahkan tandan sawit dari latar pada citra pohon. Penulis menyebut bahwa segmentasi adalah langkah awal panen dan sulit karena latar berisi daun, bunga, dan kulit batang dengan warna serta tekstur serupa. Tujuannya adalah menentukan metode terbaik untuk langkah itu, sebab penulis tidak menemukan kajian lain tentang segmentasi tandan sawit.

Data berupa sekitar 100 citra pohon sawit dari kebun di sekitar Mysuru, India, dipotret dengan kamera digital Nikon Coolpix L810 zoom 26×. Ground truth (segmentasi acuan) dibuat dengan segmentasi manual. Teks memakai dua jumlah berbeda, 100 citra untuk dataset dan 20 citra untuk rerata Tabel 2. Teks tidak menyebut pembagian latih dan uji, dan tidak menyebut siapa pembuat ground truth.

Metode meliputi K-Means dan *Fuzzy C-Means* (pengelompokan tanpa label), *hill climbing* (pemilihan puncak histogram warna), *random walker* (segmentasi interaktif berbasis peluang), *grow cut* (segmentasi interaktif berbasis automata sel), dan MSRM (penggabungan wilayah berdasarkan kemiripan maksimal) yang dimulai dari pra-segmentasi *mean shift*. Tujuh ukuran dipakai untuk membandingkan hasil dengan ground truth: korelasi, Jaccard, Dice, RMSE, Rand Index, GCE, dan VOI.

Hasil utama pada Tabel 2 (rerata 20 citra): MSRM memberi korelasi 0,58, Rand Index 0,86, GCE 0,53, dan VOI 6,32. Nilai itu tertinggi atau terendah sesuai arah ukurannya. Baris label Tabel 2 dalam teks ekstraksi tidak sejajar dengan nilainya, sehingga angka perlu diperiksa ulang pada PDF.

Keterbatasan yang dapat diperiksa: hasil bergantung pada 20 citra, dan teks tidak menyebut pembagian uji. Kajian ini tidak menghitung jumlah tandan. Metode interaktif memerlukan penanda manual dari pengguna. Penulis menyebut MSRM hanya sebagian memisahkan latar depan, sedangkan tabelnya menunjukkan nilai tertinggi untuk MSRM.
