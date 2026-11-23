# Survey of 3D Reconstruction Techniques Based on 3D Gaussian Splatting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cao2024survey` |
| Judul asli | Survey of 3D Reconstruction Techniques Based on 3D Gaussian Splatting |
| Penulis | Cao, Z.; others |
| Tahun | 2024 |
| Venue | Jiqiren Robot |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [cao2024survey.pdf](../pdf/cao2024survey.pdf)
- DOI resmi: https://doi.org/10.13973/j.cnki.robot.240088

## Gambaran Umum

Kajian ini adalah tinjauan metode tentang rekonstruksi 3 dimensi dengan *3D Gaussian splatting* (3D GS) yang diterbitkan di jurnal robotika Tiongkok pada September 2024. Penulis menyatakan bahwa 3D GS, yang diperkenalkan pada akhir 2023, lebih unggul daripada algoritma tradisional dalam kualitas sintesis pandang baru dan kecepatan *rendering*. Tinjauan ini menganalisis prinsip 3D GS dan memetakan penerapannya pada *visual SLAM* (pemetaan dan lokalisasi serentak), rekonstruksi adegan dinamis, kecerdasan buatan generatif, dan mengemudi otonom. Teks tidak membahas buah, tanaman, atau pertanian.

Kajian ini tidak memakai data sendiri dan tidak melaporkan prosedur pencarian pustaka. Daftar pustakanya memuat 91 rujukan. Data yang dikutip dari makalah lain adalah set data Replica (18 adegan dalam ruangan yang menyerupai foto nyata, dipakai untuk menilai SLAM) dan set data D-NeRF (video monokular objek sintetis dilihat dari 360 derajat, 50 sampai 200 bingkai dinamis per adegan). Tabel hasil disusun dari angka makalah asal; penulis menyebut sumber tiap baris.

3D GS menyatakan adegan dengan puluhan ribu primitif Gaussian 3 dimensi (elipsoid yang punya posisi, bentuk, dan warna). Titik awalnya dari *structure from motion* (SfM, rekonstruksi 3 dimensi dari banyak foto). Citra dibuat dengan rasterisasi paralel per blok, lalu parameter dioptimalkan dengan menurunkan selisih antara citra hasil dan citra asli. Kerapatan primitif disesuaikan secara adaptif. Penulis membandingkan ini dengan NeRF (medan radiasi saraf), yang membutuhkan latihan lama dan tidak dapat dirender waktu nyata.

Pada set data Replica, rerata PSNR (*peak signal-to-noise ratio*, rasio puncak sinyal terhadap derau) sintesis pandang adalah 24,42 dB untuk NICE-SLAM, 28,06 untuk ESLAM, dan 35,17 untuk Point-SLAM (ketiganya NeRF), serta 34,27 untuk GS-SLAM, 34,11 untuk SplaTAM, 37,5 untuk Gaussian Splatting SLAM, dan 42,08 untuk Gaussian-SLAM (semuanya 3D GS). Pada D-NeRF, PSNR 3D-GS statis 23,19 dibandingkan 34,05 untuk 4D-GS dan 34,80 untuk GauFRe. Angka diambil dari makalah asal, bukan dari percobaan penulis.

Keterbatasan yang dinyatakan penulis: 3D GS masih lemah pada pandang yang terbatas dan boros memori, sebagian aplikasinya lebih bersifat demonstrasi, dan penerapannya jauh dari praktik. Yang dapat diperiksa dari teks: tidak ada protokol pencarian, tidak ada pencacahan objek, dan perbandingan memakai angka dari protokol yang berbeda antarmakalah.
