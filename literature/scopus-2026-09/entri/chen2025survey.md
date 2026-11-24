# Survey of Advances in Semi-Supervised Learning Methods for Crop Image Processing Applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2025survey` |
| Judul asli | Survey of Advances in Semi-Supervised Learning Methods for Crop Image Processing Applications |
| Penulis | Chen, Xi; Liu, Jianping; Zhou, Guomin; Wang, Jian; Zhang, Yue; Xing, Jialu |
| Tahun | 2025 |
| Venue | Computer Engineering and Applications |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [chen2025survey.pdf](../pdf/chen2025survey.pdf)
- DOI resmi: https://doi.org/10.3778/j.issn.1002-8331.2410-0016

## Gambaran Umum

Artikel berbahasa Mandarin ini, dengan abstrak berbahasa Inggris, adalah tinjauan naratif tentang pembelajaran semi-terawasi untuk citra tanaman. Pembelajaran semi-terawasi melatih model dengan sedikit data berlabel dan banyak data tanpa label, sehingga kebutuhan anotasi berkurang. Artikel ini tidak melaporkan basis data, kueri, atau kriteria pemilihan kajian.

Bagian pertama menyusun model konseptual dari definisi dan asumsi dasar pembelajaran semi-terawasi. Metodenya dibagi menjadi dua keluarga menurut cara memakai sinyal pengawasan. Keluarga pertama adalah label semu: model memberi label pada data tanpa label, lalu label dengan keyakinan tinggi dipakai untuk melatih ulang. Keluarga kedua adalah regularisasi tanpa label, misalnya menuntut keluaran yang konsisten untuk dua versi citra yang sama.

Bagian kedua mengulas penerapan menurut tugas: deteksi objek, segmentasi, klasifikasi, dan pembelajaran beberapa tugas sekaligus. Kasusnya mencakup pengelolaan tanaman, gulma, deteksi buah, kesehatan tanaman, fenotipe, dan klasifikasi daun. Contohnya, satu kajian deteksi tahap tumbuh delima melaporkan presisi rata-rata 90,8% dengan hanya 10% data berlabel, lebih tinggi daripada YOLOv8l.

Pencacahan buah hanya muncul sebagai satu metode, CMCNet, yang menaksir peta kepadatan buah pada citra tunggal dengan tugas bantu pewarnaan citra. Penautan buah antarcitra dan hitung ganda tidak dibahas. Penutupnya membahas arah riset pembelajaran semi-terawasi untuk citra pertanian.
