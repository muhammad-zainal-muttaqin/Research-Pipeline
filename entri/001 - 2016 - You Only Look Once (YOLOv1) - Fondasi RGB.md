# 001 - You Only Look Once: Unified, Real-Time Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `redmon2016yolo` |
| Judul asli | You Only Look Once: Unified, Real-Time Object Detection |
| Penulis | Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi |
| Tahun | 2016 |
| Venue | IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2016) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1506.02640
- **Google Scholar:** https://scholar.google.com/scholar?q=You%20Only%20Look%20Once%3A%20Unified%2C%20Real-Time%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=You%20Only%20Look%20Once%3A%20Unified%2C%20Real-Time%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan YOLO (*You Only Look Once*), detektor objek pertama yang merumuskan deteksi objek sebagai satu masalah regresi tunggal: dari piksel citra masukan langsung ke koordinat *bounding box* (kotak pembatas objek) dan probabilitas kelas, diselesaikan oleh satu jaringan saraf konvolusi dalam satu kali evaluasi. Rumusan ini menggantikan *pipeline* multi-tahap yang dipakai detektor paling akurat pada masanya (keluarga R-CNN) menjadi satu jaringan yang dilatih *end-to-end* (dari masukan ke keluaran tanpa tahap terpisah).

Hasilnya adalah lompatan kecepatan: model penuh mencapai 45 *frame* per detik (FPS) dengan 63,4% mAP pada PASCAL VOC 2007, dan varian ringkasnya (Fast YOLO) mencapai 155 FPS. Sebagai perbandingan, detektor dua tahap tercepat saat itu hanya berjalan 0,5–7 FPS. Makalah ini adalah titik awal seluruh keluarga YOLO; hampir semua bab klaster Fondasi RGB dalam tinjauan ini mewarisi formulasi yang diletakkan di sini.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum 2016, detektor objek paling akurat bekerja dalam dua tahap. R-CNN (bab 012) terlebih dahulu mengusulkan sekitar 2.000 kandidat wilayah citra (*region proposal*) dengan algoritme *selective search*, kemudian mengekstrak fitur setiap wilayah dengan CNN dan mengklasifikasikannya satu per satu. Fast R-CNN (bab 013) mempercepat proses ini dengan berbagi perhitungan konvolusi untuk seluruh citra, tetapi tetap bergantung pada *region proposal* dari algoritme eksternal. Pendekatan yang lebih tua, DPM (*Deformable Parts Model*), memakai *sliding window*: sebuah pengklasifikasi dievaluasi berulang kali pada banyak jendela yang digeser menutupi seluruh citra.

Ketiga pendekatan tersebut memiliki tiga masalah yang sama. Pertama, komponen-komponennya dilatih secara terpisah (pengusul wilayah, pengekstrak fitur, pengklasifikasi, pasca-pemrosesan), sehingga sistem tidak dapat dioptimalkan secara menyeluruh terhadap tujuan akhir deteksi. Kedua, kecepatannya jauh dari *real-time* — orde detik per citra — sehingga tidak layak untuk robotika atau kendaraan otonom. Ketiga, karena setiap kandidat wilayah dinilai terpisah dari konteks penuh, metode berbasis wilayah relatif sering salah mengenali latar belakang sebagai objek (*false positive* latar).

## Ide Utama

Gagasan inti YOLO adalah membuang tahap pengusulan wilayah sama sekali. Deteksi dipandang sebagai regresi: satu jaringan menerima seluruh citra dan, dalam satu evaluasi, mengeluarkan semua kotak objek beserta kelasnya secara serentak. Karena jaringan memproses citra penuh sekaligus, informasi konteks global tersedia pada saat prediksi dibuat — berbeda dengan metode wilayah yang hanya melihat potongan citra.

Mekanismenya sederhana: citra dibagi menjadi *grid* (kisi) S×S sel. Setiap sel diberi tanggung jawab mendeteksi objek yang **titik pusatnya** jatuh di dalam sel tersebut. Setiap sel langsung memprediksi posisi kotak objek, tingkat keyakinan bahwa kotak itu berisi objek, dan kelas objeknya. Dengan desain ini, deteksi tidak lagi merupakan rangkaian tahap, melainkan satu pemetaan dari citra ke tensor keluaran.

## Cara Kerja Langkah demi Langkah

### Pembagian Grid dan Tanggung Jawab Prediksi

YOLO memakai S = 7, sehingga citra dibagi menjadi 7×7 = 49 sel. Pada citra masukan 448×448 piksel, setiap sel mencakup wilayah 64×64 piksel. Bila pusat sebuah objek jatuh pada sel tertentu, hanya sel itu yang diharapkan memprediksi objek tersebut; sel lain mengabaikannya. Pembagian tanggung jawab inilah yang membuat satu jaringan dapat menghasilkan banyak deteksi sekaligus tanpa tahap proposal.

Skema pembagian tugas dari citra ke tensor keluaran:

```
citra 448x448                        keluaran: tensor 7 x 7 x 30
┌───┬───┬───┬───┬───┬───┬───┐
│   │   │   │   │   │   │   │      setiap sel berisi 30 angka:
├───┼───┼───┼───┼───┼───┼───┤      ┌─ kotak 1: x, y, w, h, confidence
│   │   │   │   │   │   │   │      ├─ kotak 2: x, y, w, h, confidence
├───┼───┼───┼───┼───┼───┼───┤      └─ 20 probabilitas kelas (per sel)
│   │   │   │╔═══╗│   │   │ │
├───┼───┼───┤║anjing║├───┼───┤      pusat objek jatuh di sel (3,2)
│   │   │   │╚═══╝│   │   │ │  ->  hanya sel itu yang memprediksi
├───┼───┼───┼───┼───┼───┼───┤      kotak dan kelas anjing
│   │   │   │   │   │   │   │
└───┴───┴───┴───┴───┴───┴───┘
   sel 64x64 piksel
```

### Keluaran Jaringan

Setiap sel memprediksi dua hal sekaligus:

1. **B = 2 kandidat kotak.** Setiap kotak dinyatakan lima angka: (x, y) posisi pusat kotak relatif terhadap batas sel, (w, h) lebar dan tinggi relatif terhadap ukuran citra, serta skor *confidence*. Skor ini didefinisikan sebagai Pr(objek) × IOU, yaitu probabilitas adanya objek dikali IOU (*Intersection over Union* — rasio luas irisan terhadap luas gabungan antara kotak prediksi dan kotak kebenaran). Jadi, skor tinggi menuntut keduanya: ada objek dan posisinya tepat.
2. **C = 20 probabilitas kelas** (PASCAL VOC memiliki 20 kelas), berupa probabilitas bersyarat Pr(kelas | objek): bila sel ini memang berisi objek, berapa peluang objek itu termasuk tiap kelas.

Dengan demikian, keluaran akhir jaringan adalah tensor berukuran 7×7×(2×5 + 20) = 7×7×30: 49 sel, masing-masing memuat 10 angka kotak dan 20 angka kelas. Perlu dicatat bahwa probabilitas kelas dibuat **satu set per sel**, bukan per kotak — konsekuensi ini penting pada bagian keterbatasan.

### Arsitektur Jaringan

Jaringan terdiri atas 24 lapis konvolusi diikuti 2 lapis *fully connected* (terhubung penuh). Polanya terinspirasi GoogLeNet: konvolusi 1×1 dipakai untuk mereduksi jumlah kanal sebelum konvolusi 3×3, sehingga biaya komputasi tertekan. Bobot awal diperoleh dengan melatih 20 lapis pertama sebagai pengklasifikasi ImageNet pada resolusi 224×224, kemudian seluruh jaringan disetel halus (*fine-tuning*) untuk deteksi pada resolusi 448×448. Varian Fast YOLO memangkas arsitektur menjadi 9 lapis konvolusi dengan jumlah *filter* lebih sedikit.

### Fungsi Loss

Pelatihan memakai *sum-squared error* (jumlah kuadrat selisih) antara prediksi dan target, dengan tiga komponen: galat koordinat kotak, galat skor *confidence*, dan galat probabilitas kelas. Dua bobot pengimbang diperlukan karena struktur keluarannya tidak simetris. Sebagian besar sel tidak berisi objek (dari 49×2 = 98 kotak kandidat, mungkin hanya beberapa yang benar-benar menutupi objek); tanpa pembobotan, gradien akan didominasi oleh sel-sel kosong. Karena itu bobot galat koordinat dinaikkan (λ_coord = 5) dan bobot galat *confidence* pada sel tanpa objek diturunkan (λ_noobj = 0,5). Selain itu, lebar dan tinggi kotak diprediksi dalam bentuk akar kuadrat (√w, √h): selisih 10 piksel pada kotak kecil jauh lebih fatal daripada pada kotak besar, dan bentuk akar membuat fungsi loss mencerminkan hal itu tanpa memerlukan dua fungsi berbeda.

### Inferensi

Saat inferensi, citra dilewatkan melalui jaringan satu kali. Untuk setiap kotak, skor kepercayaan per kelas dihitung sebagai Pr(kelas | objek) × *confidence*. Kotak-kotak yang tumpang tindih untuk objek yang sama kemudian dirampingkan dengan *Non-Maximum Suppression* (NMS): dari sekumpulan kotak yang saling menutupi, hanya kotak berskor tertinggi yang dipertahankan. Seluruh proses ini berjalan 45 kali per detik pada GPU saat itu.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada PASCAL VOC 2007 dan 2012, tolok ukur standar deteksi objek saat itu. Metrik yang dipakai adalah mAP (*mean Average Precision*): rata-rata presisi di seluruh kelas dan ambang — semakin tinggi semakin baik, maksimal 100%.

Hasil kunci pada VOC 2007:

- YOLO (model penuh): 63,4% mAP pada 45 FPS.
- Fast YOLO: 52,7% mAP pada 155 FPS.
- Pembanding pada saat yang sama: Fast R-CNN 70,0% mAP pada ±0,5 FPS; Faster R-CNN 73,2% mAP pada 7 FPS.

Interpretasinya: YOLO mengorbankan sekitar 10 poin mAP terhadap detektor dua tahap terbaik, tetapi memperoleh kecepatan 6–90 kali lipat — dan untuk pertama kalinya membuktikan deteksi akurat dapat berjalan *real-time*.

Analisis galat pada makalah membandingkan jenis kesalahan YOLO dengan Fast R-CNN. Galat dominan YOLO adalah **lokalisasi** (kotak kurang tepat posisinya), sedangkan galat dominan Fast R-CNN adalah **latar belakang** (mengenali daerah tanpa objek sebagai objek; ±13,6% deteksi teratasnya berupa *false positive* latar, dibandingkan ±4,75% pada YOLO). Perbedaan ini konsisten dengan desain masing-masing: YOLO menilai citra penuh sehingga jarang tertipu tekstur latar, tetapi prediksi satu sel mencakup wilayah luas sehingga posisi kotak kurang halus. Karena tipe galatnya berbeda, menggabungkan keduanya menaikkan mAP gabungan hingga ±75% — bukti bahwa kedua pendekatan saling menutupi kelemahan.

Temuan terakhir: YOLO menggeneralisasi lebih baik ke domain di luar foto natural. Pada pengujian dengan citra lukisan (dataset People-Art dan Picasso), YOLO mempertahankan akurasi jauh lebih baik daripada R-CNN dan DPM.

## Kelebihan dan Keterbatasan

Kelebihan: (1) sangat cepat karena hanya satu evaluasi jaringan; (2) satu model utuh yang dilatih *end-to-end*, tanpa komponen eksternal; (3) *false positive* latar rendah berkat konteks global; (4) generalisasi lintas domain lebih baik dari pesaingnya.

Keterbatasan: (1) setiap sel hanya memprediksi satu kelas dan dua kotak, sehingga objek kecil yang berkelompok — misalnya sekawanan burung dalam satu sel — sering terlewat; (2) total deteksi dibatasi desain spasial 49 sel, sehingga *recall* (proporsi objek yang berhasil ditemukan) lebih rendah dari metode dua tahap; (3) lokalisasi kurang presisi, terutama untuk objek dengan rasio aspek yang tidak lazim; (4) fungsi loss sum-squared memperlakukan galat pada kotak besar dan kecil hampir setara — diperbaiki sebagian oleh bentuk akar kuadrat, tetapi tidak tuntas. Keterbatasan (1) dan (2) inilah yang menjadi sasaran perbaikan langsung pada generasi berikutnya.

## Kaitan dengan Bab Lain

Bab ini berdiri sebagai antitesis dari paradigma dua tahap yang dibahas pada bab 012 (R-CNN) dan bab 013 (Fast R-CNN). Generasi penerusnya membentuk garis lurus perbaikan: bab 002 (YOLOv2) menyerang masalah *recall* dan lokalisasi lewat *anchor box* dan pelatihan multi-skala; bab 003 (YOLOv3) menambah prediksi tiga skala untuk objek kecil; bab 004 (YOLOv4) menyusun resep pelatihan optimal di atas fondasi yang sama; bab 005 (YOLOX) kemudian melepaskan *anchor* dan menyempurnakan penetapan label. Formulasi "grid + regresi langsung" yang diperkenalkan di sini diwarisi oleh semuanya, termasuk turunan aplikatif pada klaster YOLO plus RGB-D.

## Poin untuk Sitasi

Kutip dengan kunci `redmon2016yolo`. Ringkasan yang aman dikutip: "YOLO merumuskan deteksi objek sebagai regresi tunggal dari citra penuh ke kotak pembatas dan probabilitas kelas, mencapai 63,4% mAP pada PASCAL VOC 2007 dengan kecepatan 45 FPS — detektor *real-time* terpadu pertama." Angka 63,4% / 45 FPS / 52,7% / 155 FPS berasal dari naskah; rincian analisis galat (13,6% vs 4,75%) dan hasil kombinasi dengan Fast R-CNN (±75% mAP) sebaiknya diverifikasi ulang ke tabel naskah sebelum dikutip dalam karya formal.
