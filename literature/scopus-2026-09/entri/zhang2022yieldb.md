# Yield estimation of citrus fruit using rapid image processing in natural background

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2022yieldb` |
| Judul asli | Yield estimation of citrus fruit using rapid image processing in natural background |
| Penulis | Zhang, Xiaohua; Toudeshki, Arash; Ehsani, Reza; Li, Haoling; Zhang, Wenfeng; Ma, Ruijun |
| Tahun | 2022 |
| Venue | Smart Agricultural Technology |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [zhang2022yieldb.pdf](../pdf/zhang2022yieldb.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2021.100027

## Gambaran Umum

Estimasi hasil panen sebelum panen penting bagi petani buah bernilai tinggi. Estimasi ini membantu perencanaan logistik panen, penyimpanan, dan penjualan. Cara konvensional berbasis pengambilan sampel buah dan pendekatan statistik dinilai rumit, padat tenaga kerja, dan memakan waktu. Kajian ini mengusulkan algoritma pengolahan citra yang cepat untuk mendeteksi dan mencacah buah jeruk matang di alam terbuka tanpa menghapus latar belakang dan derau terlebih dahulu. Penulis juga menilai bahwa algoritma yang ringkas dapat dipakai pada pengolahan citra real-time dan robot pemanen.

Citra dikumpulkan dari dua varietas jeruk, yaitu mandarin dan orange, pada masa pematangan. Pengambilan dilakukan pada September dan November 2018 di kebun Shiraz Ranch, Newman, California. Penulis mengumpulkan 133 citra, tetapi 132 citra dipakai dalam pengolahan. Kamera yang digunakan adalah kamera ponsel iPhone XR dengan resolusi 4032 × 3024 piksel, format JPG, dan tanpa zoom maupun lampu kilat. Kamera dipasang tegak lurus terhadap baris pohon pada jarak tetap 213 cm. Sebanyak 66 pohon dipotret dari sisi timur dan barat. Pengolahan dilakukan dengan laptop Intel Core i5 berbasis Windows 64-bit dan MATLAB 2018a. Penulis juga mengukur intensitas cahaya di sekitar pohon dan kamera pada kondisi cerah maupun berawan.

Metode utama mengubah citra ke ruang warna Lab dan memakai komponen a* untuk memisahkan buah dari latar. Selanjutnya, penulis menerapkan Circle Hough transform dengan rentang radius 8 sampai 20 untuk mengenali lingkaran buah. Hasil penelitian menunjukkan bahwa jarak kamera 1,5 m, 1,8 m, dan 2,1 m menghasilkan akurasi deteksi berturut-turut 90%, 91,4%, dan 92,7%. Jarak di bawah 1,5 m atau di atas 2,1 m menghasilkan akurasi di bawah 80%. Pada satu citra contoh, komputer mencacah 180 buah dari 190 buah yang dihitung manusia. Dari jumlah itu, 178 buah terhitung benar, 12 buah terlewat, dan terdapat 2 deteksi keliru. Akurasi deteksi citra tersebut 93,7%, akurasi estimasi hasil 94,7%, dan tingkat deteksi keliru 1,1%. Untuk seluruh 66 pohon, akurasi deteksi rata-rata 91,7% dengan tingkat deteksi keliru rata-rata 1,7%. Akurasi per citra berkisar antara 50% hingga 100%. Waktu proses rata-rata 1,1 s per citra, dengan waktu tercepat 0,76 s dan terlama 2,49 s. Analisis regresi linear sederhana antara hitungan mesin dan hitungan manusia menghasilkan R² sebesar 0,98 untuk kedua posisi kamera.

Penulis menyatakan bahwa kesalahan terutama disebabkan oleh oklusi hampir total, derau, bayangan, dan pantulan sinar matahari pada daun. Penulis juga menyebut bahwa hasil citra yang diproses dengan menghapus latar belakang derau berhasil dicacah seluruhnya. Penelitian ini menguji algoritma pada dua varietas jeruk di satu lokasi kebun dengan jarak kamera tetap, sehingga generalisasi ke kondisi lain belum diuji oleh penulis. Metode ini juga dibandingkan dengan hitungan manusia sebagai acuan, bukan dengan panen aktual. Penulis menyimpulkan bahwa kombinasi ruang warna Lab dan Circle Hough transform dapat mengenali jeruk di lingkungan alami, dengan keunggulan kecepatan proses dan ketahanan terhadap perubahan cahaya serta oklusi oleh daun, cabang, dan buah lain.
