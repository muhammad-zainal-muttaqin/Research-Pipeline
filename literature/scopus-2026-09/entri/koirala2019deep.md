# Deep learning for real-time fruit detection and orchard fruit load estimation: benchmarking of ‘MangoYOLO’

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `koirala2019deep` |
| Judul asli | Deep learning for real-time fruit detection and orchard fruit load estimation: benchmarking of ‘MangoYOLO’ |
| Penulis | Koirala, A.; Walsh, K. B.; Wang, Z.; McCarthy, C. |
| Tahun | 2019 |
| Venue | Precision Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | mango |

## Tautan Akses
- PDF: [koirala2019deep.pdf](../pdf/koirala2019deep.pdf)
- DOI resmi: https://doi.org/10.1007/s11119-019-09642-0

## Gambaran Umum

Penelitian ini membandingkan enam arsitektur *deep learning* untuk mendeteksi buah mangga pada citra tajuk pohon dan mengembangkan arsitektur baru, MangoYOLO. Penulis menyebut taksiran hasil panen manual memakan waktu, padat tenaga, dan tidak akurat. Target penulis adalah pemrosesan di lapangan dalam 500 ms per citra dan taksiran hasil dalam 15% dari hitung panen di tempat pengemasan.

Citra diambil malam hari dari kendaraan kebun yang melaju sekitar 6 km/jam, memakai kamera RGB 5 MP dan lampu LED 720 W, di lima kebun mangga. Setiap pohon dicitrakan dari dua sisi berlawanan (*dual-view*). Total 1.515 citra pohon. Himpunan berlabel terdiri atas 1.300 ubin latih, 130 validasi, dan 300 uji. Label kotak dibuat tangan dengan alat labelImg. Pada tiap kebun, sekitar 18 pohon contoh dipanen tangan untuk mendapat hitungan acuan.

Enam arsitektur yang dibandingkan adalah Faster R-CNN (VGG dan ZF; dua tahap, usulan wilayah lalu klasifikasi), YOLOv3, YOLOv2, YOLOv2 (tiny), dan SSD (satu tahap, prediksi langsung dalam satu lintasan jaringan). MangoYOLO menggabungkan fitur YOLOv3 dan YOLOv2 (tiny). Tiga varian dilatih dari awal (s), dengan pralatih pada COCO (pt), dan dengan set latih siang hari kajian terdahulu (bu). Untuk taksiran hasil kebun, hitungan mesin dari kedua sisi pohon dikalikan faktor koreksi buah tersembunyi, yaitu rasio hitung tangan pada citra kedua sisi terhadap hitung panen pohon contoh.

MangoYOLO(pt) memperoleh F1 0,968 dan *average precision* 0,983 pada set uji terpisah dari set latih, dengan 8 ms per ubin 512x512 dan 70 ms per citra penuh 2.048x2.048. MangoYOLO(bu) memperoleh F1 0,89 pada set data siang hari. Faktor koreksi per kebun A sampai E berturut-turut 1,69, 1,63, 2,43, 1,05, dan 1,32. Taksiran hasil kebun berbeda 4,6 sampai 15,2% dari hitung tempat pengemasan, dengan galat persentase gabungan 8 sampai 24%.

Keterbatasan yang tertera: satu faktor koreksi dari sekitar 18 pohon dipakai untuk seluruh kebun dan simpangan bakunya besar. Pada kebun D yang berpohon kecil, buah yang sama terlihat dari kedua sisi sehingga terhitung ganda. Pohon dengan tajuk lebat menyembunyikan buah dari kedua sisi. Buah yang sama tidak ditautkan antarcitra. Penulis menyarankan penyaringan depth atau pelacakan sebagai pekerjaan lanjutan. Pembagian latih dan uji per pohon tidak disebut.
