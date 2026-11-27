# An Approach for Enhancing Ripe Tomato Classification and Counting by Using Deep Learning and SAHI Image Processing

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `khiem2026approach` |
| Judul asli | An Approach for Enhancing Ripe Tomato Classification and Counting by Using Deep Learning and SAHI Image Processing |
| Penulis | Khiem, Nguyen Minh; Van Thanh, Tran; Hai, Nguyen Thanh; Bao, Le Huynh Quoc; Nghe, Nguyen Thai |
| Tahun | 2026 |
| Venue | Communications in Computer and Information Science |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [khiem2026approach.pdf](../pdf/khiem2026approach.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-031-98167-8_7

## Gambaran Umum

Kajian ini (bab prosiding Springer, 2026) mendeteksi dan mencacah tomat menurut tiga kelas kematangan, yaitu matang penuh, setengah matang, dan hijau. Metodenya YOLOv11 yang digabung dengan SAHI. SAHI adalah inferensi yang memotong citra menjadi irisan kecil supaya buah kecil dan jauh lebih mudah dideteksi.

Data berupa 904 citra dengan 11.267 tomat. Sebesar 60% citra berasal dari Kaggle, 25% dari VegNet, dan sisanya dari sumber lain. Data dibagi acak 634 latih, 135 validasi, dan 135 uji. mAP50 YOLOv11 adalah 0,888 untuk matang penuh, 0,860 untuk setengah matang, dan 0,931 untuk hijau.

Pada 135 citra uji dengan 1.996 tomat, YOLOv11 saja menemukan 1.677 tomat (0,84), sedangkan YOLOv11 dengan SAHI menemukan 1.896 (0,95). Per kelas, nilainya naik dari 0,84 menjadi 0,94 untuk matang penuh, dari 0,78 menjadi 0,98 untuk setengah matang, dan dari 0,89 menjadi 0,92 untuk hijau.

Irisan SAHI berukuran 300×300 piksel dan bertumpang tindih 30%, tetapi cara menggabungkan kotak di daerah tumpang tindih tidak dijelaskan. Akurasi hitung adalah rasio jumlah terdeteksi terhadap jumlah acuan, sehingga deteksi palsu atau ganda dapat menutupi buah yang terlewat. Setiap citra dicacah sendiri.
