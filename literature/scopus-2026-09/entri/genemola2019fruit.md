# Fruit detection in an apple orchard using a mobile terrestrial laser scanner

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `genemola2019fruit` |
| Judul asli | Fruit detection in an apple orchard using a mobile terrestrial laser scanner |
| Penulis | Gen\'e-Mola, Jordi; Gregorio, Eduard; Guevara, Javier; Auat, Fernando; Sanz-Cortiella, Ricardo; Escol\`a, Alexandre; Llorens, Jordi; Morros, Josep-Ramon; Ruiz-Hidalgo, Javier; Vilaplana, Ver\'onica; Rosell-Polo, Joan R. |
| Tahun | 2019 |
| Venue | Biosystems Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [genemola2019fruit.pdf](../pdf/genemola2019fruit.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2019.08.017

## Gambaran Umum

Pendeteksian dan pelokalan buah yang andal dapat meningkatkan nilai panen dengan mengurangi kerusakan buah serta memperbaiki praktik panen. Sebagian besar sistem deteksi buah masih memakai kamera RGB, sehingga kinerjanya bergantung pada kondisi pencahayaan yang berubah-ubah. Kajian ini mengusulkan teknik baru yang memakai *mobile terrestrial laser scanner* (MTLS) untuk mendeteksi dan melokalisasi apel Fuji (*Malus domestica* Borkh. cv. Fuji). Pertanyaan utamanya ialah apakah data *LiDAR*, khususnya nilai *apparent reflectance*, dapat dipakai untuk mendeteksi apel dan menentukan posisi 3D-nya.

Pengambilan data dilakukan pada 28 September 2017 di kebun komersial Tarasso, Agramunt, Catalonia, Spanyol. Objek kajiannya adalah kebun apel Fuji berumur delapan tahun dengan sistem *tall spindle* dan tinggi pohon maksimum 3,75 m. Sensor yang dipakai ialah Velodyne VLP-16 yang disinkronkan dengan penerima *RTK-GNSS* (GPS1200+, ketelitian sekitar 20 mm) dan dipasang di bagian belakang penyemprot bertenaga udara. Sensor memancarkan 16 berkas laser pada panjang gelombang 905 nm dan hanya memodelkan titik hingga jarak 4 m, sehingga hanya deretan pohon yang diteliti yang masuk ke dalam awan titik. Ada tiga pohon yang dianalisis. Jumlah apel hasil penghitungan lapangan (GT_lapangan) adalah 139 pada pohon 1, 145 pada pohon 2, dan 139 pada pohon 3. Dari jumlah itu, 133, 138, dan 134 buah berhasil diberi label pada awan titik 3D karena oklusi dan kesalahan penghitungan di lapangan. Pohon 1 dan 2 dipakai sebagai data latih untuk memilih dan menyetel parameter algoritma, sedangkan pohon 3 dipakai sebagai data uji.

Metode yang dikembangkan terdiri atas empat tahap, yaitu segmentasi awan titik berdasarkan ambang nilai reflektansi, pemisahan buah, dan penghapusan positif palsu berdasarkan geometri dan reflektansi klaster. Analisis reflektansi menghasilkan nilai rata-rata 28,9% untuk daun, 29,1% untuk cabang, 44,3% untuk apel, dan nilai untuk batang yang juga tercantum dalam teks. Nilai ini menunjukkan bahwa apel memantulkan cahaya laser 905 nm lebih kuat daripada daun dan batang sehingga parameter tersebut berguna untuk deteksi. Hasil uji pada pohon 3 menunjukkan tingkat keberhasilan lokalisasi 87,5%, tingkat keberhasilan identifikasi 82,4%, dan *F1-score* 0,858 terhadap jumlah total buah. Penulis menyatakan bahwa tingkat deteksi ini sebanding dengan sistem berbasis RGB, dengan keunggulan berupa lokasi buah dalam koordinat 3D yang tidak terpengaruh variasi sinar matahari.

Kesimpulan penulis menyatakan bahwa teknologi berbasis *LiDAR*, terutama informasi reflektansinya, memiliki potensi untuk deteksi apel jarak jauh dan penentuan lokasi 3D. Meski demikian, ruang lingkup penelitian ini sempit. Data hanya berasal dari tiga pohon satu varietas di satu kebun pada satu tanggal, dengan satu pohon sebagai data uji. Penelitian ini juga hanya merekam satu deretan pohon dan mengabaikan titik yang lebih jauh dari 4 m. Sensor dipasang pada kendaraan yang bergerak, dan model reflektansi yang dipakai mengasumsikan permukaan Lambertian serta tidak memperhitungkan sudut datang. Oleh karena itu, hasil ini belum dapat langsung digeneralisasi ke varietas, kondisi kebun, atau fase pertumbuhan buah yang berbeda.
