# 159 - DN-DETR: Accelerate DETR Training by Introducing Query DeNoising

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2022dndetr` |
| Judul asli | DN-DETR: Accelerate DETR Training by Introducing Query DeNoising |
| Penulis | Feng Li, Hao Zhang, Shilong Liu, Jian Guo, Lionel M. Ni, Lei Zhang |
| Tahun | 2022 |
| Venue | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2022) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2203.01305
- **Google Scholar:** https://scholar.google.com/scholar?q=DN-DETR%3A%20Accelerate%20DETR%20Training%20by%20Introducing%20Query%20DeNoising
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=DN-DETR%3A%20Accelerate%20DETR%20Training%20by%20Introducing%20Query%20DeNoising&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan DN-DETR (*Denoising* DEtection TRansformer), metode pelatihan baru untuk mempercepat konvergensi model deteksi objek berbasis *transformer*. Sebelum penelitian ini, detektor keluarga DETR (*DEtection TRansformer*) membutuhkan ratusan *epoch* pelatihan untuk mencapai akurasi optimal. Penulis mengidentifikasi bahwa kelambatan konvergensi disebabkan oleh ketidakstabilan proses pencocokan bipartit (*bipartite matching*) menggunakan algoritme Hungarian pada awal pelatihan. Ketidakstabilan ini membuat target pembelajaran kueri *decoder* berfluktuasi secara acak antar-*epoch*, sehingga menghambat optimasi jaringan.

DN-DETR mengatasi masalah ini dengan mengintegrasikan tugas pembantu berupa rekonstruksi kotak pembatas (*bounding box*) dan klasifikasi kategori langsung dari kueri yang telah dirusak oleh derau (*noise*), yaitu *query denoising*. Jalur *denoising* ini tidak melewati pencocokan Hungarian, melainkan langsung dicocokkan secara deterministik dengan objek kebenaran acuan (*ground-truth*). Hal ini memberikan sinyal optimasi yang stabil sejak awal pelatihan tanpa memberikan beban komputasi tambahan (*overhead*) saat inferensi karena jalur *denoising* dibuang setelah pelatihan. Pada dataset COCO 2017, DN-DETR mencapai akurasi 43,4% AP dalam 12 *epoch*, dan mencapai 48,6% AP dalam 50 *epoch* menggunakan *backbone* ResNet-50.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Paradigma deteksi objek mengalami pergeseran penting dengan diperkenalkannya DETR ([bab 022](./022%20-%202020%20-%20DETR%20-%20Fondasi%20RGB.md)) yang merumuskan deteksi objek secara langsung sebagai masalah prediksi himpunan (*set prediction*). Detektor ini berhasil mengeliminasi kebutuhan akan komponen manual seperti *Non-Maximum Suppression* (NMS) dan kotak acuan (*anchor boxes*). Namun, kelemahan utama DETR orisinal terletak pada efisiensi pelatihannya: model memerlukan hingga 500 *epoch* untuk konvergen penuh pada dataset COCO.

Beberapa modifikasi diajukan untuk memitigasi masalah ini. Misalnya, Deformable DETR ([bab 023](./023%20-%202021%20-%20Deformable%20DETR%20-%20Fondasi%20RGB.md)) menggantikan mekanisme perhatian penuh dengan perhatian terdeformasi (*deformable attention*) untuk menghemat biaya komputasi dan mempercepat konvergensi. Conditional DETR ([bab 160](./160%20-%202021%20-%20Conditional%20DETR%20-%20Fondasi%20RGB.md)) mempermudah pembelajaran pencocokan kueri spasial. Selanjutnya, DAB-DETR (bab terkait) memformulasikan kueri sebagai kotak jangkar (*anchor boxes*) 4D berupa $(x, y, w, h)$ untuk memfasilitasi pembaruan koordinat lapis demi lapis di dalam *decoder*. Meskipun metode-metode ini mempercepat konvergensi, penyebab mendasar dari lambatnya konvergensi DETR belum sepenuhnya terpecahkan secara teoretis.

DN-DETR mengisi celah pemahaman tersebut dengan menganalisis ketidakstabilan pencocokan bipartit. Dalam DETR, pencocokan Hungarian bersifat diskret dan bergantung pada nilai prediksi yang dihasilkan oleh *decoder*. Selama fase awal pelatihan, bobot model belum stabil sehingga prediksi kueri berubah secara drastis untuk citra yang sama pada *epoch* yang berdekatan. Akibatnya, satu objek kebenaran acuan dapat dicocokkan dengan kueri $q_a$ pada *epoch* $t$, kemudian dialokasikan ke kueri $q_b$ pada *epoch* $t+1$. Ketidakkonsistenan target optimasi ini memaksa parameter jaringan melakukan penyesuaian yang saling bertolak belakang, sehingga memperlambat konvergensi model secara keseluruhan.

## Ide Utama

Gagasan utama DN-DETR adalah menghadirkan tugas pembantu (*auxiliary task*) berupa pemulihan derau (*denoising*) kueri yang memintas proses pencocokan Hungarian. Pendekatan ini terinspirasi dari prinsip kerja *denoising autoencoder* yang dilatih untuk merekonstruksi data asli dari versi berderau.

Dalam DN-DETR, input kueri yang dikirimkan ke Transformer *decoder* dibagi menjadi dua kelompok terpisah:
1. Jalur Pencocokan (*Matching Part*): Bagian ini memproses kueri deteksi standar yang bersifat dinamis dan dapat dipelajari. Kueri-kueri ini dicocokkan dengan objek kebenaran acuan menggunakan pencocokan Hungarian.
2. Jalur Denoising (*Denoising Part*): Bagian ini memproses kueri pembantu yang dibuat dengan menambahkan derau acak secara langsung pada koordinat kotak pembatas dan label kelas dari objek kebenaran acuan.

Karena jalur *denoising* menggunakan data yang diturunkan langsung dari kebenaran acuan, pencocokan Hungarian tidak diperlukan. Kueri *denoising* ke-$i$ secara otomatis dipasangkan dengan objek kebenaran acuan ke-$i$. Melalui pemetaan deterministik ini, *decoder* dapat mempelajari regresi kotak pembatas dan klasifikasi kelas secara langsung sejak awal pelatihan. Tugas rekonstruksi ini menstabilkan gradien dan memberikan arah optimasi yang konsisten bagi seluruh lapisan *decoder*. Ketika model digunakan untuk inferensi, seluruh kueri dan komputasi di jalur *denoising* dihilangkan. Dengan demikian, model tetap memiliki parameter dan latensi komputasi yang identik dengan model dasar saat dioperasikan di lingkungan produksi.

## Cara Kerja Langkah demi Langkah

### Alur Kerja Pelatihan dan Inferensi
Dalam fase pelatihan, jaringan mengekstrak fitur memori dari citra masukan menggunakan *backbone* dan Transformer *encoder*. Fitur memori ini dihubungkan dengan kueri *decoder* melalui lapisan perhatian silang (*cross-attention*). Kueri *decoder* dibentuk oleh penggabungan kueri pencocokan standar dan kueri *denoising*. Diagram di bawah mengilustrasikan alur data di dalam sistem DN-DETR:

```
Citra Masukan ──> Backbone ──> Encoder ──> Fitur Memori ────┐
                                                            │ (Cross-Attention)
                                                            ▼
GT Bboxes  ──> Tambah Derau ──> Kueri Denoising ───┐     ┌──────┐
                                                   ├────>│      │ ──> Loss Denoising
GT Labels  ──> Tambah Derau ──> Kueri Konten    ───┘     │      │
                                                         │Decdr.│
Jangkar Baru ─────────────────> Kueri Pencocokan ────────>│      │ ──> Loss Matching
(Learnable Anchors)                                      └──────┘
```

### Pembuatan Kueri Denoising Kotak Pembatas
Untuk setiap objek kebenaran acuan yang direpresentasikan oleh koordinat kotak pembatas $(x, y, w, h)$ di mana $(x, y)$ adalah titik pusat dan $(w, h)$ adalah lebar serta tinggi kotak, sistem menambahkan derau acak untuk menghasilkan kotak berderau $(x', y', w', h')$.

1. Pergeseran Pusat (*Center Shifting*): Koordinat pusat digeser dengan menambahkan nilai $(\Delta x, \Delta y)$ yang diatur agar titik pusat baru tetap berada di dalam kotak asli. Batasan pergeseran ini diformulasikan sebagai:
   $$| \Delta x | < \lambda_1 \frac{w}{2}$$
   $$| \Delta y | < \lambda_1 \frac{h}{2}$$
   Di sini, $\lambda_1$ adalah parameter skala derau pusat yang bernilai antara $0$ dan $1$.
2. Penskalaan Ukuran (*Box Scaling*): Ukuran lebar dan tinggi kotak pembatas dikalikan dengan faktor skala acak berdasarkan parameter $\lambda_2$. Batasannya adalah:
   $$w' \in [(1 - \lambda_2)w, (1 + \lambda_2)w]$$
   $$h' \in [(1 - \lambda_2)h, (1 + \lambda_2)h]$$
Dalam implementasi praktisnya, parameter $\lambda_1$ dan $\lambda_2$ disamakan menjadi $\lambda = 0,4$.

### Pembuatan Kueri Denoising Label Kelas
Label kelas dari objek kebenaran acuan $c$ juga diberikan derau dengan metode pembalikan label (*label flipping*). 
1. Sebuah probabilitas pembalikan kelas $\gamma$ ditentukan (secara default bernilai $0,2$).
2. Dengan probabilitas $1 - \gamma$, label masukan tetap berupa kelas asli $c$.
3. Dengan probabilitas $\gamma$, label masukan digantikan oleh label kelas lain yang disampel secara acak dari daftar kelas dataset.
Label berderau ini kemudian dipetakan ke dalam bentuk representasi vektor (*embedding*) sebelum dimasukkan ke dalam *decoder* sebagai kueri konten.

### Pengelompokan Kueri Denoising
Untuk menghindari bias dari satu variasi derau tunggal, DN-DETR menerapkan beberapa kelompok *denoising* secara paralel. Jika sebuah citra memiliki $N$ objek kebenaran acuan dan sistem dikonfigurasi dengan $M$ kelompok *denoising*, maka total kueri *denoising* yang dibuat adalah $M \times N$. Setiap kelompok dibuat secara independen dengan nilai derau acak yang berbeda.

### Penerapan Masker Perhatian (Attention Mask)
Ketika kueri pencocokan standar ($N_q$) dan kueri *denoising* ($M \times N$) diumpankan secara bersamaan ke dalam Transformer *decoder*, interaksi perhatian-mandiri (*self-attention*) berpotensi menyebabkan kebocoran informasi. Kueri pencocokan standar tidak boleh melihat koordinat kebenaran acuan yang terkandung di dalam kueri *denoising*. 

Untuk mencegah hal tersebut, sebuah masker perhatian diterapkan dengan aturan:
- Kueri pencocokan standar ($Q_{match}$) hanya diizinkan berinteraksi dengan $Q_{match}$ lainnya.
- Kueri *denoising* dalam kelompok $g$ ($Q_{dn}^{(g)}$) diizinkan berinteraksi dengan $Q_{match}$ dan sesama kueri $Q_{dn}^{(g)}$ di dalam kelompok $g$ tersebut.
- Kueri *denoising* dari kelompok yang berbeda tidak diperbolehkan berinteraksi satu sama lain ($Q_{dn}^{(g)}$ diblokir dari $Q_{dn}^{(g')}$ jika $g \neq g'$).

Struktur blok masker perhatian ini digambarkan secara visual pada matriks di bawah ini:

```
              Q_match      Q_dn(1)      Q_dn(2)    ...    Q_dn(M)
            ┌───────────┬────────────┬────────────┬───┬────────────┐
    Q_match │    IZIN   │    BLOK    │    BLOK    │...│    BLOK    │
            ├───────────┼────────────┼────────────┼───┼────────────┤
    Q_dn(1) │    IZIN   │    IZIN    │    BLOK    │...│    BLOK    │
            ├───────────┼────────────┼────────────┼───┼────────────┤
    Q_dn(2) │    IZIN   │    BLOK    │    IZIN    │...│    BLOK    │
            ├───────────┼────────────┼────────────┼───┼────────────┤
      ...   │    ...    │    ...     │    ...     │...│    ...     │
            ├───────────┼────────────┼────────────┼───┼────────────┤
    Q_dn(M) │    IZIN   │    BLOK    │    BLOK    │...│    IZIN    │
            └───────────┴────────────┴────────────┴───┴────────────┘
```

Nilai "IZIN" merepresentasikan nilai nol (perhatian diperbolehkan), sedangkan "BLOK" merepresentasikan nilai $-\infty$ yang meniadakan bobot perhatian setelah fungsi eksponensial *softmax*.

### Perhitungan Fungsi Kerugian
Pelatihan DN-DETR mengoptimalkan fungsi kerugian gabungan. Untuk jalur pencocokan, fungsi kerugian $\mathcal{L}_{match}$ dihitung setelah melakukan pencocokan Hungarian. Untuk jalur *denoising*, fungsi kerugian $\mathcal{L}_{dn}$ dihitung langsung antara hasil rekonstruksi kueri *denoising* kelompok $g$ dan objek kebenaran acuan yang menjadi sumber deraunya.
$$\mathcal{L}_{total} = \mathcal{L}_{match} + \mathcal{L}_{dn}$$
Kerugian $\mathcal{L}_{dn}$ terdiri dari kerugian klasifikasi entropi silang, kerugian koordinat L1, dan kerugian GIoU, yang dibobot dengan faktor pengali yang sama dengan jalur pencocokan standar.

Setelah pelatihan selesai, modul pembuat derau dan seluruh kueri *denoising* dinonaktifkan. Decoder hanya menerima kueri pencocokan standar $N_q$ (biasanya berjumlah 100 atau 300 kueri). Akibatnya, grafik komputasi model pada saat penerapan praktis (*deployment*) bersih dari komputasi tambahan jalur *denoising*.

## Eksperimen dan Hasil

Evaluasi metode DN-DETR dilakukan pada dataset Microsoft COCO 2017 val dengan model dasar DAB-DETR.

Berikut adalah ringkasan hasil performa deteksi pada COCO 2017:
- DN-DETR dengan *backbone* ResNet-50 mencapai akurasi **43,4% AP** setelah dilatih selama 12 *epoch*. Capaian ini menunjukkan efisiensi yang sangat tinggi, melampaui hasil detektor DETR orisinal (R50) yang membutuhkan 500 *epoch* untuk mencapai 42,0% AP.
- Dalam pelatihan standar 50 *epoch*, DN-DETR dengan *backbone* ResNet-50 mencapai **48,6% AP**. Jika dibandingkan dengan baseline DAB-DETR (R50) tanpa metode *denoising* yang mencapai 45,7% AP pada 50 *epoch*, DN-DETR memberikan peningkatan performa sebesar **2,9% AP** pada anggaran pelatihan yang sama.
- Pada model yang menggunakan *backbone* lebih besar seperti ResNet-101, DN-DETR secara konsisten meningkatkan kinerja baseline sebesar lebih dari 2% AP.

Dalam studi ablasi (*ablation study*) yang dilaporkan oleh penulis:
- Efek Derau Kotak vs Label: Menambahkan derau kotak saja pada DAB-DETR R50 meningkatkan AP sebesar 1,5% AP. Menambahkan derau label saja memberikan kontribusi stabilisasi klasifikasi. Kombinasi keduanya menghasilkan peningkatan penuh sebesar 2,9% AP.
- Jumlah Kelompok Denoising ($M$): Eksperimen menunjukkan bahwa meningkatkan jumlah kelompok dari $1$ ke $5$ memberikan peningkatan performa dari 47,8% AP menjadi 48,6% AP. Namun, penambahan kelompok di atas 5 (misalnya hingga 10 kelompok) hanya memberikan peningkatan minor di bawah 0,2% AP sementara membebani memori VRAM GPU selama proses pelatihan secara linier. Oleh karena itu, $M = 5$ dipilih sebagai nilai default yang optimal.

## Kelebihan dan Keterbatasan

Kelebihan:
1. **Peningkatan Efisiensi Pelatihan**: DN-DETR memangkas kebutuhan waktu komputasi hingga 50% untuk mencapai tingkat performa yang setara dengan model detektor berbasis *transformer* lainnya.
2. **Ketiadaan Beban Komputasi Inferensi**: Karena jalur *denoising* dibuang setelah pelatihan selesai, model tidak mengalami penambahan latensi deteksi, ukuran penyimpanan parameter, atau kompleksitas saat dijalankan pada perangkat keras target.
3. **Fleksibilitas Integrasi**: Metode *query denoising* dapat diaplikasikan ke hampir semua model detektor dalam keluarga DETR dengan modifikasi kode minimal.
4. **Stabilitas Konvergensi**: Menyediakan sinyal gradien yang lebih konsisten pada lapisan-lapisan *decoder* sejak awal pelatihan, mengurangi osilasi parameter akibat fluktuasi pencocokan Hungarian.

Keterbatasan:
1. **Sensitivitas Terhadap Hyperparameter Derau**: Penentuan nilai skala derau spasial ($\lambda_1, \lambda_2$) dan tingkat pembalikan kelas ($\gamma$) membutuhkan penalaan yang cermat. Dari sisi rekayasa, jika derau terlalu rendah, efek stabilisasi tidak tercapai; jika derau terlalu tinggi, tugas rekonstruksi menjadi terlalu sulit dan dapat merusak representasi fitur yang dipelajari model.
2. **Peningkatan Konsumsi Memori Pelatihan**: Meskipun tidak ada *overhead* saat inferensi, penggunaan kelompok *denoising* multipel ($M \times N$) secara langsung meningkatkan jumlah token kueri yang diproses oleh *decoder* selama pelatihan. Hal ini menyebabkan lonjakan konsumsi memori GPU pada fase pelatihan.
3. **Penyusutan Efektivitas pada Model Skala Besar**: Secara konseptual, keuntungan efisiensi yang ditawarkan oleh metode ini cenderung berkurang pada skenario pelatihan model skala sangat besar dengan volume data yang masif. Pada kondisi tersebut, ketidakstabilan *Hungarian matching* dapat teratasi secara alami seiring dengan berjalannya proses pelatihan yang sangat panjang.

## Kaitan dengan Bab Lain

DN-DETR berada di posisi transisi yang krusial dalam peta perkembangan detektor objek berbasis *transformer*. Konsep kueri jangkar dinamis yang digunakannya diadopsi langsung dari DAB-DETR (bab terkait), yang merupakan pengembangan dari DETR orisinal ([bab 022](./022%20-%202020%20-%20DETR%20-%20Fondasi%20RGB.md)) yang memiliki masalah konvergensi lambat.

Metode *query denoising* yang diletakkan dalam bab ini terbukti sangat berpengaruh dan diwarisi oleh generasi detektor *SOTA* (*State-Of-The-Art*) setelahnya. Secara khusus, DINO detector ([bab 158](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md)) menyempurnakan formulasi DN-DETR dengan memperkenalkan *contrastive denoising* menggunakan contoh negatif untuk melatih kemampuan diskriminasi model. Di sisi lain, RT-DETR ([bab 155](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md)), yang merupakan detektor *transformer* real-time pertama yang kompetitif dengan keluarga YOLO, mengadopsi skema latihan berbasis *query denoising* ini untuk mempercepat pelatihannya pada arsitektur hibrida CNN-Transformer. Selain itu, DN-DETR juga menginspirasi skema pelatihan multi-skala dan multi-tugas yang dijumpai pada detektor komposit seperti Co-DETR ([bab 165](./165%20-%202023%20-%20Co-DETR%20-%20Fondasi%20RGB.md)).

Kaitan dengan bab-bab lain juga mencakup perbandingan dengan upaya optimasi kueri seperti Deformable DETR ([bab 023](./023%20-%202021%20-%20Deformable%20DETR%20-%20Fondasi%20RGB.md)) dan Conditional DETR ([bab 160](./160%20-%202021%20-%20Conditional%20DETR%20-%20Fondasi%20RGB.md)). Dari segi ekstraksi fitur, model ini dapat dikombinasikan dengan tulang punggung Transformer modern seperti Vision Transformer ([bab 024](./024%20-%202021%20-%20Vision%20Transformer%20%28ViT%29%20-%20Fondasi%20RGB.md)), Swin Transformer ([bab 025](./025%20-%202021%20-%20Swin%20Transformer%20-%20Fondasi%20RGB.md)), Swin Transformer V2 ([bab 163](./163%20-%202022%20-%20Swin%20Transformer%20V2%20-%20Fondasi%20RGB.md)), ConvNeXt ([bab 162](./162%20-%202022%20-%20ConvNeXt%20-%20Fondasi%20RGB.md)), dan Pyramid Vision Transformer ([bab 164](./164%20-%202021%20-%20Pyramid%20Vision%20Transformer%20-%20Fondasi%20RGB.md)).

## Poin untuk Sitasi

Kutip dengan kunci `li2022dndetr`. Ringkasan yang aman dikutip dalam tinjauan pustaka:
"DN-DETR mempercepat konvergensi pelatihan detektor berbasis *transformer* dengan memperkenalkan tugas pembantu berupa rekonstruksi kueri berderau (*query denoising*). Metode ini menstabilkan proses pembelajaran dengan memintas ketidakstabilan algoritme pencocokan Hungarian selama fase awal pelatihan, sehingga meningkatkan akurasi deteksi secara signifikan hingga mencapai 48,6% AP pada dataset COCO 2017 val menggunakan *backbone* ResNet-50 tanpa penambahan biaya komputasi saat inferensi."
Catatan verifikasi: Hasil eksperimen spesifik (43,4% AP pada 12 *epoch* dan 48,6% AP pada 50 *epoch*) diperoleh dari pengujian pada dataset COCO 2017 val. Verifikasi manual disarankan untuk memastikan parameter derau $\lambda$ dan $\gamma$ yang digunakan saat mereproduksi metode ini pada arsitektur non-DAB-DETR.
