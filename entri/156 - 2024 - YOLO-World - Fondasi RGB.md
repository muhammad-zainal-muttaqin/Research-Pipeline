# 156 - YOLO-World: Real-Time Open-Vocabulary Object Detection

## Metadata Ringkas
| Atribut | Nilai |
|---|---|
| Kunci BibTeX | `cheng2024yoloworld` |
| Judul asli | YOLO-World: Real-Time Open-Vocabulary Object Detection |
| Penulis | Cheng, Tianheng; Song, Lin; Ge, Yixiao; Liu, Wenyu; Wang, Xinggang; Shan, Ying |
| Tahun | 2024 |
| Venue | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2401.17270
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=YOLO-World%3A%20Real-Time%20Open-Vocabulary%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=YOLO-World%3A%20Real-Time%20Open-Vocabulary%20Object%20Detection&sort=relevance

## Gambaran Umum
YOLO-World memperkenalkan kerangka kerja deteksi objek *open-vocabulary* yang mampu beroperasi secara *real-time*. Model ini melampaui batasan detektor tradisional yang hanya mampu mendeteksi kategori objek dalam set tertutup yang telah ditentukan sebelumnya. Dengan mengintegrasikan efisiensi arsitektur deteksi YOLOv8 dan kekuatan representasi semantik bahasa dari *Contrastive Language-Image Pre-training* (CLIP), YOLO-World mampu mengenali berbagai macam objek secara *zero-shot* hanya berdasarkan input *prompt* teks deskriptif dari pengguna.

Masalah utama yang diselesaikan oleh YOLO-World adalah tingginya latensi komputasi pada detektor kosakata terbuka berbasis *transformer* terdahulu. Kerangka kerja ini mengadopsi modul *Re-parameterizable Vision-Language Path Aggregation Network* (RepVL-PAN) untuk memfasilitasi fusi informasi multi-skala yang efisien antara fitur visual dan tekstual. Melalui skema *prompt-then-detect*, *embeddings* teks dari *prompt* pengguna dapat diparameterisasikan ulang secara *offline* menjadi bobot klasifikasi visual. Hal ini membuang kebutuhan untuk menjalankan *text encoder* saat inferensi, sehingga model dapat mempertahankan kecepatan tinggi khas keluarga YOLO untuk kebutuhan aplikasi dunia nyata.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Sebelum kemunculan YOLO-World, ranah deteksi objek didominasi oleh dua paradigma dengan kompromi yang bertolak belakang:
1. **Detektor Kelas Tertutup (*Closed-Set Detectors*):** Model satu-tahap (*one-stage*) seperti YOLOv8 sangat cepat dan efisien untuk kebutuhan komputasi praktis. Namun, model ini dibatasi oleh dataset pelatihan yang memiliki jumlah kategori kelas tetap (seperti 80 kelas pada COCO). Apabila terdapat kebutuhan untuk mendeteksi objek baru, pengembang harus mengumpulkan data anotasi baru, menggabungkannya, dan melakukan pelatihan ulang (*retraining*) dari awal, yang memakan waktu dan biaya komputasi yang besar.
2. **Detektor Kosakata Terbuka (*Open-Vocabulary Detectors*):** Model seperti GLIP atau Grounding DINO memanfaatkan *text encoder* untuk menyelaraskan fitur regional visual dengan representasi bahasa guna mengenali kelas baru tanpa pelatihan ulang. Namun, penyelarasan ini sangat bergantung pada arsitektur berbasis *transformer* dengan mekanisme *self-attention* lintas-modal yang intensif secara komputasi. Akibatnya, model-model ini memiliki kecepatan inferensi yang sangat lambat (sering kali di bawah 10 FPS), sehingga tidak layak untuk diterapkan pada skenario waktu nyata atau pada perangkat keras dengan daya komputasi terbatas (*edge devices*).

Kesenjangan ini memicu urgensi untuk mengembangkan arsitektur detektor yang tidak hanya fleksibel dalam mendeteksi objek apa pun melalui instruksi bahasa, tetapi juga cukup ringan untuk dieksekusi secara *real-time* di lingkungan industri.

## Ide Utama
Gagasan utama di balik YOLO-World adalah memisahkan proses ekstraksi representasi bahasa dari proses deteksi visual menggunakan paradigma *prompt-then-detect*. Secara konseptual, alih-alih memproses teks dan citra secara bersamaan pada setiap bingkai (*frame*) video, *prompt* kosakata dari pengguna dikodekan terlebih dahulu menjadi vektor representasi statis (*text embeddings*).

Mekanisme ini memanfaatkan *text encoder* CLIP yang dibekukan (*frozen*) untuk memproyeksikan daftar nama objek menjadi *embeddings* tekstual. Melalui modul RepVL-PAN, representasi teks ini diselaraskan dengan fitur gambar multi-skala selama fase pelatihan. Pada saat inferensi, *embeddings* bahasa yang telah diselaraskan tersebut ditransformasikan secara matematis menjadi parameter filter lapisan konvolusi atau proyeksi linear pada kepala klasifikasi detektor. Dengan melipat (*folding*) informasi tekstual langsung ke dalam parameter visual secara *offline*, model dapat melakukan deteksi kosakata terbuka tanpa perlu menjalankan modul *text encoder* yang berat selama inferensi langsung.

## Cara Kerja Langkah demi Langkah
Operasi deteksi objek kosakata terbuka pada YOLO-World diimplementasikan melalui tahapan terstruktur berikut:

### 1. Ekstraksi Fitur Citra (Visual Backbone)
Citra masukan dilewatkan melalui jaringan tulang punggung (*backbone*) visual berbasis CSPDarknet milik YOLOv8. Jaringan ini mengekstrak representasi fitur spasial multi-skala pada tingkat resolusi $C_3$, $C_4$, dan $C_5$. Langkah ini penting untuk mendeteksi objek dengan variasi ukuran spasial yang berbeda dalam sebuah gambar.

### 2. Pengodean Teks (Frozen Text Encoder)
Secara paralel, daftar kosakata objek yang ingin dideteksi (misalnya "gelas plastik", "kucing hitam", "rambu lalu lintas") dimasukkan ke dalam *text encoder* CLIP (menggunakan varian ViT-B/32). Untuk mempertahankan pengetahuan semantik luas yang telah dipelajari CLIP dari ratusan juta pasangan citra-teks, bobot dari *text encoder* ini sepenuhnya dibekukan selama proses pelatihan detektor. Output dari tahap ini adalah matriks *embeddings* teks $W \in \mathbb{R}^{C \times D}$, dengan $C$ mewakili jumlah kelas kosakata dan $D$ melambangkan dimensi representasi (512 dimensi).

### 3. Fusi Informasi Dua Arah di RepVL-PAN
Fitur gambar multi-skala dan *embeddings* teks dimasukkan ke dalam RepVL-PAN yang menggantikan modul PAN tradisional pada YOLOv8. RepVL-PAN melakukan fusi informasi lintas-modal dua arah menggunakan dua komponen utama:
*   **Text-guided CSPLayer (T-CSPLayer):** Komponen ini menyuntikkan panduan bahasa ke dalam fitur gambar. Di setiap skala fitur visual $X_l$, model menghitung bobot perhatian spasial menggunakan mekanisme *Max-Sigmoid Attention*. Persamaan untuk pembaruan fitur gambar ini adalah:
    $$X'_l = X_l \cdot \delta\left(\max_{j \in \{1 \dots C\}} (X_l W_j^\top)\right)^\top$$
    Di sini, $\delta$ melambangkan fungsi aktivasi sigmoid yang menormalisasi bobot perhatian antara nilai 0 dan 1. Operasi $\max$ di sepanjang dimensi kelas memastikan bahwa fitur visual hanya memusatkan perhatian pada area spasial yang relevan dengan *prompt* teks mana pun dalam kosakata yang diberikan.
*   **Image-Pooling Attention (I-Pooling Attention):** Untuk memberikan umpan balik visual ke domain bahasa, fitur visual multi-skala direduksi melalui operasi *max-pooling* menjadi representasi regional ringkas $\tilde{X} \in \mathbb{R}^{N \times D_{vis}}$, di mana $N$ mewakili jumlah token wilayah visual. Representasi regional ini kemudian digunakan untuk memperbarui *embeddings* teks asli melalui mekanisme perhatian multi-kepala (*Multi-Head Attention*):
    $$W' = W + \text{MultiHead-Attention}(W, \tilde{X}, \tilde{X})$$
    Proses ini membuat representasi teks menjadi sadar visual (*image-aware*), menyesuaikan pemahaman semantik kata dengan karakteristik gambar yang sedang diproses.

### 4. Kepala Klasifikasi Kontrastif
Setelah fitur gambar dan teks diselaraskan di RepVL-PAN, kepala detektor menghasilkan prediksi koordinat kotak pembatas (*bounding box*) dan representasi wilayah visual $e_k$ untuk setiap kandidat objek. Skor probabilitas deteksi $s_{k,j}$ untuk objek ke-$k$ terhadap kelas teks ke-$j$ dihitung menggunakan kemiripan kosinus (*cosine similarity*):
$$s_{k,j} = \alpha \cdot \text{L2-Norm}(e_k) \cdot \text{L2-Norm}(w_j)^\top + \beta$$
Di mana $\alpha$ dan $\beta$ adalah parameter skala dan pergeseran yang dapat dipelajari untuk menstabilkan distribusi nilai skor selama proses pelatihan.

### 5. Reparameterisasi Inferensi (*Offline Vocabulary*)
Pada fase penerapan praktis, pengguna menentukan daftar kosakata target sekali di awal. Matriks klasifikasi *offline* dihitung dengan menormalisasi representasi teks yang telah diperbarui:
$$W_{cl} = \text{L2-Norm}(W')$$
Matriks $W_{cl}$ ini kemudian dimasukkan langsung sebagai parameter bobot pada lapisan proyeksi linear terakhir di kepala detektor. Modul *text encoder* CLIP dan operasi fusi lintas-modal dalam RepVL-PAN dinonaktifkan sepenuhnya. Selama proses inferensi berjalan, model hanya mengeksekusi operasi konvolusi visual murni pada citra masukan dengan bobot klasifikasi yang telah disesuaikan secara dinamis tersebut.

```
[ Citra ] ---> [ YOLOv8 Backbone ] ───> Fitur Multi-Skala (C3, C4, C5)
                                                      │
                                                      ▼
[ Teks  ] ---> [ CLIP Text Encoder ] ──> [ RepVL-PAN (Fusi Fitur) ]
                  (Frozen ViT-B/32)     ├── T-CSPLayer (Max-Sigmoid Attn)
                                        └── I-Pooling Attention (MHA)
                                                      │
                                                      ▼
                                           [ Fitur Terpadu Lintas-Modal ]
                                                      │
                                                      ▼
                                           [ Contrastive Head ]
                                                      │
                                                      ▼
                                           [ Box & Klasifikasi Objek ]
```

## Eksperimen dan Hasil
YOLO-World dilatih terlebih dahulu (*pre-trained*) menggunakan dataset deteksi berskala besar yang mencakup Objects365 (V1), GoldG (gabungan grounding dari GQA dan Flickr30k), serta sampel citra-teks dari CC3M. Model kemudian diuji secara *zero-shot* pada dataset LVIS yang memiliki kosakata sangat luas (1.203 kelas objek) untuk memvalidasi kemampuannya dalam mendeteksi kelas objek langka (*rare categories*).

Evaluasi yang dilakukan pada kartu grafis NVIDIA V100 menunjukkan hasil performa berikut:
*   **YOLO-World-S (Small):** Memiliki parameter visual sekitar 13 juta. Model ini memperoleh nilai Average Precision (AP) sebesar `26,2` pada LVIS *zero-shot* dengan kecepatan mencapai `74,1 FPS`.
*   **YOLO-World-M (Medium):** Memiliki parameter visual sekitar 29 juta. Varian ini mencatatkan nilai AP berkisar antara `30,6` hingga `32,8` bergantung pada resolusi citra input yang digunakan.
*   **YOLO-World-L (Large):** Memiliki parameter visual sekitar 48 juta. Model ini menghasilkan akurasi tertinggi dengan nilai AP sebesar `35,4` serta kecepatan inferensi pada `52,0 FPS`.

Hasil transfer domain melalui *fine-tuning* pada dataset COCO menunjukkan bahwa bobot pra-pelatihan lintas-modal pada YOLO-World secara konsisten mempercepat konvergensi pelatihan dan menghasilkan akurasi yang kompetitif jika dibandingkan dengan detektor yang dilatih secara tertutup dari awal.

## Kelebihan dan Keterbatasan
**Kelebihan:**
*   **Efisiensi Komputasi Tinggi:** Paradigma *prompt-then-detect* memotong kebutuhan komputasi bahasa secara *online*. Hal ini menjadikannya salah satu dari sedikit detektor *open-vocabulary* yang siap digunakan pada lingkungan komputasi tepi secara *real-time*.
*   **Fleksibilitas Penggunaan:** Pengguna dapat memodifikasi daftar kelas objek secara dinamis melalui teks bahasa alami tanpa perlu mengumpulkan data anotasi baru atau melakukan pelatihan ulang model.
*   **Fusi Informasi Dua Arah:** Penggunaan RepVL-PAN yang menggabungkan T-CSPLayer dan I-Pooling Attention secara aktif menyelaraskan representasi visual dengan representasi tekstual secara simetris, menghasilkan visualisasi fitur yang sangat peka terhadap bahasa.

**Keterbatasan:**
*   **Ketergantungan pada Kualitas CLIP:** Karena performa klasifikasinya sangat bergantung pada *frozen text encoder* CLIP, model ini mewarisi kelemahan bawaan CLIP. Model sering kali gagal mendeteksi objek apabila *prompt* teks yang dimasukkan terlalu panjang, menggunakan struktur sintaksis yang rumit, atau merujuk pada konsep abstrak yang jarang ditemui dalam dataset pra-pelatihan CLIP.
*   **Akurasi Deteksi Objek Kecil:** Dari sisi rekayasa visual, sebagai model satu-tahap, YOLO-World masih memiliki performa deteksi objek kecil yang berada di bawah tingkat akurasi detektor berbasis *transformer* murni seperti Grounding DINO, meskipun unggul jauh dalam kecepatan komputasi.
*   **Kebutuhan Data Pra-Pelatihan:** Secara konseptual, pelatihan awal model kontrastif wilayah-teks membutuhkan volume data spasial-bahasa yang sangat besar dan proses kurasi data yang ketat agar penyelarasan modalitas tidak bias.

## Kaitan dengan Bab Lain
YOLO-World memiliki keterkaitan erat dengan beberapa bab lain dalam klaster **Fondasi RGB**:
*   [001 - You Only Look Once (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20(YOLOv1)%20-%20Fondasi%20RGB.md): Hubungan silsilah mendasar. YOLOv1 merintis konsep deteksi objek satu-tahap yang memprediksi koordinat kotak pembatas dan kelas secara simultan, yang kemudian disempurnakan hingga YOLOv8 dan akhirnya diadopsi oleh YOLO-World untuk deteksi kosakata terbuka.
*   [155 - RT-DETR](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md): RT-DETR menawarkan deteksi *real-time* berbasis arsitektur *transformer* (DETR) namun terbatas pada set kelas tertutup. YOLO-World memberikan alternatif deteksi kosakata terbuka berkecepatan tinggi dengan mengandalkan arsitektur konvolusional (YOLOv8 backbone) yang direparameterisasi untuk menghindari beban komputasi *self-attention* global yang ada pada RT-DETR.
*   [157 - Gold-YOLO](./157%20-%202023%20-%20Gold-YOLO%20-%20Fondasi%20RGB.md): Model ini memperkenalkan mekanisme *Gather-and-Distribute PAN* (GD-PAN) untuk meningkatkan transmisi informasi visual multi-skala secara efisien. RepVL-PAN pada YOLO-World mengadaptasi struktur PAN serupa tetapi dengan penekanan pada interaksi lintas-modal dua arah antara visi dan bahasa.
*   [158 - DINO detector](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md): DINO merupakan salah satu model deteksi berbasis *transformer* paling akurat untuk evaluasi set tertutup, dan variannya (Grounding DINO) mendominasi akurasi *open-vocabulary*. YOLO-World memposisikan diri sebagai alternatif praktis yang menukar sedikit akurasi Grounding DINO untuk mendapatkan kecepatan inferensi hingga 20 kali lipat lebih cepat demi mendukung skenario operasional waktu nyata.

## Poin untuk Sitasi
Kunci BibTeX:
```bibtex
@inproceedings{cheng2024yoloworld,
  title={YOLO-World: Real-Time Open-Vocabulary Object Detection},
  author={Cheng, Tianheng and Song, Lin and Ge, Yixiao and Liu, Wenyu and Wang, Xinggang and Shan, Ying},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={16901--16911},
  year={2024}
}
```

Kutipan Ringkas untuk Tinjauan Pustaka:
YOLO-World (Cheng dkk., 2024) adalah model deteksi objek *open-vocabulary* satu-tahap berbasis YOLOv8. Model ini menggunakan modul *Re-parameterizable Vision-Language Path Aggregation Network* (RepVL-PAN) untuk interaksi dua arah antara fitur citra dan *embeddings* teks CLIP. Dengan reparameterisasi *offline*, model ini mampu membuang komponen pemrosesan bahasa saat waktu inferensi sehingga dapat berjalan secara *real-time*.

Catatan Angka untuk Verifikasi:
Klaim kinerja deteksi *zero-shot* pada LVIS sebesar 26,2 AP (YOLO-World-S pada 74,1 FPS) dan 35,4 AP (YOLO-World-L pada 52,0 FPS) diukur pada GPU NVIDIA V100 dengan resolusi gambar masukan sebesar 640×640 piksel. Angka-angka ini perlu diverifikasi dengan Tabel 2 pada naskah CVPR 2024 resmi. Kecepatan FPS dilaporkan menggunakan reparameterisasi *offline* penuh tanpa menyertakan latensi dari pengoperasian *text encoder* CLIP.
