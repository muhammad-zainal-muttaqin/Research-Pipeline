# Estimation of fruit load in mango orchards: tree sampling considerations and use of machine vision and satellite imagery

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `anderson2019estimation` |
| Judul asli | Estimation of fruit load in mango orchards: tree sampling considerations and use of machine vision and satellite imagery |
| Penulis | Anderson, N. T.; Underwood, J. P.; Rahman, M. M.; Robson, A.; Walsh, K. B. |
| Tahun | 2019 |
| Venue | Precision Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | mango |

## Tautan Akses
- PDF: [anderson2019estimation.pdf](../pdf/anderson2019estimation.pdf)
- DOI resmi: https://doi.org/10.1007/s11119-018-9614-1

## Gambaran Umum

Penulis menyebut bahwa prakiraan hasil mangga praktik komersial terbaik memakai hitung manual pada hingga 5% pohon per blok. Variasi jumlah buah antarpohon besar (koefisien variasi 27 sampai 93% pada sepuluh kebun), sehingga cara itu dinilai tidak andal. Kajian membandingkan tiga cara menaksir beban buah kebun: hitung sampel pohon, *machine vision* di lapangan, dan korelasi dengan indeks spektral dari citra satelit.

Data: sepuluh kebun mangga di Australia pada musim 2016/17. Kebun utama (kultivar Calypso, dekat Bundaberg) berisi 469 pohon yang dihitung. Di tiap kebun, 18 pohon dipanen dan buahnya dihitung sebagai acuan. Hitung visual manual dilakukan pada 191 pohon di kebun utama. Citra satelit WorldView-3 beresolusi 1,2 m diambil 23 September 2016. Citra RGB dan LiDAR dari platform darat diambil Desember 2016.

Metode *machine vision* memakai *Faster R-CNN* (detektor objek dua tahap) yang dilatih pada lebih dari 1500 citra buah pada musim sebelumnya. Pada tampilan *multi-view*, buah dilacak antarbingkai pada 25 citra per sisi pohon, dan deteksi dikaitkan ke pohon lewat topeng LiDAR. Hitungan dikoreksi dengan kemiringan regresi terhadap 18 pohon kalibrasi. Metode satelit meregresikan jumlah buah terhadap 18 indeks vegetasi.

Hasil: pada 18 pohon, *multi-view* menghasilkan R2 = 0,97 dan RMSE = 14,8 buah/pohon terhadap hitung panen. Metode satelit menghasilkan R2 = 0,66 dan RMSE = 56,1 buah/pohon. Panen sebenarnya 56.720 buah. Estimasi hitung manual 5% pohon sebesar 47.955, *machine vision* 53.520 (SD = 1960), dan satelit 51.944 (SD = 26.300). Hitung 5% pohon memberi galat persentase 31%, dan 157 pohon dibutuhkan untuk galat 10%.

Keterbatasan yang dapat diperiksa: validasi *machine vision* hanya pada 18 pohon di satu kebun, yang juga dipakai mengoreksi kemiringan. Hanya satu kultivar pada kebun utama. Detektor tidak dilatih ulang untuk musim ini. Teks tidak menyebut pembagian latih dan uji untuk detektor selain citra musim sebelumnya.
