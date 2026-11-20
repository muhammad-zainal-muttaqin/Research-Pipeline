# LiDAR in precision agriculture for orchards and perennial tree crops: bibliometric analysis, sensor technologies, and algorithmic workflows

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2026lidar` |
| Judul asli | LiDAR in precision agriculture for orchards and perennial tree crops: bibliometric analysis, sensor technologies, and algorithmic workflows |
| Penulis | Liu, Wenhao; Ampatzidis, Yiannis; Wilkinson, Benjamin; Lee, Won Suk; Schueller, John K. |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [liu2026lidar.pdf](../pdf/liu2026lidar.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2026.112049

## Gambaran Umum

Tinjauan ini memetakan penggunaan LiDAR (*light detection and ranging*, pengukuran jarak dengan pulsa laser) di kebun buah dan tanaman tahunan. Penulis mengumpulkan publikasi dari Web of Science, Scopus, dan CAB, menghapus duplikat, lalu menyaring berdasarkan judul, abstrak, dan kata kunci. Hasil akhirnya 288 publikasi yang mencakup 24 jenis tanaman dari 33 spesies yang disurvei. Kajian ini tidak melakukan meta-analisis ukuran efek atau metrik akurasi, sehingga hasilnya berupa peta bidang, bukan perbandingan angka antarstudi.

Apel memegang porsi terbesar, 21,8%, diikuti kelapa sawit (*oil palm*) 13,0%, pir 8,1%, zaitun 7,4%, dan jeruk 7,4%. Kelima tanaman ini bersama-sama menyumbang lebih dari separuh publikasi. Penulis menyebut ketimpangan yang jelas, baik menurut wilayah maupun jenis sistem tanam. Rambutan, kuini, pepaya, durian, dan beberapa tanaman tropis lain tidak memiliki studi yang memenuhi syarat. Kelapa sawit hanya tercantum sebagai salah satu kategori tanaman; tinjauan ini tidak membahas penghitungan buah sawit secara khusus.

Dari sisi platform akuisisi, MLS (*mobile laser scanning*, pemindaian laser dari kendaraan atau tangan) mendominasi dengan 59,4%, disusul TLS (*terrestrial laser scanning*, pemindaian laser diam di darat) 20,3%, ALS (*airborne laser scanning*, pemindaian dari pesawat atau drone, termasuk pemetaan UAV) 16,9%, dan SLS (*spaceborne laser scanning*, pemindaian dari satelit) 3,4%. MLS yang dipasang pada traktor atau kendaraan robot menghasilkan lintasan yang dapat diulang dan tetap bekerja di bawah tajuk ketika sinyal GNSS (*global navigation satellite system*, sistem navigasi satelit) melemah. TLS dipakai untuk struktur beresolusi tinggi dan validasi. ALS dipakai untuk inventaris dari skala blok hingga kebun, yaitu jumlah pohon, tinggi, dan deteksi celah, serta untuk bagian tajuk yang tertutup bila dilihat dari tanah. Penulis menyimpulkan bahwa menggabungkan platform pada berbagai skala memberi keteramatan (*observability*) yang paling efektif. Menurut dimensinya, 67,4% studi memakai data 3D, 30,3% data 2D, dan 2,3% data 1D.

Bidang ini berkembang sejak 2015. Penelitian paling awal muncul pada akhir 1990-an, sporadis sebelum 2005, meningkat sekitar 2010, dan tumbuh substansial setelah 2015, seiring dengan LiDAR berbasis UAV dan sensor multi-berkas berbiaya rendah.

Kinerja LiDAR bergantung pada koordinasi sensor, platform, dan validasi, bukan pada satu sensor saja. Penulis menyebut hambatan berikut: oklusi tajuk (*canopy occlusion*), pelemahan berkas laser, data yang hilang secara tidak acak, pergeseran registrasi pada baris tanaman yang berulang, gerak akibat angin, inkonsistensi radiometrik, keterbatasan transfer model antarkebun, dan beban komputasi untuk penggunaan waktu nyata. Prioritas yang diusulkan meliputi metadata dan pelaporan kendali mutu yang terstandar, validasi yang sesuai dengan tugas, pemodelan yang memperhitungkan oklusi, normalisasi radiometrik, fusi multi-platform, pembelajaran yang dapat ditransfer, dan pemodelan yang memperhitungkan ketidakpastian.
