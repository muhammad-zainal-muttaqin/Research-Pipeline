# Autonomous intelligent system for fruit yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hung2016autonomous` |
| Judul asli | Autonomous intelligent system for fruit yield estimation |
| Penulis | Hung, C.; Underwood, J.P.; Nieto, J.; Sukkarieh, S. |
| Tahun | 2016 |
| Venue | Acta Horticulturae |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [hung2016autonomous.pdf](../pdf/hung2016autonomous.pdf)
- DOI resmi: https://doi.org/10.17660/actahortic.2016.1130.82

## Gambaran Umum

Penulis menyoroti naiknya kebutuhan pangan, perubahan iklim, dan berkurangnya tenaga kerja pertanian. Tujuan makalah ini adalah merangkum kemajuan penghitungan buah di kebun dengan robot darat dan perangkat lunak pengolah citra dari Universitas Sydney, untuk estimasi hasil panen. Masalah yang disebut: algoritma deteksi buah yang ada dirancang khusus untuk satu kultivar dan harus dirancang ulang untuk buah lain.

Data dikumpulkan di kebun almond (Mildura), apel (Warburton), leci dan mangga (Mareeba), Australia. Robot "Shrimp" memotret dengan satu kamera depan Ladybug3 pada 5 Hz, resolusi 1232 kali 1616 piksel. Untuk segmentasi, setiap citra dibagi menjadi 32 sub-citra 308 kali 202 piksel. Lebih dari 1000 sub-citra diberi label piksel buah atau bukan buah secara manual, separuh untuk latih dan separuh untuk uji. Jumlah pohon dan baris apel tidak disebut. Acuan hasil adalah bobot dan hitungan per baris dari mesin penimbang setelah panen, dari manajer kebun.

Metode berjalan dalam tiga tahap. Tahap pertama adalah segmentasi piksel dengan jaringan saraf konvolusi multi-skala semi-terawasi (*convolutional neural network*), yang memberi label buah atau bukan buah pada tiap piksel. Tahap kedua adalah deteksi buah dengan transformasi Hough melingkar (*circular Hough transform*), yaitu pencarian gugusan piksel buah berbentuk lingkaran. Tahap ketiga menjumlahkan lingkaran pada citra yang diambil tiap 0,5 m di sepanjang baris. Jarak 0,5 m dipilih secara sembarang agar deteksi tidak tumpang tindih. Tidak ada penautan buah antarcitra.

Hasil segmentasi: F1 apel 95,7%, mangga 90,8%, leci 75,2%, almond 73,9% (presisi apel 92,6%, recall 99,0%). Penulis mengaitkan selisih ini dengan ukuran buah. Pada penghitungan apel, korelasi hitungan algoritma dengan hitungan acuan per baris R = 0,81. Estimasi sesuai pada 11 baris pertama dan menyimpang pada 4 baris terakhir; penulis menduga penyebabnya cahaya sore yang berkurang.

Keterbatasan yang dapat diperiksa: penghitungan hanya diuji pada apel, dengan total 15 baris (11 sesuai dan 4 menyimpang). Hitungan tidak cocok persis karena oklusi dan jarak citra 0,5 m. Kalibrasi regresi linear kuadrat terkecil belum diuji antarmusim. Penilaian segmentasi tidak memisahkan data per pohon atau per baris. Tidak ada galat hitung absolut yang dilaporkan, hanya korelasi.
