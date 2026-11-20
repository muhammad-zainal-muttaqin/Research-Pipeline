# Real-time oil palm FFB ripeness grading system based on ANN, KNN and SVM classifiers

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `alfatni2018real` |
| Judul asli | Real-time oil palm FFB ripeness grading system based on ANN, KNN and SVM classifiers |
| Penulis | Alfatni, Meftah Salem M; Mohamed Shariff, Abdul Rashid; Bejo, Siti Khairunniza; Ben Saaed, Osama M.; Mustapha, Aouache |
| Tahun | 2018 |
| Venue | Iop Conference Series Earth and Environmental Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [alfatni2018real.pdf](../pdf/alfatni2018real.pdf)
- DOI resmi: https://doi.org/10.1088/1755-1315/169/1/012067

## Gambaran Umum

Makalah ini membangun sistem penilaian tingkat kematangan tandan buah segar (TBS, *fresh fruit bunch*, FFB) kelapa sawit dari citra secara *real-time*. Tandan dibagi ke dalam tiga kelas: belum matang (*under ripe*), matang (*ripe*), dan terlalu matang (*over ripe*). Setiap tandan dinilai dengan fitur warna, tekstur, dan duri (*thorn*) pada permukaan tandan, lalu diklasifikasikan dengan tiga pengklasifikasi: jaringan saraf tiruan (ANN), k-tetangga terdekat (KNN), dan mesin vektor dukungan (SVM). Hasil utama yang dilaporkan penulis adalah akurasi 93% dan waktu pemrosesan 0,40 detik untuk fitur BGLAM dengan ANN.

Data terdiri atas 180 sampel TBS. Dua pertiga sampel dipakai untuk pelatihan dan sepertiga untuk pengujian, dengan 90 sampel uji per kelas. Penulis membuat basis data terpisah untuk tiap jenis TBS. Makalah tidak menyebut jumlah sampel per kelas pada data latih.

Penulis memakai tiga kelompok fitur.

- Warna: rerata, simpangan baku, dan histogram warna.
- Tekstur: wavelet Gabor, GLCM (*gray-level co-occurrence matrix*), dan BGLAM.
- Duri: fitur yang diturunkan dari duri pada permukaan tandan.

Pada rincian ini, BGLAM adalah fitur tekstur yang dipakai penulis sebagai kandidat terbaik. Makalah tidak menjelaskan rumus BGLAM secara terperinci.

Kinerja diukur dengan kurva ROC (*receiver operating characteristic*) dan nilai AUC (*area under the curve*). Garis dasar (*baseline*) yang dilaporkan memiliki AUC 92,3155%. Naskah menyebut tiga konfigurasi ROI dengan AUC sekitar 92,7% sampai 92,9%, tetapi label pada gambar dan teks tidak konsisten: teks menyebut ROI 300 × 300 dengan 92,7586% dan ROI 100 × 100 dengan 92,9067%, sedangkan label gambar memuat pasangan yang berbeda. Angka yang dapat dipakai adalah akurasi 93% untuk BGLAM dengan ANN dan waktu 0,40 detik. Makalah tidak melaporkan matriks kebingungan (*confusion matrix*) atau akurasi per kelas.

Penulis menyebut dua batas. Pertama, kecepatan dibatasi oleh model duri. Kedua, akurasi dibatasi oleh variasi fitur duri di dalam satu jenis TBS dan satu kelas yang sama.
