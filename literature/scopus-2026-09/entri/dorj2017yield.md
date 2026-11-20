# An yield estimation in citrus orchards via fruit detection and counting using image processing

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `dorj2017yield` |
| Judul asli | An yield estimation in citrus orchards via fruit detection and counting using image processing |
| Penulis | Dorj, Ulzii-Orshikh; Lee, Malrey; Yun, Sang-seok |
| Tahun | 2017 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [dorj2017yield.pdf](../pdf/dorj2017yield.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2017.05.019

## Gambaran Umum

Dorj, Lee, dan Yun (2017) menghitung buah jeruk (*citrus*) dari foto tunggal per pohon. Penelitian ini dimuat di *Computers and Electronics in Agriculture* 140, halaman 103 sampai 112. Metode mengubah citra ke ruang warna HSV, memilih piksel berwarna oranye dengan ambang batas dari histogram, menghapus latar, lalu memisahkan buah yang berdekatan dengan *watershed*. Jumlah buah hasil algoritma dibandingkan dengan penghitungan manusia.

Penghitungan panen jeruk secara manual lambat dan bergantung pada penilai. Penulis mengusulkan penghitungan otomatis dari citra kebun. Setiap pohon difoto sekali, sehingga kajian ini tidak mengenali buah yang sama di dua foto berbeda.

Pipeline terdiri dari empat tahap. Pertama, citra RGB diubah ke HSV agar warna oranye lebih mudah dipisahkan dari dedaunan hijau. Kedua, histogram kanal hue dan saturasi dipakai untuk menentukan ambang batas. Ketiga, latar belakang dihapus dengan ambang tersebut. Keempat, buah yang saling menempel dipisahkan dengan transformasi jarak (*distance transform*) dan *marker-controlled watershed*, lalu setiap wilayah yang tersisa dihitung sebagai satu buah. Penulis tidak menyajikan model pembelajaran mesin; seluruh keputusan bergantung pada aturan ambang dan morfologi.

Abstrak dan bagian hasil menyebut 84 citra dari 21 pohon. Pengantar menyebut 124 citra dari 21 pohon. Penulis tidak menjelaskan selisih ini, sehingga jumlah citra yang benar tidak dapat dipastikan dari teks. Waktu pemrosesan dilaporkan sebagai rata-rata untuk 84 citra. Koefisien determinasi R² sebesar 0,93 dilaporkan, dengan galat persentase berkisar 0% sampai 29,02% dan rata-rata galat absolut 5,76%. Hasil ini menunjukkan bahwa aturan warna dan morfologi dapat mencapai R² tinggi pada data kecil. Tabel 1 membandingkan hasil ini dengan dua kajian terdahulu: Annamalai dan Suk (2003) dengan 0,76 dan Radnaabazar dan Lee (2006) dengan 0,83. Perbandingan ini hanya memuat nilai R² dan tidak menyamakan data, jumlah pohon, atau protokol penghitungan manusia.

Kajian ini tidak mengukur galat per pohon secara terpisah dari rata-rata, sehingga sebaran galat tidak dapat dibaca. Kesimpulan menyebut hasil "suitable and effective" tanpa uji sanggah pada kondisi kebun lain, pencahayaan lain, atau jenis jeruk lain. Estimasi hasil panen 10 sampai 25% dari jumlah bunga disebut "close in value" dengan panen, tetapi tidak disertai perhitungan statistik. Karena satu foto per pohon dipakai, buah yang tertutup daun atau berada di sisi pohon yang tidak terlihat tidak tercakup, dan kajian tidak membahas cara menggabungkan beberapa pandang. Dengan 21 pohon dan tanpa uji pada data terpisah, hasil ini belum cukup untuk menyimpulkan bahwa metode berlaku di luar kebun asalnya.
