# Intelligent Mango Canopies Yield Estimation Using Machine Vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `neethi2023intelligent` |
| Judul asli | Intelligent Mango Canopies Yield Estimation Using Machine Vision |
| Penulis | Neethi, M. V.; Kiran, A. Geetha; Tiwari, Harshvardhan |
| Tahun | 2023 |
| Venue | SN Computer Science |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | mango |

## Tautan Akses
- PDF: [neethi2023intelligent.pdf](../pdf/neethi2023intelligent.pdf)
- DOI resmi: https://doi.org/10.1007/s42979-022-01602-2

## Gambaran Umum

Neethi dkk. (2023) mengusulkan sistem estimasi hasil panen mangga berbasis citra mesin. Masalah yang diangkat adalah kebutuhan data jumlah buah pada pohon yang dapat dikumpulkan secara cepat dan luas, untuk keperluan prakiraan produksi kebun. Sistem ini memisahkan area buah dari latar belakang daun dan cabang berdasarkan warna, lalu menghitung buah dengan deteksi lingkaran.

Data dikumpulkan dengan kamera utama ponsel pintar beresolusi 1920x1080 piksel, pada siang hari, selama satu musim tanam lima bulan. Foto diambil dari jarak 2 dan 3 m terhadap pohon setinggi 7 sampai 8 kaki, dalam dua sesi, yaitu pukul 09.30 sampai 10.00 dan pukul 14.30 sampai 15.00. Ada lima kultivar, dan repositori berisi 21.000 foto. Untuk eksperimen, penulis memakai 400 citra dari hari pengambilan terakhir, saat buah sudah matang, dengan pembagian 300 citra latih dan 100 citra uji. Akuisisi hanya memuat satu sisi pohon, tanpa pandangan dari atas atau bawah.

Metode berjalan bertahap. Citra diproses dengan *Gaussian filter* dan *histogram equalization*, lalu piksel latar dibuang dengan aturan ambang (R-G) > 50 atau (R-B) > 50. Area buah kemudian dikonversi ke ruang warna *HSV* dan dipisahkan dengan nilai saturasi S > 0,5. Untuk menghitung buah, penulis membandingkan tiga cara pencocokan lingkaran: *RANSAC*, deteksi berbasis geometri objek, dan *Hough transform*. Penulis menyatakan *Hough transform* memberi hasil paling akurat, sementara RANSAC melewatkan sebagian buah dan deteksi berbasis geometri memiliki tingkat salah klasifikasi tinggi. Pada 100 citra uji, penulis melaporkan 80% mangga terdeteksi, 21% terlewat, 25% muncul sebagai *false positive*, dan presisi 80%. Angka 80% terdeteksi dan 21% terlewat tidak berjumlah 100%, dan penulis tidak mendefinisikan penyebut kedua persentase itu.

Penulis sendiri menyebut beberapa batasan. Performa sistem turun menjadi sekitar 80% karena data diambil dalam kondisi pencahayaan yang berubah dan buah tertutup daun serta cabang. Sistem hanya mengenali buah yang sudah matang, sehingga belum dapat dipakai untuk prakiraan panen dini. Pengambilan gambar hanya dari satu arah pohon, sehingga buah di sisi lain tidak tercakup. Secara konseptual, aturan warna yang dipakai bergantung pada kondisi siang hari dan kultivar yang diuji, dan teks tidak memuat uji pada kondisi lain. Data tidak tersedia untuk publik dan hanya dapat diminta kepada penulis.
