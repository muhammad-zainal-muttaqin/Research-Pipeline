# Oil Palm Fresh Fruit Bunch Ripeness Classification by Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `saechen2023oil` |
| Judul asli | Oil Palm Fresh Fruit Bunch Ripeness Classification by Deep Learning |
| Penulis | , |
| Tahun | 2023 |
| Venue | Science and Engineering Connect |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [saechen2023oil.pdf](../pdf/saechen2023oil.pdf)
- DOI resmi: https://doi.org/10.14456/kmuttrd.2023.6

## Gambaran Umum

Penelitian ini bertujuan membangun model *deep learning* untuk menganalisis foto tandan buah segar kelapa sawit dan mengklasifikasikan tingkat kematangannya secara tepat. Latar belakangnya adalah praktik di Thailand, ketika pegawai pabrik menilai kematangan tandan secara visual di titik pembelian. Penilaian ini sering keliru, sehingga pabrik minyak sawit membayar tandan lebih mahal dari kadar minyak yang sebenarnya dihasilkan. Model yang akurat diharapkan membantu mengurangi kesalahan tersebut dan menekan biaya produksi.

Data berupa foto tandan buah segar yang dikumpulkan di pabrik ekstraksi minyak sawit di Surat Thani, dengan bantuan sebuah perusahaan minyak sawit. Pengambilan gambar memakai empat kamera, yaitu dua ponsel (Android dan iOS) dan dua kamera *mirrorless* (FUJI dan SONY). Empat orang pengumpul data memotret tandan dalam jumlah yang sama untuk setiap kelas, dan 5 sampai 10 pegawai pabrik menentukan kelas kematangan. Setiap foto memuat satu tandan utuh di tengah bingkai, lalu dipotong menjadi persegi. Empat kelas yang dipakai adalah tandan mentah (*unripe*), tandan setengah matang (*underripe*), tandan matang penuh (*fully ripe*), dan tandan terlalu matang (*overripe*). Data tidak dipisahkan menurut varietas, karena pabrik membeli tandan tanpa memilah varietas. Jumlah citra total dan rincian pembagian data latih, data evaluasi, dan data uji tidak tercantum dalam bagian yang dibaca.

Penulis membandingkan beberapa arsitektur, antara lain ResNet50, VGG16, dan DenseNet121, dengan variasi *fine tuning* dan pelatihan dari awal. Ukuran utama adalah *adjusted accuracy*, disertai *F1 score* per kelas dan *confusion matrix*. Model ResNet50(C) memberi *adjusted accuracy* terbaik 90 persen, dan *F1 score* tiap kategori lebih dari 80 persen. Model ini berukuran 405 MB dengan waktu uji rata-rata 2,48 detik pada GPU dan 3,27 detik pada CPU. Model DenseNet121 (*train from scratch*) mencapai 86 persen, sedikit di bawah ResNet50(C), tetapi berukuran 100 MB dengan waktu uji 1,76 detik pada GPU dan 2,56 detik pada CPU. Pada bagian hasil, DenseNet121 (*train from scratch*), ResNet50 (*fine tuning*), dan VGG16 (*fine tuning*) disebut sebagai tiga model terbaik, dengan akurasi pada data evaluasi 90, 89, dan 87 persen, serta pada data uji 92, 89, dan 88 persen. VGG16 (*fine tuning*) tercatat paling cepat, yaitu 0,19 detik per citra dengan GPU. Model juga diuji dengan *Grad-CAM* untuk memeriksa apakah area yang diperhatikan berada pada tandan. Hasil menunjukkan model umumnya memperhatikan tandan utama. Model tetap stabil ketika kecerahan foto diubah antara -70 hingga +70 dari cahaya matahari normal.

Penulis menyatakan beberapa batasan. Kelas *underripe* dan *fully ripe* sulit dibedakan, dengan *F1 score* antara 66 hingga 92 persen, karena warna keduanya mirip. Kelas *underripe* juga memiliki data lebih sedikit dibanding kelas lain. Penelitian ini hanya memakai satu tandan per foto dan tidak menghitung buah yang lepas dari tandan, karena pengumpul data tidak dapat memastikan asal buah lepas tersebut. Latar belakang foto tidak dikendalikan, dan data tidak mencakup varietas Surat Thani 1 yang memiliki warna dan tekstur berbeda. Penulis juga menyebut bahwa model dengan akurasi lebih tinggi cenderung berukuran besar dan lebih lambat, sehingga pemilihan model bergantung pada kebutuhan pabrik.
