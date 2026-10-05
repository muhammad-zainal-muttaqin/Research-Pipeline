# Research on Apple Detection and Tracking Count in Complex Scenes Based on the Improved YOLOv7-Tiny-PDE

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cao2025research` |
| Judul asli | Research on Apple Detection and Tracking Count in Complex Scenes Based on the Improved YOLOv7-Tiny-PDE |
| Penulis | Cao, Dongxuan; Luo, Wei; Tang, Ruiyin; Liu, Yuyan; Zhao, Jiasen; Li, Xuqing; Yuan, Lihua |
| Tahun | 2025 |
| Venue | Agriculture Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [cao2025research.pdf](../pdf/cao2025research.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture15050483

## Gambaran Umum
Makalah ini mengusulkan YOLOv7-Tiny-PDE, varian ringan dari YOLOv7-Tiny untuk mendeteksi buah apel pada citra kebun yang rumit (daun menutupi buah, buah saling tumpang tindih, pencahayaan bervariasi), lalu menggabungkannya dengan pelacak DeepSort untuk menghitung apel pada video. Huruf "PDE" merujuk pada tiga perubahan: konvolusi parsial (*partial convolution*, PConv) sebagai pengganti modul ELAN pada *backbone*, kepala deteksi dinamis (*dynamic head*, DyHead) pada *neck*, dan fungsi *loss* kotak EIoU sebagai pengganti CIoU. Data diambil dengan pesawat nirawak (*drone*) berkamera Intel RealSense D435i di kebun apel Shengfengyuan, Laiwu, Provinsi Shandong, China.

Dataset terdiri dari 594 citra apel beresolusi 1600 × 1600 dan satu segmen video 10 menit beresolusi 1920 × 1440. Setelah augmentasi pada 200 citra bertutupan, terbentuk 1.200 sampel yang dibagi 840 latih, 120 validasi, dan 240 uji. Pada Tabel 1, model usulan mencapai mAP@0,5 sebesar 97,90%, presisi 97,20%, *recall* 96,60%, dan F1 0,969 dengan 4.676.516 parameter dan 10,7 GFLOPs. Dibandingkan dengan YOLOv7-Tiny dasar, parameter turun 22,2% dan GFLOPs turun 18,3%.

Pada penghitungan video, gabungan YOLOv7-Tiny-PDE dan DeepSort mencapai MOTA 91,3% (DeepSort dasar 89,3%), IDF1 0,91 (dasar 0,82), dan jumlah pergantian identitas (*identity switch*, IDSW) 5,7 (dasar 12,3) pada Tabel 8. Namun, galat hitung relatif terhadap hitungan manual pada Tabel 7 justru lebih besar untuk model yang diperbaiki (rerata 0,127) daripada model sebelum perbaikan (rerata 0,089). Hal ini dibahas pada bagian keterbatasan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa estimasi hasil panen apel dan pengelolaan kebun cerdas memerlukan deteksi dan penghitungan buah yang andal. Di kebun tidak terstruktur, buah sering tertutup ranting dan daun serta saling menumpuk, sehingga akurasi deteksi dan penghitungan turun. Metode tradisional berbasis warna, bentuk, dan tekstur dinilai kurang akurat dan kurang general pada variasi cahaya dan oklusi. Detektor dua tahap seperti Faster R-CNN dinilai baik pada kondisi tanpa penghalang, tetapi lemah pada buah padat dan tertutup serta mahal secara komputasi.

Penulis merinci empat masalah pada detektor dan pelacak yang ada: (1) redundansi parameter dan beban komputasi pada skenario oklusi; (2) ekstraksi fitur lintas skala yang kurang baik, sehingga buah kecil, tumpang tindih, atau tertutup terlewat atau salah dikenali; (3) konvergensi model yang lambat; dan (4) ketidakcocokan prediksi pelacakan antarbingkai video akibat buah tertutup daun atau perubahan permukaan. Model juga harus cukup ringan untuk perangkat tepi (*edge device*) pada pesawat nirawak.

## Ide Utama
Gagasan makalah ini adalah menyederhanakan detektor satu tahap YOLOv7-Tiny melalui tiga modifikasi terarah, lalu memasangkannya dengan pelacak berbasis penampilan sehingga satu apel yang tampak pada banyak bingkai video dihitung sekali. Konvolusi parsial mengurangi komputasi dan akses memori, DyHead menambahkan perhatian (*attention*) pada tingkat skala, lokasi spasial, dan tugas untuk menekan latar belakang dan menangkap buah bertutupan, dan EIoU memisahkan selisih lebar dan tinggi kotak agar konvergensi lebih cepat.

Untuk penghitungan, identitas buah antarbingkai dijaga oleh DeepSort, yaitu SORT (filter Kalman dan algoritma Hungarian) ditambah jaringan identifikasi ulang (*re-identification*, ReID) yang mengekstraksi fitur penampilan serta strategi pencocokan bertingkat (*matching cascade*). Jumlah apel pada video ditentukan dari jumlah lintasan (*track*) unik. Makalah tidak memakai informasi kedalaman dari RealSense untuk pelacakan; kamera tersebut hanya disebut sebagai penyedia data penginderaan dan kedalaman pada akuisisi.

## Cara Kerja Langkah demi Langkah

```
  Video/citra --> YOLOv7-Tiny-PDE --> kotak apel --> DeepSort
                  (PConv, DyHead,                    (filter Kalman,
                   loss EIoU)                         ReID, cascade,
                                                      Hungarian)
                                                         |
                                                         v
                                              lintasan unik = jumlah apel
```

### 1. Akuisisi Data
Citra diambil pada 2 November 2024 pukul 10.00 di kebun petik apel Shengfengyuan (Laiwu High-Tech Zone, Kota Jinan, Provinsi Shandong; koordinat 36°14′22″ LU, 117°48′30″ BT). Pesawat nirawak dilengkapi kamera stereo Intel RealSense D435i. Jarak kamera ke buah dijaga 0,5 sampai 2,0 m, dengan variasi sudut (atas dan bawah), pencahayaan (cahaya belakang dan depan), dan oklusi (daun dan ranting, serta buah). Hasilnya adalah 594 citra JPG beresolusi 1600 × 1600 dan satu video 10 menit beresolusi 1920 × 1440. Kultivar apel tidak disebutkan; jumlah pohon tidak dilaporkan.

### 2. Pembentukan Dataset
Sebanyak 200 citra bertutupan dipilih lalu diaugmentasi dengan PyTorch dan OpenCV (penyesuaian kecerahan, derau Gaussian, pengaburan, transformasi geometri, penggabungan citra, dan *mosaic*). Gabungan dengan citra asli menghasilkan 1.200 sampel yang dibagi 7:1:2 menjadi 840 latih, 120 validasi, dan 240 uji. Dari set uji dipilih 100 citra berbuah jarang sebagai set A (oklusi ringan) dan 100 citra berbuah padat sebagai set B (oklusi padat). Untuk uji pencahayaan, 100 citra menghadap cahaya dan 100 citra membelakangi cahaya membentuk set C dan D. Anotasi memakai LabelImg dengan kotak pembatas untuk satu kelas "Apple_object"; apel yang lebih dari 80% permukaannya tertutup pada prinsipnya tidak dianotasi. Label disimpan dalam format YOLO.

### 3. Konvolusi Parsial (PConv)
PConv, yang berasal dari Fasternet, melakukan ekstraksi fitur spasial hanya pada sebagian kanal masukan sambil membiarkan kanal lain tidak berubah. Penulis menyatakan bahwa dengan rasio parsial seperempat, jumlah FLOPs PConv hanya seperenam belas dari konvolusi standar dan akses memorinya turun menjadi seperempat. Modul ini menggantikan konvolusi pada *backbone* YOLOv7-Tiny.

### 4. DyHead
DyHead (Dai dkk.) menyusun tiga perhatian: perhatian sadar-skala ($\pi_L$), sadar-spasial ($\pi_S$, memakai konvolusi deformabel), dan sadar-tugas ($\pi_C$, mengatur aktif atau nonaktif kanal fitur). Kepala deteksi asli diganti dengan DyHead pada *neck*.

### 5. Loss EIoU
CIoU mempertimbangkan luas tumpang tindih, jarak titik pusat, dan konsistensi rasio aspek. EIoU menguraikan faktor rasio aspek menjadi selisih lebar dan selisih tinggi yang dihitung terpisah terhadap kotak penutup minimum, sehingga bentuk kotak dioptimalkan lebih tepat dan konvergensi lebih cepat menurut penulis.

### 6. Pelacakan dan Penghitungan dengan DeepSort
SORT memakai IoU dan algoritma Hungarian, dengan filter Kalman untuk prediksi dan pembaruan gerak. DeepSort menambahkan jaringan ReID untuk fitur penampilan, jarak Mahalanobis dan jarak kosinus sebagai matriks biaya, dan pencocokan bertingkat. Target yang tidak cocok diberi identitas baru; lintasan yang tidak dikonfirmasi dan melampaui `max_age` dihapus. Penghitungan dilakukan pada lima segmen video apel, dengan MOTA, IDF1, IDSW, dan galat absolut rata-rata (*mean absolute error*, MAE) sebagai metrik.

### 7. Pengaturan Pelatihan
Pelatihan dan pengujian memakai laptop dengan AMD Ryzen 7 8745H, RAM 16 GB, dan GPU NVIDIA GeForce RTX 4060 Laptop 8 GB; PyTorch dengan CUDA 12.0 dan Python 3.8.2. Semua model pembanding dilatih pada dataset yang sama dengan hiperparameter yang seragam. Nilai hiperparameter spesifik (jumlah *epoch*, ukuran *batch*, laju belajar) tidak dilaporkan pada teks yang tersedia.

## Eksperimen dan Hasil
Sebelas model dibandingkan pada set uji yang disebut berjumlah 420 citra (Tabel 1): MobileNetv2, ShuffleNetv2, YOLOv8n, YOLOv8s, YOLOv9s, YOLOv10s, YOLO11n, YOLOv7, YOLOv7x, YOLOv7-Tiny, dan YOLOv7-Tiny-PDE.

| Model | Parameter | GFLOPs | P (%) | R (%) | mAP@0,5 (%) | mAP@0,95 (%) | F1 |
|---|---|---|---|---|---|---|---|
| YOLOv8n | 3.005.843 | 8,1 | 96,50 | 93,50 | 97,60 | 87,30 | 0,949 |
| YOLOv9s | 7.167.475 | 26,7 | 96,30 | 96,10 | 97,80 | 88,20 | 0,961 |
| YOLOv10s | 8.035.734 | 24,4 | 96,80 | 95,10 | 97,70 | 89,10 | 0,959 |
| YOLO11n | 2.582.347 | 6,6 | 96,70 | 93,70 | 97,80 | 86,00 | 0,951 |
| YOLOv7 | 36.481.772 | 103,2 | 95,70 | 94,80 | 94,50 | 84,00 | 0,952 |
| YOLOv7x | 70.782.444 | 188,0 | 97,40 | 94,10 | 94,20 | 83,90 | 0,957 |
| YOLOv7-Tiny | 6.007.596 | 13,1 | 96,70 | 94,10 | 94,10 | 81,20 | 0,954 |
| YOLOv7-Tiny-PDE | 4.676.516 | 10,7 | 97,20 | 96,60 | 97,90 | 82,90 | 0,969 |

Kolom "mAP@0.95" ditulis demikian pada makalah; teks tidak menjelaskan apakah yang dimaksud mAP@0,5:0,95. YOLOv7-Tiny-PDE memiliki mAP@0,5 tertinggi dan *recall* serta F1 tertinggi, tetapi mAP pada kolom kedua lebih rendah daripada YOLOv8n, YOLOv9s, YOLOv10s, dan YOLO11n. Penulis menulis bahwa YOLOv9s dan YOLOv10s sedikit lebih unggul pada kedua metrik mAP, tetapi GFLOPs keduanya jauh lebih tinggi. Model MobileNetv2 dan ShuffleNetv2 (baris tidak dikutip di tabel di atas) memiliki 4.757.846 dan 5.518.362 parameter dengan 10,2 dan 10,6 GFLOPs.

**Penghitungan pada citra (Tabel 2).** Sepuluh citra acak dihitung manual dengan total 171 apel. YOLOv7-Tiny-PDE mendeteksi 167 apel (kepercayaan 0,977), YOLOv7-Tiny 164 (0,959), YOLO11n 165 (0,965), dan YOLOv7x 158 (0,924). Semua model menghitung kurang dari hitungan manual; hitungan per citra tidak dibandingkan dengan lokasi buah, sehingga kesalahan yang saling meniadakan tidak dapat dikesampingkan (menurut pembacaan ringkasan ini).

**Oklusi dan pencahayaan (Tabel 3 dan 4).** Pada tiga model yang dibandingkan lebih rinci:

| Model | Kondisi | P (%) | R (%) | mAP@0,5 (%) | F1 |
|---|---|---|---|---|---|
| YOLOv7x | Oklusi ringan | 99,4 | 98,7 | 99,4 | 0,990 |
| YOLOv7-Tiny | Oklusi ringan | 98,8 | 99,4 | 99,5 | 0,991 |
| YOLOv7-Tiny-PDE | Oklusi ringan | 98,1 | 99,1 | 99,3 | 0,986 |
| YOLOv7x | Oklusi padat | 98,0 | 97,0 | 97,7 | 0,975 |
| YOLOv7-Tiny | Oklusi padat | 97,1 | 96,6 | 97,2 | 0,968 |
| YOLOv7-Tiny-PDE | Oklusi padat | 98,4 | 96,1 | 97,8 | 0,972 |
| YOLOv7x | Cahaya terang | 98,5 | 96,9 | 97,2 | 0,977 |
| YOLOv7-Tiny | Cahaya terang | 97,2 | 96,7 | 97,0 | 0,969 |
| YOLOv7-Tiny-PDE | Cahaya terang | 97,7 | 96,3 | 97,2 | 0,971 |
| YOLOv7x | Cahaya redup | 98,8 | 95,7 | 96,1 | 0,972 |
| YOLOv7-Tiny | Cahaya redup | 98,1 | 94,6 | 95,1 | 0,963 |
| YOLOv7-Tiny-PDE | Cahaya redup | 98,3 | 95,7 | 97,1 | 0,970 |

Pada oklusi ringan, model usulan tidak unggul; YOLOv7-Tiny memiliki F1 dan mAP@0,5 tertinggi. Keunggulan model usulan tampak pada oklusi padat dan cahaya redup, dengan selisih yang kecil. Penilaian visual (Gambar 11 sampai 14) menyatakan bahwa model usulan tidak melewatkan apel pada contoh yang ditampilkan.

**Ablasi (Tabel 5).** Dasar YOLOv7-Tiny memiliki mAP@0,5 94,10%, F1 0,954, dan waktu 19,8 ms. Penambahan komponen tunggal: PConv 94,60% (parameter 4.728.108, 10,7 GFLOPs, 19,1 ms), DyHead 94,40% (R 90,70%, 17,0 ms), EIoU 94,30% (15,6 ms). Kombinasi dua komponen: PConv+DyHead 96,90%, PConv+EIoU 96,20%, EIoU+DyHead 97,70%. Kombinasi ketiganya (PDE) mencapai 97,90%, F1 0,969, dan 17,5 ms. Penulis menyebut waktu deteksi turun 11,6%. Teks ablasi menyebut kenaikan F1 sebesar 1,6%, sedangkan abstrak dan kesimpulan menyebut 1,7%.

**Perbandingan modul perhatian (Tabel 6).** DyHead (5,96 juta parameter, 13,0 GFLOPs) mencapai mAP@0,5 97,8% dan F1 0,972, melampaui CBAM (95,3%; 0,948) dan SE (94,1%; 0,932).

**Penghitungan video (Tabel 7 dan 8).** Pada lima video, hitungan manual adalah 316, 221, 144, 151, dan 101 apel. Jumlah target sebelum perbaikan (A) adalah 355, 237, 157, 163, dan 109; setelah perbaikan (B) adalah 362, 251, 164, 166, dan 113. MAE rerata adalah 0,089 (A) dan 0,127 (B). Pada Tabel 8, MOTA naik dari 89,3% menjadi 91,3%, IDF1 dari 0,82 menjadi 0,91, dan IDSW turun dari 12,3 menjadi 5,7.

**Energi di lapangan (Tabel 9).** Pada platform pesawat nirawak P230 dengan NVIDIA Jetson AGX Xavier, YOLOv7-Tiny-PDE memakai daya rerata 8,3 W (dasar 10,1 W), daya puncak 10,9 W (dasar 12,5 W), dan pemanfaatan GPU 65% (dasar 78%).

## Kelebihan dan Keterbatasan
Kelebihan menurut makalah: model lebih ringan (parameter turun 22,2%, GFLOPs turun 18,3%) dengan mAP@0,5, *recall*, dan F1 tertinggi di antara 11 model yang dibandingkan; konsumsi daya lebih rendah pada Jetson AGX Xavier; MOTA, IDF1, dan IDSW membaik saat digabung dengan DeepSort.

Keterbatasan yang dinyatakan penulis: deteksi target sangat kecil (diameter kurang dari 50 piksel) masih terbatas; pelacakan masih gagal ketika buah tertutup ranting dan daun lebih dari 90% atau saat terjadi perubahan gerak mendadak antarbingkai, karena fitur penampilan hilang; data hanya dikumpulkan pada waktu dan lokasi terbatas sehingga generalisasi sulit dipastikan; apel muda atau kuning-hijau kurang terwakili sehingga perbedaan kematangan belum tercakup; dan penulis merencanakan pemangkasan kanal serta model deret waktu (LSTM, GRU) pada kerja lanjutan.

Menurut pembacaan ringkasan ini terdapat beberapa hal yang perlu diperhatikan. Pertama, galat hitung video (MAE) justru lebih tinggi setelah perbaikan (0,127 dibandingkan 0,089) dan kedua model menghitung lebih banyak daripada hitungan manual pada kelima video, sedangkan teks tidak menjelaskan arah selisih itu; klaim peningkatan penghitungan bertumpu pada MOTA dan IDSW, bukan pada akurasi jumlah. Kedua, penghitungan citra dan video hanya memakai sepuluh citra dan lima video. Ketiga, set uji disebut berjumlah 240 citra pada seksi 2.2 dan 420 citra pada seksi 3.1, dan peningkatan MOTA tertulis 2% pada abstrak dan 2,2% pada seksi 3.5. Keempat, augmentasi dilakukan sebelum pembagian 7:1:2 pada gabungan citra asli dan hasil augmentasi, sehingga kebocoran data antara set latih dan set uji tidak dapat dikesampingkan dari teks. Kelima, satu kelas dan satu lokasi kebun mengurangi daya generalisasi.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video melalui pelacakan multi-objek (*multi-object tracking*, MOT) DeepSort: filter Kalman memprediksi posisi, jaringan ReID memberi fitur penampilan, dan pencocokan bertingkat dengan algoritma Hungarian memberi identitas yang sama pada apel yang sama antarbingkai, sehingga jumlah lintasan unik menjadi hitungan. Mekanisme ini bekerja dalam satu urutan video kontinu; makalah tidak menangani penggabungan lintas pandang yang terputus, seperti sisi pohon yang berbeda dengan pencocokan geometris. Hitungan tidak dilaporkan per kelas, karena hanya ada satu kelas "Apple_object" tanpa atribut kematangan. Acuan hitung adalah hitungan manual pada citra atau video yang dianotasi (hitungan manual dalam sekuens video), bukan hasil panen.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pola detektor ringan ditambah pelacak berbasis penampilan untuk menjaga identitas tandan di sepanjang urutan bingkai, serta metrik MOTA, IDF1, dan IDSW untuk menilai konsistensi identitas. Keterbatasan yang dilaporkan, yaitu kegagalan pelacakan pada oklusi lebih dari 90% dan galat hitung yang tidak membaik, menunjukkan bahwa pelacakan satu video tidak cukup untuk memastikan identitas lintas sisi pohon, dan bahwa metrik pelacakan tidak sama dengan akurasi jumlah.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `cao2025research`.

Cao dkk. (2025, *Agriculture* 15, 483) mengusulkan YOLOv7-Tiny-PDE, yaitu YOLOv7-Tiny dengan konvolusi parsial, kepala deteksi dinamis (DyHead), dan loss EIoU, yang digabung dengan DeepSort untuk mendeteksi dan menghitung apel pada citra pesawat nirawak. Pada dataset apel kustom, model ini mencapai mAP@0,5 97,90% dan F1 0,969 dengan 4,68 juta parameter, mengurangi parameter sebesar 22,2% dan GFLOPs sebesar 18,3% terhadap YOLOv7-Tiny. Dengan DeepSort, MOTA naik dari 89,3% menjadi 91,3% dan pergantian identitas turun dari 12,3 menjadi 5,7; galat hitung terhadap hitungan manual pada lima video tidak membaik (MAE rerata 0,127 dibandingkan 0,089).

Catatan verifikasi data: angka Tabel 1 (deteksi), Tabel 2 (hitung citra), Tabel 3 dan 4 (oklusi dan cahaya), Tabel 5 (ablasi), Tabel 6 (perhatian), Tabel 7 dan 8 (video), serta Tabel 9 (energi) dibaca langsung dari teks ekstraksi yang terbaca baik; tabel diekstraksi satu sel per baris sehingga pemetaan kolom disimpulkan dari urutan. Parameter 6.007.596 menjadi 4.676.516 sesuai penurunan 22,2% (dihitung ulang: sekitar 22,2%). Yang tidak dapat diverifikasi dari teks: nilai hiperparameter pelatihan, jumlah pohon dan kultivar, makna persis kolom "mAP@0.95", jumlah set uji yang benar (240 atau 420), serta cara video dibagi antara pelatihan dan pengujian pelacakan. Teks berbahasa Inggris.
