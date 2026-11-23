# A Random Forest Based Smart Fruit Counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `pavithra2022random` |
| Judul asli | A Random Forest Based Smart Fruit Counting |
| Penulis | Pavithra, R.; Priyadharshini, P.Sugantha |
| Tahun | 2022 |
| Venue | Proceedings of the 2nd International Conference on Artificial Intelligence and Smart Energy Icais 2022 |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [pavithra2022random.pdf](../pdf/pavithra2022random.pdf)
- DOI resmi: https://doi.org/10.1109/icais53314.2022.9742725

## Gambaran Umum

Penulis menyebut penghitungan buah secara manual memakan waktu dan tenaga, serta menghasilkan perkiraan yang keliru karena galat manusia. Tujuan makalah ini adalah sistem penghitungan buah otomatis dari citra yang menggabungkan fitur warna, bentuk, dan tekstur. Penulis menyatakan metodenya berfungsi pada pencahayaan berbeda, daun yang menutupi buah, dan buah yang saling menumpuk.

Data berupa citra buah yang dikumpulkan dari internet. Jarak kamera ke pohon dan kondisi pencahayaan berbeda-beda. Jumlah citra, jenis tanaman per citra, pemberi label, dan pembagian data latih dan uji tidak disebut. Buah yang disebut dalam kesimpulan adalah apel, anggur, jeruk, dan pisang.

Metode dimulai dengan penghalusan citra memakai tapis Gaussian (*Gaussian filter*) berukuran 3x3 di MATLAB. Segmentasi (pemisahan buah dari latar) memakai ambang batas pada kanal kromiannya merah (*red chrominance*) ruang warna YCbCr dengan ambang 0,6. Buah yang bersentuhan dipisahkan dengan transformasi *watershed*. Jumlah buah dihitung dari jumlah maksimum regional (*regional maximum*, RM), dengan transformasi jarak (*distance transform*, DT) dan luas area sebagai pembanding. Regresi linear menghubungkan hitungan dengan nilai sebenarnya. Hutan acak (*random forest*) disebut sebagai klasifikator dengan validasi silang 10 lipatan.

Penulis melaporkan akurasi lokal optimal 95% berdasarkan selisih antara hitung manual dan hitung algoritme. Akurasi pengenalan hingga 90% disebut untuk klasifikasi berbasis jarak Euclid. Deteksi anggur putih 91% dan anggur merah 97% disebut dari sistem pengenalan berbasis warna dan morfologi. Metrik tepatnya, data uji, dan jumlah citra untuk angka 95% tidak disebut.

Keterbatasan yang dapat diperiksa dari teks: tidak ada rincian data dan pembagian latih-uji, tidak ada pembandingan dengan metode lain, dan tidak ada tabel hasil. Penjelasan hutan acak merujuk pada bidang data bernama Time, Amount, dan v1 sampai v28, yang tidak berkaitan dengan citra buah. Metode DT diakui menghitung terlalu sedikit pada buah menyatu, sedangkan metode RM menghitung terlalu banyak. Citra berasal dari satu pandang tanpa penautan antarcitra.
