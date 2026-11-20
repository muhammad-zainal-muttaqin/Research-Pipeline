# On-Tree Detection and Counting of Apple Using Color Thresholding and CHT

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `behera2018tree` |
| Judul asli | On-Tree Detection and Counting of Apple Using Color Thresholding and CHT |
| Penulis | Behera, Santi Kumari; Mishra, Namrata; Sethy, Prabira Kumar; Rath, Amiya Kumar |
| Tahun | 2018 |
| Venue | Proceedings of the 2018 IEEE International Conference on Communication and Signal Processing Iccsp 2018 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [behera2018tree.pdf](../pdf/behera2018tree.pdf)
- DOI resmi: https://doi.org/10.1109/iccsp.2018.8524363

## Gambaran Umum

Penghitungan buah apel di pohon sangat penting untuk memperkirakan hasil panen, tetapi pekerjaan ini masih bergantung pada tenaga kerja yang banyak. Di kawasan Himalaya India, yaitu Himachal Pradesh, Arunachal Pradesh, dan Jammu dan Kashmir, biaya upah panen menjadi masalah utama bagi petani apel. Sistem panen otomatis atau robot dapat mengurangi masalah ini, tetapi memerlukan pengolahan citra yang andal untuk mendeteksi buah yang berkelompok, tertutup cabang dan daun, serta difoto dalam pencahayaan yang berubah-ubah. Penulis juga menyebut bahwa daun yang tampilannya mirip buah sering menimbulkan deteksi keliru. Kajian ini ditulis oleh Santi Kumari Behera, Namrata Mishra, Prabira Kumar Sethy, dan Amiya Kumar Rath, dan dipresentasikan pada *International Conference on Communication and Signal Processing* di India pada April 2018. Tujuannya adalah membuat metode yang dapat mendeteksi dan menghitung apel di pohon, baik yang terlihat utuh maupun sebagian.

Cakupan data kajian ini berupa citra apel di pohon yang dibagi dalam beberapa situasi visual. Situasi pertama berisi buah yang tidak tertutup, situasi kedua berisi buah yang saling bersentuhan, situasi ketiga berisi buah yang tertutup daun lebih dari 60%, dan situasi keempat berisi buah yang bersentuhan dan sebagian tertutup daun sekitar 40%. Situasi kelima berisi buah yang tertutup rapat oleh daun. Penulis menyebut 15 citra sampel untuk pengujian utama, sedangkan pengamatan buah tertutup dalam Tabel II menggunakan lima sampel. Penulis juga meninjau metode sebelumnya. Jaringan saraf tiruan dan pohon keputusan mencapai ketepatan 80%, sedangkan metode warna dan kehalusan permukaan untuk apel hijau mencapai 85%. Pada kondisi pencahayaan difus, ketepatan identifikasi dilaporkan meningkat menjadi 95%.

Metode yang diusulkan mengubah citra RGB ke ruang warna *L\*a\*b\** untuk *color thresholding*, sehingga setiap piksel dapat dipisahkan antara buah dan latar. Citra hasil segmentasi kemudian diubah menjadi citra biner dan diproses dengan *circular Hough transform* (CHT), yaitu teknik deteksi lingkaran dengan jari-jari yang tidak diketahui sebelumnya. Dalam penelitian ini, jari-jari yang diuji berkisar antara 10 sampai 60, dan sudut antara 0 sampai 360 derajat. Pusat lingkaran dicari melalui akumulator voting, lalu puncak lokal pada akumulator dianggap sebagai pusat buah. Hasil utama dinyatakan dalam Tabel I, dengan akurasi penghitungan sebesar 97,70% pada kondisi alami. Beberapa baris Tabel I juga mencatat nilai 83,33% sampai 93,33%. Pada pengamatan visual, jumlah buah hasil penghitungan otomatis sama dengan penghitungan manual pada situasi pertama sampai keempat. Pada situasi kelima, satu buah yang terpisah oleh daun dihitung sebagai dua buah. Untuk buah tertutup dalam Tabel II, kesalahannya sebesar 4%.

Penulis menyatakan bahwa metode ini dapat diterapkan pada berbagai jenis apel tanpa bergantung pada bentuk dan ukuran, dalam kondisi cahaya siang hari yang normal. Keunggulannya dinyatakan sebagai kemampuan menghitung buah yang tertutup atau tumpang tindih dengan kesalahan yang sangat kecil, yaitu 4%. Keterbatasan yang disebut penulis adalah kesalahan deteksi pada daun yang memisahkan satu buah sehingga terhitung dua kali. Penulis juga menyatakan bahwa pekerjaan lanjutan diperlukan untuk mendeteksi dan menghitung apel hijau di pohon pada seluruh kondisi lingkungan.
