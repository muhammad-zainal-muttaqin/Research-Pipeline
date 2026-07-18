# 200 - AsyncMDE: Real-Time Monocular Depth Estimation via Asynchronous Spatial Memory

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ma2026asyncmde` |
| Judul asli | AsyncMDE: Real-Time Monocular Depth Estimation via Asynchronous Spatial Memory |
| Penulis | Lianjie Ma, Yuquan Li, Bingzheng Jiang, Ziming Zhong, Han Ding, Lijun Zhu |
| Tahun | 2026 |
| Venue | arXiv preprint (arXiv:2603.10438; cs.RO, cs.CV) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (abstrak/PDF gratis):** https://arxiv.org/abs/2603.10438
- **arXiv (HTML lengkap):** https://arxiv.org/html/2603.10438
- **Google Scholar:** https://scholar.google.com/scholar?q=AsyncMDE%3A%20Real-Time%20Monocular%20Depth%20Estimation%20via%20Asynchronous%20Spatial%20Memory

## Gambaran Umum

Makalah ini mengusulkan AsyncMDE, sistem estimasi kedalaman monokular (memperkirakan jarak setiap piksel dari satu citra RGB, tanpa sensor kedalaman) yang dirancang untuk berjalan secara *real-time* pada perangkat robot dengan sumber daya komputasi terbatas. Gagasan intinya adalah memisahkan proses menjadi dua jalur yang berjalan asinkron (tidak serentak, dengan kecepatan berbeda): jalur lambat berupa model fondasi besar dan beku (bobotnya tidak diperbarui) yang menghasilkan fitur spasial berkualitas tinggi secara berkala, dan jalur cepat berupa jaringan ringan yang menggabungkan fitur tersimpan dari jalur lambat dengan observasi citra saat ini untuk menghasilkan kedalaman pada setiap *frame* (bingkai video).

Dengan hanya 3,83 juta parameter yang dapat dilatih pada jalur cepat (di luar 97,5 juta parameter model fondasi yang beku), AsyncMDE mencapai 237 *frame* per detik (FPS) pada GPU RTX 4090 dan memulihkan 77% dari selisih akurasi terhadap model fondasi penuh. Makalah ini merupakan pracetak arXiv yang diunggah Maret 2026 dan direvisi Juni 2026; belum melalui proses tinjauan sejawat pada publikasi resmi mana pun sejauh yang dapat diverifikasi.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Model fondasi (*foundation model*) untuk estimasi kedalaman monokular, seperti Depth Anything V2 (bab 175), menghasilkan peta kedalaman berkualitas tinggi dan bergeneralisasi baik ke domain yang belum pernah dilihat saat pelatihan. Namun, model-model ini berukuran besar — puluhan hingga ratusan juta parameter — sehingga biaya komputasinya tinggi. Pada operasi robot yang kontinu, setiap *frame* video diproses secara independen dari awal (*per-frame inference*), padahal antar-*frame* yang berdekatan waktu terdapat kemiripan pandangan yang besar. Pemrosesan ulang penuh pada setiap *frame* membuang redundansi komputasi ini dan menghambat penerapan pada platform tepi (*edge platform*) seperti unit pemrosesan pada robot bergerak, yang memiliki daya dan memori terbatas.

Pendekatan lain untuk mempercepat estimasi kedalaman video, seperti Video Depth Anything, berupaya menjaga konsistensi temporal (kestabilan nilai kedalaman antar-*frame* berurutan) tetapi umumnya tetap memerlukan komputasi yang berat per *frame*. Persoalan yang belum terpecahkan sebelum makalah ini adalah bagaimana memanfaatkan kualitas model fondasi tanpa menanggung biaya inferensinya pada setiap *frame*, sekaligus mempertahankan akurasi yang mendekati model penuh tersebut.

## Ide Utama

AsyncMDE memisahkan komputasi menjadi jalur lambat (*slow path*) dan jalur cepat (*fast path*) yang berjalan pada kecepatan berbeda. Jalur lambat adalah model fondasi Depth Anything V2 varian ViT-B (*Vision Transformer* ukuran *Base*, 97,5 juta parameter) yang dibekukan — bobotnya tidak diubah selama pelatihan AsyncMDE. Jalur lambat ini dijalankan hanya secara berkala, menghasilkan fitur spasial multi-skala berkualitas tinggi yang disimpan sebagai memori.

Jalur cepat adalah jaringan ringan (3,83 juta parameter) yang berjalan pada setiap *frame*. Pada setiap langkah waktu, jalur cepat mengambil fitur dari memori tersimpan (hasil jalur lambat pada saat terakhir dijalankan) dan menggabungkannya dengan observasi citra saat ini melalui mekanisme yang disebut *complementary fusion* (fusi saling melengkapi). Hasil fusi ini dipakai untuk memprediksi kedalaman *frame* tersebut sekaligus diperbarui menjadi memori untuk *frame* berikutnya — sebuah proses yang disebut pembaruan memori autoregresif (*autoregressive memory update*), yaitu keluaran pada satu langkah menjadi masukan langkah berikutnya. Dengan skema ini, biaya komputasi model fondasi ditanggung (*amortized*) di sepanjang banyak *frame*, bukan dipikul penuh pada setiap *frame*.

## Cara Kerja Langkah demi Langkah

### Jalur Lambat: Model Fondasi Beku

Jalur lambat memakai Depth Anything V2 ViT-B sebagai penghasil fitur spasial. Model ini dijalankan pada interval penyegaran (*refresh interval*) tertentu, bukan pada setiap *frame*, dan hasilnya diinisialisasi serta disegarkan sebagai memori spasial multi-skala, dilambangkan M_t^(ℓ) untuk skala fitur ke-ℓ pada waktu t. Karena berjalan jarang, jalur lambat berkontribusi kecil terhadap beban komputasi rata-rata meskipun ukurannya besar (97,5 juta parameter, berjalan sekitar 60 Hz bila dipanggil sendiri).

### Jalur Cepat: Jaringan Ringan

Jalur cepat terdiri atas tiga komponen. Pertama, penyandi (*encoder*) berbasis MobileNetV3-Small (0,93 juta parameter), arsitektur konvolusi ringan yang dirancang untuk perangkat bersumber daya terbatas, menghasilkan fitur multi-skala dari citra masukan saat ini. Kedua, proyektor fitur (*feature projector*) berupa konvolusi 1×1 untuk menyelaraskan jumlah kanal antara fitur penyandi ringan dan fitur memori dari model fondasi, diikuti interpolasi bilinear untuk menyamakan resolusi spasial. Ketiga, penyahsandi (*decoder*) yang mewarisi arsitektur RefineNet beserta bobot awal dari kepala DPT (*Dense Prediction Transformer*, kepala prediksi padat) milik model fondasi, berukuran 2,52 juta parameter.

### Fusi Saling Melengkapi (Complementary Fusion)

Penggabungan memori dan observasi baru dirumuskan sebagai kombinasi cembung (*convex combination*) per piksel:

```
O = T * M + (1 - T) * F
```

O adalah fitur gabungan, M adalah fitur memori tersimpan dari jalur lambat, F adalah fitur baru dari penyandi jalur cepat, dan T adalah faktor modulasi spasial bernilai antara 0 dan 1 untuk setiap lokasi piksel. Saat T mendekati 1, sistem mempertahankan memori lama, misalnya pada wilayah statis seperti dinding ruangan indoor, sehingga fitur berkualitas tinggi dari model fondasi terus dipakai tanpa pemrosesan ulang; saat T mendekati 0, sistem menyerap observasi baru, misalnya pada tepi objek yang bergerak akibat gerakan kamera atau objek itu sendiri.

### Pembaruan Memori Autoregresif

Setelah fusi, hasil O pada waktu t langsung menjadi memori untuk waktu t+1: M_{t+1}^(ℓ) = O_t^(ℓ). Karena memori terus diperbarui dari hasil fusi sebelumnya tanpa pemanggilan ulang model fondasi, kualitas memori berdegradasi secara bertahap mengikuti hasil kali faktor modulasi pada seluruh langkah sejak penyegaran terakhir, dinyatakan sebagai perkalian berantai ∏ T_s. Degradasi ini bersifat terbatas (*bounded*) dan dapat diprediksi, sehingga sistem menyegarkan memori dari jalur lambat secara berkala untuk mencegah akumulasi galat yang tidak terkendali.

Alur data antara kedua jalur dapat diringkas sebagai berikut:

```
frame ke-t (RGB)
      │
      ├──> [jalur cepat: MobileNetV3-Small] ─> fitur baru F
      │                                             │
[jalur lambat: DAv2-ViTB]                           │
   (berjalan periodik)                              │
      │                                             │
      └──> memori M_t ──────> fusi O = T*M+(1-T)*F ─┘
                                     │
                          ├─> kedalaman frame t (decoder RefineNet/DPT)
                          └─> M_{t+1} = O_t  (memori frame berikutnya)
```

Diagram ini menunjukkan bahwa hanya jalur cepat dan operasi fusi yang dijalankan pada setiap *frame*; jalur lambat cukup dipanggil pada interval penyegaran memori.

## Eksperimen dan Hasil

Model dilatih pada gabungan data NYUv2 (sekitar 155 ribu *frame* indoor), TartanAir (sekitar 112 ribu *frame* simulasi robot), dan BridgeData V2 (sekitar 387 ribu *frame* manipulasi robot). Evaluasi dilakukan pada tiga tolok ukur: ScanNet (100 skena indoor, 43.600 *frame*, kondisi statis), Bonn (14 skena indoor dinamis, 2.850 *frame*), dan Sintel (23 sekuens sintetis, 1.064 *frame*, mengandung gerakan ekstrem). Metrik utama adalah δ₁ (persentase piksel dengan galat relatif di bawah ambang 1,25 — makin tinggi makin baik) dan AbsRel (*Absolute Relative error*, rata-rata galat relatif terhadap kedalaman sebenarnya — makin rendah makin baik).

Pembanding utama adalah Depth Anything V2 pada tiga ukuran (ViT-L, ViT-B, ViT-S), LiteMono (jaringan kedalaman ringan), Video Depth Anything (VDA, metode kedalaman video konsisten), dan CUT3R. Hasil kunci menempatkan DAv2-ViTB sebagai model fondasi acuan dengan δ₁ sebesar 0,983 (ScanNet), 0,979 (Bonn), dan 0,733 (Sintel) pada 60,1 FPS. AsyncMDE mencapai δ₁ sebesar 0,968 (ScanNet), 0,969 (Bonn), dan 0,640 (Sintel) pada 237 FPS — kecepatan hampir empat kali lipat DAv2-ViTB dengan penurunan δ₁ berkisar 1–9 poin, tergantung tingkat dinamika skena. Sebagai pembanding tambahan, LiteMono yang berukuran serupa dengan jalur cepat AsyncMDE (3,07 juta parameter, 238 FPS) hanya mencapai δ₁ 0,851 (ScanNet), 0,854 (Bonn), dan 0,502 (Sintel) — jauh di bawah AsyncMDE meskipun kecepatannya setara. Interpretasinya: pada kecepatan yang sama, memanfaatkan memori dari model fondasi memberi keunggulan akurasi besar dibandingkan jaringan ringan yang dilatih tanpa akses ke fitur model besar.

Dari sisi galat absolut, AbsRel AsyncMDE adalah 0,057 (ScanNet), 0,058 (Bonn), dan 0,287 (Sintel), dibandingkan 0,040, 0,050, dan 0,222 pada DAv2-ViTB. Selisih terbesar terjadi pada Sintel, tolok ukur dengan gerakan ekstrem, sesuai dengan mekanisme fusi yang bergantung pada kestabilan memori antar-*frame*. Pada perangkat tepi Jetson AGX Orin dengan optimasi TensorRT format presisi rendah FP16, jalur cepat mencapai 161 FPS dengan latensi 6,2 milidetik, atau percepatan 13,1 kali lipat dibandingkan DAv2-ViTB pada perangkat yang sama.

Studi ablasi (pengujian pengaruh tiap komponen dengan menghapus atau menggantinya) menunjukkan dua temuan. Pertama, penyandi jalur cepat yang lebih besar tidak selalu menguntungkan: MobileNetV3-Small memberi AbsRel terbaik (0,057), sedangkan penyandi lebih besar seperti EViT-B1 memperburuk AbsRel sekitar 12%, karena fitur observasi baru yang dominan menimpa memori berkualitas tinggi secara berlebihan. Kedua, jalur cepat tanpa memori (*FastPath-Only*) hanya mencapai AbsRel 0,132 pada ScanNet, sedangkan penambahan gerbang semantik dari fitur lapisan dalam model fondasi (*DAv2 L4 Only*) menurunkannya ke 0,057, setara dengan modul memori spasial lengkap (*SMU* dua skala) — menunjukkan bahwa fitur semantik model fondasi menyumbang sebagian besar manfaat mekanisme memori, sedangkan informasi tekstur memberi perbaikan marginal.

## Kelebihan dan Keterbatasan

Kelebihan AsyncMDE terletak pada rasio akurasi terhadap kecepatan: dengan parameter terlatih yang jauh lebih kecil daripada model fondasi (3,83 juta berbanding 97,5 juta), sistem memulihkan sebagian besar akurasi model besar sambil berjalan hampir empat kali lebih cepat pada GPU kelas atas dan lebih dari sepuluh kali lebih cepat pada perangkat tepi. Desain memisahkan jalur lambat dan cepat juga bersifat modular — bobot penyahsandi jalur cepat diwarisi dari kepala DPT model fondasi, sehingga proses pelatihan tidak dimulai dari nol.

Keterbatasan yang diakui penulis meliputi dua hal. Pertama, pada gerakan skena berskala besar yang membatalkan sebagian besar isi memori, sistem harus jatuh kembali ke inferensi penyandi mandiri, mencapai batas bawah kinerja dari prior kontinuitas temporal — kondisi ini konsisten dengan penurunan akurasi terbesar yang teramati pada tolok ukur Sintel. Kedua, keluaran sistem berupa kedalaman relatif tanpa batasan skala metrik antar-*frame*; untuk aplikasi yang membutuhkan kedalaman absolut, seperti navigasi robot, penulis menyatakan diperlukan modul penyelarasan skala temporal tambahan. Dari sisi rekayasa, ketergantungan pada interval penyegaran memori yang tetap berarti parameter ini kemungkinan perlu disetel sesuai karakteristik gerakan skena target, sebuah aspek yang tidak dibahas secara mendalam pada studi ablasi yang dipublikasikan.

## Kaitan dengan Bab Lain

AsyncMDE memakai Depth Anything V2 (bab 175) langsung sebagai model fondasi jalur lambatnya, menjadikan bab ini pewaris langsung dari kapabilitas generalisasi bab tersebut, dengan kontribusi baru berupa skema amortisasi komputasi lintas *frame*. Berbeda dari ZoeDepth (bab 176) dan Metric3D (bab 177), yang berfokus pada penyediaan skala metrik absolut dari citra tunggal, AsyncMDE mengeluarkan kedalaman relatif dan secara eksplisit menyatakan penyelarasan skala metrik sebagai kerja lanjutan, sehingga ketiga bab tersebut saling melengkapi dari sisi tujuan akhir. Survei estimasi kedalaman metrik monokular (bab 199) memberi kerangka klasifikasi metode-metode ini secara lebih luas dan dapat dipakai untuk menempatkan posisi AsyncMDE relatif terhadap pendekatan lain. Bab 201 (UniDAC) dan bab 202 (Focusable Monocular Depth Estimation), sama-sama makalah tahun 2026, berbagi konteks tren yang sama yaitu adaptasi model kedalaman fondasi untuk kondisi penerapan spesifik — UniDAC untuk keragaman kamera, Focusable MDE untuk kontrol area perhatian, dan AsyncMDE untuk kendala waktu nyata pada robot bergerak.

## Poin untuk Sitasi

Kutip dengan kunci `ma2026asyncmde`. Ringkasan yang aman dikutip: "AsyncMDE mengamortisasi biaya komputasi model fondasi kedalaman (Depth Anything V2 ViT-B, 97,5 juta parameter) lewat jalur cepat beparameter 3,83 juta yang menggabungkan memori spasial periodik dengan observasi saat ini, mencapai 237 FPS pada RTX 4090 dan memulihkan 77% selisih akurasi terhadap model fondasi." Angka δ₁ (0,968/0,969/0,640 pada ScanNet/Bonn/Sintel), AbsRel (0,057/0,058/0,287), kecepatan 161 FPS pada Jetson AGX Orin, dan hasil ablasi (penurunan AbsRel 12% pada penyandi EViT-B1) diambil dari versi HTML arXiv (revisi Juni 2026) dan sebaiknya dicocokkan ulang dengan versi PDF final sebelum dikutip dalam karya formal, mengingat status makalah masih pracetak yang belum ditinjau sejawat.
