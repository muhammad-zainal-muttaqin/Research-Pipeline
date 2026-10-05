# Tracking and Counting of Tomato at Different Growth Period Using an Improving YOLO-Deepsort Network for Inspection Robot

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ge2022tracking` |
| Judul asli | Tracking and Counting of Tomato at Different Growth Period Using an Improving YOLO-Deepsort Network for Inspection Robot |
| Penulis | Ge, Yuhao; Lin, Sen; Zhang, Yunhe; Li, Zuolin; Cheng, Hongtai; Dong, Jing; Shao, Shanshan; Zhang, Jin; Qi, Xiangyu; Wu, Zedong |
| Tahun | 2022 |
| Venue | Machines |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [ge2022tracking.pdf](../pdf/ge2022tracking.pdf)
- DOI resmi: https://doi.org/10.3390/machines10060489

## Gambaran Umum
Makalah ini mengusulkan jaringan pelacakan objek visual bernama YOLO-deepsort untuk mengenali dan mencacah tomat serta bunga tomat pada beberapa periode pertumbuhan di rumah kaca (*greenhouse*). Detektor dibangun dari YOLOv5s dengan modul ShuffleNetV2, modul perhatian *Convolutional Block Attention Module* (CBAM), dan struktur *neck* BiFPN. Keluaran detektor diteruskan ke pelacak DeepSORT yang memakai filter Kalman, sehingga setiap objek memperoleh ID yang bertahan antarbingkai video. Pencacahan dilakukan dengan garis hitung virtual yang dibuat memakai OpenCV.

Data diambil dari video yang direkam kamera pada robot inspeksi di pangkalan demonstrasi di Shouguang, Shandong, China. Data deteksi terdiri atas 1.000 citra latih dan 100 citra uji dengan tiga kelas: bunga (*flower*), tomat merah (*tomato red*), dan tomat hijau (*tomato green*). Data pelacakan bernama Tracking_tomato_115 berisi 115 target tomat dan bunga dengan 1.711 kotak terdeteksi.

Hasil utama: pada set uji, YOLO-deepsort mencapai mAP(0,5:0,95) 95,8% dengan 5.072.848 parameter dan berkas bobot 10,5 MB, dibandingkan dengan 88,7% pada YOLOv5s. Abstrak melaporkan mAP bunga, tomat hijau, dan tomat merah masing-masing 93,1%, 96,4%, dan 97,9%. Kemampuan pelacakan dan pencacahan hanya diperlihatkan secara kualitatif pada pencacahan bunga tomat (Gambar 16); makalah tidak melaporkan galat hitungan terhadap acuan lapangan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pertanian fasilitas (*facility agriculture*) memerlukan pemantauan periode pertumbuhan dan prakiraan hasil panen. Penulis menyatakan bahwa metode deteksi berbasis warna dan fitur buatan tangan, misalnya klaster K-means pada ruang warna L*a*b* atau SVM dengan HOG, memiliki kemampuan ekstraksi fitur yang terbatas sehingga kurang kokoh. Model pembelajaran mendalam yang diterapkan langsung ke pertanian tidak mempertimbangkan biaya, sedangkan rumah kaca memerlukan model dengan biaya komputasi dan penyimpanan rendah. Pelonggaran model (*lightweight*) hampir selalu menurunkan akurasi, sehingga diperlukan kompensasi.

Masalah kedua berkaitan langsung dengan pencacahan. Penulis menyatakan bahwa pencacahan buah dengan menghitung kotak deteksi pada citra tunggal tidak bernilai praktis karena pertumbuhan tanaman tidak terstruktur dan buah relatif jarang. Penggunaan jaringan deteksi saja untuk prakiraan hasil membuat hitungan ganda tidak terhindarkan. Penulis menyimpulkan perlunya metode baru, yaitu pelacakan objek yang memberi identitas pada setiap target di sepanjang video.

## Ide Utama
Gagasan utamanya adalah menggabungkan detektor ringan berakurasi tinggi dengan pelacak berbasis kemiripan tampilan. Detektor dilonggarkan dengan ShuffleNetV2, kehilangan kemampuan ekstraksi fitur akibat pelonggaran dikompensasi oleh CBAM pada lapisan awal, dan penggunaan fitur multi-skala dioptimalkan oleh BiFPN. Pelacak DeepSORT memberi ID unik pada tiap objek, sehingga objek yang melintasi garis hitung berulang kali tidak dihitung lebih dari satu kali.

Pelacak memakai jaringan konvolusi yang dilatih terpisah (*offline*) pada data Tracking_tomato_115 agar dapat menilai apakah dua pengamatan dari sudut pengambilan gambar berbeda merupakan target yang sama. Dalam teks makalah, tiap target difoto dari tiga posisi kamera dan setiap target ditangkap oleh sekurangnya dua kamera.

## Cara Kerja Langkah demi Langkah

```
  [ Video robot inspeksi ] --> [ YOLO-deepsort: detektor ]
                                   (ShuffleNetV2 + CBAM + BiFPN)
                                           |
                                           v
                          [ Kotak, skor, fitur tampilan ]
                                           |
                                           v
              [ DeepSORT: Kalman + Mahalanobis + cosinus + Hungarian ]
                                           |
                                           v
                          [ ID tiap objek ] --> [ garis hitung virtual ]
```

### 1. Akuisisi data
Pengambilan citra dan uji model dilakukan di Pusat Standar Mutu Sayuran Nasional (Shouguang, Shandong) dalam rumah kaca. Kamera dipasang pada robot inspeksi yang bernavigasi dengan kode QR melalui rute yang telah ditetapkan. Citra untuk pelatihan dan pengujian detektor diambil dari aliran video tiap 10 fps. Pembagian data latih dan uji berbanding 10:1, yaitu 1.000 citra latih dan 100 citra uji. Kultivar tomat tidak dilaporkan.

Pada studi kelayakan awal, penulis menemukan bahwa YOLOv5s dengan sekitar 600 target per kelas pada set latih menghasilkan mAP(0,95) bunga 60,4%, tomat hijau 87,6%, dan tomat merah 94,3%. Karena itu, jumlah bunga dan tomat hijau ditambah secara sengaja. Jumlah target akhir disajikan pada Tabel 1 makalah.

| Set | Bunga | Tomat merah | Tomat hijau | Total |
|---|---|---|---|---|
| Latih | 1.640 | 669 | 1.138 | 3.447 |
| Uji | 164 | 68 | 139 | 371 |

Anotasi dilakukan dengan labelImg. Untuk data pelacakan, robot merekam video dengan kecepatan konstan dari tiga posisi kamera, dengan satu citra tiap 10 fps untuk satu target dan total lima pengambilan. Setelah penyaringan diperoleh 115 target tomat dan bunga dengan 1.711 kotak terdeteksi.

### 2. Augmentasi data
Augmentasi dilakukan pada set latih deteksi: perubahan ruang warna HSV (h 0,015; s 0,6; v 0,4), pembalikan horizontal dengan peluang 50%, dan augmentasi *mosaic* yang menggabungkan empat citra dengan penskalaan, pemotongan, dan penempatan acak.

### 3. Detektor YOLO-deepsort
Detektor berbasis YOLOv5s. Lapisan awal memakai Conv_CBAM, bagian tengah tulang punggung (*backbone*) memakai blok CSP dan modul *Inverted Residual* ShuffleNetV2 (pemisahan kanal dan pengacakan kanal), lapisan akhir memakai SPPF, dan *neck* memakai BiFPN yang menggunakan koneksi lintas skala dua arah dengan fusi berbobot. Terdapat tiga kepala deteksi berukuran 80×80×21, 40×40×21, dan 20×20×21; 21 kanal berasal dari (kelas + keyakinan + empat offset koordinat) × 3 jangkar. CBAM memadukan perhatian kanal (*average pooling* dan *max pooling* global) dan perhatian spasial (konvolusi berukuran kernel 7).

### 4. Pelatihan detektor
Hiperparameter: optimizer SGD, *momentum* 0,937, *weight decay* 0,0005, ukuran *batch* 8, bobot *loss* box 0,05, cls 0,5, obj 1,0, ambang IoU 0,2, dan ambang jangkar 4,0. Laju belajar dipanaskan secara linear lalu diturunkan dengan *cosine annealing*, dan lapisan bobot, bias, serta BN memakai penyetelan laju belajar yang berbeda. *Non-maximum suppression* memakai ambang 0,5 dan CIoU. Penulis menyatakan bahwa pemilihan hiperparameter didasarkan pada pertimbangan subjektif dan pengalaman. Perangkat keras pelatihan jaringan fitur pelacak adalah CPU Xeon 2,5 GHz, memori 64 GB, dan GPU Nvidia 2080 Ti 12 GB.

### 5. Pelacakan dan pencacahan
DeepSORT meneruskan sisa kerja SORT: filter Kalman memprediksi posisi dan kecepatan kotak pada bingkai berikutnya dan diperbarui dengan hasil pengamatan. Kemiripan lintasan diukur dengan jarak Mahalanobis, kemiripan tampilan dengan jarak cosinus pada fitur dari jaringan konvolusi, dan keduanya digabung dalam biaya terbobot $c_{i,j}=\lambda t^{(1)}(i,j)+(1-\lambda)t^{(2)}(i,j)$. Pencocokan memakai algoritma Hungarian dengan matriks biaya yang juga memuat IoU. Jaringan fitur pelacak dilatih lebih dari 3.500 epoch secara terpisah. Ambang keyakinan deteksi ditetapkan 0,75 saat inferensi agar model hanya mendeteksi target pada barisan tanaman yang sedang dilewati dan menghindari penghitungan ganda dari target yang jauh. Objek yang menyentuh garis hitung virtual dihitung. Ketika deteksi gagal pada sebagian bingkai karena guncangan robot, fitur target yang sudah ber-ID disimpan agar ID tidak berubah saat target terdeteksi kembali.

## Eksperimen dan Hasil
Pembanding adalah YOLOv5s, YOLOv5m, dan YOLOv5l yang dilatih pada data dan perangkat yang sama dan diuji pada set uji yang sama (100 citra). Perbandingan kedua adalah terhadap model ringan lain (YOLO_nano, YOLOv3-tiny, YOLOv5n, YOLOv5_Lite).

Tabel 4 makalah (hasil deteksi, mAP pada IoU 0,5:0,95):

| Model | Presisi | Recall | F1 | mAP(0,5:0,95) | Parameter |
|---|---|---|---|---|---|
| YOLOv5s | 99,5% | 90,6% | 94,8% | 88,7% | 7.018.216 |
| YOLOv5m | 99,5% | 95,3% | 97,4% | 91,6% | 13.354.682 |
| YOLOv5l | 99,5% | 94,1% | 96,7% | 91,6% | 46.119.048 |
| YOLO-deepsort | 99,5% | 98,4% | 98,9% | 95,8% | 5.072.848 |

Tabel 5 makalah (biaya penyimpanan model ringan):

| Model | Ukuran masukan | Parameter | Ukuran (MB) | Presisi | mAP(0,5:0,95) |
|---|---|---|---|---|---|
| YOLO_nano | 416×416 | tidak dilaporkan | 34,8 | 30,5% | 15,4% |
| YOLOv3-tiny | 416×416 | 8,67 M | 17,4 | 95,7% | 86,7% |
| YOLOv5n | 640×640 | 1,76 M | 3,8 | 96,7% | 85,4% |
| YOLOv5_Lite | 640×640 | 5,39 M | 10,9 | 99,2% | 91,3% |
| YOLO-deepsort | 640×640 | 5,07 M | 10,5 | 99,5% | 95,8% |

Penulis menyatakan bahwa dibandingkan dengan YOLOv5s, presisi tidak berubah, F1 naik 4,1%, dan mAP(0,95) naik 7,1% (angka 4,1 dan 7,1 sesuai selisih Tabel 4: 98,9 dikurangi 94,8 dan 95,8 dikurangi 88,7). Pada bagian kesimpulan, mAP per kelas dilaporkan 93,1% (bunga), 96,4% (tomat hijau), dan 97,9% (tomat merah), naik masing-masing 17%, 2%, dan 2,3% terhadap YOLOv5s; makalah tidak menyertakan tabel per kelas untuk angka itu, dan tidak menjelaskan hubungannya dengan mAP 95,8% pada Tabel 4.

Hasil pelacakan dan pencacahan hanya disajikan secara kualitatif. Pada Gambar 16, tiga target pada citra diberi ID tertentu dan ID itu dipertahankan ketika kamera bergerak. Makalah tidak melaporkan akurasi pelacakan (misalnya jumlah pergantian ID), jumlah hitungan yang diperoleh, maupun perbandingannya dengan hitung manual.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: model sangat ringan (5,07 juta parameter, bobot 10,5 MB) dengan akurasi deteksi lebih tinggi daripada YOLOv5s, m, dan l pada set uji yang sama; konvergensi lebih cepat (mAP stabil setelah 350 epoch, sedangkan YOLOv5s baru stabil pada epoch ke-500); serta pelacakan yang mencegah hitungan ganda ketika target melintasi garis hitung berulang kali.

Keterbatasan yang dinyatakan penulis: deteksi tidak stabil karena lingkungan rumah kaca yang kompleks dan guncangan saat inspeksi, yang berdampak buruk pada pelacakan dan pencacahan. Penulis menyatakan akan meningkatkan kecepatan dan stabilitas untuk deteksi waktu-nyata pada adegan kompleks. Penulis juga menyatakan bahwa hiperparameter dipilih berdasarkan penilaian subjektif.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan tambahan. Pertama, kualitas pencacahan tidak diukur secara kuantitatif; klaim bahwa hitungan ganda dihindari hanya didukung ilustrasi. Kedua, set uji deteksi kecil (100 citra, 371 target) dan presisi 99,5% yang sama pada keempat model menunjukkan bahwa metrik tersebut mungkin jenuh. Ketiga, citra uji diambil dari pangkalan yang sama dengan citra latih, sehingga generalisasi ke kebun lain tidak teruji. Keempat, jumlah bunga dan tomat hijau pada set latih ditambah secara sengaja, sehingga distribusi kelas tidak mencerminkan kondisi alami. Kelima, mAP per kelas pada abstrak tidak dapat dicocokkan dengan Tabel 4.

## Kaitan dengan Tinjauan main6
Makalah ini menangani objek yang terlihat lebih dari sekali dalam aliran video dengan pelacakan multi-objek: detektor menghasilkan kotak, DeepSORT mengasosiasikannya antarbingkai memakai prediksi filter Kalman, jarak Mahalanobis, dan kemiripan fitur tampilan, lalu hitungan bertambah ketika objek ber-ID melintasi garis virtual. Pada data pelacakan, setiap target difoto dari tiga posisi kamera dan jaringan fitur dilatih untuk menilai apakah pengamatan dari sudut berbeda berasal dari target yang sama, sehingga ada unsur penentuan identitas lintas pandang. Pengamatan tersebut tetap berupa urutan video dari robot yang bergerak di sepanjang barisan, bukan pandangan mengelilingi satu tanaman.

Hitungan tidak dilaporkan per kelas pada tahap pelacakan; kelas (bunga, tomat merah, tomat hijau) muncul pada evaluasi detektor, sedangkan demonstrasi pencacahan hanya mencakup bunga. Acuan hitung berupa anotasi citra untuk deteksi dan data pelacakan yang dianotasi; hitung manual atau panen di lapangan sebagai pembanding tidak dilaporkan. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan ID persisten berbasis fitur tampilan yang dilatih untuk mencocokkan target yang sama dari sudut berbeda, serta penyaringan berdasarkan ambang keyakinan untuk menghindari objek di barisan lain. Kekurangan yang perlu diperhatikan adalah ketiadaan evaluasi hitungan, dan ketergantungan pada urutan gerak yang kontinu.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `ge2022tracking`.

Ge dkk. (2022) mengusulkan YOLO-deepsort, yaitu detektor YOLOv5s yang diringankan dengan ShuffleNetV2, CBAM, dan BiFPN, digabungkan dengan pelacak DeepSORT untuk mencacah bunga dan tomat pada berbagai periode pertumbuhan di rumah kaca melalui garis hitung virtual. Pada 100 citra uji, model mencapai mAP(0,5:0,95) 95,8% dengan 5,07 juta parameter dan bobot 10,5 MB, lebih tinggi daripada YOLOv5s (88,7%). Kemampuan pencacahan ditunjukkan secara kualitatif pada bunga tomat tanpa evaluasi hitungan terhadap acuan lapangan.

Catatan verifikasi data: mAP(0,5:0,95), presisi, recall, F1, dan jumlah parameter diambil dari Tabel 4; ukuran bobot dan perbandingan model ringan dari Tabel 5; jumlah target dari Tabel 1; pembagian 1.000 dan 100 citra serta data Tracking_tomato_115 (115 target, 1.711 kotak) dari Bagian 2.1.1. Angka mAP per kelas 93,1%, 96,4%, 97,9% dan kenaikan 17%, 2%, 2,3% tercantum pada abstrak dan Bagian 5 tetapi tidak ada tabelnya. Tabel 2 dan tabel hiperparameter terbaca dari ekstraksi teks namun hanya dipakai sebagian. Teks tidak melaporkan kultivar tomat, jumlah bingkai atau panjang video, galat hitungan, maupun metrik pelacakan; hal itu tidak dapat diverifikasi dari teks. Makalah berbahasa Inggris dan ekstraksi teksnya dapat dibaca.
