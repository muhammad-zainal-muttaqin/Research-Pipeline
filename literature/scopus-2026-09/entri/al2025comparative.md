# Comparative study of citrus fruits (Citrus reticulata Blanco cv. Batu 55) detection and counting with single and double labels based on convolutional neural network using YOLOv7

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `al2025comparative` |
| Judul asli | Comparative study of citrus fruits (Citrus reticulata Blanco cv. Batu 55) detection and counting with single and double labels based on convolutional neural network using YOLOv7 |
| Penulis | Al Riza, Dimas Firmanda; Musahada, Lucky Candra; Aufa, Romzi Izzudin; Hermanto, Mochamad Bagus; Nugroho, Hermawan; Hendrawan, Yusuf |
| Tahun | 2025 |
| Venue | Smart Agricultural Technology |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [al2025comparative.pdf](../pdf/al2025comparative.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2024.100763

## Gambaran Umum

Kajian Al Riza dkk. (2025) membandingkan tiga varian detektor objek YOLOv7 (YOLOv7, YOLOv7-Tiny, dan YOLOv7-X) untuk mendeteksi dan menghitung buah jeruk pada citra pohon. Data berasal dari 75 pohon jeruk. Citra dibagi menjadi 295 citra, dengan 264 citra latih dan 31 citra validasi. Setiap buah diberi label dengan dua skema: label tunggal yang hanya memuat kelas oranye, dan label ganda yang memuat dua kelas, yaitu hijau dan oranye.

Model terbaik adalah YOLOv7 dengan batch 4 pada skema label ganda. Nilainya: mAP50 0,906, precision 0,850, recall 0,825, dan F1 0,837. Nilai mAP50 per kelas adalah 0,890 untuk hijau dan 0,922 untuk oranye. Untuk penghitungan, kajian mengukur kesesuaian jumlah deteksi dengan jumlah buah hasil hitung manual pada tiap citra, dengan nilai R² 0,9661. Kajian menulis: "The best model for calculating tangerine objects has very good performance with an R square value of 0.9661." Buah yang jatuh ke tanah dihitung sebagai kelas oranye. YOLOv7-Tiny adalah varian terkecil dengan ukuran berkas 12,4 MB.

Teks yang diperiksa tidak memuat mekanisme untuk menentukan apakah buah yang sama muncul pada lebih dari satu citra atau lebih dari satu sisi pohon. Penghitungan dengan demikian menjumlahkan deteksi per citra.

Keterbatasan yang dapat diperiksa dari teks: jumlah pohon (75) dan citra (295) relatif kecil, dan kajian hanya menguji satu jenis buah. Nilai R² 0,9661 berasal dari satu pembagian data, sehingga kestabilan hasil pada pohon di luar data ini belum dapat dinilai dari teks. Keputusan kode ini didasarkan pada bagian teks yang diperiksa (baris 1 sampai 618), termasuk abstrak, metode, hasil, dan kesimpulan.
