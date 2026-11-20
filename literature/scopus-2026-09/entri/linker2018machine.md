# Machine learning based analysis of night-time images for yield prediction in apple orchard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `linker2018machine` |
| Judul asli | Machine learning based analysis of night-time images for yield prediction in apple orchard |
| Penulis | Linker, Raphael |
| Tahun | 2018 |
| Venue | Biosystems Engineering |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [linker2018machine.pdf](../pdf/linker2018machine.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2018.01.003

## Gambaran Umum

Makalah Linker (2018) di *Biosystems Engineering* 167 menghitung jumlah apel dari citra kebun untuk memperkirakan hasil panen per pohon. Penghitungan manual lambat dan mahal, sedangkan metode berbasis citra yang dilaporkan sebelumnya sering diuji pada kondisi yang sama dengan data latihnya. Penulis menguji apakah sebuah pengklasifikasi titik kunci dapat bertahan ketika tahun panen, pencahayaan, dan kamera berubah.

Dua set data dipakai. Set 2014 berisi enam citra per pohon, sedangkan set 2016 berisi citra seluruh pohon dari dua sisi. Pada set 2016, penulis mengambil 12 citra acak untuk menguji penyesuaian posterior, dan pada set 2014 mereka memakai lebih dari 250 citra. Pengklasifikasi diuji pada 7.320 citra uji.

Metode bekerja pada titik kunci spekular (*specular highlight*) yang sudah diidentifikasi sebelumnya. Setiap titik kunci dideskripsikan dengan U-SURF, lalu deskriptor dikodekan sebagai *bag of visual words* dan diklasifikasikan dengan SVM (*support vector machine*) menjadi "apple" atau "not apple". Dari 72 pengklasifikasi yang diuji, konfigurasi terpilih memakai 2.000 sampel latih "apple", 5.000 sampel "not apple", dan kosakata 7.500 kata visual. Konfigurasi ini mencapai TPR (*true positive rate*) 91,5% dan FPR (*false positive rate*) 6,1%. Probabilitas posterior kemudian disesuaikan berdasarkan entropi atau intensitas sub-citra. Pada 12 citra acak 2016, penyesuaian ini memperbaiki R2 dan bias. Pada set 2014, penyesuaian entropi sedikit lebih buruk daripada tanpa penyesuaian, dan penyesuaian intensitas paling buruk. Estimasi keseluruhan berada dalam 5% dari hitungan visual. Untuk hasil panen, estimasi per sisi digabung dengan regresi linier: set 2016 memakai Yk = a E1,k + b E2,k + c, sedangkan set 2014 memakai model enam citra yang mengikuti Linker (2017). Parameter regresi dikalibrasi dari pohon yang hasil panennya diketahui.

Penulis menyatakan bahwa metode tetap andal pada tahun, pencahayaan, dan kamera yang berbeda. Namun mereka juga mencatat dua batas. Pertama, metode hanya bekerja pada titik kunci yang sudah diidentifikasi sebelumnya. Kedua, penyesuaian posterior setelah klasifikasi tidak robust, sehingga penulis menyarankan peningkatan kualitas citra sebagai pekerjaan lanjutan.
