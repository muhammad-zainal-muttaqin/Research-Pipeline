# Detection of new oil palm fruit bunches based on deep learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `harmiansyah2024detection` |
| Judul asli | Detection of new oil palm fruit bunches based on deep learning |
| Penulis | Harmiansyah; Sembiring, E P; Oviana, E T; Supriyanto |
| Tahun | 2024 |
| Venue | Iop Conference Series Earth and Environmental Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [harmiansyah2024detection.pdf](../pdf/harmiansyah2024detection.pdf)
- DOI resmi: https://doi.org/10.1088/1755-1315/1379/1/012003

## Gambaran Umum

Makalah ini menguji YOLOv5 untuk mengenali tingkat kematangan tandan buah segar (TBS) kelapa sawit dari foto yang diambil dengan ponsel di Desa Wonosari, Lampung. Tingkat kematangan dibagi menjadi empat fraksi, yaitu 00, 1, 3, dan 4. Makalah menyebut 4.180 citra. Anotasi dibuat dengan Roboflow, dan pembagian data untuk latih, validasi, dan uji adalah 70:20:10. Makalah tidak menghitung jumlah tandan per citra atau per pohon. Yang dilaporkan adalah ketepatan klasifikasi per fraksi, presisi, recall, dan mAP per kelas.

Pada tahap uji, akurasi rata-rata 72,5%. Fraksi 00 mencapai 89%, fraksi 1 79%, fraksi 3 47%, dan fraksi 4 75%. Presisi 69,75%, recall 75,58%, mAP@0,5 0,7344, dan mAP@0,95 0,41182. Makalah menyatakan bahwa presisi dan recall "over 80%" pada bagian hasil, tetapi kesimpulan menulis rentang 63% sampai 100%. Kedua pernyataan itu tidak dapat didamaikan dari teks yang terbaca, sehingga angka presisi dan recall per fraksi perlu dicek ulang ke tabel 6 pada berkas asli. Tabel itu tidak terbaca utuh di teks ekstraksi.

Jumlah data uji juga tidak konsisten. Empat fraksi dengan 105 citra berjumlah 420, bukan 4.180. Jumlah data validasi juga berbeda: 862 pada subbagian 2.2.4 dan 836 pada bagian 3.2. Satuan nilai box loss tertinggi ditulis sebagai "0.0912%", padahal nilai loss tidak memiliki satuan persen. Matriks kebingungan (tabel 5) juga terpotong pada teks ekstraksi, sehingga pola salah klasifikasi antarfraksi belum dapat diverifikasi dari teks ini.

Makalah menyimpulkan bahwa YOLOv5 "demonstrates strong performance" dan "has proven effective for fruit maturity classification". Kesimpulan itu bertentangan dengan penilaian yang ditulis makalah sendiri: akurasi 72,5% masuk kategori "fair annotation", dan fraksi 3 hanya 47%. Kajian ini menguji satu detektor pra-latih pada satu lokasi dan satu jenis perangkat pengambilan gambar. Tidak ada perbandingan dengan detektor lain, tidak ada uji pada citra dari kebun lain, dan tidak ada analisis tandan yang tertutup pelepah atau berukuran kecil.

Makalah tidak mengukur akurasi penghitungan jumlah tandan, dan tidak mengatasi duplikasi antarpandang. Angka yang dikutip harus berasal dari tabel asli dengan koreksi jumlah data uji dan validasi yang disebut di atas.
