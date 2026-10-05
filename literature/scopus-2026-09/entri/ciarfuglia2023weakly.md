# Weakly and semi-supervised detection, segmentation and tracking of table grapes with limited and noisy data

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ciarfuglia2023weakly` |
| Judul asli | Weakly and semi-supervised detection, segmentation and tracking of table grapes with limited and noisy data |
| Penulis | Ciarfuglia, Thomas A.; Motoi, Ionut M.; Saraceni, Leonardo; Fawakherji, Mulham; Sanfeliu, Alberto; Nardi, Daniele |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [ciarfuglia2023weakly.pdf](../pdf/ciarfuglia2023weakly.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.107624

## Gambaran Umum

Makalah ini mengusulkan sistem pembangkitan label semu (*pseudo-label generation*, PLG) untuk melatih detektor dan model segmentasi instans anggur meja (*table grape*) dengan data berlabel yang sedikit dan sederhana. Sistem terdiri dari dua bagian. Bagian pertama menghasilkan kotak pembatas semu dari video ponsel dengan memanfaatkan konsistensi geometris antarbingkai (*structure from motion*, SfM, atau pencocokan fitur 2D dengan RANSAC). Bagian kedua menghasilkan masker semu dari kotak pembatas dengan Mask R-CNN lalu memperbaikinya dengan dilasi, SLIC, atau GrabCut. Pencacahan tandan untuk estimasi hasil panen dilakukan dengan menghitung jumlah lintasan (ID) dari pelacak.

Data target berasal dari kebun anggur meja di Aprilia, Lazio selatan, Italia, dengan fokus pada varietas Black Pizzutello. Data sumber adalah Embrapa WGISD (anggur wine). Data target terdiri dari 1.469 bingkai video HD (1280 × 720, 10 Hz) yang direkam dengan ponsel MotoG8 Plus (TVid) dan 134 citra diam 3000 × 4000 (TImg). Hanya segmen video 10 detik yang diberi label untuk uji pelacakan.

Hasil utama: pada TImg, detektor sumber (SDet) memiliki mAP0,5 0,69 dan detektor target (TDet) 0,77. Pada pelacakan, galat estimasi hasil panen pelacak berbasis SfM turun dari 38% (hanya data WGISD) menjadi 9% (dengan label semu), dan pelacak DeepSORT turun dari 48% menjadi 26%. Pada segmentasi, mAP0,5:0,95 naik dari 32,88 (garis dasar WGISD) menjadi 49,56 dengan data TImg berlabel semu dan GrabCut.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi, segmentasi, dan pelacakan buah mendukung pemanenan robotik dan estimasi hasil panen, tetapi algoritma modern memerlukan banyak data berlabel. Pengumpulan data mahal, sehingga usaha tani kecil dan menengah sulit memanfaatkannya. Sistem yang ada sering mengurangi variabilitas lewat perangkat keras, misalnya iluminasi buatan yang dijalankan pada malam hari atau mesin *straddle*, yang menurut penulis tidak mudah diadaptasi ke budi daya lain dan memerlukan investasi besar.

Penulis menetapkan skenario ketika sebagian kecil data berlabel dari tanaman serupa (data sumber, SD) tersedia, tetapi tidak cukup untuk kebun lain dengan pergeseran kovariat (*covariate shift*) yang jelas (data target, TD). Perbedaan SD dan TD mencakup varietas (anggur wine dibanding anggur meja, bentuk dan warna buah), kondisi iluminasi (sinar matahari penuh dibanding bayangan), perangkat kamera (kamera refleks dibanding ponsel), dan skala citra. Anggur dipilih karena sulit disegmentasi akibat oklusi, warna, dan iluminasi.

## Ide Utama

Gagasan utamanya adalah ekonomi pelabelan dan pemakaian ulang data: satu-satunya data baru yang diperlukan adalah video yang direkam di lapangan, misalnya dengan ponsel. Detektor yang dilatih pada data sumber memberi taksiran kotak awal pada bingkai kunci (*keyframe*) dengan ambang keyakinan tinggi. Korespondensi geometris antarbingkai kemudian memindahkan kotak itu ke bingkai di antaranya. Bingkai-bingkai itu menjadi data latih untuk detektor target. Untuk segmentasi, kotak pembatas dipakai sebagai petunjuk (*cue*) eksternal bagi cabang masker Mask R-CNN sehingga bias konfirmasi (*confirmation bias*) berkurang, lalu masker diperbaiki dengan metode visi komputer klasik.

Konsistensi geometris juga dimanfaatkan untuk identitas objek: satu tandan anggur yang tampak pada beberapa bingkai berurutan dihubungkan melalui fitur 2D atau titik 3D yang sama.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Kebun percobaan terdiri dari dua petak sekitar 114 m × 51 m dan 122 m × 48 m (masing-masing 0,58 ha), dengan sistem trelis tradisional *Tendone* berjarak tanam 3 × 3 m dan tertutup plastik serta jaring. Empat varietas ada di kebun: White Pizzutello, Black Pizzutello, Red Globe, dan Black Magic. Usaha pelabelan dipusatkan pada Black Pizzutello. Video direkam dengan bergerak tangensial terhadap barisan tanpa syarat jarak atau tinggi kamera. Total 1.469 bingkai video dipakai. Citra diam TImg berjumlah 134 (3000 × 4000), seluruhnya berlabel kotak pembatas dan 70 citra di antaranya berlabel segmentasi instans, dengan aplikasi Innotescus. Sensor optik dan cip untuk video dan citra diam berbeda, yang disengaja untuk menambah pergeseran kovariat. Jumlah pohon atau tandan pada data target tidak dilaporkan.

### 2. Blok konsistensi geometris

Dua pilihan diuji. Pilihan pertama memakai COLMAP (SfM penuh, pencocokan sekuensial semua-lawan-semua) seperti pada Santos dkk. (2020). Biaya komputasi pada percobaan penulis adalah 5 jam untuk video 500 sampai 600 bingkai HD pada Intel Core i7 3,4 GHz, Nvidia GTX 950M, dan memori 16 GB. Pilihan kedua adalah solusi waktu-nyata: fitur SURF diekstraksi pada bingkai $i$ dan beberapa bingkai berikutnya $i+1, \dots, i+n$, dicocokkan dengan *brute force*, lalu disaring dengan RANSAC berbasis homografi (empat pasangan dipilih acak, homografi dengan konsensus tertinggi dipertahankan). Pendekatan ini mencapai 3 bingkai per detik hanya dengan CPU pada perangkat yang sama. Alasannya, video lapangan berupa jalan lurus tanpa lintasan tertutup sehingga setiap tandan hanya tampak pada beberapa bingkai berurutan.

### 3. Interpolasi kotak pembatas

Dari kotak SDet pada bingkai $i$, pusat kotak pada bingkai $i+n$ ditetapkan pada pusat massa fitur yang cocok, sedangkan ukuran kotak dipertahankan karena kamera diasumsikan bergerak lambat dan tangensial. Parameter *skip value* adalah jumlah bingkai yang diinterpolasi sebelum prediksi SDet baru diambil. Menurut ablasi, *skip* 1 (hanya SDet) lebih rendah daripada *skip* 2, dan *skip* lebih besar tidak menambah keuntungan. *Skip* 2 dipakai sebagai nilai terbaik.

### 4. Detektor dan pelacak

Detektor adalah YOLOv5 varian S dan N, dipilih karena deteksi waktu-nyata dan potensi penerapan tertanam. Pelatihan: 300 *epoch*, *batch* 4, penghentian dini dengan kesabaran 30 *epoch*, jadwal *one cycle* ($lr$ awal 0,01, akhir 0,001), SGD dengan momentum 0,937 dan *weight decay* $5 \times 10^{-4}$, bobot awal MS COCO. Ada 242 citra latih sumber yang diaugmentasi secara luring empat kali menjadi 726 citra tambahan. Dua skema pelacakan dibandingkan: pelacak berbasis deteksi dan SfM (*SfMTrack*, mengikuti Santos dkk.) dan DeepSORT dengan metrik asosiasi dalam. Jumlah tandan diperkirakan dari jumlah ID lintasan. Evaluasi memakai metrik CLEAR MOT (MOTA, MOTP, MT, ML, $ID_{sw}$, FM) pada segmen uji 10 detik.

### 5. Pembangkitan dan perbaikan masker semu

Mask R-CNN (Detectron2, *backbone* ResNet-101) dilatih pada WGISD (SSeg). Pada inferensi, kotak dari kepala deteksi diganti oleh kotak eksternal (kotak GT atau kotak semu dari DPLG) sebagai mekanisme perhatian. Tiga perbaikan masker diuji. Dilasi memakai kernel melingkar 5 × 5. SLIC memakai pustaka scikit-image dengan 2.000 segmen dan kekompakan 0,1: superpiksel yang tertutup lebih dari ambang atas 70% ditambahkan dan yang tertutup kurang dari ambang bawah 30% dibuang. GrabCut dari OpenCV diinisialisasi dengan masker semu sebagai latar depan mungkin, dilasi dan erosi sebanding dengan dimensi kotak terkecil untuk menentukan latar belakang mungkin dan latar depan pasti. Pelatihan segmentasi memakai laju belajar 0,001, *weight decay* 0,0001, momentum 0,9, maksimum 100 *epoch*, dan penghentian dini dengan kesabaran 20.

## Eksperimen dan Hasil

Metrik deteksi dan segmentasi adalah *precision*, *recall*, IoU, dan AP gaya MS COCO. Karena kelasnya hanya satu (anggur), AP sama dengan mAP. Pelacakan dievaluasi dengan metrik CLEAR MOT. Uji pendahuluan pada WGISD (Tabel 1) menunjukkan model YOLOv5 besar hanya sedikit lebih baik daripada varian kecil: mAP0,5 89,4 (YOLOv5n, 1,9 juta parameter), 89,7 (YOLOv5s), 89,5 (m), 90,5 (l), dan 87,5 (x).

Deteksi pada data uji TImg (Tabel 2) dan TVid (Tabel 3):

| Data uji | Model | Precision | Recall | mAP0,5 | mAP0,95 |
|---|---|---|---|---|---|
| TImg | SDet | 0,90 | 0,56 | 0,69 | 0,46 |
| TImg | TDet | 0,98 | 0,68 | 0,77 | 0,47 |
| TVid | SDet | 0,62 | 0,59 | 0,55 | 0,21 |
| TVid | TDet | 0,74 | 0,60 | 0,65 | 0,23 |

Pelacakan pada segmen uji TVid (Tabel 4), dengan jumlah ID acuan (GT IDs) 31 dan deteksi acuan (GT Dets) 721:

| Metode | MOTA | $ID_{sw}$ | IDs | Galat estimasi hasil panen |
|---|---|---|---|---|
| SfMTrack, WGISD | 46,741 | 5 | 19 | 38% |
| SfMTrack, label semu | 55,756 | 9 | 28 | 9% |
| DeepSort, WGISD | 40,499 | 16 | 46 | 48% |
| DeepSort, label semu | 50,624 | 17 | 39 | 26% |

Penulis mencatat bahwa kemampuan mempertahankan ID sepanjang lintasan lebih kuat pada DeepSORT, yang menurut dugaan mereka disebabkan oleh filter Kalman. Pelacak SfM memiliki MOTA lebih tinggi daripada DeepSORT pada sebagian besar nilai *skip*, tetapi tidak dirancang untuk waktu-nyata. Gambar 14 menunjukkan bahwa *skip* 5 masih dapat ditoleransi karena hanya memerlukan 20% bingkai berlabel, dibanding 50% pada *skip* 2.

Segmentasi pada TImg (Tabel 5 dan 6, rerata lima percobaan pada Tabel 6). Garis dasar SSeg memiliki mAP 53,40 pada deteksi WGISD dan 32,65 pada TImg, serta mAP segmentasi 53,60 dan 32,88 secara berturut-turut. Penulis menyebut penurunan lebih dari 20 poin AP.

| Data latih | mAP0,5:0,95 | mAP0,5 | mAP0,75 |
|---|---|---|---|
| WGISD (garis dasar) | 32,88 | 65,40 | 34,77 |
| WGISD + TImg | 48,43 | 83,06 | 53,12 |
| WGISD + TImg, dilasi | 48,67 | 81,54 | 54,87 |
| WGISD + TImg, SLIC | 47,78 | 80,41 | 53,54 |
| WGISD + TImg, GrabCut | 49,56 | 81,03 | 57,70 |

Pada sistem lengkap (Tabel 7), kotak berasal dari YOLO (TDet), bukan dari anotasi: dengan WGISD + TImg (182 citra) GrabCut mAP0,5:0,95 adalah 46,41; WGISD + TVid (687) GrabCut 46,66; WGISD + TImg + TVid (781) tanpa perbaikan 47,44 dan dengan GrabCut 47,81, dibanding garis dasar 32,88 (88 citra). Penulis menyatakan peningkatan terutama terjadi pada IoU di atas 0,75.

## Kelebihan dan Keterbatasan

Keterbatasan dan persyaratan yang dinyatakan penulis: sistem memerlukan deteksi atau segmentasi awal kasar dari data sumber. SfM penuh hanya layak secara luring (5 jam untuk 500 sampai 600 bingkai) dan membatasi panjang video hingga beberapa ratus bingkai. Penulis menyebut pekerjaan lanjutan berupa perbaikan label semu secara iteratif dan penghapusan persyaratan awal agar sistem tanpa pengawasan penuh. Menurut pembacaan ringkasan ini, sistem hanya diuji pada satu varietas (Black Pizzutello) dan satu kebun, dan data tersedia hanya atas permintaan.

Kelebihan yang dinyatakan penulis: hanya perlu video ponsel biasa, tidak memerlukan iluminasi atau mesin khusus, dan dapat dipakai pada buah lain dengan relatif mudah.

Menurut pembacaan ringkasan ini, evaluasi pelacakan hanya memakai satu segmen video 10 detik dengan 31 ID acuan, sehingga selisih galat estimasi (misalnya 38% menjadi 9%) bersumber dari sampel kecil dan tidak disertai ulangan atau selang kepercayaan. Pada SfMTrack, peningkatan label semu disertai kenaikan $ID_{sw}$ dari 5 menjadi 9, sehingga hitungan ID yang mendekati acuan (28 terhadap 31) sebagian dapat berasal dari fragmentasi lintasan yang saling mengimbangi dengan tandan yang terlewat, dan makalah tidak memverifikasi kesesuaian ID dengan tandan fisik. Metrik pelacakan dan hitungan tidak dipisahkan per kelas, karena hanya ada satu kelas.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali dalam konteks video: satu tandan tampak pada beberapa bingkai berurutan, dan identitasnya dipertahankan oleh pelacak, baik dengan korespondensi geometris SfM (COLMAP) maupun dengan DeepSORT. Hitungan tandan adalah jumlah ID lintasan. Penulis sendiri menyebut kegagalan berupa lintasan terfragmentasi dan perpindahan ID akibat oklusi. Hitungan tidak dilaporkan per kelas, karena hanya satu kelas (anggur) yang dipakai. Acuan hitungan adalah anotasi pada video (31 ID dan 721 deteksi acuan pada segmen 10 detik), bukan panen atau hitung manual lapangan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: gagasan memakai korespondensi fitur 2D yang diverifikasi geometris (SURF, RANSAC homografi) untuk menghubungkan objek yang sama antarbingkai, serta pembangkitan label semu dari video untuk mengurangi biaya pelabelan. Asumsi geometri makalah ini adalah gerak kamera tangensial lambat dengan perubahan pandangan kecil, sehingga homografi cukup. Asumsi itu belum tentu berlaku pada pengambilan citra dari beberapa sisi pohon dengan perubahan sudut besar.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `ciarfuglia2023weakly`.

Ciarfuglia dkk. mengusulkan sistem pembangkitan label semu untuk deteksi, segmentasi, dan pelacakan anggur meja dengan data berlabel terbatas. Kotak pembatas semu dibangkitkan dari video ponsel melalui korespondensi geometris antarbingkai, dan masker semu dibangkitkan oleh Mask R-CNN dengan perbaikan GrabCut. Pada segmen uji video 10 detik, galat estimasi hasil panen berbasis jumlah ID lintasan turun dari 38% menjadi 9% (pelacak berbasis SfM) dan dari 48% menjadi 26% (DeepSORT), sedangkan mAP0,5:0,95 segmentasi pada citra target naik dari 32,88 menjadi 49,56.

Catatan verifikasi data: Angka deteksi berasal dari Tabel 2 dan 3, angka pelacakan dari Tabel 4, angka segmentasi dari Tabel 5 sampai 7, dan waktu komputasi serta parameter pelatihan dari seksi 2.6.1, 3.1.1, dan 3.3.1. Teks ekstraksi PDF terbaca baik, tetapi tabel diekstraksi sebagai daftar sel sehingga pemetaan kolom dilakukan berdasarkan urutan baris. Makalah berbahasa Inggris. Teks yang diberikan terpotong setelah daftar pustaka awal, sehingga bagian akhir daftar pustaka tidak diperiksa. Jumlah pohon, jumlah tandan di seluruh kebun, dan hitungan panen aktual tidak dilaporkan. Pada Tabel 4, selisih galat yang disebut penulis (misalnya penurunan 29%) tidak dihitung ulang di sini.
