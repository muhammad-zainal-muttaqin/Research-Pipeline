# AI-Based Ripeness Grading for Oil Palm Fresh Fruit Bunch in Smart Crane Grabber

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `harsawardana2020ai` |
| Judul asli | AI-Based Ripeness Grading for Oil Palm Fresh Fruit Bunch in Smart Crane Grabber |
| Penulis | Harsawardana; Rahutomo, Reza; Mahesworo, Bharuno; Cenggoro, Tjeng Wawan; Budiarto, Arif; Suparyanto, Teddy; Surya Atmaja, Don Bosco; Samoedro, Bayu; Pardamean, Bens |
| Tahun | 2020 |
| Venue | Iop Conference Series Earth and Environmental Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [harsawardana2020ai.pdf](../pdf/harsawardana2020ai.pdf)
- DOI resmi: https://doi.org/10.1088/1755-1315/426/1/012147

## Gambaran Umum

Kajian ini membangun sistem kecerdasan buatan untuk mengklasifikasikan tingkat kematangan tandan buah segar (TBS) kelapa sawit dari citra, lalu mengintegrasikannya ke alat pemanen *smart crane grabber*. Tujuannya membantu proses panen dan pengangkutan buah. Data yang dipakai kecil: 400 citra dari 50 tandan, masing-masing difoto dari delapan sudut, dengan tujuh kelas kematangan (U1, U2, AR, R1, R2, O1, O2). Citra diubah ukurannya dari 3264 × 2448 piksel menjadi 224 × 224 piksel, lalu dibagi 60:40 untuk latih dan validasi.

Model yang digunakan adalah ResNet152, jaringan saraf konvolusional (*CNN*) dengan 152 lapisan. Model dilatih dengan optimasi SGD bermomentum dan penurunan laju belajar bertahap. Augmentasi memakai TenCrop, yaitu sepuluh potongan citra yang terdiri atas lima potongan dan versi cerminnya. Pelatihan dilakukan pada GPU NVIDIA Tesla P100, sedangkan pemrosesan dijalankan pada perangkat Jetson TX2. Hasil terbaik pada set validasi adalah akurasi 71,34%. Penulis menyatakan angka ini dicapai dengan hanya 400 citra sebagai data latih awal.

Hasil per kelas menunjukkan selisih besar. F1-score tertinggi pada U2 (85,71%) dan U1 (80,00%), sedangkan AR (44,44%) dan O2 (23,80%) terendah. Penulis menafsirkan selisih antara presisi dan recall di hampir semua kelas sebagai tanda *overfitting*. U1, AR, R2, dan O2 memiliki recall lebih tinggi daripada presisi, sehingga banyak kesalahan positif palsu. U2, R1, dan O1 memiliki presisi lebih tinggi, sehingga banyak kesalahan negatif palsu. Angka ini hanya dari set validasi; penulis tidak melaporkan uji pada set terpisah.

Kesimpulan penulis menyatakan sistem dapat diintegrasikan ke smart crane grabber, tetapi *overfitting* harus diatasi lebih dahulu. Penulis mengusulkan dua jalan: mengumpulkan data dengan distribusi kelas yang seimbang, atau mengembangkan model yang tahan terhadap data tidak seimbang.
