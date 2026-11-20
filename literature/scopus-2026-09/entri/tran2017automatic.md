# Automatic dragon fruit counting using adaptive thresholds for image segmentation and shape analysis

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tran2017automatic` |
| Judul asli | Automatic dragon fruit counting using adaptive thresholds for image segmentation and shape analysis |
| Penulis | Tran, Chi Cuong; Nguyen, Dinh Tu; Dang Le, Hoang; Truong, Quoc Bao; Dinh Truong, Quoc |
| Tahun | 2017 |
| Venue | 2017 4th Nafosted Conference on Information and Computer Science Nics 2017 Proceedings |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | pitaya |

## Tautan Akses
- PDF: [tran2017automatic.pdf](../pdf/tran2017automatic.pdf)
- DOI resmi: https://doi.org/10.1109/nafosted.2017.8108052

## Gambaran Umum

Kajian ini membahas penghitungan buah naga secara otomatis dari citra pohon. Penaksiran hasil panen di lapangan masih banyak dilakukan secara manual. Cara ini memakan waktu dan tenaga. Selain itu, penaksiran manual sering memicu perselisihan antara petani dan pedagang saat harga dinegosiasikan. Penulis mengusulkan algoritma pengolahan citra yang dapat menghitung jumlah buah per pohon. Dengan cara ini, estimasi *yield* diharapkan lebih cepat dan lebih akurat.

Data yang digunakan berupa citra buah naga yang diambil dari internet. Penulis menyatakan bahwa citra tersebut berasal dari sudut, jarak, dan sumber yang berbeda, sehingga algoritma perlu menangani keragaman ini. Pengujian dilakukan di komputer dengan contoh buah dari sumber daring. Sensor yang digunakan adalah kamera, tetapi jenisnya tidak diuraikan. Dua kasus pohon ditampilkan sebagai contoh hasil. Kasus pertama memiliki 22 buah menurut hitungan manual, sedangkan kasus kedua memiliki 7 buah. Teks tidak menjelaskan jumlah total citra atau pembagian data latih dan data uji.

Metode terdiri dari beberapa tahap. Pertama, citra disaring dengan *Gaussian filter* berukuran 3x3 untuk mengurangi derau. Kedua, citra dipetakan ke ruang warna *YCbCr*, yang dipilih karena komponen kecerahan dan warnanya dinilai efisien untuk segmentasi. Ketiga, penulis memakai ambang adaptif berbasis metode Otsu untuk memisahkan buah dari latar belakang. Bentuk setiap objek kemudian dianalisis dengan nilai *roundness*. Buah yang saling menempel dipisahkan dengan *distance transform*, lalu area yang tersegmentasi berlebihan (*oversegmentation*) diidentifikasi. Pada citra pertama, hitungan otomatis menghasilkan 21 buah, sedangkan hitungan manual menghasilkan 22 buah. Selisihnya satu buah. Pada kasus kedua, hitungan akurat adalah 7 buah. Hasil ini bersifat ilustratif karena hanya dua pohon yang ditampilkan.

Penulis menyatakan beberapa batasan. Sistem tidak dapat mengenali buah yang tertutup sekaligus saling tumpang tindih. Sistem juga tidak dapat mengenali dan menemukan lokasi buah jika area buah yang terlihat pada citra sangat kecil akibat tertutup dan bertumpuk. Metode ini bekerja baik pada area yang besar. Untuk pengembangan lanjut, penulis berencana membangun sistem visi komputer berbasis perangkat tertanam yang mengambil citra langsung di kebun. Tujuan jangka panjangnya adalah robot visi untuk panen otomatis sekaligus estimasi produktivitas buah.
