# A Stride Toward Wine Yield Estimation from Images: Metrological Validation of Grape Berry Number, Radius, and Volume Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lanza2024stride` |
| Judul asli | A Stride Toward Wine Yield Estimation from Images: Metrological Validation of Grape Berry Number, Radius, and Volume Estimation |
| Penulis | Lanza, Bernardo; Botturi, Davide; Gnutti, Alessandro; Lancini, Matteo; Nuzzi, Cristina; Pasinetti, Simone |
| Tahun | 2024 |
| Venue | Sensors |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [lanza2024stride.pdf](../pdf/lanza2024stride.pdf)
- DOI resmi: https://doi.org/10.3390/s24227305

## Gambaran Umum

Kajian ini melakukan validasi metrologi terhadap STEWIE, jaringan saraf tersupervisi lemah yang mengestimasi jumlah dan jari-jari rata-rata buah anggur langsung dari citra warna dua dimensi. Tujuan akhirnya adalah menghitung volume gugus, baik bagian yang terlihat maupun total, sebagai dasar perkiraan hasil panen di kebun anggur. Penulis menilai bahwa kamera tiga dimensi belum andal untuk buah kecil di lapang karena pantulan permukaan, cahaya lingkungan, dan resolusi yang lebih rendah, sehingga pendekatan dua dimensi dipilih. Kontribusi baru artikel ini terletak pada validasi metrologi dan analisis ketidakpastian, yang jarang dibahas dalam riset pertanian presisi.

Data latih dan validasi berasal dari Embrapa Wine Grape Instance Segmentation Dataset (WGISD), berisi 300 citra dari lima varietas, yaitu Chardonnay, Cabernet Franc, Cabernet Sauvignon, Sauvignon Blanc, dan Syrah, dengan total 187.374 anotasi titik buah. Citra diambil dengan kamera EOS REBEL T3i (240 citra) dan ponsel Moto Z2 Play (60 citra) pada jarak 1–2 m antarbarisan pohon. Himpunan uji dibuat khusus dari varietas Flame yang tidak ada pada data latih, terdiri atas 10 gugus dengan tiga citra per gugus, sehingga total 30 citra. Kamera Arducam AR0234 dipakai pada jarak tetap 500 mm, dengan rotasi gugus 0°, 120°, dan 240° untuk mencakup variasi orientasi. Kalibrasi kamera memakai 30 citra pola papan catur berukuran kotak 20 mm di MATLAB; faktor konversi piksel ke milimeter dihitung sebagai Cpx−mm = d/f dengan d = 500 mm. Jari-jari buah diukur manual dengan jangka sorong beresolusi 0,01 mm.

Mekanisme model menerima citra berukuran H×W dan menghasilkan dua peta kepadatan, Dn dan Dr, yang masing-masing berukuran H×W. Penjumlahan nilai piksel pada Dn menghasilkan perkiraan jumlah buah Ñ, sedangkan penjumlahan pada Dr menghasilkan jari-jari rata-rata r̃mean dalam piksel. Volume bagian yang terlihat dihitung sebagai ṼI,px = Ñ·(4/3)π·r̃mean³. Volume seluruh gugus dalam milimeter kubik diperoleh dari Ṽb,mm = ṼI,px·C³px−mm·R, dengan R sebagai faktor koreksi rasio volume seluruh gugus terhadap volume buah yang terlihat, dirata-ratakan atas 30 citra uji. Ketidakpastian dihitung menurut Guide to the Expression of Uncertainty (GUM), dengan komponen σd = 25 mm, σf = 2 piksel, σR = 0,32, dan σṼI,px = 2,8×10⁵ px³.

Pada 30 citra uji, penghitungan buah memberi mean error (ME) −1,57 buah dengan simpangan baku 1,9 dan mean percentage error (MPE) −5 persen dengan simpangan baku 6,3 persen; penulis menyatakan model cenderung merendahkan jumlah karena buah tertutup. Estimasi jari-jari memberi ME 0,15 piksel, simpangan baku 1,5 piksel, MPE 0,8 persen, dan simpangan baku 7 persen. Volume tampak dalam px³ memberi MPE 0,36 persen tetapi simpangan baku 20,8 persen, sehingga penulis menilai bias yang kecil itu belum dapat diandalkan. Volume seluruh gugus memiliki koefisien variasi rata-rata 24 persen dengan simpangan baku 7 persen, dan ketidakpastian rata-rata 42 mm³ atau sekitar 20 persen dari volume estimasi. Analisis kontribusi ketidakpastian menunjukkan ṼI,px menyumbang 45 persen, R 32,6 persen, jarak kamera–gugus d 22,1 persen, dan panjang fokus f 0,3 persen. Untuk perbandingan dengan data validasi yang memuat banyak gugus per citra, penulis mengasumsikan rata-rata 14 gugus dan 50 buah per gugus; MAE ternormalisasi rata-rata adalah 3,1 persen dengan simpangan baku 0,8 persen.

Batasan utama yang dinyatakan penulis adalah ketidakpastian tinggi pada volume dalam mm³. Sekitar setengah ketidakpastian total berasal dari jarak kamera–objek dan faktor R, yang timbul karena tidak tersedia pengukuran kedalaman yang andal antara kamera dan buah. Nilai R dihitung memakai acuan manual seluruh data uji, sehingga memasukkan bias; penulis mengakui pendekatan ini dipilih karena keterbatasan ukuran data. Volume juga dipangkat tiga sehingga kecilnya galat jari-jari diperkuat. Penulis mengusulkan penggabungan kamera kedalaman dengan citra warna untuk mengetahui jarak gugus secara langsung dan menyusun formulasi R yang lebih baik, serta menerapkan sistem pada perangkat tertanam dengan keluaran ketidakpastian.
