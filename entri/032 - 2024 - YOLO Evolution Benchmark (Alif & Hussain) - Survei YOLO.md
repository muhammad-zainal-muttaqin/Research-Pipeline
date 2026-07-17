# 032 - YOLO Evolution: A Comprehensive Benchmark and Architectural Review of YOLOv12, YOLO11, and Their Previous Versions

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `alif2024yoloevolution` |
| Judul asli | YOLO Evolution: A Comprehensive Benchmark and Architectural Review of YOLOv12, YOLO11, and Their Previous Versions |
| Penulis | Nidhal Jegham, Chan Young Koh, Marwan F. Abdelatti, Abdeltawab M. Hendawi |
| Tahun | 2024 |
| Venue | arXiv preprint arXiv:2411.00201 (versi terbit: *Image and Vision Computing*) |
| Tema | Survei YOLO |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2411.00201
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLO%20Evolution%3A%20A%20Comprehensive%20Benchmark%20and%20Architectural%20Review%20of%20YOLOv12%2C%20YOLO11%2C%20and%20Their%20Previous%20Versions
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLO%20Evolution%3A%20A%20Comprehensive%20Benchmark%20and%20Architectural%20Review%20of%20YOLOv12%2C%20YOLO11%2C%20and%20Their%20Previous%20Versions&sort=relevance

## Gambaran Umum

Makalah ini menyajikan pembandingan (*benchmark*) eksperimental terhadap keluarga detektor objek YOLO dari YOLOv3 hingga YOLOv12. Sebanyak 33 model dari tujuh versi dilatih ulang dengan hiperparameter seragam pada tiga dataset yang masing-masing memuat jenis kesulitan deteksi yang berbeda, lalu diukur memakai enam kelompok metrik: Precision, Recall, mAP, waktu pemrosesan, GFLOPs, dan ukuran model. Penulis mengklaim studi ini sebagai evaluasi eksperimental komprehensif pertama pada rentang versi tersebut.

Hasilnya memetakan karakter tiap versi. YOLO11 tampil paling seimbang antara akurasi dan efisiensi pada hampir semua skala model. YOLOv10 paling cepat dan hemat komputasi, tetapi akurasinya tertinggal, terutama pada objek yang saling tumpang tindih. YOLOv9 sangat akurat, khususnya pada dataset kecil, tetapi paling lambat. YOLOv12 menyamai YOLO11 dalam akurasi, tetapi beban komputasinya tinggi tanpa perolehan akurasi tambahan. Model-model besar cenderung mengalami *overfitting* (menghafal data latih sehingga gagal menggeneralisasi ke data baru) pada dataset kecil. Temuan tersebut dirangkum menjadi tabel rekomendasi pemilihan model per skenario aplikasi.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Setiap generasi YOLO dipublikasikan dengan protokol evaluasinya sendiri. Angka akurasi resmi umumnya berupa mAP pada dataset MS COCO, tetapi diperoleh dengan bobot awal, resolusi masukan, dan resep pelatihan yang berbeda antar-versi. Akibatnya, angka-angka itu tidak terbandingkan secara adil: selisihnya dapat berasal dari arsitektur, tetapi dapat pula dari resep pelatihan.

Tinjauan yang ada belum menutup celah ini. Survei Terven dkk. (bab 026) dan Jiang dkk. (bab 028) memetakan evolusi arsitektur tanpa pengujian ulang; sebagian ulasan lain hanya memakai mAP dan FPS, mengabaikan waktu pra-pemrosesan, pasca-pemrosesan, GFLOPs, dan ukuran model. Ketika makalah ini ditulis, belum ada evaluasi eksperimental yang mencakup YOLO11 dan YOLOv12 — padahal dua versi itu yang paling mungkin dipilih praktisi. Tanpa pengukuran seragam, keputusan pemilihan model bertumpu pada klaim yang tidak setara.

## Ide Utama

Gagasan inti makalah ini adalah mengganti perbandingan berbasis kutipan dengan perbandingan berbasis pengulangan terkontrol. Alih-alih mengumpulkan angka dari publikasi tiap versi, penulis mengambil bobot pralatih resmi, menyetel halus (*fine-tuning*: melanjutkan pelatihan dari bobot yang sudah ada pada dataset baru) setiap model dengan hiperparameter yang sama pada dataset yang sama, kemudian membandingkan hasilnya. Dengan protokol ini, satu-satunya variabel yang berbeda antar-eksperimen adalah arsitektur modelnya.

Tiga dataset dipilih agar masing-masing menekan satu kelemahan khas detektor: variasi ukuran objek, dataset kecil dengan objek besar yang tumpang tindih, dan objek kecil satu kelas dengan rotasi beragam. Hasil pengukuran diperingkat dua kali — per kelas ukuran model (nano hingga extra-large) dan per keluarga versi — sehingga kesimpulan tidak didikte oleh satu skala atau satu dataset.

## Cara Kerja Langkah demi Langkah

### Lingkup Model dan Alasan Eksklusi

Studi ini hanya memakai model yang didukung pustaka Ultralytics, karena pustaka itu menyediakan bobot pralatih dan antarmuka pelatihan yang seragam. Totalnya 33 model dari tujuh versi: YOLOv3u, YOLOv5u, YOLOv8, YOLOv9, YOLOv10, YOLO11, dan YOLOv12, masing-masing dalam beberapa varian skala. Akhiran nama menandai ukuran: *n* (nano), *s* (small), *m* (medium), *l* (large), *x* (extra-large), ditambah varian khusus *t* (tiny), *c* (compact), *b* (balanced), dan *e* (extended).

YOLOv4, YOLOv6, dan YOLOv7 dikeluarkan karena Ultralytics tidak menyediakan bobot pralatihnya (untuk YOLOv6 hanya tersedia berkas konfigurasi). Pengecualian ini diuji, bukan diasumsikan: pada uji pendahuluan di dataset Traffic Signs, YOLOv5n dan YOLOv3 versi Ultralytics mengungguli versi orisinalnya, sedangkan YOLOv9c orisinal sedikit mengungguli versi Ultralytics. Karena implementasi Ultralytics telah dimodifikasi, mencampur model dari dua sumber dalam satu benchmark dinilai penulis tidak adil.

### Tiga Dataset, Tiga Jenis Kesulitan

Ketiga dataset diambil dari Kaggle dan Roboflow, tanpa augmentasi data, dengan pembagian 70% data latih, 20% validasi, dan 10% uji.

- **Traffic Signs.** Awalnya ±55 kelas rambu lalu lintas pada 3.253 citra latih berukuran 640×640; kelas beranggotakan kurang dari 50 observasi dibuang dan distribusi kelas diseimbangkan dengan *undersampling* (mengurangi sampel kelas mayoritas), menyisakan 24 kelas dan 3.233 citra. Tantangannya adalah ukuran objek yang bervariasi dan kemiripan pola antarkelas.
- **Africa Wildlife.** Empat kelas hewan (kerbau, gajah, badak, zebra), masing-masing minimal 376 citra. Tantangannya adalah jumlah data yang kecil — sehingga model besar berisiko *overfitting* — serta objek yang sering tumpang tindih.
- **Ships/Vessels.** Sekitar 13.500 citra satu kelas ("kapal") yang dikurasi dari beberapa dataset Roboflow. Tantangannya adalah objek berukuran kecil dengan orientasi dan rasio aspek beragam, kondisi yang secara historis sulit bagi YOLO.

### Pelatihan dan Metrik

Semua model berangkat dari bobot pralatih (hasil pelatihan pada COCO) lalu disetel halus dengan hiperparameter yang sama, pada dua GPU NVIDIA RTX 4090 memakai Ultralytics 8.2.55. Enam kelompok metrik dipakai. Precision adalah proporsi prediksi benar dari seluruh prediksi; Recall adalah proporsi objek yang berhasil ditemukan; keduanya dihitung terhadap IoU (*Intersection over Union*, rasio luas irisan terhadap luas gabungan kotak prediksi dan kotak kebenaran). mAP50 adalah rata-rata presisi seluruh kelas pada ambang IoU 0,50; mAP50-95 mereratakan nilai itu pada ambang 0,50 hingga 0,95 dengan langkah 0,05, sehingga menuntut lokalisasi yang lebih tepat. Efisiensi diukur dari waktu pra-pemrosesan, inferensi, dan pasca-pemrosesan per citra; GFLOPs (miliar operasi *floating-point* per citra) mengukur beban komputasi; ukuran model mengukur kebutuhan penyimpanan.

### Skema Pemeringkatan

Rangkaian benchmark dari model hingga peringkat dirangkum pada diagram berikut.

```
        RANCANGAN BENCHMARK: 33 MODEL (7 VERSI) x 3 DATASET

+--------------------+   +--------------------------------------+
| Model per versi    |   | Tiga dataset, tiga tantangan:        |
| (skala n,s,m,l,x): |   | 1. Traffic Signs : 24 kelas, 3.233   |
| v3u, v5u, v8, v9,  |   |    citra 640x640; ukuran objek       |
| v10, 11, v12       |   |    bervariasi                        |
+---------+----------+   | 2. Africa Wildlife: 4 kelas; data    |
          |              |    kecil; objek besar tumpang tindih |
          v              | 3. Ships/Vessels  : 1 kelas, 13,5rb  |
+--------------------+   |    citra; objek kecil dan terotasi   |
| Fine-tuning bobot  |   +------------------+-------------------+
| pralatih COCO;     |                      |
| hiperparameter     |<---------------------+
| seragam untuk      |   setiap model dilatih pada ketiga dataset
| semua model        |
+---------+----------+
          v
+-----------------------------------------------------------+
| Metrik: Precision, Recall, mAP50, mAP50-95, waktu pra-    |
| proses/inferensi/pasca-proses, GFLOPs, ukuran model       |
+---------------------------+-------------------------------+
                            v
+-----------------------------------------------------------+
| Peringkat per kelas skala (nano..extra-large) dan         |
| peringkat keluarga (rata-rata peringkat semua skala)      |
+-----------------------------------------------------------+
```

Diagram menunjukkan alur kerja: setiap model dari tujuh versi dilatih pada ketiga dataset dengan hiperparameter seragam, diukur dengan metrik yang sama, lalu diperingkat. Pemeringkatan berlangsung dua lapis. Pertama, model dikelompokkan per kelas ukuran; varian bersufiks khusus dipetakan ke kelas terdekat (YOLOv9t ke nano, YOLOv3u-tiny ke small, YOLOv9e ke extra-large). Peringkat akurasi memakai mAP50-95; peringkat kecepatan memakai total waktu pemrosesan. Kedua, peringkat semua skala dalam satu versi dirata-ratakan menjadi peringkat keluarga.

## Eksperimen dan Hasil

**Traffic Signs (ukuran objek bervariasi).** Akurasi tertinggi diraih YOLOv5ul (mAP50 0,866; mAP50-95 0,799), diikuti YOLO11m (mAP50-95 0,795) dan YOLO11l (0,794). Tercepat adalah YOLOv10n (2 ms per citra, 8,3 GFLOPs) dan YOLO11n (2,2 ms, 6,4 GFLOPs); terlambat keluarga YOLOv9, dengan YOLOv9e pada 16,1 ms dan 189,4 GFLOPs. Selisih akurasi model teratas tipis (±0,005 mAP50-95 antara YOLOv5ul dan YOLO11m), sedangkan selisih biayanya besar (±7 kali lipat antara YOLO11n dan YOLOv9e), sehingga YOLO11m dinilai penulis paling seimbang pada dataset ini.

**Africa Wildlife (dataset kecil, objek besar).** Keluarga YOLOv9 mendominasi: YOLOv9s mencapai mAP50-95 0,832 dan mAP50 0,956, disusul YOLOv9c dan YOLOv9t. Model-model besar justru turun performanya — YOLO11x, YOLOv5ux, dan YOLOv10l berada di bawah varian kecil dari keluarganya sendiri — gejala *overfitting* pada data terbatas; pengecualiannya YOLOv10x. YOLOv12x menjadi yang terlambat (12,8 ms, 198,5 GFLOPs). Pada dataset kecil, kapasitas model besar menjadi beban, bukan keuntungan.

**Ships/Vessels (objek kecil satu kelas).** YOLO11x terbaik dengan mAP50 0,529 dan mAP50-95 0,327, diikuti ketat YOLO11l, YOLO11m, dan YOLO11s; terendah YOLOv3u-tiny (0,489 dan 0,273). Dua hal menonjol. Pertama, angka absolutnya jauh di bawah dua dataset lain — model terbaik pun hanya menemukan sekitar setengah objek pada ambang IoU 0,50 — menegaskan objek kecil tetap titik lemah seluruh keluarga YOLO. Kedua, jurang antara mAP50 dan mAP50-95 (0,529 lawan 0,327) menunjukkan kotak prediksi sering benar secara kasar tetapi kurang presisi tepinya. YOLOv12x kembali terlambat (10,9 ms, 198,5 GFLOPs); YOLO11s dan YOLOv10s dinilai paling seimbang.

**Peringkat lintas dataset.** Per kelas ukuran: nano dimenangi YOLOv9t; small dimenangi YOLOv12s untuk akurasi tetapi dengan kecepatan buruk, sedangkan YOLOv10s dan YOLO11s lebih seimbang; medium dimenangi YOLO11m; large dimenangi YOLO11l; extra-large dimenangi YOLO11x. Per keluarga: YOLO11 dan YOLOv12 berbagi peringkat pertama akurasi, tetapi YOLO11 juga terdepan pada GFLOPs dan ukuran, sedangkan YOLOv12 membayar akurasinya dengan latensi — modul Area Attention dan FlashAttention-nya menambah waktu inferensi. YOLOv10 menjadi keluarga paling efisien dengan akurasi di bawah rata-rata; YOLOv9 kebalikannya. Hasil ini diterjemahkan penulis menjadi tabel rekomendasi: YOLOv10 dan YOLO11 varian n/s/m untuk perangkat terbatas dan pemantauan *real-time*, YOLO11 atau YOLOv12 varian m/l/x untuk objek kecil dan dataset besar, serta YOLOv9 varian kecil untuk dataset kecil.

## Kelebihan dan Keterbatasan

Kelebihan studi ini: (1) cakupannya luas — 33 model dari tujuh versi, termasuk evaluasi awal YOLOv12; (2) kondisinya seragam — bobot pralatih resmi, hiperparameter sama, perangkat keras sama — sehingga perbandingan terkendali; (3) metriknya melampaui mAP dan FPS; (4) hasil disajikan per skala dan per skenario aplikasi, bukan satu angka tunggal.

Keterbatasannya: (1) hanya model Ultralytics yang diuji, sehingga YOLOv4, YOLOv6, dan YOLOv7 absen; (2) ketiga dataset berukuran kecil hingga menengah dan tidak memakai augmentasi, sehingga angkanya tidak langsung terbandingkan dengan hasil pada COCO; (3) waktu pemrosesan terikat pada perangkat keras RTX 4090. Dari sisi rekayasa, dua catatan tambahan layak diajukan. Tanpa augmentasi, hasil mencerminkan pelatihan pada data mentah, bukan praktik umum pelatihan detektor modern. Selain itu, terdapat ketegangan antara abstrak — yang menyebut hasil YOLOv12 mengecewakan — dan pembahasan, yang menempatkan YOLOv12 sejajar dengan YOLO11 dalam akurasi; pembaca sebaiknya memegang angka per dataset, bukan satu klaim ringkas.

## Kaitan dengan Bab Lain

Bab ini tidak memperkenalkan arsitektur baru; ia menguji klaim bab-bab fondasi dalam satu kondisi terkendali. Model tertua yang diuji adalah [YOLOv3 (bab 003)](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md) dalam bentuk YOLOv3u. Sebagian inovasi yang dibandingkan dibahas pada babnya masing-masing: GELAN dan PGI pada [YOLOv9 (bab 008)](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md), pelatihan tanpa NMS pada [YOLOv10 (bab 009)](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md), serta blok C3k2 dan C2PSA pada [YOLOv11 (bab 010)](./010%20-%202024%20-%20YOLOv11%20%28Overview%29%20-%20Fondasi%20RGB.md). Temuan bab ini memberi konteks kuantitatif bagi klaim tiap bab tersebut — efisiensi YOLOv10, misalnya, terkonfirmasi, tetapi harganya berupa akurasi.

Di dalam klaster Survei YOLO, bab ini melengkapi survei naratif [Terven dkk. (bab 026)](./026%20-%202023%20-%20Review%20YOLO%20%28Terven%20dkk.%29%20-%20Survei%20YOLO.md), [Jiang dkk. (bab 028)](./028%20-%202022%20-%20Review%20Perkembangan%20YOLO%20%28Jiang%20dkk.%29%20-%20Survei%20YOLO.md), dan tinjauan sistematis [Vijayakumar & Vairavasundaram (bab 031)](./031%20-%202024%20-%20Systematic%20Review%20YOLO%20%28Vijayakumar%20%26%20Vairavasundaram%29%20-%20Survei%20YOLO.md) dengan bukti eksperimental. Hasilnya berguna bagi pemilihan *backbone* deteksi untuk sistem RGB-D pada klaster lain dalam tinjauan ini.

## Poin untuk Sitasi

Kutip dengan kunci `alif2024yoloevolution`. Ringkasan yang aman dikutip: "Jegham dkk. membandingkan 33 model dari tujuh versi YOLO (YOLOv3u hingga YOLOv12) pada tiga dataset dengan hiperparameter seragam; YOLO11 tampil paling seimbang antara akurasi dan efisiensi, YOLOv10 paling efisien, YOLOv9 paling akurat pada data kecil, dan YOLOv12 akurat tetapi berlatensi tinggi."

Catatan verifikasi sebelum sitasi formal:

- Daftar penulis pada `references.bib` ("Alif, Md Adnan Faisal; Hussain, Muhammad") **tidak cocok** dengan naskah arXiv:2411.00201, yang mencantumkan Nidhal Jegham, Chan Young Koh, Marwan F. Abdelatti, dan Abdeltawab M. Hendawi; entri BibTeX perlu diperbaiki.
- Versi terbit tercatat pada jurnal *Image and Vision Computing*; volume dan halaman perlu dikonfirmasi.
- Angka hasil pada bab ini dibaca dari teks HTML arXiv versi 4; tabel peringkat numerik (Tabel 4 naskah) tidak tersedia dalam versi HTML, sehingga urutan peringkat keluarga bersumber dari narasi makalah.
- Klaim "evaluasi komprehensif pertama" adalah klaim penulis, bukan fakta yang diverifikasi.
