# 157 - Gold-YOLO: Efficient Object Detector via Gather-and-Distribute Mechanism

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2023goldyolo` |
| Judul asli | Gold-YOLO: Efficient Object Detector via Gather-and-Distribute Mechanism |
| Penulis | Wang, Chengcheng; He, Wei; Nie, Ying; Guo, Jianyuan; Liu, Chuanjian; Han, Kai; Wang, Yunhe |
| Tahun | 2023 |
| Venue | Advances in Neural Information Processing Systems (NeurIPS) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2309.11331
- **Google Scholar:** https://scholar.google.com/scholar?q=Gold-YOLO%3A%20Efficient%20Object%20Detector%20via%20Gather-and-Distribute%20Mechanism
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Gold-YOLO%3A%20Efficient%20Object%20Detector%20via%20Gather-and-Distribute%20Mechanism&sort=relevance

## Gambaran Umum

Gold-YOLO merupakan arsitektur detektor objek waktu nyata (*real-time*) yang dirancang untuk mengatasi hambatan fusi fitur multi-skala pada detektor berbasis regresi satu tahap (*one-stage detector*). Masalah utama yang diselesaikan oleh model ini adalah kebocoran atau hilangnya informasi penting selama proses penggabungan fitur dalam struktur leher (*neck*) konvensional seperti *Feature Pyramid Network* (FPN) dan *Path Aggregation Network* (PANet). Jaringan piramida konvensional tersebut menyebarkan informasi secara bertahap hanya melalui lapisan-lapisan yang bertetangga dekat. Hal ini menyebabkan detail spasial dari lapisan bawah mengalami pelemahan (*information attenuation*) sebelum mencapai lapisan atas yang lebih abstrak.

Sebagai solusinya, Gold-YOLO introduces mekanisme *Gather-and-Distribute* (GD) yang beroperasi layaknya arsitektur *hub-and-spoke* (pusat dan jari-jari). Mekanisme ini mengumpulkan (*gather*) fitur dari seluruh tingkatan secara simultan ke dalam representasi global terpadu, lalu mendistribusikannya (*distribute*) secara langsung ke setiap level piramida fitur. Dengan pembagian beban komputasi yang efisien antara konvolusi reparameterisasi untuk fitur tingkat rendah (*low-stage*) dan atensi mandiri (*self-attention*) untuk fitur tingkat tinggi (*high-stage*), Gold-YOLO meningkatkan akurasi deteksi secara signifikan tanpa mengorbankan kecepatan inferensi waktu nyata. Eksperimen menunjukkan model ini mencapai performa unggul pada dataset MS COCO dibanding model sekelas seperti YOLOv6 dan YOLOv8, serta menjadi pelopor implementasi pra-pelatihan mandiri (*self-supervised pretraining*) bergaya *Masked Autoencoder* (MAE) pada famili YOLO.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Dalam deteksi objek berbasis citra RGB, kemampuan mendeteksi objek dengan variasi skala yang ekstrem merupakan salah satu tantangan paling mendasar. Model detektor satu tahap modern, seperti seri YOLO, biasanya membagi arsitekturnya menjadi tiga bagian utama: *backbone* (untuk mengekstraksi fitur visual bertingkat dari citra masukan), *neck* (untuk menggabungkan fitur multiskala tersebut), dan *head* (untuk memprediksi koordinat *bounding box* dan probabilitas kelas). Secara historis, struktur *neck* seperti FPN memperkenalkan jalur atas-ke-bawah (*top-down*) untuk menyuntikkan informasi semantik tingkat tinggi ke lapisan spasial bawah, sedangkan PANet menambahkan jalur bawah-ke-atas (*bottom-up*) untuk mentransfer detail spasial kembali ke atas.

Namun, fusi rekursif bertahap pada FPN dan PANet memiliki kelemahan inheren berupa hilangnya informasi jarak jauh. Sebagai contoh, jika detail spasial halus dari peta fitur resolusi tinggi $B2$ ingin diintegrasikan dengan fitur semantik kaya di level $B5$, informasi tersebut harus mengalir secara berjenjang melalui lapisan perantara $B3$ dan $B4$. Di setiap langkah perantara, operasi konvolusi berulang dan kompresi saluran (*channel reduction*) secara perlahan mengikis detail informasi asli. Meskipun fusi global lintas-lapisan secara penuh dapat dilakukan menggunakan mekanisme atensi visual penuh (*global attention*), biaya komputasi kuadratisnya terlalu mahal untuk aplikasi waktu nyata yang harus berjalan pada perangkat tepi (*edge devices*) dengan keterbatasan daya. Oleh karena itu, diperlukan suatu metode fusi global efisien yang mampu menjembatani semua lapisan fitur tanpa meningkatkan latensi inferensi secara signifikan.

## Ide Utama

Gagasan inti dari Gold-YOLO adalah mendesain ulang interaksi fitur pada bagian *neck* dari model rantai bertahap menjadi model terpusat melalui mekanisme *Gather-and-Distribute* (GD). Alih-alih membiarkan informasi mengalir secara perlahan antar-lapisan tetangga, mekanisme GD mengumpulkan fitur dari semua lapisan secara paralel, meleburnya menjadi representasi global terpadu yang kaya akan konteks, lalu mendistribusikannya secara langsung ke tingkat-tingkat target pada piramida fitur.

Untuk mencapai efisiensi komputasi yang tinggi, proses GD ini dibagi menjadi dua cabang fusi yang disesuaikan dengan karakteristik fiturnya:
1. **Low-stage GD**: Bekerja pada fitur-fitur awal yang beresolusi tinggi (dari tingkat $B2$ hingga $B5$) untuk mempertahankan detail spasial objek kecil. Karena ukuran spasial peta fitur ini besar, modul ini menggunakan blok konvolusi yang direparameterisasi (*reparameterized convolutions*) seperti *RepBlock* untuk menjaga operasi tetap cepat dan hemat memori.
2. **High-stage GD**: Bekerja pada fitur-fitur dalam yang kaya akan informasi semantik abstrak (dari tingkat $P3$ hingga $P5$). Karena ukuran spasial peta fitur ini sudah mengecil, modul ini menggunakan blok berbasis *Transformer* (atensi mandiri atau *self-attention*) untuk memodelkan hubungan spasial-semantik global jarak jauh secara optimal.

Distribusi representasi global ini ke jalur deteksi utama tidak dilakukan melalui penjumlahan sederhana, melainkan menggunakan modul *Information Injection* (Injector) berbasis *gated attention* (atensi berpagar). Modul Injector ini secara dinamis menyaring informasi global mana yang relevan untuk memperkuat fitur lokal pada setiap tingkat deteksi tertentu.

## Cara Kerja Langkah demi Langkah

Mekanisme fusi dan distribusi informasi pada Gold-YOLO dapat divisualisasikan melalui diagram alir berikut:

```
       [Citra Input]
             │
        ┌────┴────┐
        │Backbone │
        └────┬────┘
      ┌───┬──┴┬───┐
     B2  B3  B4  B5  ◄─── Peta fitur multiskala dari backbone
      │   │   │   │
      └───┼───┼───┼──┐
          ▼   ▼   ▼  ▼
      ┌────────────────┐
      │  Low-stage GD  │ ◄─── (FAM + IFM RepBlock)
      └───────┬────────┘
        ┌─────┼─────┐
        ▼     ▼     ▼
       P3    P4    P5  ◄─── Injeksi fitur spasial tersaring
        │     │     │
        └─────┼─────┘
              ▼
      ┌────────────────┐
      │ High-stage GD  │ ◄─── (FAM + IFM Transformer)
      └───────┬────────┘
        ┌─────┼─────┐
        ▼     ▼     ▼
       N3    N4    N5  ◄─── Injeksi konteks semantik global
        │     │     │
        ▼     ▼     ▼
      ┌────────────────┐
      │ Detection Head │ ◄─── Prediksi koordinat & kelas
      └────────────────┘
```

Proses pemrosesan fitur ini berlangsung melalui tahapan-tahapan sistematis berikut:

### 1. Aliran Fitur Awal dari Backbone
Citra masukan beresolusi $640 \times 640$ piksel dimasukkan ke dalam *backbone* ekstraksi fitur. *Backbone* menghasilkan empat peta fitur bertingkat dengan dimensi spasial yang berbeda:
- $B2$: resolusi $160 \times 160$ piksel, dengan jumlah saluran $C_2$.
- $B3$: resolusi $80 \times 80$ piksel, dengan jumlah saluran $C_3$.
- $B4$: resolusi $40 \times 40$ piksel, dengan jumlah saluran $C_4$.
- $B5$: resolusi $20 \times 20$ piksel, dengan jumlah saluran $C_5$.

### 2. Modul Penyelaras Fitur (Feature Alignment Module - FAM)
Sebelum fitur-fitur dari berbagai tingkat dapat digabungkan, dimensi spasial dan jumlah saluran mereka harus diselaraskan. Tugas ini dijalankan oleh FAM.
- Di dalam **Low-stage FAM**, semua peta fitur $\{B2, B3, B4, B5\}$ diselaraskan ke resolusi target yang setara dengan dimensi $B3$ ($80 \times 80$ piksel). Penyelarasan dilakukan dengan cara menurunkan sampel (*downsampling*) peta fitur resolusi tinggi $B2$ ($160 \times 160$) menggunakan penapisan rata-rata (*average pooling*) berukuran $2\times 2$ menjadi $80 \times 80$. Sebaliknya, peta fitur beresolusi lebih rendah $B4$ ($40 \times 40$) dan $B5$ ($20 \times 20$) ditingkatkan sampelnya (*upsampled*) menggunakan interpolasi bilinear menjadi $80 \times 80$. Setelah semua dimensi spasial selaras pada ukuran $80 \times 80$ piksel, keempat tensor tersebut digabungkan sepanjang dimensi saluran (*channel concatenation*).
- Di dalam **High-stage FAM**, proses serupa dilakukan untuk menyelaraskan fitur $\{P3, P4, P5\}$ ke resolusi terkecil yaitu resolusi $P5$ ($20 \times 20$ piksel) menggunakan *average pooling*.

### 3. Modul Pelebur Informasi (Information Fusion Module - IFM)
Setelah diselaraskan oleh FAM, tensor gabungan dilebur di dalam IFM untuk menghasilkan satu representasi global yang padat.
- Pada **Low-stage IFM**, fusi fitur-fitur spasial resolusi tinggi dilakukan melalui blok *RepBlock* (blok konvolusi reparameterisasi). Blok ini menggunakan beberapa cabang konvolusi paralel saat pelatihan untuk mengekstrak representasi spasial yang kaya, yang kemudian dilebur secara matematis menjadi satu konvolusi $3\times 3$ tunggal saat inferensi. Hasil peleburan ini menghasilkan fitur global tingkat rendah yang disimbolkan sebagai $F_{align\_low}$.
- Pada **High-stage IFM**, fusi fitur-fitur semantik dalam dilakukan menggunakan blok *Transformer* dengan mekanisme atensi mandiri multi-kepala (*multi-head self-attention*). Blok ini menghitung hubungan ketergantungan jarak jauh antara seluruh piksel pada fitur tingkat tinggi untuk menghasilkan representasi global tingkat tinggi $F_{align\_high}$.

### 4. Modul Penyuntik Informasi (Information Injection Module - Injector)
Representasi global yang telah dilebur oleh IFM disuntikkan kembali ke jalur utama deteksi. Modul Injector menggunakan mekanisme atensi berpagar (*gated attention*) untuk mengontrol aliran informasi global secara adaptif.
Secara matematis, untuk tingkat fitur-$i$, proses injeksi dirumuskan sebagai:
$$F_{output} = F_{local\_i} + \text{Sigmoid}(\text{Conv}_{1\times 1}(F_{inj\_i})) \odot F_{local\_i}$$
Di sini, $F_{local\_i}$ adalah peta fitur lokal pada level-$i$. Peta fitur global $F_{inj\_i}$ disesuaikan dimensi spasialnya agar cocok dengan $F_{local\_i}$ menggunakan interpolasi bilinear (jika perlu ditingkatkan sampelnya) atau *average pooling* (jika perlu diturunkan sampelnya). Operasi konvolusi $1\times 1$ digunakan untuk menyelaraskan jumlah saluran. Hasilnya dilewatkan ke fungsi *Sigmoid* untuk menghasilkan peta atensi (*attention map*) spasial-saluran dengan nilai rentang $[0, 1]$. Peta atensi ini kemudian dikalikan secara elemen demi elemen (*element-wise multiplication* yang disimbolkan $\odot$) dengan fitur lokal asli, lalu ditambahkan kembali ke fitur lokal tersebut melalui koneksi residual.

### 5. Lightweight Adjacent-Layer Fusion (LAF)
Untuk memperkuat fusi lokal tanpa membebani komputasi global, Gold-YOLO mengintegrasikan modul LAF. Sebelum fitur lokal diproses oleh Injector, modul LAF mengalirkan informasi secara langsung dari lapisan yang bertetangga dekat (misalnya, menggabungkan fitur dari $P3$ dan $P5$ langsung ke $P4$). Hal ini memastikan transisi skala antar-lapisan tetap halus dan konsisten.

### 6. Pra-pelatihan Mandiri Bergaya MAE
Sebagai tambahan peningkatan akurasi, *backbone* detektor Gold-YOLO dilatih terlebih dahulu secara mandiri menggunakan skema MAE pada dataset ImageNet-1K. Selama pra-pelatihan, sebagian besar area citra ditutupi (dimasker), dan jaringan dipaksa merekonstruksi kembali piksel yang hilang. Pendekatan ini membuat *backbone* memiliki representasi fitur visual awal yang sangat kuat sebelum disetel halus (*fine-tuning*) pada dataset MS COCO untuk tugas deteksi objek akhir.

## Eksperimen dan Hasil

Evaluasi performa Gold-YOLO dilakukan pada dataset tolok ukur deteksi objek MS COCO val2017. Evaluasi ini membandingkan akurasi deteksi menggunakan metrik *mean Average Precision* pada rentang ambang IoU (*Intersection over Union*) 0,5 hingga 0,95 ($mAP_{val}$), jumlah parameter (dalam juta, M), biaya komputasi (dalam GFLOPs), dan kecepatan inferensi (dalam *millisecond*, ms).

Hasil eksperimen utama untuk varian model Gold-YOLO pada resolusi citra masukan $640 \times 640$ piksel dirangkum dalam tabel berikut:

| Model | Parameter (M) | FLOPs (G) | mAP (val 0.5:0.95) (%) | Latensi T4 (ms) |
|---|---|---|---|---|
| Gold-YOLO-N | 5,6 | 12,1 | 39,9 | 2,7 |
| Gold-YOLO-S | 21,5 | 46,0 | 46,4 | 4,2 |
| Gold-YOLO-M | 41,3 | 87,5 | 51,1 | 6,5 |
| Gold-YOLO-L | 75,1 | 151,7 | 53,3 | 9,8 |

*(Catatan: Latensi diukur pada GPU NVIDIA Tesla T4 menggunakan pustaka akselerasi TensorRT dengan presisi FP16 pada resolusi 640x640).*

Interpretasi hasil eksperimen ini menunjukkan efisiensi tinggi dari mekanisme GD dibandingkan model-model pembanding:
- **Gold-YOLO-N** (model terkecil) meraih akurasi $39,9\%$ mAP dengan hanya $5,6\text{ M}$ parameter. Hasil ini mengungguli model baseline YOLOv6-N ($37,5\%$ mAP) sebesar +2,4% mAP pada latensi yang setara, serta mengungguli YOLOv8-N ($37,3\%$ mAP) sebesar +2,6% mAP.
- **Gold-YOLO-S** meraih $46,4\%$ mAP, melampaui YOLOv6-S ($43,8\%$ mAP) sebesar +2,6% mAP dan YOLOv8-S ($44,9\%$ mAP) sebesar +1,5% mAP.
- Varian **Gold-YOLO-M** ($51,1\%$ mAP) dan **Gold-YOLO-L** ($53,3\%$ mAP) secara konsisten mengungguli detektor-detektor waktu nyata sekelas pada anggaran latensi yang sama.

Studi ablasi (*ablation study*) dalam makalah mengonfirmasi bahwa kontribusi peningkatan akurasi terbesar disumbangkan oleh modul *Gather-and-Distribute* (GD) pada *neck*, disusul oleh modul injeksi informasi (Injector), dan disempurnakan oleh inisialisasi bobot melalui pra-pelatihan bergaya MAE.

## Kelebihan dan Keterbatasan

### Kelebihan
- **Fusi Fitur Global Efektif**: Gold-YOLO memecahkan masalah redaman informasi spasial-semantik lintas-lapisan yang jauh dengan mengumpulkan seluruh fitur ke hub terpusat dan menyebarkannya secara langsung.
- **Latensi Rendah**: Pembagian kerja antara Low-stage GD (RepBlock konvolusional) and High-stage GD (Transformer) menjaga latensi inferensi tetap berada pada batas waktu nyata untuk perangkat tepi.
- **Akurasi Tinggi Objek Kecil**: Penyelarasan resolusi spasial tinggi pada tingkat *Low-stage* serta penapisan selektif oleh modul Injector membuat deteksi objek berukuran kecil meningkat secara signifikan.
- **Inisialisasi Bobot Optimal**: Implementasi pra-pelatihan mandiri bergaya MAE memberikan transfer representasi visual awal yang jauh lebih kuat dibanding pelatihan dari nol (*training from scratch*).

### Keterbatasan
- **Kompleksitas Implementasi Tinggi**: Secara rekayasa perangkat lunak, struktur *neck* yang memisahkan aliran data menjadi Low-stage dan High-stage GD lebih rumit untuk dimodifikasi secara manual atau disesuaikan dengan arsitektur *backbone* kustom di luar bawaannya.
- **Ketergantungan Akselerasi Perangkat Keras**: Penggunaan modul *Transformer* (atensi mandiri) pada High-stage IFM membutuhkan memori GPU yang cukup besar saat inferensi jika tidak dioptimalkan dengan TensorRT. Tanpa optimasi kompilator perangkat keras, kecepatan inferensi pada CPU perangkat tepi dapat turun drastis.
- **Biaya Pra-pelatihan Sangat Besar**: Konseptual pra-pelatihan MAE pada dataset ImageNet-1K membutuhkan sumber daya komputasi (GPU) dan waktu pelatihan yang sangat besar sebelum model dapat disetel halus untuk deteksi objek.

## Kaitan dengan Bab Lain

Gold-YOLO berdiri di atas fondasi deteksi satu tahap berbasis regresi yang diletakkan oleh YOLOv1 (Bab [001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)). Dari sisi garis silsilah arsitektur, Gold-YOLO mengadopsi struktur *backbone* dan *head* dari YOLOv6, namun mengganti bagian *neck* RepPAN konvensional dengan mekanismenya sendiri. Model ini bertindak sebagai pembanding langsung bagi detektor waktu nyata modern lainnya seperti YOLOv8 dan RT-DETR (Bab [155](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md)), di mana RT-DETR memilih membuang komponen NMS (*Non-Maximum Suppression*) sepenuhnya menggunakan arsitektur berbasis *Query Transformer*.

Penerapan mekanisme atensi mandiri pada *High-stage IFM* Gold-YOLO juga dipengaruhi oleh keberhasilan pemodelan visual global jarak jauh yang ditunjukkan oleh arsitektur *backbone* Transformer seperti Swin Transformer V2 (Bab [163](./163%20-%202022%20-%20Swin%20Transformer%20V2%20-%20Fondasi%20RGB.md)) dan perbaikan konvolusi modern pada ConvNeXt (Bab [162](./162%20-%202022%20-%20ConvNeXt%20-%20Fondasi%20RGB.md)). Selain itu, konsep fusi global terpusat ini memberikan alternatif arsitektur bagi detektor berbasis teks-citra seperti YOLO-World (Bab [156](./156%20-%202024%20-%20YOLO-World%20-%20Fondasi%20RGB.md)) dalam menyelaraskan representasi visual dengan token bahasa secara global.

## Poin untuk Sitasi

Kutip makalah ini dengan kunci BibTeX: `wang2023goldyolo`.

Ringkasan aman untuk dikutip dalam tinjauan pustaka:
> "Gold-YOLO memperkenalkan mekanisme Gather-and-Distribute (GD) pada bagian neck detektor untuk mengatasi kelemahan transmisi bertahap FPN/PAN. Dengan mengumpulkan seluruh fitur ke dalam hub terpusat dan mendistribusikannya kembali secara langsung menggunakan modul Injector atensi berpagar, Gold-YOLO meningkatkan akurasi deteksi multi-skala pada dataset MS COCO (39,9% hingga 53,3% mAP) dengan tetap mempertahankan kecepatan inferensi waktu nyata."

Catatan verifikasi sebelum sitasi formal:
- Pastikan angka latensi yang diukur pada GPU Tesla T4 (2,7 ms hingga 9,8 ms) tidak tertukar dengan kecepatan FPS mentah tanpa TensorRT.
- Konfirmasikan bahwa versi baseline YOLOv6 yang digunakan sebagai pembanding utama adalah YOLOv6 v3.0, karena versi ini menentukan keadilan perbandingan performa pada bab eksperimen.
- Validasi keberhasilan transfer bobot pra-pelatihan MAE pada citra masukan terhadap dataset khusus di luar MS COCO jika model ini diterapkan pada tugas klasifikasi atau segmentasi hilir.
