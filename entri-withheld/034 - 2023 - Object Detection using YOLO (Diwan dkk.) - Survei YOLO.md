# 034 - Object Detection Using YOLO: Challenges, Architectural Successors, Datasets and Applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `diwan2023yolo` |
| Judul asli | Object detection using YOLO: challenges, architectural successors, datasets and applications |
| Penulis | Tausif Diwan, G. Anirudh, Jitendra V. Tembhurne |
| Tahun | 2023 (terbit daring 8 Agustus 2022) |
| Venue | Multimedia Tools and Applications, vol. 82, no. 6, hlm. 9243–9275 |
| Tema | Survei YOLO |

## Tautan Akses
- **DOI (versi penerbit):** https://doi.org/10.1007/s11042-022-13644-y
- **PubMed Central (teks lengkap, akses terbuka):** https://pmc.ncbi.nlm.nih.gov/articles/PMC9358372/
- **Google Scholar:** https://scholar.google.com/scholar?q=Object%20Detection%20Using%20YOLO%3A%20Challenges%2C%20Architectural%20Successors%2C%20Datasets%20and%20Applications
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Object%20Detection%20Using%20YOLO%3A%20Challenges%2C%20Architectural%20Successors%2C%20Datasets%20and%20Applications&sort=relevance

## Gambaran Umum

Makalah ini adalah survei atas detektor objek satu tahap, khususnya keluarga YOLO (*You Only Look Once*) dari versi pertama sampai YOLOv4. Deteksi objek adalah tugas menentukan kelas sekaligus posisi setiap objek dalam sebuah citra; posisi dinyatakan dengan *bounding box*, yaitu kotak persegi yang membingkai objek. Survei ini memetakan empat hal: tantangan dasar deteksi objek, rumusan regresi yang menjadi fondasi YOLO, perkembangan arsitektur antarversi beserta teknik optimasinya, serta dataset, statistik kinerja, dan aplikasi.

Simpulan utama para penulis: silsilah YOLO merupakan rangkaian perbaikan inkremental atas kompromi kecepatan dan akurasi. Detektor satu tahap yang awalnya tertinggal jauh dari detektor dua tahap dalam akurasi kemudian menyamai dan kadang melampauinya, sambil tetap unggul jauh dalam kecepatan inferensi. Para penulis mengklaim survei ini sebagai tinjauan pertama yang khusus membahas detektor satu tahap berbasis YOLO.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum survei ini disusun, literatur deteksi objek berkembang dalam dua jalur. Detektor dua tahap mengusulkan kandidat wilayah citra (*region proposal*) pada tahap pertama, lalu mengklasifikasikan dan memperhalus kotak pada tahap kedua. Keluarga R-CNN mewakili jalur ini: akurat, tetapi berat dan lambat. Detektor satu tahap menilai seluruh wilayah spasial citra dalam satu evaluasi jaringan, sehingga lebih sederhana dan jauh lebih cepat, dengan akurasi awal yang lebih rendah. YOLO, SSD (*Single Shot Detector*), dan RetinaNet termasuk jalur ini.

Dua masalah muncul dari kondisi tersebut. Pertama, tinjauan yang tersedia pada masa itu umumnya berpusat pada detektor dua tahap, padahal YOLO berkembang cepat dan makalah asli tiap versinya tersebar dengan konvensi berbeda. Kedua, praktisi membutuhkan peta yang jelas tentang kapan memilih detektor dua tahap, satu tahap, atau kombinasi keduanya. Survei ini juga merangkum tantangan teknis yang berulang pada semua detektor: variasi ukuran objek (dari 70–80% piksel citra sampai kurang dari 10%), citra beresolusi rendah, objek bertumpuk (oklusi), ketimpangan contoh objek dan latar, kebutuhan data berlabel dan komputasi yang besar, serta galat lokalisasi karena kotak prediksi ikut memuat piksel latar.

## Ide Utama

Gagasan inti yang disarikan survei ini adalah rumusan deteksi sebagai regresi tunggal. Regresi di sini berarti jaringan memprediksi nilai numerik kontinu — koordinat dan ukuran kotak — alih-alih mengklasifikasikan wilayah satu per satu. Satu jaringan saraf konvolusi (CNN, jaringan yang mengekstrak fitur citra lewat operasi konvolusi berlapis) menerima seluruh citra dan, dalam satu evaluasi, mengeluarkan tensor yang memuat semua kotak beserta skor keyakinan dan probabilitas kelasnya.

Kontribusi survei itu sendiri adalah cara membacanya: empat versi YOLO disajikan sebagai satu garis optimasi; setiap versi memperbaiki kelemahan spesifik pendahulunya, dari galat lokalisasi pada v1 sampai kegagalan pada objek kecil pada v2. Pembaca memperoleh peta kronologis beserta ukuran kuantitatif tiap perbaikan.

## Cara Kerja Langkah demi Langkah

### Detektor Dua Tahap sebagai Titik Banding

Survei dimulai dari keluarga R-CNN. R-CNN menghasilkan kandidat wilayah dengan algoritme *selective search* (pengelompokan piksel berdasarkan kemiripan warna dan tekstur), mengekstrak fitur tiap wilayah dengan CNN, lalu mengklasifikasikannya satu per satu. Fast R-CNN menghitung peta fitur (*feature map*, representasi citra hasil konvolusi) satu kali untuk seluruh citra dan membaginya ke semua proposal. Faster R-CNN mengganti *selective search* dengan *Region Proposal Network* (RPN), jaringan yang mempelajari sendiri cara mengusulkan wilayah. Pada PASCAL VOC 2007, Fast R-CNN dan Faster R-CNN dilaporkan masing-masing 25 dan 250 kali lebih cepat dari R-CNN dengan mAP yang hampir sama, sekitar 66. mAP (*mean Average Precision*) adalah rata-rata presisi deteksi di seluruh kelas; semakin tinggi semakin baik, maksimal 100.

### Formulasi Regresi YOLO

Bagian inti survei menjelaskan mekanisme YOLO. Citra dibagi menjadi *grid* (kisi) S×S sel. Sebuah sel bertanggung jawab mendeteksi objek yang titik pusatnya jatuh di dalam sel itu. Setiap sel memprediksi B buah kotak; setiap kotak dinyatakan lima angka: peluang adanya objek (pc), koordinat pusat (bx, by), serta lebar dan tinggi (bw, bh). Setiap sel juga memprediksi n probabilitas kelas bersyarat yang dipakai bersama oleh seluruh kotak pada sel tersebut. Keluaran jaringan dengan demikian berupa tensor S×S×(B×5+n); pada contoh yang dipakai survei, S = 19 dan B = 4, sehingga setiap sel memuat 20 angka kotak ditambah n angka kelas.

Alur prediksi dari citra sampai deteksi akhir digambarkan sebagai berikut:

```
citra masukan
     │
     ▼
bagi menjadi grid S x S sel
     │
     ▼
setiap sel memprediksi B kotak (pc, bx, by, bw, bh)
dan n probabilitas kelas ──► tensor keluaran S x S x (B x 5 + n)
     │
     ▼
skor keyakinan per kotak: confidence = pc x IoU
skor per kelas: confidence x p(kelas | objek)
     │
     ▼
buang kotak berskor di bawah ambang (umumnya 0,5)
     │
     ▼
Non-Maximum Suppression: pertahankan kotak berskor
tertinggi, buang kotak yang tumpang tindih dengannya
     │
     ▼
deteksi akhir: satu kotak + satu kelas per objek
```

Skor keyakinan (*confidence*) dihitung sebagai pc dikali IoU (*Intersection over Union*, rasio luas irisan terhadap luas gabungan antara kotak prediksi dan kotak kebenaran). Kotak yang lolos ambang dirampingkan dengan *Non-Maximum Suppression* (NMS): dari sekumpulan kotak yang saling menutupi dengan IoU di atas ambang, hanya kotak berskor tertinggi yang dipertahankan agar satu objek tidak dilaporkan berkali-kali. Objek dengan bentuk beragam ditampung *anchor box*, yaitu sekumpulan kotak acuan lebar-tinggi yang dipilih dari analisis dataset; mulai YOLOv2 pemilihannya memakai pengelompokan *k-means*, bukan pilihan manual.

Fungsi kerugian (*loss*) yang dipakai adalah jumlah kuadrat selisih (*sum-squared error*) dengan lima suku: galat koordinat pusat, galat dimensi, galat *confidence* untuk sel berobjek, galat *confidence* untuk sel tanpa objek, dan galat klasifikasi. Lebar dan tinggi diprediksi dalam bentuk akar kuadrat agar selisih beberapa piksel pada kotak kecil dihukum lebih berat daripada pada kotak besar. Dua hiperparameter pembobot (λcoord dan λnoobj) menjaga gradien agar tidak didominasi sel-sel kosong yang jumlahnya jauh lebih banyak. Arsitektur v1 terdiri atas 24 lapis konvolusi dan 2 lapis terhubung penuh; modul *inception* GoogLeNet diganti konvolusi 1×1 diikuti 3×3.

### Peningkatan Inkremental pada YOLOv2

YOLOv2 memakai kerangka Darknet-19 (19 lapis konvolusi dan 5 lapis *max-pooling*) dan menggabungkan dataset ImageNet dengan COCO melalui klasifikasi hierarkis WordTree, sehingga dapat mendeteksi lebih dari 9.400 kategori (dilaporkan 9.418 kategori gabungan). Survei merinci sumbangan kuantitatif tiap teknik baru. *Batch normalization* (normalisasi keluaran tiap lapis agar distribusinya stabil selama pelatihan) menambah sekitar 2 poin mAP; pengklasifikasi resolusi tinggi (pra-pelatihan pada citra 448×448, bukan 224×224) menambah sekitar 4 poin mAP. Prediksi kotak berbasis *anchor* menaikkan *recall* (proporsi objek yang berhasil ditemukan) sekitar 7 poin dengan penurunan mAP 0,3 poin; prediksi lokasi relatif terhadap posisi sel menambah sekitar 5 poin mAP; fitur berbutir halus (peta fitur 26×26×512 dibentuk ulang menjadi 13×13×2048, lalu digabungkan dengan peta fitur akhir) menambah sekitar 1 poin mAP. Pelatihan multi-skala membuat model berganti resolusi masukan dalam rentang 320×320 sampai 608×608, sehingga satu model melayani berbagai ukuran citra.

### YOLOv3: Prediksi pada Tiga Skala

YOLOv3 mengganti *backbone* (jaringan pengekstrak fitur utama) menjadi Darknet-53: 53 lapis konvolusi 3×3 dan 1×1 dengan sambungan pintas (*shortcut*) ala ResNet, yaitu sambungan yang meneruskan keluaran satu lapis ke lapis yang lebih dalam agar gradien tetap mengalir. Terinspirasi FPN (*Feature Pyramid Network*, struktur yang menggabungkan peta fitur resolusi tinggi dan rendah lewat jalur atas-bawah), deteksi dilakukan pada tiga skala sekaligus: peta fitur 13×13 (resolusi 32 kali lebih rendah dari masukan) untuk objek besar, 26×26 (16 kali) untuk objek sedang, dan 52×52 (8 kali) untuk objek kecil. Desain ini menjawab kelemahan YOLOv2 pada objek kecil; survei mencatat sebagai gantinya akurasi pada objek sedang dan besar menurun.

### YOLOv4: Dekomposisi Backbone–Neck–Head

YOLOv4 memperkenalkan cara memandang detektor sebagai tiga komponen: *backbone* pengekstrak fitur, *neck* penggabung fitur lintas skala, dan *head* penghasil prediksi. *Backbone* yang dipilih adalah CSPDarknet53 (29 lapis konvolusi 3×3, sekitar 27,6 juta parameter), yang memakai koneksi parsial antartahap (*cross-stage partial*) untuk memperkaya aliran gradien dengan biaya komputasi lebih rendah. Bagian *neck* memakai SPP (*Spatial Pyramid Pooling*, penggabungan fitur hasil *pooling* pada beberapa ukuran jendela agar jaringan menerima masukan berbagai dimensi) dan PAN (*Path Aggregation Network*, jalur agregasi bawah-atas yang melengkapi jalur atas-bawah FPN). Survei juga mencatat teknik pelatihan versi ini, antara lain aktivasi Mish, regularisasi DropBlock, *label smoothing*, dan normalisasi lintas mini-*batch*.

## Eksperimen dan Hasil

Sebagai survei, makalah ini tidak menjalankan eksperimen baru; buktinya berupa sintesis tabel dari literatur. Rekapitulasi kinerja yang disusun penulis:

- YOLOv1 pada PASCAL VOC 2007+2012: 63,4 mAP pada 45 FPS.
- Fast YOLO (varian 9 lapis): 52,7 mAP pada 155 FPS.
- YOLOv2 pada PASCAL VOC: 78,6 mAP pada 40 FPS.
- YOLO-LITE (untuk sistem tanpa GPU): 33,77 mAP pada 21 FPS.
- YOLOv3 pada MS COCO: 57,9 mAP pada 20 FPS.
- YOLOv4 pada MS COCO: 65,7 mAP pada 33 FPS.

FPS (*frames per second*) adalah jumlah citra yang diproses per detik; 30 FPS umumnya dianggap batas *real-time*. Interpretasinya: mAP YOLOv2 (78,6) melampaui Fast R-CNN (70,0) pada tolok ukur yang sama, sambil tetap berjalan jauh lebih cepat — abstrak survei memperkirakan selisih kecepatan inferensi YOLO terhadap Fast R-CNN sekitar 300 kali. Perbandingan berikutnya menuntut kehati-hatian: v1 dan v2 diukur pada VOC, sedangkan v3 dan v4 pada COCO yang lebih sulit, sehingga penurunan angka dari 78,6 ke 57,9 bukan kemunduran mutlak, melainkan perpindahan tolok ukur. YOLO-LITE memperlihatkan sisi lain kompromi: akurasinya sekitar separuh YOLOv1, tetapi model berjalan pada perangkat tanpa akselerator GPU.

Dua tabel aplikasi melengkapi sintesis: di sisi dua tahap, sistem OCR Rosetta berbasis Faster R-CNN dan deteksi cacat tabung kertas dengan akurasi 98%; di sisi YOLO, deteksi kendaraan ganda dengan laju 98,6% (v2), masker wajah dengan presisi rata-rata 81% (v2), deteksi objek pada papan sirkuit dengan mAP 93,07% (v3), dan deteksi manusia dari citra termal udara dengan mAP 91% (v4). Daftar ini menunjukkan YOLO dipilih pada sistem produksi terutama karena kecepatan inferensinya. Dataset yang dibahas survei adalah PASCAL VOC (20 kelas sejak 2007; sekitar 11.530 citra latih dengan 27.540 RoI dan 6.929 segmentasi) dan MS COCO (91 kategori dengan instans lebih banyak per kategori).

## Kelebihan dan Keterbatasan

Kelebihan survei ini adalah kelengkapan pemetaan dalam satu naskah: tantangan, rumusan regresi, optimasi tiap versi, perbandingan dua tahap melawan satu tahap, dataset, dan aplikasi. Rincian sumbangan kuantitatif per teknik pada YOLOv2 jarang ditemukan terhimpun pada tinjauan lain.

Keterbatasannya: cakupan berhenti di YOLOv4 — YOLOv5 sengaja tidak dibahas — sehingga peta ini tidak mencakup generasi sesudahnya. Dari sisi metodologi, angka kinerja dihimpun dari makalah asli masing-masing versi tanpa protokol evaluasi yang diseragamkan; basis metrik (AP50 atau mAP penuh) dan perangkat keras pengukuran tidak dicantumkan, sehingga angka pada tabel hasil harus dibaca sebagai indikasi, bukan perbandingan setara. Kedalaman tiap topik juga terbatas karena cakupannya yang luas.

## Kaitan dengan Bab Lain

Bab ini adalah peta bagi empat bab fondasi yang menjadi objek surveinya: [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md) untuk rumusan regresi aslinya, [bab 002 (YOLOv2)](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md) untuk teknik optimasi yang dirinci survei ini, serta [bab 003 (YOLOv3)](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md) dan [bab 004 (YOLOv4)](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md) untuk arsitektur multi-skala dan dekomposisi *backbone–neck–head*. Dalam klaster Survei YOLO, bab ini berbagi fungsi dengan [bab 028 (survei perkembangan YOLO oleh Jiang dkk.)](./028%20-%202022%20-%20Review%20Perkembangan%20YOLO%20%28Jiang%20dkk.%29%20-%20Survei%20YOLO.md) dan [bab 026 (tinjauan Terven dkk.)](./026%20-%202023%20-%20Review%20YOLO%20%28Terven%20dkk.%29%20-%20Survei%20YOLO.md); ketiganya saling melengkapi sebagai kerangka membaca silsilah versi.

## Poin untuk Sitasi

Kutip dengan kunci `diwan2023yolo`. Ringkasan yang aman dikutip: "Diwan dkk. (2023) meninjau detektor objek satu tahap keluarga YOLO dari versi pertama sampai YOLOv4, merangkum rumusan regresi, optimasi arsitektur tiap versi, dataset, statistik kinerja, dan aplikasi, serta menyimpulkan bahwa silsilah YOLO adalah perbaikan inkremental atas kompromi kecepatan dan akurasi."

Catatan verifikasi sebelum sitasi formal: (1) angka pada tabel hasil dihimpun survei dari makalah asli tanpa mencantumkan basis metrik (AP50 atau mAP penuh); angka v3 dan v4 sebaiknya dikutip dari makalah versi masing-masing; (2) klaim "sekitar 300 kali lebih cepat" berasal dari abstrak dan merujuk perbandingan YOLOv1 dengan Fast R-CNN; (3) tahun terbit tercatat 2023 pada terbitan jurnal, tetapi naskah terbit daring 8 Agustus 2022; (4) klaim "tinjauan pertama detektor satu tahap berbasis YOLO" adalah klaim penulis, bukan fakta yang diverifikasi secara independen.
