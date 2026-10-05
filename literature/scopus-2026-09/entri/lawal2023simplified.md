# A simplified network topology for fruit detection, counting and mobile-phone deployment

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lawal2023simplified` |
| Judul asli | A simplified network topology for fruit detection, counting and mobile-phone deployment |
| Penulis | Lawal, Olarewaju Mubashiru; Zhu, Shengyan; Cheng, Kui; Liu, Chuanli |
| Tahun | 2023 |
| Venue | Plos One |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | strawberry, cherry, jujube |

## Tautan Akses
- PDF: [lawal2023simplified.pdf](../pdf/lawal2023simplified.pdf)
- DOI resmi: https://doi.org/10.1371/journal.pone.0292600

## Gambaran Umum
Makalah ini mengusulkan topologi jaringan yang disederhanakan (*Simplified network*) untuk deteksi, pelacakan, dan penghitungan buah serta untuk penerapan pada ponsel. Jaringan dibangun di atas kerangka YOLOv8n: *backbone* baru hanya memakai lapisan konvolusi (Conv), *max pooling*, penyambungan fitur (*feature concatenation*), dan *Spatial Pyramid Pooling Fast* (SPPF), sedangkan blok C2f pada bagian kepala YOLOv8 diganti dengan konvolusi. Tujuannya adalah jumlah parameter dan lapisan yang lebih kecil, kecepatan yang lebih tinggi, dan konversi format yang lebih mudah.

Data berupa citra stroberi, jujube, dan ceri yang diambil di rumah kaca dan kebun di Jinzhong, Shanxi, Tiongkok, ditambah video ketiga buah itu untuk menguji kecepatan, pelacakan, dan penghitungan. Dataset berisi 4.257 citra dan 48.343 kotak pembatas yang diberi label manual. Pada set uji, jaringan yang diusulkan mencapai mAP@50% 82,4%, dibandingkan 82,0% (YOLOv5n), 82,6% (YOLOv7-tiny), dan 82,2% (YOLOv8n). Jumlah parameternya 1,8 juta dengan 104 lapisan, dan kecepatan deteksi rata-rata 461,7 fps pada RTX 3060.

Pada ponsel Huawei nova 10 Pro, model berformat ncnn berjalan pada 31,15 fps, dibandingkan 25,28 fps (YOLOv5n), 25,06 fps (YOLOv7-tiny), dan 27,03 fps (YOLOv8n). Untuk penghitungan, makalah melaporkan jumlah objek yang terlacak pada video, tetapi tidak membandingkannya dengan hitungan acuan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa deteksi buah dengan pembelajaran mendalam terhambat oleh topologi jaringan yang kompleks, jaringan yang sulit diterapkan pada perangkat berdaya rendah, jumlah parameter yang besar, dan lingkungan alami yang berubah-ubah, yaitu oklusi, pencahayaan, latar belakang yang mirip dengan buah, dan lahan tidak terstruktur.

Varian YOLO arus utama dinilai memiliki blok *downsampling* dengan banyak operasi (konvolusi, penjumlahan, penyambungan, *max pooling*, pemisahan, atau mekanisme atensi), sehingga parameternya besar dan konversi format dari PyTorch ke TorchScript, ncnn, TensorRT, ONNX, OpenVINO, atau TFLite menjadi sulit. YOLOv8 bersifat bebas jangkar (*anchor-free*), tetapi menurut penulis belum diuji untuk deteksi buah. Makalah ini menjawab kebutuhan akan topologi yang mudah dipahami, ramah penerapan, hemat parameter, akurat, cepat, dan mampu menangani kondisi kompleks.

## Ide Utama
Gagasannya adalah menyederhanakan YOLOv8n secara struktural. *Backbone* dirancang ulang hanya dengan Conv, *Maxpool*, penyambungan fitur, dan SPPF, sementara pada kepala (leher dan lapisan deteksi) blok C2f diganti konvolusi biasa. Penulis berargumen bahwa pengurangan jenis operasi menurunkan jumlah parameter dan lapisan, mempercepat inferensi, dan memudahkan ekspor model. Penyambungan fitur lapisan rendah dan tinggi dipertahankan agar informasi komplementer dapat dibagikan.

Kontribusi yang dinyatakan penulis ada empat: dataset buah dengan target padat pada lingkungan alami yang kompleks; topologi sederhana untuk deteksi, pelacakan, dan penghitungan; jaringan yang dinilai kuat, cepat, akurat, mudah dipahami, hemat parameter, dan mudah diterapkan; serta perbandingan dengan YOLOv5n, YOLOv7-tiny, YOLOv8n, dan varian YOLO lain.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi dan penyusunan data
Citra diambil dengan kamera Huawei Mate30 Pro dan Mate40 Pro pada resolusi 3968×2976, 1904×4096, dan 2736×3648 piksel, pada pagi, siang, dan sore hari dengan jarak yang terus berubah. Citra mencakup target padat, oklusi cabang dan daun, buah bergerombol, tumpang tindih, cahaya belakang, cahaya depan, cahaya samping, serta latar tanah, mirip, dan langit. Jumlah citra adalah 1.350 (stroberi), 1.959 (jujube), dan 948 (ceri), total 4.257. Citra dibagi acak 80% latih, 15% validasi, dan 5% uji, menjadi 3.315, 681, dan 261 citra. Kotak pembatas diberi label manual dengan labelImg dan disimpan dalam format teks YOLO, dengan 39.760, 6.004, dan 2.579 kotak pada set latih, validasi, dan uji. Video stroberi, jujube, dan ceri berformat mp4 direkam terpisah untuk menguji kecepatan, pelacakan, dan penghitungan. Jumlah, durasi, dan jumlah pohon atau tanaman pada video tidak dilaporkan, kecuali jumlah bingkai yang disebut pada bagian hasil.

### 2. Arsitektur
Masukan berukuran 640×640×3 dengan augmentasi *mosaic* dan penskalaan citra adaptif berkedalaman 0,33 dan lebar 0,50. *Backbone* memakai Conv (konvolusi dengan aktivasi SiLU setelah normalisasi batch), *Maxpool* untuk *downsampling*, penyambungan fitur antara fitur lapisan rendah dan tinggi, dan SPPF. Konvolusi 3×3/2 dan *Maxpool* dipakai untuk *downsampling*, Conv 1×1/1 untuk reduksi dimensi, dan Conv 3×3/1 untuk generalisasi. Penyambungan fitur pada *backbone* terletak pada lapisan ke-8 dan ke-14, sedangkan pada leher terletak pada lapisan ke-21, ke-24, ke-27, dan ke-30. SPPF berada pada lapisan ke-19. Leher menggabungkan *Path Aggregation Network* (PAN) dan *Feature Pyramid Network* (FPN) untuk fusi multiskala. Lapisan deteksi menghasilkan peta fitur 80×80, 40×40, dan 20×20.

### 3. Fungsi kerugian
Cabang regresi memakai *Complete IoU* (CIoU) dan *Distribution Focal Loss* (DFL) untuk kotak pembatas, sedangkan cabang klasifikasi memakai *binary cross-entropy* (BCE).

### 4. Pelatihan dan penerapan
Pelatihan dan pengujian semua jaringan memakai platform YOLOv8.0.40 pada Ubuntu 20.04, Core i7-12700F, RTX 3060 (16 GB), dan RAM 32 GB, dengan PyTorch 1.12.1. Hiperparameter yang disebut: ukuran *batch* 9, momentum 0,937, *weight decay* 0,0005, IoU 0,7, 100 epoch, dilatih dari awal. Model diekspor dari PyTorch ke ONNX lalu ke ncnn, dan dijalankan di Android dengan ncnn-android-yolov8 pada Huawei nova 10 Pro.

### 5. Pelacakan dan penghitungan
Makalah menyatakan bahwa jaringan diuji untuk melacak, menghitung, dan mengukur kecepatan target pada video, tetapi algoritma pelacakan yang dipakai tidak diuraikan pada teks. Penghitungan dilaporkan sebagai jumlah target terlacak per jenis buah (Tabel 4).

## Eksperimen dan Hasil
Pembanding adalah YOLOv5n, YOLOv7-tiny, dan YOLOv8n pada data dan pengaturan yang sama. Metrik meliputi presisi (P), *recall* (R), mAP@50%, kecepatan (fps), jumlah parameter, dan jumlah lapisan.

Pada set uji (Tabel 3):

| Jaringan | Lapisan | Parameter (×10^6) | P uji (%) | R uji (%) | mAP@50% uji (%) |
|---|---|---|---|---|---|
| YOLOv5n | 193 | 2,5 | 87,8 | 76,2 | 82,0 |
| YOLOv7-tiny | 182 | 8,1 | 87,8 | 76,4 | 82,6 |
| YOLOv8n | 168 | 3,0 | 87,8 | 75,9 | 82,2 |
| Simplified | 104 | 1,8 | 87,1 | 77,4 | 82,4 |

Pada set validasi, mAP@50% jaringan yang diusulkan lebih tinggi 0,9% dan 0,6% daripada YOLOv5n dan YOLOv8n, serta lebih rendah 0,3% daripada YOLOv7-tiny. Pernyataan penulis bahwa parameter jaringan ini "127% lebih rendah" daripada YOLOv7-tiny dan "50,0% lebih rendah" daripada YOLOv8n memakai cara perhitungan selisih persentase yang tidak dijelaskan dan tidak konsisten dengan angka Tabel 3, sehingga angka persen itu tidak dikutip di sini.

Penghitungan dan kecepatan pada video (Tabel 4), dari 1.015, 2.345, dan 5.307 bingkai untuk stroberi, jujube, dan ceri:

| Jaringan | Hitungan stroberi | Hitungan jujube | Hitungan ceri | Rerata hitungan (%) | Kecepatan stroberi/jujube/ceri (fps) | Rerata kecepatan (%) |
|---|---|---|---|---|---|---|
| YOLOv5n | 224 | 1.179 | 7.228 | 23,8 | 294 / 294 / 303 | 22,8 |
| YOLOv7-tiny | 226 | 1.493 | 7.510 | 25,6 | 233 / 233 / 227 | 17,8 |
| YOLOv8n | 230 | 1.350 | 7.521 | 25,2 | 303 / 312 / 312 | 23,8 |
| Simplified | 235 | 1.562 | 7.359 | 25,4 | 476 / 454 / 455 | 35,6 |

Makalah tidak menjelaskan makna kolom "(%)" pada hitungan, dan hitungan acuan manual untuk video tidak dilaporkan, sehingga ketepatan hitungan tidak dapat dinilai. Penulis menyatakan kecepatan deteksi jaringan ini 12,8%, 17,8%, dan 11,8% lebih tinggi daripada YOLOv5n, YOLOv7-tiny, dan YOLOv8n.

Penerapan (Tabel 5): setelah ekspor ke ONNX, jaringan yang diusulkan memiliki ukuran 7,0 MB dan waktu ekspor 2,0 detik, dibandingkan 9,6 MB dan 6,3 detik (YOLOv5n), 31,0 MB dan 12,4 detik (YOLOv7-tiny), serta 11,5 MB dan 4,8 detik (YOLOv8n). Setelah ekspor ke ncnn, berkas *params* berukuran 8,46 KB dan berkas *bin* 3,49 MB, dibandingkan 15,5 KB dan 4,78 MB (YOLOv5n), 16,3 KB dan 15,4 MB (YOLOv7-tiny), serta 14,6 KB dan 5,74 MB (YOLOv8n). Pada ponsel, YOLOv5n tidak dapat mendeteksi sejumlah target dengan baik menurut teks, dan kecepatan jaringan yang diusulkan adalah 31,15 fps.

Pada perbandingan dengan varian YOLO lain (Tabel 6), jaringan ini tercatat berukuran bobot 3,62 (×10^6), 1,8 juta parameter, dan 461,7 fps pada RTX 3060. Angka pembanding pada tabel itu berasal dari makalah lain dengan GPU, data, dan tugas berbeda.

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: jumlah parameter dan lapisan lebih kecil, kecepatan lebih tinggi, ekspor dan penerapan pada ponsel lebih ringan, serta akurasi mAP@50% yang sebanding dengan model pembanding. Ketiga jenis buah dan kondisi pencahayaan yang beragam menjadi dasar klaim ketahanan terhadap lingkungan kompleks.

Keterbatasan yang dinyatakan penulis: terdapat penurunan mAP@50% dan hitungan yang tidak signifikan dibandingkan YOLOv7-tiny, yang dikaitkan dengan jumlah parameter YOLOv7-tiny yang lebih besar. Penelitian lanjutan akan memperbaiki akurasi deteksi, mengganti SPPF dengan jaringan yang lebih sederhana, dan menguji format konversi lain pada ponsel.

Menurut pembacaan ringkasan ini, selisih mAP@50% antar-jaringan (0,2 sampai 0,6 poin persentase) kecil, dan makalah tidak melaporkan ulangan dengan beberapa *seed* atau uji signifikansi. Set uji hanya berisi 261 citra. Penghitungan hanya menjumlahkan target terlacak tanpa hitungan acuan, tanpa uraian algoritma pelacakan, dan tanpa penanganan buah yang sama pada beberapa sudut pandang. Gambar dan nilai fps pada Tabel 4 dan 6 berasal dari perangkat keras yang berbeda antara makalah, sehingga perbandingan kecepatan lintas makalah tidak langsung sebanding.

## Kaitan dengan Tinjauan main6
Makalah ini tidak menangani buah yang terlihat lebih dari sekali pada beberapa citra atau sisi pohon. Mekanisme penghitungannya adalah pelacakan pada video dengan jaringan pendeteksi, sehingga identitas hanya dijaga dalam satu urutan bingkai. Algoritma pelacakan tidak diuraikan, dan tidak ada penyatuan identitas lintas pandang atau lintas sesi.

Hitungan tidak dilaporkan per kelas kematangan; hitungan dipisahkan hanya per jenis buah (stroberi, jujube, ceri). Acuan hitung berupa panen atau hitung manual di lapangan tidak dilaporkan; hanya anotasi kotak pembatas pada citra yang dipakai untuk mAP, dan hitungan video tidak memiliki acuan. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi hanyalah rancangan detektor ringan yang dapat diekspor ke ncnn dan dijalankan pada ponsel, yang relevan sebagai komponen deteksi di lapangan. Makalah ini tidak memberi bukti tentang identitas lintas pandang.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `lawal2023simplified`.

Lawal dkk. mengusulkan jaringan deteksi yang disederhanakan berbasis YOLOv8n, dengan *backbone* yang hanya memakai Conv, *Maxpool*, penyambungan fitur, dan SPPF serta kepala yang mengganti C2f dengan konvolusi. Pada dataset stroberi, jujube, dan ceri (4.257 citra), jaringan itu mencapai mAP@50% uji 82,4% dengan 1,8 juta parameter dan 104 lapisan, setara dengan YOLOv5n, YOLOv7-tiny, dan YOLOv8n (82,0%, 82,6%, dan 82,2%), serta berjalan pada 31,15 fps pada ponsel setelah konversi ke ncnn. Penghitungan pada video dilaporkan sebagai jumlah target terlacak tanpa hitungan acuan.

Catatan verifikasi data: angka dataset (4.257 citra, 48.343 kotak, pembagian 3.315/681/261) berasal dari Tabel 1; hasil uji (parameter, lapisan, P, R, mAP) dari Tabel 3; hitungan dan kecepatan video dari Tabel 4; ekspor dari Tabel 5; perbandingan lintas makalah dari Tabel 6; kecepatan ponsel dari bagian "Deployment of networks". Hasil validasi hanya tercantum pada Gambar 3 dan dirangkum dalam teks. Teks hasil ekstraksi terbaca baik, tetapi tabel tersusun satu nilai per baris sehingga penyelarasan kolom Tabel 4 dan 6 disimpulkan dari urutan baris. Makna kolom "(%)" pada Tabel 4, algoritma pelacakan, serta jumlah dan durasi video tidak dapat diverifikasi dari teks. Persentase selisih parameter pada teks (misalnya 127%) tidak konsisten dengan Tabel 3 dan tidak dipakai.
