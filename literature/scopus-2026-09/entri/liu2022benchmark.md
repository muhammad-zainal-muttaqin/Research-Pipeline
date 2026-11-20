# A benchmark for multi-class object counting and size estimation using deep convolutional neural networks

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2022benchmark` |
| Judul asli | A benchmark for multi-class object counting and size estimation using deep convolutional neural networks |
| Penulis | Liu, Zixu; Wang, Qian; Meng, Fanlin |
| Tahun | 2022 |
| Venue | Engineering Applications of Artificial Intelligence |
| Kode | C4 (Atribut kelas dan pencacahan) |

## Tautan Akses
- PDF: [liu2022benchmark.pdf](../pdf/liu2022benchmark.pdf)
- DOI resmi: https://doi.org/10.1016/j.engappai.2022.105449

## Gambaran Umum

Liu, Wang, dan Meng (2022) mengusulkan penghitungan multi-kelas dan estimasi ukuran objek dari satu citra. Mereka membuat dataset sintetis MOCSE13 dengan Unity yang berisi 13 kelas buah dan sayur. Model memprediksi peta kepadatan (density map) dan peta ukuran (size map) per kelas, lalu algoritma IOSR dengan pencocokan TM mengambil ukuran tiap objek.

Pada dataset tiga kelas, MAE penghitungan berkisar 1,21 sampai 1,93 dan MAPE ukuran 13,34 sampai 16,67 persen (Tabel 5). Pada backbone TEDNet, MAE penghitungan 1,31 dan MAPE ukuran 11,09 persen (Tabel 7). Penulis sendiri menyatakan bahwa evaluasi belum dilakukan pada data dunia nyata.

Model menggunakan backbone yang dapat dipertukarkan. Hasil pada Tabel 7 membandingkan TEDNet, Inception-v3, VGG-16-bn, Resnet-50, Densenet-121, dan ShuffleNet v2 x 0.5. Tiga backbone (Inception-v3, VGG-16-bn, dan satu lainnya) tidak mengestimasi ukuran sehingga ditandai N.A.

Tahap estimasi ukuran memakai IOSR dengan pencocokan TM. Pada Tabel 8, IOSR dengan TM mencapai recall 98,72 persen (VGG-16-bn, apel) dan 99,75 persen (TEDNet, apel). CCL dan Watershed diukur dengan object detection rate.

Pada Tabel 6, MAE penghitungan untuk pisang turun dari 15,29 (6 citra latih) menjadi 1,69 (42 citra latih) dan 1,91 (60 citra latih). Pembanding yang diuji adalah MCNN, CCL, dan Watershed.

Kelebihan utama adalah dataset sintetis berlabel lengkap untuk 13 kelas, sehingga ukuran dan jumlah tiap objek diketahui pasti. Keterbatasannya: seluruh evaluasi memakai data Unity, belum ada uji pada citra lapangan, dan penulis merencanakan penelitian lanjutan dengan data supermarket. Dari sisi penghitungan kebun, kajian ini tidak membahas tandan sawit, tampilan multi-pandang, atau identitas lintas pandang.
