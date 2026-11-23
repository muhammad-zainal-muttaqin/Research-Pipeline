# Yield estimation in mango orchards using machine vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `neethi2021yield` |
| Judul asli | Yield estimation in mango orchards using machine vision |
| Penulis | Neethi, M. V.; Kiran, A. Geetha; Tiwari, Harshvardhan |
| Tahun | 2021 |
| Venue | Aip Conference Proceedings |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | mango |

## Tautan Akses
- PDF: [neethi2021yield.pdf](../pdf/neethi2021yield.pdf)
- DOI resmi: https://doi.org/10.1063/5.0046526

## Gambaran Umum

Penulis ingin membangun sistem estimasi hasil panen mangga yang otomatis dengan visi mesin. Mereka menyebut tenaga kerja pertanian berkurang dan tidak ada set data acuan untuk mangga. Makalah ini terbatas pada langkah pertama, yaitu memisahkan wilayah buah dari latar belakang pada citra pohon dengan ambang warna.

Data berupa citra pohon mangga dari kebun seluas 200 acre di Yelachahalli, Mysore, Karnataka, India. Citra diambil dengan kamera ponsel (OnePlus A5000) beresolusi 1920x1080 piksel pada cahaya siang. Pengambilan berlangsung lima bulan (Desember 2018 sampai Mei 2019) dengan selang 7 hari pada tiga bulan pertama. Jaraknya 2 dan 3 meter, pagi dan sore, dari arah timur laut dan barat daya. Totalnya 21.000 citra dari 5 pohon dan 4 kultivar. Dari 400 citra tahap pematangan, 350 dipakai setelah citra dengan pencahayaan terlalu tinggi dibuang. Pemberi label dan pembagian latih/uji tidak disebut.

Metodenya tanpa pelatihan. Derau dikurangi dengan *filter* Gaussian. Latar belakang dibuang dengan ambang selisih kanal merah dan biru (R-B) sebesar 50. Citra diubah ke ruang warna HSV (*hue*, *saturation*, *value*), lalu piksel dengan saturasi di atas 0,5 dianggap buah. Sisa daun dan ranting dikurangi dengan *filter* median 3x3 serta operasi morfologi *opening* dan *closing*.

Hasil dilaporkan pada Tabel 1: dari 30 buah manual, algoritma menyegmentasi 28 buah (93,33%), dengan 3 positif palsu (10%) dan 2 buah terlewat (6,66%). Teks menyebut galat 6,66% dan membandingkannya dengan metode lain yang memakai data berbeda (anggur 10,1%, mangga 7,7%, jeruk 11,2%). Angka itu dihitung pada satu kelompok tabel, bukan per pohon.

Keterbatasan yang dapat diperiksa: tidak ada pembagian latih/uji karena metode berbasis ambang, dan penulis tidak menyebut pemilihan ambang terpisah dari citra uji. Tabel 1 hanya memuat 30 buah, sedangkan teks menyebut 350 citra. Buah hijau tidak terdeteksi, dan positif palsu naik pada pencahayaan tidak seragam. Hanya satu arah pandang pohon yang dievaluasi. Hasil berupa segmentasi, bukan hitungan buah per pohon, dan tidak ada penggabungan antarcitra.
