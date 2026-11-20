# Fruit maturity and location identification of beef tomato using R-CNN and binocular imaging technology

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hsieh2021fruit` |
| Judul asli | Fruit maturity and location identification of beef tomato using R-CNN and binocular imaging technology |
| Penulis | Hsieh, Kuang-Wen; Huang, Bo-Yu; Hsiao, Kai-Ze; Tuan, Yu-Hao; Shih, Fu-Pang; Hsieh, Li-Cheng; Chen, Suming; Yang, I-Chang |
| Tahun | 2021 |
| Venue | Journal of Food Measurement and Characterization |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [hsieh2021fruit.pdf](../pdf/hsieh2021fruit.pdf)
- DOI resmi: https://doi.org/10.1007/s11694-021-01074-7

## Gambaran Umum

Kajian Hsieh dkk. (2021) membahas panen tomat jenis *beef* di rumah kaca. Dua pertanyaannya adalah apakah tomat sudah matang dan di mana posisinya dalam ruang 3D, agar lengan robot dapat memotong tangkainya. Penulis memakai *Mask R-CNN*, yaitu jaringan deteksi objek yang juga menghasilkan *mask* (bentuk piksel tiap objek), dan kamera stereo ZED mini untuk mengukur kedalaman. Kajian ini menilai satu citra per saat dan tidak menghitung buah lintas pandang.

Data yang dipakai berasal dari rumah kaca. Citra yang diambil berjumlah 363 untuk analisis warna. Objek latih dibagi menjadi tiga kelas: tomat utuh, tomat tertutup, dan tangkai. Jumlah sampel warna untuk tiga tingkat kematangan adalah 23 tomat hijau, 260 setengah matang, dan 1.113 matang (Tabel 2). Kecerahan permukaan tomat di lapangan berkisar 4.000 sampai 20.000 lux. Kamera dipasang pada kendaraan swagerak dengan rentang kedalaman 0,15 sampai 12 m.

Pada validasi, ambang *IoU* (*intersection over union*, ukuran tumpang tindih kotak prediksi dengan kotak acuan) ditetapkan 0,9. Hasil pelatihan melaporkan *precision* dan *recall* masing-masing 98,6%. Galat posisi rata-rata pada sumbu XY adalah 0,48 cm dan pada sumbu Z adalah 0,67 cm, dengan galat maksimum Z 1,86 cm. Untuk estimasi ukuran, penulis membuat regresi kurvilinear terhadap kedalaman. Koefisien determinasi (R²) untuk lebar adalah 0,9041 dan untuk tinggi 0,9344. Pengenalan tomat disebut mencapai akurasi 93%. Naskah juga menyebut *precision* dan *recall* 98% di satu bagian dan 100% di bagian kesimpulan, sehingga angka itu tidak konsisten dengan 98,6% pada hasil.

Penulis menyatakan bahwa galat kamera dipengaruhi oleh cahaya yang tidak stabil saat pengambilan citra, dan cahaya itu dapat memperbesar galat pada titik fitur. Kelas kematangan hanya mencakup tomat yang dinilai pakar layak panen. Estimasi ukuran hanya diuji pada tomat matang dan dibangun dari satu jenis kamera.
