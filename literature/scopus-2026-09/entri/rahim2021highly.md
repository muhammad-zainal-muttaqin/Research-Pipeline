# Highly Accurate Tomato Maturity Recognition: Combining Deep Instance Segmentation, Data Synthesis and Color Analysis

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `rahim2021highly` |
| Judul asli | Highly Accurate Tomato Maturity Recognition: Combining Deep Instance Segmentation, Data Synthesis and Color Analysis |
| Penulis | Fawzia Rahim, Umme; Mineno, Hiroshi |
| Tahun | 2021 |
| Venue | ACM International Conference Proceeding Series |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [rahim2021highly.pdf](../pdf/rahim2021highly.pdf)
- DOI resmi: https://doi.org/10.1145/3508259.3508262

## Gambaran Umum

Kajian ini membahas pengenalan tingkat kematangan dan pencacahan buah tomat dari citra pada beberapa tahap pertumbuhan. Penulis menilai informasi ini penting untuk pengelolaan budidaya, prediksi hasil jangka panjang, dan panen robotik. Tantangan utamanya adalah keragaman bentuk, ukuran, dan warna tomat. Oklusi dan tumpang tindih pada lingkungan pertanian yang tidak terstruktur juga menyulitkan pengenalan. Di sisi lain, jaringan saraf memerlukan data berlabel dalam jumlah besar. Pelabelan manual mahal dan memakan waktu, sehingga penulis mengusulkan pembelajaran dari data sintetis.

Data acuan terdiri atas 100 citra RGB beresolusi tinggi tomat yang dibudidayakan di rumah kaca. Citra ini dilengkapi anotasi per piksel dari *Laboro Tomato dataset*. Dari data tersebut, 60 citra berisi tomat berukuran besar dan 40 citra berisi tomat berukuran kecil dipilih untuk menjaga keseimbangan. Sekitar 1.100 objek tomat diekstraksi, lalu dipilih objek yang tampak utuh atau hampir utuh. Objek kemudian diskalakan acak antara 48 dan 200 piksel hingga terkumpul 2.000 citra objek latar depan. Objek dibagi ke dalam lima kategori: Big 250, Small(L) 400, Small(S) 450, Little(L) 450, dan Little(S) 450. Latar belakang berupa 100 foto tanaman tomat di rumah kaca di Jepang. Setiap latar diubah ukurannya menjadi 600 × 800 piksel dan dicerminkan untuk menambah jumlahnya.

Metode yang diusulkan membuat citra kebun sintetis berdasarkan aturan tandan tomat. Ukuran dan jumlah tomat dalam satu tandan berkorelasi. Buah yang lebih besar berada di bagian atas tandan, dan buah yang lebih kecil di bawah. Citra sintetis ini dipakai melatih *Mask R-CNN* untuk segmentasi instans. Hasil segmentasi pada data uji nyata mencapai *average precision* maksimum 92,1% dan *recall* 91,4%. Deteksi dinyatakan benar bila nilai *intersection-over-union* antara masker kebenaran dasar dan masker prediksi lebih dari 0,5. Tahap berikutnya mengklasifikasikan tingkat kematangan setiap objek dengan ambang warna pada ruang HSV. Objek dikategorikan matang penuh bila warna merahnya 90% atau lebih. Objek setengah matang bila warna merah atau jingga 30 sampai 89%. Sisanya dianggap hijau. Penulis melaporkan akurasi pencacahan yang tinggi untuk tiga tahap: hijau, setengah matang, dan matang penuh.

Kajian ini juga membahas kesenjangan antara data sintetis dan data dunia nyata. Penulis merujuk pada adaptasi domain dan *domain randomization* sebagai cara menjembatani kesenjangan tersebut. Pendekatan sintesis dianggap mampu menghasilkan data latih yang nyaris tak terbatas, dengan anotasi yang diperoleh otomatis. Dengan demikian, pelabelan manual dapat dikurangi. Penulis menempatkan kontribusinya pada gabungan tiga komponen: segmentasi instans, sintesis data, dan analisis warna untuk pencacahan berbasis tahap kematangan.
