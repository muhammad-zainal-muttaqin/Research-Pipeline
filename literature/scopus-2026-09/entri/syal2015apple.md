# Apple fruit detection and counting using computer vision techniques

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `syal2015apple` |
| Judul asli | Apple fruit detection and counting using computer vision techniques |
| Penulis | Syal, Anisha; Garg, Divya; Sharma, Shanu |
| Tahun | 2015 |
| Venue | 2014 IEEE International Conference on Computational Intelligence and Computing Research IEEE Iccic 2014 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [syal2015apple.pdf](../pdf/syal2015apple.pdf)
- DOI resmi: https://doi.org/10.1109/iccic.2014.7238364

## Gambaran Umum

Penghitungan buah secara manual masih banyak dilakukan di kebun, padahal cara ini memakan waktu dan membutuhkan banyak tenaga kerja. Penulis menyebut bahwa penghitungan manual untuk satu *pack house* dapat menghabiskan biaya sekitar 600.000 hingga 1.000.000 dolar AS per tahun. Hitungan buah juga menjadi dasar estimasi panen, perencanaan transportasi, dan jadwal pemetikan. Karena itu, penulis mengusulkan sistem pencacahan buah otomatis berbasis *computer vision* yang diharapkan lebih cepat, konsisten, dan hemat biaya dibandingkan penghitungan manual.

Data penelitian berupa citra pohon apel. Citra tidak berasal dari dataset baku, melainkan dikumpulkan dari berbagai situs web sehingga resolusi dan efek pencahayaannya beragam. Untuk tahap pelatihan segmentasi, penulis memakai 25 citra yang dikumpulkan dari berbagai sumber dengan kondisi pencahayaan yang berbeda. Sistem juga diuji pada basis data citra uji yang terpisah. Citra diperoleh dengan kamera dari adegan nyata. Teks ini tidak menjelaskan spesifikasi kamera secara rinci.

Metode penelitian terdiri atas dua fase, yaitu pelatihan dan pengujian. Pada tahap praproses, citra dihaluskan dengan *Gaussian filter* berukuran 7 x 7 piksel untuk mengurangi pengaruh perbedaan pencahayaan. Wilayah buah kemudian dipisahkan dengan segmentasi berbasis *minimum Euclidean distance* pada ruang warna *L*a*b**. Setelah itu, lingkaran dipasang pada wilayah buah melalui *circle fitting*, dan buah dihitung berdasarkan *centroid* setiap wilayah. Buah yang saling menutupi (*occluded*) dipisahkan dengan membandingkan wilayah besar terhadap apel tunggal yang sudah dikenali, sehingga penghitungan menjadi lebih mudah. Hasil ditampilkan dalam bentuk antarmuka grafis yang memperlihatkan deteksi tepi dan lingkaran hasil pemasangan pada citra uji. Penulis menyatakan bahwa sistem mendeteksi dan menghitung apel dengan benar pada citra uji. Teks yang saya baca tidak mencantumkan nilai akurasi, presisi, atau galat hitungan dalam bentuk angka. Penilaian kuantitatif karena itu tidak dapat dipastikan dari bagian ini.

Penulis menyimpulkan bahwa sistem memenuhi tujuan yang ditetapkan dan dapat dipakai untuk mengotomatiskan penghitungan apel. Penulis juga menyebut bahwa sistem ini dapat mengurangi biaya penghitungan manual dan kerugian akibat estimasi yang keliru. Keterbatasan yang dinyatakan penulis adalah bahwa sistem ini difokuskan pada apel matang. Penulis menyebut penghitungan apel hijau sebagai pengembangan di masa depan, dengan memanfaatkan konten tekstur citra. Dengan demikian, cakupan kajian ini belum mencakup apel hijau.
