# 194 - Le-DETR: Revisiting Real-Time Detection Transformer with Efficient Encoder Design

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `huang2026ledetr` |
| Judul asli | Le-DETR: Revisiting Real-Time Detection Transformer with Efficient Encoder Design |
| Penulis | Jiannan Huang, Aditya Kane, Fengzhe Zhou, Yunchao Wei, Humphrey Shi |
| Tahun | 2026 |
| Venue | arXiv preprint (arXiv:2602.21010) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2602.21010
- **Google Scholar:** https://scholar.google.com/scholar?q=Le-DETR%3A%20Revisiting%20Real-Time%20Detection%20Transformer%20with%20Efficient%20Encoder%20Design
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Le-DETR%3A%20Revisiting%20Real-Time%20Detection%20Transformer%20with%20Efficient%20Encoder%20Design&sort=relevance

## Gambaran Umum

Le-DETR meninjau ulang arsitektur *DETR* (*Detection Transformer*, detektor objek berbasis *transformer* yang memprediksi kotak dan kelas secara langsung tanpa pasca-pemrosesan *Non-Maximum Suppression*/NMS) *real-time* dengan menyoroti biaya pra-pelatihan *backbone* (jaringan ekstraksi fitur di awal detektor) sebagai hambatan yang selama ini tersembunyi di balik angka akurasi. Penulis mempertanyakan apakah kebutuhan data pra-pelatihan yang sangat besar pada RT-DETRv2 dan turunannya merupakan keharusan fundamental atau sekadar kompensasi atas desain arsitektur yang belum optimal. Untuk menjawabnya, makalah ini mengusulkan *backbone* baru bernama EfficientNAT dan modul *encoder* (penyandi fitur multi-skala) baru bernama NAIFI, keduanya dibangun di atas *neighborhood attention* (perhatian bertetangga, mekanisme atensi yang dibatasi pada jendela spasial lokal).

Hasilnya, Le-DETR mencapai status baru dalam trade-off akurasi-latensi pada deteksi *real-time*: varian M/L/X memperoleh 52,9/54,3/55,1 *mean Average Precision* (mAP, rata-rata presisi lintas kelas dan ambang IoU) pada COCO Val2017 dengan latensi 4,45/5,01/6,68 milidetik pada GPU RTX 4090, sekaligus memangkas sekitar 80% volume citra pra-pelatihan dibandingkan RT-DETRv2. Makalah ini melanjutkan garis RT-DETR (bab 155) dan bersaing langsung dengan D-FINE serta DEIM, dengan kontribusi yang difokuskan pada efisiensi *backbone* dan *encoder*, bukan pada kepala prediksi atau strategi pencocokan label.

## Latar Belakang: Masalah yang Ingin Dipecahkan

RT-DETR (bab 155) membuktikan bahwa detektor berbasis *transformer* dapat menandingi kecepatan YOLO dengan memisahkan interaksi fitur intra-skala berbasis atensi (AIFI) dari fusi fitur lintas-skala berbasis konvolusi (CCFF) di dalam *hybrid encoder*-nya. Pengembangan lanjutan seperti RT-DETRv2 mempertahankan formula ini tetapi menaikkan akurasi dengan menambah beban pra-pelatihan *backbone*: menurut penulis Le-DETR, RT-DETRv2 memerlukan sekitar empat juta citra tambahan — kira-kira empat kali ukuran ImageNet-1K — beserta jadwal distilasi pengetahuan (*knowledge distillation*, proses mentransfer kemampuan model besar ke model kecil) sebelum disetel halus pada COCO. Kebutuhan data dan komputasi sebesar ini menyulitkan reproduksi hasil dari nol.

Masalah kedua bersumber dari komponen atensi global pada *encoder* DETR standar. Operasi *self-attention* (atensi-diri, mekanisme yang membobot relasi setiap elemen fitur terhadap seluruh elemen lain) memiliki kompleksitas kuadratik terhadap jumlah piksel fitur, sehingga menjadi bagian termahal pada model DETR multi-skala seperti Deformable DETR. RT-DETR menekan biaya ini dengan membatasi atensi hanya pada peta fitur beresolusi terendah, tetapi pembatasan itu berarti interaksi fitur pada skala lain sepenuhnya bergantung pada konvolusi, yang jangkauan reseptifnya lebih terbatas. Le-DETR memosisikan diri untuk menjawab dua masalah ini sekaligus: menekan biaya pra-pelatihan *backbone* dan memperbaiki cara *encoder* memproses fitur multi-skala.

## Ide Utama

Gagasan inti Le-DETR adalah mengganti komponen berbiaya tinggi pada *backbone* dan *encoder* DETR dengan *neighborhood attention* (NA) — bentuk atensi yang hanya dihitung antara setiap elemen fitur dan tetangga spasialnya dalam jendela berukuran tetap, bukan terhadap seluruh peta fitur. Dengan membatasi jangkauan atensi, kompleksitas komputasi turun dari kuadratik penuh menjadi bergantung pada ukuran jendela lokal, sementara struktur spasial lokal tetap terjaga lebih baik daripada bila hanya mengandalkan konvolusi.

Prinsip ini diterapkan pada dua tempat. Pertama, pada *backbone* baru EfficientNAT, blok NA dipadukan dengan *MBConv* (*Mobile Inverted Bottleneck Convolution*, blok konvolusi efisien yang memperluas lalu menyempitkan jumlah kanal fitur) sebagai jaringan umpan-maju (*feed-forward network*), menghasilkan ekstraktor fitur yang menggabungkan efisiensi konvolusi modern dengan jangkauan atensi lokal. Kedua, pada *encoder*, modul AIFI milik RT-DETR — yang memakai atensi global penuh pada satu skala fitur — digantikan oleh modul baru bernama NAIFI yang memakai atensi bertetangga pada satu lapis transformer tunggal. Perubahan ini menekan waktu proses *encoder* sekaligus mempertahankan interaksi fitur yang relevan secara spasial.

## Cara Kerja Langkah demi Langkah

### Backbone EfficientNAT

EfficientNAT disusun berjenjang menjadi beberapa tahap dengan strategi berbeda sesuai kedalamannya. Bagian awal (*stem*) memakai konvolusi terpisah-mendalam (*depthwise separable convolution*, konvolusi yang memisahkan pemrosesan spasial dan pemrosesan kanal untuk menekan jumlah parameter). Dua tahap awal memakai *Fused-MBConv* (varian MBConv yang menggabungkan konvolusi ekspansi dan konvolusi utama menjadi satu operasi agar lebih cepat pada perangkat keras modern), sedangkan tahap yang lebih dalam memakai MBConv standar. Tahap terakhir memakai downsampling berbasis konvolusi mobile diikuti oleh serangkaian blok EfficientNAT, yaitu blok yang memadukan *neighborhood attention* dengan MBConv sebagai FFN. Susunan ini menempatkan komputasi murah (konvolusi) pada resolusi tinggi di awal jaringan, dan komputasi atensi yang lebih mahal pada resolusi rendah di tahap akhir.

Ukuran jendela atensi bertetangga (*kernel size*) konsisten pada nilai 63 di seluruh varian M, L, dan X. Ablasi arsitektur *backbone* menunjukkan dua pola penataan blok yang optimal berbeda menurut ukuran model: susunan blok seimbang (pola PA) lebih baik untuk skala L, sedangkan susunan yang menumpuk beban komputasi pada tahap awal (pola PC) lebih baik untuk skala X.

### Encoder NAIFI

Diagram berikut merangkum posisi NAIFI dalam alur data Le-DETR, dibandingkan dengan AIFI pada RT-DETR:

```
RT-DETR:  backbone -> S3,S4,S5 -> AIFI (atensi global,
                                    hanya skala S5) -> CCFF -> decoder
Le-DETR:  EfficientNAT -> S3,S4,S5 -> NAIFI (atensi
                                   bertetangga, 1 lapis) -> fusi -> decoder
```

NAIFI (*Neighborhood Attention-based Improved Feature Inference*) menggantikan modul AIFI RT-DETR dengan satu lapis transformer atensi bertetangga. Jika AIFI menghitung atensi global penuh pada peta fitur skala tertinggi (S5, beresolusi paling rendah namun paling kaya makna semantik), NAIFI membatasi jangkauan atensi pada jendela lokal berukuran tetap, sehingga biaya komputasinya lebih rendah tanpa kehilangan interaksi fitur pada wilayah yang relevan secara spasial. Modul ini dipadukan dengan komponen fusi fitur agar tetap kompatibel dengan struktur *hybrid encoder* multi-skala yang diwariskan dari RT-DETR. Pada *decoder*, Le-DETR memakai *Flash Attention* (implementasi atensi yang dioptimalkan pada tingkat memori GPU) untuk mempercepat lapisan perhatian-silang tanpa mengubah rumusan matematisnya.

### Skema Pelatihan

Pelatihan Le-DETR terdiri atas dua tahap. Pra-pelatihan pada ImageNet-1K berjalan 300 *epoch* (satu putaran penuh atas data pelatihan) dengan penjadwalan laju belajar kosinus, ukuran *batch* 128 per GPU, laju belajar dasar 1e-3, dan pengoptimal AdamW. Tahap kedua menyetel halus (*fine-tuning*) pada COCO selama 80 *epoch* dengan ukuran *batch* total 64 dan laju belajar dasar 1,25e-4. Konfigurasi *encoder* memakai satu lapis (sesuai desain NAIFI satu-lapis), sedangkan *decoder* memakai 6 lapis saat pelatihan, dengan 100 token *denoising* dan 300 kueri objek. Fungsi *loss* menggabungkan *Varifocal Loss* (VFL, untuk klasifikasi), regresi kotak, dan *Generalized IoU* (GIoU); rincian bobot masing-masing komponen tidak dikutip di sini dan perlu diverifikasi ke naskah asli.

Klaim efisiensi pra-pelatihan yang menjadi salah satu kontribusi utama makalah adalah pengurangan sekitar 80% volume citra pra-pelatihan dibandingkan RT-DETRv2, karena Le-DETR hanya memakai ImageNet-1K standar tanpa data tambahan maupun distilasi pengetahuan berjenjang.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada COCO Val2017, tolok ukur standar deteksi objek, dengan metrik mAP dan latensi inferensi yang diukur pada GPU RTX 4090. Tiga varian dilaporkan: Le-DETR-M mencapai 52,9 mAP dengan 31,4 juta parameter, 114,1 GFLOPs (miliar operasi titik-mengambang, ukuran biaya komputasi), dan latensi 4,45 milidetik; Le-DETR-L mencapai 54,3 mAP dengan 41,5 juta parameter, 124,3 GFLOPs, dan latensi 5,01 milidetik; Le-DETR-X mencapai 55,1 mAP dengan 44,9 juta parameter, 196,9 GFLOPs, dan latensi 6,68 milidetik.

Dibandingkan RT-DETRv2-L (53,4 mAP, 5,46 ms), Le-DETR-L unggul 0,9 poin mAP sekaligus sekitar 9% lebih cepat — perbaikan pada kedua sumbu trade-off sekaligus, bukan hanya salah satunya. Dibandingkan YOLOv12-L (53,7 mAP, 4,89 ms, 26,4 juta parameter), Le-DETR-L unggul akurasi tetapi dengan latensi dan jumlah parameter lebih besar, konsisten dengan pola umum bahwa detektor berbasis *transformer* masih membawa biaya komputasi lebih tinggi per titik akurasi dibandingkan YOLO pada skala sebanding. Terhadap DEIM-D-FINE-M (52,7 mAP), Le-DETR-M unggul tipis 0,2 poin mAP dengan latensi sebanding (4,39 ms berbanding 4,45 ms).

Studi ablasi menunjukkan kontribusi masing-masing komponen. Mengganti *backbone* EfficientNAT dengan ResNet50-vd-ssld (varian ResNet-50 yang dilatih dengan distilasi tambahan) menurunkan mAP dari 54,3 menjadi 53,6 sekaligus menaikkan latensi dari 5,01 menjadi 5,80 milidetik, menunjukkan bahwa EfficientNAT menyumbang baik pada akurasi maupun kecepatan. Mengganti NAIFI dengan AIFI asli menurunkan mAP dari 54,3 menjadi 54,1 dan menaikkan latensi dari 5,01 menjadi 5,18 milidetik — perbaikan lebih kecil dibandingkan kontribusi *backbone*, tetapi arahnya konsisten. Memakai 5 lapisan *decoder* saat inferensi (satu lebih sedikit dari saat pelatihan) mempercepat inferensi 0,26 milidetik tanpa penurunan akurasi yang tercatat.

## Kelebihan dan Keterbatasan

Kelebihan utama Le-DETR terletak pada penekanan biaya pra-pelatihan tanpa mengorbankan posisi kompetitif pada trade-off akurasi-latensi COCO. Pendekatan mengganti atensi global dengan atensi bertetangga pada dua titik arsitektur (*backbone* dan *encoder*) memberi bukti ablasi yang cukup rinci mengenai sumber perbaikan, bukan sekadar klaim agregat. Dari sisi rekayasa, penataan tahap *backbone* yang mencampur konvolusi murah di resolusi tinggi dan atensi lokal di resolusi rendah adalah pola desain yang wajar mengingat biaya atensi meningkat tajam pada resolusi spasial besar.

Keterbatasan yang diakui penulis sendiri ada dua. Pertama, meski volume data pra-pelatihan turun sekitar 80% dibandingkan RT-DETRv2, Le-DETR tetap memerlukan pra-pelatihan ImageNet-1K, sedangkan model YOLO umumnya dapat dilatih dari nol langsung pada COCO. Kedua, dukungan ekspor *neighborhood attention* ke format deployment seperti ONNX dan TensorRT belum matang, sehingga penerapan praktis pada jalur produksi tertentu dapat terhambat sampai kerangka kerja tersebut menambah dukungan native untuk operasi ini. Dari sisi konseptual, keunggulan Le-DETR dibandingkan DEIM-D-FINE tampak tidak konsisten pada seluruh skala berdasarkan angka yang berhasil diverifikasi (lihat Poin untuk Sitasi); klaim keunggulan menyeluruh atas seluruh varian pembanding sebaiknya diperiksa ulang terhadap tabel lengkap naskah asli.

## Kaitan dengan Bab Lain

Le-DETR mewarisi kerangka *hybrid encoder* dari RT-DETR (bab 155): pemisahan interaksi fitur intra-skala dari fusi lintas-skala tetap dipertahankan, tetapi komponen atensi intra-skala (AIFI) diganti NAIFI berbasis atensi bertetangga. Silsilah ini menempatkan Le-DETR sebagai penerus garis efisiensi *encoder* yang juga digarap Co-DETR (bab 165) dari sudut pandang berbeda — Co-DETR menambah cabang pelatihan kolaboratif untuk mempercepat konvergensi, sedangkan Le-DETR menekan biaya komputasi *backbone* dan *encoder* itu sendiri. Le-DETR juga sejalan dengan RF-DETR (bab 193), yang memakai pencarian arsitektur (*Neural Architecture Search*) untuk menemukan konfigurasi DETR *real-time* optimal; keduanya berbagi tujuan menekan biaya arsitektural DETR, tetapi RF-DETR mengandalkan pencarian otomatis sedangkan Le-DETR mengandalkan desain manual berbasis atensi bertetangga.

Sebagai pembanding lintas paradigma, Le-DETR diuji langsung terhadap YOLO26 (bab 192) dan seri YOLOv12 pada tabel hasil COCO yang sama, menegaskan posisi keluarga DETR *real-time* sebagai pesaing langsung YOLO pada rezim latensi rendah — tema yang pertama kali diangkat RT-DETR pada bab 155.

- [155 - 2024 - RT-DETR - Fondasi RGB](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md)
- [165 - 2023 - Co-DETR - Fondasi RGB](./165%20-%202023%20-%20Co-DETR%20-%20Fondasi%20RGB.md)
- [192 - 2025 - YOLO26 Detektor Real-Time End-to-End - Fondasi RGB](./192%20-%202025%20-%20YOLO26%20Detektor%20Real-Time%20End-to-End%20-%20Fondasi%20RGB.md)
- [193 - 2025 - RF-DETR NAS untuk Detektor Transformer Real-Time - Fondasi RGB](./193%20-%202025%20-%20RF-DETR%20NAS%20untuk%20Detektor%20Transformer%20Real-Time%20-%20Fondasi%20RGB.md)

## Poin untuk Sitasi

Kutip dengan kunci `huang2026ledetr`. Ringkasan yang aman dikutip: "Le-DETR mengganti *backbone* dan *encoder* DETR *real-time* dengan komponen berbasis *neighborhood attention* (EfficientNAT dan NAIFI), mencapai 52,9/54,3/55,1 mAP pada COCO Val2017 dengan latensi 4,45/5,01/6,68 milidetik pada RTX 4090, sekaligus memangkas sekitar 80% volume data pra-pelatihan dibandingkan RT-DETRv2." Angka mAP, latensi, parameter, dan GFLOPs pada bagian Eksperimen berasal dari versi HTML arXiv (2602.21010v1) yang berhasil diakses, sehingga secara umum lebih dapat dipercaya daripada parafrase murni.

Namun, dua hal berikut perlu diverifikasi ulang langsung ke naskah PDF/versi final sebelum sitasi formal: (1) klaim perbandingan "Le-DETR-L mengungguli DEIM-D-FINE-L sebesar 0,4 mAP" yang muncul pada satu sumber ringkasan bertentangan dengan tabel angka yang sama (DEIM-D-FINE-L tercatat 54,7 mAP, lebih tinggi dari Le-DETR-L 54,3 mAP) — narasi di atas hanya memakai perbandingan Le-DETR-M vs DEIM-D-FINE-M yang konsisten pada kedua sumber; (2) makalah ini terindikasi juga muncul pada CVPR 2026 (ditemukan tautan openaccess.thecvf.com), tetapi venue akhir belum terkonfirmasi langsung dari halaman arXiv resmi sehingga tabel Metadata tetap mencantumkan arXiv sebagai venue sampai dikonfirmasi. Rincian bobot fungsi *loss* dan detail lengkap tabel ablasi juga sebaiknya dicek ulang ke naskah karena hanya dikutip sebagian di sini.
