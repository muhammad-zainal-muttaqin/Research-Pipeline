# Orchard fruit segmentation using multi-spectral feature learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hung2013orchard` |
| Judul asli | Orchard fruit segmentation using multi-spectral feature learning |
| Penulis | Hung, Calvin; Nieto, Juan; Taylor, Zachary; Underwood, James; Sukkarieh, Salah |
| Tahun | 2013 |
| Venue | IEEE International Conference on Intelligent Robots and Systems |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | nut crops |

## Tautan Akses
- PDF: [hung2013orchard.pdf](../pdf/hung2013orchard.pdf)
- DOI resmi: https://doi.org/10.1109/iros.2013.6697125

## Gambaran Umum

Makalah ini bertujuan mengotomatiskan segmentasi buah di kebun untuk estimasi hasil panen oleh robot pengamat. Masalah yang disebut penulis: metode klasifikasi pertanian umumnya memakai fitur buatan tangan yang khusus untuk satu aplikasi, sehingga aturannya harus dirancang ulang untuk tanaman baru. Almond dipilih sebagai kasus karena warnanya mirip ranting, ukuran dan bentuknya mirip daun, dan ukuran buah dalam citra sangat bervariasi.

Data berasal dari kebun almond: 1600 citra RGB dan inframerah (IR) berukuran 320 kali 240 piksel, dengan 80 citra diberi label piksel untuk lima kelas (almond, batang, daun, tanah, langit). Citra RGB dan IR diambil dengan kamera yang sama memakai tapis IR, lalu disejajarkan dengan transformasi afin dan informasi timbal balik ternormalisasi (*normalized mutual information*). Fitur dipelajari tanpa label dari 477 citra RGB-NIR publik. Siapa pemberi label dan pembagian latih dan uji tidak disebut.

Metode memakai *sparse autoencoder*, jaringan yang belajar merepresentasikan potongan citra tanpa label, pada empat skala (1, 1/2, 1/4, 1/8). Klasifikator *softmax* dilatih dengan label piksel, lalu keluarannya menjadi potensial unari pada *conditional random field* (CRF), model grafis yang menghaluskan label antarpiksel bertetangga. Pembanding adalah 52 fitur deskriptor dari Hoiem dkk., yang diimplementasikan penulis sendiri.

Hasil dengan RGB: akurasi global naik dari 80,2% (tanpa CRF) ke 86,9% (dengan CRF), sedangkan pembanding mencapai 79,9%. Dengan RGB+IR dan CRF, akurasi global 88,0%, rerata akurasi 86,1%, dan ukuran F 86,1%, naik dari 79,9%, 82,3%, dan 79,4% tanpa CRF. Akurasi kelas almond RGB+IR dengan CRF 71,3%. Kekeliruan terbesar terjadi antara almond dan batang, dan berkurang dengan kanal IR.

Keterbatasan dari teks: algoritma menghasilkan label piksel dan tidak menghitung buah, sehingga tidak ada hitungan. Tidak ada pembagian latih dan uji yang dinyatakan atas 80 citra berlabel. Hanya satu kebun. Waktu proses 5 detik per citra. Penulis menyebut oklusi yang besar mungkin memerlukan sensor tambahan seperti stereo.
