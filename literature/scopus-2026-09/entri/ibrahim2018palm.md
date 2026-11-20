# Palm oil fresh fruit bunch ripeness grading recognition using convolutional neural network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ibrahim2018palm` |
| Judul asli | Palm oil fresh fruit bunch ripeness grading recognition using convolutional neural network |
| Penulis | Ibrahim, Z.; others |
| Tahun | 2018 |
| Venue | Journal of Telecommunication Electronic and Computer Engineering |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [ibrahim2018palm.pdf](../pdf/ibrahim2018palm.pdf)

## Gambaran Umum

Studi ini, yang diterbitkan di *Journal of Telecommunication, Electronic and Computer Engineering* (Vol. 10 No. 3-2), membandingkan beberapa cara mengenali tingkat kematangan tandan buah segar (TBS) kelapa sawit dari satu citra. Empat tingkat kematangan dipakai sebagai kelas. Data yang dipakai berjumlah 120 citra, masing-masing 30 citra per kelas, yang difoto pada siang hari tanpa pemotongan (*cropping*) dan diberi label oleh satu pakar sawit dari Johor, Malaysia.

Pendekatan dibandingkan dalam tiga kelompok: fitur buatan tangan (*handcrafted*) dengan pengklasifikasi SVM (momen warna, FREAK, dan HOG), CNN yang dilatih dari awal, dan AlexNet sebagai model prapelatihan. Data dibagi 80% latih dan 20% uji. Jumlah citra uji tidak dilaporkan secara eksplisit; dengan pembagian tersebut, hitungannya kira-kira 24 citra, tetapi angka ini belum diverifikasi dari teks.

Hasil utama: CNN dengan satu tumpukan lapisan mencapai akurasi 0,92 (92%) dengan waktu 1,857 detik (Tabel 1), setara dengan dua tumpukan. AlexNet mencapai akurasi 1 (100%) pada laju belajar 0,001 dengan waktu 84,47 detik (Tabel 2). Fitur buatan tangan dengan SVM mencapai akurasi tertinggi 0,75 pada HOG (Tabel 3). Penulis menyimpulkan bahwa AlexNet unggul ketika data latih sedikit, dengan biaya waktu proses yang lebih besar.

Batasan yang dinyatakan penulis: hasil CNN dan AlexNet bergantung pada ukuran filter, *stride*, jumlah epoch, dan laju belajar, dan hanya sebagian kombinasi yang diuji. Warna dipengaruhi pencahayaan, sehingga momen warna memberi hasil terendah. Penulis juga menyebut bahwa pemotongan citra manual dapat memperbaiki hasil, tetapi memakan waktu. Sebagai kerangka tinjauan ini, studi ini mengklasifikasikan kelas per citra dan tidak menghitung buah; tidak ada unsur identitas lintas pandang.
