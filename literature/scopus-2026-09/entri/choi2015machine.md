# Machine vision system for early yield estimation of citrus in a site-specific manner

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `choi2015machine` |
| Judul asli | Machine vision system for early yield estimation of citrus in a site-specific manner |
| Penulis | Choi, Daeun; Lee, Won Suk; Ehsani, Reza; Schueller, John K.; Roka, Fritz |
| Tahun | 2015 |
| Venue | 2015 ASABE International Meeting |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [choi2015machine.pdf](../pdf/choi2015machine.pdf)
- DOI resmi: https://doi.org/10.13031/aim.20152181863

## Gambaran Umum

Kajian ini (Choi dkk., 2015) menghitung buah jeruk hijau yang belum matang dari citra RGB-D yang diambil dengan sensor Kinect v2. Metode ini memakai informasi kedalaman di samping citra warna agar buah dapat dibedakan dari daun dan latar belakang pohon. Hasil utama pada 93 citra adalah tingkat identifikasi benar rerata 72,1% dan tingkat *false positive* rerata 23,2%, diukur dengan validasi silang tiga lipatan (*3-fold cross-validation*).

Kamera menghasilkan citra warna berukuran 1920×1080 piksel dan citra kedalaman berukuran 512×424 piksel. Dari data kedalaman dihitung medan gradien kedalaman (*depth gradient field*) dan vortisitas (*vorticity*) untuk menemukan area potensial yang cembung. Area kandidat itu kemudian diperiksa dengan transformasi Hough lingkaran (*circular Hough transform*, CHT) untuk mencari bentuk bulat. Setiap kandidat dijelaskan oleh 13 fitur, yang mencakup jari-jari 3D, tekstur, kedalaman, gradien, entropi, dan jumlah tepi. Klasifikasi dilakukan dengan *random forest*. Sebelum itu, kontras pencahayaan diperbaiki dengan CLAHE (*contrast limited adaptive histogram equalization*).

Pada tiga lipatan, jumlah buah sebenarnya adalah 72, 76, dan 74. Jumlah buah yang teridentifikasi benar adalah 51, 53, dan 56, dengan *false positive* sebanyak 20, 13, dan 16. Rerata akhir adalah 53,3 buah benar (72,1%) dan 17,2 *false positive* (23,2%). Hampir seperempat hasil positif berupa kesalahan, sehingga pemisahan buah dari daun masih menjadi sumber galat utama pada metode ini. Angka tersebut hanya berlaku untuk satu kumpulan citra, yaitu 93 citra.

Pengambilan citra dilakukan di kebun pada 7 Mei 2015 dengan kamera berjarak 50 sampai 60 cm dari tajuk. Buah jeruk pusar (*navel*) yang diuji berdiameter sekitar 2 sampai 3 cm. Penulis menyimpulkan bahwa metode ini mampu mendeteksi buah kecil yang masih sangat muda, dan deteksi dini itu dinilai berguna untuk memperkirakan hasil panen.
