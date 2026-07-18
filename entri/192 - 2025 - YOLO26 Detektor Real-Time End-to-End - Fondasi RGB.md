# 192 - YOLO26: Key Architectural Enhancements and Performance Benchmarking for Real-Time Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sapkota2025yolo26` |
| Judul asli | YOLO26: Key Architectural Enhancements and Performance Benchmarking for Real-Time Object Detection |
| Penulis | Ranjan Sapkota, Rahul Harsha Cheppally, Ajay Sharda, Manoj Karkee |
| Tahun | 2025 |
| Venue | arXiv preprint (arXiv:2509.25164) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2509.25164
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLO26%3A%20Key%20Architectural%20Enhancements%20and%20Performance%20Benchmarking%20for%20Real-Time%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLO26%3A%20Key%20Architectural%20Enhancements%20and%20Performance%20Benchmarking%20for%20Real-Time%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini menelaah YOLO26, detektor objek yang dirilis Ultralytics pada September 2025 dan diposisikan sebagai model "edge-first" — dirancang agar berjalan efisien pada perangkat berdaya komputasi terbatas seperti papan tersemat dan modul kamera pintar. Penulis bukan pengembang model, melainkan kelompok riset independen (Cornell University dan Kansas State University) yang sebelumnya menerbitkan telaah serupa untuk YOLOv10 hingga YOLOv13; makalah ini menganalisis empat perubahan arsitektur utama YOLO26 dan membandingkan kinerjanya dengan generasi YOLO sebelumnya serta detektor berbasis *transformer* (arsitektur jaringan yang mengandalkan mekanisme *attention*, yaitu pembobotan relasi antar-elemen fitur secara global).

Empat perubahan yang dibahas adalah penghapusan *Distribution Focal Loss* (DFL, fungsi kerugian regresi kotak berbasis distribusi probabilitas diskret), inferensi *end-to-end* tanpa *Non-Maximum Suppression* (NMS, tahap pasca-proses yang membuang deteksi tumpang tindih), skema pelatihan ProgLoss dan *Small-Target-Aware Label Assignment* (STAL) untuk objek kecil, serta optimizer baru bernama MuSGD. Menurut dokumentasi resmi Ultralytics yang dirujuk silang dalam telaah ini, YOLO26 varian *nano* (YOLO26n) mencapai 40,9% mAP pada COCO dengan latensi sekitar 1,7 milidetik pada GPU T4 memakai TensorRT, sedangkan varian terbesar (YOLO26x) mencapai 57,5% mAP dengan latensi 11,8 milidetik. Model ini mendukung lima tugas visi dalam satu arsitektur: deteksi, segmentasi instans, estimasi pose, deteksi kotak berorientasi (OBB), dan klasifikasi.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sejak YOLOv10 (bab 009), keluarga YOLO mulai menghilangkan NMS dengan menerapkan penugasan label satu-ke-satu selama pelatihan sehingga jaringan tidak lagi menghasilkan banyak kotak tumpang tindih untuk objek yang sama. Namun, generasi sebelum YOLO26 — termasuk YOLOv11 (bab 010) — masih memakai DFL pada kepala regresi kotak. DFL merepresentasikan setiap sisi kotak pembatas sebagai distribusi probabilitas atas sejumlah nilai diskret, bukan sebagai satu angka kontinu; pendekatan ini meningkatkan presisi lokalisasi tetapi menambah operasi komputasi non-standar (seperti *softmax* dan penjumlahan berbobot) yang sulit dipetakan langsung ke format ekspor edge seperti TensorRT, CoreML, atau TFLite tanpa penyesuaian khusus.

Masalah kedua menyangkut objek kecil. Skema penugasan label task-aligned (TAL) yang lazim dipakai detektor YOLO modern menilai kecocokan antara prediksi dan target berdasarkan kombinasi skor klasifikasi dan IoU (*Intersection over Union*, rasio irisan terhadap gabungan dua kotak). Untuk objek berukuran sangat kecil, wilayah irisan yang mungkin dicapai terbatas, sehingga jumlah kandidat positif yang lolos ambang penugasan sering kali sedikit atau nol, membuat sinyal pelatihan untuk kelas objek kecil lemah. Masalah ketiga adalah kebutuhan satu model tunggal yang melayani beberapa tugas visi pada perangkat tepi tanpa arsitektur terpisah per tugas.

## Ide Utama

Gagasan inti YOLO26 adalah menyederhanakan kepala deteksi hingga seluruh proses inferensi — dari citra masukan sampai daftar kotak akhir — dapat diekspor sebagai satu graf komputasi tanpa operasi pasca-proses eksternal, sambil memperbaiki sinyal pelatihan untuk objek kecil lewat perubahan pada fungsi kerugian dan penugasan label, bukan pada arsitektur *backbone* (jaringan ekstraksi fitur awal). Regresi kotak dikembalikan ke bentuk kontinu langsung (tanpa representasi distribusi DFL), kepala deteksi dilatih agar setiap objek hanya dicocokkan dengan satu prediksi (skema satu-ke-satu, sehingga NMS tidak diperlukan saat inferensi), dan pembobotan kerugian pelatihan digeser secara bertahap ke arah kepala yang dipakai saat inferensi. Optimizer MuSGD menggabungkan mekanisme SGD (*Stochastic Gradient Descent*, penurunan gradien stokastik) konvensional dengan teknik Muon — metode optimisasi yang mengatur arah pembaruan bobot memakai ortogonalisasi matriks gradien, awalnya dikembangkan untuk melatih model bahasa besar — untuk menjaga konvergensi tetap stabil pada arsitektur yang telah disederhanakan.

## Cara Kerja Langkah demi Langkah

### Penghapusan Distribution Focal Loss

Pada YOLO generasi sebelumnya, jarak dari titik acuan ke tiap sisi kotak pembatas diprediksi sebagai distribusi probabilitas atas beberapa *bin* diskret (misalnya 16 nilai), lalu nilai akhir dihitung sebagai ekspektasi (rerata berbobot) distribusi tersebut. YOLO26 mengganti representasi ini dengan regresi langsung — jaringan memprediksi satu nilai kontinu per sisi kotak. Perubahan ini mengurangi jumlah parameter dan operasi pada kepala regresi, sekaligus menghapus kebutuhan operasi *softmax* dan integrasi bobot yang tidak selalu didukung native oleh *runtime* inferensi edge. Menurut telaah ini, rentang regresi tetap tidak dibatasi (*unconstrained*) meski representasi disederhanakan, sehingga kapasitas model untuk memprediksi kotak berukuran ekstrem tidak berkurang.

### Kepala Deteksi Tanpa NMS

Kepala deteksi YOLO26 dilatih dengan penugasan satu-ke-satu: setiap objek kebenaran hanya dipasangkan dengan satu prediksi positif, bukan banyak kandidat seperti pada penugasan satu-ke-banyak yang lazim dipakai bersama NMS. Dengan penugasan ini, jaringan belajar menekan sendiri prediksi berlebih selama pelatihan, sehingga saat inferensi kotak yang dihasilkan sudah tidak tumpang tindih dan tidak memerlukan tahap NMS terpisah. Konsekuensi praktisnya adalah latensi inferensi menjadi tetap (deterministik) — pada NMS konvensional, waktu pemrosesan bergantung pada jumlah kotak kandidat yang harus disaring, yang bervariasi antar-citra.

### ProgLoss dan STAL untuk Objek Kecil

ProgLoss (*Progressive Loss*) mengatur bobot kerugian pelatihan agar bergeser secara bertahap, dari kepala bantu (*auxiliary head*, dipakai saat pelatihan untuk memperkaya sinyal gradien) menuju kepala yang dipakai saat inferensi. Dengan pergeseran bertahap ini, kepala inferensi menerima pengawasan penuh secara berangsur, bukan sejak awal, sehingga pelatihan lebih stabil dibanding bila kedua kepala diberi bobot tetap. STAL (*Small-Target-Aware Label Assignment*) menambahkan aturan pada skema penugasan task-aligned agar setiap objek kecil dijamin memperoleh sedikitnya satu kandidat positif, meski skor IoU-nya di bawah ambang normal. Ilustrasinya: bila objek berukuran 8×8 piksel pada citra 640×640 hanya tumpang tindih penuh dengan satu sel prediksi, penugasan standar berbasis ambang skor gabungan dapat menolaknya karena skornya rendah; STAL memastikan kandidat berskor tertinggi untuk objek itu tetap diberi label positif walau di bawah ambang.

### Optimizer MuSGD

MuSGD adalah optimizer hibrida yang mengombinasikan pembaruan bobot gaya SGD dengan momentum konvensional dan komponen Muon yang mengortogonalisasi arah pembaruan pada lapisan tertentu (umumnya lapisan berbobot matriks besar). Tujuannya menjaga arah langkah optimisasi tetap terarah dan tidak dominan pada satu subruang parameter, sehingga konvergensi lebih stabil terutama ketika kepala deteksi telah disederhanakan (tanpa DFL) dan sinyal gradiennya berbeda karakter dari arsitektur sebelumnya.

Diagram berikut merangkum posisi keempat perubahan pada alur pelatihan-ke-inferensi:

```
PELATIHAN                                  INFERENSI
┌──────────────┐   penugasan 1-ke-1        ┌──────────────┐
│  backbone +   │──────────────────────────▶│  backbone +   │
│  neck (tetap) │   ProgLoss: bobot         │  neck (tetap) │
└──────┬───────┘   bergeser ke head         └──────┬───────┘
       │           inferensi                       │
       ▼                                            ▼
┌──────────────┐   STAL: jamin positif     ┌──────────────┐
│ head regresi  │   untuk objek kecil       │ head regresi  │
│ (tanpa DFL)   │                           │ (tanpa DFL)   │
└──────┬───────┘   optimizer: MuSGD         └──────┬───────┘
       │                                            │
       ▼                                            ▼
  kotak + kelas                              kotak + kelas
  (banyak kandidat,                          (langsung final,
   disaring saat                              tanpa tahap NMS)
   pelatihan)
```

Diagram ini menunjukkan bahwa *backbone* (jaringan ekstraksi fitur) dan *neck* (modul agregasi fitur multi-skala) tidak berubah; perubahan YOLO26 terkonsentrasi pada kepala deteksi dan resep pelatihannya, sehingga bobot model yang sudah ada dari arsitektur YOLO sebelumnya relatif mudah diadaptasi.

## Eksperimen dan Hasil

Telaah ini membandingkan YOLO26 dengan YOLOv8, YOLOv11, YOLOv12, YOLOv13, RT-DETR, dan RF-DETR (bab 193) pada dataset COCO (*Common Objects in Context*, tolok ukur deteksi objek berskala besar dengan 80 kelas) untuk akurasi, serta pada perangkat edge seperti NVIDIA Jetson untuk latensi. Berdasarkan tabel benchmark yang juga dipublikasikan pada dokumentasi resmi Ultralytics dan dirujuk konsisten oleh telaah ini, lima varian ukuran YOLO26 mencapai mAP@50-95 sebagai berikut: nano 40,9%, small 48,6%, medium 53,1%, large 55,0%, dan extra-large 57,5%. Latensi pada GPU T4 dengan TensorRT FP16 berkisar dari 1,7 milidetik (nano) hingga 11,8 milidetik (extra-large). Rentang ini konsisten dengan klaim di ringkasan makalah bahwa YOLO26 mendorong batas Pareto akurasi-latensi (kurva yang menunjukkan tidak ada model lain yang unggul sekaligus di kedua metrik) melampaui YOLO real-time sebelumnya pada rentang ukuran yang sama.

Untuk inferensi CPU, telaah ini melaporkan klaim percepatan hingga 43% pada format ONNX untuk YOLO26n dibandingkan YOLO11n, diukur pada prosesor Intel Xeon 2,00 GHz; angka mentah yang beredar menyebut latensi sekitar 38,9 milidetik untuk YOLO26n berbanding sekitar 56,1 milidetik untuk YOLO11n. Interpretasinya: penghapusan DFL dan penyederhanaan pasca-proses memberi dampak nyata pada perangkat tanpa akselerator GPU, relevan untuk kamera edge atau papan tersemat berbasis CPU. Karena angka ini berasal dari materi yang diterbitkan Ultralytics dan dikutip ulang oleh telaah ini, verifikasi silang ke tabel hasil pasti pada naskah arXiv tetap diperlukan sebelum dipakai sebagai rujukan kuantitatif.

## Kelebihan dan Keterbatasan

Kelebihan utama YOLO26 menurut telaah ini adalah kesederhanaan jalur inferensi: tanpa DFL dan tanpa NMS, seluruh model dapat diekspor sebagai satu graf komputasi tunggal ke format seperti ONNX, TensorRT, CoreML, atau TFLite tanpa operasi kustom tambahan, yang mempermudah penerapan pada kerangka kerja inferensi edge yang dukungan operatornya terbatas. STAL dan ProgLoss menyasar kelemahan spesifik pada objek kecil tanpa mengubah *backbone*, sehingga peningkatan akurasi objek kecil dapat dicapai tanpa menaikkan biaya komputasi utama. Cakupan lima tugas visi dalam satu keluarga arsitektur juga memudahkan penerapan pada sistem yang membutuhkan lebih dari sekadar deteksi kotak, misalnya segmentasi atau estimasi pose pada jalur pemrosesan yang sama.

Dari sisi rekayasa, keterbatasan paling mendasar adalah bahwa makalah ini merupakan telaah/benchmark independen atas model yang dirilis pihak lain (Ultralytics), bukan makalah asli pengembang model; sebagian angka yang dikutip bersumber dari materi rilis dan dokumentasi resmi, sehingga independensi pengukurannya perlu diperiksa lebih lanjut pada naskah lengkap. Secara konseptual, klaim percepatan CPU hingga 43% bergantung pada perangkat keras pengujian spesifik (Intel Xeon 2,00 GHz) dan format ekspor (ONNX); besarnya pada perangkat keras atau format ekspor lain tidak tentu sama. Karena YOLO26 dirilis September 2025, replikasi independen dari kelompok riset lain masih terbatas pada saat makalah ini disusun, sehingga generalisasi hasil ke skenario penerapan lain belum banyak teruji publik.

## Kaitan dengan Bab Lain

YOLO26 melanjutkan garis penghapusan NMS yang dimulai YOLOv10 (bab [009 - 2024 - YOLOv10 - Fondasi RGB](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md)) dan mewarisi struktur multi-tugas dari YOLOv11 (bab [010 - 2024 - YOLOv11 (Overview) - Fondasi RGB](./010%20-%202024%20-%20YOLOv11%20%28Overview%29%20-%20Fondasi%20RGB.md)), dengan tambahan penghapusan DFL dan resep pelatihan baru (ProgLoss, STAL, MuSGD) yang tidak ada pada kedua pendahulunya. Dibandingkan dengan detektor berbasis *transformer* pada klaster yang sama, YOLO26 tetap berbasis konvolusi dan bersaing langsung dengan RF-DETR (bab [193 - 2025 - RF-DETR NAS untuk Detektor Transformer Real-Time - Fondasi RGB](./193%20-%202025%20-%20RF-DETR%20NAS%20untuk%20Detektor%20Transformer%20Real-Time%20-%20Fondasi%20RGB.md)) dan Le-DETR (bab [194 - 2026 - Le-DETR Encoder Efisien untuk DETR Real-Time - Fondasi RGB](./194%20-%202026%20-%20Le-DETR%20Encoder%20Efisien%20untuk%20DETR%20Real-Time%20-%20Fondasi%20RGB.md)) pada kurva akurasi-latensi yang sama, meski ketiganya memakai strategi arsitektur berbeda untuk mencapai inferensi *end-to-end* tanpa NMS. Perbandingan lintas ketiga bab ini relevan bagi pembaca yang menilai trade-off antara detektor berbasis CNN yang telah matang secara ekosistem penerapan (YOLO26) dan detektor berbasis *transformer* yang lebih baru.

## Poin untuk Sitasi

Kutip dengan kunci `sapkota2025yolo26`. Ringkasan yang aman dikutip: "YOLO26 menghapus Distribution Focal Loss dan NMS dari pipeline inferensi, menambahkan ProgLoss serta STAL untuk objek kecil dan optimizer MuSGD, mencapai 40,9-57,5% mAP pada COCO dengan latensi 1,7-11,8 milidetik pada GPU T4 di lima ukuran model." Klaim berikut perlu diverifikasi langsung ke tabel dan teks naskah arXiv sebelum dikutip dalam karya formal: (1) angka mAP dan latensi per varian (nano/small/medium/large/extra-large) yang dalam telaah ini disilangkan dengan dokumentasi resmi Ultralytics, bukan diekstrak langsung dari tabel makalah; (2) klaim percepatan CPU hingga 43% (YOLO26n vs YOLO11n, ONNX, Intel Xeon 2,00 GHz) beserta angka mentah 38,9 ms vs 56,1 ms; (3) rincian afiliasi penulis dan cakupan pembanding penuh (YOLOv8-v13, RT-DETR, RF-DETR) sebagaimana dilaporkan makalah. Karena makalah ini terbit September 2025 dan membahas model yang sama-sama baru, kehati-hatian ekstra diperlukan: pastikan versi arXiv yang dirujuk (naskah mengalami beberapa revisi) sebelum sitasi formal.
