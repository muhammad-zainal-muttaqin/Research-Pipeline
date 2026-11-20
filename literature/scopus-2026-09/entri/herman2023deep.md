# DEEP LEARNING WITH AUXILIARY LEARNING ATTENTION MECHANISM FOR OIL PALM FRUIT IMAGE RIPENESS CLASSIFICATION

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `herman2023deep` |
| Judul asli | DEEP LEARNING WITH AUXILIARY LEARNING ATTENTION MECHANISM FOR OIL PALM FRUIT IMAGE RIPENESS CLASSIFICATION |
| Penulis | Herman; others |
| Tahun | 2023 |
| Venue | Icic Express Letters |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [herman2023deep.pdf](../pdf/herman2023deep.pdf)
- DOI resmi: https://doi.org/10.24507/icicel.17.12.1303

## Gambaran Umum

Penelitian ini berangkat dari rendahnya akurasi dan keandalan model klasifikasi kematangan buah sawit yang tersedia, sehingga otomatisasi sortasi tandan buah segar belum meluas di industri. Penulis menilai pendekatan berbasis fitur warna buatan rentan terhadap perbedaan pencahayaan antara lingkungan nyata dan data latih. Tujuan penelitian adalah merancang modul mekanisme perhatian (*attention*) yang meningkatkan kinerja model klasifikasi citra berbasis pembelajaran mendalam untuk tandan buah sawit.

Model yang diusulkan bernama AuxNet dan memakai DenseNet (khususnya DenseNet121) sebagai jaringan utama. Modul yang ditambahkan disebut *Auxiliary Learning Attention Mechanism* (ALAM). Modul ini dipasang pada luaran setiap blok DenseNet, berupa konvolusi 3×3 dengan aktivasi Sigmoid yang menghasilkan tensor berukuran sama dengan masukan. Tensor perhatian dikalikan secara element-wise dengan masukan asli, lalu melalui *Global Average Pool* dan lapisan fully connected untuk klasifikasi. Perbedaannya dengan modul perhatian umum adalah luaran ALAM dialihkan ke pengklasifikasi bantu, bukan diteruskan ke lapisan berikutnya, sehingga gradien hanya melewati satu modul ALAM dan menghindari masalah gradien menghilang. Blok terakhir tidak memakai perhatian karena tidak ada blok sesudahnya.

Data terdiri atas 400 citra tandan buah sawit dalam tujuh kelas kematangan: BP (*Ripening*) 16, BM (*Raw*) 8, KM (*Less Ripped*) 64, MKM (*Almost Ripped*) 16, M (*Ripped*) 96, MM (*Perfectly Ripped*) 168, dan TM (*Excessively Ripped*) 32. Pembagian data adalah 64% latih (256 citra), 20% validasi (80 citra), dan 16% uji (64 citra). Seluruh model dilatih dengan augmentasi Ten Crop, yaitu lima crop (kiri atas, kanan atas, kiri bawah, kanan bawah, tengah) yang masing-masing dibalik secara horizontal. Model memakai bobot pralatih ImageNet dan tidak membekukan bobot. Piranti lunaknya PyTorch dengan GPU NVIDIA Tesla P100 dan P4. Konfigurasi pelatihan: learning rate 0,001, penurunan laju tiap 8 langkah, optimizer SGD, batch 8, dan 50 epoch.

Perbandingan dilakukan terhadap AlexNet, DenseNet standar, dan DenseNet dengan modul SE. Metrik yang dipakai adalah *Top-1 error rate* dan F1 Score, dengan hasil pada data uji sebagai berikut: AlexNet akurasi 0,77 dan F1 0,77; DenseNet akurasi 0,85 dan F1 0,85; DenseNet+SE akurasi 0,80 dan F1 0,81; AuxNet akurasi 0,87, presisi 0,88, recall 0,87, dan F1 0,87. Abstrak menyebut peningkatan 9,85% atas model pembelajaran mendalam terbaik sebelumnya, sedangkan simpulan menyebut kenaikan atas DenseNet sebesar 2% pada akurasi dan F1 serta 1% pada presisi dan recall. Nilai loss validasi terendah tercatat 0,9081 (AlexNet), 0,4467 (DenseNet), 0,8904 (DenseNet+SE), dan 2,4875 (AuxNet); penulis mengaitkan loss AuxNet yang lebih tinggi dengan empat lapisan fully connected yang dipakai saat backpropagasi.

Batasan yang dinyatakan penulis adalah saran untuk mengintegrasikan ALAM ke dalam mekanisme *self-attention* pada model berbasis Visual Transformer pada pekerjaan berikutnya. Penulis menjelaskan penurunan kinerja DenseNet+SE akibat gradien yang melewati beberapa fungsi softmax, tetapi tidak mencantumkan batasan lain dari hasil yang diperoleh. Kajian ini berfokus pada klasifikasi kematangan per citra dan tidak membahas penghitungan jumlah tandan atau asosiasi antarpandangan.
