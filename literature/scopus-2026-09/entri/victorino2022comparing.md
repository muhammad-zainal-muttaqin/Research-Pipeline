# Comparing a New Non-Invasive Vineyard Yield Estimation Approach Based on Image Analysis with Manual Sample-Based Methods

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `victorino2022comparing` |
| Judul asli | Comparing a New Non-Invasive Vineyard Yield Estimation Approach Based on Image Analysis with Manual Sample-Based Methods |
| Penulis | Victorino, Gon\ccalo; Braga, Ricardo P.; Santos-Victor, Jos\'e; Lopes, Carlos M. |
| Tahun | 2022 |
| Venue | Agronomy |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [victorino2022comparing.pdf](../pdf/victorino2022comparing.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy12061464

## Gambaran Umum

Penelitian ini membandingkan ketepatan metode estimasi hasil panen berbasis citra yang noninvasif dan berlaku untuk banyak kultivar dengan metode manual. Metode manual memakai jumlah tandan dikali bobot tandan historis saat panen dan memiliki keterbatasan berupa variabilitas ruang dan waktu, ketergantungan pada data historis, serta kebutuhan tenaga kerja. Penulis menguji metode citra pada kondisi lapangan nyata menjelang tahap veraison (BBCH 81) dan menguji kemampuannya mengatasi penutupan tandan oleh daun.

Tanaman yang diteliti adalah anggur. Data dikumpulkan dari enam kultivar (Alvarinho, Arinto, Castelão, Chardonnay, Encruzado, dan Syrah) di tiga kebun pada dua lokasi di wilayah anggur Lisbon, Portugal, pada musim 2019–2021. Sejumlah 213 segmen tanaman sepanjang 1 m dianalisis, dengan 30–40 segmen per kumpulan data. Citra diambil dengan kamera komersial Nikon D5200 beresolusi 6000×4000 piksel berlensa makro Sigma 50 mm secara statis, atau dengan platform robot darat Vinbot memakai Kinect v2 beresolusi 1920×1080 piksel secara bergerak. Latar biru dipakai untuk memudahkan pemisahan tanaman dari latar dan Estimasi porositas kanopi.

Mekanisme penghitungan berupa ekstraksi ciri citra secara manual dengan ImageJ: luas proyeksi tandan tampak (vBA), keliling tandan tampak (vBP), jumlah buah tampak (vBe), dan porositas kanopi (POR) melalui ambang warna pada ruang HSV memakai OpenCV. Luas tandan total (TBA) diperkirakan dari vBA dan POR dengan metode sebelumnya [42], yang mengasumsikan hubungan antara porositas dan keterbukaan tandan. Indeks kepadatan tandan (CI) diambil dari deskriptor OIV nomor 204 melalui penilaian visual pada sebagian sampel. Model regresi bertahap maju memakai statistik F kritis 0,15 untuk memilih peubah. Peubah terpilih adalah TBA×CI², vBA/vBP×vBe, dan vBA/vBP, dengan transformasi akar kuadrat pada respons hasil. Data digabung dan dibagi acak menjadi 50 persen latih (108 segmen) dan 50 persen validasi (105 segmen). Kinerja diukur dengan R², RMSE, serta uji F untuk kemiringan 1 dan intersep 0; galat dihitung sebagai (hasil perkiraan − hasil aktual)/hasil aktual. Model linear dibandingkan dengan mesin vektor pendukung, pohon keputusan, dan jaringan saraf, yang tidak menunjukkan keunggulan jelas.

Hasil utama: TBA saja hanya menjelaskan 62 persen keragaman hasil aktual dan bersifat bergantung kultivar. Model regresi akhir mencapai R² 0,86 pada himpunan validasi, dengan RMSE 0,82, intersep 0,019 (tidak signifikan), dan kemiringan 1,082 (tidak signifikan); pada himpunan latih R² 0,85 dan RMSE 0,74. Pada himpunan validasi gabungan (105 segmen), hasil aktual 2,5 kg/m, perkiraan manual 3,3 kg/m dengan galat 31,0 persen, dan perkiraan berbasis citra 2,3 kg/m dengan galat −8,3 persen; kedua metode memiliki korelasi r = 0,89 terhadap hasil aktual. Metode citra mengungguli metode manual pada lima dari enam kumpulan data kultivar, dengan sebagian besar galat absolut di bawah 10 persen. Galat manual tertinggi terjadi pada Syrah (124,2 persen) dan Chardonnay (90,0 persen), sedangkan galat metode citra tertinggi pada Encruzado (−20,8 persen) dan Arinto (−19,0 persen).

Batasan yang dinyatakan penulis: TBA saja tidak menghasilkan estimasi yang tepat lintas kultivar pada tingkat tanaman, dan model masih bergantung pada kultivar. Galat tertinggi terjadi pada kanopi sangat rapat dengan penutupan tandan oleh daun yang tinggi, sehingga kondisi tersebut menjadi batas metode. Penutupan tandan oleh tandan lain juga memengaruhi hasil, dan penulis belum menyelesaikannya. Analisis citra masih dilakukan manual, sehingga belum terverifikasi bahwa algoritme otomatis memberi hasil sama pada citra beresolusi tinggi dan rendah. Nilai CI diperoleh secara visual dari sampel dan mengacu pada tandan matang penuh, bukan pada kondisi veraison. Himpunan validasi hanya mewakili 1–4 persen tanaman di setiap kebun, sehingga ekstrapolasi dari sampel rentan terhadap variabilitas ruang. Penulis menyatakan metode ini baru berpotensi diotomatisasi penuh dan memerlukan data lebih banyak dari berbagai kultivar dan kondisi tumbuh.
