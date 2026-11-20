# Grape yield estimation with a smartphone's colour and depth cameras using machine learning and computer vision techniques

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `parr2023grape` |
| Judul asli | Grape yield estimation with a smartphone's colour and depth cameras using machine learning and computer vision techniques |
| Penulis | Parr, Baden; Legg, Mathew; Alam, Fakhrul |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | grape |

## Tautan Akses
- PDF: [parr2023grape.pdf](../pdf/parr2023grape.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.108174

## Gambaran Umum

Penelitian ini bertujuan membuat estimasi hasil panen anggur yang otomatis. Estimasi hasil panen penting bagi petani anggur untuk merencanakan pemangkasan dan penjarangan buah. Cara manual bersifat subjektif, merusak, dan memakan waktu. Cara manual juga dapat menghasilkan sampel yang kurang mewakili kebun. Penelitian sebelumnya umumnya hanya mendeteksi tandan pada citra RGB. Penghitungan buah individual jarang dilakukan karena kamera RGB-D berbiaya rendah memiliki resolusi yang terbatas. Penulis mengusulkan pemanfaatan kamera warna dan kamera *time of flight* (ToF) pada satu ponsel pintar.

Data dikumpulkan dengan ponsel Samsung Note 10+ pada tanaman anggur Chardonnay. Pengambilan citra dilakukan di lapangan dan di laboratorium. Di laboratorium, tandan diputar 360 derajat pada sebuah *turntable*. Ponsel merekam citra RGB, peta kedalaman, dan peta kepercayaan setiap 10 derajat. Sudut yang terhalang struktur platform tidak diambil. Total terdapat 1062 citra dari 34 tandan. Selain itu, 120 pemindaian tanaman anggur dalam pot tanpa buah juga diambil. Resolusi citra RGB diturunkan menjadi 640 x 480 agar sama dengan peta kedalaman. Kalibrasi kedua kamera dilakukan dengan pola papan catur.

Metode pertama mendeteksi buah dari puncak pada peta kedalaman ToF. Puncak ini muncul karena hamburan difus di dalam setiap buah. Algoritma persistensi mendeteksi puncak tersebut. Filter *signed distance field* kemudian membuang puncak di tepi objek, jaring, dan daun. Metode ini berhasil mendeteksi sebagian besar buah yang terlihat, tetapi sebagian buah di tepi hilang. Nilai R2 untuk regresi linear antara jumlah buah yang terlihat pada citra RGB dan jumlah buah yang terdeteksi adalah 0,68. Presisi rata-rata metode ini adalah 0,893. Metode kedua memakai hasil deteksi puncak untuk melatih model YOLOv7 tanpa anotasi manual. Citra latih ditambah latar dedaunan melalui penyamaran berbasis kedalaman. Model YOLOv7 mencapai R2 0,946 antara jumlah buah yang terdeteksi dan jumlah buah yang dihitung manual pada citra RGB. Presisi rata-rata model ini adalah 0,970. Penulis juga menyajikan dua teknik untuk memperkirakan ukuran buah dan membangun model 3D tandan.

Penulis menyatakan beberapa batasan. YOLOv7 cenderung kurang menghitung buah dibandingkan hitungan manual, meskipun hubungannya kuat. Penulis menilai kompensasi linear dapat memperbaiki hal ini. Buah di tepi tandan sering terlewat karena sebagian besar buah tertutup buah lain. Metode puncak juga kurang peka terhadap buah tertutup di tepi. Model juga kesulitan dengan tandan di latar belakang yang tidak fokus. Model kadang mendeteksi buah yang layu. Warna pada peta point cloud belum dimanfaatkan dalam penelitian ini. Penulis menyarankan pemakaian informasi kedalaman dan penyaringan spasial untuk mengurangi positif palsu di masa depan.
