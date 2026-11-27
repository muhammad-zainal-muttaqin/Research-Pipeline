# Fruit yield estimation using image analysis is also about correcting the number of detections

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sarron2023fruit` |
| Judul asli | Fruit yield estimation using image analysis is also about correcting the number of detections |
| Penulis | Sarron, J.; Tresch, L.; Bendahou, H.; Koffi, J.M.K.; Avlessi, N.; San\'e, C.A.B.; Faye, E.; Lavarenne, J. |
| Tahun | 2023 |
| Venue | Acta Horticulturae |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [sarron2023fruit.pdf](../pdf/sarron2023fruit.pdf)
- DOI resmi: https://doi.org/10.17660/actahortic.2023.1360.42

## Gambaran Umum

Kajian ini (Acta Horticulturae 1360, 2023) menguji model koreksi yang mengubah jumlah deteksi buah pada citra menjadi jumlah buah sebenarnya per pohon mangga. Satu-satunya masukan model adalah jumlah deteksi.

Data mencakup 325 pohon mangga 'Kent' dari 27 kebun di Senegal dan Pantai Gading, dengan sistem tanam dari monokultur sampai kebun campuran. Setiap pohon difoto dari dua sisi berlawanan, dua hari sampai dua minggu sebelum panen. Semua buah di pohon dihitung oleh dua pakar sebagai hitungan acuan. Buah dideteksi YOLOv5 yang dilatih pada 736 citra beranotasi (48.500 buah). Jumlah deteksi pohon adalah jumlah objek terdeteksi pada kedua citra.

Model dikalibrasi pada 80% pohon yang dipilih acak di setiap kebun dan divalidasi pada 20% sisanya, sehingga pohon validasi berasal dari kebun yang sama. Menurut Tabel 2, regresi linear sederhana memberi R2 0,34 dan NRMSE validasi 20,1%, sedangkan regresi dengan kovariat wilayah dan sistem tanam setelah transformasi akar kuadrat memberi R2 0,77 dan NRMSE 11,5%. Abstrak menulis R2 0,66 dan NRMSE 11%, angka yang tidak tercantum di tabel. Transformasi akar kuadrat pada kedua hitungan diperlukan agar sisaan memenuhi asumsi normalitas dan homoskedastisitas. Model efek campuran dengan kebun sebagai efek acak memberi kinerja serupa, tetapi tidak memenuhi asumsi regresi.

Penggabungan dua sisi tidak menautkan buah yang sama. Buah yang terlihat dari kedua sisi dan buah yang tertutup sama-sama dikoreksi lewat regresi. Hasil kajian menunjukkan bahwa faktor koreksi berbeda antarwilayah dan antarsistem tanam, meskipun kultivar dan tahap buahnya sama.
