# Design, development, and performance evaluation of a robot for yield estimation of kiwifruit

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `massah2021design` |
| Judul asli | Design, development, and performance evaluation of a robot for yield estimation of kiwifruit |
| Penulis | Massah, Jafar; Asefpour Vakilian, Keyvan; Shabanian, Mostafa; Shariatmadari, Seyed Mehdi |
| Tahun | 2021 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | kiwifruit |

## Tautan Akses
- PDF: [massah2021design.pdf](../pdf/massah2021design.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2021.106132

## Gambaran Umum

Studi Massah dan rekan (2021) membahas estimasi hasil kiwi dari citra yang diambil robot bergerak di kebun. Kamera CCD dipasang menghadap ke atas pada robot, sehingga setiap citra memuat tandan atau buah dari satu pandang. Penelitian ini membandingkan metode klasik berbasis fitur buatan tangan dengan lima jaringan saraf konvolusional (CNN) pada tugas yang sama, yaitu memperkirakan jumlah buah di setiap citra.

Metode usulan menggunakan segmentasi ambang RGB untuk memisahkan objek buah dari latar. Dari objek tersebut diambil empat jenis fitur: IH, HOG, SC, dan LBP. Fitur ini dimasukkan ke pengklasifikasi SVM dengan kernel Gaussian (γ = 0,5). Parameter SVM dioptimasi dengan empat algoritma, yaitu PSO, ACO, DE, dan GA. Pembanding CNN yang dilatih pada data yang sama adalah FCN-8S, ZFNet, AlexNet, GoogleNet, dan ResNet.

Data terdiri atas 100 citra dari satu kebun kiwi di Babol, Mazandaran, Iran, diambil pada siang hari dengan kamera CCD 512 × 576 piksel. Setiap citra dibagi menjadi 72 sub-citra berukuran 64 × 64 piksel. Label jumlah buah dibuat dengan menghitung secara visual, dengan setengah hitungan untuk buah yang terpotong. Parameter SVM dievaluasi dengan validasi silang lima lipatan dan fungsi tujuan R².

Pada tingkat sub-citra, nilai R² metode SVM berkisar 0,75 sampai 0,94. Pada tingkat citra, metode usulan mencapai R² 0,96 dengan waktu pemrosesan 0,553 detik per citra. FCN-8S mencapai R² 0,91 dalam 0,856 detik, GoogleNet 0,90 dalam 1,220 detik, AlexNet 0,83 dalam 0,663 detik, ZFNet 0,73 dalam 0,877 detik, dan ResNet 0,63 dalam 0,705 detik. Nilai PR-AUC dalam urutan yang sama adalah 0,967; 0,865; 0,899; 0,902; 0,912; dan 0,743. Penulis menjelaskan keunggulan CNN yang rendah dengan jebakan minimum lokal dan kebutuhan data latih yang besar. Penjelasan itu tidak diuji secara terpisah dalam studi.

Keterbatasan: studi ini tidak menggabungkan hitungan antarpandang untuk satu pohon, sehingga buah yang sama dapat terhitung di beberapa citra atau dari sudut lain. Percobaan dilakukan di satu kebun dengan satu kondisi pencahayaan, sebagaimana terlihat dari teks. Kedua hal ini adalah pengamatan dari teks, bukan pernyataan penulis.
