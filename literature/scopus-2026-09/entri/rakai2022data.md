# Data association in multiple object tracking: A survey of recent techniques

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `rakai2022data` |
| Judul asli | Data association in multiple object tracking: A survey of recent techniques |
| Penulis | Rakai, Lionel; Song, Huansheng; Sun, ShiJie; Zhang, Wentao; Yang, Yanni |
| Tahun | 2022 |
| Venue | Expert Systems with Applications |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [rakai2022data.pdf](../pdf/rakai2022data.pdf)
- DOI resmi: https://doi.org/10.1016/j.eswa.2021.116300

## Gambaran Umum

Kajian ini meninjau *data association* dalam *multiple object tracking* (MOT) pada video pengawasan. Asosiasi data adalah tahap yang mencocokkan objek yang baru terdeteksi dengan lintasan (*track*) yang sudah ada pada setiap frame video. Tahap ini penting untuk menjaga identitas objek agar tidak tertukar dan agar lintasan tidak terputus. Penulis menyatakan bahwa tahap asosiasi sering dibahas tercampur dengan keseluruhan kerangka MOT, sehingga kontribusinya sulit dinilai secara terpisah. Karena itu, penulis memfokuskan tinjauan pada teknik asosiasi itu sendiri, yaitu fungsi kemiripan dan filter yang dipakai untuk mengaitkan objek.

Cakupan tinjauan berada pada bidang visi komputer dan ilmu komputer, khususnya MOT untuk kendaraan dan pejalan kaki dalam video pengawasan lalu lintas. Penulis memilih makalah yang terbit dalam tiga tahun terakhir sebelum kajian, dengan mempertimbangkan topik, tahun terbit, kata kunci, jumlah sitasi, dan sumber terbit. Tinjauan ini tidak menggunakan satu set data eksperimen tunggal. Sumber data berupa makalah-makalah yang sudah diterbitkan, dan setiap metode dibandingkan berdasarkan karakteristik kinerjanya. Penulis juga menyebut bahwa sebagian tinjauan terdahulu memuat daftar rujukan yang terbatas, sehingga kajian ini berusaha mencakup lebih banyak makalah terbaru.

Metode tinjauan membagi teknik asosiasi data ke dalam kelompok berdasarkan teknik pokoknya. Kelompok tersebut adalah probabilistik, hierarkis, *interacting multiple model* (IMM), berbasis *Kalman filter*, asosiasi fuzzy, dan teknik baru. Setiap model dinilai dari lima aspek, yaitu stabilitas, akurasi, ketahanan (*robustness*), kecepatan, dan kompleksitas komputasi. Penulis tidak menyajikan angka hasil gabungan dari semua makalah karena hasil kuantitatif sangat bergantung pada kerangka MOT tempat asosiasi itu dipakai. Sebagai contoh, teks mengutip perbandingan *particle filter* dan *Kalman filter* pada citra mikroskopi, yang menunjukkan nilai rata-rata dan simpangan baku yang lebih tinggi untuk *Kalman filter*. Hasil utama tinjauan bersifat kualitatif dan dirangkum dalam tabel kelebihan dan kekurangan setiap model. Hasil itu juga memperlihatkan bahwa banyak publikasi masih memakai pendekatan probabilistik dan hierarkis karena keberhasilannya pada ukuran akurasi. Penelitian dengan teknik baru menunjukkan fokus pada peningkatan akurasi, tetapi hasil dari teknik baru itu lebih merata antara stabilitas, ketahanan, dan kecepatan.

Penulis menyatakan beberapa batasan tinjauan ini. Pertama, perbandingan kuantitatif antarmodel sulit dilakukan karena setiap angka hasil terikat pada kerangka MOT masing-masing. Kedua, cakupan tinjauan dibatasi pada pelacakan kendaraan dan pejalan kaki dalam video lalu lintas, baik dengan kamera tunggal maupun banyak kamera. Ketiga, penulis mencatat kelemahan yang belum teratasi, yaitu pemodelan penampilan objek, kompleksitas komputasi, dan kesulitan mencapai kinerja waktu nyata yang sesungguhnya. Penulis juga mencatat bahwa penggabungan deteksi dan asosiasi dalam satu model masih merupakan konsep masa depan, sedangkan saat ini asosiasi data umumnya masih dipisahkan sebagai model atau lapisan tersendiri. Penulis mengusulkan arah penelitian lanjutan berupa model hibrida yang menggabungkan keunggulan beberapa kategori.
