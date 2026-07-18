# 155 - DETRs Beat YOLOs on Real-Time Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhao2024rtdetr` |
| Judul asli | DETRs Beat YOLOs on Real-Time Object Detection |
| Penulis | Zhao, Yian; Lv, Wenyu; Xu, Shangliang; Wei, Jinman; Wang, Guanzhong; Dang, Qingqing; Liu, Yi; Chen, Jie |
| Tahun | 2024 |
| Venue | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2304.08069
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=DETRs%20Beat%20YOLOs%20on%20Real-Time%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=DETRs%20Beat%20YOLOs%20on%20Real-Time%20Object%20Detection&sort=relevance

## Gambaran Umum
Dalam deteksi objek *real-time*, arsitektur satu-tahap berbasis konvolusi seperti seri YOLO (*You Only Look Once*) mendominasi karena menawarkan keseimbangan optimal antara akurasi dan kecepatan. Namun, model-model ini memiliki ketergantungan kritis pada *Non-Maximum Suppression* (NMS) untuk menyaring prediksi yang tumpang-tindih. Tahap NMS ini menimbulkan hambatan komputasi karena memiliki latensi yang tidak stabil dan sangat sensitif terhadap jumlah objek dalam gambar. Di sisi lain, detektor berbasis *Transformer* seperti DETR (*Detection Transformer*) menawarkan alternatif deteksi *end-to-end* yang meniadakan NMS, tetapi terkendala oleh tingginya biaya komputasi *encoder* multi-skala serta lambatnya konvergensi saat pelatihan.

Makalah ini memperkenalkan RT-DETR (*Real-Time Detection Transformer*), detektor objek berbasis *Transformer* pertama yang mampu beroperasi dalam kecepatan *real-time* sekaligus melampaui performa detektor YOLO yang sekelas. Penulis merancang RT-DETR dengan memodifikasi komponen krusial DETR untuk meminimalkan beban komputasi. Melalui desain *hybrid encoder* yang efisien dan pemilihan kueri awal berbasis ketidakpastian minimum (*uncertainty-minimal query selection*), model ini mampu memproses fitur spasial dengan sangat cepat tanpa menurunkan akurasi deteksi. Hasil eksperimen pada dataset MS COCO menunjukkan bahwa RT-DETR-R50 mencapai 53,1% *Average Precision* (AP) dengan kecepatan 108 bingkai per detik (*frames per second* / FPS) pada GPU NVIDIA T4, menjadikannya standar baru bagi sistem deteksi objek *end-to-end* tanpa pasca-pemrosesan konvensional.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Detektor objek berbasis konvolusi modern menghasilkan ribuan kandidat *bounding box* (kotak pembatas) untuk disaring menggunakan algoritme NMS (*Non-Maximum Suppression*) sebagai pasca-pemrosesan. NMS membandingkan nilai *Intersection over Union* (IoU) antarkotak dan menyingkirkan prediksi dengan skor kepercayaan (*confidence score*) rendah. Namun, waktu eksekusi NMS bervariasi bergantung pada kepadatan objek dalam citra. Ketidakstabilan latensi ini menghambat implementasi pada sistem *real-time* industri yang membutuhkan jaminan waktu respons konstan.

DETR menawarkan deteksi *end-to-end* tanpa NMS dengan memprediksi objek secara langsung. Namun, DETR memiliki dua kendala utama. Pertama, mahalnya perhatian multi-skala: untuk mendeteksi objek multiskala, operasi atensi-diri (*self-attention*) global pada seluruh tingkat fitur memiliki kompleksitas kuadratik terhadap jumlah piksel, membuat pemrosesan *encoder* (penyandi) sangat lambat. Kedua, inisialisasi kueri yang buruk: DETR menginisialisasi kueri objek (*object query*) sebagai vektor acak tanpa korelasi langsung dengan fitur citra masukan. Akibatnya, *decoder* (penafsir) membutuhkan banyak lapisan perhatian-silang (*cross-attention*) untuk menyelaraskan kueri, memperlambat konvergensi pelatihan.

## Ide Utama
RT-DETR mengatasi keterbatasan DETR konvensional melalui dua strategi utama yang berfokus pada kecepatan dan akurasi:
1. Dekopling Pemrosesan Fitur Multi-skala: Penulis mengajukan konsep *hybrid encoder* untuk menggantikan *encoder* Transformer standar. Beban komputasi ditekan dengan memisahkan pemrosesan fitur menjadi interaksi intra-skala berbasis perhatian (*Attention-based Intra-scale Feature Interaction* / AIFI) dan fusi lintas-skala berbasis konvolusi (*CNN-based Cross-scale Feature Fusion* / CCFF). AIFI membatasi operasi *self-attention* hanya pada tingkat fitur paling atas yang kaya akan informasi semantik global tetapi memiliki resolusi spasial paling rendah. CCFF kemudian melakukan fusi fitur spasial lintas-skala yang lebih efisien menggunakan lapisan konvolusional.
2. Pemilihan Kueri Berbasis Ketidakpastian Minimum: Daripada menggunakan kueri objek acak atau kueri berbasis skor klasifikasi murni, RT-DETR mengusulkan mekanisme *uncertainty-minimal query selection*. Metode ini memilih kueri objek awal berdasarkan skor ketidakpastian yang menggabungkan prediksi kategori dan kualitas lokalisasi (IoU). Dengan memilih fitur yang paling pasti (klasifikasi tinggi dan koordinat kotak stabil), *decoder* menerima representasi awal yang sangat dekat dengan objek nyata, sehingga mempercepat proses konvergensi dan meningkatkan akurasi deteksi.

## Cara Kerja Langkah demi Langkah
Arsitektur RT-DETR terdiri dari tiga komponen utama: *backbone* untuk ekstraksi fitur, *hybrid encoder* untuk pemrosesan fitur multi-skala, dan *decoder* Transformer untuk prediksi objek langsung.

### Aliran Fitur dari Backbone
Citra masukan dilewatkan melalui *backbone* CNN (seperti ResNet-50 atau HGNetv2) untuk mengekstrak fitur visual pada berbagai tingkat kedalaman. Secara spesifik, model mengekstrak tiga peta fitur multi-skala dari lapisan akhir *backbone*, yang dinotasikan sebagai $S_3$, $S_4$, dan $S_5$. Untuk citra masukan dengan resolusi $640 \times 640$ piksel, ketiga peta fitur ini memiliki resolusi spasial berturut-turut sebesar $80 \times 80$, $40 \times 40$, dan $20 \times 20$ piksel. Fitur tingkat rendah seperti $S_3$ kaya akan informasi geometris (tepi dan detail spasial), sedangkan fitur tingkat tinggi seperti $S_5$ kaya akan informasi semantik (kategori objek).

### Attention-based Intra-scale Feature Interaction (AIFI)
Pada DETR biasa, semua fitur multi-skala diratakan menjadi satu sekuens panjang lalu diproses oleh modul *self-attention*. RT-DETR menghindari hal ini dengan menyadari bahwa redundansi informasi spasial paling tinggi berada pada skala resolusi besar ($S_3$ dan $S_4$). Oleh karena itu, modul AIFI dirancang untuk hanya melakukan interaksi intra-skala menggunakan *self-attention* pada peta fitur $S_5$. Karena resolusi spasial $S_5$ terkecil ($20 \times 20 = 400$ token), biaya komputasi perhatian global berkurang drastis dari skala kuadratik $O((HW)^2)$ menjadi hanya $O(400^2)$. Operasi ini menghasilkan fitur baru yang merepresentasikan hubungan semantik global antar-wilayah citra pada skala terkecil.

### CNN-based Cross-scale Feature Fusion (CCFF)
Setelah interaksi intra-skala selesai pada $S_5$, fitur tersebut perlu digabungkan kembali dengan informasi spasial dari $S_4$ dan $S_3$. Proses ini ditangani oleh CCFF menggunakan blok-blok konvolusional berbasis *RepVGG-style* yang efisien. CCFF melakukan fusi atas-bawah (*top-down*) dan bawah-atas (*bottom-up*) untuk menyebarkan informasi. Pertama, peta fitur $S_5$ yang telah diperkaya oleh AIFI diperbesar ukurannya (*up-sample*) dan digabungkan secara konkatenasi dengan $S_4$. Hasil gabungan ini kemudian diproses dengan blok konvolusi untuk membentuk fitur terfusi tingkat menengah. Proses serupa diulangi ke arah bawah ke tingkat $S_3$, dan dilanjutkan dengan lintasan bawah-atas untuk menghasilkan peta fitur terfusi akhir.

### Diagram Arsitektur RT-DETR
Alur pemrosesan fitur dan pembentukan prediksi pada RT-DETR divisualisasikan dalam diagram berikut:

```
           ┌───────────────────────────────────────────────┐
           │              Citra Input (640x640)            │
           └───────────────────────┬───────────────────────┘
                                   ▼
           ┌───────────────────────────────────────────────┐
           │            Backbone (ResNet / HGNet)          │
           └────┬──────────────────┬──────────────────┬────┘
                │ S3 (80x80)       │ S4 (40x40)       │ S5 (20x20)
                ▼                  ▼                  ▼
           ┌──────────┐       ┌──────────┐       ┌──────────┐
           │          │       │          │       │   AIFI   │ (Self-Attention
           │          │       │          │       │ (Spatial)│  hanya pada S5)
           │          │       │          │       └────┬─────┘
           │          │       │          │            │
           │   CCFF   │◄──────┤   CCFF   │◄───────────┘
           │ (Fusion) │       │ (Fusion) │
           └────┬─────┘       └────┬─────┘
                │                  │
                └────────┬─────────┘
                         ▼
           ┌───────────────────────────────────────────────┐
           │       Uncertainty-Minimal Query Selection     │ (Memilih K kueri)
           └───────────────────────┬───────────────────────┘
                                   ▼
           ┌───────────────────────────────────────────────┐
           │              Transformer Decoder              │
           └───────────────────────┬───────────────────────┘
                                   ▼
           ┌───────────────────────────────────────────────┐
           │          Prediksi Kategori & Box              │
           └───────────────────────────────────────────────┘
```

### Uncertainty-Minimal Query Selection
Setelah fitur multi-skala akhir diproduksi oleh CCFF, sistem harus memilih $K$ token fitur (secara default $K = 300$) untuk dijadikan sebagai inisialisasi kueri posisi (*position queries*) dan kueri konten (*content queries*) bagi *decoder*. Metode seleksi tradisional hanya mengandalkan skor klasifikasi terbesar untuk memilih token. Namun, token dengan probabilitas klasifikasi tinggi belum tentu memiliki koordinat kotak pembatas yang akurat, sehingga sering kali menghasilkan kueri yang kurang optimal. 

RT-DETR mengatasi ini dengan memprediksi skor klasifikasi $P$ dan kualitas lokalisasi berupa IoU secara bersamaan selama pelatihan. Skor ketidakpastian minimum didefinisikan sebagai kombinasi linier dari probabilitas kategori dan keselarasan lokalisasi. Token-token dengan ketidakpastian terkecil dipilih sebagai kueri awal. Hal ini memastikan bahwa koordinat kueri awal sudah sangat dekat dengan objek riil, sehingga meringankan beban optimasi pada lapisan *decoder*.

### Decoder Transformer dan Flexible Speed Tuning
Kueri yang telah terpilih diumpankan ke *decoder* Transformer multi-lapisan untuk melakukan pembaruan representasi fitur secara iteratif melalui interaksi perhatian-silang dengan fitur keluaran *encoder*. *Decoder* memprediksi koordinat *bounding box* secara langsung dalam ruang kontinu dan kelas kategorinya secara independen tanpa memerlukan NMS. 

Sifat modular dari lapisan *decoder* pada RT-DETR memungkinkan fitur *Flexible Speed Tuning*. Pengguna dapat secara dinamis membatasi jumlah lapisan *decoder* yang diaktifkan selama inferensi (misalnya hanya menggunakan 3 lapisan pertama dari total 6 lapisan) tanpa perlu melatih ulang model. Pengurangan lapisan *decoder* ini menurunkan latensi komputasi secara linier dengan hanya mengorbankan sedikit akurasi deteksi.

## Eksperimen dan Hasil
RT-DETR dievaluasi secara komprehensif pada dataset MS COCO val2017 menggunakan GPU NVIDIA T4 dan dioptimalkan melalui pustaka TensorRT dengan presisi FP16. Evaluasi ini membandingkan akurasi deteksi (AP) serta latensi inferensi terhadap model YOLOv5, YOLOv6, YOLOv8, dan detektor berbasis DETR sebelumnya.

Pada pengujian model dengan skala menengah, RT-DETR-R50 mencapai akurasi sebesar 53,1% AP dengan latensi inferensi 9,2 milidetik (setara 108 FPS). Sebagai perbandingan, YOLOv8-L menghasilkan akurasi 52,9% AP tetapi dengan latensi yang bervariasi bergantung pada jumlah objek akibat hambatan komputasi NMS. Untuk model berskala besar, RT-DETR-R101 mencapai 54,3% AP pada latensi 13,4 milidetik (74 FPS), yang secara signifikan mengungguli YOLOv8-X dalam efisiensi latensi dan akurasi deteksi pada GPU.

Selain menggunakan tulang punggung ResNet, penulis juga menguji varian RT-DETR dengan tulang punggung HGNetv2 yang dikembangkan oleh Baidu. Model RT-DETR-L (Large) dengan HGNetv2 memperoleh akurasi 53,0% AP pada kecepatan 114 FPS dengan parameter sekitar 32,9M dan komputasi 108 GFLOPs. Varian RT-DETR-X (Extra-Large) mencapai akurasi tertinggi sebesar 54,8% AP dengan kecepatan 74 FPS menggunakan parameter sekitar 67,3M dan komputasi 234,4 GFLOPs.

Eksperimen dengan skema pra-pelatihan (*pre-training*) pada dataset skala besar Objects365 juga menunjukkan peningkatan performa yang sangat signifikan. Setelah dilatih awal pada Objects365, RT-DETR-R50 mampu mencapai akurasi 55,3% AP, sementara RT-DETR-R101 mencapai 56,2% AP pada dataset COCO. Ketika dibandingkan dengan detektor DINO-R50 (salah satu varian DETR non-real-time yang canggih), RT-DETR-R50 menunjukkan keunggulan mutlak dengan melampaui akurasi DINO-R50 sebesar 2,2% AP sekaligus berjalan 21 kali lebih cepat dalam hal FPS.

## Kelebihan dan Keterbatasan
RT-DETR menawarkan keunggulan struktural yang signifikan bagi sistem visi komputer modern:
- Keunggulan Bebas NMS: Dengan meniadakan proses pasca-pemrosesan NMS, model ini memberikan jaminan latensi konstan yang tidak terpengaruh oleh jumlah objek dalam gambar. Hal ini sangat krusial untuk kestabilan sistem *real-time* di lingkungan industri.
- Desain Efisiensi Tinggi: Penggabungan AIFI dan CCFF memangkas redundansi komputasi pada *encoder* hingga mampu bersaing dengan kecepatan detektor berbasis CNN murni.
- Penyetelan Fleksibel: Kemampuan untuk mengurangi lapisan *decoder* secara dinamis saat inferensi memberikan fleksibilitas operasional tanpa membutuhkan siklus pelatihan ulang yang mahal.

Namun, model ini juga memiliki beberapa keterbatasan praktis:
- Ketergantungan Akselerator: Dari sisi rekayasa, keunggulan kecepatan RT-DETR sangat bergantung pada optimasi grafik komputasi khusus seperti TensorRT pada GPU NVIDIA. Pada perangkat keras tanpa akselerator khusus, operasi perhatian dalam *decoder* masih dapat menjadi hambatan.
- Kebutuhan Memori Pelatihan: Secara konseptual, pelatihan RT-DETR membutuhkan kapasitas memori GPU yang jauh lebih besar dan waktu konvergensi yang relatif lebih lama dibandingkan dengan model YOLO yang murni berbasis konvolusi ringan.
- Kompleksitas Implementasi: Struktur *hybrid encoder* dan integrasi perhatian-silang membuat proses ekspor model ke format edge (seperti ONNX atau TFLite) untuk dijalankan di mikrokontroler atau NPU berdaya rendah menjadi lebih kompleks dibandingkan detektor YOLO konvensional.

## Kaitan dengan Bab Lain
RT-DETR mewarisi fondasi arsitektur deteksi objek end-to-end berbasis kueri yang diperkenalkan pertama kali oleh DETR. Makalah ini secara langsung memodifikasi mekanisme inisialisasi kueri dari model-model seperti Conditional DETR (lihat [160 - 2021 - Conditional DETR - Fondasi RGB](./160%20-%202021%20-%20Conditional%20DETR%20-%20Fondasi%20RGB.md)) dan DN-DETR (lihat [159 - 2022 - DN-DETR - Fondasi RGB](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md)), serta memanfaatkan pemelajaran representasi tingkat lanjut yang diwarisi dari DINO (lihat [158 - 2023 - DINO detector - Fondasi RGB](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md)). 

Dalam silsilah detektor real-time, RT-DETR berdiri sebagai penantang langsung bagi keluarga YOLO seperti Gold-YOLO (lihat [157 - 2023 - Gold-YOLO - Fondasi RGB](./157%20-%202023%20-%20Gold-YOLO%20-%20Fondasi%20RGB.md)) dan YOLOv8. Konsep detektor bebas NMS yang diusung oleh RT-DETR kemudian menginspirasi dan diadopsi secara luas oleh model deteksi multi-modal modern seperti YOLO-World (lihat [156 - 2024 - YOLO-World - Fondasi RGB](./156%20-%202024%20-%20YOLO-World%20-%20Fondasi%20RGB.md)), yang memperluas kemampuan deteksi real-time ke domain kosakata terbuka (*open-vocabulary*).

## Poin untuk Sitasi
Kunci BibTeX untuk merujuk makalah ini adalah:
```bibtex
@inproceedings{zhao2024rtdetr,
  title     = {DETRs Beat YOLOs on Real-Time Object Detection},
  author    = {Zhao, Yian and Lv, Wenyu and Xu, Shangliang and Wei, Jinman and Wang, Guanzhong and Dang, Qingqing and Liu, Yi and Chen, Jie},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2024}
}
```

Ringkasan berikut dapat digunakan untuk merujuk makalah ini dalam karya akademis:
> Zhao dkk. (2024) memperkenalkan RT-DETR, detektor objek berbasis Transformer pertama yang mencapai performa real-time dengan meniadakan kebutuhan akan Non-Maximum Suppression (NMS). Model ini memanfaatkan hybrid encoder yang memisahkan interaksi fitur intra-skala dan lintas-skala, serta mekanisme inisialisasi kueri berbasis ketidakpastian minimum untuk mempercepat konvergensi dan mencapai akurasi superior pada anggaran latensi yang setara dengan seri YOLO.

Catatan verifikasi: Klaim latensi dan throughput (misalnya 108 FPS pada RT-DETR-R50) diukur menggunakan NVIDIA TensorRT FP16 pada kartu grafis NVIDIA T4 dengan resolusi input $640 \times 640$. Pengukuran ini menyertakan waktu pemrosesan jaringan secara end-to-end tanpa overhead pasca-pemrosesan eksternal. Performa pada perangkat keras tepi non-GPU atau pustaka runtime standar lainnya (seperti CPU ONNX Runtime) perlu diuji secara terpisah karena karakteristik komputasi operasi atensi yang berbeda dari konvolusi standar.
