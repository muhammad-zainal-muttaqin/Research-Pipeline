# MOTR: End-to-End Multiple-Object Tracking with Transformer

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zeng2022motr` |
| Judul asli | MOTR: End-to-End Multiple-Object Tracking with Transformer |
| Penulis | Zeng, Fangao; Dong, Bin; Zhang, Yuang; Wang, Tiancai; Zhang, Xiangyu; Wei, Yichen |
| Tahun | 2022 |
| Venue | Lecture Notes in Computer Science |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [zeng2022motr.pdf](../pdf/zeng2022motr.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-031-19812-0_38

## Gambaran Umum

Artikel ini mengusulkan MOTR, kerangka pelacakan banyak objek (*multi-object tracking*, MOT) menyeluruh dari akhir ke akhir (*end-to-end*) berbasis Transformer. Masalah utamanya adalah pemodelan temporal objek. Metode yang ada melakukan asosiasi deteksi setelah pemrosesan memakai kemiripan gerak, seperti IoU atau Kalman Filter, maupun kemiripan penampilan berbasis Re-ID. Sifat asosiasi yang menjadi pasca-pemrosesan menghalangi pemanfaatan variasi temporal secara menyeluruh. Penulis memandang MOT sebagai sekumpulan masalah prediksi urutan, ketika setiap urutan sesuai dengan satu lintasan objek, dan memperluas *object query* pada DETR menjadi *track query*.

Objek yang dilacak adalah objek pada kumpulan data visi komputer, bukan tanaman. Metode dievaluasi pada MOT17, DanceTrack, dan BDD100K. MOTR dibangun di atas Deformable DETR dengan ResNet50 dan bobot awal yang dilatih pada COCO. Pelatihan memakai klip video lima frame dengan panjang yang dinaikkan bertahap dari dua menjadi lima, sedangkan kecepatan inference sekitar 7,5 FPS pada Tesla V100. Metrik yang dipakai mencakup HOTA, AssA, DetA, MOTA, IDF1, dan ID switch.

Mekanisme inti adalah *track query* yang merepresentasikan satu lintasan dan diperbarui frame demi frame melalui atensi diri dan atensi silang dengan fitur citra. Agar satu kueri mengikuti satu objek, penulis memperkenalkan *tracklet-aware label assignment*, yaitu prediksi dari satu kueri diawasi oleh urutan kotak pembatas dengan identitas yang sama. Objek baru dan objek yang berhenti ditangani dengan mekanisme masuk dan keluar yang menjaga himpunan kueri tetap dinamis, sehingga tidak diperlukan asosiasi lintasan eksplisit saat inference. Untuk memperkuat pemodelan temporal, penulis menambahkan *collective average loss* yang menghitung rugi atas seluruh klip video dan *temporal aggregation network* yang mengagregasi riwayat keadaan kueri memakai mekanisme kunci-kueri.

Angka hasil menunjukkan keunggulan asosiasi, bukan deteksi. Pada MOT17 dengan deteksi privat, MOTR mencatat HOTA 57,8; AssA 55,7; DetA 60,3; IDF1 68,6; dan MOTA 73,4. Angka IDF1 ini mengungguli TrackFormer dan TransTrack sebesar 4,5%, dan MOTA mengungguli TrackFormer sebesar 73,4% berbanding 65,0%, meski masih di bawah ByteTrack yang mencatat MOTA 80,3. Pada DanceTrack, MOTR mengungguli ByteTrack sebesar 6,5% pada HOTA dan mencatat AssA 40,2% berbanding 32,1%. Studi ablasi menunjukkan penambahan *temporal aggregation network* meningkatkan MOTA sebesar 7,8%.

Batasan yang dinyatakan penulis ada dua. Pertama, kinerja deteksi objek baru belum memuaskan dan tercermin pada angka MOTA yang masih rendah, karena kueri deteksi ditekan ketika mendeteksi objek yang sudah dilacak, sehingga deteksi objek baru terbatas. Kedua, pelemparan kueri dilakukan frame demi frame, yang membatasi efisiensi pembelajaran saat pelatihan; penulis mencatat bahwa dekode paralel seperti pada VisTR tidak berhasil menangani skenario MOT yang kompleks. Kedua masalah ini menjadi topik penelitian lanjutan bagi kerangka MOT berbasis Transformer.

