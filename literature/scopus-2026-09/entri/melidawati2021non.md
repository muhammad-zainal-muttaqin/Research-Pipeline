# Non destructive evaluation quality of oil palm fresh fruit bunch (FFB) (Elaeis guineensis Jack) based on optical properties using artificial neural network (ANN)

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `melidawati2021non` |
| Judul asli | Non destructive evaluation quality of oil palm fresh fruit bunch (FFB) (Elaeis guineensis Jack) based on optical properties using artificial neural network (ANN) |
| Penulis | Melidawati; Cherie, D; Fahmy, K; Makky, M |
| Tahun | 2021 |
| Venue | Iop Conference Series Earth and Environmental Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [melidawati2021non.pdf](../pdf/melidawati2021non.pdf)
- DOI resmi: https://doi.org/10.1088/1755-1315/644/1/012032

## Gambaran Umum

Studi ini menguji apakah citra kamera ponsel dapat memperkirakan kadar minyak tandan buah segar (TBS) kelapa sawit. Penelitian dilakukan pada varietas Tenera di Kabupaten Sijunjung, dengan tandan dikelompokkan ke dalam lima kelas umur setelah antesis (*days after anthesis*, DAA). Kadar minyak diukur dengan ekstraksi soxhlet sebagai nilai acuan, lalu dipasangkan dengan fitur optik dari citra untuk melatih model.

Citra direkam dengan kamera ponsel beresolusi minimal 25 megapiksel pada jarak 3 sampai 12 meter, dengan intensitas cahaya antara 303 dan 1537 lux. Fitur optik diambil dari citra RGB dan diolah menjadi masukan 26 faktor. Data dibagi 70% untuk kalibrasi dan 30% untuk validasi. Model yang dipakai adalah jaringan saraf tiruan multilayer perceptron (JST-MLP, *multilayer perceptron*), yaitu jaringan yang memetakan masukan ke keluaran melalui lapisan tersembunyi.

Hasil utama berupa kurva kadar minyak menurut umur tandan. Kadar minyak terendah 11,50% tercatat pada 110 sampai 130 DAA. Kadar tertinggi 24,44% tercatat pada 171 sampai 190 DAA, dan 23,44% pada 191 sampai 200 DAA. Nilai R² kalibrasi 0,6934 dan validasi 0,7211 ditampilkan pada Gambar 4. Penulis menilai kedua nilai itu cukup tinggi untuk menyebut model layak.

Dari sisi metode, studi ini memprediksi satu nilai kadar minyak per tandan dari citra tunggal, dengan kelas umur sebagai pengelompokan. Ia tidak menghitung jumlah tandan, tidak mendeteksi tandan secara terpisah dalam pohon, dan tidak memakai informasi kedalaman atau banyak pandang.

Validasi hanya memakai satu varietas dan satu lokasi, dengan 30% data untuk pengujian. Bagian kesimpulan tidak menyebut keterbatasan model maupun perbandingan dengan metode lain. Naskah tidak memuat sensitivitas terhadap jarak dan pencahayaan, meskipun rentang keduanya dilaporkan di bagian metode.
