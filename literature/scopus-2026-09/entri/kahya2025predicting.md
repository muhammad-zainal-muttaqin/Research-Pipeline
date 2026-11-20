# Predicting Grain Count and Weight of Grape Clusters by Image Processing with Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kahya2025predicting` |
| Judul asli | Predicting Grain Count and Weight of Grape Clusters by Image Processing with Deep Learning |
| Penulis | Kahya, Erhan |
| Tahun | 2025 |
| Venue | Applied Fruit Science |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [kahya2025predicting.pdf](../pdf/kahya2025predicting.pdf)
- DOI resmi: https://doi.org/10.1007/s10341-025-01333-7

## Gambaran Umum

Kajian ini bertujuan mengevaluasi efektivitas teknik *deep learning* dalam memprediksi jumlah dan berat tandan anggur dari citra. Masalah yang diangkat adalah pencacahan tandan secara manual di kebun. Cara ini memerlukan banyak tenaga kerja dan sulit dilakukan karena oklusi serta sebaran buah yang rapat di lapangan. Penulis ingin menentukan model deteksi yang paling sesuai untuk memperkirakan jumlah tandan. Hasilnya diharapkan membantu petani mengambil keputusan berbasis data dalam pengelolaan kebun anggur.

Data terdiri atas 120 foto yang diambil langsung di lapangan pada Juni 2024 dan 540 citra dari berbagai sumber internet. Foto lapangan diambil dengan kamera Nikon D3100 berresolusi 1920 × 1080 piksel, dalam format JPEG dengan kualitas maksimum. Jarak pemotretan 1,0 meter dari tanaman anggur. Citra internet dan lapangan dibagi dengan rasio 8:2. Dari citra internet, 432 untuk data latih dan 108 untuk data uji. Dari foto lapangan, 72 untuk data latih dan 18 untuk data uji. Data latih akhir berjumlah 1.730 citra setelah augmentasi. Augmentasi memakai empat kombinasi acak, yaitu pembalikan horizontal dan vertikal, penyesuaian kontras, penyesuaian kecerahan, dan derau Gauss. Penulis juga menyebut rotasi dan penskalaan sebagai teknik yang digunakan.

Metode yang digunakan adalah YOLOv8, yang didahului praproses berupa pengubahan ukuran dan normalisasi citra. Segmentasi berbasis warna dan deteksi tepi dipakai untuk memisahkan butir dan tandan. Penulis menguji lima ukuran model, yaitu *nano*, *small*, *medium*, *large*, dan *xlarge*. Hasilnya, YOLOv8L memiliki tingkat akurasi tertinggi dan mengungguli model lain pada metrik mAP50-95, *precision*, dan *recall*. Penulis menyatakan bahwa augmentasi data meningkatkan akurasi model dan memperpendek waktu latih, serta mengurangi risiko *overfitting*. Model untuk prediksi berat tandan juga disebut berpotensi dipakai dalam pertanian, tetapi kajian ini tidak mencantumkan angka evaluasi untuk bagian berat tersebut dalam bagian yang terbaca.

Penulis menyebut kebutuhan komputasi algoritma yang canggih sebagai hal yang dapat membatasi penggunaan model di lingkungan pertanian tertentu. Penulis juga menyebut akses terhadap data, interpretabilitas model, dan variabilitas lingkungan sebagai hambatan penerapan yang luas. Penulis berencana meneliti pengaruh kondisi pencahayaan dan sudut pengambilan gambar terhadap ketangguhan model, serta ukuran dan keterampilan generalisasi data.
