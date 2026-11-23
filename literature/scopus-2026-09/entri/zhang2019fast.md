# Fast Detection and Yield Estimation of Ripe Citrus Fruit Based on Machine Vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2019fast` |
| Judul asli | Fast Detection and Yield Estimation of Ripe Citrus Fruit Based on Machine Vision |
| Penulis | Zhang, X.; others |
| Tahun | 2019 |
| Venue | Guangdong Agricultural Sciences |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [zhang2019fast.pdf](../pdf/zhang2019fast.pdf)
- DOI resmi: https://doi.org/10.16768/j.issn.1004-874x.2019.07.022

## Gambaran Umum

Kajian ini mencacah jeruk matang di pohon dari citra RGB untuk menaksir hasil kebun. Penulis menyebut taksiran hasil jeruk masih memakai sampel dan hitungan mata di lapangan, yang mahal, lambat, dan kurang tepat. Mereka mengusulkan cara tanpa ambang dan penghilangan derau: citra diubah ke ruang warna Lab, lalu jeruk dicari pada komponen "a" dengan transformasi Hough untuk lingkaran.

Citra diambil pada Desember 2018 di kebun Shiraz Ranch, California, Amerika Serikat. Kameranya iPhone XR di atas tripod, 2,13 m dari pohon dan 1,45 m dari tanah, dengan fokus otomatis tanpa zoom atau lampu kilat (4.032 × 3.024 piksel). Dua sisi 25 pohon jeruk keprok dan jeruk manis difoto pada hari cerah dan berawan.

Komponen biru citra RGB dibuat nol, lalu citra diubah ke ruang warna Lab, yaitu ruang warna yang memisahkan kecerahan (L) dari sumbu merah-hijau (a) dan kuning-biru (b). Pada komponen "a", jeruk tampak putih dan daun, ranting, tanah, serta langit tampak hitam. Transformasi Hough untuk lingkaran, yaitu cara mencari bentuk lingkaran dengan mengumpulkan suara titik tepi untuk setiap pusat dan jari-jari, kemudian menandai dan mencacah jeruk di MATLAB.

Pada satu citra pohon jeruk manis, cara ini menemukan 113 jeruk, sedangkan hitung tangan 117 jeruk. Tujuh jeruk terlewat dan 3 deteksi palsu berasal dari tanah dan batang. Dari citra ini dihitung akurasi pengenalan 94,01% dan akurasi taksiran hasil 96,58%, dengan waktu 1,03 detik. Pembanding dari kajian lain adalah 90,8% dalam 0,33 detik (ruang warna Cr-Cb) dan 93,0% dalam 26,05 detik (ambang dan morfologi). Angka pembanding itu disalin dari makalah asalnya, bukan diuji pada data yang sama. Untuk 10 pohon yang difoto dari dua sisi (20 citra), hitungan citra diregresikan terhadap hitung tangan. Hasilnya y = 1,0427x + 2,9117.

Keterbatasan yang dapat diperiksa dari teks adalah sebagai berikut. Akurasi 94,01% dan 96,58% hanya dari satu citra. R² ditulis 0,9879 di teks, 0,982 di grafik, dan 0,83 di abstrak bahasa Inggris. Grafik regresi memuat lebih dari 100 titik, padahal teks menyebut 20 citra, dan hal ini tidak dijelaskan. Teks tidak menyebut apakah hitung tangan dilakukan di pohon atau pada citra. Hitungan dua sisi pohon tidak digabung, sehingga buah yang terlihat dari kedua sisi tidak ditangani. Penulis menyatakan buah yang tersembunyi di dalam tajuk tidak terlihat dan cara ini hanya cocok untuk jeruk matang.
