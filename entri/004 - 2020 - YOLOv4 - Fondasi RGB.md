# 004 - YOLOv4: Optimal Speed and Accuracy of Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bochkovskiy2020yolov4` |
| Judul asli | YOLOv4: Optimal Speed and Accuracy of Object Detection |
| Penulis | Alexey Bochkovskiy, Chien-Yao Wang, Hong-Yuan Mark Liao |
| Tahun | 2020 |
| Venue | arXiv preprint arXiv:2004.10934 |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2004.10934
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOv4%3A%20Optimal%20Speed%20and%20Accuracy%20of%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOv4%3A%20Optimal%20Speed%20and%20Accuracy%20of%20Object%20Detection&sort=relevance

## Gambaran Umum

YOLOv4 bukanlah paradigma baru, melainkan **sintesis rekayasa**: penulisnya mengumpulkan puluhan teknik peningkatan deteksi yang tersebar di literatur 2015–2020, menguji kombinasinya secara sistematis, dan menyusun hasil terbaiknya menjadi satu resep detektor. Resep itu terdiri atas backbone CSPDarknet53, neck SPP + PANet, dan head YOLOv3 (bab 003), dilatih dengan seperangkat teknik yang dikelompokkan menjadi *Bag of Freebies* (teknik yang menambah biaya hanya saat pelatihan) dan *Bag of Specials* (modul yang menambah sedikit biaya inferensi demi akurasi yang jauh lebih besar).

Hasilnya: 43,5% AP (65,7% AP50) pada COCO dengan kecepatan ±65 FPS pada satu GPU V100 — titik kecepatan-akurasi terbaik pada masanya. Sama pentingnya, seluruh resep dapat dilatih pada **satu GPU konsumen** (1080 Ti atau 2080 Ti), sehingga detektor kelas riset menjadi terjangkau bagi praktisi — alasan utama YOLOv4 menjadi basis banyak bab aplikasi dalam tinjauan ini.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Antara 2015 dan 2020, literatur deteksi objek menghasilkan banyak teknik perbaikan: fungsi loss baru, metode augmentasi, modul perhatian, desain backbone hemat komputasi, dan sebagainya. Namun teknik-teknik itu diusulkan terpisah-pisah, diuji pada detektor yang berbeda-beda, dan tidak jelas kombinasi mana yang benar-benar bekerja ketika disatukan. Praktisi yang ingin memakai detektor terbaik harus menebak sendiri resepnya — dan sebagian resep menuntut pelatihan multi-GPU yang mahal.

YOLOv3 (bab 003) pada saat yang sama sudah menjadi baseline industri karena cepat dan stabil, tetapi akurasinya mulai tertinggal dari detektor baru seperti EfficientDet (bab 021). Pertanyaan yang dijawab makalah ini: seberapa jauh akurasi YOLOv3 dapat dinaikkan hanya dengan memilih dan mengombinasikan teknik yang sudah ada, tanpa mengorbankan kecepatan *real-time* dan tanpa menuntut perangkat pelatihan besar?

## Ide Utama

Gagasan pengorganisasian makalah ini adalah pembagian semua teknik peningkatan ke dalam dua kantong:

- ***Bag of Freebies* (BoF)** — teknik yang hanya mengubah strategi pelatihan tanpa menambah biaya inferensi sedikit pun: metode augmentasi data, fungsi loss yang lebih baik, regularisasi, penjadwalan laju pembelajaran. Karena "gratis" saat model dipakai, teknik ini murni menguntungkan bila terbukti menaikkan akurasi.
- ***Bag of Specials* (BoS)** — modul arsitektur atau pasca-pemrosesan yang menambah sedikit biaya inferensi tetapi memberi lompatan akurasi yang tidak sebanding kecilnya: perluasan receptive field, modul perhatian, agregasi fitur, NMS yang lebih baik.

Dengan kerangka ini, kontribusi makalah adalah **kurasi berbasis eksperimen**: setiap kandidat teknik diuji pengaruhnya pada detektor yang sama, dan hanya yang terbukti pada konfigurasi YOLO yang dipertahankan.

## Cara Kerja Langkah demi Langkah

### Arsitektur: Backbone, Neck, Head

Detektor YOLOv4 dipahami paling mudah sebagai tiga bagian. **Backbone** CSPDarknet53 adalah Darknet-53 (bab 003) yang dimodifikasi dengan *Cross Stage Partial* (CSP): peta fitur pada setiap tahap dibelah dua — satu cabang melewati blok residual, satu cabang menjadi pintasan — lalu keduanya digabung kembali. Pembelahan ini mengurangi komputasi sekitar 20% sekaligus memperkaya aliran gradien, sehingga akurasi terjaga atau justru naik dengan biaya lebih murah.

**Neck** terdiri atas dua modul. SPP (*Spatial Pyramid Pooling*) meneruskan peta fitur melalui beberapa *max-pooling* berukuran berbeda (5×5, 9×9, 13×13) secara paralel lalu menggabungkan hasilnya dengan masukan asal; efeknya, receptive field diperluas tanpa mengubah resolusi. PANet (*Path Aggregation Network*) menambah jalur agregasi **bottom-up** di atas jalur top-down ala FPN (bab 018): informasi lokasi yang rinci dari lapis dangkal disalurkan ke atas, melengkapi informasi semantik dari lapis dalam yang disalurkan ke bawah. **Head** tetap kepala prediksi YOLOv3 — tiga skala, berbasis *anchor*.

Susunan ketiga bagian dan tempat dua "kantong" teknik bekerja:

```
citra ──► backbone CSPDarknet53 ──► neck ──► head YOLOv3 ──► deteksi
              │                  ┌──┴──┐        │              │
              │                  ▼     ▼        ▼              ▼
        fitur dibelah dua,    SPP   PANet   3 skala,     NMS (DIoU):
        digabung kembali   (pool  (top-down  anchor      saring kotak
        (hemat ±20% FLOPs)  5/9/13) +bottom-up)           duplikat

  Bag of Freebies (hanya saat latih): Mosaic, CutMix, CmBN, DropBlock,
      label smoothing, CIoU loss, SAT, cosine annealing
  Bag of Specials (biaya inferensi kecil): Mish, CSP, SPP, SAM, PAN, DIoU-NMS
```

### Bag of Freebies: Teknik Pelatihan

Teknik BoF yang dipertahankan setelah seleksi antara lain:

- **Mosaic augmentation**: empat citra pelatihan digabung menjadi satu citra komposit. Model belajar mengenali objek pada konteks dan skala yang lebih beragam dalam satu masukan, dan statistik *batch normalization* dihitung dari empat citra sekaligus — ini mengurangi kebutuhan *mini-batch* besar, kunci pelatihan pada satu GPU.
- **CIoU loss**: fungsi loss regresi kotak pengganti sum-squared. Selain menghukum ketidakcocokan luasan (IoU), CIoU juga menghukum jarak antara pusat kotak prediksi dan kebenaran serta ketidaksesuaian rasio aspek, sehingga regresi kotak konvergen lebih cepat dan lebih tepat.
- **Self-Adversarial Training (SAT)**: pelatihan dua tahap di mana model terlebih dahulu menghasilkan citra adversarial terhadap dirinya sendiri (mengubah piksel, bukan bobot, untuk "menipu" deteksi), kemudian dilatih agar tetap mendeteksi dengan benar pada citra yang diubah itu — bentuk regularisasi yang memperkuat ketahanan.
- **CmBN** (*Cross mini-Batch Normalization*): statistik normalisasi dikumpulkan dari beberapa iterasi kecil dalam satu *batch*, menstabilkan pelatihan batch kecil.
- Pendukung lain: *label smoothing* (target kelas dilembutkan dari 0/1 keras menjadi nilai antara, mengurangi overconfidence), *DropBlock* (regularisasi yang membuang blok wilayah bersebelahan pada peta fitur alih-alih piksel acak), penjadwalan *cosine annealing*, dan bentuk masukan acak.

### Bag of Specials: Modul Tambahan

Teknik BoS yang dipertahankan antara lain: aktivasi **Mish** (fungsi aktivasi halus pengganti ReLU yang terbukti memberi akurasi sedikit lebih baik pada backbone ini), **SAM** termodifikasi (*Spatial Attention Module*: modul perhatian yang menimbang wilayah penting pada peta fitur; penulis mengubahnya dari perhatian spasial menjadi perhatian titik), dan **DIoU-NMS**: *Non-Maximum Suppression* yang menyeleksi kotak duplikat bukan hanya dari luas irisan, tetapi juga jarak antar-pusat kotak, sehingga dua objek bersebelahan lebih jarang saling hapus.

## Eksperimen dan Hasil

Pengujian dilakukan pada COCO dengan analisis ablation menyeluruh — inilah nilai ilmiah utama makalah ini: pengaruh tiap fitur, tiap kombinasi BoF/BoS, dan tiap pilihan backbone diukur terpisah. Hasil akhir pada COCO test-dev:

- YOLOv4: 43,5% AP dan 65,7% AP50, pada kecepatan ±65 FPS (Tesla V100).
- Peningkatan terhadap YOLOv3 (33,0% AP, bab 003): sekitar 10 poin AP tanpa kehilangan status *real-time*.
- Perbandingan sezaman: mengungguli kombinasi kecepatan-akurasi EfficientDet pada pengujian penulis, dengan kebutuhan pelatihan jauh lebih ringan.

Ablation menunjukkan CSP backbone, Mosaic, dan CIoU termasuk penyumbang gain paling konsisten; dan yang tak kalah penting bagi praktik, seluruh konfigurasi terbukti dapat dilatih pada satu GPU 1080 Ti/2080 Ti.

## Kelebihan dan Keterbatasan

Kelebihan: (1) titik kecepatan-akurasi terbaik saat rilis; (2) resep lengkap dan terdokumentasi, direproduksi luas; (3) hemat perangkat — pelatihan satu GPU; (4) nilai metodologis: peta kontribusi puluhan teknik dalam satu kerangka uji.

Keterbatasan: (1) jumlah teknik dan hiperparameter yang ditumpuk sangat banyak, sehingga menyetel ulang untuk dataset baru tidak sepele; (2) tetap berbasis *anchor*; (3) peningkatannya bersifat rekayasa inkremental, bukan gagasan konseptual baru; (4) dari sisi reproduksi, sebagian klaim ablation sensitif pada detail implementasi yang tidak semuanya terdokumentasi selengkap kode sumbernya.

## Kaitan dengan Bab Lain

Resep YOLOv4 berdiri langsung di atas bab 003: head dan kerangka dasarnya adalah YOLOv3. Bahan-bahannya datang dari banyak bab lain: piramida fitur FPN (bab 018), pola CSP dari keluarga desain backbone, serta tradisi augmentasi dan loss dari literatur deteksi umum. Sebagai "resep jadi", YOLOv4 menjadi basis modifikasi aplikatif dalam tinjauan ini — misalnya deteksi bunga apel dengan pemangkasan model (bab 122) — dan menjadi titik referensi bagi YOLOX (bab 005) yang kemudian merombak head-nya menjadi *anchor-free*.

## Poin untuk Sitasi

Kutip dengan kunci `bochkovskiy2020yolov4`. Ringkasan yang aman dikutip: "YOLOv4 menyeleksi dan mengombinasikan teknik pelatihan (Bag of Freebies: Mosaic, CIoU loss, SAT) dan modul arsitektur (Bag of Specials: CSP, SPP, PAN, Mish) menjadi detektor 43,5% AP pada COCO dengan ±65 FPS yang dapat dilatih pada satu GPU konsumen." Angka 43,5% / 65,7% AP50 / ±65 FPS dari abstrak naskah; rincian ablation per komponen sebaiknya dikutip langsung dari tabel-tabel naskah.
