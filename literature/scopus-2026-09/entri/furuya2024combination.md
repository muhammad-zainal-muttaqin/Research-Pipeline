# Combination of Remote Sensing and Artificial Intelligence in Fruit Growing: Progress, Challenges, and Potential Applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `furuya2024combination` |
| Judul asli | Combination of Remote Sensing and Artificial Intelligence in Fruit Growing: Progress, Challenges, and Potential Applications |
| Penulis | Furuya, Danielle Elis Garcia; Bolfe, \'Edson Luis; Parreiras, Taya Cristo; Barbedo, Jayme Garcia Arnal; Santos, Thiago Teixeira; Gebler, Luciano |
| Tahun | 2024 |
| Venue | Remote Sensing |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | apple, grape |

## Tautan Akses
- PDF: [furuya2024combination.pdf](../pdf/furuya2024combination.pdf)
- DOI resmi: https://doi.org/10.3390/rs16244805

## Gambaran Umum

Kajian ini merespons kebutuhan perencanaan dan pengelolaan kebun buah yang lebih tepat untuk menjamin hasil dan mutu. Penginderaan jauh yang dipadukan dengan pembelajaran mesin dan pembelajaran mendalam telah dipakai untuk memetakan luas tanam, mendeteksi penyakit, dan memantau perkembangan tanaman, tetapi belum ada tinjauan khusus yang mengaitkan teknik itu dengan produksi apel dan anggur di Brasil. Penulis menetapkan tiga tujuan: meninjau kajian penginderaan jauh dan kecerdasan buatan untuk analisis buah, memeriksa teknik pada apel (Malus domestica) dan anggur (Vitis vinifera) ditinjau dari jenis data, algoritma, dan sasaran penelitian, serta mengkaji penerapan potensial di Vacaria, Rio Grande do Sul.

Metodenya terdiri atas empat tahap. Pengumpulan artikel melalui Web of Science memakai kata kunci TS = ((fruit OR orchard OR apple OR grape) AND (machine learning OR deep learning OR artificial intelligence) AND (remote sensing)) untuk rentang 2018 hingga Juni 2024. Dari 177 rekaman yang lolos pencarian, 117 artikel dianalisis. Analisis umum memetakan 38 jenis buah, negara, dan jurnal; analisis lanjutan memeriksa 30 artikel anggur dan 27 artikel apel. Tahap terakhir mempertimbangkan penerapan teknologi di Vacaria, salah satu dari sepuluh Distrik Agroteknologi dalam proyek Center for Development in Digital Agriculture (CCD-SemeAr) yang dipimpin Embrapa.

Berdasarkan artikel yang ditinjau, penginderaan jauh menyuapi algoritma dengan citra satelit, citra UAV, dan pengukuran proksimal. Sensor yang dipakai mencakup kamera hiperspektral dan multispektral, kamera termal, spectrometer, serta citra Sentinel-2 dan Landsat 8 OLI. Algoritma yang dominan mencakup random forest, support vector machine, jaringan saraf tiruan, extreme learning machine, dan arsitektur convolutional neural network seperti YOLOv5, U-Net, dan ISDU-Net. Sumber data dipadukan dengan indeks vegetasi seperti NDVI, SAVI, dan MNLI, lalu dikurangi dimensinya melalui pemilihan variabel sebelum dimodelkan. Sebagai acuan, klasifikasi varietas anggur dengan SVM dan MLP mencapai recall dan F1 sebesar 0,99 pada validasi silang lima lipat, dengan akurasi per varietas 0,83-0,97 untuk SVM dan 0,94-0,99 untuk MLP [35]. Deteksi tanaman anggur memakai YOLOv5, sedangkan penentuan zona kebun memakai K-means, menghasilkan akurasi, presisi, recall, dan F1 di atas 0,85 hingga 0,98 [24]. Segmentasi kebun dengan ISDU-Net mencapai akurasi piksel 87,73%, mean IoU 70,68%, dan koefisien Kappa 0,84 [57]. Prediksi hasil apel dengan model Cubist menghasilkan R² 0,83, RMSE 0,56 t/ha, dan MAE 0,2 t/ha [73]. Pada kajian apel, estimasi nitrogen dengan sensor hiperspektral proksimal memberi R² di atas 0,80, sedangkan pendekatan suborbital memberi R² hingga 0,75.

Penulis mencatat sejumlah batasan. Lebih dari 80% kajian apel (17 dari 20) berasal dari China, terutama varietas Fuji di Shandong dan Shaanxi, sehingga hasilnya belum tentu mewakili daerah lain. Biaya operasional sensor hiperspektral dan UAV tinggi, sementara spektroskopi NIR lebih murah tetapi terbatas pada resolusi dan cakupan. Model yang dilatih dengan data lapang sulit diskalakan karena keragaman wilayah, ketergantungan spasial, dan batasan teknologi; reproduktivitas juga dipengaruhi ketersediaan data dan keragaman lingkungan. Citra orbital bersifat luas dan sering gratis, tetapi resolusinya kurang untuk analisis rinci, sedangkan pita SWIR lebih mudah diperoleh pada citra satelit daripada sensor proksimal. Penulis menyatakan pula bahwa hasil antarkajian tidak selalu dapat dibandingkan langsung dan tinjauan berikutnya akan memakai pedoman PRISMA.

