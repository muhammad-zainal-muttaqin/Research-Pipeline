# 011 - PP-YOLO: An Effective and Efficient Implementation of Object Detector

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `long2020ppyolo` |
| Judul asli | PP-YOLO: An Effective and Efficient Implementation of Object Detector |
| Penulis | Xiang Long, Kaipeng Deng, Guanzhong Wang, Yang Zhang, Qingqing Dang, Yuan Gao, Hui Shen, Jianguo Ren, Shumin Han, Errui Ding, Shilei Wen (Baidu Inc) |
| Tahun | 2020 |
| Venue | arXiv preprint arXiv:2007.12099 |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2007.12099
- **Kode sumber (PaddleDetection):** https://github.com/PaddlePaddle/PaddleDetection
- **Google Scholar:** https://scholar.google.com/scholar?q=PP-YOLO%3A%20An%20Effective%20and%20Efficient%20Implementation%20of%20Object%20Detector
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=PP-YOLO%3A%20An%20Effective%20and%20Efficient%20Implementation%20of%20Object%20Detector&sort=relevance

## Gambaran Umum

PP-YOLO adalah detektor objek satu tahap yang dibangun tim Baidu di atas YOLOv3 (bab 003) dengan kerangka kerja PaddlePaddle. Tujuannya secara eksplisit bukan mengusulkan arsitektur baru, melainkan menyusun detektor dengan keseimbangan efektivitas dan efisiensi yang siap dipakai pada aplikasi nyata. Dua perubahan besar dilakukan: *backbone* (jaringan ekstraksi fitur di awal detektor) DarkNet-53 diganti dengan ResNet50-vd yang tahap terakhirnya memakai konvolusi deformable, dan sepuluh trik dari literatur diseleksi satu per satu dengan syarat tidak menaikkan biaya inferensi secara berarti.

Hasil akhirnya pada COCO test-dev adalah 45,2% AP pada kecepatan 72,9 FPS (GPU V100, ukuran masukan 608), mengungguli YOLOv4 yang pada resolusi sama mencapai 43,5% AP pada 62 FPS. Karena kenaikan akurasi diperoleh dari trik yang hampir tidak menambah parameter maupun biaya komputasi, bab ini berfungsi sebagai resep rekayasa: urutan pemasangan trik beserta kontribusi masing-masing dilaporkan terbuka dan dapat ditiru.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pada 2020, YOLOv3 telah menjadi detektor yang paling banyak dipakai di industri karena cepat dan mudah dilatih, tetapi akurasinya tertinggal dari detektor dua tahap. YOLOv4 (bab 004), yang terbit beberapa bulan sebelum makalah ini, membuktikan bahwa kumpulan trik pelatihan dan modul murah dapat mengangkat akurasi YOLOv3 secara besar. Namun YOLOv4 memakai backbone CSPDarknet-53 dan menyertakan eksplorasi augmentasi data yang ekstensif, sehingga sebagian resepnya mahal untuk direplikasi.

Dua celah dibiarkan terbuka. Pertama, belum jelas kombinasi trik mana yang efektif bila dipasang berurutan pada YOLOv3, karena trik yang berguna sendirian belum tentu berguna bila digabungkan. Kedua, backbone DarkNet-53 kurang dioptimalkan oleh kerangka kerja pembelajaran mendalam dibandingkan ResNet, padahal pada penerapan nyata kecepatan inferensi sangat ditentukan oleh kualitas optimasi pustaka terhadap jaringan yang dipakai. Masalah yang dipecahkan makalah ini dirumuskan sebagai berikut: bagaimana menyusun detektor praktis yang akurat dan cepat dari komponen yang sudah ada, tanpa merancang arsitektur baru dan tanpa pencarian hiperparameter otomatis (NAS) yang mahal.

## Ide Utama

Gagasan inti PP-YOLO adalah memperlakukan pembangunan detektor sebagai resep rekayasa, bukan sebagai penelitian arsitektur. Titik tolaknya YOLOv3 utuh; backbone-nya ditukar dengan varian ResNet yang lebih didukung pustaka optimasi; kemudian sepuluh trik yang sudah terpublikasi dipasang satu demi satu. Setiap trik hanya diterima bila menaikkan akurasi tanpa menambah jumlah parameter dan FLOPs (jumlah operasi *floating point*, ukuran biaya komputasi model) secara berarti.

Masukannya tetap citra RGB dan keluarannya tetap kisi prediksi YOLOv3. Yang berubah adalah kualitas tiap komponen di sepanjang alur: ekstraksi fitur lebih baik, pelatihan lebih stabil, fungsi loss selaras dengan metrik evaluasi, skor deteksi memperhitungkan ketepatan lokalisasi, dan pasca-pemrosesan berjalan paralel. Karena hampir semua perubahan bekerja saat pelatihan atau menelan biaya di bawah satu milidetik, kecepatan inferensi praktis tidak berkurang.

## Cara Kerja Langkah demi Langkah

### Backbone: ResNet50-vd-dcn

YOLOv3 asli memakai backbone DarkNet-53; PP-YOLO menggantinya dengan ResNet50-vd, varian ResNet-50 berkoneksi sisa (*residual*) yang jalur pintasannya diperhalus saat resolusi diturunkan sehingga informasi tidak hilang. Penggantian langsung ternyata menurunkan akurasi, karena parameter dan FLOPs ResNet50-vd lebih kecil dari DarkNet-53. Sebagai kompensasi, seluruh konvolusi 3×3 pada tahap terakhir diganti konvolusi deformable (DCN, *deformable convolution*): konvolusi yang posisi pencuplikannya digeser oleh offset yang dipelajari, sehingga dapat mengikuti bentuk objek yang tidak beraturan. DCN hanya dipasang pada tahap terakhir karena terlalu banyak DCN memperlambat inferensi. Keluaran tahap 3, 4, dan 5 backbone dinamai C3, C4, C5.

### Neck FPN dan Head YOLOv3

Bagian *neck* (penghubung) memakai FPN (*Feature Pyramid Network*): modul yang menggabungkan peta fitur dalam (kaya makna, miskin detail spasial) dengan peta fitur dangkal (kaya detail) melalui koneksi lateral, menghasilkan piramida fitur tiga tingkat P3, P4, P5. Untuk citra W×H, resolusi Pl adalah W/2^l × H/2^l; pada masukan 608×608, P5 berukuran 19×19 dan P3 berukuran 76×76. *Head* (kepala prediksi) persis milik YOLOv3: satu konvolusi 3×3 diikuti konvolusi 1×1 per skala, dengan keluaran 3(K+5) kanal. Setiap lokasi pada peta keluaran dikaitkan dengan tiga *anchor* (kotak acuan berukuran tetap yang menjadi titik tolak regresi kotak), masing-masing memprediksi K probabilitas kelas, 4 koordinat kotak, dan 1 skor *objectness* (keyakinan adanya objek).

Posisi penyuntikan trik pada arsitektur ditunjukkan diagram berikut:

```
citra masukan (mis. 608x608)
        │
        ▼
┌──────────────────────────┐
│ backbone ResNet50-vd-dcn │  konv 3x3 tahap terakhir = DCN
└───┬────────┬─────────┬───┘
   C5│      C4│       │C3
     ▼        ▼        ▼
┌──────────────────────────┐
│ FPN: P5, P4, P3          │  * SPP hanya di peta teratas
│ (koneksi lateral)        │  ▲ DropBlock hanya di FPN
└───┬────────┬─────────┬───┘  ● CoordConv di konv 1x1 FPN
   P5│      P4│       │P3       dan konv pertama head
     ▼        ▼        ▼
┌──────────────────────────┐
│ head YOLOv3 per skala:   │  konv 3x3 → konv 1x1
│ keluaran 3(K+5) kanal    │  + cabang prediksi IoU
└────────────┬─────────────┘
             ▼
  skor = kelas x objectness x IoU prediksi
             ▼
       Matrix NMS (paralel)
             ▼
        deteksi akhir
```

### Trik Pelatihan: Ukuran Batch, EMA, DropBlock

Tiga trik pertama hanya mengubah cara melatih. Ukuran *batch* (jumlah citra per langkah pembaruan bobot) dinaikkan dari 64 menjadi 192 untuk menstabilkan pelatihan, dengan penyesuaian laju pembelajaran. EMA (*Exponential Moving Average*) memelihara parameter bayangan W_EMA = λW_EMA + (1−λ)W dengan peluruhan λ = 0,9998; evaluasi memakai parameter bayangan yang lebih halus, bukan bobot akhir pelatihan. DropBlock adalah dropout terstruktur yang mematikan satu wilayah bersebelahan pada peta fitur sekaligus, bukan satuan acak; pada PP-YOLO ia hanya dipasang di FPN karena pemasangan di backbone justru menurunkan akurasi.

### Trik Loss dan Skor: IoU Loss, IoU Aware, Grid Sensitive

IoU (*Intersection over Union*) adalah rasio luas irisan terhadap luas gabungan dua kotak, dan menjadi dasar metrik AP. YOLOv3 meregresi kotak dengan loss L1 yang tidak selaras dengan IoU; PP-YOLO menambahkan cabang loss IoU di samping loss L1, bukan menggantinya seperti yang dilakukan YOLOv4. IoU Aware menambah cabang kecil yang memprediksi IoU antara kotak prediksi dan kotak kebenaran; saat inferensi, skor akhir dihitung sebagai probabilitas kelas × objectness × IoU prediksi, sehingga kotak yang posisinya lebih tepat mendapat peringkat lebih tinggi saat penyortiran. Biayanya hanya 0,01% parameter dan 0,0001% FLOPs. Grid Sensitive mengubah dekode pusat kotak dari x = s(gx + σ(px)) menjadi x = s(gx + ασ(px) − (α−1)/2) dengan α = 1,05. Fungsi sigmoid σ bernilai antara 0 dan 1, sehingga bentuk asli tidak pernah menghasilkan pusat tepat pada batas sel: pusat pada batas gx = 3 menuntut σ(px) = 0, yang tidak terjangkau. Rentang baru, yaitu −0,025 sampai 1,025, menutup kedua batas sel; trik ini menambah waktu pasca-pemrosesan hanya sekitar 0,1 milidetik.

### Trik Pasca-Pemrosesan dan Modul Murah: Matrix NMS, CoordConv, SPP

NMS (*Non-Maximum Suppression*) membuang kotak ganda yang saling menutupi dengan menyisakan kotak berskor tertinggi; versi klasiknya berjalan sekuensial, satu kotak demi satu kotak. Matrix NMS, yang dipinjam dari SOLOv2, merumuskan peluruhan skor gaya Soft-NMS sebagai operasi matriks sehingga dapat dieksekusi paralel di GPU dan lebih cepat tanpa kehilangan akurasi. CoordConv menambahkan dua kanal koordinat (posisi x dan y piksel) pada masukan konvolusi agar jaringan dapat mempelajari ketergantungan posisi; ia hanya dipasang pada konvolusi 1×1 di FPN dan konvolusi pertama head, dengan tambahan 0,03 juta parameter dan 0,05 GFLOPs. SPP (*Spatial Pyramid Pooling*) menggabungkan keluaran *max-pooling* berukuran 1, 5, 9, dan 13 pada peta fitur teratas untuk memperluas wilayah penglihatan (*receptive field*); karena kanal masukan konvolusi sesudahnya membesar, trik ini menambah sekitar 1 juta parameter dan 0,36 GFLOPs, atau sekitar 2% parameter dan 1% FLOPs model.

### Model Pralatih yang Lebih Baik

Trik terakhir adalah inisialisasi: backbone diawali dari ResNet50-vd hasil distilasi pada ImageNet — proses di mana model guru yang lebih besar mengajar model kecil — alih-alih bobot pralatih biasa. Karena hanya mengganti titik awal pelatihan, trik ini sama sekali tidak memengaruhi arsitektur maupun biaya inferensi.

## Eksperimen dan Hasil

Seluruh eksperimen dilakukan pada dataset COCO: sekitar 118 ribu citra trainval35k untuk pelatihan, 5 ribu citra minival untuk ablasi, dan sekitar 20 ribu citra test-dev untuk penilaian akhir. Pelatihan memakai SGD selama 250 ribu iterasi pada 8 GPU, laju pembelajaran awal 0,01 yang dibagi sepuluh pada iterasi ke-150 ribu dan ke-200 ribu, pelatihan multi-skala 320–608 piksel, dan augmentasi MixUp (pencampuran dua citra beserta labelnya). Kecepatan diukur pada satu GPU V100 dengan batch 1, tanpa dan dengan TensorRT (pustaka optimasi inferensi NVIDIA).

Ablasi pada minival menunjukkan kontribusi tiap langkah secara berurutan. YOLOv3 dasar (model A) memperoleh 38,9% AP. Penggantian backbone menjadi ResNet50-vd-dcn (B) menghasilkan 39,1% dengan parameter, FLOPs, dan waktu inferensi lebih kecil. Paket strategi pelatihan — batch besar, EMA, DropBlock (C) — melompat ke 41,4%, kenaikan 2,3 poin yang menjadi lompatan terbesar dalam resep ini. Berturut-turut kemudian IoU Loss (D) 41,9%, IoU Aware (E) 42,5%, Grid Sensitive (F) 42,8%, Matrix NMS (G) 43,4%, CoordConv (H) 43,9%, SPP (I) 44,2%, dan model pralatih distilasi (J) 44,5%. Interpretasinya: tidak ada satu trik yang dominan; kenaikan total 5,6 poin dari A ke J adalah akumulasi banyak perbaikan kecil yang masing-masing terverifikasi hampir tidak menaikkan biaya inferensi.

Hasil akhir pada test-dev 2017: pada masukan 608, PP-YOLO mencapai 45,2% AP pada 72,9 FPS tanpa TensorRT dan 155,6 FPS dengan TensorRT. Pada resolusi yang sama YOLOv4 mencapai 43,5% AP pada 62 FPS, sehingga PP-YOLO unggul 1,7 poin AP sekaligus lebih cepat sekitar 18%. EfficientDet-D3 sedikit lebih akurat (45,8%) tetapi hanya berjalan sekitar 34,5 FPS, kurang dari setengah kecepatan PP-YOLO. Seri hasil pada resolusi 320/416/512/608 — dari 39,3% AP pada 132,2 FPS sampai 45,2% AP pada 72,9 FPS — memperlihatkan bahwa pengguna dapat memilih titik kerja sesuai anggaran latensi. Percepatan TensorRT pada PP-YOLO (sekitar 100%) lebih besar daripada pada YOLOv4 (sekitar 70%); menurut penulis, hal ini disebabkan optimasi TensorRT terhadap ResNet lebih matang daripada terhadap Darknet.

## Kelebihan dan Keterbatasan

Kelebihan utama PP-YOLO adalah kepraktisan. Resepnya terbuka per langkah, backbone-nya didukung luas oleh pustaka optimasi, kode dan modelnya dirilis dalam basis kode PaddleDetection, dan kenaikan akurasinya tidak dibayar dengan latensi. Sebagai bukti konsep, makalah ini menunjukkan bahwa seleksi trik yang disiplin dapat mengalahkan desain yang lebih baru pada pertukaran kecepatan-akurasi.

Keterbatasannya bersifat dua lapis. Dari sisi kontribusi, makalah ini murni rekayasa kombinatorik: tidak ada komponen baru, dan penulis sendiri menyatakan trik-trik tersebut tidak independen, sehingga resepnya belum tentu berpindah utuh ke detektor lain. Dari sisi desain, PP-YOLO tetap detektor berbasis anchor dengan kepala YOLOv3; kelemahan pada objek kecil terlihat dari rincian AP objek kecil 26,3% berbanding AP objek besar 57,2% pada konfigurasi 608. Dari sisi rekayasa, implementasi asli terikat pada PaddlePaddle dan pengukuran kecepatan dilakukan pada lingkungan penulis (V100), sehingga angka FPS pembanding sebaiknya dibaca sebagai perbandingan internal, bukan nilai absolut. Selain itu, augmentasi data dan pencarian arsitektur sengaja tidak dieksplorasi, sehingga ruang perbaikan masih terbuka.

## Kaitan dengan Bab Lain

Bab ini mewarisi hampir seluruh kerangka dari [bab 003 (YOLOv3)](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md): kisi prediksi tiga skala, anchor, dan bentuk kepala deteksi. Hubungannya dengan [bab 004 (YOLOv4)](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md) bersifat paralel sekaligus komplementer: keduanya menyusun ulang YOLOv3 dengan kumpulan trik, tetapi PP-YOLO meminjam Grid Sensitive dan SPP dari YOLOv4 sambil memilih jalur backbone ResNet dan himpunan trik yang berbeda. Garis ini berlanjut pada penerus internalnya, PP-YOLOv2 dan PP-YOLOE, yang tidak tercakup dalam entri tinjauan ini. Jalur berbeda diambil [bab 005 (YOLOX)](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md) yang melepaskan anchor sekaligus memodernisasi penetapan label, sedangkan fondasi formulasi kisi itu sendiri dibahas pada [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md).

## Poin untuk Sitasi

Kutip dengan kunci `long2020ppyolo`. Ringkasan yang aman dikutip: "PP-YOLO menyusun ulang YOLOv3 di atas backbone ResNet50-vd-dcn dengan sepuluh trik yang hampir tidak menambah parameter dan FLOPs, mencapai 45,2% AP pada COCO test-dev dengan kecepatan 72,9 FPS di V100 — lebih akurat dan lebih cepat dari YOLOv4 pada resolusi yang sama." Seluruh angka berasal dari naskah arXiv versi v3; makalah ini berstatus preprint tanpa tinjauan sejawat. Angka ablasi per trik (seri A sampai J, dari 38,9% ke 44,5% pada minival) dan rincian biaya tiap trik dikutip dari Tabel 1 dan teks naskah; verifikasi ulang ke tabel aslinya disarankan sebelum sitasi formal.
