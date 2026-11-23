# Oil palm fruit maturity classification based on texture feature extraction of fruit thorns and supervised machine learning classifiers using image processing technique

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `alfatni2014oil` |
| Judul asli | Oil palm fruit maturity classification based on texture feature extraction of fruit thorns and supervised machine learning classifiers using image processing technique |
| Penulis | Alfatni, M.S.M.; Shariff, A.R.M.; Marhaban, M.H.; Shafie, S.B.; Ben Saaed, O.M.; Abdullah, M.Z.; bin Amiruddin, M.D. |
| Tahun | 2014 |
| Venue | Acta Horticulturae |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [alfatni2014oil.pdf](../pdf/alfatni2014oil.pdf)
- DOI resmi: https://doi.org/10.17660/actahortic.2014.1054.42

## Gambaran Umum

Penulis menyebut perlunya sistem klasifikasi kematangan tandan buah segar (TBS) kelapa sawit yang cepat, mudah, dan akurat. Penilaian manual bersifat subjektif dan memicu sengketa antara petani dan pabrik. Kajian ini menguji klasifikasi tiga kelas kematangan (mentah, matang, terlalu matang) dari tekstur duri (*thorns*) buah.

Data berupa citra TBS yang diambil dengan pencahayaan terkendali memakai perangkat rumah tandan dari sistem penilaian sawit. Teks menyebut 180 citra untuk pelatihan (60 per kelas), 90 untuk validasi, dan 270 untuk pengujian sistem. Jumlah pohon, lokasi pengambilan, jenis kamera, dan pemberi label kelas tidak disebut.

Citra disegmentasi berdasarkan warna untuk memisahkan buah dari latar. Fitur tekstur diekstraksi dengan tiga cara: *Gray Level Co-occurrence Matrix* (GLCM, statistik pasangan piksel bertetangga), *Basic Gray Level Aura Matrix* (BGLAM, statistik aura tingkat keabuan di sekitar piksel), dan transformasi *wavelet* Gabor. Fitur diklasifikasikan dengan *artificial neural network* (ANN, jaringan saraf berlapis maju) dan *K-nearest neighbour* (KNN, klasifikasi menurut tetangga terdekat). Tiga ukuran *region of interest* (ROI) dibandingkan: 300x300, 50x50, dan 100x100 piksel.

Akurasi diukur dengan luas di bawah kurva ROC (AUC). GLCM dengan ANN pada ROI 1 mencapai 91,3%. BGLAM dengan ANN pada ROI 3 mencapai 91,1%. Gabor dengan KNN pada ROI 1 mencapai 88,7%. Semua kasus berada di atas 88%.

Keterbatasan yang dapat diperiksa dari teks: ukuran data kecil, tidak ada keterangan pembagian per pohon, dan tidak ada data uji dari lokasi lain. Abstrak menyebut hasil BGLAM 91,3% sedangkan hasil di badan teks 91,1%. Kajian ini tidak mencacah buah dan tidak menggabungkan beberapa citra tandan yang sama.
