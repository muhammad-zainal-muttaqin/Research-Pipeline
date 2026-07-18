# 197 - DiffPixelFormer: Differential Pixel-Aware Transformer for RGB-D Indoor Scene Segmentation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gong2025diffpixelformer` |
| Judul asli | DiffPixelFormer: Differential Pixel-Aware Transformer for RGB-D Indoor Scene Segmentation |
| Penulis | Yan Gong, Jianli Lu, Yongsheng Gao, Jie Zhao, Xiaojuan Zhang, Susanto Rahardja |
| Tahun | 2025 |
| Venue | arXiv preprint (arXiv:2511.13047) |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2511.13047
- **Google Scholar:** https://scholar.google.com/scholar?q=DiffPixelFormer%3A%20Differential%20Pixel-Aware%20Transformer%20for%20RGB-D%20Indoor%20Scene%20Segmentation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=DiffPixelFormer%3A%20Differential%20Pixel-Aware%20Transformer%20for%20RGB-D%20Indoor%20Scene%20Segmentation&sort=relevance

## Gambaran Umum

DiffPixelFormer mengusulkan arsitektur transformer untuk segmentasi semantik scene (adegan) indoor berbasis RGB-D (citra warna RGB dipasangkan dengan peta kedalaman/*depth*). Gagasan intinya adalah memisahkan secara eksplisit dua jenis informasi saat menggabungkan modalitas RGB dan *depth*: isyarat yang khas milik satu modalitas (disebut komponen diferensial) dan isyarat yang sama-sama dimiliki kedua modalitas (disebut komponen bersama). Pemisahan ini dilakukan pada level piksel melalui modul bernama *Differential–Shared Inter-Modal* (DSIM), yang ditempatkan di dalam blok interaksi bernama *Intra-Inter Modal Interaction Block* (IIMIB).

Pada benchmark NYUDv2, varian terbesar model ini (DiffPixelFormer-L) mencapai 59,95% *mean Intersection-over-Union* (mIoU) — metrik standar segmentasi semantik yang mengukur rerata rasio irisan terhadap gabungan antara wilayah prediksi dan wilayah kebenaran di seluruh kelas. Pada SUN RGB-D, model yang sama mencapai 54,28% mIoU. Kedua angka ini melampaui DFormer-L, salah satu metode fusi RGB-D transformer terkini, berturut-turut sebesar 1,78 dan 2,75 poin persentase. Makalah ini adalah preprint arXiv yang diunggah November 2025, sehingga belum melalui proses tinjauan sejawat pada saat entri ini ditulis.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Segmentasi semantik indoor bertugas memberi label kelas pada setiap piksel citra ruangan (misalnya dinding, lantai, meja, kursi). Penambahan modalitas *depth* di samping RGB membantu tugas ini karena kedua objek yang tampak mirip pada citra warna — misalnya dua permukaan bertekstur serupa — sering kali dapat dibedakan lewat jarak dan bentuk permukaannya. Bab 171 (SegFormer) memperkenalkan arsitektur transformer efisien untuk segmentasi semantik pada RGB murni, sedangkan bab 172 (EMSANet), bab 173 (GeminiFusion), dan bab 174 (Omnivore) sama-sama menambahkan mekanisme untuk menggabungkan cabang RGB dan *depth* pada tugas pemahaman scene indoor.

Menurut makalah ini, pendekatan fusi RGB-D sebelumnya, khususnya yang memakai *cross-attention* (mekanisme atensi yang membiarkan setiap posisi pada satu modalitas menimbang seluruh posisi pada modalitas lain) secara global antar seluruh piksel, menanggung kompleksitas komputasi yang tumbuh secara kuadratik terhadap jumlah piksel — dituliskan penulis sebagai O(N²d), dengan N jumlah posisi piksel dan d dimensi fitur. Selain mahal secara komputasi, mekanisme tersebut umumnya menggabungkan fitur kedua modalitas tanpa membedakan bagian mana yang benar-benar unik milik satu modalitas dan bagian mana yang tumpang tindih antar keduanya. Menurut penulis, kegagalan mempertimbangkan pemodelan intra-modal (di dalam satu modalitas) dan inter-modal (antar-modalitas) secara bersamaan, ditambah pengabaian pembedaan informasi bersama versus spesifik-modalitas, melemahkan daya pembeda dan kapasitas representasi model fusi.

## Ide Utama

Gagasan inti DiffPixelFormer adalah memisahkan proses penggabungan RGB-*depth* menjadi dua jalur berbeda yang ditangani modul berbeda: satu jalur memperkuat representasi di dalam masing-masing modalitas (intra-modal) melalui *self-attention* (atensi diri, mekanisme yang membiarkan setiap posisi fitur menimbang seluruh posisi lain dalam modalitas yang sama untuk menangkap dependensi jarak jauh), dan satu jalur lain memodelkan interaksi antar-modalitas (inter-modal) melalui modul DSIM yang secara eksplisit memecah fitur menjadi komponen diferensial (perbedaan antar-modal) dan komponen bersama (kemiripan struktural antar-modal).

Dengan pemisahan ini, model tidak lagi menimbang seluruh piksel citra terhadap seluruh piksel peta *depth* secara membabi buta, melainkan membatasi perbandingan pada lokasi spasial yang berkorespondensi (atensi lintas-modal yang sadar-piksel, *pixel-aware cross-attention*). Pada satu lokasi piksel tertentu, model menghitung seberapa besar RGB dan *depth* berbeda di titik itu, dan secara terpisah seberapa besar keduanya membawa isyarat struktural yang sama. Kedua skor ini kemudian digabungkan kembali untuk menghasilkan fitur gabungan pada piksel tersebut, sebelum diteruskan ke tahap dekoder untuk prediksi label kelas.

## Cara Kerja Langkah demi Langkah

### Struktur Umum: IIMIB

IIMIB adalah blok yang menerima fitur dari cabang RGB dan cabang *depth* pada suatu tahap encoder, lalu memprosesnya melalui dua sublangkah berurutan. Sublangkah pertama menerapkan *self-attention* secara terpisah pada fitur RGB dan fitur *depth*, sehingga masing-masing modalitas memperkuat representasi internalnya sendiri sebelum berinteraksi dengan modalitas lain. Sublangkah kedua meneruskan kedua fitur yang telah diperkuat itu ke modul DSIM untuk pemodelan interaksi antar-modalitas. Blok ini ditempatkan berulang pada beberapa tahap resolusi encoder, mengikuti pola umum arsitektur *encoder-decoder* (arsitektur yang mengecilkan resolusi spasial secara bertahap sambil memperkaya fitur semantik pada encoder, lalu memulihkan resolusi pada decoder untuk prediksi per-piksel) yang lazim pada segmentasi semantik.

### Modul DSIM: Discriminator Perbedaan dan Kemiripan

Di dalam DSIM, makalah menyebut dua komponen: *difference discriminator* (penilai perbedaan), yang menghitung skor seberapa besar fitur RGB dan *depth* berbeda pada tiap posisi piksel, dan *similarity discriminator* (penilai kemiripan), yang mengekstrak isyarat struktural yang sama-sama dimiliki kedua modalitas pada posisi tersebut. Pemisahan ini berbeda dari fusi konkatenasi atau penjumlahan biasa yang menggabungkan fitur RGB dan *depth* tanpa membedakan asal informasinya. Dengan discriminator perbedaan, model dapat menonjolkan wilayah tempat *depth* memberi informasi tambahan yang tidak tersedia dari RGB — misalnya batas antara dua permukaan sewarna dengan kedalaman berbeda — sementara discriminator kemiripan menjaga konsistensi struktural saat kedua modalitas sepakat.

Diagram berikut merangkum alur data satu blok IIMIB pada satu tahap encoder:

```
fitur RGB tahap-i        fitur depth tahap-i
      │                         │
      ▼                         ▼
 self-attention            self-attention        <- intra-modal
 (perkuat RGB)             (perkuat depth)
      │                         │
      └───────────┬─────────────┘
                   ▼
              modul DSIM                          <- inter-modal
    ┌──────────────┴──────────────┐
    ▼                              ▼
difference discriminator   similarity discriminator
(isyarat unik per modal)   (isyarat struktural bersama)
    └──────────────┬──────────────┘
                   ▼
        fitur gabungan tahap-i
        (diteruskan ke decoder)
```

Atensi pada tahap penggabungan dibatasi pada lokasi spasial yang berkorespondensi antar kedua modalitas (bukan atensi global ke seluruh piksel citra), sehingga menurut penulis biaya komputasi DSIM jauh lebih rendah dibandingkan *cross-attention* konvensional.

### Efisiensi dan Kecepatan Inferensi

Penulis melaporkan bahwa DSIM mengurangi jumlah parameter sebesar 83,83% dan FLOPs (jumlah operasi hitung titik-mengambang, ukuran umum biaya komputasi) sebesar 72,53% dibandingkan mekanisme *cross-attention* konvensional pada modul setara, dengan kecepatan inferensi 41,66 *frame* per detik (FPS). Angka-angka efisiensi ini berasal dari ekstraksi otomatis atas naskah dan perlu dicocokkan langsung dengan tabel ablasi pada PDF sebelum dikutip formal.

### Backbone dan Varian Model

Makalah melaporkan beberapa varian model dengan *backbone* (jaringan tulang punggung ekstraksi fitur) yang berbeda: varian yang lebih kecil memakai *backbone* keluarga MiT (*Mix Transformer*, backbone yang sama dipakai SegFormer pada bab 171), sedangkan varian terbesar (DiffPixelFormer-L) memakai *backbone* Swin Transformer skala besar. Rincian jumlah parameter persis per varian tidak dapat dipastikan sepenuhnya dari ekstraksi otomatis yang tersedia bagi penulis bab ini, sehingga angka tersebut tidak dicantumkan di sini dan harus diverifikasi dari tabel asli.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada dua benchmark segmentasi semantik indoor RGB-D standar. NYUDv2 berisi 1.449 citra beranotasi padat (pasangan RGB-*depth* dengan label kelas per piksel), diambil dari total 407.024 *frame* video indoor tanpa label penuh. SUN RGB-D berisi 10.335 citra RGB-D, terbagi menjadi 5.285 citra latih dan 5.050 citra uji. Kedua dataset ini juga dipakai pada bab 172 (EMSANet) dan bab 173 (GeminiFusion), sehingga angka mIoU pada bab-bab tersebut dapat dijadikan pembanding kasar.

Hasil utama pada varian terbesar, DiffPixelFormer-L: 59,95% mIoU pada NYUDv2 dan 54,28% mIoU pada SUN RGB-D. Dibandingkan dengan DFormer-L, metode fusi RGB-D transformer yang dipakai penulis sebagai pembanding utama, DiffPixelFormer-L unggul 2,75 poin persentase pada NYUDv2 dan 1,78 poin persentase pada SUN RGB-D. Interpretasinya: peningkatan pada NYUDv2 lebih besar daripada pada SUN RGB-D, kemungkinan karena NYUDv2 memiliki jumlah citra beranotasi jauh lebih sedikit (1.449 berbanding lebih dari 10.000 pada SUN RGB-D), sehingga kemampuan model memanfaatkan komplementaritas RGB-*depth* secara efisien per piksel — yang menjadi klaim inti DSIM — lebih terasa dampaknya ketika data latih terbatas. Makalah juga menyatakan model dievaluasi terhadap SegFormer, CMX, dan GeminiFusion sebagai pembanding tambahan; DiffPixelFormer-L dilaporkan unggul terhadap semuanya, tetapi selisih mIoU persis terhadap masing-masing metode ini tidak berhasil dipastikan dari sumber yang tersedia bagi penulis bab ini dan harus dicek langsung ke tabel makalah.

## Kelebihan dan Keterbatasan

Kelebihan yang dapat diverifikasi dari makalah: pemisahan eksplisit komponen diferensial dan bersama memberi mekanisme yang secara konseptual lebih terarah dibandingkan fusi konkatenasi sederhana, karena model tidak dipaksa mempelajari sendiri mana bagian fitur yang saling melengkapi dan mana yang redundan. Pembatasan atensi pada korespondensi spasial piksel, alih-alih atensi global ke seluruh piksel, secara konseptual mengurangi kompleksitas komputasi dibandingkan *cross-attention* penuh — sejalan dengan klaim efisiensi parameter dan FLOPs pada makalah.

Dari sisi rekayasa, makalah tidak menyertakan pengujian pada skenario modalitas hilang (misalnya ketika sensor *depth* rusak atau tidak tersedia), padahal ini adalah kondisi realistis pada aplikasi robotika lapangan. Penulis makalah sendiri mengakui hal ini secara eksplisit sebagai arah kerja mendatang, menyatakan berniat memperluas mekanisme diferensial ke tugas persepsi multimodal yang lebih luas dan mengeksplorasi generalisasinya pada skenario modalitas hilang. Secara konseptual, karena kedua benchmark yang diuji (NYUDv2 dan SUN RGB-D) sama-sama merupakan scene indoor terstruktur, belum ada bukti langsung dari makalah mengenai seberapa baik DSIM menggeneralisasi ke domain luar ruangan atau ke sensor *depth* dengan derau lebih tinggi daripada yang dipakai kedua dataset tersebut. Varian terbesar model juga memakai *backbone* Swin Transformer skala besar, yang secara umum menuntut sumber daya komputasi lebih besar daripada varian berbasis MiT yang lebih ringan — implikasi biaya ini relevan bagi penerapan waktu-nyata di luar angka FPS tunggal yang dilaporkan.

## Kaitan dengan Bab Lain

DiffPixelFormer melanjutkan garis transformer untuk segmentasi RGB-D indoor yang dibuka bab 171 ([SegFormer](./171%20-%202021%20-%20SegFormer%20-%20Segmentasi%20RGB-D.md)), yang menyediakan *backbone* MiT dan arsitektur *encoder-decoder* ringan yang juga dipakai pada varian kecil DiffPixelFormer. Bab 172 ([EMSANet](./172%20-%202022%20-%20EMSANet%20-%20Segmentasi%20RGB-D.md)) dan bab 174 ([Omnivore](./174%20-%202022%20-%20Omnivore%20-%20Segmentasi%20RGB-D.md)) mewakili pendekatan fusi RGB-D multi-tugas dan lintas-modalitas generik pada tema yang sama, menjadi konteks perbandingan pendekatan fusi yang lebih tua. Bab 173 ([GeminiFusion](./173%20-%202024%20-%20GeminiFusion%20-%20Segmentasi%20RGB-D.md)) paling relevan sebagai pembanding langsung karena sama-sama mengusulkan fusi pada level piksel; DiffPixelFormer disebut penulisnya sendiri diuji terhadap GeminiFusion sebagai salah satu baseline. Perbedaan utamanya terletak pada pemisahan eksplisit komponen diferensial dan bersama pada DSIM, yang tidak menjadi fokus mekanisme fusi pada bab-bab pendahulunya. Bab ini berpotensi memengaruhi bab-bab segmentasi RGB-D berikutnya yang membahas efisiensi komputasi fusi multimodal, mengingat klaim reduksi parameter dan FLOPs dibandingkan *cross-attention* konvensional.

## Poin untuk Sitasi

Kutip dengan kunci `gong2025diffpixelformer`. Ringkasan yang aman dikutip: "DiffPixelFormer mengusulkan blok IIMIB dengan modul DSIM yang memisahkan komponen diferensial dan bersama pada level piksel untuk fusi RGB-D, mencapai 59,95% mIoU pada NYUDv2 dan 54,28% mIoU pada SUN RGB-D dengan varian terbesarnya, unggul 2,75 dan 1,78 poin persentase atas DFormer-L." Angka ini konsisten pada dua sumber pengambilan independen (halaman abstrak arXiv dan halaman HTML naskah), tetapi karena makalah adalah preprint November 2025 yang belum melalui tinjauan sejawat, disarankan verifikasi ulang terhadap PDF asli sebelum sitasi formal. Butir yang **tidak berhasil diverifikasi** dan wajib dicek ulang ke naskah: rincian jumlah parameter dan FLOPs per varian model (S/M/L), selisih mIoU persis terhadap SegFormer dan CMX secara individual, angka detail tabel ablasi IIMIB dan DSIM secara terpisah, serta ketersediaan dan tautan repositori kode yang disebut ada di GitHub namun alamatnya tidak dapat dipastikan oleh penulis bab ini.
