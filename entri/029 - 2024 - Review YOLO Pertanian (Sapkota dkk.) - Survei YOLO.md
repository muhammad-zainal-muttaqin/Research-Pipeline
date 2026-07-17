# 029 - YOLOv1 to YOLOv10: A Comprehensive Review of YOLO Variants and Their Application in the Agricultural Domain

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sapkota2024yoloagri` |
| Judul asli | YOLOv1 to YOLOv10: A Comprehensive Review of YOLO Variants and Their Application in the Agricultural Domain |
| Penulis | Mujadded Al Rabbani Alif, Muhammad Hussain (sesuai naskah arXiv:2406.10139; entri `references.bib` mencantumkan nama lain — lihat Poin untuk Sitasi) |
| Tahun | 2024 |
| Venue | arXiv preprint arXiv:2406.10139 |
| Tema | Survei YOLO |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2406.10139
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOv1%20to%20YOLOv10%3A%20A%20Comprehensive%20Review%20of%20YOLO%20Variants%20and%20Their%20Application%20in%20the%20Agricultural%20Domain
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOv1%20to%20YOLOv10%3A%20A%20Comprehensive%20Review%20of%20YOLO%20Variants%20and%20Their%20Application%20in%20the%20Agricultural%20Domain&sort=relevance

## Gambaran Umum

Makalah ini adalah survei — sintesis atas banyak studi yang sudah terbit, bukan metode baru — yang membahas dua arus literatur sekaligus: evolusi keluarga detektor objek YOLO dari YOLOv1 (2015) hingga YOLOv10 (2024), dan penerapan versi-versi tersebut di domain pertanian. Menurut abstraknya, survei ini termasuk yang pertama memasukkan YOLOv10. Lima tujuan dinyatakan eksplisit, dari penelusuran kemajuan tiap versi sampai proyeksi tren berikutnya.

Hasilnya peta dua sumbu: garis waktu inovasi sepuluh versi YOLO dan taksonomi lima bidang aplikasi pertanian (deteksi gulma, deteksi tanaman, pelacakan hewan, deteksi penyakit, pertanian presisi), ditutup analisis komparatif, empat tantangan lapangan, dan empat arah riset lanjutan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sejak YOLOv1 (bab 001) merumuskan deteksi objek sebagai regresi satu kali evaluasi, keluarga YOLO berganti versi hampir setiap tahun; sampai 2024 terdapat sepuluh versi arus utama. Pada saat yang sama, komunitas pertanian mengadopsi YOLO untuk deteksi gulma (tumbuhan liar pesaing tanaman budidaya), identifikasi buah, dan diagnosis penyakit daun, karena sifat *real-time*-nya cocok untuk robot lapangan.

Masalahnya, literatur penerapan itu terfragmentasi: setiap studi memakai versi berbeda, dataset sempit (satu komoditas, satu wilayah), dan metrik tidak seragam, sehingga praktisi sukar memilih versi untuk tugas tertentu. Kondisi lapangan juga berbeda dari tolok ukur seperti MS COCO: objek kecil (gulma muda, serangga), oklusi (buah tertutup daun), dan variasi cahaya menuntut kemampuan khusus. Survei YOLO sebelumnya (mis. bab 028) bersifat umum dan belum memetakan versi ke tugas pertanian, apalagi memasukkan YOLOv9/v10 (2024). Celah itulah yang diisi makalah ini.

## Ide Utama

Gagasan inti survei ini adalah memperlakukan hubungan YOLO dan pertanian sebagai masalah pemetaan dua sumbu: evolusi teknis tiap versi (apa yang diubah dan masalah apa yang dipecahkannya) dipertemukan dengan kebutuhan aplikasi (tugas apa yang telah dicoba dan dengan hasil apa). Dengan begitu, kekuatan dan kelemahan tiap versi dinilai terhadap tuntutan tugas lapangan, bukan terhadap dataset tolok ukur semata.

Secara mekanis, masukannya dua arus literatur (makalah versi YOLO dan makalah aplikasi pertanian); keluarannya tabel perbandingan, daftar tantangan, dan agenda riset — tanpa eksperimen baru.

## Cara Kerja Langkah demi Langkah

### Cakupan dan Metode Survei

Survei ini bersifat naratif-terstruktur, bukan tinjauan sistematis berprotokol. Alurnya: (1) dasar CNN (*Convolutional Neural Network*, jaringan pengekstrak fitur citra lewat operasi konvolusi dan *pooling*); (2) taksonomi deteksi objek — detektor dua tahap (keluarga R-CNN: mengusulkan kandidat wilayah lalu mengklasifikasikannya) versus detektor satu tahap (SSD, YOLO: memprediksi kotak langsung dari peta fitur); (3) pembahasan versi per versi; (4) aplikasi per bidang; (5) analisis komparatif dan tantangan.

Kerangka dua sumbu tersebut digambarkan sebagai berikut:

```
SUMBU 1: evolusi versi         SUMBU 2: aplikasi pertanian
----------------------         ---------------------------
v1  2015 : grid + regresi      deteksi gulma
v2  2016 : anchor + batchnorm  deteksi tanaman / buah
v3  2018 : multi-skala         pelacakan hewan
v4  2020 : CSP + CIoU          deteksi penyakit / hama
v5  2020 : PyTorch             pertanian presisi
v6  2022 : head terpisah                |
v7  2022 : E-ELAN                       v
v8  2023 : anchor-free         analisis komparatif versi x tugas:
v9  2024 : PGI + GELAN         kekuatan, kelemahan, hardware,
v10 2024 : NMS-free            metrik galat
                                        |
                                        v
        tantangan: data, hardware, lingkungan, objek kecil
        arah riset: multimodal, XAI, sistem adaptif, human-AI
```

Inovasi tiap versi (kolom kiri) dipertemukan dengan kebutuhan tiap bidang aplikasi (kolom kanan); irisan keduanya dianalisis, lalu ditarik menjadi tantangan dan arah riset.

### Sumbu Pertama: Evolusi YOLOv1–YOLOv10

Tiap versi dibahas dengan pola tetap: masalah pendahulunya, perubahan yang dilakukan, dan angka kinerja. Dua metrik dipakai berulang: mAP (*mean Average Precision*, rata-rata presisi deteksi di seluruh kelas, maksimal 100%) dan FPS (*frame* per detik, laju pemrosesan).

**YOLOv1 (2015).** Citra dibagi grid S×S; sel yang memuat pusat objek memprediksi *bounding box* (kotak pembatas berisi koordinat, ukuran, dan *confidence score* — probabilitas adanya objek dikali IoU, rasio irisan-gabungan dua kotak) beserta kelasnya; kotak ganda dirampingkan NMS (*Non-Maximum Suppression*: hanya kotak berskor tertinggi yang dipertahankan). Hasilnya 63,4% mAP pada 45 FPS di PASCAL VOC 2007 — jauh lebih cepat dari detektor dua tahap masanya, tetapi *recall* (proporsi objek yang tertemukan) rendah.

**YOLOv2 (2016).** *Backbone* (jaringan pengekstrak fitur) Darknet-19; *anchor box* (kotak referensi berbentuk tetap, dipilih dengan klastering K-means). Perbaikannya terukur satu per satu: klasifier resolusi tinggi +4% mAP, *batch normalization* (normalisasi aktivasi agar pelatihan stabil) +2%, prediksi relatif sel +5%, anchor box +7% recall, dan koneksi lompat +1%.

**YOLOv3 (2018).** Darknet-53 dengan koneksi residual; prediksi pada tiga skala peta fitur (13×13, 26×26, 52×52) agar objek kecil terwakili. Pada MS COCO dicapai AP 36,2% dan AP50 60,6% pada 20 FPS — lompatan akurasi dari era VOC.

**YOLOv4 (2020).** Merangkai CSPDarknet53 (CSP: aliran fitur dibelah dua cabang untuk memperbaiki gradien), SPP (penggabungan fitur multi-skala), leher PAN (agregasi fitur dua arah antar-resolusi), dan loss CIoU (IoU ditambah penalti jarak pusat dan rasio aspek).

**YOLOv5 (2020).** Berpindah dari Darknet ke PyTorch; loss gabungan *binary cross-entropy* (kelas dan keobjekan) dan CIoU (lokalisasi). YOLOv5x mencapai AP 50,7% pada citra 640 piksel dengan 200 FPS pada NVIDIA V100 — titik ketika versi arus utama menembus 50% AP COCO sambil tetap *real-time*.

**YOLOv6 (2022).** Memakai FPN (*Feature Pyramid Network*, piramida fitur multi-resolusi) dan kepala klasifikasi yang dipisah dari regresi kotak. YOLOv6-L mencapai AP 52,5% (AP50 70%) pada sekitar 50 FPS di GPU Tesla T4; varian nano/tiny menyasar perangkat berdaya rendah seperti robot lapangan.

**YOLOv7 (2022).** Memperkenalkan E-ELAN (pengelolaan jalur gradien pada blok bertumpuk), penskalaan kedalaman-lebar seragam, dan kepala bantu yang hanya aktif saat pelatihan. YOLOv7-E6 mencapai AP 55,9% dan AP50 73,5%.

**YOLOv8 (2023).** Beralih ke skema *anchor-free*: pusat objek diprediksi langsung tanpa kotak referensi, ditambah augmentasi mosaik (empat citra latih digabung menjadi satu). YOLOv8x mencapai AP 53,9% — naik 3,2 poin dari YOLOv5x — dengan 280 FPS pada NVIDIA A100 dan TensorRT.

**YOLOv9 (2024).** Memperkenalkan PGI (mekanisme menjaga informasi gradien tetap utuh selama pelatihan) dan GELAN (arsitektur efisien yang ringan). Survei melaporkan kenaikan AP 0,6 poin atas YOLOv8 dengan parameter lebih sedikit.

**YOLOv10 (2024).** Pelatihan *NMS-free* dengan penugasan label ganda sehingga NMS dihapus, ditambah kepala klasifikasi ringan dan *downsampling* terpisah jalur spasial-kanal. Survei melaporkan latensi dan ukuran model turun terhadap YOLOv9 dengan akurasi setara atau lebih baik, tanpa angka rinci.

### Sumbu Kedua: Taksonomi Aplikasi Pertanian

Literatur aplikasi dikelompokkan ke dalam lima bidang berikut.

**Deteksi gulma.** YOLO-WEED (YOLOv3 pada video UAV, *unmanned aerial vehicle* atau wahana udara nirawak) untuk ladang bawang daun mencapai mAP 93,81% dan F1 0,94 — angka tinggi, tetapi hanya berlaku pada satu komoditas dan resolusi tertentu, dan gulma kecil masih terlewat.

**Deteksi tanaman.** Model YOLO-P mengenali tandan buah segar, alat pemetik, dan pohon kelapa sawit dengan mAP 98,68%, F1 0,97, dan ukuran 76 MB — akurasi nyaris sempurna, tetapi lingkupnya tiga kelas objek pada satu jenis perkebunan.

**Pelacakan hewan.** YOLOv3 mengenali perilaku ayam petelur; YOLO-BYTE melacak sapi perah dari satu kamera; EmbeddedPigCount (TinyYOLOv4) menghitung babi dengan akurasi 99,44% dari 2.675 citra — angka itu diperoleh pada koridor kandang terkontrol, bukan kandang terbuka.

**Deteksi penyakit.** YOLOv3 yang diperbaiki mendeteksi penyakit dan hama tomat dengan akurasi 92,39% dalam 20,39 ms per citra — setara sekitar 49 FPS, melampaui ambang *real-time* 30 FPS. Tiny-YOLOv3 untuk padi mencapai 98,92%, tetapi studi padi lain dengan Raspberry Pi 3 hanya 73,33%; selisih lebih dari 25 poin ini menunjukkan hasil sangat bergantung perangkat keras dan kualitas citra, bukan algoritme semata.

**Pertanian presisi.** Pembedaan tanaman dan gulma pada ladang stroberi dan kacang polong dari citra UAV mencapai akurasi 94,73%. Deteksi lalat buah zaitun mencatat presisi 0,84, recall 0,97, dan mAP 96,68% — recall tinggi berarti hampir semua hama tertangkap, tetapi presisi lebih rendah menyiratkan sebagian deteksi merupakan alarm keliru.

### Analisis Komparatif dan Sintesis

Survei menyusun tabel kekuatan–kelemahan tiap versi per bidang: misalnya YOLOv1 cepat tetapi lemah pada objek kecil; YOLOv8 sangat cepat tetapi kesulitan pada objek sangat kecil. Tiga aspek dinilai: kompleksitas tugas, ketergantungan perangkat keras (dari GPU kelas atas sampai sistem tertanam seperti NVIDIA Jetson), dan metrik galat (presisi, recall, mAP, F1, serta jenis kesalahan lokalisasi, klasifikasi, positif/negatif palsu). Simpulannya: tidak ada satu versi terbaik untuk semua tugas; pemilihan harus menimbang akurasi, ukuran objek, dan daya komputasi yang tersedia.

## Eksperimen dan Hasil

Sebagai survei, makalah ini tidak menjalankan eksperimen baru; buktinya berupa agregasi puluhan studi aplikasi. Temuan yang disintesis:

- YOLO telah dipakai pada kelima bidang aplikasi, dengan YOLOv3, v4, dan v5 paling sering muncul — versi-versi itu paling matang dokumentasinya ketika studi aplikasi dilakukan.
- Angka kinerja lintas studi umumnya tinggi (93–99% mAP atau akurasi pada tugas spesifik), tetapi tidak dapat dibandingkan satu sama lain karena dataset, kondisi, dan metriknya berbeda.
- Hambatan yang berulang dilaporkan: objek kecil terlewat, dataset sempit per komoditas, dan kebutuhan komputer *onboard* pada wahana seperti UAV penyemprot.
- Empat tantangan dirumuskan: (1) spesifisitas data — model sukar pindah komoditas, disarankan *transfer learning* (penyetelan model terlatih ke tugas baru); (2) keterbatasan perangkat keras — disarankan kuantisasi (pemampatan bobot ke presisi lebih rendah) dan arsitektur ringan untuk perangkat tepi; (3) variabilitas cahaya, cuaca, dan medan; (4) deteksi objek kecil — disarankan mekanisme atensi dan strategi multi-skala.
- Empat arah riset diproyeksikan: integrasi multimodal (citra RGB digabung data termal atau hiperspektral), keterjelasan model (XAI), sistem adaptif *real-time*, dan kolaborasi manusia–AI.

Interpretasi keseluruhan: bukti menunjukkan YOLO layak dipakai di lapangan, tetapi kematangannya timpang — deteksi gulma dan penyakit daun paling banyak diuji, sedangkan penerapan versi terbaru (v9, v10) di pertanian praktis belum ada saat survei ditulis.

## Kelebihan dan Keterbatasan

Kelebihannya: cakupan versi terlengkap pada masanya (v1 sampai v10 dalam satu naskah); taksonomi aplikasi yang jelas; perhatian pada aspek penerapan nyata seperti perangkat tepi; dan tabel komparatif yang memudahkan pemilihan varian per tugas.

Keterbatasannya: pertama, survei naratif tanpa protokol seleksi literatur eksplisit, sehingga cakupannya bergantung pilihan penulis. Kedua, dari sisi ketelitian, beberapa tabel ringkasannya tidak konsisten dengan teksnya sendiri — misalnya tabel versi mencantumkan YOLOv5 sebagai *anchor-free*, padahal teksnya sendiri menjelaskan YOLOv5 berbasis anchor — sehingga rincian versi perlu diverifikasi ke makalah aslinya. Ketiga, secara konseptual survei silsilah cepat usang: YOLO11 dan YOLOv12 terbit tidak lama setelahnya dan berada di luar cakupan.

## Kaitan dengan Bab Lain

Bab ini membungkus seluruh silsilah fondasi — mulai dari [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md) — ke dalam konteks aplikasi, sehingga menjadi jembatan antara bab-bab arsitektur dan klaster penerapan. Dibanding survei umum [bab 026 (Terven dkk.)](./026%20-%202023%20-%20Review%20YOLO%20%28Terven%20dkk.%29%20-%20Survei%20YOLO.md) dan [bab 028 (Jiang dkk.)](./028%20-%202022%20-%20Review%20Perkembangan%20YOLO%20%28Jiang%20dkk.%29%20-%20Survei%20YOLO.md), fokusnya domain-spesifik. Ia terbit berdampingan dengan [bab 030 (Ali & Zhang)](./030%20-%202024%20-%20Review%20Model%20%26%20Aplikasi%20YOLO%20%28Ali%20%26%20Zhang%29%20-%20Survei%20YOLO.md) yang juga meninjau model dan aplikasi YOLO pada 2024. Ketiadaan eksperimen pembanding di bab ini dilengkapi oleh [bab 032 (Jegham dkk.)](./032%20-%202024%20-%20YOLO%20Evolution%20Benchmark%20%28Alif%20%26%20Hussain%29%20-%20Survei%20YOLO.md), yang menguji ulang 33 model YOLO pada pengaturan seragam — bacaan pasangan yang menutup kelemahan survei naratif.

## Poin untuk Sitasi

Kutip dengan kunci `sapkota2024yoloagri`. Ringkasan yang aman dikutip: "Survei ini menelusuri evolusi YOLOv1 hingga YOLOv10 dan memetakan penerapannya pada lima bidang pertanian — deteksi gulma, deteksi tanaman, pelacakan hewan, deteksi penyakit, dan pertanian presisi — disertai analisis komparatif tiap versi serta perumusan tantangan lapangan dan arah riset lanjutan."

Catatan verifikasi wajib sebelum sitasi formal:

- **Atribusi penulis perlu diperbaiki.** Naskah arXiv:2406.10139 berpenulis Mujadded Al Rabbani Alif dan Muhammad Hussain (University of Huddersfield); entri `references.bib` saat ini mencantumkan Sapkota dkk., yang tidak cocok dengan naskah.
- Angka studi aplikasi (93,81%; 98,68%; 99,44%; 92,39%; 94,73%; 96,68%) adalah hasil studi yang dikutip survei, bukan pengukuran survei sendiri; kutip studi aslinya untuk sitasi hasil tersebut.
- Angka kinerja versi (63,4% mAP/45 FPS; AP 53,9%) diringkas survei dari makalah versi asli; verifikasi ke makalah versi yang bersangkutan bila akan dikutip.
