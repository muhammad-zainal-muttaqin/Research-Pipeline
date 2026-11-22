# Identification and Counting Method of Potted Kumquat Fruits Based on Point Cloud Registration

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhu2022identification` |
| Judul asli | Identification and Counting Method of Potted Kumquat Fruits Based on Point Cloud Registration |
| Penulis | Zhu, Qibing; Zhang, Meng; Liu, Zhenfang; Huang, Min; Li, Xuecheng |
| Tahun | 2022 |
| Venue | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [zhu2022identification.pdf](../pdf/zhu2022identification.pdf)
- DOI resmi: https://doi.org/10.6041/j.issn.1000-1298.2022.05.021

## Gambaran Umum

Makalah ini mengusulkan identifikasi dan penghitungan buah kumquat dalam pot secara menyeluruh berbasis pendaftaran awan titik tiga dimensi. Tujuannya adalah menghitung jumlah buah sekaligus menampilkan sebaran spasialnya. Penulis menyatakan bahwa citra RGB tunggal hanya memuat informasi tiga dimensi sebagian tanaman, sehingga sukar dipakai untuk estimasi total satu tanaman. Penggabungan hasil dari beberapa citra tunggal berisiko menghitung buah yang sama dua kali.

Perangkat yang dipakai adalah kamera RGB-D Kinect 2.0 berbasis time-of-flight. Kamera ini menghasilkan citra warna 1920×1080 pixel, citra kedalaman 512×424 pixel, dan awan titik dengan rentang ukur terbaik 0,8-2,0 m. Tanaman diletakkan di atas meja putar dengan keliling 1,0 m yang berjarak sekitar 1,0 m dari kamera. Putaran 60° menghasilkan enam sudut pandang. Awan titik dari tiap sudut digabungkan dengan citra warna, lalu dibersihkan dari latar, titik pencilan, derau warna putih, serta flying pixel dan derau tepi. Pembersihan memakai radius filtering, sifat vektor normal, dan Euclidean clustering dengan ambang jarak 0,005 m.

Pendaftaran awan titik dilakukan dua tahap. Tahap awal memakai RANSAC untuk mengsegmentasi awan titik silinder meja putar dan menghitung sumbu rotasi, lalu memutar awan titik sebesar sudut yang bersesuaian. Tahap lanjutan memakai ICP point-to-plane agar hasil lebih teliti. Setelah awan titik tanaman lengkap terbentuk, Euclidean clustering membagi tanaman menjadi beberapa klaster. RANSAC spherical segmentation kemudian memisahkan tiap buah, dan titik pusat serta jari-jari bola dipakai untuk menampilkan posisi tiga dimensi buah.

Uji coba dilakukan pada sembilan tanaman pot dengan total 149 buah pada tahap pertumbuhan. Abstrak melaporkan recall total 85,91%, presisi 79,01%, nilai F1 82,32%, koefisien determinasi 0,97 antara jumlah buah prediksi dan jumlah sebenarnya, serta galat absolut persentase rata-rata 16,02%. Metode ini tidak bergantung pada informasi warna sehingga tetap mengenali buah hijau yang belum matang.

Pendahuluan menyebut GONGAL dkk. memasang kamera warna dan kamera kedalaman dalam jumlah sama pada kedua sisi pohon apel, lalu mendaftarkan awan titik dari kedua sisi untuk mengenali buah yang terhitung dua kali. Penulis mengutipnya sebagai contoh penanganan duplikasi lintas pandang, sedangkan metode yang diusulkan sendiri memakai meja putar dan satu kamera.
