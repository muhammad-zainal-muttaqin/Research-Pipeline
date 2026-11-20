# Three dimensional apple tree organs classification and yield estimation algorithm based on multi-features fusion and support vector machine

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ge2022three` |
| Judul asli | Three dimensional apple tree organs classification and yield estimation algorithm based on multi-features fusion and support vector machine |
| Penulis | Ge, Luzhen; Zou, Kunlin; Zhou, Hang; Yu, Xiaowei; Tan, Yuzhi; Zhang, Chunlong; Li, Wei |
| Tahun | 2022 |
| Venue | Information Processing in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [ge2022three.pdf](../pdf/ge2022three.pdf)
- DOI resmi: https://doi.org/10.1016/j.inpa.2021.04.011

## Gambaran Umum

Ge dkk. (2022) menghitung buah apel dari titik awan tiga dimensi yang dibangun dari beberapa citra RGB. Kajian ini diterbitkan di *Information Processing in Agriculture* 9 (2022) 431–442. Citra diambil dengan kamera Intel RealSense D435 dari berbagai sudut pandang mengelilingi pohon, lalu *structure from motion* (SfM) dengan VisualSFM dan PMVS menghasilkan titik awan pohon. Setiap titik diberi 196 fitur gabungan yang berisi nilai warna RGB, HSV, kelengkungan, *fast point feature histogram* (FPFH), dan *spin image*. Titik-titik itu lalu diklasifikasikan menjadi buah, cabang, dan daun.

Masalah yang diangkat adalah pemisahan buah dari daun dan cabang pada titik awan yang tidak merata. Sebelum klasifikasi, titik awan diturunkan resolusinya dengan kisi kotak (*box grid*), outlier dihapus, dan label titik dihaluskan dengan bobot berdasarkan posisi. Setelah itu, klasterisasi hierarkis aglomeratif memisahkan buah tunggal dari kelompok buah yang menempel. Tahap ini dipakai untuk menghitung jumlah buah per pohon.

Klasifikasi dibandingkan pada tiga pengklasifikasi: *support vector machine* (SVM) linear, *k-nearest neighbors* (KNN), dan *ensemble*. Untuk kelas buah, rata-rata F1 SVM sebelum penghalusan adalah 79,66% dan sesudah penghalusan naik menjadi 86,04%. KNN memberi 51,59% dan *ensemble* 70,58% pada kelas buah. Recall buah naik dari 88,38% menjadi 94,62% setelah penghalusan. Kelas cabang naik dari 69,64% menjadi 74,49%, dan kelas daun dari 41,70% menjadi 44,90%. Kenaikan itu menunjukkan bahwa penghalusan berbobot posisi membantu, tetapi nilai kelas daun dan cabang tetap rendah.

Uji panen dilakukan pada beberapa pohon apel dan jumlah buah hasil metode dibandingkan dengan hitungan manual. Hasil akhirnya melaporkan recall 93,75%, precision 96,15%, dan F1 94,93% untuk estimasi panen. Pada pohon lain, F1 kelas daun turun hingga 29,49%, dan salah klasifikasi dikaitkan dengan pencahayaan siang hari serta oklusi. Batas kajian ini jelas: data berasal dari satu jenis pohon di satu kebun, jumlah pohon uji kecil, dan kelas daun serta cabang tidak stabil.

(2022) menunjukkan bahwa titik awan SfM dari citra RGB dapat dipakai untuk menghitung buah apel dengan pengklasifikasi konvensional. Ia termasuk kelompok depth dan sensing 3D karena rekonstruksi geometrinya menjadi dasar klasifikasi, tetapi bukti yang disajikan berasal dari apel dan belum diuji pada sawit.
