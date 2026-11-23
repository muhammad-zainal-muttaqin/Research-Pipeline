# Automating mango crop yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `payne2016automating` |
| Judul asli | Automating mango crop yield estimation |
| Penulis | Payne, A.B.; Walsh, K.B.; Subedi, P.P. |
| Tahun | 2016 |
| Venue | Acta Horticulturae |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | mango |

## Tautan Akses
- PDF: [payne2016automating.pdf](../pdf/payne2016automating.pdf)
- DOI resmi: https://doi.org/10.17660/actahortic.2016.1130.87

## Gambaran Umum

Penulis menilai beberapa teknologi pencitraan untuk menentukan beban buah mangga pada pohon, dengan preferensi pada citra RGB. Masalah yang disebut: deteksi buah pada pohon sulit karena lingkungan lapangan tidak terstruktur dan atribut buah serta latar bervariasi. Penulis juga menekankan bahwa banyak makalah hanya melaporkan hasil kalibrasi, yang menurut mereka terlalu optimistis, sehingga hasil pada set validasi diperlukan.

Citra RGB mangga pada pohon dikumpulkan di kebun pada malam hari antara 2010 dan 2013, mencakup empat musim (abstrak menyebut lima musim). Satu set siang hari berisi 555 buah. Set kalibrasi berisi 18 pohon, 20 citra, dan 705 buah. Delapan set validasi berasal dari malam, musim, kebun, jumlah lampu sorot, dan jarak kamera yang berbeda; contohnya Validation 2 berisi 74 pohon, 74 citra, dan 3148 buah. Jumlah buah dihitung tangan. Pada tahap awal 2009, citra termal, hiperspektral, dan RGB juga dicoba.

Metode yang dibandingkan adalah tapis warna dan tekstur (Payne dkk. 2013), klasifikasi piksel *K-nearest neighbour* dan *SVM* (*support vector machine*, pengklasifikasi pemisah dua kelas) disertai model bentuk elips (Linker dkk. 2012), dan SVM dengan segmentasi *superpixel* serta pengelompokan fitur *SIFT* (Qureshi dkk. 2014). Parameter dioptimalkan hanya pada set kalibrasi. Pemotretan malam dengan lampu sorot dipilih untuk mengurangi pengaruh cahaya matahari.

Pada set Validation 2, ketiga metode memberi R2 0,63, 0,67, dan 0,57, RMSEP 11,0, 9,1, dan 11,3, serta F1 0,76 untuk metode Linker dkk. dibanding 0,67 dan 0,68 untuk dua lainnya. Hasil terbaik diperoleh metode Linker dkk. pada set itu, tetapi metode lain lebih baik pada set lain. Tingkat identifikasi positif benar mencapai hingga 80%. Buah terlewat (negatif palsu) akibat oklusi tandan mencapai 10 sampai 39% dari buah acuan pada beberapa set.

Keterbatasan: citra tunggal tanpa penautan antarpandang, sehingga buah yang terhalang daun atau tangkai tetap terlewat. Penulis menyebut hasil belum cukup untuk kelayakan komersial. Video dan 3D tidak diuji. Galat berbeda tiap musim, misalnya ngengat dan pita merah menimbulkan positif palsu. Hasil antarmetode dibandingkan pada sampel terbatas, dan tabel kesalahan dihitung dari 10 citra saja.
