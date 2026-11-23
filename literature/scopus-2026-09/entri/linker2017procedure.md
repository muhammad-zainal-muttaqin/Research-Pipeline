# A procedure for estimating the number of green mature apples in night-time orchard images using light distribution and its application to yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `linker2017procedure` |
| Judul asli | A procedure for estimating the number of green mature apples in night-time orchard images using light distribution and its application to yield estimation |
| Penulis | Linker, Raphael |
| Tahun | 2017 |
| Venue | Precision Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [linker2017procedure.pdf](../pdf/linker2017procedure.pdf)
- DOI resmi: https://doi.org/10.1007/s11119-016-9467-4

## Gambaran Umum

Penelitian ini mencacah apel hijau matang pada citra kebun yang diambil malam hari dengan penerangan buatan, lalu memakai hitungan itu untuk mengestimasi hasil per pohon. Penulis menyebut bahwa estimasi hasil di kebun masih dilakukan dengan inspeksi visual pada sedikit pohon. Cara ini lambat dan rawan galat. Kebun Israel yang diteliti memiliki pohon besar dengan beban buah tinggi (sasaran sekitar 300 sampai 350 buah per pohon), sehingga banyak buah tidak terlihat kamera.

Data berasal dari kebun apel 'Golden Delicious' di Matityahu Research Station, Israel utara. Ada empat set data: 2013 (156 citra dari 26 pohon), 17 Juli dan 5 Agustus 2014 (258 citra dari 43 pohon, dari dua sisi pohon, pohon yang sama pada kedua malam), dan 13 Agustus 2015 (156 citra dari 52 pohon, dari satu sisi). Setiap sisi pohon dipotret oleh tiga kamera pada tiga ketinggian tetap. Jumlah buah yang terlihat di setiap citra ditentukan dengan inspeksi visual. Setiap pohon dipanen sendiri pada akhir musim sebagai acuan hasil, kecuali tiga pohon pada 2013 yang hasilnya tidak tercatat.

Deteksi memanfaatkan pola cahaya pada apel: intensitas yang tertangkap kamera menurun dari titik pantulan spekular ke arah tepi buah. Citra diubah menjadi beberapa citra biner dengan rentang ambang intensitas, lalu transformasi Hough lingkaran (*circular Hough transform*) mencari lingkaran pada setiap citra biner. Pusat lingkaran yang berdekatan disatukan sebagai lingkaran konsentris, dan kelompok dengan cukup banyak lingkaran serta skor cukup tinggi dianggap apel. Parameter dikalibrasi per set data dengan algoritma genetika pada 12 citra acak. Hitungan dari dua sampai enam citra per pohon (beberapa ketinggian, satu atau dua sisi) digabung dalam model regresi linear berganda untuk mengestimasi hasil pohon, tanpa menautkan buah antarcitra.

Pada tingkat citra, selisih antara jumlah apel terestimasi dan hitungan visual kurang dari 1% untuk tiga set data dan 6% untuk satu set data. Pada 12 citra kalibrasi dan 12 citra tambahan, positif palsu 1 sampai 2% dan buah terlewat sekitar 10% untuk set 2013, sedangkan pada set lain positif palsu sekitar 7% dan buah terlewat sekitar 33%. Untuk 2014 dan 2015, model dikalibrasi dengan 20 pohon acak dan divalidasi pada pohon sisanya, diulang sepuluh kali. Estimasi hasil model terbaik berada dalam 10% dari hasil sebenarnya, tetapi simpangan baku galat estimasi sekitar 26 sampai 37% dari rata-rata hasil pohon (sekitar 500 buah per pohon pada Juli 2014). Model dengan tiga kamera hanya sedikit lebih baik daripada dua kamera, dan citra dari satu sisi pohon tidak memperburuk hasil secara nyata.

Keterbatasan yang dapat diperiksa dari teks: set 2013 terlalu kecil untuk dibagi menjadi data kalibrasi dan validasi, sehingga modelnya dibuat dari seluruh data dan hanya menunjukkan kelayakan. Penggabungan antarcitra bersifat statistik; buah yang sama dapat terhitung di beberapa citra, dan model regresi yang menanggung koreksinya. Penulis menyatakan bahwa ketelitian estimasi per pohon belum cukup.
