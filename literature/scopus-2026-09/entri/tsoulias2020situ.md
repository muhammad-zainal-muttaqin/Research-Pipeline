# In-situ detection of apple fruit using a 2D LiDAR laser scanner

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tsoulias2020situ` |
| Judul asli | In-situ detection of apple fruit using a 2D LiDAR laser scanner |
| Penulis | Tsoulias, Nikos; Xanthopoulos, George; Fountas, Spyros; Zude, Manuela |
| Tahun | 2020 |
| Venue | 2020 IEEE International Workshop on Metrology for Agriculture and Forestry Metroagrifor 2020 Proceedings |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [tsoulias2020situ.pdf](../pdf/tsoulias2020situ.pdf)
- DOI resmi: https://doi.org/10.1109/metroagrifor50201.2020.9277629

## Gambaran Umum

Penulis menyatakan bahwa penghitungan apel secara manual memakan tenaga dan tidak memberi informasi spasial. Kamera RGB-D dinilai rentan terhadap cahaya matahari. Penelitian ini menguji apakah reflektansi (intensitas pantulan) dari *LiDAR* 2D dapat mendeteksi dan melokalisasi buah apel pada pohon. *LiDAR* adalah sensor laser yang mengukur jarak dari pantulan cahaya.

Data dikumpulkan pada 2019 di kebun apel varietas Gala dekat Brandenburg, Jerman. Dua pohon didefoliasi sebelum panen. Sensor LMS511 dipasang pada traktor berjalan 0,2 km/jam dengan jarak 2,5 m dari baris. Buah dihitung dan dipanen manual, lalu tingginya diukur di laboratorium. Teks menyebut luas kebun 1 ha pada abstrak dan 65 ha pada bagian lokasi.

Metode memisahkan titik buah dari kayu dengan ambang reflektansi empiris. Histogram kepadatan bivariat pada bidang x-z dan y-z mencari puncak lokal sebagai posisi buah. Tinggi buah diperoleh dari selisih titik maksimum dan minimum pada sumbu z. Penyelarasan awal memakai *iterative closest point* (ICP).

Hasil utama: 38 dari 44 apel teridentifikasi. Deteksi rata-rata mencapai 92,5% terhadap total buah pada pohon yang didefoliasi, dan turun menjadi 70,5% pada pohon berdaun. Korelasi R2 0,83 untuk tinggi dan 0,62 untuk diameter. Pada W2-3, R2adj 0,72 dengan RMSE 3,31 mm. Teks tidak merinci jumlah buah yang menjadi dasar angka 92,5%.

Keterbatasan yang dapat diperiksa dari teks: hanya dua pohon dan satu musim. Teks mengakui metode perlu divalidasi pada kanopi nyata dengan sistem pemangkasan lain. Hasil menurun di area dengan kepadatan buah tinggi. Pembagian data latih dan uji tidak disebut.
