# Improving passion fruit yield estimation with multi-scale feature fusion and density-attention mechanisms in smart agriculture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xu2025improving` |
| Judul asli | Improving passion fruit yield estimation with multi-scale feature fusion and density-attention mechanisms in smart agriculture |
| Penulis | Xu, Di; Wang, Chenxi; Li, Manzhou; Ge, Xinjin; Zhang, Jiahe; Wang, Wuxiong; Lv, Chunli |
| Tahun | 2025 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | passion fruit |

## Tautan Akses
- PDF: [xu2025improving.pdf](../pdf/xu2025improving.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2025.110958

## Gambaran Umum

Penghitungan buah markisa (*Passiflora edulis*) secara manual lambat, melelahkan, dan rentan terhadap kesalahan manusia. Metode berbasis warna dan bentuk juga kurang andal ketika pencahayaan berubah, buah tertutup daun atau cabang, dan latar belakang rumit. Kajian ini berangkat dari masalah tersebut. Penulis menyusun kerangka deteksi untuk memperkirakan hasil panen markisa dari citra kamera, dengan tiga tantangan utama: buah yang tertutup daun, buah kecil yang sulit dikenali, dan buah yang tumbuh rapat sehingga terhitung ganda. Penulis juga menyatakan bahwa jumlah buah sulit dipetakan langsung dari hasil deteksi objek konvensional.

Data dikumpulkan di rumah kaca Biro Meteorologi, Kabupaten Wuyuan, Kota Bayannur, Mongolia Dalam, pada periode Januari 2023 hingga Oktober 2024. Dua perangkat dipakai. Kamera Canon EOS R8 menghasilkan citra 6000 × 4000 piksel dengan lensa tetap 50 mm, dan iPhone 15 Pro menghasilkan citra 2556 × 1179 piksel dengan kamera utama lebar. Citra statis diambil dengan kamera, sedangkan citra dinamis diambil dengan ponsel di area yang padat. Seluruh citra diberi label, termasuk citra dengan oklusi latar belakang, buah kecil, dan kelompok buah padat, masing-masing 1.987, 1.764, dan 1.832 citra. Dataset dibagi dengan rasio 7:2:1 untuk data latih, validasi, dan uji. Penulis juga memakai validasi silang *k-fold* dengan k = 10 untuk meningkatkan generalisasi.

Model yang diusulkan memadukan *cross-multi-scale feature fusion* dan mekanisme *density-attention*. Augmentasi data memakai *cutout* untuk meniru oklusi daun serta *copy-and-resize* untuk menambah sampel buah kecil dan kepadatan tinggi. Pada pengujian segmentasi, model mencapai presisi 0,88, recall 0,83, akurasi 0,85, dan F1-score 0,85. Penulis juga melaporkan bahwa model mengungguli model pembanding pada semua metrik yang diuji, terutama pada presisi, recall, dan akurasi. Sebagai pembanding, UNet pada Tabel 1 mencapai presisi 0,74, recall 0,77, akurasi 0,75, mAP@50 0,74, mAP@95 0,43, dan 72,5 FPS. Penulis mengaitkan keunggulan model dengan kemampuannya menangani buah kecil dan area padat, yang tercermin pada skor mAP@50 dan mAP@95 yang lebih tinggi.
