# Instance segmentation and multi-object tracking for fruit quality grading and dynamic yield estimation in Egyptian citrus orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `farhoud2026instance` |
| Judul asli | Instance segmentation and multi-object tracking for fruit quality grading and dynamic yield estimation in Egyptian citrus orchards |
| Penulis | Farhoud, Saleh A.; Zaghloul, Yasmine A.; Shehata, Omar M. |
| Tahun | 2026 |
| Venue | Smart Agricultural Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [farhoud2026instance.pdf](../pdf/farhoud2026instance.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2026.102529

## Gambaran Umum

Makalah ini mengembangkan kerangka kerja penglihatan komputer untuk penilaian mutu buah (Good versus Defective) dan estimasi hasil dinamis pada jeruk (orange) di kebun komersial di Gubernuran Beheira, Mesir. Kerangka tersebut menggabungkan segmentasi instans (*instance segmentation*), pelacakan multi-objek (*multi-object tracking*, MOT) dengan BoT-SORT, dan penghitungan berbasis garis virtual yang dilintasi lintasan buah. Penulis membangun dataset sendiri berisi 618 citra asli beranotasi poligon (3024 × 4032 piksel, dipotret dengan telepon pintar), diperluas menjadi 1.545 citra latih hasil augmentasi, ditambah 15 video.

Model yang dibandingkan adalah YOLOv8 dan YOLOv11 (lima ukuran masing-masing: n, s, m, l, x), Mask R-CNN (dua tahap), dan RT-DETR-l sebagai pembanding berbasis transformer yang hanya menghasilkan kotak pembatas. Pada penilaian statis, YOLOv11l mencapai mAP@0,5 sebesar 0,932 dengan latensi 26,1 ms per citra. Pada estimasi hasil dinamis atas enam video tolok ukur, RT-DETR memberi galat total terendah (WMAPE 5,66%), sedangkan YOLOv11s terbaik di antara model segmentasi (WMAPE 6,97%, 14,2 ms per bingkai).

Temuan utama penulis adalah disosiasi tiga arah: segmenter statis terbaik (YOLOv11l), penghitung total dinamis terbaik (RT-DETR), dan penilai mutu dinamis terbaik (YOLOv11s) adalah tiga sistem yang berbeda. Akurasi penghitungan dan kemampuan penilaian mutu dinyatakan sebagai sifat yang terpisah dan harus dievaluasi terpisah.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penulis menyatakan bahwa produksi jeruk Mesir masih bergantung pada pemeriksaan, penilaian mutu, dan estimasi hasil secara manual yang lambat, subjektif, dan sulit diperbesar skalanya, di tengah menurunnya tenaga kerja pertanian. Estimasi hasil manual disebut menimbulkan galat yang mengganggu perencanaan panen, alokasi tenaga kerja, dan logistik pascapanen.

Masalah teknis yang dirumuskan adalah bahwa sebagian besar penelitian menilai model pada citra statis dengan metrik segmentasi seperti mAP, sedangkan estimasi hasil praktis dilakukan pada video kamera bergerak. Pada video tersebut, deteksi yang terputus-putus dan keyakinan yang berosilasi dapat memecah identitas lintasan sehingga menimbulkan penghitungan berlebih atau kurang secara sistematis. Penulis menyimpulkan bahwa akurasi per citra yang tinggi tidak otomatis berarti penghitungan yang andal. Penulis juga mencatat kelangkaan dataset lapangan publik untuk jeruk di Mesir dan bahwa penelitian terdahulu umumnya menangani satu tujuan saja (deteksi, segmentasi, atau penghitungan), bukan jalur terpadu.

## Ide Utama

Gagasan pokoknya adalah memperlakukan penilaian mutu statis dan penghitungan dinamis sebagai dua tahap evaluasi yang berbeda untuk setiap model yang telah disetel halus. Detektor atau segmenter dijalankan per bingkai, BoT-SORT memberi identitas persisten dengan kompensasi gerak kamera (*global motion compensation*, GMC), dan setiap buah dihitung tepat satu kali ketika pusat kotak pembatasnya melintasi garis vertikal virtual. Kelas Good atau Defective pada saat lintasan melewati garis menentukan penghitung kelas yang bertambah.

Penulis menahan konfigurasi pelacak tetap untuk semua model, sehingga perbedaan hasil hitung dianggap mencerminkan kestabilan deteksi antarbingkai, bukan perilaku pelacak. Penghitungan hanya memakai pusat kotak pembatas, sehingga model segmentasi tidak memperoleh keuntungan dari masker dibandingkan RT-DETR yang berbasis kotak.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Data dikumpulkan di kebun jeruk komersial di Gubernuran Beheira (30,5702° LU, 30,2131° BT) pada musim praapanen ketika buah telah mencapai kematangan komersial dan warna penuh. Sebanyak 618 citra beresolusi 3024 × 4032 piksel diambil dengan kamera telepon pintar dari berbagai sudut dan jarak, termasuk sudut miring untuk memasukkan buah yang separuh tersembunyi di dalam tajuk. Jumlah pohon dan kultivar tidak dilaporkan. Video untuk estimasi hasil berjumlah 15, diambil dengan kamera genggam.

### 2. Anotasi dan pembagian data

Citra dianotasi sebagai masker poligon di Roboflow. Buah berkelas Defective bila menunjukkan gejala penyakit (misalnya kanker jeruk, bercak hitam, busuk kulit), kerusakan fisik (tusukan, retak, remuk), atau perubahan warna atau bentuk yang jelas abnormal; sisanya Good. Dua anotator melabeli seluruh dataset secara independen dan peninjau ketiga memutuskan semua perbedaan. Data latih mengandung 376 instans Good dan 239 Defective (615 instans, rasio sekitar 61:39).

Pembagian dilakukan sebelum augmentasi, yaitu 515 citra latih, 50 validasi, dan 53 uji buta (83,3:8,1:8,6). Augmentasi luring di Roboflow hanya diterapkan pada data latih dengan faktor 3, menghasilkan 515 × 3 = 1.545 citra. Transformasi mencakup rotasi ±15°, pembalikan horizontal dan vertikal, serta perubahan kecerahan dan eksposur.

### 3. Pelatihan model

Pelatihan memakai satu stasiun kerja (Intel Core i9-14900HX, RAM 16 GB, NVIDIA RTX 4070 8 GB) dengan *seed* tetap 0. YOLOv8 dan YOLOv11 dilatih dengan Ultralytics 8.3.143 memakai AdamW (laju belajar awal 1,667 × 10^-3), pemanasan 3 epoch, penurunan kosinus, maksimum 300 epoch, dan penghentian dini dengan kesabaran 50. Mask R-CNN (Detectron2 0.6, ResNet-50 + FPN) memakai SGD (laju 0,001, ukuran *batch* 4) selama 6.400 iterasi. RT-DETR-l memakai AdamW, resolusi masukan 640 × 640, dan 300 *object query*.

### 4. Pelacakan dan penghitungan

BoT-SORT memprediksi posisi lintasan dengan filter Kalman dan mengasosiasikan deteksi lewat tumpang tindih IoU. Konfigurasi: max_age 30, min_hits 3, iou_threshold 0,30, GMC dengan aliran optik jarang (*sparse optical flow*) dan faktor penurunan skala 2. Garis penghitung dipasang di $x_{\text{line}} = 0{,}85W$ untuk lebar bingkai $W$; nilai ini dinyatakan penulis sebagai parameter empiris khusus protokol validasi ini. Lintasan dihitung bila pusat kotak berpindah dari kiri garis pada bingkai $t-1$ ke garis atau lebih pada bingkai $t$, dan bendera biner memastikan satu lintasan hanya dihitung sekali.

### 5. Metrik

Segmentasi dinilai dengan mAP@0,5, presisi, *recall*, dan F1, ditambah latensi, jumlah parameter, GFLOPs, serta waktu pelatihan. Estimasi hasil dinilai dengan galat relatif bertanda per video dan *Weighted Mean Absolute Percentage Error* (WMAPE), yaitu jumlah galat mutlak dibagi jumlah acuan lintas video.

## Eksperimen dan Hasil

### Segmentasi statis

Seluruh model segmentasi melampaui mAP@0,5 sebesar 0,88. YOLOv11l mencapai mAP@0,5 0,932 (presisi 0,88, *recall* 0,865, F1 0,87). Mask R-CNN memiliki *recall* 0,953 dengan presisi 0,82. RT-DETR (metrik tingkat kotak) mencatat presisi 0,753, *recall* 0,860, F1 0,803, dan mAP@0,5 0,827; penulis menyatakan metrik kotak dan masker tidak sepenuhnya sebanding. YOLOv11x (62,0 juta parameter) turun ke 0,902, yang ditafsirkan penulis sebagai kelebihan parameter pada data terbatas. Pada tingkat kelas, rata-rata *recall* Defective sekitar 0,93 dan Good 0,761, sedangkan rata-rata presisi Good 0,905 dan Defective 0,804 (Tabel 7).

| Model | Latensi per citra | Parameter | GFLOPs |
|---|---|---|---|
| YOLOv11l | 26,1 ms | 27,6 juta | 141,9 |
| Mask R-CNN | 67,8 ms | 43,9 juta | 265,5 |
| RT-DETR | 22,1 ms | sekitar 32,0 juta | 103,4 |
| YOLOv8l | tidak dilaporkan pada teks | 45,9 juta | 220,1 |

Waktu pelatihan YOLOv11l adalah 55,38 menit selama 158 epoch, Mask R-CNN 120 menit (berhenti pada 50 epoch), RT-DETR 48,66 menit (78 epoch), dan YOLOv11x 1.232,7 menit.

### Estimasi hasil dinamis

Dari 15 video, enam video dipilih sebagai tolok ukur formal (kepadatan rendah 20–70 buah, sedang 100–200, tinggi dengan oklusi berat 400). Sembilan video sisanya hanya dipakai untuk kalibrasi pelacak dan tidak dimasukkan ke tolok ukur. Acuan hitung dibuat di lapangan oleh penaksir hasil profesional melalui penghitungan fisik sepanjang lintasan tetap yang dilalui bersama operator kamera; karena itu acuan hanya mencakup buah yang terlihat sepanjang jalur yang difilmkan, bukan seluruh beban buah pohon. Acuan total enam video: 70, 200, 100, 200, 400, dan 20 buah. Dari 990 buah acuan, 14 berkelas Defective (sekitar 1,4%).

| Model | WMAPE (%) | Hitungan Video 5 (acuan 400) |
|---|---|---|
| RT-DETR | 5,66 | 418 |
| YOLOv11s | 6,97 | 408 |
| Mask R-CNN | 7,47 | 383 |
| YOLOv11x | 8,79 | 403 |
| YOLOv8l | 9,09 | 431 |
| YOLOv8m | 10,30 | 386 |
| YOLOv8s | 11,52 | 372 |
| YOLOv11m | 14,95 | 350 |
| YOLOv11l | 20,10 | 336 |
| YOLOv8n | 25,66 | 297 |
| YOLOv11n | 32,12 | 546 |
| YOLOv8x | 46,67 | 636 |

RT-DETR tidak membedakan mutu secara andal: model ini melaporkan nol buah Defective pada Video 1–5 (acuan 1, 1, 2, 4, dan 3) dan pada Video 6 memberi 20 dari 23 buah sebagai Defective, padahal acuannya 3. Penulis menafsirkan kegagalan penghitungan lewat dua mekanisme: kedipan deteksi (*flicker*) yang membuat satu buah mendapat identitas baru dan dihitung berulang (dominan pada YOLOv8x dan YOLOv11n), serta lintasan yang terputus saat buah terhalang sebagian sehingga tidak pernah mencapai garis (dominan pada YOLOv11l). Penulis menyimpulkan bahwa stabilitas deteksi temporal, bukan mAP statis, menjadi faktor dominan keandalan penghitungan.

## Kelebihan dan Keterbatasan

Kelebihan menurut makalah: jalur terpadu dari segmentasi, penilaian mutu, dan penghitungan berbasis pelacakan; pembagian data dilakukan sebelum augmentasi; konfigurasi pelacak dipilih hanya dari sembilan video pengembangan yang terpisah dari enam video tolok ukur; acuan hitung diperoleh di lapangan oleh penaksir profesional; dan semua model dibandingkan dengan pelacak serta aturan hitung yang identik.

Keterbatasan yang dinyatakan penulis: (1) seluruh hasil berasal dari satu kali pelatihan tanpa estimasi dispersi, sehingga selisih 1,31 poin WMAPE antara RT-DETR dan YOLOv11s bertumpu pada satu kali jalan; (2) prevalensi buah Defective pada video dinamis hanya sekitar 1,4%, sehingga ketelitian penilaian mutu dinamis bertumpu pada jumlah absolut yang sangat kecil dan perlu divalidasi pada rekaman kaya cacat; (3) nilai 0,85W untuk garis hitung dipilih secara empiris untuk protokol ini; (4) acuan hanya mencakup buah yang tampak pada lintasan rekaman, bukan total buah pohon; (5) data tersedia hanya atas permintaan; (6) pekerjaan lanjutan mencakup sensor kedalaman untuk ukuran 3D dan manipulator mobil.

Menurut pembacaan ringkasan ini: hanya enam video tolok ukur dipakai dengan satu pembagian data, sehingga peringkat WMAPE antarmodel (terutama selisih kecil antara model teratas) rentan terhadap pemilihan video. Hasil statis dilaporkan pada 53 citra uji dan 50 citra validasi, sehingga selisih mAP kecil antarmodel tidak dapat dibedakan dari variasi sampel. Garis hitung satu arah dengan lintasan kamera yang bergeser lateral membuat metode ini bergantung pada protokol akuisisi. Hitungan juga dilakukan dari satu pandangan sepanjang jalur sehingga buah di sisi jauh tajuk tidak dicakup. Selain itu, perbandingan latensi dilakukan pada GPU 8 GB tanpa pengujian pada perangkat tepi.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali dalam satu video melalui pelacakan antarbingkai: BoT-SORT dengan kompensasi gerak kamera memberi identitas persisten, dan garis virtual vertikal memastikan satu identitas dihitung tepat satu kali. Mekanisme ini bekerja pada satu lintasan video kamera genggam; tidak ada pencocokan identitas antarsisi pohon atau antarlintasan terpisah, dan tidak ada rekonstruksi 3D (pengukuran kedalaman disebut sebagai pekerjaan mendatang).

Hitungan dilaporkan per kelas (Good dan Defective) pada Tabel 8, dan kelas ditentukan pada saat lintasan melintasi garis. Acuan hitungnya adalah penghitungan fisik di lapangan oleh penaksir profesional sepanjang lintasan yang difilmkan, bukan hasil panen dan bukan anotasi citra. Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah desain evaluasi yang memisahkan akurasi total dari akurasi per kelas, serta pengamatan bahwa model dengan mAP statis tertinggi tidak otomatis memberi hitungan terbaik. Bukti per kelas pada makalah ini sangat tipis (14 buah Defective dari 990), sehingga ia lebih berguna sebagai peringatan metodologis daripada sebagai bukti ketelitian per kelas. Identitas lintas sisi pohon tidak ditangani.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `farhoud2026instance`.

Farhoud dkk. membangun dataset segmentasi instans jeruk Mesir (618 citra asli, 1.545 citra latih hasil augmentasi, 15 video) dan membandingkan YOLOv8, YOLOv11, Mask R-CNN, serta RT-DETR untuk penilaian mutu statis dan estimasi hasil dinamis dengan BoT-SORT dan penghitungan garis virtual. YOLOv11l mencapai mAP@0,5 0,932 pada penilaian statis, sedangkan pada enam video tolok ukur RT-DETR memberi WMAPE total terendah (5,66%) tanpa penilaian mutu yang andal dan YOLOv11s terbaik di antara model segmentasi (6,97%). Penulis menyimpulkan bahwa akurasi penghitungan dan kemampuan penilaian mutu merupakan sifat yang terpisah, dan bahwa hasil bertumpu pada satu kali pelatihan tanpa estimasi dispersi.

Catatan verifikasi data: Angka mAP@0,5, presisi, *recall*, dan F1 model utama terdapat pada teks di Seksi 4.1 dan Gambar 9 (nilai Gambar 9 sendiri berupa gambar dan tidak terbaca dari teks; angka dikutip dari narasi Seksi 4.1 dan abstrak). Angka tingkat kelas diambil dari Tabel 7, latensi dari Seksi 4.2, parameter dan GFLOPs dari Seksi 4.3, waktu pelatihan dari Seksi 4.4, hitungan per video dari Tabel 8, dan WMAPE serta galat relatif dari Tabel 9. Pembagian 515/50/53 dan faktor augmentasi 3 berasal dari Seksi 3.1.3, sedangkan jumlah instans 376 dan 239 dari Seksi 3.1.2. Latensi YOLOv8l, nilai mAP semua varian lain di luar yang disebut narasi, dan jumlah pohon atau kultivar tidak dapat diverifikasi dari teks. Teks ekstraksi tabel terbaca utuh, tetapi kolom tabel terpecah per baris sehingga pembacaan Tabel 8 dilakukan berdasarkan urutan nilai.
