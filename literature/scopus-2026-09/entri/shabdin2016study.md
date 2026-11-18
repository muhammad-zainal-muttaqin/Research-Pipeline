# A study on the oil palm fresh fruit bunch (FFB) ripeness detection by using Hue, Saturation and Intensity (HSI) approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `shabdin2016study` |
| Judul asli | A study on the oil palm fresh fruit bunch (FFB) ripeness detection by using Hue, Saturation and Intensity (HSI) approach |
| Penulis | Shabdin, Muhammad Kashfi; Shariff, Abdul Rashid Mohamed; Johari, Mohd Nazrul Azlan; Saat, Nor Kamilah; Abbas, Zulkifly |
| Tahun | 2016 |
| Venue | Iop Conference Series Earth and Environmental Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [shabdin2016study.pdf](../pdf/shabdin2016study.pdf)
- DOI resmi: https://doi.org/10.1088/1755-1315/37/1/012039

## Gambaran Umum

Penelitian ini menguji penggunaan model warna *Hue, Saturation and Intensity* (HSI) untuk menentukan tingkat kematangan tandan buah segar (TBS) kelapa sawit dalam sistem penggolongan mutu otomatis. Penulis menyatakan bahwa penilaian mutu secara visual oleh manusia bersifat tidak konsisten, kurang tepat, melelahkan, dan memakan waktu, sehingga perlu digantikan dengan teknik penglihatan mesin. Ruang lingkup dibatasi pada dua kategori, yakni kurang matang (*underipe*) dan matang (*ripe*), karena keduanya paling sulit dibedakan secara fisik dan paling menentukan mutu serta rendemen minyak. Kategori terlalu matang tidak menjadi fokus karena lebih mudah dibedakan dan tetap diolah bersama buah matang.

Datanya berupa 60 TBS varietas *Elaeis guineensis* (subspesies Nigrescens) dari Pertubuhan Peladang Salak Tinggi, Sepang, Malaysia, dengan 30 tandan per kategori. Kategori ditetapkan lebih dulu oleh petugas dan inspektor pabrik sesuai standar Malaysian Palm Oil Board, yaitu *underipe* jika buah yang rontok 1–9% dan *ripe* jika 10–50%. TBS ditempatkan dalam mesin penggolong dan citra diambil dari samping dengan kamera GigE pada area sekitar 100 cm × 100 cm. Lingkungan pengambilan citra dibuat tertutup agar cahaya luar tidak mengganggu.

Mekanisme pengolahan mencakup penghapusan latar belakang dengan ENVI classic, ekstraksi nilai RGB dengan MATLAB, lalu konversi ke nilai HSI. Hue menyatakan panjang gelombang puncak, saturasi menyatakan lebar sebaran intensitas terhadap panjang gelombang, sedangkan intensitas menyatakan kekuatan berkas cahaya. Nilai HSI dianalisis dengan dua cara. Analisis pertama memakai WEKA 3.6 dengan validasi silang dan regresi linear, yang menguji enam kombinasi peubah. Analisis kedua memakai jaringan saraf tiruan (*Artificial Neural Network*, ANN) dengan data latih dan data uji; keluaran 1 ditetapkan sebagai *underipe* dan keluaran 2 sebagai *ripe*.

Pada analisis WEKA, akurasi untuk kombinasi kategori-H sebesar 17%, kategori-S 25%, kategori-I 34%, kategori-H,S 18%, kategori-S,I 45%, dan kategori-H,I 20%. Kombinasi saturasi dan intensitas memberi hasil tertinggi, dengan galat absolut rata-rata 38% dan galat kuadrat rata-rata akar 44%; secara keseluruhan, regresi linear menghasilkan akurasi rata-rata 45%. Analisis ANN memberi nilai R sebesar 0,8 pada data latih, 0,99 pada validasi dan pengujian, serta 0,85 secara keseluruhan. Dari 20 sampel uji, akurasi untuk *underipe* 60% (empat klasifikasi salah) dan untuk *ripe* 80% (dua klasifikasi salah), sehingga akurasi keseluruhan 70%. Penulis menyatakan keterbatasan utama pada berkas cahaya berintensitas rendah di lingkungan tertutup, yang menghasilkan berkas tidak jenuh dan tidak monokromatik sehingga menurunkan mutu citra. Penambahan sampel dan peningkatan iluminasi diusulkan, tetapi berisiko memasukkan derau; pengujian dengan himpunan data lebih besar masih direncanakan.

