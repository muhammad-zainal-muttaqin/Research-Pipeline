# Counting Apples and Oranges with Deep Learning: A Data-Driven Approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2017counting` |
| Judul asli | Counting Apples and Oranges with Deep Learning: A Data-Driven Approach |
| Penulis | Chen, Steven W.; Shivakumar, Shreyas S.; Dcunha, Sandeep; Das, Jnaneshwar; Okon, Edidiong; Qu, Chao; Taylor, Camillo J.; Kumar, Vijay |
| Tahun | 2017 |
| Venue | IEEE Robotics and Automation Letters |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple, citrus |

## Tautan Akses
- PDF: [chen2017counting.pdf](../pdf/chen2017counting.pdf)
- DOI resmi: https://doi.org/10.1109/lra.2017.2651944

## Gambaran Umum

Chen dkk. (2017) menghitung buah dari citra kebun dengan satu pandangan kamera per citra. Penulis membangun sistem penghitungan untuk jeruk dan apel hijau, lalu mengukur seberapa dekat jumlah tebakan sistem dengan jumlah buah yang dilabeli manusia. Sistem terdiri atas tiga komponen yang dapat dikombinasikan: sebuah *blob detector* berbasis *fully convolutional network* yang menghasilkan peta lokasi buah, sebuah *count* CNN yang langsung menebak jumlah buah dalam satu *tile*, dan regresi linear yang mengubah keluaran itu menjadi angka hitungan. Penghitungan dilakukan per *tile* tanpa penggabungan antarpandang, sehingga kajian ini termasuk kelompok penghitungan satu pandang.

Data berasal dari dua kebun. Dataset jeruk diambil pada siang hari tanpa *trellis*. Dataset apel hijau diambil pada malam hari dengan *trellis*, sehingga kondisi cahaya dan latar belakangnya berbeda. Label dibuat melalui platform *crowd-sourcing* label.ag, tempat pelabel menandai setiap buah dengan lingkaran SVG. Citra penuh dipotong menjadi jendela yang saling tumpang tindih. Algoritma kebenaran dasar (Alg. 1) mencocokkan lingkaran pelabel dengan *tile* agar setiap buah dihitung di *tile* tempat ia tampak.

Hasil utama bergantung pada ambang keputusan (*threshold*) dan ukuran yang dipakai. Pada kurva *Receiver Operating Characteristic* (ROC), nilai terbaik terjadi pada ambang 0,02, dengan *true positive rate* 0,961 dan *false positive rate* 0,033. Pada rata-rata *Intersection over Union* (IU), nilai terbaik 0,838 terjadi pada ambang 0,37. Galat hitungan diukur dengan l½, yaitu rasio jumlah total terhitung terhadap jumlah sebenarnya beserta standar deviasinya. Galat l½ pipeline penuh sebesar 13,8 pada jeruk dan 10,5 pada apel. Pembanding berbasis tekstur hanya dijalankan pada dataset apel.

Dua batasan perlu dicatat. Pertama, label manusia dapat salah, dan kesalahan label ikut masuk ke ukuran galat dan IU. Kedua, makalah tidak menguji penghitungan lintas sensor atau lintas pandang, sehingga tidak ada bukti bahwa buah yang sama dari sudut berbeda dihitung sekali. Angka l½ dan IU juga hanya berlaku untuk dua kebun yang diuji, bukan untuk kondisi lain.
