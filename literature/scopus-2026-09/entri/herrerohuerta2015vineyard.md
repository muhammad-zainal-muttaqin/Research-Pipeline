# Vineyard yield estimation by automatic 3D bunch modelling in field conditions

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `herrerohuerta2015vineyard` |
| Judul asli | Vineyard yield estimation by automatic 3D bunch modelling in field conditions |
| Penulis | Herrero-Huerta, M\'onica; Gonz\'alez-Aguilera, Diego; Rodriguez-Gonzalvez, Pablo; Hern\'andez-L\'opez, David |
| Tahun | 2015 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | grape |

## Tautan Akses
- PDF: [herrerohuerta2015vineyard.pdf](../pdf/herrerohuerta2015vineyard.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2014.10.003

## Gambaran Umum

Herrero-Huerta dkk. (2015) mengusulkan metode estimasi hasil kebun anggur pada tingkat tandan (*cluster*) dengan *close-range photogrammetry* dan visi komputer. Metode ini memakai kamera RGB biasa, yaitu Canon EOS 500D dengan lensa tetap 17 mm, bukan sensor kedalaman. Dari beberapa foto satu tanaman, perangkat lunak *Photogrammetry Workbench* (PW) membangun model 3D tandan. Volume, berat, dan jumlah buah per tandan kemudian diestimasi dan dibandingkan dengan pengukuran laboratorium.

Data diambil pada 20 Oktober 2013 di kebun Tempranillo seluas 1,05 ha dekat Logroño, Spanyol, dengan tanaman sistem VSP. Dua puluh tandan dari 14 tanaman dipilih, lalu daun di sekitarnya dikurangi agar satu sisi tandan terlihat. Foto diambil dari jarak sekitar 2 m dengan bukaan f/5.6 dan kecepatan rana lebih cepat dari 1/160 s, tanpa *flash*. Target kuning buatan dipasang di tanah agar *point cloud* dapat diskalakan secara otomatis. Pasangan citra dicocokkan memakai *ASIFT* dan filter *ORSA*, dengan rata-rata 580 titik homolog per pasangan citra.

Hasil dibagi dua jalur. Jalur otomatis memakai *point cloud* langsung dari PW. Jalur semi-otomatis memasang model CAD buah pada *point cloud*, dengan koreksi empiris. Pada jalur otomatis, koefisien determinasi (R²) untuk volume adalah 0,77 dengan *median absolute deviation* (MAD) 34 cm³ pada median 216 cm³. Untuk berat, R² adalah 0,78 dengan MAD 35 g pada median 227 g. Untuk jumlah buah, R² adalah 0,80 dengan MAD 15 butir pada median 98 butir. Pada jalur CAD, R² berturut-turut adalah 0,76 (volume, MAD 33 cm³), 0,75 (berat, MAD 35 g), dan 0,78 (jumlah buah, MAD 15 butir). Penulis menguji pencilan dengan uji Pope dan menyatakan jalur semi-otomatis tidak memberi perbaikan yang berarti.

Angka-angka ini perlu dibaca dengan batasnya. Sampel hanya 20 tandan dari satu kebun dan satu musim, dan validasi dilakukan pada tandan yang sama dengan yang difoto. Hanya sisi yang terlihat yang difoto, sehingga sisi belakang diperkirakan dengan *convex hull*. Metode ini juga bergantung pada cahaya siang yang merata, dan penulis mengakui kondisi hujan dan angin kencang membatasi pengambilan data. Penulis membandingkan R² dengan Diago dkk. (2012), yaitu 0,73, dan Dunn dan Martin (2004), yaitu 0,85. Namun kedua studi itu mengukur besaran yang berbeda, yaitu hasil dan rasio piksel buah terhadap piksel citra, sehingga angkanya tidak dapat dibandingkan langsung. Kajian ini juga tidak melaporkan galat deteksi buah pada citra kebun secara keseluruhan.

Bagi tinjauan ini, kajian Herrero-Huerta dkk. (2015) termasuk pengukuran 3D dari beberapa citra RGB pada satu tanaman, bukan penghitungan lintas pandang. Tandan diukur sebagai satu objek per tanaman, dan tidak ada langkah yang mencocokkan buah yang sama antarfoto untuk menghindari hitung ganda. Karena itu kajian ini tidak menjawab persoalan identitas lintas pandang yang menjadi fokus tinjauan. Kontribusinya ada pada bukti bahwa rekonstruksi 3D dari kamera biasa dapat mengestimasi volume dan berat tandan di lapangan, dengan validasi laboratorium. Batas utamanya adalah ukuran sampel yang kecil dan sisi tak terlihat yang hanya diperkirakan.
