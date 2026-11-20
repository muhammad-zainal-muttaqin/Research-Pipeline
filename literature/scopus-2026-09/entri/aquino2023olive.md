# Olive-fruit yield estimation by modelling perceptual visual features

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `aquino2023olive` |
| Judul asli | Olive-fruit yield estimation by modelling perceptual visual features |
| Penulis | Aquino, Arturo; Ponce, Juan Manuel; Noguera, Miguel; And\'ujar, Jos\'e Manuel |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | olive |

## Tautan Akses
- PDF: [aquino2023olive.pdf](../pdf/aquino2023olive.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.108361

## Gambaran Umum

Kajian ini (Aquino dkk., 2023, *Computers and Electronics in Agriculture* 214, 108361) mengestimasi hasil panen buah zaitun (*olive*) dari citra satu pandang pohon. Metode yang diajukan mengambil area pohon dengan operasi morfologi citra, lalu menghitung 16 deskriptor visual dari area itu. Deskriptor tersebut dimasukkan ke jaringan saraf tiruan tipe *multilayer perceptron* (MLP), yaitu model regresi yang memetakan masukan ke satu nilai keluaran. Keluaran model adalah perkiraan berat hasil dalam kilogram.

Pada validasi eksternal, hasil aktual yang diukur manual berjumlah 173,23 kg, sedangkan estimasi metode berjumlah 177,80 kg. Selisih itu setara dengan PPE (persentase kesalahan relatif) 2,64% berupa overestimasi. Penulis juga melaporkan R² 0,9795 dan RMSE 0,9914 kg per titik sampel. Validasi eksternal memakai jumlah sampel yang kecil, yaitu n = 10, sehingga angka R² dan RMSE sebaiknya dibaca bersama ukuran sampel itu.

Metode tidak mencoba mengidentifikasi buah yang sama dari beberapa sudut pandang, sehingga tidak ada langkah deduplikasi lintas pandang. Model juga bekerja pada tingkat pohon atau titik sampel, bukan pada tingkat buah tunggal yang dapat dilacak antarfoto.

Keterbatasan yang dinyatakan penulis sendiri adalah bahwa model yang dilatih belum diuji pada kebun atau musim yang berbeda. Sebagian konfigurasi sampel hanya memuat satu atau dua pohon, sehingga variasi antarpohon dalam satu kebun belum tentu terwakili dengan baik. Kajian ini tidak menguji perbandingan dengan metode lain pada data yang sama.

Namun bukti yang diberikan terbatas pada satu kebun, satu rangkaian data, dan validasi eksternal kecil. Klaim tentang akurasi di luar kondisi tersebut belum didukung oleh kajian ini.
