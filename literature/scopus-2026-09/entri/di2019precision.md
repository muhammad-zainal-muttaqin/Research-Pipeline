# A precision viticulture UAV-based approach for early yield prediction in vineyard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `di2019precision` |
| Judul asli | A precision viticulture UAV-based approach for early yield prediction in vineyard |
| Penulis | Di Gennaro, S.F.; Toscano, P.; Cinat, P.; Berton, A.; Matese, A. |
| Tahun | 2019 |
| Venue | Precision Agriculture 2019 Papers Presented at the 12th European Conference on Precision Agriculture Ecpa 2019 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [di2019precision.pdf](../pdf/di2019precision.pdf)
- DOI resmi: https://doi.org/10.3920/978-90-8686-888-9_46

## Gambaran Umum

Penelitian ini bertujuan membangun sistem perkiraan hasil panen otomatis untuk kebun anggur sekitar lima minggu sebelum panen. Pengukuran lapang dan penimbangan manual memakan waktu serta sering menghasilkan data yang kurang representatif karena jumlah contoh terbatas. Penulis menguji pencitraan RGB beresolusi tinggi dari platform UAV pada satu zona representatif variabilitas vigor kebun. Algoritma pengenalan tanpa pengawasan dipakai untuk memperoleh jumlah dan ukuran tandan, yang kemudian menjadi dasar perkiraan produksi. Penulis menyatakan metode ini cepat, murah, dan akurat serta berpotensi membantu pengelolaan produksi di kebun dan di gudang anggur.

Kajian berlangsung di kebun anggur seluas 1,4 ha di dekat Siena, Italia, dengan kultivar Sangiovese (*Vitis vinifera*), ditanam tahun 2008, pada lereng menghadap selatan di ketinggian 355 m. Pohon dibentuk dengan teralis *vertical shoot-positioned*, dipangkas pada satu cordon, dengan jarak tanam 2,2 × 0,75 m dan baris berarah barat laut–tenggara. UAV MikrokopterOktoXL termodifikasi membawa kamera multispektral ADC-Snap dan kamera RGB Sony Cyber-shot DSC-QX100. Penerbangan dilakukan pada 26 Juni dan 7 Agustus 2018. Kamera multispektral beroperasi pada ketinggian 50 m di atas permukaan tanah dengan resolusi 0,025 m/piksel dan tumpang tindih 70%; NDVI dihitung dari citra UAV yang diproses di Agisoft Photoscan Pro, dikalibrasi radiometrik di Matlab dengan panel referensi, lalu diekstrak per pohon di QGIS. Citra Sentinel-2 Level 2A diunduh dari Copernicus dan NDVI-nya dihitung dari pita B8 (842 nm) dan B4 (665 nm) pada resolusi 10 m. Pada penerbangan kedua, delapan pohon berturut-turut di setiap zona vigor menjalani defoliasi pada zona buah. Pencitraan RGB dilakukan pukul 14.00 pada ketinggian 5 m dengan kamera miring 45° sepanjang baris, menghasilkan resolusi 0,002 m/piksel pada zona buah; UAV melayang sekitar 20 detik di depan setiap petak delapan pohon.

Pengolahan diawali dengan langkah terselia untuk memilih citra terbaik dan memotong citra tanaman contoh, lalu ImageJ melakukan pengolahan tanpa pengawasan. Citra RGB diubah ke ruang warna HSV; lapisan H (*hue*) dipilih karena paling baik memisahkan tandan. Filter Yen mengubah lapisan itu menjadi citra biner 8 bit yang memisahkan tandan dari tanah, daun, dan batang; filter median 3 × 3 menghilangkan derau garam dan merica; filter *filling holes* menutup lubang kecil hasil segmentasi. Perintah *Analyze particles* menghitung dan mengukur luas setiap tandan, dengan waktu pengolahan maksimal satu menit per citra. Pendugaan hasil dihitung dari luas total tandan per pohon (cm²/pohon) yang dikonversi menjadi hasil per pohon (kg/pohon) memakai parameter kalibrasi dari musim 2017 di kebun yang sama, sebagai cawat uji. Hasil per pohon pada tiap zona vigor kemudian dikorelasikan dengan NDVI dari peta 7 Agustus 2018, dan model regresi linear dipakai untuk menyusun peta perkiraan hasil; pendekatan yang sama diuji dengan peta NDVI Sentinel-2 tanggal 18 Juli 2018.

Hasil menunjukkan korelasi linear kuat antara hasil taksiran dan hasil teramati untuk tandan matang per pohon (R² = 0,84). Kesalahan terhadap hasil tandan matang per pohon sebesar 17,8% di zona vigor rendah (LV) dan 23,3% di zona vigor tinggi (HV), serta lebih besar untuk hasil total per pohon, yaitu 30,5% di LV dan 27,8% di HV. Nilai hasil rata-rata yang ditaksiran lebih rendah daripada pengukuran lapang, yaitu 2,33 ± 0,97 kg berbanding 2,57 ± 1,07 kg di HV dan 1,78 ± 0,69 kg berbanding 1,74 ± 0,64 kg di LV; untuk hasil total lapang (HV = 3,00 ± 1,43 kg, LV = 2,14 ± 1,06 kg) metode kehilangan semua tandan yang sebagian atau seluruhnya belum matang sehingga korelasinya R² = 0,73 dengan pendugaan lebih rendah. Peta hasil dua kelas berdasarkan median NDVI menghasilkan 2,84 ± 1,20 kg/pohon di HV dan 2,05 ± 1,05 kg/pohon di LV. Penulis menyatakan metode mensyaratkan garis pandang bebas antara sensor dan tandan serta tidak dapat membedakan tandan hijau dari daun, sehingga hanya tandan matang atau setengah matang yang terdeteksi. Variabilitas antarmusim memengaruhi morfologi tandan, kematangan, tumpang tindih, kanopi, dan cahaya, sehingga diperlukan penyesuaian musiman terhadap ukuran lapang. Penulis menyatakan metode ini tidak menggantikan pengamatan lapang dan perlu diuji pada musim, varietas, dan sistem teralis lain.
