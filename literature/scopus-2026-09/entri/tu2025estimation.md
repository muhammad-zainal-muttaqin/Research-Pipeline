# Estimation of passion fruit yield based on YOLOv8n + OC-SORT + CRCM algorithm

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tu2025estimation` |
| Judul asli | Estimation of passion fruit yield based on YOLOv8n + OC-SORT + CRCM algorithm |
| Penulis | Tu, Shuqin; Huang, Yufei; Huang, Qiong; Liu, Hongxing; Cai, Yifan; Lei, Hua |
| Tahun | 2025 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | passion fruit |

## Tautan Akses
- PDF: [tu2025estimation.pdf](../pdf/tu2025estimation.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.109727

## Gambaran Umum
Makalah ini mengusulkan alur kerja tiga tahap untuk memperkirakan hasil panen markisa (*passion fruit*) dari video yang direkam dengan ponsel pada kebun komersial di Distrik Zengcheng, Guangzhou, Tiongkok. Tahap pertama adalah deteksi buah dengan YOLOv8n. Tahap kedua adalah pelacakan multi-objek (*multi-object tracking*, MOT) dengan OC-SORT. Tahap ketiga adalah metode penghitungan baru bernama *Central Region Counting Method* (CRCM), yang menghitung buah berdasarkan masuk atau keluarnya titik pusat (*centroid*) buah dari sebuah wilayah penghitungan di tengah bingkai.

Data berupa 24 video berdurasi sekitar 1 menit (resolusi 1080×1920, 30 bingkai per detik). Lima video dipilih secara acak untuk pengujian deteksi, pelacakan, dan penghitungan. Pada himpunan uji, YOLOv8n mencapai mAP@0,5 sebesar 86,3% dengan ukuran model 6,2 MB. OC-SORT mencapai HOTA 67,10% dan melampaui BoT-SORT, ByteTrack, dan StrongSORT masing-masing sebesar 2,98%, 4,71%, dan 8,82% (angka selisih sebagaimana dilaporkan penulis).

Pada penghitungan, CRCM mencapai akurasi penghitungan rerata 87,0%, dibandingkan 37,2% untuk jumlah ID maksimum dan 76,5% untuk *Single Line Method* (SLM). Penulis menyatakan bahwa kontribusinya terletak pada evaluasi sistematis kombinasi detektor, pelacak, dan metode penghitungan, bukan pada kebaruan masing-masing komponen.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penaksiran hasil markisa secara manual dinilai membosankan dan memakan waktu. Penghitungan berbasis penglihatan komputer menghadapi oklusi oleh daun, variasi cahaya, dan guncangan kamera, yang menimbulkan deteksi terlewat, deteksi keliru, dan penghitungan ganda pada buah kecil. Markisa tumbuh sebagai tanaman merambat dengan buah yang rapat dan warna yang mirip dengan daun, sehingga kondisi ini lebih sulit daripada apel yang buahnya kontras dengan daun menurut pembahasan penulis.

Banyak penelitian menaksir jumlah buah dari banyaknya ID yang dihasilkan pelacak. Karena ID sering berganti (*ID switch*), jumlah itu cenderung melebihi jumlah buah sebenarnya. Beberapa peneliti telah memakai metode penghitungan lain selama pelacakan, tetapi penulis menyatakan belum ada penelitian yang membandingkan secara sistematis detektor, pelacak, dan metode penghitungan arus utama untuk satu tugas yang sama.

## Ide Utama
Gagasan utama adalah memisahkan jumlah buah dari jumlah ID pelacak. Buah dihitung ketika lintasannya berinteraksi dengan wilayah penghitungan tertentu, sehingga pergantian ID di luar wilayah itu tidak menggelembungkan hitungan. Wilayah berupa persegi panjang yang lebar, bukan satu garis, supaya buah yang baru terdeteksi di dalam wilayah tetap terhitung. Hal ini mengatasi kelemahan SLM yang hanya menghitung buah yang melintasi garis.

Pemilihan komponen dilakukan secara empiris. Detektor dipilih dari beberapa varian YOLO berdasarkan keseimbangan akurasi dan ukuran. Pelacak dipilih karena OC-SORT dirancang untuk gerak tidak linear dan oklusi, yang sesuai dengan perekaman genggam yang bergoyang.

## Cara Kerja Langkah demi Langkah

```
  [ Video ponsel ] -> [ YOLOv8n: kotak + skor ] -> [ OC-SORT: ID lintasan ]
                                                         |
                          +------------------------------+--------------+
                          v                              v              v
                     [ Jumlah ID ]                   [ SLM ]        [ CRCM ]
```

### 1. Akuisisi data
Video direkam pada 14 Oktober 2022 saat cuaca cerah di kebun markisa dengan budi daya sistem guludan (jarak antartanaman 1,5 m, lebar parit 1 m, lebar guludan 1 m). Perekam berjalan di sepanjang parit dengan ponsel, sudut ponsel tegak lurus terhadap guludan, jarak ponsel ke buah 1 m, dan tinggi 1,5 m. Terdapat 24 video, masing-masing sekitar 1 menit, 1080×1920, 30 bingkai per detik. Separuh direkam membelakangi matahari dan separuh menghadap matahari (rasio 5:5). Sekitar 200 citra dari seluruh bingkai terkena guncangan kamera. Kultivar markisa tidak dilaporkan.

### 2. Pengolahan data
Untuk himpunan deteksi, laju bingkai diturunkan menjadi 5 bingkai per detik, bingkai diekstrak dengan FFmpeg, dan anotasi dibuat dengan perangkat lunak DarkLabel lalu dikonversi ke format YOLO dan COCO. Total 6.445 citra dipakai untuk deteksi, terdiri atas 5.051 citra latih dan 1.394 citra validasi. Lima video yang dipilih acak untuk tugas pelacakan dan penghitungan dianotasi langsung dengan DarkLabel sebagai data validasi. Makalah menyebut pemisahan ini sebagai himpunan uji dan validasi secara bergantian; kepastian bahwa lima video itu tidak tumpang tindih dengan citra latih deteksi tidak dinyatakan secara eksplisit.

### 3. Deteksi dengan YOLOv8n
Detektor bertipe satu tahap (*single-stage*) tanpa jangkar (*anchor-free*), memakai modul C2f dan modul SPPF pada tulang punggung serta PAN-FPN pada leher jaringan. Pelatihan memakai transfer, dengan kelas standar digabung menjadi satu kelas "passion fruit". Parameter: 200 epoch, ukuran batch 32, ukuran masukan 640, laju belajar 0,01, pengoptimal SGD, conf-thres 0,25, dan iou-thres 0,45. Augmentasi mencakup Mosaic, Mixup, perspektif acak, dan HSV.

### 4. Pelacakan dengan OC-SORT
OC-SORT memperbaiki pelacak berbasis filter Kalman melalui tiga modul: *Observation-Centric Re-Update* (ORU), yang memperbarui parameter filter dengan lintasan virtual setelah objek ditemukan kembali; *Observation-Centric Momentum* (OCM), yang memakai arah gerak dari pengamatan pada matriks biaya; dan *Observation-Centric Recovery* (OCR), yang menambahkan putaran asosiasi kedua berbasis GIoU. Pada percobaan pelacakan, parameter yang dipakai adalah nilai bawaan tiap algoritma.

### 5. Metode penghitungan
Tiga metode dibandingkan. Metode jumlah ID menghitung banyaknya lintasan. SLM menambah hitungan satu bila buah yang dilacak melintasi garis vertikal tengah, dari (540, 0) ke (540, 1920). CRCM menghitung dua kejadian: buah yang masuk ke wilayah penghitungan dari luar menambah hitungan satu, dan buah yang sebelumnya berada di wilayah itu lalu keluar pada bingkai berikutnya menambah hitungan satu. Wilayah CRCM berupa persegi panjang dengan sudut kiri atas (300, 0) dan sudut kanan bawah (780, 1920). Makalah tidak menjelaskan bagaimana buah yang masuk lalu keluar tidak terhitung dua kali, dan hal itu tidak dapat dipastikan dari teks.

## Eksperimen dan Hasil
Tiga eksperimen dijalankan: perbandingan detektor (YOLOv5s, YOLOv5m, YOLOv7-tiny, YOLOv8n, YOLOv8s), perbandingan pelacak berbasis YOLOv8n (OC-SORT, BoT-SORT, ByteTrack, StrongSORT; bagian metode juga menyebut Deep OC-SORT), dan perbandingan metode penghitungan berbasis YOLOv8n dan OC-SORT. Metrik deteksi adalah P, R, F1, mAP, dan ukuran model. Metrik pelacakan adalah HOTA, MOTA, IDF1, dan IDSW. Metrik penghitungan adalah akurasi penghitungan per video dan akurasi rerata.

Tabel 1. Hasil deteksi (Tabel 1 makalah, himpunan uji):

| Model | P (%) | R (%) | F1 (%) | mAP@0,5 (%) | Ukuran (MB) |
|---|---|---|---|---|---|
| YOLOv5s | 81,3 | 79,7 | 80,5 | 86,4 | 14,4 |
| YOLOv5m | 79,9 | 80,6 | 80,3 | 86,5 | 42,5 |
| YOLOv7-tiny | 81,0 | 80,9 | 81,0 | 87,1 | 12,0 |
| YOLOv8n | 80,4 | 80,4 | 80,4 | 86,3 | 6,2 |
| YOLOv8s | 80,4 | 81,2 | 80,8 | 86,9 | 22,5 |

Kinerja deteksi antarmodel serupa, sedangkan ukuran model berbeda jauh. Penulis memilih YOLOv8n karena ukurannya paling kecil dengan kinerja yang sebanding. Pada pembahasan, YOLOv8n dibandingkan pula dengan Faster R-CNN (mAP50 86,7%, mAP50-95 41,1%, 335,3 MB), YOLOv10n (84,3%; 48,4%; 5,7 MB), YOLOv9s (86,0%; 48,5%; 15,2 MB), dan Deformable DETR (85,0%; 44,2%; 524,2 MB), sedangkan YOLOv8n memperoleh mAP50 86,3%, mAP50-95 49,2%, dan 6,2 MB (Tabel 4).

Tabel 2. Hasil pelacakan pada seluruh video uji (Tabel 2 makalah):

| Pelacak | HOTA (%) | MOTA (%) | IDF1 (%) | IDSW | Waktu (ms) |
|---|---|---|---|---|---|
| OC-SORT | 67,103 | 75,874 | 75,618 | 354 | 19,0 |
| BoT-SORT | 64,126 | 74,782 | 71,889 | 716 | 106,6 |
| ByteTrack | 62,396 | 72,429 | 74,644 | 264 | 15,4 |
| StrongSORT | 58,280 | 71,864 | 61,639 | 578 | 87,3 |

OC-SORT unggul pada HOTA, MOTA, dan IDF1. ByteTrack lebih baik pada IDSW dan waktu per bingkai. Pada video 41, selisih ID maksimum terhadap anotasi pada bingkai ke-601 adalah 20 untuk OC-SORT, 35 untuk BoT-SORT, 39 untuk ByteTrack, dan 44 untuk StrongSORT.

Tabel 3. Hasil pelacakan YOLOv8n + OC-SORT per video uji (Tabel 3 makalah):

| Video | Jumlah buah | HOTA (%) | MOTA (%) | IDF1 (%) | IDSW |
|---|---|---|---|---|---|
| 10 | 136 | 65,776 | 78,811 | 81,848 | 12 |
| 21 | 329 | 67,412 | 77,592 | 75,360 | 65 |
| 41 | 203 | 70,081 | 72,808 | 77,969 | 97 |
| 61 | 348 | 63,365 | 72,659 | 71,201 | 128 |
| 90 | 188 | 67,475 | 78,845 | 74,612 | 52 |
| Semua | 1.204 | 67,103 | 75,874 | 75,618 | 354 |

Jumlah buah acuan pada kelima video adalah 1.204. Penulis menyimpulkan bahwa jumlah buah yang banyak dan perekaman menghadap matahari menyulitkan deteksi dan pelacakan.

Penghitungan. Akurasi penghitungan rerata adalah 37,2% untuk jumlah ID, 76,5% untuk SLM, dan 87,0% untuk CRCM. Selisih 49,8 poin persentase terhadap jumlah ID dan 10,5 poin terhadap SLM dihitung dari angka rerata tersebut. Pada video contoh, hitungan jumlah ID mencapai 289 pada bingkai 1774, sedangkan anotasi hanya memuat 157 buah. Akurasi per video hanya disajikan pada Gambar 12 dan tidak terbaca pada teks ekstraksi.

## Kelebihan dan Keterbatasan
Kelebihan menurut makalah: perbandingan sistematis tiga lapisan (detektor, pelacak, penghitung) pada data lapangan nyata; model ringan (6,2 MB) yang diklaim sesuai untuk pemrosesan waktu-nyata; dan CRCM yang mengurangi penghitungan ganda dan penghitungan terlewat.

Keterbatasan yang dinyatakan penulis: jumlah ID sangat tidak akurat pada kebun yang padat, berbuah rapat, dan dengan oklusi berat pada video 60 detik. Kegagalan pelacakan terutama disebabkan buah terlewat dan daun yang dikenali keliru sebagai buah. Kinerja menurun pada perekaman menghadap matahari dan pada jumlah buah banyak. Penulis juga mencatat bahwa pada penelitian terdahulu yang memakai video sekitar 15 detik dan buah jarang, akurasi jumlah ID mencapai 86,19%.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan tambahan. Wilayah dan garis penghitungan memakai koordinat piksel tetap yang bergantung pada arah gerak dan resolusi video, serta tidak dijelaskan bagaimana menyesuaikannya bila arah gerak atau laju kamera berubah. Pengujian hanya memakai lima video dari satu kebun dan satu hari perekaman, tanpa pengulangan, sehingga ketidakpastian statistik tidak dilaporkan. Acuan penghitungan berupa anotasi pada video, bukan hitung panen. Data tersedia hanya atas permintaan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dengan pelacakan multi-objek berbasis deteksi (YOLOv8n dan OC-SORT), kemudian menyaring hitungan dengan aturan wilayah (CRCM). Identitas hanya dipertahankan sepanjang satu lintasan video dari satu sisi baris tanaman. Pencocokan lintas sisi, lintas lintasan, atau lintas pohon tidak ditangani. Hitungan tidak dilaporkan per kelas, karena hanya ada satu kelas "passion fruit". Acuan hitungannya adalah anotasi manual pada video (jumlah buah 1.204 pada lima video uji), bukan hasil panen atau hitung manual di lapangan.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan memisahkan hitungan dari jumlah ID dan data empiris bahwa jumlah ID sangat melebih-lebihkan hitungan pada tumpukan buah rapat (37,2% akurasi). Aturan wilayah tengah juga dapat diadaptasi untuk satu sisi pohon. Namun, metode ini tidak menyelesaikan masalah identitas antar-sisi, yang menjadi pokok tinjauan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `tu2025estimation`.

Tu dkk. mengusulkan alur YOLOv8n, OC-SORT, dan metode penghitungan wilayah tengah (CRCM) untuk memperkirakan hasil markisa dari video ponsel. Pada lima video uji dengan 1.204 buah, CRCM mencapai akurasi penghitungan rerata 87,0%, dibandingkan 76,5% untuk penghitungan garis tunggal dan 37,2% untuk jumlah ID maksimum. YOLOv8n mencapai mAP@0,5 86,3% dan OC-SORT mencapai HOTA 67,103%.

Catatan verifikasi data: Angka deteksi bersumber dari Tabel 1 dan Tabel 4, angka pelacakan dari Tabel 2 dan Tabel 3, dan angka akurasi penghitungan rerata dari seksi 4.6 serta kesimpulan. Akurasi penghitungan per video hanya ada pada Gambar 12 dan tidak dapat diverifikasi dari teks. Kalimat pertama pada seksi 4.6 yang membandingkan CRCM dengan SLM per video menyebut daftar peningkatan (64%, 19,1%, 71,4%, 36,2%, 95,2%) yang tampaknya merujuk pada jumlah ID dan bukan SLM karena kalimat berikutnya mengulang kata SLM, sehingga acuan pembandingnya tidak dapat dipastikan dari teks. Kesimpulan menyebut recall 80,5%, sedangkan Tabel 1 menyebut 80,4%. Makalah tidak melaporkan kultivar markisa, jumlah citra per video, atau waktu pemrosesan per bingkai untuk tahap penghitungan. Teks ekstraksi baik, tetapi nilai gambar tidak terbaca.
