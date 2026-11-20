# Apple Counting Network before Fruit Thinning Period Based on Dilated Convolution

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `song2022apple` |
| Judul asli | Apple Counting Network before Fruit Thinning Period Based on Dilated Convolution |
| Penulis | Song, Mengyang; Jiang, Guoquan; Huo, Zhanqiang; Yang, Zhengyuan; Zhang, Hongxu |
| Tahun | 2022 |
| Venue | ACM International Conference Proceeding Series |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [song2022apple.pdf](../pdf/song2022apple.pdf)
- DOI resmi: https://doi.org/10.1145/3579895.3579915

## Gambaran Umum

Penghitungan buah secara otomatis merupakan bagian penting dari manajemen kebun yang presisi. Jumlah buah pada pohon memberi informasi untuk memperkirakan hasil panen. Saat ini petani apel hanya dapat menghitung buah secara manual. Cara ini memakan waktu dan tenaga. Kajian ini mengusulkan FTACNet, jaringan untuk menghitung buah apel sebelum periode penjarangan. Jaringan ini dirancang untuk mengatasi naungan, sebaran buah yang tidak merata, dan perbedaan ukuran buah.

Data dikumpulkan dengan kamera ponsel pintar pada pohon apel yang sudah berbuah, sebelum periode penjarangan. Buah pada tahap ini umumnya berwarna hijau limau dan tumbuh berkelompok. Warnanya mirip dengan daun, sehingga buah sulit dibedakan. Citra diambil dalam berbagai kondisi cahaya, yaitu cahaya dari atas, pengukuran cahaya, dan cahaya dari belakang. Dataset berisi 862 citra. Sebanyak 689 citra dipakai sebagai data latih dan 173 citra sebagai data uji. Setiap buah diberi anotasi berupa satu titik di pusat buah, mengikuti cara pelabelan pada penghitungan kerumunan. Buah yang jatuh ke tanah tidak diberi label. Penulis menyatakan bahwa hasil pada apel dapat diperluas ke buah lain yang mirip, seperti kiwi, pir, dan persik.

Metode yang diusulkan memakai *dilated convolution* dan fungsi kerugian *Bayesian loss*. Jaringan menghasilkan *density map*, lalu jumlah buah diperoleh dengan mengintegralkan peta tersebut. Penulis menilai fungsi kerugian ini lebih tepat daripada *Gaussian kernel* untuk menghasilkan peta kepadatan, karena oklusi antarbuah dan antara daun dan buah tidak selalu tergambar baik oleh kernel Gaussian. Arsitektur terdiri atas enam lapisan *dilated convolution*. Pada ablasi, varian dengan laju dilasi 2 pada semua enam lapisan (FTACNet A) dibandingkan dengan varian yang memakai laju 2 pada tiga lapisan pertama dan 4 pada tiga lapisan terakhir (FTACNet B). Varian B menghasilkan hasil terbaik dan dipakai pada eksperimen berikutnya.

Dalam perbandingan pada data uji, CSRNet menghasilkan MAE 9,79 dan MSE 12,71. CSRNet+, yaitu CSRNet dengan ukuran kernel tetap 3, menghasilkan MAE 5,85 dan MSE 7,52. Metode *Bayesian loss* dengan VGG19 menghasilkan MAE 4,29 dan MSE 5,94. FTACNet dengan VGG19 menghasilkan MAE 4,14 dan MSE 5,62. Dibandingkan dengan *Bayesian loss*, MAE FTACNet turun 3,5 persen dan MSE turun 5,4 persen. Peta kepadatan hasil prediksi juga dinilai sangat dekat dengan jumlah sebenarnya. Penulis menyimpulkan bahwa penghitungan apel dapat dilakukan dengan baik menggunakan ponsel pintar dan model yang kecil, sehingga cocok untuk perangkat seluler.

Penulis menyebutkan bahwa data hanya dikumpulkan sebelum tahap penjarangan buah. Model belum diuji pada tahap pertumbuhan lain, seperti pembungaan dan pematangan. Penulis merencanakan pengumpulan data pada beberapa tahap pertumbuhan agar model lebih tangguh.
