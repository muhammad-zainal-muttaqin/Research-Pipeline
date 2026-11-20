# Towards linear-time incremental structure from motion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wu2013linear` |
| Judul asli | Towards linear-time incremental structure from motion |
| Penulis | Wu, Changchang |
| Tahun | 2013 |
| Venue | Proceedings 2013 International Conference on 3D Vision 3dv 2013 |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [wu2013linear.pdf](../pdf/wu2013linear.pdf)
- DOI resmi: https://doi.org/10.1109/3dv.2013.25

## Gambaran Umum

Kajian ini membahas kecepatan *structure from motion* (SfM) inkremental. Waktu komputasi SfM inkremental sering dinyatakan O(n4) terhadap jumlah kamera. Penulis menilai bahwa *bundle adjustment* (BA) sudah jauh lebih cepat sejak penggunaan *preconditioned conjugate gradient* (PCG). Karena itu, penulis ingin meninjau ulang seberapa cepat SfM inkremental sebenarnya. Tujuannya adalah merancang strategi BA yang seimbang antara kecepatan dan akurasi, serta menunjukkan bahwa banyak langkah utama SfM dapat berjalan dalam waktu O(n). Masalah lain yang diangkat adalah akumulasi *drift* tanpa *loop closing* eksplisit.

Penulis menguji metodenya pada lima kumpulan data dengan ukuran berbeda. Central Rome berisi 32768 citra dan Arts Quad berisi 6514 citra; keduanya diperoleh dari penulis kajian [4]. Loop berisi 4342 bingkai video beresolusi tinggi dari sebuah blok jalan. St. Peter's Basilica memiliki 1275 citra dan Colosseum memiliki 1164 citra. Sensornya berupa kamera biasa, dan platformnya berupa koleksi foto serta rangkaian video. Untuk Central Rome, pencocokan dilakukan dengan *preemptive matching* dengan h = 100 dan th = 4. Untuk St. Peter's Basilica dan Colosseum, seluruh pasangan citra dicocokkan secara penuh. Untuk Arts Quad dan Loop, setiap citra dicocokkan hanya dengan citra terdekat berdasarkan GPS. Eksperimen dijalankan pada PC dengan CPU Intel Xeon 5680 3,33 GHz (24 inti), RAM 12 GB, dan GPU nVidia GTX 480.

Metode utamanya adalah *preemptive feature matching*. Fitur tiap citra diurutkan menurut skala yang menurun. Kemudian, pada setiap pasangan citra, fitur pertama dicocokkan lebih dulu. Pasangan yang tidak lolos tidak perlu dicocokkan secara penuh. Pada St. Peter's Basilica, 43 persen kecocokan fitur yang benar diperoleh dengan hanya 6 persen pasangan citra. Sistem ini memproses 73K pasangan per detik dengan 24 thread. Pada tahap rekonstruksi, metode ini menghasilkan model SfM terbesar dengan 15065 kamera untuk Central Rome, serta model yang lengkap untuk kumpulan data lainnya. Pada th = 2, semua kumpulan data direkonstruksi lengkap. Pada th = 4, satu bangunan di Arts Quad hilang karena oklusi, dan model Colosseum pecah menjadi bagian interior dan eksterior. Penulis juga memakai *re-triangulation* (RT) untuk mengatasi *drift*. Pada Loop, RT membuat rekonstruksi 4342 bingkai tetap benar. Hasil akhir menunjukkan bahwa waktu rata-rata sekitar 2 kamera dan lebih dari 2000 titik fitur per detik. Waktu praktisnya kira-kira O(n) untuk masalah hingga 15K kamera.

Penulis menyatakan beberapa batasan. Pertama, *preemptive matching* dapat kehilangan tautan lemah ketika ambang batas besar, seperti terlihat pada Arts Quad dan Colosseum. Kedua, penulis belum memiliki skema pencocokan yang lebih adaptif. Penulis berencana mengeksplorasinya pada penelitian selanjutnya. Ketiga, penulis berencana memandu BA penuh berdasarkan akumulasi kesalahan reproyeksi. Keempat, penulis mengakui bahwa pendekatan inkremental tetap memiliki keterbatasan, misalnya inisialisasi yang memengaruhi kelengkapan model. Metode ini tidak memakai kalibrasi tambahan, data GPS, atau deteksi titik hilang sebagai pengganti inisialisasi tersebut.
