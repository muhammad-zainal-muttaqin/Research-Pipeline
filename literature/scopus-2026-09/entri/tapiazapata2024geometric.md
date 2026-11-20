# A geometric modelling approach to estimate apple fruit size by means of LiDAR 3D point clouds

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tapiazapata2024geometric` |
| Judul asli | A geometric modelling approach to estimate apple fruit size by means of LiDAR 3D point clouds |
| Penulis | Tapia-Zapata, Nicolas; Saha, Kowshik Kumar; Tsoulias, Nikos; Zude-Sasse, Manuela |
| Tahun | 2024 |
| Venue | International Journal of Food Properties |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [tapiazapata2024geometric.pdf](../pdf/tapiazapata2024geometric.pdf)
- DOI resmi: https://doi.org/10.1080/10942912.2024.2330494

## Gambaran Umum

Tapia-Zapata dkk. (2024) menyusun pendekatan pemodelan geometris untuk memperkirakan ukuran buah apel dari *point cloud* 3D yang diperoleh dengan *LiDAR*. Pengukuran ukuran buah di pohon sulit dilakukan karena buah sering tertutup bagian pohon lain. Selain itu, atribut geometri dan radiometri buah sangat bervariasi. Pendekatan yang paling umum, yaitu jarak Euclides terjauh dalam *point cloud*, mengabaikan bentuk buah yang berubah selama pertumbuhan. Penulis mengusulkan algoritma yang mendekatkan *point cloud* tersegmentasi ke bentuk acuan berbasis deret Fourier 2D. Tujuannya adalah mengevaluasi ketepatan estimasi ukuran dan waktu komputasi model tersebut.

Data dikumpulkan dengan sensor LiDAR 2D bergerak LMS-511 (Sick AG) yang memancarkan cahaya 905 nm dengan resolusi sudut 0,1667° dan frekuensi pindai 25 Hz. Pengukuran laboratorium memakai bola berdiameter 60 mm dan 80 mm (n = 3) serta apel yang dipindai pada 60, 74, 90, 104, 132, dan 151 hari setelah bunga mekar (DAFB), masing-masing dengan n = 10. Pengukuran lapangan dilakukan di kebun apel eksperimental Field Lab for Digital Agriculture, Potsdam-Marquardt, Jerman. Sensor dipasang pada konveyor melingkar yang bergerak mengelilingi barisan pohon dengan jarak 2,0 m dari tengah barisan. Di lapangan terdapat 20 bola yang dipasang pada bingkai logam, dan 72 apel yang dipindai pada lima tanggal, yaitu 67, 81, 117, 132, dan 136 DAFB. Ukuran acuan diperoleh dengan mengukur diameter buah secara manual menggunakan jangka sorong elektronik.

Model dibandingkan dengan dua pendekatan jarak Euclides, yaitu jarak rata-rata dan jarak maksimum. Pada seluruh periode pertumbuhan di kondisi lapangan, RMSE antara jari-jari terukur dan prediksi adalah 20,1% untuk model geometris, 76,8% untuk pendekatan rata-rata, dan 119,1% untuk pendekatan maksimum. Pada regresi linear antara nilai prediksi dan nilai terukur, koefisien determinasi (R2) model geometris adalah 0,76 untuk apel laboratorium dan 0,49 untuk apel lapangan. Pada bola laboratorium, RMSE acuan rata-rata adalah 6,09 mm untuk bola 60 mm dan 3,77 mm untuk bola 80 mm. Nilai MBE untuk ukuran hasil estimasi adalah 4,24% untuk bola 60 mm dan 1,41% untuk bola 80 mm. Selisih RMSE relatif model geometris terhadap pendekatan Euclides mencapai 1,96% terhadap rata-rata dan 5,27% terhadap maksimum. Dari sisi kecepatan, penyelesaian algoritma memerlukan 10 hingga lebih dari 100 detik di laboratorium dan 6·10⁻³ hingga 6 detik di lapangan.

Penulis menyatakan beberapa batasan. Model peka terhadap pencilan yang tidak terdeteksi, karena setiap titik ikut diperhitungkan, sehingga area dengan galat di atas 15 mm muncul. Oklusi oleh bagian pohon lain mengurangi area buah yang terpindai. Kepadatan *point cloud* dan jarak sensor memengaruhi waktu penyelesaian, sehingga penempatan LiDAR dalam sistem pemindaian terintegrasi harus menyeimbangkan kecepatan algoritma dengan ketepatan estimasi. Nilai alfa 0,5 untuk kontur awal dipilih secara arbitrer setelah eksplorasi citra. Penulis menilai metode ini dapat mendukung pemantauan buah dan pengelolaan kebun presisi, tetapi validasi lebih lanjut masih diperlukan.
