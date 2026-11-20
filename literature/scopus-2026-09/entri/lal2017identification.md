# Identification and counting of mature apple fruit based on BP feed forward neural network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lal2017identification` |
| Judul asli | Identification and counting of mature apple fruit based on BP feed forward neural network |
| Penulis | Lal, Shreya; Behera, Santi Kumari; Sethy, Prabira Kumar; Rath, Amiya Kumar |
| Tahun | 2017 |
| Venue | Proceedings of 2017 3rd IEEE International Conference on Sensing Signal Processing and Security Icsss 2017 |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [lal2017identification.pdf](../pdf/lal2017identification.pdf)
- DOI resmi: https://doi.org/10.1109/ssps.2017.8071621

## Gambaran Umum

Makalah ini mengusulkan cara mengenali apel yang sudah matang dan menghitungnya dari sebuah citra. Pemeriksaan kebun secara manual memakan banyak tenaga. Menurut pengantar makalah, pemeriksaan itu memakan waktu dan mahal, dan belum ada sensor komersial yang bekerja secara *real time* untuk menilai kesehatan buah. Tujuan makalah adalah menggabungkan klasifikasi kematangan dan penghitungan buah dalam satu alur berbasis citra warna. Pengantar juga menyebut bahwa apel sekitar 2,8% dari produksi buah nasional dan berada di peringkat keenam produksi.

Alur kerjanya dimulai dari citra apel yang diubah ukurannya. Komponen warna RGB (merah, hijau, biru) diambil dari citra, lalu *artificial neural network* (jaringan saraf tiruan) dengan arsitektur *backpropagation feed forward* mengklasifikasikan setiap apel sebagai matang atau belum matang. Jumlah apel matang kemudian dihitung. Penulis melaporkan akurasi klasifikasi 98,1% ketika ketiga atribut RGB dipakai sebagai masukan. Angka ini hanya tercantum di abstrak.

Makalah ini menempatkan karyanya di antara pendekatan berbasis warna. Zhou dkk. menghitung apel dengan ambang warna RGB dan melaporkan koefisien korelasi 0,58 hingga 0,71. Wang dkk. memakai ambang di ruang warna HSV dan melaporkan error estimasi hasil 3,2% untuk apel merah dan 1,2% untuk apel hijau. Polder dkk. membandingkan citra hiperspektral dengan RGB untuk tingkat kematangan tomat, dan menyimpulkan bahwa citra hiperspektral lebih baik daripada RGB. Savarkar dkk. melaporkan akurasi 94% untuk chikoo dan 92% untuk mangga dengan BPNN, sedangkan Jamil dkk. melaporkan 73,3% untuk penilaian tandan kelapa sawit dengan logika fuzzy. Xiao dkk. memakai BPNN bersama transformasi Hough untuk mendeteksi dan menghitung apel, dengan koefisien determinasi R² 0,985 terhadap penghitungan manual. Zhang dkk. (FSCABC-FNN) melaporkan akurasi 89,1% pada 1.653 citra warna dalam 18 kategori, lebih tinggi daripada pengklasifikasi lain yang dibandingkan dalam studi itu. Perbandingan lintas studi ini tidak setara karena data, komoditas, dan metrik berbeda.

Hasil 98,1% belum dapat dibandingkan dengan angka lain sebelum jumlah citra dan pembagian datanya diperiksa. Penghitungan dilaporkan sebagai kesesuaian dengan jumlah manual, bukan sebagai galat penghitungan per pohon. Makalah ini tidak membahas apel yang tertutup daun atau tumpang tindih antarbuah, sehingga kondisi itu tidak dapat dinilai dari teks yang dibaca.
