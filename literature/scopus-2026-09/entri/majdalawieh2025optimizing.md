# Optimizing Fruit Harvesting Through a High-Performance Deep Learning Framework for Detection, Tracking, and Automated Counting.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `majdalawieh2025optimizing` |
| Judul asli | Optimizing Fruit Harvesting Through a High-Performance Deep Learning Framework for Detection, Tracking, and Automated Counting. |
| Penulis | Majdalawieh, Munir; Khan, Shafaq |
| Tahun | 2025 |
| Venue | Proceedings 2025 27th IEEE International Conference on High Performance Computing and Communications 11th IEEE International Conference on Data Science and Systems 23rd IEEE International Conference on Smart City 11th IEEE International Conference on Dependability in Sensor Cloud and Big Data Systems and Applications and 21st IEEE International Conference on Embedded Software and Systems Hpcc Dss Smartcity Dependsys Icess 2025 |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [majdalawieh2025optimizing.pdf](../pdf/majdalawieh2025optimizing.pdf)
- DOI resmi: https://doi.org/10.1109/hpcc67675.2025.00132

## Gambaran Umum
Makalah prosiding IEEE HPCC 2025 ini mengusulkan kerangka dua fase untuk otomasi pemanenan buah: deteksi buah dengan YOLO-V7 dan pencacahan dengan pelacakan DeepSORT yang dikombinasikan dengan metode garis daerah minat (*region of interest*, ROI). Sasarannya adalah kinerja waktu-nyata (lebih dari 24 *frame* per detik, FPS) pada sumber daya komputasi terbatas.

Data berupa citra apel (dari dataset DeepFruits ditambah 500 citra dari Google) dan mangga (dari dataset MangoYOLO). Setelah augmentasi, dataset gabungan berisi 2.000 citra yang dibagi sama banyak antara apel dan mangga, dengan pembagian latih/validasi/uji 70%/20%/10%.

Hasil utama: mAP@0,50 sebesar 97,5%, presisi 94,2%, *recall* 93,2%, dan mAP@0,95 sebesar 84,1%, dengan kecepatan evaluasi 30 FPS. YOLO-V7 dilaporkan mengungguli YOLO-V5 dan YOLO-V4 yang juga digabung dengan DeepSORT. Makalah tidak menyajikan tabel galat pencacahan; klaim galat hitungan hanya muncul dalam kalimat kesimpulan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa pemanenan dan estimasi hasil secara manual mahal, padat karya, dan rawan galat. Petani biasanya memperkirakan hasil kebun dengan mengambil sampel area terbatas lalu mengekstrapolasi. Metode deteksi yang ada masih terkendala beban komputasi, kecepatan inferensi rendah, serta galat akibat oklusi dan kondisi lingkungan yang berubah. Penulis juga menyatakan bahwa kebanyakan studi sebelumnya berfokus pada deteksi dan kurang memperhatikan pencacahan otomatis.

Tujuan yang dinyatakan: model ringan untuk sumber daya terbatas, kinerja waktu-nyata di atas 24 FPS, pencacahan otomatis dengan DeepSORT dan ROI, serta kinerja yang kokoh pada beragam kondisi kebun.

## Ide Utama
Gagasannya adalah menggabungkan detektor satu tahap YOLO-V7 dengan pelacak DeepSORT agar setiap buah memperoleh identitas yang bertahan antar-*frame* video, lalu menghitung buah ketika identitas itu melintasi garis ROI. Penulis juga menyebut tiga penyesuaian: pelacakan adaptif dinamis yang menyesuaikan parameter asosiasi DeepSORT, modul pencacahan garis ROI, dan augmentasi sadar-oklusi dengan masker sintetis daun dan cabang. Teks tidak menguraikan rincian algoritmik pelacakan adaptif dinamis maupun hasil ablasinya.

## Cara Kerja Langkah demi Langkah

```
 Video buah -> YOLO-V7 (deteksi) -> DeepSORT (ID tetap) -> garis ROI
 (50% tinggi video) -> hitungan bertambah saat ID melintas
```

### 1. Akuisisi dan penyusunan data
Dataset: 63 citra kebun apel dari DeepFruits ditambah 500 citra apel dari Google (total 563), dan 1.000 citra mangga yang dipilih acak dari 1.730 citra MangoYOLO. Augmentasi (rotasi -25° dan +25°, pembalikan horizontal dan vertikal, rotasi 90°) menaikkan apel dari 563 ke 1.000 citra dan mangga dari 800 ke 1.000 citra. Semua citra diubah ukurannya menjadi 416×416 piksel. Anotasi kotak pembatas memakai Roboflow dalam format YOLO. Teks menyebut angka mangga 1.000 sampel dan 800 citra sebelum augmentasi tanpa penjelasan selisihnya. Kultivar dan lokasi pengambilan citra tidak dilaporkan.

### 2. Pelatihan detektor YOLO-V7
Perangkat keras: GPU NVIDIA GTX 1080 Ti; perangkat lunak Python 3.8 dan TensorFlow 2.4. Pelatihan 400 epoch, ukuran *batch* 32, optimizer Adam, laju belajar 0,001, bobot awal pralatih, dan lebih dari 100 konfigurasi *hyperparameter* diuji. YOLO-V7 memakai tulang punggung E-ELAN, leher FPN dan PAN, serta modul RepConv dan kepala bantu. Penulis menyatakan tidak menambahkan modifikasi khusus objek kecil.

### 3. Pelacakan dan pencacahan
DeepSORT menggabungkan prediksi gerak (filter Kalman), asosiasi dengan algoritma Hungaria, dan deskriptor tampilan CNN dengan jarak kosinus. Garis ROI diletakkan pada 50% tinggi video; hitungan bertambah setiap kali ID terlacak melintasinya. Penulis menyatakan metode ini sesuai untuk kamera bergerak.

### 4. Metrik
Presisi, *recall*, F1, dan mAP.

## Eksperimen dan Hasil
Pembanding adalah YOLO-V5 dan YOLO-V4 yang juga digabung dengan DeepSORT, semuanya pralatih pada COCO dan dievaluasi dalam kondisi yang sama.

Tabel I (model usulan, per kelas; O dan M adalah dua kelas buah, kemungkinan apel (*orange* tidak disebut; penulis tidak mendefinisikan singkatan itu)):

| Kelas | Citra | Presisi | Recall | mAP@0,5 | mAP@0,95 |
|---|---|---|---|---|---|
| Semua | 2.000 | 94,2% | 93,2% | 97,5% | 84,1% |
| O | 1.000 | 92,3% | 91,3% | 96,4% | 81,2% |
| M | 1.000 | 95,2% | 95,2% | 98,7% | 70,2% |

Tabel III (perbandingan model):

| Model | Presisi | Recall | mAP@0,5 | mAP@0,95 | Kecepatan |
|---|---|---|---|---|---|
| YOLO-V7 | 94,2% | 93,2% | 97,5% | 84,1% | 18 ms |
| YOLO-V5 | 92,3% | 92,5% | 96,7% | 80,5% | 20 ms |
| YOLO-V4 | 90,4% | 90,9% | 94,3% | 75,4% | 23 ms |

Tabel II melaporkan *recall* pada 10.000 buah: YOLO-V7 + DeepSORT 93,5%, YOLO-V5 + DeepSORT 88,4%, YOLO-V4 + DeepSORT 86,9%. Selisih yang dinyatakan penulis untuk YOLO-V7: presisi lebih tinggi 1,9% dan 3,8%, *recall* 0,7% dan 2,3%, mAP@0,5 0,8% dan 3,2%, serta mAP@0,95 3,6% dan 8,7% terhadap YOLO-V5 dan YOLO-V4. Selisih ini sesuai dengan pengurangan angka pada Tabel III.

Pada kesimpulan, penulis menyatakan pipeline diuji pada kumpulan video uji dari beberapa kebun dengan presisi deteksi di atas 94% dan galat pencacahan di bawah 5%. Angka galat pencacahan itu tidak disertai tabel, jumlah video, atau acuan hitung.

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: kecepatan waktu-nyata sekitar 30 FPS, akurasi deteksi tinggi pada apel dan mangga, serta integrasi pelacakan untuk pencacahan otomatis.

Keterbatasan yang dinyatakan penulis: kinerja bergantung pada mutu dan keragaman data latih; kebutuhan komputasi tinggi dan kamera khusus; risiko *overfitting*; belum ada uji lapangan jangka panjang.

Menurut pembacaan ringkasan ini: (1) dataset kecil (2.000 citra hasil augmentasi) dan campuran citra daring dengan dataset publik, sehingga pembagian uji kemungkinan memuat citra turunan augmentasi dari citra yang sama dengan data latih, yang tidak dijelaskan teks; (2) kinerja pelacakan dan pencacahan tidak dilaporkan dengan metrik yang dapat diperiksa (tanpa MOTA, IDF1, jumlah pergantian identitas, atau galat hitungan terhadap acuan); (3) kecepatan 30 FPS pada teks (kecepatan evaluasi) dan 18 ms per citra pada Tabel III tidak dijelaskan hubungannya; (4) klaim integrasi IoT, penerapan edge, dan pelacakan adaptif dinamis tidak didukung hasil di teks; (5) garis ROI pada 50% tinggi video mengandaikan gerak kamera searah.

## Kaitan dengan Tinjauan main6
Makalah menangani buah yang terlihat pada banyak *frame* video dengan mekanisme pelacakan multi-objek (DeepSORT dengan filter Kalman, deskriptor tampilan, dan garis ROI) sehingga satu buah dihitung sekali ketika melintasi garis. Mekanisme ini bersifat dalam-satu-aliran-video, bukan pencocokan antarsisi atau antarpandang terpisah. Hitungan tidak dilaporkan per kelas; dua kelas (apel dan mangga) hanya dilaporkan pada metrik deteksi. Acuan hitungan (panen, hitung manual, atau anotasi) tidak dijelaskan; tidak ada hasil pencacahan kuantitatif.

Yang dapat dipindahkan: gagasan identitas persisten dan penghitungan saat melintasi garis untuk video yang mengelilingi pohon. Keterbatasannya, tanpa penghubung identitas lintas sisi pohon dan tanpa evaluasi pencacahan, makalah ini hanya memberi contoh pipeline deteksi-pelacakan-hitung yang sederhana.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `majdalawieh2025optimizing`.

Majdalawieh dan Khan mengusulkan pipeline deteksi dan pencacahan buah berbasis YOLO-V7 dengan DeepSORT dan garis ROI, dilatih pada 2.000 citra apel dan mangga (416×416 piksel). Model melaporkan mAP@0,50 sebesar 97,5%, presisi 94,2%, *recall* 93,2%, serta kecepatan 30 FPS, dan mengungguli YOLO-V5 dan YOLO-V4 pada dataset yang sama. Evaluasi pencacahan tidak disajikan dalam bentuk tabel.

Catatan verifikasi data: Angka deteksi utama ada pada Tabel I dan III (Seksi VII), *recall* pada Tabel II, dan rincian dataset pada Seksi IV.B-C. Angka 30 FPS ada di abstrak dan Seksi VII.A. Klaim galat pencacahan di bawah 5% hanya ada di Seksi IX tanpa tabel pendukung dan tidak dapat diverifikasi. Teks ekstraksi terbaca baik; Gambar 8-11 tidak terbaca sebagai angka. Makna label kelas "O" dan "M" pada Tabel I tidak didefinisikan di teks.
