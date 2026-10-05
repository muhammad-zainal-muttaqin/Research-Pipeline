# Robust real-time blueberry counting in greenhouses using small-object detection and mamba-driven multi-step trajectory completion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2025robust` |
| Judul asli | Robust real-time blueberry counting in greenhouses using small-object detection and mamba-driven multi-step trajectory completion |
| Penulis | Zhang, Naiqi; Cao, Jianhua |
| Tahun | 2025 |
| Venue | Smart Agricultural Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | blueberry |

## Tautan Akses
- PDF: [zhang2025robust.pdf](../pdf/zhang2025robust.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2025.101402

## Gambaran Umum

Makalah ini mengusulkan kerangka pencacahan buah *blueberry* matang pada video rumah kaca secara waktu-nyata. Kerangka itu terdiri atas tiga bagian: detektor objek kecil berbasis YOLOv12n yang diberi fungsi kerugian hibrida (*hybrid loss*) dan modul fusi fitur multi-skala MCSPF, modul prediksi lintasan (*trajectory prediction*) dengan pengkode berbasis *Kolmogorov-Arnold Network* (KAN) dan pengurai berbasis Mamba, serta strategi pencocokan dua tahap berbasis ByteTrack yang memakai posisi hasil prediksi untuk menyambung lintasan yang terputus. Tujuannya adalah mengurangi penghitungan ganda akibat deteksi yang terlewat pada buah yang kecil, rapat, dan sering tertutup.

Data utama berasal dari rumah kaca di Provinsi Yunnan, Tiongkok, yang direkam oleh robot patroli antarbaris. Detektor juga diuji pada dataset publik PEST24 (serangga kecil), dan modul prediksi lintasan diuji pada MOT17 (pejalan kaki) untuk menilai generalisasi.

Hasil utama: pada PEST24, presisi naik 8,3% dan mAP@50 naik 2,9% terhadap *baseline*; pada dataset *blueberry* nyata, mAP@50 detektor mencapai 0,877. Prediksi lintasan menghasilkan ADE 15,4 piksel dan FDE 24,8 piksel pada 6 bingkai. Akurasi pencacahan keseluruhan 92,5% dengan kecepatan 35 FPS pada perangkat tepi (Jetson AGX Orin 32 GB).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pencacahan buah pada video umumnya dilakukan dengan menjumlahkan deteksi per bingkai, yang menimbulkan penghitungan ganda. Pelacakan multi-objek (*multi-object tracking*, MOT) diperkenalkan agar setiap buah mendapat identitas tunggal lintas bingkai, tetapi penulis menyatakan bahwa pergeseran lintasan (*trajectory drift*) dan pertukaran identitas (*identity switch*) tetap terjadi, terutama karena getaran kamera dan permukaan tanah yang tidak rata menghasilkan lintasan nonlinear.

*Blueberry* berukuran kecil (objek terkecil pada dataset penulis sekitar 16 piksel), tersebar rapat, dan sering tertutup, sehingga deteksi terlewat dan identitas terputus. Metode prediksi lintasan yang ada dinilai punya kekurangan: MLP lemah pada interaksi nonlinear, LSTM terbatas pada ketergantungan jangka panjang, Transformer memerlukan komputasi besar sehingga kurang cocok untuk perangkat tepi, dan model sosial seperti Social LSTM mengabaikan dinamika temporal objek tetangga.

## Ide Utama

Gagasan intinya adalah memakai prediksi gerak berbasis interaksi antarbuah untuk mengisi posisi buah yang tidak terdeteksi, sehingga identitas buah tidak berganti ketika buah muncul kembali. Lintasan buah utama dikodekan bersama konteks lintasan buah tetangga, lalu posisi masa depan diprediksi secara autoregresif. Posisi prediksi itu dipakai sebagai cadangan pada pencocokan tahap kedua dalam pelacak.

Dengan cara ini, buah yang hilang sesaat tetap mempertahankan nomor identitas lamanya, dan hitungan akhir (jumlah identitas unik) tidak membengkak. Mekanisme identitas yang dipakai adalah pelacakan dalam satu urutan video, bukan pencocokan antarpandang yang terpisah.

## Cara Kerja Langkah demi Langkah

```
 Video -> YOLOv12n+HL+MCSPF -> kotak deteksi -> ByteTrack tahap 1
                                                     |
       lintasan historis -> OTAM -> GamaKAN -> KG -> Mamba -> posisi prediksi
                                                     |
                               ByteTrack tahap 2 (prediksi vs deteksi sisa)
```

### 1. Akuisisi data

Dataset *blueberry* direkam oleh robot patroli antarbaris pada rumah kaca di Yunnan, Tiongkok. Segmen video 30 detik disisihkan untuk evaluasi akhir, sedangkan rekaman lain dicuplik 3 bingkai per detik sehingga diperoleh 2.182 citra. Setiap citra dianotasi kotak pembatas buah matang dengan LabelImg dan dibagi latih, validasi, uji dengan rasio 8:1:1; rata-rata 27 buah matang terlihat per bingkai. Untuk lintasan, set latih berisi video 2 menit dengan 4.132 lintasan beranotasi dan set validasi berisi video 33 detik dengan 1.743 lintasan, beresolusi 544 × 960 dan dianotasi dengan Darklabel. Kultivar tidak dilaporkan. Dataset publik PEST24 berisi 17.001 citra latih dan 7.700 citra validasi. MOT17 menghasilkan 325.791 lintasan valid, dengan paruh pertama video untuk latih dan paruh kedua untuk validasi.

### 2. Detektor objek kecil

*Baseline*-nya YOLOv12. Fungsi kerugian IoU pada regresi kotak diganti dengan kerugian hibrida bertahap: pada tahap awal dipakai *Small-Object Focal Wasserstein Loss* (jarak Wasserstein dengan galat pusat dinormalisasi lebar dan tinggi sasaran, mekanisme fokal, dan penghalusan logaritmik galat lebar dan tinggi), lalu bobot *Hierarchical Boundary Attention Loss* (HBALoss, galat ternormalisasi empat sisi kotak dengan faktor perhatian per sisi) dinaikkan bertahap. Modul A2C2f pada kepala diganti modul MCSPF (*Multi-branch Cross-stage Pyramid Fusion*), yang membagi fitur menjadi dua cabang, satu cabang langsung dan satu cabang berisi blok residual terbalik dan *Spatial Pyramid Pooling*, lalu keduanya digabung.

### 3. Prediksi lintasan

Modul masukan berupa lintasan historis dari detektor. OTAM (*Other Trajectory Aggregation Module*) menerapkan *attention pooling* pada posisi objek tetangga untuk menghasilkan konteks spasial. Pengkode GamaKAN memakai konvolusi terpisah-kedalaman (*depth-wise separable*), blok nonlinear berbasis KAN dengan fungsi dasar *spline*, dan gerbang kanal. OTEM mengodekan dinamika lintasan tetangga. Modul fusi bergerbang KG menyelaraskan aliran utama dan tetangga. Pengurai Mamba berlapis (*Selective State Space Model*) memprediksi posisi pada beberapa langkah ke depan secara autoregresif dengan pengodean posisi sinus-kosinus tetap. Supervisi memakai kerugian berbasis jarak Wasserstein untuk kotak, ditambah kerugian ADE, FDE, dan kecepatan (VEL) yang dibobot.

### 4. Pelacakan dan penyambungan lintasan dua tahap

Pada tahap pertama, deteksi dicocokkan dengan semua lintasan aktif dengan matriks biaya berupa jarak piksel antarpusat. Untuk lintasan yang tidak cocok dan riwayatnya memenuhi panjang minimum modul prediksi, kotak hasil ekstrapolasi diaktifkan dan diikutkan pada tahap kedua, yaitu dicocokkan dengan deteksi sisa. Bila cocok, lintasan diperbarui dengan posisi prediksi. Lintasan yang gagal cocok selama beberapa bingkai berturut-turut (jumlah tidak dirinci pada teks) dianggap berakhir. Jumlah buah adalah jumlah identitas unik.

## Eksperimen dan Hasil

Perangkat uji: Ubuntu 22.04, GPU NVIDIA GeForce RTX 4090D, PyTorch 2.4.0, CUDA 11.8, TensorRT 8.6.1. Metrik deteksi: *Precision*, *Recall*, F1, mAP@50, GFLOPs, dan FPS. Metrik lintasan: ADE, FDE, dan FPS. Akurasi pencacahan didefinisikan sebagai $1 - |GT - \text{prediksi}| / GT$.

Perbandingan detektor pada dataset *blueberry* (Tabel 2):

| Algoritma | Precision | Recall | F1 | mAP@50 | GFLOPs |
|---|---|---|---|---|---|
| YOLOv5 | 0,782 | 0,763 | 0,772 | 0,812 | 15,4 |
| YOLOv8 | 0,747 | 0,751 | 0,749 | 0,795 | 9,1 |
| YOLOv10 | 0,778 | 0,774 | 0,776 | 0,814 | 8,4 |
| YOLO11 | 0,790 | 0,780 | 0,785 | 0,828 | 7,0 |
| YOLOv12 | 0,804 | 0,795 | 0,799 | 0,841 | 6,0 |
| Metode penulis | 0,822 | 0,811 | 0,816 | 0,877 | 5,8 |

Ablasi pada PEST24 (Tabel 1): *baseline* tanpa komponen memperoleh presisi 0,584, *recall* 0,539, mAP@50 0,534 pada 6,0 GFLOPs. Konfigurasi lengkap (kedua kerugian, penjadwalan bobot, dan MCSPF) memperoleh presisi 0,667, *recall* 0,543, mAP@50 0,563 pada 5,8 GFLOPs.

Prediksi lintasan (Tabel 3 dan 4): konfigurasi lengkap (GamaKAN + APR + OT + KG) memperoleh ADE 15,4 piksel, FDE 24,8 piksel, dan 91 FPS. Pada Tabel 4, metode penulis memperoleh jarak bingkai pertama 3,68 piksel, FDE@6 24,8 piksel, dan 91 FPS, dibandingkan GTR (5,10; 41,3; 45 FPS), MOTR (4,71; 34,9; 26 FPS), Social LSTM (8,33; 52,4; 75 FPS), dan filter Kalman (13,7 untuk jarak bingkai pertama; 250 FPS). Pada MOT17 (Tabel 7), prediksi 6 bingkai menghasilkan FDE@1 9,0 piksel, Mean ADE 26,9 piksel, dan Mean FDE 45,8 piksel.

Pemulihan lintasan pada uji oklusi simulasi (Tabel 5): tingkat pemulihan 90,2% untuk oklusi 1 bingkai, 85,4% untuk 2 bingkai, dan 74,8% untuk 3 bingkai.

Pencacahan pada set validasi 1.743 lintasan (Tabel 6):

| Pelacak | Hitungan | Akurasi | *Undercounting* | *Overcounting* | RA-rec | RA-pre |
|---|---|---|---|---|---|---|
| SORT | 2.031 | 83,5% | 9,1% | 25,6% | tidak ada | tidak ada |
| OC-SORT | 1.293 | 74,2% | 35,7% | 11,6% | 75,1% | 52,0% |
| ByteTrack | 1.902 | 90,9% | 7,9% | 17,0% | 68,7% | 81,7% |
| Metode penulis | 1.874 | 92,5% | 3,7% | 11,2% | 73,0% | 87,2% |

Pada perangkat Jetson AGX Orin 32 GB, detektor dipercepat dengan TensorRT dan model prediksi dikuantisasi 8 bit; sistem mencapai hingga 35 FPS dengan sekitar 1,4 GB memori sistem dan 1.518 MB memori GPU.

## Kelebihan dan Keterbatasan

Kelebihan: komponen detektor dan prediksi diuji dengan ablasi yang rinci, hasil dibandingkan dengan beberapa pelacak (SORT, OC-SORT, ByteTrack) pada metrik hitungan, *undercounting*, *overcounting*, dan asosiasi ulang, serta kecepatan 35 FPS pada perangkat tepi dilaporkan.

Keterbatasan yang dinyatakan penulis: dataset publik yang mencakup *blueberry* besar dan kecil sekaligus belum tersedia; kerangka belum divalidasi pada skenario seperti pencacahan berbasis UAV; sistem hanya bergantung pada citra RGB sehingga rentan terhadap pencahayaan kuat, pantulan spekuler, dan oklusi, yang menyulitkan pembedaan buah mentah dan buah matang yang berubah warna; akurasi pemertahanan identitas jangka panjang menurun pada adegan padat dengan oklusi panjang. Penulis berencana menambah modalitas inframerah dekat dan memadukan ciri visual statis dengan informasi lintasan.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan tambahan. Acuan hitungan (*ground truth*) pencacahan tidak dinyatakan secara eksplisit; dengan 1.743 lintasan beranotasi pada set validasi, akurasi 92,5% untuk hitungan 1.874 konsisten dengan acuan 1.743 (selisih sederhana dihitung dalam ringkasan ini, bukan dinyatakan penulis). Data tersedia hanya atas permintaan. Penambahan dua jalur lintasan yang terpisah (bingkai pertama dan bingkai lanjutan) membuat nilai 3,68 piksel dipakai sebagai ADE bingkai tunggal pada abstrak tetapi diberi label jarak bingkai pertama pada Tabel 4. Pada Tabel 6, set uji pencacahan berupa video 33 detik dari satu rumah kaca, sehingga generalisasi ke kebun lain belum teruji. Hitungan hanya melalui satu urutan video, tanpa penyatuan pandangan yang terpisah.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari satu kali dalam bingkai-bingkai berurutan satu video. Mekanismenya adalah pelacakan multi-objek berbasis ByteTrack yang dilengkapi prediksi lintasan (Mamba) untuk menyambung identitas saat deteksi terlewat; hitungan akhir adalah jumlah identitas unik. Hitungan tidak dilaporkan per kelas, karena hanya buah *blueberry* matang yang menjadi sasaran (buah hijau atau merah muda dianggap mentah dan tidak dihitung). Acuan hitungan berupa anotasi lintasan pada video (Darklabel) untuk set validasi, bukan hasil panen atau hitung manual di lapangan.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi terbatas pada gagasan umum: memakai prediksi posisi untuk mempertahankan identitas saat deteksi gagal sesaat, dan pencocokan dua tahap. Makalah tidak membahas pencocokan lintas sisi pohon yang terpisah dan tidak membahas atribut kelas, sehingga tidak menyediakan mekanisme identitas lintas pandang tanpa kontinuitas gerak.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `zhang2025robust`.

Zhang dan Cao mengusulkan kerangka pencacahan *blueberry* matang di rumah kaca yang menggabungkan detektor YOLOv12n yang dimodifikasi (kerugian hibrida dan modul MCSPF), prediksi lintasan berbasis KAN dan Mamba, serta pencocokan dua tahap berbasis ByteTrack. Pada dataset rumah kaca di Yunnan, detektor mencapai mAP@50 0,877, dan pencacahan mencapai akurasi 92,5% (hitungan 1.874) pada set validasi dengan 1.743 lintasan beranotasi, dengan kecepatan hingga 35 FPS pada Jetson AGX Orin.

Catatan verifikasi data: angka detektor berasal dari Tabel 2 (mAP@50 0,877) dan Tabel 1 (ablasi PEST24); peningkatan presisi 8,3% dan mAP@50 2,9% pada PEST24 berasal dari abstrak dan seksi Discussion, dan nilai itu dalam satuan yang tidak dirinci pada teks (persen atau poin persentase). ADE 15,4 piksel dan FDE 24,8 piksel dari Tabel 3 dan 4; hitungan dan akurasi pencacahan dari Tabel 6; pemulihan lintasan dari Tabel 5; hasil MOT17 dari Tabel 7. Tabel pada teks ekstraksi tersusun satu sel per baris; pemetaan baris Tabel 1 ke kombinasi komponen dibaca dari urutan tanda centang dan sebagian sel (misalnya baris ketiga yang memuat "0 0.593") tidak sepenuhnya jelas. Nilai RA-rec dan RA-pre untuk SORT kosong pada Tabel 6. Kultivar, lokasi pasti rumah kaca selain provinsi, dan batas jumlah bingkai penghentian lintasan tidak dilaporkan. Teks ekstraksi tidak memuat angka halaman gambar; isi gambar tidak dapat diverifikasi dari teks.
