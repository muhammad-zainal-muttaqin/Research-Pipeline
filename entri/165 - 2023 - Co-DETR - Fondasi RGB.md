# 165 - DETRs with Collaborative Hybrid Assignments Training

## Metadata Ringkas
| Atribut | Nilai |
|---|---|
| Kunci BibTeX | `zong2023codetr` |
| Judul asli | DETRs with Collaborative Hybrid Assignments Training |
| Penulis | Zhuofan Zong, Guanglu Song, Yu Liu |
| Tahun | 2023 |
| Venue | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) |
| Tema | Fondasi RGB |

## Tautan Akses
- arXiv: https://arxiv.org/abs/2211.12860
- Google Scholar: https://scholar.google.com/scholar?q=DETRs%20with%20Collaborative%20Hybrid%20Assignments%20Training
- Semantic Scholar: https://www.semanticscholar.org/search?q=DETRs%20with%20Collaborative%20Hybrid%20Assignments%20Training&sort=relevance

## Gambaran Umum
*DEtection TRansformer* (DETR) memperkenalkan paradigma deteksi objek *end-to-end* bebas *Non-Maximum Suppression* (NMS) berbasis pencocokan satu-ke-satu (*one-to-one set matching*). Namun, pencocokan ini menyebabkan supervisi jarang (*sparse supervision*) pada keluaran *encoder*. Hanya sedikit kueri yang mendapat label positif saat pelatihan, menghambat pembelajaran fitur diskriminatif oleh *encoder* dan memperlambat konvergensi.

*Collaborative Hybrid Assignments Training* (Co-DETR) mengatasi masalah ini dengan mengintegrasikan beberapa kepala bantu (*auxiliary heads*) paralel bersupervisi satu-ke-banyak (*one-to-many*) seperti *Adaptive Training Sample Selection* (ATSS) dan Faster R-CNN selama pelatihan. Skema ini memaksa *encoder* mempelajari fitur spasial yang padat. Koordinat positif dari kepala bantu diekstraksi menjadi kueri positif kustom (*customized positive queries*) untuk mempercepat pembelajaran atensi *decoder*. Saat inferensi, seluruh kepala bantu dibuang sehingga model beroperasi tanpa beban komputasi tambahan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
DETR (022) mengubah paradigma deteksi objek dengan merumuskan tugas sebagai prediksi himpunan langsung via pencocokan bipartit satu-ke-satu. Pendekatan ini mengeliminasi komponen NMS buatan tangan dan kotak acuan (*anchor box*). Namun, DETR membutuhkan konvergensi pelatihan yang sangat lambat (hingga 500 epoch) dan kinerjanya tertinggal dari detektor berbasis CNN pada skala tertentu.

Upaya seperti *Deformable DETR* (023) dan *DN-DETR* (159) mempercepat konvergensi pada sisi *decoder* lewat atensi lokal terdeformasi dan latihan denoising. Namun, masalah kurangnya efisiensi fitur *encoder* belum teratasi. Pada DETR standar, representasi spasial *encoder* disupervisi secara tidak langsung melalui *decoder* satu-ke-satu. Karena jumlah objek dalam citra sedikit dibanding total piksel, hanya sebagian kecil token fitur *encoder* yang menerima gradien supervisi positif. Token lainnya dipaksa menjadi latar belakang (*background*). Supervisi yang jarang ini menghambat *encoder* mempelajari fitur visual diskriminatif. Sebaliknya, detektor konvensional menggunakan penetapan satu-ke-banyak (*one-to-many*) di mana beberapa *anchor* dipasangkan ke satu objek target, menghasilkan supervisi yang jauh lebih padat pada fitur representasional.

## Ide Utama
Ide utama Co-DETR adalah menggabungkan keunggulan supervisi padat skema satu-ke-banyak (*one-to-many*) tradisional untuk melatih *encoder*, sementara *decoder* utama tetap menggunakan skema satu-ke-satu (*one-to-one*) demi mempertahankan deteksi *end-to-end* tanpa NMS. Pendekatan ini dinamakan pelatihan kolaboratif hibrida.

Fitur multi-skala hasil *encoder* dikirim ke kepala *decoder* DETR utama dan beberapa kepala bantu satu-ke-banyak secara paralel. Kepala bantu bertindak sebagai pengawas tambahan yang memaksa *encoder* mempelajari fitur di seluruh area potensial objek, bukan hanya representasi tunggal dari pencocokan Hungarian. Umpan balik gradien dari kepala-kepala bantu diakumulasikan untuk memperbarui parameter *encoder*. Selain itu, koordinat spasial positif kepala bantu diekstraksi menjadi kueri tambahan untuk mempercepat pembelajaran *decoder*. Seluruh kepala bantu ini dibuang saat inferensi, sehingga model hasil pelatihan tetap berupa detektor DETR standar yang efisien tanpa parameter tambahan pada data uji.

## Cara Kerja Langkah demi Langkah

### Aliran Data Utama dan Ekstraksi Fitur Multi-Skala
Aliran data dimulai dengan memproses citra masukan melalui *backbone* untuk menghasilkan peta fitur multi-skala. Pada citra masukan beresolusi $800 \times 800$ piksel, *backbone* mengekstrak fitur pada resolusi spasial yang menurun, misalnya tingkat C3 ($100 \times 100$ piksel), C4 ($50 \times 50$ piksel), dan C5 ($25 \times 25$ piksel). Fitur multi-skala ini diratakan dan dimasukkan ke dalam *encoder* Transformer (seperti *Deformable Encoder*) untuk menghasilkan representasi fitur terenkode dengan dimensi spasial yang sama.

```
                             ┌──────────────┐
                             │ Citra Input  │
                             └──────┬───────┘
                                    ▼
                             ┌──────────────┐
                             │   Backbone   │
                             └──────┬───────┘
                                    ▼
                             ┌──────────────┐
                             │   Encoder    │
                             └───┬───┬───┬──┘
                                 │   │   │  (Fitur Encoder Berbagi)
        ┌────────────────────────┘   │   └───────────────────────┐
        ▼                            ▼                           ▼
┌──────────────┐             ┌──────────────┐             ┌──────────────┐
│  Aux Head 1  │             │  Aux Head 2  │             │   Decoder    │
│ (One-to-Many)│             │ (One-to-Many)│             │ (One-to-One) │
│  [ATSS/FCOS] │             │ [Faster RCN] │             └──────┬───────┘
└──────┬───────┘             └──────┬───────┘                    │
       │                            │                            │
       └──────────────┬─────────────┘                            │
                      ▼                                          │
       (Koordinat Positif Diekstraksi)                           │
                      │                                          │
                      ▼                                          │
       ┌──────────────────────────────┐                          │
       │ Customized Positive Queries  │                          │
       └──────────────┬───────────────┘                          │
                      └──────────────────────────────────────────┼───┐
                                                                 ▼   ▼
                                                            ┌──────────────┐
                                                            │ Prediksi Box │
                                                            └──────────────┘
                                                             (Hanya Cabang
                                                             Utama Digunakan
                                                             saat Inferensi)
```

### Pelatihan Kolaboratif dengan Kepala Bantu Satu-ke-Banyak
Fitur terenkode multi-skala dari *encoder* didistribusikan ke kepala detektor utama (DETR) dan $M$ kepala bantu paralel. Setiap kepala bantu dikonfigurasi menggunakan metode deteksi tradisional seperti ATSS (menetapkan sampel positif secara adaptif berdasarkan kalkulasi statistik jarak terdekat dan IoU) atau FCOS (pemetaan objek secara *anchor-free* berdasarkan pusat piksel).

Sebagai contoh, jika menggunakan kepala ATSS, metode ini menetapkan beberapa token fitur spasial dekat pusat objek sebagai sampel positif. Ini memberikan pengawasan padat kepada *encoder* karena banyak token didorong untuk memprediksi kelas dan penyimpangan (*offset*) kotak pembatas (*bounding box*) objek target. Setiap kepala bantu menghitung nilai kerugiannya sendiri secara independen.

### Pembuatan Kueri Positif Kustom untuk Decoder
Selain memberikan supervisi gradien pada *encoder*, kepala bantu membantu mempercepat pelatihan *decoder*. Dari setiap kepala bantu, koordinat spasial ($x, y, w, h$) yang ditetapkan sebagai sampel positif diekstraksi. Koordinat ini merepresentasikan area yang sangat mungkin mengandung objek target (*foreground*).

Koordinat positif tersebut ditransformasikan menjadi kueri posisi (*positional queries*) tambahan untuk *decoder* utama. Pada fase pelatihan, $N$ buah kueri objek acak pada *decoder* ditambahkan dengan kueri positif kustom ini. Dengan menyajikan kueri yang terarah langsung ke lokasi objek positif kepada *decoder*, beban *decoder* dalam mempelajari atensi silang (*cross-attention*) berkurang signifikan, mempercepat konvergensi.

### Formulasi Fungsi Rugi Total
Fungsi rugi total $\mathcal{L}_{\text{total}}$ yang dioptimalkan selama pelatihan dirumuskan sebagai akumulasi bobot dari rugi detektor utama dan rugi seluruh kepala bantu:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{main}} + \sum_{i=1}^{M} \lambda_i \mathcal{L}_{\text{aux}}^{(i)}$$

Di mana $\mathcal{L}_{\text{main}}$ melambangkan fungsi rugi detektor DETR utama (mencakup *Hungarian classification*, *L1 regression*, dan *GIoU loss*). $\mathcal{L}_{\text{aux}}^{(i)}$ menyatakan fungsi rugi kepala bantu ke-$i$ (klasifikasi menggunakan *Focal Loss* dan regresi kotak pembatas menggunakan kombinasi *L1* dan *GIoU loss*). Parameter $\lambda_i$ bertindak sebagai koefisien bobot penyeimbang kontribusi setiap kepala bantu, yang biasanya diatur mendekati $1,0$.

### Proses Inferensi Tanpa Overhead
Setelah pelatihan selesai, seluruh kepala bantu dan mekanisme kueri positif kustom dilepaskan. Bobot parameter pada *encoder* dan *decoder* utama yang telah dioptimalkan disimpan. Pada fase inferensi, citra masukan hanya melewati *backbone*, *encoder*, and *decoder* utama menggunakan kueri standar. Karena jalur bantu tidak diproses, waktu komputasi, penggunaan memori GPU, dan latensi inferensi persis sama dengan detektor DETR dasar.

## Eksperimen dan Hasil
Evaluasi eksperimental Co-DETR dilakukan pada dataset MS COCO 2017 (118 ribu citra latih, 5 ribu citra validasi, dan 20 ribu citra *test-dev*). Arsitektur dasar yang diuji mencakup *DAB-DETR*, *Deformable DETR*, dan detektor *DINO*.

Pada pengujian menggunakan *Deformable DETR* dengan *backbone* ResNet-50 pada skema pelatihan singkat 12 epoch, Co-DETR meningkatkan performa dari 43,8% *mean Average Precision* (AP) menjadi 49,6% AP (+5,8% AP). Untuk skema pelatihan 36 epoch, performa meningkat dari 46,9% AP menjadi 50,1% AP (+3,2% AP). Peningkatan tinggi pada epoch awal membuktikan bahwa Co-DETR berhasil mempercepat konvergensi melalui supervisi padat pada fitur *encoder*.

Ketika diintegrasikan dengan detektor SOTA *DINO-Deformable-DETR* berbasis *Swin-L*, Co-DETR meningkatkan performa pada data validasi COCO dari 58,5% AP menjadi 59,5% AP (+1,0% AP). Dengan memanfaatkan *backbone* ViT-L (304 juta parameter) yang dilatih awal pada dataset Objects365, Co-DETR mencapai 66,0% AP pada COCO *test-dev* dan 67,9% AP pada LVIS val. Hasil ini menetapkan standar kinerja baru saat publikasi dan menunjukkan skalabilitas metode ke arsitektur model besar tanpa menambah beban komputasi ketika digunakan pada sistem produksi.

## Kelebihan dan Keterbatasan
Kelebihan utama Co-DETR terletak pada efisiensinya yang asimetris. Model diuntungkan oleh supervisi padat satu-ke-banyak selama pelatihan, namun tetap mempertahankan kesederhanaan arsitektur satu-ke-satu tanpa NMS saat inferensi. Hal ini sangat berguna untuk penerapan praktis karena tidak menambah operasi matematika (*FLOPs*) atau latensi inferensi pada perangkat target.

Namun, dari sisi rekayasa, keterbatasan utama Co-DETR adalah kebutuhan memori GPU (*VRAM*) yang melonjak selama pelatihan karena pengaktifan beberapa kepala bantu secara paralel di atas fitur multi-skala. Secara konseptual, jumlah kepala bantu juga memiliki batas optimal sekitar 4 kepala. Menambahkan lebih dari 6 kepala bantu justru menurunkan akurasi akibat timbulnya konflik penetapan label (*label assignment conflict*). Konflik ini terjadi ketika satu token fitur menerima instruksi gradien kontradiktif dari beberapa kepala bantu yang menerapkan kriteria sampel positif-negatif berbeda, menghambat pembaruan bobot *encoder*.

## Kaitan dengan Bab Lain
Co-DETR memiliki keterkaitan erat dengan beberapa bab dalam silsilah deteksi objek berbasis Transformer dan CNN:
- **[DETR (022)](./022%20-%202020%20-%20DETR%20-%20Fondasi%20RGB.md)**: Sebagai fondasi utama, DETR memperkenalkan paradigma deteksi *end-to-end* bebas NMS. Co-DETR secara langsung mengatasi kelemahan mendasar DETR berupa supervisi yang jarang pada *encoder*.
- **[Deformable DETR (023)](./023%20-%202021%20-%20Deformable%20DETR%20-%20Fondasi%20RGB.md)**: Co-DETR sering menggunakan Deformable DETR sebagai arsitektur dasar. Pembatasan atensi pada Deformable DETR dikombinasikan dengan supervisi padat Co-DETR menghasilkan konvergensi yang sangat cepat.
- **[Vision Transformer (ViT) (024)](./024%20-%202021%20-%20Vision%20Transformer%20(ViT)%20-%20Fondasi%20RGB.md)** dan **[Swin Transformer (025)](./025%20-%202021%20-%20Swin%20Transformer%20-%20Fondasi%20RGB.md)**: Kedua arsitektur ini bertindak sebagai *backbone* ekstraksi fitur yang digunakan oleh Co-DETR untuk mencapai performa akurasi puncak di atas 66,0% AP pada COCO.
- **[DINO detector (158)](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md)**: DINO merupakan salah satu model detektor dasar yang diintegrasikan dengan skema pelatihan Co-DETR untuk mencatatkan rekor akurasi tertinggi pada masanya.
- **[DN-DETR (159)](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md)**: Sementara DN-DETR berfokus pada stabilisasi *decoder* melalui latihan denoising, Co-DETR melengkapinya dengan memperkuat representasi *encoder* menggunakan skema hibrida kolaboratif.
- **[RT-DETR (155)](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md)**: RT-DETR berfokus pada kecepatan inferensi waktu nyata dengan merancang ulang *encoder*. Sebaliknya, Co-DETR berfokus pada akurasi maksimal dengan mengoptimalkan pelatihan *encoder* yang kompleks dan membuang seluruh modul tambahan saat inferensi.

## Poin untuk Sitasi
Kunci BibTeX: `zong2023codetr`

Ringkasan untuk sitasi:
"Co-DETR memperkenalkan kerangka kerja pelatihan kolaboratif hibrida yang menempatkan beberapa kepala bantu satu-ke-banyak (seperti ATSS dan Faster R-CNN) secara paralel di atas *encoder* DETR selama fase pelatihan. Metode ini memperkaya supervisi fitur *encoder* dan mempercepat konvergensi *decoder* melalui ekstraksi kueri positif kustom, tanpa memberikan beban komputasi tambahan atau parameter ekstra pada saat proses inferensi dijalankan."

Catatan verifikasi:
"Perlu diverifikasi apakah hasil 66,0% AP pada COCO *test-dev* menggunakan model ViT-L melibatkan teknik penambahan skala gambar masukan bervariasi (*multi-scale testing*) dan *Test-Time Augmentation* (TTA), serta pastikan kecukupan kapasitas memori GPU saat mereproduksi skema latihan dengan 4 kepala bantu paralel."
