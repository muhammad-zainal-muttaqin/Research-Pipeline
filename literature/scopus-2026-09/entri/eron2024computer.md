# Computer Vision-Aided Intelligent Monitoring of Coffee: Towards Sustainable Coffee Production

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `eron2024computer` |
| Judul asli | Computer Vision-Aided Intelligent Monitoring of Coffee: Towards Sustainable Coffee Production |
| Penulis | Eron, Francisco; Noman, Muhammad; de Oliveira, Raphael Ricon; Chalfun-Junior, Antonio |
| Tahun | 2024 |
| Venue | Scientia Horticulturae |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | coffee |

## Tautan Akses
- PDF: [eron2024computer.pdf](../pdf/eron2024computer.pdf)
- DOI resmi: https://doi.org/10.1016/j.scienta.2024.112847

## Gambaran Umum

Penelitian ini bertujuan menyediakan sistem pemantauan kopi di lapangan berbasis visi komputer yang mampu menghitung buah, mengklasifikasikan kematangan, memperkirakan hasil panen, dan menilai kesehatan tanaman sebelum panen. Pemantauan manual bersifat padat karya, memakan waktu, dan rawan salah, terutama karena pembungaan yang tidak serempak menghasilkan pematangan buah yang tidak merata sehingga petani melakukan pemanenan bertahap. Mutu kopi sangat bergantung pada kematangan buah; buah hijau, terlalu matang, atau kering dalam hasil panen menurunkan mutu minuman, dan standar mutu mensyaratkan sekurang-kurangnya 98% buah matang penuh. Penulis mencatat bahwa teknologi sebelumnya untuk estimasi hasil kopi umumnya hanya bekerja saat panen, memakai peralatan mahal dan pemrosesan citra yang kompleks, atau memakai model lama, serta belum tersedia aplikasi telepon genggam untuk penghitungan dan estimasi hasil.

Data dikumpulkan dari sejumlah perkebunan kopi di Lavras dan sekitarnya, Minas Gerais, Brasil. Citra buah pada ranting diambil dengan berbagai kamera telepon genggam pada sudut dan jarak berbeda, mencakup seluruh tahap kematangan dari buah hijau sampai buah merah matang dan buah kering, serta kondisi rindang dan terkena cahaya matahari. Dari 406 citra, 324 citra berisi 33.717 buah dipakai untuk latih dan 82 citra berisi 10.094 buah untuk uji. Anotasi kotak pembatas dibuat manual dengan Label Studio merujuk pada skala Ságio (2009), lalu semua citra diubah menjadi 640×640 piksel dan diperbanyak dengan augmentasi *mosaic*. Latihan memakai YOLOv5, YOLOv6, dan YOLOv7 pada Google Colab dengan GPU Tesla T4, ukuran *batch* 16, dan 100 epoch; parameter lain memakai nilai bawaan. Metrik yang dipakai adalah presisi P = TP/(TP+FP), *recall* R = TP/(TP+FN), dan mAP@.5 sebagai rata-rata AP pada IoU 0,5. Tingkat kematangan dihitung sebagai persentase buah matang terhadap total buah, dan sisanya dinyatakan belum matang.

YOLOv7 dipilih karena unggul dalam tiga mode pengenalan, yaitu mono (semua buah), biner (mentah/matang), dan multikelas (hijau, hijau-kuning, merah, *raisin*, kering). Mekanisme semi-supervised yang diusulkan mempertahankan kotak pembatas hasil anotasi manual, tetapi menyerahkan penentuan kelas buah kepada model K-means. Buah hasil pemotongan citra diubah menjadi 28×28×3 piksel, diubah ke ruang warna LAB, dan kanal A serta B dipakai sebagai fitur; kanal L dibuang karena variasi pencahayaan dapat memihak klasifikasi berdasarkan bayang dan cahaya. Model K-means dengan jumlah klaster k dari 2 sampai 7 dilatih pada sekitar 36.000 buah yang dipilih secara acak, lalu PCA dipakai untuk memvisualisasikan batas antarklaster. Klaster yang dihasilkan mewakili warna yang menyerupai tahap kematangan, dan jumlah kelas empat ditetapkan sebagai yang paling optimal. Kategori hasil K-means dikorelasikan dengan kategori Moraes yang dipakai dalam anotasi manual agar urutannya sesuai dengan kematangan.

Pada data uji, YOLOv7 mencatat mAP@.5 sebesar 0,904 untuk mode mono dengan presisi 0,852 dan *recall* 0,871; 0,892 untuk mode biner dengan presisi 0,845 dan *recall* 0,852; serta 0,605 untuk mode multikelas dengan presisi 0,627 dan *recall* 0,682. YOLOv5 mencatat 0,885, 0,866, dan 0,555 pada ketiga mode, sedangkan YOLOv6 mencatat 0,898, 0,875, dan 0,556. Jumlah parameter berturut-turut adalah 36,9 juta untuk YOLOv7, 21,2 juta untuk YOLOv5, dan 35,7 juta untuk YOLOv6. Pada perbandingan metode anotasi, mode biner menghasilkan mAP@.5 0,89 untuk keduanya, baik supervised maupun semi-supervised, sedangkan mode multikelas dengan empat kelas menghasilkan 0,77 untuk semi-supervised berbanding 0,60 untuk supervised menurut teks dan 0,66 menurut keterangan gambar. Model juga diuji pada citra mentah di luar himpunan data dan dipakai untuk melacak pematangan buah selama 90 hari. Aplikasi CoffeApp dibangun dengan Flutter SDK memakai arsitektur *micro-service*, backend Python berbasis FastAPI, serta komunikasi REST API melalui HTTP, dan memiliki fungsi pengambilan citra, penghitungan buah, dan penentuan kelas.

Penulis menyatakan bahwa kategori yang dibentuk K-means hanya didasarkan pada warna dan tidak selalu sesuai dengan jenis atau varietas buah kopi, sehingga diperlukan analisis dan korelasi lanjutan untuk mengidentifikasi tahap kematangan yang diwakili tiap kategori. Kinerja YOLOv7 pada mode multikelas masih perlu ditingkatkan dan penambahan jumlah citra latih disarankan. Citra lapangan mengandung derau tertentu yang mencerminkan kondisi pengumpulan data sebenarnya dan menantang kemampuan generalisasi model. Penggabungan aplikasi dengan UAV serta pemanfaatan hasilnya untuk pengelolaan kebun, penentuan waktu panen, dan tindakan pascapanen disampaikan sebagai potensi pengembangan, bukan hasil yang diuji dalam kajian ini.
