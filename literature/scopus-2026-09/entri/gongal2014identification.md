# Identification of repetitive apples for improved crop-load estimation with dual-side imaging

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gongal2014identification` |
| Judul asli | Identification of repetitive apples for improved crop-load estimation with dual-side imaging |
| Penulis | Gongal, Aleana; Amatya, Suraj; Karkee, Manoj |
| Tahun | 2014 |
| Venue | American Society of Agricultural and Biological Engineers Annual International Meeting 2014 Asabe 2014 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [gongal2014identification.pdf](../pdf/gongal2014identification.pdf)

## Gambaran Umum

Penelitian ini bertujuan meningkatkan estimasi beban buah apel dengan mengatasi keterbatasan visibilitas buah akibat penutupan oleh daun, cabang, dan buah lain. Pengcitraan dari dua sisi kanopi meningkatkan visibilitas, tetapi buah yang sama dapat muncul pada kedua citra sehingga dihitung dua kali dan menyebabkan overestimasi. Penulis mengajukan cara mengidentifikasi buah berulang (*repetitive apples*) dari dua sisi kanopi yang berlawanan agar penghitungan ganda dihilangkan.

Data dikumpulkan di kebun komersial Yakima Valley Orchards di Prosser dan Grandview, Washington, pada apel kultivar Jazz dengan arsitektur *tall spindle*. Kamera warna CCD (Prosilica GigE 1290c) dipasang bersama kamera tiga dimensi berbasis waktu tempuh (PMD CamCube 3.0) pada platform sensor *over-the-row* yang digerakkan dengan traktor. Citra diambil dari dua sisi barisan pada enam hingga tujuh ketinggian per pohon. Sebanyak 266 citra (133 pasangan) dari dua sisi didaftarkan dalam sistem koordinat global. Jumlah buah berulang sebagai kebenaran (*ground truth*) ditentukan secara manual.

Identifikasi buah pada citra warna memakai segmentasi Otsu, dilasi dan erosi morfologis, serta penyaringan berdasarkan luas dan kompaktes untuk membuang daun dan cabang. Setiap buah yang teridentifikasi didaftarkan secara manual ke citra intensitas kamera 3D guna memperoleh koordinat pusat buah. Dua kerangka kamera dari sisi berlawanan diselaraskan ke sistem koordinat bersama melalui rotasi 90° pada sumbu X dan translasi pada sumbu Z sejarak antarkamera (2,45 m), ditambah translasi pada sumbu X (0 m), Y (0,05 m), dan Z (2,40–2,45 m) yang ditentukan dengan coba-coba memakai lima buah per citra dari sekurang-kurangnya 25 citra. Dua buah dianggap sama apabila jaraknya kurang dari diameter rata-rata buah, yaitu 0,08 m dalam penelitian ini.

Pada ambang jarak setara diameter penuh, akurasi identifikasi buah berulang sebesar 83,97%, dengan galat absolut persentase rata-rata (*mean absolute percentage error*, MAPE) 11,70%. Dari 260 buah berulang, 40 terlewat (*false negative*) dan 42 buah bukan berulang salah diklasifikasi (*false positive*). Pada ambang tiga perempat diameter, akurasi 89,80% dengan tingkat deteksi buah berulang 67,69%. Visibilitas buah naik dari 60% menjadi 97% dengan pengcitraan dua sisi, dan 21% buah terlihat dari kedua sisi. Simpulan penulis menyebut akurasi identifikasi buah berulang sebesar 82%; abstrak menyebut MAPE 12% pada ambang diameter penuh. Validasi memakai 19 pohon; split latih/uji tidak dinyatakan karena metode ini bukan pembelajaran mesin.

Penulis menyatakan beberapa batasan. Kekakuan dan ketahanan platform *over-the-row* yang kurang mengubah parameter transformasi untuk pendaftaran 3D antarpasangan citra dan antarpohon. Kesalahan penginderaan dan pemetaan 3D menggeser lokasi buah, sehingga buah dalam gugusan salah terdeteksi sebagai berulang. Kesalahan identifikasi buah menambah *false negative* ketika buah berulang tidak terdeteksi pada kedua citra. Pendaftaran antara citra warna 2D dan citra intensitas 3D masih dilakukan manual. Penulis menyebut perlunya otomatisasi pendaftaran dan peningkatan efisiensi komputasi.
