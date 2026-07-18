# 171 - SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xie2021segformer` |
| Judul asli | SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers |
| Penulis | Enze Xie, Wenhai Wang, Zhiding Yu, Anima Anandkumar, Jose M. Alvarez, Ping Luo |
| Tahun | 2021 |
| Venue | Advances in Neural Information Processing Systems (NeurIPS 2021) |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2105.15203
- **Google Scholar:** https://scholar.google.com/scholar?q=SegFormer%3A%20Simple%20and%20Efficient%20Design%20for%20Semantic%20Segmentation%20with%20Transformers
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=SegFormer%3A%20Simple%20and%20Efficient%20Design%20for%20Semantic%20Segmentation%20with%20Transformers&sort=relevance

## Gambaran Umum

SegFormer adalah kerangka kerja segmentasi semantik (pelabelan kelas untuk setiap piksel citra) berbasis Transformer yang menggabungkan *encoder* hierarkis tanpa *positional encoding* (kode posisi) dengan *decoder* berupa lapisan MLP (*multilayer perceptron*, jaringan saraf lapis-penuh sederhana) tanpa konvolusi. Makalah ini menjawab dua masalah pada segmentasi berbasis Transformer generasi awal: ketergantungan pada kode posisi yang rapuh terhadap perubahan resolusi uji, dan *decoder* yang berat secara komputasi. Dengan *encoder* bernama MiT (*Mix Transformer*) berskala enam varian (B0 hingga B5) dan *decoder* MLP yang hanya mengagregasi fitur multiskala, SegFormer mencapai 51,0% mIoU (*mean Intersection-over-Union*, rata-rata rasio irisan-gabungan antara wilayah prediksi dan wilayah kebenaran, metrik utama segmentasi semantik) pada ADE20K dan 84,0% mIoU pada Cityscapes menggunakan varian terbesarnya, sekaligus menunjukkan ketahanan tinggi terhadap citra terkorupsi. Model ini menjadi salah satu tulang punggung (*backbone*) yang sering diadaptasi pada cabang RGB dari sistem segmentasi RGB-D.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum SegFormer, segmentasi semantik didominasi jaringan konvolusi (*Convolutional Neural Network*, CNN) dengan struktur *encoder-decoder* (arsitektur yang mengecilkan resolusi citra secara bertahap lalu memulihkannya kembali), seperti DeepLabv3+ yang memakai konvolusi berdilasi untuk memperbesar bidang pandang tanpa menambah parameter berlebihan. Pendekatan CNN memiliki bidang pandang efektif (*effective receptive field*, wilayah citra masukan yang benar-benar memengaruhi satu keluaran fitur) yang terbatas secara struktural sehingga sulit menangkap konteks global tanpa tumpukan lapisan yang sangat dalam.

Upaya pertama menerapkan Transformer murni pada segmentasi, yaitu SETR, menggunakan *encoder* Vision Transformer (ViT, dibahas pada bab 024) yang menghasilkan fitur beresolusi tunggal dan kasar, lalu menambahkan *decoder* CNN yang berat untuk memulihkan resolusi. ViT juga bergantung pada *positional encoding* tetap yang ditambahkan ke setiap *patch* (potongan citra) di awal jaringan agar model mengetahui posisi spasialnya. Kode posisi semacam ini dilatih pada resolusi tertentu, sehingga saat citra uji berukuran berbeda dari citra latih, kode posisi harus diinterpolasi ulang secara manual dan hal ini menurunkan akurasi. Pyramid Vision Transformer (PVT, bab 164) dan Swin Transformer (bab 025) memperbaiki sisi efisiensi dengan struktur piramida multiskala dan atensi berjendela, tetapi keduanya masih mewarisi kode posisi dan umumnya dipasangkan dengan *decoder* segmentasi yang kompleks seperti *Feature Pyramid Network*. Masalah yang belum terpecahkan pada saat SegFormer diajukan adalah bagaimana merancang segmentasi berbasis Transformer yang efisien secara komputasi, tidak rapuh terhadap perubahan resolusi, dan tidak memerlukan *decoder* rumit.

## Ide Utama

Gagasan inti SegFormer adalah memisahkan tugas ekstraksi fitur multiskala dan agregasi fitur menjadi dua komponen yang masing-masing dibuat sesederhana mungkin. *Encoder* MiT menghasilkan fitur pada empat resolusi berbeda tanpa kode posisi eksplisit; informasi posisi disisipkan secara implisit melalui konvolusi 3×3 yang ditanam di dalam blok umpan-maju (*feed-forward*) Transformer, disebut Mix-FFN. Karena konvolusi bersifat lokal dan bergantung pada susunan piksel yang berdekatan, ia secara alami membawa informasi posisi tanpa perlu parameter kode posisi yang terikat pada resolusi tertentu. *Decoder*-nya berupa MLP ringan yang hanya melakukan proyeksi linear, penyamaan resolusi, dan penggabungan fitur dari keempat tahap *encoder* — tanpa konvolusi atau modul kompleks lain. Fitur dari tahap dangkal (resolusi tinggi) membawa detail lokal, sedangkan fitur dari tahap dalam (resolusi rendah) membawa konteks global; MLP sederhana cukup untuk menggabungkan keduanya karena Transformer, tidak seperti CNN, mampu menghasilkan atensi non-lokal bahkan pada tahap awal jaringan.

## Cara Kerja Langkah demi Langkah

### Encoder Hierarkis MiT

MiT terdiri atas empat tahap yang masing-masing menghasilkan peta fitur pada resolusi 1/4, 1/8, 1/16, dan 1/32 dari citra masukan, menyerupai struktur piramida pada CNN seperti ResNet. Pada citra masukan 512×512 piksel misalnya, keempat tahap menghasilkan peta fitur berukuran 128×128, 64×64, 32×32, dan 16×16. Peralihan antar-tahap dilakukan dengan *overlapped patch merging*: alih-alih memotong citra menjadi *patch* yang saling terpisah seperti pada ViT, MiT menggunakan konvolusi dengan ukuran kernel K, langkah geser (*stride*) S, dan *padding* P — tahap pertama memakai K=7, S=4, P=3, sedangkan tahap selanjutnya memakai K=3, S=2, P=1. Karena jendela konvolusi ini saling tumpang tindih, kontinuitas informasi di sekitar batas antar-*patch* tetap terjaga, berbeda dari pemotongan *patch* tanpa tumpang tindih yang memutus konteks lokal.

### Efficient Self-Attention

Mekanisme atensi mandiri (*self-attention*) standar pada Transformer memiliki kompleksitas komputasi O(N²) terhadap panjang urutan N (jumlah *patch*), karena setiap elemen dibandingkan dengan seluruh elemen lain. Pada tahap dangkal MiT, N sangat besar sebab resolusi fitur masih tinggi, sehingga komputasi ini menjadi mahal. SegFormer mereduksi urutan kunci (*key*) dan nilai (*value*) dengan rasio reduksi R sebelum dihitung skor atensinya, menurunkan kompleksitas menjadi O(N²/R). Rasio reduksi yang dipakai pada empat tahap berturut-turut adalah [64, 16, 4, 1] — tahap dangkal dengan N besar direduksi paling agresif, sedangkan tahap terdalam dengan N sudah kecil tidak direduksi sama sekali.

### Mix-FFN sebagai Pengganti Kode Posisi

Blok umpan-maju standar pada Transformer hanya terdiri atas dua lapisan linear dengan fungsi aktivasi di antaranya. Mix-FFN menyisipkan satu konvolusi 3×3 di antara dua lapisan tersebut:

```
Mix-FFN(x) = MLP( GELU( Conv3x3( MLP(x) ) ) ) + x
```

Konvolusi 3×3 ini menyebabkan kebocoran informasi posisi (*leaked location information*) karena keluaran setiap posisi kini bergantung pada susunan piksel tetangganya, bukan hanya nilai piksel itu sendiri. Dengan demikian, model tidak memerlukan parameter kode posisi terpisah yang ukurannya terikat pada resolusi citra latih.

### Decoder All-MLP

*Decoder* menerima empat peta fitur dari MiT dan memprosesnya dalam empat langkah: (1) proyeksi linear menyamakan jumlah kanal setiap peta fitur menjadi dimensi C yang seragam; (2) seluruh peta fitur diperbesar (*upsampling*) ke resolusi 1/4 citra masukan lalu digabung (*concatenate*) sepanjang dimensi kanal; (3) satu lapisan MLP menggabungkan (*fuse*) fitur gabungan tersebut; (4) satu lapisan MLP terakhir memetakan fitur ke peta segmentasi berukuran H/4 × W/4 × N_kelas, dengan N_kelas jumlah kategori target. Peta segmentasi ini kemudian diperbesar ke resolusi penuh untuk menghasilkan label per piksel.

Diagram berikut merangkum aliran data dari citra masukan hingga peta segmentasi:

```
citra HxWx3
   │
   ▼ Tahap 1 (K7,S4)      fitur H/4 x W/4     ──┐
   ▼ Tahap 2 (K3,S2)      fitur H/8 x W/8     ──┤ proyeksi linear
   ▼ Tahap 3 (K3,S2)      fitur H/16 x W/16   ──┤ + upsampling ke H/4
   ▼ Tahap 4 (K3,S2)      fitur H/32 x W/32   ──┘ + concat kanal
        (MiT: attention + Mix-FFN tiap tahap)      │
                                                     ▼
                                          MLP fusi -> MLP prediksi
                                                     │
                                                     ▼
                                      peta segmentasi H/4 x W/4 x N_kelas
```

### Varian Model B0–B5

SegFormer disediakan dalam enam ukuran, dari B0 (3,7 juta parameter, ditujukan untuk aplikasi ringan) hingga B5 (82,0 juta parameter, ditujukan untuk akurasi maksimal). Perbedaan antar-varian terutama terletak pada jumlah lapisan Transformer di tiap tahap dan lebar (dimensi tersembunyi) setiap tahap; struktur empat tahap dan mekanisme Mix-FFN tetap sama di seluruh varian, sehingga pengguna dapat memilih titik seimbang akurasi-efisiensi tanpa mengubah desain dasar.

## Eksperimen dan Hasil

SegFormer diuji pada tiga tolok ukur segmentasi semantik: ADE20K (data dalam ruangan dan luar ruangan dengan 150 kelas), Cityscapes (data jalan raya perkotaan dengan 19 kelas), dan COCO-Stuff (data 164 ribu citra dengan kelas benda dan latar). Pada ADE20K, SegFormer-B0 mencapai 37,4% mIoU dengan 8,4 GFLOPs (miliar operasi titik-mengambang), sedangkan SegFormer-B5 mencapai 51,0% mIoU dengan 183,3 GFLOPs — menunjukkan bahwa menambah kapasitas model menaikkan akurasi sekitar 13,6 poin dengan biaya komputasi naik lebih dari dua puluh kali lipat. Pada Cityscapes, SegFormer-B0 mencapai 76,2% mIoU pada kecepatan sekitar 48 *frame per second* (FPS) menggunakan citra beresolusi rendah, cocok untuk aplikasi waktu nyata, sedangkan SegFormer-B5 mencapai 84,0% mIoU pada kecepatan yang jauh lebih rendah karena resolusi uji dan kapasitas model lebih besar. Dibandingkan SETR (pendahulu berbasis Transformer), SegFormer mencapai akurasi lebih tinggi dengan model yang jauh lebih kecil dan lebih cepat — makalah melaporkan SegFormer-B5 unggul di atas SETR pada Cityscapes sambil beberapa kali lebih ringan dan lebih cepat pada tahap inferensi.

Pengujian ketahanan (*robustness*) dilakukan pada Cityscapes-C, versi Cityscapes yang dicemari beragam jenis korupsi citra (derau, cuaca, gangguan optik) pada berbagai tingkat keparahan, tanpa pelatihan ulang model (*zero-shot*). SegFormer-B5 mempertahankan akurasi jauh lebih tinggi daripada DeepLabv3+ di hampir seluruh jenis korupsi; makalah melaporkan keunggulan besar pada kondisi seperti derau Gaussian dan salju, menunjukkan bahwa *encoder* Transformer tanpa kode posisi tetap lebih tahan terhadap gangguan yang mengubah statistik citra dibandingkan CNN dengan *decoder* konvensional.

Studi ablasi pada makalah membandingkan Mix-FFN dengan kode posisi tetap saat resolusi uji diubah dari resolusi latih: model dengan Mix-FFN kehilangan akurasi jauh lebih sedikit dibandingkan model dengan kode posisi tetap, mengonfirmasi bahwa Mix-FFN adalah pengganti yang lebih tahan-resolusi. Ablasi lain mengganti *encoder* MiT dengan ResNet-101 pada *decoder* MLP yang sama; hasilnya jauh lebih rendah daripada memakai MiT berukuran sebanding, menunjukkan bahwa keunggulan *decoder* MLP bergantung pada bidang pandang non-lokal yang hanya dihasilkan Transformer, bukan berlaku umum untuk sembarang *encoder*.

## Kelebihan dan Keterbatasan

SegFormer menghilangkan dua sumber kerapuhan sekaligus: kode posisi yang terikat resolusi dan *decoder* segmentasi yang berat, sambil mempertahankan akurasi kompetitif melalui bidang pandang non-lokal bawaan Transformer. Skalabilitas enam varian memudahkan penerapan pada rentang kebutuhan komputasi yang luas, dari perangkat tepi (B0) hingga server dengan akurasi maksimal (B5). Ketahanan terhadap korupsi citra menjadikannya pilihan yang relevan untuk aplikasi luar ruangan dengan kondisi pencahayaan atau cuaca yang bervariasi.

Dari sisi rekayasa, varian besar seperti B4 dan B5 tetap menuntut memori dan komputasi yang signifikan, sehingga penerapan waktu nyata pada resolusi tinggi hanya realistis untuk varian kecil. Secara konseptual, meskipun reduksi rasio R menurunkan kompleksitas atensi, biaya komputasi pada tahap dangkal dengan resolusi tinggi tetap menjadi penyumbang FLOPs terbesar dibandingkan CNN pada tahap setara. SegFormer juga dirancang murni untuk masukan RGB; makalah tidak membahas penggabungan modalitas kedalaman (*depth*), sehingga adaptasi ke segmentasi RGB-D memerlukan modifikasi tambahan berupa cabang atau modul fusi terpisah di luar cakupan makalah aslinya.

## Kaitan dengan Bab Lain

SegFormer mewarisi konsep *encoder* hierarkis multiskala yang diperkenalkan Pyramid Vision Transformer ([bab 164](./164%20-%202021%20-%20Pyramid%20Vision%20Transformer%20-%20Fondasi%20RGB.md)) dan menjawab kerapuhan kode posisi yang melekat pada Vision Transformer ([bab 024](./024%20-%202021%20-%20Vision%20Transformer%20%28ViT%29%20-%20Fondasi%20RGB.md)); desain atensi berjendela pada Swin Transformer ([bab 025](./025%20-%202021%20-%20Swin%20Transformer%20-%20Fondasi%20RGB.md)) merupakan pendekatan sezaman yang menyasar masalah efisiensi serupa dengan mekanisme berbeda. Sebagai *encoder* RGB yang ringan dan bebas kode posisi, SegFormer menjadi rujukan desain bagi metode segmentasi RGB-D berikutnya dalam klaster ini: EMSANet ([bab 172](./172%20-%202022%20-%20EMSANet%20-%20Segmentasi%20RGB-D.md)) dan GeminiFusion ([bab 173](./173%20-%202024%20-%20GeminiFusion%20-%20Segmentasi%20RGB-D.md)) memakai strategi fusi multimodal yang dapat dipasangkan dengan *encoder* bergaya MiT, sedangkan Omnivore ([bab 174](./174%20-%202022%20-%20Omnivore%20-%20Segmentasi%20RGB-D.md)) mengeksplorasi *backbone* Transformer tunggal untuk berbagai modalitas visual sekaligus, arah yang sejalan dengan prinsip kesederhanaan arsitektur yang diusung SegFormer.

## Poin untuk Sitasi

Kutip dengan kunci `xie2021segformer`. Ringkasan yang aman dikutip: SegFormer menggabungkan *encoder* Transformer hierarkis MiT tanpa *positional encoding* (memakai Mix-FFN sebagai gantinya) dengan *decoder* MLP ringan, mencapai efisiensi dan ketahanan terhadap korupsi citra yang lebih baik daripada metode CNN dan Transformer segmentasi sebelumnya pada ADE20K dan Cityscapes. Angka yang perlu diverifikasi ulang ke naskah asli sebelum sitasi formal: mIoU SegFormer-B5 pada ADE20K (sumber berbeda melaporkan kisaran 51,0%–51,8% tergantung versi/protokol pengujian skala tunggal-vs-multiskala), jumlah parameter B4 (kisaran 62–64 juta pada sumber berbeda), FPS persis untuk setiap varian pada Cityscapes, angka mIoU per jenis korupsi pada Cityscapes-C, serta hasil lengkap pada COCO-Stuff.
