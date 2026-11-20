# Real-time Production Prediction of Kiwifruit in Orchard Based on Video Tracking Algorithm

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `guo2023real` |
| Judul asli | Real-time Production Prediction of Kiwifruit in Orchard Based on Video Tracking Algorithm |
| Penulis | Guo, M.; others |
| Tahun | 2023 |
| Venue | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | kiwifruit |

## Tautan Akses
- PDF: [guo2023real.pdf](../pdf/guo2023real.pdf)
- DOI resmi: https://doi.org/10.6041/j.issn.1000-1298.2023.06.018

## Gambaran Umum

Makalah ini mengusulkan estimasi produksi buah kiwi secara waktu nyata di kebun berdasarkan video dan pelacakan objek. Latar belakangnya adalah pola budidaya kiwi pada rak penopang yang membuat buah menggantung dan menyebar ke seluruh area kebun. Penghitungan manual dianggap memakan waktu dan akurasinya sulit dijaga. Penulis memosisikan metodenya sebagai alternatif pendekatan statistik dan deteksi pada citra tunggal, yang keduanya dianggap sukar menghasilkan estimasi total untuk area kebun yang luas.

Data dikumpulkan di kebun kiwi Universitas Pertanian Huazhong di Wuhan menggunakan kereta crawler yang bergerak 1 m/s mengikuti rute berbentuk S. Kamera tele 12 megapiksel ditempatkan pada ketinggian minimum 1,32 m, berjarak sedikitnya 1,5 m dari tanaman, dengan sudut elevasi 45°. Video yang diperoleh berdurasi 63 s dan berlaju 60,05 frame/s. Pengambilan satu frame dari setiap lima frame menghasilkan 534 citra beresolusi 3840×2160 pixel yang ditandai dengan Labelme. Untuk keperluan pelacakan, 600 frame berurutan ditandai manual memakai DarkLabel dalam tiga tingkat kondisi, yaitu sederhana, normal, dan sulit.

Metodenya terdiri atas dua tahap. Deteksi memakai YOLOv7 yang dilengkapi Soft-NMS guna mengurangi penghapusan kotak pada buah yang saling berdekatan dan berukuran kecil. Pelacakan memakai DeepSort: filter Kalman memprediksi posisi, jaringan VGG16 mengekstrak ciri tampilan buah, dan algoritma Hungaria mencocokkan objek antarframe. Setiap buah memperoleh nomor identitas unik, dan estimasi produksi dihitung dari jumlah nomor identitas tersebut.

Deteksi mencapai F1 90,09%. Pada 600 frame beranotasi, DeepSort mencapai MOTA 89,87% dan MOTP 82,34% dengan kecepatan 20,19 frame/s (Tabel 3, h. 183); angka 89,87% yang di abstrak disebut akurasi rata-rata pelacakan adalah MOTA. Hitungan dari nomor identitas terbesar dibandingkan dengan hitungan manual pada tujuh video pendek dalam tiga mode. Akurasi hitung tertinggi 97,49% pada mode sederhana, 94,83% pada mode normal, dan 88,63% pada mode sulit, dengan rerata di atas 91,59% (Tabel 4, h. 184). Pada mode sulit, buah rapat dan saling tumpang tindih.

Ditinjau dari penghitungan lintas pandang, mekanisme penetapan nomor identitas unik dan pencocokan ciri tampilan merupakan cara makalah ini mencegah satu buah dihitung dua kali pada frame berturut-turut. Penulis menyatakan bahwa kerja sebelumnya yang hanya memakai ciri gerak belum cukup akurat pada adegan kompleks, sehingga ciri tampilan ditambahkan ke dalam pencocokan.
