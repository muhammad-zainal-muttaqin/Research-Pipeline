# Thermal vision of oil palm fruits under difference ripeness quality

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fauziah2021thermal` |
| Judul asli | Thermal vision of oil palm fruits under difference ripeness quality |
| Penulis | Fauziah, WK; Makky, M; Santosa; Cherie, D |
| Tahun | 2021 |
| Venue | Iop Conference Series Earth and Environmental Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [fauziah2021thermal.pdf](../pdf/fauziah2021thermal.pdf)
- DOI resmi: https://doi.org/10.1088/1755-1315/644/1/012044

## Gambaran Umum

Kajian ini menguji apakah citra termal tandan buah segar (TBS) kelapa sawit dapat dipakai untuk menaksir *oil content* (kandungan minyak) dan tingkat kematangan tanpa merusak buah. Masalah yang diangkat adalah penentuan waktu panen yang tepat, karena kandungan minyak berubah selama proses pematangan dan pengukuran kimia konvensional bersifat merusak. Penulis menggabungkan nilai suhu hasil konversi citra termal dengan tiga kanal warna (R, G, B) sebagai masukan jaringan saraf tiruan *multilayer perceptron* (MLP) dengan empat neuron pada lapisan tersembunyi.

Data yang dilaporkan dalam teks yang dibaca berupa tingkat kematangan dalam hari setelah antesis (DAA) dan kandungan minyak hasil ekstraksi. Penulis menyatakan kandungan minyak tertinggi pada kematangan 171–190 DAA dengan suhu optimum 28,90 °C, sedangkan kematangan 110–130 DAA memiliki kandungan minyak dan suhu terendah. Nilai *coefficient of determination* (R2) antara kematangan dan kandungan minyak tercantum sebagai 0,9058 pada gambar 4b, tetapi 0,9085 pada teks; selisih ini belum diselesaikan penulis. Nilai R2 antara suhu dan kandungan minyak adalah 0,8039.

Hasil model MLP pada tahap kalibrasi memberi R2 0,7818 dengan SEC 0,0831. Pada tahap validasi, R2 naik menjadi 0,9535 dengan SEP 0,0003 dan bias 0,0001. Penulis menyimpulkan model layak karena R2 tinggi dan galat rendah. Dari sisi evaluasi, nilai SEP 0,0003 jauh lebih kecil daripada SEC 0,0831 pada satuan yang sama, sehingga perlu diperiksa apakah data validasi cukup besar dan tidak tumpang tindih dengan data kalibrasi. Kajian ini tidak melaporkan ketidakpastian atau uji pada kebun atau musim lain.

Keterbatasan yang dinyatakan penulis dalam teks yang dibaca bersifat umum: penulis menulis bahwa taksiran mutu TBS "cannot be made solely based on this information" dan perlu pemodelan tambahan. Bagian khusus keterbatasan tidak ditemukan pada teks yang dibaca. Kajian ini hanya relevan sebagai bukti bahwa citra termal dapat dipakai untuk atribut kelas (kematangan) pada tandan yang sudah tersegmentasi.
