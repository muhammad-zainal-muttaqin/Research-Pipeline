# Location of Fruits by Counting: A Point-to-Point Approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2022location` |
| Judul asli | Location of Fruits by Counting: A Point-to-Point Approach |
| Penulis | Li, Bo; Chen, Cheng |
| Tahun | 2022 |
| Venue | Agronomy |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [li2022location.pdf](../pdf/li2022location.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy12112863

## Gambaran Umum

Penelitian ini bertujuan menempatkan buah melalui pendekatan titik-ke-titik dengan anotasi berupa titik pusat buah saja. Metode deteksi atau segmentasi berbasis pembelajaran mendalam meningkatkan kinerja estimasi hasil dan pemanenan, tetapi memerlukan pelabelan kotak atau topeng instance yang memakan banyak tenaga. Penulis mengurangi beban anotasi itu dengan melatih jaringan hanya pada titik tengah buah dan menghasilkan jumlah buah serta koordinat pusatnya secara bersamaan.

Tanaman yang diteliti adalah apel. Data berupa himpunan data apel publik [24] berisi citra mentah berukuran 1024×1024 piksel dalam berbagai kondisi pencahayaan alami. Anotasi aslinya berupa kotak, tetapi penulis hanya memakai titik pusat kotak tersebut, dengan bentuk (xi, yi) untuk i = 1 sampai C, tempat C adalah jumlah apel dalam citra. Perbandingan pembagian data latih dan uji tidak dinyatakan; teks hanya menyebut himpunan latih dan himpunan uji.

Metode terdiri atas dua fase. Fase pertama berupa inferensi jaringan saraf multitugas dengan DLASeg berbasis tulang punggung DLA-34. Cabang peta salient melakukan lima kali upsampling 2× menghasilkan peta probabilitas 1024×1024, sedangkan cabang penghitung menggabungkan vektor ciri 32×32×512 dari lapisan terdalam dan peta probabilitas menjadi dua vektor 64 dimensi, lalu mengeluarkan satu bilangan yang dibulatkan menjadi perkiraan jumlah buah Ĉ. Fase kedua mengambang peta salient dengan ambang τ = 0,9 untuk memperoleh piksel buah, lalu mencocokkan titik-titik itu dengan model campuran Gaussian memakai algoritme expectation maximization; pusat tiap komponen Gaussian menjadi perkiraan titik pusat buah. Fungsi rugi posisi memakai jarak Hausdorff termodifikasi (DWH), sedangkan jumlah buah memakai rugi L1 halus, dengan total rugi L = DWH + Lreg(C − Ĉ(I)). Pelatihan memakai Python, OpenCV, dan PyTorch dengan GPU Tesla P40 serta CPU Core i5-8400, bobot awal ImageNet untuk DLA-34, ukuran kumpulan 32, pengoptimal Adam dengan laju pembelajaran 10⁻⁴ dan momentum 0,9, serta augmentasi pembalikan horizontal.

Hasil deteksi pada himpunan uji adalah presisi 87,43 persen, recall 85,32 persen, dan skor F1 86,36 persen untuk metode usulan pada τ = 0,9, dibandingkan Mask-RCNN dengan presisi 85,97 persen, recall 85,69 persen, dan F1 85,83 persen pada ambang IoU 50 persen dan keyakinan 0,9. Kecepatan deteksi metode usulan mencapai 34 frame per detik; augmentasi pembalikan horizontal menaikkan presisi dari 86,97 persen menjadi 87,43 persen dan recall dari 84,88 persen menjadi 85,32 persen. Untuk posisi, pada batas deviasi r = 1 piksel metode usulan memberi MAE 4,0, RMSE 4,1, dan MAPE 37,7 persen, sedangkan Mask-RCNN memberi 2,9, 3,0, dan 27,5 persen. Pada r = 5 piksel, nilainya 1,9, 3,8, dan 18,4 persen untuk metode usulan dibandingkan 1,8, 2,5, dan 17,7 persen untuk Mask-RCNN; pada r = 10 piksel keduanya sama, yaitu 1,4, 1,5, dan 13,2 persen. Acuan hitung posisi adalah jarak antara titik perkiraan dan titik asli, dengan true positive dihitung bila jaraknya tidak melebihi r. Ringkasan menyatakan tidak lebih dari dua target per citra memiliki deviasi posisi melebihi lima piksel. Kecepatan proses penempatan mencapai 7 frame per detik.

Batasan yang dinyatakan penulis: metode sukar membedakan apel yang saling bertumpang tindih karena tumpang tindih membentuk satu titik panas terus-menerus pada peta, dan apel yang mendominasi luas buah menyebabkan apel lain terabaikan. Pemilihan model dengan rugi lebih rendah menyusutkan titik panas dan memutus area yang menyambung, tetapi membuat area buah kecil terlewat. Penulis juga mencatat pergeseran pusat yang besar sebagai akibat langsung dari kemudahan segmentasi. Penelitian lanjutan diarahkan pada jaringan deteksi titik pusat ujung-ke-ujung agar menghilangkan proses EM yang memakan waktu.
