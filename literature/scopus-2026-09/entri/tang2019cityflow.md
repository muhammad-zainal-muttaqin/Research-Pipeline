# Cityflow: A city-scale benchmark for multi-target multi-camera vehicle tracking and re-identification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tang2019cityflow` |
| Judul asli | Cityflow: A city-scale benchmark for multi-target multi-camera vehicle tracking and re-identification |
| Penulis | Tang, Zheng; Naphade, Milind; Liu, Ming-Yu; Yang, Xiaodong; Birchfield, Stan; Wang, Shuo; Kumar, Ratnesh; Anastasiu, David; Hwang, Jenq-Neng |
| Tahun | 2019 |
| Venue | Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [tang2019cityflow.pdf](../pdf/tang2019cityflow.pdf)
- DOI resmi: https://doi.org/10.1109/cvpr.2019.00900

## Gambaran Umum

Makalah ini memperkenalkan CityFlow, benchmark berskala kota untuk pelacakan kendaraan lintas kamera (*multi-target multi-camera*, MTMC). Permasalahannya berasal dari kebutuhan kota memakai kamera lalu lintas sebagai sensor untuk mengoptimalkan arus dan menangani gangguan; hal itu menuntut pelacakan kendaraan di area luas yang mencakup banyak kamera di persimpangan berbeda. Penulis memecahnya menjadi tiga subproblems yang saling terkait, yaitu pelacakan dalam satu kamera (*multi-target single-camera*, MTSC), identifikasi ulang lintas kamera (ReID), dan pelacakan lintas jaringan kamera (MTMC). Benchmark sebelumnya dinilai tidak memadai karena cakupan spasialnya kecil, jumlah kameranya sedikit, video asli dan kalibrasi tidak tersedia, serta ada yang mengandaikan pelacakan dalam kamera sudah sempurna. Pada kendaraan, variasi antarkelas kecil sementara variasi intra-kelas besar, dan informasi plat nomor tidak boleh dipakai demi privasi pengemudi.

Dataset CityFlow memuat 3,25 jam video dari 40 kamera di 10 persimpangan sebuah kota menengah di Amerika Serikat, dengan jarak terjauh antar dua kamera yang berjalan bersamaan 2,5 km. Terdapat lima skenario (skenario 1, 3, dan 4 untuk latih; 2 dan 5 untuk uji), resolusi video minimal 960p, dan sebagian besar berlaju 10 bingkai per detik. Anotasinya mencakup 229.680 kotak pembatas dari 666 identitas kendaraan, dengan rata-rata 344,9 kotak per identitas; setiap kendaraan melintas minimal dua kamera. Kalibrasi disediakan dalam bentuk matriks homografi dari bidang citra ke bidang tanah berkoordinat GPS, diestimasi dari 5–14 titik tonggak dengan galat reproyeksi rata-rata 11,52 piksel. Plat nomor dan wajah manusia diredaksi. Subset CityFlow-ReID berisi 56.277 kotak: 36.935 citra latih dari 333 identitas, 18.290 citra uji dari 333 identitas lain, dan 1.052 kueri, dengan rata-rata 84,50 tanda tangan per kendaraan dari 4,55 sudut pandang kamera.

Mekanisme utamanya adalah asosiasi visual–spatio-temporal. MTMC dipandang sebagai gabungan pelacakan MTSC di dalam kamera dan ReID antarkamera yang dihubungkan oleh informasi ruang dan waktu. Penulis mengevaluasi detektor YOLOv3, SSD512, dan Faster R-CNN (bobot COCO, ambang skor 0,2); pelacak MTSC DeepSORT (daring, Kalman dan Hungarian), TC (luar daring, pengelompokan tracklet), serta MOANA (daring, model penampilan adaptif); dan tiga skema asosiasi spatio-temporal, yaitu PROVID yang membandingkan fitur visual lalu melakukan re-ranking, 2WGMMF yang mempelajari distribusi waktu transisi antarkamera secara daring, serta FVS yang memakai model probabilitas waktu transisi yang ditentukan manual dari jarak antarkamera. Untuk ReID, metrik yang dipakai adalah mAP dan *rank-K hit rate*; untuk pelacakan, MOTA, MOTP, IDF1, MT, dan FAR.

Hasil ReID pada CityFlow-ReID menunjukkan bahwa metode tanpa pembelajaran metrik lemah. FVS dengan norma Bhattacharyya hanya memperoleh mAP 6,3% dan *rank-1* 20,8%, sedangkan L2, L1, dan L∞ berturut-turut 5,9/20,4%, 6,2/20,3%, dan 3,2/17,0%. Pembelajaran metrik meningkatkan hasil; kombinasi *hard triplet loss* dan *cross entropy loss* dengan ResNeXt101 mencatat mAP 32,0% dan *rank-1* 48,8%, sementara DenseNet121 dengan *hard triplet loss* mencatat 30,5/45,8%. Untuk ReID kendaraan, MobileNetV1 dengan *batch hard* memperoleh mAP 32,0% dan *rank-1* 48,4%. Penulis menyatakan mAP tertinggi masih di bawah 35%, jauh lebih rendah daripada hasil metode yang sama pada Market1501, DukeMTMC-reID, dan MSMT17. Pada pelacakan satu kamera, kombinasi TC dengan SSD512 memberi IDF1 79,7%, MOTA 70,3%, dan FAR 7,4. Pada pelacakan lintas kamera, kombinasi FVS, TC, dan *batch all* mencapai IDF1 46,3%, sedangkan 2WGMMF dengan TC dan *batch sample* mencapai 45,1% dan PROVID dengan TC dan *batch all* 40,6%.

Batasan yang dinyatakan penulis mencakup dominasi perubahan sudut pandang sebagai penyebab kegagalan, kebutuhan pemilihan manual zona masuk dan keluar pada FVS serta 2WGMMF, dan keunggulan FVS yang bergantung pada model transisi buatan; tanpa pemodelan probabilistik, PROVID memberi hasil lebih rendah. Hanya kendaraan yang melintas lebih dari satu kamera yang dianotasi, sehingga evaluasi MTSC tidak memperhitungkan positif palsu. Galat kalibrasi 11,52 piksel berasal dari keterbatasan presisi Google Maps, dan lensa mata ikan serta kabur gerak akibat kecepatan kendaraan menyulitkan deteksi dan asosiasi. Penulis juga menyatakan dataset akan diperluas dan benchmark ini dapat menjadi dasar kajian lanjutan seperti estimasi pose kendaraan dan pembangkitan sudut pandang.
