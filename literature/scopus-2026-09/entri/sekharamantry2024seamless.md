# A Seamless Deep Learning Approach for Apple Detection, Depth Estimation, and Tracking Using YOLO Models Enhanced by Multi-Head Attention Mechanism

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sekharamantry2024seamless` |
| Judul asli | A Seamless Deep Learning Approach for Apple Detection, Depth Estimation, and Tracking Using YOLO Models Enhanced by Multi-Head Attention Mechanism |
| Penulis | Sekharamantry, Praveen Kumar; Melgani, Farid; Malacarne, Jonni; Ricci, Riccardo; de Almeida Silva, Rodrigo; Marcato Junior, Jose |
| Tahun | 2024 |
| Venue | Computers |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [sekharamantry2024seamless.pdf](../pdf/sekharamantry2024seamless.pdf)
- DOI resmi: https://doi.org/10.3390/computers13030083

## Gambaran Umum
Makalah ini mengusulkan sistem deteksi, estimasi kedalaman, dan penghitungan apel dari video kebun yang direkam dengan drone. Detektor berupa YOLOv7 yang diberi mekanisme perhatian multi-kepala (*multi-head attention mechanism*, MAM), dan penghitungan dilakukan dengan pelacak multi-objek ByteTrack sehingga buah yang tampak pada bingkai-bingkai berurutan dihitung satu kali.

Data dikumpulkan di kebun apel Val di Non, Trento, Italia, pada satu hari di bulan September dengan drone DJI Mavic Mini 3 dan kamera stereo Stereolabs ZED 2i. Jumlah citra, jumlah bingkai, dan jumlah anotasi tidak dilaporkan; teks hanya menyebut rekaman sebesar 10 GB. Pada citra asli, YOLOv7 + MAM mencapai presisi 0,92, *recall* 0,96, dan skor F1 0,95. Pada tiga video dengan hitungan manual total 1.645 apel, ByteTrack di atas YOLOv7 + MAM menghitung 1.691 apel dengan MAPE 0,027, sedangkan DeepSORT menghitung 1.970 apel dengan MAPE 0,197.

Klaim estimasi kedalaman disampaikan di judul dan abstrak, tetapi teks tidak memuat hasil kuantitatif akurasi kedalaman; kedalaman hanya dinyatakan ditampilkan pada keluaran dan tersedia dari kamera stereo.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa pendeteksian dan pencacahan apel di kebun terganggu oleh perubahan cahaya, kemiripan buah kecil di kejauhan dengan latar, serta oklusi oleh daun, ranting, kawat penopang (*trellis*), dan buah yang bertumpuk. Metode ambang warna tradisional dilaporkan dari pustaka mencapai tingkat pengenalan 88,0% tetapi hanya 18,0% pada kondisi cahaya latar. Penulis juga merangkum pekerjaan terdahulu pada YOLOv5 dan YOLOv7-tiny untuk apel, dan menilai bahwa semua sistem itu terganggu kompleksitas latar, keburaman gerak, dan cahaya rendah.

Pada penghitungan dari video, penulis menyatakan bahwa detektor saja tidak cukup karena apel yang sama pada bingkai berurutan dapat terhitung berulang dan menambah deteksi positif palsu. Karena itu diperlukan mekanisme pelacakan yang memberi identitas unik pada setiap buah sampai penghitung bertambah.

## Ide Utama
Ide utamanya adalah memadukan tiga komponen: augmentasi data, YOLOv7 yang diperkuat MAM untuk deteksi sekaligus prediksi kedalaman, dan ByteTrack untuk penghitungan. MAM dimaksudkan menangkap ketergantungan jarak jauh dan konteks sehingga buah yang sebagian tertutup tetap dapat dikenali dari bagian yang terlihat.

Untuk penghitungan, ByteTrack mempertahankan kotak berkeyakinan rendah (yang sering berasal dari buah tertutup) pada tahap asosiasi kedua, sehingga lintasan tidak putus saat oklusi singkat. Hitungan buah diperoleh dari jumlah ID lintasan yang unik. Penulis menyatakan bahwa koordinat 3D (x, y, z) hasil gabungan kotak dan kedalaman dipakai sebagai titik awal pelacakan.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Data diambil di dua lahan di Val di Non, Trento, dengan kamera refleks, kamera stereo, dan drone, pada jarak 30 sampai 60 cm dari tanaman. Penerbangan dilakukan pada satu hari di bulan September dengan berbagai kondisi cuaca tanpa pencahayaan buatan. Drone DJI Mavic Mini 3 (249 g) dengan gimbal tiga sumbu dan kamera resolusi 2688 × 1520 digunakan, bersama kamera stereo Stereolabs ZED 2i yang menghasilkan peta kedalaman dalam satuan metrik melalui ZED SDK. Kultivar apel tidak dilaporkan.

### 2. Anotasi dan pembagian data
Setiap apel diberi kotak pembatas dan label kedalaman (jarak ke drone). Anotasi hanya mencakup apel yang siap panen; apel belum matang tidak dianotasi, sehingga model hanya mengenali apel matang. Pembagian data: sebagian besar untuk latih, dan 30% untuk uji serta 10% untuk validasi. Jumlah citra tidak dilaporkan.

### 3. Augmentasi
Lima augmentasi dipakai: perubahan kecerahan (konversi HSV ke RGB), pembalikan citra, rotasi, keburaman, dan derau Gaussian dengan varians 0,02.

### 4. Detektor YOLOv7 + MAM
YOLOv7 terdiri atas masukan, tulang punggung (blok CBS, ELAN, MP, dan SPPCSPC), leher, dan kepala deteksi, dengan reparameterisasi struktural. MAM ditambahkan dengan menjumlahkan pengodean posisi pada peta fitur, memproyeksikannya menjadi *query*, *key*, dan *value*, menghitung perhatian skala titik-hasil-kali dengan sambungan residual dan normalisasi lapisan, lalu jaringan umpan-maju. Kerugian terdiri atas kerugian klasifikasi (fokal) dan regresi (L1 halus). Pada inferensi, kotak yang lebih kecil dari ambang ukuran yang dipelajari dianggap apel belum matang dan tidak dihitung.

### 5. Estimasi kedalaman
Kamera stereo menghitung kedalaman dari disparitas piksel antara citra kiri dan kanan; mode standar dan mode ultra serta stabilisasi kedalaman temporal dari ZED SDK dijelaskan. Resolusi kedalaman mengikuti $D_r = Z^2 \alpha$. Teks tidak menjelaskan bagaimana MAM menghasilkan keluaran kedalaman, dan tidak ada metrik akurasi kedalaman.

### 6. Pelacakan dan penghitungan dengan ByteTrack
Kotak deteksi disaring dengan ambang atas dan bawah menjadi kotak berkeyakinan tinggi, rendah, dan latar. Kotak berkeyakinan tinggi dicocokkan dengan lintasan prediksi filter Kalman memakai IoU atau fitur ReID; sisa lintasan dicocokkan dengan kotak berkeyakinan rendah pada tahap kedua dengan IoU dan ambang lebih rendah. Lintasan yang hilang dipertahankan selama beberapa bingkai. Parameter: MIN_THRESHOLD 0,001 dan ambang latar 0,1.

```
 video drone --> YOLOv7 + MAM (kotak + kedalaman)
             --> ByteTrack (tahap 1: skor tinggi, tahap 2: skor rendah)
             --> jumlah ID unik = hitungan apel
```

## Eksperimen dan Hasil
Perangkat keras: Intel i7, RAM 24 GB, NVIDIA GeForce RTX 3090, Ubuntu 22.04, PyTorch. Ambang IoU evaluasi 0,75. Biaya komputasi dilaporkan 20 ms per bingkai (simpangan baku 2 ms) dan memori puncak sekitar 300 MB. Detektor dibandingkan dengan Faster RCNN, AlexNet + Faster RCNN, ResNet + Faster RCNN, YOLOv5, YOLOv7, dan YOLOv5 + MAM, pada citra asli dan pada variasi pencahayaan (faktor 0,5 untuk cahaya rendah dan 1,5 untuk cahaya tinggi).

Tabel 1. Deteksi apel (Tabel 1 makalah).

| Metode | P asli | R asli | F1 asli | P cahaya variasi | R cahaya variasi | F1 cahaya variasi |
|---|---|---|---|---|---|---|
| Faster RCNN | 0,84 | 0,78 | 0,80 | 0,68 | 0,72 | 0,71 |
| AlexNet + Faster RCNN | 0,88 | 0,83 | 0,86 | 0,69 | 0,75 | 0,71 |
| ResNet + Faster RCNN | 0,87 | 0,64 | 0,74 | 0,72 | 0,75 | 0,72 |
| YOLOv5 | 0,82 | 0,86 | 0,84 | 0,71 | 0,77 | 0,73 |
| YOLOv7 | 0,83 | 0,91 | 0,86 | 0,82 | 0,85 | 0,84 |
| YOLOv5 + MAM | 0,88 | 0,94 | 0,92 | 0,85 | 0,91 | 0,87 |
| YOLOv7 + MAM | 0,92 | 0,96 | 0,95 | 0,87 | 0,93 | 0,89 |

Tabel 2. Penghitungan apel pada tiga video terhadap hitungan manual (Tabel 2 makalah).

| Video | Hitungan manual | Metode | Hitungan sistem | MAPE |
|---|---|---|---|---|
| 1 | 945 | DeepSORT | 996 | 0,053 |
| 1 | 945 | YOLOv7 + MAM + ByteTrack | 964 | 0,026 |
| 2 | 550 | DeepSORT | 694 | 0,261 |
| 2 | 550 | YOLOv7 + MAM + ByteTrack | 563 | 0,023 |
| 3 | 150 | DeepSORT | 280 | 0,866 |
| 3 | 150 | YOLOv7 + MAM + ByteTrack | 164 | 0,093 |
| Semua | 1.645 | DeepSORT | 1.970 | 0,197 |
| Semua | 1.645 | YOLOv7 + MAM + ByteTrack | 1.691 | 0,027 |

Tabel 3 memperbandingkan kombinasi detektor dan pelacak pada mAP 0,5: YOLOv5 + MAM + DeepSORT 75,20% (32,5 juta parameter, CPU 320 ms, GPU 11,3 ms); YOLOv7 + MAM + DeepSORT 79,32% (24,6 juta, 220 ms, 9,1 ms); YOLOv5 + MAM + ByteTrack 83,55% (17,3 juta, 161 ms, 8,2 ms); YOLOv7 + MAM + ByteTrack 92,35% (11,5 juta, 71 ms, 6,4 ms). Penulis mengaitkan penghitungan berlebih DeepSORT dengan duplikasi apel dan apel latar belakang yang tidak ikut dihitung dalam acuan, sedangkan ByteTrack dinyatakan memisahkan apel latar depan dan latar belakang.

## Kelebihan dan Keterbatasan
Kelebihan yang tampak dari makalah: hitungan sistem dibandingkan dengan hitungan manual total, pelacak dibandingkan dengan DeepSORT pada detektor yang sama, dan ketahanan terhadap variasi cahaya diuji.

Keterbatasan yang dinyatakan penulis: warna, bentuk, dan ukuran berperan sebagai faktor pembatas kecil, sedangkan kecepatan drone serta laju deteksi dan pelacakan merupakan perhatian utama; sebaran penerapan GPU pada kebun yang beragam perlu dipertimbangkan; dan penulis berencana memadukan mekanisme perhatian lain dengan model ringan.

Menurut pembacaan ringkasan ini, terdapat keterbatasan tambahan. Evaluasi penghitungan hanya memakai tiga video dengan satu video berdurasi sangat pendek (teks menulis "0,41 s", yang kemungkinan salah ketik). Jumlah citra, bingkai, dan anotasi tidak dilaporkan sehingga ukuran data tidak dapat dinilai. Anotasi hanya apel matang, dan aturan ambang ukuran untuk membuang apel belum matang dapat menyingkirkan buah kecil yang sah. Akurasi kedalaman tidak dilaporkan walau menjadi bagian judul. Hitungan acuan tidak mendefinisikan bagaimana apel latar belakang diperlakukan oleh penghitung manual. Pada Tabel 2, MAPE video 1 untuk ByteTrack (0,026) tidak sesuai dengan selisih sederhana (964 − 945) / 945 ≈ 0,020 dari angka dalam tabel yang sama. Angka mAP di Tabel 3 tidak muncul pada Tabel 1, sehingga tidak jelas apakah keduanya diukur pada data yang sama.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali pada bingkai-bingkai berurutan dari satu video drone yang bergerak. Mekanismenya adalah pelacakan berbasis deteksi (ByteTrack dengan filter Kalman, asosiasi IoU atau ReID, dan dua tahap asosiasi). Tidak ada pencocokan antar-video, antar-sisi pohon yang terpisah, atau rekonstruksi 3D; koordinat 3D dari kamera stereo disebut sebagai masukan pelacakan, tetapi teks tidak merincinya.

Hitungan tidak dilaporkan per kelas; hanya apel matang yang dianotasi. Acuan hitungnya adalah hitungan manual dari video (1.645 apel pada tiga video), bukan panen. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah strategi asosiasi dua tahap yang mempertahankan kotak berkeyakinan rendah untuk objek tertutup, serta perbandingan hitungan sistem terhadap hitungan manual per video. Tidak ada mekanisme yang menjaga identitas antar sisi pohon atau antar-sesi perekaman.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `sekharamantry2024seamless`.

Sekharamantry dkk. (2024) mengusulkan sistem pendeteksian, estimasi kedalaman, dan penghitungan apel dari video drone yang memadukan YOLOv7 dengan mekanisme perhatian multi-kepala dan ByteTrack. Pada citra asli, detektor mencapai presisi 0,92, *recall* 0,96, dan F1 0,95. Pada tiga video dengan hitungan manual 1.645 apel, sistem menghitung 1.691 apel dengan MAPE 0,027, dibandingkan MAPE 0,197 untuk DeepSORT.

Catatan verifikasi data: Angka deteksi dibaca dari Tabel 1, angka penghitungan dari Tabel 2, dan angka kompleksitas dan mAP dari Tabel 3. Biaya komputasi dan perangkat keras berasal dari awal Seksi 3. Pembagian data (30% uji, 10% validasi) berasal dari Seksi 2.1. Teks ekstraksi terbaca baik, tetapi rumus kerugian pada Persamaan 2 terpotong dan tidak dapat dipakai. Jumlah citra, kultivar, jumlah drone penerbangan, dan hasil kuantitatif estimasi kedalaman tidak dilaporkan pada teks. Durasi video 3 tertulis "0,41 s" dan tidak dapat dipastikan. MAPE video 1 untuk ByteTrack (0,026) tidak sama dengan selisih relatif yang dihitung dari hitungan pada tabel (sekitar 0,020).
