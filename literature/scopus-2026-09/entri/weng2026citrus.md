# Citrus tracking and counting using UAV remote sensing video imagery with improved YOLO11

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `weng2026citrus` |
| Judul asli | Citrus tracking and counting using UAV remote sensing video imagery with improved YOLO11 |
| Penulis | Weng, H.; others |
| Tahun | 2026 |
| Venue | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [weng2026citrus.pdf](../pdf/weng2026citrus.pdf)
- DOI resmi: https://doi.org/10.11975/j.issn.1002-6819.202508166

## Gambaran Umum
Makalah ini (berbahasa Mandarin, dengan abstrak berbahasa Inggris) mengusulkan metode pelacakan dan penghitungan buah jeruk dari video pesawat nirawak (*UAV*) yang menggabungkan detektor ringan YOLO11-PMSL dengan pelacak ByteTrack-DIoU. YOLO11-PMSL dibangun dari YOLO11n dengan empat perubahan: kepala deteksi disederhanakan menjadi tiga tingkat P2 sampai P4, modul penguat tepi multi-skala C3k2-MSEIE, fungsi *loss* SIoU sebagai pengganti CIoU, dan pemangkasan (*pruning*) LAMP. Pada ByteTrack, ukuran kemiripan IoU diganti dengan DIoU, dan ditambahkan mekanisme penghitungan wilayah dengan antigetar (*anti-shake*) berbasis garis deteksi virtual.

Objek penelitian adalah jeruk "Navel Orange 52" (脐橙52号) di kebun di Kabupaten Minhou, Fuzhou, Provinsi Fujian, yang direkam pada November 2024 dengan DJI Phantom 4. Terkumpul 30 klip video; dari video itu diekstraksi 3.549 citra beresolusi 4.096 × 2.160. Pada set uji, YOLO11-PMSL mencapai presisi 86,3%, *recall* 83,0%, dan mAP0,5 90,5% (YOLO11n: 83,0%; 71,4%; 81,2%) dengan 0,36 juta parameter, 4,6 GFLOPs, ukuran model 1,3 MB, dan 140,12 FPS. Dengan ByteTrack-DIoU, MOTA mencapai 92,8%, MOTP 81,7%, IDF1 92,0%, dan akurasi hitung rerata (*mean counting accuracy*, MCA) terhadap hitungan manual 88,4% pada lima video.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa estimasi hasil jeruk secara manual lambat, mahal, dan kurang akurat. Metode pengolahan citra klasik lemah terhadap latar kompleks dan oklusi, metode berbasis citra statis atau titik 3D memerlukan pengumpulan data yang memakan waktu dan peralatan mahal, dan banyak model deteksi terlalu berat untuk platform tepi (*edge*) hemat daya. Tiga masalah spesifik yang dirumuskan: (1) objek terlalu kecil dan latar rumit sehingga deteksi terlewat atau keliru, yang menentukan titik awal penghitungan; (2) ranting yang bergoyang dan buah yang padat menyebabkan hilangnya objek dan perpindahan identitas (*ID switch*) serta putusnya trek, sehingga identitas yang konsisten dalam waktu lama sulit dijaga; dan (3) model berkinerja tinggi berat secara komputasi sehingga sulit dijalankan waktu-nyata di perangkat tepi.

## Ide Utama
Gagasan utamanya ada dua. Pada deteksi, model dipersempit ke tingkat resolusi tinggi (P2 sampai P4) karena target pada citra udara semuanya kecil, sehingga kepala P5 yang dalam dibuang untuk menghemat komputasi, lalu pemangkasan LAMP menghilangkan bobot berlebih. Pada penghitungan, ukuran jarak DIoU memasukkan jarak titik pusat kotak ke dalam asosiasi sehingga lebih tahan terhadap pergeseran akibat gerak pesawat, angin, dan oklusi, dan penghitungan dilakukan melalui mesin status per trek yang hanya menambah hitungan setelah titik pusat kotak berada di dalam atau di luar wilayah selama $N = 5$ bingkai berturut-turut.

## Cara Kerja Langkah demi Langkah

```
  video UAV --> YOLO11-PMSL --> ByteTrack-DIoU --> mesin status wilayah
  (4K, 23,98     (P2-P4, MSEIE,   (dua tahap          (N = 5 bingkai;
   fps)           SIoU, LAMP)      asosiasi, DIoU)     hitung masuk/keluar)
```

### 1. Akuisisi Data dan Anotasi
Data direkam pada awal sampai pertengahan November 2024 di kebun Yuanwei Zonghe (Baisha, Minhou, Fuzhou; sekitar 119,04° BT, 26,22° LU). Pesawat nirawak terbang dengan sudut pandang miring sekitar 45°, ketinggian di atas 2 m dari tanah, jarak horizontal minimum 0,5 m dari tajuk di kedua sisi, dan kecepatan konstan 0,5 m/s. Terkumpul 30 klip video efektif beresolusi 4.096 × 2.160 piksel pada 23,98 bingkai per detik. Setelah perekaman, buah pada tiap baris pohon dihitung manual satu per satu. Satu bingkai diambil tiap 15 bingkai sehingga diperoleh 3.549 citra, dianotasi dengan LabelImg, dan dibagi acak 7:2:1 untuk latih, validasi, dan uji. Jumlah pohon dan jumlah bounding box tidak dilaporkan.

### 2. Modifikasi Detektor (YOLO11-PMSL)
- **Pemangkasan struktur piramida fitur.** Kepala P2 ditambahkan dari lapisan beresolusi tinggi dan kepala P5 dibuang, menghasilkan struktur P2 sampai P4.
- **C3k2-MSEIE.** Modul mengganti C3k2 pada lapisan backbone 2, 4, dan 6. Modul penguat tepi (EdgeEnhancer) memisahkan komponen frekuensi tinggi dari rata-rata pooling lalu memperkuatnya dengan konvolusi. MSEIE menjalankan empat cabang pooling adaptif (3×3, 6×6, 9×9, 12×12), tiap cabang dengan konvolusi 1×1 untuk memangkas kanal menjadi seperempat, konvolusi berkelompok, *upsampling*, penguatan tepi, dan penggabungan kanal.
- **SIoU.** Fungsi *loss* menambahkan komponen sudut, jarak, dan bentuk.
- **LAMP.** Pemangkasan terstruktur berbasis magnitudo yang adaptif per lapisan, dengan pelatihan ulang (*fine-tuning*) setelah tiap pemangkasan; laju pemangkasan 1,6 sampai 2,4 dicoba dan 2,2 dipilih.
- Pelatihan memakai 800 epoch, ukuran *batch* 8, optimizer Adam dengan laju belajar awal 0,001, pada Intel Core i7-13700KF dan NVIDIA GeForce RTX 3060 16 GB.

### 3. Pelacakan ByteTrack-DIoU
ByteTrack memakai strategi dua kali asosiasi (kotak berskor tinggi, lalu kotak berskor rendah) agar kotak berkeyakinan rendah akibat oklusi tetap dapat menyambung trek. Perubahan: biaya asosiasi memakai $1 - \text{DIoU}$, dengan $\text{DIoU} = \text{IoU} - \rho^2(b_{pred}, b_{det})/c^2$, sehingga pergeseran titik pusat ikut dihukum.

### 4. Penghitungan Wilayah dengan Antigetar
Setiap trek memiliki mesin status (OUTSIDE, ENTERING, INSIDE, LEAVING). Pencatatan dilakukan pada posisi pertama kali trek muncul: bila muncul di luar wilayah, berlaku saluran "masuk" (cocok untuk pesawat yang terbang menuju baris pohon); bila muncul di dalam wilayah, berlaku saluran "keluar". Hitungan dipicu hanya setelah titik pusat kotak berada di dalam atau di luar wilayah selama $N = 5$ bingkai berturut-turut, nilai yang diacu dari praktik pelacakan lain. Hitungan akhir adalah Count_enter atau Count_leave sesuai saluran.

### 5. Metrik
Deteksi: presisi, *recall*, mAP0,5, parameter, FLOPs, FPS. Pelacakan: MOTA, MOTP, IDF1. Penghitungan: MCA, yaitu rerata $P_i/G_i \times 100\%$ untuk $n$ video, dengan $P_i$ hitungan prediksi dan $G_i$ hitungan sebenarnya.

## Eksperimen dan Hasil
**Perbandingan detektor (Tabel 1, set uji citra jeruk).**

| Model | P (%) | R (%) | mAP0,5 (%) | Parameter (juta) | FLOPs (G) | Ukuran (MB) | FPS |
|---|---|---|---|---|---|---|---|
| Faster R-CNN | 68,9 | 53,4 | 64,6 | 41,35 | 134 | 472,1 | 30,9 |
| SSD | 73,7 | 75,9 | 76,5 | 23,75 | 214 | 272,1 | 24,8 |
| YOLOv8n | 78,6 | 70,3 | 77,8 | 2,68 | 6,8 | 5,6 | 82,83 |
| YOLOv9t | 79,6 | 74,4 | 80,8 | 1,73 | 6,4 | 4,2 | 87,06 |
| YOLOv10n | 82,8 | 69,4 | 80,6 | 2,26 | 6,5 | 5,8 | 85,46 |
| YOLO11n | 83,0 | 71,4 | 81,2 | 2,58 | 6,3 | 5,5 | 84,83 |
| YOLO12n | 80,7 | 70,6 | 78,8 | 2,51 | 5,8 | 5,2 | 75,49 |
| YOLO11-PMSL | 86,3 | 83,0 | 90,5 | 0,36 | 4,6 | 1,3 | 140,12 |

**Ablasi (Tabel 3).** YOLO11n: mAP0,5 81,2%. Penambahan P2 (P2345): 87,4% dengan 10,3 GFLOPs dan 58,32 FPS. Struktur P2 sampai P4: 86,3%, 1,16 juta parameter, 9,8 GFLOPs. Ditambah C3k2-MSEIE: 89,9%. Ditambah SIoU: P 85,2%, R 83,8%, mAP0,5 90,6%. Ditambah LAMP (YOLO11-PMSL): P 86,3%, R 83,0%, mAP0,5 90,5%, 0,36 juta parameter, 4,6 GFLOPs, 140,12 FPS. Penulis melaporkan penurunan parameter, ukuran model, dan FLOPs terhadap YOLO11n masing-masing 86,05%, 76,36%, dan 26,98% (selisih FLOPs 6,3 menjadi 4,6 G dapat diperiksa secara sederhana), dan kecepatan naik 65,18%.

**Laju pemangkasan (Tabel 2).** Pada laju 1,0, mAP0,5 90,6%, 1,21 juta parameter, 10,4 GFLOPs, 73,68 FPS. Pada 2,2: 90,5%, 0,36 juta parameter, 4,6 GFLOPs, 140,12 FPS; pada 2,4: 90,0%, 0,34 juta parameter, 4,2 GFLOPs, 155,14 FPS.

**Pelacakan (Tabel 4, detektor YOLO11-PMSL).**

| Pelacak | MOTA (%) | MOTP (%) | IDF1 (%) |
|---|---|---|---|
| SORT | 87,3 | 62,5 | 86,4 |
| DeepSORT | 87,1 | 62,3 | 89,0 |
| Bot-SORT | 88,5 | 70,9 | 90,6 |
| ByteTrack | 90,6 | 78,7 | 90,8 |
| ByteTrack-DIoU | 92,8 | 81,7 | 92,0 |

Selisih MOTA ByteTrack-DIoU terhadap SORT, DeepSORT, dan Bot-SORT adalah 5,5, 5,7, dan 4,3 poin persentase (dihitung dari tabel dan sesuai abstrak).

**Penghitungan (Tabel 5).** Lima video yang berkaitan dengan baris pohon ke-1, 2, 3, 5, dan 8.

| | Video 1 | Video 2 | Video 3 | Video 4 | Video 5 | MCA (%) |
|---|---|---|---|---|---|---|
| Hitungan manual | 970 | 1.522 | 963 | 899 | 860 | 88,4 |
| YOLO11-PMSL + ByteTrack-DIoU | 859 | 1.317 | 854 | 799 | 770 | |

Hitungan prediksi lebih rendah daripada hitungan manual pada kelima video. Rasio per video yang dihitung dari tabel adalah sekitar 88,6%, 86,5%, 88,7%, 88,9%, dan 89,5%, yang rerata sekitar 88,4% dan sesuai dengan MCA yang dilaporkan. Teks juga menyatakan bahwa hitungan prediksi berbeda kurang dari 12% dari hitungan manual. Penulis menyatakan bahwa MCA meningkat dengan penghitungan wilayah, tetapi hasil tanpa mekanisme itu tidak disajikan sebagai tabel terpisah pada teks yang tersedia.

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: model sangat ringan (0,36 juta parameter, 1,3 MB) dan cepat (140,12 FPS) sehingga cocok untuk perangkat tepi; pelacak ByteTrack-DIoU unggul pada MOTA, MOTP, dan IDF1; penghitungan wilayah mengurangi hitungan ganda akibat ID switch; deviasi hitungan dari hitungan manual di bawah 12%.

Penulis tidak menyajikan bagian keterbatasan tersendiri. Menurut pembacaan ringkasan ini terdapat beberapa hal yang perlu diperhatikan. Pertama, kelima video penghitungan semuanya menghasilkan hitungan di bawah hitungan manual, yang menunjukkan galat sistematis berupa buah yang tidak tertangkap (mungkin buah di sisi pohon yang tidak terlihat pesawat), yang tidak dianalisis. Kedua, jumlah video untuk MOTA, MOTP, dan IDF1 serta jumlah bingkai beranotasi identitas tidak dilaporkan. Ketiga, citra dibagi acak dari bingkai yang diekstraksi tiap 15 bingkai, sehingga bingkai yang mirip dari satu klip dapat jatuh pada set latih dan set uji; dari teks, tidak jelas apakah pembagian dilakukan per video. Keempat, rancangan penghitungan memakai arah terbang sejajar baris pohon dan satu sisi pandang, sehingga tidak ada mekanisme untuk menyatukan buah yang sama dari sisi pohon yang berbeda. Kelima, parameter $N = 5$ ditetapkan dengan merujuk karya lain dan tidak diuji sensitivitasnya pada teks yang tersedia. Keenam, pada Tabel 2, laju pemangkasan 2,2 dipilih meskipun laju 2,4 menghasilkan kecepatan yang lebih tinggi pada mAP0,5 yang hanya selisih 0,5 poin; pilihan itu bersifat subjektif.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video melalui pelacakan berbasis deteksi (ByteTrack dengan asosiasi DIoU dua tahap), lalu menghindari hitungan ganda dengan mesin status penghitungan yang hanya memicu hitungan setelah trek berada di dalam atau di luar wilayah selama lima bingkai berturut-turut. Mekanisme ini berlaku pada satu video yang terbang sejajar baris pohon dengan sudut miring dari satu sisi; tidak ada pencocokan lintas sisi pohon. Hitungan tidak dilaporkan per kelas (satu kelas jeruk, tanpa tingkat kematangan). Acuan hitung adalah hitungan manual buah per baris pohon, bukan hasil panen dan bukan anotasi citra.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: pengukuran asosiasi yang memasukkan jarak titik pusat untuk gerak antarbingkai yang besar, asosiasi dua tahap yang memanfaatkan deteksi berkeyakinan rendah pada oklusi, dan aturan hitung hanya setelah beberapa bingkai berturut-turut untuk menekan hitungan ganda dari getaran. Hasil hitungan yang konsisten lebih rendah daripada hitungan manual menunjukkan bahwa satu sisi pandang tidak cukup untuk mencakup semua buah, sehingga penggabungan identitas lintas sisi tetap diperlukan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `weng2026citrus`.

Weng dkk. (2026, *Transactions of the Chinese Society of Agricultural Engineering* 42(7): 182-192) mengusulkan metode pelacakan dan penghitungan jeruk dari video pesawat nirawak yang menggabungkan detektor ringan YOLO11-PMSL (kepala P2 sampai P4, modul penguat tepi C3k2-MSEIE, loss SIoU, pemangkasan LAMP) dengan ByteTrack berasosiasi DIoU dan penghitungan wilayah. Pada jeruk Navel Orange 52, mAP0,5 mencapai 90,5% (YOLO11n 81,2%) dengan 0,36 juta parameter dan 140,12 FPS, MOTA 92,8%, dan akurasi hitung rerata 88,4% terhadap hitungan manual pada lima video.

Catatan verifikasi data: teks berbahasa Mandarin, diekstraksi dengan baik; tabel (Tabel 1 sampai 5) terbaca satu sel per baris dan pemetaan kolom disimpulkan dari urutan serta keterangan tabel, yang konsisten dengan angka di abstrak dan kesimpulan. Rasio per video pada Tabel 5 dan selisih MOTA dihitung ulang dari tabel. Tidak dapat diverifikasi dari teks: jumlah pohon, jumlah bounding box, cara pembagian latih dan uji (per video atau per bingkai), jumlah video dan bingkai untuk metrik pelacakan, serta hasil penghitungan tanpa mekanisme wilayah. Kata "YOLO11-PMSL" pada beberapa bagian ditulis "YOLOv11-PCMS" atau "YOLO11n-PCMS" pada ablasi dan kesimpulan; penulisan ini dinilai sebagai ketidakkonsistenan penamaan.
