# Deep learning for oil palm fruit ripeness classification with densenet

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `herman2021deep` |
| Judul asli | Deep learning for oil palm fruit ripeness classification with densenet |
| Penulis | Herman, Herman; Cenggoro, Tjeng Wawan; Susanto, Albert; Pardamean, Bens |
| Tahun | 2021 |
| Venue | Proceedings of 2021 International Conference on Information Management and Technology Icimtech 2021 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [herman2021deep.pdf](../pdf/herman2021deep.pdf)
- DOI resmi: https://doi.org/10.1109/icimtech53080.2021.9534988

## Gambaran Umum

Penulis menyatakan bahwa pemanenan tandan buah segar (TBS) kelapa sawit di Indonesia sebagian besar masih dilakukan secara manual. Studi ini menguji pengklasifikasian tingkat kematangan TBS dari citra dengan *convolutional neural network* (CNN, jaringan saraf yang belajar fitur citra lewat lapisan konvolusi). Pembanding utamanya adalah AlexNet, yang sudah dipakai pada studi terdahulu untuk tugas yang sama, dan DenseNet 121 lapis.

Data berupa 400 citra TBS yang diberi label tujuh kategori kematangan oleh pakar. Kategorinya adalah Ripening 16, Raw 8, Less Ripped 64, Almost Ripped 16, Ripped 96, Perfectly Ripped 168, dan Too Ripped 32 citra. Tempat pengambilan, sensor, jumlah pohon, dan cara memperoleh citra tidak disebut. Data dibagi acak menjadi latih 60%, validasi 20%, dan uji 20%. Pembagian per pohon tidak disebut.

Kedua model diinisialisasi dari bobot yang sudah dilatih pada ImageNet (*transfer learning*, memakai pengetahuan dari set data besar untuk set data kecil). AlexNet memiliki lima lapisan konvolusi dan tiga lapisan terhubung penuh. DenseNet menambahkan peta fitur semua lapisan sebelumnya pada setiap *dense block* melalui sambungan padat. Pelatihan memakai 50 *epoch* dengan *stochastic gradient descent* (SGD) berlaju belajar 0,001 yang dikurangi sepersepuluh setiap delapan *epoch*, dengan PyTorch. Metrik yang dipakai adalah akurasi, presisi, *recall*, dan skor F1.

Pada data uji, AlexNet memperoleh akurasi 77%, presisi 78%, *recall* 77%, dan F1 77%. DenseNet memperoleh akurasi 86%, presisi 87%, *recall* 86%, dan F1 86%. Abstrak menyebut selisih 8,5% pada akurasi dan 8% pada F1, yang tidak sama dengan selisih pada Tabel II (9 poin). Penulis mengaitkan keunggulan DenseNet dengan kinerjanya yang lebih baik pada ImageNet dan dengan sambungan padat yang mengurangi masalah gradien lenyap. Penjelasan ini tidak diuji dengan eksperimen.

Keterbatasan yang dapat diperiksa dari teks: set uji hanya sekitar 80 citra, dengan kelas terkecil (Raw) sekitar 1 sampai 2 citra pada set uji bila pembagian proporsional. Hanya satu kali pelatihan yang dilaporkan, tanpa ulangan atau selang kepercayaan. Pembagian acak per citra tidak menjamin citra dari pohon yang sama tidak ada di latih dan uji. Tidak ada pencacahan, deteksi tandan, atau matriks konfusi per kelas.
