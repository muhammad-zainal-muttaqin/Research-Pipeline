# 010 - YOLOv11: An Overview of the Key Architectural Enhancements

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `khanam2024yolov11` |
| Judul asli | YOLOv11: An Overview of the Key Architectural Enhancements |
| Penulis | Rahima Khanam, Muhammad Hussain |
| Tahun | 2024 |
| Venue | arXiv preprint arXiv:2410.17725 |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2410.17725
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOv11%3A%20An%20Overview%20of%20the%20Key%20Architectural%20Enhancements
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOv11%3A%20An%20Overview%20of%20the%20Key%20Architectural%20Enhancements&sort=relevance

## Gambaran Umum

Makalah ini adalah tinjauan arsitektural atas YOLOv11, detektor objek satu tahap yang dirilis Ultralytics pada September 2024 dan diperkenalkan pada konferensi YOLO Vision 2024 (YV24). Penulisnya dua peneliti Universitas Huddersfield, bukan pengembang YOLOv11; deskripsinya dihimpun dari sumber resmi yang tersebar karena Ultralytics tidak menerbitkan makalah formal untuk rilisnya. Tiga perubahan utama yang diidentifikasi: blok C3k2 menggantikan blok C2f di seluruh bagian jaringan, modul atensi spasial C2PSA ditambahkan setelah blok SPPF pada *backbone*, dan *head* deteksi disusun ulang. Satu keluarga model, dari ukuran *nano* hingga *extra-large*, menangani enam tugas visi: deteksi objek, segmentasi instans, klasifikasi citra, estimasi pose, deteksi objek berorientasi, dan pelacakan objek.

Hasil utama yang dilaporkan: varian YOLOv11m mencapai mAP 51,5% pada dataset COCO dengan 20,1 juta parameter, yaitu 22% lebih sedikit daripada YOLOv8m (25,9 juta parameter, 50,2% mAP). Seluruh angka kinerja dalam makalah mengacu dokumentasi dan tolok ukur resmi Ultralytics, bukan eksperimen yang dijalankan penulis tinjauan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Lini YOLO berkembang dalam iterasi yang rapat. Sejak deteksi satu tahap dirumuskan (bab 001), versi baru muncul hampir setiap tahun dengan blok arsitektur dan resep pelatihan yang berbeda. Tahun 2024 saja melahirkan YOLOv9 (bab 008) dengan mekanisme informasi gradien terprogram dan YOLOv10 (bab 009) dengan pelatihan bebas NMS (*Non-Maximum Suppression*, tahap penghapusan kotak duplikat sesudah prediksi).

Masalah yang diangkat makalah ini bersifat dokumentatif. Ultralytics, pemelihara YOLOv8 dan YOLOv11, tidak menerbitkan makalah formal untuk kedua model tersebut; detail arsitekturnya tersebar di repositori kode, dokumentasi daring, dan artikel blog. Akibatnya, praktisi yang hendak mengetahui apa yang berubah dari YOLOv8 ke YOLOv11 tidak memiliki satu rujukan tertulis yang runtut. Makalah ini mengisi celah itu dengan deskripsi arsitektural YOLOv11 yang dihimpun dari sumber resmi per Oktober 2024.

## Ide Utama

Gagasan inti yang dilaporkan makalah: YOLOv11 mempertahankan kerangka tiga bagian YOLOv8, tetapi mengganti blok pemroses fitur utamanya dan menambahkan satu modul atensi. Secara mekanis, masukan tetap sebuah citra dan keluaran tetap kotak pembatas beserta kelasnya dalam satu kali evaluasi jaringan; yang berubah adalah cara fitur diolah di dalamnya. Blok C3k2 menggantikan blok C2f pada *backbone*, *neck*, dan *head* dengan struktur yang lebih hemat parameter. Modul C2PSA disisipkan di ujung *backbone* agar jaringan membobot posisi-posisi informatif pada peta fitur. Karena perubahannya modular, satu arsitektur yang sama diskalakan menjadi lima ukuran (n, s, m, l, x) dan dipasangi keluaran berbeda untuk enam tugas visi.

## Cara Kerja Langkah demi Langkah

### Kerangka Tiga Bagian

Seperti seluruh YOLO modern, YOLOv11 terdiri atas tiga komponen. *Backbone* adalah jaringan konvolusi pengekstrak fitur: citra masukan diproses berlapis-lapis menjadi peta fitur pada beberapa resolusi. *Neck* menggabungkan peta fitur antarresolusi, umumnya dengan *upsampling* (penaikan resolusi) diikuti penggabungan kanal, agar informasi objek kecil dan besar tersedia bersama. *Head* menghasilkan prediksi akhir dari fitur gabungan tersebut. Perubahan YOLOv11 terhadap YOLOv8 terletak pada isi blok di ketiga komponen, bukan pada kerangka ini.

### Blok C3k2

Perubahan pertama adalah penggantian blok C2f dengan blok C3k2. Keduanya adalah varian dari desain CSP (*Cross Stage Partial*): aliran fitur dibagi dua cabang, satu cabang diolah melalui tumpukan konvolusi dan cabang lain diteruskan langsung, kemudian keduanya digabung kembali; pembagian ini menekan biaya komputasi tanpa memutus aliran gradien saat pelatihan. C2f, yang dipakai YOLOv8, mengolah cabangnya melalui serangkaian *bottleneck* (pasangan konvolusi yang mereduksi lalu mengembangkan jumlah kanal) dengan keluaran yang diakumulasikan terus-menerus. Menurut makalah, C3k2 adalah implementasi CSP yang lebih efisien: alih-alih satu konvolusi besar, dipakai dua konvolusi yang lebih kecil, dan penanda "k2" ditafsirkan sebagai ukuran *kernel* yang lebih kecil — *kernel* adalah matriks bobot konvolusi, misalnya 3×3, yang digeser di atas peta fitur.

Perilaku blok ditentukan parameter c3k. Bila c3k = False, C3k2 bekerja menyerupai C2f dengan *bottleneck* standar. Bila c3k = True, *bottleneck* digantikan modul C3 yang memungkinkan ekstraksi fitur lebih dalam. Tersedia pula varian C3k dengan ukuran *kernel* yang dapat disesuaikan untuk menangkap detail lebih halus. Efek praktisnya terukur pada jumlah parameter: dua konvolusi kecil berbobot lebih sedikit daripada satu konvolusi besar dengan jangkauan piksel yang setara.

### SPPF dan C2PSA

Pada ujung *backbone*, YOLOv11 mempertahankan blok SPPF (*Spatial Pyramid Pooling – Fast*) dari versi sebelumnya. SPPF melewatkan peta fitur melalui beberapa lapisan *max-pooling* (pengambilan nilai maksimum per jendela kecil) yang disusun seri, sehingga jaringan memperoleh konteks dari beberapa ukuran wilayah sekaligus tanpa mengubah resolusi. Setelah SPPF, YOLOv11 menambahkan blok baru C2PSA — dalam isi makalah ditulis *Cross Stage Partial with Spatial Attention*. Modul ini menerapkan atensi spasial: setiap posisi pada peta fitur diberi bobot, sehingga wilayah informatif mendapat bobot lebih besar daripada wilayah latar. Tujuannya memperkuat respons pada objek kecil atau objek yang tertutup sebagian, yang pada versi tanpa atensi lebih mudah hilang setelah resolusi diturunkan berkali-kali.

### Head dan Lapisan Detect

*Head* YOLOv11 memproses tiga skala fitur dari *neck*, satu cabang per skala. Setiap cabang memakai blok C3k2 yang diikuti beberapa lapisan CBS — singkatan dari Convolution, BatchNorm, SiLU. *Batch normalization* menormalkan nilai aktivasi per batch agar pelatihan stabil; SiLU (*Sigmoid Linear Unit*) adalah fungsi aktivasi nonlinier berbentuk x dikali sigmoid(x). Lapisan Conv2D kemudian mereduksi fitur menjadi jumlah kanal keluaran yang dibutuhkan, dan lapisan Detect mengonsolidasikan prediksi akhir: koordinat kotak pembatas, skor *objectness* (keyakinan bahwa kotak berisi objek apa pun), dan skor kelas. Skema prediksi ini mewarisi desain *anchor-free* YOLOv8: posisi kotak diregresikan langsung, tanpa kotak acuan berukuran tetap.

Alur data satu kali inferensi dirangkum pada diagram berikut:

```
citra masukan 640x640 piksel
        │
        ▼
┌─ BACKBONE ───────────────────────────────────────────┐
│ konvolusi + blok C3k2 berulang (resolusi turun)       │
│ ujung: SPPF -> C2PSA (pembobotan spasial peta fitur)  │
└──────────────────────────────────────────────────────┘
   ▼ P3 80x80      ▼ P4 40x40      ▼ P5 20x20
┌─ NECK ───────────────────────────────────────────────┐
│ upsample + gabungan fitur antarskala + blok C3k2      │
└──────────────────────────────────────────────────────┘
        │  (tiga cabang ke head, satu per skala)
        ▼
┌─ HEAD ───────────────────────────────────────────────┐
│ C3k2 -> CBS -> Conv2D -> lapisan Detect               │
└──────────────────────────────────────────────────────┘
        ▼
keluaran deteksi: koordinat box + objectness + skor kelas
tugas lain: masker segmentasi | titik pose | box bersudut OBB
```

P3, P4, dan P5 adalah peta fitur pada tiga tingkat resolusi; cabang 80×80 menangkap objek kecil, cabang 20×20 menangkap objek besar. Blok C3k2 muncul di ketiga komponen, sedangkan C2PSA hanya muncul sekali, di ujung *backbone*.

### Cakupan Tugas dan Skala Model

Di luar deteksi standar, arsitektur yang sama mendukung lima tugas tambahan: segmentasi instans (pemisahan tiap objek hingga tingkat piksel), klasifikasi citra, estimasi pose (pendeteksian titik-titik kunci tubuh), deteksi objek berorientasi atau OBB (kotak pembatas dengan sudut rotasi, dipakai antara lain untuk citra udara), serta pelacakan objek antar-*frame*. Setiap tugas tersedia dalam lima ukuran model: n dengan 2,6 juta parameter, s dengan 9,4 juta, m dengan 20,1 juta, l dengan 25,3 juta, dan x dengan 56,9 juta — rentang yang dimaksudkan dari perangkat tepi (*edge device*, komputer kecil di dekat sumber data) hingga server ber-GPU.

## Eksperimen dan Hasil

Pengujian yang dirangkum makalah memakai dataset COCO, tolok ukur deteksi objek dengan 80 kelas. Metriknya mAP50-95, yaitu *mean Average Precision* (rata-rata presisi pada berbagai ambang *recall*, dirata-ratakan lintas kelas) yang dihitung pada ambang IoU 0,50 hingga 0,95 dengan langkah 0,05; IoU (*Intersection over Union*) adalah rasio luas irisan terhadap luas gabungan antara kotak prediksi dan kotak kebenaran. Makalah menampilkan kurva tolok ukur YOLOv11 terhadap YOLOv5 sampai YOLOv10 dengan angka yang mengacu dokumentasi resmi Ultralytics.

Angka kunci pada COCO, masukan 640 piksel (FLOPs adalah jumlah operasi *floating-point*, ukuran biaya komputasi per citra):

| Model | mAP50-95 | Parameter (juta) | FLOPs (miliar) |
|---|---|---|---|
| YOLOv8n | 37,3 | 3,2 | 8,7 |
| YOLO11n | 39,5 | 2,6 | 6,5 |
| YOLOv8m | 50,2 | 25,9 | 78,9 |
| YOLO11m | 51,5 | 20,1 | 68,0 |
| YOLO11x | 54,7 | 56,9 | 194,9 |

Interpretasi per pasangan ukuran. Pada skala *nano*, YOLO11n menaikkan mAP 2,2 poin sekaligus memangkas parameter sekitar 19% dan FLOPs sekitar 25%; akurasi dan efisiensi membaik bersamaan, bukan saling tukar. Pada skala *medium*, YOLO11m unggul 1,3 poin mAP dengan 22% parameter lebih sedikit — inilah klaim efisiensi utama yang dikutip makalah. Pada skala terbesar, YOLO11x mencapai 54,7% mAP, melampaui YOLOv8x (53,9%).

Sisi kecepatan dilaporkan dalam bentuk latensi, yaitu waktu pemrosesan satu citra. Menurut makalah, YOLOv11s mempertahankan akurasi sekitar 47% mAP pada latensi 2–6 milidetik, dan YOLOv11x sekitar 54,5% mAP pada 13 milidetik. Dokumentasi Ultralytics yang dirujuk mencatat angka lebih rinci: YOLO11s 47,0% mAP pada 2,5 ms dan YOLO11x 54,7% mAP pada 11,3 ms, diukur pada GPU T4 dengan TensorRT (pustaka optimasi inferensi NVIDIA). Latensi 2,5 ms setara dengan 400 citra per detik, jauh di atas kebutuhan video 30 FPS.

## Kelebihan dan Keterbatasan

Kelebihan makalah: menyusun deskripsi arsitektur YOLOv11 yang runtut dari sumber resmi yang tersebar; mengidentifikasi tiga perubahan inti (C3k2, C2PSA, head) secara tepat; serta mendokumentasikan cakupan multi-tugas dan skala model dalam satu rujukan. Bagi pembaca, makalah ini berfungsi sebagai acuan komponen sebelum membaca kode sumber.

Keterbatasan: (1) naskah bersifat tinjauan, bukan kontribusi metode; seluruh angka kinerja bersumber dari tolok ukur vendor dan tidak direproduksi secara independen oleh penulis. (2) Detail pelatihan — fungsi *loss*, augmentasi data, anggaran epoch — tidak dibahas karena Ultralytics memang tidak mempublikasikannya, sehingga perbandingan terbatas pada arsitektur. (3) Penamaan C2PSA tidak konsisten antara abstrak dan isi naskah (dicatat pada bagian Poin untuk Sitasi). (4) Secara konseptual, tafsiran "k2" sebagai "kernel size 2" adalah penjelasan penulis tinjauan, bukan dokumentasi resmi Ultralytics. (5) Dari sisi rekayasa, angka latensi diukur pada konfigurasi spesifik (GPU T4, TensorRT), sehingga tidak otomatis berlaku pada perangkat tepi lain.

## Kaitan dengan Bab Lain

Bab ini melanjutkan garis yang diletakkan [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md): formulasi regresi satu tahap tetap menjadi dasar, hanya blok pengolah fiturnya yang berganti. Dari sisi waktu, YOLOv11 hadir sesudah dua pembaruan konseptual pada tahun yang sama, yaitu [bab 008 (YOLOv9)](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md) dan [bab 009 (YOLOv10)](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md), tetapi tidak mewarisi gagasan keduanya secara langsung; basisnya justru YOLOv8 dari pengembang yang sama. Perubahannya bersifat evolusi blok (C2f menjadi C3k2) dan penambahan atensi (C2PSA), bukan perubahan paradigma. Posisi YOLOv11 dalam keseluruhan evolusi lini ini juga dibahas pada [bab 032 (survei evolusi YOLO)](./032%20-%202024%20-%20YOLO%20Evolution%20Benchmark%20%28Alif%20%26%20Hussain%29%20-%20Survei%20YOLO.md), yang menempatkannya sebagai rilis terbaru dalam perbandingan lintas versi.

## Poin untuk Sitasi

Kutip dengan kunci `khanam2024yolov11`. Ringkasan yang aman dikutip: "Khanam dan Hussain (2024) menyusun tinjauan arsitektural YOLOv11 dan mengidentifikasi blok C3k2, modul atensi spasial C2PSA, serta head yang disusun ulang sebagai perubahan utama terhadap YOLOv8, dengan dukungan enam tugas visi dalam satu kerangka."

Catatan verifikasi sebelum sitasi formal: (1) seluruh angka mAP, parameter, FLOPs, dan latensi pada bab ini mengacu dokumentasi resmi Ultralytics (docs.ultralytics.com) sebagaimana dikutip makalah, bukan eksperimen penulis; cocokkan ulang sebelum dikutip. (2) Abstrak makalah menulis C2PSA sebagai "*Convolutional block with Parallel Spatial Attention*", sedangkan bagian 4.1.2 menulis "*Cross Stage Partial with Spatial Attention*" — pilih sesuai konteks kutipan. (3) Untuk model YOLOv11 itu sendiri, rujukan primer yang diminta Ultralytics adalah entri perangkat lunak (Jocher dan Qiu, 2024, repositori Ultralytics), bukan makalah tinjauan ini. (4) Tafsiran "k2" sebagai ukuran *kernel* 2 adalah penjelasan penulis makalah, bukan dokumentasi resmi.
