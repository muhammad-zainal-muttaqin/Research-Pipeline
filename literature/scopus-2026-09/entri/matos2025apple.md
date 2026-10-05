# An Apple Counting System Robust to Multiple Intermittent Occlusions

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `matos2025apple` |
| Judul asli | An Apple Counting System Robust to Multiple Intermittent Occlusions |
| Penulis | Matos, Gon\ccalo P.; Oliveira, Tiago G.; Silva, Filipe; Martinho, Francisco; Le\~ao, Miguel; Fonseca, Filipe; Silvestre, Jos\'e; Costeira, Jo\~ao P.; Saldanha, Ricardo L.; Santiago, Carlos; Morgado, Ernesto M. |
| Tahun | 2025 |
| Venue | Lecture Notes in Computer Science Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [matos2025apple.pdf](../pdf/matos2025apple.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-031-73497-7_15

## Gambaran Umum
Makalah prosiding EPIA 2024 ini mengusulkan sistem pencacahan apel di kebun yang terdiri atas tiga komponen: kamera stereo ZED 2i yang dipegang tangan, detektor YOLOv4 yang dilatih pada citra apel beranotasi, dan algoritme pelacakan 3D berbasis sentroid yang dirancang tahan terhadap oklusi berselang (*intermittent occlusion*), yaitu buah yang tertutup beberapa bingkai lalu muncul kembali. Sistem ini merupakan penyederhanaan dari algoritme pelacakan terdahulu penulis yang memproyeksikan ulang seluruh titik 3D buah, dengan ongkos komputasi yang jauh lebih kecil.

Data diambil di kebun milik INIAV di Alcobaça, Portugal, pada klon apel Gala pada fase BBCH 81 sampai 87. Evaluasi dilakukan pada tiga set data (Galafab-west, Schnico-Red-east, Schniga-Schnico-west) yang berisi 3 sampai 6 pohon per set, dengan acuan berupa seluruh apel yang terlihat pada video, dilacak secara manual.

Hasil utama: galat persentase absolut (*absolute percentage error*, APE) algoritme usulan sebesar 14,59%, 19,66%, dan 57,10% pada ketiga set data, dengan MOTA 0,32, 0,14, dan 0,27. Algoritme pembanding yang memproyeksikan seluruh titik menghasilkan APE 17,17%, 30,34%, dan 5,90%. Waktu pemrosesan turun dari 2 sampai 3 jam menjadi 1,5 sampai 2,5 menit per set data.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pencacahan buah di kebun saat ini dilakukan dengan estimasi hitung manual yang memakan waktu, tidak praktis pada skala besar, dan rawan galat. Tantangan otomatisasinya adalah variasi warna, ukuran, orientasi, dan keterlihatan buah, kondisi cahaya, serta oklusi buah oleh buah lain, ranting, dan daun.

Penulis menilai karya terdahulu memiliki kelemahan masing-masing. Pendekatan *Structure-from-Motion* (SfM) dengan kamera DSLR memerlukan waktu komputasi tinggi. Kamera kedalaman berbasis inframerah bermasalah di bawah sinar matahari langsung dan memerlukan terowongan atau penahan cahaya. Deteksi berbasis warna sensitif terhadap perubahan cahaya dan sulit mengenali apel hijau pada fase awal. Pelacakan sekuensial berbasis kamera monokular mencocokkan deteksi hanya dengan bingkai berikutnya, sehingga satu deteksi yang terlewat memutus lintasan dan buah yang sama terhitung dua kali.

## Ide Utama
Setiap buah yang terdeteksi diwakili oleh satu sentroid 3D dalam kerangka koordinat global yang sama untuk seluruh bingkai. Sentroid dari bingkai sebelumnya diproyeksikan ulang ke bidang citra bingkai saat ini. Bila proyeksi jatuh di dalam kotak deteksi, buah dianggap sama dan memakai ID yang sama; bila tidak, buah dianggap baru. Karena sentroid tetap disimpan selama video, buah yang hilang beberapa bingkai akibat oklusi tetap dapat dikenali kembali ketika muncul lagi. Jumlah buah adalah jumlah ID unik setelah penyaringan.

Kamera stereo dipakai agar peta kedalaman dan pose kamera diperoleh waktu-nyata dari SDK ZED, sehingga SfM yang mahal (COLMAP pada karya terdahulu) tidak diperlukan.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Video direkam dengan ZED 2i yang dipegang tangan dan dihubungkan ke komputer, bergerak kurang lebih lurus sejajar barisan pohon, tanpa penstabil. Beberapa barisan klon Gala direkam saat buah mendekati panen (BBCH 81 sampai 87). Lokasi kebun: lintang 39,549 N, bujur −8,957 W.

### 2. Deteksi 2D
Bingkai tampak kiri diekstraksi dari berkas video ZED dan dianotasi dengan kotak pembatas memakai Makesense. Hanya satu dari setiap 30 bingkai yang dianotasi. Total 183 citra dianotasi, masing-masing berisi sekitar 100 buah. Model yang dipakai adalah YOLOv4 implementasi Darknet, dipralatih pada MS COCO lalu disetel halus pada data sendiri. Penulis memilih v4 karena lisensinya mengizinkan penggunaan komersial.

### 3. Proyeksi ke 3D dan sentroid
Untuk tiap deteksi, piksel dalam kotak diproyeksikan ke koordinat global memakai peta kedalaman bingkai tersebut. Karena sebagian piksel adalah latar belakang, sentroid dihitung sebagai median koordinat titik-titik tersebut.

### 4. Pelacakan
Sentroid dari bingkai-bingkai sebelumnya diproyeksikan ulang dengan persamaan $\lambda [u, v, 1]^T = K [R|t] [X, Y, Z, 1]^T$. Bila proyeksi sebuah sentroid jatuh di dalam kotak deteksi, ID sentroid itu diberikan kepada deteksi dan koordinat sentroid diperbarui dengan merata-ratakan sentroid yang telah dihitung untuk buah tersebut; bila tidak ada, ID baru dibuat. Pembaruan rerata dimaksudkan mengurangi kasus sentroid yang terlalu dekat permukaan buah sehingga proyeksinya keluar kotak dan buah terhitung dua kali.

### 5. Penyaringan dan penghitungan
Buah yang terdeteksi pada kurang dari 5 bingkai di seluruh video diabaikan untuk menekan positif palsu YOLO (aturan yang sama dengan karya terdahulu). Jumlah akhir adalah jumlah ID unik.

## Eksperimen dan Hasil
Tiga bagian barisan pohon yang tidak dipakai pada pelatihan dipilih, masing-masing dari klon berbeda (Schniga Schnico, Schnico Red, Galafab). Tiap bagian terdiri atas 3 sampai 6 pohon yang difilmkan dari satu sisi barisan. Pohon yang dipilih tidak selalu berurutan, sehingga bingkai disunting untuk menutup pohon lain. Penulis menyatakan hitungan manual di lapangan tidak cocok sebagai acuan, karena apel yang terlihat dari satu sisi lebih sedikit daripada seluruh apel pada pohon (pohon dipandu secara *espalier*, sehingga ada buah di sisi lain yang terlihat) dan lebih banyak daripada apel di sisi yang difilmkan. Karena itu seluruh apel pada video dianotasi dan dilacak manual sebagai acuan. Set data ini sama dengan yang dipublikasikan pada karya terdahulu penulis, dengan gerakan kamera tidak teratur, laju bingkai rendah, dan oklusi berselang.

| Set data | Jumlah pohon | Apel acuan | Usulan: estimasi | APE (%) | MOTA | Proyeksi seluruh titik: estimasi | APE (%) | MOTA |
|---|---|---|---|---|---|---|---|---|
| Galafab-west | 3 | 233 | 267 | 14,59 | 0,32 | 193 | 17,17 | 0,49 |
| Schnico-Red-east | 5 | 356 | 286 | 19,66 | 0,14 | 248 | 30,34 | 0,25 |
| Schniga-Schnico-west | 6 | 373 | 586 | 57,10 | 0,27 | 395 | 5,90 | 0,42 |

APE didefinisikan sebagai $|\text{estimasi} - \text{acuan}| / \text{acuan} \times 100$. MOTA (*Multiple Object Tracking Accuracy*) didefinisikan sebagai $1 - (FN + FP + IDS)/GT$.

Penulis menyimpulkan bahwa algoritme usulan sedikit lebih baik dalam galat jumlah total pada dua set data pertama, tetapi jauh lebih buruk pada set ketiga karena penghitungan berlebih. Mereka menduga hal itu akibat derau pada ekstrinsik kamera yang diestimasi waktu-nyata, dengan alasan citra set tersebut lebih sulit bagi odometri visual (dugaan penulis, tidak diuji). Algoritme yang memproyeksikan seluruh titik memiliki MOTA lebih tinggi pada ketiga set, yang ditafsirkan penulis sebagai lintasan yang lebih stabil. Sentroid lebih ringan komputasi sehingga cocok untuk perangkat IoT yang lebih lemah, dengan ongkos akurasi yang lebih rendah. Penggantian COLMAP dengan kamera stereo menurunkan waktu pemrosesan dari 2 sampai 3 jam menjadi 1,5 sampai 2,5 menit per set data.

## Kelebihan dan Keterbatasan
Kelebihan: perangkat keras sederhana dan terjangkau yang dapat dipakai di bawah sinar matahari, pelacakan yang mempertahankan identitas buah melewati oklusi berselang, serta waktu pemrosesan yang jauh lebih pendek daripada jalur berbasis SfM. Evaluasi memakai acuan buah-terlihat-di-video yang dibuat manual, bukan hitungan lapangan.

Keterbatasan yang dinyatakan penulis: kesalahan penghitungan berlebih pada set data ketiga akibat derau pose kamera, akurasi lebih rendah daripada versi proyeksi seluruh titik, dan pengujian yang baru dilakukan secara luring dengan kamera dipegang tangan, belum pada kendaraan pertanian secara daring. Penulis menyebut hasilnya sebagai hasil pendahuluan.

Menurut pembacaan ringkasan ini, evaluasi hanya mencakup 14 pohon pada tiga set data (3, 5, dan 6 pohon), dengan rentang APE 14,59% sampai 57,10% yang lebar, sehingga kesimpulan umum tentang akurasi belum kuat. Hitungan buah juga hanya untuk satu sisi barisan pohon, dan tidak dilaporkan per kelas.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dalam urutan bingkai video. Mekanismenya adalah pelacakan berbasis geometri 3D: sentroid buah dalam koordinat global diproyeksikan ulang ke bingkai berikutnya dan dicocokkan dengan kotak deteksi, ditambah ambang minimal 5 bingkai. Hitungan tidak dilaporkan per kelas, dan buah hanya dibedakan sebagai apel matang yang terdeteksi. Acuan hitung adalah anotasi dan pelacakan manual pada video (buah yang terlihat dari satu sisi), bukan panen dan bukan hitungan lapangan, karena penulis menolak hitungan lapangan sebagai acuan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan identitas berbasis koordinat 3D bersama serta pencocokan proyeksi ke kotak deteksi. Namun pelacakan ini mengandalkan urutan bingkai kontinu dan pose kamera dari SDK stereo, sedangkan skenario multi-sisi memiliki pandangan yang terputus antarsisi. Makalah juga tidak menguji penggabungan identitas lintas sisi pohon: hanya satu sisi barisan yang difilmkan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `matos2025apple`.

Matos dkk. mengusulkan sistem pencacahan apel dengan kamera stereo ZED 2i, detektor YOLOv4, dan pelacakan 3D berbasis sentroid yang menjaga identitas buah melewati oklusi berselang. Pada tiga set data kebun apel, galat persentase absolut jumlah buah adalah 14,59%, 19,66%, dan 57,10%, dengan waktu pemrosesan 1,5 sampai 2,5 menit per set data dibandingkan 2 sampai 3 jam pada jalur SfM terdahulu. Penulis menyebut hasilnya pendahuluan.

Catatan verifikasi data: angka APE, MOTA, dan jumlah estimasi berasal dari Tabel 2 (usulan) dan Tabel 3 (proyeksi seluruh titik); jumlah pohon dan apel acuan dari Tabel 1; 183 citra beranotasi dari Seksi 2.2; ambang 5 bingkai dari Seksi 2.3; dan waktu 2 sampai 3 jam menjadi 1,5 sampai 2,5 menit dari akhir Seksi 3.2. Teks ekstraksi terbaca baik; persamaan dan tabel terbaca walaupun tata letaknya terpecah per baris. Jumlah citra uji, jumlah bingkai video, dan metrik deteksi YOLOv4 (misalnya mAP) tidak dilaporkan dalam teks.
