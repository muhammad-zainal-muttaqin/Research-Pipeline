# Estimation of Oil Content in Oil Palm Fresh Fruit Bunch by Its Surface Color

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `saetang2020estimation` |
| Judul asli | Estimation of Oil Content in Oil Palm Fresh Fruit Bunch by Its Surface Color |
| Penulis | Sae-Tang, Sutat |
| Tahun | 2020 |
| Venue | Proceedings 2020 15th International Joint Symposium on Artificial Intelligence and Natural Language Processing Isai Nlp 2020 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm, citrus |

## Tautan Akses
- PDF: [saetang2020estimation.pdf](../pdf/saetang2020estimation.pdf)
- DOI resmi: https://doi.org/10.1109/isai-nlp51646.2020.9376834

## Gambaran Umum

Penulis menyebut bahwa harga tandan buah segar (TBS) kelapa sawit bergantung pada kadar minyak, yang selama ini ditaksir ahli dari warna permukaan tandan. Penaksiran berbeda antarahli karena pengalaman berbeda. Analisis kimia lebih akurat tetapi memakan waktu. Tujuan kajian ini adalah memprediksi rasio minyak terhadap tandan (*oil-to-bunch*) dari citra permukaan tandan yang diambil dengan kamera ponsel.

Data berupa 394 tandan dari dua jenis sawit di Thailand, yaitu Nigrescene (196 tandan) dan Virescene (198 tandan), dengan tiga tahap kematangan (mentah, setengah matang, matang). Total ada 5.568 citra berukuran 1.328x747 piksel, diambil dari beberapa arah (depan, belakang, dan lainnya) dalam kotak berpencahayaan terkontrol dan dalam cahaya alami. Label kadar minyak berasal dari analisis laboratorium (ekstraksi Soxhlet pada mesokarp kering, lalu dikonversi ke persen minyak per tandan). Citra dalam kotak dibagi acak 70% latih dan 30% uji (*indoor1*). Bagian lain dari citra dalam kotak dipakai sebagai uji kedua (*indoor2*). Seluruh citra cahaya alami menjadi uji ketiga (*outdoor*). Cara pembentukan *indoor2* dan jumlah per bagian tidak disebut.

Tiga model dibandingkan. Regresi linear ganda (*multi linear regression*, MLR) menjadi acuan dasar. Jaringan saraf berlapis banyak (*multilayer perceptron*, MLP) memiliki satu lapisan masukan 646 simpul, enam lapisan tersembunyi, dan satu keluaran. Jaringan saraf konvolusi (*convolutional neural network*, CNN) dibangun dari nol dengan lima lapisan konvolusi, dua lapisan padat, dan masukan citra 256x256 dalam ruang warna L*a*b* dan HSV. Fitur MLR dan MLP berasal dari kanal a* dan b* pada 323 posisi dari pusat tandan.

Hasil diukur dengan *root mean square error* (RMSE). Pada data uji tak terlihat (*outdoor*), RMSE MLR adalah 10,97 (Nigrescene) dan 10,29 (Virescene), MLP 10,39 dan 10,13, CNN 7,90 dan 7,81. Pada *indoor1* MLP lebih baik daripada CNN (1,19 dan 0,66 berbanding 7,51 dan 3,39). Abstrak melaporkan rerata RMSE CNN 7,27 (Nigrescene) dan 4,83 (Virescene).

Keterbatasan yang dapat diperiksa: pembagian latih-uji dilakukan acak pada citra, tidak per tandan, dan beberapa citra dari tandan yang sama dihitung sebagai citra terpisah. Lokasi pengambilan citra cahaya alami tidak dijelaskan. Tidak ada deteksi tandan atau pencacahan buah. Tidak ada galat per kelas kematangan. Tidak ada uji kemaknaan statistik atau pengulangan.
