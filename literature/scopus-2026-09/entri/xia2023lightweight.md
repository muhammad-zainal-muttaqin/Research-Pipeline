# A Lightweight Fruit Load Estimation Model for Edge Computing Equipment

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xia2023lightweight` |
| Judul asli | A Lightweight Fruit Load Estimation Model for Edge Computing Equipment |
| Penulis | Xia, Xue; Chai, Xiujuan; Zhang, Ning; Zhou, Shuo; Sun, Qixin; Sun, Tan |
| Tahun | 2023 |
| Venue | Smart Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [xia2023lightweight.pdf](../pdf/xia2023lightweight.pdf)
- DOI resmi: https://doi.org/10.12133/j.smartag.sa202305004

## Gambaran Umum

Artikel berbahasa Mandarin ini, dengan abstrak berbahasa Inggris, menaksir jumlah jeruk di pohon dari video dengan model yang cukup ringan untuk perangkat tepi (*edge*) NVIDIA Jetson AGX. Masalah yang disebut adalah hitung sampel manual yang lambat dan rawan galat, serta pelacak dua tahap yang terlalu berat untuk perangkat di kebun.

Data berupa 40 video jeruk Wogan dari satu kebun di Nanning, Guangxi, direkam dengan ponsel genggam sambil berjalan sepanjang baris pada jarak 0,5 sampai 1,0 m (1080×1920, 24 bingkai per detik). Tiga puluh video dipakai untuk latih dan 10 video, masing-masing satu pohon, untuk uji. Dari video latih diambil satu citra tiap 30 bingkai (2.846 citra). Kotak buah dilabeli, dan buah yang sama pada citra berurutan diberi nomor yang sama dengan alat pelabel buatan penulis.

Modelnya mengikuti FairMOT, yaitu pelacak yang melatih deteksi tanpa *anchor* dan fitur penampilan (*re-identification*) dalam satu jaringan. *Backbone*-nya diganti CSPDarkNet53 dengan PAFPN agar lebih ringan, dan langkah asosiasinya diganti algoritme Byte, yang ikut mencocokkan kotak berkeyakinan rendah. Buah dihitung sebagai ID yang terlacak lebih dari 5 bingkai.

Pada 10 video uji (14 sampai 125 buah per pohon), akurasi hitung rata-rata 91,61% terhadap hitungan yang diperiksa tangan di video, dengan R² 0,9858, RMSE 4,17 buah, dan 14,76 bingkai per detik. Tabel 5 membandingkan asosiasi asli FairMOT dengan asosiasi Byte pada data dan *backbone* yang sama. Akurasi hitung naik untuk ketiga *backbone*: 85,67% menjadi 86,98% (ResNet34), 90,75% menjadi 91,53% (HRNet18), dan 85,76% menjadi 91,61% (CSPDarkNet53 dengan PAFPN).

Keterbatasan yang dapat diperiksa: uji hanya 10 pohon dari satu kebun, tanpa sebaran antarvideo. Acuan adalah hitungan buah yang terlihat di video, bukan hitungan di pohon atau hasil panen. Buah tidak diberi kelas, dan sisi lain pohon tidak direkam.
