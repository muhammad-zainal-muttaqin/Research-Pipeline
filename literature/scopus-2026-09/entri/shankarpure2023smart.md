# Smart Fruit Identification and Counting using Machine Vision Approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `shankarpure2023smart` |
| Judul asli | Smart Fruit Identification and Counting using Machine Vision Approach |
| Penulis | Shankarpure, Madhura R.; Patil, Dipti D. |
| Tahun | 2023 |
| Venue | International Journal of Advanced Computer Science and Applications |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [shankarpure2023smart.pdf](../pdf/shankarpure2023smart.pdf)
- DOI resmi: https://doi.org/10.14569/ijacsa.2023.0141229

## Gambaran Umum

Penelitian ini bertujuan mengestimasi hasil buah jeruk untuk membantu petani merencanakan sumber daya dan menentukan waktu panen. Pendekatan pemrosesan citra diharapkan mengurangi kerja manual dan meningkatkan ketepatan hitungan buah matang. Penulis mengadaptasi metode deteksi buah mangga milik Payne dkk. untuk diterapkan pada jeruk. Ciri jeruk yang dipakai adalah warna jingga terang, tekstur kulit kasar, dan bentuk yang sebagian besar bulat.

Tanaman yang diteliti adalah jeruk (citrus). Data berupa sepuluh citra jeruk yang diunduh bebas dari sumber daring [25], dengan variasi tingkat kecerahan dan kerapatan daun. Metodenya terdiri atas dua tahap. Tahap pertama mengisolasi jeruk melalui pembuatan topeng (mask) warna dengan empat langkah: (1) indeks selisih ternormalisasi antara kanal merah dan hijau, (g − r)/(g + r), dengan ambang lebih dari 0; (2) filter ambang rata-rata adaptif 3×3 menggantikan filter varians untuk membuang daun dan langit; (3) kanal Cr ruang warna YCbCr dengan ambang nilai piksel minimal 140; dan (4) kanal Cb dengan rentang 30–120. Keempat topeng digabung menjadi satu topeng akhir berdasarkan Persamaan 1.

Tahap kedua menghitung buah dengan mendeteksi lingkaran pada topeng. Topeng dihaluskan dengan Gaussian blur, lalu tepi dicari dengan deteksi Canny dan lingkaran dengan transformasi Hough menggunakan parameter dp, minDist, ambang, serta jari-jari minimum dan maksimum yang ditentukan melalui percobaan. Penyaringan memakai rata-rata bergulir jari-jari lingkaran, persentase piksel jeruk di dalam lingkaran, batas bingkai citra, dan pemeriksaan tumpang tindih dengan lingkaran lain. Lingkaran diberi penanda warna sesuai tingkat keyakinan: hijau untuk keyakinan tinggi, jingga untuk sedang, ungu atau merah untuk rendah, dan maroon untuk ukuran yang mendekati tetapi isiannya kurang.

Hasil utama adalah tingkat keberhasilan sekitar 72,4 persen dalam mengidentifikasi jeruk dengan keyakinan tinggi, dengan simpangan baku ±12,20, dihitung atas sepuluh citra uji. Garis tren membandingkan hitungan algoritme dengan hitungan aktual menunjukkan R² sebesar 0,9923 untuk hitungan aktual (y = 0,9568x − 4,9045) dan 0,9952 untuk hitungan terdeteksi (y = 0,7841x − 5,8227). Acuan hitung berupa perbandingan jumlah jeruk terdeteksi terhadap jumlah aktual; metrik standar seperti mAP tidak dipakai. Skema pembagian data latih dan uji tidak dinyatakan.

Batasan yang dinyatakan penulis: algoritme bekerja lebih baik pada citra beresolusi lebih dari 1300×1300 piksel, gagal ketika diameter jeruk melebihi setengah ukuran layar atau ketika jeruk berukuran kurang dari 150 piksel (terkait nilai pemisahan minimum antarlingkaran), dan menjadi mahal secara komputasi pada citra besar dan padat. Algoritme juga tidak dapat menangani perbedaan tingkat kematangan dan perlu peningkatan pada segmentasi warna agar tahan terhadap variasi kecerahan.
