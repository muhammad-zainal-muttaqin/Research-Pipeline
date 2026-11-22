# TrackFormer: Multi-Object Tracking with Transformers

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `meinhardt2022trackformer` |
| Judul asli | TrackFormer: Multi-Object Tracking with Transformers |
| Penulis | Meinhardt, Tim; Kirillov, Alexander; Leal-Taix\'e, Laura; Feichtenhofer, Christoph |
| Tahun | 2022 |
| Venue | Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [meinhardt2022trackformer.pdf](../pdf/meinhardt2022trackformer.pdf)
- DOI resmi: https://doi.org/10.1109/cvpr52688.2022.00864

## Gambaran Umum

Artikel ini mengusulkan TrackFormer untuk pelacakan banyak objek (*multi-object tracking*, MOT) pada video. Masalah yang diatasi adalah mengikuti lintasan sejumlah objek, misalnya pejalan kaki, sambil membedakan identitasnya sepanjang rekaman. Pendekatan umum sebelumnya bersifat dua tahap: mendeteksi objek per frame, lalu mengaitkan hasil deteksi memakai optimasi graf atau pencocokan. Pendekatan alternatif, *tracking-by-regression*, menggantikan tahap pengaitan dengan regresi posisi, tetapi tidak memiliki konsep identitas dan komunikasi global antarlintasan. Penulis mengusulkan paradigma baru bernama *tracking-by-attention* yang melakukan deteksi dan asosiasi data secara bersamaan.

Objek yang dilacak adalah objek pada kumpulan data visi komputer, bukan tanaman. Metode dievaluasi pada MOT17, MOT20, dan MOTS20. Model mengikuti arsitektur *encoder-decoder* Transformer dari Deformable DETR dengan ekstraksi fitur ResNet50. Untuk memenuhi kebutuhan data pelatihan mekanisme atensi multitahap, penulis menyimulasikan data MOT dari citra tunggal CrowdHuman dengan augmentasi spasial acak, antara lain pengubahan ukuran dan pemotongan hingga 20%. Pelatihan model deteksi privat memakan waktu sekitar dua hari pada tujuh GPU 32 GB.

Mekanisme asosiasi bertumpu pada dua jenis kueri. Kueri objek statis mendeteksi objek baru yang masuk ke adegan, lalu berubah menjadi kueri lintasan. Kueri lintasan bersifat autoregresif dan mengikuti objek yang sudah ada dalam ruang dan waktu dengan mempertahankan identitasnya. Kedua jenis kueri memakai atensi diri serta atensi *encoder-decoder* terhadap fitur frame global, sehingga tidak diperlukan optimasi graf, pencocokan tambahan, maupun pemodelan gerak atau penampilan secara eksplisit. Kueri lintasan menyimpan posisi spasial dan identitas objek, dan jumlahnya bersifat adaptif.

Angka hasil memakai metrik MOTA untuk cakupan objek, IDF1 untuk pelestarian identitas, serta MOTSA dan sMOTSA untuk segmentasi; kecepatan dinyatakan dalam FPS. Pada MOT17 dengan deteksi privat, TrackFormer mencatat MOTA 74,1 dan IDF1 68,0 pada 7,4 FPS. Pada MOT20 dengan deteksi privat, angkanya MOTA 68,6 dan IDF1 65,7. Pada MOTS20, hasil uji mencatat sMOTSA 54,9 dan IDF1 63,6. Studi ablasi pada data validasi menunjukkan konfigurasi lengkap mencapai MOTA 71,3 dan IDF1 73,4; penghapusan pralatihan menurunkannya 2,0 dan 1,6 poin, identifikasi ulang kueri lintasan menaikkan IDF1 sebesar 1,4 poin tanpa pengaruh berarti pada MOTA, dan penghapusan augmentasi menurunkan MOTA 5,2 serta IDF1 11,2 poin.

Batasan yang dinyatakan penulis mencakup batas maksimum objek yang dapat terdeteksi per frame karena model hanya mampu mendeteksi sejumlah Nobject objek; untuk MOT17 digunakan 500 kueri objek. Model memerlukan data pelatihan dalam jumlah besar sehingga data MOT disimulasikan dari citra tunggal. Pada pengaturan deteksi publik, model tidak dapat langsung menghasilkan keluaran lintasan dari masukan deteksi dan memerlukan penyaringan dengan ambang IoU, yang keadilannya dibahas tersendiri. Penulis juga menyatakan bahwa pelatihan dan inference hanya mencakup dua frame dan mengharapkan pengembangan lebih lanjut melampaui batas tersebut.
