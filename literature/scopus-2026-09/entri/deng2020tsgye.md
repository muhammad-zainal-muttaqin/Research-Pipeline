# TSGYE: Two-Stage Grape Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `deng2020tsgye` |
| Judul asli | TSGYE: Two-Stage Grape Yield Estimation |
| Penulis | Deng, Geng; Geng, Tianyu; He, Chengxin; Wang, Xinao; He, Bangjun; Duan, Lei |
| Tahun | 2020 |
| Venue | Communications in Computer and Information Science |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [deng2020tsgye.pdf](../pdf/deng2020tsgye.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-030-63820-7_66

## Gambaran Umum

TSGYE (ICONIP 2020) memperkirakan hasil anggur dalam dua tahap. Tahap pertama mendeteksi tandan anggur. Tahap kedua mencacah buah anggur di dalam setiap kotak tandan dengan pemrosesan citra.

Detektor yang dibandingkan adalah Mask R-CNN, YOLOv2, YOLOv3, dan YOLOv4. Semuanya dilatih dan diuji pada WGISD, set data 300 citra RGB 2048×1365 piksel dengan 4.432 tandan dari lima kultivar. YOLOv4 memberi mAP@0,5 tertinggi, yaitu 96,96%. Buah anggur di dalam kotak dicari dengan transformasi Hough lingkaran (jari-jari 5 sampai 30 piksel), lalu setiap kandidat disaring dengan pengelas sederhana. Latar di luar kotak dibuang sebelum pencacahan.

Penulis melabeli tangan buah anggur pada 58 citra uji WGISD. Hanya buah yang terlihat lebih dari tiga perempat ukurannya yang dilabeli. Label ini dirilis sebagai acuan pencacahan. Galat dilaporkan per kultivar. Contohnya, untuk CDY (15 citra, 180 tandan), hitungan acuan 3.985 dan perkiraan 3.688.

Setiap citra dicacah sendiri. Acuan hanya mencakup buah yang terlihat, sehingga buah di balik buah lain tidak ikut dinilai.
