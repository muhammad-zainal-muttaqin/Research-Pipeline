# Survey on Deep Learning Based Crowd Counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yu2021survey` |
| Judul asli | Survey on Deep Learning Based Crowd Counting |
| Penulis | Yu, Y.; others |
| Tahun | 2021 |
| Venue | Jisuanji Yanjiu Yu Fazhan Computer Research and Development |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [yu2021survey.pdf](../pdf/yu2021survey.pdf)
- DOI resmi: https://doi.org/10.7544/issn1000-1239.2021.20200699

## Gambaran Umum

Kajian ini adalah tinjauan pustaka tentang penghitungan kerumunan (*crowd counting*) berbasis pembelajaran mendalam. Masalah yang diatasi adalah estimasi jumlah, kepadatan, atau sebaran orang dalam citra maupun video untuk analisis perilaku dan pengelolaan keselamatan publik, seperti deteksi kepadatan dan perilaku abnormal guna mencegah kecelakaan. Penulis menyebutkan tiga tantangan lama yang belum teratasi, yaitu penghitungan lintas adegan, distorsi perspektif, dan variasi skala. Tinjauan ini membandingkan model tradisional dengan model berbasis pembelajaran mendalam dan menyusun perkembangan bidang itu dari empat sisi: struktur jaringan, pembentukan *ground truth*, fungsi rugi, dan metrik evaluasi.

Kajian ini bukan tentang tanaman; ia termasuk metode dari luar pertanian yang dapat ditransfer ke pencacahan objek. Fokusnya adalah penghitungan pada citra statis berbasis deep learning, meskipun penulis juga menyentuh data video. Berdasarkan cara kerjanya, model dibagi menjadi metode regresi langsung yang mengeluarkan jumlah orang dan metode estimasi peta kepadatan yang menjumlahkan peta secara integral. Berdasarkan strukturnya, model dibagi menjadi jaringan satu cabang, banyak cabang, dan struktur khusus. Penulis mengulas dataset utama, antara lain UCSD (2.000 citra, 49.885 orang), Mall (2.000 citra), WorldExpo'10 (3.980 citra, 199.923 orang), dan ShanghaiTech (1.198 citra, 330.165 titik kepala; Bagian A memiliki 300 citra latih dan 182 citra uji, Bagian B memiliki 400 citra latih dan 316 citra uji).

Mekanisme deteksi dan asosiasi yang diulas mencakup penggunaan fitur multi-skala, *context awareness*, konvolusi dialasi (*dilated convolution*), konvolusi deformabel, mekanisme atensi, dan GAN. Jaringan awal bersatu cabang, seperti model Wang dkk. berbasis AlexNet yang langsung memprediksi jumlah, tidak menghasilkan peta kepadatan sehingga lebih lemah pada adegan padat dan lintas adegan. Jaringan banyak cabang, seperti CrowdNet dan MCNN, memakai beberapa kolom dengan ukuran kernel berbeda untuk menangkap skala beragam; MCNN memperkenalkan kernel Gauss adaptif dan dataset ShanghaiTech. CP-GCNN menambahkan atensi konteks dan rugi adversarial, Switch-CNN memilih cabang berdasarkan tingkat kepadatan per wilayah, sedangkan SANet menggabungkan skala dalam satu jaringan dan memakai rugi SSIM. CSRNet beralih ke jaringan satu kanal berbasis VGG-16 dan konvolusi dialasi untuk mengurangi parameter, sementara ADCrowdNet menggabungkan atensi dan konvolusi deformabel untuk menyaring latar dan memetakan bentuk kerumunan.

Angka hasil yang disajikan berupa perbandingan kinerja pada tabel dengan metrik MAE (akurasi), MSE, dan RMSE (robustness), yang didefinisikan pada Persamaan (8)–(10); Tian dkk. memperluas MAE dan RMSE menjadi PMAE dan PMSE untuk menilai daerah lokal. Pada dataset UCSD, PaDNet mencapai MAE 0,85 dan MSE 1,06, disusul PACNN dengan MAE 0,89 dan MSE 1,18 (Tabel 2). Pada Mall, SAAN memperoleh MAE 1,28 dan MSE 1,68, sedangkan DecideNet MAE 1,52 dan MSE 1,90 (Tabel 3). Pada ShanghaiTech Bagian A, SFCN mencapai MAE 64,8 dan MSE 107,5, sementara MCNN sebagai baseline mencatat MAE 110,2 dan MSE 173,2 (Tabel 4). Angka-angka ini diambil dari tabel tinjauan yang merangkum hasil publikasi sebelumnya, bukan dari percobaan baru penulis.

Batasan yang dinyatakan penulis mencakup ketahanan model yang rendah terhadap kebisingan latar, oklusi, dan sebaran kerumunan yang tidak seragam pada adegan sangat padat. Jaringan banyak cabang memiliki parameter melimpah, sulit dilatih, dan kurang real-time; penulis juga mencatat bahwa cabang-cabangnya sering mempelajari fitur yang saling mirip. Rugi Euclidean mengabaikan informasi struktural sehingga menghasilkan peta kepadatan kabur, sedangkan rugi SSIM lebih peka pada kesamaan lokal dan rugi adversarial sulit dilatih. Pembentukan *ground truth* menjadi titik kritis: metode kernel Gauss adaptif membuat kepala dekat hilang, metode kernel tetap membuat kepala jauh tumpang tindih, dan metode anotasi sadar-konteks mencoba mengatasi keduanya. Penulis menyimpulkan bahwa arah masa depan adalah merancang jaringan yang sederhana namun efektif dengan mengurangi jumlah cabang serta menggabungkan atensi, konvolusi dialasi, GAN, dan konvolusi deformabel, sekaligus menyempurnakan fungsi rugi dan cara membangkitkan *ground truth*.
