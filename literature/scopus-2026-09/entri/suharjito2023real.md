# Real-Time Oil Palm Fruit Grading System Using Smartphone and Modified YOLOv4

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `suharjito2023real` |
| Judul asli | Real-Time Oil Palm Fruit Grading System Using Smartphone and Modified YOLOv4 |
| Penulis | Suharjito; Asrol, Muhammad; Utama, Ditdit Nugeraha; Junior, Franz Adeta; Marimin |
| Tahun | 2023 |
| Venue | IEEE Access |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [suharjito2023real.pdf](../pdf/suharjito2023real.pdf)
- DOI resmi: https://doi.org/10.1109/access.2023.3285537

## Gambaran Umum

Penelitian ini menangani penyortiran tandan buah segar kelapa sawit yang masih dilakukan manual di bagian grading pabrik pengolahan. Penilaian manusia menghasilkan hasil yang tidak konsisten, sementara kadar asam lemak bebas pada minyak dipengaruhi oleh tingkat kematangan saat panen. Penulis mencatat bahwa kajian sebelumnya banyak memakai citra diam dan klasifikasi satu objek, sehingga tidak dapat mendeteksi beberapa tandan dalam satu frame secara waktu nyata. Tujuan penelitian adalah membangun sistem deteksi dan klasifikasi kematangan berbasis telepon genggam dan video, dengan memodifikasi YOLOv4 agar dapat dijalankan pada perangkat mobile.

Data video direkam dengan telepon genggam di area grading pabrik sawit di Kalimantan Tengah, beresolusi 1280×720 dalam format MP4. Himpunan data memuat 56 video multikelas dan 45 video satu kelas dengan durasi 10–15 detik per video. Enam kategori yang dipakai adalah empty bunch, unripe, underripe, ripe, overripe, dan abnormal; kategori ditetapkan dan dikonfirmasi oleh praktisi serta pakar grading pabrik. Teks melaporkan 4.214 berkas secara keseluruhan, tetapi juga menyebut 7.256 citra dan 14.757 objek, dengan rata-rata dua objek per citra. Citra dihasilkan dengan ekstraksi frame memakai VLC pada rasio 10, yaitu satu frame setiap 0,33 detik. Anotasi kotak pembatas dikerjakan dengan Roboflow dan disimpan dalam berkas .txt berisi id kelas serta koordinat kotak. Data dibagi menjadi latih, validasi, dan uji dengan rasio 7:2:1. Augmentasi yang dipakai mencakup rotasi 45° dan 90°, translasi rasio 0,5, kecerahan acak −40% sampai 60%, serta Gaussian blur dengan varians 7%–9%.

Model dikembangkan dari dua arsitektur, YOLOv4-CSPDarknet53 dan YOLOv4-Tiny. CSPDarknet53 memiliki lima blok CSP dan lapisan SPP, sedangkan YOLOv4-Tiny memiliki tiga blok CSP tanpa SPP. Keduanya memakai PANet pada neck dan detektor YOLOv3 pada head; skala deteksi YOLOv4-CSPDarknet53 adalah 52×52, 26×26, dan 13×13, sedangkan YOLOv4-Tiny memakai 13×13 dan 26×26. Pelatihan memakai DarkNet di Google Colaboratory dengan GPU Nvidia Tesla P100 dan RAM 54,8 GB, bobot awal MS-COCO, maksimum 12.000 batch, learning rate 0,001, batch 64, momentum 0,949, decay 0,0005, serta penurunan laju pada iterasi ke-9.600 dan ke-10.800. Regresi kotak pembatas memakai Complete IoU, dengan Mish untuk YOLOv4-CSPDarknet53 dan Leaky ReLU untuk YOLOv4-Tiny. Metrik evaluasi adalah mAP, F1-score, IoU, presisi, recall, dan confidence score.

Hasil menunjukkan augmentasi meningkatkan mAP@0,50, presisi, recall, F1, dan IoU rata-rata YOLOv4-320 dibandingkan tanpa augmentasi. Pada perbandingan model, mAP@50 uji tertinggi adalah 99,98% untuk YOLOv4-320, diikuti YOLOv4-512 sebesar 99,97% dan YOLOv4-416 sebesar 99,93%. YOLOv4-320 memiliki FPS terbesar 59,7 dan BFlops terkecil, tetapi YOLOv4-416 dipilih untuk aplikasi karena IoU rata-ratanya lebih tinggi. Model itu dikonversi dengan TensorFlow Lite dan dikuantisasi menjadi fp16 dan int8. Pengujian di pabrik memakai Samsung Galaxy S20+, sepuluh video per kelas ditambah sepuluh video campuran, lima frame per video, sehingga 350 frame per model. Empat model yang dibandingkan adalah YOLOv4-q-fp16, YOLOv4-416-q-int8, YOLOv4-tiny, dan YOLOv4-tiny-q-fp16. IoU tertinggi per kategori adalah 92,4% pada underripe dan terendah 74,65% pada abnormal. F1 rata-rata tertinggi 0,64 pada YOLOv4-q-fp16 dan terendah 0,52 pada YOLOv4-tiny-q-fp16. Teks menyebut mAP tertinggi 65,53% dan terendah 53,31% tetapi mengaitkan keduanya dengan YOLOv4-tiny-q-fp16, sehingga terjadi inkonsistensi internal; abstrak menyatakan model YOLOv4 dengan kuantisasi 16 bit lebih baik 12% daripada YOLOv4-Tiny berdasarkan mAP.

Penulis menyatakan sejumlah batasan. Kategori empty dan unripe mencapai mAP di atas 97% dengan F1 0,99, tetapi ripe, abnormal, dan overripe hanya mencapai mAP 40%–60% dengan F1 0,30%–0,50 karena kemiripan warna dan bentuk. Underripe sering salah diklasifikasikan sebagai unripe, dengan mAP di bawah 20% pada YOLOv4-tiny; video campuran hanya mencapai mAP 20%–40% dan F1 0,15%–0,30. Skor kepercayaan di atas 75% tidak menjamin klasifikasi yang benar. Model kuantisasi memiliki latensi lebih tinggi daripada YOLOv4-tiny karena ukurannya lebih besar. Penulis menyatakan kinerja pada video multikelas masih lebih rendah daripada video satu kelas dan mengusulkan penambahan data latih multikelas. Penerapan dibatasi pada sortasi pascapanen di pabrik, tidak pada kebun, serta pada perangkat mobile karena ukuran parameter; kuantisasi int8 mengurangi mAP 1,1% dibanding fp16.

