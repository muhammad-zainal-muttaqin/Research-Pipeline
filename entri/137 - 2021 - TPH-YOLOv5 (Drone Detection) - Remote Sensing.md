# 137 - TPH-YOLOv5: Improved YOLOv5 Based on Transformer Prediction Head for Object Detection on Drone-Captured Scenarios

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhu2021tphyolov5` |
| Judul asli | TPH-YOLOv5: Improved YOLOv5 Based on Transformer Prediction Head for Object Detection on Drone-Captured Scenarios |
| Penulis | Zhu, Xingkui; Lyu, Shuchang; Wang, Xu; Zhao, Qi |
| Tahun | 2021 |
| Venue | Proceedings of the IEEE/CVF International Conference on Computer Vision Workshops (ICCVW) |
| Tema | Remote Sensing |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=TPH-YOLOv5%3A%20Improved%20YOLOv5%20Based%20on%20Transformer%20Prediction%20Head%20for%20Object%20Detection%20on%20Drone-Captured%20Scenarios
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=TPH-YOLOv5%3A%20Improved%20YOLOv5%20Based%20on%20Transformer%20Prediction%20Head%20for%20Object%20Detection%20on%20Drone-Captured%20Scenarios&sort=relevance

## Gambaran Umum
TPH-YOLOv5 merupakan model deteksi objek satu tahap (*one-stage detector*) yang dirancang khusus untuk menganalisis citra hasil tangkapan wahana udara tanpa awak (*unmanned aerial vehicle* / UAV) atau drone. Model ini dikembangkan untuk memecahkan tantangan khas pada citra udara, seperti ukuran objek yang sangat kecil (hanya beberapa piksel), kepadatan objek yang tinggi, variasi skala ekstrem, serta latar belakang yang bising dan kompleks. Melalui integrasi modul *Transformer Prediction Head* (TPH) dan *Convolutional Block Attention Module* (CBAM) ke dalam kerangka dasar YOLOv5, model ini mampu mengekstraksi informasi konteks global secara efektif.

Penerapan modifikasi tersebut memberikan peningkatan akurasi deteksi yang signifikan dibandingkan model YOLOv5 standar. Pada ajang kompetisi VisDrone Challenge 2021, model ini berhasil menempati peringkat kelima pada kategori deteksi objek dengan nilai *mean Average Precision* (mAP) sebesar 39,18%. Keberhasilan ini membuktikan bahwa integrasi mekanisme perhatian (*attention mechanism*) dan pemrosesan berbasis *Transformer* dapat menutupi kelemahan detektor konvensional pada skenario penginderaan jauh (*remote sensing*) udara.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Deteksi objek pada citra yang diperoleh dari platform UAV menghadapi kendala geometris dan radiometris yang tidak ditemukan pada citra perspektif horizontal biasa. Objek target seperti pejalan kaki atau kendaraan sering kali hanya berukuran di bawah $10 \times 10$ piksel dan berkumpul dalam kepadatan ekstrem di area perkotaan. Akibat ketinggian terbang drone yang dinamis, ukuran objek yang sama dapat mengalami fluktuasi skala yang lebar dari satu bingkai citra ke bingkai berikutnya.

Detektor objek satu tahap konvensional seperti YOLOv5 sering kali tidak mampu mendeteksi objek sekecil ini. Fitur spasial objek kecil cenderung terdegradasi akibat operasi konvolusi dan penyusutan spasial (*downsampling*) bertingkat di dalam tulang punggung (*backbone*) jaringan. Selain itu, operasi konvolusi lokal standar memiliki keterbatasan dalam menangkap ketergantungan jarak jauh (*long-range dependencies*), sehingga model kesulitan mengasosiasikan objek dengan konteks lingkungan sekitarnya untuk mengenali objek yang mengalami oklusi (terhalang). Terakhir, latar belakang citra yang kompleks, seperti jalan raya, vegetasi, dan bayangan gedung, menghasilkan tingkat kebisingan (*noise*) yang tinggi, memicu terjadinya deteksi positif palsu (*false positives*). Ketiadaan informasi konteks global dan hilangnya resolusi spasial halus menjadi celah utama yang ingin diselesaikan oleh penelitian ini.

## Ide Utama
Ide utama TPH-YOLOv5 berfokus pada restrukturisasi arsitektur YOLOv5 untuk memelihara detail spasial halus dan menangkap informasi konteks global melalui tiga pilar:
1. **Penambahan Jalur Prediksi Resolusi Tinggi (P2):** Jalur deteksi keempat ditambahkan untuk beroperasi pada peta fitur dengan tingkat penyusutan (*stride*) rendah (hanya 4 kali penyusutan dari resolusi input), guna melestarikan representasi spasial objek yang sangat kecil sebelum hilang akibat operasi konvolusi lebih dalam.
2. **Transformer Prediction Head (TPH):** Mengganti blok konvolusi *CSP Bottleneck* pada leher deteksi dengan blok *Transformer Encoder*. Blok ini memanfaatkan mekanisme perhatian mandiri (*self-attention*) untuk mengekstrak hubungan spasial global antar-fitur di seluruh citra.
3. **Penyaringan Fitur Menggunakan CBAM:** Modul perhatian spasial dan saluran CBAM disisipkan di dalam leher jaringan (*neck*) untuk menyaring sinyal fitur secara adaptif, memusatkan fokus model pada objek sasaran dan meredam kebisingan latar belakang.

Sebagai pelengkap pasca-pemrosesan, sistem ini menggunakan pengklasifikasi sekunder berbasis ResNet-18 yang bekerja pada potongan gambar objek untuk meminimalkan kesalahan klasifikasi pada kategori yang secara visual mirip.

## Cara Kerja Langkah demi Langkah
Diagram berikut menunjukkan modifikasi alur kerja arsitektural TPH-YOLOv5 dibandingkan dengan baseline YOLOv5, yang mencakup penambahan head P2, integrasi CBAM, dan penggunaan blok Transformer pada prediction head.

```
       ┌────────────────────────────────────────────────────────┐
       │                 Input Citra (640x640)                  │
       └──────────────────────────┬─────────────────────────────┘
                                  │
                                  ▼
                     ┌──────────────────────────┐
                     │  Backbone: CSPDarknet53  │
                     └──────┬───┬───┬───┬───────┘
                            │   │   │   │
        P2 Feature (160x160)│   │   │   │ P5 Feature (20x20)
       ┌────────────────────┘   │   │   └───────────────────────┐
       │                        │   │                           │
       │    P3 Feature (80x80)  │   │ P4 Feature (40x40)        │
       │   ┌────────────────────┘   └───────────────┐           │
       │   │                                        │           │
       ▼   ▼                                        ▼           ▼
     ┌────────────────────────────────────────────────────────────┐
     │                    Neck: PANet + CBAM                      │
     │  - Multi-scale Feature Fusion                              │
     │  - Channel & Spatial Attention via CBAM Module             │
     └─┬───┬────────────────────────────────────────┬───┬─────────┘
       │   │                                        │   │
       │   │                                        │   │
       ▼   ▼                                        ▼   ▼
     ┌───────────┐                            ┌───────────┐
     │  TPH (P2) │                            │  TPH (P4) │
     │  160x160  │                            │   40x40   │
     └─────┬─────┘                            └─────┬─────┘
           │                                        │
           ▼                                        ▼
    [Objek Sangat Kecil]                      [Objek Sedang]
                                  
     ┌───────────┐                            ┌───────────┐
     │  TPH (P3) │                            │  TPH (P5) │
     │   80x80   │                            │   20x20   │
     └─────┬─────┘                            └─────┬─────┘
           │                                        │
           ▼                                        ▼
      [Objek Kecil]                            [Objek Besar]
```

### ### Integrasi Jalur Deteksi P2 Resolusi Tinggi
Pada model YOLOv5 standar, deteksi dilakukan pada tiga peta fitur dengan dimensi spasial $80 \times 80$, $40 \times 40$, and $20 \times 20$ (untuk input citra $640 \times 640$). Untuk mempertahankan informasi objek mikro, TPH-YOLOv5 memperkenalkan jalur deteksi keempat yang disebut P2. Jalur ini beroperasi pada tingkat penyusutan (*stride*) 4, menghasilkan peta fitur beresolusi $160 \times 160$ piksel. Dengan mengalirkan fitur resolusi tinggi dari lapisan awal *backbone* langsung ke leher jaringan (*neck*), detail geometris objek yang berukuran di bawah $8 \times 8$ piksel dapat dipertahankan tanpa mengalami degradasi akibat operasi *downsampling* yang berulang.

### ### Penerapan Blok Transformer Encoder pada Head Deteksi
Gagasan utama untuk membedakan objek dalam kondisi padat dan terhalang diselesaikan dengan mengganti blok konvolusi *CSP Bottleneck* pada prediction head dengan blok *Transformer Encoder*. Blok ini terdiri dari lapisan *Multi-Head Self-Attention* (MHSA) dan lapisan *Feed-Forward Network* (FFN) dua tingkat yang dilengkapi dengan normalisasi lapisan (*layer normalization*).

Dalam blok ini, setiap nilai piksel spasial dari peta fitur diubah menjadi representasi vektor yang berfungsi sebagai token. Melalui mekanisme MHSA, model menghitung bobot keterkaitan dinamis antara satu lokasi piksel dengan seluruh lokasi piksel lainnya di dalam citra. Hal ini memungkinkan model untuk menangkap konteks spasial global secara komprehensif, sehingga ketika sebuah objek (misalnya mobil) terhalang oleh pohon, model tetap dapat mengenalinya berdasarkan fitur lingkungan sekitarnya (seperti pola jalan raya atau bayangan linier).

### ### Penguatan Fitur Melalui CBAM di Neck
Untuk mereduksi kebisingan latar belakang yang bising pada citra udara, modul CBAM disisipkan sebelum fitur digabungkan dalam *Path Aggregation Network* (PANet). CBAM bekerja secara sekuensial:
1. *Channel Attention Module* (CAM) menekan saluran fitur yang tidak relevan dengan mengevaluasi kontribusi setiap saluran melalui operasi rata-rata (*average pooling*) dan maksimum (*max pooling*).
2. *Spatial Attention Module* (SAM) menentukan lokasi spasial yang paling penting dengan memproyeksikan fitur saluran ke bentuk peta probabilitas dua dimensi, memastikan detektor berfokus pada area keberadaan objek nyata dan mengabaikan area latar belakang seperti atap gedung atau air.

### ### Pemurnian Klasifikasi Menggunakan Pengklasifikasi Crop Sekunder
Objek dengan resolusi spasial yang sangat rendah sering kali memiliki fitur visual yang mirip, menyebabkan kesalahan klasifikasi antar-kelas yang berdekatan (seperti sepeda motor dengan sepeda). Untuk mengatasi masalah ini, TPH-YOLOv5 menerapkan modul pasca-pemrosesan berupa pengklasifikasi sekunder berbasis arsitektur ResNet-18.

Setiap kotak pembatas (*bounding box*) kandidat yang dihasilkan oleh model deteksi dipotong (*cropped*) dari citra asli beresolusi tinggi, diubah ukurannya (*resized*) menjadi $64 \times 64$ piksel, dan dilewatkan ke ResNet-18 yang telah dilatih secara terpisah pada dataset potongan objek. Pengklasifikasi ini bertugas memverifikasi dan memperbaiki label kelas yang meragukan dari hasil deteksi utama, sehingga secara signifikan mengurangi kesalahan klasifikasi pada objek-objek kecil yang membingungkan.

## Eksperimen dan Hasil
Evaluasi kinerja TPH-YOLOv5 dilakukan pada dataset benchmark **VisDrone-DET2021**. Dataset ini menantang karena berisi ribuan citra udara perkotaan dengan kepadatan objek tinggi yang diambil dari berbagai sudut pandang UAV.

Studi ablasi (*ablation study*) pada subset **VisDrone-DET test-dev** menunjukkan dampak dari masing-masing modifikasi arsitektur:

| Konfigurasi Model | mAP (%) | GFLOPs |
|---|:---:|:---:|
| YOLOv5 (Baseline) | 28,88 | 219,0 |
| YOLOv5 + P2 (Head Deteksi Mikro) | 31,03 | - |
| YOLOv5 + P2 + Transformer (TPH) | 32,84 | - |
| TPH-YOLOv5 (YOLOv5 + P2 + TPH + CBAM) | 33,63 | 259,0 |
| TPH-YOLOv5 + *Multi-Scale Testing* | 34,90 | - |
| TPH-YOLOv5 + *Multi-Scale Testing* + *Classifier* ResNet-18 | 35,74 | - |

Integrasi head P2 memberikan lonjakan akurasi awal yang besar (+2,15% mAP), memvalidasi kegunaan peta fitur resolusi tinggi. Blok Transformer (TPH) menambahkan peningkatan sebesar +1,81% mAP, membuktikan kegunaan fitur konteks global. Gabungan seluruh komponen menghasilkan nilai mAP sebesar 33,63%.

Saat dievaluasi pada dataset **VisDrone-DET2021 test-challenge** yang lebih kompetitif, model final TPH-YOLOv5 mencapai skor mAP sebesar **39,18%** (pada IoU 0,5:0,95) dengan menggunakan pengujian multi-skala dan pengklasifikasi sekunder. Hasil ini mengamankan peringkat kelima pada kompetisi VisDrone 2021, menunjukkan keunggulan performa dibanding detektor satu tahap standar lainnya.

## Kelebihan dan Keterbatasan
Kelebihan utama TPH-YOLOv5 adalah kemampuannya yang luar biasa dalam melokalisasi objek mikro dan menangani skenario padat objek yang mengalami oklusi. Integrasi mekanisme perhatian mandiri (*self-attention*) global melalui Transformer dan CBAM memungkinkan model membedakan objek dari latar belakang yang berisik secara presisi.

Namun, secara konseptual dan dari sisi rekayasa, model ini memiliki keterbatasan berupa beban komputasi yang sangat besar. Penambahan head keempat (P2) dan modul Transformer meningkatkan tuntutan komputasi dari 219,0 GFLOPs menjadi 259,0 GFLOPs. Peningkatan ini menyebabkan penurunan kecepatan inferensi (*frames per second* / FPS) yang drastis, sehingga membatasi kemampuan model untuk diterapkan secara langsung (*on-board*) pada perangkat komputasi tepi dengan daya terbatas di dalam drone untuk pemrosesan video *real-time*. Selain itu, penggunaan pengklasifikasi sekunder ResNet-18 di tahap pasca-pemrosesan memecah alur kerja deteksi menjadi proses dua tahap yang tidak efisien karena waktu inferensinya berbanding lurus dengan jumlah objek yang terdeteksi dalam citra.

## Kaitan dengan Bab Lain
Perkembangan deteksi objek pada citra penginderaan jauh (*remote sensing*) menunjukkan transisi dari metode berbasis pemotongan eksternal menuju modifikasi arsitektur internal.

Silsilah ini dapat ditarik dari model **YOLT** ([You Only Look Twice: Rapid Multi-Scale Object Detection in Satellite Imagery](./140%20-%202018%20-%20YOLT%20%28Satellite%20Imagery%29%20-%20Remote%20Sensing.md)) yang mengatasi masalah resolusi citra satelit yang besar dengan teknik pembagian ubin (*tiling*) eksternal dan inferensi dua langkah. TPH-YOLOv5 mengambil pendekatan berbeda dengan memodifikasi arsitektur jaringan secara internal melalui penambahan head P2 resolusi tinggi dan modul Transformer untuk menghindari *tiling* yang lambat.

Pendekatan representasi fitur hierarkis untuk mengatasi variasi skala juga telah dirintis dalam **Robust CNN High-Res Remote Sensing** ([Hierarchical and Robust Convolutional Neural Network for Very High-Resolution Remote Sensing Object Detection](./138%20-%202019%20-%20Robust%20CNN%20High-Res%20Remote%20Sensing%20%28Zhang%20dkk.%29%20-%20Remote%20Sensing.md)), yang memodelkan hubungan spasial antar-skala menggunakan jaringan konvolusi bertingkat. TPH-YOLOv5 memperluas konsep pemodelan spasial ini dengan menggabungkan mekanisme perhatian mandiri global (*self-attention*) dari Transformer dan perhatian spasial-saluran CBAM.

Evolusi model drone berikutnya diwakili oleh **UAV-YOLOv8** ([UAV-YOLOv8: A Small-Object-Detection Model Based on Improved YOLOv8 for UAV Aerial Photography Scenarios](./139%20-%202023%20-%20UAV-YOLOv8%20%28Small%20Object%29%20-%20Remote%20Sensing.md)). UAV-YOLOv8 berupaya mengatasi keterbatasan beban komputasi yang tinggi pada TPH-YOLOv5 dengan memanfaatkan arsitektur *anchor-free* YOLOv8 dan modul perhatian yang lebih ringan, memulihkan kecepatan inferensi tanpa mengorbankan akurasi deteksi objek kecil pada platform UAV.

## Poin untuk Sitasi
Kunci BibTeX untuk merujuk naskah ini adalah `zhu2021tphyolov5`.
Berikut adalah ringkasan yang aman dikutip dalam tinjauan pustaka:

> Zhu dkk. mengusulkan TPH-YOLOv5, variasi YOLOv5 untuk skenario UAV yang menambahkan head prediksi beresolusi tinggi keempat (P2) dan mengintegrasikan blok Transformer Encoder di bagian prediction head serta modul CBAM di leher jaringan. Model ini dilengkapi dengan pengklasifikasi sekunder berbasis ResNet-18 pada pasca-pemrosesan untuk menyaring klasifikasi objek kecil yang membingungkan, mencapai mAP sebesar 39,18% pada dataset VisDrone-DET2021.

Catatan untuk verifikasi lebih lanjut:
- Perlu dicatat bahwa penambahan pengklasifikasi ResNet-18 yang terpisah merupakan penyumbang peningkatan akurasi akhir sebesar 0,84% mAP pada test-dev (dari 34,90% menjadi 35,74%). Pengguna yang bermaksud mengimplementasikan sistem ini secara terpadu tanpa pengklasifikasi tambahan harus merujuk pada performa deteksi murni TPH-YOLOv5 sebesar 33,63% mAP pada subset test-dev.
