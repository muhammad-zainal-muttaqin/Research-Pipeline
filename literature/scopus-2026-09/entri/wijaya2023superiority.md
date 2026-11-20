# THE SUPERIORITY OF YOLOV4 MODEL FOR ENHANCING PALM OIL FRUIT DETECTION

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wijaya2023superiority` |
| Judul asli | THE SUPERIORITY OF YOLOV4 MODEL FOR ENHANCING PALM OIL FRUIT DETECTION |
| Penulis | Wijaya, V.F.; others |
| Tahun | 2023 |
| Venue | Journal of Theoretical and Applied Information Technology |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [wijaya2023superiority.pdf](../pdf/wijaya2023superiority.pdf)

## Gambaran Umum

Kajian ini bertujuan menguji apakah integrasi informasi warna dan tekstur dapat meningkatkan kinerja deteksi objek menggunakan model *YOLOv4*. Penulis berangkat dari keterbatasan metode deteksi tradisional, seperti *Support Vector Machine* dan *Random Forest*, yang bergantung pada rekayasa fitur manual. Metode tersebut kesulitan menangani citra dengan oklusi, perubahan skala, variasi posisi, dan kondisi pencahayaan yang beragam. Penulis menilai warna dan tekstur sebagai fitur penting untuk membedakan objek yang memiliki bentuk serupa. Dalam konteks ini, kemampuan tersebut dapat dimanfaatkan untuk menilai tingkat kematangan buah kelapa sawit.

*YOLOv4* termasuk detektor satu tahap yang memprediksi *bounding box* dan probabilitas kelas dalam satu kali proses. Arsitekturnya terdiri atas *backbone* CSPDarknet53 dan kepala deteksi. *Backbone* mengekstraksi fitur dari citra masukan, sedangkan kepala deteksi memprediksi kelas, posisi, dan tingkat kepercayaan objek. Penulis menjelaskan bahwa SPP digunakan untuk menangkap objek dengan berbagai ukuran, sedangkan *cross-stage partial* connection meningkatkan penggunaan fitur dan mengurangi jumlah parameter jaringan. *Anchor box* juga membantu model memprediksi kotak pembatas objek. Menurut penulis, mekanisme ini menurunkan jumlah positif palsu dan memperbaiki lokalisasi objek.

Kajian menggunakan kumpulan data tandan buah kelapa sawit (*oil palm fruit bunch*) yang terdiri atas 4156 citra. Citra tersebut dikelompokkan ke dalam enam kelas, yaitu Overripe, Ripe, Raw, Underripe, Abnormal, dan Empty. Pemilihan kumpulan data ini didasarkan pada potensi analisis tekstur dan warna untuk menilai tingkat kematangan buah. Penulis menyatakan bahwa mereka memilih beberapa kumpulan data dengan tingkat informasi warna dan tekstur yang bervariasi untuk eksperimen.

Penulis membandingkan beberapa varian model, yaitu YOLOv4, YOLOv4 Tiny, YOLOv4 Tiny_3l, dan YOLOv4_csp. Langkah penelitian meliputi praproses data untuk menghilangkan gangguan warna, penyetelan hiperparameter model YOLO, pengklasifikasian objek dengan warna dan tekstur yang mirip, serta perbandingan metrik evaluasi dengan beberapa model YOLOv4 terlatih. Hasil utama mencakup rata-rata *intersection over union* sebesar 89,95%, mAP@50 sebesar 99,85%, *recall* 0,996, *F1-score* 0,987, dan *precision* 0,979. Penulis menyimpulkan bahwa integrasi warna dan tekstur memberikan peningkatan akurasi deteksi yang signifikan, terutama pada skenario dengan latar belakang rumit dan pencahayaan yang bervariasi. Penulis juga menyatakan bahwa temuan ini menunjukkan efektivitas YOLOv4 untuk aplikasi tersebut dan berpotensi diterapkan pada bidang deteksi objek yang lebih luas.
