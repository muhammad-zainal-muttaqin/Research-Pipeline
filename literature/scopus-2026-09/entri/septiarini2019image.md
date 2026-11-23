# Image-based processing for ripeness classification of oil palm fruit

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `septiarini2019image` |
| Judul asli | Image-based processing for ripeness classification of oil palm fruit |
| Penulis | Septiarini, Anindita; Hamdani, Hamdani; Hatta, Heliza Rahmania; Kasim, Anita Ahmad |
| Tahun | 2019 |
| Venue | Proceeding 2019 5th International Conference on Science in Information Technology Embracing Industry 4 0 Towards Innovation in Cyber Physical System Icsitech 2019 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [septiarini2019image.pdf](../pdf/septiarini2019image.pdf)
- DOI resmi: https://doi.org/10.1109/icsitech46713.2019.8987575

## Gambaran Umum

Kajian ini mengklasifikasikan tingkat kematangan buah kelapa sawit dari citra digital. Penulis menyebut bahwa permintaan minyak sawit terus naik dan bahwa penilaian kematangan secara visual bersifat subjektif. Tiga kelas dibedakan: *raw* (mentah), *under-ripe* (kurang matang), dan *ripe* (matang). Pemrosesan citra otomatis dipakai agar penilaian tidak bergantung pada pengamat.

Data berupa 160 citra buah sawit: 60 mentah, 50 kurang matang, dan 50 matang. Citra diambil dengan kamera ponsel Samsung Edge 7 pada jarak 40 sampai 90 cm, berukuran 3264 × 2448 piksel. Teks menyebut pemotretan dilakukan di ruangan dengan pencahayaan cukup dan latar belakang beragam. Teks tidak menyebut asal kebun, lokasi panen, atau siapa yang memberi label. Tidak ada pembagian latih dan uji yang terpisah.

Metode terdiri atas empat tahap: pemilihan area buah (ROI) secara manual, segmentasi, ekstraksi fitur, dan klasifikasi. Segmentasi memakai filter median, ambang *Otsu* (cara memilih ambang otomatis dari histogram keabuan), lalu operasi morfologi buka dan tutup. Fitur berupa rerata dan simpangan baku dari kanal merah, hijau, biru, dan keabuan, sehingga totalnya delapan fitur. Klasifikasi memakai *support vector machine* (SVM), yaitu pemisah kelas dengan margin terbesar.

Hasil utama: akurasi tertinggi 92,5% pada validasi silang K=20. Akurasi pada K=2, K=4, dan K=10 berturut-turut 88,16%, 90,63%, dan 91,25%. Pada K=20, akurasi per kelas adalah 93,33% (mentah), 86% (kurang matang), dan 98% (matang). Kelas kurang matang paling rendah, dan penulis mengaitkannya dengan galat segmentasi.

Keterbatasan yang dapat diperiksa: evaluasi memakai validasi silang K-fold, bukan uji terpisah. Teks tidak menyebut pembagian per objek atau per tanaman. Pencahayaan dan latar belakang tidak diukur. Teks menyebut akurasi 95% dan 98% untuk kelas mentah dan matang, sedangkan Tabel II memuat 93,33% untuk mentah pada K=20.
