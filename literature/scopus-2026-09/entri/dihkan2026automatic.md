# Automatic Kiwifruit Segmentation From Terrestrial LiDAR Point Clouds for Precision Agriculture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `dihkan2026automatic` |
| Judul asli | Automatic Kiwifruit Segmentation From Terrestrial LiDAR Point Clouds for Precision Agriculture |
| Penulis | Dihkan, Mustafa; Yildirim, Feride Secil; Karsli, Fevzi; Erbas, Gultekin |
| Tahun | 2026 |
| Venue | Transactions in GIS |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | kiwifruit |

## Tautan Akses
- PDF: [dihkan2026automatic.pdf](../pdf/dihkan2026automatic.pdf)
- DOI resmi: https://doi.org/10.1111/tgis.70347

## Gambaran Umum

Kajian ini membandingkan dua pengklasifikasi titik, *support vector machine* (SVM) dan *random forest* (RF), untuk memisahkan titik buah kiwi dari titik lain pada awan titik (*point cloud*) pohon kiwi yang dipindai dengan LiDAR terestris (TLS). Awan titik adalah kumpulan titik tiga dimensi hasil pemindaian laser, dan setiap titik dapat membawa nilai warna RGB serta fitur geometris turunan. Tujuan kajian adalah memberi label setiap titik sebagai kiwi atau bukan kiwi sebagai langkah awal sebelum buah dapat dihitung atau diukur.

Data yang dipakai adalah awan titik pohon kiwi yang sudah diberi label. Dari 13 fitur kandidat, *recursive feature elimination* berbasis LinearSVC menyisakan 7 fitur. Fitur tersebut mencakup ukuran bentuk lokal seperti *linearity*, *planarity*, *sphericity*, dan *curvature*, serta kepadatan lokal dan jarak *k-nearest neighbor*. Setelah pengklasifikasian titik, *DBSCAN* dipakai sebagai pascaproses untuk menghapus klaster kecil dan terisolasi. Kinerja diukur dengan *overall accuracy* (OA), *precision* (Pr), *recall* (Rc), dan F1-score pada tingkat titik.

Sebelum pascaproses, RF mencapai OA 91,9%, Pr 86,0%, Rc 51,8%, dan F1 64,7%. SVM mencapai OA 90,8%, Pr 75,3%, Rc 53,4%, dan F1 62,4%. Setelah DBSCAN, RF mencapai OA 92,4%, Pr 93,2%, Rc 50,5%, dan F1 65,5%; SVM mencapai OA 91,6%, Pr 84,2%, Rc 51,2%, dan F1 63,7%. Dengan demikian RF unggul pada OA dan precision, sedangkan recall keduanya berada di kisaran 50 sampai 53%. Pengaruh DBSCAN paling besar pada precision RF, yang naik dari 86,0% menjadi 93,2%, sementara recall turun sedikit.

Kajian ini tidak mengukur jumlah buah per pohon. Keluaran yang diuji adalah label titik, bukan jumlah klaster atau jumlah objek buah, sehingga hasilnya belum menjawab penghitungan. Teks juga menyatakan bahwa SVM lebih baik menjaga integritas buah sebagai satu klaster, sedangkan RF lebih baik membedakan kiwi dari cabang dan daun.

Batas utama kajian adalah recall yang rendah pada kedua model. Sekitar separuh titik kiwi tidak terdeteksi, sehingga jumlah buah yang diturunkan dari hasil ini akan kurang dari jumlah sebenarnya. Kajian ini juga memakai satu spesies, yaitu kiwi, dan pemindaian TLS yang mahal. Relevansinya untuk penghitungan buah berbasis citra RGB atau kamera kedalaman di kebun sawit belum diuji.
