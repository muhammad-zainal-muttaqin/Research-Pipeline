# Development of an automatic grading machine for oil palm fresh fruits bunches (FFBs) based on machine vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `makky2013development` |
| Judul asli | Development of an automatic grading machine for oil palm fresh fruits bunches (FFBs) based on machine vision |
| Penulis | Makky, Muhammad; Soni, Peeyush |
| Tahun | 2013 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [makky2013development.pdf](../pdf/makky2013development.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2013.02.008

## Gambaran Umum

Makky dan Soni (2013) membangun mesin penilai (grading) tandan buah segar (TBS) kelapa sawit yang bekerja di lapangan dengan kamera dan pengolahan citra. Mesin mengambil citra setiap tandan, memisahkan latar belakang, mengekstraksi fitur warna, lalu menentukan dua hal: apakah tandan ditolak (kelas 1) atau diterima untuk diolah (kelas 2), serta fraksi kematangan dan estimasi beratnya. Studi ini menilai satu tandan per citra. Pencacahan buah per tandan tidak dilakukan.

Sistem diuji pada 465 tandan varietas tenera yang diambil secara acak dari pohon berumur 7 sampai 20 tahun di kebun Cimulang, Bogor, selama November sampai Desember 2011. Citra diambil dengan webcam 16 MP pada resolusi 640×480 piksel RGB 24 bit, di bawah pencahayaan LED 6500 K. Pemisahan latar belakang dengan algoritma ambang adaptif (*adaptive threshold*) mencapai tingkat keberhasilan 100%. Pada citra yang sudah bebas latar, histogram intensitas dibagi menjadi tiga kelompok. Kelompok 0 sampai 100 mewakili celah antarbuah, latar, buah mentah, dan kotoran. Kelompok 100 sampai 200 mewakili buah matang. Kelompok 200 sampai 255 mewakili spikelet, kelopak, dan tangkai buah. Hanya kelompok kedua yang dipakai untuk ekstraksi fitur lebih lanjut.

Klasifikasi kelas memakai analisis diskriminan bertahap dengan fungsi diskriminan kanonik dan jarak Mahalanobis, dikalibrasi dengan 240 sampel. Sebelas variabel dipakai: piksel objek, rerata R, G, B, r, g, b, H, S, I, dan indeks kematangan (*ripeness index*, RI). Label kelas diberikan oleh sekelompok penilai terlatih. Pada data kalibrasi, model mengklasifikasikan 93,33% tandan kelas 1 dan 94,44% tandan kelas 2 dengan kesalahan baku kalibrasi (SEC) 0,4835. Pada validasi silang, akurasinya 93,46% untuk kelas 1 dan 93,59% untuk kelas 2. Akurasi keseluruhan 93,53% dengan kesalahan baku prediksi (SEP) 0,5165. Luas di bawah kurva ROC adalah 0,935. Klasifikasi fraksi menghasilkan rerata keberhasilan 88,7%. Estimasi berat memakai delapan model, satu untuk setiap fraksi dari 00 sampai 6. Setiap model meregresikan berat yang ditimbang terhadap luas objek tersegmentasi dengan polinomial, dengan rerata R² 81,39%. Waktu pemeriksaan satu tandan per 5 detik, dan mesin melakukan penilaian lebih dari 12 ton TBS per jam (abstrak).

Batas studi perlu dicatat. Estimasi berat hanya memakai luas proyeksi dua dimensi dan tidak mengukur dimensi geometris tandan. Penulis menyebut alasannya: TBS akan diproses menjadi CPO, dan berat lebih relevan dengan kandungan CPO. Uji lapangan dilakukan pada siang hari, dan hasilnya dinilai dari satu lokasi kebun dengan satu varietas. Tidak ada pelaporan selang kepercayaan untuk akurasi klasifikasi. Kurva ROC disebut memiliki selang kepercayaan 99,99% tanpa angka batas bawah dan atas.
