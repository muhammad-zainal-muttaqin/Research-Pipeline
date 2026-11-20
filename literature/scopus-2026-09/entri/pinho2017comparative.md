# Comparative Analysis between LDR and HDR Images for Automatic Fruit Recognition and Counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `pinho2017comparative` |
| Judul asli | Comparative Analysis between LDR and HDR Images for Automatic Fruit Recognition and Counting |
| Penulis | Pinho, Tatiana M.; Coelho, Jo\~ao Paulo; Oliveira, Josenalde; Boaventura-Cunha, Jos\'e |
| Tahun | 2017 |
| Venue | Journal of Sensors |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [pinho2017comparative.pdf](../pdf/pinho2017comparative.pdf)
- DOI resmi: https://doi.org/10.1155/2017/7321950

## Gambaran Umum

Penelitian ini membandingkan citra rentang dinamis rendah (LDR) dan rentang dinamis tinggi (HDR) untuk deteksi dan penghitungan buah pada pohon, dengan tujuan memprediksi hasil panen guna mendukung pertanian presisi. Permasalahannya adalah pemandangan alam memiliki rentang luminansi yang tidak dapat direpresentasikan secara memadai oleh kamera konvensional 8 bit, sehingga area sangat gelap atau sangat terang kehilangan detail dan deteksi buah menjadi kurang tepat. Penulis menguji hipotesis bahwa citra HDR, yang menyimpan informasi luminansi menyerupai penglihatan manusia, meningkatkan kemampuan deteksi dibandingkan citra LDR.

Data berupa citra jeruk dan lemon dari tiga studi kasus di distrik Aveiro, Portugal, yaitu pohon jeruk tunggal (18 buah), sekumpulan pohon jeruk (27 buah), dan pohon lemon (18 buah), ditambah kasus tambahan pada jeruk, lemon, dan plum. Citra diambil dengan kamera Canon EOS 5D Mark III yang dipasang pada statif, beresolusi 5760 × 3840 piksel, dalam tiga paparan, yaitu normal, lebih terang, dan lebih gelap. Paparan digabung menjadi citra HDR dengan Corel PaintShop Pro X6; pemrosesan dan deteksi dilakukan di MATLAB menggunakan HDR toolbox dengan tiga operator pemetaan nada, yaitu Reinhard, Drago, dan pemetaan nada bawaan kamera. Setiap kasus menghasilkan empat citra masukan: satu LDR dan tiga versi HDR.

Algoritma deteksi merupakan adaptasi dari fungsi SimpleColorDetectionByHue(): citra RGB diubah ke ruang warna HSV, ambang komponen hue diterapkan, wilayah dengan luas di bawah nilai tertentu dibuang, lalu fungsi imfindcircles() mencari bentuk lingkaran dengan jari-jari dalam rentang tertentu. Enam parameter ditetapkan lebih dahulu, yaitu batas bawah dan atas hue, luas minimum wilayah, jari-jari minimum dan maksimum, serta sensitivitas deteksi lingkaran. Kinerja diukur dengan hasil (yield) η(%) = (a − δ)/T × 100, dengan a jumlah buah yang teridentifikasi benar, δ jumlah positif palsu, dan T jumlah seluruh buah.

Pada studi kasus pertama (18 buah), η citra LDR sebesar 72,2% (13 buah), sedangkan HDR dengan pemetaan nada kamera 83,3% (15 buah), Reinhard 77,8% (14 buah), dan Drago 77,8% (14 buah); perbaikan terbesar 11,1%. Pada kasus kedua (27 buah), LDR memberi 22,2% (6 buah) sedangkan ketiga versi HDR masing-masing 55,6% (15 buah), dengan kenaikan sekitar 33,4%. Pada kasus ketiga (lemon, 18 buah), LDR dan HDR berkamera sama-sama 66,7% (12 buah), sementara Reinhard dan Drago masing-masing 61,1%; pemetaan Drago menghasilkan dua positif palsu. Pada kasus tambahan, perbaikan rata-rata HDR terhadap LDR sebesar 9,1% untuk jeruk, 2% untuk lemon (maksimum sekitar 13%), dan sekitar 21% untuk plum. Abstrak menyatakan peningkatan deteksi lebih dari 30% dibandingkan LDR. Tidak ada split latih-uji atau cawat uji yang dinyatakan; keenam parameter ditetapkan secara manual dan dijaga tetap dalam satu studi kasus.

Batasan yang dinyatakan penulis mencakup efek ghosting akibat objek yang tidak sejajar antarpaparan sehingga citra hasil mengabur dan kinerja deteksi turun; kondisi pencahayaan, karena perbedaan kinerja LDR dan HDR meningkat saat ada bayangan dan menyusut saat pencahayaan merata, serta LDR kadang lebih baik karena positif palsu pada HDR; pemetaan nada bawaan kamera memotong tepi citra sehingga satu buah di sudut kiri bawah tidak terlihat pada kasus lemon; lingkungan yang berubah karena daun bergerak akibat angin dan warna buah yang mirip warna daun. Penulis juga menyebut jumlah uji coba yang sedikit, algoritma deteksi bukan fokus utama (hanya pembuktian konsep), dan perlunya menghilangkan positif palsu serta mengotomatisasi penentuan ambang dan jari-jari. Tidak dinyatakan adanya perbandingan dengan metode pembelajaran mesin; penulis mengusulkan hal itu sebagai pekerjaan lanjutan.
